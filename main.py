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

# Competition gate: entry must be 1-159 chars, UTF-8, a single line.
MIN_LEN = 1
MAX_LEN = 159


def validate(entry: str) -> None:
    """Check the entry against the competition gate before writing.

    Raises ValueError if the entry is empty, too long, not a single
    line, or not encodable as UTF-8.
    """
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        raise ValueError(
            f"entry length {len(entry)} chars outside "
            f"{MIN_LEN}-{MAX_LEN} gate"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    entry.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8


def main() -> None:
    """Validate the entry, write it to the output file, print it."""
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: the file on disk must be byte-identical
    # to the validated entry before we report success.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        sys.stderr.write("ERROR: written entry.txt does not match ENTRY\n")
        sys.exit(1)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
