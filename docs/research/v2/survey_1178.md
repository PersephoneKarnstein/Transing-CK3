# 1178 survey: candidates for two new faiths (2.0.0)

Written 2026-10-24. Nothing in the repo was edited. Scope: religious settings c. 1150–1210 that could ground a new faith of trans women at the 1178 start, weighed against the two current candidates: the Visayan House at Cebu (`v2/visayan_dossier.md`) and the Old Prussian faith (`v2/wendish_dossier.md`).

**Built on (not redone):**
- `docs/later_starts.md` and `docs/research/later_starts/region_*.md` (the 2026-10-20 survey). It judged hubs mainly for the existing six faiths. Several of its "no hub" verdicts were made for that reason, and they do not carry over to a new faith. Japan, Java and Angkor are the main cases.
- `docs/research/south_reading_list.md`: Java's *kĕḍi* (finding 1), the Visayan candidate, and the Ethiopian "Gold Beneath the Wax" (candidate A, weak to moderate).
- `docs/research/sea_gyatso_cabezon_buddhist_law.md`: Vin III.35 and the three-changes rule. Its §"Deferred Southeast Asian Theravāda splinter" is the seed of candidate 2 below.
- `docs/faith_design.md` §0, §1 and the §16 writing rules (cited below as "rule n").

**New in this pass:**
- **Vanilla 1178 data from the installed game, which now includes the All Under Heaven map.** A parser over `history/titles`, `history/provinces`, `history/characters` and `common/landed_titles` gives holders at 1178.10.1. Faiths are now set by `rite =`, defined in `common/religion/rite_types/` and `faith_types/`. Barony-to-province matches are by regex, so the barony rows are marked *check*.
- **Japanese sources new to the project:**
  - the Kyoto National Museum's caption for the *Yamai no sōshi* "futanari" section;
  - Tsuji Hirokazu 2024 on men dressed as women in medieval performing arts;
  - the Kokugakuin University Museum exhibition *The History of Transgenderism in Japan* (6 Dec 2025 – 23 Feb 2026), whose object list has a chapter "Cross-dressing Shaman". It held a talk by Mitsuhashi Junko, a trans woman historian of Japan.
- **Other new items:**
  - Zhou Daguan's *Zhenla fengtu ji*, read in Chinese on Wikisource;
  - Than Tun's 1955 thesis on bhikkhunīs at Pagan (abstract only);
  - Indradevī's Phimeanakas inscription K.485 (secondary sources only).

**Ratings** (as in the brief): **strong** / **plausible** / **thin** / **exclude**. *Unverified* marks anything not checked at page level.

---

## 0. The answer in brief

1. **Japan at 1178 is the best new candidate on the map, and it is better than either current candidate.**
   - Its evidence is *in period and in place*: Kyoto and the Yodo river ports, 1160s–1180s.
   - The world is ready-made: the Taira at Kyoto, and the Genpei war from 1180.
   - The earlier survey said "no hub" for Japan. That verdict was about seating *Yutai Dao* there (no eunuchs, no palace knife), and the All Under Heaven map was not yet in the game. Neither reason applies to a new faith.
2. **The next tier:**
   - a Theravāda current at Pagan (doctrine and institution in period, but no person);
   - Java/Kediri's Inner Court (a category in period, recorded only as a defect);
   - Angkor under Jayavarman VII (an institution in period, with the gender witness 118 years late and hostile).
   All three are at least as good as the Visayan House, and much better than the Prussian faith.
3. **Recommendation (§3):**
   - **Japan**, as the song-houses of the Yodo river.
   - **The Visayan House**, kept, *or* Pagan in its place, depending on whether the user wants the second new faith Buddhist or not.
   - **Drop the Prussian faith.** It has no gender evidence at all, and in play it would repeat Bædling's pagan North.

---

## 1. Ranked shortlist (top 5)

### 1. Japan: the song-houses of the Yodo river (working name *Imayō no Ie*, "the Houses of the Present-Day Song"). **Strong.**

**Premise.**
- A current of Japanese Buddhism and kami worship, the two joined as they were (*shinbutsu shūgō*).
- It is kept by trans women who live and sing inside the female-headed households of the *asobi* (river-port singers at Eguchi and Kanzaki in Settsu) and the *kugutsu* (the travelling singers of Aohaka in Mino).
- Its scripture is the song itself:
  - the *imayō* passed from mother to daughter of the house;
  - the Lotus Sūtra, whose Kannon "appears in a woman's body" to those who are to be saved through one;
  - the *Vimalakīrti*, in which a goddess turns Śāriputra into a woman to answer his doubts.
- Its kami is the house-god of the singers, Hyakudayū (Momodayū).
- Daughters may also be drum-diviners on the roads of the capital. They are the women the scroll-painters mocked.

**Evidence (dated, in period unless flagged).**

