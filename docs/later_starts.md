# Later starts: 1066 and 1178

**Status (2026-10-20): not being built.** Work stays on the 867 start, kept current with *Silk & Silver*. This research is kept for later. If the mod comes to require the DLC that allows landless starts, several faiths could simply start unlanded in 1178, using the dossiers here. The seeding fixes below stay in, because players can still pick the vanilla 1066 and 1178 bookmarks.

A research summary, written 2026-10-20. *Silk & Silver* centres the 1066 and 1178 bookmarks. The question here is whether the 300 years after our 867 start changed **culture and gender politics** enough, anywhere on the map, to justify designing a new start or new starter characters. Notable events alone don't count.

Seven regional research passes covered the whole map, and their full notes are kept outside the repo (see *The regional notes* at the end). Each judged a change only if it altered a faith's or a hub's premises:
- who holds the seat;
- the host society's sex and gender categories;
- the institutions a community of trans women could live inside;
- the texts it reads;
- how law and neighbours treat its daughters.

Items marked *unverified* in the notes still need checking before any of this becomes script or loc.

## The answer in one table

| Faith | 1066 | 1178 |
|---|---|---|
| **Adelphai Dorleyaiou** | Same start, new flavour (eunuchs losing ground since 1057; Manzikert ahead) | **New start.** Dorylaion was abandoned for about a century and rebuilt by Manuel I in 1175 on a new site. The House is in exile at Kyzikos. |
| **Bædling** | **New start, new seat.** Gotland is Christian by c. 1050. Uppland and the Uppsala temple stay pagan under Erik "the Heathen"; seat the faith on Åland under his protection. | **Drop the landed seat.** Uppsala has an archbishop (1164), Norway outlaws sex between men (1164), and Þorlákr's penitential dates from 1178. A secret landless current trading with pagan Ösel is possible but thin. |
| **Yutai Dao** | Stand-ins, plus flavour (Tangut Shazhou already a Zhengyi lord's) | Same seat, new flavour: the *Wuzhen pian* (1075), Cao Wenyi's alchemy text, Huizong's renaming of the nüguan (1119–20). **Plus a new hub at Lin'an**, below. |
| **Ha-Nehpakhot** | Stand-ins, with loc dating fixes | Same seat, **new starter characters** and flavour: the archbishop's jurisdiction (1144) matches the licence mechanic, Rashi reads Dinah's sex as changed, the Tibbonids work at Lunel, and Barbarossa is crowned at Arles in 1178. |
| **Cūṭikkoṭutta Mālai** | Stand-ins, light flavour | **New start, new characters.** Temple women are at their richest and most named in 1178–1300 (Orr), with hereditary rights and bought singing rights. The foothold moves to Takkolam, because the Chola emperor holds Kanchipuram and Candragiri himself. |
| **Badenya** | **New start, new seat: Ghana's royal grove-town (`c_awkar`).** Kirina's court is Muslim by 1068 (al-Bakrī), while Ghana in that very year has every premise of the faith: sister's-son succession, the guarded grove, Muslim viziers. | Same start at Kirina, new flavour. Vanilla's Kirina is a challenge character, so the seed script must leave him alone. |

**In short:** 1178 is the stronger case. Four of the six faiths need a new start, new characters or a dropped seat there, and it offers the one good new hub on the map. 1066 needs new starts for only two faiths, Bædling and Badenya, both because their 867 seats had converted by then.

## A new hub: Lin'an (Hangzhou), 1178

This is the only new hub any pass rated better than thin, and it is worth a start. Its basis is Zhou Mi's *Guixin zazhi*, read in Chinese:
- **The quarter.** Outside Lin'an's New Gate lived people the source counts as men. They "wore powder and finery, were skilled at needlework, and were addressed as women".
- **A guild head with a duty to the courts.** They had a guild head titled 師巫行頭, whom the courts summoned to examine "not a man" (不男) suits.
- **A law against them.** A Zhenghe-era law (1111–18) punished them with a hundred strokes and paid informers fifty strings of cash. Zhou Mi says the practice already existed at Kaifeng in its heyday.
- **Corroboration.** The court troupe of 1165–89 lists a 裝旦, "the one who plays the woman". Lin'an also had women's and Daoist societies.

**Cautions:**
- **The source is hostile and late.** Zhou Mi wrote in the late 13th century, so placing the quarter in 1178 is an inference across about a century.
- **The source's own framing is prostitution**: the entry is headed 禁男娼, "banning male prostitutes", and speaks of 男子為娼. Reading these people as trans women is the faith's reading, in its own voice; the narrator must not make that claim. Zhou Mi's contempt, and the Zhenghe law, are attributed hostile voices.

**The fit:** Lin'an could be Yutai Dao's second house rather than a seventh faith. It would be an unlanded Sisters' House or, if *Silk & Silver* permits, a needlework merchant company, with the Jade Embryo gate carried over. The Zhenghe law becomes a denunciation threat during the gate. The East Asia notes sketch five fictional starter characters.

## Bugs in the stand-in seeding (fixed 2026-10-21)

1. **Gotland.** Vanilla makes it a Catholic republic at 1066 and 1178; the seeding converted its patrician. The seat now goes by date: Gotland before 1050, Åland from 1050 to 1089 (vanilla's Olaf is Norse pagan, under Erik "the Heathen"), and no land from 1090. A seat holder is converted only if already of the faith's own religion.
2. **Kirina.** From 1040 the seat holder keeps the county: no county is granted away, so the challenge character Maghan Kon Fatta (1178) and Ghana's king (1066) keep their titles and faith. The seat is Ghana's grove-town (Awkar) from 1040 to 1075, where only courtiers are seeded and the county keeps its faith.
3. **The Kanchipuram comment** now gives the holder by date.
4. **Phrygia** (found by the House in Exile dossier). At every start the old count of Phrygia was converted and given the daughter-of-the-knife trait; in vanilla 1178 that count is John Doukas, a historical figure. The takeover of Phrygia now runs only before 1080, after which Dorylaion is lost; from 1080 the Mother House starts landless, in exile.
5. **Ha-Nehpakhot dating.** Who judges in "Before the …" (`tm_hipukh.0003`) now follows the sources: the worthies of the street before 1215; the three rectors of the archbishop's 1215 ordinance (Ben-Shalom 2024, pp. 27–28; Gross 1897, p. 77); the baylons from 1386, the earliest dated in our sources (Ben-Shalom p. 69); the council from 1401 (Stouff §10). Before 1323 the text no longer implies a Purim dress custom, which Kalonymus is the first to attest. The licence to shun is still voiced as "the lord's", which holds at any date. The regional note's claim that before 1144 the count and archbishop licensed together is **not** in our sources and was not used.

## Considered and not recommended

- **The Islamic world.** It closes rather than opens between 1066 and 1178:
  - Ibn ʿAbdūn's Seville code (c. 1100) expels effeminate men from the city;
  - the Almohads attack "reversed" gender in their preaching;
  - Saladin dissolves the Fatimid palace in 1171;
  - Ibn al-Jawzī pushes Hanbali policing in Baghdad;
  - the *qalandar* dervishes come after 1200.

  The *mukhannathūn* troupes of Baghdad, Rayy and Isfahan, around 1066, are the region's best-attested role. They belong in the planned Rowson event pack, not in a start. An optional Adelphai starter set at the Fatimid court in Cairo in 1066 ("Through the Curtain") rates plausible as a court niche and gone by 1178.
- **The Byzantine sphere.** Constantinople's convents (where the Kecharitomene rule requires eunuch stewards), a house of lay virgins at Thebes, and Chonai are all plausible additions to Adelphai, not separate hubs. Norman Palermo, whose court was run by palace eunuchs, is strong as an institution and could be Adelphai flavour.
- **Latin Europe.** Worms, Lunel and Narbonne could be sister houses for Ha-N. The Cathars, Fontevraud, Hildegard and the troubadours are reaction and flavour only.
- **The North.** Rügen, Iceland, Ösel, Novgorod and the *skomorokhi* all rate thin. Cuman shamans are ruled out: the evidence is modern ethnography and leads into the "third gender" trap.
- **South and Southeast Asia.** Java is plausible to thin and unchanged since 867. The Kannada śaraṇas, Kashmir, Angkor and Bengal are thin. The bissu are a living community and stay out.
- **Africa.** Sosso could be a second court at best, and its dating is unreliable. Kanem (a queen mother who imprisoned the king), Makuria (the *ngonnen*) and Zagwe Ethiopia are flavour only. No gender-crossing evidence before 1453 was found anywhere in the region.
- **Japan.** *Torikaebaya monogatari* is usable as a text, but Japan offers no hub. *Shirabyōshi* are women in men's dress, and *chigo* are minors; exclude both.

## Suggested order of work

Steps 1 and 2 are done. Steps 3 and 4 are shelved (see *Status* at the top).

1. **Fix the four seeding bugs** above. They are small, and they affect the starts that already exist.
2. **Move the 1066 stand-ins** to the seats the research supports: Bædling to Åland under Erik the Heathen, Badenya to Ghana's grove-town. No 1066 bookmark is needed.
3. **Build one 1178 bookmark**, since the case is strongest there:
   - Adelphai, the House in Exile at Kyzikos;
   - Mālai at Takkolam;
   - Ha-N at Arles in the coronation year;
   - Badenya at Kirina, beside the challenge character;
   - Yutai Dao at Dunhuang, or its Lin'an house as an unlanded start.

   Bædling is absent or landless.
4. **Verify the flagged items** before writing loc. Chief among them are the date Dorylaion fell, Rāmānuja's dates and epithet, the Peel page mapping for *Guta saga*, and Cao Wenyi's dates.

## The regional notes

The seven regional passes are in [`research/later_starts/`](research/later_starts/) as `region_*.md`. Their quotations were checked against the short-quote rule; three long translations from Zhou Mi were cut to paraphrase and short phrases. The deeper dossiers on the chosen new starts (Lin'an, the House in Exile, Ghana, the *mukhannathūn* of Baghdad, Venice) go in the same folder.
