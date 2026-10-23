# Wave 5: the Women's Chamber (Adelphai Dorleyaiou)

User, after the 1088 save of run 6: Dorley had 19 members, no ruler since the 960s, and Dorylaion under a Sunni lord. "Can we perhaps add a faction to byzantine court or religious politics comprised only of daughters, to help out Dorleyism? Similar to what we just did with Yutai." Then: "include the estate grant but keep it 'byzantine'." Prefix `tm_dl3_`, namespace `tm_dl3`. Untested in game.

## What was built
Modelled on the Yutai palace (`tm_palace`, `tm_yt2`, docs/wave3/yutai.md). The faction is a variable, a decision and four events, not a vanilla faction: daughters are mostly courtiers, and the fight in the sources is over posts, access and grants, not a war against the throne.

**The throne** (`tm_dl3_byzantine_throne_trigger`): a Christian ruler not of the Sisters who holds `e_byzantium`, or who has administrative government and Byzantine heritage. Nowhere else.

**The chamber's own** (`tm_dl3_chamber_daughter_trigger`): adult, free daughters of the faith whose top liege is such a throne. Only daughters. Cis sisters and Marked sisters stay out of it.

**The invitation** (`tm_dl3.0001`). Yearly for each unlanded daughter of the faith who is not a Companion of the Mothers: 5% (+3 at chamber's ear, −3 at the Patriarch's), at most once in 15 years. The throne is her own top liege if it qualifies, otherwise the holder of `e_byzantium`. So the chamber can call a daughter from anywhere, which is the inflow Dorley lacked. Accepting moves her to the throne's court (`add_courtier`), sets `tm_dl3_chamber` and the modifier *Post in the Chamber* (diplomacy +2, intrigue +1, prestige +0.5/month, stress gain +10%), and the throne +15 opinion.
- (a) Take the post: the clerks write her in their eunuchs' column, −25 piety. A Galenic Sister counts as the Emperor counts: +25 prestige instead.
- (b) Stay with the House: +50 piety.
- (c) Diplomacy 10+: take the post and ask a notary of the empress's to write her among the women. Roll (50 + diplomacy ×2 against 50): written, or −25 piety and −25 prestige.

**The balance** `tm_dl3_balance`, −3 to +3, on the throne's primary title. Created at 0. Yearly per seat: 30% drift toward 0; 25% +1 when a woman holds the throne or the regency (`tm_dl3_women_rule_trigger`: Garland's rule, women gained power in minorities and lost it under adult emperors, p. 198). Each daughter in post: 10% a year, +1.

