# Ha-Nehpakhot, stage 2

Status: draft for the user's review (2026-10-21). Nothing here is tested in game. Revised the same day to date-gate every text against `docs/later_starts.md` and `docs/research/later_starts/region_latin-christendom-jewish-europe.md` (see **Dates**), and again to apply the user's answers (see **Decisions**).

## Decisions (user, 2026-10-21)

1. Bailiff: the rival is **any rival**, as drafted. No change.
2. Carnival: **keep 1400**.
3. Spindle talk: **yes**, it raises the odds at the next hearing before the street's judges (`tm_hipukh.0003`). Built: a won answer in 0002 sets `tm_hn2_spindle_heard` on the county (10 years). The next hearing there reads it (+10 to both learned answers, 0003.a and .e) and removes it. A daughter of the Turning has already had her own hearing, so the bonus belongs to the **street**: it goes to the next seeker judged in that county. The scale matches the built +10 (women on the council) and +15 (licensed county).
4. **A seat below** and **Catalan names** are built. The Catalan list is an **added** option in `tm_hipukh.0002`: the scroll names (Torah) and the Provençal street names stay.

The user allowed minimal edits to the existing Ha-N files for these items. Each is listed under **Changes made to existing files**.

Files (all new, prefix `tm_hn2`, namespace `tm_hn2`):
- `events/tm_hn2_events.txt`
- `common/on_action/tm_hn2_on_actions.txt`
- `common/scripted_triggers/tm_hn2_triggers.txt`
- `common/scripted_effects/tm_hn2_effects.txt`
- `common/modifiers/tm_hn2_modifiers.txt`
- `common/opinion_modifiers/tm_hn2_opinion_modifiers.txt`
- `localization/english/tm_hn2_l_english.yml`

xTiger: no reports in these files (baseline 23 unchanged for this faith).

## Dates

Every text is gated by what its source allows. The text gates are scripted triggers in `tm_hn2_triggers.txt`: `tm_hn2_rashi_trigger`, `tm_hn2_maimonides_trigger`, `tm_hn2_hinukh_trigger`, `tm_hn2_touchstone_trigger`.

| Feature or text | Earliest date the sources support | Gate used |
|---|---|---|
| 1. The spinning circle (event) | Women spinning together: no date. The moonlit circle as an image is *Even Boḥan* (1322–23) | Event at every date. The line "as the Touchstone says women do" only from **1323**; before that, a plain desc |
| 1. Sarah as *aylonit* | bYevamot 64b (Talmud, read in Provence before 1066) | **Every date** (Talmud form) |
| 1–2. Rashi's gloss on Sarah; Rashi on Deut. 22:5 | Rashi wrote at Troyes c. 1070–1105. His reach in Provence by 1178 is *unverified* (region note §1.1) | **1105**. The commentary is complete at his death, so this is the earliest defensible date, not a proven one. Before 1105 the faith speaks from the Talmud alone: Sarah "bore Isaac", and Leah's prayer for Dinah (bBerakhot 60a). The worthies answer "Sarah was a woman before she bore and after" |
| 2. The worthies' second line: the beard (*Sefer ha-Ḥinukh* 542–543) | "A 13th-century Barcelona code" (`jud_rabbinic_primary_texts.md` §12). The year is not in the notes (*unverified*) | **1300**, the latest plausible date. Before that the worthy quotes Deut. 22:5 itself ("a man shall not put on a woman's garment") |
| 2. The adornment, the law's line (MT Avodah Zarah 12:10) | Mishneh Torah, completed c. 1180 | **1180** |
| 2. The adornment, Kalonymus's "ornaments of gold" | *Even Boḥan*, Dec. 1322–Jan. 1323 | **1323** (event desc and 0011). Before 1180: Rebecca's bracelets of gold (Gen. 24:22, 47; scripture, not in the research notes). The artifact's own description cites no book |
| 3. Before the bailiff | Assis's cases: Lleida 1263 to 1374 (Crown of Aragon). Provençal fines in the lord's court are 14th-century (Shatzmiller pp. 321–324) | **1260** |
| 4. Carnival before Purim | Arles 1433, "a novelty never seen" | **1400** (game convention: the generation before the case; user decision) |
| 5. The lord's licence (event) | The lord's licence for the ban is the mod's premise at every date (`later_starts.md` §5) | Event at every date. Desc: plain before 1305; Abba Mari's line (Montpellier c. 1305, Shatzmiller p. 86) from **1305**; the Arles terms (one year, absolution reserved) from **1405** |
| 6. A seat below | Women's synagogue below the men's: Arles 1409 and 1452 | **1409** (`tm_hn2_seat_candidate_trigger`) |
| 7. Catalan names | Girona records, 1390s–1420s | **1390** (`tm_hn2_catalan_seeker_trigger`; earlier Catalan names *unverified*) |
| 1→0003. The spindle bonus at the hearing | The bonus rides on 0002, whose texts are dated above | Any date. The bonus is mechanical only |
| Who judges (0002) | "The worthies of the street" is a gloss that holds at every date (Hildenfinger §4.6). Rectors only from 1215, baylons from 1386 | My texts say only "the worthies of the street" (0002) and "the judges of the Jewish street" (0040). They never name baylons or rectors, so nothing needs a 1215 gate |

