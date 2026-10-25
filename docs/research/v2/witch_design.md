# The Good Ladies (working name): a Latin folk faith of the night company, 1178 start. Design draft

Written 2026-10-25. Consolidates the six witch notes (listed in §9) and the user's decision of 2026-10-25 amending writing rule 25. Nothing here is built. Open decisions are in §8, with a recommendation first.

## 1. Premise

From Regino of Prüm (c. 906) to the Milan trials (1384, 1390), churchmen describe the same belief, held mostly by women. On set nights they go out in spirit, while their bodies lie in bed, in a great company of women following a Lady:
- **Her names:** Diana or Herodias in the clerics' Latin; Holda on the Rhine; Abundia and Satia, Dame Abonde, in France; Madonna Oriente in Lombardy; Percht in Bavaria after c. 1350.
- **What the company does:** it visits houses at night, eats and drinks what is left out without lessening it, and blesses the clean, orderly and generous houses with abundance.
- **The knowledge it gives:** in the later trials, women of the company are consulted for healing and finding things.

The Church called this a demonic illusion and gave penance, not death, until the early 14th century. It was then recoded, through Lombardy and the Alps, into the devil-worshipping "sect" of the first witch trials (Valais 1428).

The faith is a **household devotion**, not a church: the laid table, the night journey in spirit, the Lady's blessing. Its daughters are women the Lady counts among her company. **The Good Ladies are not "witches"** in the faith's own voice. "Witch" is the accusers' word, and becomes their whole case after c. 1430.

**Why it is not Murray.** There is no surviving pagan religion, no coven, no horned god, no sabbat. Those are the accusers' fantasy and Margaret Murray's discredited thesis. The faith rests only on what the clerical sources describe: a belief and its household practice. Vanilla CK3 already has a Murray-style witch: a secret `witch` trait, covens, novices, full-moon meetings and a "Witch God" (`events/witch_events.txt`). The Good Ladies must read as clearly different.

## 2. Attested, read, invented

| | What | Grade | Source note |
|---|---|---|---|
| **Attested** | The Lady and her company of women; set nights; travel in spirit while the body stays home; Diana/Herodias as the clerics' names; penance, not death | A, from c. 906 | `witch_papers_and_timeline.md` §3; Hutton p. 164 |
| **Attested** | Holda (Rhine, c. 1010); Abundia/Satia and the laid tables (Paris, 1230s); Berthold's table "for the blessed ladies" (Bavaria, 13th c.) | A | `witch_hutton_lecouteux.md` §2, §4 |
| **Attested** | Men as participants, as men (Pyrenees 1319; Stephen of Bourbon; the Milan dead) | A/B | `witch_hutton_lecouteux.md` §3 change 2 |
| **Attested** | Milan: "Madonna Oriente", the greeting, the staff that revives slaughtered beasts, blessing well-kept houses; first penance (1384), then death (1390) | A | Hutton pp. 172–73; Lecouteux ch. 11 |
| **Attested** | A Ghent satirist (c. 1148) expects his readers to know Herodias's endless flight, "a third of mankind" serving her, and her perching in oaks and hazels till cockcrow | B (lore known); C/D for "Pharaildis" as her name | `witch_ysengrimus.md` §4 |
| **Read** | Paris masters (1220s–40s): the soul can be away in its powers while the body lives; demons make only images | B (learned theory, not about the Ladies) | `witch_even_ezra.md` §3a–b |
| **Read** | Roland of Cremona (c. 1232–34): *cursus*, an ointment-driven night flight of "both men and women", which he keeps separate from the Ladies and half-credits as natural magic | A for the text; it is not the Ladies | `witch_cursus.md` |
| **Invented** | That daughters (trans women) belong to the company. No source puts anyone male-assigned in it *as a woman*. The faith says "the Lady decides who her women are." | design choice; label it | `witch_hutton_lecouteux.md` §4 |
| **Invented** | Any priesthood, holy order, scripture or organised hierarchy | design | (none attested) |

## 3. Faith setup (proposals)

### 3.1 Names
- **Faith:** *the Good Ladies* (Latin *bonae dominae*), the recommended working name. Alternatives: *the Lady's Table*; *the Company*. In the faith's own voice the Lady is the ***hera***, the mistress of the house (*Ysengrimus* II 90). That suits the table rite better than *domina*.
- **The Lady, by culture:** Holda (German), Abonde/Habonde (French), Oriente (Lombard), Herodias or Diana (clerical, and in every hostile voice). Percht only for Bavarian culture after c. 1350. "Pharaildis" only in a mocking cleric's voice.
- **Daughters:** a word of the faith's own is needed (open decision 3). Every faith keeps its own word (rule 6).

