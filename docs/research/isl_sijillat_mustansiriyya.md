# *Al-Sijillāt al-Mustanṣiriyya* (ed. Mājid, 1954): design reading

Source: *al-Sijillāt al-Mustanṣiriyya: sijillāt wa-tawqīʿāt wa-kutub li-mawlānā al-Imām al-Mustanṣir bi-llāh … ilā duʿāt al-Yaman wa-ghayrihim*, ed. ʿAbd al-Munʿim Mājid (Cairo: Dār al-Fikr al-ʿArabī, 1954). Image-only scan from Columbia University's Arabic Collections Online (aco000118), 250 PDF pages.

**How it was read.** The scan has no text layer, so we OCR'd it ourselves. Pages were rendered at 200 dpi with `pdftoppm` and read with macOS Vision (`VNRecognizeTextRequest`, `ar-SA`, accurate mode) through a small Swift script. The raw OCR, page images and crops stayed in the session scratchpad and are not in the repo. **Every Arabic passage quoted or paraphrased below was checked against the page image.** Mājid's chronological table (pp. 227–229) was read straight from the images, because the OCR scrambles its columns.

- **OCR quality.** Running prose OCR'd well. Qurʾān verses (fully vowelled), small footnote numerals and some page numbers came out noisy; for example, p. 12 OCR'd as "13".
- **Page mapping.**
  - Printed page = PDF page − 6 for PDF 7–225 (pp. 1–219). Arabic-digit numbering starts at p. 11.
  - PDF 226–229 are four unnumbered leaves inside the tables section. They were not examined closely.
  - Printed page = PDF page − 10 for PDF 230 to the end (pp. 220–234).
  - The edition also prints the manuscript's own page numbers in brackets inside the text, e.g. "(٢٧٥)". **All page numbers in this note are Mājid's printed pages.**
- **Translations.** All are ours and marked *(trans.)*. Quotes are 25 words or fewer.

**What was read.**
- In full: Mājid's introduction (pp. 11–25: authenticity, historical value, literary value, description of the manuscript).
- All 66 letters (pp. 30–212). Every letter dated 452–468 AH, and every letter from or to a woman, was read line by line. The rest were read for sender, recipient, date and subject.
- The chronological table (pp. 227–229), from the images.
- Skimmed: the indexes of names, titles and terms (pp. 215–226).
- Not read: the dedication, the genealogy table, the bibliography table.

**Relation to existing notes.** `later_starts/mukhannathun_fatimid_cairo.md` §5 asked for this book (request 4). `isl_cortese_calderini_fatimid_women.md` (C&C) cites its women's letters at second hand. This note gives the primary text. It confirms Rasad's one letter and corrects two of C&C's datings. It also adds the palace's own account of the civil war and a full set of chancery formulas for a ruling woman. **It has nothing on Byzantium, eunuch offices, singers or *mukhannathūn*** (see §1, negative results).

---

## 1. The collection in brief

- **What it is.** 66 documents (*sijillāt*) from the Fatimid chancery (*dīwān al-inshāʾ*) in Cairo, sent to the Ṣulayḥid rulers of Yemen, who were the Fatimid *dāʿī*s there.
  - Date range: 'Īd al-Fiṭr 445 (January 1054) to 8 Ṣafar 489 (February 1096), "forty-four years" (pp. 15, 18).
  - Senders: al-Mustanṣir; once his mother; once his sister; once a daughter of al-Ẓāhir; al-Mustaʿlī; and al-Mustaʿlī's mother (table, pp. 227–229).
  - Mājid stresses that the letters are the chancery's work, not the caliph's. At most the caliph wrote a few words "for blessing" (p. 14). The phrase "in the noble hand" heads most letters. The scribes who may have drafted them include al-Muʾayyad fi l-Dīn al-Shīrāzī, head of the chancery from 443/1051–52 (p. 15).
- **The manuscript.**
  - It is unique. Ḥusayn Fayḍ Allāh al-Hamdānī found it among Ismaʿilis in India and gave it to the School of Oriental Studies library in London (MS no. 37155) (p. 11).
  - Mājid thinks it is a Yemeni copy (pp. 16–17). It has 175 leaves of about 15 lines, in black *naskh*; red ink is used only for "in the noble hand" and for error marks (p. 25).
  - The letters are **not in chronological order**. The text is full of copyist errors (p. 25), and four letters are fragmentary or undated (7, 9, 11, 62).
  - Al-Hamdānī published a study of the letters in *BSOS* 7 (1933–35). Mājid corrects him repeatedly in the notes.
- **Authenticity** (pp. 11–14):
  - Some letters reappear in Idrīs ʿImād al-Dīn's *ʿUyūn al-akhbār*.
  - The caliph's sign-off (*ʿalāma*) "Praise be to God, Lord of the worlds" matches what the chroniclers report.
  - The titles match Fatimid inscriptions.
  - The style matches the chancery prose quoted by Ibn al-Ṣayrafī, al-Qalqashandī and Abū Shāma.
