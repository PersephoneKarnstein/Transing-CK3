# The Worn Garland, stage 2 (design note, 2026-10-21, untested in-game)

Prefix `tm_ml2_`, event namespace `tm_ml2`. Faith page: [docs/faiths/cutikkotutta-malai.md](../faiths/cutikkotutta-malai.md). Stage 1 feature it builds on: the temple's deal (`tm_kovil`).

**Why these features.** In the v0.2.0 observe run (1034) the Garland held no county. Its 25 members were courtiers at Shaiva courts, one Garland republic and a mercenary band. Almost all of stage 1 fires for rulers: *A Name in Stone* (`tm_garland.0020`) goes to a ruler of the faith through `yearly_playable_pulse`, and only `tm_kovil` reaches a courtier. Stage 2 gives a landless daughter something of her own that is tied to a place: a share on a temple street, gifts recorded in her name, and a title. This follows what the temple women of the inscriptions actually were. Their main recorded role is donor (133 of 304 inscriptions), and since they did not marry, their wealth stayed under their own control (Orr 2000, pp. 66, 72–73; `research/ind_orr_temple_women.md` §1). The faith borrows their shares and gifts. It does not make them trans, and it does not call them dancing girls, courtesans or brides of God.

Everything reaches a courtier through her host's `yearly_playable_pulse`, as `tm_kovil` does. A playable daughter (a ruler, the republic, the mercenary captain or an adventurer) gets the same events herself, and also gets a decision.

**Status.**

| # | Feature | Status |
|---|---|---|
| 1 | A Share on the Temple Street (share, pay, staying, passing on) | Drafted in script and loc |
| 2 | A Gift in Her Own Name (endowment) | Drafted in script and loc |
| 3 | She of the Illustrious Staff (title) | Drafted in script and loc |
| 4 | Reaction layers: Food and Clothing (Hindu), Of the Third Feeling (Jain), the Order's Terms (Śvetāmbara) | Drafted in script and loc |
| 5 | The Reciter: Kāraikkāl Ammaiyār and Basavaṇṇa at Shaiva courts | Drafted in script and loc |
| – | Solitary Tai vow to Kāma at Kanchi | Option only, not built (user: "either or") |

**Files (all new).**
- `events/tm_ml2_events.txt`: tm_ml2.0001, 0003, 0004, 0010, 0011, 0030, 0031, 0032, 0040
- `common/on_action/tm_ml2_on_actions.txt`: `tm_ml2_yearly` on `yearly_playable_pulse`; `tm_ml2_on_death` on `on_death`
- `common/scripted_effects/tm_ml2_effects.txt`: `tm_ml2_mark_street_effect`, `tm_ml2_grant_share_effect`, `tm_ml2_remove_share_effect`, `tm_ml2_pass_share_effect`, `tm_ml2_share_year_effect`, `tm_ml2_record_gift_effect`, `tm_ml2_give_staff_effect`
- `common/scripted_triggers/tm_ml2_triggers.txt`: `tm_ml2_share_candidate_trigger`, `tm_ml2_share_heir_trigger`, `tm_ml2_at_share_trigger`, `tm_ml2_donor_trigger`, `tm_ml2_street_trigger`, `tm_ml2_food_and_clothing_child_trigger`, `tm_ml2_reciter_listener_trigger`
- `common/modifiers/tm_ml2_modifiers.txt`: `tm_ml2_share_modifier`, `tm_ml2_name_in_stone_modifier`, `tm_ml2_staff_modifier`, `tm_ml2_admitted_modifier`, `tm_ml2_street_county_modifier` (county)
- `common/decisions/tm_ml2_decisions.txt`: `tm_ml2_gift_decision`
- `common/nicknames/tm_ml2_nicknames.txt`: `tm_ml2_nick_talaikkoli`
- `localization/english/tm_ml2_l_english.yml`

Validation: xTiger reports nothing in these files (23 reports, the known baseline). `tools/check_glyphs.py` is clean for them.

**Revision (2026-10-21), against Orr's periodisation** (`docs/later_starts.md`; `research/later_starts/region_south-asia-maritime-sea.md` §1). Orr's periods are 850–985, 985–1070, 1070–1178 and 1178–1300. The drafts now follow them: hereditary passing and bought shares start in 1070; grants and gifts are rarer in the 985–1070 trough; the Lady starts in 1119; the staff title starts in 1100. See **Dates** below.

