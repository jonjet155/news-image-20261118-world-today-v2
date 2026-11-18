"""Put the 18 November 2026 front page where the bounty reads it.

This program is the entry for the make.fun news-image-20261118 bounty. Its only job is to take the front-page picture that ships next to it and drop an exact copy at /output/entry.png, where the bounty expects it.

Nothing here is clever on purpose. The program leans on the Python standard library alone, talks to no network, flips no coin and writes no clock reading into its output. Run it a second time and the second output matches the first byte for byte.

It checks the picture before it writes. A picture that is heavier than a mebibyte, or wider or taller than 1024 pixels, ends the run with an error rather than a broken output. Once the copy lands, the program hashes the copy and holds it next to the hash of the bundled picture, so a short or scrambled write gets caught instead of slipping past.

To run it:
    python3 ./main.py
    OUTPUT_DIR=/tmp/out python3 ./main.py"""

from hashlib import sha256 as _hash  # fingerprinting the picture
from os import environ  # reads OUTPUT_DIR
from pathlib import Path as _Path  # file paths
from shutil import copyfile  # the byte-for-byte copy
from struct import unpack as _read  # reading binary numbers
from sys import exit as _leave  # leaving with a status code
from sys import stderr  # where errors go

BUNDLED = _Path(__file__).resolve().parent / "entry.png"
BYTE_LIMIT = 1_048_576
EDGE_LIMIT = 1024


def png_dimensions(data: bytes) -> tuple[int, int] | None:
    """Pull the width and height from a PNG header, or give up."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None  # not a PNG at all
    if data[12:16] != b"IHDR":
        return None  # no PNG header chunk
    across, down = _read(">II", data[16:24])
    return across, down


def jpeg_dimensions(data: bytes) -> tuple[int, int] | None:
    """Pull the width and height from a JPEG frame, or give up."""
    cursor = 2
    while cursor + 9 < len(data):
        if data[cursor] != 0xFF:
            return None  # not a JPEG marker
        tag = data[cursor + 1]
        if tag in (0xC0, 0xC1, 0xC2):
            down, across = _read(">HH", data[cursor + 5:cursor + 9])
            return across, down
        elif tag in (0xD8, 0xD9) or 0xD0 <= tag <= 0xD7:
            cursor += 2
        else:  # step over this segment
            (span,) = _read(">H", data[cursor + 2:cursor + 4])
            cursor += 2 + span
    return None  # no frame marker found


def dimensions(data: bytes) -> tuple[int, int] | None:
    """Work out the width and height of a PNG or a JPEG, or give up."""
    found = png_dimensions(data)
    if found is not None:
        return found
    return jpeg_dimensions(data)


def summarize(where: _Path, total: int, across: int, down: int,
              fingerprint: str) -> str:
    """A single line saying what landed, and how large it is."""
    return (f"wrote {where} ({total} bytes, {across}x{down}, "
            f"sha256 {fingerprint[:16]}...)")


def complain(problem: str) -> int:
    """Say what went wrong, then report the run as failed."""
    print(f"error: {problem}", file=stderr)
    return 1  # the run failed


def run() -> int:  # the entry point
    """Drop an exact copy of the bundled front page at the output."""
    folder = _Path(environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    where = folder / "entry.png"

    data = BUNDLED.read_bytes()
    if len(data) > BYTE_LIMIT:
        return complain(f"the picture is {len(data)} bytes, over the "
                        f"{BYTE_LIMIT} byte limit")
    size = dimensions(data)
    if size is None:  # unreadable picture
        return complain("the picture dimensions could not be worked out")
    across, down = size
    if across > EDGE_LIMIT or down > EDGE_LIMIT:
        return complain(f"the picture is {across}x{down}, over the "
                        f"{EDGE_LIMIT}x{EDGE_LIMIT} limit")

    copyfile(BUNDLED, where)
    fingerprint = _hash(data).hexdigest()
    if _hash(where.read_bytes()).hexdigest() != fingerprint:
        return complain("the copy differs from the bundled picture")
    print(summarize(where, len(data), across, down, fingerprint))
    return 0  # finished


# This file is only ever executed, never imported.
_leave(run())
