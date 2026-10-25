# Visayan candidate (Cebu, 1178): dossier for 2.0.0

Builds on `docs/research/south_reading_list.md` §0–§2A (the Lambon sketch) and `docs/research/east_sea_bissu_baylan.md` §3. Checked 2026-10-24 against CK3 1.20.1.2 (Crozier) game files read locally and against open-access texts fetched for this pass. Nothing was saved from the fetches. Anything not checked here is marked *unverified*. Quotes are 25 words or fewer.

## 1. Verdict

1. **Viable, as a marked reconstruction.** Nothing about religion or gender in the Philippines survives from before 1521. 1178 sits 343 years before Pigafetta. The in-period anchors attest polities and trade only (rows 1–8).
2. **Under `dayawism_religion`, as a second faith beside vanilla `dayawism`.** Dayawism has exactly one faith, so a sister faith fits the way Ha-Nehpakhot sits beside Rabbinic Judaism.
3. **Landless first.** In 1178 b_PHI_Sugbu (Cebu itself) still has `holding = none`. The county belongs to a vanilla ruler, Sikatuna, who is fictional but carries a historical 1565 Bohol name. Start as a House at his court. Building a holding at Sugbu becomes a goal, or the mod adds one by a dated province-history entry (test whether `wanua_government` lets a baroness be his vassal).
4. **1178 suits this faith better than 867.** It is the decade of the P'i-she-ye raids on Quanzhou (1171–74, and frequent through 1174–90). It is also the year Zhou Qufei wrote that the world ends east of Java (row 5). Both give in-period flavour, and neither claims anything about gender.
5. **The gate's qualifying condition is femininity lived as womanhood** (Brewer: femininity as "the vehicle"; Ngu: asog femininity is no lesser femininity). It is not a third sex. That is the faith's reading in its own voice, and the narrator does not make it (see the Ngu nuance, row 29).

## 2. What vanilla gives at 1178 (CK3 1.20.1.2)

**Titles** (`common/landed_titles/06_philippines.txt`): `k_kabisay-an` › `d_PHI_visayas` (capital c_PHI_panay). Neither has a holder in history at any date, so the Visayan counts are independent.
- `c_PHI_bool_and_cebu` has four baronies:
  - `b_PHI_Bool` (Bohol, prov 11053): the first-listed barony, and so the de facto capital. It is `bisayan`, `rite = dayawism`, `tribal_holding`.
  - `b_PHI_Sugbu` (Cebu, prov 11054): **`holding = none`**, no culture or faith, no dated entries. It stays empty in 1178.
  - `b_PHI_Siaro` (11055): `holding = none`.
  - `b_PHI_Katugasan` (Siquijor, 11056): no province-history entry at all.

**Holders at 1178.1.1** (`history/titles/k_philippines.txt`, `history/characters/filipino.txt`). All are culture `bisayan` unless noted, and all counties have `wanua_government`, set at 867 or 978.

| Title | Holder id | Name | Born–died | Dynasty | Faith | Dev. 1178 |
|---|---|---|---|---|---|---|
| c_PHI_bool_and_cebu | bisayan_boolcebu_20_fic | Sikatuna | 1146.4.21–1197.3.8 | bisayan_dapita | dayawism | 22 |
| c_PHI_panay | bisayan_panay_20 (from 1170.1.1) | Balengkaka ("likely real ruler, but unsure when he lived") | 1146–1203 | bisayan_madyaas | dayawism | 17 |
| c_PHI_buglas (Negros) | bisayan_buglas_20_fic | Sipad (**aged 11**) | 1167.2.17–1226.3.18 | bisayan_mamayla | dayawism | 10 |
| c_PHI_tandaya (Leyte) | bisayan_tandaya_20_fic | Kanor | 1138–1189 | bisayan_leyte | dayawism | 11 |
| c_PHI_samar | bisayan_samar_20_fic | Kalawi | 1145–1183 | bisayan_ibabao | dayawism | 9 |
| d_PHI_butuan + c_PHI_butuan, c_PHI_calagan | bisayan_butuan_20_fic | Silongan | 1137–1190 | bisayan_bantuan | **shaivism** | 20 |
| c_PHI_tondo | tagalog_tondo_20_fic (tagalog) | Lawin | 1153–1209 | tagalog_tundok | **shaivism** | 22 |
| c_PHI_ma-i | tagalog_mai_20_fic (tagalog) | Abucay | 1162–1218 | tagalog_mait | **vajrayana** | 18 |

