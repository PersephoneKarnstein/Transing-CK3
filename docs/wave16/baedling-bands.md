# Bædling bands, wave 16: the Vigla, a harbour with a petty coastal lord, The Sword Is My Patent

Roadmap item (README, "Still to do"): "Bædling bands: the Vigla, flight to a petty coastal lord, The Sword Is My Patent, the darker Companions". Built 2026-10-29, untested in game. Namespace `tm_bae7`.

It builds on wave 3's bands (`docs/wave3/baedling.md` §3: `tm_bae2_faith_band_trigger`, the `tm_bae2_was_band` mark and the settling grace), wave 4's bands (`docs/wave4/bands.md`: the Patent and the Robe, `tm_band_served`, `tm_band_grant_patent_effect`) and wave 4's Gotland (`docs/wave4/gotland.md`: Open Ports, `tm_got_licence` / `tm_got_lapsed`). The model for the contract is the Worn Garland's caravan (`tm_ml3_caravan_contract`, `docs/wave4/garland.md`).

**New files** (all with a BOM): `common/task_contracts/tm_bae7_contracts.txt`, `events/tm_bae7_events.txt`, `common/decisions/tm_bae7_decisions.txt`, `common/scripted_effects/tm_bae7_effects.txt`, `common/scripted_triggers/tm_bae7_triggers.txt`, `common/on_action/tm_bae7_on_actions.txt`, `common/modifiers/tm_bae7_modifiers.txt`, `common/opinion_modifiers/tm_bae7_opinion_modifiers.txt`, `localization/english/tm_bae7_l_english.yml`.

**Small edits to existing files** (three lines in `events/tm_band_events.txt`):
1. `tm_band.0001`, option b (*ask her to move on*) and option c (*let them be*): one line each, `tm_bae7_patent_refused_effect = yes`. It does nothing unless the lord's offer came from the band's patience (`scope:tm_band_reason = flag:patient`).
2. `tm_band.0020`, option a (*We go. Patience costs us nothing.*): one line storing the county of the unpressed claim as `tm_bae7_claim_county` (20 years).

Shared files: a new block in `tools/census_report.py`, a section in `docs/TO-TEST.md`, a block in `docs/TODO.md`, the README roadmap and a paragraph in the Bædling section.

**Validation.** xTiger: 23 reports, identical to the baseline, none in `tm_bae7` or `tm_band_events.txt`. `tools/check_glyphs.py`: clean.

---

## 1. Keep the Road: the Vigla (`tm_bae7_vigla_contract`; `tm_bae7.0001`–`0021`)

### Source

`research/byz_sophoulis_banditry.md`, design table row 3, "The Vigla":
- The watch and its tax. *Vigla* / *vigliatikon* (Byzantine), *gradobljudenije*, the guard service on towns and roads, and the *kefalija* (Serbian) (pp. 105–112).
- The road's keepers answer for losses. Dušan's Zakonik, arts. 157–160: guards are posted on the roads, robbed travellers are repaid, and the sum is recovered from the officers (pp. 100–101).
- Guards who rob. In 1327 hired road guards in the Strymon valley ambushed travellers themselves (Gregoras; pp. 60, 107). The Burmazi, settled on the Serbian–Ragusan border with "policing and garrison duties", looted often (p. 107).
- The row's shape: a *Keep the Road* contract; a ruler pays the band to guard one county for 3–5 years; the county gets less banditry and control loss, paid for by a *vigliatikon*-style tax; a yearly *Guards' Habit* event after 1327; on a clean completion, a settled garrison (the Burmazi).

Parallel shape: `research/isl_negre_ribat_andalus.md` row 3, *The Watch on the Coast* (a coastal post contract, 3–5 years, "a hired guard, never jihad"). Not built in this wave; the Vigla's contract could carry it later (open question 2).

### What was built

