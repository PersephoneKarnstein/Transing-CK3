# Arms and faith icons

Arms for the six starting characters (so the bookmark's character selector shows a banner, not a black one) and faith icons for the five faiths that still use vanilla placeholders. Arms live in `common/coat_of_arms/coat_of_arms/tm_coas.txt`.

## Status

| Faith | Character | Arms key | Design | In the mod | Shows in the selector |
|---|---|---|---|---|---|
| Adelphai Dorleyaiou | Theia Beatrike | `d_tm_mother_house` (title); her dynasty *of Dorylaion* points at it | The user's: gold falcon on a white roundel, on purple (200 px, 563 instances) | Yes | Should; not yet seen in game |
| Bædling | Steinn | `c_gutland` (replacing vanilla's ram and its Norse variant `c_gutland_norse`, the user's choice); dynasty `825` links to it | Red Gotland whirl (`ce_gotland_spiral`) on blue, filling 90% of the field (scale 1.28: the whirl fills 70% of its texture; at 0.7 it read as a red dot) | Yes | Should; not yet seen in game |
| Yutai Dao | Xun | `2003011` (dynasty Suo). His map banner keeps Guasha's vanilla seal, by choice | The user's: white-and-black tiger on green (250 px, 1,588 instances). Every Suo character carries it | Yes | Should (Xun has a dynasty); not yet seen in game |
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

## Sources

`research/byz_roller_god_the_mother.md` (iconography), `research/jud_friedenberg_medieval_jewish_seals.md`, `research/waf_brett_smith_bamana.md` (colour and cloth), `research/waf_conrad_conde_sunjata.md`, `research/cn_cahill_divine_traces.md`, `research/norse_price_viking_way.md`, `research/norse_gardela_bonding_pentz_norse_sorceress.md`, `research/byz_bury_kletorologion.md`, `research/cn_despeux_kohn_women_daoism.md`, `research/waf_ibn_battuta_mali.md`; Zhang Wanfu, 三洞法服科戒文 (Wikisource); Gotlands Museum, *Gotlandic Picture Stones* (online); the *Jewish Encyclopedia*, "Arles" and "Badge".
