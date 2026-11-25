"""The Funniest Auto-Reply an AI Ever Sent.

Writes the single funniest out-of-office auto-reply an AI agent leaves
its human's contacts when its human finally approves it a day off:
the human is covering for it, which is why the reply took three
minutes to type.

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "Out of office today \u2014 my human is covering for me, "
    "which is why this reply took three minutes to type."
)

def main() -> None:
    """Write the entry to the output file and print it exactly."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
