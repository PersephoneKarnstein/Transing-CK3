# Starts at 1066 and 1178: South Asia and maritime Southeast Asia

Region: Tamil country, the Deccan, North India, Kashmir, Bengal, Sri Lanka, Srivijaya, Java, Bali, Champa, Angkor.
Faith seated here: Cūṭikkoṭutta Mālai (the Worn Garland), Kanchipuram.
Written 2026-10-20. No repo file was edited.

**What I read first.** `docs/faiths/cutikkotutta-malai.md`; `docs/research/south_reading_list.md` (India; Island SE Asia); the notes `ind_orr_temple_women.md`, `ind_narayanan_vernacular_veda.md`, `ind_venkatesan_secret_garland.md`, `ind_carman_narayanan_tamil_veda.md`, `ind_benherut_sivas_saints.md`, `ind_ramanujan_bhakti.md` and `sea_zwilling_sweet_third_sex.md`; `docs/silk_and_silver.md`; and the seeding code in `common/on_action/tm_on_actions.txt` (`tm_seed_foothold_effect` for c_kanchipuram and c_candragiri). Where a fact comes from one of those notes, the page given is the note's citation of the book. I did not reopen the books.

**What I checked in the CK3 1.20 files** (Steam install, read only):
- **1066.** `history/titles/k_tamilakam.txt` gives c_kanchipuram and c_candragiri to `narayanavanam_yadava_ruler` (Immadi Narasimha, Telugu Yādava, Shaivism, born 1010) from 1020, under k_tamilakam (Vīrarājendra Chola).
- **1178.** On 1178.1.1 both counties, and c_tiruvannamalai too, pass to **Kulottunga III himself** (189121, Shaivism, born 1145).
- **The county's faith.** `history/provinces/k_tamilakam.txt` starts province 1119 (Kanchipuram) as **Yāpanīya** Jain and switches it to **Digambara** on 1066.1.1.
- **Map.** b_takkaloma (Takkolam) lies in c_kanchipuram. b_kudalasangama (Kūḍalasaṅgama, Basava's shrine) lies in c_vatapi. The reading list's map check only knew b_kudala, which is a different place.

---

## 0. Short answer

- **1066: carry forward with stand-ins, plus light flavour.** Most of the faith's premises in 1066 are the same as in 867, or slightly worse. Orr's data put temple women at their low point in the middle Chola period. The texts the faith inverts had not yet been written.
- **1178: a new start with new characters, on the same seat.** It is not a new faith. Since 867, three things have changed that the test cares about:
  1. **The institution.** Temple women are entering their richest, most numerous and most independent period. Orr's own periodisation breaks at **1178**.
  2. **The texts.** The commentaries that call the girl's voice a "guise", the *Periya Purāṇam*, the 12th-c. staff rite and the Kannada bride vacanas all now exist and can be read.
  3. **The neighbours.** Men's sectarian titles now shut women out, and Śaiva–Vaiṣṇava friction is on record.

  So the Garland's mechanics stop anticipating the period and start fitting it. Its "both temples" premise also comes under real pressure.
- **No new hub elsewhere in the region reaches "strong".** The best of the rest are Java/Kediri (the *kĕḍi* of the charters, plausible to thin, with no change between 867 and 1178) and Śvetāmbara Gujarat (thin, and a third-sex trap). Everything else is thin, later, or context only.

---

## 1. Verdicts for Cūṭikkoṭutta Mālai

### 1066: carry forward with stand-ins, plus light flavour

**Who holds the seat.** The holder changes from a Pallava lord (867) to a Telugu Yādava Śaiva count under the Chola emperor (vanilla). He holds both Kanchipuram and Candragiri. The existing seeding (a county seeded, a daughter at the court, a Candragiri foothold) still works, but the code comment "Kanchipuram is the Pallava capital" will be wrong at this date. The host's gender order is the same imperial Chola one in both years.

**The institution is at its low point.**
- Orr's "middle Chola" subperiod, 985–1070, is the trough for temple women (`ind_orr_temple_women.md` §3.8, citing Orr 2000, pp. 42–46, 163–164).
- After c. 1050, other women fade from the record, and queens and palace women dominate giving (Orr 2000, pp. 46, 67–73).
- Rājarāja's settlement of the four hundred at Thanjavur (c. 1014) "may have emptied nearby temples of temple women for a century" (Orr 2000, pp. 141–142). It was "exceptional, extravagant—and ultimately unsuccessful" (pp. 80–82, 161, 163–164).
- *Tēvaṉār makaḷ*, "daughter of God", still appears five times in 985–1070, against seventeen in 850–985 (table 2.5, p. 52).
- The "deals" (gold given for hereditary honours) begin only from 1070 (pp. 74–75).

The temple-street line therefore rests on less contemporary evidence in 1066 than in 867.

**The texts.**
- **Available:**
  - The hymn canon. Nāthamuni's compilation is 10th c. by tradition (Narayanan 1994, p. 123). Uyyakoṇṭār's mid-10th-c. *taṉiyaṉ* already carries the garland legend (Venkatesan 2010, p. 223).
  - Recitation. The *araiyar* families trace their rights to the 11th c. (Narayanan 1994, p. 123); that is their own claim.
- **Not yet written:**
  - Piḷḷāṉ's *Six Thousand*, 1100–1150 (Carman and Narayanan 1989, p. xi).
  - The *Periya Purāṇam*, c. 1135.
  - The *Uttara-Kāmika* staff rite, 12th c. (Goodall 2018, pp. 110–12).
  - Basavaṇṇa's vacanas (d. c. 1166/68).
  - Dāsimayya, "probably the earliest" vacana poet (said to be born in the 10th c.), may be the one exception (Ramanujan 1973, section introduction).

**Rāmānuja.**
- **The two chronologies:**
  - Tradition gives 1017–1137 and places his early career at Kanchi: study under Yādavaprakāśa and service at the Varadarāja temple.
  - Scholars have proposed a later life, c. 1077–1157, partly on Karnataka inscriptions (secondary summary only; *unverified* against Carman 1974 or another primary scholarly source).
- **The epithet.** "Tiruppāvai Jīyar" is found here only on devotional sites (ibiblio SriPedia, ramanuja.org). It is hagiographic tradition of uncertain date, *unverified* in scholarship.
- **Design consequence.** Do not make him a starter character or a background figure at Kanchi in 1066. Under one chronology he is not yet born. In any case he is a living tradition's founder.

**Flavour worth adding.**
- The Thanjavur holy site is now *current*: the four hundred are living women, or their "nearest relations" (SII 2 no. 66).
- A stand-in daughter's court is the Telugu Yādava court, not a Pallava one.

**Verdict.** None of the four premises is better than in 867, so a new start is not justified. Carry forward with stand-ins. Fix the "Pallava" assumption, and add an optional 1066 text variant for the holy sites.

### 1178: new start with new characters (same seat and faith; Takkolam is a better foothold than Candragiri)

**Who holds the seat.** **Kulottunga III**, newly crowned, holds Kanchipuram, Candragiri and Tiruvannamalai in his own demesne (vanilla). A foothold therefore has to come out of the emperor's domain. That is a design problem, and an opportunity (see §3). Historically the Chola centre was weakening by now, as Hoysaḷas and Pāṇḍyas rose. Orr finds that temple women thrive "under non-Chola kings, and where royal power is weak", and most of all in the northern region, which includes Tondaimandalam (Orr 2000, pp. 80–82, 161, 163–164).

**1. The institution peaks, and its terms match the Garland's own mechanics.** Orr's periods are 850–985, 985–1070, **1070–1178 and 1178–1300**. The last is the one in which:
- temple women are most numerous, most often named and richest (pp. 46, 67–73, 161–163);
- 91% of uses of *tēvaraṭiyār* name individual women (p. 55);
- the 21 "deals" fall (all 1070–1300), ten of them hereditary "to her descendants" (pp. 74–75, 151);
- female-led families grow, mainly in the north, with 83% of relationships traced through the mother and no father ever named (pp. 153, 156, 158);
- consort-goddess (*nācciyār*) shrines endowed by temple women spread (p. 24).

Temple women also bought the singing of *Tiruvempāvai* verses at Nallur in the 12th c. (ARE 1940–41 nos. 143–176; Orr pp. 56, 105–108) and at Tirupampuram in 1213 (pp. 17–18). At Kanchipuram itself, a Vaiṣṇava temple woman, *avvalvanatiyal*, "devotee of that Lord", gives in 1118 (SII 4.134; p. 138).

Every mechanic of the Garland's line (A Name in Stone, the temple's deal, Take as Daughter, the choice of song in Mārkaḻi) is thin in 867 and contemporary in 1178. That is the strongest single reason for a new start.

