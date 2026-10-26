# Badenya, wave 9: the Rock at Koulikoro and the fall of the associate

Roadmap item (README, "Larger"): "Badenya: the refuge at Koulikoro; the fall of the associate in rule". Built 2026-10-26 (user's choice for the run after run 19, where Badenya fell from 147 to 18 members), untested in game (`docs/TO-TEST.md` AK). Namespace `tm_bd3`.

Files: `common/scripted_triggers/tm_bd3_triggers.txt`, `common/scripted_effects/tm_bd3_effects.txt`, `common/on_action/tm_bd3_on_actions.txt`, `common/modifiers/tm_bd3_modifiers.txt`, `common/opinion_modifiers/tm_bd3_opinion_modifiers.txt`, `events/tm_bd3_events.txt`, `localization/english/tm_bd3_l_english.yml`; `tools/census_report.py` (a new section).

## 1. The Rock at Koulikoro (a refuge; survival)

**Source.** Bulman et al. 2023, ch. 2, p. 63 (`research/waf_bulman_corpus.md` §5 and "Koulikoro"): from 1819 to about 1930 runaways "of either sex", fleeing "a master or … a spouse", could not be taken from the hill of Koulikoro, and fields were set apart for them to farm. Jansen 2018, p. 15 (`research/waf_jansen_kangaba_griots.md`): the rock where Sumaoro turned to stone is a place of amnesty to which Sunjata's descendants are denied access. In CK3 the hill is `b_koulikoro` in `c_sibi_mali`, the faith's Kirina seat.

**Status of the evidence.** LATER (19th century). The faith speaks of the refuge as old, in its own voice; the narrator says it is recorded from the nineteenth century. Following Bulman's note and the Badenya guardrails, the mod uses **the asylum only**: no shrine, no smith-priest, no flute rite, and nothing that reads as an Underground Railroad (guardrail 11: no fugitive, maroon or plantation imagery). The words are "came to the rock", "a lord or a husband", "fields set apart"; never "fugitive", "master", "freedom" or "escape north".

**What the player sees.**
- **Who comes.** Each year, a grown member of Badenya, a daughter of any faith, or a Marked or declared sister, who is not a ruler, lives in the Sahel, and has a cause, may come to the rock (15 in 100 a year). A cause: a spouse who thinks ill of her (opinion −25 or lower), a spouse she cannot bear (her opinion −40 or lower), or a court's lord who thinks ill of her (−30 or lower). She joins the court of whoever holds Kirina's county (`c_sibi_mali`), of any faith, and is **Under the Rock** (stress gained −25%, +1 stewardship for the fields set apart). *She Came to the Rock* (`tm_bd3.0010`) tells her.
- **The one she left** gets *She Is at the Rock* (`tm_bd3.0011`): let her be, or send to the keeper of the rock for her.
- **The keeper** then gets *They Ask for Her at the Rock* (`tm_bd3.0012`): "The rock keeps whoever comes to it" (piety and prestige; the asker thinks less of him), or give her up (she goes back; she never forgives him). A keeper of Badenya keeps her almost always.
- **The rock's people.** A woman at the rock who is not of the faith may take it, 5 in 100 a year, while a member of Badenya lives at the keeper's court or the keeper is of the faith.

**Survival.** The refuge gathers the faith's scattered members at its old seat, where the growth engine's contact rules can work, even when Badenya holds no land: the holder of Kirina is a court for them whatever his faith.

## 2. The fall of the associate (from 1352)

**Source.** Ibn Baṭṭūṭa, *Voyages* IV, pp. 417–419 (`research/waf_ibn_battuta_mali.md`; Gomez 2018 ch. 7, "Qāsā's Gambit"):
- the king quarrels with his chief wife, "the associate" in rule; he confines her with a commander and gives power to another wife, "not among the daughters of kings" (p. 417);
- his paternal cousins go to congratulate the new wife with ashes on their arms but no dust on their heads; when the associate is freed, they cover themselves with dust for her (p. 417);
- she rides daily to the audience place with her people of both sexes, dust on their heads, she veiled (p. 418);
- she is charged with urging an exiled cousin of the king to take the throne; the commanders say she deserves death; she takes refuge in the preacher's house, and "the story ends there" (pp. 418–419).

**What is not used** (the stage-2 decisions of 2026-10-21 stand): the cousins' nakedness before the king; the fettered slave woman's testimony (no slave woman is a witness or a mechanic); the name "Qāsā" (the loc says "the associate"; Ibn Khaldūn uses the word for a son, so it may be a title). No death penalty is scripted: the source ends at the sanctuary, and so do the options.

**What the player sees.**
- **A quarrel** (`tm_bd3.0020`). A Badenya ruler with an associate, from 1352, 3 in 100 a year (+5 if she thinks ill of the associate, +5 if another woman she favours is at hand): *A Quarrel with the Associate*. Raise the other woman in her place (the fallen associate is "kept by a commander" for three years); make peace; or let it pass.
- **Ashes and dust** (`tm_bd3.0021`, one to three months later). The grown women of the ruler's dynasty choose whom to honour: those who think better of the fallen associate cover themselves with dust for her; the rest bring ashes for the new one. Whichever side has more, the court sees it: dust costs the ruler prestige and gives it to the fallen; ashes give the ruler a little.
- **The fallen associate's answer** (`tm_bd3.0022`): ride veiled to the audience every day with her people, dust on their heads (a petition: the ruler may restore her, `tm_bd3.0024`); write to an exiled kinsman of the ruler, a man or woman of the dynasty away from court, urging the seat (he gains a claim; word reaches the ruler half the time, `tm_bd3.0023`); or bide her time.
- **Sanctuary** (`tm_bd3.0023`). "The commanders say she deserves death. She has gone into the preacher's house." Let the sanctuary stand; pardon her; or send her to her own people. No death.

## 3. Counting

`tm_bd3_tally_effect` keeps run-wide globals: `rock_came`, `rock_asked`, `rock_kept`, `rock_given`, `rock_joins`; `quarrels`, `raised`, `dust`, `ashes`, `rides`, `restored`, `letters`, `sanctuary`. `tools/census_report.py` prints them under "Badenya: the Rock and the associate".

## 4. Guardrails (in addition to `docs/faiths/badenya.md`)

1. No Underground Railroad, fugitive or plantation imagery at the rock (guardrail 11).
2. The shrine, the smith-priest and the flute rite never appear.
3. Dust and ashes only; never nakedness.
4. No slave woman's testimony; word "reaches the ruler".
5. The narrator claims no historical woman: "a traveller at Mali's court" tells of an associate who fell.
6. The fallen associate is never a schemer by nature: her letter is a choice the player or AI makes, and the sanctuary holds.

## 5. Open questions

1. ~~Should the rock also take in men?~~ **Decided (user, 2026-10-26):** members of the faith of either sex already qualify, which is enough; others only as daughters, Marked or declared sisters.
2. Should the keeper's "give her up" exist at all? Built, because the refuge is a custom a keeper may break; a keeper of Badenya almost never does.
3. The exiled kinsman's claim could start a war. Watch the observe run.
