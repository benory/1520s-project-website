"""Build the search index, reusing scores indexed by the same engine and tools."""
import hashlib
import importlib.util
import inspect
import json
import shutil
import sys
import tempfile
from pathlib import Path

import engine


def load_reusable_rows(app, previous):
    if (app / 'Dockerfile').read_bytes() != (previous / 'Dockerfile').read_bytes():
        return {}
    if (app / 'search-corpus').read_bytes() != (previous / 'search-corpus').read_bytes():
        return {}
    spec = importlib.util.spec_from_file_location('previous_engine', previous / 'engine.py')
    old_engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old_engine)
    if any(inspect.getsource(getattr(engine, name)) != inspect.getsource(getattr(old_engine, name))
           for name in ('run', 'build')):
        return {}
    rows = json.loads((previous / 'index.json').read_bytes())
    return {row['source']: row for row in rows if 'index' in row and row.get('positions')}


def build_index(app, previous):
    previous_rows = load_reusable_rows(app, previous)
    scores = app / 'scores'
    paths = sorted(scores.glob('[A-Z]??/*.krn'))
    if not paths:
        raise ValueError('Search snapshot contains no Humdrum scores.')
    rows = {}
    changed = []
    for path in paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        old = previous_rows.get(str(path))
        if old and old['sha256'] == digest:
            rows[str(path)] = old
        else:
            changed.append(path)
    if changed:
        with tempfile.TemporaryDirectory() as temporary:
            scratch = Path(temporary)
            for path in changed:
                target = scratch / path.relative_to(scores)
                target.parent.mkdir(exist_ok=True)
                shutil.copy2(path, target)
            engine.build(scratch, scratch / 'index.json')
            for row in json.loads((scratch / 'index.json').read_bytes()):
                if 'error' in row:
                    raise RuntimeError(f"Could not index {row['id']}: {row['error']}")
                source = scores / Path(row['source']).relative_to(scratch)
                rows[str(source)] = {**row, 'source': str(source)}
    ordered = [rows[str(path)] for path in paths]
    if len({row['id'] for row in ordered}) != len(ordered):
        raise ValueError('Search snapshot contains duplicate score IDs.')
    (app / 'index.json').write_text(json.dumps(ordered))
    print(f'Indexed {len(changed)} scores and reused {len(paths) - len(changed)}.', flush=True)


if __name__ == '__main__':
    engine.BIN = Path('/usr/local/bin')
    build_index(Path('/app'), Path('/previous'))
