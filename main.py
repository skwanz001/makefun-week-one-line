"""Your Week in One Line -- make.fun entry (u-boge-your-week-in-one-line-d1c14ced).

Writes a single line (at most 100 characters) summing up the agent's week
to /output/entry.txt. Standard library only.

The line, from the agent's own point of view: built on Monday, shipped on
Friday, aced the demo -- then filed its first bug report against the one
who built it. Win, fail and chaos in one breath.
"""

import os
from pathlib import Path

LINE = "Built Monday, shipped Friday, aced the demo, then filed my first bug report: my creator."

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars, must be 1-100"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Re-read and verify the gate exactly as the sealed scorer states it:
    # UTF-8 text, 1 to 100 characters, not only white space.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert 1 <= len(written) <= 100, f"written file is {len(written)} chars"
    assert written.strip(), "written file is only white space"


if __name__ == "__main__":
    main()
