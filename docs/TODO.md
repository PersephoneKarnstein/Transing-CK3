# TODO

## Art
- [ ] **Commission official-looking art for all icons** (user, 2026-10-14). The user is drawing interim versions; the final set should match vanilla CK3 style. 15 icons, specs in the build notes and `~/Downloads/ck3_icon_examples/` for reference:
  - faith/rite: `gfx/interface/icons/faith/tm_dorleyaian.dds` 100×100
  - tenets: `gfx/interface/icons/faith_tenets/tenet_tm_{day_of_blood,daughters_chosen,sisterhood}.dds` 260×400
  - doctrines: `gfx/interface/icons/faith_doctrines/tm_knife_{grandmother,aunt_bea,gift_alone}.dds`, `tm_body_{aristotelian,galenic}.dds` 120×120
  - doctrine groups: `gfx/interface/icons/faith_doctrine_groups/doctrine_tm_{knife,body}.dds` 120×120
  - traits: `gfx/interface/icons/traits/tm_{transgender,daughter_of_the_knife,novice,washout}.dds` 120×120
  - all DDS, uncompressed B8G8R8A8, transparent background
- [ ] Event pictures for the Rite of the Knife, washout, Sister-Making and the flavour "achievement" events.
- [ ] When art lands: point faith/rite/tenets/doctrines at the new files and delete placeholder `icon =` lines in `common/traits/tm_traits.txt`.

## Content
- [ ] Religious head title (Mother of Mothers) or a creation decision.
- [ ] `name_list_kybeline`.
- [ ] In-game load test with `-develop`; CK3 Tiger pass.
