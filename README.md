# Transbian Maximalism — CK3 mod

Adds **Transbian Maximalism** to Crusader Kings III 1.20 as both a **culture** and a **faith with a scripted main Rite**, so either can be picked in the Ruler Designer. Final tenets, doctrines, pillars and traditions are still TODO; everything here is a loading skeleton with sensible placeholders.

Game files referenced below live under
`~/Library/Application Support/Steam/steamapps/common/Crusader Kings III/game/`.

## Layout

| File | What it defines | Spec (`.info`) |
|---|---|---|
| `common/religion/religion_types/tm_religion_types.txt` | Religion `transbian_maximalism_religion`: family, baseline doctrines, virtues/sins, loc block | `common/religion/religion_types/_religion_types.info` |
| `common/religion/faith_types/tm_faith_types.txt` | Faith `transbian_maximalism`: colour, icon, holy sites, faith-level doctrines | `common/religion/faith_types/_faith_types.info` |
| `common/religion/rite_types/tm_rite_types.txt` | Main Rite `transbian_maximalist_rite`: the 3 core tenets, rite doctrine overrides | `common/religion/rite_types/_rite_types.info` |
| `history/faiths/tm_faith_history.txt` | Flags the faith `created = yes` from 867 so it is pickable with zero followers | `history/faiths/_faith_history.info` |
| `common/culture/cultures/tm_cultures.txt` | Culture `transbian_maximalist`: pillars, traditions, name list, gfx, ethnicities | `common/culture/cultures/_cultures.info` |
| `common/culture/pillars/tm_pillars.txt` | New `heritage_transbian` and `language_transbian` pillars | `common/culture/pillars/_pillars.info`, `common/culture/_cultural_traits.info` |
| `history/cultures/transbian_maximalist.txt` | Innovation history (copied from Anglo-Saxon) so the culture leaves the Tribal era | `history/cultures/_culture.info` |
| `localization/english/tm_l_english.yml` | All display names (UTF-8 BOM, `l_english:`) | — |
| `descriptor.mod` | In-mod descriptor; launcher copy is `~/Documents/Paradox Interactive/Crusader Kings III/mod/transbian_maximalism.mod` | — |

## How the 1.20 religion stack fits together

```
religion_family (rf_pagan / rf_abrahamic / rf_eastern / rf_sinitic)
  └─ religion   — baseline doctrine per group, virtues/sins, deity loc keys
       └─ faith — colour/icon, holy sites, faith-intrinsic doctrines, main_rite
            └─ rite — what characters actually practise: 3 core tenets + doctrine overrides
```

Precedence for a doctrine group: **rite > faith > religion**. Core tenets go on the *rite*, not the faith.

## Ruler Designer availability

* Culture picker binds `CultureTemplate` (see `gui/window_ruler_designer.gui`), so any culture template in `common/culture/cultures/` shows up; no county needs to hold it.
* Faith picker lists each faith's rites via `Faith.GetRites`. A rite with `history = yes` is excluded from custom rulers; ours leaves the default `no`.
* A faith with no followers is "not created" until `history/faiths` flags it, hence `tm_faith_history.txt`.

## Design TODOs

* **Rite tenets** (pick 3) — current placeholders: `tenet_polyamory`, `tenet_carnal_exaltation`, `tenet_ritual_celebrations`. Full vanilla list:

  `tenet_adaptive tenet_adorcism tenet_ancestor_worship tenet_aniconism tenet_armed_pilgrimages tenet_asceticism tenet_astrology tenet_be_fruitful_and_multiply tenet_benevolent_governance tenet_bhakti tenet_carnal_exaltation tenet_celestial_hierarchy tenet_christian_syncretism tenet_communal_identity tenet_communal_possessions tenet_communion tenet_confession tenet_consolamentum tenet_cranial_trophies tenet_cthonic_redoubts tenet_dharmic_pacifism tenet_divine_liturgy tenet_divine_marriage tenet_dulia tenet_eastern_syncretism tenet_esotericism tenet_exaltation_of_pain tenet_extinction_of_dharma tenet_false_conversion_sanction tenet_filial_piety tenet_gnosticism tenet_gruesome_festivals tenet_harmonious_society tenet_hedonistic tenet_hesychasm tenet_holy_myron tenet_household_gods tenet_human_sacrifice tenet_hyperdulia tenet_inner_journey tenet_islamic_syncretism tenet_jewish_syncretism tenet_khachkar tenet_legalism tenet_literalism tenet_love_thy_neighbour tenet_megaliths tenet_mendicant_preachers tenet_miles_christi tenet_mortification_of_the_flesh tenet_mountain_worship tenet_mystical_birthright tenet_natural_primitivism tenet_no_mind tenet_ora_et_labora tenet_original_sin tenet_pacifism tenet_pastoral_isolation tenet_peace_of_god tenet_pentarchy tenet_philanthropia tenet_polyamory tenet_preservation tenet_pure_land tenet_purgatory tenet_pursuit_of_knowledge tenet_pursuit_of_power tenet_reincarnation tenet_religious_legal_pronouncements tenet_ritual_cannibalism tenet_ritual_celebrations tenet_ritual_hospitality tenet_sacred_childbirth tenet_sacred_destruction tenet_sacred_shadows tenet_sacrificial_ceremonies tenet_sanctity_of_nature tenet_scholasticism tenet_simony tenet_sinitic_syncretism tenet_struggle_submission tenet_sun_worship tenet_takamin tenet_tax_nonbelievers tenet_transubstantiation tenet_unreformed_syncretism tenet_unrelenting_faith tenet_vows_of_poverty tenet_warmonger`

  (Christian-specific ones like `tenet_communion`, `tenet_apostolic_succession`, `tenet_miaphysitism` assume `special_doctrine_is_christian_faith`.)

