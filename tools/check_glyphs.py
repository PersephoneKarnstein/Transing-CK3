#!/usr/bin/env python3
"""Flags characters in localization that CK3's interface font cannot draw.

The game shows Latin-1 and Latin Extended-A (ā ī ū ś ē) but draws a box for Latin Extended Additional, the dot-below
and line-below letters of Indic and Semitic transliteration (ṭ ṇ ṣ ḍ ḥ ḻ ḷ ṅ). Seen in game: ḻ in the faith tooltip,
ṭ in the holy-site list and Faith Details. Vanilla uses a few such letters too, in text it seldom shows.
Comment lines are skipped. Run from the repo root: python3 tools/check_glyphs.py
"""
import glob
import sys

ALLOWED_EXTRA = set('–—‘’“”…•€')


def drawable(ch):
    o = ord(ch)
    return o < 0x250 or ch in ALLOWED_EXTRA


bad = 0
for path in sorted(glob.glob('localization/**/*.yml', recursive=True)):
    for n, line in enumerate(open(path, encoding='utf-8-sig'), 1):
        if line.lstrip().startswith('#'):
            continue
        chars = sorted({c for c in line if not drawable(c)})
        if chars:
            bad += 1
            print(f'{path}:{n}: {" ".join(chars)}  {line.strip()[:90]}')
sys.exit(1 if bad else 0)
