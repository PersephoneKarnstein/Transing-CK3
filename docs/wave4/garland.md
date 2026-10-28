# The Worn Garland, wave 4: the market town and the road (design note, 2026-10-21, untested in-game)

Prefix `tm_ml3_` (new files), namespace `tm_ml3`; one option and two small changes in the stage-2 `tm_ml2_` files. Source: Kenneth R. Hall, *Trade and Statecraft in the Age of the Cōḷas* (1980), read in `research/ind_hall_cola_trade.md` (proposals 1–4 of its §11). Builds on stage 2 (`docs/stage2/worn-garland.md`: shares, gifts, temple streets).

**Why.** The Garland ends runs landless: courtiers at Hindu courts, a republic, a band. Stage 2 gave the courtier a share and gifts. This wave gives (a) a landless woman a gift that does not need a street of her own, (b) arrivals a cheap way onto a street, and (c) the faith's band a road back to land that is not conquest.

| # | Feature | Status |
|---|---|---|
| 8 | A Lamp Kept by the Market (fourth gift, through the *nagaram*) | Built (script and loc) |
| 9 | The Quarter That Dwindled (a share in an emptied quarter) | Built |
| 10 | Heroes of the Road (caravan contract) → a frontier market town (vanilla settlement) → the Lord of Vannadu (warning) | Built |

**Files.**
- New: `events/tm_ml3_events.txt` (0010, 0020, 0021, 0022, 0030, 0031, 0040); `common/task_contracts/tm_ml3_contracts.txt` (`tm_ml3_caravan_contract`); `common/on_action/tm_ml3_on_actions.txt` (`tm_ml3_yearly` on `yearly_playable_pulse`); `common/scripted_effects/tm_ml3_effects.txt` (`tm_ml3_market_lamp_effect`, `tm_ml3_caravan_done_effect`, `tm_ml3_settle_band_effect`); `common/scripted_triggers/tm_ml3_triggers.txt` (`tm_ml3_nagaram_county_trigger`, `tm_ml3_dwindled_lord_trigger`, `tm_ml3_garland_band_trigger`, `tm_ml3_caravan_employer_trigger`, `tm_ml3_town_giver_trigger`, `tm_ml3_town_county_trigger`); `common/modifiers/tm_ml3_modifiers.txt` (`tm_ml3_market_lamp_modifier`; county: `tm_ml3_erivira_county_modifier`, `tm_ml3_dues_freed_county_modifier`); `common/nicknames/tm_ml3_nicknames.txt` (`tm_ml3_nick_heroes_of_the_road`); `localization/english/tm_ml3_l_english.yml`.
- Changed (own files): `events/tm_ml2_events.txt` (0010 option e); `common/scripted_effects/tm_ml2_effects.txt` (half pay while `tm_ml3_resettled`; the variable is cleared when the share is removed); `localization/english/tm_ml2_l_english.yml` (`tm_ml2.0010.e`, decision tooltip).

Validation: ck3-tiger reports nothing in these files. Total 51 at the last run: the 24 baseline (23 + the `tm_interactions.txt:264` warning that was already there before this build) plus 27 from other builders' in-progress `tm_got_` and `tm_fut_` files. `tools/check_glyphs.py` is clean (loc uses plain letters: Kattur, Valikandapuram, Vannadu).

**Variables.** Character: `tm_ml3_resettled` (10 years, half pay), `tm_ml3_caravans` (count), `tm_ml3_town_offered` (20 years), `tm_ml3_warned` (20 years). County: `tm_ml3_market_lamp`, `tm_ml3_erivira` (a guild town; permanent, read by 0040). Contract: `tm_ml3_toll`.

## 8. A Lamp Kept by the Market

**What the player sees.** In *A Gift in My Own Name* (tm_ml2.0010), a daughter **with no land** (`is_landed = no`), with 40 gold, living in a county with a market town (any city holding: `tm_ml3_nagaram_county_trigger`) gets a fourth option, **"A lamp kept by the market, in my name."** 40 gold, +30 piety, the county is marked a temple street, and she gets *A Lamp Kept by the Market* (+0.1 piety, +0.1 prestige a month), **permanent**: the market keeps the lamp whether she stays or not. A second market lamp gives +25 prestige instead. The decision *Give to the Temple in My Own Name* opens the same event, so a landless playable daughter reaches it there too (tooltip updated). AI 30, +10 zealous, +10 with no share.