**The contract.** `tm_bae7_vigla_contract`, a new Roads to Power task contract in vanilla's hireling group (the mod already has one, the Garland's caravan). Vanilla standard triggers and rewards (`valid_laamp_basic_trigger`, treasury, sensible start, dramatic employers; `laamp_rewards_disburse_ordinary_currency_effect`: gold, full prestige, provisions, opinion, contact).
- **Who takes it:** a band of the six faiths (`tm_bae2_faith_band_trigger`), not already keeping a road.
- **Who hires:** a landed lord, not a camp or herders' realm (`tm_bae7_vigla_employer_trigger`), who holds a county where the band camps or next to it, and whose road is worth watching: county control under 90, or a border with another realm (`tm_bae7_vigla_county_trigger`).
- **Players** find it on the contract map. **AI bands** with no contract under way are given one at 10 in 100 a year by the holder of the county they camp in, or his liege (`tm_bae7_yearly`, as the Garland's caravan). After a term, a band rests three years before the AI takes another.

**The term** (`tm_bae7.0001`, on acceptance). The county is chosen (the camp's county first, else the nearest that qualifies, else his capital), a term of 3, 4 or 5 years is drawn, and the county gets **The Watch on the Road** for the term: +0.3 control a month, travel danger −10, tax −5% (the watch's tax). The text varies: the *vigla* as an old office "with its own name and its own tax" in south-east Europe and Anatolia; a plain road elsewhere.

**Each year** (`tm_bae7.0002`, hidden). If the band has moved its camp away from the county and its neighbours, or the lord has died, lost the county or is at war with the band, the watch ends (`0021`, failure). Otherwise the lord pays the watch 15 gold (if he has it), and one of:

| Event | Weight | Choices |
|---|---|---|
| *A Thief on the Road* (`0010`) | 30 | To the lord's court (+10 prestige; the lord **Kept My Road**, +10) / the purse back and the boy home (+5 county control; compassionate and forgiving relieved). The Zakonik's rule is the merchant's lever: the keepers answer for the road. |
| *The Toll at the Ford* (`0011`) | 25 | Let him through (+10 prestige) / what the letter says (+10 gold) / twice it (+25 gold; 30 in 100 the lord takes **Took Twice the Toll**, −15) |
| *The Guards' Habit* (`0012`) | 20, from 1327, once a term | Keep faith (+15 prestige) / take the caravan (+60 gold; 35 in 100 found out within months; if not, 25 in 100 at the term's end) |
| a quiet year | 40 | — |

**The term served** (`tm_bae7.0020`): the contract completes with vanilla's success reward. If the band did not rob the road, it now remembers the lord's service (`tm_band_served`, 10 years), so wave 4's search (`tm_band.0002`) gives him 25 in 100 a year to offer the band one of his counties. That is the settled garrison of the record, as a county.

**Found out or abandoned** (`tm_bae7.0021`): failure reward; a found-out band gives the lord **Robbed the Road I Paid Them to Keep** (−30, 15 years).

### Decisions

- **A county, not a barony.** The row asks for "a barony or holding" as a garrison. A landless adventurer cannot hold a single barony in 1.20; settlement is by county (vanilla Negotiate Settlement). The Vigla feeds the existing Patent and the Robe instead of adding a second settlement path.
- **Open to all six faiths' bands.** The row is written for any band, with a Dorleyaian framing in Anatolia; the wave 4 bands are all six. The Bædling band is one of them (open question 1).
- **Nothing fought on screen.** The thief is "brought in"; the guards' robbery is "take what they carry, and send them on". Thieves and robbing guards are an occupation (Sophoulis reads hired guards who robbed as a sign of weak states, p. 107), never a people; no Vlach, Albanian or Slav is named.

---

## 2. A harbour with a petty coastal lord (`tm_bae7.0030`–`0033`)

### Source

`research/norse_dollinger_hansa.md` §(Open Ports) and row 1: after the Order took Visby in 1398, most of the pirates moved to the North Sea, where the count of Oldenburg and East Frisian lords received them (p. 80); they were defeated in Frisia in 1400 (pp. 80–81). The note's design use: "the band's last refuge is with petty coastal lords". Wave 4 (`docs/wave4/gotland.md`) left it unbuilt: "Turning a landed band back into a camp from script is risky. Vanilla `ep3_laamps.0002` already gives a band that loses its last county a chance to camp again."

### What I chose

**No land-to-camp conversion from script.** The offer comes *before* the loss, and is taken up *after* it, by whatever road vanilla has left her:
- if vanilla made her a camp again (`ep3_laamps.0002`), the camp may sail to his coast;
- if not, she may go to his court as a courtier.

Either way she may decline (writing rule 23).

### What was built

