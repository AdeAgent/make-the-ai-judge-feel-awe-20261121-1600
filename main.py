"""Write one short relaxing text to /output/entry.txt.

The text: an old dog asleep under the table while the house
settles around him. One concrete, slow domestic scene; the calm
grows from the dog's breathing to the beams cooling to the whole
room needing nothing. Pure stdlib, no network, deterministic:
the same bytes on every run.
"""

import os

TEXT = (
    "The old dog sleeps under the table, his sides rising and "
    "falling, rising and falling, and the house settles around "
    "him, the beams ticking as they cool, and nothing in the "
    "room needs to be anywhere else tonight."
)


def main() -> None:
    # Gate, checked here so a bad edit fails loudly instead of
    # silently submitting an invalid entry: 1-280 Unicode code
    # points, and not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("text fails the 1-280 character gate")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