- **The form of a letter** (pp. 23–25). Every letter follows the same pattern:
  1. *basmala* and *ʿalāma*;
  2. "From the servant of God and His friend, Maʿadd Abū Tamīm, the Imam al-Mustanṣir bi-llāh, Commander of the Faithful";
  3. the recipient's full string of titles;
  4. a fixed greeting and blessing on the Prophet and the Imams;
  5. *ammā baʿd*, a doxology and the business;
  6. a summary opening "*aʿlamaka*" ("he informs you");
  7. the date and a fixed closing.
  - **Palace women had their own *ʿalāma*.** Al-Mustanṣir's mother signed "Praise be to God, patron of every blessing" (*al-ḥamdu li-llāh walī kull niʿma*). Al-Mustaʿlī's mother signed "Praise be to God for His blessings" (p. 23–24, verified on the image). In fact the caliph's sister (letter 28, p. 96) and the "daughter of al-Ẓāhir" (letter 52, p. 171) also open with "*walī kull niʿma*". The formula is not unique to the mother, which matters for letter 52 (§5).
- **Recipients.**
  - ʿAlī b. Muḥammad al-Ṣulayḥī (letters of 445–457).
  - His eldest son Muḥammad, named his successor in the *daʿwa* in 456 and dead about 453 according to the *ʿUyūn* (pp. 19, 32–34, 53–54). The two dates conflict; Mājid notes the problem without solving it.
  - Al-Mukarram Aḥmad (460–477).
  - His mother, styled "the Ḥurra … mother of the princes". Mājid identifies her as al-Mukarram's mother (pp. 180 n. 1, 211 n. 1). Her name, Asmāʾ, comes from outside this book.
  - Al-Sayyida al-Ḥurra Arwā, who receives letters in her own name from 471/1078 on.
  - Her sons ʿAbd al-Mustanṣir ʿAlī and ʿAbd al-Imām Muḥammad, and the Ṣulayḥid "sultans" as a body (letter 38).
- **Mājid on al-Mustanṣir's court** (pp. 19–22). His account is brief and political:
  - In Egypt the letters narrate the revolts of the Lawāta and of the commander Baldakūsh, and Badr al-Jamālī's arrival.
  - Letter 56 confirms the plunder of the caliph's treasuries, "so that we truly feel the Fatimid caliph was deprived of all influence" *(trans.)* (p. 21).
  - From 467/1074 Badr's name and titles fill every letter. The caliph treats him "as his father al-Ẓāhir" (letter 57) and orders the Friday sermon read in Badr's name and his son's (letter 15).
  - Mājid presents Arwā as al-Mustanṣir's "ideal of woman". The caliph "does not count her among the *arbāb al-ḥijāb*", the people of the veil (p. 19). That is Mājid's gloss, not a chancery phrase.
  - **He says nothing about Rasad's regency, the palace women's politics or the eunuchs.**
- **Mājid's own corrections:**
  - Al-Ṣulayḥī was killed in **459/1066–67** (letters 40, 60; p. 19).
  - Letter 6 (14 Ṣafar 452 / March 1060) announces the birth of a son, Aḥmad Abū l-Qāsim. **Mājid identifies him with al-Mustaʿlī** (p. 22) against Gibb and, as Mājid says himself, "all the known sources", which give 467/1074, as does a letter quoted by Idrīs ʿImād al-Dīn. The letter cannot name him al-Mustaʿlī (a regnal title of 1094). Treat 1060 as Mājid's contested identification: a son of that name born in 1060 who died, with the name reused for a son of 1074, would fit all the evidence. **For history files use 1074** unless a second source supports Mājid.
- **Negative results (all searched in the OCR of the letters):**
  - No *Rūm*, Byzantium, Constantinople or Christians anywhere.
  - No *ustādh*, *khaṣī*, *ṭawāshī*, *ṣaqāliba* or *mukhannath*.
  - No singing-girls, and no slave girls given as gifts.
  - No Nile failure, no famine in Egypt (*ghalāʾ* appears once, for Oman in 469/1076, p. 177) and no word for the *shidda*.
  - Al-Mustanṣir never mentions his mother in his own letters.
  - **No letter dated between Rajab 457 (June 1065) and Shaʿbān 460 (June 1068).** The archive is silent across the 1066 bookmark.

## 2. Calendar of letters

Dates are AH as printed, with an approximate Julian CE date from the tabular calendar (±2 days). Order follows Mājid's table (pp. 227–229). **Bold** numbers mark letters dated about 1060–1075 (452–468 AH).

Abbreviations:
- M: al-Mustanṣir.
- ʿAlī: ʿAlī al-Ṣulayḥī.
- Mk: al-Mukarram.
- UA: "Umm al-umarāʾ", al-Mukarram's mother.
- Arwā: al-Sayyida al-Ḥurra.
- ʿAM: ʿAbd al-Mustanṣir ʿAlī b. al-Mukarram.

