# Wave 3: Bædling stage 2 and landless survival

Roadmap item: "Bædling: feud and settlement, outlawry and landless war-bands, Spring the Cell". Prefix `tm_bae2_`, namespace `tm_bae2`. Untested in-game; validated with ck3-tiger, with no reports in these files.

## Files

New:
- `common/schemes/scheme_types/tm_bae2_schemes.txt`
- `common/schemes/agent_types/tm_bae2_agent_types.txt`
- `common/character_interactions/tm_bae2_interactions.txt`
- `common/decisions/tm_bae2_decisions.txt`
- `common/on_action/tm_bae2_on_actions.txt`
- `common/scripted_triggers/tm_bae2_triggers.txt`
- `common/scripted_effects/tm_bae2_effects.txt`
- `common/modifiers/tm_bae2_modifiers.txt`
- `common/opinion_modifiers/tm_bae2_opinion_modifiers.txt`
- `events/tm_bae2_events.txt`
- `localization/english/tm_bae2_l_english.yml`

Changed:
- `common/on_action/tm_flyting_on_actions.txt`: the yearly flyting challenge now checks the flavour budget (`tm_flavour_ready_trigger`) and spends it (`tm_flavour_spent_effect`). Before this it was the one pack flavour event that ignored the budget.

## 1. Spring the Cell (built)

Spec: TODO.md, "Branch faiths, stage 2". The template is vanilla `abduct` (1.20 `abduct_scheme.txt`, `start_abduct` in `00_scheme_interactions.txt`).

- **Scheme** `tm_bae2_spring_cell`: hostile, secret, intrigue-based, with a 5-year cooldown. Phase length, success growth and max secrecy are abduct's.
  - **Who may run it:** any adult of the six faiths (`rite_has_parameter = tm_sisters_faith`), landed or not, courtiers included. Vanilla lets courtiers own hostile schemes, as murder does.
  - **Target:** any character holding in prison a daughter, novice, Marked woman or declared sister (`tm_bae2_cell_prisoner_trigger`). The prisoner may be of any faith, since a House takes in whoever walks out.
  - **Valid while:** the target is alive, in diplomatic range, still holds such a prisoner, and the plotter is free and capable.
- **Success chance:** abduct's base suite (skill, hostile base, countermeasures, dangerous-scheme modifier).
  - -40 if the jailer is in another realm; -15 otherwise.
  - -500 at war.
  - +10 if a Sisters' House stands in or next to the jailer's capital county.
- **Agents** (new agent types):
  - **Marked Guard** (potential): must be Marked, a daughter, declared, of a House, or of the plotter's faith. Scales on prowess, with a bonus if she is a knight of the jailer.
  - **Faithful Servant** (secrecy): anyone at the jailer's court. Bonus if of a Sisters' faith or Marked.
  - **Friend of the House** (speed): a House member, a friend of the House, or the plotter's sworn sister.
  - The fifth slot is vanilla `agent_lookout`.
  - **Join chance:** vanilla's basic and grievous suites, plus +40 for Sisters' faith, +40 for Marked, daughter or declared, and +25 for compassionate.
- **Outcome:** each completed phase fires `tm_bae2.0001`, "A Night for It": strike tonight, or wait for better odds. This replaces vanilla's critical-moment chain, which keys on vanilla scheme types.
  - The success roll uses `scheme_success_chance`; discovery uses 100 − `scheme_secrecy`, as `abduct_outcome_roll_effect` does.
  - **Success (`0010`):** every qualifying prisoner of the jailer is released (`tm_bae2_walk_free_effect`) and goes:
    - a landed prisoner, home;
    - otherwise, to the holder of the nearest county with a Sisters' House (never the jailer);
    - else to the plotter's court if she is playable;
    - else to the plotter's employer;
    - else to the road.
  - Each freed woman gains +30 grateful opinion of the plotter, and the plotter gets minor piety. A freed player gets `0012`.
  - **The jailer (`0011`):** if the plotter was seen, he gets `tm_bae2_sprang_my_cell_opinion` (−40, an imprisonment reason) and `watchful_modifier`. If not, `watchful_modifier` only, and the event does not name her.
  - **Failure (`0020`, `0021`):** give up or try again (`reset_failed_scheme_effect`). If seen, the jailer gets `tm_bae2_tried_my_cell_opinion` (−30, an imprisonment reason) and `watchful_modifier`.
  - Monthly discovery uses vanilla `hostile_scheme_monthly_discovery_chance_effect`.
