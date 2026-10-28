# Wave 12: how the surrounding religious authorities react

TODO items (stage 2 inputs): the Catholic canonist (Huguccio's "prevailing sex" by conduct, the Susa / Hostiensis oath before the bishop, Peter the Chanter, Baldus on Giovanni Malaspina, whether Catholic hostility hardens around 1200); the Andalusi reaction (Ibn Ḥazm's charge against al-Ḥakam I); the Mamluk *istiḥlāl al-muḥarramāt* event (Ibn al-Baqaqi); the Orthodox Slav penance ladder in place of The Wills, with opinions by House. Built 2026-10-27, untested in game. Namespace `tm_rx`.

Files (new, with a BOM): `events/tm_rx_events.txt`, `common/on_action/tm_rx_on_actions.txt`, `common/scripted_triggers/tm_rx_triggers.txt`, `common/scripted_effects/tm_rx_effects.txt`, `common/modifiers/tm_rx_modifiers.txt`, `common/opinion_modifiers/tm_rx_opinion_modifiers.txt`, `localization/english/tm_rx_l_english.yml`.

**Existing files changed (one line each):**
- `common/on_action/tm_on_actions.txt`, `tm_yearly_playable`, the heresy-ladder `liege ?= { … }` limit: added `NOT = { tm_rx_slav_orthodox_trigger = yes }`. A Slavic Orthodox liege no longer draws `tm_byz.0010–0012`.
- `common/scripted_effects/tm_mech_effects.txt`, `tm_mech_scapegoat_effect`, the heresy-ladder limit: added `NOT = { liege = { tm_rx_slav_orthodox_trigger = yes } }`, for the same reason (the fervor-under-30 second chance).

The Wills (`tm_byz.0012`) was already limited to Byzantine-heritage lieges, so Slavic lieges used to stop at rung 2 (books, assemblies). Now they draw the penance ladder (`tm_rx.0030`) and none of the Byzantine rungs: "no burned books and no voided wills" (Levin note §4.1).

## How it fires

