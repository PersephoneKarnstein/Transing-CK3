# The Worn Garland, wave 10: the Tai bath, the band and the merchants, the road to Kanchi

Roadmap item (README, "Larger"): "Worn Garland: the solitary Tai vow to Kāma; Hall's company of the Five Hundred and the Pepper Merchant's Vow". Built 2026-10-27 (user's choice after run 21, where the Garland ended with 61 members), untested in game (`docs/TO-TEST.md` AL). Namespace `tm_ml4`. It builds on stage 2 (`docs/stage2/worn-garland.md`: shares, gifts, temple streets) and wave 4 (`docs/wave4/garland.md`: the caravan contract).

Files (new, with a BOM): `common/scripted_triggers/tm_ml4_triggers.txt`, `common/scripted_effects/tm_ml4_effects.txt`, `common/on_action/tm_ml4_on_actions.txt`, `common/decisions/tm_ml4_decisions.txt`, `common/modifiers/tm_ml4_modifiers.txt`, `common/opinion_modifiers/tm_ml4_opinion_modifiers.txt`, `events/tm_ml4_events.txt`, `localization/english/tm_ml4_l_english.yml`. Changed: `common/scripted_effects/tm_ml3_effects.txt` (the caravan remembers its lord and pays the sworn bonus); `tools/census_report.py` (a new section).

## 1. The Tai bath (0001–0003; decision *Keep the Tai Bath*)

**Source.** Hardy 1983 (`research/ind_hardy_viraha_bhakti.md`, items 3 and 5): the Mārkaḻi and Tai baths are separate rites (p. 512). *Nācciyār Tirumoḻi* 1 runs through Tai and Māci, is addressed to Kāma, and is kept with *kōlam* on the street, a bath before sunrise and one meal a day (p. 418 and n. 18). In the Caṅkam bath girls ask for "rain and a husband" (p. 512). Hardy's arc runs from the girls together to the woman alone (pp. 425–426).

**What the player sees.** In Tai (the game's January or February), a grown daughter of the Garland who is not keeping the pāvai vow and has not kept the Tai bath in three years may begin it: a playable daughter by decision, a courtier through her host's yearly pulse (10 in 100 a year, flavour budget; she waits for Tai, checked monthly, as the pāvai seeker waits for Mārkaḻi).
- *The Tai Bath* (0002): keep it alone for the month (*Keeping the Tai Bath*: +1 piety a month, stress lost faster; +15 piety at Kanchipuram), or "Not this Tai" (−5 stress).
- *What She Asks of Kāma* (0003), a month later: rain for the country (+20 piety; the county where she is gets +5% development growth and +5 opinion for 5 years); a love of her own (*Asked Kāma*: +10 attraction opinion, less stress gain, 10 years; −20 stress); or nothing, "the bath was the asking" (−30 stress, +10 piety).

**Guardrails.** No gate effect: the gate stays the Mārkaḻi vow, and the dream stays in the gate (`tm_garland.0013`). One meal a day costs nothing in health or stress (rule 22). Stepping back is honoured (rule 23). The old ask for "a husband" is the narrator's report of the old songs; the daughter's own ask is love, rain or nothing, and no bridegroom appears (rule 26). Āṇṭāḷ is not named; "the old poems" keep the bath.

## 2. Those Who Always Accompany Us (0010–0012; decision *Swear with the Merchants*)

**Source.** Hall 1980, pp. 191–193 (`research/ind_hall_cola_trade.md` §4 and §11 proposal 5): after Vijayabāhu I drove out the Cōḷas, the Tooth Relic temple at Polonnaruwa was entrusted to the *vēḷaikkārar*, whose inscription names the merchants "who always accompany us" (p. 192); Nilakanta Sastri reads the bond as a "spiritual or constitutional relationship" (p. 207 n. 9), Hall as "almost a kinship type bond" (p. 193).

**What the player sees.**
- Each caravan the band completes (wave 4's contract) records the lord who hired it, for 20 years.
- *Those Who Always Accompany Us* (0010): the merchants of that lord's market town ask the band for an oath. Swear (the band and the lord +25 opinion, lasting while both live; his capital gets *Those Who Always Accompany Us*, +0.2 control a month and +5% development growth, 20 years; he is told in 0011), or "We are hired, not sworn" (+10 prestige). AI bands are offered it at 25 in 100 a year (once per 10 years); a player's band uses the decision.
- While sworn, every caravan done for that lord pays a further 25 gold and 25 prestige. The oath lapses when he dies or loses his land.
- *A Third Temple* (0012): from 1070, a band of the Garland in a Lanka county held by a Buddhist ruler, 20 in 100 a year (flavour budget, once per 30 years): the king offers the band the gate of a relic temple, with the port's merchants as witnesses. Guard it (*Guards of the Third Temple*, +0.5 prestige and +0.5 gold a month for 10 years; the king +20 opinion; +50 prestige if the band is sworn with merchants), or "The road is the band's temple" (+10 prestige).

**Guardrails.** The bond binds soldiers to merchants, not kin. The narrator does not claim the *vēḷaikkārar*, the Five Hundred or the Kaikkōḷa regiment for the faith (Hall §9: modern claimants among merchant castes and the Sengunthar). The Polonnaruwa phrase is used as the merchants' words at any date (design); the relic temple is gated to 1070. "The street served two temples; the band can guard a third" is the faith's "both temples" stance, from Hall's proposal.

## 3. A Hall in the Name of the Guild (0020)

**Source.** A temple *maṇḍapa* at Tiruviḍaimarudūr was named for the Five Hundred, and the Kaikkōḷa regiment, "the armed mercenaries of the itinerant merchants", paid for part of it (Hall pp. 144, 154, 192; 253 of 1907). Tiruviḍaimarudūr also sent temple women to Thanjavur (p. 84); no source joins the regiment and the women, so the link is design.

**What the player sees.** A band of the Garland with 150 gold, whose sworn or last-hired lord is Hindu and has a capital, 15 in 100 a year (+15 if sworn; flavour budget): raise a pillared hall before the temple in the guild's name (150 gold, +100 prestige, the lord +20 opinion; his capital becomes a temple street; every daughter holding a share there +10 opinion of the captain), or keep the gold. Once per 20 years.

## 4. The Pepper Merchant's Vow (0030–0031; decision *Pay the Pepper Vow*)

**Source.** Hall p. 151 and p. 160 n. 54: a local tradition at Viriñcipuram, recorded in a 13th-century inscription, of the pepper merchant Dhanapālaṉ's vow against robbers on the road to Kanchi. The green gram is the story's. It is a tradition, not a dated event, and the text puts it in the merchants' mouths ("a story they say is cut in the temple there").

**What the player sees.** From 1200, a ruler of any faith setting out for Kanchipuram, 20 in 100 (once per 10 years): *The Road to Kanchi* (0030). Vow ten bags of pepper (−10 stress), or trust the guards (+5 prestige). On arrival with a vow (0031): pay it (30 gold; +30 piety, +10 prestige) or "Safe is safe" (*Green Gram in the Bags*: −0.5 prestige a month and −10% income for 5 years, until the decision *Pay the Pepper Vow*, 30 gold and +20 piety, clears it).

## 5. Counting

`tm_ml4_tally_effect` keeps run-wide globals, printed by `tools/census_report.py` under "Worn Garland: wave 10": `tai_kept`, `tai_not_now`, `tai_rain`, `tai_love`, `tai_nothing`, `sworn`, `oath_refused`, `sworn_caravans`, `relic_guard`, `halls`, `pepper_vowed`, `pepper_paid`, `pepper_forgot`, `pepper_paid_late`.

## 6. Not built

- A Company of the Thousand Directions (Hall §11 proposal 7): waits for merchant companies (*Silk & Silver*).
- The band defending the sworn lord's county when it is raided (Hall proposal 5): no clean hook; the county modifier stands in.

## Uncertain syntax (check in game)

- `current_travel_plan.final_destination_province` in `on_travel_plan_start` (vanilla reads it in `on_travel_plan_complete`); and whether vanilla's `is_ruler = yes` trigger on these on_actions also gates appended on_actions (assumed; the vow is for rulers, adventurers included).
- `var:tm_ml4_sworn_to = scope:employer` inside the contract's completion chain.
- `location ?= { geographical_region = custom_lanka }` on a band leader's location.
