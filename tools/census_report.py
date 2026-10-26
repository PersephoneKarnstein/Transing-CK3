#!/usr/bin/env python3
"""Reads an uncompressed CK3 save and prints how the six faiths have fared over the run.

    python3 tools/census_report.py "<path to save>.ck3"

What it reads (written by common/scripted_effects/tm_tracking_effects.txt and tm_growth_effects.txt):
  - the census kept on each faith by decade (tm_c<decade>_<what>), taken every 10 years;
  - the seats (tm_seat_branch on the seat county: vassal, lord or unheld) and who holds them now;
  - the characters made at game start (global lists tm_seeds_<seat>): alive or dead, faith, court;
  - the Women's Chamber's run-wide counts (globals tm_dl3_n_<step>, from tm_dl3_effects.txt);
  - the Bædling Account's run-wide counts (globals tm_feud_n_<step>, from tm_feud_effects.txt);
  - Ha-Nehpakhot's households and patrons' falls (globals tm_hn4_n_<step>, from tm_hn4_effects.txt).
Saves must be plain text: turn off "compress saves" in the game settings, and do not play ironman.
"""
import re
import sys

FAITHS = {
    'transbian_maximalism': 'Adelphai Dorleyaiou',
    'tm_baeddel': 'Bædling',
    'tm_yutai': 'Yutai Dao',
    'tm_nehpakhot': 'Ha-Nehpakhot',
    'tm_garland': 'Mālai',
    'tm_badenya': 'Badenya',
}
SEATS = {
    'phrygia': 'c_phrygia', 'gotland': 'c_gutland', 'aland': 'c_aland', 'shazhou': 'c_shazhou',
    'arles': 'c_venaissin', 'kanchipuram': 'c_kanchipuram', 'candragiri': 'c_candragiri', 'kirina': 'c_sibi_mali',
    'awkar': 'c_awkar',
}
METRICS = ['members', 'daughters', 'marked', 'rulers', 'counties']
COUNTERS = ['joins', 'ruler_joins', 'kahal_joins', 'matches', 'offers', 'rises', 'deaths', 'pool_deaths', 'pilgrims']

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
        print('decade  members daught marked rulers counties | per decade: joins ruler kahal match offers rises deaths  pool pilgr')
        prev = {c: 0 for c in COUNTERS}
        for d in decades:
            row = [int(v.get(f'tm_c{d:04d}_{m}', 0) or 0) for m in METRICS]
            cum = {c: int(v.get(f'tm_c{d:04d}_{c}', 0) or 0) for c in COUNTERS}
            inc = [cum[c] - prev[c] for c in COUNTERS]
            prev = cum
            print(f'{d}s  {row[0]:7} {row[1]:6} {row[2]:6} {row[3]:6} {row[4]:8} |  {inc[0]:10} {inc[1]:5} {inc[2]:5} {inc[3]:5} {inc[4]:6} {inc[5]:5} {inc[6]:6} {inc[7]:5} {inc[8]:5}')
        print()
    if decades:
        print('deaths: members seen at a census who died with a court or as rulers (from v0.3; before, every death with a\n'
              'court). pool: the rest (no court, or made and cleared between two censuses). pilgr: the kahal\'s pilgrims\n'
              'and members going to a court of their faith (from v0.3 all six faiths, and a dead ruler\'s household).\n')
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

    # Rulers who converted in through the game's conversion (tm_conv_on_actions.txt): run-wide, per faith.
    print('== Rulers converting in (run-wide) ==')
    print(f'{"":20} {"all":>6} {"outsiders":>10} {"turned away":>12}')
    for t, name in FAITHS.items():
        v = faith_vars.get(t, {})
        n = [int(v.get(f'tm_n_{k}') or 0) for k in ('ruler_converts', 'outsider_converts', 'turned_away')]
        print(f'{name:20} {n[0]:6} {n[1]:10} {n[2]:12}')
    print('all: AI rulers who took the faith by the game\'s conversion; outsiders: with no tie to its community;\n'
          'turned away: of those, kept their old faith (one in three).')
    print()

    # The Account (tm_feud_tally_effect): feud, bót, the níð suit and reprieves, run-wide.
    print('== The Account (Bædling feud) ==')
    fsteps = ('wrongs', 'requitals', 'settled', 'truce_broken', 'nid_suits', 'nid_outlawed', 'nid_poles', 'reprieve_kills', 'reprieves')
    if any(f'tm_feud_n_{s}' in gvars for s in fsteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_feud_n_{s}") or 0)}' for s in fsteps))
        print('wrongs: unanswered wrongs entered; requitals: wrongs that paid one back; settled: bót taken;\n'
              'truce_broken: a wrong within ten years of bót; nid_suits / nid_outlawed: suits for the three words, and\n'
              'speakers outlawed; nid_poles: níð-poles raised against Bædling rulers; reprieve_kills: outlaws killed toward a reprieve; reprieves: sentences lifted that way.')
    else:
        print('No counts (the save predates the Account, or nothing has been entered).')
    print()

    # Bædling, wave 7 (tm_feud_tally_effect): the rest of the feud, outlawry and the law, the era's news and lore.
    def wave7(title, names, legend):
        print(f'== {title} ==')
        if any(f'tm_feud_n_{s}' in gvars for s in names):
            print('  '.join(f'{s} {int(gvars.get(f"tm_feud_n_{s}") or 0)}' for s in names))
            print(legend)
        else:
            print('No counts (the save predates wave 7, or nothing has happened yet).')
        print()
    wave7('Bædling: the feud (wave 7)',
          ('requital_higher', 'requital_lower', 'account_admitted', 'account_refused', 'refused_unwritten', 'refused_answered',
           'self_judgment_modest', 'self_judgment_heavy', 'self_judgment_remit', 'fostered_seal',
           'avenge_offered', 'avenge_taken', 'avenge_rested', 'nid_borne', 'nid_no_bearer',
           'nid_kin_sent', 'nid_kin_came', 'nid_kin_refused'),
          'requital_higher / _lower: requitals on someone of higher or lower rank; account_admitted / _refused: a lord who\n'
          'wronged a Bædling woman ruler kept or refused her Account; refused_unwritten / _answered: wrongs not written, and her\n'
          'answers with honour; self_judgment_*: awards set; fostered_seal: settlements sealed by fostering; avenge_*: an\n'
          "outlaw's kin offered, took or let rest a private Account; nid_borne / nid_no_bearer: suits a man carried, or none was at hand;\n"
          "nid_kin_*: kinsmen sent for from afar, and whether they came.")
    wave7('Bædling: outlawry and the law (wave 7)',
          ('out_suits', 'out_iceland_client', 'out_iceland_no_client', 'out_oath_held', 'out_court_called', 'out_court_held',
           'out_court_failed', 'out_penance', 'out_secular_arm', 'out_rides', 'out_ride_settled', 'out_ride_refused',
           'out_harboured', 'out_harbour_paid', 'out_harbour_refused', 'out_harbour_witnessed', 'out_holms'),
          'out_suits: suits brought; out_iceland_*: Icelandic suits on a client, or with none; out_oath_held: cleared by oath;\n'
          'out_court_*: confiscation courts called, held, failed (the sentence lapses); out_penance: penance taken;\n'
          'out_secular_arm: relapses handed over; out_ride*: rides for sympathy, and their outcomes; out_harbour*: outlaws\n'
          "kept by a House's lord, and the summons answered; out_holms: outlaws' holms named.")
    wave7('Bædling: the era and lore (wave 7)',
          ('bae3_kings_example', 'bae3_bishops_letter', 'bae3_islands_news', 'bae3_seidmenn_charge', 'bae3_site_story',
           'bae3_calling_herself', 'bae3_warding_shirt'),
          "kings_example: the King's Example told; bishops_letter: edicts on a House; islands_news: Word from the Islands;\n"
          "seidmenn_charge: They Say He Keeps Seiðmenn; site_story: holy-site stories; calling_herself: the Rykener echo;\n"
          'warding_shirt: shirts woven.')

    # The Council of the Two Schools (tm_dl4_tally_effect): Adelphai Dorleyaiou, run-wide.
    print('== Council of the Two Schools ==')
    gy = gvars.get('tm_dl2_galenic_year')
    print(f'Galenic rite: founded {int(gy)}' + (' by a teacher\'s event' if 'tm_dl4_n_teacher' in gvars else ' by decision') if gy is not None
          else ('Galenic rite: founded (year not recorded)' if 'tm_dl2_galenic_founded' in gvars else 'Galenic rite: never founded'))
    csteps = ('called', 'ari', 'gal', 'broke', 'home', 'held')
    if any(f'tm_dl4_n_{s}' in gvars for s in csteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_dl4_n_{s}") or 0)}' for s in csteps))
        print('called: councils opened; ari / gal / broke: the Mother\'s book kept, the third estate allowed, or no vote;\n'
              'home / held: Galenic rulers who came home after the book was kept, or kept the Emperor\'s count.')
    else:
        print('No counts (the save predates the council, or none has been called).')
    school = ('students', 'school_joins')
    if any(f'tm_dl4_n_{s}' in gvars for s in school):
        print('  '.join(f'{s} {int(gvars.get(f"tm_dl4_n_{s}") or 0)}' for s in school)
              + f'  (now {int(gvars.get("tm_dl2_n_galenic") or 0)} of {int(gvars.get("tm_dl2_n_faith") or 0)} Galenic)')
        print('students: who took the rite with its founder; school_joins: members talked round in later years.')
    print()

    # The Tower on the Condition (tm_dl5_tally_effect): Adelphai Dorleyaiou, run-wide.
    print('== Adelphai: the Tower on the Condition ==')
    tsteps = ('petitions', 'granted', 'refused', 'came', 'kept', 'extended', 'revoked', 'shepherds')
    print('  '.join(f'{s} {int(gvars.get(f"tm_dl5_n_{s}") or 0)}' for s in tsteps))
    print('petitions: sisters who asked a lord for an empty tower; granted / refused: his answer; came: sisters who moved\n'
          "to a tower's court to man it; kept: five manned years; extended / revoked: an empty tower given another year,\n"
          'or taken back; shepherds: robbers taken on as herders.')
    print()

    # The Women's Chamber (tm_dl3_tally_effect): run-wide counts of each step.
    print("== Women's Chamber ==")
    steps = ('rolled', 'fired', 'took', 'stayed', 'lost', 'worked', 'chrysobull', 'estate')
    if any(f'tm_dl3_n_{s}' in gvars for s in steps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_dl3_n_{s}") or 0)}' for s in steps))
        print('rolled: the yearly roll wrote to a daughter; fired: the letter reached her; took / stayed: her answer;\n'
              'lost: a post that ended, for any cause; worked: an AI daughter in post worked the chamber;\n'
              'chrysobull: charters won for a House; estate: counties the throne granted.')
    else:
        print('No counts (the save predates the tally, or the chamber has never written).')
    print()

    # Ha-Nehpakhot, wave 6 (tm_hn4_tally_effect): run-wide.
    print('== Ha-Nehpakhot: households and falls ==')
    hsteps = ('households', 'household_joins', 'falls')
    if any(f'tm_hn4_n_{s}' in gvars for s in hsteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_hn4_n_{s}") or 0)}' for s in hsteps))
        print('households: households of the street sent for; household_joins: members of those households the kahal took in;\n'
              'falls: patrons of the sect who died while holding the translation patronage.')
    else:
        print('No counts (the save predates wave 6, or nothing has happened yet).')
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
