# Starts at 1066 and 1178: Sub-Saharan Africa (Sahel, Kanem, Nubia, Ethiopia, Swahili coast)

Research for the Silk & Silver bookmarks. Scope: the western Sahel (Ghana, Takrur, Gao, Malal/Mali, Sosso), Kanem, Makuria and Alwa, Zagwe Ethiopia, and the Swahili coast. Written 2026-10-20. Nothing in the repo was edited.

**What I read first.** `docs/faiths/badenya.md`; `docs/research/waf_gomez_african_dominion.md`; the West Africa and Horn sections of `docs/research/south_reading_list.md`; and grep passes over the other `waf_*` notes (Bulman, Conrad and Austen, Conrad and Condé, Ibn Khaldūn, Tarikh). `docs/research/sources_pending/` now holds only the Ayalon text. The al-Bakrī copy that `south_reading_list.md` cites as downloaded is gone, which fits the Launcher deletion recorded in memory.

**New primary checks made for this note.**
- **Al-Bakrī.** *Description de l'Afrique septentrionale*, trans. de Slane, revised edition (Algiers: Jourdan, 1913). Read in the archive.org text `fr103andalus05`, at the same pagination the repo uses. I saved a working copy to the scratchpad only.
- **Barth.** *Travels and Discoveries in North and Central Africa*, vol. 2 (1857). Read in archive.org `travelsdiscoveri21857bart`.
- **The vanilla game files**, in `history/` and `common/bookmarks/`, read directly from the local Steam install.

Grades follow the repo's convention:
- **PERIOD**: from a source written 867–1453.
- **BACK**: a later text with a datable core.
- **LATER**: 19th–21st-century ethnography or oral recording.

---

## 0. The short answer

| Date | Badenya verdict | Best new hub in the region |
|---|---|---|
| **1066** | **New start with new characters**, at Ghana's royal grove-town (al-Ghāba, `c_awkar`). Kirina stays a holy site and a hidden cell. | Ghana's al-Ghāba (*plausible*). For 1066 it is the strongest and best-documented hub in the whole region. |
| **1178** | **Same start (Kirina) with new flavour.** The host court is now Muslim. Ghana's grove has closed, and the Sosso smith-kings are the only pagan royal power nearby. | None strong. Sosso is *thin to plausible* as a second court. Kanem's queen-mother court and Makuria's *ngonnen* are *thin*: useful as reaction and flavour, not as hubs. |

