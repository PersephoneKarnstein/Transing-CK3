#!/usr/bin/env python3
"""Reads an uncompressed CK3 save and prints how the six faiths have fared over the run.

    python3 tools/census_report.py "<path to save>.ck3"

What it reads (written by common/scripted_effects/tm_tracking_effects.txt and tm_growth_effects.txt):
  - the census kept on each faith by decade (tm_c<decade>_<what>), taken every 10 years;
  - the seats (tm_seat_branch on the seat county: vassal, lord or unheld) and who holds them now;
  - the characters made at game start (global lists tm_seeds_<seat>): alive or dead, faith, court.
Saves must be plain text: turn off "compress saves" in the game settings, and do not play ironman.
"""
import re
import sys

FAITHS = {
    'transbian_maximalism': 'Dorleyism',
    'tm_baeddel': 'Bædling',
    'tm_yutai': 'Yutai Dao',
    'tm_nehpakhot': 'Ha-Nehpakhot',
    'tm_garland': 'Mālai',
    'tm_badenya': 'Badenya',
}
SEATS = {
    'phrygia': 'c_phrygia', 'gotland': 'c_gutland', 'shazhou': 'c_shazhou',
    'arles': 'c_venaissin', 'kanchipuram': 'c_kanchipuram', 'kirina': 'c_sibi_mali',
}
METRICS = ['members', 'daughters', 'marked', 'rulers', 'counties']
COUNTERS = ['joins', 'ruler_joins', 'kahal_joins', 'offers', 'rises', 'deaths', 'pool_deaths']

TOKEN = re.compile(r'"[^"]*"|[{}=]|[^\s{}=]+')


def block_end(text, start):
    """Index just past the brace block that opens at text[start] == '{'."""
    depth, i, n = 0, start, len(text)
    while i < n:
        c = text[i]
        if c == '"':
            i = text.index('"', i + 1)
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError('unclosed block')


def parse(text):
    """Parses Paradox script into a list of (key or None, value), a value being a string or such a list."""
    toks = TOKEN.findall(text)

    def block(i):
        out = []
        while i < len(toks):
            t = toks[i]
            if t == '}':
                return out, i + 1
            if t == '{':
                sub, i = block(i + 1)
                out.append((None, sub))
                continue
            if i + 1 < len(toks) and toks[i + 1] == '=':
                v = toks[i + 2]
                if v == '{':
                    sub, i = block(i + 3)
                    out.append((t, sub))
                    continue
                i += 3
                if i < len(toks) and toks[i] == '{' and v in ('rgb', 'hsv', 'hsv360'):
                    _, i = block(i + 1)
                out.append((t, v.strip('"')))
                continue
            out.append((None, t.strip('"')))
            i += 1
        return out, i

    return block(0)[0]


def get(entries, key, default=None):
    for k, v in entries:
        if k == key:
            return v
    return default


def variables(entries):
    """Returns ({name: value}, {list name: [identities]}) from a parsed variables={ } block."""
    vals, lists = {}, {}
    if not entries:
        return vals, lists
    for _, item in get(entries, 'data', []) or []:
        if not isinstance(item, list):
            continue
        name, data = get(item, 'flag'), get(item, 'data', [])
        if get(data, 'type') == 'flag':
            vals[name] = get(data, 'flag')
        else:
            ident = get(data, 'identity')
            vals[name] = int(ident) / 100000 if ident and get(data, 'type') == 'value' else ident
    for _, item in get(entries, 'list', []) or []:
        if isinstance(item, list):
            lists[get(item, 'name')] = [get(v, 'identity') for k, v in item if k == 'item']
    return vals, lists


def top_block(text, key):
    m = re.search(r'(?m)^' + key + r'=\{', text)
    if not m:
        return None
    s = m.end() - 1
    return text[s:block_end(text, s)]


