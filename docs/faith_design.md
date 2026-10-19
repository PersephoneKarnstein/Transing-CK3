# Adelphai Dorleyaiou (Transbian Maximalism) — design lock (v1.9, locked 2026-10-14)

One decision per slot, with the belief-list row and the history verdict that backs it. Items marked **[YOUR CALL]** are the ones where I have recommended but the choice is genuinely yours; everything else I propose to lock and build.

Working names are placeholders for localisation; in-game key names are final.

---

## 0. Scope principle (user, 2026-10-14)

**This mod adds the trans culture, faith and rites. It does not build an antagonist.** There is no constructed "TERF nation", no allegorical rival superpower, and no scripted clash of civilisations. Opposition to the Sisters comes only from the vanilla world as it already is: the hostility doctrines, crimes and opinions of the existing historical faiths, the normal Byzantine, Islamic, steppe and Chinese courts, and the era-based decay of tolerance that the history reports document. "Hostile-faith text" in the research means *how existing faiths would react*, not a new enemy. Consequences:

- The belief-list row E7 ("Raymondite heresy as a hostile foil faith") is **dropped**. Grandmother's House survives only as a *doctrine option inside the faith* and as hostile reputation, never as a rival polity.
- Flavour events against notable targets (section 11) are jokes about the vanilla world, not a war arc.
- Later pagan or Norse families are *branches of the same faith*, not opponents.
- AI behaviour toward the faith uses vanilla hostility levels. A custom casus belli *against* the Sisters is **allowed as comedy** (user, 2026-10-14: "that would be very funny"): a vanilla faith's head declaring a one-off holy war to "rescue" the sons of a realm, in the manner of the Roman Senate's ban on citizens joining the galli, is a reaction event, not an antagonist. The rule is about *who* exists on the map, not about *what the existing faiths may do*.
- The mirror is also in (user, 2026-10-14): the Sisters get a **"Rescue the Daughters" casus belli** against a realm holding characters with the *Marked by the Mother* trait (or a daughter of the knife) who are imprisoned, hostaged or otherwise held. Victory frees and transfers them to the attacker's court for adoption. Scope it like a vanilla claim or holy war on a single county or duchy, gated on the knife doctrine not being Grandmother's House. Period framing: the Byzantine–Arab prisoner exchanges on the Cilician frontier, in which eunuch envoys negotiated ransoms (Ayalon), and the Church's own "liberation of captives" casus.

## 1. Premise and setting

