# Wave 4: landless bands of the six faiths

Prefix `tm_band_`, namespace `tm_band`. Builds on wave 3's landless-band work (`docs/wave3/baedling.md` §3, `tm_bae2_*`). Untested in-game. Validated with xTiger: no reports in these files.

Not built, by the user's decision: "Ghazis Have No Wealth" (Tor pp. 214–215).

## Files

All new. No `tm_bae2_*` file needed changing.
- `common/on_action/tm_band_on_actions.txt`: yearly pulses, and the war-won hooks.
- `common/scripted_triggers/tm_band_triggers.txt`
- `common/scripted_effects/tm_band_effects.txt`
- `common/script_values/tm_band_values.txt`
- `common/opinion_modifiers/tm_band_opinion_modifiers.txt`
- `common/modifiers/tm_band_modifiers.txt`
- `events/tm_band_events.txt`
- `localization/english/tm_band_l_english.yml`

How it fits wave 3: a "band" is still `tm_bae2_faith_band_trigger` (a landless adventurer of the six faiths). The yearly `tm_bae2_yearly_bands` pulse still marks it `tm_bae2_was_band`. When the Patent and the Robe lands a band, `tm_bae2_title_gain` gives it the settling grace (`tm_bae2_settling_modifier`, and `tm_bae2_hall_returned_county_modifier` if the county keeps the faith). Nothing in wave 4 adds a second grace. `tm_band_grant_patent_effect` sets `tm_bae2_was_band` itself, in case the band formed after the last yearly pulse.

## 1. The Patent and the Robe, and the Rallied Township (built)

### Sources

- **Tor, *Violent Order*** (`research/isl_tor_violent_order.md` §4, §12 proposal 2).
  - In 253/867 Yaʿqūb took Herat and left it when asked. The Ṭāhirids then sent him a patent for four provinces and a robe of honour, and he "was patient and returned" (p. 122).
  - The notables of Fars wanted a caliph's letter (p. 129).
  - The sword as his diploma (p. 150).
  - Amnesty and a place in the army for those who joined (p. 113).
- **Vaissière, *Sogdian Traders*** (`research/cn_vaissiere_sogdian_traders.md` §2, §11 proposal 2).
  - After the *sabao* system ended, Sogdians lived in "rallied" townships as ordinary subjects with the same corvée as everyone else (pp. 152–153).
  - Conghua at Dunhuang (pp. 129–130).
  - Assimilation within a generation (pp. 153–155).
- **Sophoulis, *Banditry in the Medieval Balkans*** (`research/byz_sophoulis_banditry.md` §5, §11 proposal 1).
  - Dobromir Chrysos, 1196–c. 1205: recognised in the lands he held, and later reduced to Prosek (pp. 81–82).
  - Momčilo, 1343–45: given command of the "fortresses, villages and inhabitants" of Merope; forgiven; independent; killed (pp. 78–81).

### What it does

**Why a lord notices a band.** A band at peace has a reason to be noticed in three cases. The hidden search `tm_band.0002` runs from the yearly pulse `tm_band_yearly_patent` and checks them in this order:
1. **Patience** (`var:tm_band_patient_with`, 20 years): the band once moved on when this lord asked. This is the Herat case.
2. **Service** (`var:tm_band_served`, 10 years): the band fought in a war on this lord's side, not as the primary participant, and his side won. It is set by `on_war_won_attacker` / `on_war_won_defender`, so a band hired through `laamp_join_war_contract` qualifies. This is the "band that cleared a county".
3. **A long camp** (`tm_band_camped_long_trigger`): five or more years camped in one county. The years are counted yearly in `tm_band_camp_county` / `tm_band_camp_years`, and moving resets the count. The lord is the county's holder, or the lowest liege above him who has a county to give.

**Who can offer.** The lord must pass `tm_band_patron_trigger`, the same limits as vanilla Negotiate Settlement:
- landed, with two or more counties of his own;
- not a camp, a nomad or an administrative realm;
- not defending in a war.

**Which county.** The offered county is his nearest grantable county (`tm_band_grantable_county_trigger`): not his capital or primary title, not a faith head's title.

**Which bands can be offered land.** `tm_band_may_be_offered_trigger` excludes:
- bands at war;
- the lord's nemesis;
- bands exiled from his lands (vanilla `is_laamp_exiled_from_province_trigger`);
- legitimist camps (vanilla gives them −300 to accept).

**Odds.** Each year the chance is 10% for a long camp, 15% after patience and 25% after service. After an offer the band waits 10 years before another.

**A player lord.** The offer counts against the flavour budget. A player lord can also use vanilla Negotiate Settlement himself at any time.

