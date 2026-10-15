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
