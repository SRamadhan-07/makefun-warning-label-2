#!/usr/bin/env python3
"""Warning Label for Humans - a make.fun entry.

The program writes a single-line safety warning label, meant for
every human being, to entry.txt in the output directory.
"""

import os

# The label itself: real printed-label wording and rhythm, one
# single idea, with the turn saved for the last few words.
LABEL = "WARNING: May spontaneously say 'you too' when the waiter says 'enjoy your meal.'"


def entry_path() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> None:
    with open(entry_path(), "w", encoding="utf-8", newline="") as out:
        out.write(LABEL)


if __name__ == "__main__":
    main()