- Cebu-Bohol and Tondo share the highest development in the islands (22).
- *Sikatuna* is the name of the Bohol datu of Legazpi's 1565 blood compact. Balengkaka comes from the *Maragtas* tradition, a 1907 text whose antiquity Scott disputed (*unverified* here). The narrator should not claim either man, and the seed script should not convert either.

**Culture `bisayan`** (`00_malayic.txt`): `ethos_bellicose`, `heritage_austronesian`, `martial_custom_male_only`, `head_determination_domain`, `tradition_mystical_ancestors`.

**Religion `dayawism_religion`** (`religion_types/00_dayawism.txt`). Its only faith is `dayawism` (faith_types line 1427).
- **Doctrines:**
  - pagan hostility, polytheist, `doctrine_no_head`, `doctrine_gender_equal`, pluralistic, temporal theocracy
  - monogamy, divorce allowed, bastard legitimisation, cousin marriage allowed
  - `doctrine_homosexuality_accepted`, adultery accepted for both sexes, close kinslaying a crime, deviancy a crime, `doctrine_witchcraft_accepted`
  - `doctrine_clerical_gender_either`, clerical marriage allowed, clergy by temporal appointment, monasticism absent, sacraments absent
  - pilgrimage encouraged, `doctrine_funeral_stoic`, no anointment, oral storytelling
- **Virtues and sins:** brave, just and diligent; craven, arbitrary and lazy.
- **Tenets:** `tenet_ancestor_worship`, `tenet_mountain_worship`, `tenet_adorcism`.
- **Holy sites:**
  - Eminent: `pinatubo` (c_PHI_tondo) and `mantalingajan` (c_PHI_south_palawan).
  - Others: `cotabato` (c_PHI_cotabato), `ivatan` (c_PHI_ivatan) and `biri_larosa` (c_PHI_samar).
  - **None is in Cebu, Bohol or Panay.**
- **Localisation:** `dayawism_priest_male: "katalonan"` (female falls back to it) and `dayawism_priest_neuter: "babaylan"`. The god names are Tagalog: Maykapal, Lumikha, Lakapati, Ama-ni-Kable, Mayari. The religious symbol is "tigmamanukan".
- **A vanilla error to correct in the mod's own faith:** in the sources the *katalonan* is the Tagalog priest of either sex, and the *baylan/babaylan* the Visayan one (rows 15, 17).
- Province history uses `rite = dayawism`.

## 3. Evidence table

OA = open access. "Firm" means firm for the stated date and place. Every row is back-projected when used for 1178 unless it is in rows 1–8.