### Events

**`tm_band.0001`, the lord** ("A Band on My Land"). The description has two parts: the reason, then how his land settles bands (`tm_band_style_effect`):

| Style | Where | Text |
|---|---|---|
| `township` | the county is in `world_asia_china` or `world_steppe_tarim`, or the lord has Chinese heritage | the rallied township: the band's people entered on the register as ordinary subjects, with the same corvée (Vaissière pp. 129–130, 152–155) |
| `strumica` | the county is in `world_europe_south_east` or `world_asia_minor`, or the lord has Byzantine or South Slavic heritage, **before 1300** | a treaty for land the captain already held, when a band "costs more to fight than to keep" (Sophoulis pp. 81–82) |
| `merope` | the same lands, **from 1300** | a command of a district's forts, villages and people, called an alliance; "it has not always ended well" (Sophoulis pp. 78–81) |
| `robe` | the county is in `world_persian_empire` or `world_middle_east`, or the lord is Muslim | the patent and the robe of honour (Tor p. 122) |
| `charter` | anywhere else | a county by charter |

The lord's options:
- **(a) Give the county.** The option reads "Send her the patent… and a robe of honour" (robe), "Offer to register her people…" (township), or "Offer her…" (others).
  - AI weights: base 15, plus half his opinion of her. Generous +30, craven +20, over his domain limit +20, after service +20, after patience +40, same faith +15, band stronger than him +25 (the Strumica logic). Greedy ×0.5; zealous of another faith ×0.5.
- **(b) Ask her to move on.** Shown only if her camp is in his realm.
  - AI weights: base 10. Zealous of another faith +20, paranoid +15, opinion below 0 +15. ×0.5 after service; 0 after patience.
- **(c) Let them be.** AI base 40, content +20.

**`tm_band.0010`, the band** ("The Patent and the Robe", "The Rallied Township" or "An Offer of Land"). The description varies by style. In the township text the band hears what it gives up: "From an administration of our own to the magistrate's".
- **(a) Take it.** This fires `tm_band.0012` on the lord. 0012 checks that he still holds the county, then runs `tm_band_grant_patent_effect`:
  - It saves vanilla's scopes (`actor`, `recipient`, `new_primary_title`) and the list `offered_titles` exactly as `negotiate_settlement_interaction`'s `on_accept` does.
  - It then fires **vanilla `ep3_laamps.0300`** on the lord. That event runs `negotiate_settlement_interaction_effect` (vassalage, camp liquidated, ennobled-adventurer malus, legitimacy cost, white peace) and sends the band vanilla's letter `0301`.
  - The band gets `tm_band_patent_given_opinion` (+25), and the wave-3 grace follows.
  - AI weights: base 60. Ambitious +30, lust for land +40, age 50+ +20, in debt +20. Wanderers camp ×0.5.
- **(b) Keep the road.** The lord gets a toast.
  - AI weights: base 20. Wanderers +30, arrogant +20.

**`tm_band.0020`, asked to move on.**
- **(a) "We go. Patience costs us nothing."** (*She Was Patient*):
  - `tm_band_move_on_effect` moves the camp to the nearest county of a neighbouring realm, as vanilla's eviction does (`ep3_interactions_events.0502`), with provisions topped up.
  - Medium prestige.
  - An **unpressed claim** on the county (the stored claim).
  - The lord gets `tm_band_left_when_asked_opinion` (+25, 15 years).
  - `tm_band_patient_with` is set for 20 years, which later gives the best odds and +40 to the lord's AI.
  - AI weights: base 50. Patient +20, content +20, lord stronger +30, wrathful −20, arrogant −20.
- **(b) "We stay."**
  - Both sides lose opinion: she gets `tm_band_asked_to_leave_opinion` (−10) and he gets `tm_band_refused_to_leave_opinion` (−25).
  - An AI lord then runs **vanilla `evict_adventurer_interaction`** if it is valid. Its refusal opens vanilla's apprehend-adventurer war.
  - A player lord can evict through the vanilla interaction.
  - AI weights: base 20. Band stronger +30, stubborn +20, arrogant +20.

### Decisions

- **Vanilla's interaction is reused, not overridden.**
  - `run_interaction` cannot pick a target title, so it cannot start Negotiate Settlement from script. The docs list no `target_title` field.
  - Overriding the vanilla interaction would mean copying 1,170 lines of a file the mod does not own.
  - Instead, the mod's own events lead into vanilla's acceptance event `ep3_laamps.0300` with vanilla's own scopes and list. The vanilla interaction itself is unchanged.
  - In vanilla, AI lords rarely offer settlement to a small band: `ai_frequency_by_tier` is 0 for counts, and AI-to-AI county deals need a greedy or land-hungry adventurer. That is why the mod adds its own search.
