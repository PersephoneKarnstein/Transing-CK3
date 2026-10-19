# TODO

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

## Branch faiths, stage 2 (next)
- [ ] **Spring the Cell** (user: build with the Bæddel stage-2 work). Hostile scheme, any adult of the three faiths, landed or not; target a ruler imprisoning a daughter, Marked woman or declared sister. Agents: Marked guards, faithful servants, friends of the House. Success: prisoner walks to the nearest House (else the plotter's court), plotter possibly unknown. Discovery and failure as vanilla hostile schemes. Template: vanilla abduct. The non-war counterpart of Rescue the Daughters and the planned Bæddel raids.
- [ ] Bæddel: níð insult duels; landless war-band play; Rescue the Daughters as a raid; Christian outlawry pressure.
- [ ] Jade Embryo: daughter faction against scholar-officials in celestial and meritocratic governments; temple societies keep estates from crown confiscation; omen events.
- [ ] Dorleyism: daughters in court offices; era decay of tolerance after 1066; Aristotelian and Galenic council fight; the founding charter as a house legacy.