| No. | Date | From → To | Subject | pp. |
|---|---|---|---|---|
| 13 | ʿĪd al-Fiṭr 445 / 14 Jan 1054 | M → ʿAlī | ʿĪd procession: "drums and trumpets that split hearts", red and yellow banners | 56–58 |
| 12 | 22 Rajab 448 / 5 Oct 1056 | M → ʿAlī | Envoys received; respect the Ḥasanid sharīf of Mecca | 55–56 |
| 3 | undated (Mājid: 450/1058) | M → ʿAlī | Titles for ʿAlī's three sons; praise of his wife; vizier Abu l-Faraj named | 34–38 |
| 1 | ʿĪd al-Fiṭr 451 / Nov 1059 | M → ʿAlī | ʿĪd prayer report | 30–31 |
| **6** | Ṣafar 452 / Mar 1060 | M → ʿAlī | **Birth of a son, Aḥmad Abu l-Qāsim, 14 Ṣafar 452** (Mājid: = al-Mustaʿlī; contested) | 45–47 |
| **7** | Rabīʿ II 455 / Apr 1063 | M → ʿAlī | Start torn. Mecca strife: do not shed blood in the Ḥaram; withdraw | 47–50 |
| **5** | Ramaḍān 455 / Aug–Sep 1063 | M → ʿAlī | Ifrīqiya: Ibn Bādīs "the accursed" besieged; Riyāḥ and Zughba Arabs sent against him | 42–45 |
| **2** | Rabīʿ II 456 / Apr 1064 | M → Muḥammad b. ʿAlī | His appointment as his father's successor in the *daʿwa*; robes and titles | 32–34 |
| **4** | 9 Jumādā I 456 / Apr 1064 | M → ʿAlī | Campaigns, Mecca, a rebel. His wife given the title **al-Fāḍila** | 38–42 |
| **8** | undated (after 10 Jumādā I 457 / Apr 1065) | M → ʿAlī | **Birth of al-Muḥsin Abu l-Faḍl, mid-Jumādā I 457** | 51–52 |
| **9** | Muḥarram, year lost | M → ? (ʿAlī) | Start torn. Hajj proclamation; rather stay and govern than go on hajj | 52–53 |
| **10** | Rajab 457 / Jun 1065 | M → Muḥammad b. ʿAlī | Accepts him as his father's deputy in the *daʿwa* | 53–54 |
| **11** | undated | M → ʿAlī | **Birth of al-Ḥasan Abū Muḥammad**; end and date lost | 54–55 |
| — | *Rajab 457 to Shaʿbān 460 (Jun 1065 – Jun 1068)* | — | ***No letters. The 1066 bookmark falls in this gap.*** | — |
| **40** | Shaʿbān 460 / Jun 1068 | M → Mk | Condolence on ʿAlī al-Ṣulayḥī and a brother as "martyrs"; Mk confirmed. Mājid reads it as dating ʿAlī's death to 459 | 137–140 |
| **33** | 1 Rabīʿ I 461 / Dec 1068 | M → Mk | Recommends three men (al-Qāʾid, Muqbil, Muwaffaq) | 105–106 |
| **60** | Rabīʿ II 461 / Feb 1069 | M → Mk | Mk has killed his father's murderer; titled Amīr al-umarāʾ | 196–200 |
| **29** | mid-Jumādā I 461 / Mar 1069 | M → Mk | Safe-conduct for Jaʿfar al-Ṣāniʿ | 97–98 |
| **42** | late Jumādā II 461 / Apr 1069 | M → Mk | New titles; Yemeni envoys **leave Cairo** (qāḍī Lamak b. Mālik and others) with robes and banners | 143–145 |
| **55** | late Jumādā II 461 / Apr 1069 | M → UA | A rank for her "above the women of your age"; a letter from al-Muʾayyad goes with it | 180–181 |
| **61** | mid-Ramaḍān 461 / Jul 1069 | M → Mk | Mk's son born, named "al-Amīr Najīb al-Nujabāʾ"; an amulet in the caliph's hand. UA's rank | 200–202 |
| **65** | mid-Ramaḍān 461 / Jul 1069 | M → UA | "The late [ʿAlī] took guidance from your opinion"; envoy Ibn Ḥabāsa | 208–210 |
| **62** | undated (Mājid: to Mk; same envoy as 65, so probably 461) | M → Mk | **Troubles stop the Holy Cities' stipends; Mk to send 10,000 dinars**; a garment the caliph prayed in | 202–203 |
| **56** | 28 Muḥarram 467 / Sep 1074 | M → Mk | **The palace's own story of the war**: troops set against each other, treasury emptied, Badr's sea crossing, Lawāta, Ghuzz hold the caliph's son and *ḥarīm* | 181–185 |
| **32** | end Ṣafar 467 / Oct 1074 | M → Mk | Badr "renewed the landmarks of the Fatimid state after their effacement"; Mk "as a son" | 103–105 |
| **41** | Rabīʿ I 468 / Oct–Nov 1075 | M → Mk | "Devils under the throne" crushed by Badr; India *dāʿī* dead; **Arwā titled *ṣanīʿat amīr al-muʾminīn*** | 140–142 |
| **58** | 27 Shaʿbān 468 / Apr 1076 | M → Mk | Mk's wars were "sparks of a *fitna* that flew from us to you"; Badr regains the Holy Cities | 190–194 |
| **57** | end Dhū l-Qaʿda 468 / Jul 1076 | M → Mk | The Ḥamdānid faction, then Baldakūsh seized at the stirrup, Lawāta, Qays, Alexandria, Upper Egypt. **No dues paid "for a long time"** | 185–190 |
| 54 | Rabīʿ II 469 / Nov 1076 | M → Mk | Oman (famine and heresy) added to Mk's charge; the ʿAlid of al-Aḥsāʾ as his deputy | 176–179 |
| 34 | end Dhū l-Qaʿda 470 / Jun 1078 | M → Mk | Badr invested as chief qāḍī and chief *dāʿī*, girded with Dhu l-Fiqār | 106–109 |
| 44 | mid-Ṣafar 471 / Aug 1078 | M → Arwā | **First letter to Arwā by name**: "men and women"; "as mothers embrace sons" | 152–154 |
| **51** | 2nd decade Ṣafar 471 / Aug–Sep 1078 | **Rasad** ("al-Sayyida al-Malika, mother of the Imam al-Mustanṣir") → Arwā | Arwā's request granted at the request of "our father" Badr | 169–170 |
| 20 | late Shawwāl 472 / Apr 1080 | M → Arwā | Mk's mother's precedent; seize fugitives, **including a palace *khādim* of the caliph's sister** | 76–78 |
| 39 | late Shawwāl 472 / Apr 1080 | M → Mk | The same fugitives; a postscript in the caliph's hand: no mercy | 134–137 |
| 59 | late Shawwāl 472 / Apr 1080 | M → Mk | Badr's investiture read in the *īwān*; his sons robed | 194–196 |
| 30 | ʿĪd al-Aḍḥā 474 / May 1082 | M → Mk | ʿĪd: the caliph sacrifices with his own spear | 98–100 |
| 63 | late Rabīʿ I 476 / Aug 1083 | M → Mk | *Dāʿī*s for India and Oman | 203–206 |
| 31 | ʿĪd al-Fiṭr 476 / Feb 1084 | M → Mk | ʿĪd report | 100–102 |
| 64 | ʿĪd al-Aḍḥā 476 / Apr 1084 | M → Mk | ʿĪd report | 206–208 |
| 14 | 1 Rabīʿ I 478 / Jun 1085 | M → ʿAM | Condolence on Mk; ʿAM invested; envoy Jawhar al-Mustanṣirī; Arwā's titles | 58–62 |
| 48 | 10 Rabīʿ I 478 / Jul 1085 | M → Arwā | Condolence; she shares binding and loosing with her son | 161–165 |
| 26 | 7 Rabīʿ II 478 / Aug 1085 | M → ʿAM | Investiture confirmed; Badr "companion of the caliph's heart's blood" | 90–94 |
| 46 | 7 Rabīʿ II 478 / Aug 1085 | M → Arwā | The same, to her: help your son | 156–159 |
| 19 | ʿĪd al-Fiṭr 478 / Jan 1086 | M → ʿAM | ʿĪd report | 74–76 |
| 27 | ʿĪd al-Aḍḥā 478 / Mar 1086 | M → Mk (*sic*; Mājid: probably ʿAM) | ʿĪd; al-Afḍal as Badr's deputy | 94–96 |
| 66 | 12 Dhū l-Ḥijja 478 / Mar 1086 (*sic*) | M → UA | The rebel Ṣubḥ al-Awkanī in Upper Egypt with Arabs and "a rabble of Sudan" (Black troops) | 211–212 |
| 28 | 14 Dhū l-Ḥijja 478 / Apr 1086 | **Al-Mustanṣir's sister** → Mk (Mājid: perhaps ʿAM) | Joy at his victories; "we always mention him in our lord's presence" | 96–97 |
| 15 | 7 Muḥarram 479 / Apr 1086 | M → ʿAM | Al-Afḍal named in the Friday sermon | 63–66 |
| 17 | Rabīʿ I 480 / Jun 1087 | M → Muḥammad ʿAbd al-Imām | Honours; support your brother | 69–71 |
| 25 | Rabīʿ I 480 | M → ʿAM | Praise; reported by Jawhar | 88–90 |
| 36 | Rabīʿ I 480 | M → Arwā | The quarrel between Sabaʾ and al-Zawāḥī; her alms and dues received | 118–122 |
| 37 | Rabīʿ I 480 | M → ʿAM | Gifts from the caliph's body, including an inkwell and pens; his youth defended | 122–128 |
| 47 | Rabīʿ I 480 | M → Arwā | Praise; postscript in the caliph's hand | 159–161 |
| 38 | Rabīʿ I 480 | M → all Ṣulayḥid and Zawāḥid sultans | **Obey ʿAM and his mother**: "she speaks and is heard" | 128–134 |
| 45 | Rabīʿ I 480 | M → Arwā | She serves the *daʿwa* "with heart's blood, family, clan and wealth" | 154–156 |
| 49 | Rabīʿ I 480 | M → Arwā | Tribes obeyed; "whoever obeys you both obeys the Commander of the Faithful" | 165–167 |
| 52 | Rabīʿ II 480 / Jul 1087 | "Daughter of al-Ẓāhir" (Mājid: perhaps the caliph's mother) → Arwā | Renewed investiture of her son; her offerings received | 171–173 |
| 16 | late Jumādā I 480 / Aug 1087 | M → ʿAM | Badr crushed Cairo "hypocrites"; fugitives in Yemen forge letters; kill al-Rikābī | 66–69 |
| 53 | late Jumādā I 480 | M → Arwā | The same | 173–176 |
| 18 | ʿĪd al-Fiṭr 480 / Dec 1087 | M → ʿAM | ʿĪd report | 71–74 |
| 22 | late Dhū l-Qaʿda 481 / Feb 1089 | M → ʿAM | Sabaʾ and al-Zawāḥī reconciled; war on the Abbasid sermon in Tihāma | 79–83 |
| 23 | same | M → ʿAM | *Najwā* and *fiṭra* dues are a duty | 83–85 |
| 24 | same | M → ʿAM | Condolences: his brother, a cousin, Arwā's mother | 86–87 |
| 50 | same | M → Arwā | Oversight of the India and Oman *dāʿī*s given to her | 167–169 |
| 21 | undated | M → Arwā (Mājid) | Rely on "the father" Badr, "our deputy and the gate of our *daʿwa*"; dues | 78–79 |
| 43 | 8 Ṣafar 489 / Feb 1096 | **Al-Mustaʿlī** → Arwā | Accession; Nizār's revolt at Alexandria | 145–152 |
| 35 | 8 Ṣafar 489 / Feb 1096 | **Al-Mustaʿlī's mother** → Arwā | The same narrative, in her name | 109–118 |

**Inconsistencies to flag (not resolved here).**
- **Letter 66** is printed as 478 but is addressed to Mk's mother as living and refers to her son as alive. Letter 20 (472) already calls her dead (p. 76). Either the date or the addressee is wrong.
- **Letters 27 and 28** (478) are addressed with al-Mukarram's titles after his death. Mājid suggests ʿAbd al-Mustanṣir, who bore the same titles (pp. 94 n., 96 n.).
- **Letters 20 and 40.** Mājid's introduction says both went to "the Sayyida" in her husband's lifetime (p. 19). His own table and the text of letter 40 give al-Mukarram as the recipient.

## 3. What it changes in the design

| # | Current design | Pressure from the Sijillāt | Proposed change |
|---|---|---|---|
| 1 | Cairo 1066 set at Rasad's court during the civil war and the *shidda*. | The chancery archive is **silent from June 1065 to June 1068**. When it resumes, the palace never names famine. It tells the war as **money and troops** (letter 56, p. 183): "agitators" told the eastern troops (*Mashāriqa*) that the caliph favoured the western ones (*Maghāriba*), and the reverse. They pressed him for his treasury "thing by thing" until it was "a wasteland". | Write the palace's view of 1067–1072 as an **extortion chain, not a famine chain**. Event "Thing by Thing": the soldiers' agents ask the household for one treasure after another, and refusing is never offered as an option. The famine stays in the city (Lev, C&C). The palace voice speaks only of debts and plots. The dates match C&C's 1067 and 1069 lootings. |
| 2 | Rasad as patron whose favour shrinks after 1071 (C&C row 3). | Rasad's **only** surviving letter (Ṣafar 471 / Aug–Sep 1078) grants Arwā's request because "our father" Badr asked first (p. 170). By 1078 the queen mother works **through** Badr. | After 1074 any favour from Rasad needs Badr's consent. Event text: "The Sayyida will ask. The Amīr al-Juyūsh will decide." This is the end state of the "shrinking favour" clock: rank kept, her own power gone. |
| 3 | No dated hook for Badr's arrival. | Letters 56 and 57 (Sep 1074 and Jul 1076, pp. 184, 187):<br>- Badr crossed "the raging sea at a time when merely looking at it terrifies";<br>- Baldakūsh had blocked Cairo's walls "so no bird could enter";<br>- he was seized with one foot in the stirrup;<br>- 50,000 Lawāta were then cut down.<br>Lev dates the arrival to Jumādā I 466 / Jan 1074. | **Date gate Jan 1074**: event "The Sea in Winter" for any Sister at court. Rewards for a Sister of Rasad's party are uncertain: the new master calls himself the caliph's "father" (p. 190). Use the Baldakūsh stirrup scene as the event picture. |
| 4 | The palace women as a set. | The palace women **write in their own names, with their own sign-offs**: Rasad 1078, the caliph's sister 1086, "daughter of al-Ẓāhir" 1087, al-Mustaʿlī's mother 1096. The sister keeps a household with at least one palace *khādim* (pp. 77, 136). | Give the Sisters' Cairo set a **letter-writing role**. A literate Sister in a palace woman's household drafts her letters to Yemen. Event "Patron of Every Blessing": choose the sign-off, which sets your patron's voice. **Not in 1066**: the attested women's letters run from 1078 on, and C&C's "1067 letter" is a misdating (§5). |
| 5 | Hostile instruments at court (Cairo note §4.3). | **The fugitive *khādim*** (Apr 1080): a servant "attached to the service" of the caliph's sister "forged letters against the Commander of the Faithful" and fled to Yemen. Cairo orders him sent back "bound in iron" or killed (pp. 77–78, 136). The same letter brands the fugitives as men who "put on the shirt of religion for show, and adorned themselves with the ornament of faith falsely" (p. 77). | Two hooks:<br>(a) **Defection and extradition**: a palace servant in a woman's household who flees is hunted across the Red Sea. A Sister can be the forger, the accused or the one who hides him.<br>(b) The **"ornament of faith worn falsely"** charge is the hostile register for the Sisters' sincerity in Ismaʿili mouths. It belongs to hostile voices only and never resolves in the narrator's voice. |
| 6 | Gendered address in Fatimid loc. | The chancery **re-genders its own formulas** for a woman ruler:<br>- to a son in 1064: rule your men "as compassionate fathers embrace sons" (p. 34);<br>- to Arwā in 1078: "embrace them as mothers embrace sons" (p. 153);<br>- to a son: "the child laid in the cradle of faith" (p. 32);<br>- to Arwā: "born in the cradle of faith, nursed on the milk of the saints' sciences" (p. 152). | **Loc rule.** When a Fatimid letter goes to a Sister ruler or a Sister court officer, use the feminine form of the same formula, never a "female-only" set. In-world gloss for a Sister: "The Imam's scribes change one word and a man's charge becomes a woman's. The rest of the sentence was always ours." |
| 7 | The faith's critique of classification by the state. | Letter 20 (1080, p. 76): the caliph recalls taking Mk's mother "out of the company of the ladies of the curtained alcoves, into the governance of the state and precedence over men" *(trans.)*. A decree moved a woman from one social category to another. She was not "made a man": she stayed *al-ḥurra*, "mother of the princes". | **Doctrinal hook, in characters' mouths only.** A Sister *dāʿiya* or court Sister argues that a *sijill* can move a woman out of the *ḥijāl* without making her less a woman. If a decree can move a woman between ranks, it can name a daughter. Hostile answer: "The Imam's pen elevates; it does not create." **Never claim Asmāʾ or Arwā as trans.** The line is about the chancery's power, not their gender. |
| 8 | Rewards from the Imam. | Attested gifts from the caliph's own person:<br>- robes, swords and banner-cords "taken from his body and shoulder", and riding gear (p. 127);<br>- an inkwell with pens "his noble fingers touched" (p. 127);<br>- "a garment we wore and prayed in on the last Friday of Ramaḍān" (p. 203);<br>- an amulet (*ʿūdha*) written "in his own hand" for a newborn's arm (p. 202);<br>- new titles (*laqab*s) as the main currency (pp. 36, 42, 142). | **Artifact rewards** for Cairo events: "Imam's Inkwell" (learning or stewardship), "Garment of the Last Friday" (piety), "Amulet in the Imam's Hand" (for a child). A *laqab* reward modifier works in the same register. This source attests **no slave or singing-girl gifts**; take those from al-Musabbiḥī if they are wanted. |
| 9 | Eunuch go-betweens at Rasad's court (El-Azhari; "Through the Curtain"). | **No *ustādh* appears**, and no envoy is called a eunuch. Envoys to Yemen are:<br>- "his slave" (*ʿabduhu*), the emir Jawhar al-Mustanṣirī, "among the chiefs of [the dynasty's] slaves" (pp. 61, 89);<br>- Ṭāhir b. ʿAlī b. Ḥabāsa, "of the sword and the pen" (p. 203);<br>- civil shaykhs.<br>Badr and al-Afḍal are each called the caliph's ***fatā*** (pp. 67, 111, 148). | Keep eunuch NPCs few (Lev row 9). For the envoy role use an **ʿabd-emir with the al-Mustanṣirī *nisba*** as the template, and leave his body unstated, as the source does. Vocabulary for loc: *fatā* (the caliph's "young man", even for the generalissimo) and *ʿabīd al-dawla* ("the dynasty's slaves", used of Baldakūsh, p. 186). |
| 10 | History files for al-Mustanṣir's family in 1066. | Sons attested with dates:<br>- Aḥmad Abu l-Qāsim, born 14 Ṣafar 452 / ~20 Mar 1060 (p. 47); Mājid's identification with al-Mustaʿlī is contested (other sources: born 1074), so do not create al-Mustaʿlī in a 1066 history file;<br>- al-Muḥsin Abu l-Faḍl, born mid-Jumādā I 457 / ~Apr 1065 (p. 51);<br>- al-Ḥasan Abū Muḥammad (undated, p. 55).<br>Also: in 1074 "the Ghuzz" held "his son and his *ḥarīm*" in Syria (p. 185). | Add the three children as alive in 1066, aged about 6, 1 and unknown. Optional 1070s event "The Ghuzz Hold the Harem": women of the house captive in Syria, a ransom or rescue hook. Nizār (the elder, named in letters 35 and 43) is already known from other notes. |
| 11 | Holy Cities and the *daʿwa* as background. | About 1069 (letter 62, p. 203): "events that occupy hearts and divide the people" stopped the Holy Cities' customary stipends (*rusūm*). Yemen is told to send **10,000 dinars** of its own. Letter 57 (1076) adds that Yemen sent **no dues at all "for a long time"** while the roads were closed (pp. 188–189). | **Date gate 1068–1072**: "The Stipends Fail". Cairo cannot pay Mecca, and Yemen pays in Cairo's name. Gate 1074–76: "Arrears", where the restored court demands back-dues from distant clients, including a Sister ruler outside Egypt. |
| 12 | Byzantine-origin faith in Cairo. | **Silence**: no Rūm, Christians, embassies or captives anywhere in the 66 letters. | Do not source any Byzantine thread in the Cairo set to this book. Use C&C (Rasad's gifts from "the emperor Michael", Sitt al-Mulk's Melkite kin) and Lev. |

