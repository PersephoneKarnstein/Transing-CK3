# Zhang Yuanlin, Lotus Sutra in the Dunhuang murals (2018), design reading

**Source (checked against the downloaded PDF, 2026-10-18).** Zhang Yuanlin 張元林. "An Echo from the Ancient Past: Depictions of the Lotus Sutra in Dunhuang Murals and Their Message for the Contemporary World." Translated by Ho Chiew Hui. *The Journal of Oriental Studies* (Institute of Oriental Philosophy, Tokyo) 28: 122–149. OA: https://www.totetu.org/assets/media/paper/j028_122.pdf.
- **Verification:**
  - The PDF has the title, author, translator and running heads with page numbers 122–149.
  - It has **no journal masthead or year**. The journal and volume come from the publisher's URL (`j028_122`).
  - The year 2018 is supported by the PDF's creation date (12 Dec 2018) and by the latest citation (Ikeda 2017), but is not printed. Treat it as "2018 (from file metadata)".
- **Read:** in full (28 pp.), and Fig. 14 inspected visually.
- **Character of the piece:** a short public lecture by the Dunhuang Academy's chief librarian. It has no footnoted art history, no inscriptions, and nothing on patrons.

## 1. The argument and the specific findings

- **Overview.** Mogao has 735 caves, 492 of them with murals, made from 366 to the 14th century (p. 125). The Library Cave held about 50,000 documents, 4th–11th c. (p. 130). It held "as many as 6000 manuscripts of the Lotus Sutra and related commentaries", more than for any other sutra. "99 of the Dunhuang caves directly depict themes related to the Lotus Sutra" (p. 132).
- **Development** (pp. 132–133):
  - Northern Dynasties: the "two Buddhas" (ch. 11);
  - Sui: full sutra tableaux;
  - from the Tibetan occupation (middle Tang): multi-chapter tableaux arranged round the Eagle Peak assembly;
  - still produced under the Yuan.

  Kumārajīva's 27 chapters became 28 "during the Northern Qi", when the Devadatta story was split out of ch. 11 (p. 132).
- **Cave 331 (pp. 136–137, Fig. 14).** Exact finding:
  - Zhang writes that the "egalitarian view espoused in the Devadatta chapter of the Lotus Sutra on the possibility of evil people, women and non-humans attaining Buddhahood" is depicted "in a scene from this chapter, in which the dragon king's daughter and bodhisattvas emerge from the Eastern Ocean Dragon Palace, found in the early Tang Lotus Sutra tableau in Mogao Cave 331 (Fig. 14)" (p. 136).
  - Fig. 14 caption: "Chapter on Devadatta (east wall, Mogao Cave 331)" (p. 137).
  - **What is shown:** the *emergence* from the dragon palace. In the reproduced detail, haloed figures ride cloud-trails out of a palace at the left.
  - **What is not claimed:** Zhang does not say the change into a man, the journey south or the buddhahood is shown, and I could not identify any of them in the detail.
  - **Patron:** Zhang names **no patron or sponsor** for Cave 331 anywhere, and makes **no link to Empress Wu**.
- **Later tableaux.** "there are many images depicting the contents of Chapter 12 … such as the dragon girl's emergence from the dragon palace and her offering of a jewel to the Buddha" (p. 136). The two scenes Zhang names as the stock Dunhuang iconography are **the emergence and the offering of the jewel. Neither is the change of sex.**
- **Empress Wu (pp. 125–126).** The only Wu reference concerns the 35-m seated Maitreya in the nine-storey building (Fig. 3). It was "First built during the Tang period" and "seems to be related to Empress Wu Zetian's edict to have a Great Cloud Monastery built in every prefecture" (p. 125). The link is hedged ("seems"), and **Zhang does not give the cave number.** That this is Cave 96 (the "Northern Great Buddha", usually dated 695) is standard identification, but it is not in this article. Correct `china_reading_list.md` finding 1, which cites "Cave 96 … (Zhang p. 126)": the passage is on p. 125, its figure (Fig. 3) on p. 126, and the number is not Zhang's.
- **Other caves useful for the seat** (all from Zhang):
  - Cave 285 (c. 539): two Buddhas; Five Hundred Bandits on the south wall (pp. 133, 136).
  - Cave 23 (high Tang): the Medicinal Herbs peasant in the rain; Never Disparaging on the east wall (pp. 141, 146).
  - Cave 85 (late Tang, 848–907): more than 24 chapters on one ceiling (p. 133).
  - Caves 303 and 420: Guanyin's 33 manifestations, including "as dragon king" (Fig. 20, pp. 143–144).
  - Cave 45: Guanyin's 33 forms (p. 145).
  - Cave 61 (Five Dynasties) and Cave 76 (Song): Never Disparaging (p. 147).
