# Wave 3: flavour "achievement" events (Deeds of the House)

Roadmap item: "Flavour achievement events, the Pope first". Design: `docs/faith_design.md` §11. The user kept them as dark comedy (§12 revision 8), so Serano's proposed changes (`research/book_serano_whipping_girl.md` row 5: require consent, rename "the Unmaker") are **not** applied. Two of her points are applied because they cost nothing: the new daughter also gets a memory, and the jokes land on the courts' panic, never on the cut or the body (§16 rule 5). The knife makes the body, not the woman (rule 8): the Aunt Bea text says the House calls her a woman, and that she has not said it yet herself.

Status: built, validated by xTiger (no reports in `tm_ach_*` files), **untested in game, and not live until the hook below is added.**

## Files (all new)
- `events/tm_ach_events.txt` (namespace `tm_ach`)
- `common/scripted_effects/tm_ach_effects.txt`: `tm_ach_before_knife_effect`, `tm_ach_after_knife_effect`, `tm_ach_record_effect`, `tm_ach_memories_effect`, `tm_ach_nickname_effect`
- `common/scripted_triggers/tm_ach_triggers.txt`: the targets (Pope, Patriarch, steppe ruler, musician or poet, Muslim lord's councillor), and `tm_ach_house_has_deed_trigger`
- `common/on_action/tm_ach_on_actions.txt`: `on_imprison` (notes a captured vizier), `quarterly_playable_pulse` (Grandmother's House)
- `common/decisions/tm_ach_decisions.txt`: Deeds of the House
- `common/nicknames/tm_ach_nicknames.txt`, `common/opinion_modifiers/tm_ach_opinion_modifiers.txt`, `common/character_memory_types/tm_ach_memories.txt`
- `localization/english/tm_ach_l_english.yml`

## The hook (needs the owner of tm_rite_effects.txt)
The rite fires no on_action, and the old body must be read **before** the knife. Re-embodiment moves its titles to the new body and then kills it, and does not copy council seats or court positions. So `tm_take_the_knife_effect` in `common/scripted_effects/tm_rite_effects.txt` needs two lines:

```
tm_take_the_knife_effect = {
	tm_ach_before_knife_effect = yes
	tm_rise_daughter_effect = { TRAIT = tm_daughter_of_the_knife RENAME = tm_knife.0002 }
	tm_ach_after_knife_effect = yes
}
```

This covers every knife path: the voluntary rite (`tm_knife.0004`), a courtier offered the rite, the Dorley path (`tm_dorley.0100` .a and .b), arrivals raised by the knife, and the debug decision and interaction. The other gates (seiðr, embryo and the rest) are not hooked: §11 names the Rite of the Knife only.

## Framework
- **Officiant** (who earns the deed), set by `tm_ach_before_knife_effect`: on the Dorley path the captor (`root` of `tm_dorley.0100`). For a courtier offered the rite (`tm_rite_offered`) it is her player employer. For a player who takes the knife herself, she earns it, on her new body. It is always a player. AI captors earn nothing.
- **Consent**: the target came to the knife by his own decision. If no player brought him and he was the Pope or the Patriarch, every player of the new daughter's faith gets the deed. This is the rarer Gift Alone deed (§11 design rule). In practice it needs a Pope or Patriarch converted to a Sisters' faith, for example by the call.
- **Records**: a character flag `tm_ach_<deed>_done` on the player (once per lifetime, used by the summary deed) and a house variable `tm_ach_deed_<deed>` (persists across heirs; read by the Deeds decision). A player re-embodied later loses her flags (variables and flags do not cross bodies); the house record stays.
- **Deeds of the House** decision: shown to a player whose house has at least one deed. It opens `tm_ach.0900`, one line per deed.
- **Memories**: `tm_ach_officiated_memory` for the officiant and `tm_ach_risen_memory` for the daughter (1.20 `create_character_memory`, default duration). Not given for consent deeds.
- **Nickname**: given by every deed except the consent ones. It never overwrites "Unmaker of Fathers".

## The deeds
| Event | Target (read before the knife) | Payoff |
|---|---|---|
| `tm_ach.0001` Ioanna Secunda | holds `k_papal_state`, or heads a Christian faith and holds `c_roma`; never a Sisters' faith | Captor: "the Unmaker", +500 prestige, +100 piety, memories, and every ruler of the Pope's faith −40 opinion of her for 30 years ("Catholic hostility for a generation"). An option to adopt her (Daughters Chosen faiths). Consent: +300 piety, its own text. Before 1250 the Sisters call her Joan the Second and "nobody in Rome knows who the first is meant to be". From 1250 the chroniclers' woman pope is mentioned (the legend is first written down c. 1250–80: Jean de Mailly, Martin of Opava; general knowledge, not a repo source, so please check). With re-embodiment the new body keeps the Papal See (step 7 of `tm_reembody_as_woman_effect`), which the text plays straight. |
| `tm_ach.0002` The Keys and the Knife / An Old Custom of the City | Grandmother's House only: the Pope or the Ecumenical Patriarch is a eunuch with vanilla `castrated_me` toward the player (quarterly check) | Triumph text, as that House means it. He is a eunuch "and still a man in his own mind" (§12 rev. 6). "The Unmaker", +30 dread, prestige. For the Pope, the same −40 opinion. Counts toward the summary deed. |
| `tm_ach.0010` The Patriarch's Daughter | holds `k_orthodox`, or heads a Christian faith of Byzantine heritage (not the Pope) | Wry: Ignatios, cut at fourteen, held the throne twice (`research/byz_spencer_hall_gutt_hagiography.md`, `byz_ringrose_perfect_servant.md`). +250 piety ("the old order, restored"); for a captor also "the Restorer", +150 prestige and memories. |
| `tm_ach.0020` Al-Kunduri's Mercy | councillor of a Muslim ruler (`is_councillor_of` employer or liege), or noted at capture by `on_imprison` (5 years) | Send her back: she joins her master's court, he gains a favour hook on the player (§11), +200 prestige. Or keep her: +150 piety. From 1064 his clerks cite Tughril and al-Kunduri: castrated, then kept in office (`research/hist_ayalon_eunuchs_caliphs.md` no. 41, after Ibn Khallikan). "The Merciful". |
| `tm_ach.0030` Gelded Like My Camels + `tm_ach.0031` | a steppe ruler (nomadic government, or a tribal ruler of Turkic or Mongolic heritage) or his son | "Gelder of Khans", +250 prestige. Two months later the camp's judges send an envoy: pay horses and silver (−25 opinion, 10 years) or refuse (−60, 25 years, +50 prestige). The speaker is the khan, or for a khan her primary heir. Tengri faiths call it the cruelty of the southern courts (Terbish p. 24, `research/east_mongol_sex_genghis.md` E26). Not built: a war or casus belli from the judgment. The word *yargu* is not used, since most steppe rulers in game are not Mongol. |
| `tm_ach.0040` Six Hundred Daughters | the house counts 50 daughters of the knife (`tm_ach_knife_daughters`, counted from this version on, for every house, AI included; any knife path) | Every player of the house: "Mother of Fifty", +500 dynasty prestige. From 890 Yang Fugong's six hundred eunuch sons (`research/cn_lo_tunghwa_tang_adoption.md`, Lo p. 26); the Sisters' line is the one drafted there. |
| `tm_ach.0050` The Greater Circumcision | court musician or court poet, or `lifestyle_poet` | Her answer to the court, one of the Medinan singers' three quips of 717 (`research/hist_rowson_mukhannathun.md` §2.8, Rowson p. 691; date per `isl_rowson_gender_irregularity.md`), as option text. "The Greater". |
| `tm_ach.0060` Mother of Mothers Unmade a Father of Fathers | the Pope (any version) and the Patriarch in one lifetime | "Unmaker of Fathers", +1000 prestige, +1000 dynasty prestige. |

These are rite events, not flavour events, so they do not draw on the flavour budget (`tm_flavour_ready_trigger`). They fire only when the rite is done.

The Dorley rules are unchanged: these events only read who the target was. Whether a Pope, vizier or khan's son can enter the programme is still decided by `tm_intake_eligible_trigger` (violent men only).

## Uncertain syntax / engine behaviour
- Saved scopes from `tm_ach_before_knife_effect` must survive through `tm_rise_daughter_effect` to `tm_ach_after_knife_effect` within one effect run, and be carried by `trigger_event` to the deed events. That is the usual CK3 behaviour, and the mod already relies on it (`scope:tm_new_body`).
- Whether a foreign councillor keeps the council seat while imprisoned. Hence the `on_imprison` note; if `on_imprison` runs after the seat is gone, only the before-knife check remains.
- `pay_short_term_gold = { target gold = medium_gold_value }` in `tm_ach.0031`: the vanilla pattern, accepted by xTiger.
- Adopting a landed daughter (the new Pope) with `adopt_effect`: vanilla allows it, and Dorley 0100 .b does the same. How the Catholic faith treats a female head holding `k_papal_state` is vanilla behaviour, not tested.
- `every_ruler` over one faith is a single sweep, run once per deed.

## Test scenarios (TO-TEST style)
1. Hook added. Aunt Bea's House, re-embodiment on. Capture the Pope (console: imprison; give him `wrathful`), Take Into the House, wait for `tm_dorley.0100`. Expect `tm_ach.0001` three days after the knife, with the Dorley text and the pre-1250 line. Expect "the Unmaker", memories on both, Catholic rulers at −40, the adopt option (Daughters Chosen), and the new body holding `k_papal_state`. Set the year past 1250 and repeat for the Joan line.
2. As 1 with re-embodiment off: the same deed, with the old body still Pope.
3. The Patriarch through the Dorley path: `tm_ach.0010`. Then the Pope too: `tm_ach.0060` about ten days after the second deed.
4. Grandmother's House: castrate the Pope (vanilla interaction). Within a quarter, `tm_ach.0002` with the Pope text. Repeat with the Patriarch.
5. Capture the councillor of a Muslim ruler; check the variable `tm_ach_vizier_of`; run the programme. In `tm_ach.0020`, "send her back": she is at her master's court and he holds a favour hook on you. Before and after 1064.
6. A khan's son (nomadic or Turkic tribal) through the programme: `tm_ach.0030`, then `tm_ach.0031` two months later; both options. A khan himself: the envoy speaks for her heir.
7. A court poet or musician through the programme or the offered rite: `tm_ach.0050`, all three options.
8. Six Hundred: set the house variable `tm_ach_knife_daughters` to 49 and raise one more daughter: `tm_ach.0040` to every player of the house.
9. The voluntary rite as a player who holds no notable title: no deed, only the house count rises.
10. Deeds of the House: hidden with no deeds; afterwards it lists exactly the deeds earned.
11. AI captor finishes a Pope programme: no event, no flag, only the house count.

## Ready-to-paste text
README Roadmap: replace "- [ ] Flavour achievement events, the Pope first" with:
"- [x] Flavour achievement events (the Deeds of the House): Ioanna Secunda (the Pope, in three Houses' versions), the Patriarch's Daughter, Al-Kunduri's Mercy, Gelded Like My Camels, Six Hundred Daughters, the Greater Circumcision and Mother of Mothers Unmade a Father of Fathers. Each gives a nickname, memories and prestige or piety, and the Deeds of the House decision lists them (untested in game)."

TODO.md, Content: replace "- [ ] Flavour "achievement" events (post-v1)." with:
"- [x] Flavour "achievement" events (`tm_ach`, docs/wave3/achievements.md). Needs the two-line hook in `tm_take_the_knife_effect`; untested in game."
New section:
"## Deeds of the House (added 2026-10-21, untested in-game)
- [ ] Hook in tm_take_the_knife_effect added; scenarios 1–11 of docs/wave3/achievements.md
- [ ] A foreign councillor's seat while imprisoned (Al-Kunduri)
- [ ] Not built: a war from the steppe judgment; deeds for the other gates; event art"

## Decisions (user, 2026-10-21)

- **Keep "the Unmaker".** Serano's rename (and the consent requirement) is not applied; the deeds stay dark comedy, with the joke on the courts' panic.
- **Grandmother's eunuch Pope counts.** A Pope or Patriarch made a eunuch by Grandmother's House (`tm_ach.0002`) counts toward the summary deed.
- The hook in `tm_take_the_knife_effect` is in (`tm_rite_effects.txt`), so the deeds are live.