**What the balance does.**
- **Chamber's ear (+2 or more):** the heresy ladder (`tm_byz.0010`–`0012`) does not fire for Dorleyite rulers under that throne (`tm_dl3_ladder_stayed_trigger` in the three event triggers). Invitations +3.
- **Patriarch's ear (−2 or less):** the ladder's yearly chance +3 (`tm_on_actions.txt`). Invitations −3.
- **Synod letters** (`tm_dl3.0002`, the Yutai memorial's twin): for a daughter in post when the balance is +2 or more (backlash, 3%) or −1 or less (6/9/12%). Five-year cooldown, flavour budget. The chamber answers for her (60/40; +20 if a woman rules): kept, +25 prestige, balance +1; lost, the post and −100 prestige, balance −1. Or give up the post (+50 piety), or pay the synod's notary 100 gold.

**The decision "Work the Chamber"** (`tm_dl3_work_chamber_decision`), for a daughter in post. Five-year cooldown, AI checks every 60 months. Opens `tm_dl3.0010`:
- (a) Balance ≥ 1: a chrysobull for a House. Balance −1, +25 piety. One Dorleyite ruler in the throne's realm who keeps a House gets `tm_dl3_chrysobull` for 10 years: the heresy ladder passes her by. She gains +20 opinion of the daughter.
- (b) The throne is a woman, has a female regent, or has a wife: sit in the empress's chamber. +15 prestige, balance +1 (+2 when a woman rules).
- (c) 100 gold: bring the chamber's own staff over. Balance +1; 30% the throne hears, −15 suspicion.
- (d) **The estate.** Unlanded, never asked before, prestige 200, balance ≥ 2, and an AI throne holding four or more counties. Prestige −200, balance −2. The throne grants her a county from its own hands (`create_title_and_vassal_change` type granted): one with a Sisters' House first, then one whose people keep the faith, then the least developed; never its capital. A player's throne is never made to give land. The county keeps `tm_dl3_estate` = the seat.
- (e) Not this year.

**The annulment** (`tm_dl3.0003`). Basil II's Novel of 996 annulled the chrysobulls of Basil the Parakoimomenos and made an example of a protovestiarios who had swallowed a village (Tougher, p. 56). Yearly for a daughter holding such an estate while that seat's balance is −3: 25%, 10-year cooldown. Give it back (+50 piety; the county returns to the throne, type revoked), pay the logothete 150 gold, or appeal in person (50 + diplomacy ×2, +20 if a woman rules, against 50): kept with +25 prestige, or lost with −50 prestige.

## Sources (all in docs/research)
- byz_garland_empresses.md: the gynaikonitis staff "primarily though not entirely composed of eunuchs", the empresses who ruled made them ministers (p. 5); Nicholas had Zoe Karbounopsina tonsured (p. 119); Keroularios against Theodora's appointing of clerics (p. 166); women gained power in transitions (p. 198).
- hist_tougher_eunuch_byzantine.md: the Novel of 996 (p. 56).
- The eunuchs' column and "the court calls its eunuchs angels, and buys them as boys" are the faith's own voice (README). No historical chamberlain or patriarch is named or claimed for the faith.

## Changed files
- New: `common/scripted_triggers/tm_dl3_triggers.txt`, `common/scripted_effects/tm_dl3_effects.txt`, `common/on_action/tm_dl3_on_actions.txt`, `common/decisions/tm_dl3_decisions.txt`, `common/modifiers/tm_dl3_modifiers.txt`, `events/tm_dl3_events.txt`, `localization/english/tm_dl3_l_english.yml`.
- `events/tm_byzantine_events.txt`: the three ladder events' triggers add `NOT = { tm_dl3_ladder_stayed_trigger = yes }`.
- `common/on_action/tm_on_actions.txt`: the ladder's chance +3 at the Patriarch's ear.

## Uncertain
- The estate grant: whether a courtier granted a county inside an administrative realm takes administrative or feudal government, and whether the engine needs a noble family for it. Watch error.log and the realm view.
- `var:tm_dl3_estate ?= { ... }` on a variable holding a title (xTiger accepts it).
- `has_diarchy_type = regency` read on the throne (vanilla uses it so in 00_playable_difficulty_infos.txt).
- Saved scopes carried into events fired with a delay from the yearly pulse (as the Yutai palace).

## Test scenarios
- **C1 Invitation.** 867 start; give an unlanded daughter of the faith (`tm_make_sisters.txt`) a court anywhere. In the console `trigger_event tm_dl3.0001` needs the scope, so instead set her `tm_dl3_offered` off and wait, or observe: within ~20 years she should get *The Chamber Writes*. Accepting moves her to Basil I's court, with *Post in the Chamber*.
- **C2 Balance.** With a daughter in post, check `e_byzantium`'s variables (`tm_dl3_balance`) yearly. With an empress or a female regent it should climb.
- **C3 Ladder stayed.** A Dorleyite count under an Orthodox Byzantine duke: with the balance at +2 (set it in the console on the emperor's primary title), the books/assemblies/wills events never fire; at −2 they come faster.
- **C4 Work the Chamber.** Options show as gated: (a) only at balance ≥ 1 with a House-keeping Dorleyite ruler in the realm; (b) only with an empress, a female regent or a wife; (d) only at balance ≥ 2, prestige 200, an AI throne.
- **C5 Estate.** Take (d): she becomes count of a county from the emperor's demesne, preferring a House county. Check her government and that error.log is clean. Set the balance to −3: within a few years *The Chrysobull Annulled* comes; giving it back returns the county to the emperor.
- **C6 A player emperor.** Play Basil I with a daughter in post: (d) never appears for her.