- **Player start:** the interaction `tm_bae2_spring_cell_interaction` (Hostile) on any character holding such a prisoner. It starts with 2 Marked Guards, a Servant, a Friend and a Lookout.
- **AI start:** `tm_bae2_yearly_cell`. Each ruler holding such a prisoner has a 25% yearly chance to run the hidden `tm_bae2.0002`.
  - **Candidates:** the prisoner's sworn sisters, friends and close family, plus rulers of the six faiths in the jailer's diplomatic range who hold a House or share the prisoner's faith.
  - **Filter:** AI, able to start the scheme, not at war with the jailer, not already running it.
  - **Weights:** sworn sister ×4, family ×3, friend ×2, House holder ×1. Compassionate and brave raise them; craven and content lower them; same faith as the jailer gives ×0.3.
  - The search runs in its own event so that each jailer's candidate list starts empty.
- **Miller row 17** (the rescue opens his account against her house): built with the Account (`tm_bae2.0011`, 2026-10-23).

## 2. Outlawry (built, modest)

Sources:
- Grágás K §§51-55 (lesser and full outlawry, the life-ring, three winters), K §155 and §254 (the dress clause); `research/norse_gragas_laws.md` §1.2-1.3.
- Mitchell pp. 150, 159-61 (from c. 1100 Christian-law suits bring outlawry or exile; Gulaþing sends a sorceress out of the realm; six housewives' oath; a cleared woman's accuser is a slanderer); `research/norse_mitchell_witchcraft_magic.md`.
- Ahola pp. 85-104 (forms, the plaintiff's burden), 97 and 226 (harbouring), 100 (pardon by settlement), 113 and 210 (Hörðr's band), 401 (exile as a stage before kingship); `research/norse_ahola_outlawry.md`.
- Miller pp. 237 (service far from enemies), 262-77 (settlement); `research/norse_miller_bloodtaking.md`.
- Sophoulis pp. 117 and 120 n. 26 (pardon for war service as a ruler's grace); `research/byz_sophoulis_banditry.md` proposal 4.

### Who can be sued, and when

`tm_bae2_outlawry_candidate_trigger` requires all of:
- She is Bædling, adult, not a ruler, and free.
- The year is 1100 or later.
- She is at the court of a **Christian lord of North Germanic heritage**.
- One of two charges applies:
  - **sorcery:** a daughter of seiðr, or she knows the warding songs;
  - **the dress clause:** a daughter, Marked or declared, or a woman knight or shieldmaiden.

Before 1100, and under pagan or English lords, no suit fires, because the mod has no source for one there. This keeps rule 13: the text never implies the pagan North was free; it simply has no sourced suit for it. Rule 24 is kept: the dress clause is Grágás, which is Christian-era Icelandic law.

### Pulse

`tm_bae2_yearly_outlawry` gives a 4% yearly chance per candidate, gated by the flavour budget of her lord, who sees the event.

The accuser is the first of these that exists:
1. for sorcery, the lord's Christian court chaplain;
2. else a Christian courtier or guest with opinion ≤ −10 of her;
3. else the lord himself, if his opinion is ≤ −10.

There is no suit without an accuser. She gets a 10-year cooldown either way.

### Events

- **`0100`, to the lord:** let the law take its course, or quash the suit. Quashing costs minor piety and gives the accuser `tm_bae2_suit_quashed_opinion` (−15). AI: zealous or just lords let it run; compassionate or cynical lords, and those who like her, quash it.
- **`0101`, to her** (always AI):
  - (a) **Six housewives swear for her**, for the sorcery charge only. The base chance is 50/50: +20 if she is of a House, +15 for diplomacy ≥ 12, −20 if her lord dislikes her. If cleared, the accuser loses prestige as a slanderer. If not, lesser outlawry.
  - (b) **Pay the life-ring and go abroad:** lesser outlawry.
  - (c) **Refuse the ring:** full outlawry.
- **Lesser outlawry** (`tm_bae2_lesser_outlaw_modifier`, 3 years):
  - She pays 10 gold to the lord if she has it.
  - She goes to a court of the six faiths outside the sentencing top realm, a House holder preferred; else to the pool.
  - The accuser gets `tm_bae2_outlawed_by_me_opinion`.
  - When the modifier ends she is free (K §53: "as if that outlawry had never befallen him").
- **Full outlawry** (`tm_bae2_full_outlaw_modifier`, no end date: −0.5 prestige a month, +2 prowess):
  - If she is under 55 with martial ≥ 8, prowess ≥ 10 or knighthood, she becomes a **vanilla landless adventurer**, leading her own band: `create_landless_adventurer_title_effect`, `REASON = flag:exile`, as the vanilla governor-contract "banish" option does.
  - Otherwise she goes abroad as above.
- **`0110`, a player ruler who receives an outlaw:** keep her (the accuser gets `tm_bae2_harbours_outlaw_opinion`, −15; she gains minor prestige) or send her on (`tm_send_on_effect`).

### Reprieves

- **Time:** lesser outlawry ends after 3 years.
- **Settlement** (`0130`):
  - A full outlaw with 100 gold or more has a 20% yearly chance to offer the accuser a settlement.
  - If he accepts, the outlawry is lifted and both get `tm_bae2_settled_with_me_opinion`.
  - If he refuses, she waits 3 years before offering again.
  - AI: greedy and forgiving lords accept; vengeful and zealous ones refuse.
- **Forgiven for the war** (`0135`, once only):
  - An outlaw allied in a war with the top liege of her accuser has a 50% chance to ask his pardon.
  - The ruler may pardon her (minor prestige loss) or refuse.
  - Pardon is a ruler's grace, not the law's (Sophoulis). A band hired through vanilla `laamp_join_war_contract` reaches this naturally.
- **The high seat:** any outlaw who gains a county loses the sentence (`tm_bae2_title_gain`; Ahola p. 401).

### Specified only (not built)

- The confiscation court. Ride for Sympathy. Houses sheltering outlaws (strain and the harbouring suit). The lair. The sister's revenge.

### The Account, the níð suit and reprieve by killing outlaws (built 2026-10-23, untested in game)

Files: `common/scripted_effects/tm_feud_effects.txt`, `tm_feud_triggers.txt`, `common/script_values/tm_feud_values.txt`,
`common/on_action/tm_feud_on_actions.txt`, `common/character_interactions/tm_feud_interactions.txt`,
`common/opinion_modifiers/tm_feud_opinion_modifiers.txt`, `events/tm_feud_events.txt` (namespace `tm_feud`),
`localization/english/tm_feud_l_english.yml`. Prefix `tm_feud_`.

**The Account** (Miller rows 1, 3, 13 and 17; research/norse_miller_bloodtaking.md). Vanilla 1.20 already keeps house
relations (feud, rivalry, quarrel, neutral, cordial) and moves them for killings, imprisonment, torture and maiming,
so the Account does not replace them. It adds what they lack: who owes whom, wrong by wrong.
- Each house keeps the houses that owe it, up to three unanswered wrongs each, in three variable lists
  (`tm_acc_1`, `tm_acc_2`, `tm_acc_3`). Kept on the houses, not on vanilla's relation, which vanilla prunes.
- A wrong opens or adds to it only where a Bædling is the one wronged or the one who wronged
  (`tm_feud_wrong_effect`). A wrong the other way is a requital and pays one off (Miller p. 182).
- Wrongs: a killing outside a war between the two realms (`on_death`; war is "the top of the scale, not the
  default"); a sister imprisoned (`on_imprison`, a woman, Marked, daughter or friend of a House of the Bædlings);
  a raid on a county with a Sisters' House (`on_raid_action_completion`); the three words said before witnesses in a
  flyting (row 13); a discovered Spring the Cell rescue, against the rescuer's house (row 17). Vanilla's house
  relation moves too for the last three, which vanilla does not count itself. Maiming has no hook the mod can use;
  vanilla's relation counts it.
- An outlaw's death is no wrong: she has no standing at law.
- **Offer Bót** (`tm_feud_offer_bot_interaction`, row 3). A ruler of the house that owes pays the house owed: 50 gold
  a wrong to a count, 100 to a duke, 150 to a king, 200 to an emperor. It closes the Account; the receiver gains
  prestige and the payer loses none; ten years' truce (`tm_acc_settled`). The AI offers through the yearly pulse
  (10% a year for a house head who can pay, more if just, calm or generous; `tm_feud.0010`). Refused, it waits three
  years.
- **The truce-breaker** (Miller p. 280): a wrong within the ten years costs the wrongdoer major prestige and an
  opinion of −40 from the one wronged, and the truce ends.
- Not built: escalation by rank (row 2), Grant Self-Judgment (row 4), the refused Account (row 5), fostering to seal
  a settlement, and the martial bonus for a reopened Account.

**The níð suit** (Grágás Add. §423, St §376; K §237). When the flyter's charge is *ragr* in a hall or at the thing
(stakes 1 or 2, so before witnesses), the word enters the Account and she may sue (`tm_feud.0020`), before the lord
of the hall (`tm_feud.0021`, who may be herself). The lord can outlaw the speaker (full outlawry, no fine: he leaves
the hall, as a band if he is a fighter; anyone may then kill him without a feud), arbitrate (he pays her 50 gold,
doubled at the thing, and the words come off the Account), or dismiss it. Never against a ruler or the lord himself:
a sentence on a landed man would be a revocation, which the mod leaves to vanilla. Alone, it is words for words
(K §237): no suit. The law punishes the speaker, never the one he names.

**Reprieve by killing outlaws** (Grágás K §110). When an outlaw is killed, the killer, if an outlaw, earns a step;
otherwise a sworn sister or kinswoman of the killer who is an outlaw does ("a free man may kill on his behalf").
Steps are announced at the next thing (the yearly pulse) and taken one at a time: full outlawry, then "an outlaw who
may be given passage" (`tm_feud_passage`: whoever takes her in owes the accuser nothing, `tm_bae2.0110`), then
lesser outlawry for three years, then free. A lesser outlaw goes free with one step. A player outlaw gets
`tm_feud.0030`.

Counts for observe runs: `tools/census_report.py`, "The Account".

## 3. Landless bands regaining land (built)

### How vanilla does it (1.20)

Paths are under `game/`. There is **no "found a realm" or "settle" decision**. Adventurers become landed through:
- the four invasion CBs (`07_ep3_wars.txt`; county invasion needs prestige level 2);
- `purchase_land_interaction` and `purchase_sacred_land_interaction` (the sacred variant needs a seller of her faith);
- `negotiate_settlement_interaction` (a landed ruler offers);
- the `seize_realm` scheme;
- claim wars (`claim_cb`, legitimists only from the UI; `become_conqueror_decision` uses it from script).

All of these end in `ep3_become_landed_transfer_effect`.

**The AI** (story cycle `story_adventurer_ai`) picks war targets by strength, distance, opinion and claims, with **no faith or culture term**. It gates on prestige level 2-5 by personality.

**After landing:**
- Vanilla gives **no grace**: only +50 county control after invasions, and an ennobled-adventurer *malus* (faith, culture, prestige). By my reading of the transfer effect, the malus rarely applies after a conquest.
- On losing the last county, the AI has a random chance to become an adventurer again (`ep3_laamps.0002`).

That is how a band can take a county and lose it at once: no grace, add-claim-on-loss for the old holder, and a fresh realm with few levies.

### Gunhild's band

I did not find which Dutch county it held: th.py on `c_zutphen` shows no Bædling holder. Gotland's history:
- Steinn (860), then Áslaug (910);
- conquered by a Norse pagan in 915;
- revoked twice;
- granted to a Catholic in 971.

The census counts no Bædling-people counties after the 1040s. So "people who keep the faith" alone would not have helped in run 4. The seats and Houses are included for that reason.

### What was built

- **`tm_bae2_answer_hall_decision`** ("Answer the Hall's Call", adventurer decision group). For a landless adventurer of any of the six faiths, not at war, prestige level ≥ 1 (one below vanilla's county invasion).
  - **Valid target:** a county within adventurer reach of her camp (`ADVENTURER_DISTANCE_RESTRICTION`, as vanilla's `ep3_laamp_diplo_range_trigger`). It is held by a lord of another faith, not her ally or enemy, and **its people keep her faith, or it has a Sisters' House, or it is her faith's seat** (`tm_bae2_welcoming_county_trigger`; the seat list mirrors `tm_for_each_seat_effect`).
  - **Cost:** 250 prestige.
  - **Effect:** a pressed claim on the nearest such county and a `claim_cb` war on its holder, started from script as vanilla `ep3_laamp_decision_event.1110` does.
  - **AI:** checks every 24 months; `ai_will_do` 40, with ambitious and brave up, craven and content down, and 0 below 300 strength. The AI only targets AI holders with an AI top liege whose strength is below the band's.
  - Nothing is guaranteed.
- **Return to the seat** (`tm_bae2_yearly_bands`): an AI faith band that is at peace, not travelling, and has no welcoming county in reach has a 15% yearly chance to move its camp toward the nearest welcoming county. It uses `start_travel_plan` with the domicile and tops up provisions, as `ep3_adventurer_ai_war_travel_effect` does.
- **Settling grace** (`tm_bae2_title_gain` on `on_title_gain`):
  - The yearly pulse marks every faith band (`tm_bae2_was_band`, 3 years).
  - When such a character gains a county, she gets `tm_bae2_settling_modifier` for 10 years: defender advantage +4, garrison +25%, levy reinforcement +25%, short-reign penalty duration −50%.
  - The county gets `tm_bae2_hall_returned_county_modifier` for 20 years if its people share her faith, or it has a House, or it is the seat: county opinion +15, levies +20%, control growth +0.5.
  - It applies however she got the land (decision, vanilla invasion, purchase, settlement).
- **No size caps.** Not transparent: the decision appears only when such a county is in reach.

### Merchant companies (future DLC note)

The better form of this would be a **company charter**. A band of the faith contracts with a city or House for a trading post (a barony or holding, not a county), pays dues, and holds it by contract rather than conquest. This is closer to Ha-Nehpakhot's burgher republics and the Garland's temple deal, and to Sophoulis's road-guard (Vigla) and "tower on the condition" cases. It needs a holding-level landless government and contract-held holdings, which 1.20 adventurers lack. If a future DLC adds merchant companies, move the settling path there and keep the county war as the last resort.

### Sophoulis proposals specified, not built

1. **The Strumica Peace.** An AI bonus on `negotiate_settlement_interaction` toward a faith band that keeps fighting a ruler. It needs an override of a vanilla interaction or an event for player rulers.
2. **The Merope Command.** Land after `laamp_join_war_contract` / `laamp_help_claimant_contract` in a civil war.
3. **The Vigla.** A road-guard contract.
4. **The Tower on the Condition**, for the Dorleyaian Mother House.

None encodes any culture as criminal. Survival-builder note: `tm_surv_gather_effect` already sends members with no court to the nearest faith court or camp. The outlaw's "go abroad" here is sentence-specific and does not duplicate it.

## 4. Rescue the Daughters (`common/casus_belli_types/tm_casus_belli.txt`, not mine)

How the pieces fit:
- Spring the Cell is the CB's non-war counterpart: it frees prisoners without a war, and it is open to courtiers and adventurers.
- Its prisoner test adds **declared sisters** (`has_variable = tm_declared`) to the CB's `tm_captive_daughter_trigger`.

Suggested changes (lead to decide):
1. **Let bands use it.** The CB's `allowed_for_character` excludes `government_is_landless_adventurer`, so a Bædling band cannot wage Rescue the Daughters. Vanilla's own forbidden-for-adventurers CBs (conquest, holy war) are the precedent for keeping that. If the lead wants bands to raid for their daughters, remove the adventurer line in `NOR` and keep nomads out. Because the CB transfers the county with `create_title_and_vassal_change`, a band that wins would then become landed through `on_title_gain`, and `tm_bae2_title_gain` would give it the settling grace. **Untested**: vanilla adventurers normally land through `ep3_become_landed_transfer_effect`, which also destroys the camp, so test before enabling.
2. **Declared sisters as captives.** To make the CB and the scheme agree, `tm_captive_daughter_trigger` (`tm_triggers.txt`, shared) could add `has_variable = tm_declared`. Exact text, inside its `OR`: `has_variable = tm_declared`. This widens Rescue the Daughters slightly.

## Uncertain syntax and behaviour

- **Custom agent types:** that the UI shows their names and contributions from `<key>`, `<key>_i` and `<key>_desc`, as vanilla's do; tiger accepted them.
- **`start_war` with `claim_cb` for a landless adventurer from a decision:** vanilla does the same in 1110. Whether the war's cost is charged on top of the decision's prestige is unknown.
- **`create_landless_adventurer_title_effect` on a courtier who has just been sentenced:** vanilla uses it on an escapee in `governor_contract_events_tova.0056`. `scope:host` is set to the lord only to satisfy a branch for young warriors that cannot fire.
- **`on_title_gain` timing:** the band variable is on the character, so it does not depend on whether the camp title is destroyed before or after.
- **`is_allied_in_war` from a variable's top liege with `prev`** in the pardon pulse.
- **Saved scopes copied into `trigger_event`** from inside `every_living_character` loops (outlawry pulse).
- **Event backgrounds:** `diplomacy`, `realm` and other themes that default to `throne_room` produce strict-scope warnings from vanilla's church backgrounds. The settlement event uses the `stewardship` theme with a `study` background for that reason.

## Test scenarios (TO-TEST style)

**Spring the Cell**
1. As a Bædling ruler, imprison nothing yourself. Via console, have a neighbouring Catholic count imprison a daughter of seiðr. Open the count's interactions: *Spring the Cell (Scheme)* shows, and the agent slots list Marked Guard ×2, Faithful Servant, Friend of the House and Lookout.
2. Let a phase complete. "A Night for It" offers tonight or wait. Choose tonight with high odds: the prisoner is released and appears at the nearest House holder's court (or yours if none). The jailer gets "An Empty Cell"; with low secrecy it names you and adds "Emptied My Prison".
3. Failure: "The Door Held" offers give up or go again; the jailer gets "Footsteps in the Yard".
4. AI: put a Marked prisoner in an AI dungeon with a sworn sister of hers (an AI ruler of the faith) in range. Within a few years the sister should own a Spring the Cell scheme against the jailer (character window, schemes).
5. Free the prisoner by other means: the scheme ends with "Spring the Cell Ends".

**Outlawry**
6. Set the date to 1100 or later. A Catholic Norwegian or Swedish count keeps a Bædling daughter of seiðr as courtier, and his chaplain dislikes her. In time the count (you) gets "A Suit at Law" with the church's charge. Quashing costs piety and the chaplain's opinion.
7. Let it run: the AI daughter takes the oath, the ring or the woods. Ring: she leaves for a faith court outside the realm with "Lesser Outlaw" (3 years). Woods, if she can fight: a new adventurer camp led by her, with "Outlaw".
8. As a Bædling ruler with a House, receive the lesser outlaw: "An Outlaw at the Door" offers keep or send on.
9. A full outlaw band with 100+ gold: the accuser gets "The Outlaw's Price". Accepting lifts the sentence.
10. Hire the outlaw band for a war on the accuser's side: the accuser's top liege gets "Forgiven for the War" once.
11. An outlaw band takes any county: the outlaw modifier is gone.
12. Before 1100, or under a pagan or English lord: no suit ever fires.

**Landless bands**
13. Play a Bædling adventurer with prestige level 1+, at peace, camped within reach of Gotland held by a Catholic. "Answer the Hall's Call" shows, costs 250 prestige, and opens a claim war for Gotland.
14. Win: "Settling the Hall" (10 years) on you and "Our Own Came Home" (20 years) on Gotland. Take a county by vanilla invasion instead: you get "Settling the Hall" only, unless the county keeps the faith or has a House.
15. Observe run: AI faith bands far from any welcoming county start travelling toward one, about one band in seven per year. Bands in reach of a weaker AI holder use the decision.

## Ready-to-paste README text

For the Bædling section, after "The flyting":

> - **Spring the Cell.** Anyone of the six faiths, landed or not, can plot against a ruler who holds a daughter, a Marked woman or a declared sister in prison. Marked guards, servants inside the house and friends of the House do the work. On success she walks free to the nearest House, and the jailer may never learn who opened the door.
> - **Outlawry.** From 1100, under Christian Norse lords, a Bædling may be sued at law: for sorcery by the church, or under the law of dress. Six housewives may swear for her. Otherwise she pays the life-ring and goes abroad for three winters, or refuses and is outlawed in full. A full outlaw who can fight leads a band of her own. A settlement, service in the realm's war, or land of her own ends it.

For Shared mechanics:

> - **Bands come home.** A landless band of any of the six faiths can answer the hall's call: go to war for a nearby county whose people kept the faith, which keeps a Sisters' House, or which is the faith's seat. A band that takes land has ten years' grace to hold it, and a county that kept the faith welcomes its own.

Roadmap: tick "Spring the Cell" and "outlawry and landless war-bands"; leave "feud and settlement" open.

## Ready-to-paste TODO text

```
## Bædling stage 2 and landless survival (added 2026-10-21, untested in-game)
- [ ] Spring the Cell (`tm_bae2_spring_cell`): scheme, three agent types, interaction, AI plotter search; prisoners to the nearest House
- [ ] Outlawry (`tm_bae2`, 0100–0135): suit from 1100 at Christian Norse courts (sorcery / dress clause), six housewives, life-ring, full outlawry → adventurer band; settlement, forgiven for the war, the high seat
- [ ] Answer the Hall's Call (`tm_bae2_answer_hall_decision`), return-to-the-seat travel, settling grace on `on_title_gain`
- [ ] The Account and Offer Bót, the níð suit, reprieve by killing outlaws (`tm_feud`, built 2026-10-23; untested)
- [ ] Not built: Sophoulis proposals 1–3 and 6
- [ ] Lead: Rescue the Daughters for adventurers? declared sisters in `tm_captive_daughter_trigger`? (docs/wave3/baedling.md §4)
```

## Decisions (user, 2026-10-21)

- **Rescue the Daughters is open to landless bands** (§4 suggestion 1). The lead removed the adventurer line from the CB's `allowed_for_character` (nomads stay out). On victory a band lands as vanilla's claim war lands it: the *adventurer* trait, and her courtiers marked as followers, before `create_title_and_vassal_change`. Untested; see TO-TEST.md L16.
- **Declared sisters count** (§4 suggestion 2). The lead added `has_variable = tm_declared` to `tm_captive_daughter_trigger` in `tm_triggers.txt`, so the war and Spring the Cell agree.
- **Outlawry stays, provisionally, only at Christian courts** (Christian lords of North Germanic heritage, from 1100). No suit under pagan or English lords until a source supports one.
- Merchant companies: a future-DLC item on the README roadmap and in TODO.md.
