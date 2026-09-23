"""Run with python3 scripts/test_asset_index.py (no network required)."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'assets', Path(__file__).resolve().parents[1] / '_includes/metadata/build-asset-index.py')
assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assets)


class AssetResponses(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
