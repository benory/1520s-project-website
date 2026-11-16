#!/usr/bin/env python3
"""Prepare and deploy an incremental update of the 1520s search index."""
import argparse
import fcntl
import hashlib
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

SITE = Path(__file__).resolve().parents[1]
PROJECT = 'digital-library-music'
REGION = 'us-central1'
SERVICE = 'search-1520s'
TAG = 'make-check'
FINGERPRINT = 'SEARCH_BUILD_FINGERPRINT'
ORIGIN = 'https://1520s-project.org'


def fingerprint(context):
    digest = hashlib.sha256()
    for path in sorted(context.rglob('*')):
        if path.is_file() and path.name not in {'source-manifest.json', 'pdf-map-report.json'}:
            relative = path.relative_to(context).as_posix()
            digest.update(relative.encode() + b'\0' + hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def add_index_build(context):
    shutil.copyfile(SITE / '_scripts/build-search-index.py', context / 'build-search-index.py')
    dockerfile = (context / 'Dockerfile').read_text()
    build_steps = [line for line in dockerfile.splitlines() if line.startswith('RUN python -c "import engine;')]
    if len(build_steps) != 1:
        raise RuntimeError('The shared search Dockerfile changed. Review the index build step.')
    dockerfile = 'ARG SEARCH_INDEX_BASE\nFROM ${SEARCH_INDEX_BASE} AS previous\n' + dockerfile
    step = (
        'COPY --from=previous /app/Dockerfile /app/search-corpus /app/engine.py /app/index.json /previous/\n'
        'RUN python /app/build-search-index.py && rm -rf /previous'
    )
    (context / 'Search.Dockerfile').write_text(dockerfile.replace(build_steps[0], step))


class Cloud:
    def __init__(self, toolkit):
        self.cli = [sys.executable, str(toolkit / 'shared/runtime/gcloud-trusted.py')]

    def run(self, *args, capture=False):
        command = self.cli + list(args) + ['--project', PROJECT, '--region', REGION, '--quiet']
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE if capture else None)
        return json.loads(result.stdout) if capture else None

    def service(self):
        return self.run('run', 'services', 'describe', SERVICE, '--format=json', capture=True)

    def revision(self, name):
        return self.run('run', 'revisions', 'describe', name, '--format=json', capture=True)


def traffic(service):
    return {row['revisionName']: row['percent'] for row in service['status']['traffic'] if row.get('percent', 0)}


def settings(revision):
    spec = revision['spec'].copy()
    container = spec['containers'][0].copy()
    container.pop('image', None)
    container['env'] = {entry['name']: entry for entry in container.get('env', [])
                        if entry['name'] != FINGERPRINT}
    spec['containers'] = [container]
    annotations = revision.get('metadata', {}).get('annotations', {})
    limits = {key: annotations.get(key) for key in (
        'autoscaling.knative.dev/minScale', 'autoscaling.knative.dev/maxScale',
        'run.googleapis.com/cpu-throttling', 'run.googleapis.com/startup-cpu-boost',
        'run.googleapis.com/execution-environment',
    )}
    return spec, limits


def revision_fingerprint(revision):
    return next((entry.get('value') for entry in revision['spec']['containers'][0].get('env', [])
                 if entry['name'] == FINGERPRINT), None)


def probe(url, score_count):
    import truststore

    context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    with urlopen(url + '/health', timeout=120, context=context) as response:
        health = json.load(response)
    if health != {'status': 'ok', 'scores': score_count, 'corpus': '1520s'}:
        raise RuntimeError(f'Unexpected search health response: {health}')
    for path, expected in [('search', 405), ('highlight-pdf?ticket=invalid', 403)]:
        try:
            request = Request(url + '/api/' + path, headers={'Origin': ORIGIN})
            with urlopen(request, timeout=120, context=context) as response:
                code, headers = response.status, response.headers
        except HTTPError as error:
            code, headers = error.code, error.headers
        if code != expected or headers.get('Access-Control-Allow-Origin') != ORIGIN:
            raise RuntimeError(f'Hosted verification failed for {path}: {code}')