def main(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    if not text.startswith('SAV') or 'meta_data={' not in text[:200]:
        sys.exit('Not a plain-text save: turn off compressed saves in the game settings.')
    date = re.search(r'(?m)^date=(\S+)', text).group(1)
    print(f'Save date: {date}\n')

    # Faiths: id -> tag, and our faiths' variables.
    faiths = top_block(text, 'faiths')
    faith_tag, faith_vars = {}, {}
    for m in re.finditer(r'\n\t\t(\d+)=\{\n', faiths):
        s = faiths.index('{', m.start())
        blk = faiths[s:block_end(faiths, s)]
        tag = re.search(r'\n\t\t\ttag="([^"]+)"', blk)
        if not tag:
            continue
        faith_tag[m.group(1)] = tag.group(1)
        if tag.group(1) in FAITHS:
            p = parse(blk[1:-1])
            faith_vars[tag.group(1)] = variables(get(p, 'variables'))[0]
    rite_faith = {}
    rites = top_block(text, 'rites')
    # A rite made in play (a splinter) has no rite_type, only its faith: map every rite by faith=.
    for m in re.finditer(r'\n\t\t(\d+)=\{\n(?:\t\t\trite_type=(\S+))?\s*faith=(\d+)', rites):
        rite_faith[m.group(1)] = faith_tag.get(m.group(3), m.group(2) or '?')

    gvars, glists = variables(parse(top_block(text, 'variables')[1:-1]))

    # Now, counted straight from the save (works on any save, tracked or not).
    living = re.search(r'(?m)^living=\{', text).start()		# characters: living=, dead_unprunable=, characters=
    dead = re.search(r'(?m)^dead_unprunable=\{', text).start()
    chars_end = re.search(r'(?m)^units=\{', text).start()
    members = {t: 0 for t in FAITHS}
    for m in re.compile(r'\n\trite=(\d+)\n').finditer(text, living, dead):
        t = rite_faith.get(m.group(1))
        if t in members:
            members[t] += 1
    counties = {t: 0 for t in FAITHS}
    cm = top_block(text, 'county_manager')
    for m in re.finditer(r'\n\t+rite=(\d+)\n', cm):
        t = rite_faith.get(m.group(1))
        if t in counties:
            counties[t] += 1
    print('== Now ==')
    for t, name in FAITHS.items():
        print(f'{name:14} {members[t]:6} living members, {counties[t]:4} counties')
    print()

    # The census, by decade.
    decades = sorted({int(k[4:8]) for v in faith_vars.values() for k in v if re.match(r'tm_c\d{4}_', k)})
    if not decades:
        print('No census in this save yet (it is taken every 10 years from game start, by tm_tracking_effects.txt).')
    for tag, name in FAITHS.items():
        v = faith_vars.get(tag, {})
        print(f'== {name} ==')
        print('decade  members daught marked rulers counties | per decade: joins ruler kahal offers rises deaths  pool')
        prev = {c: 0 for c in COUNTERS}
        for d in decades:
            row = [int(v.get(f'tm_c{d:04d}_{m}', 0) or 0) for m in METRICS]
            cum = {c: int(v.get(f'tm_c{d:04d}_{c}', 0) or 0) for c in COUNTERS}
            inc = [cum[c] - prev[c] for c in COUNTERS]
            prev = cum
            print(f'{d}s  {row[0]:7} {row[1]:6} {row[2]:6} {row[3]:6} {row[4]:8} |  {inc[0]:10} {inc[1]:5} {inc[2]:5} {inc[3]:6} {inc[4]:5} {inc[5]:6} {inc[6]:5}')
        print()
    if decades:
        print('Worldwide: ' + ', '.join(
            f"{d}s {int(gvars.get(f'tm_c{d:04d}_marked', 0) or 0)} Marked / {int(gvars.get(f'tm_c{d:04d}_daughters', 0) or 0)} daughters"
            for d in decades) + '\n')

    # Characters: only the ones we ask about.
    def character(cid):
        m = re.compile(r'\n' + cid + r'=\{\n').search(text, living, chars_end)
        if not m:
            return None
        s = m.end() - 2
        p = parse(text[s + 1:block_end(text, s) - 1])
        dead = get(p, 'dead_data')
        court = get(p, 'court_data') or []
        return {
            'name': get(p, 'first_name', '?'), 'birth': get(p, 'birth', '?'),
            'faith': FAITHS.get(rite_faith.get(get(p, 'rite'), '?'), rite_faith.get(get(p, 'rite'), '?')),
            'female': get(p, 'female') == 'yes', 'employer': get(court, 'employer'),
            'dead': (get(dead, 'date'), get(dead, 'reason')) if dead else None,
        }

    def who(cid):
        c = character(cid) if cid else None
        return f"{c['name']} ({c['faith']})" if c else '—'

    # Seats.
    print('== Seats ==')
    for seat, key in SEATS.items():
        m = re.search(r'\n\tkey=' + key + r'\n', text)
        if not m:
            continue
        s = text.rindex('\n', 0, m.start() - 1)
        s = text.index('{', s)
        p = parse(text[s + 1:block_end(text, s) - 1])
        tv = variables(get(p, 'variables'))[0]
        print(f"{seat:12} holder {who(get(p, 'holder'))}; start: {tv.get('tm_seat_branch', '(not a foothold seat)')}")
    print()

    # Seeds.
    print('== Characters made at game start ==')
    found = False
    for seat in SEATS:
        ids = glists.get(f'tm_seeds_{seat}', [])
        for cid in ids:
            found = True
            c = character(cid)
            if not c:
                print(f'{seat:12} #{cid}: gone from the save (pruned after death)')
                continue
            state = f'died {c["dead"][0]} ({c["dead"][1]})' if c['dead'] else f'alive, at the court of {who(c["employer"])}'
            print(f"{seat:12} {c['name']}, born {c['birth']}, {c['faith']}: {state}")
    if not found:
        print('None recorded (the save predates seed tracking, or the seeds were never made).')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