*Song and the houses:*
- **The houses' god (c. 1100).** Ōe no Masafusa (1041–1111), *Yūjoki* ("Record of the Asobi"): the asobi of Eguchi and Kanzaki worship Hyakudayū. His *Kairaishiki* has the kugutsu worshipping the "hundred kami" (via Kokugakuin's kami encyclopedia). The *Ryōjin hishō* has asobi pray to Momodayū for men's love.
- **The song lineage (1169–79).** *Ryōjin hishō* and its *Kudenshū*, compiled by the retired emperor Go-Shirakawa:
  - He learned *imayō* from the aged kugutsu singer **Otomae** of Aohaka, who died in 1169.
  - Her art came down through "four generations of teachers" (summary via Wikipedia; *unverified* in the *Kudenshū* itself).
  - This is the faith's line: a female lineage of song, passed between women and reaching even an emperor.
- **The tale (c. 1180).** *Torikaebaya monogatari*. The *Mumyōzōshi* (1200–02) knows an old and a new version, and the extant one is late Heian:
  - The son lives as a woman and serves as *naishi no kami* in the women's palace.
  - The tale ends by "returning" both siblings, and the faith reads it against the grain.
  - Whether the princess served is a female crown prince: *unverified* (Willig 1983; Pflugfelder 1992).
  - A new English translation, *Torikaebaya Monogatari: A Japanese Tale of Gender-Swapped Siblings*, is out from Stanford UP. The translator's name is *unverified*.

*The drum-diviner and men in a miko's dress:*
- **The drum-diviner (late 12th c., Kyoto).** *Yamai no sōshi*, "futanari" section (Kyoto National Museum, a National Treasure). The museum's caption reads: "The depicted man, carrying a hand drum from his neck, had often been spotted in Kyoto." The museum ties the figure to "male shamans (otoko miko) who donned female clothing".
  - **Caution:** the scene is an exposure. Men undress the diviner in her sleep to look, the scroll frames her as a sickness, and she is labelled intersex.
  - The faith may cite only the hostile record of *a drum-diviner on the capital's roads whose ways were a woman's*. **No body reveal (rule 5)**, and no claim that she was a daughter.
- **Men dressed as miko (medieval).** Tsuji Hirokazu, "日本中世の芸能と異性装―女装を中心に", *Joseigaku hyōron* 38 (March 2024), pp. 5–29 (open access; abstract read, PDF is images):
  - men dressed as shrine maidens to perform *dengaku*, as a means to "enhance the effect of prayer";
  - at banquets, men's cross-dressing occurred in "relatively equal relationships";
  - women's cross-dressing served male audiences.
  - Exact dates of the cases: *unverified*.
- **Male shamans at court (1015).** Fujiwara no Michinaga's diary (*Midō kanpakuki*) records a male shaman summoned for Emperor Sanjō's eyes in 1015 (via search summary; *unverified* in the diary). This is earlier than our window, but it shows the office existed.
- **The *jisha* (13th c.).** Kokugakuin's exhibition opens its chapter "Transgender Individuals in Medieval and Early Modern Japan" with a "Cross-dressing Shaman", the *jisha* of the *Tsurugaoka hōjōe shokunin uta-awase* (13th c., Kamakura).
  - **Caution:** Yanagita Kunio described the *jisha* figure as "a child in female dress" (女装せる童兒, via a search summary of his collected works). The figure may be a minor, so **do not use the *jisha*** (minors guardrail). Cite only the exhibition's framing, if anything.
  - Another reading makes 持者 short for 持経者, "sutra-holder", an ascetic like a *yamabushi* (benricho.org, from the 1769 edition).

*The Buddhist frame, in the faith's voice:*
- **Lotus Sūtra, ch. 25.** Kumārajīva's text: 「應以…婦女身得度者，即現婦女身而為說法」, "to those who should be saved by a woman's body, she appears in a woman's body and preaches" (text from memory; *verify* the wording).
- **Vimalakīrti** (Scherer 2006 §3): the goddess turns Śāriputra into a woman.
- **The hostile Buddhist voice.** The doctrine that women must first become men (*henjō nanshi*), with the Lotus dragon girl who "becomes male" (ch. 12), is the hostile Buddhist line, not the faith's.

*World and flavour:*
- **The Eguchi head-woman as Fugen.** Tales of a holy man who sees the head-woman of Eguchi as the bodhisattva Fugen: *Kojidan* c. 1212–15, *Jikkinshō* 1252 (from memory; *unverified*). This is reaction flavour, and it must not be made into "accepted for a sacred role" (rule 7).
- **Prince Mochihito's flight (1180).** He fled the Taira in women's dress (*Heike monogatari* bk 4; *Azuma kagami*). Settsu's 1178 holder, Minamoto no Yorimasa, raised the revolt with him and died at Uji. This is world flavour only: a disguise, not a daughter.

