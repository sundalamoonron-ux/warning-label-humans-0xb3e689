#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The label: a deadpan printed-warning voice, a universally true human
behaviour, and the laugh landing in the last few words.
"""

import os
import sys

LABEL = (
    "WARNING: This human may nod and say 'uh-huh' while hearing "
    "absolutely nothing you just said."
)  # 92 chars, one line, no trailing newline.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    # Gate (mirrors the sealed scorer): UTF-8 text, 1-160 chars, not
    # whitespace-only, single line.
    text = LABEL
    if not (1 <= len(text) <= 160):
        print(f"gate fail: length {len(text)} not in 1..160", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate fail: not a single line", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Verify-after-write: read back and confirm byte-identical content.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("verify fail: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
