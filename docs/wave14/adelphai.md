# Adelphai Dorleyaiou, wave 14: the Founding Rule, and the rest of the Dorley precedent

Roadmap item (README, "Still to do"; `docs/TODO.md`, Stage 2 inputs): "the founding charter as a house legacy; the Dorley precedent's disclosure, ward schooling, and washouts sent to a holy order". Built 2026-10-28, untested in game. Namespace `tm_dl6`.

**New files** (all with a BOM): `events/tm_dl6_events.txt`, `common/scripted_effects/tm_dl6_effects.txt`, `common/scripted_triggers/tm_dl6_triggers.txt`, `common/decisions/tm_dl6_decisions.txt`, `common/modifiers/tm_dl6_modifiers.txt`, `common/opinion_modifiers/tm_dl6_opinion_modifiers.txt`, `common/on_action/tm_dl6_on_actions.txt`, `common/script_values/tm_dl6_values.txt`, `localization/english/tm_dl6_l_english.yml`.

**Small edits to existing Dorley files** (each one line or one option):

1. `common/scripted_effects/tm_dorley_effects.txt`, `tm_begin_programme_effect`: one line, `tm_dl6_intake_effect = yes`, after the sponsor is set. It adds the kin's grievance and the dread, and schedules the disclosure.
2. `events/tm_dorley_events.txt`, `tm_dorley.0100`, options a and b: one line each, `tm_dl6_begin_ward_years_effect = yes`, after `tm_dorley_sponsor_reward_effect`. This starts the second and third years.
3. `events/tm_dorley_events.txt`, `tm_dorley.0200`: one new option, *Give him to the order*. It sits between the existing *friends of the House* option and Grandmother's House's execution option. Nothing else in the event changed.

No shared file was touched (`tools/census_report.py`, `docs/TO-TEST.md`, `docs/TODO.md`, `README.md`, `descriptor.mod`, `tm_house_*`). The text to paste is at the end.

**Validation.** xTiger: 23 reports, identical to the baseline, none in `tm_dl6` or the edited Dorley files. `tools/check_glyphs.py`: clean.

---

## 1. The Founding Rule of the Mother House

### Shape: a title variable and a decision, not a dynasty legacy

Vanilla legacies can be gated. `common/dynasty_legacies/_dynasty_legacies.info` gives a track an `is_shown` trigger, and `95_fp3_legacies.txt` gates the Khvarenah track on the dynast's heritage, with `can_be_picked` on each perk. A track could have been shown only to dynasts of `faith:transbian_maximalism`. It was rejected for four reasons:

- **Wrong owner.** The research note's correction (`research/byz_thomas_hero_typika.md`, design table row 1) is that the Kecharitomene typikon does not pass the convent to a family. The convent is "independent and under its own control" ([1], p. 667). The founder's female line inherits only the *protection* (the ephoreia, [80], p. 709), and the protectress may not touch property, admissions or the rule ([3], p. 669). A dynasty legacy would make the charter family property. The Mothers of Mothers are adopted and come from many houses, so it would also drop out of the faith's hands the first time the title passed outside one dynasty.
- **The gate leaks.** A track stays shown once its first perk is unlocked (`.info`: "Always shown if the legacy's first perk is unlocked"). Its `character_modifier` then applies to every member of the dynasty, whatever their faith, and keeps applying after the dynasty converts. `faith_character_modifier` can narrow a perk only by *doctrine*, and the Adelphai have no doctrine of their own that a perk could key on cleanly.
- **Legacy triggers cannot call scripted triggers** (`.info`: it "will cause CTD during launching"), so the faith's own triggers could not be reused.
- **Currency.** Renown accrues to large dynasties. The faith's line runs by adoption into small, scattered houses, and observe runs show it holding few rulers (`docs/wave8/adelphai.md`).