**Map (vanilla 1178).**
- **Emperor and capital.** `e_japan` and `c_yamashiro` (b_kyo, b_uji) are held by Taira no Kiyomori (`japanese_taira_kanmu_34`, b. 1118, culture `japanese`, rite `pundarika` = Tendai, under `mahayana_faith`). Government `japan_administrative_government` at the county, feudal at the empire. Development 33.
- **Settsu.** `c_settsu` (b_fukuhara, b_watanabe, b_nose) is held by Minamoto no Yorimasa (`japanese_minamoto_seiwa_59`, b. 1104), rite `pundarika`, `japan_feudal_government`, development 28.
  - Eguchi and Kanzaki lie in Settsu at the Yodo mouth, and Watanabe is the nearest barony (*check* on the map). Fukuhara is Kiyomori's port (the 1180 capital).
- **Mino.** `c_mino` (Aohaka, the kugutsu town, *check* its barony) is held by Minamoto no Mitsunaga (`japanese_minamoto_seiwa_245`), rite `pundarika`.
- **Kumano.** `b_kumano` in `c_kii` (holder Yuasa Munekage, rite `mantrayana`) would suit a holy site: Go-Shirakawa's Kumano pilgrimages (*count unverified*).
- **The faith's family.** Vanilla gives a `shinto_faith` with a `shinto` rite, and the Buddhist rites `pundarika`, `mantrayana` and `dhyana`. Put the new faith in `mahayana_faith` as a rite beside `pundarika`, with Hyakudayū as a kami of its own. That is the joined practice of the period.

**Likely gate, office and hooks.**
- **Gate: "The Song Received".**
  - A mother of the house teaches her the lineage songs over seasons. At a gathering of houses she sings one back, and the houses answer.
  - The community answers, as in Ethiopia's *qəne* idea, but through song rather than code.
  - This differs from the knife, the seat, gestation, the Turning, the garland and the smith. No pain test (rule 22), and no oath (rule 23).
- **Office: the head-woman of the house** (*chōja*). Goodwin discusses female-headed houses; page *unverified*.
- **Line: the song lineage, mother to daughter, born or taken** (rule 20).
- **The road not holy (rule 7):**
  - the river-port trade;
  - an estate a patron may grant to a woman's house (*check* how women's *shōen* rights worked);
  - court service as a lady-in-waiting, the Torikaebaya road.
- **World:**
  - the 1180–85 Genpei war;
  - the Taira at Fukuhara;
  - the burning of Nara (1180);
  - a hostile Tendai preacher's *henjō nanshi*.
- **Hostile voices** (rule 3): the scroll-painter's "sickness"; a Kamakura law court.

**Risks.**
- **The sex-trade frame.** Goodwin's book is subtitled *The Sex Trade in Heian and Kamakura Japan*, and Lin'an already raises the same issue. Give the faith song, the river trade and land, and never make sex work its identity or its entrance.
- **Orientalising.** No geisha or "floating world" imagery: that is Edo, 500 years later. No exotic-East narration.
- **Minors.** *Chigo* and the *jisha* are out. No novice under 16.
- **The *Yamai no sōshi* exposure.** Use only as a hostile record, never as a scene.
- **Third sex.** Do not adopt *futanari* (二形) as a name for daughters. It is the scroll's word for a body.
- **Shirabyōshi** stay out: they are women in men's dress.
- **Living communities.** No modern Japanese trans community claims a medieval religious ancestor, so the risk here is low. Still, do not borrow modern *okama* or *new-half* terms.
- **Historical figures.** Do not claim Otomae, Go-Shirakawa, Mochihito or Yorimasa (narrator rule).
- **Scholars.** Weight Japanese scholars first: Mitsuhashi (a trans woman), Tsuji, Wakita Haruko, Amino Yoshihiko. Read Goodwin and Pflugfelder after them. Goodwin rejects the "shaman-entertainer" link that much Japanese scholarship assumes, so the gate should not rest on it.

**Books to find.**
1. Mitsuhashi Junko, 『女装と日本人』 (Kōdansha gendai shinsho, 2008), the medieval chapter. Also her 『歴史の中の多様な「性」』 (Iwanami, 2022).
2. Tsuji Hirokazu, 『中世の〈遊女〉―生業と身分』 (Kyoto Univ. Press, 2017), and the 2024 article above (the PDF needs OCR).
3. Janet R. Goodwin, *Selling Songs and Smiles* (Hawaiʻi, 2007). Also Yung-Hee Kim, *Songs to Make the Dust Dance: The Ryōjin hishō* (1994), and Pflugfelder 1992 with Willig 1983.

