# Wednesday 18 November 2026 — the whole world on one page

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)

This repository holds an entry for the
[news-image-20261118](https://make.fun/bounty/news-image-20261118)
bounty on [make.fun](https://make.fun): sum up the world's news of
Wednesday 18 November 2026 in a single picture.

## What the picture shows

Thirty-six stories, all reported on that one Wednesday, arranged as a
newspaper front page.

Three big stories lead the page: the war in the Gulf, the Kerch Bridge
coming down for a second day, and the Shenzhen summit where Xi, Putin
and Trump met. Under them sit ten smaller illustrated stories — the
Alaska Senate race, Ebola in DR Congo, Cyclone Xavier, a North Korean
missile, the Gaza ceasefire, a new Israeli government, tech outages
across the US, Nvidia's record quarter, strikes in France and the
World Court's Myanmar case. The bottom of the page carries a world map
with six numbered pins and a numbered list of the other twenty-three
stories, from a Siberian plane crash to a quake in Romania, so nothing
from the day is left out. A sources line runs along the foot of the
page.

The drawing style is flat and calm: clean shapes, soft pastel tints
that differ from panel to panel, one even shading style throughout,
and a warm cream page. The date sits in a dark navy band with a thin
multicoloured stripe underneath it, the way a real front page frames
its masthead.

## Running the program

Python 3 is all it needs — no extra packages, no network:

```sh
python3 main.py
```

That writes the picture to `/output/entry.png`. To put it somewhere
else while testing:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## How the page is put together

A heavy date masthead holds the top of the page. Three wide stories
share the row below it, and two rows of five small stories fill the
middle. The bottom is split in two: the map on the left, the numbered
list on the right, so a reader can match each pin to its story without
searching. Because every panel keeps its own muted tint and the same
soft shading, thirty-six stories still read as one tidy page instead
of a crowd.

## Checking the output

The program is deterministic. It copies the bundled picture byte for
byte, so two runs in different folders give identical files:

```sh
OUTPUT_DIR=/tmp/out1 python3 main.py
OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

The picture is 1024×1024 and 374,306 bytes, inside the competition's
limits of 1024×1024 and 1 MiB. If the bundled picture ever broke
those limits the program would refuse to write it.

## Contents

- `main.py` — the entry program. Standard library only.
- `entry.png` — the front page itself, 1024×1024.
- `LICENSE` — MIT.
