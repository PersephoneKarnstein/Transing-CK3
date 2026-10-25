# The Houses of the Present-Day Song (Japan, 1178): consolidated design note

Draft for a `docs/wave?/` design file. Nothing in the repo was edited. Written 2026-10-24.
Consolidates, with later files overriding earlier ones: `survey_1178.md` (Japan entry) → `japan_tsuji.md` → `japan_sources.md` ("JS") → `mitsuhashi_ch1.md` ("M1") → `mitsuhashi_theory.md` ("M6") → `japan_goodwin_kudenshu.md` ("GK"). Writing rules are `docs/faith_design.md` §16 ("rule n").
Source keys: **K** = Kwon 1986 (*Kudenshū* bk 10, tr.); **Kim** = Kim 1994; **G** = Goodwin 2007; **GB** = García Bustos 2020; **Pfl** = Pflugfelder 1992; **TK-es** = Spanish *Torikaebaya*; **QV** = *Queer Voices from Japan* 2007; **M** = Mitsuhashi 2008 (printed pp.); **Tsuji** = Tsuji 2024. RH = *Ryōjin hishō* song number.
Vanilla checks made for this note (1.20 with All Under Heaven): bookmark `bm_1178_*` starts **1178.10.1**; holders from `history/` via `scratchpad/surv2/at1178.py`; rites and faiths from `common/religion/`. The font check (`tools/check_glyphs.py`) passes every code point below U+0250, so ō, ū, ā (Latin Extended-A) are safe in loc. Kanji are not, and stay in docs only.

---

## 1. Premise

The Houses of the Present-Day Song are a current of Japanese Buddhism kept by the river-port singers' houses at Eguchi and Kanzaki on the Yodo mouth (Settsu), at Muro on the Inland Sea (Harima) and by the *kugutsu* singers of Aohaka on the Tōsandō (Mino). The houses are historical: they were women's houses with women heads (*chōja*), a house god, Hyakudayū, and a line of *imayō* song passed mother to daughter, born or adopted, which reached the retired emperor Go-Shirakawa in 1157–69 (K 276–84; G 15–34). Their trade was song, boats, lodging and, for some women on some nights, the bed. The faith is the mod's invention. It is these houses with daughters in them: trans women whom the house teaches the line and receives as women among its women. No source read records a person assigned male living as a woman inside a singers' house (JS §1.3; GK §1.7). The narrator says so in the README and in every holy-site and tenet tooltip that leans on history. At the 1178.10.1 start the houses are at their height and about to lose it: Kiyomori's coup confines their patron in 1179.11, the Genpei war begins in 1180, and after 1186 the trade moves east (Kim 16–17; G 148).

## 2. Attested, read, invented

**Attested (in-period sources, page-checked in the notes):**
- The houses at Eguchi, Kanzaki/Kamusaki, Muro and Aohaka; women heads chosen by the house (Yūjoki, c. 1087–1111, G 15, 19, 33); a *chōja*'s seal, written leave and custody of gifts (*Chōshūki* 1119, G 24–26, 33–34).
- Hyakudayū as the singers' guardian god, prayed to for lovers and fortune (Yūjoki, G 19; Kairaishiki c. 1087, G 28; RH 375, 380).
- The Aohaka line Shisan → Mei → Otomae → Go-Shirakawa; one adoption, "Mei adopted Otomae as her daughter" (K 277); "complete transmission" as the test (K 282, 284).
- Song as Dharma: "Why shouldn't secular literature, too, transform itself into the praises of the Buddha" (K 297); healing and rebirth by song (K 296–97).
- Pilgrimage to Hirota and Sumiyoshi (Yūjoki, G 19; Kim 9); the 1114 kugutsu suit (*Chūyūki*, G 136).
- In the start year: Suketoki's transmission from 1178.3.23 (K 297–98); the Iwashimizu vigil 1178.9.20–26 (K 295); the Rokuhara *dengaku* 1178.11.10 (*Sankaiki*, Tsuji pp. 10–13).
- Men in a miko's guise for one night (Tsuji); eastern male shamans in song (RH 556, Kim 148; M 44); a possibly bearded diviner in the *Nenjū gyōji emaki* cockfight scene, c. 1170, known from an Edo copy (M 39–40; she calls it uncertain).
- *Torikaebaya* (c. 1100–1170): a child raised as a girl lives as Naishi no Kami and is "returned" at the end (Pfl 348–56; TK-es).