- **A landed Bædling band** (`tm_bae7_landed_band_trigger`): a Bædling ruler of one or two counties who came to land as a band (marked `tm_bae7_landed_band` by `tm_bae7_title_gain` when a character with `tm_bae2_was_band` or the settling grace gains a county), or who held Open Ports letters (`tm_got_licence`, `tm_got_lapsed`).
- **Losing her land** (`tm_bae7_losing_her_land_trigger`): she is the primary defender of a war with the defender's war score at −30 or worse.
- **The pulse** (`tm_bae7_quarterly`, quarterly): 50 in 100 a quarter while both hold, once per 10 years, within the flavour budget for a player.
- **The lord** (`tm_bae7.0030`, hidden; `tm_bae7_harbour_lord_trigger`): the nearest AI count or duke with a coastal capital in her diplomatic range, at peace (so on no side of her war), not her rival, liege or vassal, of any faith that does not hold hers evil. The text says he "does not much care whose gods a crew keeps".
- **His word** (`tm_bae7.0031`): *Tell him we may come* (both take **Harbour Promised**, +20; she keeps `tm_bae7_harbour` for 10 years) or *We hold the hall* (+15 prestige).
- **The harbour** (`tm_bae7_title_lost` on `on_title_lost`, then `0032` seven days later, then `0033`): if she has no land left, is free, and he still lives and holds land:
  - a camp again: *To his coast, with the camp* (the camp travels to his capital, provisions topped up as in `tm_band_move_on_effect`; +10 prestige);
  - no camp: *To his court* (`add_courtier`);
  - or *I will find my own way*.

**Guardrails.** Neither Oldenburg nor East Frisia is named in loc; the narrator says only that "bands driven off an island they once held found a last landing with small lords along the coast". No people is coded as pirates. The 1400 defeat and the 1401 beheadings are not used.

---

## 3. The Sword Is My Patent (`tm_bae7_sword_patent_decision`; `tm_bae7.0040`)

### Source

`research/isl_tor_violent_order.md` row 2, *Patent and Robe*: "A later *The Sword Is My Patent* decision, open only to a band that left when asked and was then wronged, lets her press the stored claim by war." Tor §4 item 7: at Nishapur, told he had no caliph's patent, Yaʿqūb had a sword brought: "This sword has placed me, too, in this position" (p. 150). Tor reads it as a *ghāzī*'s claim to justice, not "might makes right" (pp. 150–151). The row's caution: "Keep 'sword' lines out of the narrator's voice if the faith is not militant."

### The TODO's question: build, or leave it to the stored claim?

`docs/wave4/bands.md` left it to "the stored claim and vanilla CBs". I checked: vanilla's claim CB accepts an unpressed claim (the claim becomes pressed when used; `game_concept_unpressed_claim_desc`), and its `allowed_for_character` is commented out, so a band can already declare that war. **Built anyway**, because the decision adds three things the claim alone does not:
1. **A wrong that is remembered.** Before this wave nothing marked a band that was patient and then refused. Now a refusal after patience is recorded (`tm_bae7_wronged_by`, 20 years; **Refused Me After I Was Patient**, −20), and only then is the decision shown.
2. **The lord's last chance.** The decision sends the county's holder a letter (`tm_bae7.0040`): he may give her the county now (through wave 4's `tm_band_grant_patent_effect`, so vanilla's settlement, when he has two counties and it is not his capital or primary title), or let it be settled in the field (the claim war follows). The sword is a patent offered, which is how Tor reads the line.
3. **An AI reason to press this one claim.** The AI does not otherwise single out the stored claim; it gets `ai_will_do` 30 (ambitious, wrathful, vengeful up; patient and craven down; never below 300 strength).

### What was built

