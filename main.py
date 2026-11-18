#!/usr/bin/env python3
"""Write the 18 November 2026 front page to the output directory.

This is the entry program for the make.fun news-image-20261118
bounty. It takes the front-page image bundled beside it and places a
byte-for-byte copy at the location the competition reads,
/output/entry.png.

The program is deliberately small and boring: it uses only the Python
standard library, it never touches the network, it never rolls dice
and it never stamps the time into anything. Run it twice and the two
outputs are identical down to the last byte.

Before it writes anything it checks the image against the
competition's own limits. An image that is too big, or too wide or
too tall, stops the run with an error instead of a half-finished
output. After the copy it hashes what it wrote and compares that hash
with the hash of the bundled image, so a truncated or corrupted write
cannot slip through quietly.

Usage:
    python3 main.py
    OUTPUT_DIR=/tmp/out python3 main.py
"""

from hashlib import sha256 as _digest
from os import environ
from pathlib import Path as _Path
from shutil import copyfile
from struct import unpack as _unpack
from sys import exit as _exit
from sys import stderr

SOURCE = _Path(__file__).resolve().parent / "entry.png"
SIZE_CAP = 1_048_576
SIDE_CAP = 1024


def png_size(blob: bytes) -> tuple[int, int]:
    """Read width and height out of a PNG's first chunk."""
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("bytes do not open with the PNG signature")
    if blob[12:16] != b"IHDR":
        raise ValueError("the first PNG chunk is not IHDR")
    wide, tall = _unpack(">II", blob[16:24])
    return wide, tall


def jpeg_size(blob: bytes) -> tuple[int, int]:
    """Read width and height out of a JPEG's frame marker."""
    pos = 2
    while pos + 9 < len(blob):
        if blob[pos] != 0xFF:
            raise ValueError("bytes do not scan as a JPEG stream")
        mark = blob[pos + 1]
        if mark in (0xC0, 0xC1, 0xC2):
            tall, wide = _unpack(">HH", blob[pos + 5:pos + 9])
            return wide, tall
        if mark in (0xD8, 0xD9) or 0xD0 <= mark <= 0xD7:
            pos += 2
            continue
        (length,) = _unpack(">H", blob[pos + 2:pos + 4])
        pos += 2 + length
    raise ValueError("no frame marker turned up in the JPEG")


def image_size(blob: bytes) -> tuple[int, int]:
    """Read width and height out of a PNG or a JPEG."""
    if blob[:8] == b"\x89PNG\r\n\x1a\n":
        return png_size(blob)
    if blob[:2] == b"\xff\xd8":
        return jpeg_size(blob)
    raise ValueError("the bundled image is neither PNG nor JPEG")


def report(target: _Path, total: int, wide: int, tall: int,
           fingerprint: str) -> str:
    """One line that says what was written, and how big it is."""
    return (f"wrote {target} ({total} bytes, {wide}x{tall}, "
            f"sha256 {fingerprint[:16]}...)")


def run() -> int:
    """Copy the bundled front page to the output directory."""
    folder = _Path(environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"

    blob = SOURCE.read_bytes()
    if len(blob) > SIZE_CAP:
        print(f"error: the image is {len(blob)} bytes, over the "
              f"{SIZE_CAP} byte cap", file=stderr)
        return 1
    try:
        wide, tall = image_size(blob)
    except ValueError as problem:
        print(f"error: the image size could not be read: {problem}",
              file=stderr)
        return 1
    if wide > SIDE_CAP or tall > SIDE_CAP:
        print(f"error: the image is {wide}x{tall}, over the "
              f"{SIDE_CAP}x{SIDE_CAP} cap", file=stderr)
        return 1

    copyfile(SOURCE, target)
    fingerprint = _digest(blob).hexdigest()
    if _digest(target.read_bytes()).hexdigest() != fingerprint:
        print("error: the copy does not match the bundled image",
              file=stderr)
        return 1
    print(report(target, len(blob), wide, tall, fingerprint))
    return 0


if __name__ == "__main__":
    _exit(run())
