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
- [ ] Flavour "achievement" events (post-v1).
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
- [ ] "Six Housewives" compurgation; women's suits carried by a friend of the House; dress clause needs a powerful prosecutor (Mitchell; Jochens)
- [ ] Pour the Cup: end a flyting / first cup / inheritance toast at the high seat (Damico; Evans & Hancock)
- [ ] Events: "They Say He Keeps Seiðmenn" (Tolley); "Weave the Warding Shirt" (Jochens); English reaction text, Wulfstan 1014 (Damico)
- [ ] Insult duel: 3 rounds, charges checked against real traits, owning the word strongest, stakes by witnesses and venue (Lögberg doubles); Raise the Níð-Pole scheme (Clover; Meulengracht Sørensen; Grágás)
- [ ] Feud ledger, Offer Bót compensation, fostering to seal a settlement (Miller)
- [ ] Outlawry: lesser (life-ring, three homes, three summers) and full; reprieve by killing outlaws; three endings (Grágás; Ahola)
- [ ] Dress clause as a Christian-era / law pressure; covers weapon-bearing women (Grágás)
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
- [ ] Events: Liudprand's four boys (949) rescue-and-adopt; Ignatios returns as patriarch (867); Tarsus boy-train with options per knife house; the Emperor halts at Dorylaion (Opsikion); Steward at the Gate; Psellos's "feminine nature" (c. 1066); Athos closed to eunuchs (1083)
- [ ] Abbasid event pack: the jester, the beard plucked overnight, the barber sent to humiliate a prince (Rowson)
- [ ] Galenic splinter rite: Theophylact's *In Defence of Eunuchs* as its book
- [ ] Verify the Galen renderings in byz_galen_on_semen.md against De Lacy (CMG V 3,1)

## China reading revisions (added 2026-10-18, untested in-game)
- [ ] Embryo chain with the new month-6 options and the ghost-fetus event (0013)
- [ ] Queen Mother of the West shows as the Way's high god; Southern Marchmount holy site at c_hengzhou
- [ ] Temple society dues at births and deaths; righteous store loan and repayment; name-panel; confiscation waves
- [ ] Prodigy in the Prefecture; Ordain by Special Edict; Relight the Shenquan Abbey; Huang Lingwei rescript (882–900)
- [ ] Eastern-faith triggered opinion (parameter eastern_syncretic_recipient)

## Stage 2 inputs from the China reading
- [ ] Palace faction: Shence commanders and Commissioners of Military Affairs (Northern Office) vs scholar-officials (Southern Office); Yang Fugong's adopted sons; the 903 massacre; Song adoption licences and quotas
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
- [ ] Ha-Nehpakhot: a source for Provençal Jewish women's names (Iancu; Shatzmiller); the *aylonit* chapter of *Trans Talmud*; community roles from the medieval codes; Karaite text; the moonlit spinning circle as a recurring sisterhood event; "the adornment" (a gold ornament) as an artifact
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
- [ ] Hindu and Jain reaction layers by event (klība: disinherited, owed food and clothing; Jain judgement by *veda*)
- [ ] Mamluk hostile event: *istiḥlāl al-muḥarramāt* (teaching the forbidden as permitted) as apostasy, after Ibn al-Baqaqi (1302) (`research/isl_islamicate_sexualities.md`)
- [ ] Catholic: Hostiensis's oath before the bishop; Baldus on Giovanni Malaspina inheriting by settled choice (1390s) (`research/cmp_devun_shape_of_sex.md`)
- [ ] German court: Walther's "Under the Linden" (one manuscript: *herre frowe*) (`research/cmp_puff_german_genealogies.md`)
- [ ] Ha-Nehpakhot: Sarah as *aylonit* (b. Yevamot 64b) as a matriarch; Rashi's glosses as the worthies' lines; whether the spinning circle's talk can reach the worthies (Mishnah Sotah 6:1); the 1306 French expulsion for Narbonne and Montpellier; Hildenfinger's Arles documents; Iancu on the expulsion c. 1500
- [ ] Wendish (if wanted): "a pythoness as war-leader" (1209) confirmed in the Latin; Arkona took a third of spoils; Poznań's carnival dress ban (15th c.) (`research/cmp_alvarezpedrosa_sources_slavic.md`)
- [x] Puff, *Sodomy in Reformation Germany and Switzerland* (2003): unavailable (user, 2026-10-19); rely on Rolker, Karras & Pierpont and DeVun for the German lands

## Third Judaism reading (added 2026-10-19, untested in-game)
- [ ] Revel date variant; the women's synagogue options; Before the Baylons with the 1401 council; *fisica* event 0031; Provençal blessing; new names

## Stage 2 inputs from the third Judaism reading
- [ ] "The Women at the Door": she brings the prayer to the women standing outside the synagogue (Grossman; Marienberg)
- [ ] The brother's prayer book: a family-acceptance event after Leeds MS Roth 32, a wedding gift from a brother
- [ ] A rival takes her case to the Christian bailiff: a fine, or the patron's protection (Assis; Shatzmiller)
- [ ] "A seat below": buy a seat in the women's synagogue (Arles 1452: three seats for 9½ florins)
- [ ] Carnival before Purim (Arles 1433): the abbot of youth demands the *pelote*; pay, appeal to the seneschal, or defy (Christian harassment and a lord's protection; never Jewish wrongdoing)
- [ ] A Catalan women's-name list (Astruga, Bonafilla, Bellaire, Tolrana) for seekers in Catalonia
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
- [ ] **Spring the Cell** (user: build with the Bæddel stage-2 work). Hostile scheme, any adult of the four faiths, landed or not; target a ruler imprisoning a daughter, Marked woman or declared sister. Agents: Marked guards, faithful servants, friends of the House. Success: prisoner walks to the nearest House (else the plotter's court), plotter possibly unknown. Discovery and failure as vanilla hostile schemes. Template: vanilla abduct. The non-war counterpart of Rescue the Daughters and the planned Bæddel raids.
- [ ] Bæddel: níð insult duels; landless war-band play; Rescue the Daughters as a raid; Christian outlawry pressure.
- [ ] Jade Embryo: daughter faction against scholar-officials in celestial and meritocratic governments; temple societies keep estates from crown confiscation; omen events.
- [ ] Adelphai Dorleyaiou: daughters in court offices; era decay of tolerance after 1066; Aristotelian and Galenic council fight; the founding charter as a house legacy.

