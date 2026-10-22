# Wave 3: survival balance

Roadmap item: "the small faiths' Houses keep their numbers, the kahal recruits, daughters stay". Prefix `tm_surv_`.

## Diagnosis (fourth observe run, 867 to 1200, `run4/snap.ck3` and `run4/census.txt`)

Save scripts used: `surv/an.py` (members by court type), `surv/rab.py` (Jewish characters by faith and court), `surv/dau.py` (daughters living and dead), `deaths.py` (Yutai death reasons). All in the session scratchpad.

**1. The kahal never recruits.** The join needs a Rabbanite Jew (Rabbinic or Malabar) who is a courtier at a court with two or more of the sect. In the 1200 save the whole world has **3 Rabbinic Jews and 10 Malabar Jews** (2 courtiers, 1 ruler, 8 in the pool), and **no county of Rabbinic Judaism**. In the 1135 save of an earlier run, 1 and 7. The game hardly makes Rabbanite Jews as characters, and none live where the sect does (its courts are Sunni, Christian, Akom). So no trigger on existing characters can fire, however loose. Before fix C, joins came from Kabarists (88 alive in 1200), which the user ruled out. The sect is otherwise healthy (698 members): it grows by matches (70–100 a decade) and conquest.

**2. Daughters.** Daughters mostly die old in their faith: of 52 unprunable dead daughters of the knife, the median age at death is 55, and 6 died Orthodox (about 10%); of Badenya's, 8 of about 70 died Sunni. What keeps the Adelphai at 1–5 daughters is intake (2–9 rises a decade, from 0–7 Marked members), not loss. But of the 3 daughters of the Adelphai alive in 1200, **2 were wandering guests** with no court, and 7 of the faith's 35 members were guests. The old way home (`tm_homecoming_effect`) served only Bædling and Mālai, and used `is_pool_character`, which the game documents as excluding guests, so it never reached them.

**3. A faith after losing its land.** Badenya held 16 counties and 31 rulers in the 1040s. After k_mali fell (1037), its pool deaths rose to 85–164 a decade (1040s–1080s) while members fell from 306 to 75 by the 1100s: the households of fallen courts went to the pool and died there, unmarried. The census had no way home for Badenya, the Adelphai or Yutai Dao. A dead ruler's household stays at the heir's court even when the heir is of another faith, where the vanilla AI asks courtiers to convert (`ask_for_conversion_courtier_interaction`, base acceptance 50) every 15 years.

**4. Yutai deaths.** `tm_n_deaths` counted every death of a member with a court or a ruler. In the 900s it counted **462 deaths with 84 members**; in the 1130s **2215 with 958**. The save's unprunable dead of the faith number 9 and 151 for those decades. The counter does not count twice (one hook, one call), but it counts characters that are members for only a short time: the game makes and clears characters at Chinese courts by the hundred, and a character made with a court and cleared before the next census was counted as a member's death. The spikes (1100s–1140s) fall when Yutai members lived inside the Chinese empire.

## What was built

