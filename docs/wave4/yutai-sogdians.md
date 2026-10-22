# Wave 4: Yutai Dao and the Sogdians of Dunhuang (`tm_yt3`)

Source: de la Vaissière, *Sogdian Traders* (2005), read in `docs/research/cn_vaissiere_sogdian_traders.md` (design rows 4–6, guardrails §9). Not tested in game. ck3-tiger: no reports in the new or changed files.

## What was built

### 11a. Hide the Name (`tm_yt3_hide_name_decision`, `tm_yt3.0001`)
After An Lushan's revolt "the hu began to hide their origins" (p. 220). In 756 the Li Baoyu family changed its surname from An to Li, back through four generations (p. 221). Others claimed Guiji as their birthplace. Guiji was a famous southern city, and also the old name of Changle near Dunhuang, thought to be An Lushan's ancestral home (p. 221). Families whose loyalty was proven kept their descent openly, like He Wenzhe (p. 222).

- **Who.** A member of the Way (`faith:tm_yutai`), adult and free, who is not an independent ruler and has not hidden her name already, and who is either:
  - of Sogdian heritage (Sogdian culture, or a Sogdian parent) under a liege who is not Sogdian; or
  - a daughter or declared sister (`tm_world_daughter_trigger`) at a hostile court. That means a liege of another faith whose faith is hostile to hers (hostility at least `faith_hostile_level`) or who has −20 opinion of her or worse, or that she lived through the 903 purge in the last few years.
- **How.** A decision with a 10-year cooldown (the AI checks every 120 months: craven, paranoid, shy and a hostile court raise it; brave or arrogant characters never take it). A palace daughter who lived through the 903 purge is also offered the event once, 30–180 days after next year's pulse, until 910. That call is in `tm_yt2_yearly_effect`.
- **Description by case.** After the purge (until 910); Sogdian heritage from 756 (the An Lushan text: the An who became Li, back through four generations); Sogdian heritage before 756 (generic: no revolt, no date); otherwise a daughter at a hostile court ("I will not hide what I am. Where I came from is another matter.").
- **Options.**
  - (a) A new family name written back through four generations: −50 prestige; she hides the name.
  - (b) Another birthplace in the register: 25 gold; she hides the name. From 756, for Sogdian heritage, the text is "we come from Guiji". 15% chance a clerk notices, for −25 prestige; the Sogdian text is "a clerk knew that Changle was once called Guiji".
  - (c) Stand on my record (councillor, knight, or liege opinion of her at 50 or more): +25 prestige. Nothing is hidden.
  - (d) Keep the name: +10 piety.
- **Keep Quiet in This Land is reused, not copied.** `tm_yt3_hide_name_effect` sets `tm_yt3_name_hidden` (a permanent record) and the Keep Quiet variable `tm_world_keep_quiet`, unless she already has it. So every existing effect applies unchanged. Hostile `tm_world` events are half as likely to single her out (`tm_world_keeps_quiet_trigger`), she can't be Elder Sister (`tm_elder_sister_eligible_trigger`), and **Speak Aloud Again** (`tm_world_speak_aloud_decision`, shown whenever she has the variable) ends it. The name in the register stays written: speaking aloud does not bring back the decision.
- **Where Keep Quiet lives:** in `tm_world_*`, not `tm_mech_*` (`common/decisions/tm_world_decisions.txt`, `common/scripted_triggers/tm_world_triggers.txt`). No change is needed there. An optional comment line is in "Changes for other files" below.
- The source's disguise hides descent, not gender. The event hides only her origins; a daughter never hides what she is.

### 11b. The banquet at the Cao inn (`tm_yt3.0010`)
A she circular of 973 calls the members to the year-end banquet "at the inn of the Cao family". A third of its fifteen members were An or Cao, the head and the assessor among them (p. 324; S. 2894v). The Sogdian families of Conghua went on marrying among themselves into the 10th century (pp. 323–324).