**The licence before 1144.** The coordinator asked for "the count and the archbishop" before 1144 and "the archbishop" after. `docs/later_starts.md` §5 records the decision that the pre-1144 joint arrangement "is not in our sources and was not used", and that the licence stays voiced as "the lord's", which holds at any date. My texts follow that decision. 0040 is the sect's own ruler licensing her own land, so neither the count nor the archbishop appears. None of my texts names who licenses a ban under a Christian lord.

**1178 hooks these features could use later** (notes only, from the region note §§1.1 and 3.1; nothing built):
- **The 1144 grant** (Conrad III gives the archbishop jurisdiction over the Jews of Arles; Ben-Shalom p. 26). At a 1178 start, 0040's "the ban is pronounced in my land" matches the archbishop's position exactly. A Christian-lord version of 0040 for the archbishop of Arles would fit from 1144.
- **Lunel's Tibbonids.** Benjamin's "R. Judah the Physician, the son of Tibbon" (Adler p. 4). This is the period footing for the "served the lord" protection in 3 and 4. A 1178 daughter's service could be "trained at Lunel".
- **Benjamin's figures** (c. 1165): about 200 Jews at Arles, 300 at Lunel, 100 at Saint-Gilles, 300 at Narbonne (Adler pp. 2–6). Lunel's congregation boarded poor students. That is a model for 1's pupil and for the pilgrimage.
- **Abba Mari, "bailiff of Count Raymond" at Saint-Gilles** (Benjamin, Adler p. 5). An earlier frame for 3: before 1260, the officer who hears the rival could be a Jewish bailiff of the count. Not built (see feature 3, question 4).
- **Barbarossa crowned at Arles, 30 July 1178.** The kahal seeks confirmation of its privileges. This is a natural trigger for 0040-style licence content at the 1178 start.
- **Rashi on Gen. 30:21** ("its sex was changed"). Beside the Yevamot gloss, it could give 0001 a third Rashi line from 1105, for the scroll.


| # | Feature | State |
|---|---|---|
| 1 | By moonlight: the spinning circle, Sarah, and talk that reaches the worthies | **Drafted** (0001, 0002) |
| 2 | The adornment, an artifact given at her wedding | **Drafted** (0010, 0011) |
| 3 | A rival takes her to the bailiff | **Drafted** (0020) |
| 4 | Carnival before Purim | **Drafted** (0029, 0030) |
| 5 | The lord's licence: a ruler of the sect and the street's ban | **Drafted** (0040) |
| 6 | A seat below | **Drafted** (0050; +10 in `tm_hipukh.0001`) |
| 7 | Catalan names of the street | **Drafted** (added option in `tm_hipukh.0002`) |
| — | The Maghreb | **No source in the notes.** Reading proposed, nothing built |

Every event is flavour (0050 included: 5% a year). Every recipient is checked against `tm_flavour_ready_trigger` and spends the budget (`tm_flavour_spent_effect`) when an event is fired. The chances are modest: a daughter has 8% a year for the circle, 4% for the bailiff (only with a rival under a Christian lord, from 1260), and a Christian court with members has 10% a year for Carnival (from 1400).

---

## How the faith ends up in runs

In observe run 1034 (v0.2.0) the sect holds **k_maghreb** as a royal faith from 912: 22 rulers, 595 members. Its kahal never recruits; it grows by matches and conquest. Most of the built Ha-N content assumes a landless sect under a Christian lord in Provence. So:
- Features 1 and 2 work anywhere a daughter of the Turning lives, landed or not, in Fes as in Arles. Their text names no Provençal office.
- Features 3 and 4 are for the sect under Christian lords (the Provençal diaspora). They do not fire in a Ha-N realm.
- Feature 5 is for the sect as a ruling faith. It works in the Maghreb without inventing any Maghrebi history, because it rests on how a Jewish community's ban was licensed by its lord (Provençal sources).

---

## 1. By moonlight (drafted: `tm_hn2.0001`, `tm_hn2.0002`)

