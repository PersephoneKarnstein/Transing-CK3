# East Asia at 1066 and 1178: starts for Crusader Dolls

Region: Song, Liao, Western Xia (Tangut), Jin, Goryeo, Heian Japan. Faith seated here: **Yutai Dao** (Shazhou / Dunhuang).
Written 2026-10-20. Builds on the repo notes in `docs/research/` (cn_*, east_*, china_reading_list.md) and does not repeat them. "Repo note" means a claim already verified there. Anything new was checked against primary text (zh.wikisource, read in Chinese) or scholarship found online. Anything not checked is marked **unverified**.

**Vanilla facts** (from the installed game's `history/titles/e_china.txt`, `e_japan.txt` and `history/characters/`):
- **c_shazhou.** 1066: held by Tangut "Suogu" of the Yeli clan (id 206725), liege d_guasha, liege k_xia, meritocratic. 1178: held by Tangut "Jichong" of the Weimu clan (206807). Both have `rite = "zhengyi"`, so vanilla already codes Shazhou's lords as Daoists.
- **c_hangzhou (Lin'an).** 1178: held by han_11858 of the Zhao clan, rite dhyana, development 60, the highest of the three dates (16 in 1066).
- **c_yamashiro (Kyoto).** 1066: Fujiwara no Yorimichi. From 1167: Taira no Kiyomori.
- **c_dengzhou (Shandong, Sun Bu'er's country).** 1178: a fictional Jurchen magistrate.

---

## 1. Verdicts for Yutai Dao

### 1066: carry forward with stand-ins, plus a little new flavour

What changed between 867 and 1066, weighed against the test:

- **Who holds the seat.** The Guiyi circuit is gone. The Tanguts took Shazhou in 1036 (Rong 2013, p. 46; repo note). Tangut control was weak at first: the Guiyijun still sent tribute to the Song until 1052, and direct Xia rule is attested by 1070 (Rong 2013, p. 47).
  - Some scholars put a "Shazhou Uighur" regime in the gap, c. 1036–1068, and credit it with 27 new or rebuilt caves. This is contested: it is reported in secondary summaries and was not read in a monograph (**unverified**).
  - Either way, a non-Han Buddhist overlord rules a Han Daoist remnant. That is the faith's 867 premise again (Tibet then, Xia now), not a new one.
- **Institutions.** The library cave was sealed c. 1006, in good order, probably from fear after Khotan fell to the Karakhanids (Rong 2013, pp. 131–133; repo note).
  - The she documents that ground the Temple Societies all predate 1002. After the sealing we lose the evidence, not necessarily the institution. At 1066 the societies become the faith's memory and practice, with no new attestation.
- **Song gender order.** Women were 3–4% of the registered Daoist clergy: 738 nuns in 1068 against 18,746 men (Despeux and Kohn 2003, p. 201; repo note). Taizu's edict of 972 sorted renunciants by the rule "there are distinctions between men and women" (Cheng 2021, p. 120; repo note).
  - Both already feed the mod's era arc and change nothing at the seat.
- **Texts.** The *Wuzhen pian* (c. 1075) is still nine years off. In 1066 the gate's ten-month text is about to be written: worth a line, not a start.

**Recommendation.**
- Keep the 867 seeding: the count of Shazhou converts and a nüguan is seeded in the foothold.
- Add date-gated loc:
  - the count is a Tangut lord of the Xia, and Xia law and Tangut Buddhism are the host order;
  - the cave holds the sealed books ("we did not hide them in haste");
  - Khotan has fallen.
- No new starter characters. Nothing at Dunhuang in 1066 changes who a daughter is, where she lives, or what she reads.

### 1178: same seat with new flavour at Dunhuang, but give the faith's *playable* 1178 start to a new hub (Lin'an; §3)

**At Dunhuang little changes in kind.**
- Xia is at its height under Renzong (r. 1139–1193). The Tiansheng code (*Tiansheng gaijiu xinding lüling*, 1149–1169, ed. and trans. Kychanov) regulates clergy and women's status. A 2023 Russian study analyses women in it as mothers, wives, daughters, widows, concubines, **nuns** and slaves (Zamalieva and Nesterenko, *Vestnik KSU* 2023/3).
  - That article could not be fetched (the host was unreachable), so nothing about what the code says on Daoist women is **verified**.
- Dunnell's *The Great State of White and High* (1996) gives the eleventh-century empress-dowager regencies (1049–1099) and Tangut Buddhism as state ideology. The regencies are a section heading confirmed from the book's table of contents; their content was not read.
- None of this alters the premises of a daughter's life at Shazhou. And the evidence for any Daoist women at Xia Shazhou is nil in what I could read.

**What has changed by 1178 is the faith's *texts and Chinese context*, and that is large.**
1. **The gate's scripture is now contemporary.**
   - Zhang Boduan's *Wuzhen pian* (1075) gives the ten months (Wang Mu 2011, §2.3; repo note).
   - The three-stage scheme with the Barrier of the Ten Months is fixed in the 11th–12th centuries (Pregadio 2019, p. 66; repo note).
   - In 867 the narrator had to anchor on older texts. In 1178 the faith reads the gate's own manual.
2. **A woman's inner-alchemy text exists, and it is Song, not Ming–Qing.**
   - Cao Wenyi (fl. 1119–1125) was summoned by Huizong and titled. She wrote a *Daode jing* commentary, the only woman's among twenty in Peng Helin's collection (Despeux and Kohn 2003, pp. 133–134; repo note).
   - Her *Lingyuan dadao ge* 靈源大道歌 is a long poem on neidan, called "the first undisputable female Daoist work" (Equinox chapter "Cao Wenyi: The Song of the Ultimate Source of the Great Dao"; Women in Taoism, Wikipedia, which gives her dates as 1039–1115). The **dates conflict**: Despeux and Kohn give fl. 1119–1125. Check this before use.
   - This answers the brief's question. The *nüdan* corpus attributed to Sun Bu'er is late and apocryphal (Valussi 2008, n. 8; repo note). Cao Wenyi's poem is the one real Song woman's alchemy text.
3. **The court once renamed women clergy by edict.** *Song shi* 22, 1119 (宣和元年正月乙卯), read in Chinese:
   - 佛改號大覺金仙…僧為德士…寺為宮，院為觀。改女冠為女道，尼為女德: "the Buddha renamed Great Enlightened Golden Immortal … monks become *deshi* … *nüguan* are renamed *nüdao*, nuns *nüde*".
   - The edict was reversed: 復德士為僧, "the deshi became monks again", ninth month, apparently of 1120.
   - This is the strongest in-period hook for **Rectified Names**: the throne itself renamed the category the faith lives in, and then renamed it back. With the 1124 bearded woman ordained by edict (*Song shi* 62; repo note), Huizong's court becomes the faith's remembered golden age.
4. **A deposed empress lived as a Daoist nun and saved the dynasty.**
   - Empress Meng, Zhezong's empress, was deposed and sent to the Yaohua Palace as a Daoist. Because she had no imperial rank, the Jurchen missed her in 1127. As empress dowager she then legitimised Gaozong.
   - Source: Wikipedia "Empress Meng" and secondary summaries. Read a Song source or Ebrey before use; **unverified** in scholarship. She died in 1135, so she is lore only, claimed in the faith's voice.
5. **Quanzhen.**
   - Wang Chongyang came to Shandong in 1167. Sun Bu'er (1119–1182) joined in 1167–69 and later formally separated from Ma Danyang.
   - **From 1179**, not before, she practised at Lady Feng's grotto in Luoyang. She is listed among the Seven Perfected only from 1241 (Despeux and Kohn 2003, pp. 140–148; repo note).
   - So at 1 Jan 1178 she is still in Jin Shandong, a year before Luoyang. Women's mass entry into Quanzhen (a third of its clergy) is Yuan (pp. 152, 157).
   - In 1178 Quanzhen is a small, suspect northern movement under the Jin, not yet a refuge.
6. **Song neo-Confucian gender norms.**
   - Cheng Yi (1033–1107): 餓死事極小，失節事極大, "starving to death is a very small matter; losing chastity is a very great one" (*Henan Chengshi yishu* 22B; Ebrey 1993, *The Inner Quarters*; page **unverified**).
   - Footbinding: the earliest discussion is Zhang Bangji, soon after 1148; the earliest archaeology is Huang Sheng's tomb, 1243 (Ebrey 1993; summarised secondhand, **pages unverified**).
   - Zhu Xi is teaching in the 1170s. His Zhangzhou proclamation urging *nüdao* to return to lay life (勸女道還俗榜) is c. 1190 and so after the start, and it is **unverified** (I could not retrieve the text).
   - The pressure is real but rising, not yet at its Yuan–Ming height.

**Verdict for 1178.**
- Dunhuang: carry forward with stand-ins, with flavour for the Tangut count, the Tiansheng code and Tangut Buddhism.
- Rewrite the faith's text so that the *Wuzhen pian*, Cao Wenyi, the 1119 renaming and the 1124 ordination are things that have happened.
- The best case for a **new start with new characters** is not at Dunhuang but at **Lin'an**, the Southern Song capital (§2A, §3). It has the only attested Song community of people assigned male who lived and were addressed as women.

---

## 2. Candidate hubs

### A. Lin'an (Hangzhou), 1178: **plausible, verging on strong**

**Attested basis.**
1. **Zhou Mi 周密 (1232–1298), *Guixin zazhi* 癸辛雜識, *houji*, entry 禁男娼 ("Banning male prostitutes"),** read in Chinese from zh.wikisource:
   - 聞東都盛時，無賴男子亦用此以圖衣食。政和中，始立法告捕，男子為娼者杖一百，賞錢五十貫。
     Paraphrase: in Kaifeng's heyday men also lived this way; in the Zhenghe era (1111–1118) a law first allowed denunciation and arrest, with "a hundred strokes" and "fifty strings of cash" to the informer.
   - 吳俗此風尤盛，新門外乃其巢穴。皆傅脂粉，盛裝飾，善針指，呼謂亦如婦人，以之求食。
     Paraphrase: the custom is commonest in Wu, with its "nest" outside the New Gate; they wear powder and finery, are "skilled at needlework", and are "addressed as women".
   - 其為首者號師巫行頭。凡官府有不男之訟，則呼使驗之。
     Paraphrase: their head is titled *shiwu hangtou* ("master-shaman guild head"), whom the courts summon to examine suits over someone "not a man".
   - The entry closes in Zhou Mi's own hostile voice (attribute it): 敗壞風俗，莫甚於此, "nothing ruins customs more than this". He also notes that no one had revived the old law.
   - **The New Gate (新門) is a Lin'an gate.** The same work's fire entry (*xuji* 上, 天雨塵土) runs the fire "east as far as the New Gate".
2. **What this gives, by the test.**
   - **A named, organised community** with a head bearing a ritual-and-guild title (*hang* 行 is the word for a trade guild).
   - **A living made from needlework and dress.** Sex work is the frame of Zhou Mi's heading, but the needlework is part of the livelihood he describes.
   - **A quarter of the capital.**
   - **A sanctioned role before the magistrate**: the courts call its head as the examiner in "not a man" suits (impotence or annulment cases).
   - **A hostile law** with an informer's reward, which is a ready-made pressure mechanic.
   - The pronoun used of the leader in my translation is the source's neutral 其, and nothing in the text claims these people were women. The mod's characters are fictional.
3. **Theatre.** Zhou Mi, *Wulin jiushi* 武林舊事, juan 4, section 乾淳教坊樂部 ("Court music bureau of the Qiandao–Chunxi eras", 1165–1189: our date) lists, under 雜劇色 and the 德壽宮 (Gaozong's retirement palace), the role **裝旦 *zhuangdan*, "the one who plays the woman"**, filled by 孫子貴 (Sun Zigui; the Siku text reads 吳子貴). Read in Chinese.
   - The performer's sex is not stated: **do not** claim Sun Zigui for anything.
   - It does show that "playing the woman" was a named post in the 1178 court troupe.
4. **Women's and Daoist societies in Lin'an.** Wu Zimu, *Mengliang lu* 夢粱錄 juan 19, 社會 (preface 1274; read in Chinese) lists:
   - a Daoist Lingbao association (靈寶會) that recites Zhengyi scriptures monthly;
   - a Gengshen association (庚申會) of palace and official wives who recite the *Yuanjue jing* and is nicknamed the "treasure-contest" for their jewels;
   - a monastery that once kept a monthly day for "good women" (善女信人);
   - dozens of guild and street *she*.
   - So the **Temple Societies** mechanic transfers to Lin'an with Lin'an's own evidence. This text is late Southern Song: use it as a description of the city's associational life, not of 1178 specifically.
5. **Law the faith already uses applies here.** The Song extinct-household law and adopted daughters (McKnight and Liu 1999; repo note) come from the Southern Song interior. *Lin'an is where the Temple Societies tenet's own legal sources actually ran*, which it never did at Dunhuang.
6. **The Huizong legacy is fifty years old and remembered.** The 1119 renaming, the 1124 ordination and Cao Wenyi all fall within living memory of the court that fled south.

**Weaknesses (why not "strong").**
- Zhou Mi writes in the late 13th century, probably after 1279. His Lin'an quarter is undated, and his only date is the Kaifeng law of 1111–1118. A community outside the New Gate in 1178 is an inference across about a century, though a reasonable one: the practice is attested in the Northern Song capital before the court moved, and the capital's population moved with it.
- The source frames them as prostitutes and a moral scandal. The design must not reduce the hub to sex work, and must not use the Zhenghe law as titillation.

### B. Kaifeng (Bianjing), 1066: **thin to plausible**
- Zhou Mi's 東都盛時 places the practice in Northern Song Kaifeng's heyday, and the Zhenghe law (1111–1118) shows it there by the 1110s. 1066 is about 50 years before the first datable evidence.
- Tao Gu's *Qingyi lu* (10th century) is often cited for male prostitution in the capital. I could not retrieve the passage, and nothing shows the men were addressed as women: **unverified**.
- In 1066 Kaifeng also has none of the Huizong material yet.
- Verdict: a stand-in Yutai presence (one Marked courtier at a Kaifeng court) is defensible. A start is not.

### C. Heian-kyō (Kyoto), 1178: **thin as a hub for trans women; strong as a source of texts and institutions**
- ***Torikaebaya monogatari*.** Siblings are raised as the other sex. The son, living as a woman, holds the post of *naishi no kami* in the women's palace. In the end both "return", and the son becomes Minister of the Left.
  - The *Mumyōzōshi* (1200–1202) knows two versions. Willig dates the extant *Ima Torikaebaya* to 1100–70 (Willig 1983, *The Changelings*; via Wikipedia).
  - Pflugfelder, "Strange Fates: Sex, Gender, and Sexuality in *Torikaebaya monogatari*," *Monumenta Nipponica* 47.3 (1992): 347–368 (citation verified).
  - Whether the princess served is a *female* crown prince (onna tōgū): **unverified**; check Willig.
  - Use it as a text a faith could read against the grain: the story *undoes* the son's life as a woman.
- ***Shirabyōshi*.** Women performers in men's court dress: tate-eboshi, suikan, a sword. They rose in the 12th century, with Giō, Hotoke and Shizuka in the *Heike* tradition. The origin story in *Tsurezuregusa* 225 is **unverified** here.
  - This is women in men's dress, the wrong direction for this mod. It shows the court's dress codes and its female-headed performing households, not a place for trans women.
- ***Asobi* and *kugutsu*.** Female entertainers in female-headed households (Goodwin 2007, *Selling Songs and Smiles*; the household and adoption details are **unverified** at page level). Go-Shirakawa learned *imayō* from the kugutsu woman Otomae (*Ryōjin hishō kudenshū*; **unverified** here).
- **Insei court women.** The women's estates of the *nyoin*, for example Hachijō-in's very large holdings: **unverified** numbers. Strong women's property, but no gender-variant role.
- **Chigo.** Monastery boys in feminised dress. They are minors in a context of sexual use. **Exclude them** as a hub or a gate: it would sexualise children and imply a "boy to girl" pipeline.
- **Japan had no eunuchs** (Tsai 1991, p. 122, via the repo note east_tang_ming_goryeo: "with the exception of those in Japan"). The palace-knife polemic, central to Yutai, has no object there.
- Verdict: no hub. At most, a Yutai text event in which a nüguan reads a copy of a Japanese tale brought by a Song merchant would be anachronistic and Orientalising, so **don't**. Japan is better left alone at 1178.

### D. Jin Shandong (Ninghai / Dengzhou) and Luoyang, 1178: **plausible as Yutai expansion flavour, thin as a hub**
- Quanzhen's women, Sun Bu'er's separation from her husband, and Ma Danyang's poem praising "Aunt Guo" for a "man's ambition" (Huang and Geng 2023, p. 8; repo note) are all in place.
- But the movement is tiny in 1178, its women's houses are Yuan, and its rhetoric praises women for becoming *like men*. That is the reverse of the faith's.
- Use it as a Jin-side event chain ("A Quanzhen master calls her manly; the nüguan corrects the word"), as the repo note already proposes. No start.

### E. Western Xia (Xingqing / Shazhou), 1066 and 1178: **thin**
- Tangut Buddhism, empress-dowager regencies 1049–1099 (Dunnell 1996, table of contents), and the Tiansheng code on nuns.
- Nothing found on gender-variant roles. Flavour only (§1).

### F. Liao 1066, Jin 1178, Goryeo, Qara Khitai: **thin**
- **Liao and Jin.** Strong women of the court and of the steppe: Liao empresses, and the Qara Khitai women rulers Xiao Tabuyan and Yelü Pusuwan (to 1177/78; Biran 2005, **unverified** here). They show women's power, not gender-variant institutions. Johnson, *Women of the Conquest Dynasties* (2011), was not read.
- **Goryeo.** Its *naesi* were court officials, **not eunuchs** (Kim 2006; repo note). Its women inherited and married uxorilocally (Deuchler 1992, **unverified** page). Nothing gender-variant found for 1066 or 1178.

---

## 3. Start sketch: "The House outside the New Gate", Lin'an, 1178 (Yutai Dao's second seat)

**Seat and holder.**
- Do not convert c_hangzhou. Its vanilla count is a Zhao clansman of the reigning house, and flipping the Song capital to the faith would be implausible and would unbalance it.
- Instead give the faith an **unlanded seat in the city**:
  - a Sisters' House whose Elder Sister is a courtier of the count of Hangzhou;
  - if the expansion allows, a S&S merchant company (an embroidery and needlework house) with the count as Patron (`docs/silk_and_silver.md`; it depends on whether merchants can be placed in history files).
- Dunhuang stays seeded as the faith's ancestral seat (the Mogao holy site), held by its Tangut count with stand-ins.
- Narrative frame: "The Way came south with the court."

**Fictional starter characters.** All are invented. None is a historical person, and none is a portrait of a real one.

1. **Elder Sister Ling Xuanmiao** 凌玄妙, about 58, a daughter of the embryo, *nüdao*.
   - Her ordination was entered in Huizong's last years, under the 1119 name 女道, which she still uses with pride ("the throne gave us a name once").
   - She keeps a quiet chamber and the House's long-life store, and holds a purchased ordination certificate.
   - Learning-heavy; the House's teacher. She carries the *Wuzhen pian* and a copy of Cao Wenyi's *Song of the Numinous Source*.
2. **Shen Qiao'niang** 沈巧娘, about 40, a daughter, the *hangtou* (guild head) of the New Gate household.
   - Needlework, dress and ritual healing. The prefecture's court summons her to give evidence in "not a man" suits, which gives her a hook on the magistrate's clerks.
   - In the faith's voice she is "the one the court asks to say who is a man, who has never once been asked who is a woman".
   - Intrigue and stewardship. Keep the examination offstage, as a summons and a verdict only.
3. **A-Lan** 阿蘭, 17, Marked, an apprentice embroiderer the House took in from a failed household. She has not yet begun the gestation. She is the player's natural heir and the gate's first test.
4. **Madam Wu** 吳氏, about 45, a cis woman of the faith (a sister, not a daughter).
   - The widow of a minor official, heir of an extinct household under the *hujue* law, and the House's Protectress.
   - Her property and lawsuits are the Temple Societies' shield.
5. **Optional: Yao Jinge** 姚錦哥, about 25, a daughter who plays the *zhuangdan* in a troupe that performs at the Deshou Palace. She is fictional; do not name or imply Sun Zigui.
   - She gives a court-adjacent route. Her hostile line: a dress prodigy (服妖), "inner and outer not distinguished".

**Pressures.**
- **The Zhenghe law.** Denunciation with a 50-string informer's reward and 100 strokes. Make it a scheme-like threat:
  - a neighbour or a rival guild can denounce a House member;
  - the House answers by bribing the clerk, appealing through Madam Wu, or calling in the hangtou's standing with the court.
  - Zhou Mi's note that the law had lapsed in his day lets the threat fade over time.
- **Rising neo-Confucian moralism.** Cheng Yi's chastity line; footbinding spreading among the elite women the House dresses; Zhu Xi's circle, with the c. 1190 anti-*nüdao* proclamation if verified. Event weight rises from 1178 to 1279.
- **The physician.** Xu Shuwei (*jinshi* 1132) on women "without men", read as "single yin without yang" (Cheng 2021, pp. 23–25; repo note). This dates the ghost-fetus event's 1130–1280 loc band exactly to this start.
- **The register.** Ordination certificates are bought and sold by the state. The House must buy a name-panel or a certificate for each daughter it wants protected. That is the existing *Petition for a Name-Panel*, with Lin'an's own price.
- **Buddhist dominance.** Lin'an's grand societies are Buddhist (*Mengliang lu* 19). The existing −5 opinion "A Man Become a Woman" applies, with full force.
- **War.** The Jin border, and Mongol conquest by 1276. Under the Yuan, the existing Magistrate's Inventory ramps from 1264.

**The gate.** Keep *Gestate the Jade Embryo* unchanged; it is the faith's core. Add two Lin'an variants:
- **The guarantor is the hangtou.**
  - In the first bathing (month 3), the censor's threat becomes **a denunciation under the Zhenghe law**.
  - The new option: *Let the hangtou answer for her*. It uses Shen's hook on the court, costs no gold, and adds stress to the hangtou.
- **A Name Before Witnesses**, with the House's needle.
  - The new daughter's first act is to sew her own robe, as the House "makes its living by the needle".
  - The name is entered under the 1119 title *nüdao*, in the faith's voice: "the throne wrote 女道 once; we write it again."

**Existing mechanics that carry over.**
- The ten-month gestation and its events.
- Ghost Fetus, with the date band already planned.
- Temple Societies: dues, the righteous store and the name-panel.
- Take as Daughter, Sisters' Houses and The Sisters Choose.
- A Prodigy in the Prefecture, with its *No reading* branch: "after c. 1050 the historians wrote it down and said nothing" fits the Southern Song.
- Ordain by Special Edict. Huizong's 1124 case is now a precedent Lin'an remembers.
- From the Silk & Silver notes: Lin'an is a natural Textiles/Silk market. A needlework company is the cleanest use of the DLC for this faith.

**Second-best sketch (if Lin'an is rejected): Dunhuang 1178 with a Tangut count of the Way.**
- Seat c_shazhou, held by the vanilla Weimu count (already Zhengyi Daoist).
- Characters:
  - a Han nüguan;
  - a Tangut widow-Protectress;
  - a Uighur Marked girl.
- Pressure: Tiansheng-code registration of clergy (**verify first**).
- Gate unchanged.
- Rating: thin. It is mostly the 867 design moved in time.

---

## 4. Counter-evidence: what closed off or worsened

- **Dunhuang.**
  - The library sealed c. 1006, so the faith's documentary base ends there.
  - Tangut conquest in 1036, and depopulation and pasture under the Yuan and Ming (Rong 2013, pp. 46–49; repo note).
  - No Daoist women attested at Xia Shazhou in anything read.
- **Song women Daoists collapsed.** About 700 nuns against about 19,000 Daoist men, 1021–1077 (Despeux and Kohn 2003, p. 201).
- **The state insists on sex categories for clergy** (972 edict; Cheng 2021, p. 120).
- **Law against the Lin'an community.** The Zhenghe law (1111–1118): 100 strokes and an informer's reward. Zhou Mi's own verdict: "nothing ruins customs more."
- **Neo-Confucian chastity and footbinding** spread from the 12th century. Zhu Xi's school dominates after 1200. The Yuan (1264, 1273, 1313) and Ming (1369) tightenings are already in the repo's era arc.
- **Huizong's Daoist state was short and discredited.** The 1119 renaming was reversed by 1120. Huizong's Daoism was blamed for 1127, so later officials cite it as a cautionary tale. The faith remembers a golden age that its neighbours remember as a ruin.
- **Japan.** No eunuchs, so the palace-knife polemic has nothing to bite on. The one feminised male institution (chigo) is unusable. Women's formal ordination was weak until the Hokkeji revival of the 1240s (Meeks 2010, **unverified** here).
- **Quanzhen praises women as "manly".** That is the rhetoric the faith must answer, not borrow.

---

## 5. Open questions

1. **Zhou Mi's date.** Is the 禁男娼 entry datable within the *houji* (before or after 1279)? Does any Southern Song source (*Ducheng jisheng* 1235, *Xihu laoren fanshenglu*, *Mengliang lu*) mention the New Gate quarter or the *shiwu hangtou*?
   - Check Hinsch, *Passions of the Cut Sleeve* (1990), and Wenqing Kang, *Obsession* (2009), for their readings of this passage and of the *Qingyi lu*.
2. **"師巫行頭".** Is *shiwu* here a real ritual role (spirit-medium healers) or a mocking title? Song law also targeted 師巫 as "licentious cults" (淫祠). That would add a second hostile law.
3. **Cao Wenyi's dates and authorship** (1039–1115 against fl. 1119–1125). Read the Equinox chapter and Despeux and Kohn pp. 133–134 before naming her in narrator text.
4. **The Tiansheng code on Daoists and women.** Get Kychanov's translation or the Zamalieva and Nesterenko article.
5. **Empress Meng's Daoist status.** Read a scholarly source before using it (Ebrey, *Emperor Huizong*, 2014, or the *Song shi* biography).
6. **Merchants in history files.** Can S&S place a merchant company in 1178 history files? That decides whether the Lin'an House is a company or a courtier group.
7. **The 1120 reversal.** Confirm that the 九月乙巳，復德士為僧 line in *Song shi* 22 falls in 宣和二年.
8. **Zhu Xi's 勸女道還俗榜.** Confirm the text, its date (c. 1190) and its meaning. *Nüdao* there may mean lay Buddhist "vegetarian women", not Daoist nuns.
9. **Torikaebaya.** If anyone wants Japan later, read Willig's translation and Pflugfelder 1992 first.
10. **Map access.** Does the mod require All Under Heaven for East Asian seats? Lin'an exists in the vanilla map files read here, but check DLC gating.

## Sources used

Read in Chinese (zh.wikisource):
- Zhou Mi, *Guixin zazhi*, *houji* 禁男娼 and *xuji* 上 天雨塵土.
- Zhou Mi, *Wulin jiushi* 4, 乾淳教坊樂部.
- Wu Zimu, *Mengliang lu* 19, 社會 and juan 20.
- *Song shi* 22, Xuanhe 1.

Via repo notes: Rong 2013; Despeux and Kohn 2003; Cheng 2021; Valussi 2008; Huang and Geng 2023; Pregadio 2019; Wang Mu 2011; Kim 2006; Tsai 1991; *Song shi* 62.

Online, at citation level:
- Pflugfelder 1992 (*MN* 47.3: 347–368).
- Willig 1983.
- Dunnell 1996 (table of contents).
- Goodwin 2007.
- Zamalieva and Nesterenko 2023 (abstract only).
- Wikipedia: Empress Meng, Shirabyōshi, Torikaebaya, Foot binding (leads only).

Vanilla CK3 history files for the holders.
