"""Run with python3 scripts/test_asset_index.py (no network required)."""
import importlib.util
from datetime import datetime, timedelta, timezone
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'assets', Path(__file__).resolve().parents[1] / '_includes/metadata/build-asset-index.py')
assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assets)


class AssetResponses(unittest.TestCase):
    def test_weekly_refresh_and_failure_limit(self):
        now = datetime(2026, 9, 23, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(assets, 'ROOT', Path(directory)):
            with patch.object(assets, 'build', return_value={'work': {}}) as build:
                assets.refresh(now)
                assets.refresh(now + timedelta(days=7, seconds=-1))
                self.assertEqual(build.call_count, 1)
                assets.refresh(now + timedelta(days=7))
                self.assertEqual(build.call_count, 2)
            with patch.object(assets, 'build', side_effect=OSError('Offline')) as build:
                with self.assertRaises(OSError):
                    assets.refresh(now + timedelta(days=14))
                assets.refresh(now + timedelta(days=15))
                self.assertEqual(build.call_count, 1)
                self.assertEqual(json.loads((Path(directory) / 'assets.json').read_text()), {'work': {}})

    def test_available_and_missing_files(self):
        cases = [
            ('HTTP/1.1 200 OK\nContent-Type: audio/mpeg\n', True),
            ('HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\n', False),
            ('HTTP/1.1 404 Not Found\n', False),
            ('HTTP/1.1 410 Gone\n', False),
            ('HTTP/1.1 302 Found\nContent-Type: text/html\n\nHTTP/2 200 OK\nContent-Type: image/svg+xml\n', True),
        ]
        for headers, expected in cases:
            with self.subTest(headers=headers), patch.object(assets, 'curl', return_value=headers):
                self.assertEqual(assets.exists('https://example.test/asset'), expected)

    def test_uncertain_responses_abort_instead_of_marking_missing(self):
        for headers in ['HTTP/1.1 503 Unavailable\n', 'HTTP/1.1 429 Rate Limited\n',
                        'HTTP/1.1 200 OK\n', '']:
            with self.subTest(headers=headers), patch.object(assets, 'curl', return_value=headers):
                with self.assertRaises(RuntimeError):
                    assets.exists('https://example.test/asset')

    def test_network_failure_propagates(self):
        with patch.object(assets, 'curl', side_effect=OSError('Network unavailable')):
            with self.assertRaises(OSError):
                assets.exists('https://example.test/asset')


class R2Routing(unittest.TestCase):
    def test_r2_first_and_fallback(self):
        base = 'https://assets.test/1520s/'
        source = assets.SERVER + '/Any1001a.mp3'
        urls = assets.candidates(source, base, {})
        self.assertEqual(urls, [base + 'mirror-assets/Any1001a.mp3', source])
        with patch.object(assets, 'exists', return_value=True) as check:
            self.assertEqual(assets.first_available(urls), urls[0])
            check.assert_called_once_with(urls[0])
        with patch.object(assets, 'exists', side_effect=[False, True]):
            self.assertEqual(assets.first_available(urls), source)

    def test_explicit_mapping_and_pdf_holds(self):
        base = 'https://assets.test/1520s/'
        source = assets.SERVER + '/Any1001a.mp3'
        index = {'sources': {source: 'audio/Any1001a.mp3'}}
        self.assertEqual(assets.candidates(source, base, index)[0], base + 'audio/Any1001a.mp3')
        pdf = 'https://old.test/A.pdf'
        self.assertEqual(assets.candidates(pdf, base, {'pdfs': {'A.pdf': None}}), [])
        self.assertEqual(assets.candidates(pdf, base, {'pdfs': {'A.pdf': 'pdfs/A.pdf'}, 'blocked': [pdf]}), [base + 'pdfs/A.pdf'])

    def test_uncertainty_preserved_unless_fallback_succeeds(self):
        with patch.object(assets, 'exists', side_effect=[OSError('offline'), False]):
            with self.assertRaises(OSError):
                assets.first_available(['r2', 'legacy'])
        with patch.object(assets, 'exists', side_effect=[OSError('offline'), True]):
            self.assertEqual(assets.first_available(['r2', 'legacy']), 'legacy')


if __name__ == '__main__':
    unittest.main()