**Sources.** The chief's daughter at Valikandapuram (10th c.) gave a lamp "using the nagaram members as her intermediaries" (Hall p. 194; 241 of 1943–44). The *nagaram* became "the collective agent of the donor"; gold or animals went in and oil, ghee or paddy came out to the god, "even if they were to leave this village" (pp. 76–77).

**Decisions.** Perpetual endowment only: the text and code have no loan, interest, return or "investment". The gold is gone; what she keeps is the record. Women are donors here, never guild members (Hall §8: no woman appears in any guild record he cites). The narrator does not call her a temple woman. A city holding stands in for a *nagaram*: Hall's one-assembly-per-*nāḍu* thesis is his model (p. 161 n. 65), so the game's market town is a fair proxy.

## 9. The Quarter That Dwindled

**What the player sees.** From 970, a Hindu lord whose capital county has development under 12 or county control under 60, with a daughter of the Garland at court holding no share, may get *The Quarter That Dwindled* (tm_ml3.0010). The families of a quarter have gone where dues were lighter; the temple's lamps go short of oil. She asks for an empty house, and will keep the temple's oil and rice if he takes no dues while the quarter fills.
- **Settle her there, free of the city's dues.** Costs him nothing; +10 piety; she gets a share in his capital (stage 2's share, street mark included), +15 opinion. The share pays **4 gold a year for 10 years**, then the usual 8.
- **Let the quarter stand empty.** −5 opinion from her.

Chance 3% (+2 in 1070–1300), flavour budget on the lord. AI: settle 40 (+20 if he has under 50 gold, +10 generous, +10 zealous); refuse 20 (+20 arrogant).

**Sources.** Madras Museum Plates of Uttama Cōḷa (r. 970–85, reign dates general knowledge): a Kanchipuram quarter that "had dwindled" and stopped supplying oil and rice to a temple was resettled tax-free "in consideration of their poverty" (Hall pp. 74, 91); leaving as leverage and resettlement by remission (pp. 74–75, 198; p. 212 n. 47).

**Decisions.** The historical settlers were not women of the temple, and the loc does not say they were. The lord's text names no king. It gives arrivals a way onto a street at no cost to the host, which answers stage 2's "share lapses with no one in the county" problem. No size cap; one share per event.

## 10. Heroes of the Road, the guild town, and the Lord of Vannadu

**A captain for the road** (0050, added 2026-10-27 after run 23). In run 23 the faith had no band in six centuries: all 196 adventurer bands in the 1452 save were of other faiths, so the contract below, and wave 10's oath, hall and relic guard, never fired. The yearly pulse of a landed Hindu or Jain lord who could hire a caravan (`tm_ml3_caravan_employer_trigger`) now gives each AI daughter of the Garland at his court with a sword arm (martial 8 or prowess 10; adult, under 50, not a ruler, councillor or ruler's wife; `tm_ml3_road_captain_trigger`) 2 in 100 a year, 5 while the faith has no band anywhere (flavour budget; asked once per 15 years). His merchants ask her to raise a band: take the road (vanilla `create_landless_adventurer_title_effect`, reason `voluntary`; two hired swords of the lord's culture and faith, not the Garland's; +25 gold; a player lord gets a toast), or stay on the temple street (no cost: rule 23). AI 50 (+25 ambitious, +15 brave, +10 arrogant) / 30 (+20 content, +20 craven, +10 shy). She is hired by the merchants, not a guild member (§8). Guilds hiring troops: Hall 1980, pp. 154, 167–68, 191–93. Census: `bands_founded`, `bands_declined` on the wave 10 line.

