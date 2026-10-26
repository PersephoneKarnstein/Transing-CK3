# Adelphai Dorleyaiou, wave 8: the Tower on the Condition

Roadmap item (README, "Larger"): the Tower on the Condition. Built 2026-10-25, untested in game (`docs/TO-TEST.md` AJ). Design: `research/byz_sophoulis_banditry.md` row 6. In runs 16 and 17 the Adelphai held no county for most of the run, and the faith shrank to 13–18 members: the faith seldom has a ruler, so a mechanic that needs one does not fire. The tower is asked for by a sister who is not a ruler, and granted by a Christian lord of another faith.

Files (new, BOM): `common/scripted_triggers/tm_dl5_triggers.txt`, `common/scripted_effects/tm_dl5_effects.txt`, `common/on_action/tm_dl5_on_actions.txt`, `common/modifiers/tm_dl5_modifiers.txt`, `common/opinion_modifiers/tm_dl5_opinion_modifiers.txt`, `events/tm_dl5_events.txt`, `localization/english/tm_dl5_l_english.yml`. Edited: `events/tm_house_events.txt` (0050: a desc line and AI weights for a kept tower), `localization/english/tm_dl5_l_english.yml` holds the new 0050 line, `tools/census_report.py`, `README.md`.

## Sources

Sophoulis, *Banditry in the Medieval Balkans*, p. 111: in 1313 Alypiou received state land on Athos "on the condition" that it restore a pirate-wrecked tower; c. 1418 the Despot Andronikos Palaiologos paid for a tower for those who would settle at Mariskin, a deserted village Dionysiou had acquired; Iviron's tower at Komitissa was manned by peasant watchmen (1323–34). Towers were built or rebuilt by monks on imperial request (pp. 105–12). Gregory of Sinai's robbers at Paroria "became humble shepherds" (Life by Kallistos, p. 61).

## 1. The petition (`tm_dl5_yearly_petition`, `tm_dl5.0001`)

- **Who asks.** An adult sister of the Adelphai who belongs to a House (`tm_house_member_trigger`), is not a ruler, and is not keeping quiet. Weighted by diplomacy, +5 for a daughter, +5 if the lord thinks well of her.
- **Whom.** Her court owner: a Christian lord of count tier or above, not of the six faiths, whose capital is in Asia Minor or south-east Europe, who holds no House yet and has a county without one. Asked once per lord; on the flavour budget.
- **How often.** 10 in 100 a year when anyone qualifies, and not again for fifteen years after a petition.
- **Which county.** The least developed county he holds directly, not his seat if he has another.
- **Grant** (AI base 40; opinion of her ×0.5; compassionate +30, content +20, at war +20, generous +15; zealous −40, paranoid −20): a Sisters' House is founded there, tolerated by him (`tm_house_tolerated_by`); the county gets "A Tower Being Rebuilt"; she becomes Keeper of the Tower, pays 50 gold if she has it, and has +25 opinion of him for twenty years; he gains minor piety.
- **Refuse** (AI base 40; zealous +30, greedy +20, paranoid +15): nothing else.

## 2. The condition (`tm_dl5_yearly_towers`)

Each year, while the House stands: if two grown sisters of a House are at the holder's court, the year counts. Five such years keep the tower (`tm_dl5.0010`): the county gets "The Sisters' Tower" (garrison +20%, hostile raids slower, development +5%), the keeper gains piety, the holder minor prestige. Two empty years in a row call the holder (`tm_dl5.0011`): take it back (the House closes; the keeper −15 opinion of him) or give them one more year. A House closed any other way clears the tower.

The petitioner herself counts toward the two. A lord who holds a House is the faith's second choice of home in the yearly gathering (`tm_surv_find_home_effect`), so a granted tower draws wandering sisters to his court: that is how it was meant to be manned. Run 18 (to 1314) showed it is not enough: 7 towers granted, none kept, all 7 taken back, because the sisters are few and the gathering takes only those with no court. Since then the House calls them in (`tm_dl5_gather_effect`): at the grant, up to two grown members who are not rulers, rulers' wives or councillors, and are not at a court of the faith, move to the lord's court, nearest first; while the tower is short of hands, one more comes at 25% a year. The census counts them as `came`.

## 3. After

- A later holder of another faith still gets *A House in My County* (`tm_house.0050`). With a kept tower its text adds that the House holds the tower by a grant, and the AI leans +40 to letting it stand, −30 to closing it.
- **The tower's herders** (`tm_dl5.0020`): 3 in 100 a year for a kept tower's holder, once in thirty years per county. Men who robbed the road come to the House, and the Sisters set them to the flocks. "The Sisters do not say the men have repented." Keep them (development and levies +5% for twenty years) or send them on (minor prestige). No ethnic label; no conversion claim.

## 4. Counting

`tm_dl5_tally_effect`: `petitions`, `granted`, `refused`, `kept`, `extended`, `revoked`, `shepherds`. The census prints them under "Adelphai: the Tower on the Condition".

## 5. Rules respected

- The lord is neither hero nor villain: his reasons are a watched road and a cost-free tower. The narrator does not praise or blame his answer.
- No violence on screen. The robbers are not named by people or region.
- The tower is held by a grant and can be taken back: shelter granted by a lord can be withdrawn (Raha & van der Drift, as for every House).

## 6. Open questions

1. **No date gate.** The grants in the source are 14th–15th century; observe runs from 867 end near 1150–1175, so a 1300 gate would mean the tower never fires in them. The narration cites no dated case ("Monks have taken towers on such terms before"). Gate it at 1300 if that reads as an anachronism.
2. Only Christian lords in the Byzantine world grant it. Should Georgia and Armenia count?
3. Should the Mother of Mothers, if she is landed, be able to ask a neighbouring Christian lord too?
