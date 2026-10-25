# Wave 3: Adelphai Dorleyaiou, stage 2

Prefix `tm_dl2_`, namespace `tm_dl2`. Roadmap item: "the Galenic splinter rite; more events from the reading (Ignatios, the Tarsus boy-train)". Untested in game.

## What was built

### 1. The Galenic rite (`tm_galenic_rite`)
- **Rite type** in `common/religion/rite_types/tm_rite_types.txt`: faith `transbian_maximalism`, `create = no`, `convert = yes`, the main rite's three tenets and doctrines with `tm_body_galenic` in place of `tm_body_aristotelian`. Not on the map at the start.
- **How a ruler gets it.** 1.20 has no vanilla decision that changes rite inside a faith. Rites change through the conversion screen, `create_dynamic_rite` / `create_rite_from_type` (heresy outbreaks; the historical characters who found daoxue and quanzhen) and `set_character_rite`. The mod follows the daoxue/quanzhen pattern: `create_rite_from_type` once, behind a global variable, then `rite:tm_galenic_rite`.
  - **Found the Galenic Rite** (`tm_dl2_found_galenic_decision`): a landed Dorleyaian of the main rite who is not the Mother of Mothers, from **886** (Leo VI, 886–912; Novel 98). Costs 300 piety and 150 prestige. It creates the rite, converts her, copies her old rite's House of the knife onto the new rite, and moves her capital county to the new rite if its people are of the faith. Then event `tm_dl2.0001`.
  - **Join the Galenic Rite** (`tm_dl2_adopt_galenic_decision`): once it exists. 150 piety.
  - **Return to the Rite of Dorleyaion** (`tm_dl2_return_aristotelian_decision`): 100 piety. The Mother of Mothers gains +15 "Came Home to the Mother House". Stepping back is honoured (writing rule 23).
  - On founding or joining: a liege of another Christian faith gains +15 "Counts as the Emperor Counts" (10 years). The Mother of Mothers, if she keeps the main rite, gets `tm_dl2.0002`: "the old cage with a new name" (mutual −20, 10 years; +50 piety) or "she is still our sister" (+10 stress).
  - AI: only rulers whose liege is of another Christian faith, checked every 120 months, weight 0 + 10 under any suppression rung + 10 at the third rung + 5 content/craven; zealous and daughters −50. Rare by design.
- **The doctrine's modifier** (`tm_doctrine_types.txt`): `tm_body_galenic` now gives `different_faith_liege_opinion = 10` and `monthly_piety_gain_mult = -0.05`. The wing of accommodation: lieges find it easier, the Houses find less to pray for. The comment no longer says "beloved of the angels".
- **The heresy laws** (`events/tm_byzantine_events.txt`): a Galenic answer at two rungs.
  - `tm_byz.0010.e` (the books): show the Emperor's own count. −25 piety, liege +10.
  - `tm_byz.0012.e` (the wills): register the adoptions under Leo's adoption law and enter each daughter as a eunuch. Free; sets `tm_wills_registered`; each daughter who is the ruler's child gains −15 "Registered Me as a Eunuch".
  - `tm_byz.0001.b` (Cybele in Christian clothes) existed already and is now reachable.
- **Its book** (`tm_dl2.0030`, from 1107): Theophylact of Ochrid's *In Defence of Eunuchs*. Galenic rulers: "This is our book" (+50 piety, learning xp). Aristotelian rulers: "The archbishop defended the uncle. No one asked the boy." A learned ruler of either wing can shelve it with the answer beside it. Yearly 2%, +8% for Galenic rulers, +2% at learning 12. Once per ruler.