## Decisions (user, 2026-10-21)

- **The share stays at 8 gold a year, with the three-years-away rule.** Approved after a comparison with vanilla: the share is about the tax of a tier-3 temple building, a little above a major court position's salary.
- **The Lady beside the god stays at 1119** (SITI 118; Orr p. 17).
- **The Śvetāmbara door is built (option a)**, as tm_ml2.0031 option d and tm_ml2.0032. How it keeps writing rule 7 is in §4b.

## Dates

| Feature | Earliest supported date | Source | Gate used |
|---|---|---|---|
| Share granted by a lord | c. 1014 (Rājarāja's royal settlement at Thanjavur); temple women hold land and give from 850 | SII 2 no. 66, ¶1; Orr 2000, pp. 65–73 | Any date. Chance halved (4 → 2) in 985–1070, the trough when Thanjavur "may have emptied nearby temples of temple women for a century" (Orr pp. 42–46, 141–42, 163–64). +4 in 1070–1300. |
| Share bought by the woman (0001 options b and c) | 1070: the first of the 21 "deals", gold for an honour (Orr pp. 74–75) | Orr pp. 74–75, 151 | `current_year >= 1070`. A lord who is herself a daughter is offered the event only from 1070, since she can only buy. |
| Share passes to her daughter ("to her descendants") | 1070: ten of the 21 deals (all 1070–1300) are hereditary (Orr pp. 75, 151) | Orr pp. 74–75, 151 | `current_year >= 1070` in `tm_ml2_pass_share_effect`. Before 1070 it passes only by the women of the street's choice, after Thanjavur's rule that with no qualified relations the other incumbents choose (SII 2 no. 66, ¶1). Thanjavur itself says "nearest relations", but it was a royal exception that failed (Orr pp. 161, 163–64), and it is not the women's own grant; the design reads the pre-1070 share as the temple's, not the family's. |
| Gift: a lamp | 850: temple women's gifts are recorded from the start of Orr's data (for example, in 875 a woman of Srirangam gave a lamp at Tiruverumbur; SII 13.88, Orr pp. 65, 142) | Orr pp. 65–66 | Any date. Chance 10, −5 in 985–1070, +5 in 1070–1300, −5 from 1300. |
| Gift: a feeding house in her name | Gifts of food offerings from 850 (Orr pp. 65–66); the named feeding house is 1118 (Cattankaitoli, Kanchipuram; p. 138) | Orr pp. 65–66, 138 | Any date (a food gift; the 1118 case is the model, not the first). |
| Gift: set up the Lady (*nācciyār*) | 1119: a temple woman sets up the "Queen of the Bedchamber" (SITI 118; Orr p. 17). Such shrines spread in the 13th century (p. 24) and in 1178–1300 (regional dossier §1) | Orr pp. 17, 24, 60, 74 | `current_year >= 1119`. (The coordinator suggested c. 1150 or 1178; 1119 is the earliest dated case in the notes. Raise to 1178 if the user prefers the "spread" date.) |
| She of the Illustrious Staff (*talaikkōli*) | Staff rite: 12th c. (*Uttara-Kāmika*; Goodall pp. 110–12). The title: Orr pp. 60–61, **date unverified** in the notes. One bearer's title-element, *Mummuticolat-talaikkōli* (Orr p. 56), is built on Rājarāja I's title Mummuḍi-Cōḻa, which may point to c. 1000; unverified, needs the book. | Goodall pp. 110–12; Orr pp. 56, 60–61 | `current_year >= 1100` (event trigger, and the chain from 0010). Marked unverified. |
| Food and Clothing (Hindu law) | Manu is far older than the period | `comparanda_reading_list.md` lines 940–941 | Any date. |
| Of the Third Feeling (Jain) | Jain *veda* doctrine is older than the period (Zwilling and Sweet pp. 112–16) | as cited | Any date. |
| The Order's Terms (Śvetāmbara door) | The "expedient admission" of skilled or well-connected candidates: Zwilling and Sweet p. 122 give no date for it; the Niśītha Bhāṣya rule on ordaining 6 of 16 types (n. 80) is a commentary of uncertain date (unverified in the notes) | Zwilling and Sweet 2000, p. 122 | Any date; needs `rite:svetambara`. |
| The Reciter: Kāraikkāl Ammaiyār | *Periya Purāṇam*, under Kulōttuṅga II (r. 1133–50) | Pechilis 2012, pp. 12, 202 | `current_year >= 1135`. |
| The Reciter: Basavaṇṇa's sayings | Basavaṇṇa d. c. 1166/68; his community "probably the span of one generation" | Ramanujan 1973 | `current_year >= 1160`, Kannada lord. |

**"Daughter of God."** *Tēvaṉār makaḷ* is 17 uses in 850–985, five in 985–1070, then one each in 1070–1178 and 1178–1300 (Orr table 2.5, p. 52). None of the tm_ml2 loc uses the title. One line in 0011 said Śiva's watchman named "the god's daughters" (Goodall's 12th-c. "daughters of Rudra", not the inscriptional title); it now says "the women of the god's temple" to avoid any echo. The stage-1 trait and clergy title "Daughter of God" are outside these files; the regional dossier suggests the narrator call it an old Śaiva honorific the faith revives after 985 (§1 item 4).

**1178 hooks (notes only, not built).** From `docs/later_starts.md` and the regional dossier §§1–3:
- **Takkolam as a temple holding.** b_takkaloma, in c_kanchipuram, is a *tēvaṉār makaḷ* cluster and the site of the one attested mother-to-daughter title, Kumarati-nankai (Orr pp. 58, 149–50). A 1178 start would seat an elder daughter there as a temple barony instead of Candragiri, since Kulottunga III holds both counties. A share in c_kanchipuram would then sit beside a Garland holding.
- **Buy a Verse at Nallur and Tirupampuram.** Temple women bought the singing of *Tiruvempāvai* verses at Nallur in the 12th c. (ARE 1940–41 nos. 143–176; Orr pp. 56, 105–08) and at Tirupampuram in 1213 (pp. 17–18). `tm_kovil` already sells the verse; a 1178 start could name these towns in its text.
- **The araiyar men's stage, as a dissent event.** The *araiyar* perform the girl's part, men only, attested by 12th-c. anecdote (Narayanan 1994, pp. 123, 126, 132). The faith's grievance, in its own voice: the temple lets a man play the girl but will not let the girl in. Never cast the *araiyar* as the faith's institution (faith page, "What it leaves out").
- **The sectarian squeeze on women's titles.** Men of status become *mahēśvara*, *śivabrāhmaṇa* or *śrīvaiṣṇava*, groups that shut women out, while *tēvaraṭiyār* becomes a woman's word (Orr pp. 55–56). In 1178 the Garland's "both temples" stance is provocative; a reaction event could have both sides call the street's double allegiance treachery.

**Variables.** Character: `tm_ml2_share` (the county title of her share), `tm_ml2_away` (years away, 0–2), `tm_ml2_gifts` (count), `tm_ml2_ruled_on` (0030 done), `tm_ml2_veda_ruled` (0031 done). County: `tm_ml2_street` (a temple street; the county modifier is added once). The older county mark `tm_temple_street` (set by `tm_kovil.0001` option c and `tm_garland.0020`, read nowhere until now) counts as a street in `tm_ml2_street_trigger`.

---

## 1. A Share on the Temple Street (drafted)

**What the player sees.** A Hindu lord (any Hindu faith, the Garland's own rulers too) with a daughter of the Garland at court who holds no share may get *A House on the Temple Street* (tm_ml2.0001). The text says the Brahman accountants of the temple would write the share in her name, not his.
- **Grant her the house and the share.** 60 gold from the lord, +15 piety; she gets the share in his capital county and +20 opinion of him.
- **She can buy it from her own purse.** She pays 40 gold. Shown only if she has it, and only from 1070.
- **Buy it in my own name.** Shown when the lord is herself a daughter of the Garland: 40 gold, from 1070.
- **Not now.** −5 opinion from her.

Holding a share gives *A Share on the Temple Street* (+0.1 piety, +0.1 prestige a month), and once a year, through her host's pulse, **8 gold while she lives in the county of the share**. The county gets the modifier *A Temple Street* (+5% development growth), once.

When she dies, the share passes. **From 1070** it goes "to her and her descendants": to her eldest daughter of the Garland, born or taken (`ordered_child`, so *Take as Daughter* counts). **Before 1070, or with no such daughter, the women of the street choose**: a random adult daughter of the Garland without a share who is in a province of that county. She gets *To Her and Her Descendants* (tm_ml2.0003), with one text for a child and one for a woman the street chose.

If she has been away from the county at three yearly checks in a row, the share passes the same way while she lives, and she gets *For Those Who Do the Work* (tm_ml2.0004). If no one takes it, it goes back to the temple. The county keeps its temple-street modifier.

**Why this gives a landless faith a base and a reason to stay.** The share is her own gold, under her own control, and it is tied to one county. A daughter who stays where her share is grows a little richer every year, and that gold pays for the gifts in feature 2. A county where shares are held becomes a temple street, which is visible on the map, grows a little faster, and gives the host a small reason to keep her. The share outlives her and stays in the faith.

**Mechanic.**
- Fired from `tm_ml2_yearly` for a Hindu lord with a capital county. Base chance 4%, −2 in 985–1070, +4 if the capital county is already a street, +4 in 1070–1300. Flavour budget on the lord.
- Payment and absence: `tm_ml2_share_year_effect` on the lord and on `every_courtier` with a share. "In the county" is `location.county ?= var:tm_ml2_share`. Not budgeted (no event unless the share passes).
- Death: `tm_ml2_on_death` skips bodies left at re-embodiment (`tm_reborn`), like `tm_kovil_on_death`.
- AI: grant 30 (+20 generous, +10 zealous, −20 greedy); she buys 30; not now 20 (+20 greedy).

**Sources.**
- The share: one share is the produce of one *veli*, 100 *kalam* of paddy a year, with a house on a named temple street; if she died or left, her "nearest relations" received it and did "the work"; with no relations, the other incumbents chose a successor (SII 2 no. 66, ¶1; `research/ind_tanjavur_inscription.md`, lines 14–16).
- Wealth under their own control; female-led families; merit of gifts passed to daughters, never to men (Orr 2000, pp. 72–73, 82, 153–58; `ind_orr_temple_women.md` §2.3).
- Hereditary grants "to her descendants" (*santanapravesam*): Orr 2000, pp. 75, 151.
- Era: the women grow richer in the 12th–13th centuries; they stop giving after 1300 (Orr 2000, pp. 46, 67–73, 174–77).

**How it respects the rules.** The narrator says what the inscriptions say (shares, houses, "the work", Brahman accountants: caste stays visible). Inheritance by an adopted daughter stays a marked reconstruction, as on the faith page (Orr's "may have", p. 72; adoption is her guess, ch. 3 n. 28, p. 228). The Thanjavur order gives "nearest relations", not daughters, so "the women of the street choose" is closer to the record than the daughter-first rule. No size cap; the gold is small.

**Open questions.**
1. *Decided (user, 2026-10-21):* three years away stays. The record says "died or left" (¶1); three years is design.
2. *Decided (user, 2026-10-21):* 8 gold a year stays (about a tier-3 temple building's tax, a little above a major court position's salary).
3. Should a lord of another religion (Jain, Buddhist, Muslim) ever grant shares? Drafted for Hindu lords only.

## 2. A Gift in Her Own Name (drafted)

**What the player sees.** A daughter of the Garland with at least 30 gold of her own, wherever she lives, may get *A Gift in My Own Name* (tm_ml2.0010). The masons will cut the gift in the temple wall under her own name; the priests will set it below the grants of kings.
- **A lamp to burn before the god.** 30 gold. +30 piety; *Her Name in the Temple Wall* (+0.2 prestige a month) for 10 years.
- **A feeding house that bears my name.** 80 gold. +50 prestige; the modifier for 20 years; her lord (if she has one) gains +15 respect for her.
- **Set up the Lady beside the god.** From 1119. 150 gold. +50 piety; the modifier for 20 years; **a share in that county if she has none**; and, if she is not yet one, the staff title follows (feature 3).
- **Keep my gold this year.**

Each gift marks the county where she lives as a temple street. A playable daughter can also give when she chooses, with the decision *Give to the Temple in My Own Name* (gold ≥ 30, 5-year cooldown).

**Mechanic.** From `tm_ml2_yearly`: the lord or a courtier who passes `tm_ml2_donor_trigger` and the flavour budget. Chance 10%, −5 in 985–1070, +5 in 1070–1300, −5 from 1300. Budget spent on the donor. AI: lamp 30; feeding house 20 (+15 generous); the Lady 25 (+15 zealous, +10 if she has no staff); keep 20 (+30 greedy). Decision AI: only with 100 gold or more, base 10.

**Sources.**
- Gifts of the same kinds as other donors': lamps, food offerings, land, gold, images (Orr 2000, pp. 65–66).
- Cattankaitoli, a Vaiṣṇava temple woman at Kanchipuram, endowed a feeding house named after herself (1118; Orr 2000, p. 138; `ind_orr_temple_women.md` §5).
- Pillaiyar Cirritai Arivai bought five plots, one from a Brahman woman, for a garden for the goddess at Chidambaram (c. 1250; pp. 69–70).
- Setting up a goddess (*Nacciyar*) beside the god: SITI 118 (1119), NK 134 (1213), TAS 6.15 (1252) (Orr 2000, pp. 17, 74). Nakkan Centalvi built and endowed a goddess shrine and received shares (*panku*) from the priests (ARE 468 of 1916; p. 60). That is why the Lady brings a share.
- Temple women's gifts went to medium-sized temples more than royal ones (pp. 80–82). Not modelled; see the open questions.

**How it respects the rules.** The gift is hers and the name is hers. The narrator does not call her a temple woman. "The priests will set it below the grants of kings" keeps caste and rank visible without a golden past. The Lady here is the consort goddess the inscriptions name; the Garland's daughters are not "the Lady" and not brides of God.

**Open questions.**
1. Overlap with `tm_kovil` (an honour for a gift) and `tm_garland.0020` (a ruler's inscribed gift). Should 0020 be folded into this event for rulers, so a Garland ruler sees one gift event and not two? See "Changes to existing files".
2. Orr says royal temples gave women less. Should a gift be worth less in a capital that is a holy site or a ducal capital? Not drafted.

## 3. She of the Illustrious Staff (drafted)

**What the player sees.** After she sets up the Lady, from 1100 (unverified, see Dates), *She of the Illustrious Staff* (tm_ml2.0011) follows in 20 to 40 days. The temple will give her the title *talaikkōli*. The Ādiśaiva priests say the staff is theirs to lay and ask a fee. The women of the street say Śiva's watchman lent his staff to name the women of the god's temple, and they can lend it again.
- **Pay the priests' fee, and have it cut in stone.** 25 gold. +50 prestige; the modifier *She of the Illustrious Staff* (+0.2 prestige, +0.2 piety a month, +1 diplomacy); and the nickname **"of the Illustrious Staff"** if she has no nickname yet.
- **Let the eldest of the street lay the staff.** +30 piety, −10 stress; the same modifier, but no nickname (the priests do not cut it in stone).

The nickname is the point for a landless daughter: her standing shows on her name wherever she goes.

**Sources.**
- *Talaikkōli*, "she of the illustrious staff", borne only by temple women, often joined to a god's name (Orr 2000, pp. 60–61; `ind_orr_temple_women.md` §2.1).
- The *Uttara-Kāmika* rite: Śiva borrows Nandin's staff and touches each woman on the head; *śirodaṇḍinī* translates *talaikkōl* (Goodall 2018, pp. 110–12; `ind_goodall_rudraganikas.md` §2.4).
- The priests' fee and the Ādiśaiva monopoly: the guru "must be an Ādiśaiva and must have received a fee of five *niṣkas* or more" (Goodall 2018, p. 132 n. 56). The faith refuses to adopt the fee and the monopoly (note §3 item 2), so the faith's own option is the street's elder; the priests' option is the world's price.
- The faith's line, "Śiva's watchman lent his staff to name the daughters; we borrow it back", is the Goodall note's suggested faith-voice text (§4).

**How it respects the rules.** Rule 7: the title is a standing that is not holy office, earned by a gift. No name-giving rite is attested before the 15th century (Orr 2000, p. 148), so the faith page already marks the staff rite as reconstruction; this event is the temple's title, not the gate. No dance, no "classical" dance terms (rule 11). The loc avoids the courtesan frame of Goodall's texts.

**Open questions.**
1. Should a staff-holder be preferred as the elder of the pāvai vow, with a small bonus at `tm_garland.0001`? That needs changes to existing files (below).
2. Should the nickname carry a god's name, as the inscriptions do ("talaikkōli of the Lord of X")? It would need one nickname per god or a dynamic name, so it is left plain.

## 4. Reaction layers (drafted; one part specified only)

### 4a. Food and Clothing (Hindu)

**What the player sees.** A Hindu lord not of the Garland whose own adult child is a daughter (any gate) may get *Food and Clothing* (tm_ml2.0030). His pandit has read the law books over her: to him she is "a man in the form of a woman", whom the law bars from inheritance and the rites, owed only food and clothing. Her friends answer that the law books also let a father appoint a daughter as his heir.
- **Food and clothing, as the law books say.** +25 piety; she gets the vanilla trait *Disinherited*; −40 opinion of him; he pays her 30 gold if he has it.
- **An appointed daughter. She stays my heir.** −15 piety; +25 respect from her.
- **A share on the temple street, in her own name.** Only for a daughter of the Garland without a share, and a lord with 60 gold and a capital. +10 piety; she gets a share in his capital; +15 opinion.

Once per child. Budgeted on the lord; chance 6%. AI: law books 30 (+30 zealous, −20 cynical, −20 if he likes her at 50+); appointed daughter 25 (+20 compassionate, +20 if he likes her); share 25 (+15 generous).

**Sources.** Manu 9.201 bars "the impotent [*klība*] and the outcast" from inheritance, and 9.202 asks heirs to give them food and clothing (`research/comparanda_reading_list.md`, South Asia, lines 940–941; Zwilling and Sweet 2000, p. 121, in `sea_zwilling_sweet_third_sex.md`). The pandit's phrase follows the note's "a man in the form of a woman" (after Maitrāyaṇī Saṃhitā 2.5.5; `sea_zwilling_sweet_third_sex.md` §4). The appointed daughter is the *putrikā* (Pechilis and Raj 2013, p. 54; `ind_pechilis_karaikkal.md` §2.5). Olivelle's *Manu* (2005) is listed in the reading list but not yet read: the verse numbers come through the notes, page unverified.

**How it respects the rules.** The hostile reading is the pandit's, a speaker at a vanilla Hindu court. The narrator never calls her a klība; the word itself is not in the loc. Disinheritance is attributed hardship, not the faith's view. The share option links the reaction to feature 1.

**Open question.** Is *Disinherited* too heavy for a flavour event? It removes her from succession for good (as vanilla's interaction does). A lighter version would be an opinion malus from his same-faith vassals, as the Zwilling and Sweet note proposed.

### 4b. Of the Third Feeling (Jain)

**What the player sees.** A Jain lord (`faith:jain_faith`) with an adult daughter (any gate) at court may get *Of the Third Feeling* (tm_ml2.0031). A monk says his law judges by desire, not the body, that hers "burns like a city on fire", and that the Order will not house her. She has not asked the Order for anything; she lives in the lord's hall.
- **The monk speaks for the Order.** +15 piety; −15 opinion from her.
- **The Order's rule is for the Order. My hall is mine.** +15 prestige, −10 piety; +20 respect from her.
- **Let it lie.** +5 stress.

Once per daughter. Budgeted; chance 5%. AI: monk 35 (+25 zealous); hall 30 (+20 just, +10 compassionate); let it lie 20.

**Sources.** Jains replace *liṅga* with *veda*, sex as desire; napuṃsaka-*veda* burns "like the conflagration of a great city" (Zwilling and Sweet 2000, pp. 112–13; `sea_zwilling_sweet_third_sex.md` §1, and the monk's line in §4). Vanilla Jainism in 1.20 is one faith, `jain_faith`, with the rites `digambara` and `svetambara` (checked in `common/religion/faith_types/00_faith_types.txt` and `history/provinces/k_gujarat.txt`).

**The Śvetāmbara door (drafted; user decision 2026-10-21).** A fourth option in 0031, shown only when the lord's rite is `rite:svetambara` and the daughter has stewardship or learning ≥ 12: **"The Order's own rule admits the skilled. Admit her by it."** +10 prestige for the lord. AI 30 (+15 just, +10 diligent). It sends her *The Order's Terms* (tm_ml2.0032) 3 to 7 days later, as a chain under way (no budget):
- **"I will take the place. Write down that I am a woman, not a skill."** *Admitted on the Order's Terms* (+0.1 prestige a month, 10 years; no skill bonus); +5 stress; the lord +10 respect. AI 40 (+20 ambitious, +10 content).
- **"Keep the place. I did not ask the Order to let me in."** +20 piety, −5 stress; the lord −10 opinion of her. AI 30 (+20 stubborn, +20 zealous, +10 arrogant).

Source: candidates were admitted "when they were known to be socially well-connected, or if they had special expertise in an area such as medicine or administration" (Zwilling and Sweet 2000, p. 122; `sea_zwilling_sweet_third_sex.md` §1). In the source this is admission to the Order (ordination); the game applies the Order's rule to a lord's household, which is design. Digambara lords get no such option.

**How rule 7 is kept.** The rule ("no text says they are accepted for a sacred role or for being useful") is about endorsement. Here usefulness is the condition of a vanilla institution, spoken by the monk and the lord (0031 option d names it as "the Order's own rule"). The narrator never says it. The faith answers in her own voice and rejects the terms: "The women of the street are not women because they are useful, and they do not stay where they are welcome only for their use." Both of her options name the condition. Taking the place costs stress, and the modifier gives no skill bonus, so the game does not reward the condition either; refusing is honoured with piety, as rule 23 asks for stepping back.

## 5. The Reciter (drafted)

**What the player sees.** A daughter of the Garland at a court whose lord is of `faith:shaiva_faith`, from 1135, may get *The Reciter* (tm_ml2.0040).
- At most courts: a reciter brings Cēkkiḻār's lives of Śiva's servants and tells of the merchant's wife of Kāraikkāl, who asked the Lord to take away the beauty she bore for a husband, was given the form she asked for, and was called Mother. The lord is looking at her.
- At a Kannada lord's court from 1160 (*A Singer of Sayings*): a singer brings Basavaṇṇa's sayings, where he wears men's clothes only for the Lord and will be the bride of the Lord's devotees. The narrator says that in his life it was a song and a rite; "the women of the Garland hear more in it".

Options: **the faith's word** (+20 piety, −10 stress): "She asked, and was given the form she asked for." / "He wore them only for the Lord. I have taken mine off."; **reward the singer in her lord's hall** (10 gold; the lord +15 grateful): the courtier's way to stand well with a Shaiva host; **listen, and keep it to herself** (−15 stress). Budgeted on her; chance 6%. AI: faith's word 40 (+20 zealous); reward 30 (+20 generous, −20 greedy); listen 20 (+20 shy).

**Sources.**
- Kāraikkāl Ammaiyār: *Periya Purāṇam* (under Kulōttuṅga II, r. 1133–50), vv. 49–50 and 58, the self-requested change and "Mother" (Pechilis 2012, pp. 202–04; `ind_pechilis_karaikkal.md` §2.1–2.2). The faith claims the pattern, not the saint (faith page; note §4.1); the option line is the note's suggested faith line (§4.4).
- Basavaṇṇa, vacana 703 (Ramanujan 1973; verified in `ind_ramanujan_bhakti.md` §2); his community at Kalyāṇa, d. c. 1166/68. Ben-Herut: the bride role in Harihara is liturgical; "voice and rite, not life" (Ben-Herut 2018, pp. 85–88; `ind_benherut_sivas_saints.md` §3 item 5). The faith's answer that the clothes "can be taken off" is the Ramanujan note's design line (§2, "For the design").

**How it respects the rules.** The narrator never claims Kāraikkāl Ammaiyār or Basavaṇṇa; the faith speaks in the option. The Garland is not cast as Vīraśaiva or Liṅgāyat (no such words appear). No death-wish lines; the bride is the devotee, not a temple woman; the bridegroom is neither jealous nor punishing (rule 26).

**Open questions.** Should the Kannada variant need `faith:shaiva_faith` too, or any Hindu Kannada lord? Should a Vaiṣṇava court get a counterpart (the Mārkaḻi recitation; Narayanan 1994)? Not drafted.

## Option, not built: the solitary Tai vow

The user left this "either or". Hardy keeps the Mārkaḻi and Tai baths apart (Hardy 1983, p. 512); NT 1 runs through Tai and Māci, addressed to Kāma, with *kōlam* on the street, a sunrise bath and one meal a day (p. 418 and n. 18), and is solitary where Mārkaḻi is kept with friends (`ind_hardy_viraha_bhakti.md` items 3 and 5). As an option it would be a decision open in Tai (mid-January to mid-February) for a daughter who kept the Mārkaḻi vow, at Kanchipuram, with no gate effect: piety and stress relief, and the dream moved here. The Tai bath asks for "rain and a husband" (p. 512), so the text would need care with rule 26. Not built.

## Changes to existing files (not made; for the user to decide)

1. **Fold `tm_garland.0020` into tm_ml2.0010 for rulers** (`common/on_action/tm_on_actions.txt`, `tm_yearly_south`): remove the `tm_garland.0020` block, or make it require `NOT = { has_variable = tm_ml2_gifts }`, so a Garland ruler does not see two gift events.
2. **Prefer a staff-holder as the vow's elder** (`common/scripted_effects/tm_rite_effects.txt`, `tm_pavai_begin_effect`): before `random_courtier` for an elder, try one with `has_character_modifier = tm_ml2_staff_modifier`. In `events/tm_garland_events.txt`, `tm_garland.0001`, add `modifier = { add = 10 scope:tm_garland_elder = { has_character_modifier = tm_ml2_staff_modifier } }`.
3. **The growth call notices temple streets** (`common/scripted_effects/tm_growth_effects.txt`, the contact modifiers): add `modifier = { add = 3 location ?= { county ?= { tm_ml2_street_trigger = yes } } }`. This makes a street a contact point for the call, like a Sisters' House (+5). Modest.
4. **`tm_kovil` honours could also pass to a woman the street chooses** (`common/scripted_effects/tm_kovil_effects.txt`, `tm_kovil_pass_on_effect`): with no heir, pick as `tm_ml2_pass_share_effect` does. Optional.
5. **Docs**: add stage-2 rows to the faith page's "From source to mechanic" table and a TO-TEST section once the user approves.

## Survival balance: ideas only (not built)

- Shares are the anchor: a daughter with a share is less likely to wander. If the AI moves courtiers away anyway, consider a small opinion bonus from a shareholder to a host whose capital holds her share, so she does not leave the court.
- The women of the street choose a successor only among daughters already in the county. If none, the share lapses. A later rule could let the street adopt a newcomer (an arrival) into an empty share, which would turn shares into a slow pull for arrivals at street counties.
- A Garland republic or mercenary band with a capital could hold several shares in one county; count streets per county in the census (`tools/census_report.py`) to see whether streets form.
- The host's +15 opinion from a feeding house or a rewarded singer may be enough to stop dismissals; check in an observe run whether Garland courtiers are being dismissed or are dying out.

## Uncertain syntax (check in game)

- `location.county ?= var:tm_ml2_share` as a scope comparison in a trigger (vanilla compares `activity_location.county = title:…`, so it should work).
- `random_character_in_location` inside `every_county_province` to let the street choose (the docs list `any_character_in_location` on provinces; the `random_` form is assumed).
- `clear_saved_scope` inside a scripted effect run from `every_courtier`, to stop a saved heir leaking between two shares passed in the same pulse.
- `ordered_child` counting adopted daughters (as `tm_kovil_pass_on_effect` assumes).
- Courtiers with gold: AI courtiers seldom hold gold, so feature 2 depends on feature 1's yearly pay. Watch whether gifts ever happen.

## Test scenarios (for TO-TEST.md)

1. Kanchipuram start: give a daughter of the Garland at a Hindu court 100 gold; fire tm_ml2.0001 on the lord; check the share, the county modifier, and 8 gold a year.
2. Move her to another court; after three pulses, check tm_ml2.0004 and who gets the share.
3. Kill a shareholder with an adopted daughter; then one with no daughter but another daughter of the Garland in the county; check tm_ml2.0003's two texts.
4. Fire tm_ml2.0010, choose the Lady; check the share, the staff event, and the nickname with and without the fee.
5. Fire tm_ml2.0030 on a Hindu lord with a daughter child; check each option, and that it never fires twice for her.
6. A Jain lord and a Shaiva lord (Kannada culture after 1160, Tamil after 1135); check tm_ml2.0031 and both texts of tm_ml2.0040.
7. A Śvetāmbara lord (`rite:svetambara`, e.g. in Gujarat) with a daughter at court with stewardship 12 or more: fire tm_ml2.0031; option d shows; tm_ml2.0032 reaches her; check both answers. Repeat with a Digambara lord and with a daughter whose stewardship and learning are under 12: option d must not show.
8. Before 1070: kill a shareholder who has an adopted daughter; the share must go to a woman the street chooses, not to the daughter. Fire tm_ml2.0001 before 1070: the "buy" options must not show.
