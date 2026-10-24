# TODO

In-game test scenarios for playtesters are in [TO-TEST.md](TO-TEST.md); the "untested" items below are covered there.

## Art
- [ ] **Commission official-looking art for all icons** (user, 2026-10-14). Interim user-drawn icons installed 2026-10-14: faith/rite `tm_dorleyaian`, traits `tm_transgender`, `tm_washout`; the final set should match vanilla CK3 style. 15 icons, specs in the build notes and `~/Downloads/ck3_icon_examples/` for reference:
  - faith/rite: `gfx/interface/icons/faith/tm_dorleyaian.dds` 100×100
  - tenets: `gfx/interface/icons/faith_tenets/tenet_tm_{day_of_blood,daughters_chosen,sisterhood}.dds` 260×400
  - doctrines: `gfx/interface/icons/faith_doctrines/tm_knife_{grandmother,aunt_bea,gift_alone}.dds`, `tm_body_{aristotelian,galenic}.dds` 120×120
  - doctrine groups: `gfx/interface/icons/faith_doctrine_groups/doctrine_tm_{knife,body}.dds` 120×120
  - traits: `gfx/interface/icons/traits/tm_{transgender,daughter_of_the_knife,novice,washout}.dds` 120×120
  - all DDS, uncompressed B8G8R8A8, transparent background
- [ ] Event pictures for the Rite of the Knife, washout, Sister-Making and the flavour "achievement" events.
- [ ] When art lands: point faith/rite/tenets/doctrines at the new files and delete placeholder `icon =` lines in `common/traits/tm_traits.txt`.

## Content
- [x] Religious head title: d_tm_mother_house, given to Theia Beatrike at game start (tm_on_game_start). Test: she appears as head of faith; her landless government is sensible.
- [x] `name_list_kybeline` (86 female, 148 male, 22 dynasties; attested names cited per report).
- [x] New Personal History rename event (untested in-game).
- [x] Dorley path: prisoner interaction, intake trigger, sponsor chain, levers, washout (untested in-game).
- [x] Sister-Making relation + interaction; Rescue the Daughters CB (untested in-game).
- [x] Flavour "achievement" events (`tm_ach`, docs/wave3/achievements.md). The two-line hook in `tm_take_the_knife_effect` is in; untested in game.
- [ ] Compatibility note for the README: the mod overrides vanilla `allowed_to_marry_same_sex_trigger` (zz_tm_marriage_override.txt).
- [ ] In-game load test with `-develop`; CK3 Tiger pass.

## Validation notes
- CK3 Tiger v1.19.0 (built from source 2026-10-14) lags the 1.20 religion schema. Expected false positives on this mod: unknown `doctrine_group_type`/`index`/`divergence`/`special_parameters`, list-form doctrine parameters, `rite_has_doctrine`, the character→`rite` link, holy-site `county_holder_character_modifier`/`faith_character_modifier`, and faiths "not defined in common/religion/religions" (1.20 uses faith_types). All are documented in the installed 1.20 `.info` files. Remaining real warnings: missing art only.

## Matriline continuity (added 2026-10-17)
- [ ] In-game test: Take as Daughter on a courtier, a ward, an adult guest, and a girl with landed kin.
- [ ] In-game test: Petition for a Refuge, then Send to the Mother House; check all five options and the adopt follow-up.
- [ ] In-game test: re-embody an adopted daughter and confirm she is still her adoptive mother's child and heir.
- [ ] In-game test: re-embody a mother and confirm her children still list her as parent (raw `adopt` on children who already have two parents is unverified).
- [ ] Tune arrival chance: base 6 / Mother House +6 / daughter courtier +3 / refuge +15 per year.
- [ ] With the re-embodiment rule off, daughters keep male bodies and cannot inherit under female-only law. Decide whether that rule should also relax the gender law.

## Branch faiths, stage 1 (added 2026-10-18)
Built: shared daughter trigger and per-faith daughter traits; Bæddel faith (Gotland) with the seiðr gate; Way of the Jade Embryo (Dunhuang) with the ten-month gestation gate; arrivals raise by whichever gate the ruler's rite keeps.
- [ ] In-game test: new game; both faiths present at Gotland and Shazhou; both selectable in the Ruler Designer.
- [ ] In-game test: Go Under the High Seat as a Marked man, success and failure; naming; the Before the Thing declaration on the new body.
- [ ] In-game test: Gestate the Jade Embryo through all four events, including a lost embryo and a restart.
- [ ] Check the weighted random_list modifiers that add learning or diplomacy compute as intended.
- [ ] Commission icons: two faith icons, two daughter traits.

## Serano / Raha & van der Drift / Sanders revisions (added 2026-10-18, untested in-game)
- [ ] Declare Before Witnesses: name kept through each gate, with and without re-embodiment (`change_first_name = { template_character }` on a dead old body is unverified)
- [ ] Embryo trials: delay re-fires the same trial; gestating modifier refreshes; "set it down" clears state
- [ ] Found a Sisters' House: Elder Sister chosen, term expires at 5 years, strain rises/falls, burnout (0020), split (0030), tend-you (0040)
- [ ] Hand a House county to another faith: 0050 fires once per lord; closing sends sisters to another House or the pool
- [ ] Old saves: house variable `tm_refuge` migrates to the capital county
- [ ] The Sisters Choose: law appears for duchy+ rulers of the faiths; electors and candidates as intended; Tiger flags the law/election files as unknown fields (1.20 format lag, same structure as vanilla)
- [ ] Friend of the House arrival (0004); turned-away arrivals reach another House

