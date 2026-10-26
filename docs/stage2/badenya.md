# Badenya, stage 2 (design note, 2026-10-21, untested in-game)

Prefix `tm_bd2_`, event namespace `tm_bd2`. Faith page: [docs/faiths/badenya.md](../faiths/badenya.md).

**Why these features.** In the v0.2.0 observe run (1034) Badenya held k_mali, k_takrur and k_guinea with 198 members. It ends up a royal faith. Stage 1 gave it a gate, a feast, a burial and the New Roof, all built around a small House. Stage 2 adds things that happen at a mansa's court as well as in a county: what happens to the sister's line when a ruler dies, the heat of a new reign, and the jelimuso who sings before the ruler and must be paid. Features 1–4 also fire for a count, so a small House sees them too.

**Status.**

| # | Feature | Status |
|---|---|---|
| 1 | The Sister's Line (succession) | Drafted in script and loc |
| 2 | A Hot Realm, a Cool Word | Drafted in script and loc |
| 3 | Praise Before the Court | Drafted in script and loc |
| 4 | Uninvited Praise (at a naming) | Drafted in script and loc |
| 5 | Named With the King (associate in rule) | Drafted in script and loc (the honour only), from 1352 |

**Files (all new).**
- `events/tm_bd2_events.txt`: tm_bd2.0001, 0002, 0010, 0020, 0030, 0040–0042
- `common/decisions/tm_bd2_decisions.txt`: `tm_bd2_name_associate_decision`, `tm_bd2_set_aside_associate_decision`
- `common/on_action/tm_bd2_on_actions.txt`: hooks on `on_death`, `yearly_playable_pulse`, `on_birth_child`
- `common/scripted_effects/tm_bd2_effects.txt`: `tm_bd2_find_jeli_effect`, `tm_bd2_succession_effect`, `tm_bd2_name_associate_effect`, `tm_bd2_associate_opinions_effect`, `tm_bd2_clear_associate_effect`
- `common/scripted_triggers/tm_bd2_triggers.txt`: `tm_bd2_jeli_trigger`, `tm_bd2_has_jeli_trigger`, `tm_bd2_sisters_child_trigger`, `tm_bd2_quarrel_party_trigger`, `tm_bd2_associate_ok_trigger`, `tm_bd2_associate_near_trigger`, `tm_bd2_has_associate_candidate_trigger`
- `common/modifiers/tm_bd2_modifiers.txt`: `tm_bd2_hot_realm_modifier`, `tm_bd2_cooled_realm_modifier`, `tm_bd2_associate_modifier`
- `common/opinion_modifiers/tm_bd2_opinion_modifiers.txt`: ten opinion modifiers
- `localization/english/tm_bd2_l_english.yml`

Validation: xTiger reports nothing in these files (23 reports in the worktree, all baseline). `tools/check_glyphs.py` is clean; every file has a BOM.

## Decisions (user, 2026-10-21)
- **Sister's line claims:** claims on kingdom-tier titles (e.g. k_mali) are fine; kept as drafted.
- **Named With the King:** built as a decision, a modifier and events, **not** vanilla diarchy (diarchy untouched). From 1352. "Associate in rule" in loc, never "Qasa". **The honour only**: no fall or plot chain (kept below as an optional later add). Ending it by decision or at a death, with no scripted villainy. No nakedness-at-court content.
- **Named With the King, follow-up:** open to player counts (AI at kingdom tier), unchanged. Eligible associates are **women only, cis and trans**: female-coded, a daughter by any gate (`tm_is_daughter_trigger`), or a Marked (`tm_transgender`) or declared (`tm_declared`) sister still coded male. No cis men. She/her in all text.
- **tm_badenya.0011:** the claiming woman is now stored (change made, below).

**Revision 2026-10-21 (after `docs/later_starts.md`, `research/later_starts/region_subsaharan-africa.md` and `research/later_starts/badenya_ghana_1066.md`).** The sister's line now leads with al-Bakri's dated Ghana case. Ghana's custom is spoken of in the present tense before 1077 and in the past tense after. A Muslim heir answers from Maliki inheritance, with al-Bakri's own rationale in a jurist's mouth. The royal-court detail of *Praise Before the Court* is gated by the dates of its sources. A Dates table and the later-start hooks are at the end.

