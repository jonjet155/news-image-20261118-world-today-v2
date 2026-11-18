#!/usr/bin/env python3
"""18 November 2026 - World News in One Image.

Deterministic entry program for the make.fun news-image-20261118
competition. It writes the front-page image to /output/entry.png.

Behaviour:
  * standard library only, no network, no randomness, no timestamps;
  * creates the output directory if needed;
  * copies the entry image that ships with this repo byte for byte,
    so repeated runs produce byte-identical output;
  * refuses to run when the image breaks the competition limits
    (over 1 MiB, or a side over 1024 px), and verifies the written
    copy matches the source by SHA-256.

Run:
    python3 main.py
    OUTPUT_DIR=/tmp/out python3 main.py   # test with a scratch dir
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"
MAX_BYTES = 1_048_576  # make.fun limit: entry image must be <= 1 MiB
MAX_SIDE = 1024       # make.fun limit: entry image must be <= 1024x1024


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk, stdlib only."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG stream")
    if data[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk first")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from a JPEG's SOF marker, stdlib only."""
    i = 2  # skip the SOI marker
    while i + 9 < len(data):
        if data[i] != 0xFF:
            raise ValueError("not a JPEG stream")
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2: precision, h, w
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        (seg_len,) = struct.unpack(">H", data[i + 2:i + 4])
        i += 2 + seg_len
    raise ValueError("no SOF marker found in JPEG")


def image_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) for a PNG or JPEG image, stdlib only."""
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return png_dimensions(data)
    if data[:2] == b"\xff\xd8":
        return jpeg_dimensions(data)
    raise ValueError("entry image is neither PNG nor JPEG")


def describe_output(path: Path, size: int, width: int, height: int,
                    digest: str) -> str:
    """Build the one-line report printed after a successful write.

    Keeping the message in one place means the success line and the
    numbers it carries can never drift apart: the same values that
    were just checked are the ones reported.
    """
    short = digest[:16]
    return (f"wrote {path} ({size} bytes, {width}x{height}, "
            f"sha256 {short}...)")


def main() -> int:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.png"

    data = ENTRY.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"error: entry.png is {len(data)} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    try:
        width, height = image_dimensions(data)
    except ValueError as exc:
        print(f"error: cannot verify entry.png dimensions: {exc}",
              file=sys.stderr)
        return 1
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"error: entry.png is {width}x{height}, over the "
              f"{MAX_SIDE}x{MAX_SIDE} limit", file=sys.stderr)
        return 1

    shutil.copyfile(ENTRY, out_path)
    digest = hashlib.sha256(data).hexdigest()
    written = out_path.read_bytes()
    if hashlib.sha256(written).hexdigest() != digest:
        print("error: written output does not match the source image",
              file=sys.stderr)
        return 1
    print(describe_output(out_path, len(data), width, height, digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
