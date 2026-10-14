# Transbian Maximalism — design lock (v1.1, locked 2026-10-14)

One decision per slot, with the belief-list row and the history verdict that backs it. Items marked **[YOUR CALL]** are the ones where I have recommended but the choice is genuinely yours; everything else I propose to lock and build.

Working names are placeholders for localisation; in-game key names are final.

---

## 1. Premise and setting

- **What it is.** A heretical rite inside the Eastern Christian world at the 867 start: the sect that kept the eunuch-angel theology the Byzantine court was already drifting away from, fused it with the memory of the Mother's priestesses, and drew one conclusion the orthodox never would: that the cut are women. Secret survival, not revival. (Beliefs F2, H18; G2 consequence 7.)
- **Homeland.** North-west Anatolia and Galatia, with Constantinople as the eminent site. Counties confirmed in game: `c_byzantion`, `c_kyzikos`, `c_ankyra`, `c_dorylaion`, `c_nikomedeia`, `c_abydos`, `c_antiocheia`. (G2 homeland verdict; AN: every ancient text calling castrates women is Anatolian or Syrian.)
- **Branches.** A Norse rite is optional later content (seiðr, *ergi*, Uppsala bells) arriving by the Varangian route; it shares the faith but not the knife. Britain is out. (NB verdict.)
- **Era arc.** Legal cover and neighbours' tolerance decay with the culture era: strong at 867, contested by 1066, gone by 1300. (G3 consequence 14.)

## 2. Religion stack

Keep the current file structure (religion → faith → main rite) but change the religion's family. **[YOUR CALL]**

| Option | Family | Effect | Recommendation |
|---|---|---|---|
| A | New faith under `christianity_religion` (`rf_abrahamic`) | Reads as a Christian heresy; inherits Christian doctrines and GHW; hostility handled by `heresy_hostility_doctrine`; Christian tenets (`tenet_communion` etc.) available; eunuch-angel theology fits. | **Recommended.** Matches every history verdict ("stage it as a heresy") and the Nicaea canon 1 story. |
| B | Own religion under `rf_pagan` (current scaffold) | Reads as a revived Cybele cult; freer tenet choice; "evil" hostility from all Abrahamic faiths. | Fits the trans-pagan wing of the online discourse but not the 867 Byzantine anchor. |
| C | Own religion under `rf_abrahamic` | Middle path: Abrahamic hostility rules, own doctrines, no Christian-only tenets. | Fallback if A's Christian special doctrines fight the design. |

Under A: faith key stays `transbian_maximalism`, `religion = christianity_religion`, `main_rite = transbian_maximalist_rite`, with the rite carrying the three core tenets and the doctrine overrides below. The religion-level file `tm_religion_types.txt` is deleted.

## 3. Doctrines (rite overrides on top of Christianity's baseline)

| Group | Pick | Backing |
|---|---|---|
| Gender | `doctrine_gender_female_dominated` **[YOUR CALL: `_equal` is the conservative fit]** | A1, H2, H9; WH (m): female rule attested, full matriarchy not |
| Clerical gender | `doctrine_clerical_gender_female_only` | E1; strongest row in every matrix; castrates count as women via the trait (section 5) |
| Clerical marriage | `doctrine_clerical_marriage_allowed` | C3/C4 |
| Head of faith | `doctrine_spiritual_head`, held by the Mother of the House (an elective theocratic title) **[YOUR CALL: `doctrine_no_head` per BD "No gods, no masters", H11]** | E1; Medina order's elected chief (MM) |
| Pluralism | `doctrine_pluralism_pluralistic` | D10, E5 |
| Marriage type | `doctrine_monogamy` reflavoured; sister-making is a separate rite with no inheritance effect | C4, H6; RP: adelphopoiesis below marriage in law |
| Divorce | `doctrine_divorce_allowed` | C4 |
| Bastardry | `doctrine_bastardry_none` ("no bastards") | C1 |
| Consanguinity | `doctrine_consanguinity_cousins` | default |
| Homosexuality | `doctrine_homosexuality_accepted` | C3 |
| Adultery (both) | `_accepted` | required by `tenet_polyamory` if ever picked; otherwise `_shunned` |
| Deviancy | `doctrine_deviancy_virtuous` | B5 |
| Witchcraft | `doctrine_witchcraft_accepted` | B4 |
| Clerical function | `doctrine_clerical_function_alms_and_pacification` | D2; galli alms economy (AN) |
| Clerical succession | `doctrine_clerical_succession_spiritual_appointment` | Medina order; eunuch bishops |
| Monasticism | `doctrine_monasticism_encouraged` | convent typikon as succession shell (QG) |
| Funeral | `doctrine_funeral_bewailment` | galli lament; joyas as undertakers (T2) |
| Pilgrimage | `doctrine_pilgrimage_encouraged`, reflavoured as flight to a sister's house | E9 |
| **New group `doctrine_tm_knife`** | three doctrines: `tm_knife_grandmother` / `tm_knife_aunt_bea` / `tm_knife_gift_alone`; chosen by event in the first year; `divergence = category` so rites can split on it | Dorley note; G3 (n) |
| **New group `doctrine_tm_body`** | `tm_body_aristotelian` ("the cut are women") / `tm_body_galenic` ("the cut are a third kind"); main rite takes Aristotelian; a scripted splinter rite takes Galenic | A3, H13; TG/NV: Aristotle vs Galen |

