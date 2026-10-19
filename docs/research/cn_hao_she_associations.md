# Hao Chunwen, "She Association Manuscripts from Dunhuang" (2021): design reading

**Citation (verified from the PDF):** Hao Chunwen 郝春文, "She Association Manuscripts from Dunhuang and the Study of Medieval She Association," trans. Huang Bo 黃勃, *Hualin International Journal of Buddhist Studies* 4.1 (2021): 59–98. DOI 10.15239/hijbs.04.01.03. The article translates part II, ch. 1 of Hao, 《中古時期社邑研究》 (Shanghai: Shanghai guji chubanshe, 2019), a later edition of the 2006 Taipei monograph. OA.
**Read:** the whole article, pp. 59–91. The bibliography, pp. 92–98, was skimmed.
**What it is:** a survey of the corpus (§1, pp. 60–77) and a review of research from 1938 to 2006 (§2, pp. 78–91). It does **not** transcribe S.527, quote 大者若姊, or name the nun-officer. Those come from Galambos 2020 and the manuscript (`cn_s527_womens_association.md`).

## 1. Argument

- **The corpus.** There are over 480 she 社 documents, including about 60 copies or duplicates (p. 61). Hao sorts them into five types:
  - bylaws (*shetiao* 社條), 27–28 of them (pp. 62–63);
  - circulars (*shesi zhuantie* 社司轉帖), 265, of which "over ninety" are documents actually used (p. 68);
  - records (*sheli* 社曆), 60 (p. 71);
  - liturgies (*shewen* 社文), 107 (p. 72);
  - reports and notes (*shezhuang*, *shedie*), 24 (p. 75).
- **Dating.** About 230 documents can be dated. Ten are before 786, 18 from the Tibetan period (786–848), and "over 150 date to the period of the Cao 曹 family Guiyi jun (914–1002)". The latest dated document is from 982 (pp. 76–77).
- **Bylaws were sealed.**
  - A she's founding "great regulation" (*datiao* 大條), also called the standard or ancestral regulation (*zhengtiao* 正條, *zutiao* 祖條), was rolled, glued and sealed. It was opened only for a dispute "the masses cannot make a decision" on (S.6005, pp. 63–64).
  - Day-to-day rules went into "separate ordinances" (*pian'an* 偏案, *piantiao* 偏條) (pp. 64–65).
  - S.8160, the bylaws of a "Qinqing she" 親情社 (Affection She), survives still sealed. The recorder's and leaders' names are written across the seal (pp. 63–64).
- **She refounded their bylaws** after war, deaths and dispersals, or turnover of members. Examples are P.3544 (855) and S.527 (pp. 65–66).
  - S.527 copies the model bylaw S.6537v "Shangzu shetiao" 上祖社條 in substance (p. 63). Real bylaws trimmed the models and added a member list.
  - Hao dates S.527 to 959 on p. 63 and to "960" on p. 66; 959 is right (Xiande 6.1.3).
- **Funeral aid was the core activity.**
  - Death circulars are not the most numerous, but most of them are documents in use. This shows "that mutual aid in regard to funerals was the most important activity" (p. 70).
  - Spring and autumn banquet circulars are the most numerous but are mostly copies, so the banquets were "probably not as important as mutual aid for funerals" (p. 70).
- **Funeral ledgers and a common store.**
  - "Records concerning offering for the deceased" (*shengu nazeng li* 身故納贈曆) list each member's gift when a member *or a member's relative* died. Ticks show what was received, and some gifts went on to the bereaved family (p. 71).
  - "Records … for convenient goods" (*shesi bianwu li* 社司便物曆) record loans of noodles, oil, millet, wheat and jute from the she to members. Hao calls this "the public accumulation of goods of the private she" (pp. 71–72).
  - Other records list arrears, fines and expenditure (p. 72).
- **Circulars were marked by hand.**
  - Members acknowledged a circular with 知 ("understood") or an ink dot, and the last member returned it (p. 68).
  - On S.5632, a death circular for Zhang Han'er's mother, the she office added hooks and circles. These show who came and gave (pp. 68–69).
- **Leaving was rare and punished.** "Each she devised strict punishments for people who wanted to leave", and only one application to leave survives (p. 75).
- **Officers and names.**
  - Naba's list of leaders: *sheseng* 社僧, *shezhang* 社長, *sheguan* 社官, *shelao* 社老 and *yuhou* 虞候 (p. 80).
  - Members were *sheren* 社人, *shezi* 社子 or *shehu* 社戶 (p. 82).
- **Relation to monasteries (pp. 78–84).** Naba saw three types: Buddhist faith associations, purely mutual-aid she, and mixed ones.
  - Monks who joined a mutual-aid she joined "as a member of the mutual aid group", not as believers (p. 79).
  - Faith-type she were "subordinate to a certain monastery" and did its lamp-burning, sand-printing and cave repair (pp. 80–81).
  - Hao rejects Gernet's view that the monks and nuns in Dunhuang she were its religious masters: it "did not conform to facts" (p. 84).
  - Chikusa showed that membership could be "a heavy burden", which drove poor members out (p. 85).
- **Women's she** are a recognised subfield (pp. 89–90): Ning & Hao 1990, Huang Xia, Yang Sen, Lin Yanzhi, Yu Xin 2002 (on a "walking the bridge" custom in a women's bylaw), and Meng Xianshi 2005.

