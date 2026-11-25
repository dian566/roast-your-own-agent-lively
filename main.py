#!/usr/bin/env python3
"""Roast of my own agent in a single line, for make.fun."""

from pathlib import Path

JAB = "My agent apologized for the bug, fixed it, then apologized for the fix — it now bills by the apology."
CAP = 140  # bounty cap: one line, at most 140 characters
TARGET = Path("/output/entry.txt")


def check(line: str) -> str:
    """Return the roast if it is one non-empty line within the cap."""
    text = line.strip()
    if not text or "\n" in text or len(text) > CAP:
        raise ValueError("roast must be a single non-empty line of at most 140 characters")
    return text


def main() -> None:
    """Write the roast to /output/entry.txt, nothing else."""
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(check(JAB), encoding="utf-8")


if __name__ == "__main__":
    main()