`yearly_playable_pulse` → `tm_rx_yearly`, with two entry points:
- a court whose clergy speak (Latin, Andalusi or Mamluk, and of no Sisters' faith) rolls for each daughter among its courtiers;
- a landed daughter rolls for herself when her liege is such a court.

`tm_rx_roll_effect` then tries the voices in order. Each voice checks the flavour budget and `tm_world_rested_trigger` on the daughter, then spends the budget and marks her (`tm_world_mark_effect`, the same three-year rest the `tm_world` events use). A daughter hears at most one voice a year, and none for three years after one. *Keep Quiet in This Land* halves the chances, as it does for `tm_world`. "Daughter" means an adult daughter of any gate or a declared sister who is not imprisoned (`tm_world_daughter_trigger`).

The penance ladder is separate: a landed Dorleyite ruler under a Slavic Orthodox liege rolls 3 in 100 a year, under the budget and the scapegoat calm.

A "Latin court" (`tm_rx_latin_court_trigger`) is Catholic, or (before the schism, or if it never comes) the Chalcedonian faith under a Western rite. "Slavic Orthodox" (`tm_rx_slav_orthodox_trigger`) means East, South or West Slavic heritage, and either the Orthodox faith or the Chalcedonian faith under the Greek or Slavic rite.

## 1. The bishop's court (`tm_rx.0001`, 1188–1390)

**Sources.**
- Huguccio's test is behavioural: "lacks a beard and always wants to be with women and do women's work", and the female sex prevails. Hermaphrodites could "influence their assigned identity by their behavior" (van der Lugt 2010, p. 111 and n. 34).
- Beards counted because they could be seen "without invasive examination" (p. 110).
- The canonists were calm and pragmatic; the theologians were the harsh ones (pp. 104, 113). Interest in the question is "concentrated in a rather brief period", the 1170s to the early 13th century (p. 111).
- Hostiensis (mid-13th century): a person should swear an oath to the bishop to use one sex only, with no change afterwards (DeVun 2021, p. 128; the Susa oath is Rolker's case of the same practice).
- "The canons fear only a turning back" is the bishop's line, after the Chanter's "adopt a gender and stick to it" (van der Lugt p. 113; DeVun note §4 item 2).

**What the player sees.** A daughter at, or the vassal of, a Latin court; not a daughter of Ha-Nehpakhot. Chance 4 in 100 a year, halved from 1250 as the canonists lose interest. A will before the bishop's court needs her witness, and a church court weighs a woman's witness by its own rules, so the canonist must write down which she is. His only rule is the one for a person of doubtful sex, "not written for her". He asks to see nothing.
- **1188–1249, Huguccio's questions.**
  - "My company is women, and my work is women's work": *Counted Among the Women* (+5 clergy opinion, 20 years); +10 prestige; the chaplain +10.
  - "I will not be weighed by my spindle": +15 prestige, +5 stress.
- **1250–1390, Hostiensis's oath.**
  - "I swear it. It was my word before it was your oath": *Sworn Before the Bishop* (+10 clergy opinion, 30 years); the chaplain +15. Tooltip: the bishop grants nothing she did not have.
  - "I will swear that I am a woman. No woman is made to swear for the rest of her life": +20 prestige; the chaplain −10.
- **Either era:** "Not today": nothing is written (rule 23).

## 2. A master from Paris (`tm_rx.0002`, 1191–1300)

**Sources.**
- Peter the Chanter (d. 25 September 1197) was a theologian, not a canonist (Baldwin pp. 5–8, 11). The long *Verbum abbreviatum* dates from 1191/92, the short version from 1197 at the latest (Baldwin pp. 13, 15).
- His gloss: God made "non androgynos" (van der Lugt p. 106 n. 19). The rule "adopt a gender and stick to it" is his (p. 113).
- When in doubt, the Chanter would have a male name given at baptism, and "its female variant may later be used" at confirmation (p. 112 n. 39).
- The Chanter's word-book, *Abel*: virgins, "the weaker sex", overcame "the world, the flesh, and the devil" (Barney p. 517; `hist_baldwin_peter_chanter.md` row 9).
- Lateran IV (1215), c. 3: three men of good reputation in each parish name those whose "life and habits differ" (Goodich p. 52).

**What the player sees.** A daughter at, or the vassal of, a Latin court; not Ha-Nehpakhot. A master of the Chanter's school preaches in hall: "not both in one … choose one, and keep it." From 1215 he reminds the hall of the parish inquest.
- "God made them male and female. I am the second": +15 prestige, −5 stress.
- *Dorleyites only, as Christians:* "Your Chanter's own rule lets a name take its woman's form at confirmation. If his Church can do that, so can mine": +25 piety.
- *Learning 10 or more:* the Valley Gate, "What is your excuse, Master?": +25 prestige, +5 stress; the chaplain −10.
- "Let him preach. I will eat in my own rooms tonight": no cost.

**Does Catholic hostility harden around 1200?** The sources say it hardens in one voice and not in the others:
- DeVun's turning point is "the turn of the thirteenth century" in theology (p. 11). Natural philosophy hardens after the 1250s (pp. 115–116).
- Law stays pragmatic from Gratian to Baldus (pp. 124–129).
- Lateran IV adds the parish inquest (Goodich p. 52), and the canonists' interest fades (van der Lugt p. 111).

So the theologian's voice grows: 2 in 100 a year, 4 from 1215, with the inquest line from 1215. The canonist's voice halves from 1250. The jurist is still there in the 1390s (§3). Natural philosophy (Albert's "monster in nature", after c. 1260) and the surgeons are not built (see Not built).

## 3. A consilium from Perugia (`tm_rx.0003`, from 1395)

**Source.** Baldus de Ubaldis on Giovanni Malaspina, 1390s (DeVun pp. 128–129). Malaspina was an heir who lived as a man and asked to succeed to his father's fief. Baldus called his sex "mixed" or "confused", but let him inherit, because his disposition suited "riding horses, handling weapons, and giving wise counsel". Had he been "fragile and feminine" he would have been judged female. The choice, made after puberty, was permanent.

**What the player sees.** A landed daughter (not Ha-Nehpakhot) under a Latin liege, once in her life, 5 in 100 a year. A Latin kinsman, if she has one, petitions the liege's judges to hold her inheritance void; otherwise a chancery clerk asks. The judges send for the consilium. The text names Malaspina as the jurist's past case, says he lived as a man, and says that Baldus's riding-arms-counsel test "is the jurist's test, and has nothing to do with her". The rule the judges read it for: a settled will, kept, decides.
- "Let the court read the consilium. I will pay the doctor's fee" (50 gold): *A Settled Will* (+5 vassal opinion, 20 years); the liege +10.
- "My life is no news to anyone here. I need no doctor to say it": +25 prestige. The kinsman, if any, gains an unpressed claim on her primary title.
- *Diplomacy or martial 12 or more:* "Tell the doctor his test is his own. I ride, I give counsel, and I am a woman": +40 prestige; the liege +10 respect.

## 4. Within our borders (`tm_rx.0010`, 1030–1250)

**Source.** De la Puente 2023 (the extraction has no page numbers, so references are to endnotes):
- Ibn Ḥazm charged that al-Ḥakam I "used to castrate the children of his subjects who stood out for their beauty" and named mosques after them: "an apogee of regnal cruelty" (n. 73).
- "All legal schools prohibited castration in Islamic territory … although not the purchase or the possession of eunuchs from other territories" (n. 74).
- The first *maẓālim* judge of al-Andalus was a eunuch, Masarra (n. 15).
- Ibn Ḥazm (994–1064) wrote from the 1020s; the gate opens at 1030.

**What the player sees.** A daughter of the knife at, or under, a Muslim court whose capital is in Iberia. Chance 6 in 100 a year. A jurist who has read Ibn Ḥazm tells the charge and asks where she was cut, and by whose hand. One added line depends on her House: Grandmother's House ("captives, cut without their asking"); the Gift Alone ("The schools forbid it whatever was asked"); any other ("Within our borders, or beyond them. Tell me which.").
- "Not here. No knife has been raised within your borders, and none of ours will be": +10 prestige; the lord +10 (*No Knife Within Our Borders*, 20 years).
- *Learning 10, or diplomacy 12:* Masarra: "Give me a hearing": +30 prestige; the lord +15 respect.
- *Grandmother's House:* "Al-Hakam's sin is ours too. Our House will answer for it before God": +30 piety, −15 prestige. This is the one condemned way of the knife (`faith_design.md` §16 decisions).
- *Gift Alone:* "I asked for the knife. If your schools call that a sin, it is mine, and I am a woman still": +20 prestige, −5 stress.

## 5. The forbidden made permitted (`tm_rx.0020`, from 1250)

**Source.** Rowson, "Homoerotic Liaisons among the Mamluk Elite", in Babayan and Najmabadi (eds.), *Islamicate Sexualities* (2008), pp. 213–214. In 1287 the jurist Ibn al-Baqaqi was charged with "declaring illicit things licit" (*istiḥlāl al-muḥarramāt*), "legally understood to imply apostasy and thus justify the death penalty"; he was put to death in Cairo in 1302.

**What the player sees.** A daughter of any faith at, or under, a Sunni court whose capital is in Egypt or Syria, from 1250. Chance 4 in 100 a year, 6 while the case is the talk of Cairo (1287–1301). A qadi warns the court's Muslims that whoever calls her life lawful declares the forbidden permitted, which the law reads as leaving Islam. The charge falls on Muslims, not on her. From 1287 he names Ibn al-Baqaqi as charged. From 1302 he says only that the sultan's court put him to death for it in 1302: past news, no detail. "No one will say one for her, either."
- "Then let no one speak for me. I am not of your law, and I ask no one to break it for my sake": +20 prestige, +5 stress.
- "What my faith teaches, it teaches among its own. Not in your streets": −10 prestige, −10 stress.
- *If she has a Muslim friend at that court (courtier, vassal or the ruler):* "Tell [friend] to say nothing for me. I will not be the reason a friend stands before a qadi": +10 prestige; the friend +20 (*Would Not Let Me Speak for Her*, 20 years).

## 6. The penance ladder (`tm_rx.0030`, from 900)

**Source.** Levin 1989:
- The church enforced sexual morality almost alone, through confession and penance, and "Unlike Byzantium, the Slavic states granted complete authority over morality … to the church" (pp. 4, 21–35, 297). Princes rarely enforced canon law (pp. 23, 298).
- The confessor's questions take the later form "Did you not…?" (p. 29).
- Penance meant a dry fast on Mondays, Wednesdays and Fridays with counted prostrations (p. 31), and exclusion from communion. It could be commuted by alms ("ninety nogaty or sixty dinars" for a year), by hearing the liturgy, or by monastic vows (p. 32). The last resort was excommunication and ostracism (p. 34).
- Slavic canonists chose the lighter of the Byzantine penances (pp. 30–31).
- The knife, by who cut whom:
  - castrating a son to sell him: three years (p. 73 n. 114);
  - self-castration: three years on bread and water (p. 209), later treated more harshly (p. 260);
  - one "made a eunuch in childhood" may be ordained (p. 257).

The gate is 900, the start of Levin's period; she argues the norms were stable throughout (p. 9).

**What the player sees.** Root is a landed Dorleyite ruler under a Slavic Orthodox liege. `var:tm_rx_penance` counts the rungs borne or refused; the third ends the ladder.
- **Rung 1, *The Confessor's Questions*.** The liege sends word only that "it is the bishop's business, and that there is a war". One added line depends on her House: the Gift Alone (the knife to one's own flesh, the gravest); Grandmother's House (the cutter's three years; the boy carries no sin); Aunt Bea's House (the cutter's three years).
  - **Opinions by House.** The liege's chaplain stands for the bishop's court. He takes −20 toward a Grandmother's ruler (*The Cutter's Sin*), and nothing toward her daughters. Under Aunt Bea's House: −10 toward the ruler (*Keeps a House That Cuts*) and −5 toward each daughter of the knife at her court (*Cut by Another*). Under the Gift Alone: −15 toward each daughter of the knife, the ruler included (*Took the Knife Herself*). The most consensual House is the most condemned: Levin's irony, as the TODO line asks.
- **Rung 2, *The Dry Fast*.**
- **Rung 3, *Barred from the Chalice*,** with excommunication as the next step.
- **Options.**
  - Commute by alms: 30, 60 or 90 gold by rung; +10 piety; the bishop lets her be for 10 years.
  - Bear it (rungs 1–2): +25 piety (+10 stress at the dry fast, the world's penance and not a gate: rule 22). The ladder climbs.
  - *If she holds a House:* "our House keeps a rule, as any convent does. Let its vows count". Half the time the bishop accepts (+20 prestige, commuted); otherwise not (+10 prestige; the ladder climbs).
  - "I confess to my own Mothers" (rungs 1–2): +15 prestige; the chaplain −15; the ladder climbs.
  - Rung 3, "Then I will eat at my own table": +25 prestige; *Barred from the Chalice* (−5 county opinion, 10 years). The ladder ends.

## 7. Counting

`tm_rx_tally_effect` keeps run-wide globals `tm_rx_n_<what>`. Print section for `tools/census_report.py` (not added; for the user to paste, after the Ha-Nehpakhot wave 6 section):

```python
    # Reactions, wave 12 (tm_rx_tally_effect): how the surrounding religious authorities react.
    print('== Reactions: wave 12 ==')
    rsteps = ('counted', 'weighed_refused', 'sworn', 'oath_refused', 'not_today',
              'master_answered', 'master_name', 'master_valley_gate', 'master_away',
              'consilium', 'no_doctor', 'own_test',
              'no_knife_here', 'masarra', 'owned_charge', 'asked_it',
              'for_herself', 'among_own', 'spared_friend',
              'penance_1', 'penance_2', 'penance_3', 'commuted_alms', 'commuted_house', 'house_refused', 'borne', 'refused', 'excluded')
    if any(f'tm_rx_n_{s}' in gvars for s in rsteps):
        print('  '.join(f'{s} {int(gvars.get(f"tm_rx_n_{s}") or 0)}' for s in rsteps))
        print('counted / weighed_refused: the bishop\'s court, Huguccio\'s questions (1188-1249), answered or refused; sworn / oath_refused:\n'
              'Hostiensis\'s oath (1250-1390), sworn or refused; not_today: either era, not today; master_*: the Paris master (1191-1300),\n'
              'answered, the confirmation name (Dorleyites), the Valley Gate, or kept away; consilium / no_doctor / own_test: the Perugia\n'
              'consilium (from 1395); no_knife_here / masarra / owned_charge / asked_it: Ibn Hazm\'s charge at an Andalusi court (1030-1250);\n'
              'for_herself / among_own / spared_friend: istihlal at a Mamluk court (from 1250); penance_1/2/3: rungs of the Slavic penance\n'
              'ladder reached; commuted_alms / commuted_house / house_refused: commutations by alms or by the House\'s rule, and the bishop\'s\n'
              'refusals; borne / refused: rungs borne or refused; excluded: rulers who ended the ladder barred from the chalice.')
    else:
        print('No counts (the save predates wave 12, or no voice has spoken yet).')
    print()
```

## 8. Guardrails

- **Hostile voices only for the hostile material.** Each voice is a named speaker of a vanilla court: the bishop's canonist, a Paris master, a jurist who has read Ibn Ḥazm, a qadi, a Slavic confessor. The narrator never endorses them.
- **Categories she does not claim.** Where a source's category is the hermaphrodite (Huguccio, Hostiensis, Baldus) or the castrate (Ibn Ḥazm, Levin), the text says that is the speaker's book reaching for the one rule it has. She never claims it. No Sister claims hermaphrodite or khunthā status.
- **No examination.**
  - The canonist "asks to see nothing", as the canonists judged by what could be seen "without invasive examination" (van der Lugt p. 110).
  - The oath is an oath.
  - Rowson's barracks anecdote (p. 227) is never used.
- **No sexual classification.** The Chanter's ch. 138 lines ("change themselves from males to females", Sardanapalus, the 342 statute) and his sodomy rationale for "choose and keep" are not quoted: they classify men who have sex with men (`hist_baldwin_peter_chanter.md` §1). No line frames a daughter as a gay man or a cross-dresser. No line says she "dressed as a woman".
- **No violence on screen.** Ibn al-Baqaqi's death appears once, as past news with no detail. No execution, burning or torture; no suicide or self-harm. The Slavic canon that treated self-castration like suicide (Levin pp. 73, 260) is rendered as "the newer canons count it graver than anything else in it", with no mention of suicide.
- **Historical figures are not claimed.** Al-Ḥakam's servants are his victims. Malaspina "lived as a man" and is the jurist's case. Masarra is "a cut man" a Sister cites as precedent for a hearing. Ibn al-Baqaqi is the qadi's example. None is claimed as a daughter or for any faith.
- **Islamic material.**
  - All legal argument comes from Muslim characters (the jurist, the qadi). There is no Qur'an or hadith in a non-Muslim mouth, and no "put them out" hadith.
  - "Born so" and "sick" do not appear. No *khawal*, no Al-Azhar, no *zār*.
- **Ha-Nehpakhot.**
  - Never drawn into the Latin events: the oath's "turning back" is the hyena trope's word for Jews (DeVun pp. 72–79, 84; `cmp_devun_shape_of_sex.md` §2.1 row 2).
  - A Ha-Nehpakhot daughter can meet the Mamluk qadi, whose words she answers. That is not a persecution mechanic.
  - No Jewish character appears in any event.
- **Rule 23.** The Hostiensis oath is the world's demand, not a gate. "Not today" and the refusal are honoured: the refusal gains prestige, and only the chaplain's opinion falls.
- **Rule 22.** The dry fast is the world's penance; bearing it is optional, and commuting it costs gold, not pain.
- **Rule 24.** No dress or skirt imagery; the outward line is the spindle and women's work, in Huguccio's own terms.
- **Rule 25.** No witchcraft material, and no Cathar or Waldensian ties.
- **No antagonist nation, no golden past.** Every hostile court also holds a pragmatic voice or a way through: the canonist's register, the Chanter's own confirmation rule, the consilium, the Andalusi lord's promise, the commuted penance.
- **Insiders over outsiders.** The answers are the daughters' own. The scholars' readings (Rolker's "humanity never in question", DeVun's "transgender as analytic") stay in the comments.

## 9. Not built

- The learned physician after 1260 (Albert's "monster in nature") and the surgeons' "correction" (DeVun proposal 3). The correction may appear only as a threat the player refuses; it is left for a later wave.
- The Mālikī *faqīh* who calms the emir's anger with Mālik's hadith (de la Puente §4).
- "A Legacy for the Sick" (an endowment in a woman's name).
- The Mamluk anti-vice pulse (Rowson p. 215).
- Levin's other proposals: the beard charge, the carnival penance, the Bulgarian "sisters of Lazar and Kirill", the *posestrima* blessing and the *proskurnica*.
- A `triggered_opinion` on the daughter traits for Slavic Orthodox observers. See Open questions.

## 10. Open questions for the user

1. **Opinions by House** are carried by the bishop's court (the liege's chaplain) when the ladder opens, not by a `triggered_opinion` on the traits. No vanilla parameter picks out Slavic Orthodox observers. `christian_syncretic_recipient` would hit every Christian (Catholics, Byzantines and Dorleyites too) and could not vary by the daughter's House, since the opinion is fixed per trait. If wanted, a world-wide Christian opinion on `tm_daughter_of_the_knife` could be added with a cancelling parameter on the Dorleyite rites, as Ha-Nehpakhot cancels `jewish_syncretic_recipient`. That would mean editing `tm_traits.txt` and the rite files.
2. **Replacing the whole Byzantine ladder for Slavic lieges** (not only The Wills). I read Levin's "no burned books and no voided wills" as covering rungs 1–2 too. If the user wants Slavic lieges to keep books and assemblies and only swap The Wills, remove the two added lines and fire `tm_rx.0030` when `var:tm_suppression = 2`.
3. **The witness frame for the bishop's court** (a will before the court) is my inference. It gives the canonist a reason to need her sex for a non-Christian daughter, since canon courts weighed witnesses and heard testaments. The sources discuss baptism, marriage and ordination; the witness rule is van der Lugt p. 111 ("a woman could testify in a church court").
4. **Dates by inference:**
   - Huguccio is taken from his *Summa* (c. 1188–90).
   - Hostiensis from 1250 ("mid-thirteenth century").
   - Baldus from 1395 ("1390s").
   - Ibn Ḥazm from 1030, ending at 1250 because the Andalusi courts are mostly gone by then.
   - The Slavic ladder from 900.

   Adjust if wanted.
5. **Masarra.** He was a eunuch whom a Sister cites as "a cut man", and the precedent is "for a hearing". Check the line reads as she means it, and not as claiming him.

## Uncertain syntax (check in game)

- `title = { first_valid = { triggered_desc … } }` on `tm_rx.0030` (vanilla uses the form).
- `clear_saved_scope` before re-saving inside an `every_courtier` loop, and whether the saved scopes travel with each `trigger_event` (assumed: they are copied when the event is queued).
- `rite = rite:slavic_rite` on a ruler whose faith has no such rite (the trigger checks the faith first).
- The empty loc string `tm_rx.0020.desc_plain` as a `first_valid` fallback.

## Test scenarios (for TO-TEST.md)

```
## AM (or the next free letter). Wave 12: how the surrounding religious authorities react (added 2026-10-27, untested; docs/wave12/reactions.md)
- [ ] 0001 Huguccio: a declared sister at a Catholic court, date 1200; `trigger_event tm_rx.0001` with scope:tm_rx_court
      saved: the Huguccio text and options a/b/e only; a gives Counted Among the Women and the chaplain's +10.
- [ ] 0001 Hostiensis: same at 1300: the oath text, options c/d/e; c's tooltip; never fires for a daughter of the
      Turning (Ha-Nehpakhot).
- [ ] 0002 Paris master at 1200 (no inquest line) and 1220 (inquest line); the confirmation-name option shows only for
      a Dorleyite; the Valley Gate needs learning 10.
- [ ] 0003 consilium: a landed daughter under a Catholic liege after 1395, with and without a Catholic kinsman (kin
      text and the claim in option b; clerk text otherwise); fires once per daughter (tm_rx_consilium_heard).
- [ ] 0010 Ibn Hazm: a daughter of the knife at an Andalusi Muslim court, 1100: the House line matches her rite
      (Grandmother, Gift Alone, other); options c/d by House; Masarra by learning/diplomacy.
- [ ] 0020 istihlal at a Sunni court in Cairo: 1260 (no name), 1290 (charged), 1310 (put to death, no detail); the
      friend option only with a Muslim friend at that court.
- [ ] 0030 penance ladder: a Dorleyite count under a Slavic Orthodox liege (Kyiv): rung 1 applies the House opinions
      from the liege's chaplain; rung 2 the dry fast; rung 3 ends the ladder; alms commute and pause 10 years; the
      House option needs a House.
- [ ] The Byzantine ladder (tm_byz.0010-0012) no longer fires under a Slavic Orthodox liege, and still fires under a
      Byzantine one.
- [ ] Observe run 867-1450: tm_rx_n_* counts appear in the census; no voice fires twice on one daughter within three
      years; no error.log lines from tm_rx files.
```

## Ready-to-paste README text

> **How the neighbours' clergy answer (wave 12).** The faiths are met by the clergy of the world around them, each voice in its own century and its own lands, and each with an answer the daughter can give:
> - A Latin bishop's canonist asks whose company she keeps and whose work she does (Huguccio, from 1188), and later asks her to swear before the bishop (Hostiensis, from 1250). She may answer, swear to today and not to her whole life, or not come.
> - A Paris master of the Chanter's school preaches "not both in one" (from 1191, harder after the Lateran council of 1215).
> - A doctor of Perugia's consilium settles an heir by her settled will (from 1395).
> - In al-Andalus, a jurist who has read Ibn Ḥazm asks where a daughter of the knife was cut.
> - In Mamluk Egypt and Syria, a qadi warns the court's Muslims that calling her life lawful is "declaring the forbidden permitted".
> - Under a Slavic Orthodox prince, a Dorleyite lord meets the bishop's penance ladder (the confessor's questions, the dry fast, exclusion from the chalice), which may be commuted by alms or by the House's own rule. It replaces the Byzantine heresy laws there: Slavic princes left these matters to the church (Levin).
>
> These are hostile voices, and none of them is the narrator's. No one is examined, and the daughters never claim the categories the books reach for.
