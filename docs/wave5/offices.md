# Wave 5: the faiths' own offices

User: "we're building *trans-women religions*, not just trans-affirming ones that provide transition care." Each faith now has one office of its own, held only by a daughter of that faith. Cis women stay members and sisters; they don't hold the office.

## What was built

Six court positions (`common/court_positions/types/tm_voice_court_positions.txt`). Every one of them:
- is shown to any ruler of the faith with a court (county tier and up, landless adventurers included, as with vanilla `court_physician_court_position`);
- takes only an adult daughter of that faith (`tm_voice_office_holder_trigger`: `faith`, `is_adult`, `tm_is_daughter_trigger`) plus vanilla `base_court_position_validity_trigger`;
- pays a piety salary (`minor_court_position_piety_salary`, 0.5 a month), not gold. It is a religious office, and this keeps the Elder of the Lamp clear of money;
- has AI weights that fill it whenever a valid daughter is at court: `ai_position_score = 100`; `ai_candidate_score = 200 + court_position_candidate_score_base_value + court_position_candidate_aptitude_value`. The gold terms (`scope:base_value`, debt) are left out because the office costs no gold. A daughter who already holds another office still scores above 0 when hired. When firing, the -150 does not apply, so there is no hire/fire loop;
- gives one small employer modifier and one small holder modifier, and has a custom employer tooltip.

| Faith | Office | Who | Employer | Holder | Its job |
|---|---|---|---|---|---|
| Adelphai Dorleyaiou | Companion of the Mothers (up to 3 seats) | daughter of the faith, only at the court of the holder of `d_tm_mother_house` | piety gain +5% | learning XP +10% | Taking the seat makes her a Companion (`tm_companion_modifier`, if there are fewer than seven). The Companions back a daughter for the Mother House (below). |
| Bædlings | Völva of the Hall | **daughter of seiðr only** | stress loss +5% | learning XP +10% | Sings the seiðr at her court (`tm_seidr_begin_effect` picks her first); the rite gets +10 when she sings. |
| Yutai Dao | Head of the Society | daughter of the faith | same-faith opinion +3 | diplomacy +1 | +10 to both Jade Embryo trials (`tm_embryo.0010`, `0011`) for an adept at her court. |
| Ha-Nehpakhot | Elder of the Lamp | daughter of the faith | learning +1 | learning XP +10% | Reads at the Turning (`tm_turning_begin_effect` picks her as `tm_zekenah` first); +10 when she reads. |
| Worn Garland | Eldest of the Street | daughter of the faith | prestige gain +5% | diplomacy +1 | Keeps the pāvai vow (`tm_pavai_begin_effect` picks her as `tm_garland_elder` first); +10 when she lays the staff. |
| Badenya | Mother of the Roof | daughter of the faith | courtier and guest opinion +5 | diplomacy XP +10% | Claims the new woman at the crossing (`tm_badenya.0011`) when no woman of her family will, before the rite falls back on any friendly woman at court. No one waits for a mother. |

Aptitude: the office's skill ×2.5 (max 50), plus learning or diplomacy, plus "her years" (age − 30, ×0.5, 0–15) for the four offices held by elders (Völva, Elder, Eldest, Mother of the Roof).

**All six**, in addition:
- **The call** (`tm_sisters_call_effect`): +2 to the chance when the seeker's employer is of the call's faith and has her office filled. Next to the existing terms, that is small: the "member at court" term is +8.
- **House strain** (`tm_house_yearly_effect`): when a House's lord has the office filled, a 33% chance each year that strain falls by 1 (only while it is above 0).

A court of the faith without the office simply lacks these. Nothing penalises a ruler.

### Why the Völva needs the seiðr trait
The völva sings the varðlokkur and goes up on the high seat. The rite already takes its völva only from daughters of seiðr (`tm_seidr_begin_effect`), so the office holder is the völva the rite would have looked for. A daughter of another gate who later joined the Bædlings (rare) can still be a sister, but not the hall's seeress.

## The Mother of Mothers leans to daughters

`common/on_action/tm_voice_on_actions.txt` (yearly_global_pulse) → `tm_voice_companions_back_daughter_effect` (`common/scripted_effects/tm_voice_effects.txt`), scope `title:d_tm_mother_house`.

- Runs when the holder is of the faith and is 60 or older, or ill (`ill`, `pneumonic`, `infirm`, `incapable`), or no valid daughter is backed yet.
- **Choice.** The pool is adult, free daughters of the faith among the Mother's courtiers and vassals (`tm_voice_backable_daughter_trigger`). Clerical_christian's `default_candidates` are `holder_councilor holder_court_position direct_subject clerical_region_clergy...`, and courtiers and vassals cover the first three. The best is the one with the highest `appointment_candidate_score(scope:tm_voice_mh)`, the appointment's own score. She is stored as `var:tm_voice_backed` on the title.
- **Backing.** Companions (`tm_voice_is_companion_trigger`: the modifier or the seat, of the faith, adult; not the Mother or the backed daughter herself; ordered by learning) each put `change_appointment_investment = { target investor value = 25 }` on the title, once per Companion (`succession_appointment_score_invested < 25`). The total is capped at 75 (`var:tm_voice_backed_sum`). Companions need not live at her court: `clerical_christian` has `allow_out_of_realm_investment = landless`, and the Mother House is landless.
- **Re-targeting.** If the backed daughter dies, leaves the faith, the Mother's court or her vassals, or becomes the Mother, the next run chooses again and the sum starts from zero. A new Mother (`var:tm_voice_backed_for`) also starts afresh.
- **Size.** In `clerical_christian.txt` the same-rite bonus is +50, a vassal +25 and a courtier +15. Each scholar level is worth +10 to +75, and age 40–69 is worth +20 to +35. +75 is about one strong advantage. A daughter who is a plausible candidate usually wins; a cis woman with a much better score (a landed prelate, a scholar, a strong hook) still can. A seated Companion also gets vanilla's +10 for holding a court position.

