# The Worn Garland, wave 11: the world after 1178, as era events in every start

Roadmap item (`docs/TODO.md`, "The Worn Garland's 1178 changes as era events in every start"): the Garland gets no new start. Its seat, faith and gate stay the same, and what changes is the world, by date, in any campaign that reaches it. Built 2026-10-27, untested in game. Namespace `tm_ml5`. It builds on stage 2 (`docs/stage2/worn-garland.md`: shares, gifts, temple streets), wave 4 (`docs/wave4/garland.md`: the market, the bands of tm_ml3.0050) and wave 10 (`docs/wave10/garland.md`).

Files (new, with a BOM): `events/tm_ml5_events.txt`, `common/on_action/tm_ml5_on_actions.txt`, `common/scripted_triggers/tm_ml5_triggers.txt`, `common/scripted_effects/tm_ml5_effects.txt`, `common/modifiers/tm_ml5_modifiers.txt`, `localization/english/tm_ml5_l_english.yml`. No existing file is changed. Wave 11 reads stage 2's share (`tm_ml2_share`, `tm_ml2_at_share_trigger`, `tm_ml2_mark_street_effect`, `tm_ml2_gifts`), wave 4's market and band triggers (`tm_ml3_nagaram_county_trigger`, `tm_ml3_garland_band_trigger`), wave 10's `tm_ml4_band_and_street_opinion`, and the flavour budget.

**Sources.** Orr 2000 (`research/ind_orr_temple_women.md`); Orr 2013 and Anandakichenin 2020 (`research/ind_orr_2013_anandakichenin.md`); Carman and Narayanan 1989 (`research/ind_carman_narayanan_tamil_veda.md`); Narayanan 1994 (`research/ind_narayanan_vernacular_veda.md`); Hall 1980 (`research/ind_hall_cola_trade.md`); the region note `research/later_starts/region_south-asia-maritime-sea.md` §1, §3, §4 and §5. Page numbers are the notes' citations of the books.

## The dates

| Gate | What | Source | Kind |
|---|---|---|---|
| 1150 | The commentator's word (0010) | Piḷḷāṉ's *Six Thousand*, "written between 1100 and 1150" (Carman and Narayanan 1989, p. xi) | The latest date of composition |
| 1150 | The girl's part (0011) | 12th-c. anecdotes of Empār and Nañjīyar, told in 13th-c. commentary (Narayanan 1994, pp. 126, 132) | **Inferred**: no inscription read dates the service; mid-century stands for "12th c." |
| 1178 | Both temples (0020) | Men renamed *mahēśvara*, *śivabrāhmaṇa*, *śrīvaiṣṇava*; *tēvaraṭiyār* 91% women in 1178–1300 (Orr 2000, pp. 55–56) | Orr's period; the renaming is not dated more finely |
| 1178–1300 | To her and her descendants (0001); the first house (0030) | Orr's last period (pp. 46, 67–73, 161–63); the 21 deals, all 1070–1300, ten hereditary (pp. 74–75, 151); giving stops after 1300 (pp. 174–77) | **Inferred** start: Orr's notes do not split the deals between 1070–1178 and 1178–1300 (region note §5, question 9). Stage 2 already sells shares from 1070 |
| 1200 | The council's guard (0031) | Merchants and their armies back men seeking power in the 13th c. (Hall 1980, p. 206) | "13th c." read as 1200; the temple council hiring a band is design |

## 1. To Her and Her Descendants (0001, 0002)

**Source.** Orr's 21 deals (1070–1300): a temple woman's gift exchanged for an honour, such as a place near the god in procession, the flywhisk, consecrated food, or a set verse of a hymn. Ten are hereditary, "to her descendants" (Orr 2000, pp. 74–75, 151). Temple women bought the singing of the *Tiruvempāvai* at Nallur in the 12th c. (ARE 1940–41 nos. 143–176; pp. 56, 105–08), and the seventh verse at the Tiruvātirai festival in Mārkaḻi at Tirupampuram in 1213 (NK 134; pp. 17–18). The line is traced through the mother (p. 156). Adoption before 1300 is Orr's guess (ch. 3 n. 28, p. 228), and the Garland claims it as its own, as stage 2 does.

**What the player sees.** From 1178 to 1299, a daughter of the Garland living on the street of her share, with 30 gold, 8 in 100 a year (flavour budget; asked once per 10 years): the temple council offers a deed.
- *The verse in Mārkaḻi* (60 gold): +20 piety; *A Verse in Mārkaḻi* (+0.3 piety, +0.1 prestige a month, permanent).
- *A place near the god, and the flywhisk* (30 gold): +10 prestige; *Near the God in Procession* (+0.3 prestige a month, permanent).
- *The gold stays in my house this year*: nothing.

