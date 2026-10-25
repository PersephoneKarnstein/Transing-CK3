# Wendish candidate for 1178 (2.0.0): dossier

Written 2026-10-24 for the Crusader Dolls 2.0.0 question (two new faiths for the 1178 start). Nothing in the repo was edited.

**Built on:** `cmp_alvarezpedrosa_slavic_rituals.md`, `cmp_alvarezpedrosa_sources_slavic.md`, `later_starts/region_north.md` (§§0, 2C–D, 4), `comparanda_reading_list.md` (central Europe, candidates A and C, items 12–27), `faith_design.md` §16 writing rules, `later_starts.md`. Those notes' Wendish findings are cited by row, not redone.

**New for this note:**
- The vanilla files, read by a parser over `history/provinces`, `history/titles`, `history/characters`, `common/landed_titles/00_landed_titles.txt` and `common/religion/*` (current install).
- Primary texts read in open editions on archive.org:
  - Peter of Dusburg, *Chronica terre Prussie* III.4–5, in Toeppen (ed.), *Scriptores rerum Prussicarum* I (Leipzig 1861), pp. 52–54.
  - The Treaty of Christburg (1249), *Preußisches Urkundenbuch* I.1 (Philippi, 1882), no. 218, pp. 160–162.
  - Henry of Livonia, *Heinrici Chronicon Lyvoniae*, ed. Arndt (Hannover 1874). Page numbers below are Arndt's, ±1, because the OCR page heads are loose. Chapter numbers are *unverified* except where noted.
  - Adam of Bremen IV.16–19, Lappenberg's text (Hannover 1876).
- Scholarship: Mažeika 2023 (open access), with a full Latin text and English translation of Dusburg III.5.

---

## 1. Verdict

