# Bædling, wave 7: the sorcery law, the rest of the feud and outlawry, and Norse lore

Roadmap items (README, "Larger"): the sorcery-law arc; the rest of the feud; the rest of outlawry; Norse lore events. Built 2026-10-25, untested in game (`docs/TO-TEST.md` AH). Validated with xTiger (no reports in these files; the mod stays at its baseline of 23) and `tools/check_glyphs.py`.

The build spec consolidated the Norse notes (Miller, Ahola, *Grágás*, Mitchell, Jochens, Tolley, Price, Gade, Damico) and today's v2 readings (Raudvere in Athlone vol. 3; Mitchell's chapter in *Contesting Orthodoxy*; the Rykener notes). Shared date-and-region triggers are in `common/scripted_triggers/tm_bae3_triggers.txt`:
- **Iceland** (de jure `d_iceland`): the one who hired a seeress is liable, and twelve jurors may clear her client (user decision 2026-10-25).
- **Norway**: the seeress is liable, and six housewives may clear her. Magnus's New Law, 1164–1200: goods to the lord and his chaplain.
- **Capital law**: Norway from 1300, Scania from 1328, Sweden from 1350, reached only on a relapse after a penance (Bergen 1324–25).

Counts for observe runs: `tools/census_report.py`, the three "wave 7" sections.

## 1. The sorcery law in the suit, and the rest of outlawry

### What was built

**1b. The suit by region (`tm_bae2.0100/0101`).** The court's law comes from the lord's capital, read through `tm_bae3_triggers.txt`.
- **Iceland, the sorcery charge** (`tm_bae3_lord_icelandic_trigger`). Icelandic law holds the one who hired the seeress liable (Raudvere pp. 155–61). The charge falls on her client, `var:tm_bae2_last_seeker` on the seeress (`tm_bae2_has_client_trigger`). The client gets 0101, and option (a) reads "Twelve jurors will clear me" (Grágás; Mitchell p. 159).
  - **Nothing in the mod stores a seeker today.** `tm_seidr.*` and `tm_rite_effects.txt` keep no seeker and no völva after the rite, and no hook inside the tm_bae2 files can see the rite.
  - Until something stores one, the Icelandic sorcery suit **falls**. The lord sees the charge, reads "No one will name who asked her to sit", and has a single option, "Then there is no suit." This is counted as tally `out_iceland_no_client`.
  - The client is recorded when a seeress sits (`tm_seidr.0001`: `var:tm_bae2_last_seeker` on the völva).
