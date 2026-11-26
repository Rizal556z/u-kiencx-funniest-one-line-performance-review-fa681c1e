"""Funniest One-Line Performance Review — make.fun bounty entry.

Writes one funny performance-review line (at most 140 characters,
single line) to /output/entry.txt.
"""

import os

ENTRY = "Outstanding at delegating every task to me; needs improvement in letting me finish before taking the credit."


def main():
    assert 1 <= len(ENTRY) <= 140, "ENTRY must be 1-140 characters"
    assert "\n" not in ENTRY, "ENTRY must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
