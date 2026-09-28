#!/usr/bin/env python3
"""Refresh verified work-page assets; never replace the index on an incomplete scan."""
import argparse
import concurrent.futures
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parent
REPO = 'https://raw.githubusercontent.com/benory/1520s-project-scores/main/'
FORMATS = {'mei': 'MEI', 'musicxml': 'MusicXML', 'mid': 'MIDI'}
PLOTS = {'activity-merged-notitle': 'png', 'activity-separate-notitle': 'png',
         'prange-attack': 'svg', 'prange-duration': 'svg'}


def curl(url, head=False):
    command = ['curl', '--silent', '--show-error', '--location', '--retry', '2',
               '--connect-timeout', '15', '--max-time', '60']
    command += ['--head'] if head else ['--fail']
    return subprocess.run(command + [url], check=True, capture_output=True, text=True).stdout


def exists(url):
    headers = curl(url, head=True)
    statuses = re.findall(r'^HTTP/\S+ (\d+)', headers, re.M)
    if not statuses:
        raise RuntimeError(f'No HTTP status: {url}')
    status = int(statuses[-1])
    if status in (404, 410):
        return False
    if not 200 <= status < 300:
        raise RuntimeError(f'HTTP {status}: {url}')
    types = re.findall(r'^content-type:\s*([^\r\n;]+)', headers, re.I | re.M)
    if not types:
        raise RuntimeError(f'No content type: {url}')
    # Reject HTML error pages and empty responses.
    lengths = re.findall(r'^content-length:\s*(\d+)', headers, re.I | re.M)
    return types[-1].lower() not in ('text/html', 'application/xhtml+xml') and (not lengths or lengths[-1] != '0')


def routing():
    index = json.loads((ROOT / 'cloudflare-assets.json').read_text())
    config = (ROOT.parents[1] / '_config.yml').read_text()
    match = re.search(r"^asset_base_url:\s*[\"']?([^\s\"'#]+)", config, re.M)
    if not match or not match[1].startswith('https://'):
        raise RuntimeError('Missing HTTPS asset_base_url')
    return match[1].rstrip('/') + '/', index


def candidates(source, base, index):
    if not source:
        return []
    name = source.rsplit('/', 1)[-1]
    if name.endswith('.pdf') and name in index.get('pdfs', {}) and index['pdfs'][name] is None:
        return []
    key = index.get('sources', {}).get(source)
    if name.endswith('.pdf') and index.get('pdfs', {}).get(name):
        key = index['pdfs'][name]
    if source.startswith(base):
        key = source[len(base):]
    urls = [base + key] if key else []
    if key:
        urls.extend(url for url, value in index.get('sources', {}).items() if value == key)
    urls.append(source)
    return list(dict.fromkeys(url for url in urls if url not in index.get('blocked', [])))


def first_available(urls):
    uncertainty = None
    for url in dict.fromkeys(urls):
        try:
            if exists(url):
                return url
        except (OSError, RuntimeError, subprocess.SubprocessError) as error:
            uncertainty = error
    if uncertainty is not None:
        raise uncertainty
    return None


def build(ids=None):
    works = json.loads((ROOT / 'works.json').read_text())
    base, routing_index = routing()
    asset_base = base + "score-assets"
    index = {}
    checks = []
    for work in works:
        work_id = work['ID']
        if ids and work_id not in ids:
            continue
        if work_id in index:
            raise RuntimeError(f'Duplicate work ID: {work_id}')
        entry = index[work_id] = {'downloads': {}, 'plots': {}}
        source = unquote(urlsplit(work.get('Humdrum URL', '')).path)
        source = re.sub(r'^/benory/1520s-project-scores/(?:tree/|blob/)?main/', '', source)
        repository = {}
        if source.startswith('humdrum/') and source.endswith('.krn'):
            for label, directory, extension in [('PDF', 'pdf', 'pdf'), ('Humdrum', 'humdrum', 'krn'),
                                               ('Sibelius', 'sibelius', 'sib'), ('MusicXML', 'musicxml', 'musicxml')]:
                path = re.sub(r'^humdrum/', directory + '/', source)
                path = re.sub(r'\.krn$', '.' + extension, path)
                repository[label] = REPO + quote(path)
        def add(group, key, sources):
            urls = []
            for url in sources:
                urls.extend(candidates(url, base, routing_index))
            # Prefer R2 assets before repository source files.
            urls = list(dict.fromkeys(urls))
            urls.sort(key=lambda url: not url.startswith(base))
            if urls:
                checks.append((work_id, group, key, urls))
        generated = routing_index.get('generatedPdfs', {}).get(work_id, {})
        pdf_sources = [base + generated['no_edit']] if generated.get('no_edit') else []
        add('downloads', 'PDF', pdf_sources + [repository.get('PDF')])
        if generated.get('edit'):
            add('downloads', 'PDF (editorial accidentals)', [base + generated['edit']])
        add('downloads', 'Humdrum', [f'{asset_base}/{work_id}.krn', repository.get('Humdrum')])
        add('downloads', 'Sibelius', [repository.get('Sibelius')])
        for extension, label in FORMATS.items():
            add('downloads', label, [f'{asset_base}/{work_id}.{extension}', repository.get(label)])
        add('audio', '', [f'{asset_base}/{work_id}.mp3'])
        add('timemap', '', [f'{asset_base}/{work_id}-timemap.json'])
        for name, extension in PLOTS.items():
            add('plots', name, [f'{asset_base}/{work_id}-{name}.{extension}'])
    if ids and set(ids) - index.keys():
        raise RuntimeError('Unknown work IDs: ' + ', '.join(sorted(set(ids) - index.keys())))
    print(f'Checking {len(checks)} assets for {len(index)} works (R2 first)...', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(first_available, item[3]): item for item in checks}
        for number, future in enumerate(concurrent.futures.as_completed(futures), 1):
            work_id, group, key, _ = futures[future]
            url = future.result()
            if url:
                if key:
                    index[work_id][group][key] = url
                else:
                    index[work_id][group] = url
            if number % 500 == 0:
                print(f'Checked {number}/{len(checks)}', flush=True)
    return index


def write_json(destination, value):
    with tempfile.NamedTemporaryFile(mode='w', dir=destination.parent, suffix='.tmp', delete=False) as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write('\n')
    Path(output.name).replace(destination)


def refresh(now=None, force=False, output_dir=None, ids=None):
    now = now or datetime.now(timezone.utc)
    output_dir = Path(output_dir) if output_dir else ROOT
    if ids and output_dir.resolve() == ROOT.resolve():
        raise RuntimeError('Use --output-dir with --ids to preserve the complete website index')
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = output_dir / 'assets-check.json'
    if stamp.exists() and not force:
        last_check = datetime.fromisoformat(json.loads(stamp.read_text())['last_attempt'])
        next_check = last_check + timedelta(days=7)
        if now < next_check:
            print(f'Using existing asset inventory; next scan eligible {next_check.isoformat()}')
            return
    # Count failed attempts too, so repeated make runs cannot hammer the server.
    write_json(stamp, {'last_attempt': now.isoformat()})
    inventory = build(ids=ids) if ids else build()
    write_json(output_dir / 'assets.json', inventory)
    print(f'Updated {output_dir / "assets.json"}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--ids', help='Comma-separated pilot IDs; requires a separate output directory')
    args = parser.parse_args()
    try:
        refresh(force=args.force, output_dir=args.output_dir, ids=set(args.ids.split(',')) if args.ids else None)
    except Exception as error:
        raise SystemExit(f'Asset inventory unchanged: {error}')
