from typing import Dict
import re


def parse_log(log: str) -> Dict[str, str]:
    """
    Parses a single Nginx access log entry into a structured dictionary.

    The log format is:
    122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] "GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 "-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"

    The parsed log data should be returned as a dictionary:
    {
        "client_ip": "122.176.223.47",
        "date": "05/Feb/2024:08:29:40 +0000",
        "http_method": "GET",
        "path": "/web-enabled/Enhanced-portal/bifurcated-forecast.js",
        "http_version": "1.1",
        "status": "200",
        "response_bytes": "1684",
        "user_agent": "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"
    }

    Hint: Use regex

    Args:
        log: the Nginx log string

    Returns:
        A dictionary containing parsed log data

    Raises:
        ValueError: if the log format is invalid
    """

    pattern = re.compile(
        r'(?P<client_ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'
        r'\[(?P<date>[^\]]+)\]\s+'
        r'"(?P<http_method>\w+)\s+(?P<path>[^\s]+)\s+HTTP/(?P<http_version>[\d.]+)"\s+'
        r'(?P<status>\d{3})\s+'
        r'(?P<response_bytes>\d+)\s+'
        r'"[^"]*"\s+'
        r'"(?P<user_agent>[^"]+)"'
    )

    match = pattern.match(log)
    if not match:
        raise ValueError("Invalid log format")

    return match.groupdict()


if __name__ == "__main__":
    log_entry = (
        '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
        '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
        '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
    )

    parsed_log = parse_log(log_entry)
    print("Parsed log data:", parsed_log)