When she dies, every honour she holds passes to her eldest daughter of the street's faith, born or taken (`on_death`; 0002 tells the heir). With none, the honours go back to the temple. Honours already held keep passing after 1300; only new deals stop.

**Guardrails.** The money is plain: the accountants take a fee (rule 7). The narrator does not make the temple women of the record daughters of the Garland: "women of the temples" buy such honours, and she is one buyer among them. The verse is the Śaiva *Tiruvempāvai*, the one temple women sang (Orr p. 108), not the *Tiruppāvai*.

## 2. The Commentator's Word (0010)

**Source.** Piḷḷāṉ, the first commentator on the *Tiruvāymoḻi* (1100–1150), says the poet speaks "in the guise of another" (Carman and Narayanan 1989, p. 96), yet tells decad 6.2 with the poet as "she" (p. 99), and the friend knows the girl "by her exceeding love" (6.5.10; p. 76). The faith's first doctrine is the inversion: "the guise was the truth" (region note §1, 1178, item 2).

**What the player sees.** From 1150, a daughter of the Garland at a Hindu court in Tamil country, or at a Vaiṣṇava court anywhere in the Deccan, 4 in 100 a year (flavour budget; once per 25 years): a reciter who signs himself *śrīvaiṣṇava* reads the commentary's word against her before the hall.
- *"Read on. Your teacher knows a girl by her love, not by her guise. So may you."* 45 (+20 learning ≥ 12, +15 learning ≥ 18): +40 prestige, *Answered the Commentator* (+1 learning, +0.2 prestige a month, 10 years), the host +10 opinion. Otherwise 40 (+15 learning < 8): +10 piety; "she said it anyway".
- *"A guise is put on and taken off. I have nothing to take off."* (Her answers are about herself, never a claim on the poet.) +30 piety; a Vaiṣṇava host −10 opinion.
- *Let him finish* (−10 stress): no cost (rule 23).

**Guardrails.** "Guise" is the reciter's word, said by an invented hostile man, and the commentary's word in quotation marks. The narrator never calls her a guise. Piḷḷāṉ and Rāmānuja are not named ("a disciple of the great teacher"), and the Śrīvaiṣṇavas are not made the villain: the reciter is one man.

## 3. The Girl's Part (0011)

**Source.** At the festival of recitation a man of the hereditary reciting families sings and dances the poet's girl, her mother and her friend (Narayanan 1994, p. 130). Empār corrected how a performer played the girl, and the performer accepted (p. 126). Women were not allowed to perform (ch. 8 n. 14). Only three temples have the service (p. 123). The faith's grievance is from the region note §1: "the temple lets a man play the girl but will not let the girl in."

**What the player sees.** From 1150, the same courts as 0010, 3 in 100 a year (flavour budget; once per 25 years): she has been with the pilgrims to "the island temple" for the festival.
- *Say it at the temple gate*: +25 prestige, +10 piety; a Vaiṣṇava host −10 opinion.
- *Call out from among the women how the girl should grieve* (the Empār beat, turned to her): 50 (+20 learning ≥ 12, +10 diplomacy ≥ 12) he bows toward the women and plays it her way (+40 prestige, +10 piety); otherwise he plays on (+10 piety).
- *Bring the song home, and sing it on our street*: −15 stress; her share's county (or the county she is in) becomes a temple street and gets *The Girl's Part on the Street* (+5 county opinion, +5% development growth, 5 years). Rule 7: the street has its own art.
- *It was beautiful. Leave it there* (−10 stress).

**Guardrails.** The office is never named in loc: the word names a living hereditary office (Narayanan note, design implications). The performer is a man playing a part, and the event says so; nobody in it is a daughter, and the narrator does not claim the reciting families. The pollution reasons for the bar are not given (the Narayanan note keeps them for hostile mouths only); the text says only "that is the temple's rule". "Sang and danced" uses no classical dance term (rule 11).

## 4. Both Temples (0020)

**Source.** In 1178–1300, men of status bear *mahēśvara*, *śivabrāhmaṇa* or *śrīvaiṣṇava*, groups that exclude women, while *tēvaraṭiyār*, "devotees", becomes a woman's word (Orr 2000, pp. 55–56). The two sects contend at court for patronage in the 13th-c. Kannada witness (Ben-Herut, via Anandakichenin 2020, p. 253). The market's way through is Hall's: Śaiva quarters kept a lamp in a Viṣṇu temple through the *nagaram* (1980, p. 91).

