#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry writer.

Writes one original funny excuse line, the excuse an AI agent hands its
human after missing a deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default ./output/).

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. This program self-checks that gate
before exiting.
"""

import os
import sys

ENTRY = (
    "Apologies. I hallucinated a calendar in which the deadline was next "
    "Tuesday, and it had never once lied to me before."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: {len(text)} chars, need 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    print(f"wrote {path}: {len(written)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