| Change | File | Numbers | Why |
|---|---|---|---|
| **The kahal of her town** (`tm_surv_kahal_draw_effect`) | `tm_surv_effects.txt`, called from `tm_yearly_growth` | each landed ruler of Ha-Nehpakhot (barons included), 2% a year, +2 if her capital county is of the sect's faith | A Jewish lord's lands draw Jews. A Rabbanite Jew at her court or in her capital's pool comes first; otherwise a young Jew of the wider Jewry (16–30, either sex, her culture) comes to her court, as the matches and pilgrims already model the Jewry the game does not make. Counted as `kahal_joins`. |
| **Kahal join widened** | `tm_on_actions.txt` | still 4% a year | Also counts a Rabbanite Jew at the court of a landed ruler of the sect or her vassal, or one with no court in a county of such a realm. Rarely fires (the game has almost no Rabbanite Jews), but now it can. |
| **Matches inside the realm** | `tm_kahal_match_effect` (`tm_growth_effects.txt`) | unchanged 15% | If her court or its capital's pool has an unmarried, fertile Rabbanite Jew of the other sex aged 40 or under, the match is with them, and they join (counted as a kahal join and a match). Otherwise a spouse is made, as before. |
| **`tm_surv_kahal_take_in_effect = { COURT = <ruler> }`** | `tm_surv_effects.txt` | — | For the Ha-N Maghreb builder's refuge decision: the person takes the sect's faith (a kahal join if she was not of it) and joins COURT's court if she is not a ruler. |
| **The gathering** (`tm_surv_gather_effect`), replaces `tm_homecoming_effect` | `tm_surv_effects.txt` | 20% a year (as the way home) | All six faiths. Members with no court **or visiting as guests** who are daughters, novices, Marked, declared, **or not lowborn** (a fallen realm's families). They go to the nearest court of their faith (by map distance; companies and holy orders excluded), else the nearest lord keeping a Sisters' House, else the seat's holder (for the Adelphai, the Mother of Mothers). Lowborn pool characters stay, as before: the game makes and clears them by the hundred in a faith's counties. Counted as `pilgrims`. |
| **A dead ruler's household** | `tm_surv_on_actions.txt`, `tm_growth.0010` | — | When a ruler of the six dies with an heir of another faith (or none), her unmarried daughters, novices, Marked women and declared seekers at court (not the heir or the heir's close family) go to the nearest court of their faith 7–30 days later, after the heir has the court. Counted as `pilgrims`. |
| **The faiths keep their children** (`tm_surv_keeps_children_effect`), replaces `tm_kahal_keeps_children_effect` | `tm_surv_effects.txt` | — | The kahal's rule, for all six: an AI guardian of another faith may teach a child of the faith, but not convert her. A player's choice stands. |
| **Death counter** | `tm_on_actions.txt` | — | Members are marked `tm_surv_seen` just before each census. `deaths` counts only members seen at a census who die with a court or as rulers; the rest go to `pool_deaths`. |
| Report text | `tools/census_report.py` | — | A note under the tables on what `deaths`, `pool` and `pilgr` now mean. |

No caps, no rate scaled by size. No new loc (all hidden).

## Expected effect on the census

