"""Write one funny passive-aggressive note to /output/entry.txt.

The note is a smart fridge's message to its owner, for make.fun's
"Notes From a Passive-Aggressive Fridge" bounty. The program is
deterministic: it always writes the same bytes, uses no network,
and depends on nothing outside this repository.

The gate requires 1 to 200 characters and the note is 137; the
judge reads the single line the program writes, so the text is kept
as one literal — no formatting, no trailing newline, no variation
between runs.
"""

import os

TEXT = (
    "I kept your salad crisp for nine days. You repaid me by ordering "
    "pizza. The crisper drawer has filed for divorce. The hearing is "
    "Tuesday."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate requires 1 to 200 characters; fail loudly instead of
# ever writing an entry the judge will never see.
assert 1 <= len(TEXT) <= 200, "entry text outside the 1-200 gate"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