---

## 1. The Sister's Line (drafted)

**What the player sees.** When a ruler of Badenya dies holding a county or more, one of two things happens to the heir.
- If the heir is a child of the dead ruler's sister and is of the faith, the heir gets *The Sister's Child* (tm_bd2.0001), a short event: "My mother's name goes first." +50 prestige, +25 piety. The text cites Ghana's custom and its stated reason (a man is sure his sister's child is of his blood) in the faith's voice: "they say … is" before 1077, "the old men say … was, before its king prayed toward Mecca" from 1077.
- Otherwise, if a sister's child of the faith is alive (adult, free, not the heir), the heir gets *The Sister's Line* (tm_bd2.0002). The heir may be of any faith: a Muslim heir of a Badenya mansa sees it too, with neutral text ("Among the Mother's Children, they tell me…"). Three answers:
  - **Give the sister's share in gold.** The heir pays `minor_gold_value` (vanilla, scaled to income), and the sister's child receives it. The child gains "Honoured the Sister's Line" (+25, 10 years). A Badenya heir gains +25 piety.
  - **Honour the sister's line before the court.** −50 prestige for the heir; the same opinion for the child.
  - **"The seat is mine. The belt is closer than the milk."** For a Muslim heir the option reads "The law of inheritance gives the seat to me", and the description gives the jurist's view: inheritance goes to a man's own children, and the old custom rested "on a doubt about paternity", as a geographer of Cordoba wrote (al-Bakri's own report of the reason, p. 328, attributed). This is a lawful position, not villainy: by 1178 every royal court in the region except Sosso is Muslim at the top (`later_starts.md`; regional note §"Court Islamisation"), so a Muslim heir of a Badenya ruler is a common case. +15 prestige for the heir. The sister's child gains an **unpressed claim** on the dead ruler's primary title and "Passed Over the Sister's Line" (−30, 20 years).

**Mechanic.** `tm_bd2_on_death` (`on_death`, which fires while the ruler still holds her titles) runs `tm_bd2_succession_effect`. It saves the dead ruler, her `primary_title` and `primary_heir`. The heir is a "sister's child" if the heir's mother is a sibling of the dead ruler. The candidate is the eldest child of any of her sisters (full or half) who passes `tm_bd2_sisters_child_trigger`. Events come 5 to 10 days after the death and check that the heir now holds the title. Bodies left at re-embodiment (`tm_reborn`) are skipped. Not budgeted: it is a succession mechanic, not flavour, and it happens once per death.

AI weights for 0002: base 20 / 10 / 30 for gold / word / claim. A Badenya heir adds +50 to gold, +20 to word, −20 to claim. Greed pushes toward the claim, honour toward the word.

**Sources.**
- **Period anchor:** al-Bakri, *Description de l'Afrique septentrionale* (finished 460/1067–68), trans. de Slane, p. 328: "Beci était l'oncle maternel de Tenkamenîn", who reigned from 455/1063; the custom gives the throne to the king's sister's son, because the king is sure his nephew is his sister's child but cannot be sure of his own son. The heir apparent is again the sister's son in the sewn-clothes rule (p. 329; L&H pp. 79–80 excerpt) ([dossier](../research/later_starts/badenya_ghana_1066.md) §2.2). Al-Zuhri (c. 1137) says Ghana's people became Muslim in 469/1076–77 (variant 496), hence the 1077 tense switch in the loc (dossier §5).
- Ibn Khaldun, *Histoire des Berbères* II, p. 111: Abu Bakr, a daughter's son of Mari Jata, chosen under the principle that gives the throne to the sister or the sister's son ([note](../research/waf_ibn_khaldun_mali.md)).
- Gomez 2018, chs. 3 and 6, reads the same al-Bakri passages ([note](../research/waf_gomez_african_dominion.md)).
- Ibn Battuta, *Voyages* IV, p. 388 (Walata: the heirs are the sister's sons) and p. 443 (Tagadda) ([note](../research/waf_ibn_battuta_mali.md)). Both are Berber towns, not Mande, and the evidence is from 1352. The loc no longer names Walata.
- Faith-voice lines: "The father is everybody's; the mother is one's own" (after Conrad and Condé 2004, l. 2163); the heir's refusal quotes the public patrilineal saying "the two ends of the belt get closer than the breast milk" (Koné 2004, p. 2) ([note](../research/waf_kone_male_female_mande.md)).

**Standing rules.**
- The mod does not claim Mansa Musa for the sister's line. The loc names no king of Mali or Ghana (not Tunka Manin either: vanilla's Tunka Menin is Bassi's son, against al-Bakri, so naming him would contradict the game's own data).
- No "African matriarchy": the feature is a claim and a payment, not a law, and the heir may refuse it.
- Hostility is the heir's own choice, in a saying the source attributes to the public patrilineal ideology.
- Re-embodied daughters bear no children, so a sister's line is the route the faith already relies on. This feature only makes the route visible at a succession.

**Optional flavour, not built: Makuria's *ngonnen*.** The Old Nubian title *ngonnen*, "sister of the current ruler and mother of the future one", is attested for Maria Iesousikol at Qasr Ibrim, probably 1155–c. 1180 (P. QI 3 32; DBMNT IMRef_5186), and for Aserimari in 1333 (regional note §E). A Makurian (Miaphysite) heir answering 0002 could get a reaction line from 1155 ("At Dongola too the king's sister is the mother of the next king"), or a Makurian court could think better of a sister's-line claimant. It needs a Makuria culture or title check, so it is noted only. No faith claim on Maria Iesousikol.

**Open questions.**
1. Should a "sister" be a sister of one mother only? That is closer to *badenya*. But many history characters have no recorded mother, so the draft takes any sister.
2. ~~Is an unpressed claim on a kingdom too strong?~~ Decided: kingdom claims are fine (user, 2026-10-21). Watch claimant wars in the next observe run.
3. Should the passed-over child get an event of her own, so a player in that seat notices the claim? Not built.

## 2. A Hot Realm, a Cool Word (drafted)

**What the player sees.** A new ruler of Badenya takes the realm *hot*: the modifier "A Hot Realm" (vassal opinion −5) for two years. With a 50% chance, 2 to 13 months after the death, *Hot Words* (tm_bd2.0010) arrives. Two vassals (or, without two vassals, two courtiers) have quarrelled before the court. Three answers:
- **Let the jelimuso speak of it coolly** (needs a jelimuso and `minor_gold_value`). The heat goes, and "The Realm Has Cooled" (vassal opinion +5) lasts five years. The two quarrellers gain "Cooled Our Quarrel" (+15) for each other. The jelimuso gains "Paid for My Praise".
- **Judge it myself, now.** +25 prestige. The second party gains "Judged Against Me" (−20). The realm stays hot.
- **Let it burn itself out.** The two gain "Hot Words" (−15) for each other.

Praise Before the Court (feature 3, option a) also cools a hot realm. Otherwise the heat simply runs out after two years.

**Mechanic.** Set in `tm_bd2_succession_effect` when the primary heir is of the faith. 0010 checks the flavour budget in its trigger and spends it in `immediate`. The jelimuso is found by `tm_bd2_find_jeli_effect`: the court chaplain if she is a woman or daughter of Badenya (the faith's clergy are *jelimusow*), else such a woman at court, daughters weighted up. AI: 60 / 25 / 15.

**Sources.**
- Jansen 2002, p. 53: heat is the Mande idiom for a society in change; the praise line "the Mande has cooled" ([note](../research/waf_jansen_kangaba_griots.md) §2.1).
- Schulz 2002, p. 816 n. 49: *suman*, cool and deliberate, against *kalan*, hot and quick to quarrel; p. 816: a cool speaker conveys a problem "without naming it in too explicit a manner"; p. 797 n. 1: jeliw resolved conflicts and restored "order and harmony" ([note](../research/waf_schulz_jelimusow.md)).

**Standing rules.** The feature uses the idiom only, as the faith page already says ("The House uses the idiom and none of the sanctuary's rites"). It does not use the Kamabolon's rules: not the one authorised speaker, not the red-cloth ban, not the "hot" rites for a royal death (Jansen 2002, pp. 53–54 and n. 105). The jelimuso who settles a quarrel follows Schulz's pre-colonial summary (LATER), not Kela practice. No stress is added: heat is a state of the realm, not a test of the ruler.

**Open questions.**
4. Should the heat also fall on a Badenya ruler who takes a kingdom by conquest or usurpation? Not built; only inheritance by a member of the faith.
5. −5 / +5 vassal opinion is modest on purpose. Tune after a run.

## 3. Praise Before the Court (drafted)

**What the player sees.** At a Badenya court with a jelimuso, *Praise Before the Court* (tm_bd2.0020). She begins with the ruler's mother's name, and her praise must be paid before everyone. The setting depends on tier and date:
- **King or emperor, from 1352:** the dais under the parasol with the gold bird; the bards in feather birds come after her and sing that those who sat there before did good, and that the ruler should do good so it is remembered (Ibn Battuta).
- **King or emperor, 1330–1351:** the dais, with the poet who speaks between the king and the people beside it (al-Umari). No parasol, birds or admonition.
- **Before 1330, or a lesser court at any date:** the household gathers and she sings "as the jelimusow of the House do". This is the faith's custom, and the text implies no period record. No jeli is attested at Ghana (al-Bakri has interpreters, a drum and viziers), so nothing before Mali is presented as attested.

Three answers:
- **Pay her before the whole court** (`medium_gold_value`): +100 prestige. She receives `minor_gold_value` and "Paid for My Praise". If the realm is hot, it cools.
- **Pay what is owed, and hear her out** (`minor_gold_value`): +25 prestige, +25 piety.
- **Pay nothing:** −50 prestige; she gains "Would Not Pay for Praise".

**Mechanic.** `tm_bd2_yearly` on `yearly_playable_pulse`. It needs a Badenya ruler of county tier or above, free, under the flavour budget, with a jelimuso. Chance 5% a year, +5 at kingdom tier or above from 1330 (the mansa's court heard the singers every Friday and at both feasts), +3 while the realm is hot. It spends the budget when it fires. AI: 40 / 40 / 5, greed shifting toward paying nothing.

**Sources.**
- Ibn Battuta, *Voyages* IV: Dugha sings the king's wars on feast afternoons and is paid 200 mithqals before the court (pp. 411–413); then the *djâli* in bird figures, whose verses say the kings before did good and tell the king to do good so it is remembered (pp. 413–414); the parasol with a gold bird above the dais (p. 406). The bards' admonition and its age are hearsay to him (pp. 413–414) ([note](../research/waf_ibn_battuta_mali.md)). Al-ʿUmari's poet-intermediary before the throne (Wilks, in Austen (ed.) 1999, pp. 44–47) ([note](../research/waf_conrad_austen_sunjata.md)).
- Schulz 2002, p. 797 n. 1: jeli women praised their patrons' genealogy at festivals and were paid in goods ([note](../research/waf_schulz_jelimusow.md)).
- The mother's name first: Conrad and Condé 2004, p. xxxv; Niane 1965, p. 15 n. 27; Jansen 2018, p. 14 n. 50.

**Standing rules and dates.** Ibn Battuta's visit is 1352–53; al-Umari wrote in the late 1330s from informants on Mansa Musa's court (reigned c. 1312–37). The gate for the first royal variant is **1330**: a round date inside the reign al-Umari's informants describe, and before he wrote, so it does not run ahead of a source by more than a few years. The Ibn Battuta detail waits for **1352**, the year he saw it. The event itself is not date-gated: the jelimuso's song is the faith's custom from its start, as in the existing gate's jeli step. The masked bards have no fee in the source. Joining Dugha's paid song and the bards' admonition in one woman's performance is the faith's invention, and the code comment says so. The bird figures are kept as Ibn Battuta's period detail; no Komo link (`waf_bulman_corpus.md`, "Do not use"). No informant's or real singer's name is used.

**Open questions.**
6. Should a Badenya jelimuso also sing at a *non-Badenya* West African court (a Muslim mansa with a jelimuso of the faith among his courtiers)? That would carry the faith into courts it does not rule. Not built.
7. Should the event be gated to Fridays or the feasts? CK3 has no weekday trigger; the existing calendar gates use months.

## 4. Uninvited Praise (drafted)

**What the player sees.** When a child is born to a parent of Badenya, on the eighth day a jelimuso nobody sent for comes to the naming. She sings the name with the mother's name first ("[mother]'s [child]") and waits to be paid. *Uninvited Praise* (tm_bd2.0030) goes to a ruling mother of the faith first, then a ruling father, then the mother if she is of the faith. Three answers:
- **Pay her** (`minor_gold_value`): +30 prestige.
- **Pay what I can** (`tiny_gold_value`): a coin toss between praise (+10) and a joke the yard laughs at (−25), as in the existing gate's satire.
- **Send her away:** −40 prestige.

**Mechanic.** `tm_bd2_on_birth` on `on_birth_child`. Chance 15%, under the flavour budget, which it spends. AI: 60 / 30 / 10.

**Sources.** Schulz 2002, p. 801 n. 10: some jeli singers come, often uninvited, to weddings and namings and impose praise that must be paid (1990s) ([note](../research/waf_schulz_jelimusow.md)). The name given on the eighth day, with the mother's name prefixed: Niane 1965, pp. 14–15 and n. 27 ([note](../research/waf_conrad_conde_sunjata.md)). Koné 2004, p. 3, gives the mother's family the right to name every third child ([note](../research/waf_kone_male_female_mande.md)); not used mechanically.

**Standing rules.** The practice is 1990s Mali (LATER) and is used as texture for the faith's world, as the faith page already does with Schulz. The loc depicts no living person or community and uses no real singer's name. This is the parents' side of a naming. The existing *A Naming Feast* (tm_badenya.0020) is a daughter serving and hosting. The two do not overlap.

**Open questions.**
8. Should it fire only for rulers? As drafted, a Badenya mother who rules nothing also hears it, under her own flavour budget.

## 5. Named With the King (drafted: the honour only)

**Date gate: from 1352.** The shared rule is attested only by Ibn Battuta, who saw it in 1352–53. The decision is hidden before 1352.

**What the player sees.**
- **Name an Associate in Rule** (decision; a Badenya ruler of county tier or above, from 1352; costs 100 prestige). It opens *Associate in Rule* (tm_bd2.0040), which offers whoever qualifies: her spouse, her eldest sister, her mother, or the woman who claimed her (stored by tm_badenya.0011 since this change). The candidate must be an adult woman, cis or trans (female-coded, a daughter, or a Marked or declared sister still coded male; no cis men), alive, free and not already someone's associate. A sister, mother or claimer must be at the ruler's court or her vassal. "Not yet" refunds the prestige. If the ruler has Muslim vassals or courtiers, the text adds the qadi's view: "a custom of this country, not of the law" (after Ibn Battuta's own "d'après l'usage de ce peuple", p. 417, put in an attributed courtier's mouth).
- **On naming:** the associate gets "Associate in Rule" (diplomacy +2, stewardship +2, +0.5 monthly prestige) and +50 prestige. Each vassal of the faith gains "Associate in Rule" opinion of her (+15, while it lasts). Each Muslim vassal gains "A Custom of the Country, Not of the Law" (−10, 10 years) of the ruler: a lawful view, not hostility.
- **Two Names at the Feast** (tm_bd2.0041): yearly, chance 8%, under the flavour budget. Her name is said with the ruler's: +20 prestige each, and new vassals of the faith gain the opinion.
- **Ending it.** *Set Aside My Associate in Rule* (decision) removes the honour; she takes "Set Me Aside" (−15, 5 years) and nothing else. If she dies, the ruler gets *One Name at the Feast* (tm_bd2.0042) and the honour ends. If the ruler dies, it ends silently (the honour was hers to give). In each case the modifier, the variables and the vassal opinions are removed.

**AI.** AI rulers rarely use it: only at kingdom tier or above, checked every 120 days, will-do 3 (+5 if the spouse qualifies and has diplomacy 12+). In the choice event, spouse 50, sister 30, claimer 30, mother 20, "not yet" 5. AI set-aside only if the associate's opinion of the ruler is −50 or worse.

**Mechanic.** Ruler variable `tm_bd2_associate` (the associate); associate variable `tm_bd2_associate_of` (the ruler). Clean-up in `tm_bd2_clear_associate_effect`, hooked on `on_death` (`tm_bd2_associate_on_death`) for both parties.

**Sources.** Ibn Battuta IV, p. 417: Qasa, Sulayman's chief wife, "the associate" in government by the custom of the people, her name said from the pulpit with his ([note](../research/waf_ibn_battuta_mali.md)). Gomez 2018, ch. 7, "Qasa's Gambit" ([note](../research/waf_gomez_african_dominion.md)). Ibn Khaldun II, p. 114 gives "Cassa" as Sulayman's son: the name may be a title, so the loc says "associate in rule".

**Standing rules.** No nakedness at court (pp. 417–418, 423–424) appears. The narrator claims no historical woman; the decision text cites "a traveller at Mali's court". The faith gains no "matriarchy": it is one ruler's honour to one woman, ended at will. The Muslim reaction is an opinion, not a scheme.

**The fall: built in wave 9 (`tm_bd3.0020`–`0024`, `docs/wave9/badenya.md`).** Originally an optional later add: Source, pp. 417–419: the king confines Qasa and raises another wife, Banju, "not among the daughters of kings"; his female cousins honour Banju with ashes only and Qasa with dust when she is freed; Qasa is charged with urging an exiled cousin to take the throne, and takes sanctuary in the preacher's house. A chain could let a ruler raise a second woman over the associate, with the women of the dynasty choosing whom to honour (dust only, never nakedness), and sanctuary as the release. No slave woman's testimony as a mechanic. Build only if the user asks.

**Open questions.**
9. Should the decision be open below kingdom tier? As drafted, a count may use it (player only: the AI needs kingdom tier).
10. ~~Should a male spouse be eligible?~~ Decided: women only, cis and trans (user, 2026-10-21).

## Dates

| Feature | Earliest date its sources support | Gate used |
|---|---|---|
| 1. Sister's Line (0001, 0002) | 455/1063 at Ghana (al-Bakri, written 1067–68); the custom is reported as old there. Mali's daughter's son: undated reign, written 1380s (Ibn Khaldun). Walata 1352. | None. The faith holds the custom from 867, in its own voice. Loc tense switches at **1077** (al-Zuhri's 469/1076–77). The Muslim heir's lines need no gate. |
| 2. Hot Realm (0010) | The idiom is LATER (Jansen fieldwork 1990s; Schulz 1994–2000). | None; idiom only, faith's voice. |
| 3. Praise Before the Court (0020) | Poet before Mali's throne: al-Umari, late 1330s (Musa's reign). Parasol, feather birds, admonition, paid singer: Ibn Battuta 1352–53. Jelimusow paid in goods: Schulz, pre-colonial summary (LATER). No jeli at Ghana. | Royal variant **1330** (poet only) and **1352** (full detail). Plain faith-custom version otherwise. Kingdom-tier frequency bonus from 1330. |
| 4. Uninvited Praise (0030) | Uninvited praise at namings: Schulz, 1990s (LATER). Eighth-day naming with the mother's name: Niane 1960 (LATER). | None; faith custom, no period claim in the text. |
| 5. Named With the King (0040–0042, decisions) | Qasa, 1352–53 (Ibn Battuta). | **1352**: both `is_shown` and `ai_potential`. |

## Later-start hooks (notes only, not built)

From `docs/later_starts.md` and the Ghana dossier. The starts themselves are shelved; these are where the stage-2 features could attach if they are built.
- **1066, Ghana's grove-town (`c_awkar`, `b_al-ghaba`).** The sister's son is reigning there, after his mother's brother (Tunka Manin from 1063). *The Sister's Line* would be the natural first event at a 1066 start. But vanilla makes Tunka Menin Bassi's *son* and Kambine his son-successor, against al-Bakri. Any scripted sister's-son heir there belongs to the start script (dossier §6.7, item 3), not to these events, which only react to whoever the game makes heir.
- **1066, the word at Ghana.** No jeli is attested; the dossier's "Before the Drum" puts the word with the Muslim interpreter at the *duba* audience. *Praise Before the Court* at a Ghana-held court would want an interpreter variant in place of the jelimuso (not built; the plain version is the faith's custom, which is acceptable but less grounded).
- **The grove closed after 1076.** The 1077 tense switch in 0001/0002 is the stage-2 echo of the dossier's "The Grove Is Closed" and of the `awkar` holy-site past-tense loc. If that chain is built, the two should share one trigger (e.g. a global variable set when Ghana's ruler converts) in place of the fixed year.
- **1178, Kirina under Maghan Kon Fatta** (161018), a vanilla challenge character, Shafiʿi. **Never touch him.** None of the stage-2 features targets him: 0001/0002/0010 fire only on the death of a ruler *of Badenya*, and 0020 only for Badenya rulers. If a Badenya courtier at his court is ever seeded, 0030 can reach her births only.
- **1178, Muslim courts.** By 1178 every royal court in the region except Sosso is Muslim at the top. The Muslim-heir variant of 0002 is written for that world. A Maliki jurist reaction pass at long-converted courts (regional note, 1178 flavour 3) would sit beside it.

