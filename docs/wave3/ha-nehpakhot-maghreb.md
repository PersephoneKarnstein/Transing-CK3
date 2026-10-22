# Ha-Nehpakhot in the Maghreb (and the Sahel), wave 3

Status: built, untested in game (2026-10-21). xTiger: no reports in any `tm_hn3_*`, `tm_hn2_*` or `tm_hipukh_*` file. `tools/check_glyphs.py` passes.

Sources: the eleven notes `docs/research/jud_maghreb_*.md`. Kraemer, Krakowski and Rustow have no print pages in our copies, so they are cited by chapter in comments, and no loc cites a page of theirs. The user approved all ten merged proposals; each is built.

## Files

New (prefix `tm_hn3`):
- `events/tm_hn3_events.txt` (namespace `tm_hn3`: 0010, 0011, 0020, 0030, 0040, 0050, 0060)
- `common/scripted_triggers/tm_hn3_triggers.txt`, `common/scripted_effects/tm_hn3_effects.txt`
- `common/script_values/tm_hn3_values.txt` (`tm_hn3_maghreb_era`)
- `common/decisions/tm_hn3_decisions.txt` (three decisions)
- `common/on_action/tm_hn3_on_actions.txt` (`yearly_playable_pulse`)
- `common/modifiers/tm_hn3_modifiers.txt`, `common/opinion_modifiers/tm_hn3_opinion_modifiers.txt`
- `localization/english/tm_hn3_l_english.yml`

Changed (owned files; each change carries a `wave 3` comment):
- `events/tm_hipukh_events.txt`: 0001 (rope line, +10 for the Purim fire), 0002 (Maghrebi names option), 0003 (the three ban calls now go through `tm_hn3_niddui_effect`), 0011 (Purim fire desc and option), 0031 (Maghreb version).
- `events/tm_hn2_events.txt`: 0010 (attire option and desc end), 0011 (attire desc).
- `common/on_action/tm_hn2_on_actions.txt`: the story joins the yearly member scan; the ruler pulse fires `tm_hn3.0020` instead of `tm_hn2.0040` when her capital is in the Maghreb or the Sahel, and skips a ruler who has the decree.
- `common/scripted_triggers/tm_hn2_triggers.txt`: `tm_hn2_served_lord_trigger` also accepts the two new physician modifiers.

## Regions and era

- **Maghreb** = counties de jure in `e_maghreb` (k_maghreb, k_tahert, k_africa, k_anbiya, k_sahara, k_canarias). **Ifriqiya** = `k_africa` (Kairouan, Tunis with al-Mahdiyya, Gabes, Tripolitania, Constantine). **Sahel** (and Volta) = `e_mali`, `e_kanem_bornu`, `k_gur` (Dagomba), `k_akan` (Bono): where run 4 put the faith after 1077. "West" = Maghreb or Sahel.
- `tm_hn3_maghreb_era` (script value; trigger `tm_hn3_maghreb_era_trigger = { ERA = n }`), for text only, plus the refuge decision's window:

| Era | From | Choice where the books disagree |
|---|---|---|
| 1 Qayrawan | start | — |
| 2 after Qayrawan / Almoravid | 1 Nov. 1057 (sack: Gil p. 741) | The Almoravids take Fes 1074–75 (Bennison p. 337); the era starts at the sack, since its texts speak of Qayrawan in the past |
| 3 Almohad | 1146 (Fes: Bennison p. 341); **1160 in Ifriqiya** (Tunis campaign, Bennison pp. 88, 342) | Kraemer gives Fes 1145: **1146** used |
| 4 Hafsid / Marinid | 1229 (al-Ma'mun renounces mahdism, Hafsids break away: Bennison p. 345; Stillman p. 77) | Hirschberg gives the Hafsids 1228: **1229** used. Marinid Fes: **1248** (Bennison) over 1250 (Hirschberg); no text names the Marinids, so the era does not split there |

## What was built

1. **The ban, Maghreb version** (`tm_hn3_niddui_effect`, `tm_hn3.0010`, `tm_hn3.0020`, decision `tm_hn3_two_parties_decision`).
   - Under a Muslim county holder in the West, a lost hearing lays `tm_niddui_modifier` with no licence: the ban is the street's own (Hirschberg pp. 221, 233–237; Gil's Maghreb pages have no licence). Thirty days later (Hirschberg p. 237), if his flavour budget allows, the lord gets **The Street's Ban** (0010): (a) send it back for a new Jewish hearing by their own law (Krakowski ch. 6; Goitein p. 212) → 0011; (b) lend his court: *The Ban Enforced* (3 years, −0.5 prestige/month, +10% stress) (Hirschberg pp. 236–237); (c) forbid it, only on her petition (Rustow ch. 8): the ban is lifted, and Jews of other faiths at his court and hers take −10 of her ("Took the Street's Case to the Ruler"); (d) "We do not interfere" (Cohen p. 74). The petition exists when a protector of the sect serves him (a physician of the sect, either version; or he commissioned a translation) or a Jew at his court is her friend or likes her (≥50).
   - Under a ruler of the sect in the West the ban is also the street's own; her yearly pulse brings **The Two Parties** (0020) instead of the Provençal licence (0040): (a) decree that neither party may ban the other; (b) forbid this ban only (other Jews −10, as 0040.a); (c) "The judges of the street have ruled" (+20 piety). From 1030 the desc cites the caliph's decree (Rustow ch. 8; Stillman p. 198); before, a plain line. The narrator never says a Maghrebi ruler issued it.
   - **The decree** (`tm_hn3_two_parties_effect`; also a decision for a West ruler with Jews of another faith at court or among vassals): lasts her lifetime; lifts current bans; no Jewish court in her realm can ban a daughter (toast); non-zealous Jewish courtiers +10, zealous −10. A yearly check lifts bans on daughters who come to her land.
   - Elsewhere: unchanged (`tm_turning_niddui_effect`, the Provençal lord's licence; 0040 stays).
2. **The trustworthy women** (0011). The new judge sends women to hear her at home. Roll 50 + learning (+15 if a Jewish female friend or kinswoman sits with her, +20 *Teach Her the Answers*) against 50. Win: ban lifted, +50 prestige, the county's worthies' licence (10 years, as 0003). Lose: +10 stress. Or "I will not be heard twice" (+20 piety).
3. **The physician as protector** (0031, Maghreb version: a Muslim lord whose capital is in the West). The paid licences are hidden; instead: take her into service (*Physician to the Lord*, 10 years: learning +2, prestige +0.3/month), or from **1075** with the title of vizier (learning +2, diplomacy +1, prestige +0.5/month, +50 prestige; his Muslim courtiers −5 of him, Bennison p. 167), or "I have physicians enough". Desc: from 1015 the nagid line (present tense in era 1, past after 1057; Stillman pp. 46, 183–187); from 1075 the vizier line (Kraemer ch. 5; Hirschberg pp. 122, 351). The protection is hers: while she serves, any daughter banned in his land can petition (above), and the bailiff's "served" test accepts her. It lapses when the modifier ends or she dies (Stillman pp. 186–187).
4. **Maghrebi names**: an added option at the naming (0002) for a daughter in the Maghreb or of Arabic or Berber heritage. Sitt al-Kull, Mawlat, Surura, Sittuna, Sitt al-Ahl, Mubaraka, Berakha, Sitt al-Dar, Sittat, Banina, weighted (`tm_hn3_maghreb_name_effect`, pages in comments). Scroll, Provençal and Catalan options unchanged. No date gate (see questions).
5. **The stirrup of Purim** (0011, Ifriqiya, any date): a desc line by era (Qayrawan before 1057; "behind the gate of the quarter" 1160–1229; "the families who came from Qayrawan" otherwise) and an option "Remember the fire" (+10 at the prayer, −15 stress, +10 prestige). Hirschberg p. 170.
6. **Qayrawanese attire** (`tm_hn2.0010`/`0011`): for a bride in the West or of Arabic/Berber heritage the necklace option is replaced by "Send for the robe, cap, veil and mantle" (same 40 gold, same AI). Artifact *The Qayrawanese Attire* (`miscellaneous`, `fabric_roll` visuals as vanilla's lover keepsake; diplomacy +1, prestige +0.1). It carries `tm_hn2_adornment`, so one adornment per daughter. Kalonymus's line is not shown for it. Goitein p. 167.
7. **The story with no ending** (0030; from 1062, daughters in the West or of Maghrebi speech; 5% a year, budget): she tells Nissim's "Abandoned Girl" up to the break and chooses an ending (women of her faith +10 / +20 piety / +20 prestige). Nissim pp. 6, 175–176. **The rope from heaven** (0001): from 1160 in the West, for a seeker who has prayed before, the elder adds the image from the *Epistle of Consolation* (Kraemer ch. 6). Nothing about conversion.
8. **They shall not be turned away** (decision for a ruler of the sect in the West in era 3, cooldown 10 years → 0050). A Rabbanite couple finds shelter at her court and keeps its own faith (`tm_hn3_receive_refugees_effect`: a married man and woman of `faith:rabbinic_faith`, culture of her capital county, employer = her, variable `tm_hn3_refugee`); shelter is not conversion. The kahal of her town (`tm_surv_kahal_draw_effect`) takes Rabbanite Jews at her court first, so some may join later. +50 piety; they like her (+25, 20 years). From 1165 the desc quotes the faith's reading of Maimonides (Hirschberg p. 195); before, a plain line. No persecution is shown; nothing happens to anyone in the Almohad lands.
9. **The decorous hush** (decision for any landed ruler of the sect → 0060): daughters of the Turning at her court +10 (permanent) and *The Decorous Hush* (−10% stress gain, refreshed yearly for newcomers); Jews of other faiths at court −5 (5 years). From 1160 the ruler's own desc compares it to the western Jews' silence about returned converts (Stroumsa p. 59). This analogy is the mod's; the narrator does not equate the Turning with forced conversion.
10. **Robes of Honour** (0040; before Nov. 1023; a woman ruling a realm with its capital in Ifriqiya, or the female regent/diarch of such a ruler, with a daughter of learning ≥10 at court; 10% a year, budget): robes and a saddled mule (+50 prestige, +20 opinion), or let her read again (learning xp), or not this year. Gil p. 188 and n. 126; Goitein p. 357. The narrator names no one.

**The Sahel.** The notes give no Jewish source for the Sahel. Only mechanics resting on general Islamic practice or on the faith's own law apply there: the Muslim lord's four answers to a ban (their texts name no place), the Two Parties, the physician's service (desc: "as the amirs of the Maghreb do"), the refuge (refugees reached Dar'a, Cohen pp. 181–182), the rope line, the story, the hush. The Purim fire, the Zirid robes and the Qayrawan names stay with Ifriqiya and the Maghreb (names also by culture).

## Uncertain syntax

- `tm_hn3_maghreb_era = $ERA$` inside a scripted trigger: a script value compared in a trigger. xTiger accepts it.
- `diarch` link used as the regent, with `diarch ?= { is_female = yes }`.
- `capital_county.culture = { save_scope_as = … }` then `culture = scope:…` in `create_character`.
- `type = miscellaneous`, `visuals = fabric_roll` with no features: as vanilla (`lover_events.txt`).
- Saved scopes from `tm_hn3_niddui_effect` (called inside `tm_hipukh.0003`'s random_list) reaching `tm_hn3.0010`, 30 days later.

## Test scenarios (for TO-TEST.md)

- **Ban, Muslim lord.** A seeker in Fes (Muslim holder) loses 0003. She gets the ban; 30 days on the holder sees 0010. Without a protector or Jewish friend at his court, option c is hidden. Give his court a courtier with `tm_hn3_physician_modifier`: c shows and lifts the ban, and Jews of other faiths at both courts get −10 of her. a → 0011 within a month. b → *The Ban Enforced*.
- **Ban, sect ruler.** A ruler of the sect with capital in `k_maghreb`, a shunned daughter at court: the yearly pulse gives 0020, not 0040. Take a: courtier bans are lifted; a new loss in 0003 in her realm shows the toast and no ban. The decision appears only without the decree and with Jews of another faith at court.
- **Provence unchanged.** The same in Arles: `tm_turning_niddui_effect` and 0040 as before.
- **Rehearing.** 0011 with and without a Jewish female friend; check +15 in the tooltip.
- **Physician.** A Muslim lord with capital at Kairouan, 1030: Maghreb desc with the nagid line in present tense; no vizier option. At 1100: past tense, vizier option and line. A Christian lord: the old event.
- **Names.** A seeker of Berber culture turned: the Maghreb option shows; names display (Sitt al-Kull etc.).
- **Purim fire.** A seeker at Tunis in 1000, 1100, 1180 and 1300: three different lines; the option gives +10 at 0001; a seeker at Fes sees neither.
- **Attire.** A daughter at Marrakesh marries: the attire option replaces the necklace; the artifact is created, and 0011 reads the attire text without the Kalonymus line. A second marriage offers neither.
- **Story.** A daughter at a court in Gao after 1062: 0030 fires (raise the chance to test); before 1062, never.
- **Rope.** A seeker at Fes after 1160 with `tm_turning_prayers`: the rope line follows the elder's desc.
- **Refuge.** A ruler of the sect with capital in Fes at 1150: decision shown; at 1100 and 1240, hidden. Taking it adds a married couple at court, now of the sect; the census `kahal_joins` rises by 2.
- **Hush.** Decision, then check opinions and the modifier; a daughter who arrives later gets the modifier at the next yearly pulse.
- **Robes.** A female ruler at Kairouan in 1010 with a daughter of learning ≥10; also a male ruler with a female regent. After Oct. 1023 it does not fire.

## Questions for the user

1. The Muslim-lord ban is limited to the Maghreb and the Sahel. Its sources (Krakowski, Goitein, Cohen, Rustow) are mostly Egyptian or general Islamic law. Should it apply under every Muslim lord (Egypt, al-Andalus, the Levant)?
2. Maghrebi names have no date gate. Goitein's corpus starts in the mid-10th century. Gate at 950?
3. The vizier gate is 1075 as approved; the attested cases are under 'Ali b. Yusuf (1106–43; Hirschberg p. 122 "early 1130s"). Keep 1075?
4. `tm_hipukh.0003`'s judges are still named by Arles dates (custom loc, not my file). See stage 2, "Still proposed" 1.

## Ready to paste

**README (Ha-Nehpakhot section):**
> *In the Maghreb and the Sahel.* Under a Muslim lord the street's ban is its own: no lord licenses it. The lord may send a case back to be heard again (trustworthy women come to hear her at home), lend his court to enforce the ban, forbid it if someone at his court speaks for her, or stay out of it. A ruler of the faith there may decree that neither party of the Jews bans the other. A daughter who serves a Muslim lord as physician (from 1075, as vizier) can speak for her people. Also: Maghrebi names, the Purim fires of Qayrawan, the Qayrawanese attire, Nissim's story with no ending, a refuge decision for the Almohad years (1146–1229) and the decorous hush.

**TODO (new block):**
> - [x] Ha-Nehpakhot, wave 3: Maghreb and Sahel (`tm_hn3`; `docs/wave3/ha-nehpakhot-maghreb.md`). Untested.
> - [ ] Questions: Muslim-lord ban everywhere? Name gate 950? Vizier gate 1075? Maghrebi judges in `tm_kahal_judges`.
> - [ ] Print pages for Kraemer, Krakowski and Rustow.

## Decisions (user, 2026-10-21)

1. **The Muslim-lord ban stays limited to the Maghreb and the Sahel** (question 1).
2. **Maghrebi names have no date gate** (question 2).
3. **The vizier option starts in 1075** (question 3).
4. **The Maghreb judges** (question 4): the lead added a first `text` to `tm_kahal_judges`, `_cap` and `_title` in `tm_custom_loc.txt` for `tm_hn3_in_west_trigger`: "the elders and the dayyan" (Hirschberg pp. 224, 230).
5. **Refugees keep their own faith.** Shelter is not conversion: they fled one forced conversion. The lead changed `tm_hn3_receive_refugees_effect` so the couple stays Rabbinic and no longer calls `tm_surv_kahal_take_in_effect`. They live at her court, where the kahal of her town may draw them later. §8 above and its test scenario describe the earlier draft; TO-TEST.md Q11 has the current expectation.
6. **Kahal joins may create characters**, as a stand-in for the wider Jewry the game does not make (see survival.md).