## Norse reading revisions (added 2026-10-18, untested in-game)
- [ ] Seiðr chain 0010 → 0011 → 0001: scopes tm_volva / tm_host carry through; travelling völva created when no daughter of seidr at court; feast gold taken from host
- [ ] Winter völva visit (0020): sitting for a courtier runs the chain on the courtier
- [ ] Teach the Warding Songs on a daughter and a ward
- [ ] Níðhöggr shows as the Bædling devil; feminised names apply (vanilla Norse name keys)

## Stage 2 inputs from the Norse reading
- [ ] Sorcery law era arc (conversion examples; church outlawry 1100–1300; death penalty Norway c. 1300, Sweden c. 1350), rare dated trials (Óláfr Tryggvason; Bergen 1324–25; Kirkjubær 1343; Greenland 1407) (Mitchell)
- [ ] "Six Housewives" compurgation; women's suits carried by a friend of the House; dress clause needs a powerful prosecutor (Mitchell; Jochens). Six housewives built in the outlawry suit (`tm_bae2.0101`, wave 3); the friend of the House carrying a suit is not.
- [ ] Pour the Cup: end a flyting / first cup / inheritance toast at the high seat (Damico; Evans & Hancock)
- [ ] Events: "They Say He Keeps Seiðmenn" (Tolley); "Weave the Warding Shirt" (Jochens); English reaction text, Wulfstan 1014 (Damico)
- [x] Insult duel: 3 rounds, charges checked against real traits, owning the word strongest, stakes by witnesses and venue (Lögberg doubles); Raise the Níð-Pole scheme (Clover; Meulengracht Sørensen; Grágás)
- [ ] Feud ledger, Offer Bót compensation, fostering to seal a settlement (Miller). Specified in docs/wave3/baedling.md §2, not built.
- [x] Outlawry: lesser (life-ring, three winters) and full; three endings: time, settlement, the war's pardon, the high seat (Grágás; Ahola; `tm_bae2`, wave 3). Not built: reprieve by killing outlaws (K §110).
- [x] Dress clause as a Christian-era / law pressure; covers weapon-bearing women (Grágás; outlawry suit from 1100 at Christian Norse courts, `tm_bae2`, wave 3)
- [ ] Holy-site lore: York (Eiríkr's 80 seiðmenn, Gunnhildr), Trondheim (Þorgerðr Hǫlgabrúðr), Kyiv (armed women among the Rus' dead, 971) (Price)
- [ ] Eleanor Rykener event; female-king title keys; `secret_tm_sister` (medtrans notes)

## Byzantine reading revisions (added 2026-10-18, untested in-game)
- [ ] Two-day knife rite (0001 → 0004)
- [ ] Court offices appear for Dorleyite dukes+, valid holders as intended; the lifestyle-xp modifier names (vanilla pattern) load
- [ ] Pepouza holy site in c_lydia / b_sebaste
- [ ] Protectress named at founding, passes on death; Elder Sister lot (ordered_courtier max 3 + random_in_list)
- [ ] Foster as Daughter; Take as Daughter half price for one's own foster-daughter
- [ ] Name a Companion (Mother of Mothers only, max 7)
- [ ] tm_byz.0001 answers per wing; suppression ladder 0010→0012 under a non-Dorley Christian liege, faster after 1081
- [ ] Islamic triggered opinion (parameter islamic_syncretic_recipient on the observer); tm_isl.0001 / 0002

## Stage 2 inputs from the Byzantine reading
- [x] Liudprand's four children (949) and the Emperor halts at Dorylaion (`tm_byzr`)
- [x] Events: Ignatios returns as patriarch (867); Tarsus boy-train with options per knife house; Steward at the Gate; Athos closed to eunuchs (1083) (`tm_dl2`, wave 3)
- [x] Psellos's "feminine nature": The Consul's Letter, 1063–1078 (`tm_dl2.0060`; dates from Jeffreys and Lauxtermann 2017)
- [ ] Abbasid event pack: the jester, the beard plucked overnight, the barber sent to humiliate a prince (Rowson)
- [x] Galenic splinter rite: Theophylact's *In Defence of Eunuchs* as its book (`tm_dl2`)
- [ ] Verify the Galen renderings in byz_galen_on_semen.md against De Lacy (CMG V 3,1)

## China reading revisions (added 2026-10-18, untested in-game)
- [ ] Embryo chain with the new month-6 options and the ghost-fetus event (0013)
- [ ] Queen Mother of the West shows as the Way's high god; Southern Marchmount holy site at c_hengzhou
- [ ] Temple society dues at births and deaths; righteous store loan and repayment; name-panel; confiscation waves
- [ ] Prodigy in the Prefecture; Ordain by Special Edict; Relight the Shenquan Abbey; Huang Lingwei rescript (882–900)
- [ ] Eastern-faith triggered opinion (parameter eastern_syncretic_recipient)

## Stage 2 inputs from the China reading
- [ ] Palace faction: Shence commanders and Commissioners of Military Affairs (Northern Office) vs scholar-officials (Southern Office); Yang Fugong's adopted sons; the 903 massacre; Song adoption licences and quotas. Built as a small version in wave 3 (`tm_yt2`); tick when tested.
- [ ] Event chains: Xue Xuantong (874–883), Wang Fengxian (d. 886), the abbess of Mo-shan; three routes into the abbeys; Liao Empress Chengtian
- [ ] Regency rules by culture (Song curtain; Liao/Yuan command)

