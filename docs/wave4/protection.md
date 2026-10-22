# Protection under Muslim and Orthodox lords, wave 4

Status: built, untested in game (2026-10-21). xTiger: no reports in any `tm_fut_*` file. `tools/check_glyphs.py` passes.

Two grants, both for honour and service, never for gold:
- **Under Her Chivalry** (Tor, *Violent Order*, 2007, pp. 244, 248–250, 257; `research/isl_tor_violent_order.md` §6, §11, proposal 3).
- **No Service in the Prince's Wars** (Dollinger, *The German Hansa*, Document 3, pp. 381–382, cls. 10 and 32; p. 30 for the witnesses; `research/norse_dollinger_hansa.md` §7, §11, proposal 3).

## Files

All new (prefix `tm_fut`, namespace `tm_fut`):
- `events/tm_fut_events.txt` (0001, 0010, 0011, 0020, 0030, 0032, 0033)
- `common/on_action/tm_fut_on_actions.txt` (`yearly_playable_pulse` → `tm_fut_yearly_ruler`)
- `common/character_interactions/tm_fut_interactions.txt` (`tm_fut_grant_terms_interaction`)
- `common/scripted_triggers/tm_fut_triggers.txt`, `common/scripted_effects/tm_fut_effects.txt`
- `common/modifiers/tm_fut_modifiers.txt`, `common/opinion_modifiers/tm_fut_opinion_modifiers.txt`
- `localization/english/tm_fut_l_english.yml`

No file of another builder was changed.

## What was built

### 1. Under Her Chivalry

- **The code.** A Muslim lord (count or above) keeps it when he has one of two modifiers:
  - *Javanmard* (`tm_fut_javanmard_modifier`: +0.3 prestige/month, +1 prowess). Only from **The Fityan** (0001): the young men of his capital swear him in, with the oath by the futuwwa and the trousers of the order (Tor p. 248). Only in Iran and Iraq (`world_persian_empire`, which includes the Jazira) and **before 1056**, Tor's land and years. Yearly, 2% (+1 each for brave, generous, honest, just), only at a court where a daughter of the six faiths lives or visits; budget; 20-year cooldown.
  - *A Free Man's Word* (`tm_fut_free_word_modifier`: +0.3 prestige/month). Taken when he gives his word in 0011 without the first. This is the code in plain words, for every other Muslim land and every later date. No *fata* is named in its text (Tor note §11, "Geography").
- **She puts herself under his word** (0010, to the daughter). A daughter or declared sister of any of the six faiths, not a ruler, at a Muslim lord's court or visiting it. Yearly 3%, 6% if he already keeps the code; budget on her; asked once in ten years. She can ask (→ 0011) or keep her own counsel. The text says "entrust myself to his chivalry" only when he is *Javanmard*.
- **He gives his word, or not** (0011, to the lord; follow-up, no budget). Give it: she gets `tm_fut_sheltered_by` (him), *Under a Lord's Word* (−10% stress loss, refreshed yearly), +30 opinion of him; he gets +25 prestige and, if he lacked it, *A Free Man's Word*. A guest joins his court, so the gathering does not take her away. Refuse: no cost to her; if he keeps the code, he loses it and 50 prestige. AI: likely if he keeps the code, brave, just, honest; less if zealous.
- **The demand** (0020, to the lord). A lord who keeps the code and has a daughter under his word at court: his liege, else a neighbouring top liege, demands her. The demander is of no Sisters' faith and never Jewish (`tm_fut_demander_trigger`). Yearly 3%, budget, once in ten years. Options:
  - "She is under my word": +50 prestige; the demander −20 (10 years); she +20.
  - *The roadside answer* (*Javanmard* only, Tor p. 249): he moves one step and says no one has passed while he sat there. +25 prestige; she +20; the demander is not offended.
  - "Send her from my court, to her own people": he loses the code and 75 prestige; she −30 of him and goes to the nearest court of her faith (`tm_surv_go_home_effect`), or to the pool. **She is never handed to the demander.** Nuh's lashes (p. 234) are not shown.