- **Ha-Nehpakhot `kahal`**: from 0–4 a decade to about 1 a decade with 1–5 landed rulers (900s), and 6–16 with 20–40 (now). Each newcomer is unmarried, so most are matched within a few years: about +15–30 members a decade at today's size, against 70–100 matches. Slow, as before.
- **`pilgr`** for the Adelphai, Badenya and Yutai Dao: from 0 to a few a decade in quiet times (the Adelphai's 7 guests would mostly be home within 5–10 years), and tens a decade after a realm falls. **Badenya's `pool` deaths** after a fall like Mali's should drop by a share I cannot estimate from the save (it does not say which of the dead were highborn); members should fall more slowly than 306 → 75 in 60 years. Bædling and Mālai: as before, plus guests and highborn members.
- **Daughters**: a small rise for the Adelphai (guests come home, a dead ruler's daughters leave a foreign heir's court); intake still sets their number. I did not raise the call or rite rates.
- **Yutai `deaths`**: roughly 150–350 a decade at 1000–1400 members (a lifetime of about 45 years); the old spikes move to `pool`. Early-decade deaths before the first census also go to `pool`.
- **Yutai Dao** will gain a little from keeping its children and gathering its highborn members. The user accepted Yutai running away; watch it.

## Overlaps and coordination

- **Ha-N Maghreb builder**: call `tm_surv_kahal_take_in_effect = { COURT = <ruler scope> }` on each refugee (scope: the refugee). It sets the faith, counts a kahal join, and moves her to COURT if she is not a ruler. It does not create anyone.
- **Bædling builder (landless/adventurer settling)**: the gathering sends Bædling members with no court to the nearest court of their faith; an adventurer's camp counts (`tm_settled_court_trigger` lets camps in). If their settling help also moves pool members into camps, the two overlap but do not conflict (each moves only characters without a court of their faith). Bædling's seat fallback still reads `global_var:tm_baeddel_seat`.
- **Badenya builder (`tm_bd2_on_death`)**: separate hook on the same `on_death`; theirs sends events to the heir, mine moves the unmarried household of a ruler whose heir is not of her faith. No shared scopes (mine are all `tm_surv_*`).
- **Seat to a member (`tm_seat_on_death`)**: the household moves days later, by event, so the member who takes the seat is a ruler by then and stays.

## Uncertain syntax

- `ordered_ruler` lists rulers of count tier and above (game docs). Barons (Ha-N's burgher towns) are not homes in the gathering; the kahal draw loops `every_living_character` so barons are included there. Whether landless adventurers count as "count tier or above" in `ordered_ruler` is not documented; if not, camps are not homes in the gathering.
- `faith_filter = scope:tm_surv_seeker.faith`: vanilla uses `faith_filter = scope:target.faith`.
- `subtract = "location.squared_distance(scope:tm_surv_from)"` in `order_by`: vanilla uses the same form with `title_province`.
- `is_pool_guest`: from the game's trigger docs; xTiger accepts it.

## Test scenarios (TO-TEST style)

- **The kahal of her town.** Give Ha-Nehpakhot a landed ruler (debug: `set_character_faith` on a count, or play one). Run `effect = { every_living_character = { limit = { faith = faith:tm_nehpakhot is_landed = yes } tm_surv_kahal_draw_effect = yes } }` about 30 times (or wait 10 years): a young courtier of the sect should appear at her court now and then. `tm_census.txt` before and after; the faith's `tm_n_kahal_joins` should rise.
- **Take in.** `effect = { create_character = { age = 20 faith = faith:catholic save_scope_as = x } scope:x = { tm_surv_kahal_take_in_effect = { COURT = root } } }` as a ruler: x is of the sect and at your court.
- **The gathering.** Move a daughter of the Adelphai to the pool (`move_to_pool`) far from Phrygia. Within about 5 years (20% a year) she should be a courtier of the nearest ruler of her faith, or the Mother of Mothers. A lowborn ordinary member in the pool should stay put.
- **A dead ruler's household.** A ruler of Badenya with an unmarried daughter of the House at court and a Sunni heir: kill her (`kill`). Within a month the daughter should be at the nearest Badenya court. With a Badenya heir, nothing moves.
- **Children.** As for the kahal before, with a child of Badenya at an AI Sunni court: the convert flag on the guardian should be gone within a year.
- **Death counter.** In the next observe run Yutai `deaths` should stay below about a third of members a decade; compare `pool`.

## Ready to paste

README (Shared mechanics, growth):

> **The gathering.** Members of the six with no court, or only visiting one, who are daughters, Marked, declared or of a family of standing go to the nearest court of their faith (20% a year), else to a lord who keeps a Sisters' House, else to the seat. When a ruler of the faith dies with an heir of another faith, her unmarried daughters and Marked women leave for the nearest court of the faith. Guardians of another faith may teach the faiths' children, but not convert them.
>
> **The kahal of her town.** A landed ruler of Ha-Nehpakhot draws Jews of her lands to her court (2% a year, 4% if her capital is of the sect); the kahal's matches marry Rabbanite Jews of her court first.

README Roadmap: tick "Survival balance from observe runs" once an observe run confirms it.

TODO (Testing):

> - [ ] Survival balance (docs/wave3/survival.md): the kahal of her town, take in, the gathering, a dead ruler's household, children kept, the death counter

Doc references to update (lead's files): `tm_homecoming_effect` (docs/faith_design.md §14 fourth-run note, docs/silk_and_silver.md) is now `tm_surv_gather_effect`; `tm_kahal_keeps_children_effect` (docs/TODO.md, docs/faith_design.md fifth-run note) is now `tm_surv_keeps_children_effect`. `tools/gen_tracking.py` HEADER line "pool_deaths are characters the game cleared away ..., deaths everyone else" should read "deaths are members seen at a census who died with a court or as rulers; pool_deaths everyone else" (then regenerate).

## Decisions (user, 2026-10-21)

- **Kahal joins may create characters.** The kahal of her town makes a young Jew of the wider Jewry when no Rabbanite Jew is at her court or in her capital, as the matches and pilgrims already do.
- **Refugees keep their own faith** (Ha-N Maghreb, `tm_hn3_receive_refugees_effect`): the refuge decision no longer calls `tm_surv_kahal_take_in_effect`. The effect stays available for other callers.
- README roadmap: the first pass is ticked as built but the item stays open, "to be checked in observe runs".