## Ha-Nehpakhot (added 2026-10-19, untested in-game)
- [ ] The Adar window (`tm_is_adar_trigger`, `current_month`), and AI seekers catching it (ai_check_interval 20)
- [ ] The five-part Turning; the persistence variable `tm_turning_prayers`; conversion of Rabbinic and Karaite seekers
- [ ] Before the Elders: county licence `tm_worthies_licence`, *Niddui*; the 1322 gate on the *Touchstone* lines
- [ ] Yearly: the three lamps (0020), a book in Arabic (0030), a Jewish lord's ruling (0040)
- [ ] `triggered_opinion` with a tenet parameter (`tm_turning_gate`) and with `jewish_syncretic_recipient`
- [ ] Seed at Arles: three unlanded sect characters; whether they drift away from Provence

## Stage 2 inputs from the comparanda round (2026-10-19)
- [ ] Ha-Nehpakhot: a source for Provençal Jewish women's names (Iancu; Shatzmiller); the *aylonit* chapter of *Trans Talmud*; community roles from the medieval codes; Karaite text; the moonlit spinning circle as a recurring sisterhood event; "the adornment" (a gold ornament) as an artifact. The spinning circle and the adornment are built in stage 2 (`tm_hn2.0001`, `0010`).
- [ ] Catholic reaction: a canonist event on Huguccio's "prevailing sex" by conduct (women's company and work) and the Susa oath before the bishop of Turin (`research/cmp_vanderlugt_sex_difference.md`; Rolker); Peter the Chanter's woman's name at confirmation; whether Catholic hostility to daughters hardens around 1200
- [ ] Andalusi reaction: Ibn Ḥazm's charge against al-Ḥakam I as a reaction to Grandmother's House (`research/cmp_delapuente_alhakam.md`)
- [ ] Possible fifth faith (Wendish), if wanted: women's ash divination (Saxo 14.39.11), the woman seer who led a Polish army in 1209, goddess banners (`research/cmp_alvarezpedrosa_slavic_rituals.md`)
- [ ] Southeast Asian faith deferred (user, 2026-10-19): a Visayan babaylan/asog faith at Cebu, marked as a reconstruction

## Second comparanda reading (added 2026-10-19, untested in-game)
- [ ] Names split in `tm_hipukh.0002` (scroll / street); the women's blessing line
- [ ] *Niddui* refused by a protecting lord (`tm_turning_niddui_effect`)
- [ ] Eastern opinion split: knife −15, other gates −5
- [ ] The Wills only under Byzantine-heritage lieges

## Stage 2 inputs from the second comparanda reading
- [ ] Orthodox Slavs: a penance ladder for Slavic Orthodox lieges in place of The Wills; opinions by House (Gift Alone most condemned: self-castration as suicide, a boy cut by force still ordainable; `research/cmp_levin_orthodox_slavs.md`); `christian_syncretic_recipient` would also hit Dorleyites, so cancel it as for the sect
- [x] Hindu and Jain reaction layers by event (klība: disinherited, owed food and clothing; Jain judgement by *veda*) (`tm_ml2.0030`–`0032`, stage 2)
- [ ] Mamluk hostile event: *istiḥlāl al-muḥarramāt* (teaching the forbidden as permitted) as apostasy, after Ibn al-Baqaqi (1302) (`research/isl_islamicate_sexualities.md`)
- [ ] Catholic: Hostiensis's oath before the bishop; Baldus on Giovanni Malaspina inheriting by settled choice (1390s) (`research/cmp_devun_shape_of_sex.md`)
- [ ] German court: Walther's "Under the Linden" (one manuscript: *herre frowe*) (`research/cmp_puff_german_genealogies.md`)
- [ ] Ha-Nehpakhot: Sarah as *aylonit* (b. Yevamot 64b) as a matriarch; Rashi's glosses as the worthies' lines; whether the spinning circle's talk can reach the worthies (Mishnah Sotah 6:1) (these three built in stage 2, `tm_hn2.0001`–`0002`); the 1306 French expulsion for Narbonne and Montpellier; Hildenfinger's Arles documents; Iancu on the expulsion c. 1500
- [ ] Wendish (if wanted): "a pythoness as war-leader" (1209) confirmed in the Latin; Arkona took a third of spoils; Poznań's carnival dress ban (15th c.) (`research/cmp_alvarezpedrosa_sources_slavic.md`)
- [x] Puff, *Sodomy in Reformation Germany and Switzerland* (2003): unavailable (user, 2026-10-19); rely on Rolker, Karras & Pierpont and DeVun for the German lands

## Third Judaism reading (added 2026-10-19, untested in-game)
- [ ] Revel date variant; the women's synagogue options; Before the Baylons with the 1401 council; *fisica* event 0031; Provençal blessing; new names