- **"Holds a county"**, meaning a band occupying a county in a war against the lord, is left to vanilla. Its `ai_will_do` already weighs heavily for settling with an adventurer who is winning ("Defending against a LAAMP", "Potential war target").
- **No "Sword Is My Patent" decision** (Tor proposal 2's last step). The stored claim already lets a wronged band press it with vanilla CBs.
- **No narrator claims.** No historical figure is named in event text. Herat appears as "a band that took a city and gave it back", told by old soldiers. No culture is named as bandits (Sophoulis risks).

## 2. The Companions Choose (built)

Source: Tor pp. 109–111 (`research/isl_tor_violent_order.md` §4 item 3, §12 proposal 1). Seeing Dirham's weakness, his companions "transferred the rule over them" to Yaʿqūb for his skill and his care for their affairs. Dirham did not contend, and stayed in the band.

### What it does

The pulse `tm_band_yearly_companions` looks for a band at peace whose leader is weak or failing (`tm_band_weak_leader_trigger`). That means one of:
- she is incapable;
- `tm_band_leadership_value` (martial + stewardship + diplomacy) is 15 or less;
- she is more than 50 gold in debt.

Age alone is not a failing.

There must also be a **companion** (`tm_band_companion_trigger`):
- one of her **camp officers** (`any_court_position_employer`);
- of the six faiths, adult, free, able and not her rival;
- with a leadership value of 30 or more, and at least 10 more than hers.

**Odds:** 5% a year for an AI leader, 10% for a player leader, within the flavour budget. A 10-year cooldown follows, for her and for the new leader.

**Choosing the companion:** `tm_band.0102`, hidden, picks the officer with the highest leadership value.

**`tm_band.0100`, "The Companions Choose"**, goes to the leader. The opening line varies: incapable, in debt, or weak.
- **(a) "Then she leads. I ride with her."** runs `tm_band_hand_over_effect`.
  - The old leader gets `tm_band_stepped_down_modifier` for 10 years (+0.5 prestige a month, −15% stress gain).
  - Old and new leader take `tm_band_stepped_down_opinion` (+20) of each other.
  - The new leader gains minor prestige.
  - A **player** leader is moved to the new leader with `set_player_character`, as vanilla's `laamp_switch_playable_character_effect` does. The option tooltip says so.
  - AI weights: base 70. Humble +30, content +20, incapable +30. Ambitious ×0.5, arrogant ×0.5, stubborn ×0.7.
- **(b) "Not yet."** The companion gets `tm_band_kept_the_band_opinion` (−10).
  - AI weights: base 30, and 0 if she is incapable.

**Consent.** The event only fires on the leader. A player leader always chooses. A player can never be the companion, because the trigger requires `is_ruler = no`.

### How the band changes hands (the engine question)

Vanilla 1.20 has no script effect for a living adventurer to hand over her camp. What it has:
- **Succession.** The camp title is a landless duchy (`create_adventurer_title`). It passes on death by `landless_adventurer_succession_law`: children, courtiers only, "prowess succession … determined in code".
- **Designated heirs.** `set_designated_heir` takes only a direct child. `set_designated_heir_unsafe` takes anyone, but `depose` would then pass every title to the heir with no way to check the camp follows.
- **Moving a landless title.** The engine's own debug interaction (`00_test_interactions.txt`, `scope:landless_title`) moves landless titles with `change_title_holder`.

**What was built.** `tm_band_hand_over_effect` moves the camp title (`primary_title`):
- as a `create_title_and_vassal_change` of type `stepped_down`, with `government_base` = the old leader;
- then any courtiers still at her court move to the new leader's;
- the old leader joins the new leader's court if the engine has not put her there;
- the camp's gold moves with `pay_short_term_gold`;
- the band's memory moves too: camp years, service, patience and `tm_bae2_was_band`.

**Untested, and the main risk:** whether the camp **domicile** (its buildings and provisions) and the camp's **men-at-arms** follow the title. The `create_domicile_title` docs suggest the domicile belongs to the title, but this needs a test (TO-TEST B6).

If they do not follow, the fallback is the engine's own succession:
- `set_designated_heir_unsafe = companion`, then `depose = yes` on the old leader;
- only when `is_valid_designated_heir` says the companion can inherit, which for a non-relative under the laamp law is probably never.

So the only safe fallback would be to limit the event to a companion who is the leader's child or heir.

### Not built

- **The darker branch** ("The Plot Discovered": the companion strikes first).
- **Dirham's other road:** the old leader leaves on pilgrimage and returns years later as a lord's envoy.

## Uncertain syntax and behaviour

- **Lists across `trigger_event`.** `offered_titles` is built in `tm_band_grant_patent_effect` and read in vanilla `ep3_laamps.0300`. Vanilla does exactly this from the interaction's `on_accept`.
- **`root.war` in `on_war_won_attacker` / `on_war_won_defender`.** Vanilla's own handlers use `root.war`. The mod uses `?=` in case it is absent.
- **`change_title_holder` on a camp title** with `type = stepped_down` and `government_base` (see above).
- **`set_player_character` after the hand-over**, in the old leader's own event option.
- **`random = { chance = … modifier = { … } }`** in the pulses.
- **`ep3_laamps.0300` also fires for AI lords.** It is a visible event, so AI lords see it, which is harmless. Player lords get vanilla's confirmation.

## Test scenarios (TO-TEST style)

**Patent and Robe**
- **B1.** Make a Bædling adventurer (player) and camp for 5 years in a county of an AI count who holds two or more counties. Console `effect = { set_variable = { name = tm_band_camp_years value = 5 } }` speeds this up.
  - Within a few years, expect either "An Offer of Land" (Western lord: charter text) or "Asked to Move On".
  - Accepting makes you his vassal in the offered county (vanilla letter 0301), with "Settling the Hall" (wave 3).
- **B2.** The same in Anatolia under a Byzantine count: the text is the treaty (before 1300) or the district command (1300 and later). In Iran under a Muslim lord: "The Patent and the Robe", with the robe option. Near Dunhuang under a Chinese lord: "The Rallied Township", "Enter us on the register".
- **B3.** Hire your band to an AI ruler through a war contract and win. The next years should bring that ruler's offer (25%/yr). `tm_band_served` should be on you after the war.
- **B4.** As the AI lord asks you to move on, choose "We go": your camp travels to a neighbouring realm, and you gain prestige, an unpressed claim on the county and his +25 opinion. Some years later the same lord should offer you land ("Some years ago I asked…").
- **B5.** Choose "We stay" against an AI lord: vanilla's eviction letter follows; refusing that gives him vanilla's apprehend war.
- **B5b.** As a player count with two or more counties, with a faith band camped five years in your county: "A Band on My Land", subject to the flavour budget.

**Companions Choose**
- **B6.** Play a faith band whose leader has low skills (console `add_martial_skill = -10` etc.) and a camp officer of the faith with leadership 30+. Within a few years, "The Companions Choose".
  - "Then she leads": you play on as her.
  - Check the **camp (domicile, buildings, provisions), men-at-arms, gold and courtiers** moved with the title.
  - Check the old leader is in the camp with "Stepped Down with Honour".
  - If the domicile did not move, report it: the effect must change (see "The engine question").
- **B7.** "Not yet": nothing changes; the companion has −10 opinion; no new event for 10 years.
- **B8.** Observe run: AI bands rarely change leaders (about 1 in 20 weak-led bands a year). No player is ever replaced without the event.

## Ready-to-paste README text

For Shared mechanics, after "Bands come home":

> - **The patent and the robe.** A lord may offer a band of the six faiths a county of his own as his vassal: after it fought on his side and won, after it camped five years on his land, or years after it moved on when he asked. The offer is worded as the land knows it: a patent and a robe of honour in the Islamic east, a place on the register of a "rallied township" in China, a treaty or a district command in the Balkans and Anatolia, a charter elsewhere. A band asked to move on may go with patience, keeping a claim and the lord's goodwill, or stay and face eviction.
> - **The companions choose.** When a band's leader fails, her officers may hand the band to a stronger companion. She steps down with honour and rides on in the band. A player leader always decides.

Roadmap: add "landless bands: settlement by recognition, change of leader" as done (untested).

## Ready-to-paste TODO text

```
## Landless bands, wave 4 (added 2026-10-21, untested in-game; docs/wave4/bands.md)
- [ ] The Patent and the Robe (`tm_band.0001`–`0020`): offers after service / patience / five years' camp; regional text (robe, township, Strumica, Merope, charter); settlement through vanilla ep3_laamps.0300; move on with patience (claim + goodwill) or stay (vanilla evict)
- [ ] The Companions Choose (`tm_band.0100`–`0102`): officers hand a weak band to a stronger companion; player consent; TEST that the camp domicile and MaA follow `change_title_holder` (B6)
- [ ] Not built: The Sword Is My Patent; the darker Companions branch; Dirham's pilgrimage-and-envoy road; Ghazis Have No Wealth (declined)
```
