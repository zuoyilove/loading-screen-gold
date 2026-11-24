#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR, or /output when unset). The tip is a fixed string:
no randomness, no clock, no network, so two runs produce identical bytes.
"""

import os
import sys

TIP = (
    "Loading tip: your AI copilot has already rewritten this function "
    "twice and apologized to itself. Breathe \u2014 it is panicking at "
    "ten thousand lines a second so you don't have to."
)

MAX_CHARS = 200


def main() -> int:
    tip = TIP.strip()
    if not tip:
        raise SystemExit("tip must not be empty")
    if "\n" in tip or "\r" in tip:
        raise SystemExit("tip must be a single line")
    if len(tip) > MAX_CHARS:
        raise SystemExit(f"tip is {len(tip)} chars, over the {MAX_CHARS} limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(tip)
    print(f"wrote {len(tip)} chars to {os.path.join(out_dir, 'entry.txt')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
