# Ha-Nehpakhot, wave 6: the bailiff's variants and the households of the street

Roadmap item (README, "Larger"): "Ha-Nehpakhot: the bailiff's variants (Catalonia's *batlle*, the panic after a patron's fall); invite a household of the street". Built 2026-10-25, untested in game (`docs/TO-TEST.md` AG). The ideas were already in the stage-2 notes (`docs/stage2/ha-nehpakhot.md`, feature 3 open questions 2–3, and "Survival balance", item 3), sourced to Assis 2001 (`research/jud_assis_catalonia_sexuality.md`) and Stouff. Run 16 (to 1175) left the sect with one living member, so the household is also a survival lever.

Files: `common/scripted_triggers/tm_hn4_triggers.txt`, `common/scripted_effects/tm_hn4_effects.txt`, `common/decisions/tm_hn4_decisions.txt`, `common/on_action/tm_hn4_on_actions.txt`, `common/opinion_modifiers/tm_hn4_opinion_modifiers.txt`, `events/tm_hn4_events.txt`, `localization/english/tm_hn4_l_english.yml`. Edited: `common/customizable_localization/tm_custom_loc.txt`, `localization/english/tm_hn2_l_english.yml` (the bailiff's lines), `events/tm_hipukh_events.txt` (two modifiers), `common/on_action/tm_on_actions.txt` and `common/scripted_effects/tm_surv_effects.txt` (a tally), `tools/census_report.py`.

## 1. The batlle

**What the player sees.** In the Crown of Aragon (a county de jure in `k_aragon`, which holds Barcelona, or in `k_valencia`), *Before the Bailiff* (`tm_hn2.0020`) becomes *Before the Batlle*: the rival carries the complaint to "the batlle of" the lord. The options and outcomes are unchanged.

**Source.** Assis 2001, p. 44: Vives, son of Jucef Abenvives, *batlle* of Alfandech and Marines, accused in 1274; the Crown's cases are heard by the king's officers. The event already starts in 1260, from Assis's first case (Lleida, 1263).

**How.** Scripted loc `tm_hn4_bailiff` (with `_cap`, `_title`), keyed on `tm_hn4_in_aragon_trigger`.

## 2. The berurim

**What the player sees.** In the Crown of Aragon from 1270, the street's judges in the hearing (`tm_hipukh.0003`) are "the berurim of the street" instead of Arles's worthies, rectors or baylons. Before 1270 they stay "the worthies". Arles and Provence are unchanged.

**Source.** Assis 2001, pp. 38–39: the Lleida *berurim* (elected judges) "menaven una campanya de reformes morals i religioses" (Adret, responsa I:1187); the Alzira *berurim* in the late 14th century. 1270 is a round date inside Adret's working life (he answered from the 1260s to 1310). This also corrects a small error: the rectors (1215) and baylons (1386) are Arles's own offices and should not have shown in Catalan towns.

**How.** A first `text` in each of `tm_kahal_judges`, `_cap` and `_title`, after the Maghreb's elders.

## 3. After the fall (`tm_hn4.0001`)

**What the player sees.** When a lord who took a daughter of the Turning's translations into his house dies within the ten years of his patronage (`tm_translation_patron_modifier`, from `tm_hipukh.0030`), each daughter of the Turning at his court or in his realm hears it (within 3–30 days, once per flavour budget):

> [The patron] is dead, who took my work into his house, and the street has lost its friend at court. Fear has come in where he stood. In the synagogue the preachers say that God's anger has fallen on the street for its sins […] They do not name me. They do not need to: when I pass, the talk stops.

Her county is afraid for a year (`tm_hn4_after_fall`): the hearing's two learned answers are 15 harder to win, and a Turning prayer there is 10 less likely. She can:
- **a. Keep my name indoors until the fear passes.** +10 stress; for a year the fear does not weigh on her (`tm_hn4_sheltered`).
- **b. Answer them: God's anger is not on my name.** 40 + 2×learning against 50. Win: the county's fear ends, +30 prestige. Lose: +15 stress, −20 prestige.
- **c. Go to the women of the street** (if there are Jewish women at her court: `tm_kahal_door_trigger`). −10 stress; sheltered for the year.

**Source.** Assis 2001, pp. 27–28: the Toledo ordinance of 1281 against sexual immorality followed the fall of the Jewish courtiers in 1279–80, and the preachers read the fall as God's anger at the community's morals. Assis's own design note proposes exactly this event (`research/jud_assis_catalonia_sexuality.md` §4).

**Rules respected.**
- The preachers are afraid, not cruel. No one is punished, shunned or named; the cost is a harder year. The narrator does not call the preachers wrong or right.
- No Christian voice, and nothing about Jews as a people. The patron may be of any faith.
- The street's fear is never "contagion" (rule 10). No golden past (rule 2): the fear is this year's.
- Only death counts as a fall. Imprisonment or the loss of a title would also fit Toledo, but they are not modelled yet.

## 4. Send for a household of the street (decision)

**What the player sees.** A ruler of the sect (landed, or the leader of a landless camp) may pay 50 gold, once in ten years, for a Jewish household to settle at her court: a man, his wife and their child. They come as Rabbanite Jews, not members; with +20 opinion of her for twenty years. At her court the kahal's yearly 4% (Rabbanite Jews at a court where the sect is two or more) may later take them in, and its matches marry Rabbanite Jews of her court first.

**Where they come from.** From Barcelona (culture `sephardi`); for a ruler whose capital is in the Crown of Aragon, from the street at Arles (`occitan`); for a ruler in the Maghreb or the Sahel, a household of her own land's culture, as the refugees of wave 3 are.

**Source.** Stouff, "Les juifs d'Arles" §16: a contract of 1422 at Arles paid a man to bring his wife and child from Barcelona. It is service and settlement, paid travel, not the purchase of protection (the sect's protection is always earned by service).

**AI.** Base 25 every 120 days; never with fewer than 100 gold, nor when three Rabbanite Jews are already at court.

## 5. Counting

`tm_hn4_tally_effect` keeps run-wide globals: `households` (decisions taken), `household_joins` (members of those households the kahal took in, by either path) and `falls` (patrons who died). `tools/census_report.py` prints them under "Ha-Nehpakhot: households and falls".

## 6. Open questions

1. Should imprisonment or the loss of his title also count as the patron's fall?
2. Is 50 gold right? The decision is cheap so that a landless camp can afford it.
3. A Jewish bailiff before 1260 (Abba Mari at Saint-Gilles, c. 1165) is still not built: the Jewish officer would be the one who fines her.

## 7. The lamp relit (added 2026-10-28, untested in game)

**Why.** Ha-Nehpakhot died out in observe run 25 (0 members from the 1410s). In runs 24 and 25 it held 6–25 members for most of six centuries with no ruler of the sect, so the household decision (which needs a ruler) and the kahal's draw (which needs a landed one) never fired. In run 23 it reached 294. The swing is too wide for a small faith that should grow slowly but last.

**What.** `tm_hn4_relight_effect` (`tm_hn4_effects.txt`), fired by the hidden event `tm_hn4.0010` on the lord of the Venaissin from `tm_yearly_growth` (`tm_on_actions.txt`).
- **When:** from 880, while the sect has fewer than 40 living members and either no house of it stands (no ruler of the sect, a camp counting, and no court where three of it live) or it is down to fewer than 12. 4% a year, then not again for 40 years.
- **Who comes:** an elder daughter of the Turning (45–60, learning), a physician of the sect with his wife and two children, and a Marked young man to be taken in. Six people, of the Venaissin's culture.
- **Where:** with Roads to Power the elder keeps a scholars' camp at the Venaissin, as Bonadonna does from 867, and the others are of her camp. Without it, all six join the court of the Venaissin's lord, as at a later start's seed.
- **Why the Venaissin:** the seed's street, and a papal land from 1274 that kept its Jews when France (1306) and Provence (1501) expelled theirs.
- **Player:** if the Venaissin's lord is a player, a toast, "Lamps in the Street Again".
- **Census:** `relit` in "Ha-Nehpakhot: households and falls".

Not a cap: it adds six people at most once in 40 years, only when the sect has no house, and the sect must keep them by its own means.

**Decisions (user, 2026-10-28).** 4% a year with a 40-year pause, for now (about once in 65 years in a run like 25). The condition looks at numbers too: never at 40 or more, always eligible under 12. Without Roads to Power the six go to the lord's court, accepting the AI's conversion asks.
