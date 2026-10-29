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
           'nid_hired', 'nid_kin_sent', 'nid_kin_came', 'nid_kin_refused'),
          'requital_higher / _lower: requitals on someone of higher or lower rank; account_admitted / _refused: a lord who\n'
          'wronged a Bædling woman ruler kept or refused her Account; refused_unwritten / _answered: wrongs not written, and her\n'
          'answers with honour; self_judgment_*: awards set; fostered_seal: settlements sealed by fostering; avenge_*: an\n'
          "outlaw's kin offered, took or let rest a private Account; nid_borne / nid_no_bearer: suits a man carried, or none was at hand; nid_hired: of those borne, by a man hired for a fee;\n"
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

    # Bædling, wave 15 (tm_feud_tally_effect, bae6_*): raising a níð-pole oneself, the Níð of the Land, vows over the cup.
    print('== Bædling: wave 15 ==')
    w15 = ('poles_begun', 'poles_raised', 'poles_weighed_two', 'poles_failed', 'carver_named', 'pole_burned',
           'pole_turned', 'pole_humility', 'pole_suit', 'pole_law', 'carver_outlawed', 'sverrir_forfeit',
           'sverrir_exile', 'carver_sent_home', 'land_nid', 'land_noses', 'land_humility', 'land_crime', 'land_borne',
           'vows', 'vow_requital', 'vow_house', 'vow_land', 'vow_none', 'vow_kept', 'vow_broken', 'vow_owned',
           'vow_shout')
    if any(f'tm_feud_n_bae6_{s}' in gvars for s in w15):
        print('  '.join(f'{s} {int(gvars.get(f"tm_feud_n_bae6_{s}") or 0)}' for s in w15))
        print('poles_begun / _raised / _failed: Raise the Níð-Pole schemes started, poles that stood, nights that went wrong;\n'
              'poles_weighed_two: requitals by a pole that paid off two wrongs; carver_named: the carver\'s name came out;\n'
              'pole_burned / _turned / _humility / _suit / _law: how the one named answered (burned it, the hat is Óðinn\'s,\n'
              'Christian humility, a wrong in the Account, the carver to law); carver_outlawed: lesser outlawry under the old\n'
              'law; sverrir_forfeit / _exile: under the Christian law of Norway from 1270; carver_sent_home: caught and sent\n'
              'back; land_nid / land_noses: Níð of the Land made, and the verses (noses) in all; land_humility / _crime /\n'
              '_borne: the king\'s answer; vows / vow_requital / _house / _land / _none: vows over the cup and which;\n'
              'vow_kept / _broken: after five years; vow_owned: broken and said before the benches; vow_shout: flytings opened.')
    else:
        print('No counts (the save predates wave 15, or nothing has happened yet).')
    print()

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

    # Adelphai, wave 14 (tm_dl6_tally_effect): the Founding Rule, and the rest of the Dorley precedent.
    print('== Adelphai: wave 14 ==')
    dsteps = ('rule_1', 'rule_2', 'rule_3', 'copy_city_kept', 'copy_city_returned', 'intakes', 'disclosed',
              'disclosed_turned', 'disclosed_shaken', 'disclosure_waited', 'disclosure_shown', 'wards', 'ward_letters',
              'ward_accounts', 'ward_hall', 'ward_lapsed', 'sisters_made', 'sisters_declined', 'sponsor_gone', 'graduated',
              'book_her_word', 'book_all_of_it', 'stepped_back', 'order_holy', 'order_gate', 'word_kept', 'word_asks',
              'word_left', 'order_friend')
    print('  '.join(f'{s} {int(gvars.get(f"tm_dl6_n_{s}") or 0)}' for s in dsteps))
    print('rule_*: stages of the Mother House\'s rule written (read aloud, three copies, sealed); copy_city_*: the second\n'
          'copy lodged in the City or sent back; intakes: men taken into the Dorley cells; disclosed / _turned / _shaken:\n'
          'told that the sponsors were under the knife, and how he took it; disclosure_waited / _shown: not yet, or an evening\n'
          'at the House\'s table; wards: daughters raised from the cells into their ward years; ward_letters / _accounts /\n'
          '_hall: the second year\'s schooling; ward_lapsed: chains that ended early; sisters_made / _declined / sponsor_gone:\n'
          'the third year\'s answer; graduated (book_her_word / book_all_of_it): written into the House\'s book;\n'
          'stepped_back: left the House at the end; order_holy / _gate: washouts given to a holy order of the faith, or to\n'
          'the lay order at the Mother House; word_*: the letter years later (keeps the hours, asks for the door, left);\n'
          'order_friend: given the House\'s friendship.')
    print()

    # Badenya, wave 9 (tm_bd3_tally_effect): the Rock at Koulikoro and the fall of the associate.
    print('== Badenya: the Rock and the associate ==')
    bsteps = ('rock_came', 'rock_asked', 'rock_kept', 'rock_given', 'rock_joins', 'quarrels', 'raised', 'dust', 'ashes',
              'rides', 'restored', 'letters', 'sanctuary')
    print('  '.join(f'{s} {int(gvars.get(f"tm_bd3_n_{s}") or 0)}' for s in bsteps))
    print('rock_came: came to the rock at Koulikoro; rock_asked / _kept / _given: the one left sent for her, and the keeper kept\n'
          'the custom or gave her up; rock_joins: took the faith at the rock; quarrels / raised: quarrels with an associate, and\n'
          'another raised in her place; dust / ashes: whom the women of the house honoured; rides / restored: the fallen\n'
          'associate rode to the audience, and was restored; letters / sanctuary: wrote to a kinsman in exile, and was found out.')
    print()

    # Worn Garland, wave 10 (tm_ml4_tally_effect): the Tai bath, the band and the merchants, the road to Kanchi.
    print('== Worn Garland: wave 10 ==')
    gsteps = ('tai_kept', 'tai_not_now', 'tai_rain', 'tai_love', 'tai_nothing', 'bands_founded', 'bands_declined', 'caravans_taken', 'caravans_done', 'sworn', 'oath_refused', 'sworn_caravans',
              'relic_guard', 'halls', 'pepper_vowed', 'pepper_paid', 'pepper_forgot', 'pepper_paid_late')
    print('  '.join(f'{s} {int(gvars.get(f"tm_ml4_n_{s}") or 0)}' for s in gsteps))
    print('tai_*: Tai baths kept or put off, and what was asked of Kama; bands_founded / _declined: daughters hired by a southern\n'
          'lord\'s merchants to raise a band (wave 4, tm_ml3.0050), and those who stayed; caravans_taken / _done: wave 4 caravan contracts\n'
          'taken by Garland bands, and brought to the coast (the oath and the hall need one); sworn / oath_refused: bands that swore with the\n'
          'merchants or would not; sworn_caravans: caravans done for a sworn lord; relic_guard: bands guarding a relic temple\n'
          'in Lanka; halls: halls raised in a guild\'s name; pepper_*: vows on the road to Kanchi, paid, forgotten, paid late.')
    print()

    # Worn Garland, wave 11 (tm_ml5_tally_effect): the world after 1178, as era events.
    print('== Worn Garland: wave 11 ==')
    gsteps = ('deal_verse', 'deal_procession', 'deal_declined', 'first_house', 'first_house_declined', 'honour_passed',
              'honour_lapsed', 'guise_won', 'guise_lost', 'guise_face', 'guise_let_pass', 'part_spoken', 'part_taken',
              'part_ignored', 'part_street', 'part_watched', 'both_kept', 'both_slowed', 'both_market', 'both_one',
              'council_guard', 'council_declined')
    print('  '.join(f'{s} {int(gvars.get(f"tm_ml5_n_{s}") or 0)}' for s in gsteps))
    print('deal_*: honours bought from the temple, 1178-1300 (a verse in Markali, the flywhisk), or declined; first_house /\n'
          '_declined: the first house in the quarter where the king\'s hand is light; honour_passed / _lapsed: honours that\n'
          'went to a daughter at the holder\'s death, or back to the temple; guise_*: the commentator\'s word, answered and\n'
          'won or lost, turned ("nothing to take off"), or let pass; part_*: the girl\'s part at the festival, spoken against, corrected\n'
          '(taken / ignored), brought home to the street, or watched; both_*: the keeper of registers asks for one house\n'
          '(kept both, of which slowed; through the market; one); council_guard / _declined: bands hired by a temple council.')
    print()

    # Baedling bands, wave 16 (tm_bae7_tally_effect): the Vigla, the harbour, the Sword Is My Patent.
    print('== Bædling bands: wave 16 ==')
    bsteps = ('vigla_offered', 'vigla_taken', 'vigla_done', 'vigla_failed', 'robber_court', 'robber_home', 'toll_waived',
              'toll_kept', 'toll_double', 'habit_kept', 'habit_took', 'habit_found', 'harbour_offered', 'harbour_promised',
              'harbour_refused', 'harbour_camp', 'harbour_court', 'harbour_stayed', 'patent_refused', 'sword_drawn',
              'sword_granted', 'sword_war')
    print('  '.join(f'{s} {int(gvars.get(f"tm_bae7_n_{s}") or 0)}' for s in bsteps))
    print('vigla_offered: Keep the Road contracts given to AI bands; vigla_taken / _done / _failed: contracts taken by any band\n'
          '(players too), terms served, watches ended early; robber_*: a road thief sent to the lord\'s court or home;\n'
          'toll_*: the toll quarrel (waived, as the letter says, doubled); habit_*: the guards\' habit from 1327 (kept faith,\n'
          'robbed the road, found out); harbour_*: a landed Baedling band losing its land offered a harbour by a petty coastal\n'
          'lord (promised or refused), then, with the land gone, to his coast with the camp, to his court, or her own way;\n'
          'patent_refused: bands wronged after their patience; sword_*: The Sword Is My Patent sent, answered with the county,\n'
          'or with the claim war.')
    print()

    # Reactions, wave 12 (tm_rx_tally_effect): how the surrounding religious authorities react.
    print('== Reactions: wave 12 ==')
    rsteps = ('counted', 'weighed_refused', 'sworn', 'oath_refused', 'not_today',
              'master_answered', 'master_name', 'master_valley_gate', 'master_away',
              'consilium', 'no_doctor', 'own_test',
              'no_knife_here', 'masarra', 'owned_charge', 'asked_it',
              'for_herself', 'among_own', 'spared_friend',
              'penance_1', 'penance_2', 'penance_3', 'commuted_alms', 'commuted_house', 'house_refused', 'borne', 'refused', 'excluded')
    if any(f'tm_rx_n_{s}' in gvars for s in rsteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_rx_n_{s}") or 0)}' for s in rsteps))
        print('counted / weighed_refused: the bishop\'s court, Huguccio\'s questions (1188-1249), answered or refused; sworn / oath_refused:\n'
              'Hostiensis\'s oath (1250-1390), sworn or refused; not_today: either era, not today; master_*: the Paris master (1191-1300),\n'
              'answered, the confirmation name (Dorleyites), the Valley Gate, or kept away; consilium / no_doctor / own_test: the Perugia\n'
              'consilium (from 1395); no_knife_here / masarra / owned_charge / asked_it: Ibn Hazm\'s charge at an Andalusi court (1030-1250);\n'
              'for_herself / among_own / spared_friend: istihlal at a Mamluk court (from 1250); penance_1/2/3: rungs of the Slavic penance\n'
              'ladder reached; commuted_alms / commuted_house / house_refused: commutations by alms or by the House\'s rule, and the bishop\'s\n'
              'refusals; borne / refused: rungs borne or refused; excluded: rulers who ended the ladder barred from the chalice.')
    else:
        print('No counts (the save predates wave 12, or no voice has spoken yet).')
    print()

    # Yutai Dao, wave 13 (tm_yt4_tally_effect): the levers, the women's chains and the regency rules.
    print('== Yutai Dao: wave 13 ==')
    ysteps = ('cui_took', 'cui_refused', 'cui_listened', 'cui_aside', 'boy_kept', 'boy_ransomed', 'boy_home',
              'levy_paid', 'levy_hidden', 'levy_found', 'levy_patron', 'ledgers_sealed', 'ledgers_audited',
              'ledgers_grain', 'ledgers_opened', 'ledgers_declined', 'xue_read', 'xue_wrote', 'xue_declined',
              'xue_altar', 'xue_record', 'xue_kept', 'wang_names', 'wang_levy', 'wang_listened', 'wang_saint',
              'wang_oracle', 'wang_both', 'moshan_fox', 'moshan_form', 'moshan_bowed', 'anteroom_kept',
              'anteroom_complied', 'anteroom_refused', 'consort_kept', 'consort_honoured', 'consort_sent',
              'widow_vows', 'widow_household', 'widow_refused', 'chengtian_answered', 'chengtian_asked',
              'chengtian_silent', 'regent_face', 'regent_curtain', 'regent_no_curtain', 'curtain_stepped',
              'curtain_robes', 'curtain_minister')
    print('  '.join(f'{s} {int(gvars.get(f"tm_yt4_n_{s}") or 0)}' for s in ysteps))
    print('cui_*: Cui Yin\'s memorial, 901-902 (took the palace women\'s seal, refused, listened for the inner offices,\n'
          'stood aside); boy_*: a tribute boy at the House gate before 907 (kept, the year\'s boys ransomed, sent home);\n'
          'levy_*: the Commissioner of Merit\'s repair levy (paid, hidden in the society store or found, a palace patron);\n'
          'ledgers_*: Seal the Ledgers, 1403-1449; xue_*: Lady Xue at Hezhong 874-881 and the news of 882-885; wang_*:\n'
          'Wang Fengxian heard, and which account the House wrote; moshan_*: the answer at Mo-shan; anteroom_* / consort_* /\n'
          'widow_*: the three routes into the abbeys; chengtian_*: the hut of rebirth, 982-1009; regent_*: Way regencies\n'
          'by rule (face to face, curtain, without the curtain); curtain_*: how a curtain regency ended.')
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
    hsteps = ('households', 'household_joins', 'falls', 'relit')
    if any(f'tm_hn4_n_{s}' in gvars for s in hsteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_hn4_n_{s}") or 0)}' for s in hsteps))
        print('households: households of the street sent for; household_joins: members of those households the kahal took in;\n'
              'relit: times the women of the lamp came back to the Venaissin when no house of the sect stood;\n'
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