1. **(b), and only as a new Prussian faith.** At 1178 the Wendish faith has no land and no public cult. Of the three options, only (b) gives a landed and attested pagan society. But (b) is a *different faith*, built on Prussian sources, and it should not be relabelled "Wendish".
2. **Landed, in `baltic_religion` under vanilla `baltic_pagan`.** Seed one county (Galindia `c_allenstein`, or Sambia `c_konigsberg`). Keep Duke Budo and the other Prussian rulers as they are.
3. **Wendish memory as an invented thread.** Rügen exiles after 1168 bring the women's ash rite east. Mark it as design in the README: no source attests a Wendish flight to Prussia.
4. **Keep the Wendish design itself for 867 or 1066 (option c).** There it has Arkona standing. At 1178 it can survive only as landless flavour (option a), and that would repeat Bædling's 1178 "secret current" premise.
5. **The gender evidence is as thin as it gets.** No source in either region shows gender crossing. The nearest items are three:
   - men spinning "to please their gods" (Dusburg 1326);
   - a woman held "holy and a prophetess" who ruled Galindia (Dusburg's morality tale);
   - two-way carnival cross-dressing in fifteenth-century Poznań.

   **The faith is an explicitly invented inversion, and the README must say so.**

---

## 2. What vanilla gives at 1178.10.1 (exact ids)

### 2.1 The Wendish lands: no Slavic pagan county at all

| County | Holder at 1178 (char id) | Culture / faith | Converted to `roman_rite` |
|---|---|---|---|
| `c_rugen` (b_rugen = cn_arkona, prov 2811) | Jaromar (221735, b. 1147, house 101890), vassal of `k_denmark` from 1168.6.15 | polabian / `roman_rite` | province **1150.1.1** (the known error); Jaromar himself **1168.1.1** (correct) |
| `c_wolgast` | Kazimierz (221715, dyn 177, Griffins), under `d_pommerania` | pommeranian / roman_rite | 1128 |
| `c_stettin`, `c_kolobrzeg` (Wolin) | Wartislaw (30521), Griffins | pommeranian / roman_rite | 1128 |
| `c_mecklenburg`, `c_rostock`, `c_werle` | Przybysław (452004), holder of `d_nordmark`, **dies 1178.12.1**; Danish vassal | pommeranian (sic: he was Obodrite) / roman_rite from 1160.8.2 | 1150 |
| `c_lubeck` (nearest county to Starigard/Oldenburg i.H. and Prove's grove; no barony for it) | — | saxon / roman_rite | 1168 |
| `c_brandenburg`, `c_havelberg` etc. (`d_ostmark`) | — | saxon / roman_rite | 1120 |
| `c_cottbus`, `c_gorlitz`, `c_dresden` (`k_sorbia`, Lusatia) | — | polabian / roman_rite | **1178.1.1**, nine months before the bookmark |

- `d_pommerania` is held by Bogislaw (221710) as a vassal of `k_denmark` from 1168.
- Across the whole map, the only living `slavic_pagan` character at 1178 is **"Sareika"** (`skalauti_1`, b. 1149, d. 1202): a *Prussian* of dynasty `prussian_skalauti`, landless, with the Slavic faith. This is probably a vanilla data slip.

### 2.2 The Baltic and Finnic lands still pagan

**`baltic_pagan`: 25 counties.**

| Duchy | Counties | Holder | Culture |
|---|---|---|---|
| `d_prussia` | `c_konigsberg` (Sambia), `c_natangia`, `c_malbork`, `c_wormditt`, `c_bartenstein` (contains `b_insterburg`, the Nadruvia area: Dusburg's Romow, *placement inferred*) | **Budo** (228016, b. 1150, dyn 100371), duke from 1170 | prussian, tribal |
| `d_masuria` | `c_torun` (eminent holy site), `c_osterode`, **`c_allenstein` (commented `#c_galindia`)**, `c_angerburg` | Milzas (228015) holds `c_torun` and `c_malbork`, de jure under `d_prussia` | prussian |
| `d_lithuanians` | `c_kernave`, `c_trakai`, `c_braslau` (holy site), `c_yatvyagi` | Algimantas (82198, b. 1151) | lithuanian |
| `d_samogitia` | `c_scalovia`, `c_memel`, `c_palanga`, `c_siauliai`, `c_raseiniai` | Gediminas (82287, independent) holds `c_scalovia`; Antanas (143135) holds `c_palanga` | prussian / lithuanian |
| `d_courland` | `c_zemigalians` (**pokaini**, eminent), `c_grobin`, `c_selpils` | Sabe (143133) | latgalian |
| `d_latgalians` | `c_kokenois`, `c_jersika`, `c_aluksne` | | latgalian |

- `k_lithuania` has no holder.

**`finnish_pagan`, Estonian culture: `k_esthonia`.**
- `c_osel` (holy site `hiiumaa`; holder Dergun, 228021, d. 1228);
- `c_reval`, `c_wiek`, `c_narva` (Illimar, 228026, holds `d_esthonia`);
- `c_livs`, `c_vidzeme`, `c_dorpat` (`d_livonia`);
- plus `c_vanemane` and `c_talava` in Courland and Latgalia.
- Note: vanilla files the Livonians and Estonians as **Finnic**, not Baltic.

### 2.3 Religion definitions

- **`slavic_pagan`** (religion `slavic_religion`).
  - Eminent holy sites: `kiev` (`c_kiev`) and `rugen` (`c_rugen`). Holy sites: `novgorod`, `barlad`, `plock`.
  - Tenets: sanctity_of_nature, ritual_celebrations, communal_identity.
  - Doctrines: gender male_dominated; homosexuality **crime**; deviancy crime; witchcraft crime; clerical gender either; cremation; no head of faith.
  - **At 1178 every one of its holy sites is Christian.**
- **`baltic_pagan`** (`baltic_religion`).
  - Eminent holy sites: `pokaini` (`c_zemigalians`) and `torun` (`c_torun`). Holy sites: `hiiumaa` (`c_osel`), `braslau`, `rugen`.
  - Tenets: sacred_childbirth, ancestor_worship, sanctity_of_nature.
  - Doctrines: male_dominated; homosexuality **shunned**; concubines; pluralism righteous; deviancy crime; witchcraft crime; clerical gender either; cremation.
  - Vanilla loc: head title "Kriwe" at "Romowe"; priests *vaidilė* / *vaidilutė*. These are sixteenth-century names (row 29).
- **`finnish_pagan`** (`finno_ugric_religion`).
  - Eminent holy sites: `raivola`, `hiiumaa`. Holy sites: `akkel`, `perm`, `torun`.
  - Doctrines: homosexuality shunned; adultery and witchcraft **accepted**; deviancy shunned.

**Consequence.**
- `rugen` is a holy site of *both* `slavic_pagan` and `baltic_pagan`. A Baltic faith can claim Arkona without inventing a link the game lacks.
- Holy sites in a Christian county still count, so a Prussian faith can hold Arkona as a pilgrimage target "after the fall".

---

## 3. Evidence table

Status key: **firm** = text read and the claim is in it; **hostile** = firm text from an enemy voice; ***unverified*** = not seen in a copy. "OA" = open access. Rows 1–15 are Wendish; rows 16–29 are Baltic; rows 30–33 are scholarship.

| # | Claim | Source (OA? link) | Date & place | Status |
|---|---|---|---|---|
| 1 | Arkona's temple destroyed by Valdemar I and Absalon; Rügen made tributary to Denmark | Saxo 14.39; read via Álvarez-Pedrosa ed. 2021, §2.28 (repo note) | 1168, Rügen | firm event; Saxo hostile |
| 2 | The Rani priest outranks the king; tribute comes from all Slavic lands | Helmold II.12 (= 2.108), Álvarez-Pedrosa p. 165 | before 1168 | firm, hostile |
| 3 | Rani "without whose judgement nothing public may be done", feared for "familiarity with the gods"; Rügen's islands "full of pirates" | Adam IV.18, Lappenberg 1876 text ([archive.org](https://archive.org/details/gestahammaburgen00adamuoft)) OA | c. 1075 | hostile. **The piracy label is Adam's framing; do not adopt it.** |
| 4 | Women at Rügen draw lines in the hearth ash "without counting", even = good | Saxo 14.39 (block 2–13), Álvarez-Pedrosa pp. 183/188 | 12th c., Rügen | firm text, hostile narrator |
| 5 | Arkona: one coin a year from every man and woman; a third of spoils to the god; priest marked by long hair and beard | Saxo 14.39, pp. 182–186 | Rügen | firm |
| 6 | Prove's grove: refuge for "those in danger of death"; no blood shed even in war | Helmold I.84 (83), Álvarez-Pedrosa p. 162 | Wagria, mid-12th c. | firm |
| 7 | Bishop Gerold, with Helmold, destroyed Prove's grove | Helmold I.84 | **1156** | standard; edition page *unverified* |
| 8 | Lutici carried goddesses on banners; Riedegost's walls showed "gods and goddesses" | Thietmar VI.23, VII.64 | 1017, Lutician lands | firm |
| 9 | A widow kept Triglav's image hidden in a hollow oak after the priests fled | Ebo II.13, Álvarez-Pedrosa pp. 117–120 | 1120s, Pomerania | firm text; "priestess" is the editor's inference |
| 10 | Otto tells the Szczecin people to "praise women", since they killed surplus daughters | Herbord II.33, p. 138 | 1128, Szczecin | hostile (missionary) |
| 11 | Szczecin returned to paganism after the 1124 mission and was reconverted in 1128 | Herbord/Ebo (standard) | 1126–28 | standard; pages *unverified* |
| 12 | Polish army had "a pythoness as war-leader"; the victor killed her first | *Chron. Montis Sereni* s.a. 1209, Álvarez-Pedrosa p. 211 | 1209, Lebus | firm; Christian army |
| 13 | At carnival "men wear women's clothes, and women men's" (forbidden) | Bniński's Poznań statutes c. XXXIII, Álvarez-Pedrosa pp. 243–44 | 1438–79, Poznań | firm, late, Catholic, two-way |
| 14 | Punitive castration on Poznań's market bridge | Thietmar VIII.2 | c. 1000, Poland | hostile. **Never use as a precedent** |
| 15 | No gender crossing in any Wendish pagan source | Álvarez-Pedrosa 2021 index; 2023 passim | — | firm negative |
| 16 | **"Women and men are accustomed to spin, some linen, some wool, as they believed pleases their gods"** | Dusburg III.5; Toeppen SRP I p. 54; trans. Mažeika 2023 p. 106 ([OA](https://e-journals.ku.lt/journal/AHUK/article/2897)) | written 1326, about pre-conquest Prussia | firm text. The only item where a gendered task is shared for the gods |
| 17 | Galindia: the women go to a woman "held holy and a prophetess by their rite", "by whose command each affair of this land was ruled"; she, "pitying her own sex", sends the men unarmed to their deaths; the women are enslaved | Dusburg III.4; Toeppen pp. 52–53 ([archive.org](https://archive.org/details/bub_gb_YX8OAAAAYAAJ)) OA | 1326; legendary past; Galindia = `c_allenstein` | hostile morality tale (modelled on Pharaoh, Exod. 1). Includes mutilation and infanticide: **do not use those details** |
| 18 | Criwe at Romow "revered for a pope"; perpetual fire; receives a third of victory spoils; says he saw the dead pass by | Dusburg III.5, Mažeika pp. 102–105 | 1326 | firm text. Mažeika: "neither invented exemplum nor literal" (abstract) |
| 19 | Prussians rarely began any task without casting lots | Dusburg III.5 | 1326 | firm |
| 20 | Wives bought; "a man keeps his wife as a servant"; she washes the guests' feet on set days | Dusburg III.5 | 1326 | hostile. Mažeika nn. 15–16: possibly dower or a rite |
| 21 | No beggars; the poor go freely house to house; guests are given all the house has | Dusburg III.5 | 1326 | firm (idealising) |
| 22 | Tulissones or Ligaschones, "most lying play-actors", act "as if priests of the pagans" at funerals and see the dead man "flying through the sky on a horse", hawk in hand | Treaty of Christburg, PUB I.1 no. 218, p. 161 ([archive.org](https://archive.org/details/preussischesurk00conrgoog)) OA | 7 Feb 1249, Pomesania, Warmia, Natangia | firm text, hostile (legate) |
| 23 | An idol, Curche, made once a year after the harvest; promise not to sell daughters in marriage, nor to cast out or kill a son or daughter | Christburg, PUB pp. 161–62 | 1249 | firm, hostile |
| 24 | Thoreida: whether a priest is sacrificed is decided by a horse stepping over a spear; the diviner says the Christian god rides the horse | Henry I.10, Arndt pp. 3–4 | 1190s, Livonia | firm. The horse oracle is shared with the Wends |
| 25 | In the same chapter, women's "stubborn persistence" keeps a sick Livonian from baptism | Henry I.10, Arndt p. 4 | 1190s | hostile; women as keepers of the old way |
| 26 | Semigallians cast lots to their gods before battle | Henry, s.a. 1208, Arndt pp. 53–54 | 1208 | firm; chapter *unverified* (prob. XII) |
| 27 | Tharapita, "the great god of the Oeselians", was born on a wooded hill in Vironia and flew to Ösel; priests cut down the images | Henry XXIV.5, Arndt p. 170 | 1220 | firm |
| 28 | The raiders' pattern: men killed, women and children taken captive; women of Gerwen freed from Oeselian captivity strike their captors "may the God of the Christians strike you"; a sacred grove fouled with blood | Henry passim; Gerwen passage Arndt p. 161 | 1200s | firm. Answers "how the conquerors treated pagan women": as captives and booty |
| 29 | *Vaidilutės* (virgin fire priestesses) and the Kriwe hierarchy come from sixteenth-century writers (Grunau, Łasicki) | comparanda item 25 (Young 2022) | 16th c. | method warning; vanilla loc uses them |
| 30 | Courland: "all houses are full of diviners, augurs and necromancers", "even dressed in monks' habit" | Adam IV.16, Lappenberg text | c. 1075 | hostile. The habit clause is a bracketed later addition, *unverified* as Adam's |
| 31 | *Terra feminarum*: women "living together, scorn men's company" and drive them off "manfully" | Adam IV.19 | c. 1075 | mythic, hostile. Scholars place it in Finland or Kvenland (Wikipedia pointer only). **Omit the cynocephali clause** |
| 32 | Only the names of Mindaugas's and Algirdas's wives are known reliably from the pagan period | Petrauskas 2024 ([OA, VU](https://epublications.vu.lt/object/elaba:195902282/index.html)) | 13th–15th c., Lithuania | firm (insider scholar); shows how thin the women's record is |
| 33 | No medieval Baltic text shows anyone assigned male living as a woman | this search; reading list finding 4 | — | firm negative as far as searched |

**Excluded on purpose:** Henry's report of Lithuanian widows' deaths in 1205 (self-harm); Dusburg's line on Prussian suicide; Ibn Fadlan; Adam's cynocephali; the Galindian mutilation. These must not reach loc.

---

## 4. Design hooks for the recommended faith (Prussian, landed, 1178)

**Working name:** "Those Who Spin for the Gods" (from row 16). An Old Prussian name is better avoided: the vocabulary is thin and modern revivalists use it.

**Premise.**
- Ten years after Arkona burned, Galindia's eastern woods are half-empty: Dusburg's "deserted land" (row 17).
- A household of sisters lives under Duke Budo's peace in Sambia and Galindia.
- **Invented:** the faith says its first daughters were Rugian women who carried the ash rite east after 1168. Their crossing is not attested (rows 1, 4).
- **Invented:** daughters are women who take up the spindle "to please the gods". Dusburg's Prussians shared that work across the sexes (row 16), so the faith treats spinning as no one's birthright.

**Gate: "The Spindle and the Ash"** (two steps, different from the völva's platform). Rows 4, 16, 19, 23.
1. At the harvest feast (Curche's day, row 23), she spins wool before the household's gods.
2. The sisters then draw lines in the hearth ash "without counting" (row 4); even means the gods have seen a daughter.

- Odd means "not this harvest". Per rule 23 this is never a refusal for ever, and "Not today" is honoured equally.
- No pain test, no probation by outsiders (rules 22–23).
- *Invented:* the combination, the meaning of the result, and the women doing it for a daughter.

**Office: "the Holy One of the House"**, after Dusburg's woman "held holy and a prophetess" who ruled Galindia's affairs (row 17).
- *Invented:* that she is a daughter, and that the office is held by sisters.
- Dusburg's story is a hostile exemplum in which she leads her people to ruin. In the faith's voice: "They wrote that she ruled Galindia and then emptied it. They never wrote what she pitied." Note that "pitying her own sex" is a quote.
- Keep the vanilla Kriwe as the *religion's* head; the faith's head is the Holy One.

**Doctrines** (on top of the `baltic_religion` baseline).
- Clerical gender: *either*. Vanilla already allows it; a female-dominated clergy would go further.
- Hospitality and no beggars: an opinion bonus and a "the poor eat where they like" House modifier (row 21).
- Refuge: brought from Prove's grove by the Rugian exiles (row 6). *Invented transfer.* No one in fear of death is turned away.
- Children: "we cast out no daughter" (row 23 inverted). The faith's voice must not claim that it was first; Christburg is the hostile record.
- Funeral speakers: the faith keeps a "tulisson" who sees the dead ride (row 22). This is ritual flavour, not a seer gate, to avoid Bædling overlap.

**Holy sites** (vanilla keys first).
- `torun` (eminent, `c_torun`).
- `rugen` (`c_rugen`, Arkona remembered, Christian-held).
- `c_allenstein`, Galindia, the land of the prophetess (new site; key *unverified*).
- `c_bartenstein`, with `b_insterburg` ≈ Nadruvia and Romow (*placement inferred*).
- `c_konigsberg`, Sambia: Adam's *homines humanissimi* who aid the shipwrecked (row 3; Adam IV.18).
- Optional: `pokaini` (`c_zemigalians`).

**Event ideas** (3–6).
1. **"What Came Over the Sea from Rana"** (1178–80). A Rugian widow arrives with ash on her hands and a coin "for the god who no longer has a house". Options: take her into the House; send her to the Danish-held island.
   - Rows 1, 4, 5. *Invented migration.*
   - Faith loc: "Even the women count the lines in the ash." A grudging Rugian priest's voice, from Saxo.
2. **"Curche's Day"** (yearly, after harvest). The household's sheaf-idol; the spindle and ash gate fires here. Rows 16, 23.
3. **"He Saw Her Ride"**. At a sister's funeral the tulisson sees her pass through the sky on a horse, in her own dress and girdle.
   - Rows 18, 22. Dress per rule 24: girdle and hair, no skirts.
   - Hostile counter-voice, the papal legate of 1249 (era event after 1249): "Most lying play-actors."
4. **"The Lots Before the Raid"**. Before a Prussian or Curonian raid the lots are cast. If a sister casts them, the old men grumble, and the duke chooses whose lots stand.
   - Rows 19, 24, 26. Neutral toward daughters.
5. **"Women and Children Taken"** (era of the Livonian crusade, from 1198/1200, and the Teutonic Order in Prussia from 1230). Christian raiders kill the men and take the women. *Rescue the Daughters* gains a Baltic variant: ransom the captives.
   - Row 28, plus rule 3 hostile tagging.
6. **"A Merchant from Visby"**. A Gotland trader puts in at Sambia. This links Bædling's 1178 "Heathen Sparks" current (`region_north.md` §3B) as an alliance, not a merger (rule 6).

**In-period hostile voices** (rule 3: a named speaker of a vanilla faith).
- **Helmold of Bosau**, priest of Bosau, writing to 1172. He is alive at the start and is the eyewitness to the grove's fall (row 7). A design line in his voice (not a quote): "We burned the grove at Prove's place, and still they turn to their old gods at home." Whether Helmold says anything about household survivals is *unverified*; check Tschan before use.
- **Bishop Fulco of the Estonians** and the 1171/72 bull of Alexander III, which calls for war on Estonians and Finns. Wording *unverified* (Christiansen; Fonnesberg-Schmidt).
- Later eras: Henry of Livonia (rows 25, 28); the 1249 legate (row 22); Dusburg (rows 17, 20).

**What is invented, in one list:**
- the Wendish exiles;
- the spindle as a gate;
- the ash rite outside Rügen;
- a daughter as Holy One;
- refuge transferred to Prussia;
- every reading of the result.

**What is attested:**
- spinning for the gods by both sexes (Dusburg);
- women's ash lots (Saxo);
- a woman held holy and a prophetess, in a hostile tale (Dusburg);
- funeral seers (Christburg);
- the harvest idol (Christburg);
- lots before war (Dusburg; Henry).

---

## 5. Risks and handling

1. **No crossing evidence (rows 15, 33).** Put a README line: "No medieval source records a trans woman, or any gender-crossing rite, among the Wends or the Prussians. This faith is our invention, built on attested rites." The narrator never says spinning men were "really" women.
2. **The sources are the conquerors'.** Dusburg wrote for the Teutonic Order, Henry for the Riga church, Saxo for Absalon, Helmold for Holstein's bishop. Tag every borrowed custom as theirs: "the Order's priest wrote…". Mažeika (2023) is the guide to how far Dusburg can be trusted.
3. **Sixteenth-century inventions in vanilla loc (row 29).** Kriwe, Romowe and vaidilutės are Grunau and Łasicki era names. Do not build the faith on *vaidilutės* as "virgin priestesses"; they are also a "third gender"-adjacent romance in popular writing.
4. **Living communities.** Romuva (Lithuania), Dievturība (Latvia), Maausk/Taara (Estonia), Rodnovery (Slavic) and the Sorbs are not this faith. Avoid their modern terms and symbols. Do not use Tharapita or Taara for the faith; Estonia is Finnic and outside it. Seed nothing in Estonian or Lithuanian culture.
5. **Romance of a "vanished people".** The Prussians did not vanish; they were conquered and assimilated. No golden past (rule 2), and no "last free people" framing.
6. **Grim material next to the useful bits.** The Galindia tale holds mutilation and infanticide, Henry holds the 1205 self-killings, and Dusburg holds a suicide line. Quote only the prophetess clause. Rules 17 and 5 apply.
7. **The piracy and "cruelty" framing.** Adam's "pirates and bloodiest robbers" (row 3) and his "cruelest people" for Courland are hostile voices only. Raiding events treat both sides' raids alike.
8. **Bædling overlap.** Both faiths are pagan, Baltic-rim and seer-flavoured. Keep the gate chance-based and domestic (spindle and ash, done by the sisters), not "the seer sees". No völva and no Ösel seat; leave Ösel to Bædling's hidden current.
9. **Growth.** Lithuania becomes a pagan empire in history, and a converted Lithuanian ruler could snowball (`faith_design.md` §14, §17). Seed Prussia only, one county, slow conversion; no Lithuanian seed.
10. **Name collision.** "Prussian" reads as Hohenzollern. Loc should say "Old Prussian" once, then the tribal names (Sambians, Galindians).
11. **Vanilla slips to fix or work around.** Rügen Catholic from 1150 (fixable in history or by event); Sareika's Slavic faith; Przybysław's Pomeranian culture; Lusatia flipping on 1178.1.1.
12. **Option (a) if the user prefers Wendish anyway.**
    - Landless and secret, in `slavic_pagan`: a few seeded sisters in the Danish-held Rügen court under Jaromar, with the ash rite as the gate.
    - Thematically apt (women's rites survived "away from power", Álvarez-Pedrosa 2023 p. 63), but it has no land, no growth base, and the same shape as Bædling at 1178.
    - It also needs a landless-start DLC (`later_starts.md` status note).

---

## 6. Books and articles to find (not open access)

Ranked for the recommended (b). Items 4–5 rank first if the user picks (a) or (c).

1. **MUST FIND. Francis Young, *Pre-Christian Baltic Religion and Belief*** (Leeds: Arc Humanities Press, 2025), DOI 10.1515/9781802703221.
   - Read the chapters on Prussia, on women and religious specialists, and on the Kriwe debate. Chapter titles *unverified*.
   - Answers: is there *any* evidence for women's or gendered religious roles among Prussians before 1230, beyond Dusburg? Is "spinning for the gods" discussed?
   - Companion: Young, *Pagans in the Early Modern Baltic* (Arc 2022), ISBN 978-1-64189-437-1, DOI 10.1515/9781802700213. Use it to sort the sixteenth-century inventions (row 29).
2. **MUST FIND. Peter von Dusburg in a modern annotated edition.**
   - First choice: the Pisa doctoral thesis *La Cronaca della terra di Prussia di Pietro di Dusburg* (2012; parallel Latin and Italian, notes), which **is OA** at [etd.adm.unipi.it](https://etd.adm.unipi.it/t/etd-01142013-095423). Get it first. The author is probably Piergiorgio Bugiani (*unverified*).
   - Otherwise one of these:
     - Scholz and Wojtecki (eds.), *Chronik des Preussenlandes* (FSGA 25, Darmstadt 1984; ISBN *unverified*);
     - Wenta and Wyszomirski (Polish, 2004/2007);
     - Batūra (Lithuanian, Vilnius 1985).
   - Read III.4–6 and the commentary. Answers: the Galindian prophetess (*phitonissa*? *prophetissa*), the source of "spinning for the gods", and whether a Prussian source lies behind III.5.
3. **MUST FIND. Henry of Livonia, *The Chronicle of Henry of Livonia*, trans. James A. Brundage** (Madison 1961; repr. New York: Columbia UP, 2003), ISBN 0-231-12889-4 (*unverified*).
   - Answers: chapter numbers and English for rows 24–28, and every passage on pagan women, lots and sacred groves.
4. Stanisław Rosik, *The Slavic Religion in the Light of 11th- and 12th-Century German Chronicles* (Leiden: Brill, 2020), DOI 10.1163/9789004331488.
   - Read the Helmold chapters. Answers: how far Helmold's post-1150 survivals (row 7) are reliable, and what Wendish cult outlasted 1168. This is the core book for options (a) and (c).
5. Leszek Paweł Słupecki, *Slavonic Pagan Sanctuaries* (Warsaw: IAE PAN, 1994), ISBN 83-85463-27-5.
   - Read the chapters on Arkona, Garz, Szczecin and Rethra. Answers: women's presence at West Slavic sanctuaries, and what archaeology says about survival after 1168 (holy-site design).
6. Aleksander Pluskowski, *The Archaeology of the Prussian Crusade: Holy War and Colonisation* (London: Routledge, 2013); ISBN *unverified*.
   - Read the chapters on pre-conquest Prussian society, burial and sacred landscapes. Answers: what Sambia and Galindia looked like c. 1178. Settlement or desertion in Galindia tests Dusburg's "deserted land".
7. Pluskowski (ed.), *Environment, Colonization, and the Baltic Crusader States: Terra Sacra I* and *Ecologies of Crusading…: Terra Sacra II* (Turnhout: Brepols, 2019); not OA ([Reading record](https://centaur.reading.ac.uk/73090/)).
   - Read the Sambia and Pomesania case studies. Answers: sacred groves and their destruction, and the event flavour for row 28.
8. Eric Christiansen, *The Northern Crusades* (2nd ed., London: Penguin, 1997), ISBN 0-14-026653-4.
   - Answers: the 1171/72 bull, Fulco, Arkona 1168 and Danish Estonia, for the hostile-voice dates.
9. Saxo Grammaticus, *Gesta Danorum*, ed. Friis-Jensen, trans. Fisher (Oxford: OMT, 2015), vol. II, Book XIV, ISBN 978-0-19-820523-4.
   - Answers: the exact subsections for the ash rite and the white horse, flagged *unverified* in the repo notes.
10. Jerry C. Smith and William L. Urban (trans.), *The Livonian Rhymed Chronicle* (Bloomington 1977; 2nd ed. Chicago 2001; ISBN *unverified*).
    - Answers: Curonian, Semigallian and Lithuanian women in war and cult. Not searched here.
11. Vykintas Vaitkevičius, *Studies into the Balts' Sacred Places* (BAR IS 1228, Oxford, 2004; ISBN *unverified*).
    - Answers: sacred hills and groves as holy-site candidates. Vaitkevičius is a Lithuanian insider archaeologist.
12. Anna Kłosowska, "Wojciech of Poznań and the Trans Archive, Poland, 1550–1561", in LaFleur, Raskolnikov and Kłosowska (eds.), *Trans Historical* (Ithaca: Cornell UP, 2021), ISBN 978-1-5017-5952-9.
    - Method only. It is the one published trans-historical study on the region found, by a Polish-born scholar, but it falls outside 1453. Check the case's direction (officials ruled the person female) before any use; it may be out of scope.
13. Endre Bojtár, *Foreword to the Past: A Cultural History of the Baltic People* (Budapest: CEU Press, 1999; ISBN *unverified*).
    - Read the religion chapters. Answers: an overview, and a check on Mažeika's and Young's readings.

**OA items to pull next** (not read here):
- Szczepański, "Traktat dzierzgoński (1249 r.) a elementy religijności Prusów", *Tabularium Historiae* 2 (2017).
- Wadyl, "The sacred sphere of Prussian life in the early Middle Ages".
- Błaszczyk (2011), gender in Polish row cemeteries, *Folia Praehistorica Posnaniensia* (AMU repository).

**Archaeology caution:** the Opole double female burial (JASR 2026, DOI 10.1016/j.jasrep.2026.105792) is Christian and not pagan, and its authors warn against modern categories. Do not cite graves as evidence of gender crossing.