* **Doctrines** — one per group is mandatory. Options per group (vanilla):

  | Group | Options |
  |---|---|
  | theism | `doctrine_monotheist` `doctrine_polytheist` |
  | head_of_faith | `doctrine_no_head` `doctrine_spiritual_head` `doctrine_temporal_head` |
  | gender | `doctrine_gender_equal` `doctrine_gender_female_dominated` `doctrine_gender_male_dominated` |
  | pluralism | `doctrine_pluralism_fundamentalist` `doctrine_pluralism_pluralistic` `doctrine_pluralism_righteous` |
  | theocracy | `doctrine_theocracy_lay_clergy` `doctrine_theocracy_temporal` |
  | marriage_type | `doctrine_monogamy` `doctrine_polygamy` `doctrine_concubines` |
  | divorce | `doctrine_divorce_allowed` `doctrine_divorce_approval` `doctrine_divorce_disallowed` |
  | bastardry | `doctrine_bastardry_all` `doctrine_bastardry_legitimization` `doctrine_bastardry_none` |
  | consanguinity | `_unrestricted` `_aunt_nephew_and_uncle_niece` `_cousins` `_dynastic` `_restricted` (prefix `doctrine_consanguinity`) |
  | homosexuality | `doctrine_homosexuality_accepted` `_shunned` `_crime` |
  | deviancy | `doctrine_deviancy_virtuous` `_accepted` `_shunned` `_crime` |
  | adultery_men / adultery_women | `_accepted` `_shunned` `_crime` |
  | kinslaying | `_accepted` `_shunned` `_close_kin_crime` `_extended_family_crime` `_any_dynasty_member_crime` |
  | witchcraft | `doctrine_witchcraft_virtuous` `_accepted` `_shunned` `_crime` |
  | clerical_function | `_taxation` `_alms_and_pacification` `_recruitment` |
  | clerical_gender | `_either` `_female_only` `_male_only` |
  | clerical_marriage | `_allowed` `_disallowed` |
  | clerical_succession | `_spiritual_appointment` `_spiritual_fixed_appointment` `_temporal_appointment` `_temporal_fixed_appointment` `_conditional` |
  | monasticism_group | `doctrine_monasticism_absent` `_accepted` `_encouraged` `_forbidden` |
  | sacraments_group | `doctrine_sacraments_absent` `doctrine_sacraments_central` |
  | pilgrimage | `_encouraged` `_forbidden` `_local_rites` `_mandatory` |
  | funeral | `doctrine_funeral_stoic` `_bewailment` `_cremation` `_mummification` `_sky_burial` `doctrine_family_rites` |
  | coronation | `doctrine_no_anointment` `doctrine_anointment_permitted` `doctrine_imperial_anointment` |
  | preservation | `doctrine_mythic_literary` `doctrine_oral_storytelling` `doctrine_scriptural` |
  | hostility_group | `pagan_hostility_doctrine` `abrahamic_hostility_doctrine` `eastern_hostility_doctrine` `sinitic_hostility_doctrine` |

* **Culture pillars** — ethos: `ethos_bellicose stoic bureaucratic spiritual courtly egalitarian communal`; martial custom: `male_only equal female_only`; head determination: `domain` or `herd`.
* **Traditions** — 173 in `common/culture/traditions/`. Thematic shortlist: `tradition_equal_inheritance tradition_female_only_inheritance tradition_festivities tradition_xenophilic tradition_poetry tradition_culture_blending tradition_religion_blending tradition_esteemed_hospitality tradition_culinary_art tradition_gardening tradition_chanson_de_geste tradition_philosopher_culture tradition_polygamous`.
* **Name list** — write `common/culture/name_lists/tm_name_lists.txt` (spec `_name_lists.info`) and point `name_list` at it.
* **Icons** — faith/rite icons: `gfx/interface/icons/faith/<key>.dds` (100×100). Placeholder is `custom_faith_1`.

## Testing

Launch with `-debug_mode` (console) and optionally `-develop`. In the console:

```
effect = { set_culture = culture:transbian_maximalist }
effect = { set_character_faith = faith:transbian_maximalism }
```

Keep `~/Documents/Paradox Interactive/Crusader Kings III/logs/error.log` open; every missing loc key or bad doctrine key lands there. Run [CK3 Tiger](https://github.com/amtep/ck3-tiger) over the mod folder for static validation.