| # | Claim | Source (OA?) | Date, place | Grade |
|---|---|---|---|---|
| 1 | A Tagalog/Old Malay legal record of a debt release; it attests polities, titles and Indic loan law. It is said to name a daughter, Angkatan, as a party. | Laguna Copperplate; Postma 1992, *Philippine Studies* 40(2) (OA, philippinestudies.net); revised reading by Clavé & Griffiths 2022, *Philippine Studies* 70(2) (OA, HAL; not reached this pass) | 900, Laguna/Tondo | Firm for polity. *Daughter reading unverified* |
| 2 | Ma-i (Mindoro/Luzon) is in a Song trade edict of 972; its traders reached Canton in 982. | Scott 1983, "Filipinos in China before 1500", *Asian Studies* 21, pp. 1–2 (OA, asj.upd.edu.ph); Hirth & Rockhill 1911, p. 160 n. (OA, archive.org `chaujukuahiswork00chauuoft`) | 972–982, Song China | Firm (trade only) |
| 3 | Butuan's tribute missions: 1001 first, 1003 (red parrots), 1007 (Kiling asks parity with Champa, refused: "Butuan is beneath Champa"), 1011 (Sri Bata Shaja's gold-tablet memorial). | Scott 1983 pp. 3–4, appendix (Song huiyao ch. 197; Song shi ch. 488, 7–8) | 1001–1011, Butuan/Kaifeng | Firm (polity, trade, Indic titles) |
| 4 | P'i-she-ye raids on the Quanzhou coast at Shui-ao and Wei-tou "during the period shun-hi (A.D. 1174–1190)". Scott dates them to the monsoons of 1171–72. Their identity is contested: Zhao and Hirth & Rockhill put them off SW Formosa ("probable that they were of Philippine origin"); Scott says "more likely Filipino Visayans". | Zhao Rugua, *Zhufan zhi* ch. 43, Hirth & Rockhill 1911 pp. 165–166 (OA); Scott 1983 p. 5 (Wang Dayou biography; Quanzhou gazetteer 1612) | 1171–1190, Fujian | Event firm. **Visayan identity contested** |
| 5 | An account of overseas trade written in 1178 does not know the eastern islands: it "flatly says the world comes to an end just east of Java". | Zhou Qufei, *Lingwai daida* (1178), via Scott 1983 p. 6 and Hirth & Rockhill pp. 22–27 | 1178, Guangxi | Firm, **in the bookmark year** |
| 6 | Ma-i's trade: cotton, yellow wax, pearls, tortoise-shell and *yü-ta* cloth, exchanged for porcelain, trade-gold, iron censers and glass beads. Chiefs use white umbrellas. | Hirth & Rockhill pp. 159–160 | c. 1225, Mindoro/Luzon | Firm (not Cebu) |
| 7 | Cebu as a settlement and port from about the 10th century. The 2006 Plaza Independencia digs found burials and mostly Ming (14th–16th c.) tradeware; Song-era wares are in Cebu collections. | Nishimura 1992 (Michigan diss., not OA) via secondary; southeastasianarchaeology.com news (2006) | 10th–16th c., Cebu | *10th-c. date unverified*; 1178 plausible |
| 8 | Butuan plank boats (*balangay*): radiocarbon dates span roughly the 4th–13th c. | NHCP/NM reports | Butuan | *Dates unverified* |
| 9 | Pigafetta's hog rite at Cebu: "two very old women come, each of whom has a bamboo trumpet". They bow to the sun; one wears "a kerchief with two horns". | Pigafetta, B&R vol. 33 pp. 167–171 (OA, Gutenberg #42884) | April 1521, Cebu | Firm for 1521 |
| 10 | (Pigafetta, cont.) The horned one sprinkles wine on the hog's heart and spears it. The killer quenches a torch held in her mouth. The other marks with blood "first the foreheads of their husbands, and then the others". | same | 1521, Cebu | Firm. **The officiants are married women** |
| 11 | (Pigafetta, cont.) The two women "invite only women [to eat with them]". "No one but old women consecrate the flesh of the hog". | same | 1521, Cebu | Firm |
| 12 | (Pigafetta, cont.) The new convert burned an idol "certain old women had concealed in his house". Shrines "along the seashore … in which the consecrated meat was eaten" were destroyed. | same, p. 167 | 1521, Cebu | Firm; colonial scene, use only as flavour of shore shrines |
| 13 | Loarca on Panay: "the priestesses, or the men who perform this office, are also called *baylanes*". The priestess is possessed, prophesies on the sick and spears the hog. Sacrifices are made "only in case of sickness, and in times of seed-sowing or of war". | Loarca, *Relación*, B&R vol. 5, c. pp. 129–133 (B&R vol. 33 n. 335 cites pp. 131, 133) (OA, Gutenberg #16501) | 1582, Arévalo (Iloilo), Panay | Firm |
| 14 | **Cebu-specific cosmology.** The Yligueynes, "the people of Çubu, Bohol, and Bantay", go at death with Sisiburanen to a mountain "in the island of Burney"; Maguayen ferries them. The poor "who have no one to offer sacrifices for them" stay below. | Loarca, B&R vol. 5, same section | 1582, of Cebu-Bohol | Firm for 1582; **the only pre-1600 Cebu religion text besides Pigafetta** |
| 15 | Loarca: for the sick kin of the drowned, a *baylana* "who is a sort of priestess" leads them to sea, where a chest of robes is thrown in. The god Sidapa marks each newborn's span on a tree on Mt Mayas (Panay). | same | 1582, Panay | Firm |
| 16 | Plasencia: the *catolonan* "was either a man or a woman". The office was "held ordinarily by people of rank". The twelfth office, *bayoguin*: "a man whose nature inclined toward that of a woman". | Plasencia, "Customs of the Tagalogs", B&R vol. 7 (OA, Gutenberg #13701; p. 192 per Ngu/repo, *page unverified*) | 1589, Tagalog | Firm (Tagalog) |
| 17 | The Boxer Codex on the bayog: so effeminate "one who does not know them would believe they are women"; "marry other males". | via Brewer 1999 ¶13, ¶22; Ngu 2022 ¶13. MS at Lilly Library (images online *unverified*); trans. Souza & Turley 2016 (not OA) | c. 1590, Manila | Firm (mainly Tagalog) |
| 18 | Chirino: priests and priestesses "whom the Tagalos call *Catolonan*, and the Bissayans *Babailan*". The office is passed "through special friendship, or kinship, or as a legacy". The priest takes "the third part" of the offerings. | Chirino, *Relación*, B&R vol. 12 (OA, Gutenberg #15022; c. p. 270, per B&R 33 n. 335) | 1604, general | Firm |
| 19 | **A new Visayan witness.** Mentrida's Hiligaynon dictionary: "*Asog.* Ministros de los diwatas, que embiaban con recaudos á otros divatas, ó que los remaban" ("ministers of the diwatas, sent with messages to other diwatas, or who rowed them"). A second sense of *asog/umasog* is a barren animal (*machorra*). | Alonso de Mentrida, *Diccionario de la lengua bisaya, hiligueina y haraya de la isla de Panay* (OA, archive.org, Manila reprint, 1841 *unverified*), s.v. Asog | Composed before Mentrida's death in 1637 (*unverified*), Panay | Firm as lexicon |
| 20 | Lisboa (Bikol): asog "unaccustomed to marriage with women". | via Ngu ¶12, n. 1 | 1628, Bikol | Firm (not Visayan) |
| 21 | **A new Visayan witness.** Tapar of Iloilo went "in the garb of a woman, on account of the office of the babaylan". | Diaz 1667, via Ngu ¶20 | 1667, Panay | Firm; a revolt context |
| 22 | Alcina: in "ancient times" the asog "considered themselves more like women than like men". They wore the *lambon*; the "mute indian" of Sulat wove, made pots and danced as women did. The priestesses "were commonly women not men". | Alcina, *Historia* (1668), via Brewer 1999 ¶14–15, n. 81 | 1668, Samar/Leyte | Firm for 1668; Alcina back-projects |
| 23 | Alcina records bards still singing the romance of Datong Sumangga, who "made a raid on Grand China to win the hand of" Princess Bugbung Humayanun of Bohol. | Scott 1983 p. 6 and n. 13 (Alcina Pt 1, Bk 4, ch. 16) | Recorded 1668, Visayas | Firm as a 17th-c. song; *not datable to 1178* |
| 24 | Colín: at a chief's feast the catalona ordered "the girl of the best appearance and who was best adorned, to give the spear-thrust" to the hog. At weddings a catalona or babaylana kills a hog while the couple sit in old women's laps. | Colín, *Labor evangélica* (1663), B&R vol. 40, from p. 37 (OA, Gutenberg #30253) | 1663 (from Chirino/Plasencia), Tagalog | Firm (Tagalog) |
| 25 | **A hostile late voice.** "The bayòguin was an effeminate man [hombre maricon], inclined to be a woman and to all the duties of the feminine sex." | San Antonio, *Crónicas* (1738), B&R vol. 40, from p. 296 | 1738, Manila | Firm, hostile; copies Plasencia |
| 26 | Bolinao: 145 priestesses against 3 male ritualists who dressed as women only for rites. | Brewer 1999 ¶17, ¶29 | 1679–85, Zambales | Firm (Zambal, not Visayan) |
| 27 | Visayans saw three divinely sanctioned orders: datu, timawa, oripun. The timawa were the datu's kin and comrades. | Scott 1980, "Filipino Class Structure in the Sixteenth Century", *Philippine Studies* 28: 142–75 (OA) | 16th c. | Firm |
| 28 | Brewer: potency comes from "identification with the feminine – whether the biological sex was female or male" (¶34); femininity was "the vehicle to the spirit world" (¶38). | Brewer 1999, *Intersections* 2 (OA, ANU) | Scholarship | — |
| 29 | Ngu: "why should their performance of femininity be considered less than the performance of femininity by women?" (¶8). Ngu places asog in a liminal space, "more like women than like men", not a discrete third gender, and uses they/them (¶9). Babaylan rites had "masculine components" such as the spear (¶13–15). Seven early references (n. 1). Ngu gives no positionality statement. | Ngu 2022, *Intersections* 48, DOI 10.25911/EKER-DS41 (OA) | Scholarship | — |
| 30 | **Insider.** Alegre, a transpinay psychologist and gender-studies scholar, calls the asog her "TransCestors". The baylans or asogs are "reflective of our transgendered past". She also asserts a "matriarchal" pre-colonial society and repeats modern deity claims (Bulan and Sidapa as lovers; Lakapati as trans, from a blog). | Alegre 2022, "From Asog to Bakla to Transpinay", *Alon* 2(1): 51–64, DOI 10.5070/LN42156404 (OA, eScholarship) | 2022 | Insider voice on kinship; **her historical claims are not evidence** |
| 31 | Torres reads the asog as "the earliest representation of Cebuano gay identity". Priests described the asog as performing Satan's bidding by "spreading false news and stealing gold". The meaning shifted in the late 19th c. | Torres 2022, "Locating the Asog", *Humanities Diliman* 19(1) (OA journal; **abstract only read**, full text 404 this pass) | Scholarship | Closes the repo's open Torres lead (south list l. 882, 1241) |
| 32 | Wiesner: baylans were older married women "regarded as to some degree androgynous" because past childbearing. | Wiesner, *Gender in History*, p. 205 (repo row 107) | Outside synthesis | Conflicts with rows 28–29; don't build on it |
| 33 | 1970s Iloilo babaylan were mostly men; the shift is colonial-era. | McCoy 1982 p. 164 n. 10, p. 166 (repo) | 1970s | Late; shows the office changing |

## 4. Design hooks

**Faith.** `tm_lambon` (working name) in `dayawism_religion`, a sister of vanilla `dayawism`.
- Keep the gender-equal, homosexuality-accepted and witchcraft-accepted doctrines.
- Clergy female only, as in the other Sisters' faiths.
- Use "baylan" for the faith's own priest title (rows 13, 18), not vanilla's swapped pair.
- Tenets: keep `tenet_adorcism` (Loarca's possession, row 13) and `tenet_ancestor_worship` (redeeming souls, row 14). Replace `tenet_mountain_worship`: Cebu's dead go overseas to Borneo, not up a mountain. Choose a tenet that fits a feasting and trade economy (*check the 1.20 tenet list*).

**Gate: the Call, the Lambon, the Hog.** The Lambon sketch is kept, with three corrections.
1. **The Call is not a sickness.**
   - The sketch's sickness (catalepsy, madness) breaks writing rule 22: no gate may test her pain or require a misery event. McCoy's catalepsy evidence is also from the 1970s.
   - Use Chirino's three roads instead (row 18): a friend who teaches her, a kinswoman's legacy, or a diwata's summons in a dream.
   - She may refuse it ("Not today."), per rule 23.
2. **The Lambon** (row 22): a season of weaving, pottery and the women's dance. Progress counts work done, not tests passed.
3. **The Hog** (rows 9–11):
   - Two elder baylan, both married women (row 10), with trumpets and the horned kerchief. The horned one speaks to the sun, the other answers.
   - The spear stroke stays an old woman's act. That answers Ngu's "masculine spear" point inside the source: at Cebu a woman held the lance.
   - **Variant, Tagalog-sourced, mark it:** Colín's "girl … best adorned" gives the thrust herself (row 24).
   - Blood is marked on the husbands' foreheads, then everyone's. Then she eats with the women only.
   - The rite waits if two elders are not present, and it never fails.

**Offices and roads.**
- *Baylan* (holy): healing for fees, a third of the offering (row 18). Sacrifice at sowing and in war (row 13).
- **Rower of the diwata** (row 19, new): Mentrida's asog carried messages between the spirits. This becomes a court role for envoys and go-betweens, which suits a datu's diplomacy. It needs no invented Visayan word; use the English.
- **Non-holy roads** (rule 7):
  - A weaver of the cotton and *yü-ta* cloth sold into the Ma-i trade (row 6).
  - Standing as a timawa in a datu's household (row 27), or as a wife (row 17: the bayog "marry other males").
- **Line:** teaching passes by friendship, kinship or legacy (row 18). Bolinao's "only after they were married" (row 26) is Zambal; use it only as a soft weight.

**Holy sites** (new `tm_` sites):

| Site | Where | Basis |
|---|---|---|
| **Seat: Sugbu** | c_PHI_bool_and_cebu / b_PHI_Sugbu | rows 9–12, 14 |
| Panay | c_PHI_panay / b_PHI_Irong_Irong | Three Visayan witnesses: Loarca 1582, Mentrida, Diaz 1667 (rows 13, 19, 21); Mt Mayas and Sidapa's tree (row 15) |
| Samar | c_PHI_samar | Alcina's asog of Sulat (row 22); shares the county with vanilla's `biri_larosa` |
| Leyte | c_PHI_tandaya | Alcina's mission field; replaces Bolinao, which is Zambal (row 26) |
| Butuan | c_PHI_butuan | The Song tribute port, held by a Shaivite ruler (row 3): a contested site |

**Events.** The first six are Visayan; the last is Tagalog-sourced.
1. **The Hog of the Two Old Women** (rows 9–11): the gate rite.
2. **The Chest for the Drowned** (row 15): a family asks her to lead the sea offering. Funerals are a gap in the existing research, and this fills it.
3. **No One to Sacrifice for Them** (row 14): the poor dead of Cebu stay below unless someone offers for them. The House pays for the rites, a quiet sororal charity. Write it in the faith's voice, with no promise of deliverance (rule 15).
4. **Where the World Ends** (row 5, 1178 only): a Butuan or Quanzhou trader says Chinese books stop at Java. This is a trade-income and envoy event for the Rower of the diwata.
5. **Sumangga's Song** (rows 4, 23): a datu wants a raid on "Grand China" for a Bohol bride, and asks the baylan to sacrifice for the war (row 13). She may bless it, refuse, or bargain.
   - Keep the raid off-screen.
   - Never voice Zhao's rape or cannibalism text.
   - Never use the "dark as lacquer" complexion lines (as rule 12 bans race rhetoric for Badenya).
6. **Butuan's Envoy** (row 3; repo §1.6): the Shaivite court of Silongan would enrol her as a palace dependent in the Javanese *kĕḍi* manner. This is an in-period Indic outside voice that gives a dependent's place but not womanhood.
7. *(Optional, Tagalog-sourced)* **The Wedding Hog** (row 24): she marries a couple who sit in old women's laps.

**Outside and hostile voices in period.** All Spanish and friar voices (rows 12, 16, 25, 31) are post-1521 and stay out of the world before 1521. They may appear only in the narrator's source notes.
- **A Song coastal official.** Zhao's "the people go naked and are in a state of primitive savagery like beasts" is attributable, and unpersoning by shape. Use it sparingly.
- **The Shaivite courts of Butuan and Tondo** (event 6).
- **A Vajrayana Ma-i trader** (row 6): curious, not hostile.
- **Datus who want her blessing for a raid**: the pressure here is political, not doctrinal.

**What the Lambon sketch already covers, and what this adds or corrects.**

*Already covered:*
- The faith inside Dayawism, the three-part gate, the Sugbu seat.
- The spirit spouse as flavour.
- The risks: back-projection, revival movements, third gender.

*Added:*
- Rows 3–5: the 1178 hooks.
- Row 14: the Cebu afterlife.
- Row 15: the sea rite for the drowned.
- Row 18: the three roads of succession and the fee economy.
- Row 19: Mentrida's asog as rowers of the diwata.
- Rows 21 and 13: Diaz and Loarca as further Visayan witnesses.
- Row 30: an insider voice.
- Row 31: Torres, closing the repo's open lead.

*Corrected:*
- **Visayan witnesses.** The sketch says the asog is attested in the Visayas only in 1668. Mentrida (before 1637) and Diaz (1667) are Visayan too, and Loarca (1582) names men in the office without using the word asog.
- **The Call.** It should not be a sickness (rule 22).
- **Bolinao.** It is Zambal; swap it for Leyte or Panay.
- **The blood.** Pigafetta's blood goes to the husbands first (row 10). The sketch's "her forehead among the women" is an adaptation and should say so.
- **The 1178 start.** In 1178 Sugbu is still empty, and Sikatuna is vanilla's ruler. The sketch's "Islam in Sulu" late pressure is out of range; Song China and Butuan replace it.
- **Ngu.** The repo calls Ngu "she", but the article states no pronouns. Ngu supports the femininity reading, not "womanhood" as such (row 29).
- **The spirit spouse.** It is unsourced in anything read so far: *unverified*, flavour only.

## 5. Risks and handling

1. **Back-projection of 343 years or more.** Every rite text is dated 1521–1738. The narrator says so in the faith's description. The faith's own voice may say the old women were always there; the narrator never does.
2. **Living communities.**
   - The faith is never called "Babaylan". There is a babaylan-revival spirituality: "babaylan feminism" (Mangahas and Llaguno, eds., 2006) and Filipino-American groups such as the Center for Babaylan Studies (*unverified* current status). UP Babaylan, a long-standing LGBT student organisation (*unverified details*), also uses the word.
   - The bakla, bayot and transpinay communities of Cebu today are not this faith. Say so in the README line (rule 14).
3. **Third gender and the asog's gender.**
   - Qualify by femininity lived as womanhood (rows 28–29).
   - Never use "third sex" in the narrator's voice.
   - Don't claim all asog were trans women: Bolinao's dressed only for rites (row 26), and Torres reads the asog as gay (row 31). The faith claims those who lived as women, in its own voice.
   - Alegre's "transcestors" (row 30) supports the faith calling them **kin, not proof** (rule 19).
4. **Golden-past and modern-myth material.** Do not use:
   - Alegre's "matriarchal" pre-colonial society (rule 2);
   - Bulan and Sidapa as lovers: in Loarca, Sidapa measures lives (row 15);
   - Lakapati as a trans goddess (a blog source);
   - Wiesner's infertility-as-androgyny reading (row 32);
   - the *Maragtas* (Balengkaka) as history.
5. **Content to exclude.**
   - Zhao's raid text: rape and cannibalism.
   - The complexion lines (row 4).
   - Colín's slave sacrifice (B&R 40 §109).
   - Pigafetta's passage on genital pins, a body text (rule 5).
   - The Chinese "slave-raider" framing of Visayans as identity: Scott, citing a 14th-c. source.
   - No minors: Negros's vanilla count is 11 in 1178, so no events should target him.
6. **Historical names in vanilla.** Sikatuna, Balengkaka, Kiling and Sri Bata Shaja are names from the sources (row 3). The seed must not convert them or give them traits; seed fictional courtiers.
7. **A tolerant baseline.** Dayawism already accepts homosexuality and has equal gender doctrine. Distinctness comes from the rite, the sacrifice and feast economy, and the envoy office, not from persecution.
8. **Fonts.** The ASCII forms *baylan*, *asog*, *diwata*, *lambon*, *Sugbu* and *Sisiburanen* are safe. *Bayòguin* and *Çubu* need `tools/check_glyphs.py`; prefer *bayoguin* and *Sugbu*.
9. **Growth.** Use a small ethnoreligious pace, with no size cap (memory: growth tuning).

## 6. Books and articles to find (not open access)

1. **MUST FIND.** Francisco Ignacio Alcina, *History of the Bisayan People in the Philippine Islands: Evangelization and Culture at the Contact Period*, trans. Cantius J. Kobak and Lucio Gutiérrez, 4 vols. (Manila: UST Publishing House, 2002–2005).
   - *Chapters to read:* the volume on religion, idolatry and priests (Pt 1, Bk 3, *unverified*); the asog passage and the "mute indian" of Sulat; Pt 1, Bk 4, ch. 16 (the Sumangga romance).
   - *Answers:* the full asog text in context; whether Alcina says anything of the asog in Cebu; *diwata* possession and spirit spouses; the lambon and *bahaque*; women's work and dance; funerals.
2. **MUST FIND.** William Henry Scott, *Barangay: Sixteenth-Century Philippine Culture and Society* (Quezon City: Ateneo de Manila UP, 1994), ISBN 971-550-135-4 (*unverified*).
   - *Chapters to read:* the Visayan chapters on social structure, women and religion (babaylan, asog, diwata, the hog rite), *pages unverified*.
   - *Answers:* the best single synthesis of Visayan religion; Scott's reading of Pigafetta's rite; marriage, divorce, bride-wealth and inheritance; the datu, timawa and oripun ranks; women's dress and tattooing.
3. **MUST FIND.** Carolyn Brewer, *Shamanism, Catholicism and Gender Relations in Colonial Philippines, 1521–1685* (Aldershot: Ashgate, 2004), ISBN 0-7546-3437-9 (*unverified*).
   - *Chapters to read:* the chapters on the asog and bayog, the Bolinao manuscript, and women's ritual authority.
   - *Answers:* the full apparatus behind the 1999 article; whether any Cebu-specific asog text exists; the spirit spouse; how the office passed.
4. George Bryan Souza and Jeffrey S. Turley (eds., trans.), *The Boxer Codex* (Leiden: Brill, 2016), ISBN 978-90-04-29273-3 (*unverified*).
   - *Chapters to read:* the Visayan ("Pintados") chapters, and the Tagalog section on the bayog.
   - *Answers:* the context of "Luzon, Panay, and Cebu … almost all agree", and the Visayan rites in their own chapter.
5. Laura Lee Junker, *Raiding, Trading, and Feasting: The Political Economy of Philippine Chiefdoms* (Honolulu: University of Hawai'i Press, 1999); e-book ISBN 978-0-8248-6406-4.
   - *Chapters to read:* the Tanjay (Negros) phases for the 10th–13th c., and the chapter on feasting.
   - *Answers:* whether hog feasting and chiefly competition are attested archaeologically around 1178. This is the best route to an in-period practice.
6. William Henry Scott, *Prehispanic Source Materials for the Study of Philippine History*, rev. ed. (Quezon City: New Day, 1984).
   - *Chapters to read:* ch. 3 (Chinese sources).
   - *Answers:* the P'i-she-ye debate in full; Wada Sei's 1929 study; what Song sources say of the islands.
7. Masao Nishimura, "Long Distance Trade and the Development of Complex Societies in the Prehistory of the Central Philippines: The Cebu Central Settlement Case" (PhD diss., University of Michigan, 1992).
   - *Answers:* Cebu's actual extent and imports around 1178, which would justify (or not) a Sugbu holding in 1178.
8. J. Neil C. Garcia, *Philippine Gay Culture: Binabae to Bakla, Silahis to MSM*, 2nd ed. (Hong Kong UP, 2009), ISBN 978-962-209-985-2, plus his "Nativism or Universalism", *Kritika Kultura* 20 (2013). The journal is OA, but the archium host returned 403 this pass.
   - *Chapters to read:* the babaylan/asog genealogy chapter (*unverified* location).
   - *Answers:* how an insider bakla scholar weighs the asog-to-bakla link, and his "moderate nativism" as a guard against golden-past framing.
9. Fe B. Mangahas and Jenny R. Llaguno (eds.), *Centennial Crossings: Readings on Babaylan Feminism in the Philippines* (Quezon City: C&E, 2006); also Zeus A. Salazar, "Ang Babaylan sa Kasaysayan ng Pilipinas", in *Women's Role in Philippine History* (UP Center for Women's Studies, 1996).
   - *Answers:* the shape of the living revival, so the mod knows what not to imitate; Salazar's account of the babaylan office in Filipino-language historiography.
10. Francis Luis M. Torres, "Locating the Asog", *Humanities Diliman* 19(1) (2022). It is OA, but the host returned 404 this pass; get the PDF.
    - *Answers:* the five dictionaries' glosses (probably Mentrida, Sánchez, Encarnación and others: *unverified*); the full Spanish hostile vocabulary for event voices.
11. Marya Svetlana T. Camacho, "Perspectives on Visayan Women from … Alcina's *Historia*", *Journal of History* 62(1) (2016) (login on ejournals.ph).
    - *Answers:* Alcina's "antiguamente" picture of Visayan women's status, marriage and property.
