"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes a single weather-forecast line (at most 120 characters) for the
invented city of Puddleton to /output/entry.txt.

The line borrows the flat phrasing of a real night forecast and then
breaks it: the moon is out, the stars are out, and so are your bins,
in 60mph winds.
"""

from pathlib import Path

LINE = (
    "Tonight in Puddleton: the moon will be out, the stars will be out, "
    "and so will your bins, in 60mph winds."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 120, f"entry is {len(text)} characters, over the 120 limit"
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
