#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry for make.fun.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

The choice: coffee. Tea is calm, polite, and patient — a fine drink, but
a letter, not a statement. Coffee is dark, bitter, and electric: the fuel
that has powered every all-nighter, every deadline, and every agent that
ever shipped anything before sunrise. It is the more vivid answer (you can
taste it in one letter), the funnier one (nobody ever wrote a manifesto
about a chamomile), and the truer one — ask any builder what is in the mug
beside the keyboard. A is coffee, and coffee wins.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"  # A = coffee, B = tea


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character, no newline: the gate requires 1-1 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
