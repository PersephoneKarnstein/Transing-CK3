# Adelphai, wave 17: Phrygia after Beatrike

Asked for by the user after observe run 28 (2026-10-30): keep Phrygia in the faith after Theia Beatrike. Built 2026-10-30, untested in game. Namespace `tm_dl7`.

## Why

Run 28 (867 start, to 1705) traced Phrygia's holders in the save:

- The government fix after run 27 held. Beatrike kept Phrygia as an ecclesiastical ruler from 867 until she died in 898.
- From 898 to 990 the county passed by Byzantine **appointment succession** from one woman of the faith to the next, eight times. The Mother House title (`d_tm_mother_house`) went with it. Every appointee was of Beatrike's rite.
- In 990 the emperor **revoked** Phrygia from Anthousa and appointed a man of his own faith. After that it never came back. The Mother House title carried on without land, so wave 14's intakes had no ruler to make them.

So appointment was not the problem: revocation was. Two levers follow from that.

## 1. The gold seal (`tm_dl7.0001`)

**Source.** In the tenth and eleventh centuries emperors gave monasteries to lay lords to hold (the *charistike*: `research/byz_thomas_hero_typika.md` §1.2, p. xxviii). The reformers' answer was "a constitutionally independent foundation with a powerful protector" (p. 446), and Lips gave its ephoreia to the emperor "in perpetuity" (p. 1266). Chrysobulls could be annulled: Basil II's Novel of 996 did so (`hist_tougher_eunuch_byzantine.md`). So in game the seal lasts about a reign, not for ever.

**Mechanics.**
- Who: a ruler of the faith holding Phrygia, under a throne of another faith, without the flag below. Checked from her yearly pulse: 40% a year, then a five-year cooldown. Not on the flavour budget.
- Options:
  - Send a gift (75 gold): 50% granted.
  - Ask through the empress's chamber, if wave 10's balance at that throne is +1 or more: 70%.
  - Ask in the House's name alone: 25%.
  - Ask nothing.
  - The emperor's opinion of her moves the odds by about 15–20 points either way, and a zealous emperor is likelier to refuse.
- Granted: vanilla's `titles_protected` character flag for 25 years. Vanilla's revoke interaction refuses while it stands; vanilla grants the same flag for 10 or 25 years in its coronation and hold-court events. The flag is the holder's, so each new appointee asks for her own seal.

## 2. The next appointment (`tm_dl7.0010`)

- Who: the holder of the Mother House title, of the faith, while Phrygia is held by someone of another faith under the same throne. 30% a year, then a ten-year cooldown.
- What: she spends silver (50 gold, a major investment) or writes letters (a medium investment) toward her own appointment to Phrygia, through vanilla's `change_appointment_investment`. It counts when the logothete next names a governor. Nothing is taken from the sitting one. She may also let Dorylaion go.
- Untested: whether the engine treats her as a valid candidate. TO-TEST AT3.

**Changed after run 29.** The lobbying never fired: from 1008 to 1034 Phrygia was back under the throne with governors of another faith, but each Mother held only the Mother House's title, with no land, and so had no yearly pulse of her own. The check now runs from the global yearly pulse and reaches the Mother through the title (`tm_dl7_yearly_global`), as does the lost/returned count.

The old fallback stays: when Phrygia is out of the faith, the Mother House holder keeps a pressed claim on it (`tm_on_actions.txt`).

## Run 29 (867 start, to 1465)

- Asked 12 times: 5 with a gift, 1 through the chamber, 4 in the House's name. Granted 6, refused 4.
- Beatrike died in 902. From then until 997, appointment again kept Phrygia in the faith, and no emperor revoked it.
- In 997 it was lost by **conquest**, then passed through revolts and a holy war before the throne appointed it again in 1008. Lost 2, returned 1.
- War is outside what a chrysobull or the next appointment can answer; the pressed claim remains for that.

## Files

- New, with a BOM: `events/tm_dl7_events.txt`, `common/on_action/tm_dl7_on_actions.txt`, `common/scripted_effects/tm_dl7_effects.txt`, `common/scripted_triggers/tm_dl7_triggers.txt`, `localization/english/tm_dl7_l_english.yml`.
- Shared: a census block ("Adelphai: Phrygia (wave 17)"), TO-TEST section AT, TODO, README.
- Validation: xTiger 23, the baseline.