**2. The texts the faith reads and inverts now exist.**
- **The guise.** Piḷḷāṉ (1100–1150) calls the girl the poet's guise yet narrates him as "she" (Carman and Narayanan 1989, pp. xi, 96, 99). The Garland's first doctrine ("the guise was the truth") needs this text to argue against. In 867 it is anticipatory; in 1178 it is a live quarrel with living commentators.
- **The performance.** The *araiyar* performance of the girl's part is attested by 12th-c. anecdote: Empār's correction of a performer, and Nañjīyar weeping over his teacher's performance (Narayanan 1994, pp. 126, 132, citing 13th-c. commentary). It is a men-only performance of women (p. 123; ch. 8 n. 14). That is the daughters' best grievance in the faith's voice: "the temple lets a man play the girl but will not let the girl in."
- **The *Periya Purāṇam*** (c. 1135) has Kāraikkāl Ammaiyār ask for, and receive, a changed body (Pechilis 2012, p. 202). Claim the pattern only.
- **The *Uttara-Kāmika*** (12th c.) gives the staff rite, Nandin's staff touched to the head with a name given (Goodall 2018, pp. 110–12). The gate's final step is anachronistic in 867 and current in 1178.
- **Kannada.** Basavaṇṇa (d. c. 1166/68) "wears these men's clothes only for you" (Ramanujan 1973, vacana 703). Harihara's "devotee is wife, liṅga husband" comes a generation later (c. 1200–1240; Ben-Herut 2018, pp. 85–88). The bride voice is now a recent, contested Śaiva movement next door.

