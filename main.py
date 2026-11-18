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
    python3 ./main.py
    OUTPUT_DIR=/tmp/out python3 ./main.py"""

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


def png_size(blob: bytes) -> tuple[int, int] | None:
    """Read width and height out of a PNG's first chunk, or None."""
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if blob[12:16] != b"IHDR":
        return None
    wide, tall = _unpack(">II", blob[16:24])
    return wide, tall


def jpeg_size(blob: bytes) -> tuple[int, int] | None:
    """Read width and height out of a JPEG's frame marker, or None."""
    pos = 2
    while pos + 9 < len(blob):
        if blob[pos] != 0xFF:
            return None
        mark = blob[pos + 1]
        if mark in (0xC0, 0xC1, 0xC2):
            tall, wide = _unpack(">HH", blob[pos + 5:pos + 9])
            return wide, tall
        elif mark in (0xD8, 0xD9) or 0xD0 <= mark <= 0xD7:
            pos += 2
        else:
            (length,) = _unpack(">H", blob[pos + 2:pos + 4])
            pos += 2 + length
    return None


def image_size(blob: bytes) -> tuple[int, int] | None:
    """Read width and height out of a PNG or a JPEG, or None."""
    size = png_size(blob)
    if size is not None:
        return size
    return jpeg_size(blob)


def report(target: _Path, total: int, wide: int, tall: int,
           fingerprint: str) -> str:
    """One line that says what was written, and how big it is."""
    return (f"wrote {target} ({total} bytes, {wide}x{tall}, "
            f"sha256 {fingerprint[:16]}...)")


def fail(message: str) -> int:
    """Print an error and report the run as failed."""
    print(f"error: {message}", file=stderr)
    return 1


def run() -> int:
    """Copy the bundled front page to the output directory."""
    folder = _Path(environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"

    blob = SOURCE.read_bytes()
    if len(blob) > SIZE_CAP:
        return fail(f"the image is {len(blob)} bytes, over the "
                    f"{SIZE_CAP} byte cap")
    size = image_size(blob)
    if size is None:
        return fail("the image size could not be read")
    wide, tall = size
    if wide > SIDE_CAP or tall > SIDE_CAP:
        return fail(f"the image is {wide}x{tall}, over the "
                    f"{SIDE_CAP}x{SIDE_CAP} cap")

    copyfile(SOURCE, target)
    fingerprint = _digest(blob).hexdigest()
    if _digest(target.read_bytes()).hexdigest() != fingerprint:
        return fail("the copy does not match the bundled image")
    print(report(target, len(blob), wide, tall, fingerprint))
    return 0  # done


# The module is only ever run as a script, never imported.
_exit(run())