**Built instead.** The rule is a variable on the title `d_tm_mother_house`, so it passes from Mother to Mother with the House, whatever her family. It is written in three stages through one decision, *The Rule of the Mother House* (`tm_dl6_rule_decision`). The decision is open to the holder of `d_tm_mother_house` while she keeps the faith. Its modifiers are kept current once a year (`tm_dl6_yearly_rule`, `tm_dl6_rule_upkeep_effect`). This is the shape the research note proposed as a "legacy track" (row 12), built where the typikon puts it.

### Source per stage

| Stage | Typikon provision | In game |
|---|---|---|
| 1. The rule read aloud | The typikon is read aloud to the nuns each month ([65], [77]; note row 12). Lips set a three-year novitiate, and every founder's rule sets out who keeps the house and how its superior is chosen (note §1.1, §1.3) | Event `tm_dl6.0100`: the Mother writes the rule and picks its opening clause. Every Sisters' House of the faith gets **The Rule Read Aloud** (county: +5 county opinion, +5% development growth) |
| 2. Three copies | Kept in three copies: Hagia Sophia, the convent's sacristy, and the protectress ([65], [77]; note row 12) | Event `tm_dl6.0101`: the second copy goes to the City (50% "lodged", +75 prestige; 50% "came back unopened", +10) or to Pessinus (+50 piety). Every living Protectress of a House of the faith gets **Keeper of the Rule's Copy** (+1 diplomacy, +0.2 prestige a month), which moves when the office passes |
| 3. Sealed | Cannot be amended "not even at a critical moment" ([3]; note row 12) | Event `tm_dl6.0102`: seal as it stands (+50 piety) or add the fall-back clause first (+50 prestige). Each Mother of Mothers in turn gets **The Rule Sealed** (+0.5 piety a month, +5 same-faith opinion). It moves to the next Mother on succession |

**Clauses.** The opening clauses are the note's in-world lines (§3), in the Sisters' own voice:
- (a) "Where this rule says sister, every daughter is meant, however she came to us." This inverts the gender clause of [79]. It also answers the Dorley path: a daughter raised from the cells is a sister like any other.
- (b) "No one is bought into this House, and no one buys her way." After [7]: admission "as a gift … without any gift".
- (c) "She who protects a House shall keep it, not own it." After [3].

The stage-3 fall-back clause is the note's line after [80]: "As long as the line of daughters lasts; and when it fails, let the sisters choose." The clause chosen at stage 1 is stored as `tm_dl6_rule_clause` (flag `every`, `gift` or `keep`) and quoted again at the seal.