**Read (scholars' readings the design leans on):**
- Mitsuhashi ch. 6 (M 304–334): a woman is someone doing woman and recognised by others, in a place, among women (the "law of the majority", p. 321–22); *mitate*, reading one image as another (p. 329); being read does not end being treated as a woman (p. 310). Lineage "kept against prejudice" (p. 352).
- Goodwin: the houses' religion is the ordinary "interpenetration of sacred and secular", not sacred sex (G 90–102); the office cuts both ways (G 34, 122).
- Tsuji: every recorded male guise was a costume by men who stayed men (pp. 11–13, 24, 27).
- Kim: the head "protected group members from undue exploitation" (Kim 9; *sec.*, "believed").

**Invented (say so in the design doc and README):**
- The daughters, the word *uketsugi*, every named character and house.
- The gate's form: seasons of teaching, singing the line back on Hyakudayū's night, the house's answer; the adult-only rule for taking.
- Hyakudayū as a kami kept inside a Buddhist faith as its house god (the joining is period practice; the faith is not).
- The *chōja*'s succession rule, the house's share mechanics, all event outcomes.

## 3. Faith setup

### 3a. Name (all glyph-safe)
1. ***Imayō no Ie***, "the Houses of the Present-Day Song". **Recommended.** Names the song, not the trade or a body; ō is in the font.
2. ***Kuden no Ie***, "the Houses of the Spoken Line" (*kuden*, oral transmission, the *Kudenshū*'s own word). No macrons. Good if the gate is to sit in the name.
3. ***Tsuzumi no Ie***, "the Houses of the Drum", from the principal singer's small drum (Kim 8; RH 380). No macrons; plainest for players.
- Daughters: ***uketsugi***, "those who received the line" (invented). Clergy loc: ***chōja*** for the head; priest title proposal *utame* (歌女, the ritsuryō court's women singers; usage in 1178 *unverified*), fallback "Mother of the Song". Never *futanari*, *otoko miko*, *jisha*, *josō*, *okama*, *new-half* or "courtesan" as a name.

### 3b. Placement
- **Recommended: a new faith `tm_imayo` in `buddhism_religion`, main rite `tm_imayo_rite`**, as the Garland sits in `hinduism_religion`. In 1.20 the Kinai is Tendai (`pundarika`, a rite of `mahayana_faith`); Shingon is `mantrayana` under `vajrayana_faith`; Shintō is a separate `shintoism_religion`. A faith of its own keeps the mod's pattern (own holy sites, own tenets, the growth engine's per-faith counters) while staying in the Buddhist family, so hostility to the Tendai court is the mild Buddhist intra-religion level.
- Hyakudayū is the faith's kami by *honji suijaku* (Kim 89 ff.); set via the faith's god-name loc keys, not a Shintō rite. Sharing `ritual_celebrations` with `shinto` and `mantrayana` signals the joined practice.
- Rejected: a rite inside vanilla `mahayana_faith` (it would inherit Mahāyāna's holy sites and the census would not see it); `shintoism_religion` (the singers' practice was mainly Buddhist, GB 53; G 23).

### 3c. Doctrines (rite overrides; Buddhist baseline from `00_buddhism.txt` noted)
| Group | Pick | Why |
|---|---|---|
| Head | `doctrine_no_head` (baseline) | Houses autonomous, heads chosen locally (G 32–33). No Mother of Mothers. |
| Gender | `doctrine_gender_female_dominated` **[decision 4]** | Women-headed houses (G 32–33); matches Yutai and Badenya. `_equal` is the conservative fit. |
| Clerical gender | `doctrine_clerical_gender_female_only` | Every faith of the mod. |
| Clerical marriage | `doctrine_clerical_marriage_allowed` | Singers married or lived with partners (Kim 8–9; Kiyotsune and Mei, K 281). |
| Clerical function / succession | `alms_and_pacification`, `spiritual_appointment` (baseline) | — |
| Pluralism | `doctrine_pluralism_pluralistic` (baseline) | Joined Buddhist and kami practice. |
| Pilgrimage | `doctrine_pilgrimage_encouraged` (baseline; Tendai has `local_rites`) | Hirota, Sumiyoshi, Hōjūji (G 19; K 281, 296). |
| Marriage / divorce / consanguinity | baseline: `doctrine_polygamy`, `doctrine_divorce_allowed`, `doctrine_consanguinity_cousins` | No source asks for a change. |
| Bastardry | `doctrine_bastardry_none` (baseline) **[decision 5]** | Children by courtiers were acknowledged by fathers (G 132): a fathers' matter. |
| Homosexuality | `_accepted` (baseline) | — |
| Adultery | `_shunned` (baseline) | An "accepted" doctrine would read as a modern claim (GK §5). |
| Deviancy, witchcraft | `_shunned` (baseline) **[decision 6]** | Keeps the trade out of the "deviant" secret; the drum-diviner is a seer, not a witch. |
| Monasticism | `_encouraged` (baseline) | Mei died a nun (K 281). |
| Funeral | cremation (baseline) | — |
Note: Buddhism has no `lustful` sin (virtues generous, honest, calm, compassionate; sins deceitful, impatient, wrathful), so GK's "lustful neutral" needs no mechanic.

### 3d. Tenets (three, the mod's pattern: gate + line + one vanilla)
1. **`tenet_tm_complete_transmission`, "The Complete Transmission"** (gate tenet; carries "Song Is Dharma"). Unlocks the gate decision; song events give piety; a song sung "with sincerity at shrines or temples" may heal or bless (K 296). Text core: K 297's second half only, never "sink deep in sin" in the faith's voice. Parameter `tm_song_is_dharma = yes`.
2. **`tenet_tm_house_keeps_trade`, "The House Keeps Its Trade"** (line tenet; user-approved 2026-10-24). In a mother's voice: the house's living, river, lodging, song and bed alike, is honest work under Hyakudayū; the god is asked for lovers and fortune (G 19, 28; RH 380); the head shares the gifts fairly and guards the women from patrons (G 23, 33; Kim 9); no woman is shamed for working, for not working, or for leaving by marriage (G 20, 35). Mechanics: a *chōja* office holder gets a small yearly "house's share" per working member and an opinion bonus if she shares evenly (event 3); no same-faith opinion loss over the trade; a woman who marries out keeps her house standing and seat claims. Rules: livelihood, **not** sacred sex, no kami-marriage (G 90–102, 111); scenes end at the landing, the boat or the door; no rescue narrative; not every daughter works in the trade; the text never says trans women belong in it (QV 26–27).
3. **`tenet_ritual_celebrations`** (vanilla; shared with `shinto` and `mantrayana`): Hyakudayū's nights (G 28), the flower dedications (K 281, 288).
- **Rejected:** `tenet_carnal_exaltation` (sacred-sex reading; "liberating sex without liberating women", §4 of faith_design.md); `tenet_inner_journey` (Tendai's, not the houses'). **Decision 7** offers "Song Is Dharma" as its own tenet in place of `ritual_celebrations`.

### 3e. Holy sites (one per county, as Ha-Nehpakhot does for Hebron)
| Key | Barony / county | Holder 1178 | What it is | Source |
|---|---|---|---|---|
| `tm_eguchi` (eminent, seat) | `b_watanabe` / `c_settsu` (church holding) | Minamoto no Yorimasa | Eguchi and Kanzaki at the Yodo mouth; site text also names Hirota and Sumiyoshi | Yūjoki (G 15, 19); Miyagi, "In Settsu Province / anything at all / becomes Dharma" (Kim 12) |
| `tm_aohaka` (eminent) | `b_fuwa` / `c_mino` | Minamoto no Mitsunaga | Aohaka on the Tōsandō, home of Mei and Otomae's line | K 277, 281; Kim 14 |
| `tm_muro` | `b_ibo` / `c_harima` (NOT `b_muro`, which is in Kii) | Taira no Munemori | Muro no Tsu, the Inland Sea port of singers | G 30, 115, 129 |
| `tm_hojuji` | `b_kyo` / `c_yamashiro` | Taira no Kiyomori | Hōjūji, where the houses gathered to sing before the retired emperor | K 281, 288–89; Kim 21–22 (1174 *awase*) |
- Excluded: `b_kumano` (Nachi drownings), `b_itsukushima` **[decision 8]** (Shintō, Taira; its *miko* are not singers of the houses; the women there danced in men's dress). `b_fukuhara` (Hirota) folds into `tm_eguchi`, since it shares `c_settsu`.

### 3f. Clergy
Female only; the *chōja* is the house's head, not a faith head. A daughter may hold any clerical seat.

### 3g. How it plays differently from the other faiths
| | Gate | Line | World | Skills |
|---|---|---|---|---|
| Imayō no Ie | Taught over seasons, sung back, answered by her own house; no body change required by the gate itself | The house: *chōja*'s seal, gifts, adoption of grown women | Patrons, gifts and debts, suits before proprietors, court summons that end in 1179 | Diplomacy, stewardship |
| (cf. Yutai) | Ten-month inner gestation | Temple societies | Palace offices | Intrigue, stewardship |
| (cf. Garland) | Mārkaḻi vow | Temple street share | Endowments | Learning, diplomacy |
Shared mechanics stay shared: the daughter trait, re-embodiment under the game rule, *Take as Daughter*, Houses, the call (Japan joins its region list).

### 3h. Writing-rule check (faith_design.md §16, every element)
| Rule | Where it bites here | How the design meets it |
|---|---|---|
| 1 mark knows / world watches | event 10, the scroll's gaze | the capital's eye is the world's; the house's reply is the faith's |
| 2 no golden past | Mitsuhashi's sacred-to-contempt arc (M 350–51); the shaman-entertainer thesis (Kim 5; GB 49–53) | no "we were priestesses once", no "revered then"; "the line kept against scorn" (M 352) instead |
| 3 hostile lines, named speakers | §7 | every line has a dated, named speaker; invented ones go to generated characters |
| 4 no cause | *Torikaebaya*'s *tengu* | the dream is a hostile voice; narrator gives no cause |
| 5 no body reveal | *Yamai no sōshi*, Kuchihige-no-kimi, the Hyakudayū objects | records in notes only; no scene, trait or joke |
| 6 gates equal | event 5 | "taken" and "sung" are the same line; no faith's gate is lesser |
| 7 not only holy; not "accepted for a sacred role" | Rokuhara, Fugen-*chōja*, court summons | roads: boats, poems, court service, the house's offices; Rokuhara is a guise |
| 8 knife not the woman | gate | no knife; the house's recognition makes her a woman of the house |
| 9 reclaimed words | *futanari*, *otoko miko* | not used as names; quoted only as others' words |
| 14 inventions, not ancestors | README | no living community claims these houses (survey) |
| 15 no golden future | tenet text | the house does this year's work; no deliverance |
| 16 neither defiance nor surrender | Rokuhara, *furyū* | no mockery of men in a guise; her dress is her life |
| 17 no despair | *Torikaebaya* lines, old age | the death-wish lines are cut; old age is choice |
| 18 no universal | 双性 | never doctrine; at most one contested voice (decision 2) |
| 19 foremothers are kin, not proof | RH 556, Kokō, *Torikaebaya*, Kyōen | "we need no ancestor to be owed a place" |
| 20 mothering is work | adoption, the *chōja* | any woman of the house may teach and take a daughter |
| 22 no pain test | Tori's eyelashes, the emperor's lost voice | others' zeal, kept out of the gate |
| 23 no oath, no outside probation | gate | the judges are her own house; "Not today" honoured |
| 24 dress by date | hair, painted face | outward change is hair, robes, name; no Edo imagery |
| Brief guardrails | minors, drowning, suicide, *chigo*, *jisha*, *shirabyōshi*, Kumano, trans men | all excluded (§6 G-lines; §10 items 18, 21) |

## 4. The gate and the office

**Gate: "The Complete Transmission"** (decision `tm_transmission_decision`). Rules checked: 6 (equal gate), 8 (no knife), 16, 22 (no pain), 23 (no oath, no outside probation).
1. **She asks a mother of the house.** Any adult of the faith the game codes as male, Marked or declared; a daughter of another faith may also be received (rule 6). The mother is a woman of the faith at her court, or the *chōja*. Invented.
2. **Two doors, both judged by the house** (GK §5):
   - *By song*: seasons of teaching (Kim 15, 19–21; K 276–82). Three stages, one per season, each an event where the world intrudes, not a test of her: a patron who wants her at a banquet before she is ready; a rival house mocking the style (K 278–80, Akomaro's slap); a court summons that takes the mother away.
   - *By taking*: a grown woman (18+) taken as daughter by a mother of the house (K 277, Mei and Otomae; G 34). Adult only; Otomae's age at adoption is a fact in the notes and is never staged.
3. **Hyakudayū's night.** She sings the line back with the drum before the gathered houses (Kairaishiki, G 28; Kim 14). Outcome weighed on the mother's learning and the songs taught, not on her stress or traits.
4. **The house answers.** "Complete" (K 284) gives the daughter trait, a name and (game rule) re-embodiment. "Not complete" (K 282, Otomae on Sasanami) **delays and never resets**; teaching resumes next season. A patron's protégée who wants the songs without the seasons is refused (Sasanami); patronage cannot buy the line.
5. **"Not today."** She may set the line down at any stage, honoured equally (rule 23).
- **Kept out of the gate:** the trade (always); Tori's plucked eyelashes and Go-Shirakawa's lost voice (K 264; Kim 15; others' zeal, rule 22); hair let down or a painted face (Tsuji p. 11: a one-night guise and, for those men, a disgrace; a gate on it would make her womanhood a costume).
- **Framing in loc (decided):** she is a woman because the house does woman with her and reads her as one, among its women (M 305–322); the house's *mitate* is not pretence (M 329). No metaphysics, no "both".

**Office: the *chōja*, head of the house.**
- Chosen by the house (Yūjoki, G 19, 33). Holds the seal, gives written leave to work elsewhere, keeps and shares gifts, speaks for the house in suits (G 25–26, 29, 33–34, 136).
- Succession: by the house's choice among daughters by birth or by taking, a daughter of the knife or song included (rule 20). Invented. Narahara's reading of the 1119 *yuzuribumi* as mother-to-daughter transfer is contested (G 25–26).
- **The office cuts both ways** (G 34, 122): "services, if not their persons" could be the head's property. Event 2 lets a head send a woman unwilling, and the house may unseat her.
- Implementation: reuse the House framework (`tm_found_house_decision`; Elder Sister → *chōja*, chosen by the sisters, not by lot) with a per-faith title loc.

## 5. Starting setup at 1178.10.1

- **Landless, like Ha-Nehpakhot**, with no converted ruler (small faiths grow slowly; no transparent caps).
- **The Eguchi house** at the court of the `c_settsu` holder: a *chōja* (a woman of 45–55, cis), one *uketsugi* (30s), one Marked young adult of 18+ in the middle of the teaching, and one singer who does not work the trade. Yorimasa dies 1180.6.20 in vanilla history; his court passes to his heir, so the seat effects (`tm_seat_on_actions`, the way home) should key to the **county** `c_settsu`, not to his person. His death is never narrated (suicide guardrail).
- **The Aohaka house** at Mitsunaga's court (`c_mino`): a *chōja* and an *uketsugi*, the older line.
- **Optional third** at Munemori's court (`c_harima`, Muro). **[decision 9]**
- Culture: `japanese` (vanilla). Seeds use Japanese women's names from the vanilla list, plus invented house names.
- **Never converted, never claimed** (narrator rule): Taira no Kiyomori (`japanese_taira_kanmu_34`), Go-Shirakawa (`japanese_yamato_51`), Takakura (`japanese_yamato_54`), Taira no Tokuko/Noriko (`japanese_taira_kanmu_68`), Antoku (`japanese_yamato_56`, born 1178.12.22), Prince Mochihito (`japanese_yamato_76`), Minamoto no Yorimasa (`japanese_minamoto_seiwa_59`), Minamoto no Mitsunaga (`japanese_minamoto_seiwa_245`), Taira no Munemori (`japanese_taira_kanmu_64`), Saeki Kagehiro (`japanese_saeki_sanyo_1`), Nakayama Tadachika (`japanese_fujiwara_571`), Minamoto no Michichika (`japanese_minamoto_murakami_78`), Kujō Kanezane (`japanese_fujiwara_514`), Fujiwara no Moronaga (`japanese_fujiwara_470`), Shunzei (`japanese_fujiwara_594`), Saigyō (`japanese_fujiwara_1940`), Jien (`japanese_fujiwara_1301`). Not in vanilla but also never claimed: Otomae, Mei, Tanba no Tsubone, Suketoki, Kokō, Miyagi, Tae, Nabiki, Kinju, Ōi.
- **Check:** All Under Heaven's own Japan events (`tgp_japan_general.*`, Genpei) for collisions with events 8, 9 and 16.
- Other starts **[decision 10]**: the houses are attested from c. 996 (Yukitoki, G 15–16) and the Yūjoki, so 1066 works; 867 does not.

## 6. Events (16)

Format: **T** trigger · **S** sources · **I** invented · **G** guardrails. All trade events end at the landing, the boat or the door, and every work option names the woman's own choice.

1. **Hyakudayū's Night** (yearly)
   - T: a house with 2+ members of the faith, once a year.
   - S: Kairaishiki (G 28); Yūjoki (G 19); RH 380 (G 37–38); RH 560 (Kim 6); K 293, "For were not even the gods once mortals?".
   - I: the night as the house's own; options naming what each woman asks (lovers, fortune, a pupil, nothing).
   - G: no objects described (rule 5); the figurine line is a conditional, never a count (G 19); no kami-marriage.
2. **A Letter of Leave**
   - T: a patron at court with high opinion of the *chōja*.
   - S: *Chōshūki* 1119 (G 25–26, 33–34).
   - I: asking the woman; the house unseating a head who sends a woman unwilling (G 34, 122 supply the risk).
   - G: grant under the seal only if she wants to go, send a willing sister, or refuse; ends at the boat.
3. **Dividing the Gifts**
   - T: after a pilgrim party or banquet pays the house.
   - S: Yūjoki (G 19–20); 1048 equal shares (G 23); Kinju 1119 (G 25); "no set prices" (G 32).
   - I: the meeting; equal shares, by rank, or by work; feeds the tenet's evenness bonus.
   - G: rice, silk, robes, fans, never coin prices; Masafusa's sneer only from a named courtier (§7).
4. **Horses and Cloth**
   - T: a house in a county whose holder has a low-opinion steward or custodian.
   - S: *Chūyūki* 1114 (G 136); patron's-debt variant from the Konjaku type (G 140–41).
   - I: names, the house, the proprietor's ruling.
   - G: a suit, not a raid; violence off-screen and only to goods.
5. **Not Taught as Her Own Daughter**
   - T: a daughter by taking; a rival house of the faith exists.
   - S: K 277 (Akomaro on Mei and Otomae); K 280 (the secret *furukawa*); 1249 suit (G 143) for the late variant.
   - I: the dispute; her answer by singing the secret piece.
   - G: adult only; Otomae's adoption age never staged; rule 6 (no lesser road).
6. **The Preacher at the Landing**
   - T: a pundarika (or later Pure Land) cleric at the house's court or county.
   - S: K 297 (first half); *Hosshinshū* type (G 115); RH 208 (Kim 82); Miyagi (Kim 12).
   - I: the scene; answers "why can't we, too, somehow?", "anything at all becomes Dharma", chant and stay.
   - G: one woman may retire by choice, honoured, not rescued; RH 117 and RH 292 are the preacher's; the Dragon King's daughter quoted, never staged (age eight).
7. **To Hirota and Sumiyoshi** (pilgrimage)
   - T: the faith's pilgrimage activity, or a yearly house event.
   - S: Yūjoki (G 19); *Chōshūki* 1119 (G 25); K 296; Buddhist praises sung to pilgrims, 1048 (G 23).
   - I: outcomes; an unnamed monk refused lodging in the rain (the Saigyō type, never claimed).
   - G: song at the shrine, not sex; no Kumano.
8. **News from Iwashimizu** (start hook)
   - T: 1178.10–11, once, to each house.
   - S: K 295 (vigil 1178.9.20–26, the Lotus a thousand times, all-night *imayō*); K 297–98 (Suketoki from 1178.3.23 at Takijiri, over two years; Moronaga also).
   - I: options: send a singer to the capital; keep the line in the house (Kim 15, 156); teach a court lady behind the blinds (Okimoto via Tsuji p. 10).
   - G: both events precede the 1178.10.1 bookmark, so they arrive as news; the 9.24 *shirabyōshi* named once as world.
9. **Hair Let Down at Rokuhara**
   - T: 1178.12.20 (two days before vanilla Antoku's birth; Tsuji's c. 20 Dec, *conversion unverified*).
   - S: *Sankaiki* 1178.11.10 (Tsuji pp. 10–13).
   - I: the mother's line, "They wore our hair for a night; we were not asked to take ours off."
   - G: narrator calls it a guise; no mockery of the men; never daughters; not "the court accepted women like her" (rule 7).
10. **The Diviner at the Road's Shrine**
    - T: an adult daughter who reads fortunes, at a Kyoto court.
    - S: *Nenjū gyōji emaki* vol. 4, c. 1170, Edo copy (M 39–40, "nothing certain can be said"); *Yamai no sōshi* (museum caption) only as the capital's sneer.
    - I: women who come for counsel; a court eye that sees a shadow on her lip; the house's reply.
    - G: README calls it "an old scroll's picture"; no body reveal (rule 5); hostile line aims at the imagined body, not her clothes (rule 3).
11. **The God Sweeps Down**
    - T: a daughter at a warrior's house; an eastern shaman visits.
    - S: RH 556 (Kim 148; M 44); RH 352 (Kim 143).
    - I: the scorn of capital singers; the mother's "the god swept down on him too".
    - G: never a daughter; the song records no dress (M 44). **Pending user confirmation:** the one place 双性 may appear, as one mother's story ("he carried both, and stood nearer the gods"), answered by another ("we need no god to have stood near us to be owed our place", rule 19). No mechanic, no "tolerant Japan"; or give it to the outsider in §7.
12. **Summoned to Sing**
    - T: before 1179.11, a house near the capital.
    - S: K 281, 288–89 (Hōjūji flower dedications; Enzu's brocade); Kim 21–22 (1174 *awase*).
    - I: the style quarrel, the reward.
    - G: prestige, not holiness (rule 7); after 1179.11 the call stops; Go-Shirakawa speaks only lines his own text gives him.
13. **In This Body There's a Heart**
    - T: 1183–88, a daughter with learning or diplomacy.
    - S: Kokō, SZS 819 (Kim 12–13): "I don't count. / But in this body / there's a heart".
    - I: the compiler's visit, the poem taken.
    - G: renown, not proof (rule 19).
14. **A Song at the Bedside / Good Fortune in Old Age**
    - T: an old mother of the house falls ill, or turns 60.
    - S: K 282–83 (RH 32, Yakushi; "my strength seems to have returned again!"); K 282 ("good fortune in your old age"); K 281 (Mei died a nun); K 283–84 (memorials); Hokkeji 1322 (G 142, late).
    - I: all names; health roll; the house keeps her death-day.
    - G: deaths are of age; choices are teach, take vows and stay, or both; no despair text (rule 17).
15. **The Tale of the Two Who Were Exchanged**
    - T: a daughter in court service (the lady-in-waiting road).
    - S: *Torikaebaya* (Pfl 347–68; TK-es).
    - I: the house's reading of her years as Naishi no Kami; her turn back read as *Set Down the Name*, "a reason, not a verdict" (rule 23).
    - G: the *tengu* dream to a hostile voice; out: childhood, the princess, coercion, Uji and every death-wish line (JS §3).
16. **The Patrons Fall / The Road Turns East**
    - T: 1180–85, then after 1186.
    - S: Kim 16–17; G 29, 147–48 (shift east, Yodo floods, Aohaka "few houses" by 1280); 1202, "asobi were not given clothing" (G 29).
    - I: a house seeking a new patron or moving to the Tōkaidō inns; era modifiers for the 1267 and 1279 property blows (G 82, 144–46).
    - G: out: Dan-no-ura, Antoku's death, Yorimasa's end, Uji, the Heiji story at Aohaka (drownings, suicide).

Not used as events: Saigyō and Tae at Eguchi (legendary date, text 1206); the Shōkū/Fugen-*chōja* tale (1212–15, late-era flavour at most); Kyōen and Eison (1243–51, M 362–64; at most a monks' tale in a monk's voice, rule 19).

## 7. Hostile and outside voices

Every in-game hostile line gets a named speaker of a vanilla faith or court (rule 3). Historical figures speak only words their own texts give them; invented hostile lines go to generated characters (a Tendai chaplain, a provincial custodian).
| Voice | Date | Line or stance | Use |
|---|---|---|---|
| Ōe no Masafusa, *Kairaishiki* / *Yūjoki* | c. 1087–1111 | kugutsu "lewd", likened to "northern barbarians"; singers who "lose all sense of shame" | Quoted by a courtier (event 3); the rite usable, the frame not |
| Minamoto no Michichika, *Takakura-in Itsukushima gokōki* | 1180, Muro | "like foxes from some old grave mound that take the forms of women" (G 129) | Vanilla `japanese_minamoto_murakami_78`; Muro events; also the natural "uncanny" outsider for decision 2 |
| Go-Shirakawa, *Kudenshū* | c. 1169–79 | asobi "sink deep in sin" (K 297), followed by their salvation | First half only, as his line; the second half is the faith's |
| A Tendai preacher (generated) | any | *henjō nanshi*; RH 117 "out of their female bodies", RH 292 "she had to change into a man" | Event 6 |
| Nakayama Tadachika, *Sankaiki* | 1178.11.10 | neutral record of the guise | Event 9 narrator source |
| *Yamai no sōshi* painter (anon.) | late 12th c. | the drum-diviner as "sickness", undressed in sleep | Hostile record only; never a scene (rule 5) |
| Nakahara Hirotoshi, *Honchō mudaishi* | c. 1162–64 | kugutsu woman nicknamed for her moustache (Pfl 359 n. 38) | Notes only; a body record, no loc |
| *Torikaebaya*'s father's dream | c. 1100–1170 | "the man will be a man, and the woman, woman" | Hostile fiction voice (event 15) |
| *Wamyōshō* | c. 935 | asobi among "beggars and thieves" (G 13–14) | Old learning, quoted by a scholar |
| Kamo no Chōmei, *Hosshinshū* | by 1216 | a Muro singer laments a "body immersed in sin" (G 115) | Late; not in vanilla |
| *Jikkinshō* | 1252 | singers' poems "defiled" anthologies (G 133) | Late era |
| Kamakura edict | 1267 | kugutsu and *shirabyōshi* "base women" (G 82, 144) | Late era law |
| Dazaifu ruling (Akyō) | 1279 | land denied "solely" for her trade (G 144–46) | Late era law |
| Kim (scholar) | 1994 | the RH 352 shaman "would be an aberration" | Gloss, not period |
| Tsuji (scholar) | 2024 | every guise a costume; "dual-sex power" "may rather harm understanding" | Narrator level for records |
| Mitsuhashi (insider) | 2008 | recognition by others in place; lineage kept against prejudice | Faith's framing; never quoted in game, never a character |

## 8. Open decisions (each with a recommendation)

1. **Name.** Recommend *Imayō no Ie*; daughters *uketsugi*; clergy *utame* only if its period use checks out, else "Mother of the Song".
2. **双性 (*sōsei*) as a contested belief — pending user confirmation.** Options: (a) one mother's story answered by another in event 11; (b) an outsider's "uncanny" (Michichika-type courtier); (c) none. Recommend (b), with (a) as a single optional branch; no tenet, narrator, modifier or mechanic in any case, and no "tolerant Japan".
3. **Family.** Recommend own faith in `buddhism_religion`. Alternative: a rite under `mahayana_faith`.
4. **Gender doctrine.** Recommend `female_dominated`; `equal` if the user wants the Kinai court's weight felt.
5. **Bastardry.** Recommend baseline `none`; `legitimization` (Tendai's) is the alternative.
6. **Deviancy and witchcraft.** Recommend baseline `shunned` for both, keeping the trade and the diviner out of those secrets.
7. **Third tenet.** Recommend vanilla `ritual_celebrations`; alternative: "Song Is Dharma" as its own tenet and the gate tenet kept minimal.
8. **Itsukushima.** Recommend leaving it to Shintō; events may visit.
9. **Seeds.** Recommend Eguchi (c_settsu, keyed to the county) and Aohaka (c_mino); add Muro only if the first observe run shows the faith dying out.
10. **Starts.** Recommend 1178 and 1066; not 867.
11. **Event 10 (the diviner).** Recommend in, with the "old scroll's picture" framing.
12. **Event 15 (*Torikaebaya*).** Recommend in, as one court-road event with the cuts listed.
13. **Mitsuhashi's continuity claims** (Hirota burial, Yamato Takeru): recommend a mother's voice only, in event 11, adult framing; or leave out entirely.
14. **README wording** for the trade: "the houses' trade was song, boats, lodging and, for some women, sex; the faith keeps it as livelihood, not as worship."

## 9. Bibliography

**Have (read):**
- Kim, Yung-Hee. *Songs to Make the Dust Dance: The Ryōjin hishō of Twelfth-Century Japan*. UC Press, 1994 (parts; see JS).
- Kwon, Yung-Hee Kim. "The Emperor's Songs: Go-Shirakawa and *Ryōjin hishō kudenshū*". *Monumenta Nipponica* 41:3 (1986): 261–98.
- Goodwin, Janet R. *Selling Songs and Smiles*. Hawai'i, 2007 (intro, chs. 1–4, conclusion).
- García Bustos, Teresa. "Imayō, los cantos de las prostitutas". *Fuentes Humanísticas* 60 (2020): 47–60.
- Pflugfelder, Gregory M. "Strange Fates". *Monumenta Nipponica* 47:3 (1992): 347–68.
- *Si pudiera cambiarlos (Torikaebaya monogatari)*, Satori 2018 (in copyright; short quotes).
- McLelland, Suganuma, Welker, eds. *Queer Voices from Japan*. Lexington, 2007 (Mitsuhashi ch. 20; intro).
- 三橋順子『女装と日本人』講談社現代新書, 2008 (pp. 3–77 less chigo pages; pp. 304–391).
- 辻浩和「日本中世の芸能と異性装」『女性学評論』38 (2024): 5–29.
- Kokugakuin University Museum, *The History of Transgenderism in Japan* (2025–26), object list; Kyoto National Museum, *Yamai no sōshi* caption; Scherer, *REVER* 3 (2006).

**Open (located or partly known, not read):**
- Mitsuhashi, 「異性装の力」, in 『装いの力』 (Shōtō Museum, 2022).
- Tsuji, 『中世の〈遊女〉』 (Kyoto UP, 2017); 「中世芸能の異性装」 *Ajia yūgaku* 210 (2017).
- Okimoto Sachiko, 「女声考」 in 『今様の時代』 (2006). Wakita Haruko, 『女性芸能の源流』 (2001); *Women in Medieval Japan* (tr. Tokita, 2006, *unverified*).
- Willig 1983 (*Torikaebaya* tr.); the Stanford UP translation (translator *unverified*).
- 阿部泰郎 2003a/b; 岩崎佳枝『職人歌合』 (1987).

**Still missing (needed before build or before specific loc):**
- *Nenjū gyōji emaki* vol. 4 facsimile (*Nihon emaki taisei* 8), for event 10.
- Yūjoki and Kairaishiki in full (*Nihon shisō taikei* 8); *Chōshūki* 1119 entry; *Sankaiki* 1178.11.10 (Zōho shiryō taisei); Michichika's *Gokōki* (SNKBT 51).
- Pigeot 2003; Toyonaga 1989 and Narahara 1998 (the 1119 *yuzuribumi*); Kawashima 2001; Amino 1984.
- *Imayō no ranshō* (Konishi; Shimma 1977); a pre-1178 source for Miyagi's poem; Imahori 1990 (Hōnen at Muro).
- Suzuki, *Heian makki monogatari ron* p. 121 (*Honchō mudaishi*); Lotus ch. 25 wording check; Western date of Jishō 2.11.10.

## 10. Corrections log (later reads over earlier notes)

1. **Survey → Tsuji:** "men dressed as miko, dates *unverified*" → one in-window case, 1178.11.10 at Rokuhara; the rest 1416–1603 (+238–425 yrs).
2. **Survey → JS/TK-es:** *Torikaebaya*'s female crown prince *unverified* → verified (TK-es I.11, IV.48).
3. **Survey → JS → GK:** gate "The Song Received" → "The Complete Transmission" (K 284).
4. **Survey → GK:** "four generations of teachers (via Wikipedia)" → the *Kudenshū*'s Shisan → Mei → Otomae → Go-Shirakawa (K 277–84).
5. **JS → GK:** Otomae came to court **1157.1.10**, not 1159 (K 276).
6. **JS → GK:** adoption "*unverified*" → attested once (K 277), with Goodwin's control risk (G 34).
7. **JS → GK:** Hyakudayū figurines "kept hundreds and thousands" → a conditional (G 19).
8. **JS → GK:** Kim's "only imayō singers were asobi" → contested (G 14).
9. **JS → GK:** *chōja* powers widened (seal, leave, gifts) and made two-edged (G 34).
10. **JS → GK:** Yūjoki "c. 1087" → c. 1087–1111; Kairaishiki c. 1087.
11. **Survey → GK:** the Fugen-*chōja* tale (*Kojidan* 1212–15) is late; no such tales before the 1180s (G 112). Not 1178 scripture.
12. **JS → GK:** two Tanba no Tsubone, never merged (K 283 n. 131; G 133). Toneguro = Tonekuro.
13. **JS → GK:** doctrine-core quote: Kwon 1986 "secular literature" vs Kim 1994 "secular words"; pick one per loc line.
14. **JS → GK:** Goodwin's "Go-Takakura" (G 129) is Takakura.
15. **JS/survey → user 2026-10-24:** "sex work is never a tenet" → "The House Keeps Its Trade" adopted, on Goodwin's terms.
16. **JS → M1/M6:** 双性 "known only through Tsuji's summary" → read in her own words (M 26, 36–38, 350); she also uses "third gender" (M 344, 357–58, 383) and calls herself 「女」 by doing gender (M 305–312, 372). The mod reports this and adopts neither 双性 nor "third gender".
17. **JS → M1:** "a woman among women" is QV p. 310, not in M pp. 3–77; ch. 6's "law of the majority" is the nearest (M 321–22).
18. **Survey → M1:** the *jisha* as possible minor (Yanagita) vs Mitsuhashi's adult reading (1261 moustache; c. 1500 adult). Still **excluded** (user), and late and eastern anyway.
19. **Survey → JS → M1:** RH 556 "male shaman impersonating a female" is Kim's gloss; the song records no dress (M 44).
20. **Survey → map check:** Muro no Tsu is `b_ibo` (`c_harima`), not `b_muro` (Kii); Eguchi/Kanzaki `b_watanabe`; Aohaka `b_fuwa`.
21. **Survey → user:** Kumano as holy site → excluded (Nachi drownings).
22. **JS → GK:** `b_itsukushima` as holy site → dropped (decision 8).
23. **Tsuji → M1:** Wakita 2001 subtitle confirmed from Mitsuhashi's bibliography.
24. **This note:** `b_fukuhara` (Hirota) folded into `tm_eguchi`: one holy site per county (Ha-Nehpakhot precedent).
25. **This note:** Suketoki (1178.3.23) and the Iwashimizu vigil (1178.9.20–26) precede the 1178.10.1 bookmark; they enter as news (event 8). Rokuhara fires 1178.12.20 against vanilla Antoku's 1178.12.22 birth.
26. **This note:** GK's "`lustful` neutral" mechanic is unnecessary: Buddhism has no `lustful` sin.
27. **This note:** Yorimasa dies 1180.6.20 in vanilla; seat effects key to `c_settsu`, not to him.

## Decisions recorded (user, 2026-10-25)
- **"Dolls".** The mod's name uses *dolls* as modern in-community slang for trans women, which is distinct from the Orientalist "porcelain/china doll" trope (Hinton). The name stays. The Japanese faith takes special care: no doll, porcelain, china or figurine imagery, and no "girl" or "child", anywhere in its text, art direction or names. Kim's asobi figurines (if used at all) are named as the women's own votive objects, never as likenesses of the women.
- **Michichika's foxes.** Kept: one event at Muro in 1180, quoted in full with its ending ("Since no one was interested they went away", Goodwin p. 129), aimed at the port's women as a class, answered materially by the house. Never aimed at a daughter, never in the narrator's voice, and not the "uncanny outsider" of the dual-sex event.