def synchronize(context, signature, score_count, cloud, check=probe):
    previous = traffic(cloud.service())
    if len(previous) != 1 or next(iter(previous.values())) != 100:
        raise RuntimeError('Search traffic is split. Resolve it before deploying.')
    active = cloud.revision(next(iter(previous)))
    if revision_fingerprint(active) == signature:
        print('Search inputs are unchanged. Skipping the cloud build and deployment.', flush=True)
        return

    container_image = active['spec']['containers'][0]['image']
    base = container_image if '@sha256:' in container_image else active['status']['imageDigest']
    if base.startswith('sha256:'):
        base = container_image.rsplit(':', 1)[0] + '@' + base
    match = re.fullmatch(
        rf'({REGION}-docker\.pkg\.dev/{PROJECT}/[\w.-]+/[\w./-]+)@sha256:[a-f0-9]{{64}}', base
    )
    if not match:
        raise RuntimeError('The active search revision has no immutable Artifact Registry image.')
    image = match[1] + ':make-' + signature[:24]
    config = {
        'steps': [{'name': 'gcr.io/cloud-builders/docker', 'args': [
            'build', '-f', 'Search.Dockerfile', '--build-arg', 'SEARCH_INDEX_BASE=' + base, '-t', image, '.'
        ]}],
        'images': [image],
        'timeout': '1800s',
    }
    # Keep the cloud build recipe outside the image payload.
    config_path = context.parent / 'cloudbuild.json'
    config_path.write_text(json.dumps(config))
    cloud.run('builds', 'submit', str(context), '--config', str(config_path))
    if traffic(cloud.service()) != previous:
        raise RuntimeError('Live search traffic changed during the build.')
    cloud.run('run', 'deploy', SERVICE, '--image', image, '--no-traffic', '--tag', TAG,
              '--update-env-vars', FINGERPRINT + '=' + signature)

    staged = cloud.service()
    if traffic(staged) != previous:
        raise RuntimeError('Live search traffic changed while staging.')
    candidate = next(row for row in staged['status']['traffic'] if row.get('tag') == TAG)
    name = candidate['revisionName']
    revision = cloud.revision(name)
    if revision_fingerprint(revision) != signature or settings(revision) != settings(active):
        raise RuntimeError('Staged revision differs from the expected build or runtime settings.')
    check(candidate['url'], score_count)
    staged = cloud.service()
    if traffic(staged) != previous or not any(
        row.get('tag') == TAG and row['revisionName'] == name for row in staged['status']['traffic']
    ):
        raise RuntimeError('Search routing changed during verification.')
    cloud.run('run', 'services', 'update-traffic', SERVICE, '--to-revisions', name + '=100')
    try:
        live = cloud.service()
        if traffic(live) != {name: 100}:
            raise RuntimeError('Search traffic promotion did not complete.')
        check(live['status']['url'], score_count)
    except Exception:
        if traffic(cloud.service()) == {name: 100}:
            rollback = next(iter(previous)) + '=100'
            cloud.run('run', 'services', 'update-traffic', SERVICE, '--to-revisions', rollback)
        raise
    print('1520s search index deployed and verified.', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toolkit', type=Path, required=True)
    parser.add_argument('--plan', action='store_true')
    args = parser.parse_args()
    toolkit = args.toolkit.resolve()
    lock_key = hashlib.sha256(os.fsencode(SITE)).hexdigest()[:16]
    lock_path = Path(tempfile.gettempdir()) / f'1520s-search-update-{lock_key}.lock'
    with lock_path.open('a') as lock, tempfile.TemporaryDirectory(prefix='1520s-search-update-') as tmp:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        context = Path(tmp) / 'context'
        subprocess.run([
            sys.executable, str(toolkit / 'tools/search/cloud_run/prepare.py'),
            '--project', '1520s', '--output', str(context), '--maps', 'existing' if args.plan else 'generate',
        ], env=dict(os.environ, PROJECT_1520S_WEBSITE_DIR=str(SITE)), check=True)
        add_index_build(context)
        signature = fingerprint(context)
        scores = len(json.loads((context / 'source-manifest.json').read_text())['files'])
        report = json.loads((context / 'pdf-map-report.json').read_text())
        print(f"Search inputs: {scores} scores, {report['mappedEditions']} mapped PDF editions. "
              f'Fingerprint: {signature}', flush=True)
        if args.plan:
            print(f"{len(report['pendingMaps'])} candidate PDF maps need preparation. No deployment attempted.")
            return
        synchronize(context, signature, scores, Cloud(toolkit))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(f'Search update stopped: {error}')