- **What it is.** A heretical rite inside the Eastern Christian world at the 867 start: the sect that kept the eunuch-angel theology the Byzantine court was already drifting away from, fused it with the memory of the Mother's priestesses, and drew one conclusion the orthodox never would: that the cut are women. Secret survival, not revival. (Beliefs F2, H18; G2 consequence 7.)
- **Name.** *Adelphai Dorleyaiou*, "Sisters of Dorleyaion" (user, 2026-10-14): the Greek genitive of Dorylaion would be *Dorylaiou*; the *-ley-* spelling is deliberate and canonical, making the Dorley pun explicit. Adjective/adherent: Dorleyaian, Dorleyaian Sister. `tm_` remains the key prefix.
- **Homeland.** North-west Anatolia and Galatia; **Dorylaion (`b_dorylaion` in `c_phrygia`) is the faith's seat and eminent holy site**, with Constantinople as the second eminent site. In 1.20 the classical towns are **baronies**: Dorylaion (`b_dorylaion`) and Pessinus (`b_pessinus`) both lie in the county of Phrygia (`c_phrygia`, duchy of Opsikion); Kyzikos is `b_kyzikos` in `c_nikaea`; Ankyra is `b_ankyra` in `c_galatia`. Constantinople is the vanilla `constantinople` holy site (`c_byzantion`). (G2 homeland verdict; AN: every ancient text calling castrates women is Anatolian or Syrian.)
- **Interpretations, not a merge (user, 2026-10-14).** The final product may ship two or more *distinct cultural interpretations* of the premise as separate faiths. This file specifies the Byzantine one. A Tang/Chinese interpretation (eunuch dynasties, Daoist gender-by-rite, the knifer's liturgy) is a separate later faith, and its research is not folded into this one.
- **Branches.** A Norse rite is optional later content (seiðr, *ergi*, Uppsala bells) arriving by the Varangian route; it shares the faith but not the knife. Britain is out. (NB verdict.)
- **Era arc.** Legal cover and neighbours' tolerance decay: strong at 867, contested from 1057 and especially after the Komnenian turn of 1081 (Athos closed to eunuchs 1083), gone by 1300. Leo VI's Novel 60 was never repealed; what decays is eunuch power and tolerance (research/byz_sideris_eunuques_societe.md, byz_ringrose_perfect_servant.md). (G3 consequence 14.)

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
| `tm_transgender` | The random seed | `random_creation = 1` (1%; tune), `birth = 1`, not inheritable, `shown_in_ruler_designer = yes`. **Visible trait** (CK3 has no hidden traits; see 5a). Raises weight for seeking the rite and for intake selection; AI otherwise ignores it. Theology: "Sisters are born of any womb" (H26). In-world name: *Marked by the Mother*. |
| `tm_daughter_of_the_knife` | The result of the rite | `category = health`, `group_equivalence = eunuch` (so vanilla eunuch checks still fire), `can_have_children = no`, `flag = can_not_marry` **removed**, **no** `inheritance_blocker`; `genetic_constraint`-free; portrait modifier (cosmetic route); all faith script treats holders as women; `shown_in_ruler_designer = yes` |
| `tm_novice` | Dorley chain stage marker | Timed trait/modifier for the three-year programme; carries the sponsor relation |
| `tm_washout` | Failure marker | For the washout event and the holy-order hand-over |

**Infertility is non-negotiable (user, 2026-10-14).** A re-embodied daughter is female to the engine and would otherwise roll normal fertility. Two guards: `create_character` sets `fertility = 0`, and the effect always adds `tm_daughter_of_the_knife` (`can_have_children = no`) to the new body regardless of what the old one carried. Test: a re-embodied daughter married to a man must never conceive.

Re-embodiment (`tm_reembody_as_woman_effect`) fires on completion when the game rule allows; otherwise cosmetic only.

### 5a. Finding daughters to recruit and adopt (user request, 2026-10-14)

Since succession runs through adoption and the Gift Alone cannot compel anyone, players need to *find* marked characters. Facts from the game files:

- `gui/window_character_finder.gui` already exposes `CharacterSelectionList.GetFilter('trait_filter')` alongside culture, religion, gender, sexuality, range and more. Any ordinary trait can be filtered with **no GUI modding**.
- `common/traits/_traits.info` offers only `shown_in_encyclopedia` and `shown_in_ruler_designer`; there is no per-viewer or hidden trait. A truly hidden state would have to be a character flag, which the finder cannot filter.

**v1 decision: `tm_transgender` is a visible trait**, so the vanilla finder's trait filter finds every marked character in diplomatic range for free. This matches CK3's omniscient UI (sexuality is already a finder filter) and costs nothing. Open the finder, filter by *Marked by the Mother*, invite or adopt.

**Later option (thematic):** keep the seed as a hidden flag and add a visible marker trait granted only when a Sister *recognises* the person (a short "Discern the Mark" scheme or an on-action when a marked character enters your court or a faith holy site). The finder then filters by the marker, so only discovered daughters are findable. Ship behind a game rule if wanted.

To verify in-game: that a custom trait appears in the finder's trait list (expected, since the list is engine-built from trait definitions), and that `range_filter` does not hide too many candidates for a small Anatolian realm.

## 6. The Rite of the Knife (decision + interaction)

- **Voluntary path.** Decision for any adult male character of the rite with `tm_transgender` or high enough event-driven progress; performed by a priestess; in-world recorded "for health" (Leo VI Novel 60). Cost: piety; gain: trait, rename event, re-embodiment.
- **Dorley path** (`tm_knife_aunt_bea` only). Prisoner interaction gated on the intake trigger (male, 18–30, imprisoned by a rite ruler, violent marker: `sadistic`/`wrathful`/`callous`, `secret_murder`/`secret_murder_attempt`, imprisonment reason, or mod abuse flag; excluded: `stubborn` + strongly masculine profile). Assign sponsor (`set_relation_guardian`), three-year chain with "lever" events, knife at end of year one, release as ward, "New Personal History" rename and adoption at completion; washout on violence toward a woman of the court or failed progress.
- **Vanilla castration coexists (user, 2026-10-14).** The mod never overrides vanilla castration: the prison and family castrate interactions still produce ordinary eunuchs (`eunuch_1`/`beardless_eunuch`), not daughters. Becoming a daughter happens only through the faith's own rite, decision or Dorley path.
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
| Traditions | `tradition_court_eunuchs` (grants `can_castrate_prisoners`, `family_castration`, eunuch bonuses), `tradition_monastic_communities`, `tradition_esteemed_hospitality`, `tradition_female_only_inheritance` (built; its can-pick rule accepts a female-dominated rite) | B1, D5, C2 |
| Name list | New `name_list_transbian`: Greek female names + attested gallae/eunuch/mukhannath names from the terminology sections (TG ~200, MM ~50, RW ~35, AN 33); male names = Greek list for pre-rite characters | H28 "Renaming is rebirth" |
| GFX | Byzantine sets (`byzantine_*_gfx`) | homeland |
| Culture name | "Baeddel" as the culture's *own* name is a north-west word; use a Greek one and keep *bæddel* for the Norse branch. Working name: **Kybeline** | H23 |

## 8. Succession

- Titles under the faith's rulers use the vanilla **female-preference** (or female-only) gender law. Because re-embodied daughters are female to the engine, adoptive matrilines then work with no custom succession code: adopt a daughter, she inherits.
- Where re-embodiment is off (game rule), fall back to designate-heir scripting for daughters still male to the engine.

## 9. Localisation and flavour

- HighGod: the Mother (barren protector, not progenitor; H20). Devil: the Bearded (the Galenist slur inverted). House of worship: *metroon*. Clergy: Daughter / Elder Sister / Mother of the House. Religious head title: Mother of Mothers.
- Festival: Day of Blood (spring). Founding trauma: 717 (Rowson; earlier notes said 715) and "the Greater Circumcision" (RW). Hostile texts: Firmicus Maternus ("they wish to be believed women"), Roman *semivir*, Islamic *haram*.
- Easter eggs for the in-group only in event text, never in UI strings: AGA, novelty mug, "Dorleypilled".

## 10. Build order

1. Rewrite the three religion files for option A; add the two new doctrine groups and three tenets; faith history file flags the faith created in 867.
2. Traits file; cosmetic portrait modifiers.
3. Culture file on Byzantine pillars; name list.
4. Rite of the Knife decision; prisoner interaction; first-year knife-doctrine event.
5. Dorley chain events; washout; Sister-Making ceremony; New Personal History.
6. Re-embodiment effect wired to completion behind a game rule.
7. Loc; icons; CK3 Tiger; in-game test with `-develop`.

## 11. Flavour "achievements" (events, since mods cannot add Steam achievements)

CK3 is known for its joke achievements, and the mod should carry its own as events that fire on completion of the Rite of the Knife (voluntary or Dorley path) against a notable target. Each grants a nickname, a memory, prestige or piety, and a unique event picture or text; a hidden character flag on the player records it so a "Deeds of the House" decision can list them. Working titles:

| Event | Trigger (on rite completion) | Payoff | Period hook |
|---|---|---|---|
| **Ioanna Secunda** | Target holds `k_papal_state` or is head of a faith with `special_doctrine_is_christian_faith` and a Roman seat | Nickname "the Unmaker" for the officiant; the new daughter may be adopted into the player's house; Catholic hostility pinned at maximum for a generation; event text invokes the Pope Joan legend (c. 855) and calls her "the second" | Pope Joan; Nicaea canon 1; Byzantine eunuch patriarchs make the Eastern equivalent *less* scandalous |
| **The Patriarch's Daughter** | Target is Patriarch of Constantinople or any eunuch-eligible Orthodox head | Lower payoff: Byzantium had eunuch patriarchs, so the text is wry rather than apocalyptic; piety bonus for "restoring the old order" | TG: eunuch patriarchs and bishops |
| **Al-Kunduri's Mercy** | Target is a vizier or councillor of a Muslim ruler, captured and taken through the Dorley path, then returned to office | Precedent event quoting the 1064 case; the realm that takes him back gains a hook on you | Ayalon: al-Kunduri castrated and kept in office |
| **Gelded Like My Camels** | Target is a steppe ruler or his son | Hostility event from the khan's court; chance of a *yargu* judgment and war; Tengrist faiths treat it as foreign Chinese cruelty | Terbish: Mongols met "castrated and feminine men" only in China |
| **Six Hundred Daughters** | Player's house reaches 50 adopted daughters by the knife | Reference to Yang Fugong's "six hundred adopted sons"; dynasty prestige | Hoeckelmann: Tang eunuch dynasties |
| **The Greater Circumcision** | A rite performed on a court musician or poet | Rowson's 715 jokes as the event's option text | Rowson |
| **Mother of Mothers Unmade a Father of Fathers** | Both the Pope and the Patriarch in one lifetime | Achievement-style summary event; legendary nickname | — |

Design rule: the Pope event must exist in all three knife doctrines but read differently — triumph under Grandmother's House, uneasy rehabilitation under Aunt Bea's, and impossible under the Gift Alone unless he consents (a separate, rarer event).

## Open questions resolved (user, 2026-10-14)

| # | Question | Decision |
|---|---|---|
| 1 | Starting presence in 867 | **Yes**: a few Phrygian counties around Dorylaion start Kybeline and Dorleyaian under a small landed house. |
| 2 | Marked women / trans men | **Out of scope.** This mod is about trans women; a trans-masculine mod is someone else's to make. The seed trait is restricted to male-born characters (`valid_sex = male`). |
| 3 | Head of faith | Mother of Mothers title seated at Dorylaion, filled by clerical appointment. The starting holder leans into the Dorley allusion: **Theia Beatrike** ("Aunt Beatrice"; *theia* is the ordinary Byzantine/modern Greek word for aunt). |
| 4 | Seed heritability | Either is fine; slight heritability is acceptable ("debated in the real world"). Keep `genetic = yes` for v1. |
| 5 | Marriage on re-embodiment | **Carry the marriage over.** |
| 6 | Perks on re-embodiment | Lifestyle XP carries; perks lost. Accepted. |
| 7 | Dorley intake age | **18 and up, no upper limit.** |
| 8 | AI knife doctrine | AI-run faiths may pick any of the three Houses. |
| 9 | Galenic splinter rite | **Deferred.** v1 is the minimum viable product; splinter rites and the Norse/Eastern religions come later. |
| 10 | Sister-Making | **Custom scripted relation.** |
| 11 | Casus belli scope | No preference; chosen: *Rescue the Daughters* targets a single county; *Rescue the Sons* may be declared by the head of any Christian or Islamic faith whose hostility toward the Sisters is Hostile or worse. |
| 12 | Era decay of tolerance | After the core loop works. |
| 13 | Name list | Draft `name_list_kybeline` from attested names in the research. |

### v1 minimum viable product
Faith, rite, culture, traits (done); starting presence and head of faith; voluntary rite (done) and House choice (done); Dorley prisoner path with sponsor and washout; re-embodiment carrying marriages; rename event; Sister-Making; Rescue the Daughters CB; name list. Everything else is post-v1.

## Decisions (locked 2026-10-14)

| # | Decision | Locked value | Note |
|---|---|---|---|
| 1 | Religion family | **A — Christian heresy** (faith under `christianity_religion`) | User: start with the best-supported family; add an Eastern pagan revival (Cybele) and a Norse pagan family as separate faiths in a later version. |
| 2 | Gender doctrine | **`doctrine_gender_female_dominated`** | User decision. |
| 3 | Head of faith | **`doctrine_spiritual_head`**, elected Mother of Mothers | Recommendation adopted by default. |
| 4 | Heritage | **`heritage_byzantine`** | Recommendation adopted by default; custom heritage can return with the pagan families. |
| 5 | Ethos | **`ethos_communal`** | Recommendation adopted by default. |
| 6 | Culture name | **Kybeline**; **mod/faith name: Adelphai Dorleyaiou** (`kybeline` culture key); *bæddel* reserved for the Norse branch | Recommendation adopted by default. |

## Deferred research (not blocking the build)

- **Ayalon, *Eunuchs, Caliphs and Sultans* (1999)** — PDF received 2026-10-14, converted to `docs/research/sources_pending/ayalon_eunuchs_caliphs_sultans.txt`, not yet read. Target: al-Jahiz's statement on eunuchs' transfer to the female realm, in context, for flavour text.
- **East and Southeast Asia.** CK3 1.20 includes China, Korea, Japan and Southeast Asia. Needed before the faith is given Asian branches or hostile-faith text there: Chinese court eunuchs (Tang–Yuan; Tsai, *The Eunuchs in the Ming Dynasty* for the later end), Mongol/Khanate attitudes to castration and gender variance, Korean *naesi*, Japanese absence of eunuchs, Southeast Asian *bissu*, *baylan* and *kathoey*-adjacent roles (Wiesner-Hanks touched bissu and baylan only briefly). Also the Mongol *Yassa* on sexual offences.
- **Kerala Nair matriliny and Tuareg descent** for on-map matrilineal precedents (G verdict g).

## 12. Branch faiths: distinct playstyles (planning, 2026-10-18)

Three faiths, no more for now. Each answers three questions differently: how one becomes a daughter (the gate), how the line continues, and how the faith meets a hostile world. Shared across all three: the Marked trait, re-embodiment, Take as Daughter. Everything else is per-faith.

| | Dorleyism (Byzantine, built) | Bæddel faith (Norse and Anglo-Saxon) | Chinese faith |
|---|---|---|---|
| Gate | The knife as sacrament, with a sponsor | Seiðr: trance-unmanning and public declaration; the knife only a rare Varangian import | Inner alchemy: a ten-month inner gestation, then rebirth. The knife is refused as the eunuch's road |
| Line | Typikon: a house rule passing land to adopted daughters | Sworn sisters and fostered daughters of the hall | Adopted heirs placed in office; temple and burial societies hold property against crown confiscation |
| World | Refuge, intake, church politics, Aristotelian vs Galenic council fight | Outlawry, landless war-band play, raiding, níð insult duels | Palace faction against the scholar-officials inside celestial / meritocratic government |
| Skills | Learning, stewardship | Martial, prowess | Intrigue, stewardship |
| Era arc | Eunuch power peaks 867, decays from 1057 and after 1081 | Tolerated while pagan, outlawed as Christianity arrives | Tang open (women a third of Daoist clergy); Song daughters inherit but women fall to 3–4% of clergy; Yuan confiscates heirless estates (1264) and bars women's suits; Ming forces lineage adoption (1369) and bars women of childbearing age from orders |

### Decisions (user, 2026-10-18)
1. **Bæddel, seiðr and ergi are one faith** for now. Name to be chosen; *bæddel* is the attested Old English word.
2. **Chinese gate, grounded in Chiang (ed.), *Transgender China* (2012)** (`research/east_transgender_china.md`):
   - Chiang argues that reading eunuchs as a "third sex", and China as a "castrated civilization", is a construction of 1870s-1930s Western observers (ch. 2), and warns against universalising "transgender" onto eunuchs (ch. 1). Stryker's afterword frames the field as de/colonising.
   - Exporting Dorleyism's "the cut are women" to China would repeat exactly that projection. So the Chinese faith's founding polemic is **"we are not eunuchs"**: womanhood comes by rite, name and recognition, not by the cut.
   - The rite inverts *neidan*: the adept gestates her own body for ten months and is born from it (ch. 3, pp. 84-86; Laozi's self-birth, p. 84). This maps directly onto re-embodiment.
   - Hostile vocabulary the faith defines itself against: *renyao* 人妖 (portent in period, a slur today, ch. 5); the Dongfang Bubai trope of self-castration plus feminisation plus occult power (ch. 7).
   - Remaining open question, kept for the faith's own schism: do eunuchs who seek the faith count as sisters? Recognition-by-rite says yes if they choose it; the faith never assumes it.
   - Outside the book and to verify before use: legal gender change in the PRC is gated on surgery, which gives the alchemical (non-surgical) gate a modern resonance.
3. **Three faiths is enough.** Southeast Asian bissu/baylan material waits for its own branch.
4. **Shared vs separate** as in the table above.

### Revisions after Bhatt's "The Third Sex" (approved by user 2026-10-18, applied)
See `research/book_bhatt_third_sex.md` §2. In short:
1. **Compromise (user):** Dorleyism stays nostalgic, but for a mostly forgotten sect, the Mother's gallae at Pessinus (inside c_phrygia), not for the Byzantine court. The Sisters remember Pessinus kinder than it was, and the eldest know it. They refuse the court's eunuch-angel "reverence" and its slave market as one system; the cut are women, not a third thing.
2. The Galenic splinter is written as the accommodationist wing, not a neutral alternative.
3. The Jade Embryo's polemic aims at the palace's classification, not at eunuchs; eunuchs who seek womanhood are sisters.
4. Alms flavoured as mutual aid, not outsider "reverence".
5. Candidate mechanic: refuges and arrivals also take in barren and widowed women discarded by the reproductive order.

### Revisions after Serano, Raha & van der Drift, and Sanders (approved by user 2026-10-18, applied)
Notes: `research/book_serano_whipping_girl.md`, `research/book_raha_vdd_trans_femme_futures.md`, `research/hist_sanders_khuntha.md`.
1. **Gates recognise, they do not test (Serano).** The embryo trials no longer punish `impatient` or `gluttonous` or let her buy her way through; the danger is outside her (a palace censor's eunuch register in month three, a summons home in month six). A failed trial delays the gestation and never resets it (`tm_embryo_delayed_effect`); she may set the work down by choice. The guarantor vouches for the house that shelters her, not for her sincerity. The seiðr trance loses its `craven` malus (ergi and cowardice were one slur).
2. **Recognition is separate from the body.** `tm_declare_decision` (Declare Before Witnesses) gives a daughter's name and `tm_declared` before any gate; the gate then keeps that name. Arrivals and refuge children come already named: she says what she is.
3. **Houses belong to the county, not the family (Raha & van der Drift).** `tm_found_house_decision` replaces the house-variable refuge. A House has an Elder Sister chosen by the sisters for five years, strain (too few hands, war levies), a burnout event, a "let them tend you" event, and splits into a daughter House at strain 6. A later lord of another faith chooses to let it stand or close it; closing sends the residents to another House or the roads (`tm_send_on_effect`), never deletes them. Turned-away arrivals are sent on the same way. Old saves migrate the house variable to the capital county.
4. **Houses are not separatist.** Cis women of the faith are sisters (`tm_house_member_trigger`); men of the faith can join as friends of the House (`tm_arrival.0004`, `tm_house_friend_modifier`). Clergy stay female-only.
5. **The Sisters Choose** (`tm_sisters_elective_succession_law`): an elective law for the Sisters' faiths. Adoption stays the succession engine; electors are the ruler, same-faith vassals and same-faith clergy; candidates are children (born or adopted), women of the faith on the council, and same-faith vassals.
6. **The Dorley path stays ungated (user).** Aunt Bea's House holds that every woman it makes is a woman: Greaves's thesis that gender intensity is a spectrum and most "succeed" at womanhood without having called themselves trans. The House's text admits it keeps cells learned from Grandmother's. This stands in explicit tension with the Gift Alone ("a gift you cannot refuse is not a gift"), which is now the strongest long-run doctrine (piety, same-faith opinion, arrivals). Grandmother's House calls its cut **eunuchs**: unmanning them while they stayed men in their own minds was the point.
7. **Femininity (Serano vs Bhatt):** middle path. `tm_seidr.0003` gains a fourth answer to *ergi*: seiðr is women's art and she is a woman who does it, beside answering with steel.
8. **Kept as is:** the §11 achievement events stay as dark comedy (user). No Islamic branch rests on khuntha law. Spring the Cell (a non-war rescue scheme) is approved and staged with the Bæddel stage-2 work (TODO.md).

### Revisions after the Norse reading (approved by user 2026-10-18, applied)
Notes: `research/norse_*.md`, `research/oe_fulk_jurasinski_canons_theodore.md`, `research/medtrans_*.md`; reading list `research/norse_reading_list.md`.
1. **Law corrected.** Grágás outlaws whoever calls a man *ragr*, *stroðinn* or *sorðinn*; the man named may kill the speaker. Being *argr* was never outlawed. Faith text, `tm_seidr.0003` and the README now say so.
2. **The völva goes into trance, not the seeker** (Eiríks saga ch. 4; Price; Gardeła et al.). The gate is a three-part chain like a wedding: the völva comes (high seat of honour, feast), the warding songs (a singer who knows the *varðlokkur*, or a reluctant woman who learned them as a girl, or humming), and the platform. Odds come from the feast, the song and the völva's learning, not the seeker's character. Failure is the song's, not hers. A travelling völva visits on the winter road (`tm_seidr.0020`). The songs pass from foster-mother to foster-daughter: `tm_teach_vardlokkur_interaction`.
3. **Name: Bædling** (user). *Bædling* is the word of the Old English Canons of Theodore (five times); *bæddel* only glosses *Hermafroditus*. Display strings only; `tm_baeddel*` keys unchanged.
4. **Devil: Níðhöggr** (user), the malice-striker of Völuspá, instead of vanilla Loki, whose shape-changing and child-bearing would cast the faith's devil as the gender-crosser.
5. **Ergi answers:** a fifth, "That word is for men" (*argr* is said only of men: Meulengracht Sørensen p. 18). Naming adds a name fastened with a gift and the woman's form of a Norse man's name (`tm_feminise_name_effect`), also at Declare Before Witnesses.
6. **Corrections:** Saxo's Uppsala passage names effeminate mimes and bells, no priests or dress; Alvild's crew had men; Grágás has no adoption (*ættleiðing*) law, so Take as Daughter's precedents are *arfsal* and fostering; northern castration was a punishment, not absent.
7. **Rules adopted:** faiths may claim historical figures in their own voice, the narrator never does; no suicide content; a daughter's courage is never "manly"; Þrymskviða and Saxo's Óðinn-as-Wecha are never precedents (the latter is a rape and is named and rejected).
8. **Stage 2 inputs** (TODO.md): insult duel structure, feud ledger and compensation, outlawry tiers and reprieve, the dress clause, holy-site lore, Eleanor Rykener event, female-king titles, `secret_tm_sister`.

### Revisions after the Byzantine reading (approved by user 2026-10-18, applied)
Notes: `research/byz_*.md`, `research/isl_*.md`; reading list `research/byzantium_reading_list.md`.
1. **Corrections.** The decline runs from 1057 and the Komnenian turn of 1081, not 1066; Leo VI's Novel 60 was never withdrawn. "The court calls its eunuchs angels" is the Sisters' polemic (the image began in 7th-century saints' Lives), not the narrator's. *Gallae* is outsiders' poetry (Catullus 63, a Hellenistic fragment); narrator text says galli. Pessinus was run by hereditary priests titled Attis, not a eunuch house. Anatolian galli dressed as women but their inscriptions are masculine; only Syrian texts call castrates women. Aunt Bea's House claims no Byzantine precedent (Byzantium rarely castrated as punishment). Rowson dates Sulayman's order 717.
2. **Galenic splinter = the rite that agrees with the Emperor** (Leo VI, Novel 98: men, women, eunuchs). Both labels checked: Aristotle has castrates "change into the female condition" (GA 784a, 787b); Galen leaves "neither female nor male, but some third thing" (K IV 585). Galen quotes in the notes are our own renderings of Kühn's Greek; check against De Lacy before publishing them.
3. **No House cuts a child** (Byzantium honoured cutting boys of 7–14). **Exception (user): Grandmother's House**, which cut boys as the court's merchants did.
4. **Two-day rite:** Day of Blood (24 March, blood and mourning) then the Hilaria (knife, question, name): `tm_knife.0001` → `tm_knife.0004`.
5. **Court offices** for Dorleyite dukes and above: Parakoimomene, Protovestiaria, Papias (daughters of the knife and eunuchs), Praiposita (any woman or daughter). `common/court_positions/types/tm_court_positions.txt`.
6. **Montanism as ancestry, in the faith's voice:** Pessinus → Pepouza → Dorylaion. Ruined Pepouza replaces Antioch as a holy site (`tm_pepouza`, c_lydia/b_sebaste). Up to seven Companions of the Mother of Mothers (`tm_name_companion_interaction`). "Cybele in Christian clothes" (`tm_byz.0001`) with an answer per wing. Suppression ladder under a lord of another Christian faith (`tm_byz.0010–0012`): books, assemblies, wills; faster after 1081.
7. **Protectress and lot** (user: "mirrors the college of cardinals"): a House Protectress from the founder's female line, else elected from the holder's house (`tm_house_name_protectress_effect`); she sways a new lord against closing the House. The Elder Sister is drawn by lot from three nominees. **Fostering** separated from full-heir adoption (`tm_foster_daughter_interaction`; Take as Daughter half price for a foster-daughter).
8. **Islamic neighbours:** daughters carry `tm_islamic_daughter_opinion` (−10) with Islamic observers; `tm_isl.0001` (the khasi of the household) and `tm_isl.0002` (laughed at in the hall). Court cross-dressing is presented as entertainment for the powerful, never tolerance.
9. **Staged for later** (TODO.md): Liudprand's four boys (949) as a rescue-and-adopt event; Ignatios returning as patriarch (867); the Tarsus boy-train; the Emperor halting at Dorylaion (Opsikion); the Steward at the Gate; Psellos c. 1066; the Athos ban (1083); an Abbasid event pack.

### Revisions after the China reading (approved by user 2026-10-18, applied)
Notes: `research/cn_*.md`; reading list `research/china_reading_list.md`.
1. **Corrections.** No link between Empress Wu and Cave 331 (Zhang, Chen, Rothschild; the claim is Burton-Rose 2012 alone); the dragon girl becomes a man. The embryo is born *from* the adept and becomes her true self. "Red dragon" is a later term (1310; the regimen is Qing); month 6 is the White Tiger. No menstruation as the mark of womanhood. Month 3's threat is the clergy roll (unregistered "private" nun), not a eunuch register. Temple Societies rests on Song daughters' inheritance (*hu jue*), dues, a lending store and name-panels, not goods in common or confiscation of a servant's estate. The narrator never calls Tang eunuchs quasi-women. The era arc is Tang open → Song (daughters inherit; women's clergy collapses) → Yuan confiscation → Ming lineage law.
2. **Gate texts** use period terms (the embryo forms; two bathings; complete in ten months, 1075; birth from the crown). New options at month 6 (Xue Xuantong's "Not yet!"; nursing parents first). New `tm_embryo.0013` "ghost fetus" physician event.
3. **Precedents** in the faith's voice: Lord Lao in Mother Li's womb (*Santian neijie jing*); the alchemists' "state of pregnancy". Wu's *Great Cloud*, the abbess of Mo-shan and Lotus ch. 13 for palace and Buddhist material.
4. **High god:** the Queen Mother of the West ("Metal Mother"). The Way keeps `doctrine_no_head`.
5. **Holy sites:** Wudang replaced by the Southern Marchmount (`tm_nanyue`, c_hengzhou); Mogao's effect text grounded in the 758 ordinations.
6. **Temple Societies mechanics:** dues at births (`tm_embryo.0012`) and deaths (`tm_on_death` → `tm_yutai.0040`); the righteous store (`tm_righteous_store_decision`, repaid in `tm_yutai.0030`); the name-panel (`tm_name_panel_decision`) protecting Houses from `tm_yutai.0010` confiscation waves (rarer before 1264) and from closure.
7. **Omens and neighbours:** `tm_yutai.0001` "A Prodigy in the Prefecture"; `tm_ordain_by_edict_interaction` (kings and up; the 1124 bearded woman); `tm_eastern_daughter_opinion` (−10) from Buddhist, Hindu and Jain observers.
8. **Start and characters:** `tm_relight_shenquan_decision` at Shazhou; `tm_yutai.0020` Huang Lingwei's rescript (882). Staged for later: Xue Xuantong, Wang Fengxian and the abbess of Mo-shan as event chains; the palace faction (Shence commanders, Commissioners of Military Affairs, Yang Fugong; Liao Empress Chengtian; three routes into the abbeys).