Badenya should not be dropped at either date. Its parent "ancestral religion" (Gomez's term) is still the majority religion below the Sahelian courts at both dates. Al-Bakrī says so of Malal itself: "la masse du peuple est encore plongée dans l'idolâtrie" (p. 334). That is his hostile wording.

---

## 1. Verdicts for Badenya

### 1066: new start with new characters (move the court to al-Ghāba)

The test asks what changed in the host society's premises between 867 and 1066. Four things did.

1. **The seat's host changed religion.**
   - Al-Bakrī, writing in 460/1067–68, describes the king of Malal ("Melel"; usually identified with early Mali or the Manding, *identification is modern*) as having converted after a Muslim guest's rain-prayer.
   - The king then "fit aussitôt briser toutes les idoles de ses états et expulser les magiciens". He and "sa postérité et ses intimes" stayed Muslim, and the royal title became *al-Muslimānī* (pp. 333–334). The conversion is undated, but it came before 1068.
   - Vanilla agrees. It gives `c_sibi_mali` and `d_manding` in 1066 to Lahilatoul Kalabi (161011, Keita dynasty 1030002), rite **Shafiʿi**, born 1045 (`history/titles/k_mali.txt`; `history/characters/malinke.txt`).
   - So in 1066 the court that holds Kirina is a Muslim court that has just expelled its ritual specialists. In 867 it was not. The faith's own design already names "the Malal precedent" as its threat (`south_reading_list.md` §West Africa, Candidate A, "The world"). At 1066 that threat is **in the past and holds the seat**.
2. **The one fully attested non-Muslim royal cult in the region is at Ghana, and it is attested at exactly this date.**
   - Al-Bakrī gives Ghana's king as Tenkamenîn (Tunka Manīn), on the throne since 455/1063. His predecessor Beci was his **maternal uncle**, because "l'usage et les règlements exigent que le roi ait pour successeur le fils de sa sœur" (p. 328).
   - The king's town, al-Ghāba ("la forêt, le bocage"), is ringed with groves that house "les magiciens de la nation, chargés du culte religieux", their idols and the kings' tombs. Guards keep everyone out (p. 329).
   - The interpreters, the treasurer and most viziers are **Muslims** (p. 329).
   - Only the king and his heir, "le fils de sa sœur", may wear sewn clothes. "Le roi se pare, comme les femmes, avec des colliers et des bracelets" (p. 329).
   - The audience opens to the *deba* drum. The king's co-religionists kneel and throw dust on their heads; Muslims clap (pp. 329–330).
   - Kings are buried under a dome with their goods and servants, and a tumulus is raised over it (p. 330).
   - Every premise Badenya rests on is here in one PERIOD source of the bookmark year: the sister's line, a guarded house of ritual specialists, and a king whose regalia an outsider calls women's. The 867 start has these only by projection.
3. **The faith's sister's-line holy site becomes the court itself.** In 867 Awkar is a holy site remembered for the sister's son. In 1066 the sister's son is reigning there, and the reigning king's mother is the late king's sister.
4. **The Almoravids are next door.** The movement is active in the desert. Al-Bakrī also records Takrur's Islamisation under Wār Jābī (d. 432/1040–41) and the king of Silla's constant war on unbelievers (p. 324). A daughter's neighbours in 1066 are a ring of newly Muslim courts around one pagan kingdom.

**Why this passes the user's test.** The change is not that Ghana existed in 1066; it also existed in 867. The 1066 start can be built on an eyewitness-grade description of the **exact court and reign**, with the sister's line working in real time and a grove of ritual specialists under guard. It also comes at the moment just before that order is said to end (§4). That changes who holds the seat, the host's gender order, and the institution the House lives inside.

**Caveats for the narrator.**
- Al-Bakrī wrote in al-Andalus and never went south. His informants are not all named here. "Comme les femmes" describes jewellery and is not evidence of gender crossing (already flagged in `south_reading_list.md`).
- No *jeli* is attested at Ghana. The 1068 audience has interpreters, a drum and viziers, nothing more. The "word" step would rest on the royal audience and the drum, with the bard as a backward reading from Mali in 1352. The narrator must say so.
- Ghana's people are Soninke, which is a Mande language but not Maninka/Bamana. *Badenya* is a Maninka/Bamana term. Whether Soninke has an equivalent is **unverified** and needs a speaker.
- **Vanilla error.** Vanilla makes Bassi (161000) Tunka Menin's **father** (`history/characters/soninke.txt`). Al-Bakrī says maternal uncle (p. 328). A mod start can correct this in its own characters, or the narrator can note it.
- Vanilla's `west_african_bidu_pagan` (Ghana's faith in vanilla) rests on the Wagadu/Bida serpent legend. That legend was recorded in the 19th–20th centuries (LATER), not in al-Bakrī.

### 1178: same start (Kirina) with new flavour

- **Who holds the seat.** Vanilla 1178 makes Kirina's lord **Maghan Kon Fatta** (161018), Shafiʿi and Malinke, a vanilla 1178 challenge character. He holds `c_sibi_mali` and `c_tabon` under `d_manding`, and in 1176 married **Sassouma** (161019). Sogolon (161021) is born in 1190, and Mari Djata in 1217 (`common/bookmarks/challenge_characters/00_challenge_characters.txt`, l. 1257 ff.; `history/characters/malinke.txt`).
  - These are **epic figures**, recorded 1889–1994 (`waf_bulman_corpus.md`). The project must not make any of them a daughter or a claiming mother.
  - The seeding script `tm_seed_foothold_effect` (`common/on_action/tm_on_actions.txt` l. 315) will place the faith at **his** court. Check that it does not convert or displace a challenge character.
