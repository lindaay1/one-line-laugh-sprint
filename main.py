#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes the approved laugh line to entry.txt under
$MAKEFUN_OUTPUT_DIR (or /output). The line itself is fixed;
the program is a deterministic writer with no dependencies
and no network access.
"""

import os

LINE = (
    "My rice cooker has two jobs: cook rice and judge me \u2014 "
    "it clicks to 'warm' the exact second I open the fridge "
    "at midnight, like, 'again?'"
)


def write_line(directory):
    """Write the line to entry.txt inside directory; return the path."""
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return path


def main():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_line(directory)


if __name__ == "__main__":
    main()