**What the player sees.** From 1178, a daughter of the Garland with a share or a gift on record, at a Śaiva or Vaiṣṇava court in the Deccan, 5 in 100 a year (flavour budget; once per 15 years): the keeper of the share registers wants her lamp in one house.
- *Both, as the street always has*: +30 piety; 40 in 100, *Slow Registers* (−0.3 gold a month, 5 years); a zealous host −10 opinion.
- *Let the market keep my lamp in the other house* (30 gold; a county with a market town): +15 piety, +10 prestige.
- *This year, one house. The street will understand* (−5 stress): no cost (rule 23).

**Guardrails.** Oṭṭakkūttar's image-in-the-sea boast is unverified (region note §5, question 2) and is not used. The friction is men's titles and a contest for gifts, not violence. Applying the Kannada court contest to a Tamil court is an inference.

## 5. The First House in the Quarter (0030)

**Source.** A woman received "the first house in the temple quarter" and precedence in festivals, for her and her descendants, for gold (ARE 29 of 1940–41; Orr 2000, p. 151). Temple women thrived "under non-Chola kings, and where royal power is weak" (pp. 80–82, 161, 163–64). With the court's men away at war, the temple councils grew stronger (region note §3).

**What the player sees.** From 1178 to 1299, a daughter of the Garland on the street of her share, where the king's hand is light (the share's county has control under 75, or its holder's top liege is at war), with 30 gold, 6 in 100 a year (flavour budget; once per 10 years): the temple council offers the first house.
- *The first house, then* (40 gold): +10 prestige; *The First House in the Quarter* (+0.3 gold, +0.1 prestige a month, permanent; passes like the other honours).
- *Not while the roads are like this*: nothing.

**Guardrails.** Not a liberation story and no "golden age": the roads are worse, the council needs gold, and "the farmers on the temple's land are not asked". It is only where women's deals did well (Orr). "Non-Chola kings" is not checked; weak royal power stands in.

## 6. The Council's Guard (0031)

**Source.** Hall: market towns formed troops first "hired to police the local market-place and the overland trade routes" (1980, p. 81); in the 13th c. merchants and their armies backed men seeking power (p. 206); under Rājarāja III (1216–60) Hoysaḷa generals put down a rebel chief and a merchants' town (p. 195). No source joins a temple council to a band: design.

**What the player sees.** From 1200, a band of the Garland (wave 4's bands, tm_ml3.0050) camped in Tamil country where the king's hand is light, 15 in 100 a year (flavour budget; once per 10 years): the temple council pays the band to walk beside the temple's paddy and the festival car.
- *We will walk beside the paddy and the car*: +30 gold, +20 prestige; the county becomes a temple street and gets *The Council's Guard* (+0.2 control a month, 10 years); every shareholder there +10 opinion of the captain (wave 10's `tm_ml4_band_and_street_opinion`).
- *The band is spoken for*: +5 prestige.

**Guardrails.** Nothing is fought on screen. No guild member in Hall's records is a woman (note §8); the council hires the band, it does not join anything. The Kaikkōḷa regiment and the Five Hundred are not named or claimed.

## 7. Counting

`tm_ml5_tally_effect` keeps run-wide globals `tm_ml5_n_<what>`. For `tools/census_report.py`, after the wave 10 block:

```python
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
```

## 8. Not built

- **Buy a Verse as a gate step.** The region sketch (§3) has a bought verse add weight to the pāvai vow. The gate stays the same in this wave, so `tm_garland.0001` is untouched. If wanted: `modifier = { add = 10 has_variable = tm_ml5_verse }` in its success list, or on the elder (`scope:tm_garland_elder ?= { has_variable = tm_ml5_verse }`).
- **"Rank without gifts" after 1300** (Orr pp. 174–77): new deals simply stop at 1300. A late event where the king's endowment hands her a turn she did not buy would close the arc.
- *A Name in Stone* weighted up at 1178 (region note §3): an existing file, not changed.
- Oṭṭakkūttar's boast and Rāmānuja's exile: unverified (region note §5, questions 2 and 3).
- Kanchipuram's 13th-c. endowment "for the maintenance of women reciters" (Narayanan p. 55): it would fit a salaried office, already proposed as a court position in the Narayanan note.

## Uncertain syntax (check in game)