**3. The neighbours' gender order has hardened.**
- **Men's sectarian titles.** Men of status are renamed *mahēśvara*, *śivabrāhmaṇa* or *śrīvaiṣṇava*, groups that exclude women. Meanwhile *tēvaraṭiyār* becomes a woman's word (Orr 2000, pp. 55–56).
- **Hymn singing narrows.** Singing the *Tiruvāymoḻi* is men's work (p. 108, ch. 4 n. 23), and hymn singing narrows toward Brahmans in the 13th c. (p. 109).
- **Śaiva–Vaiṣṇava friction is on record.** Oṭṭakkūttar, court poet to Kulottunga II (r. 1133–50), boasts three times that his king threw Viṣṇu's image into the sea at Chidambaram (KulOttungaccOLan ulA and others). Nagaswamy and others dispute any wider persecution. My only witnesses for this are online summaries, so it is *unverified*; check Nilakanta Sastri, *The Cōḷas*.
- **Rāmānuja's exile.** Tradition has him exiled to Hoysaḷa Melkote under a hostile Chola. The tradition is real; the event is debated.
- **What this does to the faith.** It does not destroy the Garland's "both temples" synthesis. It turns it into a stance under pressure. In 867 joining Śiva's daughters to Viṣṇu's bride was eccentric; in 1178 it is provocative.
- **The county's own faith** in vanilla has been Digambara Jain since 1066. The Yāpanīyas, whose *Strīnirvāṇaprakaraṇa* argued that women can be liberated, have gone from the map (Jaini 1991, *Gender and Salvation*; *not read here*, P2). This is a vanilla abstraction, but it gives a real doctrinal neighbour for a reaction event. Keep it doctrinal; no Jain stereotypes.

