# Transbian Maximalism — belief list (working draft v3)

Running list of beliefs drawn from the research, each mapped to a CK3 slot. Sources are the reports in `docs/research/`:

| Tag | Source |
|---|---|
| **TM** | `book_transgender_marxism.md` (Gleeson & O'Rourke anthology) |
| **BH** | `book_bhatt_chu.md` part I (Talia Bhatt, *Trans/Rad/Fem*) |
| **CH** | `book_bhatt_chu.md` part II (Andrea Long Chu, *Females*) |
| **ST** | `book_stryker_history.md` (Stryker, *Transgender History*) |
| **T1** | `book_tsr_1_2.md` (Transgender Studies Reader vol. 1; the PDF does not contain vol. 2) |
| **TR** | `book_tsr_remix.md` (TSR Remix) |
| **W-B / W-3 / W-M** | web reports on baedelism / third-wave transfeminism / transgender Marxism |
| **T2** | `book_tsr_2.md` (Transgender Studies Reader vol. 2) |
| **TH / KA / AN / WH** | history reports (Trans Historical, Karras, Surtees & Dyer, Wiesner-Hanks); see section G |

Movement column: **BD** baedelism, **3W** third-wave transfeminism, **TMx** transgender Marxism, **GEN** broader trans studies. Plausibility column (history pass, 2026-10-14): **S** strengthened, **M** mixed/needs in-world reinterpretation, **W** weak (the faith's own invention). See section G for the consolidated verdicts.

Design frame from the user (2026-10-13): random "transgender" trait; ritual castration of male-assigned characters on the gallae model; castrated men are culturally women; inheritance through adoptive matrilines; women-centred priesthood.

---

## A. Sex, gender and recognition

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| A1 | Women rule; men hold office only by exception. Fits adoptive matrilines. | `doctrine_gender_female_dominated` (alt: `_equal`) | 3W, BD | BH#1 "The Regime Is a Lie"; TM#4 | **M** — female rule attested on-map (Hausa, Aceh); full matriarchy not. `_equal` + female-only clergy is the conservative fit |
| A2 | Sex is mutable; womanhood is achieved by rite, not recorded at birth. | Core rite tenet (new) + the castration rite; `doctrine_witchcraft_accepted` | GEN, 3W | ST "Mutable Flesh"; T1#2,#19; BH#16 "Gender Is Given, Not Claimed" (conferred by sisters at a naming rite) | **S** — rite fixes legal sex in every book (oath before prelate, renaming, re-clothing); M→F direction is the faith's heresy |
| A3 | Trans women are women, not a venerated third caste. | Design rule: no third-gender category; hostility override vs faiths that "third-sex" | 3W, BD | BH#20 "No Third Sex"; T1#24 | ? (history pushes the other way: galli/hijra were "third") |
| A4 | Transness needs no cause; asking "why" is idle. | Faith flavour / doctrine text | GEN, TMx | ST "Left-Handed Doctrine"; TM§2.15 | **S** — "some simply are that way" matches humoral/Galenic indifference to cause |
| A5 | No physician or priest may gate the body; remedies pass freely. | Rite tenet (new, "Open Apothecary"); free transition decision | TMx, GEN | TM#6,#29; T1#3,#4; ST "Alchemy Freely Given", "Healers Serve, Not Judge" | **M** — anti-gatekeeping is modern; medieval analogue is women examiners/midwives certifying sex (Wojciech 1550s) |
| A6 | The court registers sex by lived body and status; a clerk may re-record gender on request. | Faith doctrine (new) "Writ of Gender" | 3W, GEN | ST "Writ of Gender"; BH#24 "Materialist Sex" | **S** — bishops, town halls and courts did re-record sex (Marin le Marcis, Germain, Céspedes) |
| A7 | No sumptuary law may bind the body; all dress is lawful to all. | Faith doctrine (new) "Equality in Dress" | GEN | ST | **M** — sumptuary law is period; its abolition is the faith's dissent |
| A8 | Trans women's testimony is binding; "no one believes trans women" is made law. | Rite tenet (new) "The Doll Speaks" | 3W | BH#15 | **W** — modern epistemic claim; nearest hook is women's testimony in sex examinations |
| A9 | Gender is consensual: forced gendering (incl. of intersex infants) is sin. | Faith doctrine (new) | GEN | T1#3 | **M** — hermaphrodites "elected" a sex under oath; forced assignment was the norm |
## B. Body, sacrament, castration

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| B1 | Remaking the flesh is worship; the castrated are whole. **Core mechanic.** | Core rite tenet (new, "Galli of the Great Mother"); `tradition_court_eunuchs` reflavoured (`can_castrate_prisoners`, `family_castration`); custom trait in group `eunuch` without inheritance blockers | GEN, CH | ST "Galli of the Great Mother"; T1#5 "Body-Craft Is Holy"; BH/CH#19 "The Castrated Are Whole"; BH#12 "Kill the Man Who Wears Your Face" (initiation buries the male self) | **M→S** — practice attested everywhere; theology of rebirth must be supplied (Attis/Dionysiac, Indian twice-born). Strong in Byzantium/Syria/Anatolia, condemned in Latin West (Nicaea canon 1) |
| B2 | A sacramental draught (mare's urine = estrogen) marks passage out of manhood. | Rite tenet (new, Communion-style) "The Mare's Draught" | CH, TMx | CH#8; TM#29 "Hormones Are Bread" | **M** — sacramental draught has no precedent; mare's urine is period-plausible material; frame as cult-internal |
| B3 | The barren are holy; fertility confers no status, heirless rulers lose nothing. Supports adoption. | Inverted `tenet_sacred_childbirth` (new) | CH, 3W | BH/CH#9 | **S** — celibacy/sterility as visible holy caste (monks, eunuchs, post-reproductive women; hijra infertility = priesthood) |
| B4 | Alchemists and wise-women who reshape bodies are honoured, not burned. | `doctrine_witchcraft_accepted` or `_virtuous` | 3W | BH#7 "Transmutation of the Flesh" | **M** — wise-women/medicine attested; "accepted" witchcraft is the faith's dissent |
| B5 | Slurs and monstrosity are reclaimed as titles of power. | `doctrine_deviancy_virtuous`; flavour | GEN, TMx | T1#15 "Monster's Pride"; ST "Impurity Is Power"; TM§2.30 | **S** — slurs reclaimed is how hijra/galli self-named (puellae/korasia); hostile vocabulary abundant |
| B6 | Pain and debility are the commons of all flesh; the maimed are owed care. | Rite tenet (reworked `tenet_exaltation_of_pain`) | TMx | TM#22 | **M** — Goodrich on maimed limbs/biosalvation; care commons via monastic hospitals |
| B7 | Dysphoria is a holy rupture; "true thought begins with the scream". | Rite tenet (Inner Journey-style) | TMx | TM#19 | **W** — modern; nearest is mystic rapture/possession |
| B8 | Captured men of hostile faiths may be ritually unmanned ("force is feminizing"). Ties to prisoner castration. | Interaction on prisoners; `can_castrate_prisoners` | CH | CH#18 | **S** — castration of captives/slaves is the actual medieval supply of eunuchs (sqâliba); morally the faith's darkest period-true element |
## C. Kinship, marriage, inheritance

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| C1 | Blood confers nothing; a house is those who choose each other. **Adoptive matrilines.** | `allows_adoption` + `free_adoption` cultural params (cf. `tradition_noble_adoption`) or custom rite param like `tenet_adoptionism`; bastardry doctrine making all children legitimate | TMx, 3W, ST | TM#1 "Nurture Beyond the Hearth", #27 "Chosen Kin"; BH#10; ST "The Street Is Our Hearth" (houses led by "mothers") | **W→M** — adoption as spiritual kinship (godparenthood, adelphopoiia) attested; the celibate/castrated clergy *must* recruit heirs by adoption, as monasteries did. Adoptive *matriline* as succession law is the mod's invention |
| C2 | Property and authority should not pass down bloodlines. (Tension with any inheritance; reconciled as *adoptive* matrilineal succession.) | `tradition_equal_inheritance` or female-preference succession + adoption | TMx, 3W | TM#11; BH#25 | **M** — Occitan female landholding (Ermengarde); monastic corporate property. Abolished inheritance has no precedent |
| C3 | Love between women is the model household; same-sex marriage legitimate. | `doctrine_homosexuality_accepted`; same-sex marriage via consorts doctrine | 3W, BD | BH#5 "Sappho's Sanction"; T1#20 | **M** — woman-woman love tolerated as invisibility; adelphopoiia and sworn-sister brasses give a recognised-bond hook |
| C4 | Bonds freely made and unmade; any woman may walk away. | `doctrine_divorce_allowed`; `tenet_polyamory`; `doctrine_concubines` reflavoured "Companions" | TMx, 3W | TM#12 "Free Love"; BH#4 "Fugitives from the Contract" | **M** — concubinage/sworn bonds/divorce (Islamic, Orthodox) high; a *woman* with plural partners low. Model as sworn-sisterhood/companions |
| C5 | Lesbians stand outside the marriage contract and owe no fealty to the two-sex law. | Rite tenet / tradition (Wittigian) | 3W, BD | T1#16; BH#28 "Our Prophet" | **M** — convent as the women's world outside the marriage contract |
| C6 | Do **not** make pleasure the core: "liberating sex without liberating women" fails. | Design anti-pattern: avoid `tenet_carnal_exaltation` / `tenet_hedonistic` as core | 3W | BH#26 | — |
| C7 | Mentorship outside the dynasty is honoured; wards of non-kin learn better. | `better_ward_education` param; tradition | TMx | TM#15 | **S** — fosterage and oblation are core medieval practice |
## D. Economy, labour, state (transgender Marxism)

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| D1 | Land and larder are held in common; clergy hold nothing. | `tenet_communal_possessions`; `tenet_vows_of_poverty`; ethos `ethos_communal` or `ethos_egalitarian`; `tradition_collective_lands` | TMx | TM#2,#9; ST "Live the Future Now" | **M** — alms economy of the galli STRONG; monastic common property attested; classless commons/abolished inheritance WEAK |
| D2 | Clergy must labour, feed and nurse; no caste of thinkers. | `doctrine_clerical_function_alms_and_pacification`; `doctrine_theocracy_lay_clergy` | TMx | TM#7,#10 | **S** — labouring clergy = monastic rule; alms and pacification period-true |
| D3 | Care, cooking and the making of one another count as paid labour. | Tradition (new) "Wages Due" | TMx | TM#16 | **W** — modern; keep in myth/tithe mechanics |
| D4 | Those who labour may remake the world; rank is suspect. | `ethos_egalitarian`; `tradition_warriors_by_merit` | TMx, GEN | T1#8; TM§2.10 | **M** — 1381 slogans, bhakti; Engels story works as creation myth, not in-world vocabulary |
| D5 | Shelter the cast-out; turning away a wanderer is anathema. | `tenet_ritual_hospitality`; `tradition_esteemed_hospitality` | TMx, ST | TM#8; ST "Mycelial Aid" | **S** — hospitality/sanctuary core to monastic and beguine houses |
| D6 | Pleasure is a class demand; feasts and dances are duties. | `tradition_festivities`; `tenet_ritual_celebrations` | TMx, CH | TM#17,#30; CH#27 | **S** — festival and procession culture of galli and medieval confraternities |
| D7 | No sacred law-books; the clerk's ledger is the enemy's eye. Prisons are sin. | Avoid `tenet_legalism`/`tenet_religious_legal_pronouncements`; "Free the Confined" tenet | TMx, ST | TM#26; ST "Free the Confined" | **M** — anti-legalism reads as heresy (Free Spirit); prison abolition modern |
| D8 | A disciplined minority at the chokepoints of care can halt a realm. | Tradition (populist factions, revolt events) | TMx | TM#24; ST "Street Power" | **M** — peasant revolts exist; vanguard framing modern |
| D9 | Sex work is lawful and honoured; courtesans form guilds with sanctuary. | Rite tenet (new) "Companions of the Street" | ST, GEN | ST | **M** — Rykener's world; sex work tolerated and regulated, not honoured |
| D10 | No circle is free while another is chained: internationalism, **anti-separatist**, no holy war. | No GHW; alliances; conflicts with E1 | TMx | TM#22,#25 | **M** — pilgrimage networks/mendicant orders as internationalism; separatism is the stronger medieval image (see E1) |
## E. Community, boundaries, militancy (baedelist / third-wave strand)

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| E1 | Only women may be priestesses; the faith "remembers we were oracles". **Separatism.** | `doctrine_clerical_gender_female_only` (with castrated men counting as women) | BD, 3W | BH#2 "Oracles of the Unmanned" | **S** — strongest row in every matrix: abbess + eunuch clergy + hijra/bissu/bori priestess give a women-plus-castrates clergy a firm veneer. Trans-*inclusive* women's space needs doctrine (d) to carry it |
| E2 | All dissidents from the heterosexual regime are one congregation. | `tenet_communal_identity` | 3W, GEN | BH#11; ST "We Unite Around Our Oppression"; T1#6 | **M** — guild/ocak/college of the caste (köçek houses, galli colleges) |
| E3 | Never hide what you are; stealth is dishonour, visibility a festival. | Rite tenet (new) "Read Aloud" / "Visible Before God" | GEN, BD | T1#1,#21,#29; ST | **M** — galli were loudly visible; medieval passing cases (Rykener, Céspedes) were punished when read |
| E4 | Anger at injustice is holy; complacency the sin. | Virtues `wrathful`; sins `craven`, `content` | 3W, GEN | BH#14; T1#13 | **M** — wrath is a vice in all period faiths; keep as the faith's inversion |
| E5 | Do not rank oppressions; no purges of the "impure". Counterweight to intra-queer hostility. | Faith doctrine / pluralism | GEN | T1#10,#22 | **W→M** — intra-queer hostility is modern content; medieval fault lines exist (castrated vs intact, passing vs mixing). Implement as a schism (Proclaimer/Abolisher) |
| E6 | Holy war may be declared on realms whose law makes women property. | `doctrine_pluralism_fundamentalist` toward male-dominated faiths; hostility overrides | 3W | BH#13 | **M** — heresy framing is how the faith *will* be treated; its own holy war is the fiction |
| E7 | Hostile foil: "men without members remain men" (Raymondite heresy for a rival faith). | Antagonist faith/rite with `special` hostility | — | T1#12 | — |
| E8 | Butches and transsexual women ride together; Amazons are still necessary. | `martial_custom_female_only` or `_equal`; `tradition_warrior_culture` | 3W, GEN | BH#23; T1#17,#18; TM#23 | **M** — Amazons, Artemisia, women orators in crisis; sworn virgins. Period image, not norm |
| E9 | Pilgrimage reimagined as flight from the father's house to a sister's. | `doctrine_pilgrimage_encouraged` reflavoured | 3W | BH#22 | **S** — flight to convent/sanctuary is period-true |
| E10 | Keep the archive; read the names of the dead each year. | Rite tenet (new) "Remembering Our Dead"; tradition "Keepers of the Archive" | GEN | ST | **M** — martyrologies and necrologies are monastic staples |
## F. Cosmology and flavour

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| F1 | In the beginning all were undivided; the cutting into man and woman was the Fall. | Creation myth; Gnosticism-style tenet | TMx | TM#20 "Before the Binary" | **S** — Plato's androgyne, Hermaphroditus cosmogony, Gnostic undivided Adam |
| F2 | The Great Mother and her castrated priestesses (Cybele/Attis framing). | Deity loc keys; HighGodName etc. | ST, GEN | ST "Galli of the Great Mother" | **S** — Cybele/Attis/Syrian Goddess; but no source bridges c.250–867, so the faith must claim *survival* or *revival* |
| F3 | "Cyborg, not goddess": crafted bodies over a pure natural order. Tension with F2. | Anti-`tenet_sanctity_of_nature` stance; flavour | TMx, GEN | TM#21; T1#30 | **W** — anti-nature stance is modern; keep as theology of "the Mother's art over Nature" |
| F4 | The world is a roll of dice; chance is courted. | `tenet_astrology`-style "The Aleatrix" | TMx | TM#18 | **M** — astrology/omens period-true; aleatory framing modern |
| F5 | Mediums hosting a differently gendered spirit serve as prophets. | Rite tenet (new) "Possessed by the Other Spirit" | ST | ST | **S** — spirit-possessed gender-variant mediums attested widely (jin bandaas, bori, shamans) |
| F6 | Bearded saints and silent knights are venerated (Wilgefortis, *Roman de Silence*). | Rite tenet (new); saint flavour | ST | ST | **S** — Wilgefortis/Ontcommer, Roman de Silence, Marinos, Thecla |
| F7 | Male gods are honoured only as lovers and healers, never conquerors. | Pantheon loc | GEN | T1#27 | **M** — Dionysus/Attis as gentle consort gods |
| F8 | Heraldry of the underground: the old mole, dice, stars. | CoA / nickname flavour | TMx | TM#28 | ? |
| F9 | A founding Prophet (Wittig role) whose words are code, not law. | Faith flavour | 3W | BH#28 | **M** — foundress-prophetess has precedents (Guglielma, Kimpa Vita, Hutchinson) |
---

## G. Historical plausibility — consolidated verdicts (history pass)

Four history reports were asked the same thirteen questions. Sources: **TH** `hist_trans_historical.md` (87 entries), **KA** `hist_karras_medieval_sexuality.md` (215), **AN** `hist_ancient_gender_diversity.md` (53 + galli dossier), **WH** `hist_wiesner_gender_in_history.md` (113).

| Belief | TH | KA | AN | WH | Consolidated |
|---|---|---|---|---|---|
| (a) Trans women as distinct sex class | Strong, if built on eunuch/köçek/khuntha model | Medium: stigmatised class existed; faith sacralises it | Partial: third-category words existed as deficient-male | Third class attested on-map; "women" is the mod's step | **M.** Reclaim an attested third estate that the faith *also* counts among women |
| (b) Womanhood achieved by rite | Strong for the *form* (oath, renaming, re-clothing) | Medium: attested direction is woman→honorary man | Strong inside the cult, weak for outsiders | Strong: rite, not body, fixed legal status | **S.** Make the rite the legal moment; hostile faiths see a "half-man" |
| (c) Castration as sacred rebirth | Moderate: practice attested, condemned by all orthodoxy | High in Byzantium, medium-as-heresy in Latin West | Partial: act attested; rebirth theology must be borrowed from mysteries | Sacred eunuch attested (India); rebirth language from "twice-born" | **M→S east.** Present as heretical sacrament performed *by the priestess on another*; Matt. 19:12 read literally |
| (d) Castrated men regarded as women | **Strong** — best-supported belief, Byzantine core + 6th-c. Frankish convent | Medium-High: al-Jahiz (867-contemporary) on eunuchs' transfer to the female realm | Partial→Strong in Syrian/Anatolian sphere; Roman texts say "half-men" | Never "as women", always "neither/both" | **M→S.** Explicit, contested faith doctrine; homeland east of Rome |
| (e) Women-only / transfem priesthood | Moderate-to-Strong as heterodox order | Medium: eunuch clergy attested, female priests not; abbesses the model | Strong for women-only mysteries; mixed cis/trans clergy is the synthesis | **Strongest row**: abbess + bori + hijra/bissu | **S.** Clerical gender female-only with castrates counted as women |
| (f) Separatism from men | Moderate: convent and Amazon; model as monastic vows | **High** in convent/beguine/ribat form | Partial: withdrawal, not secession | Convents/guilds plausible; trans-inclusive version needs doctrine (d) | **M.** Monastic/withdrawn separatism, not political |
| (g) Adoptive / matrilineal heirship | Weak-to-Moderate: caste apprenticeship lineages only | Medium: spiritual kinship real; adoptive matriline as law not | Weak-Partial: celibate clergy *must* adopt heirs, as monasteries did | Matriliny attested off-map; combination is the mod's invention | **W→M.** Sell as spiritual kinship under an invented Salic-style law; childlessness is the historical engine |
| (h) Communal property / no inheritance | Weak: only ocak/monastic commons | Medium: monastic corporation is the medieval form | **Strong** for the galli alms economy | Weakest row | **M.** Alms economy + corporate temple property yes; classless commons no |
| (i) Polyamory / non-marital kinship | Moderate for serial unions and same-sex handfasting; weak for plural marriage | High for concubinage and sworn bonds; low for a woman with plural partners | Partial: symbios attested; sharing only as satire | Plural/dissoluble marriage has core precedents; woman-headed plural households do not | **M.** Companions/sworn-sisterhood and free divorce, not plural wives |
| (j) Bodily modification as sacrament | Moderate: practices rich, sacrament framing pagan/imperial | Medium-High: circumcision mainstream, castration its extreme | **Strong**: blood-rites richest element | Strong as category (footbinding as honour) | **S** |
| (k) Intra-queer hostility | Moderate: sources rank castrated vs effeminate | Low-Medium: no intra-community schism of baedelist type | Partial: boundary-policing material only | Entirely modern; implement as Proclaimer/Abolisher variants | **W→M.** Stage as schism between two rites |
| (l) Heresy / class-struggle framing | **Strong**: every hostile source codes it as heresy | High for heresy; low for class struggle as self-description | Strong: labour is how ancients saw gender | Period hooks (1381, bhakti); keep economics in myth | **S for heresy, W for class vocabulary** |
| (m) Matriarchy / female-dominated | — | — | — | Female rule attested; full matriarchy not | **M.** `female_dominated` defensible as faith law; `equal` + female clergy more conservative |

### Design consequences

1. **Homeland east of Rome.** Every ancient text that calls castrated men women is Syrian, Anatolian or Scythian; Roman texts say *semivir*. Byzantine eunuch culture and al-Jahiz carry it into 867. Place the culture's heritage in Anatolia/Syria/the steppe, not Latin Europe.
2. **Stage it as a heresy.** Hostile faiths should treat the rite as sodomy/counterfeit; that is the most period-true reception and gives natural hostility overrides and "Burned" endings.
3. **Castrate-as-woman is doctrine, not assumption.** Make it an explicit tenet or doctrine that rival faiths deny, since no historian says it was universal.
4. **Adoption is driven by childlessness.** The honest in-world logic: a castrated/celibate clergy cannot breed heirs, so the house chooses them (monastic succession). Matriline is the faith's law layered on that.
5. **No source bridges c. 250–867.** The faith must claim either secret survival of the Mother's cult or a revival; flavour text should say which.
6. **Borrow institutions, not identity concepts** (KA). Convent, guild, ocak, godparenthood and adelphopoiia are the shells; modern identity language stays in the design doc.

---

## H. Additions from the web sweeps and TSR volume 2 (v3)

Tags: **W-B** `web_baedelism.md`, **W-3** `web_third_wave_transfeminism.md`, **W-M** `web_transgender_marxism.md`, **T2** `book_tsr_2.md`. Plausibility uses the same history verdicts as section G.

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| H1 | Transmisogyny is the structural core of patriarchy; a wrong to a daughter is a wrong to a woman. | Core rite tenet "The Root of Wrong"; crime doctrine "Transmisogyny Is Misogyny" | BD, 3W | W-B#1,#2,#4; W-3#30 | **W** — modern theory; in-world as the faith's cosmology of the Fall (cf. F1) |
| H2 | Womanhood as defection from the male class: any adult may lay down manhood before the Mother. Manhood is a class one can leave. | Rite tenet "The Refusal"; `doctrine_gender_female_dominated` with one open door | 3W, BD | W-3#1,#9; W-B#24 | **S** — rite fixes legal sex (G-b); al-Jahiz on eunuchs' transfer (G-d) |
| H3 | Touched / Untouched (TMA/TME) as two legal estates; the Untouched may not hold the altar. | Faith doctrine (two estates) | BD | W-B#5,#6; W-3#8 | **M** — medieval estates are period; this cut is modern. Carry it as the faith's law |
| H4 | The daughters speak first; decentre the rest. | Faith doctrine (council priority) | BD | W-B#3,#7 | **M** |
| H5 | Trans lesbian separatism: own hall, bed and law; men barred from the hall. | Culture tradition "Lezsep" + `doctrine_clerical_gender_female_only`; hostility | BD | W-B#10,#16; W-3#8 | **M** — convent/beguine form strong (G-f); trans-inclusive version carried by (G-d) |
| H6 | t4t as a vow: two daughters who swear share the last draught; blessed above all unions. | Rite tenet "Vow of the Last Vial" / "Cybelean Love" | BD, 3W | W-B#11; W-3#11 | **M** — sworn-sisterhood/adelphopoiia hooks (G-i, m) |
| H7 | Desire for men is the regime's wound; a daughter who takes a husband is pitied. | Marriage/opinion doctrine | BD, 3W | W-B#12; W-3#10 | **W** — political lesbianism modern; convent-as-refuge is the veneer |
| H8 | Masculinity is power not dress; women in mail are women. | `martial_custom_female_only`/`_equal`; tradition | BD | W-B#13 | **M** (E8) |
| H9 | Love the sister you loathe: quarrels never carried before outsiders; shelter owed whatever the grudge. | Rite tenet (communal identity variant) "Unbending Sisterhood" | BD, 3W | W-B#15; W-3#7 | **M** — guild/ocak solidarity (G-a) |
| H10 | The hard foremothers' books were ours all along (second wave read as transfeminist). | Ancestor veneration flavour "The Old Mothers Were Ours" / "The Foremothers" | BD, 3W | W-B#17,#18; W-3#21 | **M** — foundress-prophetess precedents (F9) |
| H11 | No pontiff, no dungeons, no absolution; forgiveness is arrogance. | `doctrine_no_head`; no confession; "No Absolution" | BD | W-B#19,#20,#30 | **M** — anti-clerical heresies (Free Spirit) are period; prison abolition modern |
| H12 | Changing the flesh, not the name, is what frightens kings; the body is the deed. | Rite tenet (sacred modification) | BD | W-B#21,#22,#27 | **S** (G-j) |
| H13 | The third *political* sex: those who cannot or will not breed; the faith counts them women, the world counts them eunuchs. | Contested special doctrine | 3W | W-B#25; W-3#3,#4,#18 | **S** — this is exactly the attested third estate (G-a) plus the faith's step (G-d) |
| H14 | The poison and the draught: testosterone poison, estrogen quasi-sacred; dosing against will owed blood-price. | Culture tradition "Herb-Wives" | BD | W-B#26; W-3#16 | **M** — herb-wives period; no HRT. Mare's-urine legend disputed even in-group |
| H15 | Crack the egg: a priestess may speak privately with any courtier; some leave as daughters. | Character interaction (clergy proselytism) "The Contagion" | BD, 3W | W-B#28; W-3#24 | **M** — conversion by preaching is period; frame as heresy's spread |
| H16 | Unpersoning and social death as sacrament; the daughter who has died a thousand times is holiest. | Rite tenet "The Thousand Deaths" | BD | W-B#29 | **M** — martyrdom/kenosis language is period |
| H17 | Public call-outs of a daughter are scapegoat rituals; leaders of the stoning bear the stain. | Crime doctrine | BD | W-B#31 | **W→M** — stage as schism (G-k) |
| H18 | We have always existed: gallae, bædlings, eunuch-priestesses as foremothers; the Church that burned them is the hereditary enemy. | Heritage flavour; ancestor veneration; hostility toward Christian faiths | BD, 3W | W-B#32, §4.7-4.8; W-3#25,#27,#28 | **S** for the lineage claim, **W** for continuity (no source bridges 250–867; claim survival or revival) |
| H19 | Day of Blood: each spring novices take the knife, die as the god and rise as daughters. Two rival readings = two sects. | Core rite tenet (calendar rite) | BD, 3W | W-B§4.5; W-3#2 | **M→S east** (G-c) |
| H20 | The Mother is barren; she is protector, not progenitor. | HighGod loc keys | BD, 3W | W-B§4.3; W-3#4 | **S** — Cybele material |
| H21 | Begging sisters: honoured in the temple, poor in the street; fortune-telling and dance. | Culture tradition (clergy income) | BD, 3W | W-B§4.1; W-3#29 | **S** — best-attested galli trait (G-h) |
| H22 | Feminine grammar: the court records every daughter in the feminine; otherwise a fine. | Culture tradition (naming law) | BD | W-B§4.4,§4.8 | **S** — gallae self-naming, bædling penitential pronouns |
| H23 | Bæddel as reclaimed name over the hall door. | Culture/heritage name | BD | W-B§4.8 | **S** — attested OE word; place-name hypothesis unproven |
| H24 | The knife is a gift, never a sentence: castrating a captive is kinslaying of the Mother. **Conflicts with B8.** | Doctrine forbidding penal castration | BD | W-B§4.6 | **W** — penal/slave castration *is* the period source of eunuchs; the faith's refusal is its dissent |
| H25 | No shame in the veil: concealment before enemies is sacred cunning. **Conflicts with E3.** | Faith doctrine "Disguise is Virtue" | 3W (Bettcher) | T2#7 | **S** — Rykener, Céspedes survived by it |
| H26 | Sisters are born of any womb: the Goddess sows daughters among every people. Theology for the random trait. | Faith doctrine "Daughterhood by Recognition" | GEN | T2#2 (joya emergence) | **S** — joya, bissu, baylan emergence narratives |
| H27 | Keepers of the threshold: only the cut and the crone may wash the dead. | Rite tenet (exclusive funerary office) | GEN | T2#4 (Miranda on joyas) | **S** — exclusive ritual office is the strongest third-gender pattern |
| H28 | Renaming is rebirth: renamed before fifty witnesses, the old name buried as a corpse. | Rite tenet / tradition | GEN | T2#11 (Rivera's ceremony) | **S** — monastic name-taking |
| H29 | The sisterhood's school: veterans teach dress, voice and bearing. | Culture tradition (education) | GEN | T2#26 (dansho school) | **S** — guild apprenticeship (G-g) |
| H30 | A cut daughter may be taken as wife by a chief, "more robust than the women". | Marriage custom | GEN | T2#25 (joya wives) | **S** on the colonial record; weak on-map |
| H31 | The body is common land: hormone, herb and knife belong to all sisters. | `tenet_communal_possessions` reflavoured | TMx | T2#13 (Preciado gender-copyleft); W-M | **M** (G-h) |
| H32 | No worth in labour: the idle, the ill, the whore and the prisoner are as holy as the steward. | Doctrine against the "productive body" | TMx | T2#14 (Irving) | **M** — mendicant ideal |
| H33 | Abolish the heir: the dead sister's goods return to the house. | Succession/tradition "Common Inheritance" | TMx | T2#15 (Bassichis, Lee & Spade); W-M | **W** (G-h) — monastic reversion of goods is the veneer |
| H34 | Trickle up: justice begins with the lowest sister. | `ethos_egalitarian` | TMx | T2#16 | **M** |
| H35 | Our dead are not your coin: no lord may raise a shrine over a murdered sister to buy virtue. | Funeral doctrine | GEN | T2#20 | **M** — relic politics inverted |
| H36 | Against the pure: take what the world gives and bend it. | Doctrine forbidding ascetic purity | TMx | T2#22 (O'Brien) | **M** |
| H37 | Man, woman and homosexual are also inventions. | Doctrine "Categories Are Idols" | GEN | T2#24 | **W** — modern; keep as esoteric tenet |
| H38 | Cis is not a caste: the line between them and us is thin as a tincture. | Tolerant ethos toward non-trans | 3W | T2#28; W-3 critics | **M** |
| H39 | Innate before the rite: the trait exists from birth and raises the chance of seeking the Refusal; the rite recognises, it does not create. | Design rule for the "transgender" trait | 3W | W-3#31 | — |
| H40 | Transition as loss of value to patriarchal reproduction (sterility as the price and the point). | Core logic linking castration, barrenness and adoption | TMx, 3W | W-M§2.2; W-3#18 | **S** — the faith's childless clergy *must* adopt (G-g) |
| H41 | Rehabilitation by the knife: a selected violent man is unmade and remade as a daughter under a sponsor who went through it herself. "The Dorley precedent." | Doctrine group `doctrine_tm_knife` option B; prisoner interaction gated on an intake trigger; 3-stage chain | Dorley (Greaves), CH#18 | `docs/dorley_precedent.md` | **M** — captive castration is period practice; the rehabilitative frame and the sponsor are the faith's invention (monastic oblation and conversion of captives are the veneer) |
| H42 | Grandmother's House: the same knife as extortion, trafficking and torture. The regime the faith defines itself against. | Hostile template / option A; rival-faith slander text | Dorley | `docs/dorley_precedent.md` | **S** — this *is* the medieval eunuch trade |
| H43 | Washout: those who will not change are not kept; Beatrice breaks the news in the darkened wing. | Event + execution/exile/hand-over to a holy order of washouts | Dorley | `docs/dorley_precedent.md` | **M** — monastic expulsion and penal slavery as veneer |
| H44 | The sponsor becomes the sister: manipulator to mentor to adoptive kin. Closes the loop to adoptive matrilines (C1). | Guardian/ward scripting; `adopt_interaction` at completion | Dorley; H29 (sisterhood's school) | `docs/dorley_precedent.md` | **S** — fosterage, oblation, guild apprenticeship |

### New tensions surfaced

7. **Penal castration.** B8 (Chu: force is feminizing; castrate captives) vs H24 (the knife is a gift, never a sentence). **User decision (2026-10-14): yes, lampshaded as "the Dorley precedent"** (Alyson Greaves, *The Sisters of Dorley*): castration of a *selected* violent man as rehabilitation under a sponsor, with an older crueller regime as the foil and a washout path for failures. Implemented as an early-campaign three-way choice (Grandmother's House / Aunt Bea's House / The Gift Alone); see `docs/dorley_precedent.md`. History sides with the practice (captive eunuchs) and with the faith's dissent (Nicaea), so the two-regime structure is also the honest one.
8. **Visibility vs the veil.** E3 (Read Aloud) vs H25 (No Shame in the Veil). Resolve as two rites or as inside/outside: visible among sisters, veiled before enemies (W-3#22 "Against Plausible Histories").
9. **TMA/TME estates vs "cis is not a caste".** H3 vs H38. Natural schism line, alongside Proclaimer/Abolisher.

---

## Open design tensions to resolve

1. **Third sex vs. women.** History (galli, hijra, eunuchs) supports a *third* category; BD/3W insist trans women are simply women (A3). The user's rule "castrated men are culturally women" sides with BD/3W. Options: female-dominated doctrine + custom trait that scripted triggers treat as female, with rival faiths doing the "third-sexing".
2. **Separatism vs. internationalism.** BD/3W separatism (E1) against TMx anti-separatism and solidarity (D10). Likely resolution: separatist *clergy/community* (E1) with pluralist *foreign policy*.
3. **No inheritance vs. matrilines.** TMx rejects bloodline transmission (C2); user wants adoptive matrilines (C1). Resolution: inheritance exists but runs through adopted daughters, so blood never carries it.
4. **Goddess vs. cyborg.** Cybele framing (F2) is the medieval veneer; TMx "cosmos against nature" (F3) can live as the faith's anti-"natural order" theology rather than nature worship.
5. **Engine limit.** CK3 has no scripted effect to change a character's sex. "Castrated men are women" has to be done with a trait that custom triggers, succession scripting and portrait modifiers treat as female.

## Pending inputs

- Terminology lists from the four history reports (section 4 of each) still to be mined for localisation strings.
- Nothing else outstanding; all twelve research reports are in `docs/research/`.