- **Who and when.** A landed ruler of the Way who holds a Sisters' House in a county of de jure `k_hexi` (Shazhou, Guazhou, Ganzhou, Liangzhou and the rest of the Gansu corridor), from 900. The chance is 4% a year with a 15-year cooldown, under the flavour budget. Fired from `tm_yt3_yearly` (`yearly_playable_pulse`).
- **The scene.** The street's society, which the House belongs to, sends its circular. Fifteen names; five are An or Cao, and the head is one of them. The House pays its own society's dues at every birth and burial, which ties the event to `tm_yutai.0040` (the burial society) and the House strain used by `tm_yutai.0030`/`0040`.
- **Options.**
  - (a) Bring the flour, and bring the neighbours' daughters into our own society: 10 gold, +10 piety, House strain −1 on each House she holds. 50% chance a neighbour's daughter (Sogdian culture, 16–30) joins the court with +20 opinion. She **keeps her own faith**: the county's, or Mahayana if the county is of the Way. Only the normal call can reach her.
  - (b) Go, and keep our society to the House: +5 piety.
  - (c) Hold the banquet at the House: 25 gold, +30 prestige, House strain −1.
- The *xian* temple is not shown, and no neighbour is made a member. Neighbours stay neighbours (note §9).
- **Date:** from 900, not from 914 (the Cao period of the Guiyijun) as the note's row 5 suggested. The inn's Cao are a Sogdian family of the town, not the ruling Cao. Gating the event on the ruling clan would imply a link that the note does not make.

### 11c. Miunai's Road (`tm_yt3.0020`, "No Reply from There")
Modelled on the Ancient Letters (c. 313): Miunai abandoned at Dunhuang by her husband, a kinsman fled from his debts, the fear of having to "enter into service with the Chinese", a camel promised by a priest so she could join a caravan, and women who perhaps could write (pp. 47, 56–57 and n. 37, 188).

- **The story is set in the game's present.** The letters lay sealed in a guard tower from c. 313 until Stein found them in 1907, so no one in 867 can know them, and the faith cannot tell her story. The woman is a woman of the game's own time in the same straits. Miunai is never named in loc. The name appears only in comments and in this note, as the source of the model. She is never a member of the Way, Marked, or a sister.
- **Who and when.** A landed ruler of the Way whose capital is in de jure `k_hexi`, or who holds a House there. The chance is 2% a year, 3% with a House in Hexi, with a 25-year cooldown and the flavour budget. Any date.
- **Who she is.** Sogdian culture, 24–40, learning 6–12. If any landed Sogdian ruler of another faith exists, that ruler's court is her mother's people (`scope:tm_yt3_kin_court`) and she shares its faith. Otherwise she takes the county's faith, or Mahayana if the county is of the Way.
- **Options.**
  - (a) A camel and a place in the next caravan west: 25 gold, +15 piety. She joins her kin's court, and its ruler gets +15 opinion (grateful). With no kin court, she goes west and takes her chances on the road (she stays in the pool).
  - (b) Lodger of the House: she joins the court with +20 opinion and keeps her faith; +5 piety.
  - (c) A clerk for the court's letters west (her learning 8 or more): she joins the court with +30 opinion; +15 prestige.
  - (d) We cannot help her: −10 piety (the AI almost never chooses it when it has 25 gold).
- The "service in a stranger's household" line comes from the letters' fear. The narrator does not cast Chinese households as hostile. The creditors are not described or given a people: no moneylender NPC.

