# Starts at 1066 and 1178: Scandinavia, Iceland, Norse/Old English Britain, the Baltic, Rus', western steppe

Region slug: `north`. Written 2026-10-20 for the Silk & Silver start-date question. Nothing in the repo was edited.

**What was read.**
- Repo: `docs/faiths/baedling.md`, `docs/silk_and_silver.md` and `docs/research/norse_gragas_laws.md`.
- Repo research notes: `norse_mitchell_witchcraft_magic.md`, `norse_meulengracht_sorensen_unmanly_man.md`, `norse_saxo_gesta_danorum.md`, `norse_gade_homosexuality_law.md`, `cmp_levin_orthodox_slavs.md` and `cmp_alvarezpedrosa_sources_slavic.md`.
- `comparanda_reading_list.md` §"Northern central and eastern Europe". Its candidates A–E already assess Arkona, the Baltic, the Rus' mummers and the Sámi, so this note does not redo them. It dates them instead.
- The mod's own seeding code: `common/on_action/tm_on_actions.txt` ll. 112–135, where `tm_seed_foothold_effect` converts the holder of `c_gutland` at every start.

**Newly read for this note.**
- **Christine Peel, *An Edition of Guta Saga with Introduction, Translation, Commentary and Glossary*.** MPhil thesis, University College London, 1998 (UCL Discovery eprint 10103042; the PDF is in the scratchpad at `north/peel_thesis.pdf`, not in the repo). Page numbers are the thesis's own. This is the forerunner of her Viking Society edition of 1999, so check the pages against that edition before citing it in loc.
- **The Primary Chronicle (*PVL*)** in the IRLI online edition, which a previous search left in the scratchpad (`pvl.html`). Read for the entries for 1068 and 1071.
- **The vanilla CK3 history files** in the local game install: `history/provinces/k_sweden.txt`, `k_norway.txt`, `k_denmark.txt`, `k_esthonia.txt`, `k_pomerania.txt`, `k_lithuania.txt`, `k_finland.txt` and `k_cuman.txt`; `history/titles/k_sweden.txt`; and `history/characters/swedish.txt`. These are the current game files, before Silk & Silver, so recheck them on release.

---

## 0. What the game already puts on the board (vanilla history, before Silk & Silver)

This matters more than any chronicle, because the mod's start script converts whoever vanilla seats in Gotland.

| | 867 | **1066.9.15** | **1178.10.1** |
|---|---|---|---|
| **Gotland (`c_gutland`)** | Norse pagan, tribal | **Catholic (`roman_rite`), Swedish culture, a *republic*.** Holder: **"Botstain af Stenkyrka"**, a Catholic educated in learning, b. 1047 (char 100536). He is followed by a rotation of Gutnish farm-houses: Guldsmed, Hejnum, Straben, Gildehusen. | Catholic republic under `d_gotland` (from 1161). Holder 167372 (from 1173). |
| **Uppland (`c_upland`, Sigtuna, with the special building `temple_of_uppsala_01`)** | Norse pagan | **Still Norse pagan until 1090.** Held by **Erik "Hedningen", the Heathen** (char 100546, `norse_pagan`, zealous). He holds `d_svealand` and a pressed claim on `k_sweden`, and dies 1067.12.20 in "the war of the two Eriks" against the Catholic Erik Stenkilsson. | Catholic (from 1090) |
| Other pagan Swedish counties at 1066 | | Gästrikland, Åland, Västmanland, Dalarna, Hälsingland, Medelpad, Ångermanland and Värend (Catholic between 1080 and 1123) | none |
| Iceland | pagan | Catholic (from 1000) | Catholic, culture becomes `norwegian` |
| Rügen (`c_rugen`, Arkona) | Slavic pagan | **Slavic pagan, castle** | Catholic from **1150**. That is an error: Arkona fell in **1168**. |
| Saaremaa / Ösel (`c_*` Arensburg and Soneburg, `k_esthonia`) | Finnish pagan | Finnish pagan | **Finnish pagan, until 1228** |
| Lithuania, Prussia, Curonia | Baltic pagan | Baltic pagan | Baltic pagan |
| Finland | Finnish pagan | Finnish pagan | South-west Catholic from 1158; the rest pagan until 1250 or 1292 |
| Cumania (`k_cuman`) | Tengri pagan | Tengri pagan | Tengri pagan |

