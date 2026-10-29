# Bædling, wave 15: raising a níð-pole oneself, the Níð of the Land, and vows over the cup

Roadmap item (README, "Still to do"): "Bædling: raising a níð-pole oneself (a scheme with a proxy carver), the Níð of the Land, vows over the cup kept or broken". Built 2026-10-29 on branch `wave15-baedling-nid`, untested in game (`docs/TO-TEST.md` AR). Namespace `tm_bae6`.

**New files** (all with a BOM):
- `events/tm_bae6_events.txt`
- `common/schemes/scheme_types/tm_bae6_schemes.txt`, `common/schemes/agent_types/tm_bae6_agent_types.txt`
- `common/character_interactions/tm_bae6_interactions.txt`, `common/decisions/tm_bae6_decisions.txt`
- `common/scripted_effects/tm_bae6_effects.txt`, `common/scripted_triggers/tm_bae6_triggers.txt`
- `common/modifiers/tm_bae6_modifiers.txt`, `common/opinion_modifiers/tm_bae6_opinion_modifiers.txt`
- `common/on_action/tm_bae6_on_actions.txt`, `localization/english/tm_bae6_l_english.yml`

**One-line edits to existing files** (the two doors to the vow):
1. `events/tm_bae5_events.txt`, `tm_bae5.0020` (the bragarfull), option a: `tm_bae6_to_the_vow_effect = { DOOR = flag:bragarfull }`.
2. `events/tm_flyting_events.txt`, `tm_flyting.0020`, the cup option: `tm_bae6_to_the_vow_effect = { DOOR = flag:flyting }`.

**Shared files:** a "Bædling: wave 15" block in `tools/census_report.py`; section AR in `docs/TO-TEST.md`; a wave-15 section in `docs/TODO.md`; the README roadmap line and a paragraph in the Bædling section.

**Validation.** xTiger: 23 reports, the baseline, none in these files. `tools/check_glyphs.py`: silent.

---

## 1. Raise the Níð-Pole (scheme `tm_bae6_raise_pole`)

### Sources (the spec rows)

| Row | What it says | In game |
|---|---|---|
| Gade row 8 (`research/norse_gade_homosexuality_law.md`) | The blue hat on the pole is Óðinn's; a "burn the pole" option; "the faith can raise one too" | The faith's own pole. The target may burn it, and a target of the rite may answer "the hat is Óðinn's" |
| Gade row 9 | Níð has a material form, the pole as well as verse (p. 134). A hostile scheme ending in prestige loss and stress for the target | The scheme; on success the target loses medium prestige and gains 10 stress |
| Mitchell row 9 (`research/norse_mitchell_witchcraft_magic.md`) | Egill's pole turned toward the land (pp. 68–69). Gulaþing treats carved níð (*tréníð*) apart from spoken (*tunguníð*) (p. 71). Sverrir's Christian law: forfeiture plus confession, or exile (p. 164) | The pole faces his hall. Carved níð weighs more in the Account. Under the Christian law of Norway from 1270, the carver chooses forfeiture and confession, or exile (`tm_bae6.0030`) |
| Evans and Hancock row 3 (`research/norse_evans_hancock_masculinities.md`) | The pole shames the raiser too: onlookers judged that "neither" figure stood well (pp. 168–69). A proxy (court poet or craftsman, p. 181) takes the legal charge; the lord takes half the social cost | The carver is an agent; the charge at law is his. The raiser gets **Paid for a Níð-Pole** (−5% prestige gain, 5 years), half of `tm_bae5_nid_raised_modifier` |
| Evans and Hancock row 9 | Bishop Friðrekr answers níð with humility (p. 170): a Christian ruler's "turn it with humility" option | A Christian target may let it stand: +minor piety and prestige, nothing in the Account |
| Miller row 13 (`research/norse_miller_bloodtaking.md`) | Insults are "gifts" that demand repayment (p. 182); a raised pole adds to the Account | The pole is written through `tm_feud_wrong_effect`. Where his house owed hers, it is a requital |

### How it works