## Not built (by rule)
- No Sogdian moneylender or usurer, as an NPC type or in text (note §9).
- No massacres of 755–763, and no Beijing "large noses" scene (p. 220).
- No house renaming in script. Option (a) of Hide the Name is abstract (prestige and the hidden flag). Renaming a house or making a cadet house for one member would touch her whole family and its succession, and many members are lowborn courtiers with no house at all.
- Note rows 1–3, 7 and 8 (Master of the Caravan, Rallied Township, Sabao to Office, the Network's Post, the Town of the Grape) are not part of this item.

## Files
- New: `common/scripted_triggers/tm_yt3_triggers.txt`, `common/scripted_effects/tm_yt3_effects.txt`, `common/decisions/tm_yt3_decisions.txt`, `common/on_action/tm_yt3_on_actions.txt`, `events/tm_yt3_events.txt`, `localization/english/tm_yt3_l_english.yml`.
- Changed: `common/scripted_effects/tm_yt2_effects.txt`. `tm_yt2_yearly_effect` offers `tm_yt3.0001` once after the 903 purge.

## Uncertain syntax
- `kingdom ?= { this = title:k_hexi }` from a county (`kingdom` is the de jure kingdom link). ck3-tiger accepts it.
- `learning = { 6 12 }` inside `create_character` (the min–max form of vanilla templates). ck3-tiger accepts it.
- `save_temporary_scope_as` at the top of scripted triggers, used instead of `root` so that the eligibility trigger also works from the global pulse (`tm_palace_yearly`, where root is none). Vanilla uses `save_temporary_scope_as` inside triggers (`00_courtier_guest_management_triggers.txt`).
- `faith_hostility_level = { target = … value >= faith_hostile_level }` with the script value name; vanilla compares against `faith_evil_level` the same way.
- `random_ruler` filtered on Sogdian culture: a loop over every ruler, but the event fires at most every 25 years per ruler.
- The faith key `faith:mahayana_faith` (1.20 `faith_types/00_faith_types.txt`).

## Test scenarios (TO-TEST style)
- **Hide the Name, Sogdian.** Make a courtier of the Way of Sogdian culture under a Han lord (`set_culture` in the console). The decision *Hide the Name* shows. Take (b): the Guiji text appears, 25 gold goes, and she now has `tm_yt3_name_hidden` and `tm_world_keep_quiet`. *Speak Aloud Again* shows. Use it: Keep Quiet ends, `tm_yt3_name_hidden` stays, and *Hide the Name* does not come back.
- **Hide the Name, hostile court.** A daughter of the Way under a lord whose faith is hostile to the Way (or one with −20 opinion of her). The decision shows, and the court description appears. Option (c) shows only if she is a councillor or knight, or her liege has 50 opinion of her or more.
- **Not shown.** An independent ruler, a member of the Way who is not Sogdian under a friendly lord, or a Sogdian member under a Sogdian lord: no decision.
- **After 903.** Hold a palace seal on 903.2.1 (`tm_palace.0003`). In 904 the yearly pulse should bring `tm_yt3.0001` once, with the purge text, provided she is still under a liege.
- **Banquet.** Rule Shazhou with a Sisters' House after 900, and fire `tm_yt3.0010` (use `scope:tm_yt3_house_county` or let the pulse fire it: about once in 25 years). Option (a): the House strain drops by 1, and half the time a Sogdian woman of the county's faith joins the court. She is not of the Way.
- **Stranded woman.** Fire `tm_yt3.0020` as a Shazhou ruler of the Way. If any Sogdian ruler exists (Transoxiana in 867), (a) sends her to that court and that ruler's opinion rises by 15. Option (c) shows only if her learning is 8 or more. She never has the Way's faith.
- **Budget.** Neither 0010 nor 0020 fires while `tm_flavour_cooldown` is set.

## Changes for other files (not mine)
- Optional, comment only, `common/scripted_triggers/tm_world_triggers.txt` above `tm_world_keeps_quiet_trigger`: add the line
  `# Also set by Hide the Name (tm_yt3_hide_name_effect, tm_yt3_effects.txt), for members of the Way who hide their origins.`
  No script change is needed: Keep Quiet's variable, trigger and Speak Aloud decision work as they are.

## Ready-to-paste text

**README, Yutai Dao, after "The palace offices" bullet:**
- **Neighbours from the west.** At Dunhuang the Sogdian families of the old merchant towns sit in the same street societies as the House. A year-end circular may call the sisters to a banquet at the Cao family's inn, and the House may open its own society to the neighbours' daughters, who keep their own faith. A woman of a merchant family, stranded far from home with no reply to her letters, may come to the House for a camel and a caravan west. Since An Lushan's revolt, families from the west have hidden their names: a member of the Way of Sogdian heritage, or a daughter at a hostile court, may *Hide the Name*, writing a new surname or another birthplace in the register and keeping quiet in this land.

**TODO, new heading "Wave 4" or under Yutai Dao:**
- [ ] Yutai and the Sogdians (`tm_yt3`, docs/wave4/yutai-sogdians.md): *Hide the Name* (decision and `tm_yt3.0001`, reusing Keep Quiet's variable; offered once after 903), the banquet at the Cao inn (`tm_yt3.0010`, Hexi, from 900), No Reply from There (`tm_yt3.0020`, after the Ancient Letters). Not built: Vaissière rows 1–3, 7, 8 (Master of the Caravan, Rallied Township, Sabao to Office, the Network's Post, the Town of the Grape).

**TO-TEST:** the scenarios above, as a new subsection under Yutai (§M or similar).