---

## Changes to existing files (not made; for the user to apply)

1. **docs/TODO.md**, under "Stage 2, first pass", or a new "Stage 2, second pass" heading:
   `- [ ] Badenya stage 2 (`tm_bd2`): the sister's line at a succession (0001, 0002); a hot realm and the cool word (0010); praise before the court (0020); uninvited praise at a naming (0030). Not built: Named With the King (Qasa).`
2. **docs/TO-TEST.md §J**, add:
   - **The sister's line (Badenya).** Give a Badenya count a sister with an adult child of the faith, then kill the count (`kill`). The heir gets *The Sister's Line* in 5–10 days. Check (a) gold moves to the sister's child, (b) prestige, (c) an unpressed claim on the dead count's primary title and the −30 opinion. Make the sister's child the heir (e.g. a childless ruler under partition with the nephew as heir) and check *The Sister's Child* instead. Repeat with a Muslim heir: the text should be the neutral variant.
   - **A hot realm.** The Badenya heir has "A Hot Realm". *Hot Words* comes in 2–13 months about half the time; check the jelimuso option needs a Badenya woman or daughter at court and cools the realm.
   - **Praise before the court.** `trigger_event = tm_bd2.0020` on a Badenya ruler with a Badenya court chaplain. Check the three descriptions (a king before 1330, 1330–1351, from 1352; a count at any date), the mother's-name line with and without a known mother, and that (a) cools a hot realm. For *The Sister's Line*, also check the Ghana tense switch at 1077 and the Muslim heir's description and option text.
   - **Associate in rule.** Before 1352 the decision is hidden. From 1352, a Badenya ruler with a wife, a sister at court or a mother at court: take the decision, check each candidate option and "Not yet" (prestige refunded), the modifier, the +15 opinion from vassals of the faith, the −10 from Muslim vassals and the qadi's line. `trigger_event = tm_bd2.0041` (with the flavour budget free) brings in new faith vassals. Set her aside by decision; kill her (`kill`) and check *One Name at the Feast* and that the vassal opinions are gone; name another, then kill the ruler and check the associate loses the modifier.
   - **Uninvited praise.** `trigger_event` is not enough (it needs the newborn's scopes). Let a Badenya ruler have a child with the flavour budget free; the event comes eight days after the birth about one time in seven.
3. **docs/faiths/badenya.md**, "From source to mechanic" table, add rows:
   - *The Sister's Line* (tm_bd2.0002) | The heir pays the sister's share, honours it in words, or refuses, and the sister's child gains a claim. | al-Bakri (de Slane p. 328; 455/1063); Ibn Khaldun II, p. 111; Ibn Battuta IV, pp. 388, 443
   - *A Hot Realm* / *Hot Words* (tm_bd2.0010) | A new ruler's realm is hot until a jelimuso's cool word settles a quarrel. | Jansen 2002, p. 53; Schulz 2002, pp. 797 n. 1, 816 and n. 49
   - *Praise Before the Court* (tm_bd2.0020) | The jelimuso sings the ruler's line, the mother's name first; paid before everyone. At a king's court from 1330 the poet stands by the dais; from 1352 the parasol, the feather-bird bards and their admonition. | al-Umari (Wilks, pp. 44–45); Ibn Battuta IV, pp. 406, 411–414; Schulz 2002, p. 797 n. 1
   - *Uninvited Praise* (tm_bd2.0030) | On the eighth day a jelimuso nobody sent for sings the child's name and must be paid. | Schulz 2002, p. 801 n. 10; Niane 1965, pp. 14–15
   And in "Invented by the mod": "The hot realm after a succession, the heir's three answers to the sister's line, and the merging of Dugha's paid song with the masked bards' admonition in one jelimuso."
4. **events/tm_badenya_events.txt, tm_badenya.0011: MADE (2026-10-21, user's go-ahead).** In options (a) and (b), `set_variable = { name = tm_claimed_by value = scope:tm_claimer }` on root (the claimed daughter), each marked with a `# tm_bd2:` comment. It lets *Named With the King* offer the claiming woman. Only daughters claimed after this change have it.
5. **README.md**, the Badenya section's "How it plays", one short paragraph: "**At court.** When a ruler of the faith dies, the heir answers the sister's line: pay the sister's share, honour it in words, or refuse, and the sister's child gains a claim. A new ruler's realm is hot until a jelimuso's cool word settles it. The court's jelimuso sings the ruler's line, mother's name first, and must be paid before everyone; at a child's naming one may come uninvited. From 1352 a ruler may name her spouse, a sister, her mother or her claiming mother associate in rule, and her name is said with the ruler's at the feast."

## Notes for the survival-balance task (ideas only, not built)

- **The sister's line as a rescue for the faith's titles.** When a Badenya ruler's heir is not of the faith, the sister's child's claim (feature 1) already gives the faith a road back to the title by war. A stronger form, for that task to judge: if the heir is of another faith and the ruler had no child of the faith, the sister's child of the faith could get a *pressed* claim, or the AI weight for (c) could rise only in that case. This is the royal-scale counterpart of the seat fix (§16 "Fix B").
- **Daughters leaving.** The jelimuso at a court (features 2–3) gives a daughter a paid, honoured place at court. A small yearly chance that a jelimuso who was paid well ("Paid for My Praise") stays rather than wanders could help keep daughters at Badenya courts. It would be a weight, not a cap.
- **House decline.** The uninvited praise (feature 4) only touches births. Badenya's line runs by claiming, not birth. A naming event for a *claimed* daughter (after tm_badenya.0011) might matter more for continuity than births.
- **Conversion of heirs.** An heir of another faith who answers the sister's line with (a) or (b) might be a candidate for the growth engine's call (small modifier), since the heir has publicly honoured the faith's line.

## Uncertain syntax (for the in-game test)

- `order_by = age` in `ordered_in_list` (vanilla also writes `order_by = { value = age }`).
- `mother ?= { any_sibling = { this = scope:tm_bd2_old } }` on the heir, run inside `on_death` while the dead ruler is still alive.
- `scope:mother` and `scope:father` reaching a child on_action of `on_birth_child` (vanilla's own child on_actions there, such as `pam_auspicious_birthright_birth_on_action`, are hooked the same way).
- `add_unpressed_claim = scope:tm_bd2_title` from a saved title scope.
- Saved scopes (`tm_bd2_old`, `tm_bd2_title`, `tm_bd2_sisters_child`) carried through `trigger_event` with a delay, as the existing packs do.
- Clearing the honour from inside the associate's own `on_death` (the clean-up runs in the ruler's scope while the associate still lives), and `scope:tm_bd2_former` reaching tm_bd2.0042 one day later.
- `var:tm_bd2_associate ?=` on a character variable that may point to a dead character after a missed clean-up (guarded by `is_alive` in 0041).