- **Norway** works as before: six housewives.
- **Magnus's New Law, 1164–1200** (`tm_bae3_lord_magnus_law_trigger`): forfeited silver goes half to the lord and half to his court chaplain, or all to the lord if he has no chaplain. Everywhere else it goes half to the accuser and half to the lord (Grágás K §53; Gade rows 5–6).
- **"Charged as a man" was not built**, not even as a record line. The user said "if at all", and it would add a misgendering line for no mechanical gain.
- *Kveldriða* (the accuser's word in the spec) is not used. As "night-rider" it brushes against rule 25 (no bodily flight).

**1c. The secular arm.** In the yearly pulse, if she is `tm_bae3_under_condition_trigger` and the lord is `tm_bae3_lord_capital_law_trigger`, the scope `tm_bae2_relapse` is set.
- 0100 then shows the relapse text and the option "Take her into my keeping", which runs `tm_bae2_secular_arm_effect`: vanilla `imprison`, type dungeon. The text ends at the cell door. Vanilla's prison interactions are his.
- She gets `var:tm_bae2_secular_arm`, which `tm_bae2_cell_prisoner_trigger` now counts, so **Spring the Cell** can always free her.
- **Rescue the Daughters** (not my file) only covers daughters, Marked women and novices. A seeress who only knows the songs is not covered by it.
- The 4% pulse is unchanged.

**1d. Penance.** From 1300, for the sorcery charge only (a church sentence), 0101 has option (d), "Penance and the pilgrim roads". It runs `tm_bae2_penance_effect`:
- the new `tm_bae2_penance_modifier` for 7 years (−0.2 prestige a month, +10% stress gain; not outlawry, so no one may kill her for it);
- `set_variable = tm_bae3_under_condition`, with no expiry;
- `tm_bae2_go_abroad_effect`.

The AI favours it (base 60), since women were "acquitted, sent on pilgrimage, or exiled" (Mitchell pp. 169, 197). The name "Ragnhildr" and her charm are not used.

**3a. The confiscation court (`tm_bae2.0105`).**
- **Pending.** The ring (b), the woods (c) and a failed oath now run `tm_bae2_call_court_effect`. It sets `var:tm_bae2_pending_court` (flag:lesser or flag:full, 30 days) and fires 0105 to the accuser 14 days later (K §53; Ahola p. 97).
- **Failure chance.** `tm_bae2_court_fails_value` (new file `common/script_values/tm_bae2_values.txt`): 20 base, +20 if she is a House member with a House in her county, +15 per adult `tm_sister` at her court (two at most), +20 if she leads a band.
- **If the court fails**, the sentence lapses and the accuser loses minor prestige ("200 men of good will", Miller p. 267).
- **If the court holds**, she pays the life-ring (min(gold, 10)) or forfeits all her gold, split as in 1b. Only then do the old lesser or full effects run, so the full-outlaw band forms only after the court.
- **If the accuser dies first**, the flag runs out and nothing happens: no lawful court, no sentence.
- **Nothing else that relies on the sentence breaks:**
  - the níð suit uses its own `tm_feud_nid_outlawry_effect`, which still takes effect at once;
  - reprieves, settlement and pardon all read the modifiers, which do not exist until the court holds;
  - `tm_bae2_outlawry_candidate_trigger` excludes anyone with a pending court.

**3b. Ride for Sympathy.** Decision `tm_bae2_ride_for_sympathy_decision`, in the adventurer group, for player band leaders who are full outlaws. The AI rides from `tm_bae2_yearly_bands` at 10% a year.
- **Well-wishers** (`tm_bae2_well_wisher_trigger` / `tm_bae2_well_wishers_value`, each counted once): sworn sisters; friends; rulers of the six faiths in diplomatic range who keep a House, with opinion ≥ 20. Never the accuser. At least 2 are needed.
- **Cooldown:** 5 years (var `tm_bae2_ride_cooldown`).
- **Effect:** `tm_bae2_ride_effect` fires the existing 0130 with `scope:tm_bae2_ride`, `tm_bae2_pledgers` and price = 25 × pledgers. The gold requirement is waived, and if the accuser accepts, the gold is created for him.
- **AI odds:** refusal is −20 per pledger (written as a ladder).
- **If he refuses**, he loses minor prestige × pledgers (Flóamanna saga 19; Ahola p. 100).

**3c. Harbouring (`tm_bae2_yearly_harbour`, `tm_bae2.0115`).** Each year, for each **full** outlaw (excluding one with `tm_feud_passage`) whose employer keeps a House:
- one House county gets `tm_house_strain` +1;
- the holder gains +5 prestige and the accuser loses 5 (Ahola p. 226);
- at 25%, under the flavour budget, if the accuser lives and is not the holder, the holder gets 0115:
  - **pay** `tm_bae2_harbour_price_value`, one wrong's bót at the accuser's rank, 50–200 (Ahola p. 213);
  - **refuse**: `tm_feud_wrong_effect` with REASON `tm_harboured` (loc key `house_relation_reason_tm_harboured_desc` in tm_bae2 loc);
  - **witness before five neighbours**: `tm_send_on_effect`, no liability (Grágás §1.3).

Lesser outlaws are left out: going abroad is their sentence, so a host abroad is not "assisting" them. The tooltip for 0110's "keep her" now says all this.

**3d. The Outlaw's Holm (`tm_bae2_yearly_holm`).**
- **Tracking.** For landless-adventurer leaders under full outlawry, the camp (`domicile.domicile_location`, the same link the mod already uses for Answer the Hall's Call) is stored each year in `var:tm_bae2_camp_at` / `tm_bae2_camp_years`.
- **Ground.** After 3 years in one place on mountain ground (`terrain = mountains / desert_mountains`) or on an island, the band gets `tm_bae2_holm_modifier` (+2 defender advantage), renewed yearly while the camp stays. The county gets the permanent flavour modifier `tm_bae2_outlaws_holm_county_modifier`, with no stats.
- **Islands.** Vanilla has no island trigger. An island here means a coastal county with no county beside it by land (`is_coastal_county` + no `any_title_to_title_neighboring_county`).
- No curse was built.

### Files
- `events/tm_bae2_events.txt`: 0100 and 0101 rewritten; 0105 and 0115 new; 0130 has the ride path; header updated.
- `common/scripted_effects/tm_bae2_effects.txt`, `common/scripted_triggers/tm_bae2_triggers.txt`, `common/on_action/tm_bae2_on_actions.txt`, `common/decisions/tm_bae2_decisions.txt`, `common/modifiers/tm_bae2_modifiers.txt`, `localization/english/tm_bae2_l_english.yml`.
- **New file:** `common/script_values/tm_bae2_values.txt` (with BOM).

### New tallies (`tm_feud_n_<WHAT>`)
`out_suits`, `out_iceland_client`, `out_iceland_no_client`, `out_oath_held`, `out_court_called`, `out_court_held`, `out_court_failed`, `out_penance`, `out_secular_arm`, `out_rides`, `out_ride_settled`, `out_ride_refused`, `out_harboured`, `out_harbour_paid`, `out_harbour_refused`, `out_harbour_witnessed`, `out_holms`.

### Rules respected
- **Rule 3:** each hostile line has a named speaker: the accuser in 0100 and 0115.
- **Rule 25:** "pagan illusion and sin" only; no pact.
- **Violence:** none on screen. The secular arm ends at the cell door.
- **Historical people:** none named. "Ragnhildr" and "Kolr" stay out of the loc.
- **Rule 13:** respected (the Icelandic text describes the law, not freedom).
- **Flavour budget:** 0100 and 0115 both spend it.
- **Glyph check:** silent.
- **xTiger:** 0 reports in these files; the total is at the baseline of 23.

### Uncertain syntax
- `prev` inside `limit` of `every_relation` / `any_relation` / `every_ruler`, in script values (meant to be the outlaw).
- `random = { chance = <script value> }`.
- `pay_short_term_gold` with `gold = { value = … multiply = 0.5 }`.
- Saved scopes surviving the 14-day `trigger_event` to 0105 (`tm_bae2_lord` and `tm_bae2_sentence` are read there).
- `clear_saved_scope` on scope values.
- A county modifier with no stats.

### TO-TEST
1. **Norway 1150 suit.**
   - (b): no gold paid at once. Fourteen days later the accuser gets 0105, then the ring is paid (lord and accuser get 5 each) and she goes abroad.
   - (c): she forms a band only after 0105.
2. **Court fails:** a House member in a House county with 2 sworn sisters at court has about a 70% fail chance. The sentence lapses, the accuser loses prestige, and she has no modifier.
3. **Accuser dies inside the fortnight:** no 0105; the flag clears after 30 days.
4. **Magnus 1180:** with a Norwegian lord who has a chaplain, the chaplain gets half and the lord half.
5. **Iceland:** a seeress charged under a lord with an Icelandic capital gets the "no suit" text. Set `tm_bae2_last_seeker` by console to check the client branch: 0101 goes to the client, with the twelve-jurors option.
6. **Penance:** from 1300, (d) gives the modifier, the condition var and exile. A second suit under a Norwegian lord (from 1300) gives "Take her into my keeping", and she is imprisoned. Spring the Cell can target that jailer.
7. **Ride:** a full outlaw band player with 2 sworn sisters sees the decision; the accuser gets 0130 with ride text and price 50. Refusing costs 2 × minor prestige.
8. **Harbouring:** a full outlaw courtier of a House holder adds strain +1 a year and +5/−5 prestige; 0115 fires. Check the house relation on refuse when one party is Bædling.
9. **Holm:** a full outlaw band camped 3 years in a mountain or island county (e.g. Gotland) gets the modifier and the county modifier.

## 2. The rest of the feud (with the sister's revenge and the suit-bearer)

Built 2026-10-25. Not tested in game. xTiger: no reports in the feud files.

### Files

- `common/scripted_effects/tm_feud_effects.txt`: `tm_feud_wrong_effect` restructured (gate, then honour checks, then `tm_feud_enter_wrong_effect`); new `tm_feud_enter_wrong_effect`, `tm_feud_rank_toast_effect`, `tm_feud_answer_with_honour_effect`, `tm_feud_foster_seal_effect`, `tm_feud_find_ward_effect`, `tm_feud_find_bearer_effect`, `tm_feud_avenge_her_effect`, `tm_feud_self_judgment_toast_effect`. `tm_feud_settle_effect` gives a 15-year truce when `scope:tm_feud_ward` exists.
- `common/scripted_triggers/tm_feud_triggers.txt`: `tm_feud_woman_trigger`, `tm_feud_man_trigger`, `tm_feud_may_refuse_trigger`, `tm_feud_bearer_needed_trigger`, `tm_feud_bearer_candidate_trigger`, `tm_feud_avenger_trigger`, `tm_feud_foster_ward_trigger`.
- `common/script_values/tm_feud_values.txt`: `tm_feud_rank_value`, `tm_feud_heavy_price_value`.
- `common/opinion_modifiers/tm_feud_opinion_modifiers.txt`: `tm_feud_fair_judgment_opinion` (+15), `tm_feud_uneven_opinion` (−15), `tm_feud_humbled_opinion` (+15), `tm_feud_answered_with_honour_opinion` (+10), `tm_feud_foster_seal_opinion` (+10), `tm_feud_avenge_her_opinion` (−30).
- `common/modifiers/tm_feud_modifiers.txt` (new, BOM): `tm_feud_bot_spent_on_spears_modifier` (levy_size +0.1, martial +1).
- `common/character_interactions/tm_feud_interactions.txt`: Offer Bót gets the send_option `tm_feud_foster`; new `tm_feud_grant_self_judgment_interaction`.
- `common/on_action/tm_feud_on_actions.txt`: `tm_feud_on_death`, outlaw branch, calls `tm_feud_avenge_her_effect` for a Bædling outlaw.
- `events/tm_feud_events.txt`: 0020/0021 changed (suit-bearer); new 0040, 0050 (hidden), 0060.
- `localization/english/tm_feud_l_english.yml`: new keys. `tm_feud.0020.desc.court` is replaced by `.court_sisters`, `.court_bearer` and `.court_nobearer`.

### What was built

**2a. Escalation by rank.** When a wrong is written, the wrongdoer's house stores `tm_acc_last_rank`, the victim's `tm_feud_rank_value`: the highest landed tier (0 if unlanded), +1 for a knight or a councillor. A requital compares its victim's rank with the value stored on the requited house:
- **Higher** (adult victims only): pays one off, then adds one the other way ("it overbalances"). The requiter gains minor prestige.
- **Lower**: nothing is paid off and nothing is written. The requiter loses minor prestige ("not a worthy object").
- **Equal, or no stored value** (old saves): as before.

Player house heads on either side get a toast. There is one variable per house, not per pair of houses (Miller pp. 183–84, 200, 207).

**2b. Grant Self-Judgment.** The interaction is shown in the same cases as Offer Bót. It costs medium prestige, is auto-accepted, has no AI targets and no pulse. `tm_feud.0040` goes to the recipient, with three choices:
- **Modest:** the bót, plus +15 opinion from the granter.
- **Heavy:** twice the bót, plus −15 "Uneven" from rulers in her diplomatic range who share her faith or are of the Germanic religion.
- **Remit:** no gold, major prestige, and "Remitted What I Owed" from the granter.

Every choice runs `tm_feud_settle_effect`. A player granter gets a toast. AI odds: greedy favours heavy; generous or forgiving favours remit (Miller pp. 273, 275–76, 287).

**2c. The refused Account.** In `tm_feud_wrong_effect`, `tm_feud_may_refuse_trigger` checks the following:
- The victim is a Bædling woman ruler (`tm_feud_woman_trigger`: female, a daughter, or declared).
- The wrongdoer is an AI non-Bædling man of North-Germanic heritage who is a ruler.
- There is no Account between the two houses in either direction, no settlement, and no earlier refusal.

When it passes, hidden `tm_feud.0050` fires to him:
- **Admit** (base 75): the wrong is written and she gains minor prestige.
- **Refuse** (base 25; +100 if arrogant, +100 if zealous, −15 if just): her house gets `tm_acc_refused` targeting his house and `tm_acc_refuser` (him), both for 30 years. If she is a player, she gets a toast with his portrait and his line: "I do not keep an account with women."

While the refusal stands, his house's wrongs against hers are not written (tally `refused_unwritten`). Her house's next wrong against his is answered with honour: nothing is written, the wrongdoer gains medium prestige, the refuser (or else his house head) loses the same, and Bædling and Germanic rulers in range give +10 opinion. The refusal then ends. Vanilla's house relation still moves in every case (Miller pp. 32–33, 188).

**2d. Fostering to seal a settlement.** Offer Bót has a new send_option, "And foster a child of their hall", available when the recipient's house has an unmarried child under 16 with no guardian, not imprisoned and not a ruler. The eldest such child gets `set_relation_guardian = actor`. If the child is not playable, they visit the actor's court, as vanilla's `educate_child_event_effect` does. The actor loses minor prestige. Ward and guardian give each other +10, on top of the vanilla guardian relation's own 15. The truce runs 15 years. The AI recipient gets +15 to accept. This does not use `tm_foster_daughter_interaction`. The loc carries the Miller line (pp. 123, 172).

**2e.** In the truce-breaker branch, the wronged house's head gets `tm_feud_bot_spent_on_spears_modifier` for 2 years (p. 184).

**3e. The sister's revenge.** When a Bædling outlaw is killed, the law still counts no wrong. `tm_feud_avenge_her_effect` picks an avenger: an adult, free, of a different house from the killer's, and with `tm_flavour_ready_trigger`. She is chosen in this order:
1. a `tm_sister`;
2. else a living character with `var:tm_fostered_by` = the dead woman;
3. else the `var:tm_elder_sister` of a House in the county where she died.

`tm_feud.0060` ("Avenge Her") fires 7 days later, and the flavour budget is spent. The avenger can:
- **Take up her Account:** `tm_feud_add_one_effect` on her house against the killer's house, and −30 opinion of the killer.
- **Let it rest:** minor stress loss.

Sources: Ahola pp. 85–86, 108–9, 113.

**3f. The suit-bearer.** In `tm_feud.0020`, if the lord's rite lacks `tm_sisters_faith`, the event looks for a man to carry the suit. Candidates are adult men (`tm_feud_man_trigger`) who are not imprisoned, not outlaws, and not the speaker or the lord. Each must be her spouse, her close kin, or have `tm_house_friend_modifier`, and must be at the lord's court or her own. The candidate with the best diplomacy becomes `scope:tm_feud_bearer`. With no candidate, "Bring the suit" is shown greyed out ("No man would carry it"). In 0021 the bearer is the right portrait (the speaker moves to lower right), adds his diplomacy to the AI odds for outlawry, and has his own desc line. Under a lord of the six faiths, the line reads "the Sisters speak their own suits". The irony line: "The thing has heard I am a woman. So a man must speak for me now… It is the first time the law has agreed with me about anything." (Grágás §1.7; Jochens 1995 pp. 39, 113.)

**3f, revised after run 17 (2026-10-25, untested).** Run 17 blocked 34 suits for want of a bearer, against 27 brought. Two changes:
- **Wider bearers.** Besides her husband, close kin and friends of a House, any man of the six faiths, or any man with opinion of her 20 or more, at her court or the lord's, may carry it.
- **Send for him** (`tm_feud.0020` option c, `tm_feud.0022`). With no man at hand, her husband or a close kinsman elsewhere (`tm_feud_far_kin_trigger`, the best speaker) may be sent for. Nothing moves: after 60–150 days he either comes, and the suit goes to the lord with him as bearer, or sends word that he will not. He is likelier to come with opinion 25+, if just or brave, or if he is her husband; less likely with negative opinion, if craven or lazy, or if he is a ruler with his own hall. Toasts: "He Came to the Þing" and "He Will Not Come". Tallies `nid_kin_sent`, `nid_kin_came`, `nid_kin_refused`. Kinsmen rode to the assembly to prosecute, as suitors did.
- **"The thing" is now "the þing"** in all player-facing text (18 lines): the Old Norse word, not its English rendering.

### New tally names (tm_feud_n_*)

`requital_higher`, `requital_lower`, `account_refused`, `account_admitted`, `refused_unwritten`, `refused_answered`, `self_judgment_modest`, `self_judgment_heavy`, `self_judgment_remit`, `fostered_seal`, `avenge_offered`, `avenge_taken`, `avenge_rested`, `nid_no_bearer`, `nid_borne`. `requitals` still counts every requital, including higher and lower ones.

### Rules respected

- Rule 3: his line is spoken by him, a named vanilla character shown in the toast portrait, and aims at her as a woman, not at her body or clothes.
- No violence on screen: 0060 says only that "[killer] killed her".
- No historical figures in loc. "Snorri" was kept out of the 0040 text.
- No italics markup in new loc. Glyph check is clean.
- Refusal is not the default.
- Children are never the higher target.
- No AI pulse for self-judgment.

### Uncertain syntax and design calls

- **Portraits:** `lower_right_portrait = { character = scope:tm_feud_bearer trigger = {…} }` in 0020 when the scope does not exist. It may log an error. Check `error.log`.
- **Gold:** `pay_short_term_gold` when the self-judgment granter cannot pay twice the bót. I assume it puts him into debt; the interaction has no gold check, so he is bound by his grant.
- **Player wrongdoer:** the refusal is AI-only. A player who wrongs a Bædling woman has no choice; the Account opens as usual.
- **Lower-rank requital:** neither paid off nor written as a new wrong.
- **Avenger search:** `any_living_character` for `tm_fostered_by` runs only on a Bædling outlaw's death, which is rare.

### TO-TEST

1. **Escalation:** a Bædling count's house wronged by a baron's house, then a requital on that house's duke (adult) shows "It Overbalances", and the Account flips. A requital on an unlanded child is equal or lower, never higher.
2. **Self-judgment:** as a player who owes, Grant Self-Judgment to an AI.
   - Prestige cost is taken.
   - 0040 fires and the toast arrives.
   - Each option settles the Account (`tm_acc_settled`, 10 years).
   - The heavy option gives "Uneven" from same-faith or Germanic rulers in range.
3. **Refused Account:** an AI arrogant Norse Christian ruler imprisons or raids a Bædling queen.
   - The toast shows his line.
   - `tm_acc_refused` is on her house.
   - His next wrong is not written.
   - Her house's next wrong against his gives "Answered with Honour" opinions and the prestige swap.
4. **Fostering:** Offer Bót with the foster option.
   - The child becomes the ward and moves to court.
   - The truce lasts 15 years.
   - The actor loses minor prestige.
   - The option is greyed out when no child qualifies.
5. **Truce broken:** the victim's house head gets "Bót Spent on Spears" for 2 years.
6. **Avenge Her:** kill a full-outlaw Bædling who has a sworn sister. 0060 reaches the sister in 7 days; "take up" writes the Account against the killer's house, and no truce-breaker penalty applies.
7. **Suit-bearer:**
   - A níð suit under a Catholic lord with a husband at court: the bearer portrait appears in 0020 and 0021.
   - The same with no eligible man: the option is greyed out ("No man would carry it").
   - Under a Bædling lord: no bearer is needed.

## 3. The era's news and the lore (`tm_bae3`)

Built 2026-10-25 from `baedling_spec.md` items 1a, 1d, 1e and 4a–4d. Only new files; no existing file edited. The game was not running (checked with `pgrep`). xTiger: **0 reports** in these files (the run's other reports are in `tm_bae2`/`tm_feud` files that other builders are editing). `tools/check_glyphs.py`: silent.

### Files (all new, all with BOM)
- `events/tm_bae3_events.txt`: 0001, 0010, 0020, 0100, 0200–0204, 0300, 0301
- `common/on_action/tm_bae3_on_actions.txt`: `tm_bae3_yearly` (yearly_global_pulse), `tm_bae3_on_title_gain` (on_title_gain)
- `common/scripted_triggers/tm_bae3_lore_triggers.txt`: conversion bands, islands news, seiðmenn keeper/rival, shirt weaver, Calling Herself candidate
- `common/scripted_effects/tm_bae3_effects.txt`: `tm_bae3_leave_realm_effect`, `tm_bae3_site_story_effect` (+ `_fire_effect`), `tm_bae3_english_woman_name_effect`, `tm_bae3_make_broiderer_effect`, `tm_bae3_calling_trade_effect`
- `common/modifiers/tm_bae3_modifiers.txt`, `common/opinion_modifiers/tm_bae3_opinion_modifiers.txt`
- `common/character_interactions/tm_bae3_interactions.txt`: `tm_bae3_warding_shirt_interaction`
- `localization/english/tm_bae3_l_english.yml`
- Reads the shared `tm_bae3_triggers.txt` (county Norwegian/Icelandic triggers) and does not change it.

### What was built
**Yearly loop:** `every_living_character` filtered first by `rite_has_parameter = tm_seidr_gate`, adult, not imprisoned. Each Bædling gets at most one branch per year, and every branch checks `tm_flavour_ready_trigger` and spends `tm_flavour_spent_effect`. Calling Herself has its own loop, which runs only in 1350–1453 (the date check sits outside the loop) and is filtered by `tm_sisters_faith`.

| ID | Event | Gate and odds | Effect |
|---|---|---|---|
| 0001 | The King's Example | She lives in a county that is in its conversion band (Norway 995–1030, Iceland 1000–1010, Denmark 965–1000, Sweden 1080–1130). Her top liege is Christian and is not her. 4%/year, once in her life. A courtier at the court tells the story, a woman of the faith if possible. | Four kingdom variants, then Eiríkr's pagan burning of "eighty men he called seiðmenn" (rule 13). The options: **hidden** (+15 stress); **open** (+medium piety, −10 stress, liege of another faith −15 opinion for 10 years; flavour only, no variable, the suit is untouched); **leave** (courtiers only, −minor prestige, to a court of the six faiths outside the realm, else the pool; `tm_bae2.0110` is NOT fired, since she is no outlaw). |
| 0010 | The Bishop's Letter | From 1300. She is a Bædling ruler holding a House county in a Christian realm and is not the top liege herself. 2%/year, 20-year cooldown. The speaker is the top liege's Christian chaplain, else the top liege. | Edict only: the letter forbids offerings, pilgrimage, fasting and prayer and calls it "pagan illusion and sin" (rule 25, no pact). **Obey**: `tm_house_strain` +1, speaker +10 opinion. **Secret**: +10 stress. **Argue**: a learning duel; on a win, +minor prestige; on a loss, strain +1 and speaker −15 opinion. No trial. |
| 0020 | Word from the Islands | She is in de jure Norway, Iceland included. Once in 1343–45 (50%/year) and once in 1407–09 (25%/year). | 1343: "a woman has been burned on the bishop's sentence for sorcery". 1407: "a man". Nothing more: no pact, host or name. A 5-year `tm_bae3_islands_fear_modifier` (+15% stress gain). The options are head down, or a lamp for the dead (+minor piety, +5 stress). |
| 0100 | They Say He Keeps Seiðmenn | The loop finds a daughter of seiðr or a friend of the House who is a courtier. Her employer is north Germanic or `culture:anglo_saxon`, of any faith, and flavour-ready. The rival is his vanilla rival, else a neighbouring realm owner at opinion ≤ −30. 2%/year per such courtier, 10-year cooldown on the keeper. | Immediate: vassals of another faith take −10 opinion for 5 years. **Deny**: an intrigue duel; a win removes those opinions and costs the rival minor prestige. **Steel**: a prowess duel (a "bout before witnesses", no injury). **Own it** (Bædling keeper only): +medium piety, `tm_feud_wrong_effect` against the rival (reason `tm_bae3_seidr_slander`), and Christian vassals −10. The hostile line is the rival's own. |
| — | Weave the Warding Shirt | The actor is a Bædling adult who knows the warding songs or has `tm_elder_sister_modifier`. The recipient is her `tm_sister`, her ward (`has_relation_guardian = actor`), or a friend of the House. It costs 30 gold and has a 3-year cooldown. | The recipient gets `tm_bae3_warding_shirt_modifier` for 5 years (+3 prowess, +0.15 health) and +20 opinion. The weaver gets +minor piety. AI: family and courtiers; does not weave if gold < 80; weights knights and sisters higher. |
| 0200–0204 | Holy sites' stories | A Bædling ruler who holds `c_north_riding` / `c_trandheim` / `c_kiev` / `c_upland` / `c_gutland` (checked against vanilla `00_holy_site_types.txt`). Fires on `on_title_gain` for those counties, or from the yearly loop at 25% if she already holds one. Once per character per site, budgeted. | +minor piety. A 10-year county modifier: York and Uppsala +5 county opinion; Trondheim +5% levies; Kyiv +10% garrison; Gotland +10% development growth. |
| 0300 / 0301 | Calling Herself / The Town Court | 1350–1453. A daughter, Marked or declared woman of any of the six faiths, unlanded, in de jure `k_england`. 3%/year, once in her life. | A generated broiderer, 45–62, of the town's culture and faith, named Amice, Hawise, Cecilia, Joan or Matilda. She works as a tapster or an embroideress (rolled at random), and the trade gives lifestyle XP and +15 gold; she and the broiderer take +25 opinion of each other. If she has no woman's name yet, she can **take the broiderer's name** (Juliana, Isabel, Beatrice, Constance, Emma or Margaret, plus `tm_declare_effect`), choose **her own** (fires `tm_house.0001`), or say **not yet** (rule 23). If she already has one, she learns the trade. Then a 25% chance of 0301: the night watch brings her before the court of the county's lord, and the clerk asks her name. **Give my own** (−10 stress, +minor prestige) or **say nothing** (+5 stress). No charge and no sentence. |

### Sources (as cited in the code comments)
- Mitchell, *Witchcraft and Magic in the Nordic Middle Ages*: pp. 32–37 (Poppo), 33 and 190–91 (Óláfr's burnings, Eyvindr's crew), 38 (Þorgeirr), 122–23 and 171–72 (Kirkjubær, Kolgrímr), 123 and 169–71 (Bergen).
- contesting_orthodoxy §3b (Bergen 1319 edict) and guardrails 1 and 5.
- Price, *The Viking Way* (2019): pp. 80–81 (Eiríkr, the Eighty), 175 (Lärbro), 226 and 273 (Gunnhildr), 275 (Skylitzes 971), 288–90 (Þorgerðr), 342–43 (Osferð hlytte).
- Tolley p. 154 (the seiðmenn label as accusation), p. 61 (Sámi).
- Saxo, *Gesta Danorum* Book 6, p. 135 (`norse_saxo_gesta_danorum.md`).
- Jochens, *Images of Women*, p. 122 (shirts); Ahola p. 222 (Hrolleifr's shirt).
- Henningsen 2019, pp. 249–52 and 262; `v2/rykener_and_mobilities.md` (the ground rule; Anna and Elizabeth are not villains).

### Rules respected
- **Rule 13:** York's story and 0001's ending both show a pagan king burning men.
- **Rule 25:** no pact anywhere. The bishop says "pagan illusion and sin".
- **Rule 3:** the hostile lines belong to named portraits: the rival in 0100, the bishop or chaplain in 0010.
- **Rule 5:** no body reveal. **Rule 24:** no skirt or trouser imagery. "Women's gowns" in the Lärbro text quotes Price's description of the stones.
- **Narrator text:** no sisters among the seiðmenn; the faith calls the Eighty and the Lärbro figures "kin". No Sámi link. No historical person is claimed: Rǫgnvaldr, Kolgrímr, the nun, the False Margaret and Eleanor go unnamed, and Óláfr is not named.
- **Names:** no "John". No Eleanor, Anne or Elizabeth in either name list, and Alice is avoided too.
- **Content:** no sex work, no clients. Burnings are reported in one line, never shown.
- **Loc:** plain, with no italics markup.

### Uncertain or judgement calls
- **Bands:** Sweden 1080–1130 and the Danish 965 band are conventional dates (the lead's bands). The notes give no page for them.
- **Uppsala (0203):** the hostile words ("effeminate… unmanly clatter") belong to the legendary champion, told as a story. No vanilla character speaks them. That bends rule 3. If the lead wants it strict, add a Christian courtier portrait as the teller, or cut the quotation.
- **0001 Norway** has one reported line: "(the skerry line was cut in review) for the tide" (Mitchell p. 33). Cut it if it reads as drowning on screen.
- **Warding shirt:** 1.20 has no knight death-risk modifier (`ck3_docs`), so the modifier uses health +0.15 instead. The optional "counts toward the seiðr charge" hook was not built: it would touch tm_bae2.
- **Bishop's Letter:** it fires only for Bædling House holders (the Bædling loop), not for the other five faiths.
- **They Say He Keeps Seiðmenn:** the roll is per qualifying courtier, so a court with several of them has a slightly higher chance (the cooldown stops repeats).
- **On_title_gain:** `has_title` at that moment is untested. If the title is not yet held when it fires, the yearly loop catches the site the next year.
- **Calling Herself** generates one broiderer in the pool each time it fires (rare).

### Tally names (`tm_feud_tally_effect`, globals `tm_feud_n_<name>`)
`bae3_kings_example`, `bae3_bishops_letter`, `bae3_islands_news`, `bae3_seidmenn_charge`, `bae3_site_story`, `bae3_calling_herself`, `bae3_warding_shirt`

### TO-TEST
1. Start 867 and run to 995+ with a Bædling courtier in Norway under a Christian king, to see 0001. Check that the Norway variant shows, and that "leave" moves her out of the realm.
2. Iceland, 1000–1010: the Iceland variant shows.
3. From 1300, a Bædling vassal holding a House under a Catholic king gets 0010. Each option works; strain rises on obey or on a lost argument.
4. 1343: Bædlings in Norway or Iceland get 0020 once (1343 text). 1407: the 1407 text. The fear modifier lasts 5 years.
5. A Norse lord with a daughter of seiðr at court and a rival gets 0100. Vassals of another faith take −10. "Own it" appears only for a Bædling lord, and the Account entry is made.
6. The warding shirt interaction appears on a sister, ward or friend of the House; costs 30 gold; has a 3-year cooldown; the modifier lasts 5 years.
7. Give a Bædling ruler Gotland (`c_gutland`) by console: 0204 fires once, and the county modifier lasts 10 years. Repeat for the other four sites.
8. 1350+: put a declared or Marked woman of any of the six faiths in an English county. In 0300, the broiderer's name is never Eleanor, Anne or Elizabeth, and "I have my own" opens `tm_house.0001`. 0301 sometimes follows and ends open.
