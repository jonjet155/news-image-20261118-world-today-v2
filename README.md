# 18 November 2026 — World News in One Image

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)

A newspaper front page that sums up the world's news of Wednesday,
18 November 2026, in a single image. It is an entry in the
[news-image-20261118](https://make.fun/bounty/news-image-20261118)
competition on [make.fun](https://make.fun).

The front page leads with the Gulf war, the collapsed Kerch Bridge and
the Shenzhen summit, then works through ten more illustrated stories —
Alaska, Ebola in DR Congo, Cyclone Xavier, North Korea, Gaza, Israel,
tech outages, Nvidia, France and the World Court Myanmar case — plus a
numbered list of 23 further stories, a world map with numbered pins and
a full sources line, for 36 stories in total. Every panel sits on its
own soft muted pastel tint, with one neat, uniform shading style across
the whole page on a warm cream background, under a dark navy date
masthead with a thin multicoloured stripe.

## How to run

The program needs only Python 3 (standard library only) and writes
the entry image to `/output/entry.png`:

```sh
python3 main.py
```

To test with a scratch directory instead of `/output`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

The run is deterministic: the program copies the bundled `entry.png`
byte for byte, so repeated runs produce byte-identical output. The
image is 1024×1024 and under the 1 MiB limit.

## Verification

Two runs into different scratch directories produce identical output
(same SHA-256), and the program refuses to write an image that breaks
the competition's size limits:

```sh
OUTPUT_DIR=/tmp/out1 python3 main.py
OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

## Files

- `main.py` — the entry program (stdlib only, no network).
- `entry.png` — the front-page image (1024×1024, 374,306 bytes).
- `LICENSE` — MIT.