**What the player sees.** A daughter of the Turning sits with the women of her court, spinning by moonlight. She can:
- **a. Tell them of Sarah.** From 1105: "The sages say she was an *aylonit*, with no place for a child, and Rashi says a woman's body was made for her." Before 1105: "…with no place for a child. Yet she bore Isaac." +20 piety, the spinning-circle modifier for a year, and +10 opinion (3 years) from members of her faith at the court. 15% chance the talk travels (below).
- **b. Teach a younger woman or a seeker to comb the flax and spin.** −10 stress, 50 stewardship xp, +15 opinion from the pupil. A pupil who is a seeker of the Turning also counts as taught the prayer (`tm_hevrah_taught`, the built +15 to her Turning). Shown only if there is such a courtier (adult of her faith, 10 to 29, a woman or a seeker).
- **c. Only listen.** −20 stress, the spinning-circle modifier. 5% chance the talk travels.

**The talk travels (0002).** 60 to 180 days later the worthies of the street send for her. One answers her Sarah: "a womb was made for Sarah, not a sex" (from 1105) or "Sarah was a woman before she bore and a woman after" (before). Another quotes the law: "even one hair plucked from the beard is a woman's adornment" (from 1300) or Deut. 22:5 itself (before). She can:
- **a. Answer Rashi with Rashi**: "the Torah forbade only the dress that leads to abomination" (from 1105). Before 1105: "Leah prayed, and the child in her womb was turned into Dinah" (bBerakhot 60a). Roll: 40 + 2×learning (+20 with *Teach Her the Answers*) against 50. Win: +40 prestige. Lose: −25 prestige, +10 stress.
- **b. "As Rashi says of Sarah: a woman's body was made for her."** +30 piety. Before 1105: "The sages say Sarah had no place for a child, and she bore Isaac."
- **c. "It was only talk at the spindle."** +5 stress.

There is no *niddui* here: gossip is not a judgment. The real hearing stays in `tm_hipukh.0003`.

**Sources.**
- The circle: *Even Boḥan*, Lemberg p. 16, the women "telling stories to one another" (`research/jud_kalonymus_even_bohan.md` §§2, 6, 8: "a recurring sisterhood event"). Ben-Shalom 2024, p. 112 (`jud_benshalom_provence_languedoc.md` §4.5). Grossman: a daughter raised "to sew, to spin, and to do good deeds" (ch. 7 §7; `jud_grossman_pious_rebellious.md`).
- Sarah: bYevamot 64b, "Sarah our mother was an *aylonit*"; Rashi ad loc., "a female organ was made for her" (`jud_rabbinic_primary_texts.md` §§10–11; Strassfeld 2022, ch. 5 n. 63, `jud_strassfeld_trans_talmud.md` §2.2).
- The talk reaching a court: Mishnah Sotah 6:1, where the spinners' gossip is used as testimony (Rosen 2003, p. 249 n. 26, after Peskowitz; `jud_rosen_circumcised_cinderella.md`, rows on `tm_spinning_circle_modifier_desc` and "the spinning circle is not safe"). Ben-Shalom also puts Sotah 6:1 behind Kalonymus's image (p. 113).
- The worthies' lines and hers: the summary table in `jud_rabbinic_primary_texts.md`. Opponent: "Her womb was made, not her sex" (the rejoinder to Rashi on 64b) and *Sefer ha-Ḥinukh* 542–543 on the beard (§§13–14). Sect: Rashi on Deut. 22:5 (c) (§15).

**Rules respected.**
- Sarah is claimed in the faith's voice only. The narrator never says Sarah crossed sexes: the line is in an option, spoken by the daughter, and the worthies get the rabbinic rejoinder in the same chain.
- The *aylonit* is not etymologised (no ram, `jud_strassfeld_trans_talmud.md` §4.5).
- Rashi (b) "to sit among the women" and Nazir 59a are never voiced (`faith_design.md` §13).
- Rule 19: Sarah is kin, "her lamp", never proof that the sect is owed a place. The option is a story told at the spindle, not an argument in court. The court argument (0002.a) is Rashi on dress, not Sarah.
- The circle is not a male idyll (Rosen): its talk can hurt her.

**Open questions.**
1. *Decided:* a won answer makes the next hearing in that county easier (+10, consumed at the hearing). See **Decisions** 3.
2. Is 15% for the risk too high? It fires at most every few years for any one daughter, given the 8% roll and the budget.

## 2. The adornment (drafted: `tm_hn2.0010`, `tm_hn2.0011`)

