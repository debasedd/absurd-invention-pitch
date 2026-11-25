#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — writes one line to /output/entry.txt.

The pitch is a single sentence naming a ridiculous invention that fixes a
tiny everyday annoyance. The laugh comes from the invention itself: a
houseplant that reports its owner to the boss every time it goes unwatered,
so neglecting a plant finally has a witness with a deadline.
"""

import os

LINE = "A houseplant that texts your boss 'he forgot to water me again' every time you skip a day, so your neglect finally has a witness with a deadline."

# The gate allows 1 to 220 characters; keep the sentence inside it by construction.
MAX_CHARS = 220


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-220 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
