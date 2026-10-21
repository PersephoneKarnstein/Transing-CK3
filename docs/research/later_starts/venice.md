# Venice, 1066 and 1178: could the lagoon hold a start? Design reading

Written 2026-10-20 for the later-starts pass (`docs/later_starts.md`). The user likes the city and had no thesis about it. This note asks the user's question: does Venice in 1066 or 1178 change **culture and gender politics** enough to justify a new start or new starter characters, and not merely offer interesting events? If the answer is thin, it still sketches the best defensible version.

## Sources

**Read for this note**, from text extractions in the gitignored `docs/research/sources_pending/venice/`:
- Donald M. Nicol, *Byzantium and Venice: A Study in Diplomatic and Cultural Relations* (Cambridge: Cambridge University Press, 1988; pbk 1992). Archive.org scan `donald-m.-nicol-byzantium-and-venice-a-study-in-diplomatic-and-cultural-relations`, with the OCR's running heads giving print pages. Read: pp. 23–24 (San Zaccaria), 40 (the 992 chrysobull), 45–48 (Maria Argyropoulaina and Peter Damian), 51–52 (San Marco, Selvo's Byzantine bride), 58–64 (the chrysobull of Alexios I), 90 (Kinnamos on the Venetians), 96–106 (1170–1179, the arrests and their aftermath, Romano Mairano).
- Anna Rapetti, "Uscire dal chiostro. Iniziative di riforma e percorsi di autonomia di un monastero femminile (Venezia, secolo XII)", *Reti Medievali Rivista* 20.2 (2019), pp. 127–153, DOI 10.6092/1593-2214/6260. Open access. Read in full, with notes where they bear on persons and dates.
- Daniele Morossi, *Political and Economic Relations between Venice, Byzantium and Southern Italy (1081–1197)*, PhD thesis, University of Leeds, 2018 (White Rose eTheses 23526). Read only: pp. 35 (Selvo's marriage), 47 (the 960 slave-trade ban) and 85 (Dalmatian *servi* in Venice). The page numbers are the thesis's own.

**Read online** (Treccani's *Storia di Venezia*, chapter pages with no print pagination, so cited by chapter):
- Jean-Claude Hocquet, "Le saline", in *Storia di Venezia*, I, *Origini – Età ducale* (Rome, 1992). Read: the passages on 11th–12th-century owners of salt pans.
- Fernanda Sorelli, "La società", in *Storia di Venezia* (Treccani reports 1995; whether it is in vol. I or II is *unverified*). Read: the section on women's legal capacity, trade and wills, which is mostly 13th-century.
- Giuseppina De Sandre Gasparini, "La pietà laicale", in *Storia di Venezia* (1995). Read: the women's monasteries. It has almost nothing before 1200.
- Federica Ambrosini, "Cerimonie, feste, lusso", in *Storia di Venezia* (1996; the volume is *unverified*). Read: the Festa delle Marie, Giovedì Grasso, the Sensa, San Zaccaria, masks.

**Not read; cited second-hand and marked as such:**
- Edward Muir, *Civic Ritual in Renaissance Venice* (Princeton, 1981). Archive.org holds a lending copy only. The 1162 tribute is cited at p. 160 by Wikipedia's "Ulrich II of Aquileia" article. *Unverified* until read.
- Guido Ruggiero, *The Boundaries of Eros: Sex Crime and Sexuality in Renaissance Venice* (Oxford, 1985). Lending copy only. The Rolandina case is taken from the repo's own `hist_karras_medieval_sexuality.md` (E179), which reads Karras.
- Thomas F. Madden, *Enrico Dandolo and the Rise of Venice* (Johns Hopkins, 2003), and "The Chrysobull of Alexius I Comnenus to the Venetians: The Date and the Debate", *Journal of Medieval History* 28 (2002): 23–41. Known from the abstract and secondary reports only.
- Stanley Chojnacki, *Women and Men in Renaissance Venice* (2000); Linda Guzzetti, "Dowries in Fourteenth-Century Venice", *Renaissance Studies* 16 (2002); Dennis Romano, *Venice: The Remarkable History of the Lagoon City* (Oxford, 2024). Not read. Chojnacki and Guzzetti work on the 14th–15th centuries, and none of them is evidence for 1066 or 1178.
- Silvia Carraro, *La laguna delle donne. Il monachesimo femminile a Venezia tra IX e XIV secolo* (Pisa, 2015), and Irmgard Fees, *Le monache di San Zaccaria a Venezia nei secoli XII e XIII* (Venice, 1998). These are the standard works on the nuns. Known only through Rapetti's notes; the open copy of Carraro's thesis sits behind a Cloudflare wall.
- James H. Johnson, *Venice Incognito: Masks in the Serene Republic* (2011). The mask-law dates below come from popular sites that agree with each other, and should be checked against Johnson.

**Game files.** Vanilla 1.20.1 ("Crozier"): `history/titles/k_venice.txt`, `history/provinces/k_venice.txt`, `history/characters/cisalpine.txt` and `greek.txt`, `common/landed_titles/00_landed_titles.txt`, and the bookmark dates in `common/bookmarks/bookmarks/`. *Silk & Silver* is not yet released, so its content comes from `docs/silk_and_silver.md`.

**Relation to existing notes.**
- `docs/faiths/adelphai-dorleyaiou.md`, and the 1178 Byzantine sketch ("the House in exile" at Kyzikos) in the session's `starts_byzantium-anatolia-caucasus-levant.md`.
- `jud_phelan_slave_trade_motif.md` (rule 6: name Venetian, Frankish, Arab or Byzantine traders, never Jews), and `isl_el_azhari_queens_eunuchs.md` (El-Azhari p. 254: "Venetian slave merchants" in the Fatimid supply).
- `byz_liudprand.md`, for the eunuch envoy who travelled from Venice in 949.
- `hist_karras_medieval_sexuality.md` E179, for Rolandina Ronchaia (Venice, 1354).
- The Latin-Europe regional pass said nothing about Venice.

## 1. The argument and the evidence

### 1.1 The game's Venice at the two dates

- **Title and government.** `k_venice` is a kingdom-tier title under `republic_government` from 811. Its county `c_venezia` has a single barony, `b_venezia` (province 2517, a castle holding with the special building `doges_palace_01`). The neighbouring county `c_veneto` has Mestre (castle), Chioggia (city) and Malamocco (`b_malamacco`, no holding). Culture is `cisalpine`. The faith is `rite = roman_rite`, under 1.20's religion, faith and rite structure.
- **1066 (bookmark date 1066.9.15).** The holder is **Domenico Contarini** (char 7800, dynasty Contarini, born 1008; diplomacy 7; `education_diplomacy_3`). Vanilla gives him sons Iacopo, Andrea and Carlo and a daughter Ricciarda. Domenico Selvo (7802) succeeds in 1071. His Greek wife Theodora (9812, born 1058, `byzantine_rite`, greek) is a child in Constantinople in 1066, and he marries her in 1074. Buildings: `common_tradeport_02` and walls.
- **1178 (bookmark date 1178.10.1).** The holder is **Orio Mastropiero** (213600, born 1120; `just`, `diplomat`, `education_stewardship_3`), from 1178.4.13. Sebastiano Ziani died on that day; his son Pietro Ziani (32120) is alive. **Enrico Dandolo** (213601, born 1107) is alive and has the `blind` trait from 1176.10.1. `de_jure_liege = e_italy` is set in 1178. `c_venezia` has development 41 and `common_tradeport_03`.
- **No religious house appears on the map.** San Zaccaria, San Lorenzo and the patriarch of Grado have no title. The file lists patrician baronies (`b_dandolo`, `b_contarini`, `b_ziani` and others) only in comments, which suggests Silk & Silver's patrician houses will fill them.

### 1.2 Women's houses: San Zaccaria above all

**The founding.** San Zaccaria was built to house relics sent by Leo V about 819. The emperor endowed it, and it was "erected by Byzantine masons sent from Constantinople" (Nicol, pp. 23–24). Rapetti dates the ducal foundation to 828–829 (p. 128). Nicol tells two more stories:
- Doge Pietro Tradonico was murdered outside its church in September 864 (Nicol, p. 35).
- Maria Argyropoulaina, the Byzantine bride of 1004, was buried there with her husband and son after the plague of c. 1006–07 (Nicol, p. 46).

From its birth, then, the house is a Byzantine object in a Latin city.

**The twelfth century is the strongest material in this note** (Rapetti 2019):
- **A ducal monastery fought over.** Two Michiel women, Vita and Nella, held the abbacy from 1116 to 1141 (p. 133). When Nella died, the patriarch Enrico Dandolo, a reformer, claimed the right to consecrate her successor. Doge Pietro Polani claimed it as ducal patronage, and for a decade no abbess was elected (pp. 131–132). In November 1145 two *primiceriae* told the doge's court they could do nothing, "because they had no abbess" (p. 132 n. 15, quoting ASVe, San Zaccaria b. 7 n. 17).
- **Cluny, 1151.** The house adopted Cluniac customs and won papal protection (p. 130). The bull forbade receiving nuns who meant to keep personal property, and later bulls repeated the ban (p. 134). The new abbess, Giseltruda, was probably an outsider from the mainland, with no surname, and ruled for about 25 years (p. 133).
- **Enclosure, in name only.** Cluny's enclosure "continued to be largely ignored" by nuns and abbesses alike (p. 138). In 1181 Alexander III granted the house burial rights, because Venetians from other parishes wanted to lie there (p. 138).
- **1172–1175: the doge's murder reaches the abbey.** In 1172 Marco Caisolo killed Doge Vitale II Michiel, who had sought refuge, mortally wounded, in the monastery. In 1175 the nuns elected **Casota Caisolo, the killer's sister**. The vote split the house between two candidates and needed two papal delegates to settle (p. 143). In 1178, then, the abbess of the doge's own monastery is the sister of the man who killed the last doge but one.
- **The abbess as a political actor, 1195.** On 22 December 1195 Casota and four nuns sat before the *concio* of Verona, the podestà and the consuls. There they settled the Ronco all'Adige estate, a *castrum* with its *curtis* (pp. 138–141). The deed lists the women who signed, each with a cross: **13 veiled, 15 unveiled and 16 of unstated status**. Most bear patrician surnames (Falier, Da Molin, Dolfin, Bembo, Marcello, Cupo, Dauro, Steno). By 1209 the house had 64–66 members (pp. 143–144).
- **Lay sisters of high birth.** Rapetti floats, and does not prove, that high-born women entered as *converse* (lay sisters) out of the new piety (pp. 144–145). In the 1170s lay men and women of Monselice had bound themselves to the house as *conversi* (p. 145).
- **Rule by a working circle, not by office.** Casota governed through a working group of four nuns: Emerenziana Mastropiero "of a ducal family", Celestina Da Molin, Calandria Cupo and Imilia Falier. Calandria became abbess in 1199. No prioress appears at all (pp. 146–147). Rapetti's summary: three abbesses in succession, Giseltruda, Casota and Calandra Cupo, each ruled for more than twenty years and travelled the estates themselves (p. 149).

**San Lorenzo.** Founded under the will of Orso Participazio, bishop of Olivolo (13 February 854), for his sister Romana, its first abbess (secondary report, *unverified* against the charter). In 1169 Domenico Gradenigo left its abbess a large lagoon water, the *aqua Plancido* (Hocquet, "Le saline").

**Santa Maria delle Vergini** was a noble Augustinian house founded in the 13th century. A convent chronicle of 1523 ties it to the Peace of 1177. That is a later legend; the founding date is *unverified* (De Sandre Gasparini; secondary reports). A 1178 start must not place it on the map.

**What this means.** In 1178 Venice has a rich, patrician, half-enclosed women's community that negotiated with a foreign commune in its own name. It has lay sisters of several statuses, elected leaders, and an internal working circle. That is an institution "a community of trans women could live inside" in the same sense as the Kecharitomene in the Adelphai notes, with the same caution: **nothing attests a gender-crossing person in it**.

### 1.3 Women's property and legal standing before 1242

- **Salt pans** (Hocquet): in 1075 a widow and her children buy salt pans in the *fondamento* of Enrico Gradenigo. In 1188 Maria, widow of Zaccaria Bello, has recently bought rights in a salt pan, and Dansa, widow of Guido, holds one at San Pantaleon, Chioggia. The widow Petronia and her daughter Gysla inherit salt holdings from Pietro Enzio (12th century; exact date *unverified*).
- **Dowries in trade.** Romano Mairano "invested his wife's substantial dowry" in his ventures from 1153. After her death he married again, "again to a lady of means", in 1168, and built a three-masted ship with her money (Nicol, pp. 104–105, after Morozzo della Rocca and Lombardo, *Documenti del commercio veneziano*, 1940).
- **Legal capacity.** Sorelli's account of women's full rights over their own goods, guardianship, executorship (the *commissaria*), procurations and loans *ad negociandum* is drawn from 13th-century documents and the 1242 statutes. It cannot be pushed back to 1066 or 1178 without the earlier charters. Her named women (Smeralda Pagan, 1255; Agnese Gradenigo) are all post-1242. Treat the earlier position as **plausible but unverified**. The documents to check are the *Documenti del commercio veneziano* and the San Zaccaria fonds.
- **Women at the doge's side.** The *dogaressa* had a ceremonial office bound by a code of conduct, but the evidence is late, e.g. Dea Morosini's entry in 1471 (Ambrosini).

**Reading.** In both 1066 and 1178, widows hold salt, dowries capitalise trade, and abbesses run estates. That gives a Silk & Silver company of women good grounding. It says nothing about gender-crossing.

### 1.4 Festivals: what is attested, and from when

Dated strictly. Most of the popular "carnival" picture comes from the 13th to 16th centuries.

| Item | Earliest date with evidence | Source and status |
|---|---|---|
| **Giovedì Grasso tribute.** In 1162 Doge Vitale II Michiel captured Patriarch Ulrich of Aquileia and twelve canons. Their release cost a yearly bull, twelve pigs and loaves, slaughtered in public. The bull and the pigs stood for the patriarch and his canons. | **1162** for the war. The ritual's earliest *description* is later. | Muir 1981, p. 160, via Wikipedia (*unverified*). Ambrosini: the tribute ran until 1420; the "bull" was really an ox. |
| The word "Carnival" in a document of Doge Vitale Falier, **1094** | Popular claim | No scholarly source found. **Treat as unverified, probably a myth.** Do not use in loc. |
| **Festa delle Marie** (2 February, the Purification). Patrician houses of two parishes in rotation display twelve "Maries", processions go by water to San Pietro di Castello, and the poor are fed. | "From the 12th century" until its abolition in **1379** (Ambrosini). The wooden statues are attested by **1349**. Whether the Maries were living girls in the 12th century is *unverified*. The abduction-by-pirates story (dated 944 or 973) is a **15th-century legend** (Ambrosini). | Muir ch. on the Twelve Marys, not read. |
| **The Sensa** (Ascension): the doge marries the sea with a ring | The ritual grew from about 1000; the ring formula *in signum veri perpetuique dominii* comes from later sources. The story that Alexander III gave the ring in 1177 is a later Venetian myth. | Ambrosini; Muir, not read. |
| **Masks** | The first mask law is **2 May 1268** (masked men throwing scented eggs) | Popular sources; check Johnson 2011. |
| Masks banned in convents; painted faces, false beards and wigs banned | **1339** | Same. |
| Men barred from entering convents **dressed as women** | **24 January 1458** | Same. Post-1453, so out of the game's window. |
| Easter visit of the doge to San Zaccaria; the abbess Agnesina Morosini's gift of the ducal *corno* (9th century) | The visit is attested late. The *corno* story is a **legend**, probably compensation for land taken for the Piazza. | Ambrosini. |

**Reading.** There is **no attested masking or cross-dressing in Venice in 1066 or 1178.** What 1178 does have is (a) a mock-execution ritual that ridicules clergy as animals (1162–63 onward), (b) a February festival in which patrician women of a parish are on show and the poor are fed, and (c) the doge's annual wedding to the sea. All three are gendered civic rituals. None is a crossing.

### 1.5 Byzantium: an open road in 1066, a broken one in 1178

**1066.**
- **Venetians already trade in Constantinople** under Basil II's chrysobull of March 992 (Nicol, p. 40).
- **San Marco is being rebuilt by Domenico Contarini**, on the model of the Holy Apostles and under a master architect who "was a Greek from Constantinople" (Nicol, pp. 51–52).
- **The Greek bride.** The next doge, Selvo, will marry a sister of Michael VII, probably Theodora: in 1072 by Morossi (p. 35), in 1074 in vanilla. Byzantine historians are silent on the marriage; only later Venetian chroniclers record it (Nicol, p. 52).
- **A live hostile voice.** Peter Damian (d. 1072) told the tale of a Greek dogaressa who used a golden fork, perfumed her rooms and died rotting. He wrote it in his *Institutio monialis*, a work of instruction for a nun. Nicol identifies her as Maria Argyropoulaina (d. c. 1006) and rejects the identification with Theodora (pp. 46–47). The tale's moral: beware eastern ways, "lest the Orontes flow into the Tiber" (Nicol's paraphrase, p. 47). It is a Latin reformer's attack on a Byzantine woman's body and comforts, aimed at women religious, and current in the 1060s.

**The 1082 chrysobull.** Alexios I gave the Venetians wharves, warehouses and shops at Perama on the Golden Horn as freehold, and freedom from the *kommerkion* (Nicol, pp. 62–63). The date is disputed. Nicol keeps May 1082 (p. 59). Madden (2002) argues for 1092, the date both full Latin copies bear. A 1066 start sits before either date, so loc should say "Venetian merchants in the City", not "the Venetian quarter". Nicol himself says it may be "incorrect to speak of a colony or quarter" before the 1130s or so (p. 62).

**The rupture of 1171.**
- **Venetian life in the City.** By the 1150s, Kinnamos complains, Venetians "cohabited with Greek women and set up house with them beyond the limits of the Venetian quarter" (Nicol's paraphrase of Kinnamos, p. 90).
- **The arrests.** On **12 March 1171** Manuel had every Venetian in the empire arrested at the same hour: more than 10,000 in the capital, some "confined in monasteries". Romano Mairano escaped by night with a shipload of refugees (Nicol, p. 97).
- **The failed reprisal.** The doge's fleet died of plague at Chios. The doge was killed in Venice in 1172, at San Zaccaria as Rapetti specifies (Nicol, pp. 98–100; Rapetti, p. 143).
- **The release.** Merchants imprisoned in Byzantium were freed in **1179** (Nicol, p. 102, citing Morozzo–Lombardo nos. 303–314). Privileges came back only under Andronikos and Isaac II.
- **Dandolo's blindness.** Nicol has him "partially blinded" in a brawl on his embassy (p. 99). Madden argues for a later, progressive blindness from a head wound: his signature is normal in 1174 and illegible by 1176. Madden's pages are *unverified*. Vanilla's `blind` from 1176 follows Madden.

So in **1178 the road from Venice to Constantinople is shut**: Venetians are still in Byzantine prisons, and there is neither a quarter nor a chrysobull. The city is bitter towards the "wily Greeks" (Nicol, p. 98). Venice has just hosted the **Peace of July 1177**, when Barbarossa was reconciled with Alexander III, and Manuel was the one interested party not invited (Nicol, p. 103).

**The Adelphai link.** A Constantinople–Venice route for daughters of the knife is **open and plausible in 1066** and **closed in 1178**, with 1179 as its reopening. Both facts are useful. In 1178 the route's story is refuge: a Greek woman in a Venetian household who left with the arrested, or was left behind.

### 1.6 Slaves and eunuchs: handle with care

- **Venetian slave trading is real and early.** It is attested in the 8th–9th centuries (McCormick 2001, *not read*; Pope Zacharias freeing slaves bought by Venetians in Rome in 748, secondary). The *Pactum Lotharii* of 840 binds Venice not to buy Christian slaves in the Empire (secondary).
- **The bans.** Doge Pietro IV Candiano's ban of June 960 forbade ship captains to carry slaves or slave traders, or to buy slaves for Greeks (Morossi, p. 47, citing CDI no. 76). There may have been an earlier ban in 945 (Morossi, p. 47 n. 71).
- **Later presence.** Dalmatian *servi* appear in Venetian charters of the late 11th and 12th centuries, though "Venetian involvement in the slave trade is hard to demonstrate unequivocally" (Morossi, p. 85). In the 13th century enslaved women (*ancelle*) are freed and dowered in wills (Sorelli).
- **Eunuchs.** El-Azhari names Venetian merchants in the Fatimid supply (p. 254, repo note). Liudprand's *carzimasia* were made by "Verdun merchants" (*Retribution* 6.6). The eunuch envoy Salemon travelled with Liudprand from Venice in 949 (`byz_liudprand.md`). **No source read attests eunuchs living in Venice**, or the making of eunuchs there.
- **Rules carried over:**
  - Name Venetian traders when the provenance of a captive must be named (Phelan rule 6), and never attach any of this to Jews.
  - No Jewish character appears in any Venice slave or eunuch content.
  - The Venetian slave trade is backdrop, not a mechanic. The starters below have no part in it.

### 1.7 Counter-evidence: how the city policed sex and gender, later

All of this is **14th–15th century** and must not be backdated into a 1066 or 1178 start.
- **The Signori di Notte** handled sodomy until the scandal of 1406–08 moved it to the Council of Ten. A *collegium* on sodomy followed in 1418, and burning was the usual penalty (Ruggiero 1985, ch. 6, *pages unverified*; secondary summaries).
- **Rolandina Ronchaia, 1354.** A Venetian record describes a person "feminine in face, voice, and behavior", with "breasts like a woman", whom "many people thought ... to be a woman". Rolandina lived as a woman, did sex work, and was burned (Karras, via `hist_karras_medieval_sexuality.md` E179; Ruggiero, *unverified* page). Karras's reading is quoted in that note. **The narrator must not call Rolandina a trans woman.** The faith may claim Rolandina only in its own voice and only after 1354.
- **1458:** men barred from convents "dressed as women" (§1.4).

**Reading.** The best-attested trans-feminine person in medieval Italy lived in Venice, but 176 years after the 1178 start, and is known only because the city burned Rolandina. The Venice of the start dates had no such machinery that we know of. Its sodomy law and its night magistrates come later. A long game that reaches the 1350s could carry this as a late hostile turn (§3.6).

## 2. Verdict

**Thin as a start, and it does not pass the user's test.** Nothing in 1066 or 1178 Venice changes the sex and gender categories in a way a community of trans women could use:
- no attested gender-crossing person or practice before 1354;
- no masking before 1268;
- no eunuch institution in the city.

The festivals are real but are **reversal and display**, not a life.

**Plausible as an Adelphai daughter-house**, and better than most of the places the regional passes rated. Three things are strong and well dated:
1. **San Zaccaria, 1151–1195.** A patrician women's house with elected abbesses, lay sisters, a governing circle and its own diplomacy. In 1178 its abbess is the sister of the doge's killer (Rapetti).
2. **Women's capital.** Widows own salt pans, and wives' dowries finance the Constantinople trade (Hocquet; Nicol, pp. 104–105).
3. **The Byzantine road.** Open in 1066 (992 privileges; San Marco on the Holy Apostles; a Greek bride coming), broken in March 1171, reopening in 1179 (Nicol).

**By date:**
- **1066: plausible as a small optional starter set** riding the open road. The faith's premises do not change; only the place does.
- **1178: plausible as a refugee cell.** It is the stronger *story* (the closed road, the abbess, the Peace), but it has no new *gender* premise. Rate it as Adelphai flavour plus up to four starter characters, not a new bookmark.
- **If the user wants only one,** take 1178: it pairs with the Adelphai "House in exile at Kyzikos", and both stories are about a cut road.

## 3. Design reading

**Frame.** This is *not* a seventh faith, and *not* a Venetian current of a Latin faith. It is an **unlanded Adelphai Dorleyaiou house** at Venice, "the Lagoon House", whose daughters are Greek or Kybeline by origin and Catholic Venice's guests. A Venetian current of a Latin faith would be wholly invented, and §1 gives it nothing to stand on. The Adelphai already hold the cut to be women, already model their Houses on a typikon, and already have a Constantinople holy site.

### 3.1 Setting at the date, with vanilla holders

- **1178.10.1.** The doge is Orio Mastropiero (213600), elected that April when Sebastiano Ziani died. Enrico Dandolo (213601), 71 and blind since 1176, sits in the councils. Pietro Ziani (32120) is the rich son.
  - The Peace of Venice (July 1177) is a year old.
  - Venetians are still in Manuel's prisons until 1179.
  - At San Zaccaria, Abbess Casota Caisolo has ruled since 1175, after a split vote. Her working nuns include Emerenziana Mastropiero, of the new doge's family (Rapetti, p. 146; that she sat on this circle *in 1178* is an inference from the 1195 evidence).
  - In Byzantium, the Adelphai's mother house is in exile at Kyzikos (Byzantine pass).
- **1066.9.15.** The doge is Domenico Contarini (7800), 58, three years into rebuilding San Marco with a Greek master (Nicol, pp. 51–52). Venetians trade in Constantinople under the 992 privileges. Theodora Doukaina (9812) is eight and in Constantinople; she reaches Venice as dogaressa in 1074. Peter Damian is alive and writing.

### 3.2 Seat

- **Unlanded, with no new county.** `c_venezia` has one barony, and taking it would mean usurping the doge, which reverses history in the way the Gotland bug does (`docs/later_starts.md`, bug 1). `b_malamacco` is empty, and empty is historically right: the old Malamocco was lost to the sea in 1106–07 and its bishop moved to Chioggia in 1110 (standard dates, *unverified* page). Leave it empty.
- **With Silk & Silver:** a **merchant company with its Company Palace in `b_venezia`**, with the doge as **Patron**. Purpose: *Artisan* or *Reputable*, never *Creditor*. Goods with period grounding:
  - **Salt** (the widows' salt pans; Hocquet);
  - **silk cloth** (a Venetian carried Greek silks from Constantinople to Damietta in 1111; Morossi, p. 85);
  - **incense** (a hundred pounds of incense a year pledged to Cluny by Venetian donors in 1152; Rapetti, p. 136).

  The company head is a cis Venetian widow. The charter is the House's licence to exist under a Latin doge.
- **Without Silk & Silver:** the starters are **courtiers of the doge** (or of the widow's kin), as Ha-Nehpakhot's unlanded characters are. A `tm_lagoon_house` variable on `c_venezia` marks the House, as `tm_kahal` does at Arles.
- **Holy site:** none new. Constantinople is already eminent. San Zaccaria is a Latin house; the faith may *revere* it in its own voice, and the convent never becomes theirs.

### 3.3 Starter characters (fictional; 1178 set)

Names follow attested practice: Venetian women's given names from the 1145–1199 San Zaccaria and salt-pan documents (Rapetti; Hocquet), and minor attested surnames. No starter is a historical person, and none belongs to a family that held the dogeship.

1. **Eirene "of Perama"** (about 46). Kybeline culture, Adelphai faith, a daughter of the knife. She was cut as a child for a palace career that dried up under the Komnenoi, and taken as a daughter by the House as an adult (the Constantinople daughter in the Byzantine sketch has the same backstory). For twenty years she was steward of a Venetian merchant household near the Perama wharves. On 12 March 1171 she was not arrested, because the law counted her Greek. She sailed for Venice that autumn on a ship of returning traders, *not* on Mairano's night escape. The household counts her a eunuch. The House counts her a woman. She is the Elder Sister of the Lagoon House. Traits: stewardship-leaning; *Unbending Sisterhood*.
2. **Dansa Dauro** (about 52). Cisalpine, Catholic, a widow. She holds a salt pan at Chioggia and two shares in ships. The name pairs Hocquet's widow Dansa (1188) with a San Zaccaria surname (Dauro, 1195). She is the company head under Silk & Silver, or the House's lay patron. Her late husband's household was the one Eirene ran at Perama. **She is not of the faith.** She is the *Protectress* in the Kecharitomene sense: she guards the House and may not touch its goods. Under the Adelphai rules a Protectress comes from the founder's female line, so Dansa is a lay variant and needs a rule tweak (§3.7).
3. **Calandra** (about 16). Kybeline-Venetian, Adelphai, **Marked** (a trans girl the game codes as male). She is the child of a Venetian father and a Greek mother of the kind Kinnamos complains about. Her father was arrested in 1171 and is still in prison. The name comes from the 1195 list (Calandria). She cannot take the knife in Venice (§3.4).
4. **Imilia Aunario** (about 34). Cisalpine, Catholic, an unveiled member (status uncertain, perhaps a lay sister) of San Zaccaria. The surname is from the 1195 list (Aunario/Onario). She is **not** of the faith and is **not** a trans woman. She is the House's friend inside the convent, a source of letters and burial-ground favours, and its hostage to the abbess's politics. Including her shows the convent as a real neighbour without claiming it.
5. *Optional:* **Teodoro Bello** (about 40). Cisalpine, Catholic, a ship's master on the Halmyros run who waits for 1179. He is the route's carrier. The surname is Hocquet's Bello (1188).

**1066 variant.** Eirene is replaced by **Anna** (about 40), a daughter sent west in the household of Venetian merchants under the 992 privileges, to look for daughters among Greek women in Venice. Dansa becomes **Petronia** (Hocquet's widow) with her daughter **Gysla** as heir. Calandra's Greek mother is unchanged. There is no prison and no closed road. Instead, from 1074, a Greek dogaressa's household arrives in the city (Theodora, 9812). Whether her household included eunuchs is *unattested*, so do not assert it.

### 3.4 The gate

- **Keep the Adelphai knife** (Day of Blood, 24 March, then the Hilaria), with one rule: **no cut in Venice.** Venice has no Novel 60 and no tradition of physicians cutting, and a cut in Venice has nothing in the record behind it.
- **1178:** a Marked woman of the Lagoon House must **travel east** for the rite, to Kyzikos or Constantinople. That is impossible until the road reopens:
  - a global variable `tm_road_east_closed`, set at start for 1171–1179;
  - cleared by an event in 1179 that reads "merchants freed from the emperor's prisons" (Nicol, p. 102);
  - closed again by the 1182 massacre of the Latins (Byzantine pass), which is already in the Adelphai notes.

  Calandra's arc is the wait.
- **1066:** the road is open. A scheme-like journey on the Silk & Silver *Trade Opportunity* pattern takes her to the City and back.
- Adoption (*Take* or *Foster as Daughter*) works in Venice unchanged.

### 3.5 Pressures and hostile voices (all attributed)

- **Peter Damian** (1066): the dogaressa who ate with a fork and rotted, told to a nun (Nicol, p. 47). Use it as a preacher's sermon against "Greek" women in a patrician house.
- **Latin canon law on eunuch clergy**: Humbert's 1054 charge, "like Valesius" (Byzantine pass). It comes from a canon of Castello or the patriarch of Grado.
- **Kinnamos** (1178, from the Greek side): Venetians living with Greek women outside the quarter. It hits Calandra's family from the other direction.
- **The street in 1171–72**: "revenge upon the wily Greeks" (Nicol, p. 98). A Greek steward in a patrician house is suspect after the arrests. Keep this as popular opinion in a county modifier, not as a war.
- **Cluniac enclosure**: the 1151 bull forbids nuns personal property (Rapetti, p. 134), which cuts the convent's informal favours.
- **No antagonist nation.** The doge is a patron who can withdraw the charter. Under Silk & Silver that is the vanilla "abuse charter" risk run in reverse.

### 3.6 Event ideas

1. **"Twelve Maries"** (2 February, Purification). The House's patron's parish takes its turn. Dansa opens her house, and Calandra rides in the boat of the parish's unmarried women. Options: give alms to the poor (piety, popular opinion); keep Calandra home (stress). The date gate is honest only from the 12th century, and the boats and statues are later, so keep the desc to "the parish's maidens and their Marie". The pirate legend is 15th-century and stays out.
2. **"The Patriarch's Pigs"** (Giovedì Grasso, gated `current_date >= 1163.1.1`). The ox and the pigs are killed in the Piazza as the patriarch and his canons. An Adelphai elder remarks that the city dresses its clergy as beasts for a day and calls it justice. This is reversal flavour only, with **no masks** before 1268.
3. **"The Doge's Ring"** (Ascension). The doge marries the sea. The faith's reading, in its own voice: "The City is a bride every year, and nobody asks what she was born." Keep the formula and the papal-ring story out of the narrator's mouth; both are later.
4. **"The Abbess's Brother"** (1178–80; requires `tm_lagoon_house`). Casota Caisolo's house is split. Imilia asks the Lagoon House to carry a letter to Verona or Monselice. Options: help (opinion with San Zaccaria allies, risk with the doge's Michiel kin), or refuse. Use no dialogue for Casota. She is historical and appears only as reported action.
5. **"Freed from the Emperor's Prisons"** (1179, the road opens). Calandra's father may come home. A branch: he will not have a daughter. A second branch: he will. Do not frame it as a coming-out melodrama; follow the Adelphai's existing reaction templates.
6. **"The Fork and the Rot"** (1066 only). A canon preaches Damian's tale. The four Adelphai wing answers from `tm_byz.0001` carry over.
7. **Late game, after 1354 (optional, careful).** The House hears of a burning on the Piazzetta. Any text quotes the record, not the narrator, and contains no description of death. Gate it behind a game rule, given its weight. Never use the 1458 convent decree before 1458.

### 3.7 Mechanics that carry over, and new script

**Carries over:** the Adelphai knife, the three Houses, *Take* and *Foster as Daughter*, Sister-Making, *Cybele in Christian Clothes* (now with a Latin preacher), *Unbending Sisterhood*, growth by the call (Marked characters in Italy should hear it rarely; keep growth slow), and the suppression-ladder logic, retuned for a Latin lord.

**New script:**
- `tm_road_east_closed` (global variable; 1171–1179, again 1182–83), and a gate check in the Hilaria for Lagoon House members.
- A *Lagoon House* Sisters' House anchored to `c_venezia` by variable, since the House has no county of its own. This needs checking against how Sisters' Houses currently bind to counties.
- **A Protectress variant**: allow a non-member patron (Dansa) as Protectress when the house is unlanded. That departs from the Kecharitomene line rule and should be flagged in loc as the House's own compromise.
- **Silk & Silver (behind the DLC check):** a company start for Dansa, goods weights for salt, silk and incense, and no Creditor purpose. Venice is a vanilla **entrepôt**. If vanilla gives Venice a *Trade Post* in Constantinople at 1066, it is the quarter, and 1171 is its seizure; check that on release.
- **Bookmark seeding**: four or five characters in `history/characters/tm_characters.txt` with 1178.10.1 dates. **Do not touch** Mastropiero, Dandolo or the Ziani.

## 4. Attested / reconstructed / invented

**Attested** (in the sources read):
- San Zaccaria's Byzantine foundation (Nicol, pp. 23–24).
- Its abbesses Vita and Nella Michiel, the 1141–51 vacancy, Cluny in 1151, Giseltruda, Casota Caisolo elected in 1175 as the sister of Vitale II's killer, the Verona deed of 1195 with 44 signatories in three groups, the governing circle, and Calandra Cupo as abbess in 1199 (Rapetti).
- San Lorenzo's 1169 bequest, and widows holding salt pans in 1075 and 1188 (Hocquet).
- Mairano's use of his wives' dowries (Nicol, pp. 104–105).
- The 992 privileges, the 1082/1092 chrysobull and Perama, Kinnamos's complaint, the 12 March 1171 arrests, the 1172 murder, the 1177 Peace and the 1179 releases (Nicol).
- Peter Damian's tale (Nicol, p. 47).
- The 960 slave-trade ban (Morossi, p. 47).
- The Giovedì Grasso tribute from 1162 (Ambrosini; Muir via Wikipedia), and the Festa delle Marie "from the 12th century" to 1379 (Ambrosini).
- The vanilla holders and traits.

**Attested but late** (never backdate): masks (1268, 1339), the 1458 convent decree, the Signori di Notte and the Council of Ten on sodomy (1406–18), Rolandina (1354), the wooden Maries (by 1349), the Sensa ring formula and the 1177 ring legend, and Le Vergini (13th century).

**Reconstructed:**
- The Lagoon House as a Sisters' House shaped like San Zaccaria (a widow-patron outside, a working circle inside, members of several statuses).
- The closed road of 1171–79 as a rite gate.
- A Greek steward in a Venetian household in Constantinople, a type Kinnamos implies but no source names.

**Invented:**
- Every starter, and the Lagoon House itself.
- Any Adelphai presence in Venice.
- Eunuchs in Venice, of any kind.
- Calandra's mixed household.
- Dansa's stake in Eirene's former household.
- The faith's readings of the Sensa and the Pigs.

No source shows a person assigned male living as a woman in Venice before 1354.

## 5. Open questions

1. **Read Muir 1981** (pp. 135–181 on the Marie, the Sensa and the Giovedì Grasso). When is the bull-and-pigs ritual first *described*? Were the 12th-century Maries living girls?
2. **Read Fees 1998 and Carraro 2015.** Do any 12th-century San Zaccaria documents show the *converse* or unveiled women's status, or any oddity of naming or status? (Expect none.) Was Emerenziana Mastropiero already in the governing circle in 1178?
3. **Women's legal standing in the 12th century.** Check Sorelli's capacities against the *Documenti del commercio veneziano* (Morozzo della Rocca and Lombardo 1940) for women's colleganza and wills before 1200.
4. **Madden 2003** for the pages on Dandolo's blindness and the 1171 embassy; Madden 2002 for the chrysobull date. Loc should hedge "1082 or 1092".
5. **Johnson 2011** for the 1268, 1339 and 1458 mask laws, and Ruggiero for the Rolandina page and the earliest Venetian sodomy statute.
6. **Silk & Silver on release.** Does vanilla seed a Venetian Trade Post or quarter in Constantinople? Can a merchant company start in `b_venezia` with the doge as patron? Is the Carnival activity scriptable, so the Pigs and the Maries can hang on it?
7. **Malamocco.** Confirm the 1106–07 loss and the 1110 move of the see, since the empty barony is being used as evidence.
8. **Theodora Doukaina's household (1074/75).** Did a Byzantine bride's retinue include eunuchs (compare Maria Argyropoulaina's "servants" and "maids", Nicol, pp. 46–47)? If no source says so, the 1066 variant must not.
9. **Scope.** Is the user content with an Adelphai house rather than a Venetian faith? If they want something Venetian-born, the honest answer is that §1 supplies institutions (the convent, widows' capital, civic ritual), but no gender premise.