**What the player sees.** When a daughter of the Turning marries, 40% of the time her spouse is asked whether a goldsmith should make her a necklace. The desc is dated: from 1323 Kalonymus's wish for "ornaments of gold" and the law's line; from 1180 the law's line alone (MT Avodah Zarah 12:10); before 1180 Rebecca's bracelets of gold (Gen. 24:22, 47). The spouse can pay 40 gold for it, or say "Not now". A refusal costs her nothing. If given, she receives **The Adornment**: a common, non-decaying necklace artifact (diplomacy +1, monthly prestige +0.1), and +25 opinion of the giver (permanent). A week or two later she wears it (from 1323 the women of the lamp add "what Kalonymus asked for and never had"): at the Sabbath lamp (+20 piety) or in the street (+20 prestige), each −15 stress.

The artifact is an ordinary artifact: it can be inherited, given or taken. A daughter who already owns one is not offered another (the artifact carries the variable `tm_hn2_adornment`).

**AI.** The spouse gives it at base 40 (+30 if they like her, +20 generous, ×0.3 greedy) against 40 for "Not now" (+30 if they dislike her, +20 greedy).

**Sources.** *Even Boḥan* p. 17, "he would adorn me with ornaments of gold", and the item idea "the adornment as an artifact" (`jud_kalonymus_even_bohan.md` §8). Maimonides, *Mishneh Torah* Avodah Zarah 12:10: gold bracelets as a woman's adornment "in a place where only women wear them", "all according to the custom of the country"; the same verb (`jud_rabbinic_primary_texts.md` §5).

**Rules respected.** The gift is the spouse's free choice, on the model of the prayer book (`tm_kahal.0001`). Same-sex spouses are allowed by the mod; the text does not assume the giver is a man. No body text. Rule 24: jewellery is one of the outward signs allowed at every date.

**Open questions.**
1. Necklace or bracelet? Vanilla has a necklace artifact type with art, and no bracelet type outside the Oxus bracelet. Kalonymus has necklaces on Purim (p. 29) and "ornaments of gold" (p. 17); Maimonides has bracelets. The loc says "necklace".
2. Should a player daughter also be able to commission it herself (a decision)? Not built.

## 3. Before the bailiff (drafted: `tm_hn2.0020`)

**What the player sees.** From 1260, a daughter of the Turning who has a living rival and lives in a county held by a Christian lord: her rival "has carried a complaint about me to the bailiff of [lord]: that I go about in a woman's dress and under a woman's name. The lord's court hears such charges, and it fines more often than it punishes. The fines go to the lord." She can:
- **a. Pay the fine**: 25 gold, paid to the county's lord. +5 stress.
- **b. Ask the lord she has served to stand for her.** Only if she has *earned* it: the lord commissioned a translation from a daughter of the Turning (`tm_translation_patron_modifier`, `tm_hipukh.0030`), or she holds a physician's licence (`tm_fisica_licensed_modifier` / `tm_fisica_women_modifier`, `tm_hipukh.0031`). The charge is quashed: +25 prestige, +5 opinion from the lord.
- **c. Answer before the bailiff herself.** Roll 40 + 2×learning + diplomacy against 50. Win: the charge is voided, +40 prestige. Lose: +10 stress, and the fine is taken (25 gold), or −50 prestige if she cannot pay.

**Sources.** Assis 2001: in the Crown of Aragon such charges were heard by the king's officers and "often" remitted "for a sum of money" (p. 44); the pardon "paid" (p. 36); at Lleida in 1263 the king voided the charges brought by two men and the accuser persisted (p. 44). Assis's own design proposal is this event: "a rival takes it to the bailiff… gold paid to the liege, or her patron's protection" (`jud_assis_catalonia_sexuality.md` §§2.1–2.2, 4). Shatzmiller 2023: the fines of the lord's court were the lord's income (pp. 321–324); the Arles licence and the Manosque trial of 1310 show the lord's court reaching into the street (pp. 87, 89). TODO: "a fine, or the patron's protection (Assis; Shatzmiller)".

**Rules respected.**
- Protection is earned by service (translation, medicine), never bought. Option a is a fine imposed by the court, not a payment for protection, and it buys nothing beyond the case.
- No moneylending. The patron is never betrayed.
- **The rival's faith is not named.** Assis's accusers are Jews, and the guardrail says Jewish characters are never the wrongdoers in Christian-harassment events. This event is a private quarrel taken to a Christian court, so the text uses the game's rival relation, of whatever faith, and never says "a Jew accused her". See open question 1.
- No burning, no lashes, no *beit din* violence (Assis p. 44: burning recorded once, 1374, for acts, not dress). The penalty is a fine.

