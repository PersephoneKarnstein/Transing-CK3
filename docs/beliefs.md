# Transbian Maximalism — belief list (working draft v1)

Running list of beliefs drawn from the research, each mapped to a CK3 slot. Sources are the reports in `docs/research/`:

| Tag | Source |
|---|---|
| **TM** | `book_transgender_marxism.md` (Gleeson & O'Rourke anthology) |
| **BH** | `book_bhatt_chu.md` part I (Talia Bhatt, *Trans/Rad/Fem*) |
| **CH** | `book_bhatt_chu.md` part II (Andrea Long Chu, *Females*) |
| **ST** | `book_stryker_history.md` (Stryker, *Transgender History*) |
| **T1** | `book_tsr_1_2.md` (Transgender Studies Reader vol. 1; the PDF does not contain vol. 2) |
| **TR** | `book_tsr_remix.md` (TSR Remix) — tenet table pending |
| **W-B / W-3 / W-M** | web reports on baedelism / third-wave transfeminism / transgender Marxism — pending |
| **H-*** | history reports (Trans Historical, Karras, Surtees & Dyer, Wiesner-Hanks) — pending |

Movement column: **BD** baedelism, **3W** third-wave transfeminism, **TMx** transgender Marxism, **GEN** broader trans studies. Plausibility column is filled by the history pass: **S** strengthened, **W** weakened, **M** mixed, **?** not yet assessed.

Design frame from the user (2026-10-13): random "transgender" trait; ritual castration of male-assigned characters on the gallae model; castrated men are culturally women; inheritance through adoptive matrilines; women-centred priesthood.

---

## A. Sex, gender and recognition

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| A1 | Women rule; men hold office only by exception. Fits adoptive matrilines. | `doctrine_gender_female_dominated` (alt: `_equal`) | 3W, BD | BH#1 "The Regime Is a Lie"; TM#4 | ? |
| A2 | Sex is mutable; womanhood is achieved by rite, not recorded at birth. | Core rite tenet (new) + the castration rite; `doctrine_witchcraft_accepted` | GEN, 3W | ST "Mutable Flesh"; T1#2,#19; BH#16 "Gender Is Given, Not Claimed" (conferred by sisters at a naming rite) | ? |
| A3 | Trans women are women, not a venerated third caste. | Design rule: no third-gender category; hostility override vs faiths that "third-sex" | 3W, BD | BH#20 "No Third Sex"; T1#24 | ? (history pushes the other way: galli/hijra were "third") |
| A4 | Transness needs no cause; asking "why" is idle. | Faith flavour / doctrine text | GEN, TMx | ST "Left-Handed Doctrine"; TM§2.15 | ? |
| A5 | No physician or priest may gate the body; remedies pass freely. | Rite tenet (new, "Open Apothecary"); free transition decision | TMx, GEN | TM#6,#29; T1#3,#4; ST "Alchemy Freely Given", "Healers Serve, Not Judge" | ? |
| A6 | The court registers sex by lived body and status; a clerk may re-record gender on request. | Faith doctrine (new) "Writ of Gender" | 3W, GEN | ST "Writ of Gender"; BH#24 "Materialist Sex" | ? |
| A7 | No sumptuary law may bind the body; all dress is lawful to all. | Faith doctrine (new) "Equality in Dress" | GEN | ST | ? |
| A8 | Trans women's testimony is binding; "no one believes trans women" is made law. | Rite tenet (new) "The Doll Speaks" | 3W | BH#15 | ? |
| A9 | Gender is consensual: forced gendering (incl. of intersex infants) is sin. | Faith doctrine (new) | GEN | T1#3 | ? |

## B. Body, sacrament, castration

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| B1 | Remaking the flesh is worship; the castrated are whole. **Core mechanic.** | Core rite tenet (new, "Galli of the Great Mother"); `tradition_court_eunuchs` reflavoured (`can_castrate_prisoners`, `family_castration`); custom trait in group `eunuch` without inheritance blockers | GEN, CH | ST "Galli of the Great Mother"; T1#5 "Body-Craft Is Holy"; BH/CH#19 "The Castrated Are Whole"; BH#12 "Kill the Man Who Wears Your Face" (initiation buries the male self) | ? |
| B2 | A sacramental draught (mare's urine = estrogen) marks passage out of manhood. | Rite tenet (new, Communion-style) "The Mare's Draught" | CH, TMx | CH#8; TM#29 "Hormones Are Bread" | ? |
| B3 | The barren are holy; fertility confers no status, heirless rulers lose nothing. Supports adoption. | Inverted `tenet_sacred_childbirth` (new) | CH, 3W | BH/CH#9 | ? |
| B4 | Alchemists and wise-women who reshape bodies are honoured, not burned. | `doctrine_witchcraft_accepted` or `_virtuous` | 3W | BH#7 "Transmutation of the Flesh" | ? |
| B5 | Slurs and monstrosity are reclaimed as titles of power. | `doctrine_deviancy_virtuous`; flavour | GEN, TMx | T1#15 "Monster's Pride"; ST "Impurity Is Power"; TM§2.30 | ? |
| B6 | Pain and debility are the commons of all flesh; the maimed are owed care. | Rite tenet (reworked `tenet_exaltation_of_pain`) | TMx | TM#22 | ? |
| B7 | Dysphoria is a holy rupture; "true thought begins with the scream". | Rite tenet (Inner Journey-style) | TMx | TM#19 | ? |
| B8 | Captured men of hostile faiths may be ritually unmanned ("force is feminizing"). Ties to prisoner castration. | Interaction on prisoners; `can_castrate_prisoners` | CH | CH#18 | ? |

## C. Kinship, marriage, inheritance

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| C1 | Blood confers nothing; a house is those who choose each other. **Adoptive matrilines.** | `allows_adoption` + `free_adoption` cultural params (cf. `tradition_noble_adoption`) or custom rite param like `tenet_adoptionism`; bastardry doctrine making all children legitimate | TMx, 3W, ST | TM#1 "Nurture Beyond the Hearth", #27 "Chosen Kin"; BH#10; ST "The Street Is Our Hearth" (houses led by "mothers") | ? |
| C2 | Property and authority should not pass down bloodlines. (Tension with any inheritance; reconciled as *adoptive* matrilineal succession.) | `tradition_equal_inheritance` or female-preference succession + adoption | TMx, 3W | TM#11; BH#25 | ? |
| C3 | Love between women is the model household; same-sex marriage legitimate. | `doctrine_homosexuality_accepted`; same-sex marriage via consorts doctrine | 3W, BD | BH#5 "Sappho's Sanction"; T1#20 | ? |
| C4 | Bonds freely made and unmade; any woman may walk away. | `doctrine_divorce_allowed`; `tenet_polyamory`; `doctrine_concubines` reflavoured "Companions" | TMx, 3W | TM#12 "Free Love"; BH#4 "Fugitives from the Contract" | ? |
| C5 | Lesbians stand outside the marriage contract and owe no fealty to the two-sex law. | Rite tenet / tradition (Wittigian) | 3W, BD | T1#16; BH#28 "Our Prophet" | ? |
| C6 | Do **not** make pleasure the core: "liberating sex without liberating women" fails. | Design anti-pattern: avoid `tenet_carnal_exaltation` / `tenet_hedonistic` as core | 3W | BH#26 | — |
| C7 | Mentorship outside the dynasty is honoured; wards of non-kin learn better. | `better_ward_education` param; tradition | TMx | TM#15 | ? |

## D. Economy, labour, state (transgender Marxism)

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| D1 | Land and larder are held in common; clergy hold nothing. | `tenet_communal_possessions`; `tenet_vows_of_poverty`; ethos `ethos_communal` or `ethos_egalitarian`; `tradition_collective_lands` | TMx | TM#2,#9; ST "Live the Future Now" | ? |
| D2 | Clergy must labour, feed and nurse; no caste of thinkers. | `doctrine_clerical_function_alms_and_pacification`; `doctrine_theocracy_lay_clergy` | TMx | TM#7,#10 | ? |
| D3 | Care, cooking and the making of one another count as paid labour. | Tradition (new) "Wages Due" | TMx | TM#16 | ? |
| D4 | Those who labour may remake the world; rank is suspect. | `ethos_egalitarian`; `tradition_warriors_by_merit` | TMx, GEN | T1#8; TM§2.10 | ? |
| D5 | Shelter the cast-out; turning away a wanderer is anathema. | `tenet_ritual_hospitality`; `tradition_esteemed_hospitality` | TMx, ST | TM#8; ST "Mycelial Aid" | ? |
| D6 | Pleasure is a class demand; feasts and dances are duties. | `tradition_festivities`; `tenet_ritual_celebrations` | TMx, CH | TM#17,#30; CH#27 | ? |
| D7 | No sacred law-books; the clerk's ledger is the enemy's eye. Prisons are sin. | Avoid `tenet_legalism`/`tenet_religious_legal_pronouncements`; "Free the Confined" tenet | TMx, ST | TM#26; ST "Free the Confined" | ? |
| D8 | A disciplined minority at the chokepoints of care can halt a realm. | Tradition (populist factions, revolt events) | TMx | TM#24; ST "Street Power" | ? |
| D9 | Sex work is lawful and honoured; courtesans form guilds with sanctuary. | Rite tenet (new) "Companions of the Street" | ST, GEN | ST | ? |
| D10 | No circle is free while another is chained: internationalism, **anti-separatist**, no holy war. | No GHW; alliances; conflicts with E1 | TMx | TM#22,#25 | ? |

## E. Community, boundaries, militancy (baedelist / third-wave strand)

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| E1 | Only women may be priestesses; the faith "remembers we were oracles". **Separatism.** | `doctrine_clerical_gender_female_only` (with castrated men counting as women) | BD, 3W | BH#2 "Oracles of the Unmanned" | ? |
| E2 | All dissidents from the heterosexual regime are one congregation. | `tenet_communal_identity` | 3W, GEN | BH#11; ST "We Unite Around Our Oppression"; T1#6 | ? |
| E3 | Never hide what you are; stealth is dishonour, visibility a festival. | Rite tenet (new) "Read Aloud" / "Visible Before God" | GEN, BD | T1#1,#21,#29; ST | ? |
| E4 | Anger at injustice is holy; complacency the sin. | Virtues `wrathful`; sins `craven`, `content` | 3W, GEN | BH#14; T1#13 | ? |
| E5 | Do not rank oppressions; no purges of the "impure". Counterweight to intra-queer hostility. | Faith doctrine / pluralism | GEN | T1#10,#22 | ? |
| E6 | Holy war may be declared on realms whose law makes women property. | `doctrine_pluralism_fundamentalist` toward male-dominated faiths; hostility overrides | 3W | BH#13 | ? |
| E7 | Hostile foil: "men without members remain men" (Raymondite heresy for a rival faith). | Antagonist faith/rite with `special` hostility | — | T1#12 | — |
| E8 | Butches and transsexual women ride together; Amazons are still necessary. | `martial_custom_female_only` or `_equal`; `tradition_warrior_culture` | 3W, GEN | BH#23; T1#17,#18; TM#23 | ? |
| E9 | Pilgrimage reimagined as flight from the father's house to a sister's. | `doctrine_pilgrimage_encouraged` reflavoured | 3W | BH#22 | ? |
| E10 | Keep the archive; read the names of the dead each year. | Rite tenet (new) "Remembering Our Dead"; tradition "Keepers of the Archive" | GEN | ST | ? |

## F. Cosmology and flavour

| # | Belief | CK3 slot / vanilla template | Movement | Sources | Plaus. |
|---|---|---|---|---|---|
| F1 | In the beginning all were undivided; the cutting into man and woman was the Fall. | Creation myth; Gnosticism-style tenet | TMx | TM#20 "Before the Binary" | ? |
| F2 | The Great Mother and her castrated priestesses (Cybele/Attis framing). | Deity loc keys; HighGodName etc. | ST, GEN | ST "Galli of the Great Mother" | ? |
| F3 | "Cyborg, not goddess": crafted bodies over a pure natural order. Tension with F2. | Anti-`tenet_sanctity_of_nature` stance; flavour | TMx, GEN | TM#21; T1#30 | ? |
| F4 | The world is a roll of dice; chance is courted. | `tenet_astrology`-style "The Aleatrix" | TMx | TM#18 | ? |
| F5 | Mediums hosting a differently gendered spirit serve as prophets. | Rite tenet (new) "Possessed by the Other Spirit" | ST | ST | ? |
| F6 | Bearded saints and silent knights are venerated (Wilgefortis, *Roman de Silence*). | Rite tenet (new); saint flavour | ST | ST | ? |
| F7 | Male gods are honoured only as lovers and healers, never conquerors. | Pantheon loc | GEN | T1#27 | ? |
| F8 | Heraldry of the underground: the old mole, dice, stars. | CoA / nickname flavour | TMx | TM#28 | ? |
| F9 | A founding Prophet (Wittig role) whose words are code, not law. | Faith flavour | 3W | BH#28 | ? |

---

## Open design tensions to resolve

1. **Third sex vs. women.** History (galli, hijra, eunuchs) supports a *third* category; BD/3W insist trans women are simply women (A3). The user's rule "castrated men are culturally women" sides with BD/3W. Options: female-dominated doctrine + custom trait that scripted triggers treat as female, with rival faiths doing the "third-sexing".
2. **Separatism vs. internationalism.** BD/3W separatism (E1) against TMx anti-separatism and solidarity (D10). Likely resolution: separatist *clergy/community* (E1) with pluralist *foreign policy*.
3. **No inheritance vs. matrilines.** TMx rejects bloodline transmission (C2); user wants adoptive matrilines (C1). Resolution: inheritance exists but runs through adopted daughters, so blood never carries it.
4. **Goddess vs. cyborg.** Cybele framing (F2) is the medieval veneer; TMx "cosmos against nature" (F3) can live as the faith's anti-"natural order" theology rather than nature worship.
5. **Engine limit.** CK3 has no scripted effect to change a character's sex. "Castrated men are women" has to be done with a trait that custom triggers, succession scripting and portrait modifiers treat as female.

## Pending inputs

- Web reports (baedelism, third-wave transfeminism, transgender Marxism online) for BD/3W-specific beliefs and quotes.
- TSR Remix tenet table and precedents.
- Four history reports to fill the plausibility column and add terminology.
