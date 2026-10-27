# Arms and faith icons

Arms for the six starting characters (so the bookmark's character selector shows a banner, not a black one) and faith icons for the five faiths that still use vanilla placeholders. Arms live in `common/coat_of_arms/coat_of_arms/tm_coas.txt`.

## Status

| Faith | Character | Arms key | Design | In the mod | Shows in the selector |
|---|---|---|---|---|---|
| Adelphai Dorleyaiou | Theia Beatrike | `d_tm_mother_house` (title); her dynasty *of Dorylaion* points at it | The user's: gold falcon on a white roundel, on purple (200 px, 563 instances) | Yes | Should; not yet seen in game |
| Bædling | Steinunn (Steinn's elder sister, from 2026-10-23) | `c_gutland` (replacing vanilla's ram and its Norse variant `c_gutland_norse`, the user's choice); dynasty `825` (Gute) links to it | Red Gotland whirl (`ce_gotland_spiral`) on blue, filling 90% of the field (scale 1.28: the whirl fills 70% of its texture; at 0.7 it read as a red dot) | Yes | Should; not yet seen in game |
| Yutai Dao | Huijing (replaces Xun, 2026-10-23) | `tm_dyn_jade_embryo`, her one-person dynasty *of the Jade Embryo*; `house_tm_jade_embryo` links to it. The map banner in the selector shows the tiger too: `d_guasha`'s default arms are the tiger, and the start script sets vanilla's seal back on the title (`tm_d_guasha_vanilla`), so in play Guasha keeps its seal (user, 2026-10-23). Suo (2003011) keeps vanilla's arms | The user's: white-and-black tiger on green (250 px, 1,588 instances) | Yes | Should; not yet seen in game |
| Ha-Nehpakhot | Bonadonna | `d_laamp_tm_lamp` (camp title); her dynasty *of the Lamp* points at it | A seal of the Midi, white on blue: ✶ מנשים באהל תבורך (Judges 5:24) round the rim, a portcullis in the field (300 px, 1,335 instances; drawing `~/Downloads/ck3_banner_examples/hebrew/6_bonadonna_verse.png`) | Yes | Should; not yet seen in game (the camp's own arms do not show there) |
| Mālai | Cantiradevi | `c_candragiri` (her bookmark county; vanilla defines none); her house and dynasty link to it | The user's: a garland of tulsi and jasmine on green (200 px, 2,875 instances) | Yes | Should; not yet seen in game |
| Badenya | Djeneba | `c_sibi_mali` (her bookmark county; vanilla defines none); her house and dynasty link to it | The user's: a gold buffalo on black (200 px, 552 instances) | Yes | Should; not yet seen in game |

Faith icons: only Dorleyaiou has its own (`gfx/interface/icons/faith/tm_dorleyaian.dds`, the user's). The other five use vanilla placeholders (`common/religion/faith_types/tm_faith_types.txt`).

## The lowborn leaders: one-person dynasties (decided 2026-10-23)

Theia, Cantiradevi, Djeneba and Bonadonna were lowborn, so the selector had no arms to show (a landless camp's arms do not show there either). Each now has a one-person dynasty and house, as vanilla does for famous figures who would otherwise be lowborn (Hildegard "von Bingen", Maimonides "ben Maimon": `game/common/dynasties/05_historical_character_dynasties.txt`, `game/common/dynasty_houses/99_historical_character_houses.txt`). Named for places and institutions, never a real lineage (Mande clan names are living lineages):

| Character | Dynasty and house | Shows as | Arms |
|---|---|---|---|
| Theia Beatrike | `tm_dyn_dorylaion`, `house_tm_dorylaion` | Theia of Dorylaion | `d_tm_mother_house` |
| Cantiradevi | `tm_dyn_temple_street`, `house_tm_temple_street` | Cantiradevi of the Temple Street | `c_candragiri` |
| Djeneba | `tm_dyn_do`, `house_tm_do` | Djeneba of Do (the buffalo woman's land) | `c_sibi_mali` |
| Bonadonna | `tm_dyn_lamp`, `house_tm_lamp` | Bonadonna of the Lamp | `d_laamp_tm_lamp` |
| Huijing (added 2026-10-23) | `tm_dyn_jade_embryo`, `house_tm_jade_embryo` | Huijing of the Jade Embryo | the tiger (`tm_dyn_jade_embryo`) |

Steinunn needs none: she is of Steinn's dynasty, Gute (825), whose arms link to Gotland's. Huijing replaces the vanilla duke Xun, a historical man (Suo Xun, later military governor at Dunhuang), whom the mod no longer converts; she raises his son Chengxun as her ward and heir.

Files: `common/dynasties/tm_dynasties.txt`, `common/dynasty_houses/tm_dynasty_houses.txt`, `localization/english/tm_dynasties_l_english.yml`; the characters' `dynasty_house =` lines in `history/characters/tm_characters.txt`; each leader's `dynasty`/`dynasty_house` and `dynasty_splendor_level` in `common/bookmarks/bookmarks/tm_bookmarks.txt`; the arms links at the end of `tm_coas.txt`. They are no longer lowborn, so their children or heirs of the blood carry the name and arms. The stand-ins the start script makes at later start dates stay lowborn (`dynasty = none`).

## How the selector picks a banner

The bookmark screen shows arms in two places (checked in game, 2026-10-23):

- **The banner beside each name on the map** is the arms of the bookmark entry's `title` (`coa_realm_bookmark` in `game/gui/shared/coat_of_arms.gui`: `GetLandedTitleTemplate.GetCoA`), framed by tier. Dynasty and house play no part, except for a landless adventurer (`coa_adventurer_bookmark`), whose banner shows her house's arms. So Theia shows the Mother House's falcon and Bonadonna her house's seal, while Steinn shows Gotland's ram and Xun Guasha's seal (vanilla title arms), and Cantiradevi and Djeneba show black (their counties, `c_candragiri` and `c_sibi_mali`, have no arms defined).
- **The panel for the selected character** (`coa_dynasty_bookmark`) shows the house's arms, else the dynasty's. The dynasty or house comes from the bookmark entry (`dynasty = …` or `dynasty_house = …`, with `dynasty_splendor_level`), not from history; without them the name line says "Lowborn". The history must agree, or xTiger warns.
- Arms the game generates in play (for titles and dynasties with none defined) do not exist on this screen: they show black.

The banner is `game/gfx/interface/frontend/mask_coa_flag.dds`, 720 × 720: a square of cloth with frayed edges. Only the outer 10–20 px are lost, so the whole square is usable; keep the main shape within the middle 80%. The same arms also appear as shields and other shapes in play, which crop more, so centred designs are safest.

## Making arms from a drawing

**Draw:** a square image, flat colours (no shading or anti-aliasing), corners in the field colour. Any size; it is scaled down.

**Convert:** `python3 tools/img2coa.py design.png <key> 200 out.txt [--disc]`, then paste `out.txt` into `tm_coas.txt` with a comment. `<key>` is the title (`d_…`, `c_…`) or the dynasty id.
- It snaps the image to its few main colours, makes the corner colour the field, and draws the rest as rectangles of `ce_block_02`: runs of same-coloured pixels along each row, merged with identical runs in the rows below. Rectangles overlap their neighbours by 0.08 px, so no hairline seams show.
- Transparent pixels (an export's border) are flattened onto the image's main colour. Colours closer than 40 RGB units merge, so keep deliberate shades at least that far apart.
- `--disc`: the second colour is a plain disc behind the device; it is drawn with vanilla `ce_circle` instead of strips. Its edge is slightly soft.
- Resolution: 200 px suits a bold design (Dorleyaiou's falcon: 563 instances); 250 px holds fine detail better (Yutai's tiger: 1,588 at 250, 1,280 at 200). The generator's one-square-per-pixel output of the falcon was 4,722 at 100 px.

**The generator** ([Perondas/Ck3-Coa-Generator](https://github.com/Perondas/Ck3-Coa-Generator)) also works, but it needs a square image (it places each pixel at x/width and y/width, so a tall image runs off the bottom), turns every pixel into its own instance (its README warns that over 100 px slows the game), and keeps anti-aliasing shades as extra colours. Its output is the in-game designer's format.

**Previews:** `~/Downloads/ck3_banner_examples/` (outside the repo) has a square template of the banner mask, the mask itself, and previews of the suggested designs below, as squares and in the selector's cloth.

**Emblem colours:** vanilla emblems have three colour slots: the body is `color1`, the green-channel details (claws, beak) `color2`, the red-channel details (eyes) `color3`; the blue channel is shading. Colours are named (`common/named_colors/default_colors.txt`; heraldic gold is `yellow`) or `rgb { r g b }`.

## Hebrew legends (Ha-Nehpakhot)

From Friedenberg, *Medieval Jewish Seals from Europe* (1987), read from the page images (the Hebrew is not in the PDF's text layer). Copy the Hebrew below exactly; it is transcribed from the book. Note on the research: `research/jud_friedenberg_medieval_jewish_seals.md` §5.

**How a seal of the Midi is lettered** (Nos. 19, 21, 26, 27, Narbonne and Provence, 13th century):
- The legend runs round the edge, starting with a small star. **Never a cross** with Hebrew: "these are never present, however, when the seal has a Hebrew inscription" (p. 45).
- **Name, then *bar* (son of) or *bat* (daughter of), then the father's name, then a pious contraction** saying whether he is alive or dead (pp. 45–47). Examples: טובי בר יצחק ז״ל, "Tobiah son of Isaac, his memory be for a blessing" (No. 26); קלונימוס בר שלמה יצ״ו, "Kalonymos son of Solomon, may his Rock and redeemer guard him" (No. 27).
- Often a **second face or second legend in the vernacular**: "S' MIELET DEL PORTAL", "Seal of Mielet of the Portal" (No. 21); "S': MOVMET IVDEV D'NERBO", "Seal of Moumet the Jew of Narbonne" (No. 19). *S'* is *sigillum*, seal.
- The contractions (pp. 46–47): father alive: יצ״ו = ישמרהו צורו וגואלו, "may his Rock and his redeemer guard him" (the most common); also י״א, ש״י. Father dead: ז״ל = זכרונו לברכה, "his memory be for a blessing"; נ״ע = נוחו עדן, "may his soul rest in Eden".

**Women's seals and rings:**
- Dulcie of the Portal (No. 23, Narbonne): Latin only, "+ S : DVLCIE : DE PORTALI". The cross and the lack of Hebrew are unusual for the Midi.
- Dulce (No. 64, Teruel ring): her name alone, דולסה.
- Jochebed (No. 62, Teruel ring): בשם יוכבד, "in the name of Jochebed".
- Astruga (No. 65, Barcelona ring, 13th–14th c.): three lines, מ׳ ב׳ / אשתרוגה / ת׳, which is מנשים באהל אשתרוגה תבורך, "Above women in the tent Astruga be blessed": Judges 5:24 with her name in Jael's place.

**Recommendations:**
1. **Faith icon: Astruga's form.** Her ring abbreviates Judges 5:24 round her name: מ׳ ב׳ on top, the name in the middle, ת׳ below. For the faith rather than one woman, write the verse's own words out on three lines instead: מנשים / באהל / תבורך, "above women in the tent / she shall be blessed". This is the only legend in the book that praises a woman; the ring's form is attested, the version without a name is design.
2. **Bonadonna's banner, if it carries lettering:** her own seal on the Midi pattern, בונדונה בת [father] [contraction], with a vernacular face "S' BONADONA …". **Two things are missing, and should not be guessed:** her father's name (history gives none) and an attested medieval Hebrew spelling of *Bonadonna*. The name is attested in Latin at Manosque in 1338 (Shatzmiller, p. 357), but no source read so far spells it in Hebrew. A Provençal Hebrew document or a Hebrew reader should settle it.
3. **Legibility:** a legend round a 720 px banner gives letters of about 25 px, but `tools/img2coa.py` at 200 px makes them about 7 strips tall, which will not read. For lettering, convert at 400 px or more (more instances), or keep the lettering to the faith icon and leave the banner to the portal.

**Examples** (`~/Downloads/ck3_banner_examples/hebrew/`, 720 px squares in flat blue and white, ready to edit and convert; `overview.png` shows all five):
1. `1_astruga_ring_as_printed.png`: Astruga's ring as Friedenberg prints it, to show the three-line layout.
2. `2_faith_icon_verse.png`: the faith's version, the verse on three lines.
3. `3_midi_seal_no27_as_printed.png`: a round seal of the Midi, with No. 27's attested legend קלונימוס בר שלמה יצ״ו round a portcullis, to show the layout.
4. `4_bonadonna_template_gaps.png`: Bonadonna's seal with dashed gaps for the two unknowns: [name] בת [father] יצ״ו.
5. `5_vernacular_face.png`: the vernacular face, S' BONADONA.

In the round ones the legend starts at a small star at the top. The Hebrew runs anticlockwise, which is right to left with the letter tops toward the rim; the Latin runs clockwise. The book's photographs are too small to confirm the Hebrew direction letter by letter. The fonts are Arial Hebrew and Times New Roman Bold, chosen for legibility, not as period letterforms.

## Background: suggestions by faith

These were suggestions before the user's redesigns; they stand as research. Banners use vanilla emblems, each one looked at; faith icons need new art.

| Faith | Suggested banner | Suggested faith icon | Avoid |
|---|---|---|---|
| Adelphai Dorleyaiou | A falcon (`ce_falcon`). Matar's most frequent attribute in central Phrygia is the hawk or falcon; the lion is secondary there (Roller 1999, p. 108) | Has the user's icon. An alternative: the goddess's doorway, a facade niche with a hawk (p. 97) | Pine and Attis (self-castration and death); tympanum, mural crown, lion chariot (Greek and Roman Meter); double-headed eagle, Chi-Rho |
| Bædling | (implemented) The Gotland whirl, the disc of Gotland's picture stones; or `ce_norse_longship_gotland` | A miniature chair pendant, the high seat (Price 2019, pp. 120–25); or the iron staff with a distaff-like cage (Gardeła, p. 422) | Valknut, Vegvísir and other symbols taken up by white-supremacist "Odinism"; red, black and white together (the Reich colours); the whirl black on white or white on black (it then reads as the "Black Sun") |
| Yutai Dao | A white tiger (`ce_tiger`): the Queen Mother of the West's envoy (Cahill, p. 53). Neutral for the non-Yutai Suo: `ce_seal_cloud` | The Queen Mother's *sheng* headdress (patron of Daoist women, Cahill p. 43); or the embryo in the tripod-furnace (Wang Mu) | The yin-yang swirl (Song or later); Mogao's apsaras (Buddhist); reddish yellow (赤黃, imperial) |
| Ha-Nehpakhot | A portal with a portcullis (`ce_portcullis`), after the seal of Dulcie of the Portal, Narbonne (Friedenberg No. 23) | A round seal with a Hebrew legend from Judges 5:24, "blessed shall she be above women in the tent", as on Astruga's ring (No. 65). Needs a Hebrew-literate check | The Jew's hat and the *rouelle* (imposed badges); the hexagram (late); the crescent and star (period-true, but reads as Islamic in game); the arms of Arles; any yellow, and red with white or with yellow (the badge colours). The menorah is not on medieval seals (p. 28), though it is fair for an icon |
| Mālai | A flower garland, which needs art (vanilla's wreath is laurel); `ce_lotus_flower` as a stand-in | A closed garland: "the garland worn and given" | Āṇṭāḷ's parrot and the Srivilliputtur tower (later temple; the tower is the modern Tamil Nadu emblem); the Pallava bull, Chola tiger, Pandya fish; saffron (the modern Hindu banner) |
| Badenya | A buffalo head (`ce_bull_head` as a stand-in): Do Kamissa, the sister denied her share (Conrad and Condé, ll. 1254–61, 3206–17) | The calabash, the women's instrument (Jansen, p. 184) and the vessel of welcome (Ibn Baṭṭūṭa, p. 386); or the smiths' iron staff (Bulman) | Mud-cloth patterns and rust red (excision cloth: Brett-Smith fig. 12); a mainly white banner; red with gold (Mansa Musa's banner, and the modern Mali flag); vanilla's Akan Adinkra emblems; Komo masks; *ci wara*; the buffalo as arms of the Condé, a living lineage |

## Background: colours

The faiths' map colours (`tm_rite_types.txt`) were placeholders with no rationale: Dorleyaiou's pink is the trans flag's #F5A9B8, Bædling's violet came with it. The colours below are grounded in each faith's antecedent. "Attested" means a period source gives the colours for the antecedent, not for a banner; arranging them as arms is design.

| Faith | Suggested | Evidence | Alternatives |
|---|---|---|---|
| Adelphai Dorleyaiou | White, gold, purple | **Attested, 899.** The dress of the palace chamber: the *primikerios* in a "white tunic with gold-embroidered shoulders", the *koubikoularios* in a "tunic edged with purple" (Philotheos in Bury 1911, p. 122; `byz_bury_kletorologion.md`). The Women's Chamber makes this the faith's world. The suggestion kept purple to a trim, since purple was the emperor's colour; the user's design uses it as the field | Saffron field, white falcon (the galli's *crocota*: hostile Roman sources, plausible). Not pavonazzetto: its veins are "the blood of Attis" (Roller, p. 342) |
| Bædling | Blue field, red whirl (implemented) | **Attested, c. 980.** The Fyrkat 4 vǫlva's foot-length blue wool garment with red cords (Gardeła, Bønding and Pentz 2023, pp. 297, 329–36). The picture stones' own colours are lost: "the red or black paint you can see on many stones today, was applied no earlier than in the 20th century" (Gotlands Museum) | Dark blue field, white whirl (the saga vǫlva's dark cloak and white catskin; 13th-century text) |
| Yutai Dao | Purple field, white tiger, blue-green border | **Attested, c. 712.** Zhang Wanfu's rules for vestments give an ordained woman of the high (*dongzhen*) grade 「紫紗」 purple gauze and 「青紗之裙」 a blue-green skirt (*Sandong fafu kejie wen*). White is the West and the Metal Mother (Cahill, pp. 39–40) | Yellow field, white tiger outlined black: the common grades' yellow robe and black cap (「黃裙」「玄冠」), and Song Yuxian's "yellow linen skirt" (Despeux and Kohn, pp. 114–15). Use an ochre yellow, not the imperial 赤黃 |
| Ha-Nehpakhot | Blue field, white portal | **Plausible.** The thread of blue on white of the *tzitzit*, remembered after *tekhelet* was lost; Maimonides likens it to a clear sky (*Hilkhot Tzitzit* 2:1), and the Mishneh Torah reached Provence by the 1190s. Tallit stripe colours in medieval Provence are not attested | Green field, white portal (green sealing wax: Friedenberg says seal wax was "vermilion for the red seals and verdigris for the green"; red is ruled out here) |
| Mālai | Green field, white garland | **Attested in the poems.** Nārāyaṇa "crowned with fragrant tulasi" (*Tiruppāvai* 10) and "buds of jasmine" (*Nācciyār Tirumoḻi* 9.2). The poems name no flower for her own garland; tulasi for it is hagiography (Govindacharya 1902, p. 44) | Dark blue or purple field (the Lord's colour, *Tiruppāvai* 23, *NT* 9.3); red field with a yellow garland (red lotus, and Śiva's golden *koṉṟai*: the faith crosses both temples) |
| Badenya | Black field, gold buffalo | **Gold attested** (al-Bakrī, 1068; Ibn Baṭṭūṭa: the golden bird on the king's parasol, p. 406; the bard paid in gold, p. 412). **Black is ethnographic** (Brett-Smith, 20th century), projected back: black is life, white is death and the spirits (pp. 132–33) | Indigo field, gold or white buffalo (indigo cloth from the Bandiagara caves, 11th–12th century: archaeology, but Tellem, not Mande) |

**Guardrail colours:** for Ha-Nehpakhot, no yellow, and no red with white or with yellow (the Arles badge was yellow; the French one later red and white); for Bædling, no red, black and white together; for Badenya, no rust red and no red with gold; for Mālai, no saffron; for Yutai, no imperial reddish yellow.

## The v2 faiths (planned): suggestions

Researched 2026-10-26 for the two faiths planned for the 1066 start (`docs/TODO.md`, *Version 2.0.0 plan*; designs in `research/v2/japan_design.md` and `research/v2/witch_design.md`). Nothing is built. Grades as above. Previews, 720 px squares and in the selector's cloth, are in `~/Downloads/ck3_banner_examples/v2/`.

**Chosen (user, 2026-10-26).**
- **Imayō no Ie:** the gold `ce_kamon_moon`, tilted, on indigo, as in the preview `japan_moon_gold_on_indigo_square.png`.
- **The Good Ladies:** the second choice below, as drawn by the user (`~/Downloads/good women.png`): a white field, two blue bars in base, and a gold wicker basket with a handle, holding three brown loaves. The basket is modelled on the one in the arms of Cardinal Joachim Meisner. The key, which the table below gives as the first suggestion, is dropped from the banner. The table's *hera*-key notes stay as research.

### Suggestions

| Faith | Suggested banner | Suggested faith icon | Avoid |
|---|---|---|---|
| Imayō no Ie | **A moon on the houses' parasols** (`ce_kamon_moon`, gold, tilted about 25°, scale 0.62, on indigo). **Attested object:** parasols "decorated with figures of moons" at Eguchi in 1031 (*Eiga monogatari* bk 31, via G 22, n. 50). **Plausible link:** Masafusa's "half-moon emblems" (*Yūjoki*, G 20) rest on Ōsone's tentative emendation, which Goodwin ties to the Eiga moons (G 159–60 n. 36). **Design:** the moon as a house badge. No singers' house had a *mon*: in the 12th century *mon* were nobles' marks on carriages. An option: the moon over `ce_waves_04` (the Yodo), but see Notes | **The parasol with a moon** (needs art): the fixed Heian canopy (*kinugasa*, *karakasa*) on a long pole, with a crescent on the canopy. The parasol is **attested** for the boat crew: c. 996 the old women "carrying the parasols and poling the boats" (Yukitoki, G 15); RH 380 *ōgasa kazashi*, "the woman who holds her large parasol" (Kim p. 10). The moon on it is Eiga's (above). Alternative: the small hourglass drum (*tsuzumi*), RH 380 and *Kairaishiki* (Kim pp. 8, 10, 14; G 28) | Any figure, puppet or carved image: Hyakudayū was a carved object (*Yūjoki* 剜, G 19), and kugutsu men worked wooden puppets (Kim p. 13). No doll or porcelain imagery at all. The Edo paper umbrella with ribs and a *janome* ring (it folds only from the late 16th century), fans, cherry blossom, kimono-woman montages. Imperial chrysanthemum (`ce_kamon_chrysanthemum`), paulownia (`ce_kamon_pawlonia*`), the sun (`ce_kamon_sun`) and any **half-disc**, which reads as a rising sun. Real lineages' *mon*: Taira butterfly (`ce_kamon_butterfly`), Minamoto gentian (`ce_kamon_gentian`), Fujiwara wisteria (`ce_kamon_*wisteria*`), and vanilla's own Japanese dynasties: **yellow `ce_kamon_moon` on black is `japanese_funya`**, red `ce_kamon_gessei` (moon and star) is `house_taira_chiba`, `ce_kamon_hat` is `japanese_tomo`, `ce_kamon_commas` (*tomoe*) appears on several. Also the manji, the *shirabyōshi*'s white *suikan* and tall cap (a separate trade the design excludes), and Islamic-looking crescents (`ce_crescent`, `ce_mena_crescent`) |
| The Good Ladies (*bonae dominae*) | **The laid cloth and the *hera*'s key:** a white field (the table linen) with two narrow blue bars in base (the woven bands of a table cloth) and one black iron key (`ce_key`), hung bow up as from a girdle. The cloth is **Attested** in substance (the laid table, William of Auvergne 1230s; Berthold, 13th c.: `witch_hutton_lecouteux.md` §2) and its blue-on-white bands are attested for 14th–15th-c. Italian tables (V&A). The key as the housewife's sign is **Plausible** (Roman, Danish 1241, Norwegian law); the faith's own word for the Lady is *hera*, mistress of a household (*Ysengrimus* II 90). Arranging them as arms is **Design**. Second choice: the same field with a gold bread basket (`ce_basket`; **Design**, abundance) | The morning place at the table: a white cloth with blue bands, a loaf, an **uncovered** jug and cup, and one empty place set. Uncovered vessels are **Attested** (William of Auvergne, `witch_hutton_lecouteux.md` §2 table); food, drink and salt c. 1440 (Ebendorfer, ibid.); the set place is the faith's gate (**Design**, `witch_design.md` §4). Alternative for Lombard cultures: Madonna Oriente's staff with an apple on it (**Attested**, Milan 1384–90; Lecouteux ch. 11, via `witch_hutton_lecouteux.md`). Needs new art either way | Broom, cauldron (vanilla `ce_pot` reads as one), pointed hat, black cat or **black cock**, goat or horned figure, pentagram, any flight. The crescent (`ce_crescent`, `ce_moon`, `ce_crescent_random`): Diana's sign in c. 1400 manuscripts, but it reads as Islam in CK3 and as Wicca's triple moon. The distaff and spindle of Holda (post-medieval folklore, and modern heathenry's Holda). The hunting horn (`ce_horn`: the Wild Hunt, a separate strand, Hutton pp. 164, 171). Chalice (Eucharist), crossed keys and `ce_key_st_peter` (papal; Regensburg; Bremen), crozier, cross, crown or stars of the "Queen of Heaven" (Marian). Blue field with a white key (vanilla `c_worms`). Perchten masks (living custom). The 1451 *Champion des Dames* "vaudoises". Hogwarts-style quartering or beasts |

### Colours

| Faith | Suggested | Evidence | Alternatives |
|---|---|---|---|
| Imayō no Ie | Indigo field (about `rgb { 28 40 78 }`), gold moon | **Gold is attested** as the singers' finery: in 1031 they wore "ornaments of mother-of-pearl and gold or silver lacquer" (*Eiga*, G 22). *Kairaishiki* (c. 1087, hostile) gives kugutsu women "clothes embroidered with golden threads" and "golden hair ornaments" (Kim pp. 13–14). **Indigo is plausible:** *ai* was the common dye and outside the forbidden colours (*kinjiki*). No source gives the houses' colours, and none gives the river a colour. Gold is a metal, not a dye, so the *kinjiki* do not touch it; keep it gold, not the crown prince's orange *ōtan* | Indigo field, white moon (silver lacquer and mother-of-pearl, G 22; Kim p. 14). Green field, gold moon (design; check it against Mālai's green). Not a crimson field: Yukitoki's "crimson boudoirs" (G 16) is the hostile essay's cliché for the trade, and deep scarlet (*kokiake*) is a forbidden colour |
| The Good Ladies | White field, blue bars, black key | **Attested, 14th–15th c., Italy:** Perugia table cloths, "white linen warp and weft" with bands "almost always dyed blue with indigo or woad" (V&A O15355; production 14th–16th c., V&A towel record). Similar cloths are painted on tables from Giotto to Ghirlandaio. **Plausible** for the Rhine: white linen as a household's wealth (it took washing and servants: ikfoundation), and woad was the Rhineland's blue. **Plausible** for the black: keys were iron | White field, blue bars, gold (CK3 `yellow`) basket: bread and plenty, the meaning of Abundia and Satia (`witch_hutton_lecouteux.md` §4). Blue field with a white cloth bar and gold key, if the white field reads too empty in the selector (keep the key gold, not white, to stay clear of Worms) |

**Guardrail colours.** Imayō no Ie: never red with white (the later Taira red and Minamoto white); no gold or yellow moon on black (vanilla's Fun'ya arms); none of the forbidden colours (*kinjiki*: deep purple, deep scarlet, sappanwood, *ōtan*, *kōrozen*); no rouge-and-white-powder palette (the hostile *Kairaishiki*'s line, and it reads as "geisha"); no *kasane* colour sets (no source gives the singers one). The Good Ladies: no blue field with a white key (vanilla Worms, a holy site); no gold and silver keys on red (papal); no black field with a white crescent; no black animal.

### Notes: Imayō no Ie

- **Why the moon.** It is the one image the sources put on the houses' own things: in 1031 the Eguchi singers came to the boats with parasols "decorated with figures of moons" (*Eiga monogatari* bk 31, via Goodwin p. 22 n. 50; the Japanese wording is unchecked). Masafusa's "half-moon emblems" (*Yūjoki*) rest on Ōsone's tentative emendation of 九 to 丸 (Goodwin pp. 20, 159–60 nn. 35–36). The moon also does doctrinal work in the songs: "the Buddha-moon is hidden" (*Ryōjin hishō* 194; Kim p. 83).
- **Mon.** In the 12th century *mon* were nobles' marks on carriages; no source gives a singers' house one, so the badge is design in an attested motif. Vanilla's *kamon* emblems are later in form but right for CK3's Japan.
- **The parasol.** Every boat source has one, from Yukitoki c. 996 to a diary of 1119. Heian parasols were stiff canopies on a long pole; the folding paper umbrella is late 16th century and Edo. The icon art must show the canopy, with no ribs or ring pattern, and say so in the brief (the orientalism note's ban on "paper parasols" is about the Edo object). Vanilla's `ce_parasol` is a South Asian tiered *chatra* and does not fit.
- **Hyakudayū is never drawn.** *Yūjoki* says the singers carved him; no figure of any kind as an emblem (the Japanese faith's no-doll rule).
- **The waves option** (a white moon over `ce_waves_04`) risks a moonlit-river picture; use it only if the plain crescent reads as Islamic in game. Tilt the crescent so it does not copy Fun'ya's upright moon, and check it at shield size.
- Later picture evidence, flagged as later: the 14th-century *Hōnen shōnin gyōjō ezu* shows a Muro boat with a drummer, a parasol-bearer and a rower.

### Notes: the Good Ladies

- **No medieval picture of the Ladies exists**, so the arms come from what the texts describe, a **table**: William of Auvergne (1230s) on Abundia and Satia touching only **uncovered** vessels; Berthold of Regensburg's table "for the blessed ladies"; an early-13th-century list tying the laid table to "Frau Holda" (unchecked against the edition); salt c. 1440 (Ebendorfer). The first image of a women's night company is the accusers' own, the 1451 *Champion des Dames* "vaudoises" on a broom: avoid it.
- **The key.** The faith calls the Lady *hera*, mistress of a household (*Ysengrimus* II 90). The key as the mistress's sign is legal and Plausible (Cicero, *Phil.* 2.69; Danish law of 1241; Norwegian law), but Nancy Marie Brown warns that the Viking "housewife's keys" are partly a Victorian idea. In CK3 keys mean St Peter: use plain `ce_key`, one key, black iron, **bow up** as from a girdle (Peter's key is shown wards up); never `ce_key_st_peter`, never white on blue.
- **Holda's distaff is late.** No medieval source ties Holda or Percht to spinning; it is folklore collected from 1835 on (Mencej), and the distaff is the badge of present-day heathen Holda devotion, a living community. Avoid.
- **Madonna Oriente's staff with an apple** (Milan, 1384–90) is the one object the Lady herself is said to hold; keep it for Lombard event art or an alternative icon, never without the apple (alone it reads as a crozier).
- **The crescent** (Diana's in c. 1400 manuscripts) reads as Islamic in CK3 and as Wicca's triple moon: avoid for the Ladies.
- **Open check (consolidation):** a white field with blue bars reads at a glance like a tallit or the flag of Israel, and blue-on-white is Ha-Nehpakhot's colour (the thread of blue). The chosen design's gold basket weakens that reading, but check it at shield size in game; if it still reads that way, use the alternative (blue field, white cloth bar, gold key) or unbleached-linen brown bars.

## Sources

`research/byz_roller_god_the_mother.md` (iconography), `research/jud_friedenberg_medieval_jewish_seals.md`, `research/waf_brett_smith_bamana.md` (colour and cloth), `research/waf_conrad_conde_sunjata.md`, `research/cn_cahill_divine_traces.md`, `research/norse_price_viking_way.md`, `research/norse_gardela_bonding_pentz_norse_sorceress.md`, `research/byz_bury_kletorologion.md`, `research/cn_despeux_kohn_women_daoism.md`, `research/waf_ibn_battuta_mali.md`; Zhang Wanfu, 三洞法服科戒文 (Wikisource); Gotlands Museum, *Gotlandic Picture Stones* (online); the *Jewish Encyclopedia*, "Arles" and "Badge".

For the v2 faiths: Goodwin 2007, Kim 1994 and Kwon 1986 (`research/v2/japan_*.md`); Shinma Mizuo on the *Hōnen shōnin gyōjō ezu* (Hokkaidō University repository); `research/v2/witch_hutton_lecouteux.md`, `witch_ysengrimus.md`, `witch_papers_and_timeline.md`; V&A records of Perugia table linen (O15355); Mencej on Holda's late spinning lore; Nancy Marie Brown on Viking keys. Full working notes, with URLs and the vanilla emblems inspected, were kept outside the repo.
