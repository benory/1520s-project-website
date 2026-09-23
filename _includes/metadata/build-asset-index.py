#!/usr/bin/env python3
"""Refresh verified work-page assets; never replace the index on an incomplete scan."""
import concurrent.futures
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parent
SERVER = 'https://data.1520s-project.org'
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
    # This server returns HTTP 200 with HTML for missing assets.
    return types[-1].lower() not in ('text/html', 'application/xhtml+xml')


def build():
    works = json.loads((ROOT / 'works.json').read_text())
    tree = json.loads(curl('https://api.github.com/repos/benory/1520s-project-scores/git/trees/main?recursive=1'))
    if tree.get('truncated') or not isinstance(tree.get('tree'), list):
        raise RuntimeError('Incomplete scores repository listing')
    paths = {entry['path'] for entry in tree['tree'] if entry['type'] == 'blob'}
    index = {}
    checks = []
    for work in works:
        work_id = work['ID']
        if work_id in index:
            raise RuntimeError(f'Duplicate work ID: {work_id}')
        entry = index[work_id] = {'downloads': {}, 'plots': {}}
        source = unquote(urlsplit(work.get('Humdrum URL', '')).path)
        source = re.sub(r'^/benory/1520s-project-scores/(?:tree/|blob/)?main/', '', source)
        for label, directory, extension in [('PDF', 'pdf', 'pdf'), ('Humdrum', 'humdrum', 'krn'),
                                              ('Sibelius', 'sibelius', 'sib'), ('MusicXML', 'musicxml', 'musicxml')]:
            path = re.sub(r'^humdrum/', directory + '/', source)
            path = re.sub(r'\.krn$', '.' + extension, path)
            if path in paths:
                entry['downloads'][label] = REPO + quote(path)
        for extension, label in FORMATS.items():
            checks.append((work_id, 'downloads', label, f'{SERVER}/{work_id}.{extension}'))
        checks.append((work_id, 'audio', '', f'{SERVER}/{work_id}.mp3'))
        checks.append((work_id, 'timemap', '', f'{SERVER}/{work_id}-timemap.json'))
        for name, extension in PLOTS.items():
            checks.append((work_id, 'plots', name, f'{SERVER}/{work_id}-{name}.{extension}'))
    print(f'Checking {len(checks)} data-server assets for {len(index)} works...', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(exists, item[3]): item for item in checks}
        for number, future in enumerate(concurrent.futures.as_completed(futures), 1):
            work_id, group, key, url = futures[future]
            if future.result():
                if key:
                    index[work_id][group][key] = url
                else:
                    index[work_id][group] = url
            if number % 500 == 0:
                print(f'Checked {number}/{len(checks)}', flush=True)
    return index


if __name__ == '__main__':
    try:
        inventory = build()
        with tempfile.NamedTemporaryFile(mode='w', dir=ROOT, suffix='.tmp', delete=False) as output:
            json.dump(inventory, output, indent=2, sort_keys=True)
            output.write('\n')
        Path(output.name).replace(ROOT / 'assets.json')
        print(f'Updated {ROOT / "assets.json"}', flush=True)
    except Exception as error:
        raise SystemExit(f'Asset inventory unchanged: {error}')