## 4. Core tenets of the main rite (exactly three)

| Tenet key | Working name | Mechanics | Backing |
|---|---|---|---|
| `tenet_tm_day_of_blood` | Day of Blood | Unlocks the Rite of the Knife (decision + prisoner interaction); yearly spring festival event; the cut gain the daughter trait and are treated as female by all faith script; parameter `tm_castrates_are_women = yes`; piety on each rite | B1, H19; AN galli dossier; TG medical loophole |
| `tenet_tm_daughters_chosen` | Daughters Chosen, Not Born | Grants `allows_adoption` + `free_adoption`-equivalent rite parameters (reuse the `tenet_adoptionism` parameter pattern); adopted daughters are full dynasts; childlessness carries no opinion malus; parameter `tm_adoptive_matriline = yes` | C1, H44; RP: Leo VI let eunuchs and childless women adopt; QG: Irene Doukaina's typikon |
| `tenet_tm_sisterhood` | Unbending Sisterhood | Reflavoured `tenet_communal_identity`: same-rite opinion bonus, hospitality to the cast-out, and the Sister-Making ceremony (no inheritance effect, prestige and piety for both houses) | E2, H6, H9; RP rite dossier; MM Medina quarter |

Rejected for core: `tenet_carnal_exaltation` and `tenet_hedonistic` (C6, "liberating sex without liberating women").

## 5. Traits

| Key | Purpose | Spec |
|---|---|---|
| `tm_transgender` (hidden) | The random seed | `random_creation = 1` (1%; tune), `birth = 1`, not inheritable, `shown_in_ruler_designer = yes` so designer rulers can start with it, hidden from AI reasoning except as event weight. Raises weight for seeking the rite and for intake selection. Theology: "Sisters are born of any womb" (H26). |
| `tm_daughter_of_the_knife` | The result of the rite | `category = health`, `group_equivalence = eunuch` (so vanilla eunuch checks still fire), `can_have_children = no`, `flag = can_not_marry` **removed**, **no** `inheritance_blocker`; `genetic_constraint`-free; portrait modifier (cosmetic route); all faith script treats holders as women; `shown_in_ruler_designer = yes` |
| `tm_novice` | Dorley chain stage marker | Timed trait/modifier for the three-year programme; carries the sponsor relation |
| `tm_washout` | Failure marker | For the washout event and the holy-order hand-over |

Re-embodiment (`tm_reembody_as_woman_effect`) fires on completion when the game rule allows; otherwise cosmetic only.

## 6. The Rite of the Knife (decision + interaction)

- **Voluntary path.** Decision for any adult male character of the rite with `tm_transgender` or high enough event-driven progress; performed by a priestess; in-world recorded "for health" (Leo VI Novel 60). Cost: piety; gain: trait, rename event, re-embodiment.
- **Dorley path** (`tm_knife_aunt_bea` only). Prisoner interaction gated on the intake trigger (male, 18–30, imprisoned by a rite ruler, violent marker: `sadistic`/`wrathful`/`callous`, `secret_murder`/`secret_murder_attempt`, imprisonment reason, or mod abuse flag; excluded: `stubborn` + strongly masculine profile). Assign sponsor (`set_relation_guardian`), three-year chain with "lever" events, knife at end of year one, release as ward, "New Personal History" rename and adoption at completion; washout on violence toward a woman of the court or failed progress.
- **Grandmother path** (`tm_knife_grandmother`). Vanilla `castrate_interaction` behaviour, vanilla eunuch trait, dread and prestige up, piety down, "evil" hostility from all.
- **Gift Alone.** Voluntary path only.

## 7. Culture

