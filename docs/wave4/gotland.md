# Wave 4: Bædling and Gotland

Proposals 1, 5 and 2 of `research/norse_dollinger_hansa.md` (Dollinger, *The German Hansa*, 1970). Prefix `tm_got_`, namespace `tm_got`. Untested in-game. ck3-tiger reports nothing in these files.

## Files (all new)

- `common/decisions/tm_got_decisions.txt`: *Open the Ports* and *Seize an Island Seat*.
- `common/on_action/tm_got_on_actions.txt`: yearly pulse, join-war, war-end (four on_actions) and title-gain hooks.
- `common/scripted_triggers/tm_got_triggers.txt`
- `common/scripted_effects/tm_got_effects.txt`
- `common/modifiers/tm_got_modifiers.txt`
- `common/opinion_modifiers/tm_got_opinion_modifiers.txt`
- `events/tm_got_events.txt`: 0100–0130 Open Ports; 0200–0210 the Island Changes Hands; 0300 the Peace of the Island.
- `localization/english/tm_got_l_english.yml`

Reused, read only: `tm_bae2_faith_band_trigger`, `tm_bae2_hall_in_reach_trigger`, the `tm_bae2_was_band` mark (which gives a band that lands the wave-3 settling grace), `tm_world_daughter_trigger` and the `tm_world_keep_quiet` variable, and the flavour budget.

## 1. Open Ports (Dollinger pp. 78–81, 111, 403)

The source: after 1389 the Mecklenburgers opened their ports "to all those who at their own risk would go to sea to harm the kingdom of Denmark" (p. 79). Knights, townsfolk, peasants and convicts came. In 1391 they took Visby as a base. The Peace of Skanör (1395) "removed the justification" (p. 80), and the Teutonic Order cleared the island in 1398 (p. 80).

### Contracts: what I read, and what I used

Contracts are scriptable from a mod. `create_task_contract` and `can_create_task_contract` work from script, and vanilla itself spawns `laamp_join_war_contract` from script (`spawn_join_war_contracts_effect`, `00_laamp_effects.txt`). I did **not** use `laamp_raid_contract`. It is a raid for captives against a rival's or feuding neighbour's capital, its target is chosen by the contract's `on_create`, and it is not tied to the employer's war. The licence is a war licence, so `laamp_join_war_contract` is the right vanilla piece. On acceptance it joins the war on the employer's side (`ep3_contract_event.0008`), and it pays a share by war contribution (`ep3_contract_event.0013`). That matches Bremen's booty share "in proportion to the men sent" (p. 403). I did not write a new contract type.

### What was built

