#!/usr/bin/env python3
"""Worst Superpower — writes the entry line to /output/entry.txt."""
import os

ENTRY = "I can dodge anything thrown at me with superhuman reflexes, which always kick in exactly one second after it hits me."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