| Slot | Pick | Backing |
|---|---|---|
| Heritage | `heritage_byzantine` **[YOUR CALL: keep the custom `heritage_transbian` if you want a distinct map colour]** | homeland |
| Language | `language_greek` | homeland |
| Ethos | `ethos_communal` **[YOUR CALL: `ethos_egalitarian`]** | D1, D4; Medina quarter; convent |
| Martial custom | `martial_custom_female_only` | E8; Amazons, Alvild's crew (NB), women orators in crisis (AN) |
| Head determination | `head_determination_domain` | settled |
| Traditions | `tradition_court_eunuchs` (grants `can_castrate_prisoners`, `family_castration`, eunuch bonuses), `tradition_monastic_communities`, `tradition_esteemed_hospitality`, `tradition_equal_inheritance` **[YOUR CALL: swap for a new `tradition_tm_daughters_house` with female-only inheritance params]** | B1, D5, C2 |
| Name list | New `name_list_transbian`: Greek female names + attested gallae/eunuch/mukhannath names from the terminology sections (TG ~200, MM ~50, RW ~35, AN 33); male names = Greek list for pre-rite characters | H28 "Renaming is rebirth" |
| GFX | Byzantine sets (`byzantine_*_gfx`) | homeland |
| Culture name | "Baeddel" as the culture's *own* name is a north-west word; use a Greek one and keep *bæddel* for the Norse branch. Working name: **Kybeline** | H23 |

## 8. Succession

- Titles under the faith's rulers use the vanilla **female-preference** (or female-only) gender law. Because re-embodied daughters are female to the engine, adoptive matrilines then work with no custom succession code: adopt a daughter, she inherits.
- Where re-embodiment is off (game rule), fall back to designate-heir scripting for daughters still male to the engine.

## 9. Localisation and flavour

- HighGod: the Mother (barren protector, not progenitor; H20). Devil: the Bearded (the Galenist slur inverted). House of worship: *metroon*. Clergy: Daughter / Elder Sister / Mother of the House. Religious head title: Mother of Mothers.
- Festival: Day of Blood (spring). Founding trauma: 715 and "the Greater Circumcision" (RW). Hostile texts: Firmicus Maternus ("they wish to be believed women"), Roman *semivir*, Islamic *haram*.
- Easter eggs for the in-group only in event text, never in UI strings: AGA, novelty mug, "Dorleypilled".

## 10. Build order

1. Rewrite the three religion files for option A; add the two new doctrine groups and three tenets; faith history file flags the faith created in 867.
2. Traits file; cosmetic portrait modifiers.
3. Culture file on Byzantine pillars; name list.
4. Rite of the Knife decision; prisoner interaction; first-year knife-doctrine event.
5. Dorley chain events; washout; Sister-Making ceremony; New Personal History.
6. Re-embodiment effect wired to completion behind a game rule.
7. Loc; icons; CK3 Tiger; in-game test with `-develop`.

## Decisions (locked 2026-10-14)

| # | Decision | Locked value | Note |
|---|---|---|---|
| 1 | Religion family | **A — Christian heresy** (faith under `christianity_religion`) | User: start with the best-supported family; add an Eastern pagan revival (Cybele) and a Norse pagan family as separate faiths in a later version. |
| 2 | Gender doctrine | **`doctrine_gender_female_dominated`** | User decision. |
| 3 | Head of faith | **`doctrine_spiritual_head`**, elected Mother of Mothers | Recommendation adopted by default. |
| 4 | Heritage | **`heritage_byzantine`** | Recommendation adopted by default; custom heritage can return with the pagan families. |
| 5 | Ethos | **`ethos_communal`** | Recommendation adopted by default. |
| 6 | Culture name | **Kybeline** (`kybeline` culture key); *bæddel* reserved for the Norse branch | Recommendation adopted by default. |

## Deferred research (not blocking the build)

- **Ayalon, *Eunuchs, Caliphs and Sultans* (1999)** — PDF received 2026-10-14, converted to `docs/research/sources_pending/ayalon_eunuchs_caliphs_sultans.txt`, not yet read. Target: al-Jahiz's statement on eunuchs' transfer to the female realm, in context, for flavour text.
- **East and Southeast Asia.** CK3 1.20 includes China, Korea, Japan and Southeast Asia. Needed before the faith is given Asian branches or hostile-faith text there: Chinese court eunuchs (Tang–Yuan; Tsai, *The Eunuchs in the Ming Dynasty* for the later end), Mongol/Khanate attitudes to castration and gender variance, Korean *naesi*, Japanese absence of eunuchs, Southeast Asian *bissu*, *baylan* and *kathoey*-adjacent roles (Wiesner-Hanks touched bissu and baylan only briefly). Also the Mongol *Yassa* on sexual offences.
- **Kerala Nair matriliny and Tuareg descent** for on-map matrilineal precedents (G verdict g).
