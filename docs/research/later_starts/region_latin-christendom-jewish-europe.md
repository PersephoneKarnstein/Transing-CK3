# Starts at 1066 and 1178: Latin Christendom and the Jews of Europe

Region: France, Occitania, Christian Iberia, Italy, the Empire, England, and the Jewish communities of Europe and al-Andalus. The faith seated here is Ha-Nehpakhot (Arles).

Method. I read `docs/faiths/ha-nehpakhot.md` and the `jud_*` notes (above all Ben-Shalom, Grossman, Shatzmiller, Stouff/Gross, the women's-synagogue articles), plus `comparanda_reading_list.md` (Latin section), `cmp_devun_shape_of_sex.md` and `cmp_vanderlugt_sex_difference.md`. I checked vanilla CK3 title and province history for the two dates and verified the new leads on the web. `docs/research/sources_pending/` holds nothing for this region; `books/` and `raw/` hold nothing relevant. Anything I could not check against a page is marked *unverified*.

## Verdict at a glance

| | 1066 | 1178 |
|---|---|---|
| **Ha-Nehpakhot (Arles)** | **Carry forward with stand-ins.** A few loc lines need dating (no *baylons* before 1215). Nothing at this date changes the faith's premises for the better, and the Rhineland has better women's evidence than Arles does at this date (see §2). | **Same start, new flavour. A new set of starter characters is worth doing, but not a new start.** The seat, the gate and the "landless and learned" premise all hold, and several of the faith's mechanics are better supported at 1178 than at 867. The pressures change: Cathar neighbours (in vanilla), Lateran III, and Alan of Lille. |
| **New hub in the region** | Only one is plausible: a Rhineland (Worms) branch of the same current. There is no case for a new faith. | None justifies a new faith. Norman Palermo has a real eunuch office at a Latin court, but it belongs to the Adelphai Dorleyaiou discussion, not to this faith. |
| **Drop** | Jewish al-Andalus as a hub: the Granada massacre was on 30 Dec. 1066. | Jewish al-Andalus is gone under the Almohads. |

The short version against the user's test: in this region, 1066 and 1178 change the **pressures** (reform canon law, sodomy legislation, heresy-hunting, crusade violence) much more than they change the **premises** (seat, gate, institutions, texts). The one textual premise that really moves is that by 1178 Rashi has put Dinah's turning into the most-taught Jewish commentary. That justifies new flavour and new starter characters at 1178. It does not justify a new start.

---

## 1. Ha-Nehpakhot: verdicts

### 1.1 When each premise becomes available

| Premise the faith rests on | Earliest attestation | 1066? | 1178? |
|---|---|---|---|
| Organised community at Arles, "a great assembly" | 11th-c. responsum (Ben-Shalom 2024, p. 25) | yes | yes |
| Leah's prayer and Dinah turned in the womb (bBerakhot 60a); "by the hands of heaven" (bYevamot 80b) | Talmud, read in Provence long before 1066 | yes | yes |
| **Rashi on Gen. 30:21**: Leah "offered prayer regarding it, and its sex was changed" (Rosenbaum–Silbermann trans., citing Berakhot 60a) | Rashi wrote at Troyes c. 1070–1105 | **no** | **yes**, in the most-taught Torah commentary of Ashkenaz and northern France (its reach in Provence by 1178 is *unverified*) |
| Archbishop's jurisdiction over the Jews of Arles, and with it the lord's licence for the ban | 1144, Conrad III's grant (Ben-Shalom p. 26) | no (count and archbishop; the arrangement is *unverified*) | **yes, exactly as modelled** |
| *Baylons* / three rectors | 1215 charter (Ben-Shalom pp. 27–28) | no | no |
| Women's synagogue below the men's | Arles 1409/1452 (Hildenfinger; Stouff) | no | no (no evidence) |
| Women on the council | 1401 (Stouff §10) | no | no (already gated) |
| Jewish translators and physicians serving lords | Lunel from c. 1150 (Judah ibn Tibbon) | no | **yes**: Benjamin names "R. Judah the Physician, the son of Tibbon" at Lunel (Adler 1907, p. 4) |
| A Jew in a Christian lord's office | Abba Mari, "bailiff of Count Raymond" at Saint-Gilles (Benjamin, Adler p. 5) | no | **yes** |
| Kalonymus's *Even Boḥan*, Purim dress, the Three Lamps lament | 1322–23 | no | no (already gated to 1323) |
| Women's blessing *qui fis me fenna* | 15th-c. manuscript | no | no |

Reading the table: at 1066 the faith has its scriptural core (Berakhot 60a) and a community, and nothing else. At 1178 it also has Rashi's Dinah, the archbishop's licence, the translator-physician milieu and a Jewish office-holder under a count. Those are the exact things the mod's mechanics are built on, so most of the mechanics are better grounded at 1178 than at 867.

### 1.2 Verdict for 1066: carry forward with stand-ins

Against the test:
- **Who holds the seat.** Vanilla gives `c_venaissin` in 1066 to a placeholder, Rainaut (char 32534), under `d_provence`. Historically the Jews of Arles answered to the counts of Provence and the archbishop. The mod already handles "lives under another lord", so nothing new is needed.
- **Gender order.** No change for Arles that I can document. Rabbenu Gershom's *takkanot* (early 11th c.) banned polygamy and divorce against a wife's will in Ashkenaz, but the ban "was never accepted" in Provence or Spain (Jewish Virtual Library, "Bigamy and Polygamy", after Falk 1966, *unverified* page). Provence later made its own anti-divorce edicts: R. Moses Nasi renewed them in 27 communities, according to R. Mordecai Kimhi (Grossman 2004, ch. 4). Those are 12th–13th c. and *not* datable to 1066.
- **Institutions.** None of the street institutions the faith uses are attested yet (no baylons, women's synagogue, lamp alms or confraternity).
- **Texts.** Berakhot 60a only. No Rashi, no Kalonymus.
- **Neighbours and law.** Gregorian reform is under way. Peter Damian's *Liber Gomorrhianus* (1049, to Leo IX) built "sodomy" as a clerical crime in four grades. By Jordan's and Boswell's accounts, Leo IX accepted the diagnosis but declined Damian's harshest penalties (Jordan 1997, ch. 3; Boswell 1980, pp. 210–213, verified 2026-10-27, who dates the book c. 1051 and Leo's reply 1051 (pp. 210, 365; `../hist_boswell_social_tolerance.md`); Jordan's pages *unverified*; trans. Payer, *Book of Gomorrah*, 1982). This is Latin clerical discipline and does not touch a Jewish street directly.

**Recommendation.** Keep the existing script stand-ins. Make two dating fixes, which are flavour, not a new start:
- Before 1215, events that name the *baylons* should say "the worthies of the street" or "the great assembly" (Ben-Shalom p. 25).
- Before 1144, the *niddui* licence comes from "the count and the archbishop", and after 1144 from "the archbishop" (and from 1251 the Angevin count, as already noted).

### 1.3 Verdict for 1178: same start, new flavour, new starter characters

Against the test:
- **Who holds the seat.** Vanilla 1178 gives `c_venaissin` to Bertrand des Baux, prince of Orange (char 32516, from 1173), under `d_provence`. The lords of Orange were a troubadour house: Raimbaut d'Aurenga died in 1173, and Bertrand's claim came through Raimbaut's sister Tiburge (*unverified*). On **30 July 1178** (some sources say 30 June) Frederick Barbarossa was crowned king of Burgundy in Saint-Trophime at Arles. That puts the emperor whose predecessor granted the Jews of Arles to the archbishop (1144) in the city in the start year. It is a good opening event: the kahal seeks confirmation of its privileges at the coronation (*suggestion*).
- **Gender order and categories.** The Latin categories around the street harden. Alan of Lille's *De planctu Naturae* (1160s–70s) opens with the clearest contemporary Latin naming of the crossing this faith is about, in a hostile voice: "Man is made woman, he blackens the honour of his sex; the craft of magic Venus makes him of double gender" (Metre 1; trans. Moffat 1908; Sheridan 1980, p. 67–68, *page unverified*). Alan means the sodomite, read through a grammatical metaphor. DeVun places him in the same "neither one nor the other" polemic as Guibert and Bernard of Cluny (DeVun 2021, pp. 83–87). He later lived and wrote in the Montpellier region against heretics, Jews and Muslims (*De fide catholica*, c. 1190–1200; *unverified*). He is the right **attributed hostile voice** for a 1178 Christian lord's opinion of a daughter.
- **Institutions.**
  - The archbishop's licence for the ban is exactly the model already built (`tm_turning_niddui_effect`). At 1178 the archbishop of Arles is Raymond de Bollène (c. 1163–82, *unverified*).
  - The translator-physician service the faith uses for protection (`tm_hipukh.0030`, `.0031`) is now contemporary rather than anachronistic. Judah ibn Tibbon fled Granada c. 1150 to Lunel and translated Baḥya's *Duties of the Heart* in 1161 at the request of Meshullam of Lunel and his son Asher (Jewish Virtual Library, "Judah ibn Tibbon"; Posen Library). Benjamin calls him "the Physician" (Adler 1907, p. 4).
  - Benjamin of Tudela (c. 1165) counts about 200 Jews at Arles. He names "R. Moses, R. Tobias, R. Isaiah, R. Solomon, the chief rabbi R. Nathan, and R. Abba Mari, since deceased" (Adler 1907, p. 6). He also counts 300 at Lunel, about 40 at Posquières under Rabad, about 100 at Saint-Gilles and 300 at Narbonne (pp. 2–6).
  - Lunel's congregation "taught, boarded, lodged and clothed" poor students. That is a period model for the kahal's pilgrimage and adoption mechanic: a community that takes in young people from afar (p. 4).
  - **Asher ben Meshullam "the recluse, who dwells apart from the world… fasts periodically and abstains from all meat"** (Adler p. 3) shows that a Provençal kahal honoured a member who lived a withdrawn, set-apart life. That is a period precedent for an elder of the lamp who keeps her own rule. It is in the faith's voice only, and the narrator does not compare her to him.
- **Texts.**
  - Rashi on Gen. 30:21 puts the turning of Dinah into the first commentary a child learns. The elder at the scroll (`tm_hipukh.0010`) can teach "as Rashi of Troyes taught it" before 1323. That is a period-correct pre-Kalonymus liturgy, and it is better than the bare Talmud.
  - Provençal halakhah's pro-women rulings come from Rabad of Posquières, alive in 1178 (d. 1198): no beating of wives, and the childless wife keeps her *ketubbah* (Grossman 2004, chs. 10–11). These support the existing infertility/ketubbah hook at this date.
  - Purim dress is still unattested before 1322 (Horowitz 2006, p. 252). The existing pre-1323 branch stays: she wears it alone.
- **Neighbours and law.**
  - In vanilla 1178, Toulouse, Albi, Carcassonne (which holds `b_narbonne`), Béziers and Agen are **Cathar** (`history/provinces/k_aquitaine.txt`, set from 1150). The holy site at Narbonne therefore sits inside a Cathar county at this start.
  - The 1178 papal legation of Henry of Marcy and Peter of Pavia came to Toulouse, and Lombers (1165) had seen a public debate.
  - **Lateran III (March 1179)**, canon 11: clerics "convicted of… incontinence against nature" are deposed or sent to monasteries for penance (EWTN/Tanner text; the lay penalty of excommunication is in Tanner's translation, *unverified* wording). This is the first general council to legislate on sodomy. Canon 26 forbade Jews to keep Christian servants (*unverified* numbering). Canon 27 called for force against the heretics of the Midi.
  - So in the first year of play, a Christian lord's court moves from tolerating doubtful sex (Rolker: no persecution of "hermaphrodites" as such) toward policing "against nature". The Jewish physician at court is newly exposed too.

**Recommendation.** Keep Arles as the seat, keep the gate, and write a **1178 seed**: new starter characters, three events and some loc dating.
- *Characters.* See §3.1. The household is a translator-physician family with Lunel ties, which suits the period better than a generic physician.
- *Events.*
  1. The coronation at Saint-Trophime, where the kahal asks for its privileges to be confirmed.
  2. Alan's line spoken by a Catholic courtier, as a hostile opinion event.
  3. Lateran III, as a one-off decree that raises Catholic hostility to daughters at Catholic courts. The event aims at "against nature", never at Jews as a people.
- *Loc.* Teach Rashi's Dinah before 1323. Use "the worthies" before 1215. The licence comes from "the archbishop".
- This is a new set of starter characters at the same seat. It is not a new start.

---

## 2. Candidate hubs in the region

| # | Hub and date | Attested basis | Rating |
|---|---|---|---|
| A | **Worms / Mainz / Speyer Jewry (Rhineland), 1066 and 1178** | R. Isaac ha-Levi of Worms (c. 1002–1070, Rashi's teacher, alive in 1066) ruled that women who wish to take on time-bound commandments "are permitted… and one does not object" (Grossman 2004, ch. 8 §3, ch. 1 §6). Rabbenu Gershom's takkanot gave wives a veto on divorce and banned polygamy in Ashkenaz. By the late 12th c. there were women's prayer leaders: Dulca of Worms (d. 1196) taught women to pray and sing, and Richenza and Urania came later (Grossman ch. 7 §7, ch. 8 §4; Baumgarten 2016, pp. 47–49). The Worms women's synagogue dates from 1212/13. Vanilla: `c_worms` is held by Emperor Henry IV in 1066. | **Plausible** for a Jewish women's current, with stronger women's evidence at 1066 than Arles has. **Thin** for anything trans-specific: Kalonymus's link is to Arles, and the Purim premise is Provençal. |
| B | **Lunel / Posquières, 1178** | Benjamin (Adler pp. 3–5): Meshullam's sons, the recluse Asher, Judah ibn Tibbon, Rabad's academy. It is the heart of the translation movement and of Provençal halakhah. CK3 has no Lunel barony, so it would map to `c_montpellier` (Guilhem VIII). | **Plausible as a second house of the same current**, not as a new seat. It adds the translator premise but no gender evidence. |
| C | **Narbonne, 1178** | Benjamin: "the Torah goes forth to all countries"; the Davidic nasi Kalonymos ben Todros held lands "of which no man can forcibly dispossess him"; 300 Jews (Adler p. 2). The city was ruled 1143–c. 1192 by **Viscountess Ermengard**, a woman sovereign, arbiter and patron of troubadours, who appears as a judge in Andreas Capellanus's *De amore* (c. 1180s; Cheyette 2001, *Ermengard of Narbonne and the World of the Troubadours*, *unverified* pages). Vanilla: `b_narbonne` is a barony of Cathar `c_carcassonne` (Roger II Trencavel), and Ermengard is not landed. | **Thin to plausible.** A woman holds the city, which matters for "who holds the seat", but the gate is unchanged and there is no trans evidence. It works better as holy-site flavour for 1178 ("the city a lady rules"). |
| D | **Cathar Languedoc (Toulouse, Lauragais, Albigeois), 1178** | Dualist teaching that souls are fallen angels with no sex, and transmigration across bodies. Cross-sex transmigration is attested in early-14th-c. testimony (Fournier register; Le Roy Ladurie, *Montaillou*, *page unverified*). Women could receive the consolamentum, and houses of *bonnes femmes* are attested in the 13th c. (Abels and Harrison 1979, *unverified*). Vanilla seeds Catharism here in 1178. | **Plausible as context; thin as a hub.** This is the one belief system in the region that says the body's sex is not the soul's, and that is a real premise change. But (1) the cross-sex claim is 14th-c. evidence, (2) Pegg (2001) and Moore (2012) doubt that an organised Cathar church existed in 1178, (3) it would be a second Christian heresy seat, and (4) it invites the "secret matriarchal heresy" trope the comparanda list warns about. Use it as a **neighbour opinion and a conversion temptation**, not as a faith. |
| E | **Fontevraud, 1101 →** | Robert of Arbrissel's double order. Men and women were "all subject to the abbess", justified by "Behold thy mother" (John 19:27). Petronilla of Chemillé, a twice-widowed laywoman, was first abbess 1115–49. The order was exempt from the bishop and became the Plantagenet house. | **Thin.** It is a real institution in which men served women, but it offers no route for trans women. Abbess rule over monks is an inversion of status, not of sex. Use it as Latin flavour (a lord's widowed mother retires there), not as a hub. |
| F | **Rupertsberg (Hildegard of Bingen), 1178** | In 1178 the Mainz prelates laid an interdict on her nuns for burying a reconciled excommunicate, and it silenced their singing. Her letter to the prelates defends sung liturgy. She died 17 Sept. 1179. *Scivias* II.6.77: "a man should never put on feminine dress or a woman use male attire… unless a man's life or a woman's chastity is in danger" (Hart and Bishop trans. 1990, *page unverified*). | **Thin; reaction only.** She is a hostile-but-measured voice: a "necessity" exception like Aquinas's. Never present her as an ally. |
| G | **Troubadour and trobairitz courts (Orange, Die, Narbonne, Toulouse), 1178** | *Midons* ("my lord", with a feminine possessive and a masculine noun) addresses the lady (Kay 1990, ch. "Gender and status"). The Comtessa de Dia (fl. c. 1175–1212) sang from a woman's position. Raimbaut d'Aurenga (d. 1173) was lord of Orange, which is the seat's own lord's house. | **Thin.** The gender play is in grammar and the lyric persona, not in social roles. It is good flavour for Bertrand des Baux's court, and a reason a daughter might find a polite hearing there. Avoid Kay-style "third gender" framing. |
| H | **Norman Palermo, 1178** (Italy) | William II's court ran on palace eunuchs, *al-fityān al-majābīb*, who were "disguised Muslims who strictly observe the Muslim religion secretly" (Ibn Jubayr, 1184–85, as quoted in Ayalon 1999, pp. 312–313; the project's note `hist_ayalon_eunuchs_caliphs.md` item 74). Caid Peter and Richard appear in Hugo Falcandus, 1154–69 (trans. Loud and Wiedemann 1998); Johns (2002) covers the "palace Saracens". | **Strong as an institution** (a Latin king's eunuch office in the 1178 window), but **not a hub for this faith**. Ha-Nehpakhot refuses the knife. The eunuchs saw themselves as men and Muslims. It belongs to the Adelphai Dorleyaiou or Islamic-region discussion: a possible destination for that faith's daughters in 1178. Hand it on to those researchers. |
| I | **Toledo, 1178** | Christian Castile's translators: Abraham ibn Daud (d. c. 1180), Gerard of Cremona (d. 1187). | **Thin.** It doubles the Lunel translator premise and has no gender evidence. |
| J | **Jewish al-Andalus** | 1066: the Granada massacre of 30 Dec. 1066 killed the vizier Joseph ibn Naghrela and much of the community. Andalusian Hebrew love poetry (Samuel ha-Nagid, d. 1056) addresses a male "gazelle" (Roth 1982, *Speculum* 57: 20–51, *unverified*). 1178: Almohad rule since 1147 had ended open Jewish life, and the Tibbonids and Maimonides' family left. | **Drop.** At 1066 it is the eve of a massacre. At 1178 it no longer exists as a Jewish hub. The poetry is male–male desire, not a women's current. |

**A better hub than Arles?** For **1066**, the Rhineland (A) has more contemporary evidence about Jewish women taking on observance than Arles has. But moving the seat would cut the faith off from Kalonymus and Purim, which are its reason to exist. The better use is a **second house at Worms**. For **1178**, Arles is the right seat (archbishop's licence, Benjamin's figures, the coronation), with Lunel (B) as a sister house.

---

## 3. Start sketches

### 3.1 Ha-Nehpakhot at 1178: "The Coronation Year" (recommended)

- **Seat.** The Jewish street of Arles, in `c_venaissin`. The county is held by Bertrand des Baux, prince of Orange (vanilla, char 32516), under the count of Provence. Over the street, the archbishop of Arles holds jurisdiction over the Jews (grant of 1144). No landed head, as now.
- **Starter characters** (all fictional; names from the project's Provençal lists or Benjamin's period):
  - **Bella, daughter of the Turning, elder (c. 60).** She teaches Dinah "as Rashi of Troyes set it down". Learning is her strength. She was turned before Kalonymus's book existed, so her rite has no Purim dress, which is the existing pre-1323 branch.
  - **Mairona (c. 19), Marked, not yet turned.** She is the daughter of the physician household below. She learns Arabic letters from her father's books.
  - **R. Ṭodros the physician (c. 45) and his wife Douce (c. 40)**, with two or three children. He trained at Lunel among the Tibbonid circle and serves the prince of Orange. This is the existing household seed, re-skinned as a translator-physician family, which gives `tm_hipukh.0030` its period footing (Adler p. 4). *Glyph check:* "Ṭodros" uses ṭ, which the CK3 font lacks, so use "Todros".
  - **Optional at Lunel (`c_montpellier`):** **Sara of Lunel (c. 30), Marked**, a pupil who boards with the congregation "so long as she studies" (Adler p. 4). She is the line's second house and a pilgrimage source.
- **Pressures.**
  - The coronation (July 1178): an event to have the privileges confirmed.
  - Lateran III (1179): Catholic courts' opinion of daughters worsens ("against nature"), and the physician's place at a Christian court is questioned (canon on Christian servants, *unverified* number).
  - Alan of Lille's hostile line as a Catholic opinion source.
  - Cathar neighbours: a Cathar lord may shelter her ("the soul has no sex", in his voice), at the price of leaving Judaism. That is a temptation, not an alliance.
  - The archbishop's licence: whether the worthies may shun her depends on Raymond de Bollène's goodwill.
- **Gate.** Unchanged: the Turning in Adar. Before 1323 the scroll step reads Esther with Rashi's Dinah. The revel is hers alone. The judgment is before "the worthies", with no baylons before 1215.
- **Carries over.** `tm_turning_decision` and the patience bonus; `tm_turning_niddui_effect` (now exactly the 1144 arrangement); `tm_hipukh.0030` (a book in Arabic, now contemporary); `tm_hipukh.0031` (the fisica); the Three Lamps; kahal matches; the pilgrimage; the Jewish-opinion modifier. The 1401 women's-council bonus stays gated.
- **New work.** One seed variant in `tm_on_game_start` keyed to 1178, three events and loc dating. No new mechanics.

### 3.2 A second house at Worms at 1066 (optional; plausible but thin)

- **Seat.** The Jewish community of Worms, in `c_worms`, held in 1066 by Emperor Henry IV (vanilla char 1316). Historically Henry IV gave the Jews and other men of Worms a toll privilege in 1074 and a protection privilege in 1090 (*unverified* dates). It is a branch of the same faith, not a new faith.
- **Starter characters** (fictional):
  - **Hanna (c. 50), the women's prayer-singer.** She repeats the reader's prayer aloud for the women. The narrator says "as the women of the Rhine later had their prayer leaders": Dulca is d. 1196, and the office is not attested at 1066.
  - **One Marked young woman (c. 18)** who has taken on the blessing over the lulav. Isaac ha-Levi's ruling, "one does not object", is cited by the worthies.
  - **A merchant household**, since Worms Jewry traded under imperial privilege.
- **Pressures.**
  - Rabbenu Gershom's *ḥerem* is the community's own ban power. In Ashkenaz it was not licensed by a lord the way Provence's was, so shunning is a stronger threat here (*suggestion*: no lord's veto; *unverified* as legal history).
  - The Hasidei Ashkenaz, at a 1178 start, would be the stringent pietist voice.
  - The Investiture Contest brings imperial protection or its absence.
- **Gate.** Prayer in Adar from Berakhot 60a alone (no Rashi yet at 1066), with the judgment before the community's worthies.
- **Content limit.** The 1096 massacres at Speyer, Worms and Mainz fall 30 years into a 1066 game. **Do not script them.** The Hebrew chronicles centre on martyrdom, including killing one's own children and oneself (Eidelberg 1977; Chazan 1987, *unverified* pages). That breaks the no-self-harm rule and the mod's choice not to model expulsions or massacres. If anything, use a quiet era flag that lowers the Rhineland house's growth after 1096.
- **Carries over.** Everything in §3.1 except the Provençal licence and the translator event.

---

## 4. Counter-evidence: what closed off or got worse

1. **Latin sodomy discourse hardens across exactly this window.** It starts with Peter Damian (1049) and runs through the reform synods (clerical celibacy at Lateran I 1123 and II 1139, *unverified* canons), Alan of Lille's "man made woman" (1160s–70s) and Lateran III canon 11 (1179). In 867 there was no such general-council law, and by 1178 there is. A daughter at a Catholic court is more exposed at 1178 than at 867.
2. **The Latin category system has no crossing toward womanhood.** It had female-to-male saints (Eugenia's trial carved at Vézelay, c. 1120–40: Mills 2018), and canonists sorted doubtful sex by the "prevailing sex", with no changing back (the canonists; the theologian Peter the Chanter added a sodomy rationale, 1190s: van der Lugt; Rolker 2013). Daughters fall under "fraud" or "sodomy", not heresy (comparanda list, findings 1 and 4).
3. **Crusade-era violence against Jews.** The Rhineland in 1096. Granada in 1066 (by Muslims). The Almohad end of Jewish al-Andalus in 1147. Ritual-murder accusations appear from 1144 (Norwich) and 1171 (Blois). These are listed only as historical context, **never as content**, by the mod's existing rule.
4. **Cathar heresy pulls the Church's attention to Occitania.** The 1178 legation and Lateran III canon 27 lead to the Albigensian Crusade (1209). For Arles's Jews this means more scrutiny of Christian–Jewish contact.
5. **Gershom's monogamy and divorce protections did not reach Provence.** The Rhineland's better position for women did not carry south.
6. **Beguines are too late for 1178.** Mary of Oignies was born in 1177 and died in 1213, and the first recognisable community dates from the early 13th c. Do not seat a beguine-like house at 1178.
7. **Ascetic stringency.** Provençal philosophy produced harsh statements about women (Grossman ch. 13 §2). The Hasidei Ashkenaz (later 12th c.) were stringent too.

## 5. Open questions

- Was Rashi's Torah commentary in use in **Provence** (not just northern France) by 1178? Check Ta-Shma or Ben-Shalom on the Provençal reception of Rashi.
- Does Moses ha-Darshan of Narbonne's midrash (11th c.; *Bereshit Rabbati*) carry the Dinah aggadah? If so, Narbonne has a 1066 textual anchor of its own.
- What was the exact legal position of the Jews of Arles in 1066, before the 1144 grant: count, archbishop or both?
- Get the exact wording of Lateran III canons 11, 26 and 27 from Tanner, *Decrees of the Ecumenical Councils* (1990), vol. 1, with page numbers.
- Pages for Sheridan's Alan of Lille (1980), Hart and Bishop's *Scivias* (1990), Cheyette (2001) on Ermengard, and Le Roy Ladurie on Cathar cross-sex transmigration.
- Is there any **pre-14th-c.** source for Cathar teaching that a soul passes between sexes (e.g. Moneta of Cremona c. 1241, Rainerius Sacconi 1250)? Without one, treat it as a later belief at 1178.
- Should the Worms house exist at 867 too, for consistency? Or should it be a 1066-only seed?
- Norman Palermo's eunuch office: hand it to whoever covers Adelphai Dorleyaiou and the Islamic Mediterranean.

## Sources used

Primary, in translation:
- Benjamin of Tudela, *Itinerary*, trans. M. N. Adler (1907), pp. 2–6 (Project Gutenberg #14981).
- Rashi on Gen. 30:21, trans. Rosenbaum and Silbermann (1929–34), via Sefaria.
- Alan of Lille, *De planctu Naturae*, trans. Moffat (1908); trans. Sheridan (1980).
- Hildegard, *Scivias* II.6.77, trans. Hart and Bishop (1990); her letter to the Mainz prelates (1178).
- Ibn Jubayr, as quoted in Ayalon 1999, pp. 312–313.
- Lateran III, canon 11 (EWTN text of Tanner).

Scholarship:
- Ben-Shalom 2024; Grossman 2004; Baumgarten 2016; Horowitz 2006; DeVun 2021; van der Lugt and Rolker via `comparanda_reading_list.md`; Kay 1990; Cheyette 2001; Jordan 1997 and Boswell 1980 (*unverified* pages); Pegg 2001 and Moore 2012 (historiography, not read here).

Game data:
- `history/titles/k_burgundy.txt` (`c_venaissin`); `k_aquitaine.txt` (`c_carcassonne`, `c_montpellier`); `k_east_francia.txt` (`c_worms`).
- `history/provinces/k_aquitaine.txt` (Cathar provinces from 1150).