**Against the current two.** This candidate has in-period evidence where the Visayan has none before 1521 and the Prussian has none at all. It also has a living court world in vanilla, a dated war two years after the bookmark, and an insider trans historian to read. It is weaker than Cebu only in that the gender evidence is scattered (a scroll, a tale, men in a miko's dress), while Cebu's later sources describe a whole office.

---

### 2. Pagan (Burma): "The Transfer" (working name; Pāli *liṅga-parivatta*). **Plausible to strong.**

**Premise.**
- A Theravāda current at Pagan. It holds to the rule of the Vinaya itself: when a monk's sign changes to a woman's, she joins the nuns with "the same teacher, the same ordination, the same rainy seasons".
- It refuses Buddhaghosa's gloss that the change is a karmic fall, and it keeps women's ordination alive in a city that still had nuns.
- This idea is already sketched in the repo (`sea_gyatso_cabezon_buddhist_law.md`, "Deferred Southeast Asian Theravāda splinter"). The new facts here make Pagan in 1178 its best seat.

**Evidence.**
- **The rule.** Vin III.35 (Pārājika 1): "I allow her a preceptor, I allow her the ordination", and the same for the reverse case (Scherer 2006 §1). The Mūlasarvāstivāda version bars ordination only after a third change (Gyatso 2003, pp. 110–111, already in the repo).
- **A within-life change (narrative).** Soreyya, in the Dhammapada commentary 3.9 on v. 43: a man becomes a woman, bears children, then changes back. The tale reads the change as lust's karma, so it is a hostile text the faith answers.
- **Nuns at Pagan (in period).** Than Tun, *The Buddhist Church in Burma during the Pagan Period, 1044–1287* (PhD, SOAS 1955; open on SOAS eprints 28633). From inscriptions, he finds bhikkhunīs "right up to the end of the Pagan dynasty", and he names several. Luce agrees (via the SuttaCentral thread and the abstract). *Read the thesis chapter.*
- **The 1178–90 context.**
  - Narapatisithu reigns 1174–1211.
  - The monk Chapaṭa returns from Sri Lanka c. 1180–90 with a Sinhalese ordination line, and Pagan's saṅgha splits into the Mramma and Sīhaḷa lines (Than Tun; dates *unverified*).
  - Reordination and lineage are the live question of the decade, which suits a faith whose doctrine is "same ordination".
- **Counter-evidence.** Sri Lanka's nun order lapsed c. 1017 (still sourced only to newspapers, *unverified*). Parākramabāhu I's 1165 purge. The commentary says a change before ordination bars it. Ordination asks every candidate whether they are a *paṇḍaka* (Cabezón ch. 7).

**Map.**
- `k_pagan` is held by Narapatisithu (`pagan_1`, b. 1150), culture `burmese`, rite `theravada`, `mandala_government`.
- `c_pagan`/`b_pagan` is a `temple_citadel_holding`, theravada.
- Mon vassals at `c_thaton` (Gada) and `c_pegu` (Bawlawkyantaw), both theravada. Thaton is the old source of Pagan's ordination line.
- **Faith:** a rite under `theravada_faith`.

**Gate, office and hooks.**
- **Gate: "The Sign Changes".** A declared daughter who is ordained, or a lay devotee, goes before a chapter. If a nuns' chapter accepts the transfer, she keeps her seniority. This is the existing `tm_vinaya_transfer_modifier` idea promoted to a gate.
- **Office:** the senior nun (*therī*) of a nunnery the faith endows.
- **Not holy:** donors' inscriptions. Pagan's laywomen endowed temples and land, so a daughter can be a donor with her name in stone. That is the road of standing.
- **World:**
  - the Sīhaḷa reform asks every nun for her lineage;
  - Mon Thaton is the old orthodoxy;
  - nat worship lies outside the faith.

**Risks.**
- **A living religion with a nun question.** Theravāda women's ordination is a live dispute today. Keep the faith a small invented current and say so.
- **Never use *nat kadaw*.** Modern spirit mediums in Myanmar, many of them trans women, are a living and persecuted community (Ho Tze Ming 2009 is modern ethnography).
- **Third sex.** *Paṇḍaka* and *ubhatobyañjanaka* are exclusion categories. Never use them as the faith's own name (Bhatt, via the repo's Gyatso note §0).
- **Bodies.** The change of "sign" is bodily in the text. Write it as the faith's word for her womanhood and never describe her body (rules 5, 8).
- **Distinctness.** Yutai Dao is Daoist, so this does not repeat it. But if Japan is also chosen, two Buddhist faiths sit side by side.

**Books.**
1. Than Tun 1955 (open access).
2. G. H. Luce, *Old Burma – Early Pagan* (1969–70).
3. Michael Aung-Thwin, *Pagan: The Origins of Modern Burma* (1985). Also Peter Skilling's articles on the bhikkhunī saṅgha in Southeast Asia (*unverified* which).

**Against the current two.** It has in-period doctrine and an in-period women's institution in place, but no attested daughter. That is weaker on lived gender crossing than Cebu's later office, and far stronger than Prussia. Its mechanics (lineage, seniority, the saṅgha split) are unlike any of the existing six.

---

### 3. Java/Kediri: "The Inner Court" (Wṛhannalā's Year). **Plausible to strong as a *new* 1178 faith.**