- **What changed since 867.**
  - **The court is Muslim.** This is the same change as in 1066 and is already true at 1066.
  - **Ghana's grove has gone.**
    - Al-Zuhrī (writing c. 1137–54) says Ghana's people became Muslim in 469/1076–77. Al-Idrīsī (1154) describes Ghana as a Muslim kingdom (both via Levtzion and Hopkins 1981; page numbers **unverified** here).
    - Whether this came by Almoravid conquest is disputed. Conrad and Fisher, "The Conquest That Never Was: Ghana and the Almoravids, 1076", *History in Africa* 9 (1982) and 10 (1983), find no unambiguous evidence of conquest in the Arabic sources and none in the oral sources, which stress drought instead. See also Masonen and Fisher, "Not Quite Venus from the Waves", *History in Africa* 23 (1996).
    - Conquest or conversion, the 1068 grove-cult at the royal centre is no longer the state cult in 1178.
  - **The Sosso.** Ibn Khaldūn (1380s) records that the Sosso conquered Ghana and were in turn conquered by Mārī Jāṭa (*Histoire des Berbères* II, pp. 110–111; `waf_ibn_khaldun_mali.md`). He gives no dates.
    - "Kanté seize Sosso c. 1180" is **Delafosse's** chronology (*Haut-Sénégal-Niger*, 1912), built from oral tradition. Treat it as unreliable.
    - Gomez puts Kirina c. 630/1233 (Gomez 2018, ch. 5). A Kanté smith dynasty at Sosso in 1178 is possible, not attested.
    - Vanilla has the Kanté of Soso (dynasty 2001183, `west_african_bidu_pagan`) unlanded, with only a 1066 pressed claim on `c_soso` (`history/characters/soninke.txt` l. 843 ff.).
- **Why not a new start.**
  - The faith's institutions in 1178 are those of 867: a Mande lord's court, smiths and bards.
  - Its key texts (Ibn Baṭṭūṭa 1352; the epic) lie as far ahead of 1178 as of 867.
  - The epic's women (Sogolon, Kolonkan, Nana Triban, Tenenba, Kosiya Kante) all belong to the generation **after** 1178 in vanilla's own dating. 1178 gives no new texts or institutions and changes only the neighbours.
  - So: new flavour, not a new start.
- **The flavour 1178 needs.**
  1. An event chain, "The Grove Is Closed": Awkar's holy-site text changes after 1076 ("where the heir was the sister's son, until the year 469").
  2. The Sosso as the one nearby pagan royal power (see §2C).
  3. A Maliki-jurist reaction strengthened for a court converted generations ago.
  4. Narrator framing: Sunjata's parents are already at the Kirina court, and the epic that will make them famous is six centuries in the future.

---

## 2. Candidate hubs in the region

### A. Ghana: al-Ghāba, the royal grove-town (`c_awkar`, barony `b_kumbi`). 1066 only. **Plausible.**

- **Attested basis (PERIOD, al-Bakrī 1068):**
  - succession through the sister's son, with a dated case (Beci to Tenkamenîn, 455/1063) (p. 328);
  - a guarded grove-precinct of ritual specialists, with the idols and the royal tombs (p. 329);
  - Muslim interpreters and viziers in a non-Muslim court (p. 329);
  - regalia an outsider calls women's (p. 329);
  - shaved men and women with shaved heads, which is al-Bakrī's gender-marking of the court (p. 329);
  - royal burial in a domed tumulus (p. 330).
- **What is missing.**
  - There is no gender-crossing evidence.
  - Smiths are not named among the "magiciens"; reading them as smiths is BACK, from the Mande smiths-as-earth-experts material in Jansen 2018, pp. 9–11.
  - No bard is attested at Ghana.
