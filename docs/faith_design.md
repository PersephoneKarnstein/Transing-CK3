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
- The mirror is also in (user, 2026-10-14): the Sisters get a **"Rescue the Daughters" casus belli** against a realm holding characters with the *Marked by the Mother* trait (or a daughter of the knife) who are imprisoned, hostaged or otherwise held. Victory frees and transfers them to the attacker's court for adoption. Scope it like a vanilla claim or holy war on a single county or duchy, gated on the knife doctrine not being Grandmother's House. Period framing: the Byzantine–Arab prisoner exchanges on the Cilician frontier, in which eunuch envoys negotiated ransoms (Ayalon), and the Church's own "liberation of captives" casus. **Widened (user, 2026-10-21):** captives alone were too rare for the war ever to be declared, and most members are not daughters. It now also targets a neighbouring county where two or more daughters, novices or Marked women of the attacker's faith live under a lord of another faith; they come to the attacker's court on victory. Daughters cluster at a few courts, so it does not become a free war.

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
| 6 | Culture name | **Kybeline**; **faith name: Adelphai Dorleyaiou** (the mod is *Crusader Dolls*, renamed 2026-10-20; the repo *Transing-CK3*) (`kybeline` culture key); *bæddel* reserved for the Norse branch | Recommendation adopted by default. |

## Deferred research (not blocking the build)

- **Ayalon, *Eunuchs, Caliphs and Sultans* (1999)** — PDF received 2026-10-14, converted to `docs/research/sources_pending/ayalon_eunuchs_caliphs_sultans.txt`, not yet read. Target: al-Jahiz's statement on eunuchs' transfer to the female realm, in context, for flavour text.
- **East and Southeast Asia.** CK3 1.20 includes China, Korea, Japan and Southeast Asia. Needed before the faith is given Asian branches or hostile-faith text there: Chinese court eunuchs (Tang–Yuan; Tsai, *The Eunuchs in the Ming Dynasty* for the later end), Mongol/Khanate attitudes to castration and gender variance, Korean *naesi*, Japanese absence of eunuchs, Southeast Asian *bissu*, *baylan* and *kathoey*-adjacent roles (Wiesner-Hanks touched bissu and baylan only briefly). Also the Mongol *Yassa* on sexual offences.
- **Kerala Nair matriliny and Tuareg descent** for on-map matrilineal precedents (G verdict g).

## 12. Branch faiths: distinct playstyles (planning, 2026-10-18)

Three faiths, no more for now. Each answers three questions differently: how one becomes a daughter (the gate), how the line continues, and how the faith meets a hostile world. Shared across all three: the Marked trait, re-embodiment, Take as Daughter. Everything else is per-faith.