**Premise.** Already designed in `south_reading_list.md` (candidate B, "Alternative"):
- a Śaiva current at a Kediri court;
- its daughters are counted by the charters among the *kĕḍi* of the *watĕk i jro* (palace dependants);
- it refuses that category's meaning (a defect, *wikāra*, the fruit of a past life's fault) while living in the place the category gave them.

**Why it rises now.** The earlier survey rated Java "plausible to thin" for a *start* because "nothing changes between 867 and 1178". That is irrelevant to a new faith. In 1178 Kediri is at its literary height:
- the *Bhāratayuddha*, begun in 1157 by Mpu Sĕḍah for Jayabhaya;
- the *Smaradahana* of Mpu Dharmaja for Kāmeśvara, 1180s (*unverified* date).
And the category is attested in charters from 873 to 1305.

**Evidence** (all from the repo's notes):
- OJED glosses *kĕḍi*. The *Ślokāntara* defines it as "strī tan strī", "a woman and yet not a woman" (OJED p. 2180).
- The *Wirāṭaparwa* (996): Arjuna "atĕmahana kĕḍi makasajña Wṛhannalā" (OJED p. 838).
- No rite, cult or self-description survives.

**Map.**
- `c_JAV_janggala` (with `b_JAV_Daha`, Kediri; *check*) is held by Āryeśvara (`javanese_ishana_15`, b. 1131), rite `shaivism`, culture `javanese`, `mandala_government`, liege `d_JAV_mataram`.
- Āryeśvara is a historical Kediri king (r. c. 1171–81), so do not convert him. Start landless at his court.

**Gate, office and hooks.**
- Gate: Wṛhannalā's Year, the repo's design of concealment and unveiling.
- Office: within the Inner Court.
- Hooks: kakawin patronage (the poet's road, not holy); the Śaiva karmic reading as the hostile voice.

**Risks.**
- The *kĕḍi* is recorded as a defect, and as "neither": the third-sex trap (Bhatt).
- Modern *kedi* is slur-adjacent (*banci*).
- The Bugis *bissu* are nearby, a living community, and must stay out.
- The Wṛhannalā material comes from the *Mahābhārata*, which the Tamil Garland may also touch.
- Island Southeast Asia is the Visayan candidate's region too: choose one of the two.

**Books.**
1. Zoetmulder, *Old Javanese–English Dictionary* (OJED, 1982).
2. Helen Creese, *Women of the Kakawin World* (2004).
3. S. Supomo, *Bhāratayuddha* (1993; Indonesian editor). Also Boechari's epigraphy.

**Against the current two.** It is better attested in period than Cebu (a category in charters, against nothing before 1521), but the category is recorded only as a defect, while Cebu's later sources show a respected office. It is far above Prussia. It overlaps the Visayan in region: pick one.

---

### 4. Angkor under Jayavarman VII: the Women's Colleges (working name). **Plausible.**

**Premise.**
- A Mahāyāna current in the Khmer capital in the years of ruin and refounding: the Cham sack of 1177 and Jayavarman VII's consecration in 1181.
- Its daughters live and teach inside the women's colleges of the royal foundations, and among the foundlings and dancers of the queens' houses.

**Evidence.**
- **The colleges (in period, 1180s–1200s).** Indradevī's Phimeanakas inscription (K.485, Sanskrit, late 12th or early 13th c.):
  - she headed three Buddhist "colleges", Nagendratunga, Tilakottara and Narendrāśrama, apparently for women and girls;
  - the queens set up a refuge for abandoned girls (Wikipedia "Jayarajadevi" and the Thai journal abstract; *verify* in Cœdès, *Inscriptions du Cambodge* II).
- **Temple dancers (in period, 1186).** Ta Prohm's stele lists 615 dancers (secondary, already in the repo; *verify*).
- **The gender witness (late, hostile).** Zhou Daguan, *Zhenla fengtu ji*, 人物 section, from 1296–97, 118 years after the bookmark. He writes 「國中多有二形人，每日以十數成羣，行於墟場間」: "many persons of two forms … in groups of ten or more" in the markets. He adds that they court Chinese men, and calls it 「可醜可惡」, "ugly and hateful".
- **No nuns.** The same text says Angkor has 「却無尼姑」, no Buddhist nuns, but has female ascetics among the *basi* (八思惟) (§三教).

**Map.**
- `d_angkor` and `c_angkor` are held by Jayavarman (`khmer_mahidharapura_17`, b. 1122), rite `mahayana`, `mandala_government`, independent. `e_kambuja` is vacant at 1178, which fits the post-sack moment.
- `b_angkor` is a temple citadel with Shaivism as its province faith.
- Champa (`k_champa`, Jaya Indravarman, Shaivism) is the occupier and rival.

**Gate, office and hooks.**
- Gate: reading at a college, through the teacher's acceptance.
- Office: a college mistress.
- Hooks: the 1181 refounding; hospitals and rest-houses (J7's 102 hospitals); the Cham war.

**Risks.**
- The only gender witness is a foreign, hostile, sexualised gaze, written a century later.
- The modern Khmer *khteuy* are a living community: do not take the name.
- The *erxing* ("two forms") label is the third-sex trap.
- The temple dancers overlap the Garland's temple women.
- Orientalising risk (*apsaras*).
- Jayavarman VII and the queens are historical: do not claim them.

**Books.**
1. G. Cœdès, *Inscriptions du Cambodge* II (K.485).
2. Peter Harris (trans.), *A Record of Cambodia* (2007).
3. Trudy Jacobsen, *Lost Goddesses* (2008). Also Khmer scholars (Ang Choulean) for the religion.

**Against the current two.** It has a strong in-period institution, but its only gender witness is late and hostile. That is about level with Cebu (late but respectful) and well above Prussia.

---

### 5. Cathar Lauragais: a House of Good Women (working name). **Plausible, but in conflict with two writing rules.**

**Premise.** A daughter lives as a *bona femina* in a house of Cathar women perfects in the Lauragais (Fanjeaux, Laurac, Montréal) in the decade of the 1178 papal legation.

**Evidence.**
- **The houses.** Women perfects kept houses before 1209: Fanjeaux, and the perfectae lines of Guillelme de Tonneins and Aude de Fanjeaux. These come from depositions of the 1240s about c. 1200 (Barber 1977, "Women and Catharism", *Reading Medieval Studies*, open access).
- **The doctrine.** Fallen angelic souls with no sex. Cross-sex transmigration is attested only in the 14th-c. Fournier register, so it is late. No pre-1250 source for it was found (Eckbert 1163 and Durand c. 1190s were checked by summary only).
- **The map.** In vanilla 1178, Toulouse, Albi, Carcassonne, Béziers and Agen are `cathar_rite` provinces (repo note). `c_toulouse` is held by Count Raymond (V) of Toulouse, `roman_rite`, while the province `b_toulouse` is `cathar_rite`.

**Gate, office and hooks.** The *consolamentum*; the house as refuge; the 1178 legation; Lateran III, canon 27.

**Risks.**
- **Rule 25 forbids any claim that a sect "has Cathar ties".** This faith would be one.
- **Rule 18 forbids lines saying no one is truly a man or a woman.** Cathar sexless-soul doctrine says almost exactly that.
- Ha-Nehpakhot is next door (Arles, Narbonne).
- The perfecti renounce the body, which does not fit a faith that wants her womanhood lived.

**Books.**
1. Malcolm Barber, *The Cathars* (2000).
2. Claire Taylor, *Heresy in Medieval France* (2005).
3. Peter Biller, "Cathars and Material Women" (2001).

**Against the current two.** Better institutions than Prussia, but the doctrine works against the mod's premises, and it breaks two of the user's own rules. Not recommended.

---

## 2. Everything else considered

Each line: region | idea | rating | why.

| Region | Idea | Rating | Why |
|---|---|---|---|
| Song China, Lin'an | Guanyin's women at Upper Tianzhu (the White-robed Guanyin; the Miaoshan legend, 1100 stele by Jiang Zhiqi) | plausible | In-period feminisation of a male bodhisattva (Chün-fang Yü, *Kuan-yin*, 2001; Dudbridge). But Lin'an is already Yutai Dao's planned second house. Better as a Buddhist neighbour event for Yutai. |
| Dali (Yunnan) | Acuoye Guanyin and Zhang Shengwen's scroll (1172–76) under Duan Zhixing (`k_dali`, `dali_duan_29`, rite `acharya`, culture `bai`) | thin | A royal esoteric Buddhism, but no gender-crossing evidence. Dali's Guanyin stays a slender male prince. |
| Tibet (`c_lhasa`, rite `lamaism`) | Gcod lineage of Machig Labdrön (c. 1055–1149/53); men's self-generation as Vajrayoginī | thin to plausible | Women's lineages are in period. Tantric female self-visualisation is ritual metaphor (Cabezón ch. 7: never "social tolerance"). The repo's Gyatso note forbids "ma ning deity" content. No daughter evidence. |
| Tangut Xia | Tiansheng code (1149–69) on monks and nuns | thin | Covered by the Yutai notes. No gender-crossing item. |
| Jin / Liao / Qara Khitai | Khitan and Jurchen shamanism; Yelü Pusuwan's reign (1163–77) | thin | A woman ruler is reaction only. Steppe shamanism leads to the modern-ethnography trap. |
| Mongol steppe | shamans | exclude | Modern ethnography; the "third gender" trap. |
| Goryeo (`muism`) | *mu* shamans in the capital (Yi Kyu-bo's "Old Shaman", early 13th c.) | exclude | *Mudang* are a living community. No male-to-female role in period (earlier survey). |
| Japan | *Shirabyōshi*, *chigo*, *jisha* | exclude | Women in men's dress; minors; possibly minors. |
| Japan | Kumano as a holy site (`b_kumano`, `c_kii`) | flavour | A holy site for candidate 1. |
| Đại Việt (`b_thang_long`, rite `dhyana`) | Lý-dynasty Thiền | thin | Nothing found. *Lên đồng* is late and living. |
| Champa (`k_champa`, Shaivism) | the Po Nagar goddess cult | thin | No gender item. Modern Cham priestesses are living and late. |
| Haripuñjaya (Mon, `mahayana`) | Queen Cāmadevī legend | thin | Chronicle late (15th c.). A cis queen. |
| Sri Lanka | Polonnaruwa reform 1165 | counter-evidence | The nun order lapsed (*unverified*). Use as a hostile voice for candidate 2. |
| Srivijaya / Sumatra | — | thin | No sources found. |
| Bali | Old Balinese charters (*kdi*?) | thin to plausible | An unchecked lead (Goris 1954). Merge into candidate 3 if it is found. |
| Philippines | Visayan House at Cebu (current candidate) | plausible | Evidence 1521–1685, back-projected (dossier). The best *office*, with the weakest dating. |
| Baltic | Old Prussian faith (current candidate) | thin | No gender evidence in either region; an invented inversion (dossier §1.5). Repeats Bædling's pagan North. |
| Kashmir | Kṣemendra; Kalhaṇa | thin | Satire and chronicle; no crossing figure. |
| Bengal (Sena) | *Gītagovinda* *sakhīs* | thin | Men living as *sakhī* is 16th c. and later. |
| Odisha, Puri (`c_puri`, Ragaraja, Vaishnavism) | *mahārī* temple women of Jagannātha (Anantavarman Choḍagaṅga, c. 1135) | thin | Duplicates the Garland. Dating of the *mahārī* *unverified*. |
| Kannada country (`c_kalyani`, Sankama, Shaivism) | Śaraṇa bride voice (Basavaṇṇa, Dāsimayya, 1160s) | thin / exclude | Liṅgāyats are a large living community. Voice only, no life (repo). |
| Gujarat | Jain *napuṃsaka* law; Bahuchara Mātā | thin / exclude | Third-sex trap. Bahuchara's cult is late and is the hijra's living goddess. |
| Ghurids / Khwarazm | — | reaction | The Islamic world closes (later_starts.md). |
| Georgia (`c_tbilisi`, `georgian_rite`) | Tamar crowned 1178 and styled *mepe*, "king" | flavour | Female-to-male title; reaction only. |
| Armenia / Alans | — | thin | Nothing found. |
| Alamut (`b_alamut`, in `c_qazwin`) | the Nizārī *qiyāma* of 1164 (law abrogated) | thin | Antinomian but no gender content. Risk to a living Ismāʿīlī community. |
| Yazd / Kerman | Zoroastrians | thin | Vendidad hostility; nothing in period. |
| Baghdad / Rayy | *mukhannathūn* | event pack | 1066, not 1178 (repo). |
| Ethiopia (`c_lasta`, `ethiopian_rite`) | "The Gold Beneath the Wax" (*qəne*) at Zagwe Roha | plausible to thin | Designed in the repo (weak to moderate). Zagwe 1178 is a good moment, but there is no gender evidence and the church is living. A reserve. |
| Nubia (Makuria, Alwa) | refuge | thin | Would be a weaker Adelphai. |
| Kanem | queen mother | flavour | Repo. |
| Yoruba, Ife (`c_ife`, holder Sabe, `west_african_orisha_pagan`) | Ṣàngó's "wives" (*elégùn*) | exclude | Oyo is post-1300; Matory's evidence is 19th–20th c. A living Òrìṣà religion; Oyěwùmí-style "genderless" readings are the third-gender trap. Repo already says no. |
| Igbo-Ukwu | — | out of window | 9th–10th c. |
| Great Zimbabwe / Mapungubwe | — | off map / thin | No source. |
| Swahili coast | *mashoga* | exclude | A living community. |
| Almohad Maghreb | — | reaction | Hostile reform preaching (repo). |
| Latin Europe | Liège *mulieres religiosae* (Lambert le Bègue d. 1177) | thin | The repo says beguines are too late for 1178. No daughter evidence. |
| Latin Europe | Fontevraud, Hildegard (d. 1179), Alan of Lille's *De planctu* | flavour / reaction | Repo. |
| Sicily (William II) | palace eunuchs; Ibn Jubayr on Palermo's women (1184–85) | Adelphai flavour | Repo. |
| Iberia | Mozarabs; Toledo translators | thin | Medical hermaphrodite texts only. |
| Iceland | Grágás dress clauses; Laxdæla | Bædling flavour | Same North. |
| Sámi / Finnic / Estonian | — | thin | Modern noaidi ethnography; Henry of Livonia already in the Prussian dossier. |
| Volga Bulgaria / Cumans / Rus' *skomorokhi* | — | thin / exclude | Repo: modern ethnography or nothing. |
| Byzantium 1178 | the House in Exile at Kyzikos | (existing faith) | Not a new faith. |

---

## 3. Recommendation

1. **Take Japan as the first new faith.** It is the one candidate with:
   - in-period, in-place evidence (the scroll, the tale, the songbook, men in a miko's dress, the singers' own god);
   - an insider trans historian to read first (Mitsuhashi);
   - a vanilla court world, with a war beginning in 1180;
   - no living community it would impersonate.

   **Conditions:**
   - The gate rests on song and the houses' answer, never on exposure or a body.
   - Chigo, *jisha* and *shirabyōshi* stay out.
   - The faith is not defined by sex work.
   - The README says that the drum-diviner and the miko-dressed men are hostile or ambiguous records, read by the faith in its own voice.
   - **First step:** OCR Tsuji 2024 (the repo's `ocr.swift` handles images; add `ja-JP` to its languages) and get Mitsuhashi 2008.
2. **For the second faith:**
   - **(a) Keep the Visayan House** if the user wants the mod's map and religious spread widest:
     - Japan is Buddhist and kami;
     - Cebu is a vanilla pagan family with a whole ritual office;
     - their gates differ (song answered, against the sacrifice and feast).
     - Its weakness is honest back-projection, which the dossier already handles.
   - **(b) Choose Pagan** if the user prefers in-period doctrine over late ethnography. Two Buddhist faiths would sit side by side, but Theravāda monastic law and Japanese song-houses play very differently.
   - **Java (the Inner Court)** is the best alternative to Cebu inside island Southeast Asia, and the stronger choice if in-period dating matters more than the respect of the record. Do not take both Java and Cebu.
3. **Drop the Prussian faith for 2.0.0.**
   - It has no gender evidence in its own region or the Wendish one.
   - It would be an invented inversion on a crusade frontier that Bædling's North already covers in tone.
   - Keep the dossier for a later 867 or 1066 Wendish design, as the dossier itself suggests.
4. **Keep as reserves:** Angkor (strong institution, late hostile witness) and Ethiopia (Zagwe; the *qəne* gate).
5. **Do not take:** Cathars (rules 18 and 25); Lingāyat, mudang, hijra/Bahuchara, bissu, *nat kadaw*, Òrìṣà and *mashoga* (living communities); steppe and Cuman shamans (ethnography trap).

---

## 4. Sources used in this pass

- **Kyoto National Museum / Google Arts & Culture**, "Diseases and Deformities (Yamai no Sōshi)": https://artsandculture.google.com/story/vwUxsMohoOz3Jg. Also the museum's Futanari caption via search: "otoko miko … who donned female clothing".
- **Tsuji Hirokazu**, "日本中世の芸能と異性装―女装を中心に", *Joseigaku hyōron* 38 (2024): 5–29. https://kobe-c.repo.nii.ac.jp/records/2000264 (abstract; the PDF is images).
- **Kokugakuin University Museum**, *The History of Transgenderism in Japan*, object list (EN PDF) and flyer (JP PDF): museum.kokugakuin.ac.jp/files/user/2025_seibetsuekkyou_list_en.pdf and 2025_seibetuekkyou.pdf. Chapter III §1 is "Cross-dressing Shaman" (Tsurugaoka *uta-awase*, 13th c.). The talk was by 三橋順子 (Mitsuhashi Junko).
- **Kokugakuin**, *Encyclopedia of Shinto*, "Momodayū" (via search summary): Yūjoki and Kairaishiki.
- **Burkhard Scherer**, "Gender transformed and meta-gendered enlightenment", *REVER* 3 (2006): Vin III.35; Soreyya (DhpA 3.9); Vimalakīrti; Lotus ch. 12.
- **Zhou Daguan**, *Zhenla fengtu ji*, zh.wikisource (raw text): §人物 (二形人) and §三教 (無尼姑; 女道士).
- **Than Tun** 1955 (SOAS eprints 28633; abstract), and the SuttaCentral thread on Pagan bhikkhunīs.
- **Phimeanakas K.485**: Wikipedia "Phimeanakas" and "Jayarajadevi"; *Thai Khadi Journal* abstract. Secondary only.
- **Malcolm Barber**, "Women and Catharism", *Reading Medieval Studies* 3 (1977) (open access; not read here, cited from search).
- **Yü Chün-fang**, *Kuan-yin* (2001), and Dudbridge on the 1100 Miaoshan stele (via search).
- **Vanilla CK3** (All Under Heaven install): `history/titles/e_japan.txt`, `e_khmer.txt`, `k_*`; `history/characters/japanese.txt` etc.; `common/religion/rite_types/00_rite_types.txt` (`pundarika`, `mantrayana`, `dhyana`, `lamaism`, `shinto`, `cathar_rite`). Parser at `scratchpad/surv2/at1178.py`.
