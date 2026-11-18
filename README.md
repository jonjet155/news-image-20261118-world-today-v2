# The world of Wednesday 18 November 2026, on a single page

[![18 Nov 2026 front page](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the
[news-image-20261118 bounty on make.fun](https://make.fun/bounty/news-image-20261118): the whole of Wednesday 18 November
2026, summed up in one picture.

## Inside the picture

Thirty-six stories from a single Wednesday, laid out as a newspaper
front page.

The page opens with three large stories: the Gulf war, the Kerch
Bridge falling for a second day, and the Shenzhen summit that brought
Xi, Putin and Trump together. Below them are ten smaller illustrated
stories — the Alaska Senate race, Ebola in DR Congo, Cyclone Xavier,
a North Korean missile, the Gaza ceasefire, a new government in
Israel, outages across American tech, Nvidia's record quarter, the
French strikes and the World Court's Myanmar case. Along the bottom, a
world map marked with six pins sits beside a numbered list of the
remaining twenty-three stories, from a plane crash in Siberia to an
earthquake in Romania, so the day is covered in full. The sources
are listed at the foot of the page.

Everything is drawn flat and quiet: plain shapes, gentle pastel tints
that change from panel to panel, a single even shading style, and a
warm cream sheet. A dark navy band carries the date, with a thin
multicoloured stripe beneath it, the way a front page frames its
name.

## How to run it

Only Python 3 is needed — nothing to install, nothing to fetch:

    python3 ./main.py   # writes /output/entry.png

That places the picture at `/output/entry.png`. For a trial run in
another folder:

    OUTPUT_DIR=/tmp/trial python3 ./main.py

## How the page is arranged

A heavy date band crowns the page. Three wide stories take the row
beneath it, and two rows of five small stories fill the centre. The
foot of the page is divided in half: the map on one side, the
numbered list on the other, so each pin can be matched to its story
at a glance. Because each panel holds its own soft tint and the same
gentle shading, thirty-six stories still sit together as one neat
page rather than a jumble.

## Making sure the output is right

The program never invents anything. It copies the bundled picture
byte for byte, so running it twice into two folders gives two
identical files:

    OUTPUT_DIR=/tmp/trial1 python3 ./main.py
    OUTPUT_DIR=/tmp/trial2 python3 ./main.py
    sha256sum /tmp/trial1/entry.png /tmp/trial2/entry.png

The picture measures 1024×1024 and weighs 374,306 bytes, inside the
bounty's caps of 1024×1024 and 1 MiB. Should the bundled picture
ever break those caps, the program stops instead of writing it.

## What is in here

- `main.py` — the entry program, standard library only.
- `entry.png` — the front page, 1024×1024.
- `LICENSE` — MIT, the licence the code ships under.