The narrator never names Irene Doukaina or the Kecharitomene. The rule echoes "the founders' rules", and the faith claims no empress (writing rule 19 and the README's rule on historical figures).

The stage-3 seal text says the sealed rule binds the House, not the sisters: "Any sister may still leave it" (rule 23, no oath of permanence).

### Numbers

- Cost in piety: 150 for stage 1, 250 for stage 2, 350 for stage 3 (`tm_dl6_rule_cost`).
- At least ten years between stages (`tm_dl6_rule_cd` on the title).
- AI: checks every 60 months; base 40, +20 zealous, +20 learning ≥ 12; never if her piety is below the cost plus 100.
- "A House of the faith" (`tm_dl6_adelphai_house_trigger`): a county with `tm_house` whose county faith, lord or Elder Sister is Adelphai. A House under a tolerant lord of another faith still hears the rule.

---

## 2. The disclosure (`tm_dl6.0001`)

**Source.** In the serial the sponsor decides when to tell her charge that the sponsors are themselves graduates (`docs/dorley_precedent.md`, "Sponsors"; Dorleybase, "Sponsor").

**In game.** At month 7 of the programme, between the second and third levers (`tm_dorley.0010` fires at 3, 6 and 9 months), the captor is asked. The event only fires if the novice is still in the cells with `tm_novice` and the sponsor is a daughter of any faith's gate.

The House's adaptation: in the mod, a sponsor is any daughter at the court, not only a graduate of the cells. So the disclosure says that every woman who feeds and teaches him "has been under the knife he is waiting for". A line is added when the sponsor herself came up from the cells (`tm_dl6_graduate`). She is never described as having been a man (writing rule 8).

| Option | Effect |
|---|---|
| Tell him | 60 (+15 if he is Marked, +10 if the sponsor has diplomacy ≥ 12): progress +2. 40 (+20 if stubborn): progress −1 and +25 stress. Sponsor −10 stress |
| Not yet. Let him come to ask | No change; the sponsor carries it (+10 stress) |
| Let him see them, one evening, "with a sister at the door" (only if the captor holds a House) | Progress +1 |

Progress decides the knife (≥ 3) or washout after the third lever, as before. So the disclosure can tip a novice either way.

**Honesty.** The closing paragraph: "He may hear it as a promise. He may hear it as a threat. It is both … he did not choose this cell, and nothing said to him in it makes that otherwise."

### The crime, kept visible (`tm_dl6_intake_effect`)

At intake, every close family member of the novice who is not of the captor's faith gains **Took Our Kin into the Cells** toward the captor: −30, decaying over 20 years. The captor gains +5 dread. The vanilla imprisonment opinion ends when he leaves the cell; this one does not. That keeps the path a crime in the eyes of every other faith (dorley_precedent.md, last section) without making persecution a mechanic. It is opinion only: no war, no antagonist.

---

## 3. Ward schooling, years two and three (`tm_dl6.0010`, `0020`, `0030`)

**Sources.**
- The programme's second and third years are spent above ground, under the sponsor (dorley_precedent.md, "Three years"). In year two the room is still locked.
- The sponsor's role "develops from manipulator to mentor. She becomes the new girl's 'Sister'" (Dorleybase, "Sponsor", via dorley_precedent.md). Serano row 7 (`research/serano_blog_essays.md`) keeps *manipulator* out of the faith's voice, so the events say keeper, teacher, sister.
- The period anchors: Lips gave outsiders a three-year novitiate (Constable, p. xxi; typika note §1.1). The Medina novices were "given in charge to their elder brethren … then set up their own establishments" (Marmon p. 105; dorley_precedent.md, historical anchors).

**What changed at the knife.** `tm_dorley.0100` used to release the new daughter at once. A released prisoner from another court goes back to it. Now `tm_dl6_begin_ward_years_effect`:
- adds her to the captor's court (unless she is a ruler or already there);
- records her sponsor (`tm_dl6_sponsor`; the captor, if the sponsor is gone or was the captor);
- gives her **In Her Sponsor's Care** for two years (+25% lifestyle experience, +20% stress loss);
- starts the chain. The rename at the knife (`tm_knife.0002`, "A New Personal History") is unchanged and is not repeated.

**Year two, *The Upper Rooms*** (`0010`, 12 months after the knife). "The door at the foot of the stair is still locked at night. Nobody calls that freedom." The schooling is one of three:
- letters and the Psalter (learning);
- the House's accounts (stewardship);
- the courtesies of the hall (diplomacy).

The ward gets +1 skill, +150 lifestyle experience and −10 stress. The sponsor gets +75 experience in the same line. The AI chooses by the ward's own aptitude. Rule 7 (a road to standing that is not holy office): two of the three are not religious.

**Year three, *Keeper, Teacher, Sister*** (`0020`). The stair door is open now. The daughter answers her sponsor, and either answer is "an honour to the one who hears it":
- she asks her to be her sister: the `tm_sister` relation (Sister-Making's own);
- she keeps her as her teacher: **Teacher and Pupil**, +20 both ways for 20 years.

If the sponsor has died, the daughter lights a lamp for her (+10 piety).

**End of year three, *Her Name in the House's Book*** (`0030`). The text says plainly that she was brought down into the cells without asking, "and nothing the House has given her since makes that otherwise. The Gift Alone would say so, and would be right." Then she chooses:
- written as she tells it: **Written in the House's Book** (+1 diplomacy, +0.1 prestige a month) and +50 prestige;
- written in full, "the cells too, for the next one to read": the same modifier, +50 piety for her and +25 for the captor;
- she leaves the House. She is let go to another House or the road (`tm_send_on_effect`) with **Let Me Go Freely** (+15 for 10 years toward the captor). "No one goes after her." This is rule 23: stepping back is honoured.

A graduate keeps `tm_dl6_graduate`. If she later sponsors a novice, the disclosure says she came up from the same cells.

**Lapse.** Each of the three events checks that she is alive, free and still at the captor's court. If not, the chain ends quietly (`on_trigger_fail`): her markers are cleared and `ward_lapsed` is counted.

---

## 4. Washouts given to an order (`tm_dorley.0200`, new option; `tm_dl6.0210`)

**Sources.**
- dorley_precedent.md, "Washout" and the proposed mapping step 5: "hand-over to … a holy order … of the faith".
- beliefs H43: "monastic expulsion … as veneer".
- Raha and van der Drift rows 6 and 10 (`research/book_raha_vdd_trans_femme_futures.md`): the washout "is handed to a holy order" and "never kills".
- Byzantium castrated and tonsured rivals instead of killing them (Tougher 2008, p. 140, the sons of Leo V made monks on Prote; `research/hist_tougher_eunuch_byzantine.md`, P30 and "Exile to Prote").
- Entering religion was "a second baptism" (Constable, p. xv).
- The Kecharitomene staffed its estates with eunuchs "around the convent", while the enclosure was "closed even to eunuchs themselves" ([14], [15], [80]; typika note §1.4).

**In game.** The option *Give him to the order* (`tm_dl6_give_to_order_effect`) releases him and sends him to:
1. the leader of a holy order of the faith, if one stands. A monastic order is ten times likelier than a military one;
2. otherwise, the Mother of Mothers' court, as one of the House's **lay order at the gate**. These are men who work its estates and roads "outside the wall", as the Kecharitomene kept its eunuch steward and priests;
3. with no Mother of the faith, the captor's own court, on the same terms.

He gets **Given to the Order** (+0.2 piety a month, −10% stress gain) and keeps `tm_washout`. The captor gains +15 piety. The AI weights the option 100, +50 if compassionate, +50 if the faith has a holy order.

In three to five years, on the flavour budget, **Word from the Order** (`0210`) comes back:
- 60: he keeps the hours and says little. "The letter does not say he has changed, and the Sisters do not ask it to."
- 25: he asks to come to a House's door as a friend. The captor may grant the House's friendship.
- 15: he has left. "He walked out of the gate with his cloak and a loaf, and no one went after him."

**Guardrails.**
- No killing, torture or pain on screen. He is not watched.
- The serial's idea of deniable operatives who kill the former patrons is not built.
- He is not made a monk by force (no `devoted` trait). The order is somewhere he is sent, and he may leave.

---

## 5. Counting

`tm_dl6_tally_effect` keeps run-wide globals `tm_dl6_n_<what>`:

| Group | Tallies |
|---|---|
| Rule | `rule_1`, `rule_2`, `rule_3`, `copy_city_kept`, `copy_city_returned` |
| Intake and disclosure | `intakes`, `disclosed`, `disclosed_turned`, `disclosed_shaken`, `disclosure_waited`, `disclosure_shown` |
| Wards | `wards`, `ward_letters`, `ward_accounts`, `ward_hall`, `ward_lapsed`, `sisters_made`, `sisters_declined`, `sponsor_gone`, `graduated`, `book_her_word`, `book_all_of_it`, `stepped_back` |
| Order | `order_holy`, `order_gate`, `word_kept`, `word_asks`, `word_left`, `order_friend` |

---

## 6. Not built, and why

- **The serial's deniable operatives** who kill former patrons: excluded by the content rules (no violence; Raha and van der Drift row 10).
- **A pain test, or a washout by stress**: rule 22.
- **Protectress succession sealed to the line** (note row 12, tier 3: "can never pass outside the line"). This needs a change to the shared `tm_house_name_protectress_effect`. The stage-3 clause records the fall-back in text only.
- **A House holding a copy is harder to close.** It would need two lines in `tm_house.0050`'s AI weights (as wave 8 did for the tower). That file is shared, so this wave leaves it alone. Proposed: `modifier = { add = 20 scope:tm_house_county = { has_variable = tm_dl6_copy_keeper } }` on *Let it stand*, and the same −20 on *Close it*.
- **Charistike and "Declare the House Self-Governing"** (note row 5): a separate era arc (before and after c. 1080), not part of the charter itself.
- **A real holy order founded for the faith.** Creating one needs a leased barony (`create_holy_order` from the vanilla decisions). The lay order at the gate stands in when the faith has none.
- **Graduates preferred as sponsors.** `tm_begin_programme_effect` still picks a random daughter at court. One weight line could prefer `tm_dl6_graduate`.
- **Event art**: the placeholders follow the existing pattern.

## 7. Open decisions for the user

**User, 2026-10-28:** (1) keep Grandmother's House execution option as it is; (2) keep the lay order as the fall-back; (3) no date gate for the seal (the event plays without one); (4) staying at the captor's court is intended; (5) sizes accepted; (6) README table reworded to "A founding rule the House keeps, not owns".

1. **Grandmother's House execution option** in `tm_dorley.0200` (*There is nothing left to save*). It predates this wave (Serano row 7 kept it for Grandmother's House only). This wave's brief says washouts get no execution option. Remove it, or keep it as the condemned regime's one on-screen cruelty? It was not touched.
2. **The lay order at the gate** as the fall-back when the faith has no holy order. The alternative is to show the option only when a real holy order exists, which in practice the Adelphai seldom have.
3. **Date gate for the rule.** The Kecharitomene dates from 1110–16, and its female-line clause from the 1120s (Gautier, p. 14). The Sisters' rule is modelled on the genre, not on that text, so it has no gate. Gate stage 3 at 1120 if that reads as an anachronism.
4. **Behaviour change at the knife.** A daughter raised on the Dorley path now stays at the captor's court for her ward years, where before she was released and probably went home. Is that intended?
5. **Sizes:** the kin's −30 for 20 years and +5 dread; the disclosure's 60/40; the rule's costs (150/250/350 piety) and its small modifiers.
6. **The README comparison table** says "A founding charter passes land to adopted daughters". The typikon reading says the rule passes protection, not land. Reword it to "A founding rule the House keeps, not owns"?

## 8. Uncertain syntax (check in game)

- `every_close_family_member` on a prisoner from another court, and `add_dread` from an interaction's effect chain.
- `release_from_prison` followed by `add_courtier` in the same effect (the ward, and the washout to a holy order's leader).
- `random_faith_holy_order` with `weight` and `leader ?=`; `add_courtier` on a holy order's leader.
- `on_trigger_fail` in the ward events.
- Saved scopes (`tm_dl6_ward`, `tm_dl6_sponsor`) carried across three 12-month `trigger_event` hops.
- `var:tm_house_protectress ?= var:tm_dl6_copy_keeper`, and `faith =` on a county title in `tm_dl6_adelphai_house_trigger`.
- The decision for a landless Mother of Mothers. Does the AI weigh it? If not, observe runs will show `rule_1` stuck at 0.

---

## Ready to paste

### (a) `tools/census_report.py`, after the "Adelphai: the Tower on the Condition" block

```python
    # Adelphai, wave 14 (tm_dl6_tally_effect): the Founding Rule, and the rest of the Dorley precedent.
    print('== Adelphai: wave 14 ==')
    dsteps = ('rule_1', 'rule_2', 'rule_3', 'copy_city_kept', 'copy_city_returned', 'intakes', 'disclosed',
              'disclosed_turned', 'disclosed_shaken', 'disclosure_waited', 'disclosure_shown', 'wards', 'ward_letters',
              'ward_accounts', 'ward_hall', 'ward_lapsed', 'sisters_made', 'sisters_declined', 'sponsor_gone', 'graduated',
              'book_her_word', 'book_all_of_it', 'stepped_back', 'order_holy', 'order_gate', 'word_kept', 'word_asks',
              'word_left', 'order_friend')
    print('  '.join(f'{s} {int(gvars.get(f"tm_dl6_n_{s}") or 0)}' for s in dsteps))
    print('rule_*: stages of the Mother House\'s rule written (read aloud, three copies, sealed); copy_city_*: the second\n'
          'copy lodged in the City or sent back; intakes: men taken into the Dorley cells; disclosed / _turned / _shaken:\n'
          'told that the sponsors were under the knife, and how he took it; disclosure_waited / _shown: not yet, or an evening\n'
          'at the House\'s table; wards: daughters raised from the cells into their ward years; ward_letters / _accounts /\n'
          '_hall: the second year\'s schooling; ward_lapsed: chains that ended early; sisters_made / _declined / sponsor_gone:\n'
          'the third year\'s answer; graduated (book_her_word / book_all_of_it): written into the House\'s book;\n'
          'stepped_back: left the House at the end; order_holy / _gate: washouts given to a holy order of the faith, or to\n'
          'the lay order at the Mother House; word_*: the letter years later (keeps the hours, asks for the door, left);\n'
          'order_friend: given the House\'s friendship.')
    print()
```

### (b) `docs/TO-TEST.md`

Heading: `## AQ. Adelphai: the Founding Rule and the rest of the Dorley precedent (wave 14, added 2026-10-28, untested in-game; docs/wave14/adelphai.md)`

- [ ] **AQ1. Intake.** As an Aunt Bea's House ruler, take a violent prisoner from another faith's court into the cells. His close kin of another faith show "Took Our Kin into the Cells" (−30) toward you; your dread rises by 5. `intakes` counts.
- [ ] **AQ2. The disclosure.** With a daughter at court as sponsor, `tm_dl6.0001` fires about 7 months after intake (after the second lever). Check all three options. Option c shows only if you hold a Sisters' House. A sponsor with `tm_dl6_graduate` adds the "same cells" line. With no daughter as sponsor (the captor is not a daughter), it does not fire.
- [ ] **AQ3. The knife, then the ward.** Let a novice reach the knife (`tm_dorley.0100`), both options, with re-embodiment on and off. The new daughter is a courtier of yours (not back at her old court) with **In Her Sponsor's Care**, `tm_dl6_ward` and `tm_dl6_sponsor`. `wards` counts.
- [ ] **AQ4. Year two.** 12 months on, `tm_dl6.0010`: each option gives +1 skill and experience to her and experience to the sponsor. The sponsor portrait is hidden if she has died.
- [ ] **AQ5. Year three.** `tm_dl6.0020`: (a) sets `tm_sister` both ways; (b) Teacher and Pupil both ways; (c) shows only when the sponsor is dead. A sponsor who died after year two is not shown as alive.
- [ ] **AQ6. The book.** `tm_dl6.0030`: (a) and (b) give **Written in the House's Book** and `tm_dl6_graduate`; (c) sends her to another House or the pool with Let Me Go Freely. The ward modifier and variables are gone after each.
- [ ] **AQ7. Lapse.** Move the ward to another court (or imprison her) before a step: the event does not fire, her markers clear, and `ward_lapsed` counts.
- [ ] **AQ8. Washout to the order.** Force a washout (`tm_dorley.0200`). With a holy order of the faith: *Give him to the order* makes him a courtier of its leader (a monastic one if both kinds exist). With none: he goes to the Mother of Mothers' court. With no Mother of the faith: he stays at yours, released. **Given to the Order** on him; +15 piety to you.
- [ ] **AQ9. Word from the order.** Three to five years later, with the flavour budget ready, `tm_dl6.0210`: three variants. "Left" puts him in the pool. "Asks" offers the friend modifier.
- [ ] **AQ10. The rule, stage 1.** As holder of `d_tm_mother_house` with 150 piety: the decision opens `tm_dl6.0100`. Every Sisters' House county of the faith gets **The Rule Read Aloud**, including a House under a tolerant lord of another faith. A House that closes loses it at the next yearly pulse.
- [ ] **AQ11. Stages 2 and 3.** The decision is greyed out for ten years. Stage 2 gives each Protectress **Keeper of the Rule's Copy**, and the modifier moves when the office passes. Stage 3 gives the Mother **The Rule Sealed**, which moves to the next Mother at succession; the seal text quotes the stage-1 clause.
- [ ] **AQ12. Observe run.** The census "Adelphai: wave 14". Does the AI Mother ever take the decision (`rule_1` > 0)? Are `wards` and `graduated` above 0 when the Dorley path runs at all? Check the error log for `tm_dl6`.

### (c) `docs/TODO.md`

- Under "Content", change `- [x] Dorley path: prisoner interaction, intake trigger, sponsor chain, levers, washout (untested in-game).` to:
  `- [x] Dorley path: prisoner interaction, intake trigger, sponsor chain, levers, washout; the disclosure, ward years and washouts given to an order (wave 14, tm_dl6; untested in-game).`
- Under "Stage 2 inputs from …" (the Adelphai line `daughters in court offices; era decay …; the founding charter as a house legacy`), append: `The founding charter is built as the Mother House's Rule (wave 14, tm_dl6), a title variable, not a dynasty legacy.`
- New section:

```markdown
## Wave 14: the Founding Rule and the rest of the Dorley precedent (added 2026-10-28, untested in-game; docs/wave14/adelphai.md)
- [x] Adelphai wave 14 (`tm_dl6`): the Rule of the Mother House in three stages (read aloud, three copies, sealed); the disclosure at month 7; the ward years (the upper rooms, keeper to sister, the House's book); washouts given to a holy order of the faith or the Mother House's lay order at the gate, with word from the order years later (built, not yet tested in game)
- [ ] Decide (docs/wave14/adelphai.md §7): Grandmother's House execution option in tm_dorley.0200; the lay-order fall-back; a 1120 gate for the seal; daughters now staying at the captor's court after the knife; sizes; the README table's "charter passes land"
- [ ] Not built: protectress succession sealed to the line (shared tm_house effect); copy-holding Houses harder to close (two AI lines in tm_house.0050); charistike era events; graduates preferred as sponsors
```

### (d) README

Paragraph to add to the Adelphai section, after "Daughters are chosen, not born …":

> **The Rule and the cells (wave 14).** The Mother of Mothers may write the Mother House's rule in three parts, years apart, as the founders of convents did. It is read aloud each month in every House, kept in three copies (one with each House's Protectress), and finally sealed "not even at a critical moment" against change. It belongs to the House, not to any family. Under Aunt Bea's House the cells now run their full three years. Some months in, the novice learns that every woman who keeps him has been under the knife he fears. Once raised, the new daughter spends two years above ground as her sponsor's ward: the first behind a stair door still locked at night, the second as her sponsor's pupil and, if she asks it, her sister. Then the House writes her into its book, or lets her go. Those who wash out are given to a holy order of the faith, or to the Mother House's lay order outside the wall. They are neither killed nor watched, and they may walk away. Kin of another faith do not forgive the cells. (Thomas and Hero 2000; Tougher 2008; the Dorley serial)

Roadmap: move the item from "Still to do" to "Done", merged into the existing Adelphai line:

`- [x] Adelphai Dorleyaiou: the Galenic rite and school, the Council of the Two Schools, the Tower on the Condition, decaying tolerance from 1050; the Mother House's Rule; the Dorley precedent's disclosure, ward years, and washouts given to an order`