### 3.2 Religion placement and secrecy
- **A faith of the Christian religion**, not pagan. Believers were baptised Christians who also kept the Lady's nights, and the clergy treated them as erring Christians, not heathens.
- **Practised in secret** under a Catholic public faith, using CK3's secret-faith (crypto) mechanic: publicly Catholic, privately the Lady's. This matches the record. It is also the one faith of the seven to play this way, which serves the uniqueness memory.
- **No head of faith.** There is no church.
- **`doctrine_witchcraft_shunned`** (recommended; open decision 4). The Ladies' people healed and undid harm. They did not see themselves as sorcerers, and the Milan women counteracted *maleficium*. "Accepted" would invite vanilla's coven events and its "Witch God" into the faith.

### 3.3 Tenets (three; keys to verify against `tenet_types` when built)
1. **The Lady's Table** (custom): leaving food and drink out on the Lady's nights; uncovered vessels; the house kept clean and open-handed. Mechanic: a household modifier for abundance or stewardship, and a stress or piety benefit on the nights.
2. **The Body Keeps the House** (custom): going out in spirit while the body stays home, kept by the household. Mechanic: a short "gone out" state (no travel or scheme actions), then a memory of *having gone*, not of all that was seen (Even-Ezra pp. 61–67). Allowed by amended rule 25.
3. **One vanilla tenet**, to fit a hidden lay devotion of the household. Candidates to check against vanilla keys: a communal or charity tenet, or an esoteric one. Open decision 5.

### 3.4 Holy sites (baronies checked in `00_landed_titles.txt`)
| Barony | County | Why |
|---|---|---|
| `b_worms` | `c_worms` | Burchard's diocese, Holda (c. 1010) |
| `b_prum` | `c_aachen` | Regino's abbey (c. 906) |
| `b_paris` | `c_ile_de_france` | William of Auvergne's Abundia; Jean de Meun; Raoul de Presles |
| `b_milano` | `c_lombardia` | Madonna Oriente (1384–90) |
| `b_regensburg` | `c_regensburg` | Berthold's table for the blessed ladies |

Ghent (`b_gent`, `c_brugge`) is a "lore known here" county, not a holy site (`witch_ysengrimus.md` §6). `b_pamiers` (`c_toulouse`, 1319) is a possible fifth if Regensburg is too far east.

## 4. The gate (proposal; open decision 6)

**Going out with the Ladies.** The gate is one of the Lady's nights, in spirit, and the morning after.

1. **The night.** On a night of the Lady a Marked woman lies down, and a woman of the house keeps her body and the hearth (tenet 2). The faith holds that the Lady counts her among her women; the narrator does not confirm it.
2. **The table.** In the morning the mistress of a household that keeps the Lady's table sets her a place among the women, and calls her by the name she brought back. That is the recognition: by the *hera* of a house, not by a priest.
3. **Not tonight.** If no house sets the place, she may go out again on another night. Nothing is lost (rule 23). There is no test of pain, merit or stress (rule 22), and no oath "for ever".

**Uniqueness check.** Different from the knife, the völva's song (Bædling's odds), the gestation, the Adar fast, the pāvai vow and the smith; and from the Lambong's season of work and its feast. The Ladies' gate happens at night, in spirit, inside a household, and in secret.

**Standing that is not holy** (rule 7):
- the household's stewardship, *the mistress of a well-kept house*;
- the healer or finder the neighbours consult (the 1319 and Milan role).

## 5. The Church's response, by date (a hostile overlay, not the faith's self-image)

| Phase | Dates | What the Church does | Mechanic sketch |
|---|---|---|---|
| Illusion | to c. 1230 | Confessors ask the penitential's question (paraphrased: has she believed she rides with Diana?) and give penance | Penance events: piety cost, a fast; no trial |
| Tools forged | c. 1230–1320 | Mendicant preachers; masters dispute whether riders really go; the Amalrician template makes secret gatherings with ecstatic claims suspect | "A Master's Quaestio" event; regular gatherings raise suspicion earlier (`witch_even_ezra.md` §5) |
| Recoding | c. 1320–1430 | 1326 papal ruling on demon-summoning; Milan: the same story given penance (1384), then death (1390) | Lombardy and the Alps first; a second accusation of the same woman is graver |
| The sect | from c. 1430 | Valais, Nider: a sect of witches | Accusers' text may say "sect" and "night gatherings", never *sabbat*, *synagogue*, pact, familiar or broom (rule 25), and never castration lines |

The Rhineland and France stay mostly in the penance register, as the sources do (Hutton p. 174).

## 6. Events (sketch, 12)