## Stage 2 inputs from the third Judaism reading
- [x] "The Women at the Door": she brings the prayer to the women standing outside the synagogue (Grossman; Marienberg)
- [x] The brother's prayer book: a family-acceptance event after Leeds MS Roth 32, a wedding gift from a brother
- [x] A rival takes her case to the Christian bailiff: a fine, or the patron's protection (Assis; Shatzmiller) (`tm_hn2.0020`, from 1260)
- [x] "A seat below": buy a seat in the women's synagogue (Arles 1452: three seats for 9½ florins) (`tm_hn2.0050`, from 1409)
- [x] Carnival before Purim (Arles 1433): the abbot of youth demands the *pelote*; pay, appeal to the seneschal, or defy (Christian harassment and a lord's protection; never Jewish wrongdoing) (`tm_hn2.0029`–`0030`, from 1400)
- [x] A Catalan women's-name list (Astruga, Bonafilla, Bellaire, Tolrana) for seekers in Catalonia (option in `tm_hipukh.0002`, from 1390)
- [ ] Not modelled: the French expulsion of 1306, and any expulsion (user: the base game models none)

## Validation (added 2026-10-19)
- Validator is now xTiger (CK3 1.20 fork of Tiger), built at `~/.local/share/xtiger`, also connected as the `xtiger` MCP server. Old Tiger's 1.20 false alarms are gone (20 reports, against 378).
- Fixed from its reports: *The Sisters Choose* used the invalid voter type `same_faith_clergy` (now `same_faith_clerical_electors`); `reformed_icon` removed from all four faiths; tenet `is_shown` now checks the faith or its main rite.
- Known remaining reports, kept on purpose: `history` on rites (vanilla uses it, so a likely xTiger false alarm); `faith:…` inside tenet `is_shown` (xTiger expects a rite, while the game's `_tenet_types.info` says faith; the `OR` covers both). Check in-game that each faith's tenets show in the reform screen.

## Growth engine (added 2026-10-19, untested in-game)
- [ ] Tune the call (2% base) and the courtier rite (8/25%) from the `tm_census_log` counts of one or two observe runs
- [ ] Does the theocracy keep Phrygia out of Byzantium's administrative appointments? If not, consider making the Mother House independent, or a `title_lost` re-grant
- [ ] Conversion resistance for House counties would need a vanilla script-value override (court_chaplain_conversion_factors); decide whether it is worth it

## The Worn Garland and Badenya (added 2026-10-19, untested in-game)
- [ ] Mārkaḻi window; companions falling away; the staff roll; names of the temple street; the endowment and the pandit's objection
- [ ] Badenya: the three-party gate; no claimant; the jeli's satire; the djinn's single return (and on the new body); naming feasts; burial skipping re-embodied bodies
- [ ] Badenya's god names (Ala, the ancestors, the bush spirits): check with a Mande speaker; check every vanilla god-name key is overridden
- [ ] Optional, not built: a solitary Tai vow to Kāma at Kanchi after the Mārkaḻi vow (user: "either or")
- [ ] Commissioned faith icons for both (placeholders: hinduism, mande_reformed)

## Branch faiths, stage 2 (next)
- [x] **Spring the Cell** (user: build with the Bæddel stage-2 work; built in wave 3 as `tm_bae2_spring_cell`, open to all six faiths). Hostile scheme, any adult of the four faiths, landed or not; target a ruler imprisoning a daughter, Marked woman or declared sister. Agents: Marked guards, faithful servants, friends of the House. Success: prisoner walks to the nearest House (else the plotter's court), plotter possibly unknown. Discovery and failure as vanilla hostile schemes. Template: vanilla abduct. The non-war counterpart of Rescue the Daughters and the planned Bæddel raids.
- [x] Bæddel: níð insult duels; landless war-band play; Rescue the Daughters as a raid; Christian outlawry pressure. (Flyting in stage 1; outlawry, Answer the Hall's Call and Rescue the Daughters for bands in wave 3.)
- [ ] Jade Embryo: daughter faction against scholar-officials in celestial and meritocratic governments; temple societies keep estates from crown confiscation; omen events. (Faction built small in wave 3, `tm_yt2`.)
- [ ] Adelphai Dorleyaiou: daughters in court offices; era decay of tolerance after 1066; Aristotelian and Galenic council fight; the founding charter as a house legacy. (The Galenic rite and the Mother's answer are built in wave 3; no council fight.)

## Stage 2, first pass (added 2026-10-20, untested in-game)
One feature per faith, each in its own files; scenarios in TO-TEST.md §J.
- [ ] Bædling flyting (`tm_flyting`): interaction, yearly hostile challenges, three rounds, stakes, the cup. Not built: Raise the Níð-Pole, feud ledger.
- [ ] Liudprand's four children and the Emperor at Dorylaion (`tm_byzr`)
- [ ] Yutai palace offices (`tm_palace`): the offer, the censor's memorial, the 903 purge. A small faction followed in wave 3 (`tm_yt2`).
- [ ] Ha-Nehpakhot prayer book and women at the door (`tm_kahal`); the kahal keeps its children (`tm_surv_keeps_children_effect`, now for all six faiths)
- [ ] Mālai temple's deal (`tm_kovil`)
- [ ] Badenya New Roof (`tm_newroof`)

## Bookmark (added 2026-10-20)
- [x] `bm_867_crusader_dolls`: five heads; Theia Beatrike and the Candragiri and Kirina countesses moved to history characters
- [x] Tab art (user's stained-glass shark, 2026-10-20); the start button and the info-panel backdrop are cut from it
- [x] Map and highlights (draft): cropped from the game's own flatmap, highlights from the province map; replace or paint over as wanted, then adjust `position` in tm_bookmarks.txt
- [x] Portraits dumped in game (2026-10-20). Theia Beatrike has fixed DNA (common/dna_data/tm_dna.txt): 44 at the start, dark brown hair, grey-green eyes, as Welcome to Dorley Hall describes her; the others are left to game defaults (user)
- [x] Coats of arms for the Gotland and Guasha leaders (done 2026-10-23: Steinunn of Gute carries Gotland's whirl; Huijing of the Jade Embryo the tiger)
- [x] Ha-Nehpakhot: an unlanded start (Roads to Power) so the sect can join the bookmark: Bonadonna and her scholars' camp, *Women of the Lamp* (2026-10-21)
- [x] Bonadonna's map highlight `gfx/interface/bookmarks/bm_867_crusader_dolls_bookmark_tm_bonadonna.dds` (user's art) and her portrait (dumped 2026-10-22: physician's robes, quill and book)

## Roads to Power required (user, 2026-10-21; from the next release)
- [ ] The next release requires *Roads to Power*: observe runs keep leaving the faiths landless (Bædling as an adventurer camp, the Garland as courtiers and a mercenary band), and it lets Ha-Nehpakhot start as a landless figure on the bookmark map without a jury-rigged holding.
- [ ] Workshop page and README: state the requirement (README Prerequisites done on the stage2 branch). Descriptor files cannot enforce DLC; check whether the Workshop "required items" list can name it.
- [ ] Audit script for `has_dlc_feature` guards around landless-adventurer and Roads to Power content; they can stay but are no longer needed.
- [ ] Design: a landless-adventurer path for each faith that loses its land (Bædling war-band first, with the stage-2 outlawry work); a landless Ha-N bookmark figure at Arles. Wave 3 built *Answer the Hall's Call*, the return to the seat and the settling grace for bands of all six faiths, and opened Rescue the Daughters to bands; the Ha-N figure is still open.
- [ ] Future DLC: if merchant companies arrive, move the bands' settling path to a company charter (a trading post held by contract) and keep the county war as the last resort (docs/wave3/baedling.md §3).


## Stage 2, second pass: Ha-Nehpakhot, the Worn Garland, Badenya (added 2026-10-21, untested in-game)
Design notes: docs/stage2/ha-nehpakhot.md, worn-garland.md, badenya.md. Scenarios in TO-TEST.md §P, §R and §S.
- [ ] Ha-Nehpakhot stage 2 (`tm_hn2`): by moonlight and the spindle talk (0001, 0002; the +10 at the next hearing); the adornment (0010, 0011); before the bailiff (0020, from 1260); Carnival before Purim (0029, 0030, from 1400); the lord's licence (0040); a seat below (0050, from 1409); Catalan names (from 1390)
- [ ] Ha-N open questions: is 15% for the spindle talk too high; necklace or bracelet; a player decision to commission the adornment; *batlle* and *berurim* in Catalan counties; a Jewish bailiff before 1260 (Abba Mari at Saint-Gilles); a narrower Carnival region; 0040 for Rabbinic rulers too
- [ ] The Worn Garland stage 2 (`tm_ml2`): a share on the temple street (0001, 0003, 0004; 8 gold a year, three years away); a gift in her own name (0010 and the decision); She of the Illustrious Staff (0011, from 1100, date unverified); Food and Clothing (0030); Of the Third Feeling and the Order's Terms (0031, 0032); the Reciter (0040)
- [ ] Garland, not made (user to decide): fold `tm_garland.0020` into `tm_ml2.0010` for rulers; prefer a staff-holder as the vow's elder; the growth call notices temple streets; `tm_kovil` honours passed by the street's choice. Not built: the solitary Tai vow
- [ ] Garland open questions: shares from non-Hindu lords; less worth for gifts at royal temples; a god's name in the staff nickname; *Disinherited* too heavy for a flavour event; a Vaiṣṇava counterpart to the Reciter
- [ ] Badenya stage 2 (`tm_bd2`): the sister's line at a succession (0001, 0002); a hot realm and the cool word (0010); praise before the court (0020); uninvited praise at a naming (0030); Named With the King, the honour only (0040–0042 and two decisions, from 1352)
- [ ] Badenya open questions: sisters of one mother only; an event for the passed-over sister's child; heat after conquest; a jelimuso at non-Badenya courts; the associate decision below kingdom tier. Not built: the associate's fall; Makuria's *ngonnen*; an interpreter variant at Ghana
- [ ] Watch claimant wars from sister's-line claims on kingdom titles in the next observe run

## Bædling stage 2 and landless survival (added 2026-10-21, untested in-game)
- [ ] Spring the Cell (`tm_bae2_spring_cell`): scheme, three agent types, interaction, AI plotter search; prisoners to the nearest House
- [ ] Outlawry (`tm_bae2`, 0100–0135): suit from 1100 at Christian Norse courts (sorcery / dress clause), six housewives, life-ring, full outlawry → adventurer band; settlement, forgiven for the war, the high seat
- [ ] Answer the Hall's Call (`tm_bae2_answer_hall_decision`), return-to-the-seat travel, settling grace on `on_title_gain`
- [ ] Not built: feud ledger and Offer Bót; reprieve by killing outlaws (K §110); the níð suit against the flyter; Sophoulis proposals 1–3 and 6
- [x] Lead: Rescue the Daughters for adventurers? declared sisters in `tm_captive_daughter_trigger`? (docs/wave3/baedling.md §4). Both done by the lead (user decision, 2026-10-21): bands may wage it and land on victory; declared sisters count.

## Yutai Dao palace faction (added 2026-10-21, untested in-game)
- [ ] Yutai palace faction (`tm_yt2`): the balance on the throne's title, *Work the Inner Offices*, the Clerk of Ceremonies (971+), the Censor's Brush (celestial thrones only), the licences option at month 3. Not built: Liao and Ming levers ("Seal the Ledgers", Grass 2024), Cui Yin's 902 proposal (So row 9), the Boy from Min (Rideout row 3), the Commissioner of Merit's repair levy (Rideout row 6).

## Adelphai Dorleyaiou stage 2 (wave 3, untested in-game)
- [ ] Galenic rite: name, colour and icon after create_rite_from_type; knife doctrine copied; tenets shown on the new rite
- [ ] Found / Join / Return decisions; the Mother's answer (tm_dl2.0002); liege opinion
- [ ] Galenic answers at tm_byz.0010 and 0012
- [ ] Ignatios lands in late November 867; Tarsus train gates (990, Muslim Cilicia); Athos once 1083-89; the steward from 1120; the Consul's Letter 1063-78
- [ ] Watch observe runs: how often the AI founds the Galenic rite (should be rare)
- [x] `tm_body_galenic_desc` rewritten to "some third thing" (docs/wave3/dorley.md, "Changes needed" 1)
- [ ] Only if the in-game check fails: add the Galenic rite to the three tenets' `is_shown`. Optional: a lighter suppression ladder for the Galenic wing

## Deeds of the House (added 2026-10-21, untested in-game)
- [x] Hook in tm_take_the_knife_effect added
- [ ] Scenarios 1–11 of docs/wave3/achievements.md (TO-TEST.md §O)
- [ ] A foreign councillor's seat while imprisoned (Al-Kunduri)
- [ ] Check the date of the woman-pope legend (c. 1250–80) used in `tm_ach.0001`; it is general knowledge, not a repo source
- [ ] Not built: a war from the steppe judgment; deeds for the other gates; event art

## Ha-Nehpakhot in the Maghreb (added 2026-10-21, untested in-game)
- [x] Ha-Nehpakhot, wave 3: Maghreb and Sahel (`tm_hn3`; `docs/wave3/ha-nehpakhot-maghreb.md`). Untested.
- [x] Questions answered (user, 2026-10-21): the Muslim-lord ban stays limited to the Maghreb and the Sahel; Maghrebi names have no date gate; the vizier gate stays at 1075; the Maghrebi judges are in `tm_kahal_judges` ("the elders and the dayyan", added by the lead).
- [ ] Print pages for Kraemer, Krakowski and Rustow.

## Survival balance (added 2026-10-21, untested in-game)
- [ ] Survival balance (docs/wave3/survival.md): the kahal of her town, take in, the gathering, a dead ruler's household, children kept, the death counter
- [ ] Check in the next observe run: Ha-N `kahal` about 1 a decade with a few landed rulers; `pilgr` for the Adelphai, Badenya and Yutai Dao; Badenya's `pool` deaths after a fallen realm; Yutai `deaths` below about a third of members a decade
- [ ] Yutai Dao gains a little from children kept and the gathering; the user accepted Yutai running away, so watch it
- [ ] Whether landless adventurers count in `ordered_ruler`; if not, camps are not homes in the gathering

## Wave 3 (untested in-game)
In-game checks for everything built on 2026-10-21. Scenarios are in TO-TEST.md §L–§T.
- [ ] **Load.** Start a fresh game with all wave-3 files in place (new script files are not hot-loaded; adding them mid-run once crashed the game). Send `error.log`.
- [ ] **Bædling (§L).** Custom agent types show names and contributions; `start_war` with `claim_cb` from a decision charges no extra cost; `create_landless_adventurer_title_effect` on a newly sentenced courtier; the settling grace on `on_title_gain`; saved scopes in the outlawry pulse; no suit before 1100 or under pagan or English lords.
- [ ] **Rescue the Daughters for bands.** A band that wins lands through `create_title_and_vassal_change` (not vanilla's `ep3_become_landed_transfer_effect`): check the camp is cleaned up and `tm_bae2_title_gain` gives the settling grace. Declared sisters count as captives.
- [ ] **Yutai (§M).** `tm_yt2_balance` on the throne's primary title; `title:e_minister_censor.holder ?=` with no holder; `random_realm_county` covers the throne's own counties; saved scopes in delayed events.
- [ ] **Adelphai (§N).** `create_rite_from_type` name, colour and icon; `convert = yes` and `change_rite_doctrine` the same tick; `set_character_rite_with_conversion` on a landed ruler; tenets shown on the Galenic rite; Ignatios lands on 20 November 867.
- [ ] **Deeds (§O).** Saved scopes survive from before to after the knife; adopting a landed Pope; a female head holding `k_papal_state`.
- [ ] **Ha-N stage 2 and Maghreb (§P, §Q).** Artifact variables (`set_variable` on an artifact scope); the necklace and the Qayrawanese attire artifacts; the Carnival court list; `tm_hn3_maghreb_era` in a trigger; the `diarch` link as regent; saved scopes from `tm_hn3_niddui_effect` reaching 0010 thirty days later; the elders-and-dayyan judges' text in the West.
- [ ] **Garland (§R).** `location.county ?= var:tm_ml2_share`; `random_character_in_location` for the street's choice; `clear_saved_scope` between two shares in one pulse; adopted daughters in `ordered_child`; whether AI courtiers ever have gold enough to give.
- [ ] **Badenya (§S).** `order_by = age`; the heir's mother as the dead ruler's sibling inside `on_death`; `scope:mother` at `on_birth_child`; `add_unpressed_claim` from a saved title; the associate's clean-up on either death.
- [ ] **Survival (§T).** `faith_filter` on a saved scope; `is_pool_guest`; the death counter split between `deaths` and `pool_deaths`; `tools/census_report.py` notes.
- [ ] **Flyting budget.** The yearly flyting challenge now checks and spends the flavour budget (`tm_flyting_on_actions.txt`).

### Decisions (user, 2026-10-21)
- Rescue the Daughters is open to landless bands and counts declared sisters (done by the lead in `tm_casus_belli.txt` and `tm_triggers.txt`).
- Outlawry is provisionally only at Christian courts (Christian lords of North Germanic heritage, from 1100); the pagan North has no sourced suit.
- The Censor's Brush fires at celestial thrones only.
- The Deeds of the House keep "the Unmaker"; a Pope made a eunuch by Grandmother's House counts toward the deeds.
- Kahal joins may create characters, as a stand-in for the wider Jewry the game does not make.
- Refugees from the Almohads keep their own faith: shelter is not conversion (the lead changed `tm_hn3_receive_refugees_effect`). They live at her court, where the kahal of her town may draw them later.
- The Maghreb judges' custom loc reads "the elders and the dayyan" (added by the lead).
- The Muslim-lord ban is limited to the Maghreb and the Sahel.
- Maghrebi names have no date gate.
- The vizier option starts in 1075.

## Landless bands, wave 4 (added 2026-10-21, untested in-game; docs/wave4/bands.md)
- [ ] The Patent and the Robe (`tm_band.0001`–`0020`): offers after service / patience / five years' camp; regional text (robe, township, Strumica, Merope, charter); settlement through vanilla `ep3_laamps.0300`; move on with patience (claim + goodwill) or stay (vanilla evict)
- [ ] The Companions Choose (`tm_band.0100`–`0102`): officers hand a weak band to a stronger companion; player consent; TEST that the camp domicile and MaA follow `change_title_holder` (TO-TEST §U6)
- [ ] Not built: The Sword Is My Patent; the darker Companions branch; Dirham's pilgrimage-and-envoy road; Ghazis Have No Wealth (declined by the user)

## Gotland (wave 4, added 2026-10-21, untested in-game; docs/wave4/gotland.md)
- [ ] Open Ports (`tm_got_open_ports_decision`): vanilla join-war contract for player bands, event 0100 for AI bands; licence recorded on join, lapses at peace (0110); Seize an Island Seat (claim war); island seat (0120) and the clearing fleet (0130)
- [ ] The Island Changes Hands (`tm_got.0200`–`0210`): non-inheritance transfer of `c_gutland` to another faith; 1361 / 1391 / 1398 / 1407 variants by realm; keep quiet, the levy, the ships
- [ ] Swear the Peace of the Island (`tm_got.0300`): yearly 5%, once per ruler; county modifier and mutual opinions
- [ ] Not built: flight to a petty coastal lord (East Frisia); Dollinger proposals 3, 4 and 7 wait for merchant companies; 6 (the vitte) not in this wave
- [ ] Lead: AI bands spare a sworn island? (`NOT = { has_variable = tm_got_island_peace }` in `tm_bae2_hall_county_trigger`; see the questions below)

## Protection under Muslim and Orthodox lords (wave 4, added 2026-10-21, untested in-game; docs/wave4/protection.md)
- [ ] Under Her Chivalry (`tm_fut.0001`–`0020`; Tor pp. 244, 248–250): the Fityan (Iran and Iraq, before 1056), she puts herself under his word, he gives it or not, the demand (she is never handed over)
- [ ] No Service in the Prince's Wars (`tm_fut.0030`–`0033`, `tm_fut_grant_terms_interaction`; Dollinger pp. 381–382): terms for Nehpakhot courtiers; physician, interpreter or steward; unless they ask; in their own fashion
- [x] Guard for 0041 in `tm_world_on_actions.txt` (done by the lead). The interim flag loan in `tm_fut_shelter_upkeep_effect` is now redundant but harmless
- [ ] The bailiff guard in `tm_hn2_on_actions.txt` was not added (lead's decision): a sheltered member can still meet the bailiff

## The Worn Garland, wave 4 (added 2026-10-21, untested in-game; docs/wave4/garland.md)
- [ ] Garland wave 4 (`tm_ml3`): a lamp kept by the market (`tm_ml2.0010` option e); the quarter that dwindled (0010); Heroes of the Road contract (0020–0022) → guild town by vanilla settlement (0030–0031); the Lord of Vannadu (0040)
- [ ] Garland, from Hall §11, not built: Those Who Always Accompany Us (band sworn to merchants; Polonnaruwa); A Hall in the Name of the Five Hundred (a band's *maṇḍapa* marks a street); the Pepper Merchant's Vow; a company of the Thousand Directions (waits for merchant companies)
- [ ] Badenya could borrow the caravan contract (a Mande trader as employer, not "the Dyula")

## Yutai and the Sogdians (wave 4, added 2026-10-21, untested in-game; docs/wave4/yutai-sogdians.md)
- [ ] Yutai and the Sogdians (`tm_yt3`): *Hide the Name* (decision and `tm_yt3.0001`, reusing Keep Quiet's variable; offered once after 903), the banquet at the Cao inn (`tm_yt3.0010`, Hexi, from 900), No Reply from There (`tm_yt3.0020`, after the Ancient Letters)
- [ ] Not built: Vaissière rows 1–3, 7 and 8 (Master of the Caravan, Rallied Township as a Yutai feature, Sabao to Office, the Network's Post, the Town of the Grape); no Sogdian moneylender in any form; no house renaming
- [ ] Optional comment line above `tm_world_keeps_quiet_trigger` naming Hide the Name as a second source of the variable (no script change)

## Wave 4 (untested in-game)
In-game checks for everything built on 2026-10-21 in wave 4. Scenarios are in TO-TEST.md §U–§Y.
- [ ] **Load.** Start a fresh game with all wave-4 files in place (new script files are not hot-loaded). Send `error.log`.
- [ ] **Bands (§U).** The list `offered_titles` survives `trigger_event` into vanilla `ep3_laamps.0300`; `root.war` in `on_war_won_attacker` / `on_war_won_defender`; `change_title_holder` on a camp title with `type = stepped_down` moves the domicile, buildings, provisions and men-at-arms (§U6, the main risk); `set_player_character` after the hand-over; `ep3_laamps.0300` is harmless for AI lords; the `random = { chance … modifier … }` form in the pulses.
- [ ] **Gotland (§V).** `create_task_contract` from a decision on a player band, and whether the contract's `on_create` overwrites its variables; `on_join_war_as_secondary` after `add_attacker` from script; `scope:war` in the four war-end on_actions; a variable holding a war compared after save and load; the island heuristic (do sea crossings count as neighbours?); `ordered_ruler` by `max_military_strength`; `change_fervor` with `desc`.
- [ ] **Protection (§W).** `set_knight_status = forbid` / `default` persists until changed; `tm_fut_grant_terms_effect` building `flag:$SERVICE$` and the modifier key; `tm_fut_sheltered_trigger = no` when the variable is absent; `add_character_flag` with `years` resets the timer; `trigger_event = tm_fut.0030` from an interaction's `on_accept`. The lead's new guard keeps `tm_world.0041` away from a sheltered daughter.
- [ ] **Garland (§X).** `create_task_contract` + `accept_task_contract` from the yearly pulse, and `save_scope_as` inside it; contract gold at `on_create` (if 0, use the employer); contract loc keys; `yearly_playable_pulse` reaching landless adventurer leaders; `negotiate_settlement_interaction_effect` outside its interaction; `order_by` on squared distance; the `tm_ml3_toll` contract variable through `trigger_event`; `employer = prev` in the on_action.
- [ ] **Yutai (§Y).** `kingdom ?= { this = title:k_hexi }` from a county; `learning = { 6 12 }` in `create_character`; `save_temporary_scope_as` in triggers called from the global pulse; `faith_hostility_level` against `faith_hostile_level`; the key `faith:mahayana_faith`.
- [ ] **Debug programme.** `tm_debug_force_programme_interaction` now raises the daughter without the Deeds of the House. Deeds scenarios (§O) need the real programme or the Dorley path, not the debug interaction.
- [ ] **Validation.** The `tm_interactions.txt:264` warning in the baseline (garland.md) may be gone now that the debug programme no longer runs `tm_take_the_knife_effect`; check at the next xTiger run.

### Decisions (lead, 2026-10-21)
- The women's-quarters guard for sheltered daughters was added to `tm_world_on_actions.txt` (block 38, *Those Without Desire*, both limits): a daughter under a Muslim lord's word is never asked.
- The bailiff guard (`tm_fut_under_terms_trigger = no` in `tm_hn2_on_actions.txt`) was NOT added: it would cover quarrels with anyone, which is broader than clause 10.
- The debug programme interaction now skips the Deeds of the House (their effects read `root`, which an interaction lacks).

## Questions for the user (wave 4)
- [ ] **The Cao inn banquet** fires from 900, not 914 as the Vaissière note's row 5 suggested. The inn's Cao are a Sogdian family of the town, not the ruling Cao of the Guiyijun. Keep 900?
- [ ] **Hide the Name** is abstract: option (a) costs prestige and sets the hidden flag, but no house is renamed. Keep it abstract?
- [ ] **The market lamp modifier** is permanent. Should it stay permanent, or last a term of years?
- [ ] **The guild town** comes after three caravans with any employer; the third employer makes the offer. Should all three be with the same employer?
- [ ] **Valikandapuram** (the Lord of Vannadu, `tm_ml3.0040`) only warns; nothing is taken. Is a warning enough?
- [ ] **A sworn island.** Should AI bands spare an island that swore the peace? (Add `NOT = { has_variable = tm_got_island_peace }` inside the AI-only part of `tm_bae2_hall_county_trigger`.)
- [ ] **Open Ports** offers the letters to Bædling bands only. Open it to the bands of all six faiths?
- [ ] **Futuwwa after 1182.** Should the *futuwwa* framing also run after 1182 in Iraq and Anatolia (al-Nasir's orders, the *akhi*)? That is general knowledge, not in Tor. Built: Iran and Iraq before 1056 only.
- [ ] **Muslim lords and the terms.** No Service in the Prince's Wars is open to any lord of another faith except Jewish lords. Keep Muslim lords, or limit it to Christian lords as in the Smolensk precedent?
- [ ] **A vassal of the sect.** Should a ruler of Ha-Nehpakhot who is a vassal of another faith be able to ask her liege for the terms? There is no clean per-vassal war exemption; it would need a levy or contract change.
- [ ] **The Companions Choose fallback.** If the camp does not follow `change_title_holder` (§U6), limit the event to a companion who is the leader's child or heir?
- [ ] **The Sword Is My Patent.** Build the decision (Tor proposal 2's last step), or leave it to the stored claim and vanilla CBs?
- [ ] **The companion strikes first / the deposed leader's return.** Build the darker branch (the plot discovered) or Dirham's road (pilgrimage, then a lord's envoy)?