- **The hostile household event is blocked now** (interim, without editing `tm_world_*`): `tm_world.0041` (*Those Without Desire*, the household's place "without desire", whose order carries the household chaplain's or jurist's seal) is asked only of a daughter without the flag `tm_world_quarters_asked`. While she is under his word, `tm_fut_shelter_upkeep_effect` lends her that flag for two years at a time (refreshed yearly), and only when she did not already have it (`tm_fut_quarters_held` marks the loan). When the word lapses, both run out.

### 2. No Service in the Prince's Wars

- **The terms** (0030, to the lord). A lord of another faith (not Ha-Nehpakhot, not Jewish: Jewish lords have their own ruling, `tm_hipukh`) with adult members of Ha-Nehpakhot at court. Reached two ways:
  - the yearly pulse: 3%, +3 when a member already serves him (`tm_hn3_lord_has_protector_trigger`: a physician or vizier of the sect, a licensed *fisica*, or a translation he commissioned); budget; once in ten years. The spokeswoman is the member with the highest learning;
  - **Grant Terms to Her People** (`tm_fut_grant_terms_interaction`): a player lord, on a member at his court. No AI weights.
- The desc: no part in his wars unless they ask (cl. 32); their quarrels settled in their own fashion, not by his court (cl. 10); no coin either way; service in return. For an **Orthodox lord from 1229** his scribe knows the clauses from the prince of Smolensk's treaty with the German merchants; otherwise the scribe says princes have given foreign merchants such terms. The narrator never says the Smolensk Germans were Jewish, or that any lord historically gave the sect these terms.
- Options: grant, with her as **physician** (lord: +0.25 health), **interpreter** (+1 diplomacy, +1 learning) or **steward** of his household (+1 stewardship, +0.1 monthly county control). Or "No terms". No option touches gold, tax, loans or war money.
- **Granted:** `tm_fut_terms` on the lord (+25 prestige); every member at court gets *No Part in the Prince's Wars* (−5% stress gain, refreshed yearly) and `set_knight_status = forbid`, and +20 opinion of him (20 years). The yearly pulse covers newcomers, releases members at a court without terms (modifier removed, `set_knight_status = default`), and ends the terms if no member is left or the lord joins the sect.
- **Unless they ask** (0032). While he is at war, a member under the terms who is brave or has prowess ≥10 may ask to ride. 5%, budget. Let her: `set_knight_status = default`, flag `tm_fut_rides`, +15. Or "Stay. You need not."
- **In their own fashion** (0033). Two members' households fall out over a betrothal; his bailiff asks whether to hear it. 2%, budget, once in fifteen years. "No concern of mine" (+10 prestige, members +10) or "My bailiff will hear it" (the terms end, members −20). No wrongdoer, and no money, in the text.

## Decisions

- **Geography and date of *futuwwa*.** Restricted, not "general knowledge": *fityan*, *futuwwa* and *javanmard* appear only for a lord with his capital in Iran or Iraq before 1056. Al-Nasir's futuwwa after 1182 and the Anatolian *akhi* are general knowledge (note §12) and not used. Everywhere else, the same code in plain words. So in the Maghreb and the Sahel, where Ha-Nehpakhot and Badenya actually live under Muslim lords (run 4), only *A Free Man's Word* appears.
- **The *Qabus-nama*** (1082, date general knowledge) is not named, since the fata land ends in 1056. The demand cites what "the fityan say" (the code's protection, p. 250) and the roadside riddle is unattributed (p. 249).
- **Never the Jewish street.** `tm_hn3.0010` (the Muslim lord and the street's ban) is **not** guarded. A code lord overruling the Jewish judges would read as "a Muslim lord protects her from the Jews" (the same worry that keeps faith_design §16 item 23 undecided). The protection is against a demander of another faith.
- **The qadi's ruling** (`tm_world.0040`) is not guarded: it fires for a ruler of a Sisters' faith whose daughter lives at *her* court, with the Islamic liege or neighbour as the speaker. A daughter under a lord's word lives at his court, so 0040 never reaches her.
- **Courtiers only.** The terms cover members at his court. A ruler of the sect who is his vassal is not covered (a vassal's levies have no per-vassal exemption the mod could set without changing contracts).
- **Service, not gold.** The guardrail is met: neither grant moves money, and the service modifiers touch health, skills and county control only.

## Uncertain syntax

- `set_knight_status = forbid` / `default` (vanilla uses `force`, `forbid`, `allow`, `default`). Assumed to persist on the character until changed; checked only by xTiger.
- `tm_fut_grant_terms_effect = { SERVICE = physician }` building `flag:$SERVICE$` and `tm_fut_terms_$SERVICE$_modifier`.
- `tm_fut_sheltered_trigger = no` when the variable is absent: relies on `has_variable` failing before `var:` is read.
- `add_character_flag` with `years` on a flag the character already has: assumed to reset the timer (the loan refresh).
- `trigger_event = tm_fut.0030` from an interaction's `on_accept`, with `scope:tm_fut_spokeswoman` saved just before.

## Changes needed in files I do not own (optional)

1. `common/on_action/tm_world_on_actions.txt`, block "38. Those Without Desire": a clean guard (the interim flag loan then becomes redundant but harmless). In **both** the `any_courtier = {` limit (inside the outer `limit`) and the `random_courtier = { limit = {` that saves `tm_world_quarters_daughter`, after `NOT = { has_character_flag = tm_world_quarters_asked }`, add:
   ```
   tm_fut_sheltered_trigger = no		# wave 4: under a Muslim lord's word, his household does not ask (tm_fut)
   ```
2. `common/on_action/tm_hn2_on_actions.txt`, `tm_hn2_yearly`, bailiff block (optional; lead's call): in the `limit` with `tm_hn2_bailiff_trigger = yes`, add
   ```
   tm_fut_under_terms_trigger = no		# wave 4: under the lord's terms his bailiff hears no quarrel of hers (tm_fut, cl. 10)
   ```
   This is broader than cl. 10 (which covers quarrels among the community only), since the bailiff's rival can be of any faith. Leave it out if that is too broad.

## Test scenarios (for TO-TEST.md)

- **Fityan.** A Muslim count with capital at Nishapur, 900, a daughter of any of the six at court, chance set to 100: 0001 fires; option a gives *Javanmard*. Same at Fes, or at Nishapur in 1100: never fires.
- **Entrust, plain.** A Muslim lord at Kairouan with a Badenya or Ha-Nehpakhot daughter as guest: 0010 to her shows the plain text ("Put myself under [his] word"). Ask → 0011 to him; give word → she joins his court, has *Under a Lord's Word* and the variable; he has *A Free Man's Word*. Check she has `tm_world_quarters_asked` and `tm_fut_quarters_held`.
- **Entrust, fata.** Same at Nishapur in 900 with a *Javanmard* lord: the fata texts show.
- **Household blocked.** With the daughter sheltered, force the 0041 pulse chance: she is never picked. Remove his code modifier: after two years she can be picked.
- **Refuse while keeping the code.** 0011 option b with *A Free Man's Word*: the modifier is removed, −50 prestige.
- **Demand.** A sheltered daughter; his liege is Christian or Muslim: 0020 with the liege as demander. A Jewish liege: the demander falls to a neighbour, or no event. Option b only with *Javanmard*. Option c: she moves to the nearest court of her faith (or the pool); no prisoner, no transfer to the demander.
- **Terms, AI.** A Catholic count in Provence with two Ha-Nehpakhot courtiers: the pulse (chance raised) fires 0030; the plain scribe line shows. An Orthodox prince of Smolensk in 1230: the Smolensk line. In 1200: plain line.
- **Terms, player.** Play that count: the interaction appears on a Ha-Nehpakhot courtier, not on others; after granting, it is invalid ("already granted").
- **Knights.** After the grant, members with high prowess are not on the knights' list; 0032 option a puts one back. A member who moves to another court loses the modifier at that ruler's next yearly pulse and is eligible as a knight again.
- **Quarrel.** 0033 option b: terms, service modifier and member modifiers gone; members −20.
- **Budget.** No lord receives more than one tm_fut event a year from the pulse.

## Questions for the user

1. Should *futuwwa* framing also run after 1182 in Iraq and Anatolia (al-Nasir's orders, general knowledge), or wait for a source? Built: restricted to Tor.
2. The terms are offered by any lord of another faith except Jewish lords. Keep them open to Muslim lords too, or Christian lords only (as the Smolensk precedent)?
3. Should a ruler of the sect who is a vassal of another faith be able to ask her liege for the terms? There is no clean per-vassal war exemption; it would need a levy or contract change.
4. Apply the optional bailiff guard (above)?

## Ready to paste

**README (Shared mechanics, after "Islamic neighbours"):**
> - **Under a lord's word.** A daughter of any of the six faiths at a Muslim court may put herself under the lord's word. One who gives it keeps the code: he takes her into his court, will not give her up when a liege or neighbour demands her, and his household does not offer her a place "without desire". In Iran and Iraq before 1056 the town's *fityan* may swear him in, and the text speaks of *futuwwa*; elsewhere it is a free man's word. Protection for honour and service, never gold.

**README (Ha-Nehpakhot, "The world"):**
> A lord of another faith may give the Nehpakhot at his court terms: his wars are none of their concern unless they ask to ride with him, and they settle their own quarrels. In return they serve as his physician, interpreter or steward. No money passes either way. An Orthodox lord's scribe knows such clauses from the prince of Smolensk's treaty with German merchants (1229).

**TODO (new block):**
> ## Protection under Muslim and Orthodox lords (added 2026-10-21, untested in-game)
> - [x] Under Her Chivalry (`tm_fut.0001`–`0020`; Tor pp. 244, 248–250); No Service in the Prince's Wars (`tm_fut.0030`–`0033`, `tm_fut_grant_terms_interaction`; Dollinger pp. 381–382). `docs/wave4/protection.md`.
> - [ ] Optional guards in `tm_world_on_actions.txt` (0041) and `tm_hn2_on_actions.txt` (bailiff): see the note.
> - [ ] Questions: futuwwa after 1182; terms from Muslim lords; vassal terms.