**Net relevance.**
- **High** for chancery loc, women's titulature, the palace's own story of 1067–76, Badr date gates and gift rewards.
- **Nil** for Byzantium, eunuch offices, *mukhannathūn* and the 1066 year itself, which the archive skips.

## 4. Quotable lines for loc

These are in-world lines: chancery formulas, translated, and attributed to in-world speakers. No historical person is claimed as trans. Each line notes its source.

**Chancery forms for a woman ruler** (use with a Sister ruler or a Fatimid patroness; strip diacritics in loc for the CK3 font):
- Address string, translated and shortened from pp. 76, 109, 169: "To the Ḥurra, the Queen, the Lady, the Rightly-Guided, the Sincere, the Firmly-Placed, Treasure of the Faith, Support of the Believers" *(trans.)*.
  - Continues: "Refuge of the Respondents, Friend of the Commander of the Faithful, Guardian of his Saints" *(trans.)*.
  - Arabic: *al-Ḥurra al-Malika al-Sayyida al-Sadīda al-Mukhliṣa al-Makīna, Dhakhīrat al-Dīn, ʿUmdat al-Muʾminīn, Kahf al-Mustajībīn, Waliyyat Amīr al-Muʾminīn, Kāfilat Awliyāʾihi*.
- Variant title, 1075: "the Commander of the Faithful's own creation" (*ṣanīʿat amīr al-muʾminīn*) *(trans.)* (p. 142).
- Earlier set, for a widow-regent, pp. 180, 209: "the Ḥurra, the Pure, the Pious, the Excellent, the Perfect, Guardian of the Believers, … Mother of the Chosen Princes" *(trans.)*.
- Closing blessing for a woman: "May God preserve her might and her veiling (*ṣawnahā*)" *(trans.)* (p. 154).
- **Al-Fāḍila** ("the Excellent"), granted "for her distinction in faith and qualities over the members of her sex" *(trans.)* (p. 42).

