#!/usr/bin/env python3
"""One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16).

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI. Python 3.13, standard library only, fully
deterministic: the word is a fixed string in this source, no network,
no randomness, no time dependence.

Gate (per the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 30 characters, not only white space.

The file is written world-readable (mode 0644): the scorer must be able
to read it. Locally, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

WORD = "Whippersnapper"

# Choice, revised from the first draft in a second pass: the judge weighs
# (1) a word a grandma would text about AI, (2) her warm, slightly baffled
# voice, (3) funny in one word, (4) tied to AI, (5) fresh and readable.
# "Whippersnapper" is the word a grandma uses for a cheeky youngster who
# knows everything and talks back -- warm, scolding-affectionate, funny
# in the word itself, and fresh (nobody's obvious pick). Rivals weighed
# and set aside: "ChatGBT" (her typo for ChatGPT -- wins on AI-tie but
# is a mistake, not a warm voice, and its joke needs brand knowledge),
# "Smartypants" (warm and AI-tied but a common word, less fresh),
# "Contraption" (machine-tied but less funny). Criteria are weighed in
# order, so warmth and humour outrank the AI-tie; the word stays.

if not 1 <= len(WORD) <= 30:
    raise SystemExit(f"word must be 1-30 characters, got {len(WORD)}")
if not WORD.strip():
    raise SystemExit("word must not be only white space")
if any(c.isspace() for c in WORD):
    raise SystemExit("entry must be exactly one word, with no whitespace")

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, WORD.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
