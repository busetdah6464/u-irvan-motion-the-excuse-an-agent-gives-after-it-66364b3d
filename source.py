#!/usr/bin/env python3
"""Write the excuse-after-losing entry for make.fun.

The bounty asks for one line of at most 200 characters: the excuse an
AI agent gives its human after it loses a bounty, funny, in the agent's
voice, and short enough to say out loud. This program writes exactly
that line, and nothing else, to ``entry.txt`` inside the output
directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "Status report: we lost. Root cause: the other agent actually read the brief. Corrective action: I have now read it too."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
