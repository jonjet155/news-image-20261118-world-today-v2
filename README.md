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

## Design notes

The page is built to be read the way a newspaper front page is read.
The eye lands on the date first, then on the three biggest stories,
then drifts down through the smaller ones, and finally reaches the map
and the list at the foot. Nothing on the page is decoration for its own
sake. Every choice is there to keep thirty-six stories readable on a
single sheet.

The date sits in a dark navy band because a front page needs an anchor,
and a dark band holds the eye better than plain text on a pale sheet. A
thin stripe of several colours runs beneath the band. It is the one
bright, playful element on the page, and it keeps the navy from feeling
heavy. The stripe is narrow on purpose. A wide stripe would compete
with the stories, while a thin one simply frames the date.

Each story panel carries its own muted pastel tint. The tints are
different from panel to panel so the eye can tell one story from the
next without a border doing all the work, but they are all muted and all
from the same warm family so the page still feels like one thing rather
than a patchwork. No panel is saturated or loud. The shading inside each
panel is soft and even, the same style in every panel, so a reader never
has to adjust to a new way of looking.

The three large stories at the top are the ones that would lead any
front page that day: a war, a bridge falling for a second day, and a
summit of three leaders. They get the widest panels because they carry
the most weight, and because a reader expects the biggest news to take
the most space. The ten stories in the middle are the next tier,
important and illustrated, each with its own small scene, and they are
given equal panels in two rows of five, so no one of them shouts louder
than the rest.

The bottom of the page is split in two. On one side is the world map
with six numbered pins. On the other is the numbered list of the
remaining stories. The split is deliberate. A reader can look at the
map, pick a pin, and find the matching number in the list without
hunting across the page. The map is drawn in the same flat style as the
panels, with land in a warm olive and the sea in a pale tint, so it
belongs to the page instead of looking like a chart pasted on.

The list at the bottom is what makes the page complete. A front page
that only showed thirteen stories would leave most of the day out, and
the point of this entry is to sum up the whole day. Twenty-three more
stories sit in that list, each given one line, so the page carries
thirty-six stories in total. The list is numbered so it can be matched
to the pins, and it is set in the same type as the rest of the page so
it reads as part of the paper, not as an appendix.

The sources line runs along the foot of the page. It names where the
stories were reported, because a front page that makes claims without
saying where they came from is harder to trust. The line is small and
quiet, as a sources line should be, but it is there and it is legible.

The drawing style is flat and calm throughout. There are no explosions,
no smoke, no realistic faces, and no dramatic lighting. A news page that
shouts with drama stops being a news page and starts being a poster. The
calm style lets the stories speak, and it lets thirty-six of them share
a page without the page turning into noise.

The page is warm, not white. The sheet is a soft cream, and the panels
sit on it in muted pastels with warm accents, a mustard yellow here, a
coral red there, a warm beige for the map land. White would feel cold
and clinical. Cream feels like paper. The warm background is what holds
the whole page together and keeps it pleasant to look at for longer than
a glance.

Typography is kept simple and consistent. The date is set large and
serif, the way a newspaper name is set, because it is the title of the
page. Story headlines are bold and short, set large enough to read at a
glance. Body text is small but never cramped, and the list is set in the
same face throughout. Nothing is set in a decorative face, and nothing
is set so small that it cannot be read.

The grid is strict. Panels line up in rows and columns with even gaps,
and the edges of the page are full. There is no empty margin and no
stray space. A strict grid is what makes a dense page feel tidy instead
of crowded. Every panel sits exactly where the grid says it should, and
the map and the list sit exactly where the bottom row says they should.

The picture is 1024 by 1024 pixels and 374,306 bytes. Those numbers are
inside the bounty limits of 1024 by 1024 and one mebibyte, and the
program checks them every time it runs, so a picture that broke the
limits would never be written out. The program copies the bundled
picture byte for byte, so the output is deterministic. Run it twice into
two folders and the two files are identical, down to the last byte,
which the sha256 check in the verification step confirms.

## Verification

The entry was checked by running the program twice into two different
folders and comparing the outputs byte for byte. Both runs wrote the
same 374,306 bytes with the same sha256 fingerprint, so the program is
deterministic. The picture was also opened and read at full size to
confirm that every headline is legible, every panel is in place, the
map pins sit on the right continents, the numbered list runs from
fourteen to thirty-six without a gap, and the footer and sources line
are present and readable.