### Can a Marked woman (game-coded male) be a candidate under `doctrine_clerical_gender_female_only`?
Not settled from script. `clerical_christian.txt` has no gender term, and the doctrine's only effect is the parameter `clergy_must_be_female`, which the engine reads. If the engine filters appointment candidates by clergy gender, a Marked woman is not a candidate. If it does not, she is, with the same score as anyone. This mechanism never backs Marked women, only daughters. With the default rule `tm_reembodiment_on` a daughter is game-coded female and valid either way. With `tm_reembodiment_off` a daughter stays game-coded male, and the same question applies to her: the Companions might back someone the engine then skips (their 75 is wasted, nothing breaks). Test S5 below settles it.

## Edits to existing files (minimal)
- `common/scripted_effects/tm_rite_effects.txt`: in `tm_seidr_begin_effect`, `tm_turning_begin_effect` and `tm_pavai_begin_effect`, a first `if` that takes the office holder at the host's court (not the seeker, not imprisoned). The old first `if` becomes `else_if`.
- `events/tm_seidr_events.txt` (tm_seidr.0001), `events/tm_hipukh_events.txt` (tm_hipukh.0001), `events/tm_garland_events.txt` (tm_garland.0001): one `modifier = { add = 10 ... }` line each, when the völva, zekenah or elder holds the office.
- `events/tm_embryo_events.txt`: one +10 line in each of `tm_embryo.0010` and `0011`.
- `events/tm_badenya_events.txt` (tm_badenya.0011 immediate): the Mother of the Roof as claimer, between family and any friendly woman at court.
- `common/scripted_effects/tm_growth_effects.txt` (`tm_sisters_call_effect`): one +2 modifier.
- `common/scripted_effects/tm_house_effects.txt` (`tm_house_yearly_effect`): the 33% strain relief.

New: `common/court_positions/types/tm_voice_court_positions.txt`, `common/scripted_triggers/tm_voice_triggers.txt`, `common/scripted_effects/tm_voice_effects.txt`, `common/on_action/tm_voice_on_actions.txt`, `localization/english/tm_voice_l_english.yml`.

## Uncertain syntax
- A piety-only `salary`: documented in `_court_positions.info`, but no vanilla position uses it. Watch the court position window and error.log.
- `order_by = "appointment_candidate_score(scope:tm_voice_mh)"` in `ordered_in_list`: the string form is vanilla's (06_ep3_interactions.txt), but there it is used in a `value`.
- `change_appointment_investment` with `investor`: vanilla uses it so in 06_ep3_interactions.txt. Unknown: whether a dead investor's share stays, and whether investments clear on a new holder (the code starts afresh either way).
- That `d_tm_mother_house` really uses `clerical_christian` (the brief and the run say so). If not, the investment does nothing and breaks nothing.
- ck3-tiger: 25 reports, none in these files. That is the baseline 23 plus 2 from the lead's work in progress (`tm_bookmarks.txt` missing .dds, `d_laamp_tm_lamp_adj` loc).

## Test scenarios (TO-TEST style)
- **S1 The offices appear.** Play a ruler of each faith with `tm_make_sisters.txt` (adult daughters). The court positions window shows the faith's office. A daughter is valid. A cis woman of the faith and a Marked woman are not. For the Bædlings, only a daughter of seiðr is valid.
- **S2 AI fills them.** Observe 10 years. Every AI court of a faith that has an adult daughter courtier should hire her. Check debug.log for hire/fire churn on `tm_voice_*`.
- **S3 The gate hooks.** With the office filled: `tm_seidr_now.txt` shows the Völva of the Hall as the völva. `tm_turning_now.txt` shows the Elder of the Lamp as the elder. `tm_pavai_now.txt` shows the Eldest of the Street. `tm_crossing_now.txt` with no female family has the Mother of the Roof claim her. Each random_list shows the +10 line in its tooltip. Jade Embryo trials show +10 with a Head of the Society.
- **S4 Companions.** As or watching the Mother of Mothers: seat a daughter as Companion of the Mothers. She gains *Companion of the Mother* (unless seven exist). Use `tm_name_companion_interaction` too: it still works and is hidden for someone already a Companion.
- **S5 Succession.** Set the Mother's age past 60 (`age 61` on her) or make her ill. Name 3 Companions and keep a daughter courtier. After a yearly pulse, the title's succession view should show the daughter with +75 from three investors, and she should be the current heir unless someone much stronger is there. Kill the daughter: the next year another daughter is backed. Add a Marked woman courtier: does she appear among the candidates at all? (She is never backed; this answers the clerical gender question.) Repeat with the rule `tm_reembodiment_off`.
- **S6 Strain.** A House with strain 3 under a lord with the office filled: over several `tm_house_tick.txt` runs strain should sometimes fall by 1 more than without.

## README text (ready to paste, under Shared mechanics)
- **The faith's own office.** Each faith has an office that only its daughters hold: the Companions of the Mothers at the Mother House, the Völva of the Hall, the Head of the Society, the Elder of the Lamp, the Eldest of the Street and the Mother of the Roof. Any ruler of the faith may appoint one; the AI does whenever a daughter is at court. She keeps the faith's gate at that court (the völva sings the seiðr, the elder reads the scroll, the eldest lays the staff, the Mother of the Roof claims the new woman, the society stands by the adept), the call reaches the court a little more readily, and its Houses bear their strain more easily. When the Mother of Mothers grows old or ill, her Companions put their weight behind a daughter to follow her.