- **The frame.** The lecture reads the murals as messages of "equality" and "harmony with differences", and ends by quoting Daisaku Ikeda (pp. 137–148). This is the publisher's (Sōka Gakkai's Institute of Oriental Philosophy) house framing, not evidence about Tang intent. Do not cite it for what Tang patrons meant.

**Where the Wu–Cave 331 claim came from.** The mod's line traces to Burton-Rose in *Transgender China* (2012), p. 73: Wu was "lavishly funding a mural of this key scene in Dunhuang cave 331" (`east_transgender_china.md`, row 22). Zhang, a Dunhuang Academy specialist on exactly these murals, gives no such patron, and the reading-list search found none. So Burton-Rose's claim is **unsupported by the specialist source**. Treat it as an error unless a primary inscription or a Dunhuang Academy catalogue entry turns up.

## 2. What it changes in the design

| # | Current design | Pressure | Proposed change |
|---|---|---|---|
| 1 | README line 175: "Cave 331 there holds a mural of the Lotus Sutra's dragon girl, who changed her body in an instant. Empress Wu Zetian paid for it." | Cave 331 (early Tang, east wall) shows the dragon girl and bodhisattvas **emerging from the dragon palace**. No patron is named; no Wu link; no change of body depicted (pp. 136–137). | README: "Cave 331 there holds an early Tang mural of the Lotus Sutra's dragon king's daughter rising from the sea palace." Delete the Wu sentence. If Wu is wanted at Mogao, use "the great Maitreya, raised after Empress Wu's Great Cloud edict" (p. 125, hedged; cave number from standard references). |
| 2 | `localization/english/tm_l_english.yml:273` `holy_site_tm_mogao_effects`: "Cave 331, where the dragon girl changed her body in an instant". | The same correction. | "Cave 331, where the dragon king's daughter rises from the sea." Possible faith-voice tooltip: "The painters showed her rising and her pearl; they did not paint the change." |
| 3 | Comments in `common/religion/holy_site_types/tm_holy_site_types.txt:44` and `common/religion/faith_types/tm_faith_types.txt:128` ("where Wu Zetian paid for a mural…"). | Wu claim unsupported. | Fix the comments to match (cosmetic). |
| 4 | `docs/beliefs.md:206` and `east_transgender_china.md` row 22 rely on Burton-Rose's "funded cave 331". | Specialist source silent; claim unsupported. | Add a correction note to row 22 pointing to this file. |
| 5 | Dunhuang seat flavour. | Stock iconography is **emergence and offering**, not the change (p. 136). Never Disparaging, beaten and still bowing, is painted in Tang, Five Dynasties and Song caves (pp. 146–147). | Seat events can use painted scenes that really exist: the girl's pearl (recognition before change), and Never Disparaging (the sisters bear abuse and keep calling others by their right names). Fits Rectified Names. |
| 6 | Era arc 867–1453. | Lotus tableaux continue at Mogao into the Yuan (p. 133); the Tibetan-period and late-Tang formats are current in 867. | No change; confirms Mogao as an active Lotus site across the whole window. |

## 3. In-world lines

- "In Cave 331 she is still rising from the sea, with the pearl in her hands. The painters stopped there, and so do we."
- "The great Maitreya stands where the Empress ordered a Great Cloud temple. The Way remembers who paid for that one."
- "On the Song walls the bodhisattva Never Disparaging is beaten and keeps bowing: *I would never dare disparage you.* The sisters say the same to the censor, and give him his true name."