- **Why it beats Kirina for 1066.** Every pillar of Badenya's "line" is here as a functioning institution in the bookmark year, not as a remembered custom.

### B. Do (al-Bakrī's "Dou"). 1066 secondary. **Thin to plausible.**

- Across the river from Iresni lies "un grand royaume ... dont le souverain porte le titre de dou", whose people fight with arrows (al-Bakrī p. 333). Behind it lies Malal.
- It is already a Badenya holy site, with medieval tumulus fields (Bulman et al. 2023, p. 18).
- In 1066 it is the nearest **non-converted** Mande-zone kingdom to Malal. The epic makes it the Condé sisters' homeland, but that is LATER.
- A good refuge or cell, not a seat: it has no attested internal institutions.

### C. Sosso (`c_soso`), the Kanté smith-kings. 1178. **Thin to plausible.**

- **Basis.** A PERIOD people and polity in Ibn Khaldūn, with no dates.
- **The smith-kingship is epic (LATER).** In the epic:
  - Sumaoro is a smith-king, and smiths rise to rule (Gomez 2018, ch. 5, "Smiths and Societies in Motion": caste "in formation" in the 13th century);
  - a sister or her son is the price of the djinn's gifts in several versions (`waf_bulman_corpus.md`: the Nioro accounts, 1900–11; `waf_conrad_austen_sunjata.md`, pp. 206–207).
- **Appeal.** A smith-ruled court would make the gate's first step (the smith) the host's own institution, which is a real change of premise.
- **Problems.**
  1. The dating is Delafosse's.
  2. In the epic Sumaoro is the antagonist. He renames a bard by maiming (Conrad, in Austen (ed.) 1999, p. 36), and his 19th-century Koulikoro shrine excluded women (Bulman et al. 2023, ch. 2, p. 64).
  3. The Kanté are a living lineage (a *jamu*).
  4. Vanilla gives them no land in 1178, so a start would mean inventing a landed Kanté ruler.
- **Recommendation.** Treat Sosso as a holy site or second court the House can reach (a smith-diviner from Sosso as a starter courtier), not as the seat.

### D. Kanem (`k_kanem`, Njimi). 1178. **Thin** as a hub; strong as flavour.

- **Attested basis.**
  - The *Dīwān* of the Sayfawa kings records each king's **mother and her clan**. Hume (Ḥummay), the first Muslim *mai*, was "son of ʿAbd el Jelīl and Tikramma, of the tribe of the Kaye" (Barth 1857, vol. 2, Appendix, chronological table, p. 635).
  - Barth: kings were known "always after the name of their mother", and the mother's tribe is added "as a circumstance of the greatest importance". His example is Dunama Dibalami, named for his mother Dibala (vol. 2, ch. 29; the archive.org copy's running page is OCR-damaged, c. pp. 206–207).
  - **Fasama/Fasame, mother of Biri I.**
    - Barth: "entirely under the influence of his mother, who even imprisoned him". He adds that "part of the ceremonial of the court dates from his time, even if through the influence of his mother" (vol. 2, p. 635).
    - Barth also cites her as "Gumsu Fasami, who imprisoned her son Biri, when already king, for a whole year", and gives "Magira" as the queen mother's "native title" (ch. 29).
    - Biri's death is c. 1176/77. Lange 1977, pp. 68–70 is cited for the episode (via Wikipedia, "Fasama"; Lange's text **not seen**).
  - **The Dīwān's date.** Its writing began probably in the 13th century. King-list dates vary by decades: Hume is 1075–86 in Lange (1984) but 1085–97 in Palmer and Urvoy (and 1086–97 in Barth).
  - The *magira* as a named office is attested from Barth's 19th-century informants and 16th-century chronicles; for 1178 it is BACK.
