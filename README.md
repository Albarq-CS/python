# Python Practice Utilities
## Overview
Small learning scripts for regular expressions, HTTP fetching, HTML parsing, and CSV output.

## Contents
| Path | Purpose |
| --- | --- |
| `check_valid_email/valid_email.py` | Regex-based email-format exercise |
| `check_valid_email/readme.md` | Original regex learning notes |
| `check_valid_email/output.png` | Existing output image |
| `ex2.py` | Fetches a public gold-price page and exports parsed fields to CSV |

## Installation and Usage
Use Python 3 in a virtual environment:
```sh
python -m pip install requests beautifulsoup4
python check_valid_email/valid_email.py
```
The email regex is a format exercise, not comprehensive address validation or deliverability checking. The example currently prints a literal `{e}` rather than interpolating the address.

Before running `ex2.py`, review its target site's access rules, update the machine-specific CSV output path, and inspect its expected HTML structure. It makes a network request and writes a local file; it was not run in this audit.

## Future Improvements
Add network timeouts/error handling, configurable output paths, parsing fixtures, and regex tests. Preserve learning notes while keeping this repository secondary to application projects.

## Author
[Albarq-CS](https://github.com/Albarq-CS)
