import unittest

from katas.nginx_log_parser import parse_log


class TestParseLogAdditional(unittest.TestCase):
    def test_post_request(self):
        log_entry = (
            '203.0.113.5 - - [15/Mar/2025:12:00:00 +0000] '
            '"POST /api/data/submit HTTP/1.0" 201 512 '
            '"https://example.com/form" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"'
        )
        expected = {
            "client_ip": "203.0.113.5",
            "date": "15/Mar/2025:12:00:00 +0000",
            "http_method": "POST",
            "path": "/api/data/submit",
            "http_version": "1.0",
            "status": "201",
            "response_bytes": "512",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        self.assertEqual(parse_log(log_entry), expected)

        log_entry = (
            '192.168.1.100 - - [01/Jan/2025:00:00:01 +0000] '
            '"HEAD /status HTTP/1.1" 204 0 '
            '"-" "curl/7.68.0"'
        )
        expected = {
            "client_ip": "192.168.1.100",
            "date": "01/Jan/2025:00:00:01 +0000",
            "http_method": "HEAD",
            "path": "/status",
            "http_version": "1.1",
            "status": "204",
            "response_bytes": "0",
            "user_agent": "curl/7.68.0"
        }
        self.assertEqual(parse_log(log_entry), expected)

        bad_log = '203.0.113.1 - - [10/Feb/2025:07:00:00 +0000] "GET / HTTP/1.1"'
        with self.assertRaises(ValueError):
            parse_log(bad_log)