**Consequences.**
- **At 1066 the mod's own script misfires.** `tm_seed_foothold_effect` would make a Bædling out of a Catholic patrician whose house name, Stenkyrka, is the farm where *Guta saga* puts the first church of northern Gotland (§1 below).
- **At 1178 the same thing happens to a Catholic Visby-era republic.**
- **The real pagan North at 1066 is Svealand,** and vanilla already gives it a named pagan pretender sitting on the Uppsala temple.
- **Silk & Silver note.** Vanilla has Gotland as a *republic* at both 1066 and 1178. The "Gutnish commune" idea in `silk_and_silver.md` is therefore what the game already does at those dates. What remains open is whether Silk & Silver's republic rework turns Gotland into a Communal or Maritime republic with an Assembly. Recheck on release.

---

## 1. Verdicts for Bædling (seat: Gotland)

### 1066: **new start with new characters, and the seat moves from Gotland to Uppland/Svealand** (Gotland is kept as a holy site or House)

**Why the premises change (the user's test).**

1. **Who holds the seat, and the gender order there.**
   - *Gotland had converted.* *Guta saga* tells the conversion as a merchants' story. Gotlanders "sailed on trading voyages to all countries, both Christian and heathen", saw Christian customs and brought priests home (Peel 1998, p. 78).
   - Botair of Akebäck's first church was burned. His second, at Vi, was spared only because his father-in-law Likkair Snielli intervened. Likkair was then baptised "with his wife, his children, and all his household" and built Stenkyrka, "the first church on the island up in the northernmost third". Then the Gotlanders "received Christianity generally, of their own free will, without duress" (pp. 78–79).
   - Peel cites runic evidence that "Christianity was well established in Gotland by 1050" (Söderberg 1922, in Peel 1998, p. 109).
   - So in 1066 a pagan count of Gotland contradicts the very text the island remembers itself by, and vanilla agrees (Catholic republic, house of Stenkyrka).
2. **The pagan institution is still alive, one sea-crossing away, in Uppsala.**
   - Adam of Bremen, writing c. 1075, describes the Uppsala temple and its nine-yearly sacrifice in the present tense. He says the songs sung at it are "manifold and unseemly" (Adam IV.26–27; Tschan 1959, pp. 207–208).
   - Peel notes that the first Swedish see went to Skara, not Uppsala, probably because of "the strong pagan influence which still pervaded Uppsala". Sigtuna got a bishop only c. 1050, and the archbishopric came later still (Peel 1998, p. 108).
   - This is the holy site the faith already ranks *eminent*. Saxo's Uppsala, with its "effeminate gestures ... the unmanly clatter of the bells" (Book 6, p. 135, Elton ed., in the repo note), is the faith's own reason for choosing it.
   - At 1066 that cult has a living political sponsor: Erik the Heathen, in vanilla.
3. **The political moment is a pagan war.**
   - Stenkil died in 1066. Adam says two Eriks then fought for the kingship, that "all the Swedish magnates are said to have fallen", and that "Christianity was disturbed" (Adam III.53; Tschan's page *unverified*).
   - Two decades later the *Hervarar saga* tradition has Blót-Sveinn depose the Christian King Ingi and sacrifice at Uppsala (c. 1084–87; *unverified* against an edition).
   - This is a short window, about 1060 to 1090, in which an open seiðr-keeping court is historically defensible in Sweden, and the window closes during play.
4. **Law and the neighbours.** The Icelandic dress clause and *ragr* clauses already apply (*Grágás* K §155, §254; Add. §423). Gotland and Denmark are Christian neighbours. Norway's capital sorcery law is still two centuries off (Mitchell 2011, pp. 125, 156–57). The pressure on the seat is therefore a Christian king's war, not a court. That is a different game from 867, where the faith's world is pagan on every side.
5. **The English half closes.**
   - The Old English *Canons of Theodore*, where *bædling* lives, were translated at some point before about 1025 (Fulk and Jurasinski 2012, p. xl, in the faith page).
   - After Hastings the English church goes Latin and Norman. York's link to the faith, through Eiríkr Blóðøx, is a memory from the 950s.
   - This is a flavour change, not a reason for a new start. *To verify before use:* Anselm's Council of London (1102), with its canon on sodomy and his preaching against men's long hair, as the English reaction rung after 1066. This comes from memory and no page has been seen.

**What a 1066 start should be.** See the sketch in §3A. Gotland stays in the faith's world as a holy site or a House: the merchant island where the Lärbro stones stand (Price 2019, p. 175). It should not be its seat.

### 1178: **drop the landed seat; at most, a hidden landless current. A new start only if built around a different premise (§3B)**

**Why the premises collapse.**

1. **There is no pagan public cult left in Scandinavia.**
   - The archbishopric of Uppsala was founded in 1164 (Peel 1998, p. 4; Peel's commentary on p. 108 prints "1154", an error in the thesis).
   - Lund has had an archbishop since 1103/04, and in **1178 Absalon**, Saxo's patron, becomes its archbishop (standard date; *unverified* against a scholarly page).
   - Nidaros has been an archbishopric since 1152/53, and its archbishop Eysteinn crowned Magnús Erlingsson in 1163/64.
   - Gotland is in the see of Linköping: Bishop Gisle took office in 1139, and Peel uses that date as a terminus post quem for the account of the bishop's visitations (Peel 1998, pp. 4, 52).
   - Every one of the four holy sites (Uppsala, Trondheim, York, Kyiv) is a Christian cathedral town.
2. **The law has turned on the faith's own body and loves.**
   - **1164**, Norway: Magnús's Gulaþing clause makes two men convicted of sex "permanent outlaws". It is a crown-and-archbishop tool for confiscation (Gade 1986, pp. 124–25, 130–31).
   - **1178**, the year of the bookmark: Þorlákr Þórhallsson is consecrated bishop of Skálholt by Archbishop Eysteinn. His penances (1178–93) ran "nine or ten years" with flogging, and **women "who satisfy each other" got the same penance as men** (Meulengracht Sørensen 1983, p. 26). The faith page's sworn sisters and lesbian households are named by the penitential from this year on.
   - The Christian sections of *Grágás* make it lesser outlawry to have magic spoken over oneself (K §7). That is exactly the seeker's position at the platform.
   - Gulaþing church law outlaws the soothsayer and fines the person who consults her 40 marks (Mitchell 2011, pp. 160–61).
3. **The texts the faith reads mostly do not exist yet.**
   - At 1178, *Eiríks saga rauða*, *Ynglinga saga* (Snorri is born in 1179), Saxo (begun c. 1185 at Absalon's request) and the *Grágás* codices (c. 1250–70) are all unwritten.
   - Only Hafliði's law of 1117–18 and Ari's *Íslendingabók* (1120s–30s) are on parchment.
   - At 1178 the völva rite would survive only as oral memory and a few "heathen sparks" (*Grettis saga*'s phrase, Mitchell 2011, p. 94). Such a faith would be living *under* the milieu that was about to write the sagas, not reading them.
4. **No institution would house the daughters.**
   - The only women's institutions are Christian nunneries: Vreta in Östergötland (c. 1100), and Kirkjubær in Iceland (founded 1186, after the start; the date is standard, page *unverified*).
   - None of them has any attested gender-variant use.
   - Gotland's institutions are the parish church, the *Gutnalþing* (the island's assembly) and the merchant voyage (Peel 1998, pp. 77–78).

**Conclusion for 1178.**
- A Gotland count who is openly a Bædling at 1178 fails the test outright. Turn the foothold seeding off for this date.
- Two honest choices remain:
  - **(a) Drop the faith from the 1178 map,** like Ha-Nehpakhot before 1323. This is the most faithful.
  - **(b) A hidden current with no land.** Seed only Marked courtiers and one landless völva with `secret_faith` at Gotland's court and in a few eastern-Baltic pagan courts (Ösel, Curonia), so that the faith can be played as a survival. Section 3B gives a version of this that may be worth a start of its own.

---

## 2. Candidate new hubs in the region

| # | Hub and date | Attested basis | Rating |
|---|---|---|---|
| **A** | **Uppsala / Svealand, 1066** (Erik the Heathen's court; seat in Uppland or Åland) | A pagan temple cult still working, described by a contemporary (Adam IV.26–27, Tschan 1959, pp. 207–208), with "unseemly" songs. Saxo's later topos of "effeminate gestures" and "unmanly" bells at Uppsala (Book 6, p. 135). A named pagan claimant in vanilla. The archaeology already used by the faith (staffs, chair pendants, Klinta, Lärbro) is Swedish (Price 2019, pp. 103, 121–24, 175). The seiðr/*ergi* complex holds (Meulengracht Sørensen 1983, pp. 18–20). **No source shows anyone assigned male living as a woman there.** | **Plausible** as a seat for the existing faith. The gender evidence is the same as at 867, no better and no worse. Its institutional basis is *better* than Gotland's at 1066. |
| B | **Gotland's merchant voyages, 1178** (a hidden Bædling current inside the Catholic republic, trading to the pagan eastern shore) | Gotlanders sailed "to all countries, both Christian and heathen" (Peel 1998, p. 78). A Gotlandic trading station with a St Olaf church existed in Novgorod in the first half of the 12th century (Peel 1998, p. 115). The *Guta saga* author still knew of the island-wide human sacrifice, the "boiling-companions" (p. 76). The 1171/72 papal bulls (*Non parum animus noster*, and the related letter often cited as *Gravis admodum*) call for war on the pagan Estonians and Finns. Fulco was missionary bishop of the Estonians from 1165 (standard dates; scholarly pages *unverified*; check Christiansen, *The Northern Crusades*). | **Thin** for gender, which is the same as Bædling's evidence everywhere. **Plausible** as the shape of a survival start, and it is the one place where Silk & Silver merchant mechanics are period-true. |
| C | **Ösel / Saaremaa, 1178** (the last pagan maritime power across from Gotland; vanilla pagan until 1228) | Pagan in fact until 1227. Henry of Livonia names Tharapita as an Oeselian god (*Chronicle* XXIV.5, Brundage trans.; page *unverified*). Oeselian, Curonian and Karelian raids on Scandinavia peak around the sack of Sigtuna in 1187 (standard; *unverified*). **There is no gender evidence of any kind,** and Estonian religion is not Norse: a Bædling seat here would be colonial ventriloquism. | **Thin.** Use it only as a refuge county the hidden current can flee to, or as a host for a travelling völva. It must never become an Estonian "version" of the faith. |
| D | **Rügen / Arkona, 1066** (with the Obodrite and Liutizian pagan revival) | A powerful cult institution: the flamen outranks the king (Helmold 2.108(12), p. 165, Álvarez-Pedrosa ed.). Women's divination at the hearth (Saxo 14.39, p. 183/188 in that edition). In **1066** the Obodrites killed the Christian prince Gottschalk, and Bishop John's head was offered to Redigast at Rethra on 10 Nov 1066 (Adam 3.51, Álvarez-Pedrosa §2.11.2, pp. 85–86). The cult is at a peak in 1066 and is destroyed in **1168**. **There is no gender crossing anywhere** (comparanda candidate A). | **Thin.** The best *map* hub of 1066 outside Sweden, but it would need a new invented faith on no evidence. Use it as the Bædling's pagan ally across the sea. Arkona's fall in 1168 is the right counter-evidence event (§4). |
| E | **Iceland, 1178** (Oddi and Skálholt; the saga milieu before the sagas) | The richest *legal* sex/gender categories in the region: the dress clause in both directions (K §155, §254), *ragr* (Add. §423), fostering and *arfsal*, the "six good housewives" defence (Gulaþing, Mitchell 2011, p. 161). A literate milieu forms around Oddi; Snorri is born there in 1179 and fostered from 1181 (standard; *unverified*). But Þorlákr's 1178 penances bite here first (Meulengracht Sørensen 1983, p. 26). | **Thin** as a hub: it is Christian and the reaction is sharpening. **Strong** as *reaction* and *flavour* for any Bædling start. |
| F | **Novgorod / the Rus', 1066–1178** | *Skomorokhi* are named in the Primary Chronicle s.a. 1068 among the devil's lures: "with trumpets and skomorokhi, gusli and rusalii", while the churches stand empty (PVL, IRLI ed.). In 1071 two *volkhvy* from Yaroslavl killed "the best women", accused of hoarding grain (PVL s.a. 1071; Álvarez-Pedrosa §4.1.16, pp. 285–89). Lay cross-dressing was a penanced sin "largely because it occurred in the context of carnival festivals of pagan origin" (Levin 1989, p. 280 n. 195), with a mild penance of 7 weeks (p. 195). Levin's claim that the skomorokhi were "the surviving remnant of the class of pagan priests" rests on Rybakov and is disputed (p. 86). | **Thin** as a hub (comparanda candidate D). Good as reaction and event content. Festival dress is seasonal inversion, not a life. |
| G | **Cuman/Kipchak steppe, Volga Bulgaria** | Golden, "Religion among the Qipčaqs of Medieval Eurasia", *Central Asiatic Journal* 42 (1998): 180–227 is the standard study (citation verified; **contents not read**). I found no medieval source for gender-crossing shamans among Cumans. The often-cited "transvestite shaman" material is **modern ethnography**: Basilov's Fergana case of 1968 and Chukchi and Koryak data (Basilov 1978, in Diószegi and Hoppál, eds., *Shamanism in Siberia*). Volga Bulgaria had been Muslim since 922. | **Thin; do not use.** Reading 20th-century Siberian or Central Asian ethnography back onto 12th-century Cumans is the primitivising and "third gender" trap the project rules forbid, and it touches living communities. |

No hub in the region beats Uppsala at 1066 for the Bædling, and none in the region qualifies for a *new* faith at either date.

---

## 3. Start sketches

### 3A. **"The Last Sacrifice" — 1066.9.15, Svealand** (recommended)

**Seat and who holds it.**
- **Seat:** move `tm_baeddel`'s 1066 foothold from `c_gutland` to **`c_aland`**. Åland is a small pagan island county under Svealand, about a day's sail from Uppsala, and pagan in vanilla until 1090.
- **Alternative:** a barony in `c_upland` if one can be granted cleanly.
- **Do not convert Erik the Heathen.** The 867 test runs showed that a converted ruler can snowball into an empire (`faith_design.md` §14). He stays `norse_pagan`, as the faith's protector and patron of Uppsala.
- Gotland remains a holy site of the faith, but its Catholic Stenkyrka holder is left alone.
- **Script change:** date-gate `tm_seed_foothold_effect` so that at ≥1066 it targets `c_aland` (if still pagan) and not `c_gutland`.

**Starter characters.** All are fictional; the faith claims no historical figure.
- **Ása Ulfsdóttir, countess of Åland**, about 40, Bædling, a cis widow. She holds the island for her late husband's house and keeps the hall's high seat for the seeress. She is a vassal of Erik the Heathen.
- **Þórvé the seeress**, about 55, a landless völva at Ása's court. The faith claims her as "one of nine sisters, and not all of them by blood" (faith voice, after Mitchell 2011, p. 131).
- **Hallveig, a daughter of the High Seat**, about 24 (she/her, a declared daughter). She is Ása's foster-daughter under a fostering contract (*Grágás* K §141) and knows the warding songs. She is the playable heir candidate, but not the heir by blood.
- **A Marked courtier**, about 16, from Sigtuna (she/her in narration once she is a daughter; before that, the game's Marked state). She is the first seeker of the start.
- Optionally, **a Gotland merchant's daughter, baptised**, who learned the songs from a heathen foster-mother. She is the "Guðríðr" singer who may refuse ("I am a Christian woman"). Her presence links Gotland to the start without making it pagan.

**Pressures.**
- **The war of the two Eriks** (vanilla). If Erik the Heathen dies (historically 1067), the faith loses its protector. A Christian Stenkilsson heir takes Svealand, and the Christian-law suits start to fire.
- **Hamburg–Bremen missions** (Adam's own church) and the Sigtuna bishopric (c. 1050). These feed missionary events, and the Uppsala temple is "under threat". The Uppsala special building in Uppland becomes an object of war.
- **The 1080s conversion window.** Vanilla turns the remaining Svealand counties Catholic in 1080–1090. An event pair "Blót-Sveinn" / "Ingi returns" (c. 1084–87, from the saga tradition; *unverified*) could give the faith its last open sacrifice and then the end of it.
- **Wendish allies.** The 1066 Obodrite and Liutizian revival (Adam 3.51) and pagan Rügen give the faith friendly courts across the Baltic until 1168.
- **Neighbours' law.** *Grágás* dress and *ragr* rules in Iceland; Gulaþing church law in Norway (outlawry for the soothsayer, a fine for the client); Danish law "quiet on witchcraft" (Mitchell 2011, p. 157); Pope Gregory VII's letter of 1080 telling the Danish king not to blame women for storms (Mitchell 2011, p. 169), already proposed as a dated event.

**Gate.** The existing *Ask a Völva to Sit for Me* is unchanged. Two dated touches:
- At Uppsala itself the rite can be tied to the nine-yearly feast (Adam IV.27). If the seeker travels to the temple in a feast year, odds go up. That is design built on attested timing.
- After Uppland converts (1090), the platform rite inside Svealand gains the Christian-law liability split from the Mitchell note: the völva risks outlawry, the seeker a fine.

**Mechanics that carry over unchanged.** The three-part seiðr chain; *A Name of the Hall*; *Before the Thing*; the flyting; *Teach the Warding Songs*; fostering and sworn sisterhood; *Rescue the Daughters*; Níðhöggr; Houses and Homecoming (homecoming target `title:c_gutland` in `tm_on_actions.txt` l. 833 must follow the seat). What is new is about four dated events and the foothold retarget.

### 3B. **"Heathen Sparks" — 1178.10.1, the Gotland voyage** (optional; only if the user wants the faith present at 1178)

**Premise.** The public cult is gone. The faith survives as a secret current among the households of a Catholic merchant republic that still trades with the last pagan shore. It is a different game: no landed seat, `secret_faith`, and survival rather than conversion.

**Seat and who holds it.** No faith-held county.
- **Silk & Silver installed:** a Bædling-secret *merchant company* domiciled in Visby, if the DLC allows merchants at 1178 and the decision gate permits it (`silk_and_silver.md`, open questions). The patron is the vanilla Gotland republic.
- **Without the DLC:** two or three secret-faith courtiers in the Gotland ruler's court and one landless völva who winters on **Ösel**. Ösel is used only as a pagan host county; its Estonian ruler stays `finnish_pagan`.

**Starter characters (fictional).**
- **Rodvé Hejnumsdóttir**, about 45, widow of a Gotland trader. She is Catholic in public and Bædling in secret, and runs the voyages east. Her house name echoes vanilla's Hejnum patrician house; she is not one of its historical members.
- **A daughter of the High Seat**, about 30 (she/her). She was made under the platform as a girl on Ösel, where no bishop reaches. She sails as Rodvé's partner.
- **An old Icelandic woman**, about 70, who knows the warding songs and has crossed to Visby on a pilgrimage sentence. She is the oral source in a world before the sagas.

**Pressures.**
- **Þorlákr's penances (1178).** The sisters' loves are named sin, and *secret_faith* exposure risk goes up in Icelandic and Norwegian courts.
- **Sverrir's war in Norway** (from 1177). The 1164 Gulaþing clause makes outlawry a confiscation tool.
- **The papal bulls of 1171/72** make Ösel and the Estonian shore a crusade target. Vanilla converts Ösel only in 1228, so the refuge has a 50-year clock.
- **The sack of Sigtuna in 1187** (standard date; *unverified*) brings a backlash against anyone who trades with heathens.
- **Absalon at Lund (1178)** and the coming *Gesta Danorum*. Saxo's Wecha story (Book 3, pp. 80–82) becomes the slander the faith must answer; the repo's line is "He put on the dress to get into her room. We put it on because it is ours."

**Gate.** The rite must go *abroad* to work. The seeker sails to Ösel, or to a heathen farm "out east", and the völva sits there. The Christian-law split applies on return. This reuses the travel/scheme step proposed in `silk_and_silver.md` ("Trade Opportunity schemes as rite steps").

**Honesty note.** This start is speculative throughout. Its only attested anchors are the voyages, the Novgorod station, the bulls and the Christian law. No source shows Gotlanders keeping seiðr after about 1050. Rate it **thin**. Only build it if the project wants every faith on every bookmark.

---

## 4. Counter-evidence: what closed or worsened in the region

- **Gotland had converted before 1066.** *Guta saga* (Peel 1998, pp. 78–79) and the runic evidence (p. 109) both say so. **Trap:** Strelow (1633) read the *Guta saga* name *Ormika* as feminine and made Ormika a woman. Peel calls this "almost certainly incorrect" (p. 42). Do not use Ormika as a woman convert.
- **Uppsala's cult ended between about 1080 and 1100,** and Uppsala became an archbishopric in 1164. The holy site becomes a cathedral.
- **Norway, 1164:** the first and only Norse law against sex between men (Gade 1986).
- **Iceland, 1178–93:** Þorlákr's penances extend to women's love for women (Meulengracht Sørensen 1983, p. 26).
- **Arkona, 1168:** the last great pagan temple of the southern Baltic is destroyed by Valdemar I and Absalon (Saxo XIV, in Álvarez-Pedrosa). Vanilla wrongly dates Rügen's conversion to 1150; a fix or event could correct it.
- **Rus':** pagan *volkhvy* are put down with beard-pulling and hanging (PVL 1071). Lay cross-dressing is penanced as pagan play (Levin 1989, pp. 195, 280). Rus' had already accepted a eunuch metropolitan in 1090 ("a dead man has come", PVL; comparanda item 20). The Rus' reaction rung is penance, not death.
- **The *ergi* shame is itself partly Christian.** Colwill argues that the written shame around seiðr is a later Christian layer (2021, p. 184), and Mitchell notes that magic in the sagas marks "the past" (2011, p. 103). The 1178 world is where that layer is being laid down. Every saga quotation the faith uses was written *after* 1178.
- **The Baltic pagans are crusade targets from 1171/72.** Finland is converted in vanilla from 1158. Ösel holds until 1227/28.
- **Later deterioration, after both bookmarks** (for era arcs): Norway's capital sorcery law c. 1300; Sweden's c. 1350; the burning of the Kirkjubær nun in 1343 (Mitchell 2011, pp. 122–25, 156–57).

---

## 5. Open questions

1. **Retargeting the foothold.** Can `tm_seed_foothold_effect` take a date-dependent county (`c_aland` at ≥1066), and does the homecoming target (`tm_on_actions.txt` l. 833) follow it? Should Gotland stay a holy site? I suggest yes, replacing York, which loses its Norse meaning after 1066 and Stamford Bridge.
2. **Will Erik the Heathen keep the faith alive?** In observe runs from 1066, does he survive the war of the two Eriks and keep Uppland pagan? If he dies on schedule, Svealand converts by script in 1080–1090 whatever the AI does, and the start becomes a deliberate last stand.
3. **Silk & Silver republics.** Vanilla Gotland is a republic at 1066 and 1178. Does the rework give it an Assembly? Can a merchant company exist at 1178 with a `secret_faith` head?
4. **To verify before any loc cites them:**
   - Tschan's page for Adam III.53;
   - the *Hervarar saga* edition for Blót-Sveinn;
   - Christiansen (or Fonnesberg-Schmidt, *The Popes and the Baltic Crusades*) for the 1171/72 bulls and Fulco;
   - Henry of Livonia XXIV.5 for Tharapita;
   - the date of the Sigtuna sack (1187);
   - Absalon's elevation (1177/78);
   - Kirkjubær's founding (1186);
   - Anselm's 1102 council;
   - the edition of Þorlákr's penitential (*Skriftaboð Þorláks*), so as to read the women's clause directly rather than through Meulengracht Sørensen.
5. **Golden 1998** should be read before the Cuman question is closed for good. I expect it to confirm *qam* (shaman) vocabulary and Umay, not gender crossing. That expectation is *unverified*.
6. **Peel 1998 vs. Peel 1999.** The page numbers here are the thesis's. Map them to the Viking Society edition (Text Series XII) before citing in the faith page.

**Sources consulted on the web:** [UCL Discovery, Peel 1998](https://discovery.ucl.ac.uk/id/eprint/10103042/1/An_edition_of_Guta_saga_with_i.pdf); [World History Encyclopedia, Temple at Uppsala](https://worldhistory.org/Temple_at_Uppsala) (for the Tschan pages); [Wikipedia, Eric and Eric](https://en.wikipedia.org/wiki/Eric_and_Eric); [Wikipedia, Fulco](https://en.wikipedia.org/wiki/Fulco_(bishop_of_Estonia)); [Wikipedia, Saint Thorlak](https://en.wikipedia.org/wiki/Saint_Thorlak); [SPRI catalogue, Basilov 1978](https://www.spri.cam.ac.uk/library/catalogue/records/199501/). The Wikipedia hits are pointers only; replace them with scholarly pages before use.