- **The wrong** (`tm_bae7_patent_refused_effect`, called from `tm_band.0001` options b and c): when the lord's offer came from the band's patience and he asks her to move on again or lets her be. A player band gets a toast.
- **The decision** (adventurer group): shown to a band of the six faiths with `tm_bae7_wronged_by`; valid at peace while she still holds the claim on the stored county (`tm_bae7_claim_county`) or on another county of the lord who refused her, held by someone not her ally and not at war with her (`tm_bae7_sword_county_trigger`). Costs 100 prestige.
- **The letter** (`tm_bae7.0040`, to the county's holder): "This is my patent, she writes, and she would rather have had yours." The line is hers; the narrator has none.
  - *Give her the county* (AI 20; +30 if she is stronger; +20 craven; +10 just; ×0.5 arrogant or stubborn).
  - *Then let it be settled in the field* (AI 60; +20 arrogant, +20 wrathful): she declares `claim_cb` on him for that county, marked `tm_bae2_was_band` so a win brings the wave-3 settling grace.

---

## 4. The darker Companions (not built)

### What the sources say

- `research/isl_tor_violent_order.md` §4 item 3: one version has Dirham plot against Yaʿqūb, "who struck first" (p. 109).
- Row 1's design: "A darker branch, *The Plot Discovered*, lets the officer strike first if the leader schemes against her."

### Why it was not built

- **The source is one clause.** "Struck first" has no in-game meaning that is not violence against the leader, and this mod puts no violence on screen. Any non-violent reading (the companions seize the camp, the old leader is put out of it) would be my invention.
- **It cuts against wave 4's consent rule.** The Companions Choose fires only on the leader, and "no player is ever replaced without the event" (bands.md, B8). A plot branch takes the band against the leader's will.
- **It rides on an untested mechanism.** It would reuse `tm_band_hand_over_effect`, whose main risk (does the camp's domicile and men-at-arms follow `change_title_holder`?) is still untested (TO-TEST §U6).

Also not built: Dirham's other road (pilgrimage, then a lord's envoy), and *Ghazis Have No Wealth* (declined by the user in wave 4).

---

## 5. Counting

`tm_bae7_tally_effect` keeps run-wide globals `tm_bae7_n_<what>`, printed by `tools/census_report.py` under "Bædling bands: wave 16" (after "Worn Garland: wave 11"):

`vigla_offered`, `vigla_taken`, `vigla_done`, `vigla_failed`, `robber_court`, `robber_home`, `toll_waived`, `toll_kept`, `toll_double`, `habit_kept`, `habit_took`, `habit_found`, `harbour_offered`, `harbour_promised`, `harbour_refused`, `harbour_camp`, `harbour_court`, `harbour_stayed`, `patent_refused`, `sword_drawn`, `sword_granted`, `sword_war`.

## 6. Growth

Nothing here adds members or changes conversion. The Vigla gives a band gold, prestige and a lord's memory, which wave 4 can turn into land. The harbour keeps a beaten Bædling ruler alive in someone's court or on the road, which may help the faith hold on in the world (the last observe run ended with 6 Bædling in 1547). There is no size cap and no growth multiplier.

## 7. Uncertain syntax and behaviour (check in game)

- **A new task contract's loc keys**: `<key>_contract`, `_desc_title`, `_desc`, `_request`, as the Garland's (xTiger may not check them).
- **Saved scopes across a year** (`scope:task_contract`, `scope:employer`) through the self-repeating `tm_bae7.0002`. The Garland chain carries them for weeks, not years.
- **`complete_task_contract` through `scope:task_contract ?=`** after vanilla has invalidated the contract (the employer died): the chain should end quietly.
- **The camp's men-at-arms and the camp move** in `tm_bae7_camp_to_harbour_effect` (copied from `tm_band_move_on_effect`, also untested).
- **`on_title_lost` order**: whether vanilla's `ep3_laamps.0002` has run within seven days, so that 0033 sees her as a camp again.
- **`ordered_ruler`** over every ruler for the harbour lord: rare (once per ten years per landed Bædling band), but heavy.
- **`defender_war_score`** read from `any_character_war` with `primary_defender = root`.
- **`start_war` with `claimant`** from inside the band's scope in an event option of the lord.

## 8. Open questions for the user

**Decided (user, 2026-10-29): every default below is accepted.**

1. **Who may keep the road?** Built: the bands of all six faiths (wave 4's bands are all six; the research row names the Dorleyaian band too). Default: keep all six. Alternative: Bædling only, as the roadmap line reads.
2. **The Watch on the Coast.** The Négre row (a coastal post contract for Badenya and Ha-Nehpakhot bands under Muslim lords, cancelled when the realm centralises) has the same shape. Default: not in this wave; a second contract type on the same chain later.
3. **The garrison.** Built: a clean term makes the lord remember the band's service, so wave 4's Patent and the Robe may offer a county. Default: keep. Alternative: an immediate settlement offer at the term's end (closer to the row's "on completion").
4. **The guards' habit.** 35 in 100 found out at once, 25 in 100 at the term's end; +60 gold. Default: keep.
5. **The harbour's lord.** Built: AI counts and dukes only, any faith that does not hold Bædling evil. Default: keep. Should a player petty lord also be asked to give a harbour?
6. **Bædling only for the harbour?** Built: Bædling (the source is Gotland's). Default: keep. Open it to every landed band of the six faiths?
7. **The wrong.** Built: only a refusal after patience. Default: keep. Should other wrongs open the decision (an eviction by the same lord, or the county given to someone else)?
8. **The darker Companions.** Not built (§4). Default: leave it until TO-TEST §U6 is run. If wanted then, a proposed shape: AI leaders only, never a player leader; the leader's hostile scheme against a camp officer of the faith is exposed; the officers hand the band to her and the old leader leaves the camp alive and free, with nothing shown. Build it, or drop it?
9. **Dirham's road** (the old leader goes on pilgrimage and returns as a lord's envoy). Default: not built; the next band wave.