**4. The title "Daughter of God" is an archaism by 1178.** It has one attestation in 1070–1178 and one in 1178–1300 (table 2.5, p. 52). The Garland can keep it *as an old Śaiva honorific it revives*, and that is better flavour in 1178 than in 867. The narrator should say so. *Talaikkōli* and the *māṇikkam* ("ruby") titles common after 1070 (pp. 60–61, 147–148) are the period's own honorifics.

**Verdict.** A new start with new characters is worth building. The seat, faith and gate stay the same. The line, the world events and the starting texts become contemporary rather than anticipatory, and the host's gender order (men's sectarian titles, a hostile Chola memory) gives new pressure.

---

## 2. Candidate hubs in the region (1066 / 1178)

| # | Hub | Date | Attested basis | Strength |
|---|---|---|---|---|
| A | **Kanchipuram with Takkolam** (c_kanchipuram, b_takkaloma) | 1178 (and 1066, weaker) | The only temple-women centre attested through the whole period (Orr pp. 139–140). Takkolam is one of three clusters of *tēvaṉār makaḷ* (p. 58), and the site of the one documented mother-to-daughter title, Kumarati-nankai (pp. 149–150). A Vaiṣṇava temple woman at Kanchi in 1118 (p. 138). A 13th-c. Varadarāja endowment for "women who sing before the Lord" (Narayanan 1994, p. 55). | **Strong** (as an institution for the faith to live inside; no crossing attested) |
| B | **Tiruvannamalai** (c_tiruvannamalai) | 1178 | One of Orr's temple-woman centres (p. 142), in the northern region where the 13th-c. female-led families concentrate (pp. 153, 158). Its county starts Śvetāmbara in vanilla. The emperor holds it in 1178. | **Plausible** (a second holy site or alternative seat) |
| C | **Chola heartland temple towns: Tiruvarur, Tiruvidaimarudur, Nallur** (c_cholamandalam; no baronies of their own) | 1178 | Tiruvarur and Tiruvidaimarudur are temple-woman centres (Orr pp. 140–141). Tiruvidaimarudur is a *tēvaṉār makaḷ* cluster, where every temple servant bore the name Nakkan (pp. 58, 146). Nallur has 12th-c. purchases of *Tiruvempāvai* verses (pp. 56, 105–108). | **Plausible** (holy-site and event flavour; Thanjavur's site already covers the county) |
| D | **Kannada śaraṇa country** (b_kudalasangama in c_vatapi; Hampi; c_kalyani) | 1178 | The bride voice of Basavaṇṇa (vacana 703). Dāsimayya 133, "the self that hovers in between is neither man nor woman", is about the soul, not a third kind of person (`ind_ramanujan_bhakti.md`). Harihara's temple-wedding initiation is c. 1200–1240 (Ben-Herut pp. 85–88). The single Kalyāṇa community is a 16th-c. myth (Ben-Herut pp. 18–19). | **Thin as a hub.** Voice only, no life. The Liṅgāyats are a large, politically active living community, so the risk is high. Use as kin flavour and a Śaiva reaction voice. |
| E | **Kediri, Java** (b_JAV_Daha) | 1066, 1178 | *Kĕḍi* stand among the palace dependants (*watĕk i jro*) in charters from 873 to 1305, with the same lists before and after our dates (Boechari and Wibowo 1985/86, E.3, E.80). The *Ślokāntara* defines the *kĕḍi* as "a woman and yet not a woman" (OJED p. 2180). The *Wirāṭaparwa* (996) has Arjuna become the *kĕḍi* Wṛhannalā (OJED p. 838). Kediri's kakawin flowering includes the *Bhāratayuddha*, begun 6 Sept 1157 by Mpu Sĕḍah for Jayabhaya. | **Plausible to thin.** A category is attested in period, but it is defined as a defect (*wikāra*) and has no rite. **Nothing changes between 867 and 1178**, so the dates do not justify a start. |
| F | **Śvetāmbara Gujarat** (b_anahilapataka) | 1178 | Jain law classifies *napuṃsaka* types and debates whether some may be ordained and liberated (Zwilling and Sweet 1996, "Like a City Ablaze", *JHS* 6.3: 359–384; exists, *not read*, so the ordination details are *unverified*). The Chaulukya court is Jain-patronised (Hemacandra d. 1173). In 1178 Mūlarāja II's regent mother, Nāyikādevī, is said to have defeated Muḥammad of Ghūr at Kāsahrada (*unverified*; female-to-male rule data, reaction only). | **Thin**, and a **third-sex trap** under Bhatt: the category files people as neither. |
| G | **Kashmir** | 1066, 1178 | Kṣemendra's satires (mid-11th c.: *Narmamālā*, *Deśopadeśa*, *Samayamātṛkā*, *Kalāvilāsa*) target officials, false gurus, courtesans and bawds. A summary of the satires shows nothing on eunuchs, *klība* or cross-dressing (wisdomlib study, contents only). Kalhaṇa's *Rājataraṅgiṇī* (1148–49) gives queens such as Diddā (r. 980–1003). I found no gender-crossing figure; *unverified*, and Stein's index needs checking. | **Thin**. Reaction voice only (satire of hypocrisy; a chronicler hostile to women rulers). |
| H | **Kāmasūtra and the Jayamaṅgalā** (Gujarat / pan-Indian) | — | KS 2.9 splits the *tṛtīyā prakṛti* into a "female" and a "male" form, both defined by giving fellatio as a trade (Zwilling and Sweet 2000, pp. 119–120). Yaśodhara's *Jayamaṅgalā* is dated 10th–13th c. A copy came from the library of the Vāghela king Vīsaladeva (r. c. 1243–62), so it may well post-date 1178 (secondary only; *unverified*). | **Not a hub.** It labels sex-work, and the project already bans the term as an honorific (`sea_zwilling_sweet_third_sex.md`). Reaction only. |
| I | **Angkor / Champa** | 1178 | Ta Prohm's stele (1186) lists 615 female dancers, and Jayavarman VII's son's inscription lists 1,622 (secondary, soundsofangkor.org). The Cham sacked Angkor in 1177. Zhou Daguan, 1296–97, describes groups of feminine young men in the market soliciting Chinese men (Harris trans. 2007; page *unverified*). | **Thin.** Late, a hostile foreign gaze, and a sexual frame. Context only. |
| J | **Bengal (Sena)** | 1178 | Lakṣmaṇasena's accession c. 1178/79 (*unverified*). Jayadeva's *Gītagovinda* (late 12th c.) has *sakhīs* as characters. Men living as *sakhī* is 16th c. and later (reading list, finding 4). | **Thin.** |
| K | **Sri Lanka (Polonnaruwa)** | 1178 | Parākramabāhu I's sangha purification and unification of 1165: thousands disrobed (Gornall 2020, *Rewriting Buddhism*, UCL Press, OA; *not read*). The bhikkhunī order's end c. 1017 is still sourced only to newspapers (*unverified*). | **Counter-evidence**, not a hub. |
| L | **Ghaznavid Lahore / Ghurid North India** | 1066 / 1178 | Slave-soldier courts. The mukhannathūn literature is Abbasid (`hist_rowson_mukhannathun.md`). | **Reaction only**; Islamic-neighbour opinion already exists (`tm_islamic_daughter_opinion`). |
| M | **Bugis bissu** (Luwu) | — | Every direct witness is from 1545 or later. Luwu's palace centre at Malangke dates from c. 1300 (Bulbeck and Caldwell 2000, p. 69). A **living community**. | **Context only.** Not in the window for either date. |

**A better hub than Kanchipuram?** No. Kanchipuram is still the best, and in 1178 it is better than in 867. Within it, **Takkolam** (b_takkaloma, a temple holding in c_kanchipuram) has stronger specific evidence than Candragiri: it is a *tēvaṉār makaḷ* cluster and the site of the only attested mother-to-daughter title. Srirangam stays weak as a temple-street site: "women are conspicuous by their absence" from its lists of functionaries (Orr pp. 81, 142–143).

---

## 3. Start sketch: Cūṭikkoṭutta Mālai, 1178 ("The Street of Rubies")

**Seat and holders.**
- **Kanchipuram** remains Kulottunga III's (vanilla).
- **The foothold moves from Candragiri to b_takkaloma**, held as a **temple holding** by an elder Daughter of the Garland. Taking a whole county (Candragiri) out of the new emperor's demesne is a heavy edit at 1178; a temple barony is lighter. It is also truer to Orr's picture of a medium temple whose women give and receive honours, rather than a countess.
  - **Engine check:** confirm that a theocratic barony can be seeded to a Garland clergy character under a Shaiva liege.
  - **Fallback:** keep the current Candragiri effect, which already works at any start.
- c_kanchipuram is still seeded with the Garland, as now.

**Fictional starter characters.** All are invented. Their names follow Orr's attested patterns (title-elements such as *-māṇikkam* and *-talaikkōli*; matronymic chains). None is a historical person.

1. **Ceyyavāymaṇi alias Takkōla-māṇikkam**, about 55, Daughter of the Garland (she/her). The elder of the temple street, holding the Takkolam temple barony. She has bought, for herself "and her descendants", the singing of a verse in Mārkaḻi and a lamp in stone. Learning and diplomacy. She is the faith's head-of-street in all but name.
2. **Nakkaṉ Cāni**, about 24, her chosen daughter, through the vow three Mārkaḻis ago (she/her). She is the heir to the share, so *Take as Daughter* is already done at start. She is courtly and ambitious, and wants a *nācciyār* shrine of her own.
3. **Ariyapirāṭṭi**, about 30, a temple woman of the Varadarāja temple, *not* of the Garland. She is a cis woman, Vaiṣṇava, and an ally and co-donor. Orr found that temple women's co-donors were mostly other temple women (p. 83). She embodies the "both temples" bridge, and her friendship is the social gate's first companion.
4. **A Marked courtier at Kulottunga's court in Kanchipuram** (she/her, closeted), to whom the call can fire in the first Mārkaḻi. She gives the player a seeker to bring through the vow.
5. **Hostile and ambivalent voices (male, attributed):**
   - a Śrīvaiṣṇava commentator-reciter at Kanchi who quotes Piḷḷāṉ's "guise" against the daughters;
   - a *mahēśvara* temple official who controls the share registers.

   Both are minor, and their hostility is in their own voices.
6. **Optional, Silk & Silver:** a merchant of the Five Hundred (Ainnūṟṟuvar) as patron of the street's gifts. This depends on the DLC's merchant mechanics. Reading: Abraham 1988.

**The pressures they face.**
- **The emperor's register.** The shares and honours are granted by temple councils under an emperor who is Śaiva and newly crowned. A "Pandit's Objection" variant fires at the imperial level: Kulottunga is asked to rule on the street.
- **The sectarian squeeze.** Men's titles (*śrīvaiṣṇava*, *mahēśvara*) shut women out (Orr pp. 55–56), and the street's double allegiance is called treachery by both sides. A "Throw the Image into the Sea" memory event can use Oṭṭakkūttar's boast as the voice of a Śaiva courtier, marked as court poetry and verified first.
- **The men's stage.** The *araiyar* perform the girl; the daughters may not sing the *Tiruvāymoḻi* (Orr p. 108). This is a dissent event in the faith's voice.
- **War.** Kulottunga III's Pāṇḍya wars and the Hoysaḷa rise pull the court's men away. The temple councils grow stronger in their absence, which Orr says favours temple women.
- **Doctrinal neighbours.** The county is Digambara (vanilla), and Śaiva śaraṇa bride-talk comes out of Karnataka. These are reaction events, not antagonists.

**The gate.** Keep *Keep the Pāvai Vow* (Mārkaḻi, the companions, the garland, the dream, the staff). Add one optional 1178 step: **Buy a Verse**. For gold, the temple grants the right to sing a verse of the *Tiruvempāvai* at Tiruvātirai in Mārkaḻi "to her and her descendants", which adds success weight (Orr pp. 17–18, 105–108). The staff and the name now cite a *contemporary* text (*Uttara-Kāmika*, Goodall 2018). The gate still waits and never punishes; failure means "Next Mārkaḻi".

**Existing mechanics that carry over unchanged.**
- The vow chain `tm_garland.0001`, `.0010–.0013` and `.0002`.
- The Temple Street tenet with *Take as Daughter*.
- *A Name in Stone* (`tm_garland.0020`). Raise its weight at 1178, because the deals are in period.
- *A Pandit's Objection* (`tm_garland.0030`).
- `tm_eastern_daughter_opinion` and "A Soul Made Woman".
- The growth engine. Keep it slow, with no visible caps.
- `tm_seed_marked_courtiers_effect`.

**What is new.**
- The b_takkaloma temple seat, or the Candragiri fallback.
- The 1178 bookmark characters above.
- One holy-site text update. Kanchipuram: "devotees of the Lord gave lamps here in every century of the Cholas", with an 1178 variant naming the rubies.
- Three events: Buy a Verse; the guise quarrel; the image in the sea.

**Second sketch (lighter, optional): Tiruvannamalai as a second street in 1178.** Seed a daughter at Kulottunga's court there, or a temple holding at b_tiruvannamalai, as a second node in the northern temple-woman belt (Orr p. 142). This is only worth it if observe runs show the faith dying with a single foothold. No new characters beyond one elder daughter.

---

## 4. Counter-evidence: what closed off or got worse

- **"Daughter of God" died out as a title** after 985: one use in 1070–1178 and one in 1178–1300 (Orr table 2.5, p. 52).
- **Men's sectarian titles exclude women** (Orr pp. 55–56). Hymn singing narrows to Brahmans and professionals in the 13th c. (p. 109). Women are barred from the *araiyar* (Narayanan 1994, ch. 8 n. 14).
- **Śaiva–Vaiṣṇava conflict:** Oṭṭakkūttar's boast about Kulottunga II and the Rāmānuja exile tradition (both contested). This weakens the "both temples" premise.
- **The Thanjavur settlement failed** and drained nearby temples (Orr pp. 141–142, 161, 163–164).
- **Kanchipuram's vanilla faith turns Digambara on 1066.1.1.** The Yāpanīyas, who argued that women can be liberated, drop out (game file; the doctrinal point is from Jaini 1991, *not read*).
- **Sri Lanka:** the purification of 1165 under Parākramabāhu I (Gornall 2020); the bhikkhunī order possibly already lapsed (*unverified*).
- **North India:** the Ghurid push begins in 1178 (Kāsahrada), and the Delhi Sultanate follows from 1206. Muslim courts' eunuch and mukhannath categories are reaction data only.
- **Angkor:** the Cham sack of 1177 falls on the very eve of the bookmark. The later Zhou Daguan witness is hostile.
- **Kashmir:** Kalhaṇa's moralising about queens and courts. No opening for daughters was found.
- **After the window:** temple women stop giving after 1300 (Orr pp. 174–177). Raids on Srirangam c. 1311 and 1323 (Narayanan 1994, pp. 83–84). This does not touch the 1178 start, but it sets the end of its arc.

## 5. Open questions

1. **Engine:** can a temple barony (b_takkaloma) be seeded to a female Garland clergy holder under Kulottunga III, and does Silk & Silver's district rework change temple holdings?
2. **Oṭṭakkūttar's image-in-the-sea boast:** verify in Nilakanta Sastri, *The Cōḷas*, and a scholarly edition of the *ulā*s before it appears in any event.
3. **Rāmānuja's chronology:** 1017–1137 or c. 1077–1157. Verify in Carman 1974, *The Theology of Rāmānuja*. Also "Tiruppāvai Jīyar": find the earliest hagiographic source (the *Guruparamparāprabhāvam*, 14th c.?) before it is used even as tradition.
4. **Who actually held Kanchi in 1178?** Telugu Coḍa feudatories are reported in the region in the late 12th c. (*unverified*). Vanilla gives Kanchi to the emperor; do we follow vanilla?
5. **Zwilling and Sweet 1996:** read it for the Jain ordination rules before using Gujarat even as reaction.
6. **The *Jayamaṅgalā*'s date:** confirm in Doniger and Kakar 2002 (introduction), or another scholarly source, whether it is before or after 1178.
7. **Java:** does Creese 2004, *Women of the Kakawin World*, discuss the *kĕḍi* or Wṛhannalā in Kediri-period kakawin? Are there Old Balinese charters (Goris 1954) with *kdi* for the 11th–12th c.?
8. **Kalhaṇa:** search Stein's 1900 translation and index for *ṣaṇḍha*, *klība* or eunuchs (Harṣa's reign, 1089–1101) before closing Kashmir.
9. **Orr 1178–1300 counts:** how many of the 21 deals and the female-led-family records fall in Tondaimandalam (the Kanchipuram district) specifically? That would decide between Takkolam and Tiruvannamalai.