| | Adelphai Dorleyaiou (Byzantine, built) | Bæddel faith (Norse and Anglo-Saxon) | Chinese faith |
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
   - Exporting Adelphai Dorleyaiou's "the cut are women" to China would repeat exactly that projection. So the Chinese faith's founding polemic is **"we are not eunuchs"**: womanhood comes by rite, name and recognition, not by the cut.
   - The rite inverts *neidan*: the adept gestates her own body for ten months and is born from it (ch. 3, pp. 84-86; Laozi's self-birth, p. 84). This maps directly onto re-embodiment.
   - Hostile vocabulary the faith defines itself against: *renyao* 人妖 (portent in period, a slur today, ch. 5); the Dongfang Bubai trope of self-castration plus feminisation plus occult power (ch. 7).
   - Remaining open question, kept for the faith's own schism: do eunuchs who seek the faith count as sisters? Recognition-by-rite says yes if they choose it; the faith never assumes it.
   - Outside the book and to verify before use: legal gender change in the PRC is gated on surgery, which gives the alchemical (non-surgical) gate a modern resonance.
3. **Three faiths is enough.** Southeast Asian bissu/baylan material waits for its own branch.
4. **Shared vs separate** as in the table above.

### Revisions after Bhatt's "The Third Sex" (approved by user 2026-10-18, applied)
See `research/book_bhatt_third_sex.md` §2. In short:
1. **Compromise (user):** Adelphai Dorleyaiou stays nostalgic, but for a mostly forgotten sect, the Mother's gallae at Pessinus (inside c_phrygia), not for the Byzantine court. The Sisters remember Pessinus kinder than it was, and the eldest know it. They refuse the court's eunuch-angel "reverence" and its slave market as one system; the cut are women, not a third thing.
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
7. **Omens and neighbours:** `tm_yutai.0001` "A Prodigy in the Prefecture"; `tm_ordain_by_edict_interaction` (kings and up; the 1124 bearded woman); `tm_eastern_daughter_opinion` (−5) from Buddhist, Hindu and Jain observers.
8. **Start and characters:** `tm_relight_shenquan_decision` at Shazhou; `tm_yutai.0020` Huang Lingwei's rescript (882). Staged for later: Xue Xuantong, Wang Fengxian and the abbess of Mo-shan as event chains; the palace faction (Shence commanders, Commissioners of Military Affairs, Yang Fugong; Liao Empress Chengtian; three routes into the abbeys).

### Revisions after the second Norse reading (approved by user 2026-10-18, applied)
Notes: `research/norse_jochens_*.md`, `norse_mitchell_witchcraft_magic.md`, `norse_damico_wealhtheow_valkyrie.md`, `norse_evans_hancock_masculinities.md`, `norse_tolley_shamanism.md`, `norse_solli_queering_cosmology.md`, `oe_sayers_baedling_etymology.md`.
1. **Name wording:** *bædling* is a word of uncertain meaning the Canons set apart from "other men" (Sayers "sodomite"; DOE and Fulk & Jurasinski query "homosexual"); the faith's text no longer glosses it "effeminate man". Nothing supports "bad" from *bæddel*.
2. **The shout is *ragr*,** and the retort "*Ragr* is said of men": *ergi* was also hurled at women (Solli; Mitchell). No narrator text says the word was never used of women.
3. **The rite in the faith's voice.** Tolley: the *Eiríks saga* scene is "almost wholly unreliable", but a light trance on a platform and the warding songs (which keep the völva) survive. Lines now say "the song held" and "I did not make her. I saw her." (Jochens: the völva uncovers fate).
4. **"Óðinn's host has no men" is the faith's polemic** against the skalds' Valhöll of dead men (the einherjar). Seiðr is Freyja's art.
5. **The winter-road völva** no longer cites Þorbjörg (set c. 1000). She goes everywhere, Iceland included: the sources' silence on living Icelandic völur (Jochens) is an absence of evidence, not a ban, and a Bædling realm is not saga Iceland.
6. **Stage 2 inputs:** sorcery law in three stages (royal examples at conversion; church outlawry c. 1100–1300; death penalty Norway c. 1300, Sweden c. 1350; trials rare); "Six Housewives" compurgation; Pour the Cup (end a flyting, first cup, the inheritance toast); women's suits through a friend of the House; dress clause only with a powerful prosecutor; "They Say He Keeps Seiðmenn"; "Weave the Warding Shirt"; *sigewif* for the war-band; English reaction text (Wulfstan 1014: valkyries among witches).

## 13. Ha-Nehpakhot, the Jewish sect (approved by user 2026-10-19, built)

Grounded in `research/jud_*.md` (Strassfeld 2013, Kalonymus's *Even Boḥan*, the rabbinic primary texts, Neis 2023, Grabowski 2015, Phelan 2023) and the "Medieval Judaism" section of `research/comparanda_reading_list.md`.

**Decisions (user, 2026-10-19).**
1. **Era.** Present at every start, as the other faiths are. Content that quotes Kalonymus (the *Touchstone* variant of the prayer, the elders' *Touchstone* answer) waits for 1322.
2. **The body.** The Turning ends like the other gates: the daughter trait and, under the game rule, re-embodiment. Told in the faith's voice as heaven's turning, "as Dinah was".
3. **Other daughters.** Daughters of every gate are sisters; the knife is refused as this faith's own gate (as for the Bædlings).
4. **Text.** Every quotation is rendered afresh from the public-domain Hebrew; the CC-licensed English translations are reading aids only.
5. **Rescue the Daughters** is *not* barred from Jewish targets. Its text never calls anyone a slaver, so a bar would be an overcorrection.
6. **No head of faith**, as in vanilla Judaism. The ḥevrah's offices wait for a source.
7. **README** says why the slave-trade motif is excluded (Phelan).

**How it plays differently** (user: "we do want each faith to play differently").

| | Bædling (seiðr) | Ha-Nehpakhot (the Turning) |
|---|---|---|
| When | Any time; cooldown a year | Adar only (February–March); one Purim a year |
| What decides it | The warding songs, the feast, the völva's learning | Her own learning and the elder's; patience (+10 per unanswered Adar, never reset); the gallery and the kept dress; the county's licence and the ḥevrah's street |
| Who keeps it | A völva, at court or on the winter road | An elder of the ḥevrah, at court or from the Jewish street |
| Afterwards | Before the thing: an insult duel | Before the elders: a learned dispute that licenses the county for ten years, or *niddui* (shunning) for three |
| The line | Fostering, the songs taught to a ward | The three lamps; the prayer taught to a Marked courtier (+15) |
| The world | Martial: raids, warrior clergy | Landless and learned: a lord of any faith may commission a translation and protect her people; Jewish lords are asked to rule on daughters |
| Conversion | — | A seeker of another Jewish faith who is turned joins the sect |

**Built.**
- `tm_nehpakhot` (faith in `judaism_religion`), `tm_nehpakhot_rite` (tenets: The Turning, The Three Lamps, vanilla Legalism; gender equal, clergy of either sex).
- Holy sites: `tm_arles` (seat, `b_arles`), `jerusalem`, `tm_narbonne`, `tm_montpellier`, `hamadan`. Hebron sits in Jerusalem's county, so it is not a separate site.
- Trait `tm_daughter_of_the_turning` (learning, diplomacy; not a eunuch equivalent).
- Opinion: every daughter trait now carries `tm_jewish_daughter_opinion` (−10, Jewish observers: "what came forth male is male") and `tm_turned_sister_opinion` (+10 for the sect, cancelling it).
- Decision `tm_turning_decision`; events `tm_hipukh.0010 → 0011 → 0001 → 0002 → 0003`; yearly `tm_hipukh.0020` (the three lamps), `0030` (a translation), `0040` (a Jewish lord's ruling).
- Seed: the variable `tm_kahal` on `c_venaissin`; an elder daughter of the Turning and two Marked young men of the sect in Arles, unlanded.

**Hard limits.** No knife and no potion (Issurei Bi'ah 16:12). No lashes on screen. No "until I expire" line. No hyena or other animal imagery (a Christian slur). No "a created being of its own" as the sect's self-description; the faith refuses it as a compromise. No Jewish slave or eunuch traders; no Khazar seat. Christian hostile text attacks doctrine, never Jews as a people, and never ties Jewish "inconstancy" to intersex bodies (Wingard on DeVun). The narrator never says the Talmud recognised six genders, or that Kalonymus was a trans woman. Added after the second reading (`research/cmp_devun_shape_of_sex.md`, `jud_strassfeld_trans_talmud.md`, `jud_fonrobert_sexed_body.md`): no Christian "turning" puns (turncoat, "will turn again"); no "neither" or *neutericum* slurs against the lords who protect them; no beast or demon imagery for Jews at all; never voice b. Nazir 59a's "slip in among women" rationale; never name the modern book titled after Deut. 32:20's *dor tahapukhot*.

**Open.**
- A source for Provençal Jewish women's names (Iancu; Shatzmiller). Until then the naming list is biblical.
- *Trans Talmud* (2022), for the *aylonit* chapter.
- Community roles (quorum, witness, confraternity offices) need the medieval codes.
- The Turning is open to Marked seekers of every Jewish faith (Rabbinic, Karaite and the rest). Karaite law differs from rabbinic law on Purim and on the Talmud's authority, so a Karaite seeker may need her own text.

### Revisions after the second Judaism and comparanda reading (approved by user 2026-10-19, applied)
1. *Touchstone* prayer line: "The learned call it a jest; the ḥevrah says he meant it." No source ties the lament to Purim; the Purim parody is *Massekhet Purim*, written in Rome (Rosen).
2. *Even Boḥan* was written in Catalonia; Arles is Kalonymus's birthplace (Rosen). README corrected.
3. `tm_isl.0002`: the jester is "a shaven man in women's finery"; no source has a veil (Rowson 2008; William of Adam; Leo).
4. Jaunpur: Jackson confirms the adopted-heir succession but calls neither Malik Sarwar nor Khusraw Khan a eunuch, and Sarwar never took the title of sultan.
5. Names, option (b): "A name from the scroll and the Torah" (Dinah, Esther, Sara; `tm_turning_scroll_name_effect`) and "A name of the street" (Rosa, Mairona, Bella, Regina, Blanca, Gratiosa, Bonadonna, Comtessa, Mandina, Benvenguda, Bonahora, Astes, Roseta; `tm_give_daughter_name_effect`), from Shatzmiller.
6. *Niddui* needs the lord's licence (Shatzmiller pp. 87, 89): `tm_turning_niddui_effect` lets a county lord who protects her people (`tm_translation_patron_modifier`) refuse it.
7. The women's blessing "who made me a woman" (a 15th-c. Judeo-Provençal prayer book, Rosen citing Tabory) in `tm_hipukh.0002`.
8. Hard limits extended (above).
9. Eastern opinion split by gate: `tm_eastern_knife_opinion` (−15, a castrated man to Buddhist, Hindu and Jain law) on the knife's daughter; `tm_eastern_daughter_opinion` (−5, "A Man Become a Woman") on the others.
10. `tm_byz.0012` (The Wills) fires only under a liege of Byzantine heritage; Slavic princes left sexual morality to the church (Levin).

### Revisions after the third Judaism reading (approved by user 2026-10-19, applied)
Sources: `research/jud_hildenfinger_arles_documents.md`, `jud_stouff_gross_arles.md`, `jud_benshalom_provence_languedoc.md`, `jud_grossman_pious_rebellious.md`, `jud_women_synagogue_articles.md`, `jud_kahn_three_blessings.md`, `jud_assis_catalonia_sexuality.md`, `jud_horowitz_reckless_rites.md`, `jud_davidson_renan_kalonymus.md`, `jud_shatzmiller_medicine.md`, `jud_male_menses_myth.md`.

**Corrections.**
1. The Revel: "the rabbis grumble and let it pass". Rabbinic permission for Purim dress is 16th-century (Minz, Isserles); Horowitz calls the custom "technically an infringement".
2. The women's gallery becomes the women's synagogue, the room below the men's (Arles deed of 1452, REJ 48: 75–76). Variable `tm_turning_gallery` renamed `tm_turning_women_synagogue`.
3. Holy-site text: the *nasi* of Narbonne held land outright, under no lord (Ben-Shalom); the translators' country runs from Lunel to Montpellier.
4. The *Touchstone* gate moves to 1323.1.1 (*Even Boḥan* is dated Tevet 5083, winter 1322–23).
5. README: the blessing "who made me a woman" is written down only after 1453 (Leeds MS Roth 32; Farissol 1478, 1480); its age is the faith's claim. Kalonymus worked at Arles (1307–17, 1328), not only was born there. Gilgul into a woman is 13th-century Castilian (Sachs-Shmueli), not only Lurianic; character voice only.
6. Hard limits, added: none of the medieval "Jewish male menses" tropes (`research/jud_male_menses_myth.md` lists 18), and no "blood" in Three Lamps text; no Christian Purim-violence accusations, no Haman on a cross, no Haman burned in effigy, no "Purim cakes" (a blood-libel motif); no Byzantine converts' oath (8th–11th c.); the Manosque 1306 Purim dress exists only inside a Christian accusation and is not used. The sect's era stays as built (user); the French expulsion of 1306 is not modelled, since the base game models no expulsions (user: "we're adding a transfeminism expansion").

**Design.**
7. The Revel before 1323 is unattested: a dated variant (`tm_hipukh.0011.desc_early`) has her alone in the dress, and "laugh with the others" appears only from 1323.
8. No medieval women-only confraternity is attested, and the Arles *holim* of 1401 was 18 men. The sect is **the women of the lamp**: women householders who sit together in the women's synagogue and keep the synagogue's lamp alms (Stouff's *aumône du luminaire*). Player text no longer says *ḥevrah*.
9. The elders become **the baylons and the council** (`tm_hipukh.0003`, "Before the Baylons"). From 1401, in a county with `tm_kahal`, the council includes women (Arles, Oct. 1401: five women called, "what touches all must be approved by all"; 1407: Estes de Cailario and Regina sat): a desc variant and +10 to win.
10. Names: Venguessona, Dulcia, Bonafilia, Astruga join the street list; Estes (the Arles form of Esther) joins the scroll list. Name keys added to loc for every street name missing from vanilla (Tiger flagged nine that the previous commit lacked).
11. The Three Lamps for a daughter whose days do not come: she keeps them "as the *zekenah* keeps them", the old woman past them (m. Niddah 1:3–5, *unverified*).
12. A physician variant, `tm_hipukh.0031` "A Fisica at Court", beside the translation (women physicians are well attested, women translators are not): licence her (`tm_fisica_licensed_modifier`), licence her for women only (`tm_fisica_women_modifier`), or refuse.
13. In Provence (Occitan culture) the naming text gives the women's blessing as *qui fis me fenna* (Baricci 2023 p. 66; *unverified* against the manuscript).

## 14. Growth: why the faiths died out, and the engine (approved by user 2026-10-19, built, untested)

**The observe run.** 867 to 986 (119 years), all DLC. At 986.1.1 of 44,585 living characters: Adelphai Dorleyaiou 16 (2 rulers, 0 counties), Bædling 20 (1 ruler; 4 counties in Livonia, Dorpat, Pinsk and Kletsk), the Jade Embryo 44 (1 ruler; Shazhou), Ha-Nehpakhot 1. Daughters who ever rose: 11 of the knife, 7 of seiðr, 1 of the embryo, 0 of the Turning. The save showed the rite doctrines applied correctly; the faith-level doctrine lists are engine defaults.

**Causes.**
1. Nothing drew anyone in: the AI converts only to its liege's faith, and Marked characters of other faiths had no pull toward ours.
2. Only rulers could start a rite (the AI weighs decisions for rulers), and nearly every Marked character and daughter is a courtier.
3. No *Take as Daughter* in the whole save: a daughter who rules is infertile, so her titles left the faith at her death.
4. Phrygia was revoked by Byzantium's administrative appointments and given to an Orthodox governor; Gotland was revoked and conquered.
5. Ha-Nehpakhot's unlanded seed in the pool dwindled to one.

**The engine** (`common/scripted_effects/tm_growth_effects.txt`, `tm_yearly_growth` on `yearly_global_pulse`).
- **The call** (revised after the third run, below). Each year every adult Marked character of another faith may join one of the six.
- **The rite offered to courtiers.** Each year a Marked man, eunuch or declared sister of the four who is not a ruler has an 8% chance (25% if Marked, +10 if declared) to begin the faith's own chain; then not again for three years. The Turning waits for Adar (`tm_hipukh.0009`).
- **Adoption.** *Take as Daughter*: the AI now weighs it every year, targets family too, and wants it (+70) whenever it has no living child of its own faith, +30 more if it is a daughter.
- **Seats** (Gotland, Kanchipuram and Kirina revised after the third run, below). The Mother of Mothers rules as a theocracy (untested whether this keeps Phrygia out of the Byzantine appointments); if Phrygia leaves the faith, the Mother House holder gets a pressed claim. Each seat court starts with two Marked young men; the Arles sect is employed at the count of Venaissin's court instead of left in the pool.
- **Not done:** conversion resistance for House counties. The engine has no such county modifier; vanilla's chaplain formula checks named modifiers only, so it would need a vanilla override.
- **Tuning.** Every 10 years `tm_census_log_effect` (`tm_tracking_effects.txt`, generated by `tools/gen_tracking.py`) keeps a census on each faith by decade, with running totals of joins, kahal joins, rites offered, daughters raised and deaths (`tm_track_effect`). Seeds are kept on global lists per seat (`tm_seeds_<seat>`, `tm_seeds_dead`), and each foothold seat county records its branch (`tm_seat_branch`). `tools/census_report.py` prints all of it from one save. `debug_log` never reached any log file in this setup, even with `-debug_mode`, so it is no longer used. Rates are first guesses: expect to tune them after one or two observe runs.

**The second observe run** (867 to 1023, six faiths, the engine above). No census lines reached `debug.log`, since `debug_log` writes only in debug mode; the counts below are from the 1023.1.1 autosave. Of 43,922 living characters: the Bædlings 1,204 (114 counties; their rulers hold the empire of Scandinavia and the kingdoms of Sweden, Denmark, Norway, Finland, Sápmi and Bjarmaland), Badenya 851 (48 counties; its rulers hold Mali, Songhay, Ghana, Kanem, Hausaland and eight other kingdoms), the Jade Embryo 150, Ha-Nehpakhot 102 (12 counties, the duchy of Gurgan), Adelphai Dorleyaiou 54 (no counties: Phrygia lost again), the Worn Garland 35 (4 counties). Daughters: 311 of seiðr, 33 of the House, 11 of the embryo, 10 of the Turning, 7 of the knife, 5 of the Garland.

**Why the two booms.** Not the call: both followed a ruler the start converted. Gotland's count (Steinn, then Vagn) passed the faith to Alf, who created Sweden in 900 and Scandinavia in 914; every holder of Sweden since has been Bædling. The lord of Kirina's line took Mali in 967 (Tenenbajan, a daughter of the House) and went on from there. A converted ruler in a region where vanilla realms grow fast is a dice roll the faith can win outright. **Fix (approved by user 2026-10-19):** Gotland and Kirina now start as Kanchipuram does, the county and the court of the faith and the lord not. Still open: Adelphai Dorleyaiou keeps dying (Phrygia), and seiðr makes daughters faster than any other gate.

**A bug the second run hid.** The call saved its target with `save_scope_value_as` inside the yearly loop over every character and never cleared it. Once one character in a region set a target, every Marked character the loop reached afterwards kept it, wherever they lived. That probably explains the 102 Ha-Nehpakhot holding 12 counties and the duchy of Gurgan, and some of the North's volume. Fixed with `clear_saved_scope`.

**The third observe run** (867 to 1060, minority starts at Gotland and Kirina). The 1042 census in the save: Jade Embryo 245, Badenya 29, Adelphai Dorleyaiou 21, the Worn Garland 17, Bædling 11, Ha-Nehpakhot 0 (extinct). At 1060.1.1: Jade Embryo 233 (4 counties; its lords hold 5 counties and a duchy, a stable seat at Shazhou), Adelphai Dorleyaiou 26 (no counties), Badenya 22, Bædling 19, the Worn Garland 9; 23 daughters, 243 Marked alive in the world. Without a landed member the lord's chaplain converts the seat county back, and the call is the only intake.

**Revision (approved by user 2026-10-19).** The user rejected scaling the call by faith size ("transparently anti-collapse/anti-bloom"; a larger faith should draw more, being known to more). Instead:
- **The call travels by contact.** Which faith: one met at court first, else Jewish faiths to Ha-Nehpakhot, else by region (Asia Minor and the Balkans to Adelphai Dorleyaiou; the North, Britain and the eastern Baltic to the Bædlings; China and the Tarim to the Jade Embryo; the Deccan to the Worn Garland; West Africa to Badenya). Chance: 1% as a rumour; +8 with a member at her court or as her lord, +4 more with three or more; +4 with a member living in her county at another court; +4 if the faith holds a county in her realm; +5 for a House in her county; +3 for a holy site of the faith in her duchy; +3 for a daughter of any faith at court; +4 if declared. A count ×0.25; a duke or above ×0.05, and their vassals take *Turned Faith on a Courtier's Word* (−30, decaying). A larger faith reaches more people by being in more places. The ceiling is the Marked supply (about 250 alive at a time), since daughters bear no children; realm-scale booms need a ruler, and those are now rare and costly.
- **Footholds** (`tm_seed_foothold_effect`). Gotland, Kanchipuram and Kirina: if the lord holds other counties and the seat is not their capital, the county goes to a new woman of the faith (her own dynasty) as the lord's vassal, with the seat's baronies the lord held. Her own chaplain keeps the county, and a vassal count cannot march on a kingdom. Otherwise the lord keeps the county and the faith lives at their court, as before.
- **Ha-Nehpakhot renews as a community.** Arles also starts with a household of the sect at the count of Venaissin's court: a physician, his wife and three children aged 6–12, their own dynasty, each child with a parent as guardian (in the first tracked run, unguarded, all three were Christian by 901). Each year a Jewish adult at a court with two or more of the sect has a 4% chance to join it. Children born to members are born into it. **Matchmaking** (after the second tracked run, where the sect died out again by the 930s with no joins and no births; approved by user 2026-10-19): each year an unmarried, fertile adult of the sect aged 40 or under who is neither a daughter nor Marked has a 15% chance of a match with a Jewish spouse from outside the courts (`tm_kahal_match_effect`), who joins the sect and the court; a woman marries matrilineally. Counted as `matches`. Badenya also fell to 3 members after Kirina's vassal died in a siege (883); the user chose to wait for another run before treating that as systemic.
- **Third tracked run (to 1104).** Badenya fell to 1 member in the 970s and recovered to 39 by the 1000s: not systemic. Ha-Nehpakhot grew to 70 by matches alone, but with no daughters after about 900: the Marked trait is 1% at birth, too rare for one household. Adelphai Dorleyaiou lost Phrygia in the 1060s and fell to 16; the user does not mind it struggling, so long as it stays playable (open). **Pilgrimage to the kahal** (user's idea, 2026-10-20; `tm_kahal_pilgrimage_effect`): the kahal is the court with most of the sect. Each year there is a 10% chance a Marked young Jew (16–26, culture of a random Jewish character in the world) arrives there; +5 at 10 members, +5 at 20, +10 at 40, since a larger kahal is known further. The eldest woman of the sect at least 16 years older, a daughter first, adopts him; the courtier rite may then offer the Turning. Marked members and daughters of the sect living elsewhere have a 10% chance a year to come to the kahal. Both counted as `pilgrims`.
- **Fourth tracked run (to 1198).** Yutai Dao 218 members (14 rulers in the census, a queen of Lingnan, 14 counties); every other faith 2–17 members, and none but Yutai with a landed ruler. Mālai's people held 6 counties (the Himalaya and Java) under Vaishnava lords; Ha-Nehpakhot peaked at 43 members, 2 rulers and 4 counties in the 1150s and lost them by the 1170s. The difference is the start: Shazhou's holder, a duke with 8 counties, is converted; Badenya gets a vassal count; Bædling and Mālai got no ruler at all. **Revision (user, 2026-10-20):** split the difference for the two faiths hemmed in by expanding realms. Gotland's count is converted again, as Shazhou's is (the island as the faith's own; tune it if Scandinavia recurs). Mālai gets a foothold at Candragiri, a second county of Tondai Nadu, held by a woman of the faith as Nandivarman's vassal; the daughter stays at Kanchipuram's court and the two Marked young men go to hers. **The way home** (`tm_homecoming_effect`, Bædling and Mālai): Marked members, daughters and declared seekers of the faith with no court have a 20% chance a year to join the home court (the seat's holder if of the faith, else the ruler of the faith with most members at court, else the seat's lord); counted as `pilgrims`. Pool characters of ordinary members are left alone: the game makes and clears them by the hundred in a faith's counties.
- **Fifth tracked run (to 945; it crashed when new script files were added mid-run).** Gotland's converted line held the island for 80 years without expanding (Halla rules it in 945). Shazhou fell to a Confucian lord in the 900s and the Way had no rulers after, growing only by the call (13 to 36 members): Yutai Dao's lead in the fourth run was its ducal line surviving, not anything built in. The Candragiri foothold was lost to Jain lords; Mālai's people again spread overseas (Takua Pa, Salo Tai, Borneo) with no rulers. The way home brought 1–4 a decade to Bædling and Mālai. Ha-Nehpakhot fell to 3: the seed household's children died Christian and Muslim. **Cause:** an AI ruler who gives a courtier's child a guardian of his own rite picks the "convert faith" education by default (vanilla `00_education_interactions.txt`, +500 when the child's rite differs from his). **Fix (2026-10-20):** `tm_kahal_keeps_children_effect` yearly removes the `convert_faith` flag from an AI guardian of another faith on a child of the sect; a player's own choice stands.

## 15. The fifth and sixth faiths: the Worn Garland and Badenya (approved by user 2026-10-19, built, untested)

The user chose two of four southern candidates (`research/south_reading_list.md`): India and West Africa, "if we can get them to all feel unique". Shared mechanics with other faiths are fine (user: "they can share some similarities"). Neither region has a recorded pre-1453 case of a man living as a woman in a religious role: each gate is a reconstruction the narrator marks, built on institutions that are attested.

### The Worn Garland (working name), Tamil South India
Notes: `research/ind_*.md` (14). Works read: Ganguli's *Mahābhārata*; Merkle 2016; SII 2 no. 66; Orr 2000, 2013; Venkatesan 2010; Narayanan 1994; Ramanujan 1973, 1981, 1982; Doniger 1999; Goodall 2018; Anandakichenin 2020; Govindacharya 1902.
- **Family.** A current inside vanilla Hinduism that crosses Śaiva and Vaiṣṇava devotion, as the inscriptions' shared vocabulary does (Orr 2013). The bride and the worn garland come from the Vaiṣṇava poets; the "daughter of God" title, the rite and the women's song from Śiva's temples.
- **Theology, in period.** "Before God all men are women" (Ramanujan 1982, p. 324); Mahādēvi 68, Basavaṇṇa 703 ("I'll be your devotees' bride"), the 13th-c. *Ācāryahṛdayam* ("in love, a woman's words"). Scripture: Bhaṅgāśvana, who chose to stay a woman (MBh 13.12). Ilā, who asked to alternate and was cured back to manhood in every version, is the "third thing" the faith refuses (Bhatt).
- **Gate: the pāvai vow, in Mārkaḻi** (mid-December to mid-January). A month-long trial kept with companions:
  1. the waking: before dawn she wakes the girls of the street (companions at court; each week one may fall away);
  2. the song: the Śaiva *Tiruvempāvai* (which temple women paid to sing, Orr pp. 17–18, 107–08) or Āṇṭāḷ's *Tiruppāvai*; the choice tilts which holy sites favour her;
  3. the garland worn before it is offered (Āṇṭāḷ's transgression, first witnessed in a mid-10th-c. verse; Venkatesan p. 223): the risk of being caught;
  4. the dream: a sign, not the success (in the poem she wakes to find it false);
  5. the staff on the head and a name: the 12th-c. Śaiva initiation that made a temple woman a "daughter of Rudra" (Goodall pp. 110–112), at the temple, with a gift.
- **Line.** The temple street: a daughter's share (paddy and a house, as the 400 women of Tanjavur held, SII 2 no. 66), recorded in stone. Inheritance from a temple woman "may have" passed mother to daughter (Orr p. 72); adoption before 1300 is Orr's guess, so *Take as Daughter* here is a marked reconstruction.
- **World.** An endowment economy: gold buys an inscription, which buys lasting piety and a protected share; temple managers and dynastic patrons; diplomacy. Era arc: "daughter of God" (*tevanar makal*) flourishes 850–985 and fades after 1070 (Orr pp. 52, 57–59), so the faith's institutions weaken late in the game.
- **Seat.** Kanchipuram: the only temple-women centre attested through 850–1300, with Śaiva and Vaiṣṇava temples (a Pallava queen's Śiva temple of 758 had fifteen named women on its staff). Holy sites: Srirangam, Thanjavur, Madurai, and a Chidambaram-area site if the map has one.
- **Reaction.** Orthodox lines from the Ilā variants ("To hell with birth as a woman", Sahyādrikhaṇḍa); Buddhist and Jain lines already in §13 revisions.
- **Never.** No hijra link; Āṇṭāḷ venerated, never founder or a trans figure; no "bride of God" for temple women (17th c.); no courtesan or slave framing (Goodall's frame); Śrīvilliputtūr's Āṇṭāḷ temple (c. 1571) is out of period.

### Badenya, the Mother's Children (working name), Mande West Africa
Notes: `research/waf_*.md` (14). Works read: Ibn Baṭṭūṭa; Ibn Khaldūn; *Tārīkh al-Sūdān*; Brett-Smith 1994; Koné 2004; Johnson 1921; Matory 2003, 2005; van Beek 1991; Austen (ed.) 1999 (Conrad, Wilks, Camara and others); Gomez 2018; Jansen 1996, 1996, 2002, 2018; Schulz 2002; eight contemporary studies (Broqua 2010, 2017; Broqua & Larmarange 2022; Larmarange & Broqua 2023; Geoffrion 2013; Mackin 2026; Pierce 2016; Bertolt 2020).
- **Family.** Inside vanilla West African religion, overriding every god-name key: vanilla uses Griaule's Dogon names (Amma, Nummo, Yurugu), which van Beek's restudy undercuts. Mande *nyama* is usable; Dogon cosmology is not.
- **Gate: the crossing**, in three parts, with a "hot" seeker "cooled" by the authorised word (Jansen; Schulz):
  1. the smith's bargain: the djinn's price is a dependant's life; she gives her own manhood instead (Brett-Smith p. 76, a demotion in the sculptor's words that the faith reclaims; Kosiya Kante's self-substitution in the epic, Conrad pp. 206–07, in the faith's voice only). A smith and potter pair; a yearly debt to the djinn afterwards;
  2. the claiming: a woman of the faith calls her "my mother's child" and pays bracelets for her crossing; the epic's sister-guide and foster-mother are the models (Conrad p. 205);
  3. the word that cools: a jeli, man or woman, speaks her name before the mansa, with the claiming mother's name prefixed (Sun-Jata); paid well it is praise, ill-paid it is satire (Ibn Baṭṭūṭa pp. 413–414: the bird-masked bards; al-ʿUmarī's court poet).
- **Line.** Through a sister or daughter (Ghana 1063, Walata; not Mali's royal line, which is contested: `waf_ibn_khaldun_mali.md` correction). "The House buries its own": refusal of burial is the oldest exclusion in the contemporary record, so the faith's own burial is a doctrine.
- **World.** A praise and shame economy (jeli and jelimusow), smiths' dangerous power, Maliki jurists at court, hunters. Daughters run naming ceremonies and weddings and are sponsored by "mothers" in networks ranked by seniority: the contemporary pattern (Broqua; Geoffrion; Mackin), used to make the faith feel familiar and marked by the narrator as reconstruction. People in those studies say "born so", "God made us", and more choose "woman" than "transgender".
- **Festival.** A seven-yearly "New Roof" that gathers the daughters into an age-set (invented on the pattern of the Kangaba re-roofing, whose present form is 1880–1912; the Kamabolon's own rites are not used: a living, guarded sanctuary).
- **Seat.** Kirina (`c_sibi_mali`), with a refuge rock at Koulikoro (a barony there). Holy sites: Niani, Awkar (Ghana), Walata, and one more to choose.
- **Reaction.** The vanilla Orisha faith reads a daughter warmly, as an initiand (+5; Matory); Oyo-type courts are out of period (Old Oyo's datable layer is c. 1555–1610).
- **Never.** No Ṣàngó priests, 'yan daudu, góor-jigéen, woubi, sasso (or the derogatory Kwadwo Besia) or Ibbi mapped onto the faith: in the scholarship these are mostly men who act "like women" and see themselves as men (Gaudio p. 10; Otu), so Badenya borrows their social roles only, never their identity; no Griaule or Dieterlen cosmology; no Kamabolon rites; Bamana terms to be checked by a speaker.

### §15 revisions after the second southern reading (2026-10-19)
New notes: `ind_benherut_sivas_saints.md`, `ind_prentiss_embodiment.md`, `ind_pechilis_karaikkal.md`, `ind_kersenboom_nityasumangali.md`, `ind_shulman_temple_myths.md`, `ind_carman_narayanan_tamil_veda.md`, `ind_dehejia_venkatesan_antal.md`, `ind_hardy_viraha_bhakti.md`; `waf_conrad_conde_sunjata.md`, `waf_bulman_corpus.md`, `waf_gaudio_otu.md`, and additions to `waf_contemporary_gender.md`.

**The Worn Garland.**
- *Bride, in period:* *śaraṇasati liṅgapati*, "the devotee is wife, the liṅga husband" (Harihara, early 13th c.; Ben-Herut pp. 85–88); Basavaṇṇa's initiation as a temple wedding with Nandi officiating (pp. 86–87). In period the bride role is a rite, not a life; the faith claims it as a life in its own voice. The 13th-c. *Īṭu* on *Tiruvāymoḻi* 1.4: the devotee "loses his own male nature and will wear the dress of a woman" (Hardy p. 563). Hardy argues the commentators misread poems whose girl is a body, not a soul (pp. 270, 368): the faith sides with the body.
- *Precedent the faith may claim:* Kāraikkāl Ammaiyār, whose body Śiva changed at her own request and who stayed a woman, "Mother" (*Periya Purāṇam*, c. 1135, vv. 49–50). Never "disease": the faith's voice says "they thought her possessed".
- *Gate, refined:* the pāvai vow has two wakings, first the friends and then the god (Hardy pp. 416, 436, 513); the *pāvai* is a sand image of the goddess (p. 414); the *paṟai* drum is the token the girls ask for (Hardy pp. 476–478; Dehejia); a mother or friend witnesses. The final step, the staff on the head and a name, can be at court or temple (Kersenboom: the *talaikkōli* title).
- *Dates:* Āṇṭāḷ c. 850; Nammāḻvār before 900; Tirumaṅkai at Kanchi under Nandivarman II (8th c.). An Āṇṭāḷ shrine at Śrīvilliputtūr is attested by 1453/54. "God alone is male" has no dated source: do not use.
- *Line:* "married to the god" stays 17th c. (Kersenboom gives no earlier date); adoption stays a reconstruction; the *putrikā*, the appointed daughter of Brahmanical law (Pechilis & Raj p. 54), is the period precedent for a daughter as heir.
- *Map:* Kanchipuram is a vanilla holy site (`kanchipuram`, county only); Srirangam, Thanjavur and Madurai need `tm_` sites (baronies `b_srirangam`, `b_tanjavur`, `b_madurai`). Chidambaram, Tiruvālaṅkāṭu and Kāraikkāl are not on the map.
- *Excluded:* the palmyra-horse ride (*maṭal*), a lover's public self-mortification.

**Badenya.**
- *Claiming, stronger:* Ma Tenenba, foster-mother of Fakoli, "I have given birth to a child without getting pregnant!" (Conrad 2004, l. 3110); Fakoli is "Soma Tenenba's son" (ll. 2688–89); her brothers grant her three months at home as for a new mother. The mother's-name prefix is confirmed, for daughters too (So'olon Kolonkan).
- *Smith's bargain, weaker:* Kosiya Kante's genies ask for four named kin and refuse substitutes (ll. 2835–3099), and the episode is a 1994 recording only. Self-substitution now rests on Brett-Smith alone (20th-c.), marked as reconstruction.
- *Line and burial:* "The House buries its own" rests on the grave-price episode (eight accounts from 1890) and on the contemporary record (burial under one's own name; blood kin taking the estate).
- *Texture:* a "mother" takes in a newcomer by referral and teaches her a craft; feasts have a "mother" and a "father"; the young serve and dance while elders sit as a jeli speaks for them (Gaudio pp. 62–69, 145, 164–169; Niang). The naming feast becomes a two-stage arc: a daughter first serves, later hosts.
- *Holy sites:* Do (al-Bakrī's "Daw", 1068; medieval burial mounds) added. Koulikoro's refuge was Sumanguru's shrine (1819–1930) whose rites excluded women: place-name only.
- *Kept:* the bird-masked bards (Ibn Baṭṭūṭa, 14th c.); the corpus editors' Komo link is their reading, and no Komo rite is shown.
- *Names:* about 25 verified Mande women's names in `waf_conrad_conde_sunjata.md`.

### Decisions (user, 2026-10-19) and build
1. The Garland crosses Śaiva and Vaiṣṇava ("it can cross, if that makes sense for the religion and sources").
2. Name: the Worn Garland.
3. The djinn's debt is a one-off: one return a year after the bargain, then never again ("I don't think any other mechanic has a pay-to-play subscription in perpetuity").
4. Both built at once, then a long observation round.
5. The optional Tai vow is not built.

Built: faiths `tm_garland` (in `hinduism_religion`) and `tm_badenya` (in `west_african_religion`, every god-name key overridden: Ala, the ancestors, the spirits, the bush spirits); rites, tenets (The Pāvai Vow, The Temple Street, vanilla Bhakti; The Crossing, Mother's Children, vanilla Ancestor Worship); holy sites (`kanchipuram` reused; `tm_srirangam`, `tm_tanjavur`, `tm_madurai`; `tm_kirina`, `niani`, `awkar` reused, `tm_walata`, `tm_do`); traits `tm_daughter_of_the_garland` ("Daughter of God") and `tm_daughter_of_the_house`; decisions `tm_pavai_decision` (Mārkaḻi only) and `tm_crossing_decision`; events `tm_garland.0010–0013, 0001, 0002, 0009, 0020, 0030` and `tm_badenya.0010–0012, 0002, 0015, 0020, 0030`; seeds at Kanchipuram (county only) and Sibi (county and lord); the growth engine's call reaches the Deccan and West Africa; burial on `on_death`, skipping bodies marked `tm_reborn` by re-embodiment (the Jade Embryo's burial hook now skips them too).

## 16. Revisions after the October 2026 reading (approved by user 2026-10-21)

Sources: `research/book_bhatt_brown_trans_les.md`, `research/serano_blog_essays.md`, and the TSQ notes (`research/tsq_*.md`, `research/wsq_libby_wondrous_bodies.md`). Numbers are those of the compiled list the user approved.

### Decisions (user, 2026-10-21)
- Approved: every item of the compiled list except those below.
- **Undecided:** item 23, the Ha-Nehpakhot licence rebalance (the lord's veto may read as "a Christian lord protects her from the Jews"). Not built.
- **Kept:** Grandmother's House cutting boys stays. It is the one condemned "way to do it", so it may make the child-lifter slander true in the world; the narrator still never confirms a rumour about any other House.
- **Dropped:** the Tiresias Question. The myth is Hellenic, known in Byzantium only as classical learning in later scholia.
- **Saints (new):** the Adelphai get a canon of *fictional* foremothers, named after Dorley's main characters in Byzantine form: Stephania, Bethania, Diana, Christina, Philippa (Diana keeps her own name: user, 2026-10-21). The Orthodox monk-saints (Marinos, Euphrosyne, Pelagia, Eugenia, Theodora, Anastasia) are not claimed: they crossed toward manhood (out of scope) and are the Church's own double standard, which the Sisters name in their own voice.

### Writing rules (all loc, all faiths)
1. The Mother's mark *knows*; the world's mark *watches*.
2. No golden past. The faiths say "the fight kept", never "the honour lost". No creation story of an undivided first sex in any faith's main voice.
3. Hostile lines are tagged by family (*inner*: the seed's heat; *birth*: "I baptised a boy"; *trace*: "born to take, not be taken") and by shape (unpersoning: "a thing"; exposing: "a deceiver"). Physicians come in four kinds: the lure, the contagion, the mutilation, the madness. Hostile lines aim at the imagined body, not the clothes. Blame is split between the physician (nature erred) and the preacher (the house that raised her). Every hostile line belongs to a named speaker of a vanilla faith or court.
4. The narrator never confirms that a child was taken (Grandmother's House excepted, above), never says the Mark runs in families, and never gives the Mark a cause. Hostile voices may say all three.
5. No body reveal as a twist or a joke. No before-and-after scene. No text about a Marked child's future body.
6. Every gate is equal: no faith calls another gate lesser, and no road to womanhood is "more complete". Each faith keeps its own word for its daughters; sisterhood across faiths is an alliance, not one people.
7. Not only holy: every faith gives daughters a road to standing that is not holy office, and no text says they are accepted for a sacred role or for being useful.
8. The knife makes the body the world must read as a woman's; it does not make the woman. Marked and declared sisters are sisters before the knife.
9. Reclaimed words only in a daughter's voice. A Greek "monster" word needs a Byzantine source first.
10. "Contagion" is a hostile word only.
11. Worn Garland: never describe temple song in the terms of modern "classical" dance.
12. Badenya: no race-curse rhetoric, even attributed. Do not use Somé. In the faith's voice the smith's price is the mask the world put on her.
13. Bædling: no era text implying the pagan North was free.
14. The faiths are inventions, not anyone's ancestors (README).

### Collapse fixes (approved by user 2026-10-21)
A 867–1188 observe run: the five small faiths (all but Yutai Dao) kept collapsing. Bædling lost Gotland when it passed by inheritance to heirs not of the faith; Adelphai Dorleyaiou lost Phrygia when the Byzantine liege revoked it from the Mother's appointee (925); Ha-Nehpakhot's kahal absorbed whole Kabarist ruling houses (Udmurtia 1036, Permia 1054), and Samaritans in another run; each faith had only 0–20 Marked characters to draw from.

- **B. The seat to a member** (`tm_seat_on_actions.txt`, `tm_seat_effects.txt`). The seats are those of `tools/census_report.py` (Phrygia, Gotland, Åland, Shazhou, Venaissin, Kanchipuram, Candragiri, Kirina, Awkar). When a ruler of the seat's faith dies holding it and the county's heir (`current_heir`) is not of her faith, `on_death` (which fires while she still holds her titles) moves the county and the baronies she holds in it, as a grant, to a member: her daughter by birth or adoption (a grown one first), else a daughter or House member at her court, else any adult of the faith at her court. The new countess is a vassal of the dead holder's liege; if the holder was independent and kept other land, of her heir; otherwise independent. Only the seat moves. Never taken from a player heir; a player holder of the faith benefits, but only when she holds other land, so her heir has a realm to play. `set_designated_heir` was not used: in 1.20 it takes only a direct child and names an heir to every title, not the seat alone. The county keeps `tm_seat_passed` (the member) for save inspection.
- **The charter** (`tm_charter_on_actions.txt`, `tm_charter_opinion_modifiers.txt`, `tm_seat_effects.txt`). On `on_title_lost` with transfer type `revoked`, when a seat is taken from a holder of its faith by a revoker of another faith: the revoker loses major piety and major prestige (shown in a message), and every member of the faith in the revoker's realm (vassals and courtiers, the holder among them), the faith's head and, for Phrygia, the Mother House holder take "Took the Seat of Our Faith" (−40, 20 years). Not forbidden. The AI's revoke weights are in vanilla script (`00_revoke_title_interaction.txt`, read but not overridden), and none of them read a modifier the mod could set, so the AI is discouraged only by the after-cost. (A stronger option, not built: the vassal-contract flag `religiously_protected` keeps faith hostility from making a revocation non-tyrannical, but it would change vassal contracts.)
- **C. The kahal draws Rabbanite Jews only** (`tm_rabbanite_jew_trigger`, `tm_fixes_triggers.txt`): Rabbinic Judaism (with Merkabah, its rite) and the Jews of Malabar. Samaritans, Karaites, Kabarists and the Beta Israel (Haymanot) are out of the kahal joins, the pilgrim's home culture, the call's Jewish branch and `tm_turning_seeker_trigger`. Karaites: §13 lists them among possible seekers as an *open* question and notes that their law differs on Purim and on the Talmud's authority; every path into the sect is now framed as the Provençal Rabbanite community, so they are excluded until the open question is answered with their own text.
- **Reach.** The call's rumour chance rises from 1% to 2%, and +3 for a member of the faith living within three counties of hers (three steps of `any_neighboring_county`, not her own county, which has its own +4). The other contact modifiers stay. A modest widening, not a cap or a size-scaled rate.
