#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single original line of text (1-240 characters) to
/output/entry.txt: a quiet, earned moment of pride for someone in a
scene. Deterministic: the same line is written on every run.
"""

import os

LINE = (
    "Eleven Sundays he'd spent rebuilding the engine in the driveway, "
    "and when it finally coughed awake, his daughter looked at him "
    "like he could fix anything."
)


def main() -> None:
    # The gate: entry.txt must be UTF-8 text of 1-240 characters,
    # not only white space. Refuse to write anything invalid.
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-240")
    if not LINE.strip():
        raise ValueError("line must not be only white space")
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Determinism guard: what we wrote is exactly the line, byte for byte.
    with open(output_path, "r", encoding="utf-8") as handle:
        assert handle.read() == LINE


if __name__ == "__main__":
    main()