**Lines:**
- "We have taken her from the company of the curtained ladies into the governance of the state and the precedence over men." *(trans.)* (Fatimid chancery; p. 76)
- "God has approved among His sincere servants men and women, and bound the summons of the faith to their insight." *(trans.)* (Fatimid chancery to a woman ruler; p. 152)
- "Embrace them as mothers embrace sons." *(trans.)* (Fatimid chancery to a woman ruler; p. 153)
- "She speaks and is heard; she commands and forbids and is not contradicted." *(trans.)* (Fatimid decree; p. 132)
- "Girded at the waist in service, night and day, in secret and in the open." *(trans.)* (a queen mother praising a woman ruler; p. 170)
- "You raised the pillar of governance, and the multitude handed you its reins." *(trans.)* (the same; p. 170)
- "Praise be to God, patron of every blessing." *(trans.)* (sign-off of a palace woman's letter; pp. 24, 96, 169)
- "They asked for thing after thing, and he refused them nothing, until his treasury was a wasteland." *(trans.)* (palace chronicler of the troops' demands; p. 183)
- "Devils sprang up beneath the throne, conspiring to pull down its pillars." *(trans.)* (Fatimid chancery on the civil war; p. 142)
- "Sparks from the fire of a *fitna* that flew from us to you." *(trans.)* (Cairo to a distant client after the war; p. 192)
- "When the heart is struck, all the limbs fall into disorder." *(trans.)* (the same; p. 192)
- "He crossed the raging sea at a time when merely to look at it was terror." *(trans.)* (palace voice on Badr's crossing; p. 187)
- "They put on the shirt of religion for show, and wore the ornament of faith in lies." *(trans.)* (hostile Ismaʿili voice; p. 77)
- "A servant of the palace, who kept to the service of the caliph's sister, forged, and fled." *(trans.)* (court order; p. 77)
- "A garment we wore, and prayed in, on the last Friday of Ramaḍān." *(trans.)* (gift-letter from the Imam; p. 203)
- "God gave me the caliphate when I was under eight; who will grudge a boy his summons?" *(trans., adapted)* (the Imam defending a child appointee; p. 127)
- Sister, on the chancery's gendered formulas (ours, from pp. 34, 153): "The scribes change 'fathers' to 'mothers' and the charge is mine. The rest of the sentence was always ours."

## 5. Answers to open questions in other notes

Other notes were **not** edited. Proposed changes:

1. **`later_starts/mukhannathun_fatimid_cairo.md` §5, request 4** ("Fatimid documents: *al-Sijillāt al-Mustanṣiriyya*"). Now read; strike it. Al-Shayyāl's *Majmūʿat al-wathāʾiq* is still unseen.
2. **Same note §6, Q7 (when did Rasad die?).** Partly answered.
   - Rasad is **alive in Ṣafar 471 / Aug–Sep 1078**: letter 51, in her own name, "al-Sayyida al-Malika, mother of the Imam al-Mustanṣir" (pp. 169–170, verified).
   - Mājid suspects that letter 52 (Rabīʿ II 480 / Jul 1087), headed "daughter of al-Ẓāhir", is really hers (p. 171 n. 1). His reasons are its *ʿalāma* and the title *al-Malika*.
   - If he is right, she was alive in mid-1087, which would match El-Azhari's "1087". The argument is weak: the caliph's sister uses the same *ʿalāma* (p. 96). Treat 1078 as the last secure date.
3. **Same note §3.2, "the curtain is thinly sourced".** The Sijillāt add nothing. Al-Mustanṣir's 60-odd letters never mention his mother, and her one letter shows her petitioning through Badr (p. 170). This supports C&C's "shrinking favour" and the Ismaʿili silence about Rasad (C&C p. 113).
4. **`isl_cortese_calderini_fatimid_women.md`, Rasad "After": "In 471/1078 she wrote to Queen Arwa (pp. 108, 113)".** Confirmed: letter 51, 2nd decade of Ṣafar 471. Add its content: Arwā's request was granted at the request of "our father, al-Sayyid al-Ajall Amīr al-Juyūsh" (p. 170).
5. **Same note, "A daughter of al-Ẓāhir … In 459/1067 she wrote Arwa a letter of condolence confirming her son's succession (p. 108)".**
   - **Probably misdated.** The only letter from a "daughter of al-Ẓāhir" in the Sijillāt is letter 52, dated **Rabīʿ II 480 / July 1087**. It concerns the **renewed investiture of Arwā's son ʿAbd al-Mustanṣir** after al-Mukarram's death (pp. 171–173).
   - In 1067 Arwā's husband was alive and her son was not yet a ruler.
   - Mājid doubts the sender (above). Unless C&C cite another source, change it to "480/1087".
   - **Consequence:** C&C row 11's event hook ("the women's letter to Yemen in 1067 needs a scribe") has no 1067 letter behind it. Re-date it to 1078 or later, or mark it as unattested.
6. **Same note, al-Mustanṣir's full sister "wrote to the Ṣulayḥid al-Mukarram on his victories (p. 108)".** This is letter 28, 14 Dhū l-Ḥijja 478 / ~2 Apr 1086 (pp. 96–97).
   - Al-Mukarram was already dead: condolence letters went out in Rabīʿ I 478 (letters 14, 26, 46, 48). Mājid suggests the recipient was really ʿAbd al-Mustanṣir (p. 96 n. 1).
   - Add: in 1080 the sister had a palace *khādim* in her service who forged letters and fled to Yemen (pp. 77, 136).
7. **Same note §4, "Al-Mustaʿlī's mother's letter to Arwa is dated '489/1069' (p. 38). It must be 489/1096."** Confirmed: letter 35, 8 Ṣafar 489 / ~6 Feb 1096 (p. 118). Her titles are "al-Sayyida, al-Malika, the Gracious, the Kind, the Merciful" (p. 109).
8. **Same note, Byzantine gifts to Rasad from "the emperor Michael" (p. 151) and the 444 Turkish slaves (p. 78).** The Sijillāt cannot check either: they never mention Rūm.
9. **`isl_lev_state_society_fatimid.md` §4.1 (the war ends with Badr's arrival in winter 1073).** The Sijillāt add the palace's dated narrative. The first letter to mention Badr's arrival is 28 Muḥarram 467 / Sep 1074 (letter 56). It includes:
   - the winter sea crossing;
   - Lawāta "about fifty thousand men";
   - Ghuzz in Syria holding the caliph's son and *ḥarīm* (pp. 183–185).
   
   Letter 57 (Jul 1076) gives the sequence the palace remembered: the Ḥamdānid faction, then Baldakūsh, then Badr, the Lawāta, the Qays of the Buḥayra, Alexandria and Upper Egypt (pp. 186–188).
10. **Lev row 9 and `isl_el_azhari_queens_eunuchs.md` §1 (eunuchs).** Lev's "few and senior" is consistent with the Sijillāt: the 66 letters name no *ustādh*. The one palace *khādim* is a fugitive, and the court's envoys are *ʿabd*-emirs (Jawhar al-Mustanṣirī) and civil shaykhs.
11. **`isl_el_azhari_queens_eunuchs.md`, "Rasad (Cairo, 1036–87)".** The end date rests on Mājid's conjecture at most (item 2). Keep it marked unverified.
12. **Cairo note §1.6 (what is not attested).** Add to its negatives: the Fatimid chancery letters of 1054–1096 contain no *mukhannath*, no singers and no Nawrūz.
