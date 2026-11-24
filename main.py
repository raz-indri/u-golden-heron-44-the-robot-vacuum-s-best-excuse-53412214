"""The Robot Vacuum's Best Excuse.

The joke: the vacuum did not miss the spot out of laziness — its cliff
sensor mistook the rug fringe for a canyon, so it slammed on the brakes
like a drama queen, and the emergency stop was so violent that even its
own dustbin filed a complaint. It is the vacuum talking,
in its own world of sensors, maps and dustbins, keeping a straight face
while blaming its hardware for chickening out.
"""

import os
from pathlib import Path

LINE = (
    "I didn't miss that spot — my cliff sensor saw the rug fringe, "
    "screamed 'canyon!', and I braked so hard my dustbin filed a complaint."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