**Open questions.**
1. *Decided:* any rival, as drafted (Assis's accusers were Jews; the text never names the rival's faith).
2. ~~In Catalan and Aragonese counties, should the officer be the *batlle* and the street's judges the *berurim* (Assis p. 39)?~~ Built in wave 6 (`docs/wave6/ha-nehpakhot.md`).
3. ~~Assis's "moral panic after a patron's fall" (Toledo 1281, pp. 27–28) is not built.~~ Built in wave 6 (`tm_hn4.0001`).
4. Before 1260 the event does not fire. An earlier frame exists: Abba Mari, "bailiff of Count Raymond" at Saint-Gilles (Benjamin c. 1165, Adler p. 5), so a Jewish bailiff could hear the rival's complaint. I have not built it, because the Jewish officer would then be the one who fines her. Do you want that variant?

## 4. Carnival before Purim (drafted: `tm_hn2.0029`, `tm_hn2.0030`)

**What the player sees.** Once a year 10% of Christian courts that hold members of the sect, in a county of Frankish heritage (Occitan, French), from 1400, pick one adult member (a daughter of the Turning and the old likelier). A hidden event waits for February. "It is Carnival, a few weeks before Purim. The town's young men have chosen an abbot of youth, and he and his fellows have come into the Jewish street to take pledges for the *pelote*. It is a due the youth abbeys take from newly married couples. It was never asked of the Jews." She can:
- **a. Pay the *pelote*** (15 gold) and have the pledges back. +5 stress.
- **b. Appeal to the seneschal.** Roll 50 (+30 if she has served the lord as above, +15 if he likes her, +2×diplomacy) against 50 (+20 if he dislikes her). Win: "a novelty never seen", the pledges returned, +30 prestige. Lose: the seneschal will not cross the young men this year, −15 prestige, +10 stress.
- **c. Refuse. Let them keep the pledges.** +15 piety, +10 stress.

