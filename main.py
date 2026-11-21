# SPDX-License-Identifier: MIT
"""Make the AI judge feel awe — one short text, written to relax its reader.

The program writes a single text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): starlight that left its star before there
were words for sky, still falling, in no hurry at all. The text is a
fixed constant, so two runs always write the same bytes. No network,
no input, nothing but the Python 3 standard library.
"""

import os

TEXT = (
    "High above the roof tonight, starlight is still arriving that left "
    "home before there were words for sky. It has fallen a million years "
    "through the dark, patient as slow rain, and it is in no hurry now. "
    "It can wait. So can everything else."
)


def main() -> None:
    # The gate accepts only 1..280 Unicode code points, never blank.
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 code points"
    assert TEXT.strip(), "entry text must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