- **Who.** The owner is a ruler of the Bædling rite (`tm_bae6_pole_raiser_trigger`). She needs a carver at court: a grown man, free, not a ruler, not a daughter or Marked or declared woman (`tm_bae6_carver_trigger`). Without one the interaction is greyed out ("A grown man of your court … must carve it").
- **Whom.** A grown man (`tm_bae6_a_man_trigger`, see question 2) whose house owes hers a wrong in the Account (`tm_bae6_owes_trigger`, reading `tm_acc_1`), or her rival. Not her own house. One pole per target in five years (`tm_bae6_pole_cd`); the scheme's own cooldown is five years.
- **Agents.** The **Carver** gives success chance (learning, intrigue; a `lifestyle_poet` bonus). The **Night-Man** gives secrecy (intrigue, prowess; a bonus if he is of the target's household). There are two night-men and two vanilla lookouts. Template: `tm_bae2_spring_cell` (vanilla abduct, 1.20).
- **The night** (`tm_bae6.0001`, at each phase). Strike now or wait. Success rolls the scheme's success chance; the carver is named on a roll against secrecy.
- **Secrecy.** The pole is public, so the target always learns who paid. The secret is the carver's name, and with it the charge at law.
- **The pole stands** (`0010`; `tm_bae6_pole_stands_effect`).
  - The target loses medium prestige. The raiser takes Paid for a Níð-Pole.
  - The pole enters the Account as a wrong by her house against his. Where his house owed hers, it is a requital. A requital by a pole pays off **two** of what he owed, not one ("carved níð weighs more"; tally `poles_weighed_two`). Otherwise it is an ordinary wrong her house now owes his.
  - Rank escalation and the refused Account apply as in `tm_feud`.
- **His answer** (`0011`): burn it (−10 stress), "the hat is Óðinn's" (a target of the rite: +piety), turn it with humility (Christian), bring the carver to law (named carver, and a court whose law knows the pole), or carry it to the þing (a wrong in the Account the other way, and "Raised a níð-pole against me", −30).
- **The law** (`tm_bae6_carver_at_law_effect`). The court is the target's top liege.
  - **Christian law of Norway, Iceland included, from 1270** (`tm_bae6_sverrir_law_trigger`). The carver chooses (`0030`): forfeit his silver (up to 50, to the lord) and confess (**Confessed to the Pole**, 3 years), or take ship (`tm_bae2_go_abroad_effect`).
  - **Any other North Germanic court** (`tm_bae6_pole_law_trigger`). The older law: lesser outlawry before twelve (Meulengracht Sørensen p. 17), through `tm_bae2_lesser_outlawry_effect`: three winters abroad, with the reprieves and settlements of `tm_bae2`/`tm_feud`.
  - **Elsewhere** no law the mod sources names the pole, and the option does not show.
  - The pole is the heavier insult and the lighter crime. The three words carry full outlawry (`tm_feud_nid_outlawry_effect`); the pole carries lesser. See question 1.
- **Failure** (`0020`). Let it go, or cut another (only if the carver was not named). A named carver means `0021` for the target. Nothing stood, so nothing enters the Account. He may bring the carver to law, or send him home with a word for the one who paid (+minor prestige to him, −minor to her, −20 opinion).
- **AI.** Yearly pulse (`tm_bae6_yearly` → hidden `0002`). An AI ruler of the rite with a carver at court rolls 4% a year (+4 vengeful, +2 wrathful, +2 arrogant, −2 forgiving), at most once in five years. She targets a debtor house's head (weight 4) or a rival (weight 1) in diplomatic range. Players use the interaction.

### Built against the spec, and not

- Built: proxy carver, prestige loss, the pole in the Account (heavier), the answer event (burn, law, suit), exposure, the Christian-law crime with forfeiture-and-confession or exile, census.
- Not built: the −10 opinion from all neutral same-culture characters in Evans and Hancock row 3. It would touch hundreds of characters for a flavour line. The raiser's half-modifier carries the social cost instead.
- Not built: **Provoke the Words** (Miller row 13), an AI scheme by a hostile house to goad her into flyting first. It is a separate scheme and belongs with the bands or a later feud wave.

## 2. The Níð of the Land (decision `tm_bae6_nid_of_land_decision`)

### Source

Evans and Hancock row 4: law treats níð against kings as its own category, and Icelanders made a verse "for each nose" against Haraldr Gormsson (pp. 176–78). The row proposes: collective, every member pays a little prestige; the king takes −legitimacy and −dread; once per liege per ten years; no single outlawry.

### How it works

- **Who.** A landed ruler of the rite, adult, prestige level 2. Cost: 150 prestige. Decision cooldown: 20 years.
- **The king** (`tm_bae6_land_king_trigger`). A king or emperor, a man (question 2), not of the rite, whose house owes hers a wrong in the Account. He is her own top liege or a neighbouring top liege (`any_neighboring_and_across_water_top_liege_realm_owner`, as in `tm_bae5`). He must not have been sung against in ten years (`tm_bae6_land_nid_cd`).
- **The verses** (`0100`; `tm_bae6_count_noses_effect`). Every grown ruler of the rite under the king (`every_vassal_or_below`), her own such vassals, and herself make a verse; each of the others loses minor prestige. The count is the "noses".
- **The king** (`0101`). He loses 100 + 50 per nose prestige (at most 400) and 10 + 5 per nose legitimacy (at most 50, if he has legitimacy). He takes **The Níð of the Land** for 10 years: −15% prestige gain, −5 vassal opinion, −10 dread baseline (the row's "−dread-resistance"). Then he chooses:
  - **Humility** (Christian only; Evans and Hancock row 9): +medium piety, and the modifier goes.
  - **A crime against the crown:** "Made the Níð of the Land against me" (−40, 15 years), which carries vanilla's imprisonment and revoke-title reasons (as `declared_war` does), so a liege may lawfully imprison her or take back her titles. A wrong in the Account the other way (reason `tm_bae6_land_nid`).
  - **Bear it:** +20 stress.
- **Collective, so no outlawry.** No one is sued. The crime reason falls only on the one who began it (question 4).
- **AI.** Every 36 months, base 10 (vengeful, wrathful, arrogant up; craven, forgiving, calm down). It needs the Account against a king's house, so it will be rare.
- **Not built:** the "faction discontent boost" in the row. Vanilla factions are joined by vassals of any faith, and pushing discontent from one faith's verses into a liberty or claimant faction was judged too blunt. The vassal-opinion malus stands in.

## 3. Vows over the cup (`tm_bae6.0200`–`0211`)

### Sources

- Damico row 4 (`research/norse_damico_wealhtheow_valkyrie.md`): the heir "vows over the bragarfull, drains it", and takes the high seat (*Ynglinga saga* ch. 36, p. 55). A vow from a menu (avenge, rescue, raise a House, win land). Keeping it brings prestige and legitimacy; breaking it brings a broken-bragarfull modifier, "and the níð-shout opens against her".
- Damico row 5: vows over the *full* are "sealed in the gods" (Grønbech, p. 55). One vow tracker, several doors.
- Damico row 3: the cup comes right after the Unferth flyting and turns it into a vow (p. 10).

### How it works

- **Two doors.** The bragarfull (`tm_bae5.0020`, on inheriting) and the cup that ends a flyting (`tm_flyting.0020`). The first cup (`tm_bae5.0010`) is counsel, not a vow, and is not a door (question 5).
- **The menu** (`0200`). Swear to:
  - **answer the wrong** a named house did hers: kept when that house no longer owes hers, by requital or by settlement;
  - **raise a Sisters' House** (landed, holds none): kept when she holds one;
  - **widen the hall's land** (landed): kept when `sub_realm_size` is greater than when she swore.
  - Or **drink and swear nothing**, with no cost (writing rule 23: vows are for now, never required).
- **The term.** Five years, not for ever. Whoever handed her the cup (the bragarfull's bearer, or the lady who poured after the flyting) is stored as the witness.
- **The yearly look** (`tm_bae6_yearly` → hidden `0209`).
- **Kept** (`0210`): major prestige, medium legitimacy if she has it; courtiers and vassals +10, the witness +20.
- **Broken** (`0211`). **Broke a Vow over the Cup** for 5 years: −15% prestige gain, −5 general opinion. For a broken requital vow, the head of the house that owed hers gains minor prestige. Then:
  - **Say it before the benches:** minor prestige loss, +10 stress, nothing more.
  - **Say nothing:** courtiers and vassals −10, the witness −20. A man of her hall who thinks little of her (opinion ≤ 10, not of the rite) opens a flyting (`tm_flyting.0001`): the níð-shout.
- **Not built:** the "rescue a daughter" vow. Nothing in the mod records a rescue that a yearly check could read without hooks in the Rescue war and Spring the Cell.

## 4. Counting

`tm_feud_tally_effect` with names `bae6_*` (globals `tm_feud_n_bae6_*`). `land_noses` is a sum, not a count. The census prints them as "Bædling: wave 15":

`poles_begun`, `poles_raised`, `poles_weighed_two`, `poles_failed`, `carver_named`, `pole_burned`, `pole_turned`, `pole_humility`, `pole_suit`, `pole_law`, `carver_outlawed`, `sverrir_forfeit`, `sverrir_exile`, `carver_sent_home`, `land_nid`, `land_noses`, `land_humility`, `land_crime`, `land_borne`, `vows`, `vow_requital`, `vow_house`, `vow_land`, `vow_none`, `vow_kept`, `vow_broken`, `vow_owned`, `vow_shout`.

## 5. Rules respected

- **No violence on screen.** The pole is carved and set up at night; the law ends at forfeiture or a ship.
- **Rule 3.** Every hostile line has a speaker. The pole's runes are read by the man they name (`0011`), and the verses by the king (`0101`). The mare insult is the misogyny the historical níð used, aimed at a man and reported by him. The Bædling raiser's own line is "It says the worst thing the North knows how to say of a man: that he is like a woman. I know what that is worth." The narrator does not endorse it.
- **Daughters.** Daughters, Marked and declared women are never targets, carvers or kings sung against (`tm_bae6_a_man_trigger`), though the game may code them as male.
- **Historical figures.** None claimed. Haraldr Gormsson appears only as "a Danish king" in the poet's own voice. Sverrir's name stays out of loc: the text says "the Christian law of Norway".
- **Rule 13.** No line says the pagan North was free; the old law outlaws the carver too.
- **Rule 23.** The vow is optional and for five years. Saying the broken vow aloud is honoured, not punished beyond the shame.
- **Rule 25.** No pact or Sabbat imagery.
- **Loc.** Plain, with no italics markup. Glyph check silent.

## 6. Uncertain syntax (check in game)

- `random_scheme_agent_slot` with `is_agent_slot_type` and `slot_character` (finding the carver). If it finds no one, the fallback is the best courtier by learning.
- `every_in_list` with `change_local_variable` and `save_scope_value_as` from a local variable (the nose count), and `add_prestige` with `min` on a negative value.
- Saved scopes (`tm_cup_bearer`, `tm_cup_lady`, `tm_bae6_door`) surviving `trigger_event = { days = 1 }` into `0200`.
- `scope:x ?= flag:y` in a `triggered_desc`.
- `sub_realm_size` stored in a variable and compared with `>`.

## 7. Open questions for the user

**Decided (user, 2026-10-29): every default below is accepted.**

1. **Is carved níð heavier or lighter?** Mitchell (row 9) has the pole "a heavier insult and a heavier crime than spoken níð". Evans and Hancock (row 3) have it drawing a *lower* legal penalty than verse. **Default (built):** heavier as an insult, lighter as a crime. The pole costs the target medium prestige where the spoken word costs minor, and a requital by a pole pays off two wrongs. At law it brings only lesser outlawry, where the three words bring full outlawry.
2. **Men only?** The pole and the verses are misogyny aimed at a man, so the target of a pole and the king sung against must be men, and never daughters, Marked or declared women. A woman who wronged her house cannot be poled, and a queen cannot be sung against. **Default:** keep it so. The sources' níð against women is a different insult (sexual slander), which the mod does not want as a mechanic.
3. **Where Sverrir's law applies.** Built for de jure Norway, Iceland included, from 1270 (`tm_bae6_sverrir_law_trigger`). Danish and Swedish courts use the "older northern law" branch (lesser outlawry) at every date. **Default:** keep. Add Sweden from 1350 (Magnus Eriksson) only if a source names the pole there.
4. **The crime on the poet alone.** The row says no single outlawry, since the act is collective. The king's "crime against the crown" gives an imprisonment and revoke reason against the one who began it, and nothing against the other noses. **Default:** keep. It is the liege's choice, not outlawry, and it is what makes a vassal think twice.
5. **The doors to the vow.** Only the bragarfull and the flyting's cup. **Default:** keep the first cup as counsel, without a vow. Option: add the vow to a feast (vanilla activity) if vows prove too rare in observe runs. The bragarfull fires only on inheritance.
6. **Settlement counts as keeping a vow to answer a wrong.** Bót was honourable (Miller pp. 262–63). **Default:** yes. Option: only a requital keeps it.
7. **The land vow counts any gain**, by inheritance or grant as well as war. **Default:** keep, since it is simpler and the hall cares that the land is wider. Option: count only conquest, through vanilla's war on_actions.
8. **Male raisers.** Any ruler of the rite may pay for a pole, including a man of the faith. **Default:** keep.
9. **AI frequency.** A 4% yearly roll for each eligible AI ruler, five years between attempts. The Níð of the Land: AI base 10 every 36 months. **Default:** keep until an observe run shows the counts.