**Sources.** Arles, Shrove Tuesday 1433 (Hildenfinger's date, 24 Feb.): the abbot of youth and his fellows took pledges from the Jews for the *pelote*, a due "properly by newly married couples"; the seneschal's lieutenant called it "a novelty never seen" and ordered the pledges returned (Hildenfinger, *REJ* 41: 73 n. 1, 93–94, `jud_hildenfinger_arles_documents.md` §3.7 and §5.3; Stouff, "Chrétiens et juifs" §59, `jud_stouff_gross_arles.md` §2.5). Arles's own carnival in Kalonymus's day, with the "abbess of fools" (Ben-Shalom 2024, p. 96), shows a licensed reversal at Arles a century earlier, but nothing about the *pelote* or the Jews. The gate is 1400.

**Rules respected.** Christian harassment, attributed to the town's young men and their abbot, and a lord's protection; Jewish characters do nothing wrong. Stouff: the attacks came from "people of small condition", and the town's elite protected the Jews (§§60–61). Nothing from 1450 (the "Passion" case) or any Purim accusation. No expulsion foreshadowed.

**Open questions.**
1. *Decided:* gated at 1400.
2. The region gate is Frankish-heritage counties. Should it be narrower (only Provence and Languedoc)?

## 5. The lord's licence (drafted: `tm_hn2.0040`)

**What the player sees.** A landed ruler of the sect, with a daughter of the Turning under *niddui* at her court or among her vassals (half the years, within the budget): "The judges of the Jewish street have shunned [her] and they ask me to confirm the ban." Then, by date:
- before 1305: "The ban is pronounced in my land, so it is mine to license or refuse."
- from 1305: Abba Mari's line, "no community may ban one of its own without its lord's consent";
- from 1405: "In Provence the lords grant it for a year at a time, and keep absolution for themselves." She can:
- **a. "Absolution is mine to give. Lift the ban."** The *niddui* modifier is removed. −15 piety. The daughter +30 opinion (10 years). Jewish courtiers of other Jewish faiths −10 opinion (5 years).
- **b. "License it for one year, and no more."** The ban is cut to one year. +10 piety.
- **c. "The judges of the street have ruled."** +20 piety.

**Why this is the royal-faith feature.** In the observe runs the sect rules the Maghreb. `tm_turning_niddui_effect` already lets a *Christian* patron refuse the ban; a ruler of the sect has no say at all. This gives her the say that a medieval lord had, without inventing anything about the Maghreb. It also meets the worry recorded in `faith_design.md` §16 (item 23 undecided: the lord's veto "may read as a Christian lord protects her from the Jews"): here the lord who lifts the ban is of the sect, and she pays for it with the other Jews at her court.

**Sources.** Abba Mari, Montpellier c. 1305: "we have no right to excommunicate except with the consent of our lord" (Shatzmiller 2023, p. 86). Arles 1405: the archbishop's vicar licensed the ban for one year, each sentence to be notified to him, absolution reserved to him (Hildenfinger, *REJ* 41: 67 n. 5, 85–86; `jud_hildenfinger_arles_documents.md` §3.7). Manosque 1310: a rabbi indicted for an unlicensed ban (Shatzmiller p. 89). Montpellier 1305: the lord allowed one ban of three (pp. 86–87). All in `jud_shatzmiller_jews_of_provence.md` §3.3.

**Rules respected.** No supersessionist framing: Jewish law is not the enemy. Option c honours the judges, and the Rabbanite courtiers' displeasure at a is fair, not villainy. No expulsion. No mikveh.

**Open questions.**
1. Should the event also reach a Jewish ruler of another faith (Rabbinic, under whom the sect lives)? Drafted for the sect's own rulers only.
2. Whether `tm_turning_niddui_effect` itself should skip the ban when the county's holder is of the sect (see "Changes to existing files"). Then 0040 would only handle shunned daughters who live under other lords but are the ruler's vassals or courtiers. As drafted, the ban lands first and the ruler lifts it, which gives the player the choice.

## 6. A seat below (drafted: `tm_hn2.0050`)

**What the player sees.** From 1409, 5% a year (flavour budget), a member of the sect who is a daughter of the Turning or a seeker, at a court and with no seat yet: "A widow and her daughter are selling the seats they inherited: two in the men's school above, and one below, in the school of the women. In this street the seats belong to households, and the women of the house sit in them. The one below could be mine, in my own name." Outside a county with `tm_kahal` the desc says "one in the women's places" instead, since the room below is attested only at Arles.
- **a. Buy the seat below, in my own name** (20 gold): `tm_hn2_women_seat` (permanent) and the modifier *A Seat Below* (monthly piety +0.2). For a seeker, the seat adds **+10** to her Turning's prayer (`tm_hipukh.0001`), the same as going down to the women's synagogue that Adar. The two stack.
- **b. Let someone else have it.**

**AI.** Buy at base 50 (+20 seeker, ×0.3 greedy) against 30.

**Sources.** Arles, 31 Jan. 1451/52: Astrugia and her daughter Blanqueta sold "two in the men's school above" and "one below in the school of the Jewesses", 9½ florins for the three (Hildenfinger, *REJ* 48: 75–76; 47: 233). Dulcia, 1409, sold a seat "in the men's places, on the upper side" (Stouff n. 24). Gardeta, a widow, sold two seats in 1355 (41: 77–78). Seats in the women's room were listed by their neighbours' (men's) names: households owned seats (an *unverified* inference in the note). Women held and sold seats in their own name.

**Rules respected.** The seller is a widow of the street selling her inheritance. No lending and no conversion: Astrugia's husband's baptism in the deed is left out. The price is a modest 20 gold.

## 7. Catalan names of the street (drafted: an added option in `tm_hipukh.0002`)

**What the player sees.** At the naming on Shushan Purim, a new daughter in Catalonia or Aragon gets a third naming choice beside the scroll (Torah) names and the Provençal street names: "A name of the street, as the Jewish women of Catalonia are called." The option needs `tm_hn2_catalan_seeker_trigger`: from 1390, Catalan or Aragonese culture, or a county de jure in `k_aragon` (which holds `d_barcelona`). +25 prestige, as for the Provençal street names.

**Names** (`tm_hn2_catalan_name_effect`, weighted): Astruga, Bonafilla, Regina, Dolça, Bellaire, Orfila, Preciosa, Tolrana, Desiyada, Briona, Amoretes, Estel·lina. Girona notarial records, 1390s–1420s (Guerson and Lightfoot 2019, pp. 92–123; `jud_women_synagogue_articles.md` §4). Left out: Blanca, Constança, Francina and Elionor, the *conversas*' baptismal names (p. 108).

**Loc keys.**
- Astruga is already in `tm_l_english.yml`.
- Regina and Preciosa are vanilla keys.
- New keys in `tm_hn2_l_english.yml`: Bonafilla, Dolca ("Dolça"), Bellaire, Orfila, Tolrana, Desiyada, Briona, Amoretes, Estellina ("Estel·lina").
- ç and the middle dot are Latin-1, which the font draws, and the glyph check passes.

**Rules respected.** Tolrana is a real woman of the archive (her refusal on the tower steps, 1391). Her name is used for fictional daughters, as the street names are. She is never claimed as a member.

---

## The Maghreb: what the notes have, and what reading is needed

**Superseded by wave 3.** The reading below has been done (`docs/research/jud_maghreb_*.md`) and the Maghreb and Sahel content is built: see `docs/wave3/ha-nehpakhot-maghreb.md`. In the Maghreb and the Sahel, 0040 is replaced by `tm_hn3.0020` (the Two Parties), and `tm_hipukh.0003` lays the ban through `tm_hn3_niddui_effect`. This section is kept as the stage-2 record.

**The notes have nothing on Maghrebi Jewry.** I searched every `jud_*`, `isl_*` and `hist_*` note for Maghreb, Fes, Marrakesh, Morocco, Almohad, Almoravid, Qayrawan, Tlemcen, Sijilmasa, Tunis, North Africa and *dhimmi*. The only hits:
- Stouff, "Les juifs d'Arles" §§16–20: after about 1300 Provençal Jews "no longer had direct ties with North Africa" (`jud_stouff_gross_arles.md` §1).
- Gross, p. 401–402: the byname Narboni spread as far as Algiers.
- `hist_ayalon_eunuchs_caliphs.md`: Fatimid and Almohad *eunuchs*, nothing on Jews. It must not be used for the sect (the slave- and eunuch-trade guardrail).

So I propose **no Maghreb-specific content**. Feature 5 is the royal-faith feature, and 1 and 2 work there as they are. Texts that name Arles offices (`tm_hipukh.0003`'s dated judges, "the women's synagogue below the men's") will read oddly at Fes; see "Changes to existing files" 3.

**Reading that would be needed** (none of it is in the repo; titles from general knowledge, to be checked before use):
1. A general history of North African Jewry for the 9th–15th centuries: H. Z. Hirschberg, *A History of the Jews in North Africa*, vol. 1 (1974). For the community's structure under Muslim rulers (*nagid*, *dayyan*, the community's dealings with the ruler).
2. The Cairo Geniza on Maghrebi and Ifriqiyan families and women: S. D. Goitein, *A Mediterranean Society*, vol. 3 (*The Family*); Menahem Ben-Sasson on Qayrawan. For women's names, trades and marriage documents, as Shatzmiller and Hildenfinger gave for Provence.
3. Fes: Jane Gerber, *Jewish Society in Fez 1450–1700* (1980), mostly after the game, and work on the Marinid period (Corcos, *JQR* 1964). For the period the sect actually rules, a source on Jews at the Idrisid and Almoravid courts would be the real need.
4. The Almohad period (1140s on) has forced conversions. Any use would need a separate decision: expulsions are not modelled, and persecution must not become a mechanic.
5. *Dhimmi* law as applied in the Maghreb, to know how a Jewish ruler would even be read by Muslim neighbours (the game already makes a Ha-N king; the faith's own voice about that needs a source).

Until such reading is done, the honest position is the one in the docs: the sect's texts and customs are Provençal, and a Maghrebi kingdom of the sect is a game outcome.

---

## Survival balance: ideas only (not built)

The kahal never recruits (joins 0 all run) because the yearly join needs a Rabbanite Jew at a court with two or more members, and the sect's courts in the Maghreb hold few such Jews. Ideas for the later task:
1. Let a **landed ruler of the sect** count as a kahal: Rabbanite Jews in her capital county, not only at her court, may join (same 4%).
2. Let the matchmaking spouse come from the ruler's realm when the sect rules, not only from "outside the courts".
3. *(Built in wave 6 as Send for a Household of the Street.)* A ruler of the sect could **invite a household of the street** (a decision, gold for travel, as the Arles contract of 1422 paid a man to bring a wife and child from Barcelona, Stouff "Les juifs d'Arles" §16). That is sourced and is service, not purchase of protection.
4. The Carnival appeal (4) and the bailiff (3) give daughters in Christian lands a reason to stay near a patron; a won appeal could raise the court's draw for the pilgrimage. Tuning only.

---

## Changes made to existing files (user-approved, 2026-10-21)

All edits are in the worktree only, and each is marked with a `tm_hn2` comment.
1. **`events/tm_hipukh_events.txt`, `tm_hipukh.0001`** (the prayer). One line in the success weights: `modifier = { add = 10 has_variable = tm_hn2_women_seat }`.
2. **`events/tm_hipukh_events.txt`, `tm_hipukh.0002`** (the name). One new option, `tm_hn2_catalan_name_option`, with `trigger = { tm_hn2_catalan_seeker_trigger = yes }`, calling `tm_hn2_catalan_name_effect`, +25 prestige. Options a (scroll) and d (Provençal street) are unchanged.
3. **`events/tm_hipukh_events.txt`, `tm_hipukh.0003`** (the hearing).
   - In `immediate`: if the county has `tm_hn2_spindle_heard`, save the scope value `tm_hn2_spindle_heard = yes` and remove the county variable; else save `no`.
   - In options a and e: `modifier = { add = 10 scope:tm_hn2_spindle_heard = yes }`.
4. No change to `localization/english/tm_l_english.yml` or `tm_custom_loc.txt`. The new option's loc and the name keys are in `tm_hn2_l_english.yml`.

### Still proposed, not made
1. **Royal faith, `tm_hipukh.0003` and `common/customizable_localization/tm_custom_loc.txt`** (optional). The judges' names are Arles offices by date (worthies, rectors, baylons, council). Add a first `text` to `tm_kahal_judges`, `_cap` and `_title` for a court outside Provence, e.g. `trigger = { NOT = { location ?= { county ?= { culture ?= { has_cultural_pillar = heritage_frankish } } } } }` → "the worthies of the street". The 1401 council bonus already needs `tm_kahal`, so it does not leak.
2. **`common/scripted_effects/tm_rite_effects.txt`, `tm_turning_niddui_effect`** (optional; see feature 5, question 2). I recommend **not** doing it, so the player keeps the choice in 0040.
3. **`docs/TODO.md`**: tick the stage-2 inputs used here and add a "Ha-Nehpakhot, stage 2 (untested)" block. **`docs/TO-TEST.md`**: the scenarios below. **`docs/faiths/ha-nehpakhot.md`** and the README: one line each, after review.

## Test scenarios (for TO-TEST.md)

- **0001.** Give a daughter of the Turning a court with women of her faith and fire `tm_hn2.0001`. Check each option, and `tm_hevrah_taught` on a seeker pupil. Before 1105 the Sarah option has the Talmud text. Before 1323 the desc has no Touchstone line.
- **0002.** Set `tm_hn2_spindle_talk` and fire `tm_hn2.0002` at 1066, 1200 and 1350. Check the Talmud and Rashi variants, the Torah and Ḥinukh lines, the roll, and the *Teach Her the Answers* bonus.
- **Spindle → hearing.** Win 0002.a and check `tm_hn2_spindle_heard` on her county. Then run a seeker's Turning to `tm_hipukh.0003` in that county: the tooltip for a and e shows +10, and the county variable is gone after the hearing. A second hearing there has no bonus.
- **0010 and 0011.** Marry a daughter of the Turning at 1100, 1200 and 1330; check the desc variant at each. On the spouse, give the necklace and check the artifact (name, desc, icon, modifier, no decay). A second marriage offers none.
- **0020.** At 1300, a daughter with a rival, living in a Christian-held county. Check the served option with and without `tm_translation_patron_modifier` on the county holder. Before 1260 it does not fire.
- **0030.** A member at a Christian Occitan court after 1400. The hidden wait reaches February. Check each option. Before 1400 it does not fire.
- **0040.** A landed ruler of the sect with a shunned daughter at court (give her `tm_niddui_modifier`). Check each option, and the desc at 1200, 1350 and 1420.
- **0050.** From 1409, a seeker of the sect at the count of Venaissin's court: the Arles desc. Elsewhere: the plain desc. Buy the seat; her next Turning prayer shows +10 for the seat. Before 1409 it does not fire.
- **Catalan names.** A seeker at Barcelona (or of Catalan culture) after 1390 who is turned. At the naming, the scroll, Provençal and Catalan options all show, and the Catalan option gives a name from the list with its loc (Dolça, Estel·lina drawn correctly). In Provence the Catalan option is hidden.

## Syntax I am unsure of

- `set_variable` on an artifact scope (after `create_artifact … save_scope_as`) and `any_character_artifact = { has_variable = … }`: xTiger accepts both; unverified in game.
- `create_artifact` with `type = necklace` and `visuals = necklace` and no features: vanilla does the same (`tour_phase_cultural_festival_james.txt`), so the required features should be filled automatically.
- The Carnival court list is guarded with `is_in_list` before `add_to_list`, so each court rolls once a year whatever the engine does with duplicates.

## Survival fixes after run 15 (2026-10-25, untested)

Run 15 (867–1210) lost the sect in the 1040s. Its only home was Bonadonna's camp, which passed in 906 to an eight-year-old great-grandson of another faith and was dissolved that day; the members scattered over ten courts, married out, and all ten children of member mothers died in another faith. Run 13 survived only because a member took a Breton mercenary band in 897.

- **Descent through the mother.** The born-in-faith rule skips a child born into the house of a father of another faith (the fix for Yutai's Mandate). Ha-Nehpakhot mothers are now exempt: the child of a Jewish mother is Jewish (Mishnah Kiddushin 3:12). The sect is landless, so no throne follows from it.
- **The camp passes to the community** (`common/on_action/tm_hn_camp_on_actions.txt`). An AI camp leader of the sect whose heir is a child or of another faith adopts the ablest grown woman of the community in her camp and names her heir, as the faith's Houses continue by adoption. A player decides for herself.

Held back unless the next run still shows no newcomers: a weak yearly draw of an unmarried young Jew to the community's court when it has no land, and a gathering that prefers the community's court to another faith's House.
