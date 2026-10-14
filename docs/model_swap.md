# Portrait / body-model swap on transition — findings and approach

Question (user, 2026-10-14): when a character completes a transition (the Day of Blood or whatever the rite ends up being), swap the male character model for a female one with similar physical characteristics.

## What the engine does

- **Body mesh is keyed to sex, not DNA.** `common/portrait_types/00_human_types.txt` selects head and torso entities by `sex = male` / `sex = female` (`male_body_entity`, `female_body_entity`, boy/girl variants under 18). Face morph genes (`gene_chin_*`, `gene_eye_*`, etc.) are shared between the sexes; clothing, hair and beard accessory genes have separate `male = { }` / `female = { }` template lists.
- **No scripted effect changes a living character's sex.** Nothing in vanilla script uses one (`set_sex`, `set_gender`, `change_gender` etc. appear nowhere in `common/` or `events/`). Vanilla only sets sex at creation (`create_character = { gender = female }`, `opposite_gender = root`) or during pregnancy (`set_pregnancy_gender`). The one workshop mod called "Change Gender" has been removed from Steam and gave no implementation details.
- **What the eunuch traits actually do to portraits** is small: `special_beardless_eunuch` in `gfx/portraits/portrait_modifiers/99_special.txt` zeroes `gene_body_hair` and removes the beard; `is_eunuch_trigger` adds +200 weight to a hairstyle in `05_hair_situational.txt`. There are no "premade eunuch avatars" beyond that; the trait just filters accessories on the ordinary male body.

So a purely visual route cannot deliver a female body on a character the engine considers male. A portrait modifier triggered by our trait could at most feminise the face (morph genes), strip beard and body hair, and force a hairstyle, with the torso and clothing still drawn from the male lists.

## Two routes

### Route 1 — Visual feminisation (cosmetic, lossless)

A `trait_portrait_modifiers` entry keyed to our transition trait, modelled on the dwarfism entry in `gfx/portraits/trait_portrait_modifiers/00_trait_modifiers.txt`:

- `morph` modifiers nudging jaw width, brow forward, chin height etc. toward feminine means; `gene_body_hair` to 0; beard template removed (reuse `special_beardless_eunuch`).
- A `99_special`-style group adding weight to long hairstyles for the trait.
- Clothing stays male-list because female clothing templates have no male-body mesh variant.

Good as the **immediate** post-rite state (the novice, mid-transition) and as the fallback when Route 2 is undesirable (e.g. unlanded courtiers where state loss does not matter but a sudden new character ID would).

### Route 2 — Re-embodiment (true female model, lossy)

Recreate the character as a woman and move everything across. Every effect below is used by vanilla script (counts are usages in `game/common` + `game/events`):

| Step | Effect | Vanilla precedent |
|---|---|---|
| Create the new body | `create_character = { gender = female age = ... culture = ... faith = ... dynasty_house = ... save_scope_as = new_body }` | 1,000+ uses; `gender = root` / `opposite_gender = root` in travel events |
| Same face | `copy_inheritable_appearance_from = scope:old_body` | 11 uses; the Reincarnation decision (`tgp_decision_events.0200`) copies an ancestor's appearance onto a child |
| Traits | `every_character_trait = { scope:new_body = { add_trait = prev } }` | `every_character_trait` 16 uses; `add_trait = scope:x` 13 uses |
| Faith, culture, house, sexuality | `set_character_faith`, `set_culture`, `set_house`, `set_sexuality` | 194 / 116 / 38 / 100 |
| Resources | `add_gold`, `add_prestige`, `add_piety`, `add_*_lifestyle_xp` with the old values as script values | common |
| Titles | `create_title_and_vassal_change = { type = ... save_scope_as = change }` → `every_held_title = { change_title_holder_include_vassals = { holder = scope:new_body change = scope:change } }` → `resolve_title_and_vassal_change = scope:change` | faction/diarchy effects |
| Court | `set_employer`, `set_realm_capital`, courtiers follow titles | common |
| Player | `set_player_character = scope:new_body` (only if `is_ai = no`) | 30 uses, incl. EP3 adventurer hand-over |
| Retire the old body | `death = { death_reason = death_vanished }` or `remove_character` (29 uses) | `death_vanished` / `death_disappearance` exist in `common/deathreasons/` |

**What is lost or awkward:** memories, secrets, hooks, scheme progress, opinions, relations (friends/lovers/rivals can be re-set with `set_relation_*`), marriages (would need divorce + `marry`), and parentage of existing children (`set_mother = scope:new_body` makes a female parent record; `set_real_father` keeps biology). The character ID changes, which breaks any saved scopes or variables pointing at the old body. Flags and variables can be copied by hand for the ones the mod owns.

**Hidden upside:** the lossiness is thematically defensible. The faith's own texts call unpersoning a sacrament and the rite a death and rebirth ("the Baeddel has died a thousand times"; Rivera's renaming "felt just like being reborn"). The old name is buried, the register is rewritten, the new woman keeps her face.

## Recommendation

Implement both, staged:

1. **On the rite:** add the transition trait, apply Route 1 portrait modifiers immediately (novice look), fire a flavour event.
2. **On "completion"** (a follow-up event some months later, or immediately for AI courtiers): run the Route 2 scripted effect `tm_reembody_as_woman_effect` (draft in `common/scripted_effects/tm_scripted_effects.txt`). Gate it behind a game rule so players who prefer the cosmetic-only version can opt out.
3. Treat children via the faith's own mechanic: the new body adopts them (vanilla `adopt_interaction` path), which is the matrilineal story anyway.

## Open checks before scripting for real

- Generate the authoritative effect/trigger docs in-game (`script_docs` in the console writes `effects.log`, `triggers.log` and `event_targets.log` to `~/Documents/Paradox Interactive/Crusader Kings III/logs/`) and confirm `create_character` parameters (`gender`, `dynasty_house`, `age`, `random_traits = no`) and whether anything newer than 1.19 added a sex-change effect.
- Verify `copy_inheritable_appearance_from` copies enough (it copies inheritable genes only; accessories regenerate for the new sex, which is what we want).
- Decide the trait's `inheritance_blocker` behaviour: vanilla `eunuch_1` blocks all inheritance; our trait must not, or adoptive succession cannot work.
