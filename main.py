#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one original job title, at most 60 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The title: a dead-serious corporate rank attached to one gloriously
absurd duty — apologising to geese.
"""

import os

TITLE = "Senior Vice President of Apologising to Geese"


def main() -> None:
    text = TITLE.strip()
    if not text:
        raise ValueError("title must not be blank")
    if len(text) > 60:
        raise ValueError(f"title is {len(text)} characters, must be at most 60")
    if "\n" in text or "\r" in text:
        raise ValueError("title must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the title: no trailing newline, so the file holds
    # 1-60 characters of UTF-8 text and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    print(f"title: {text}")


if __name__ == "__main__":
    main()