**The contract** (`tm_ml3_caravan_contract`, vanilla Roads to Power task contract). Offered to a **landless adventurer band whose leader is of the Garland**, by a landed Hindu or Jain ruler whose capital is in `world_india_deccan` (Deccan, Tamil country, Lanka) and who holds a county with a city holding. It sits in vanilla's `laamp_contracts_hireling_group`, so it appears on a player's contract map like any other; vanilla standard triggers (`valid_laamp_basic_trigger`, treasury, sensible start, dramatic employers) and rewards (`laamp_rewards_disburse_ordinary_currency_effect`: gold, half prestige, provisions, opinion, contact). AI bands of the faith are given one directly (20% a year when they hold no contract), by the lord of the county they camp in or his top liege (`create_task_contract` + `accept_task_contract`, as vanilla's AI adventurer story does).
- *Heroes of the Road* (0020): a merchant's caravan of pepper and cloth to the coast. → 20–40 days →
- *Drawn Swords* (0021): at an unwalled market town, take a toll at sword point (+30 gold; honest/just stress; the guild may hear) or keep faith with the guild (+15 prestige; greedy stress). AI 60 (+20 honest, +20 just) / 15 (+25 greedy, +10 arbitrary). → 20–40 days →
- *The Coast* (0022): success 75 (−35 if tolled, +10 martial ≥ 12, +5 prowess ≥ 12); dismissed for the toll 25 (only if tolled); robbed on the road 15 (+10 martial < 8). The contract completes `success_standard` or `failure_standard`.
- After the **third** successful caravan the captain takes the nickname *of the Heroes of the Road* (if she has none), and the third employer, if he holds two counties or more, is at peace and has a county that is neither his capital nor his primary title, gets 0030 (once per 20 years per band).

**The frontier market** (0030 → 0031). *Where the Heroes of the Road Trade*: the employer may offer the band his county **farthest from his capital** (`ordered_held_county` by `squared_distance`). AI 25 (+20 generous, +15 craven, +10 if the county's control is under 60, −15 greedy) against 50 (+20 paranoid). If offered, the band answers in *A Town on the Far Road* (0031):
- **Hold it, and free the town of its dues** (50 gold): *Freed of Its Dues* (+10 county opinion, 10 years), then settle.
- **Hold it**: settle.
- **The road is our home**: +10 prestige.

Settling runs vanilla's `negotiate_settlement_interaction_effect` with the scopes and list its interaction sets (`scope:actor` = the ruler, `scope:recipient` = the band, list `offered_titles`, `scope:new_primary_title`), so vassalage, ended wars, the legitimacy cost and the "landed" messages are vanilla's. The county gets *A Guild Town* (+10% development growth, −10% control growth, 10 years: the guild, not the lord, keeps the peace) and the permanent mark `tm_ml3_erivira`.

**The Lord of Vannadu** (0040). From 1220, a ruler of the Garland who holds a guild town and has joined a faction against her liege (25% a year, once per 20 years): merchants tell the story of Valikandapuram. Leave the faction (+10 respect from the liege) or "We know our own road" (+10 prestige). A warning only; nothing is taken. AI 40 (+20 craven, +10 content) / 30 (+20 ambitious, +10 brave).

**Sources.** Guilds as merchants banded "for their mutual protection" (p. 151); *erivīrapaṭṭiṇam* (p. 143) far from the heartlands, royal protection "more symbolic than practical" (pp. 151, 188); guild regiments and hired troops (pp. 154, 167–68, 191–93); the Kaṭṭūr rules against tolls "by threatening people with drawn swords" (256 of 1912; pp. 151, 193) and the remission of dues with "twice the privileges" (p. 144); Valikandapuram: the "eighteen lands" guild's tenure and *śūradaḷam* (late 12th c.), the alliance with "the lord of Vaṇṇāḍu", and the Hoysaḷa generals under Rājarāja III (1216–60) who redrew three *nāḍu* into two (pp. 194–95).

**Decisions and guardrails.**
- **Coordination with `tm_band_`.** This is a **Garland-specific contract** that ends in **vanilla** Negotiate Settlement. It does not define a general band-to-land path; the general "Patent and Robe" settlement for every band is `tm_band_`'s. If both fire for the same Garland band, they should not conflict: mine only needs the band to still be a landless adventurer when 0031 fires.
- Bandits are merchants with swords (p. 193): the toll is the band's own choice, and the robbers in 0022 are "armed men", no people named. No "tribal" or "turbulent" wording.
- No caste ranking, no Kottayam "slaves" clause, no Hall vocabulary for temple women, no lending or war finance. No Jewish or Geniza merchant appears.
- The narrator does not claim the *vēḷaikkārar*, the Five Hundred or the Kaikkōḷa regiment for the faith; the guild is only named in the band's own first-person text as the hirer.
- Mercenary companies (vanilla AI mercenary titles) cannot take task contracts; this reaches only adventurer bands, including those with the mercenary camp purpose.

## Uncertain syntax (check in game)

- `create_task_contract` from a yearly pulse in the band leader's scope, then `accept_task_contract = scope:…`; vanilla does it inside its AI adventurer story (`07_dlc_ep3_story_cycle_adventurer_ai_scripted_effects.txt`). Whether `save_scope_as` inside `create_task_contract` works (the docs list it as optional).
- The contract's `on_create` copies `laamp_base_1001`: `task_contract_taker.task_contract_success_gold_gain_full_value` before the contract is taken. Vanilla does the same; if gold shows 0, use the employer instead.
- Loc for a contract: `<key>_contract` (name), `_desc_title`, `_desc`, `_request`, by vanilla's pattern. ck3-tiger may not check task-contract loc.
- `yearly_playable_pulse` reaching landless adventurer leaders (assumed; not checked).
- `negotiate_settlement_interaction_effect` called outside its interaction, from the band's event: scopes `actor`/`recipient`, the `offered_titles` list and `new_primary_title` are set first in the same effect.
- `order_by = "title_province.squared_distance(root.capital_province)"` (vanilla uses the same form in `09_dlc_mpo_scripted_effects.txt`).
- Saved scopes and the `tm_ml3_toll` contract variable carrying from 0020 to 0022 through `trigger_event`.
- `employer = prev` inside `root = { can_create_task_contract = … }` in the on_action.

## Test scenarios (for TO-TEST.md)

1. **Market lamp.** A landless Garland daughter with 50 gold in a county with a city: fire tm_ml2.0010; option e shows; take it: 40 gold gone, permanent modifier, county marked a street and `tm_ml3_market_lamp`. Move her: the modifier stays. Repeat for a landed daughter or in a county with no city: option e hidden. Fire it twice: +25 prestige the second time, no second modifier.
2. **Dwindled quarter.** After 970, a Hindu lord with a capital of development under 12 and a Garland courtier with no share: fire tm_ml3.0010; settle her; check the share, 4 gold a year for 10 years, then 8. Before 970 it must not fire from the pulse.
3. **Contract.** A player adventurer of the Garland camped in Tamil country: the contract *Heroes of the Road* appears on the map from a Hindu or Jain ruler with a city county. Accept: 0020 → 0021 → 0022; check both toll branches and that the contract completes (gold, prestige) or fails.
4. **AI contract.** An AI Garland adventurer in the Deccan: run yearly pulses and check it takes the contract and the chain completes.
5. **Town.** Set `tm_ml3_caravans = 2` and complete one more: nickname; 0030 to the employer (two counties or more); offer; 0031 to the band; both "hold" options settle the band as the employer's vassal in his farthest county, with *A Guild Town*; the dues option needs 50 gold. Decline: nothing changes. An employer with one county: no 0030.
6. **A captain for the road.** A southern Hindu lord with a city county and an AI Garland daughter at court (martial 8+): fire tm_ml3.0050 with `scope:tm_ml3_road_lord`; take the road: she holds a new adventurer title near his capital with two hired swords of his faith; the next yearly pulses offer her the caravan contract. Stay: nothing changes.
7. **Vannadu.** After 1220, a Garland countess holding a county with `tm_ml3_erivira` who joins a faction: 0040; leave the faction works; she is not asked again for 20 years.

## Ready-to-paste README text (Worn Garland section)

> **The market and the road (wave 4).** A daughter with no land can give a lamp through the market assembly of her county, which keeps it burning in her name for ever, wherever she goes. A poor Hindu lord may settle a daughter in an emptied quarter of his capital, free of its dues, at half a share's pay for ten years. A band of the Garland in the south can hire out to guard merchants' caravans to the coast; after three, the merchants' lord may offer the band a frontier county as a guild town, by a negotiated settlement. A guild town that joins a faction against its liege hears what happened at Valikandapuram. (Hall 1980)

## Ready-to-paste TODO text

- [x] Garland wave 4 (`tm_ml3`): a lamp kept by the market (tm_ml2.0010 option e); the quarter that dwindled (0010); Heroes of the Road contract (0020–0022) → guild town by vanilla settlement (0030–0031); the Lord of Vannadu (0040)
- [ ] Garland, from Hall §11, not built: Those Who Always Accompany Us (band sworn to merchants; Polonnaruwa); A Hall in the Name of the Five Hundred (band's *maṇḍapa* marks a street); the Pepper Merchant's Vow; a company of the Thousand Directions (wait for merchant companies)
- [ ] Badenya could borrow the caravan contract (a Mande trader as employer, not "the Dyula")