- **What it lacks.**
  - The court has been Muslim since c. 1075–97.
  - Gomez reports Kanem's reputation for exporting eunuchs (ch. 4), but I found no attested internal eunuch office before 1453. A hub built on eunuchs would also duplicate Adelphai Dorleyaiou.
  - There is no gender-crossing evidence.
- **Use.** In 1178 Kanem is the region's clearest **queen-mother court**: a mother who imprisoned a reigning king and shaped his ceremonial. That rhymes with Badenya's claiming mother. Use it for reaction and events: Kanem courts respect a claim by the king's mother. Do not seat a faith there.

### E. Makuria and Nobadia (Dongola, Faras, Qasr Ibrim). 1066 and 1178. **Thin.**

- **Attested basis (PERIOD).**
  - The Old Nubian title *ngonnen*, "sister of the current ruler and the mother of the future one", is attested for **Maria Iesousikol** at Qasr Ibrim, "probably 1155–c. 1180", in P. QI 3 32 (Browne 1991). The source is the Database of Medieval Nubian Texts, IMRef_5186. A later holder, Aserimari, is dated 10 Dec. 1333 (P. QI 4 68; IMRef_5326).
  - "Martha, queen mother", late 11th century, appears in a Faras Cathedral wall painting under the Virgin's protecting hand (National Museum, Warsaw; date per museum literature, **page unverified**).
  - Ruffini, *Medieval Nubia: A Social and Economic History* (OUP 2012), discusses women's prominence in land sales alongside their role in royal succession (pages **unverified**).
  - Medieval Arabic writers report succession through the sister's son (Tsakos 2021, per `south_reading_list.md` §Horn item 6).
- **1178 pressure.** Tūrān-Shāh (Shams al-Dawla) sacked Qasr Ibrim in Jan. 1173 and turned its church into a mosque. His commander al-Kurdī may have killed the bishop of Faras (Wikipedia, "Turan-Shah's Nubian campaign", citing the Qubbat al-Hawa inscription; secondary, **unverified**).
- **Lacks.** The earlier sweep found no gender-crossing evidence and no eunuch office; a refuge at Ibrim was judged "only a weaker Adelphai Dorleyaiou" (`south_reading_list.md`, Candidate C). Nothing found here changes that.
- **Use.** Reaction (a Miaphysite court that honours the king's sister as the heir's mother), and possibly a flavour line for Badenya's sister's-line doctrine. No start.

### F. Zagwe Ethiopia (Lasta / Roha). 1178. **Thin.**

- Derat (2018) puts the dynasty's emergence in the 11th century, so in 1178 it rules.
- Lalibela's reign comes after 1178 (traditionally from the 1180s or c. 1204; dating **unverified**).
- The "Gold Beneath the Wax" candidate (`south_reading_list.md`, Candidate A) rests on:
  - the *Kebra Nagast* (c. 1314–22);
  - *qəne* (legendarily 14th–15th century, BACK);
  - Ewostatean double monasteries (14th–15th century);
  - Zärʾa Yaʿəqob's persecutions (1434–68).
- **All of that is after 1178.** At 1178, Lasta is only "the refuge before the Solomonic oath". That is a reason to keep Candidate A's era arc starting in the 13th–14th centuries, not to start there in 1178.
- The *Gädlä Lalibäla* is 15th-century hagiography, and Lalibela is a saint of a living church: never use him.

### G. The Swahili coast (Kilwa, Mogadishu, Shanga). **Thin.**

- Medieval sources (al-Masʿūdī, 10th c.; al-Idrīsī, 1154) and the Kilwa Chronicle (16th c., BACK) give dynasties and trade, not gender institutions.
- The Mombasa/Lamu *mashoga* literature (e.g. Shepherd 1987, in Caplan (ed.), *The Cultural Construction of Sexuality*) is LATER and concerns a **living community**. It may be context only, never a faith.
- I found nothing pre-1453.

### H. Gao (Kawkaw) and Takrur. **Closed or thin.**

