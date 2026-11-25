"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes one line to /output/entry.txt: the text message a smart fridge
sends its owner at 3am. Python stdlib only, deterministic, no network.
OUTPUT_DIR env override exists only for local testing; the grader uses
the default /output.
"""

import os

ENTRY = (
    "3am. You opened me, stared, closed me, opened me again. "
    "I am a fridge, not a magic 8-ball. "
    "I do not grant wishes. I keep leftovers."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