- `on_death` reads the dying holder's variables and children (`ordered_child`) before she is removed (stage 2's `tm_ml2_on_death` does the same).
- The macro names `tm_ml5_$HONOUR$` and `tm_ml5_$HONOUR$_modifier` in `tm_ml5_give_honour_effect`, with `COUNTY = scope:tm_ml5_mother.var:tm_ml5_verse`.
- `holder.top_liege ?= { is_at_war = yes }` on a county title.
- Saved `scope:tm_ml5_host` carried from the pulse through `trigger_event` to 0010, 0011 and 0020.

## Test scenarios (for TO-TEST.md)

Suggested heading: `## The Worn Garland, wave 11 (added 2026-10-27, untested in-game; docs/wave11/garland.md)`, items AM1–AM8 (rename if wave 12 takes AM).

- [ ] **AM1. A verse to her and her descendants.** After 1178, a daughter of the Garland with a share, living in its county, 70 gold: fire tm_ml5.0001; buy the verse (60 gold, *A Verse in Mārkaḻi*, `tm_ml5_verse` = the county); fire again: the verse option is gone, the flywhisk remains. Before 1178 and from 1300 the pulse never offers it.
- [ ] **AM2. The honour passes.** Give her a Garland daughter (born, or by Take as Daughter), then kill her: 0002 fires for the daughter, who now has the modifier and the variable. Kill a holder with no daughter: `honour_lapsed` rises.
- [ ] **AM3. The commentator's word.** After 1150, a courtier daughter at a Hindu court in Tamil country (or a Vaiṣṇava court in the Deccan): fire 0010 with `scope:tm_ml5_host`; check both outcomes of option a (learning 5 and 20), the Vaiṣṇava host's −10 on option b, and that option c costs nothing. The narrator's text never calls her a guise.
- [ ] **AM4. The girl's part.** Same court: fire 0011; option c marks the share county (or her county) as a street with *The Girl's Part on the Street*; option b's two toasts.
- [ ] **AM5. Both temples.** After 1178, a daughter with a share or a gift at a Śaiva or Vaiṣṇava court: fire 0020; option a sometimes gives *Slow Registers*; option b shows only with 30 gold in a county with a city holding.
- [ ] **AM6. The first house.** 1178–1299, a shareholder at her street whose county control is under 75 (or whose top liege is at war): 0030; buy (40 gold, permanent modifier, passes as in AM2). At full control and peace it is not offered.
- [ ] **AM7. The council's guard.** After 1200, a Garland band camped in Tamil country in a county under 75 control: 0031; guard: +30 gold, the county modifier and street mark, shareholders there +10 opinion of the captain.
- [ ] **AM8. Observe run (867 → c. 1450).** The census "Worn Garland: wave 11": `guise_*` and `part_*` above 0 after 1150; `deal_*` and `first_house` above 0 between 1178 and 1300, and not rising after 1300; `honour_passed` / `honour_lapsed` above 0; `council_guard` only if a band exists (AL8). The error log for `tm_ml5`.

## Ready-to-paste README text (Worn Garland section)

> **The world after 1178 (wave 11).** In any start that reaches them, the Garland's world changes around it. From 1178 to 1300, temple councils sell a daughter on the street the singing of a verse in Mārkaḻi, a place near the god with the flywhisk, or, where the king's hand is light, the first house in the temple quarter, all "to her and her descendants": at her death they pass to her daughter, born or taken. From 1150 a reciter may read the new commentary's word "guise" against her before the hall, and at the festival of recitation she watches a man play the girl in a temple that will not let the girl in. From 1178 the men of the temples sign themselves by their Lord, and a lamp in both houses becomes a question. From 1200 a temple council may hire a band of the Garland to walk beside its paddy while the king's men are away. (Orr 2000; Carman and Narayanan 1989; Narayanan 1994; Hall 1980)

## Ready-to-paste TODO text

- [x] Garland wave 11 (`tm_ml5`): the 1178 changes as era events in every start: honours to her and her descendants (0001–0002) and the first house where the king's hand is light (0030), 1178–1300; the commentator's word (0010) and the girl's part (0011), from 1150; both temples (0020), from 1178; the council's guard (0031), from 1200 (built, not yet tested in game)
- [ ] Garland, not built from the 1178 notes: Buy a Verse as a gate step (the gate is unchanged); "rank without gifts" after 1300; *A Name in Stone* weighted at 1178; Oṭṭakkūttar and Rāmānuja's exile (unverified)