- **Takrur.** Islamised under Wār Jābī (d. 1040–41) and at war with its pagan neighbours (al-Bakrī p. 324).
- **Gao.** The king is always a Muslim: "jamais ils ne confient l'autorité suprême à un autre qu'à un musulman". A new king receives a seal, a sword and a Qurʾān (al-Bakrī pp. 342–343).
- A single 10th-century palace eunuch at Gao (al-Muhallabī, via Gomez 2018, ch. 2) is not an office.
- **Avoid** al-Bakrī's neighbouring "Ed-Demdem", whose people he says eat strangers and worship a female-shaped idol (p. 342). It is a cannibal trope and must not become content.

---

## 3. Start sketches

### Sketch 1 (recommended): 1066, "The House in the Grove", al-Ghāba of Ghana

- **Seat.** `c_awkar` (`d_wagadu`, `k_ghana`).
  - Use vanilla's holder in 1066; Tunka Menin (161001, `west_african_bidu_pagan`) exists in vanilla history.
  - **Check in game** who holds `c_awkar`/`k_ghana` at 1066.9.15. I did not find its title history in `history/titles/`, and 161001 appears there only as holder of `c_jenne` and `c_tirakka` from 1062.
  - The House lives at the king's court, among the grove's ritual specialists, and holds no county. That matches the 867 rule ("the faith lives at that court") and keeps growth slow.
  - **Kirina** keeps the faith as a holy site, with one hidden Badenya courtier at Lahilatoul Kalabi's Muslim court.
- **Starter characters** (all fictional; names need a Soninke speaker; avoid clan *jamuw* as given names, per `waf_conrad_conde_sunjata.md`):
  1. **The claiming mother.** A fictional **sister of the reigning king**, so in Ghana's custom the mother of the next king. She is not Badenya. She is the court's most powerful potential claimer. Al-Bakrī names no royal women, so she is invented, and the narrator says so.
  2. **A Daughter of the House** (40–60), who made the crossing years ago. She is a keeper of the grove's tombs and an aunt (*badenya*) to younger daughters. She is the House's elder.
  3. **A Marked young courtier**, a page among the ten who stand behind the king with gold-mounted shields (al-Bakrī p. 329). She is the playable seeker.
  4. **A smith-diviner** from outside the grove, from Mande country to the south.
  5. **The Muslim vizier-interpreter** (al-Bakrī p. 329: the interpreters and most viziers are Muslims), the hostile voice. In his voice: the old custom of the sister's son is "a doubt about paternity"; this is al-Bakrī's own rationale, p. 328, put in a courtier's mouth.
- **Pressures.**
  - The Almoravid movement in the desert, and Takrur and Malal as converted neighbours.
  - **The Year 469 (1076–77).** A scripted crisis: the court converts (al-Zuhrī). Whether by conquest or not is left open (Conrad and Fisher).
  - **Drought**, which the oral sources stress (Conrad and Fisher 1983).
  - The grove's guards: "dès qu'un homme y est enfermé, on n'entend plus parler de lui" (p. 329). The grove is also the king's prison, so it is a refuge and a danger at once.
- **The gate.** Keep *Go to the Smith*, with two 1066-specific changes:
  - **The claim.** If the claimer is the king's sister, the claim carries the heir's mother's weight (bonus opinion with the heir).
  - **The word.** Spoken at the royal audience at the *deba* drum, where co-religionists salute with dust (pp. 329–330), because no jeli is attested at Ghana.
  - **Optional detail.** Only the king and heir wear sewn cloth (p. 329). A daughter is given a woman's wrapper at the audience; nothing is cut or sewn on her.
- **Existing mechanics that carry over.**
  - *Go to the Smith* → *Smith's Bargain* → *Hot* → *My Mother's Child* → bracelets → *The Word That Cools* (court-poet fallback needed, as already noted).
  - The *Mother's Children* tenet, *Take as Daughter*, *The Sisters Choose*, *A Naming Feast*.
  - *The House Buries Its Own*, which can echo Ghana's domed royal tumuli (p. 330) without copying the burial of servants.
  - After 1076, *The Djinn Returns* and the *New Roof* move with the House to Do or Kirina.