1. **The Penitential's Question** (any date): a confessor reads Burchard's question. The answer is the player's: confess, deny, or "I believe it".
2. **The Lady's Table**: a household lays the table, and in the morning finds it blessed, or the vessels covered.
3. **The Body Keeps the House**: who watches her body tonight? A sister, a wife, a servant who might talk.
4. **A Master's Quaestio** (1215+): three positions: images, the soul away, "joy can stop the heart" (`witch_even_ezra.md` §5.1).
5. **The Satirist** (1148+, Flanders and the Rhine): a canon's comic verse makes the Lady a local saint. Droll, not lethal, but the butt is a poor old woman, and the player sees that (`witch_ysengrimus.md` §6).
6. **The Mummers** (Kalends or New Year): men in women's dress for a laugh. A daughter is no mummer. Rule 5 stands (`cracked_ivory_podcast.md` CI4).
7. **The Staff** (Lombardy): a beast slaughtered for the Lady's company is said to rise. The narrator does not confirm it.
8. **The Feigned Rider** (1210+): someone joins the household's nights to inform (the Amalrician spy, 1210).
9. **The Ointment Rumour** (1230+): a physician-friar is asked about flying salves and doubts them. No flight, no gathering, no sex, no recipe (`witch_cursus.md`). The Ladies' people answer that they need no salve: the body stays home.
10. **Lady Oriente's Greeting** (Milan, 1370s–90s): the greeting, and the question of who heard it.
11. **The Second Accusation** (1384+): the same story that once earned penance now earns the stake. Told from outside, with an open ending. A daughter may stand for the accused woman who would not have stood for her (`cracked_ivory_podcast.md` CI12).
12. **Kept from the Bride**: a daughter and a childless wife are kept away from a wedding together (CI3).

## 7. 1178 start setup (sketch)

- **No church, so no landed seat is required.** Seed secret believers (crypto) among courtiers in two or three of the holy-site regions. Recommended: Worms and Milan (the Lombard League's city, rebuilt 1167), with Paris as a third.
- **All seeded characters are fictional**, lowborn or in one fictional house. No historical person is converted or claimed. The 1178 holders of the counties above are to be read from vanilla history with the survey's parser before building.
- **A playable character** needs either a landless household (Roads to Power, which the mod already requires) or a fictional minor ruler. Open decision 7. Note that Ha-Nehpakhot's landless camp died out in run 15, before the camp fix.
- **Growth:** slow, by household and kin, with no size caps (memory). "A third of mankind serves her" is a doctrine boast, not a target.
- **Other starts:** 1066 works (Burchard is fresh; Rather of Verona gives an Italian foothold). 867 rests on inference: Regino writes c. 906.

## 8. Open decisions (recommendation first)

1. **Is a Latin folk faith a v2 faith at all, beside Japan and the Visayan House?** It is the strongest Latin candidate the project has found. The survey's Cathar "House of Good Women" conflicts with rule 25's Cathar clause. Recommended: a third v2 faith, or the second if the Visayan faith slips.
2. **Name:** *the Good Ladies* (recommended) / *the Lady's Table* / *the Company*.
3. **The daughters' word:** a vernacular word for the Lady's women. Recommended: *the Lady's women* in English loc, with a period word to be found (MHG *nahtvrouwen*, "night women", is attested for the spirits themselves; check before use).
4. **Witchcraft doctrine:** shunned (recommended) / accepted.
5. **Third tenet:** pick from vanilla keys when building.
6. **Gate:** going out with the Ladies plus the table (recommended) / the table alone (no night).
7. **Playable seed:** courtiers plus a landless household (recommended) / a fictional minor countess / courtiers only.
8. **Secret faith:** yes (recommended); it is the faith's distinct way to play.
9. **Where the persecution phase fires:** Lombardy and the Alps first (recommended, following Hutton p. 174) / everywhere at once.
10. **The army of the dead (Hellequin, Herla):** out of doctrine (decided by the evidence). Optional separate flavour event in Normandy or England, or none.

## 9. Sources (the six notes, all in this folder)

- `witch_papers_and_timeline.md`: Hollister (2022), De Lis (2021), and the pre-1453 timeline and verdict.
- `witch_studies_reader.md`: Chaudhuri and Ward, eds., *The Witch Studies Reader* (2025). Guardrails; little pre-1453 material.
- `witch_hutton_lecouteux.md`: Hutton, "The Wild Hunt and the Witches' Sabbath" (*Folklore* 2014); Lecouteux, *Phantom Armies of the Night* (2011). The core of §2–§3.
- `witch_ysengrimus.md`: Mann (1987) and Schilling (2020) editions; the Pharaildis passage.
- `witch_even_ezra.md`: Even-Ezra, *Ecstasy in the Classroom* (2019).
- `witch_cursus.md`: Even-Ezra, "*Cursus*" (*MRW* 12.3, 2017).
- Also: `../book_federici_caliban_witch.md` (rule 25's origin), `../cracked_ivory_podcast.md` (CI3, CI4, CI12), and `rykener_and_mobilities.md` (a Latin daughter's life, 1394, not witchcraft).

## 10. Guardrails (in addition to rules 1–26)

- No Murray: no coven, horned god, Old Religion, or continuity from paganism in any voice.
- No living community is the faith or its continuation: Wicca, Stregheria, heathenry, Leland's *Aradia*, Perchten runs.
- Accusers' fantasies (child-eating, devil-sex, orgy) appear nowhere, not even as allegation. Rule 25 already bans pact and sabbat. The cursus orgy is Roland's penitents' report, not the Ladies.
- If a death toll ever appears: about 40,000–60,000 executions for 1450–1750, nearly all after the game ends. Never "nine million".
- Joan of Arc is not claimed, and her gender is left unresolved. Rykener is not claimed.