### 2. Events from the Byzantine reading (`events/tm_dl2_events.txt`, hooks in `common/on_action/tm_dl2_on_actions.txt`)
- **Ignatios returns** (`tm_dl2.0010`). 867 start only, around 20 November 867. To the Mother of Mothers (or the greatest ruler of the faith) and every human player of the faith. Options: "so long as it may call him father" (Aristotelian); "the court cuts its princes as we cut our captives" (Grandmother's House); "pray for him; he was Niketas once" (everyone).
- **The train to Tarsus** (`tm_dl2.0020`). Dorleyaian rulers with a capital in Asia Minor, while Cilicia's holder is Muslim, before 990. Yearly 4%, once per 20 years per ruler, on the flavour budget. One option per House:
  - Gift Alone (100 gold): buy them all free; those with a village go home; two cut boys and one uncut stay and are adopted; no one asks anything of them. +100 piety.
  - Aunt Bea's House: free the children and give the merchant a cell. The merchant is created greedy, Sunni, Levantine, and imprisoned. The House's intake rules then apply as usual: he can go to the knife only if he meets `tm_intake_eligible_trigger` (violent men only); the event does not make him eligible. +50 prestige; Cilicia's holder −15.
  - Grandmother's House (100 gold), the condemned way: pay the merchant for the cut ones and call them daughters; the rest go on to Tarsus. +10 dread. No uncut child is taken, and no cutting is shown.
  - Any ruler under a Christian top liege: send word to the strategos (50%: turned back to the coast, "where the boys go from there, no one says"; 50%: the strategos has his own price).
  - Past the Gates: +15 stress.
  - No child is cut, given a rite or given a name. Children are 8–12, Greek, raised in root's faith, adopted by root.
- **The Holy Mountain closes** (`tm_dl2.0040`). Once, 1083–1089, to the Mother of Mothers (or the greatest ruler) and every player of the faith. Aristotelian: "never our door"; Galenic: petition for the cut monks; with a House: take in turned-away monks (House strain +1); or "the Komnenoi have their kin".
- **The Steward at the Gate** (`tm_dl2.0050`). From 1120, rulers with a Sisters' House whose capital is in Asia Minor or south-eastern Europe. Yearly 2%, once per ruler, on the budget. A convent's eunuch steward, barred from the enclosure, asks for work: stay as a friend of the House (converts, `tm_house_friend_modifier`), or come in with the offer of the Hilaria and a name if she asks (`tm_offer_courtier_rite_effect`: the steward chooses), or bread for the road (sent to the pool).
- **The Consul's Letter** (`tm_dl2.0060`), Psellos. 1063–1078, landed Dorleyaian rulers. Yearly 3%, +7% for the holder of the Mother House, +2% at learning 12. Once per ruler, on the flavour budget. A copy of Psellos's letter reaches the Mother House. The desc paraphrases two dated letters: S 72 to the kaisar Ioannes Doukas (c. 1063–4), "with regard to nature I am feminine", and S 157 to Constantine, nephew of Keroularios (c. 1074), "more feminine or more masculine?". The narrator says he wrote it of his soul, to great men, in a learned style, and that each wing reads it its own way. It does not claim him or name what he was. Options: Aristotelian "He says it of his soul. We say it of our sisters." (+25 piety); Galenic "Even the consul of the philosophers is a little of a third thing." (+25 piety); anyone "Copy it for the library. Write beside it that this is our reading, not his word." (learning xp).

## Sources (by note)
- Novel 98, three *genê*: Sidéris 2010, p. 89 (`research/byz_sideris_eunuques_societe.md`); "some strange sex": Tougher 2008, p. 111 (`research/hist_tougher_eunuch_byzantine.md`). Leo VI 886–912: Neville 2019 #50; Tougher p. 29.
- Novels 26–27 (adoption): Macrides 1990, p. 111.
- Galen: only "some third thing", as a paraphrase. The renderings in `research/byz_galen_on_semen.md` are not verified against De Lacy.
- Theophylact: Mullett in Tougher (ed.) 2002, pp. 177–86 (date c. 1100–07; personal gift; asceticism, not gender); Tougher 2008, pp. 75, 98, 108; Ringrose 2003, pp. 195–97 (the nephew, "their own murderers"); `research/byz_tougher_eunuchs_antiquity_beyond.md` row 12 and quote list.
- Ignatios: Ringrose 2003, pp. 62, 118 (cut at 14; patriarch again from Nov. 867); Szabo in Spencer-Hall and Gutt 2021, pp. 117–25 (beardless in the mosaic, "father"); Tougher 2008, monastic name Niketas → Ignatios.
- Tarsus: Ayalon 1999, pp. 105–8, 218–19 (al-Jahiz; al-Muqaddasi: Rum eunuchs into Syria and the Jazira by purchase or raid, until the frontier fortresses fell); El-Azhari 2019, pp. 143–45, 254 (Byzantium as a castration centre; eunuchs at three or four times the price); event shape from `research/isl_el_azhari_queens_eunuchs.md` row 2.
- Athos: Guilland 1943, p. 232 (1083); Tougher 2008, p. 75 (beardless and eunuch bans); "the new dynasty prefers kinsmen": `research/byz_ringrose_perfect_servant.md` row 7.
- Steward: Kecharitomene [80], Thomas and Hero 2000, p. 710 ("closed even to eunuchs themselves"); [79]–[80] c. 1120/30 (Gautier); Guilland 1943, p. 205; `research/byz_thomas_hero_typika.md` row 6.
- Psellos: Jeffreys and Lauxtermann 2017, pp. 345 (S 72, c. 1063–4), 387 (S 157, c. 1074), 400–1 (S 180, weak date); Papaioannou 2013, pp. 195–209 (texts and translations), 202, 215, 231 (the persona reading), p. 11 (death likely 1078). `research/byz_psellos_papaioannou_letters.md`. Betancourt 2020, pp. 109, 112–13 quotes the same three letters.

## Date gates
| Content | Gate | Source of the gate |
|---|---|---|
| Found the Galenic Rite | from 886 | Leo VI's reign (Novel 98) |
| Ignatios | 867 start only, late Nov. 867 | Ringrose pp. 62, 118 |
| Train to Tarsus | before 990, while Cilicia is Muslim-held | al-Muqaddasi (d. c. 990): the trade stopped with the frontier fortresses |
| Theophylact's book | from 1107 | Mullett: written c. 1100–07 |
| Athos | 1083–1089 | Guilland p. 232 |
| Steward at the Gate | from 1120 | Kecharitomene [80], c. 1120/30 |
| The Consul's Letter (Psellos) | 1063–1078 | S 72 c. 1063–4, S 157 c. 1074 (Jeffreys pp. 345, 387); Psellos dies likely 1078 (Papaioannou p. 11) |

## Decisions taken
- One rite, three decisions (found, join, return), not a dynamic `create_dynamic_rite`: the rite needs its own name and fixed doctrine.
- The Galenic rite keeps the founder's House of the knife; only the body doctrine differs. The wings split on what the cut are, not on who may be cut.
- The Mother of Mothers cannot take it. The Mother House stays the main rite.
- The Galenic gain is peace with lieges (opinion, the cheap wills option); its costs are piety and the daughters' names in the register. It is not a free upgrade, and nothing calls it the better road.
- Under Grandmother's House the train option buys only the children already cut and lets the rest go on. That keeps the condemned way condemned without new harm to a child on screen.
- The Tarsus merchant is not made violent by the event; the Dorley prisoner rules decide.

## Uncertain syntax and behaviour (check in game)
- `create_rite_from_type` on a rite type with `faith =` and `create = no`: the doc says names and icon are generated "dynamically" from faith and founder. Expect "Galenic Rite" from the type's `name`; vanilla daoxue/quanzhen suggest so. Check the name, colour and icon.
- `convert = yes` inside `create_rite_from_type`, and whether `change_rite_doctrine` on the new rite works the same tick.
- `set_character_rite_with_conversion` ("if they can"): check it converts a landed ruler with no further piety cost, and that `faith.main_rite` resolves for the return.
- **Tenet `is_shown`** (not my file): the three Dorleyaian tenets show only for `faith:transbian_maximalism` or `rite:transbian_maximalist_rite`. On the Galenic rite they are scripted core tenets, so they should hold, but the reform screen may hide them. Check; see the change request below.
- `different_faith_liege_opinion` is read as "a liege of another faith's opinion of me" (vanilla pairs it with `opinion_of_different_faith_liege` in 00_tenet_types.txt).
- `on_game_start_after_lobby` with a delay of 323 days lands on 20 November 867 for the 867.1.1 start.

## Test scenarios (TO-TEST style)
- **Found the Galenic Rite.** Play a Dorleyaian count under an Orthodox liege, set the date past 886. The decision shows (not for the Mother of Mothers). Take it: the rite exists, you are of it, your capital county too if Dorleyaian; your House of the knife matches your old rite (try with Gift Alone); your liege has +15; the Mother of Mothers gets *A Sister Counts Three* within a month. The found decision disappears for everyone; *Join* appears for other Dorleyaians; *Return* appears for you. Return: back to the main rite, the Mother +15.
- **Before 886** the found decision does not show.
- **Heresy laws, Galenic.** As a Galenic ruler under an Orthodox liege, `event tm_byz.0010` and `event tm_byz.0012`: the Galenic answers show; at 0012, adopted daughter-children gain −15 of you and `tm_wills_registered` is set.
- **Ignatios.** New 867 game as any Dorleyaian player: *The Patriarch Without a Beard* arrives around 20 November 867, once, also to the Mother of Mothers. A later start never sees it.
- **Train to Tarsus.** Before 990, as a Dorleyaian ruler in Anatolia with Cilicia Muslim-held, `event tm_dl2.0020`. Only your House's option shows (plus the strategos under a Christian top liege, plus "past the Gates"). Gift Alone and Aunt Bea: three boys aged 8–12 (two eunuchs) adopted at court; Aunt Bea: a greedy Sunni merchant in your dungeon, and the prisoner interaction shows only if he happens to qualify. Grandmother: two eunuch boys, dread. Fires at most once in 20 years per ruler, not after 990, and not without a Muslim holder of Cilicia.
- **The book.** After 1107, `event tm_dl2.0030` as a Galenic ruler (option a) and as an Aristotelian (option b); learning 10+ adds option c. Once per ruler.
- **Athos.** Set the date to 1083 on an observe save: *The Holy Mountain Closes* fires once by 1090.
- **Steward.** After 1120, with a Sisters' House in Anatolia, `event tm_dl2.0050`: an Orthodox eunuch courtier appears; (a) converts and becomes a friend of the House; (b) converts and gets the courtier rite offer (tm_growth.0001); (c) sends the steward to the pool.
- **The Consul's Letter.** Set the date to 1070 as a Dorleyaian ruler of the main rite, `event tm_dl2.0060`: options a and c show, b does not. As a Galenic ruler: b and c. Check the text never calls Psellos a Sister or names what he was. Fires once per ruler; not before 1063 or after 1078; the Mother House's holder sees it more often in observe runs.
- **Budget.** With the rare flavour rule, Tarsus, the book and the steward never come within two years of another flavour event.

## Changes needed in files I do not own
1. `localization/english/tm_l_english.yml`, `tm_body_galenic_desc` paraphrases Galen beyond "some third thing" (the sow comparison), which the renderings do not support yet. Proposed replacement:
   ` tm_body_galenic_desc:0 "After Galen, the cut are some third thing, neither man nor woman. It is the rite that agrees with the Emperor, whose law counts three kinds of people: men, women and eunuchs. A third kind can be honoured, employed and kept apart, and it sits easier with bishops. The Aristotelians call it the old cage with a new name."`
2. `common/religion/tenet_types/tm_tenet_types.txt`, the three Dorleyaian tenets' `is_shown`: if the Galenic rite's tenets are hidden in game, add the Galenic rite on the rite side, guarded because the rite does not exist at the start, for example `OR = { this = faith:transbian_maximalism this = rite:transbian_maximalist_rite AND = { has_global_variable = tm_dl2_galenic_founded this = rite:tm_galenic_rite } }`. Only if the in-game check fails.
3. Optional, `common/on_action/tm_on_actions.txt` (the suppression ladder): if the Galenic wing should feel the laws less, multiply the 3% rung chance by 0.5 for `rite ?= { rite_has_parameter = tm_castrates_third_kind }`. Not needed for the feature to work.

## README text (ready to paste)
Roadmap line, replacing the Adelphai item:
`- [x] Adelphai Dorleyaiou: the Galenic splinter rite (found, join, return); Ignatios (867), the train to Tarsus, Theophylact's book, Psellos's letter (1063–78), the Athos ban (1083), the Steward at the Gate`

Replacement for "The schism to come" (README l. 166):
`- **The Galenic wing.** The main rite is Aristotelian: the cut body changes into the female condition. From 886 a ruler of the faith may found the Galenic Rite, the rite that agrees with the Emperor: Leo VI's law counts men, women and eunuchs, and the Galenic Sisters call the cut some third thing. It buys peace with Christian lieges and costs piety and the daughters' names in the register. Its book, from 1107, is Theophylact of Ochrid's *In Defence of Eunuchs*. The Aristotelians call it "the old cage with a new name"; a ruler may come home to the main rite.`

`docs/faiths/adelphai-dorleyaiou.md`, the "Galenic splinter (planned)" row: change "(planned)" to built, and the source cell to "Sidéris 2010, p. 89 (Novel 98); Mullett 2002, pp. 177–86 (Theophylact). Galen only as 'some third thing'."

## TODO text (ready to paste)
Under "Stage 2 inputs from the Byzantine reading":
```
- [x] Events: Ignatios returns as patriarch (867); Tarsus boy-train with options per knife house; Steward at the Gate; Athos closed to eunuchs (1083) (`tm_dl2`, wave 3)
- [x] Psellos's "feminine nature": The Consul's Letter, 1063–1078 (`tm_dl2.0060`; dates from Jeffreys and Lauxtermann 2017)
- [x] Galenic splinter rite: Theophylact's *In Defence of Eunuchs* as its book (`tm_dl2`)
```
New block:
```
## Adelphai Dorleyaiou stage 2 (wave 3, untested in-game)
- [ ] Galenic rite: name, colour and icon after create_rite_from_type; knife doctrine copied; tenets shown on the new rite
- [ ] Found / Join / Return decisions; the Mother's answer (tm_dl2.0002); liege opinion
- [ ] Galenic answers at tm_byz.0010 and 0012
- [ ] Ignatios lands in late November 867; Tarsus train gates (990, Muslim Cilicia); Athos once 1083-89; the steward from 1120; the Consul's Letter 1063-78
- [ ] Watch observe runs: how often the AI founds the Galenic rite (should be rare)
```

## Council of the Two Schools (built 2026-10-24, untested)
Files: `events/tm_dl4_events.txt`, `common/{on_action,scripted_effects,script_values,decisions,opinion_modifiers}/tm_dl4_*.txt`, `localization/english/tm_dl4_l_english.yml`, console helper `tools/run/tm_council_now.txt`.

- **When.** Ten years after the Galenic rite is founded, then at most every 25 years (15 after a broken council). Each year without a cooldown, a 10% chance that the Mother of Mothers (or the greatest ruler of the faith) calls it. A player of the faith may call it by decision (150 piety). Both wings need a landed adult ruler.
- **The motion.** The Emperor's third estate: its offices, its peace, its column in his register. No daughter's name is on the table (Serano row 18). The schools give their reasons with their proof-texts, GA 787b against *De semine* K IV 585 (Galen note row 4).
- **Who speaks.** The most learned landed ruler of each rite. The host may lean (+10). Each champion picks a proof: the school's text (adds learning), the polemic or the appeal to peace (adds diplomacy), or dated evidence (15: Athos 1083 and, from 1120, the Kecharitomene, +5, for the main rite; Theophylact 1107 for the Galenic). The benches' floor: 10, +3 a landed ruler of the wing, +10 for the main rite if the Mother of Mothers keeps it, +2 for the Galenic per landed ruler of the faith under a liege of another Christian faith.
- **The vote.** Weighted draw: main-rite score, Galenic score, and a fixed 15 for a broken council. Kept: 25 years of `tm_dl4_register_upheld` (AI joins the Galenic rite half as often, returns more often), and each landed Galenic ruler chooses whether to come home or keep the count. Allowed: 25 years of `tm_dl4_count_allowed` (+10 to the AI's join weight). Broken: mutual −20 between the champions.
- **Not built.** No fervor change: both wings share the faith's fervor. No faith split or expulsion: losing the vote never puts anyone out of the faith.

## The Galenic teacher (added 2026-10-24, untested)

Runs 11, 12 and 14 never founded the Galenic rite: the founding decision needs a landed ruler of the main rite who is not the Mother of Mothers, and the faith seldom has one. A second road now exists. Each year from 886 there is a 2 in 100 chance that a learned member of the faith on the main rite takes up Novel 98 (`tm_dl2.0003`). This can be a courtier, and lords, rulers under Christian lieges and content characters are favoured. Excluded: the Mother of Mothers, daughters, zealots, and anyone under learning 10. Writing the rite runs the same effect as the decision. Declining gives twenty quiet years. A courtier's rite has a handful of followers until landed rulers join it by decision. The council needs a landed ruler in each wing, so it waits until then.

### Champions need not be landed (2026-10-24, after run 15)

Run 15 (867–1210) founded the Galenic rite in 902 but never held a council: after 950 the faith seldom had more than one ruler, and the council wanted a landed ruler in each wing. Each school's champion is now its most learned adult, landed or not; a landed member is preferred (+5 in the order), and a higher title breaks ties (`tm_dl4_champion_trigger`, `tm_dl4_champion_value`). The host is still the Mother of Mothers or the greatest ruler of the faith; with no ruler at all, the main rite's champion calls the Houses herself. The decision's check follows the same rule. By 1210 the Galenic rite had no living members, so the wing can still die out; the teacher event only founds it once.
