# 0x03. Log Parsing

## Description

This project involves writing a Python script that processes log entries from standard input in real time. The script must parse each line, extract key data points, and print metrics periodically or upon keyboard interruption.

## Requirements

- Language: Python 3.4.3
- OS: Ubuntu 20.04 LTS
- Style: PEP 8 (version 1.7.x)
- All files must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable
- Allowed editors: `vi`, `vim`, `emacs`

## Concepts Covered

- Reading from `sys.stdin`
- Signal handling with `signal` and `KeyboardInterrupt`
- String parsing and regular expressions
- Using dictionaries for data aggregation
- Handling exceptions gracefully

## File

- `0-stats.py` - Script that reads logs from stdin and prints metrics.

## Input Format

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that don't match this format should be ignored.

## Output Format

After every 10 lines or on keyboard interrupt (CTRL + C), print:

```
File size: <total size>
<status code>: <count>
```

- Track only these status codes: 200, 301, 400, 401, 403, 404, 405, 500
- Print status codes in ascending order
- Omit any code that hasn’t appeared

## Example

```
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

## How to Test

You can use a generator script to pipe log entries into your parser:

```bash
./0-generator.py | ./0-stats.py
```

## Directory Structure

```
alx-interview/
└── 0x03-log_parsing/
    ├── 0-stats.py
    ├── README.md
```

## Author

OMAR MOHUMD.