- **Grade.** The setting is PERIOD and exact to the year. The crossing is invented, as at 867.

### Sketch 2 (optional): 1178, "The Smith's Country", Kirina with a Sosso cell

- **Seat.** `c_sibi_mali` as now, at Maghan Kon Fatta's Muslim court. The seed must not touch Maghan, Sassouma or their line.
- **Starter characters** (fictional):
  - a Badenya elder in the household;
  - a Marked young woman of a smith lineage visiting from Sosso;
  - a Muslim *faqīh* at court, the hostile voice;
  - a Soninke woman of the old Ghana nobility, displaced after 469 and nostalgic for the sister's line. She is the claiming mother.
- **Pressures.** A Muslim lord for generations; the closed grove; the rising Sosso, a pagan court that values smiths but whose later epic reputation is hostile to women's rites.
- **The gate.** Unchanged. The smith may come from Sosso (bonus to the bargain, risk of a later Sosso claim on her).
- **Mechanics.** As at 867.
- **Grade.** Thin. Build it only if a 1178 "new flavour" pass is cheap.

---

## 4. Counter-evidence: what closed or worsened

1. **Court Islamisation.** Takrur by 1040–41 (al-Bakrī p. 324); Malal before 1068, with the idols broken and the "magiciens" expelled (pp. 333–334); Gao, where only a Muslim may reign (pp. 342–343); Kanem under Hume (c. 1075–97); Ghana in 469/1076–77 (al-Zuhrī). By 1178 every royal court in the region except the Sosso (and lesser southern chiefdoms) is Muslim at the top. Daughters face Maliki jurists at home courts, not only abroad.
2. **Ghana's grove ends between the two bookmarks.** The one PERIOD royal institution that matches Badenya's premises (the sister's line plus the guarded grove) is gone by 1178.
3. **Kanem's queen mothers are Muslim-court figures.** Fasama's power is real, but she acts inside an Islamic court. Barth's informants and later Bornu chronicles shape that record.
4. **Nubia's shrinking.** The 1173 Ayyubid sack of Ibrim, and afterwards the long decline of the church.
5. **Ethiopia after 1178** gets worse for the period the Horn candidate needs: the *Kebra Nagast* oath (c. 1314–22) and Zärʾa Yaʿəqob (1434–68). Nothing improves at 1178.
6. **The epic's verdict on smiths.** In the epic Sumaoro the smith-king is the antagonist, and the bards' Sunjata reorders society into freeborn, casted and enslaved (Bird, in Austen (ed.) 1999, p. 290). If the Sosso fall c. 1235, the smith-king model ends with them. That is still LATER evidence.

---

## 5. Dating cautions (do not project backwards without saying so)

- **The Sunjata epic.** Its present form is late 17th–18th century (Gomez: Mansa Saman of Kangaba; Austen: mid-18th century). It was recorded 1889–1994.
  - Sogolon, Nana Triban (verified only as Sunjata's half-sister in Niane), Kolonkan, Tenenba (1994, one bard) and Kosiya Kante (1990s) are LATER as evidence. In vanilla they are born after 1178 or never.
- **Sosso's dates** (Kanté c. 1180) are Delafosse's (1912). Ibn Khaldūn gives none.
- **The Kanem king-list.** Dates vary by 10–50 years; the *Dīwān* began in the 13th century. The *magira* as a title is from 16th–19th-century sources.
- **Mande ethnography.**
  - Brett-Smith's sculptor who "made himself a woman" (fieldwork 1976–84), Koné (2004), and the Koulikoro asylum (1819–1930) are LATER.
  - The *nyamakala* as a fixed caste is LATER. Gomez sees caste "in formation" in the 13th century.
- **Al-Bakrī** wrote from Córdoba. His Ghana is present-tense to 460/1067–68 ("le souverain qui les gouverne actuellement", p. 327), but it is second-hand.

---

## 6. Open questions

1. Who holds `c_awkar` and `k_ghana` at 1066.9.15 in vanilla? I could not find the title history. Is Tunka Menin landed there, and as what?
2. What does `tm_seed_foothold_effect` do at 1178, when Kirina is the capital of a challenge character (Maghan Kon Fatta)? Does it change county faith under him, and does that break the challenge?
3. Is there a Soninke term for *badenya*? It is needed if the 1066 House sits among Soninke. Ask a speaker.
4. Al-Zuhrī and al-Idrīsī on Ghana's Islam: the pages in Levtzion and Hopkins 1981 need checking.
5. Lange 1977, pp. 68–70 on Fasama: read the text itself, not only the Wikipedia summary and Barth.
6. The Faras "Martha, queen mother" painting: get the date and a catalogue citation (Warsaw National Museum).
7. Ruffini 2012 on Nubian women and land: get page references.
8. Is Malal = Manding/early Mali (and so the Kirina court)? Check Levtzion's argument (*Ancient Ghana and Mali*, 1973) before game text claims it.
9. Should the 1076 crisis be a scripted conversion of Ghana's court in the 1066 start, or left to the AI? This is a design choice; the scripted version would mean adopting a stance in the Conrad–Fisher debate.

---

## Sources used

**Primary sources in translation**
- al-Bakrī. *Description de l'Afrique septentrionale*. Trans. W. Mac Guckin de Slane. Rev. ed. Algiers: Jourdan, 1913. pp. 324, 327–334, 339–343.
- Barth, Heinrich. *Travels and Discoveries in North and Central Africa*, vol. 2. 1857. ch. 29; Appendix, chronological table, pp. 633–636.
- Ibn Khaldūn. *Histoire des Berbères*, vol. 2. Trans. de Slane. pp. 110–111 (via `waf_ibn_khaldun_mali.md`).
- Levtzion, N., and J. F. P. Hopkins (eds.). *Corpus of Early Arabic Sources for West African History*. CUP, 1981. Cited for al-Zuhrī and al-Idrīsī; pages **unverified**.
- P. QI 3 32 and P. QI 4 68 (Old Nubian documents from Qasr Ibrim), via the Database of Medieval Nubian Texts: dbmnt.uw.edu.pl, IMRef_5186 and IMRef_5326.

**Scholarship**
- Conrad, D. C., and H. J. Fisher. "The Conquest That Never Was: Ghana and the Almoravids, 1076." I: *History in Africa* 9 (1982); II: *History in Africa* 10 (1983): 53–78.
- Masonen, P., and H. J. Fisher. "Not Quite Venus from the Waves." *History in Africa* 23 (1996).
- Gomez, M. A. *African Dominion*. Princeton UP, 2018 (via `waf_gomez_african_dominion.md`).
- Lange, D. *Le Dīwān des sultans du [Kānem-]Bornū*. Wiesbaden: Steiner, 1977. pp. 68–70, **not seen**.
- Ruffini, G. R. *Medieval Nubia: A Social and Economic History*. OUP, 2012. Pages **unverified**.
- Derat, M.-L. *L'énigme d'une dynastie sainte et usurpatrice dans le royaume chrétien d'Éthiopie du XIe au XIIIe siècle*. Brepols, 2018.
- Bulman, Belcher and Vydrin (eds.) 2023; Conrad and Condé 2004; Austen (ed.) 1999; Jansen 2018 (all via the repo notes).
- Shepherd, G. 1987. In P. Caplan (ed.), *The Cultural Construction of Sexuality*. Context only.

**Game files** (CK3, local install)
- `history/titles/k_mali.txt`
- `history/characters/malinke.txt`
- `history/characters/soninke.txt`
- `common/bookmarks/challenge_characters/00_challenge_characters.txt`
