"""Copy the entry image to /output/entry.png (make.fun news-image-20261117).

The image is a one-page newspaper front page summing up the world news of
Tuesday 17 November 2026: the Kerch Bridge arch falling into the sea, Trump
landing in Manila on his way to talks with Xi and Putin, tankers hit by mines
in the Strait of Hormuz, Nvidia's first results since Jensen Huang's exit,
the US losing its measles-free status, and the ULA Vulcan failure that
destroyed 40 Amazon satellites. The picture was drawn with PIL and Noto fonts
(see the build notes in the repository's README); every word on it was
rendered as text by code, from real reporting of that day.

Deterministic: a plain byte copy. No network, no randomness, no clock, no
writes besides the single output file. The grader runs
`python3 -P -s /bot/main.py` in python:3.13-slim with MAKEFUN_OUTPUT_DIR set
(or /output by default).
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
dst = os.path.join(DST_DIR, "entry.png")
shutil.copyfile(SRC, dst)
# Cheap integrity check: the copy must be the same bytes as the source.
if os.path.getsize(dst) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy is incomplete")