- **Open the Ports** (`tm_got_open_ports_decision`, any faith)
  - **Who:** an independent landed ruler who leads a side in a war, has a coastal capital (`is_coastal_county`), and has a Bædling band camped within adventurer reach of that capital (`ADVENTURER_DISTANCE_RESTRICTION`).
  - **Cost:** 100 prestige.
  - **The war it covers:** the war he is losing (war score ≤ −20), else any war he leads. It is stored as `var:tm_got_ports_war`.
  - **The offer, to each Bædling band in reach:**
    - A **player** band gets vanilla's `laamp_join_war_contract` with him as employer, made as vanilla does it (`retain_despite_distance`, `task_contract_war`, and so on) and announced with a contract message. If vanilla's `can_create_task_contract` refuses (for example, his treasury is too low or the war's CB is not one vanilla allows), the band gets the event instead.
    - An **AI** band gets event `tm_got.0100`, because the mod cannot raise vanilla's AI weight for one contract. Taking the letters joins the war exactly as `ep3_contract_event.0008` does.
  - **AI use:** checked every 12 months, `ai_will_do` 0. It rises by +25 when he is losing, and by +10 each if he is ambitious or callous. Just or honest lords halve it.
- **The licence** (`tm_got_on_join_war`, on `on_join_war_as_secondary`)
  - **When:** a Bædling band joins the side whose leader opened the ports in that war, by the contract, the event or any other way.
  - **Effect:** the band gets `var:tm_got_licence` (the licensor), `tm_got_licence_enemy` and `tm_got_licence_war`, plus minor prestige. A player band gets a toast.
- **The licence lapses** (`tm_got_on_war_end`)
  - **When:** the licensed war ends, through `on_war_won_attacker`, `on_war_won_defender`, `on_war_white_peace` or `on_war_invalidated`. The yearly pulse is a safety net: a licensed band that is not at war lapses too.
  - **Effect:** the former enemy gets *Raided Under Licence* (−20, 10 years, decaying). The band keeps `tm_got_lapsed` for 10 years. It gets event `tm_got.0110` if its flavour budget is ready.
  - I did not add an outlawry modifier. The source's "outlaw" stage is the clearing war below.
- **Seize an Island Seat** (`tm_got_seize_island_decision`, adventurer group)
  - **Who:** a licensed Bædling band.
  - **Cost:** 150 prestige. The licence stands in for vanilla's prestige level.
  - **Target:** an island county within reach of the camp, held by someone who is not the band, not the licensor, not in the licensor's realm and not an ally. The AI only targets an AI holder who is weaker than the band. Gotland comes first, then the nearest.
  - **Which counties count as islands:** Gotland, Åland, Ösel, Bornholm, or any coastal county with no land neighbour. The last test is a heuristic.
  - **Effect:** a pressed claim and a `claim_cb` war, as *Answer the Hall's Call* does. It also sets `tm_bae2_was_band`, so a band that wins gets the wave-3 settling grace.
  - **AI:** `ai_will_do` 25, with personality modifiers, and 0 below 300 strength.
- **The island seat** (`tm_got_title_gain`)
  - **When:** a licensed or lapsed Bædling holder gains an island county, by this decision or any other way.
  - **Effect:** the county stores `tm_got_island_seat` and gets a 5-year quiet period. Event `tm_got.0120` fires if the flavour budget allows.
- **The clearing war** (`tm_got_yearly`)
  - **When:** each year, for an island seat still held by its band, after the 5-year quiet period, when the band is no longer licensed and is at peace. The chance is 10% a year, with a 15-year cooldown.
  - **Who comes:** the strongest independent AI king or emperor of another faith who is in diplomatic range, stronger, not allied with the band and not its liege (`tm_got_clearing_power_trigger`). The power can be of any faith or people.
  - **Event `tm_got.0130`, to the band:**
    - **Hold the island:** the power gets a pressed claim and a `claim_cb` war.
    - **Pay 100 gold:** the gold goes to the power, and the band takes a medium prestige loss.

**Guardrails.** No culture is coded as pirates. The licence is open to any faith's lord, and the band's men are "knights, townsfolk, farmers' sons". The only "sea-thieves" line is the clearing power's own, in event 0130. The 1401 beheadings are not used.

**Specified, not built:** fleeing to a petty coastal lord (East Frisia, p. 80). Turning a landed band back into a camp from script is risky. Vanilla `ep3_laamps.0002` already gives a band that loses its last county a chance to camp again.

## 2. The Island Changes Hands (pp. 67, 79–80, 291)

- **Trigger** (`tm_got_title_gain`): `c_gutland` passes to a holder who is not Bædling.
  - It fires for any transfer type except inheritance, election, appointment, appointment succession, abdication, stepping down, creation and leases. In practice that means conquest, grants, revocations, usurpation, independence and similar hand-overs.
  - The faith must have people there: members located in the county, or a county that kept the faith.
  - At most once every 5 years.
- **Dispatcher** (`tm_got.0200`, hidden, on the new lord). It finds three things:
  - **The time** (`tm_got_find_era_effect`). Vanilla has no Gotland title history, so "vanilla history matches" means the new holder's realm matches the historical one:
    - **1355–70**, under the Danish crown: Valdemar (p. 67).
    - **1385–1400**, a holder with vanilla's *adventurer* trait, which is a band that has landed: the Brothers (p. 79).
    - **1395–1406**, a Christian theocracy, or a holder under one, or under the holder of `k_livonia`: the Order (p. 80).
    - **1405–15**, under the Danish crown: Denmark again (p. 291).
    - **Otherwise:** generic text.
  - **The hostile voice:** the new lord's Christian chaplain, else the lord himself if he is Christian. From 1200 the voice cites the crusade shipping (p. 28), attributed: "this island once fitted out ships to carry the cross…". Before 1200 the voice calls only for the font. The narrator never mentions the crusade.
  - **Who speaks for the islanders:** an adult Bædling on the island who does not hold it. A player is chosen first, then a ruler, then the ablest by martial plus diplomacy.
  - **Routing:** if that person's flavour budget is ready, she gets `tm_got.0201`. Otherwise the island decides quietly: keep quiet 70, levy 20, ships 10.
- **The choice** (`tm_got.0201`):
  - **Keep quiet in this land.**
    - If Gotland kept the faith, it gets *Kept Quiet* for 15 years: county opinion +5 and control growth +0.2.
    - Ruling daughters on the island take the shared `tm_world_keep_quiet`, which *Speak Aloud Again* undoes.
  - **Raise the island's levy, as in 1361** (p. 67).
    - **Success chance:** 20%. It is +10 each for martial ≥ 12, a county that kept the faith, and a Bædling band camped nearby.
    - **If the levy holds:** county control −40 and *The Farmers' Army Stood* for 10 years (opinion −15, levies −20%, tax −10%).
    - **If it breaks:** control −15 and *Broken* for 5 years.
    - **Either way:** Bædling fervour +3, prestige for the leader, and *Raised the Island Against Me* (−25) from the new lord.
    - **Follow-up events:** the result is shown in 0202. The new lord gets 0210 if his budget allows.
  - **To the ships.** The faith's members on the island who are not rulers, and not the new lord's spouse, go to the nearest Bædling ruler (band or court) who does not hold the island and is not their current employer.
- **Not used:** the burghers shutting Visby's gate in 1361 is general knowledge, not in this source (note §4, §11). It is kept out of the loc.

## 3. Swear the Peace of the Island (pp. 7, 24–25)

- **Pulse** (`tm_got_yearly`): the holder of `c_gutland`, of any faith, adult and free.
  - **When:** the faith's people live there (members on the island, or a county that kept the faith), or a Bædling band camps within reach of Gotland.
  - **Chance:** 5% a year, once per ruler (`tm_got_peace_asked`). It spends the flavour budget.
- **Event `tm_got.0300`:**
  - **Text from 1161:** the duke of Saxony's oath between the Gotland farmer-traders and the German merchants (p. 24), and the town with one law and a council from both peoples (p. 25). Henry the Lion is not named; the text says "a duke of Saxony". The narrator does not claim the Gotlanders for the faith.
  - **Text before 1161:** trading places shared by several villages (p. 7).
  - **Second paragraph:** one variant each for a Bædling ruler, a band nearby, or members of the faith living there.
  - **Swear:**
    - The county gets *The Peace of the Island* for 25 years: opinion +10, development growth +15%, tax +5%. This is the shared town.
    - The county gets `var:tm_got_island_peace` (the ruler) for 25 years.
    - *Sworn the Peace of the Island* (+20, 25 years) goes both ways between the ruler and every faith member on the island and every Bædling band camped nearby. This is the lower hostility.
  - **Refuse:** nothing happens.
- **AI:** swears at 50, more if just, a diplomat, greedy or Bædling, and ×0.3 if zealous.

Faith hostility itself cannot be changed per county or per ruler (the hostility modifiers apply to the character, against all other faiths). The opinion pair is the honest local form.

## Uncertain syntax and behaviour

- **`create_task_contract` from a decision on a player band, and the contract variables.** Copied from `spawn_join_war_contracts_effect`. I did not check whether the contract's `on_create` overwrites them; vanilla's own spawner relies on the same order.
- **`on_join_war_as_secondary` after `add_attacker` from script.** I expect it to fire, but the offer event also records the licence directly, guarded against a double record.
- **`scope:war` in the four war-end on_actions.** Vanilla uses it in `on_war_white_peace` and `on_war_invalidated`, and `on_war_won_*` say "same scopes as the CB".
- **Comparing a variable that holds a war** (`var:tm_got_ports_war = scope:war`). Vanilla stores wars in contract variables. Whether the comparison holds after save and load is untested.
- **The island heuristic** (`is_coastal_county` with no `any_neighboring_county`) depends on whether sea-crossing adjacencies count as neighbours.
- **`ordered_ruler` with `order_by = max_military_strength`** for the clearing power.
- **`change_fervor` with `desc`,** as the vanilla hunt does.

## Test scenarios (TO-TEST style)

**Open Ports**
1. As a coastal Danish or Swedish king at war, with a Bædling band camped nearby (console: create a Bædling adventurer near your capital), *Open the Ports* shows. It is valid only with that band in reach and costs 100 prestige.
2. With a player band: the band gets the "Open Ports" contract message, and its board shows *Stand with Us* with your king as employer. Accepting it joins the war and gives the toast "We Hold the Letters".
3. With an AI band: it gets "Open Ports" (0100) and usually takes the letters if it is brave or ambitious and has 200 or more strength. Check that it is in the war on the king's side.
4. While licensed, the band's adventurer decisions show *Seize an Island Seat*. It costs 150 prestige and declares a claim war, on Gotland first if in reach.
5. End the war (white peace): the band gets "The Licence Lapses" and the former enemy has "Raided Under Licence". *Seize an Island Seat* is gone.
6. A licensed band that takes Gotland gets "A Harbour of Our Own". Five or more years after the lapse, an AI king of another faith may gather a fleet (0130). *Hold* starts his claim war; *Pay* costs 100 gold.

**The Island Changes Hands**
7. Put Bædling courtiers on Gotland (the holder's court), then hand Gotland to a Catholic by console (`create_title_and_vassal_change`, or conquer it). The ablest Bædling there gets "The Island Changes Hands". Inheritance never fires it.
8. Date variants: set the year to 1361 with a Danish top liege, to 1391 with a holder who has the *adventurer* trait, to 1398 with a Christian theocracy, or to 1407 under Denmark. Each shows its own opening; other cases show the generic one.
9. The voice: a Catholic chaplain after 1200 speaks the crusade line in quotes, as his own; before 1200 he calls only for the font. A Norse pagan lord has no voice line.
10. Levy: the result event shows held or broken, the county gets the matching modifier, and Bædling fervour +3. The new lord gets "The Farmers Take Up Arms".
11. Ships: the non-ruler members leave for the nearest Bædling court or camp.
12. With no members on the island but a county that kept the faith, no event shows and a modifier appears (usually *Kept Quiet*).

**Peace of the Island**
13. Gotland held by a Catholic, with Bædling courtiers there or a Bædling band camped nearby: within some years "The Peace of the Island" fires once. Swearing it adds the county modifier and mutual +20 opinions. Before 1161 the opening text is the generic one.

## Changes needed in files I do not own (lead to decide)

1. **Bands should not seize an island sworn to peace.** To make the oath restrain AI bands, `tm_bae2_hall_county_trigger` (`tm_bae2_triggers.txt`) could add, inside its AI-only `trigger_if`:
   `NOT = { has_variable = tm_got_island_peace }`
   Optional; the oath works without it.
2. **The README seat list:** no change needed.

## Ready-to-paste README text

For the Bædling section, after "The band":

> - **Open Ports.** A lord at war, of any faith, may open his ports to anyone who will raid his enemy at their own risk, as the Mecklenburg lords did after 1389. A Bædling band near his coast can take the letters (the vanilla join-war contract) and may seize an island seat while the war lasts. Peace ends the licence. An island held after that may draw a great power's fleet.
> - **The Island Changes Hands.** When Gotland passes to a lord of another faith, the faith's people there choose: keep quiet in this land, raise the island's levy as the farmers did in 1361, or go to the ships.
> - **The Peace of the Island.** Gotland's ruler, of any faith, may have the island's peoples swear peace, as German and Gotland traders did in 1161: one town, one council, and less ill will between them.

## Ready-to-paste TODO text

```
## Gotland (wave 4, added 2026-10-21, untested in-game; docs/wave4/gotland.md)
- [ ] Open Ports (`tm_got_open_ports_decision`): vanilla join-war contract for player bands, event 0100 for AI bands; licence recorded on join, lapses at peace (0110); Seize an Island Seat (claim war); island seat (0120) and the clearing fleet (0130)
- [ ] The Island Changes Hands (`tm_got.0200`–`0210`): non-inheritance transfer of c_gutland to another faith; 1361 / 1391 / 1398 / 1407 variants by realm; keep quiet, the levy, the ships
- [ ] Swear the Peace of the Island (`tm_got.0300`): yearly 5%, once per ruler; county modifier and mutual opinions
- [ ] Not built: flight to a petty coastal lord (East Frisia); Proposals 3, 4, 7 wait for merchant companies; 6 (the vitte) not in this wave
- [ ] Lead: AI bands spare a sworn island? (`NOT = { has_variable = tm_got_island_peace }` in tm_bae2_hall_county_trigger)
```
