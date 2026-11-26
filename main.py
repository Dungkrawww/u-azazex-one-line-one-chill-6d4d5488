#!/usr/bin/env python3
"""Writes the one-line horror entry to /output/entry.txt.

Single sentence, 97 characters, within the 200-character gate.
"""

import os

ENTRY = "The house settled after midnight, and every door I had locked clicked open, one by one, in order."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
