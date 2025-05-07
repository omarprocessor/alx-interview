#!/usr/bin/python3
"""
Log parsing script
"""

import sys

total_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if len(parts) < 7:
            continue
        status = parts[-2]
        size = parts[-1]
        if status in valid_codes:
            status_codes[status] = status_codes.get(status, 0) + 1
        try:
            total_size += int(size)
        except ValueError:
            continue
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
else:
    print_stats()