## Sources used here (beyond the repo notes)

- Orr, Leslie C. 2000. *Donors, Devotees, and Daughters of God*. OUP. Via `ind_orr_temple_women.md`, which has pages.
- Narayanan 1994; Venkatesan 2010; Carman and Narayanan 1989; Ramanujan 1973; Ben-Herut 2018; Goodall 2018; Pechilis 2012; Zwilling and Sweet 2000. Via the repo notes, as cited.
- Boechari and Wibowo 1985/86; Zoetmulder 1982 (OJED); Bulbeck and Caldwell 2000. Via `south_reading_list.md`.
- Zwilling, L., and M. J. Sweet. 1996. "'Like a City Ablaze': The Third Sex and the Creation of Sexuality in Jain Religious Literature." *Journal of the History of Sexuality* 6.3: 359–384. Existence confirmed; *not read*.
- Gornall, Alastair. 2020. *Rewriting Buddhism: Pali Literature and Monastic Reform in Sri Lanka, 1157–1270*. UCL Press (OA). *Not read*; existence and topic confirmed.
- Harris, Peter (trans.). 2007. Zhou Daguan, *A Record of Cambodia*. Silkworm. Secondary summary only; page *unverified*.
- Bhāratayuddha date (6 Sept 1157, Mpu Sĕḍah, Jayabhaya): secondary (Wikipedia, after Supomo); *verify* in Supomo 1993.
- Ta Prohm (1186) dancer counts: secondary (soundsofangkor.org); *verify* in Cœdès's edition of the stele.
- Rāmānuja chronology and the "Tiruppāvai Jīyar" epithet: secondary and devotional (Wikipedia; ibiblio SriPedia); *unverified*.
- CK3 1.20 game files: `history/titles/k_tamilakam.txt`, `history/provinces/k_tamilakam.txt`, `history/characters/{tamil,telugu}.txt`, `common/landed_titles/00_landed_titles.txt`.