## 2. Design table

| # | Current design | Pressure | Proposed change |
|---|---|---|---|
| 1 | Temple Societies tenet: "temple and burial societies hold their sisters' goods in common, keep the rites for the kinless, and adopt the heirs." | The real core was **funeral aid paid by fixed dues per death**. The common store was small and was lent out (oil, grain, cloth), not a shared estate. | Loc fix: "...pay each sister's dues at every death in the society, lend from a common store, and adopt the heirs who will keep the rites." Mechanic: a `tm_burial_society` county or House modifier. When a member or a member's close kin dies, members pay a small gold or prestige due and the bereaved gets a stress-relief or piety bonus. |
| 2 | (none) | The founding bylaw was **sealed** and opened only for disputes the assembly could not settle. Separate ordinances ran daily life. | An event when a House splits or a dispute deadlocks: "Break the seal on the great regulation?" Breaking it settles the dispute with the founder's word (and the Protectress's opinion counts), at a cost in strain or prestige. |
| 3 | Sisters' Houses split at strain 6. | She **refounded** their bylaws after war or dispersal (P.3544 in 855, S.527 in 959). | When a House recovers from strain or comes through a war, offer "Renew the bylaws": a New Year event that resets strain and re-swears the members. Fits S.527, written on New Year's day. |
| 4 | Strain from too few hands. | Dues were a burden, so the poor left or were let go (Chikusa; S.5698 in Galambos). | A strain source, "dues in arrears". The Elder Sister can forgive (−gold, +opinion) or release the member, whose deaths and births "no longer concern the society". |
| 5 | Leaving a House is free. | Leaving a she was rare and punished. | Optional: leaving a Yutai House costs a feast (gold) and the stick (S.527: three strokes). Keep it soft, as an opinion and prestige hit, not a wound. |
| 6 | Clergy have a role in Houses. | Monks and nuns joined as ordinary members or officers, **not** as religious masters (Hao vs Gernet). | No change. This confirms that a nüguan in a House is a sister, not its priest. The Elder Sister is not automatically clergy. |
| 7 | Era arc: estates revert to the crown. | 150+ of the dated documents are from the Cao period (914–1002). That is the floruit of Dunhuang she. | Starting-situation flavour. At the 867 start, the she are refounding after Zhang Yichao's war (P.3544, 855). Their documented peak is the Cao century (914–c.1036). By 1066 Shazhou is Tangut, and the library cave was sealed c. 1006, so the record goes silent. Societies could become "remembered" lore after the Tangut conquest. |

## 3. In-world loc lines

- "Unless the sisters cannot agree, the great bylaw stays sealed."
- "At every death in the society, each sister brings oil, flour and grain."
- "Whoever holds back the circular will be fined according to the bylaw." (formula of the circulars)
- "Her name is struck from the bylaw. If anyone in her house is born or dies, it no longer concerns the society."
