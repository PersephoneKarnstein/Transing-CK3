# To test

Scenarios for playtesters. Each one sets up a situation on purpose, so that a single session gives as much debug data as possible. None of this has been tested in-game yet. Anything you try is useful, including "it worked".

## Before you start

**Launch options.** In the Paradox launcher, open *Game settings* and add `-debug_mode` to the launch options. Debug mode gives you:
- the console (press `~`);
- a debug tooltip with ID numbers and variables when you hover over characters and titles;
- event IDs on event windows.

**Helper scripts.** Copy everything in `tools/run/` into the `run` folder next to your `mod` folder (create it if it isn't there). The console then runs them with `run <file>`:

| Script | What it does |
|---|---|
| `tm_census.txt` | Counts the Marked and the daughters in the world |
| `tm_rise.txt` | Makes you a daughter of the knife at once |
| `tm_make_sisters.txt` | Adds four adult sisters of your faith to your court |
| `tm_programme_prisoners.txt` | Puts every male prisoner you hold through the Dorley programme |
| `tm_house_tick.txt` | Runs one year of House life now |
| `tm_house_strain.txt` | Sets your capital's House strain to 6, so the next tick splits it |
| `tm_seidr_now.txt` | Starts the seiðr rite, skipping the cooldown |
| `tm_suppression_next.txt` | Fires the next rung of the heresy laws |
| `tm_isl_jest.txt` | Fires "Laughed At in the Hall" against a random Islamic ruler |
| `tm_khasi.txt` | Fires "The Khasi of the Household" (you must be of an Islamic faith) |
| `tm_adopt_check.txt` | Logs why vanilla adoption is or isn't offered for your wards |
| `tm_turning_now.txt` | Starts the Turning (Ha-Nehpakhot) at once, skipping the decision, its cooldown and the Adar window |
| `tm_turning_prayers.txt` | Adds three unanswered Adars to your next Turning (+30 to the roll) |
| `tm_pavai_now.txt` | Starts the pāvai vow (the Worn Garland), skipping the Mārkaḻi window |
| `tm_crossing_now.txt` | Starts the crossing (Badenya) |
| `tm_growth_now.txt` | Runs one year of the growth engine now (the call, and the rite offered to courtiers) |
| `tm_census_log.txt` | Takes the census now and keeps it on each faith for this decade (read it with `tools/census_report.py`) |
| `tm_join_baeddel.txt` | Makes you a Bædling (for playing Gotland) |
| `tm_join_badenya.txt` | Makes you Badenya (for playing Kirina) |

**Vanilla console commands you'll use:**
- `add_trait <trait> <id>` and `remove_trait <trait> <id>`
- `gold 1000`, `prestige 1000`, `piety 1000`
- `event <event_id> <character_id>`
- `effect <script>`
- `play <id>`, which switches you to another character
- `kill <id>`
- `yesmen`, which makes the AI accept everything
- `observe`

**What to send.** With every report, include:
1. **The scenario number** (for example "D5") and what you saw, against what this page says you should see.
2. **`error.log`** from the `logs` folder next to your `mod` folder. Lines with `tm_` in them matter most. Quit the game first so the log is complete.
3. **`debug.log`** from the same folder, for the scenarios that ask for it.
4. **A save** taken just before the thing that went wrong, if you can.
5. **Screenshots** of the event window, and of the debug tooltip when the scenario says to hover over something.

**Game rule.** Under *Game Rules*, the mod adds *Re-embodiment* (default on). Several scenarios ask you to run once with it on and once with it off. Bugs often appear in only one of the two.

---

## 0. Smoke test (everyone, five minutes)

**0.1 Load.** Start the 867 bookmark.
- In the faith screen, check that *Adelphai Dorleyaiou*, *Bædling*, *Yutai Dao*, *Ha-Nehpakhot*, *Cūṭikkoṭutta Mālai* (the Worn Garland) and *Badenya* all exist with their icons and holy sites. Ha-Nehpakhot sits under Judaism, the Worn Garland under Hinduism, and Badenya under the West African religion.
- Check the holy sites:
  - **Adelphai Dorleyaiou:** Dorylaion, Constantinople, Kyzikos, Ankyra, Pepouza.
  - **Bædling:** Uppsala, Trondheim, York, Kyiv.
  - **Yutai Dao:** Mogao, Longhu, Qingcheng, the Southern Marchmount (Mount Heng in Hunan).
  - **The Worn Garland:** Kanchipuram, Srirangam, Thanjavur, Madurai.
  - **Badenya:** Kirina, Niani, Awkar, Walata, Do. Its god names should be Ala, the ancestors and the bush spirits, never Amma or the Nummo.
  - **Ha-Nehpakhot:** Arles, Jerusalem, Narbonne, Montpellier, Hamadan. Hover each and read its text: Arles should mention the women's synagogue and the lamp alms; Narbonne the *nasi* who held land "under no lord"; Montpellier "from Lunel to Montpellier".
- Send `error.log` even if nothing looks wrong.

**0.2 Starting presence.**
- Phrygia should be Dorleyite and held by Theia Beatrike, the Mother of Mothers, with three Elder Sisters at her court.
- **Seats (Gotland, Kanchipuram, Kirina).** Each county should follow its faith. If its lord holds other counties and it is not their capital, it should be held by a new woman of the faith, the lord's vassal, with the seed characters at her court. Otherwise the lord keeps it, in their own faith, with the seed characters at their court. Note which happened at each seat.
- **Bædling:** Gotland, with a völva and two Marked young men.
- Shazhou should follow Yutai Dao, with a nüguan (a Daoist nun) at court.
- **The Worn Garland:** Kanchipuram, with a daughter of God and two Marked young men.
- **Badenya:** Sibi (Kirina), with a daughter of the House and two Marked young men.
- **Ha-Nehpakhot holds no land.** In the Character Finder, filter for the trait *Daughter of the Turning*: an elder (50–65) should be living unlanded in Arles (county of Venaissin). Filter for Ha-Nehpakhot: two Marked young men should be there too, and a household: a physician, his wife and three children, of their own dynasty. Hover the county of Venaissin in debug mode: it should carry the variable `tm_kahal`. Screenshot both.
- Hover over Theia's portrait and screenshot the debug tooltip.

**0.3 Census.** Run `run tm_census.txt`. Note the counts of Marked characters and daughters (all six gates count). They should be roughly 1% of adult men, and a handful of daughters.

**0.4 Ruler Designer.** Check that all six faiths and the Kybeline culture can be picked, and that the Marked trait costs nothing. Ha-Nehpakhot is listed under Judaism.

**0.5 The six decisions.** As a Marked man of each faith (Ruler Designer, or `add_trait tm_transgender` and convert), open the decisions list and screenshot it. Each faith should show its own gate: *Take the Knife*, *Ask a Völva to Sit for Me*, *Gestate the Jade Embryo*, *Keep the Fourteenth of Adar* (greyed out outside February and March), *Keep the Pāvai Vow* (greyed out outside December and January) and *Go to the Smith*.

**0.6 Text check.** Read the faith description and the tenets of Ha-Nehpakhot (*The Turning*, *The Three Lamps*, vanilla *Legalism*) and the trait *Daughter of the Turning*. Report any raw `tm_` key or broken text.

---

## A. Adelphai Dorleyaiou

**A1. The two-day knife rite.** Play Theia's Phrygia, or design a Dorleyite ruler. Then `add_trait tm_transgender` on yourself and `piety 500`.
- Take *Take the Knife*.
- **Expect:**
  - **"The Day of Blood" (`tm_knife.0001`).** Choose to let your blood fall.
  - **Two days later, "The Hilaria" (`tm_knife.0004`).** Answer "Never".
  - **Then you rise a daughter and the naming event fires.**
- **Repeat with re-embodiment off.** Then try choosing "Not this spring" on day one, and check you get 50 piety back.
- **Send:** screenshots of both events and of your character afterwards, plus `error.log`.

**A2. The Dorley path (Aunt Bea's House).** This is the default house of the knife.
- Win a battle and capture some men, or use `effect` to imprison a few. Run `run tm_programme_prisoners.txt`.
- Let three months pass several times. Expect three "lever" events, then either the knife (`tm_dorley.0100`) or a washout (`tm_dorley.0200`).
- **Check:**
  - the new daughter is released;
  - the sponsor becomes her guardian;
  - the "adopt her" option works.
- **Send:** the event IDs you saw and their order.

**A3. Choosing the house of the knife.** On a fresh game as the first human Dorleyite player, "The Houses of the Knife" should fire around day five. Play it three times, once with each choice, and check each doctrine's text in the faith screen:
- **Grandmother's House:** calls the cut eunuchs and takes boys.
- **Aunt Bea's House:** never takes a child and admits it keeps cells.
- **Gift Alone:** "Even the Mother of God was asked".

Check that the Gift Alone gives more piety and better opinion from your own faith than the other two.

**A4. Court offices.** You need a Dorleyite duke or higher. Get there with `effect` or by conquest, or play a duchy-tier ruler you have converted.
- Run `run tm_make_sisters.txt` and `run tm_rise.txt` on a courtier, or `add_trait eunuch_1 <id>`.
- In the court positions screen, look for *Parakoimomene*, *Protovestiaria* and *Papias*. Only daughters of the knife and eunuchs should be valid for these.
- Look for *Praiposita*: any woman or daughter should be valid.
- Appoint all four, and screenshot the salary and modifier tooltips.
- **Also check:** a count of the faith should not see the offices, and a Christian duke of another faith should not either.

**A5. Companions.** Play Theia (`play` her ID).
- Run `run tm_make_sisters.txt` twice.
- On each daughter, use *Name a Companion*. The eighth attempt should be refused with "already has seven Companions".

**A6. "Cybele in Christian Clothes"** (`tm_byz.0001`). Fire it with `event tm_byz.0001 <your id>`.
- Check that only the right answers show:
  - the Aristotelian answer under the main rite;
  - "the Mother was ours first" only under Grandmother's House;
  - the "We are Christians" answer always.

**A7. The heresy laws.** Play a Dorleyite count who is a vassal of the Byzantine emperor, as Phrygia's holder is at the start.
- Run `run tm_suppression_next.txt` three times, letting each event resolve.
- **Expect:** books, then assemblies, then wills.
- **Check:**
  - the assemblies rung raises House strain if you hold a House (combine with D5);
  - the wills rung's "Let them try" option gives your daughters *Contested Inheritance*.
- **For long games:** note whether the ladder fires on its own, and whether it fires more after 1081.

---

## B. Bædling

Design a Bædling ruler, or play Gotland (if its count is not Bædling, `run tm_join_baeddel.txt`). Then `add_trait tm_transgender` on yourself, `piety 500` and `gold 500`.

**B1. The full rite, in the best case.** Keep the starting völva at court, and add a woman who knows the warding songs. Any daughter of the high seat knows them; `run tm_make_sisters.txt` gives you two.
- Take *Ask a Völva to Sit for Me*.
- **Expect:**
  - **"The Völva Comes".** Feast her for 50 gold.
  - **"The Warding Songs".** A known singer should be offered.
  - **"The Platform".** Wait for her answer.
- **Check:**
  - the völva in the portraits is your court völva, not a stranger;
  - the 50 gold comes out of the host's purse.

**B2. The travelling völva, in the worst case.** Remove every daughter of the high seat from your court first, by sending them away or with `kill`.
- Start the rite. A new seeress should be created on the road.
- At the songs, choose "The women will hum what they remember".
- Do this several times (`run tm_seidr_now.txt` skips the cooldown) and **record successes against failures.** The odds should be clearly worse than in B1.

**B3. The reluctant singer.** Have a woman of another faith at your court, and no one who knows the songs. At the songs step, ask her.
- **Check:** if she agrees, she should now count as knowing the songs. Test this by trying B1 again later with her as the singer.

**B4. The winter visit.** Wait for "A Völva on the Winter Road" (`tm_seidr.0020`), or fire it with `event tm_seidr.0020 <your id>`.
- Try "Ask her to sit for one of my court" with a Marked courtier. Add one with `add_trait tm_transgender <id>`.
- **Check:** the rite runs on the courtier, not on you, and the courtier rises.

**B5. Teach the Warding Songs.** A daughter of the high seat with a daughter or ward who doesn't know the songs should see *Teach the Warding Songs*.
- **Check:** after teaching, the pupil can serve as the known singer in B1.

**B6. Naming and the Thing.**
- At the naming event, try "The woman's form of my own name". It only appears for common Norse names: test with a character named Ragnarr, Sigurðr, Gunnarr, Þórsteinn and so on.
- Then try "Fasten a name with a gift".
- At "Before the Thing", try all five answers across several runs and screenshot each result: verse, steel, seiðr is women's art, "That word is for men", and let him talk.

**B7. Devil and name.** In the faith screen, the faith should be called *Bædling* and its devil *Níðhöggr*, not Loki. Screenshot both.

---

## C. Yutai Dao (the Way of the Jade Embryo)

Play Shazhou, or design a ruler of the Way. Then `add_trait tm_transgender` on yourself and `piety 500`.

**C1. The full gestation.**
- Take *Gestate the Jade Embryo* and answer the guarantor.
- **Expect:** "The Censor's Register" around month three, "The Red Dragon" around month six, then birth around month ten.
- **Check:** the *Gestating the Jade Embryo* modifier stays on you throughout.

**C2. Delays.** Choose "Hold the stillness" at month three and "Turn the work" at month six. Repeat until one of them fails.
- **Expect:** the same trial comes back 60–90 days later, and nothing is lost.
- **Check:** the gestating modifier is refreshed, not removed.

**C3. Help and opting out.**
- With a daughter or Marked sister at court, "My sisters will stand at the gate" should appear and should always pass.
- "Set the work down" should end the gestation cleanly. Then take the decision again and check it isn't blocked as "already gestating".

**C4. Month 6 and the physician.**
- At "The White Tiger", try each answer:
  - "Not yet! Don't rush me!" should go straight on to the birth.
  - "I will go home and nurse my parents" should only show while a parent is alive, and should delay the trial.
- About one gestation in three, "A Ghost Fetus" should fire between months 4 and 5. **Check:** none of its three answers ends the gestation.

**C5. Temple societies.** With a Sisters' House and the Way's rite:
- Give birth by the embryo. Your House's strain should drop and you should gain piety: the dues at a birth.
- Kill a sister courtier with `kill <id>`. "The Society Buries a Sister" should fire.
- Take *Borrow from the Righteous Store*, then pass a year. The repayment event should ask for 150 gold.
- As a vassal, take *Petition for a Name-Panel*. Then fire `event tm_yutai.0010 <your id>` with a fresh unnamed House, and check that a named House never triggers it on its own.

**C6. The world of the Way.**
- Fire `event tm_yutai.0001 <your id>` ("A Prodigy in the Prefecture") and try all four answers.
- As a king or higher of the Way, use *Ordain by Special Edict* on a Marked courtier. She should be declared and ordained.
- Holding Shazhou, take *Relight the Shenquan Abbey*.
- **The faith screen:** the high god should read *the Queen Mother of the West*, and the holy sites should include *the Southern Marchmount*, not Wudang.
- In a game started in 867, the Huang Lingwei rescript should fire once, between 882 and 900.
- Hover over a Buddhist ruler's opinion of a daughter. It should show *A Man Reborn a Woman* (−10). Screenshot it either way.

---

## D. Shared systems

**D1. Declare Before Witnesses.** As a Marked man in any of the six faiths, take *Declare Before Witnesses* and choose a name.
- Then go through your faith's rite (A1, B1, C1 or F2), **once with re-embodiment on and once with it off.**
- **Check:**
  - your declared name survives the rite;
  - the naming event does not fire a second time.
- Note that with re-embodiment on, the name is copied from the old body after it dies, which is the step most likely to fail.
- **Send:** a screenshot of your name before and after, plus `error.log`.

**D2. Re-embodiment carry-over.** With the rule on, set up a ruler who has all of the following before their rite. In 867, a married count with children is easy to find.
- titles (including vassals);
- a spouse;
- children (born and adopted);
- an adoptive parent;
- some gold, prestige and piety.

After the rite, **check each item carried over.** Screenshot the family tree before and after.

**D3. Take as Daughter matrix.** Try *Take as Daughter* on:
- a courtier;
- a ward;
- an adult guest;
- a woman with a living mother;
- a girl whose relatives hold land (vanilla blocks this case);
- a ruler (should be refused).

Note the cost and whether she accepted. Then **check the line of succession lists her.**

**D4. Fostering.** Use *Foster as Daughter* on a courtier.
- **Check:** she does NOT appear in your line of succession.
- Then use *Take as Daughter* on her. The price should be half the normal one.
- **Send:** both cost tooltips.

**D5. Sisters' Houses.** As any ruler of the six faiths, run `run tm_make_sisters.txt`, then take *Found a Sisters' House*.
1. Hover over your capital county in debug mode. It should carry the variables `tm_house`, `tm_house_strain` (0) and `tm_house_protectress`. Screenshot it.
2. Run `run tm_house_tick.txt`. "The Sisters Choose" should fire, with an Elder Sister drawn from the lot. Run it a few times on fresh Houses and see whether different nominees win.
3. Run `run tm_house_strain.txt`, then `run tm_house_tick.txt`. "The House Divides" should found a House in a neighbouring county. Hover over that county to confirm.
4. **Burnout.** Remove most of your court, so that fewer than two sisters remain, and tick several times. Strain should climb and "The Little Work" (burnout) should fire.
5. **Protectress.** Kill your Protectress with `kill <id>`, then tick. A new Protectress should be named from her daughters or your house.

**D6. A House under a lord of another faith.** With a House founded, run `effect set_character_faith = faith:orthodox`, then `run tm_house_tick.txt`.
- "A House in My Lands" should fire. Try both answers on separate saves.
- **Let it stand:** ticking again should not ask again.
- **Close it:** your sister courtiers should move to another ruler who holds a House, or leave court. They must not vanish; use `run tm_census.txt` before and after. If you have a Protectress, she should now dislike you.

**D7. Sending to the Houses.** With a House, take *Send to the Houses* several times; it has a five-year cooldown, so pass time or use separate saves.
- **Check:**
  - all three candidates match your faith's culture and daughter type;
  - sometimes the young or elder candidate declines, and her option is hidden;
  - the "all who will come" option skips anyone who declined.

**D8. Arrivals.** Play ten to twenty years at speed 5 as a ruler of the faith with a House, and log every arrival event:
- a Marked traveller (`tm_arrival.0001`);
- a woman turned out for being barren (`0003`);
- a friend of the House (`0004`).

**Check:**
- a traveller arrives already named;
- "Turn her away" sends her to another House rather than deleting her.

**Send:** the count of each type and how many years you played.

**D9. The Sisters Choose.** As a duke or higher of any of the six faiths, change your realm's succession law to *The Sisters Choose*.
- Run `run tm_make_sisters.txt` and adopt one of them.
- Open the succession screen and check who can vote and who can stand:
  - voters: you, your vassals of the faith, and clergy of the faith;
  - candidates: your born and adopted children, women of the faith on your council, and vassals of the faith.
- Kill yourself (`kill <your id>`) and see who inherits.
- **Send:** screenshots of the voters and candidates.

**D10. Old saves.** If you have a save from before 18 October 2026 where you used *Petition for a Refuge*, load it with the new version and play one year. The refuge should become a Sisters' House in your capital county.

**D11. Islamic neighbours.**
- As a daughter who rules next to an Islamic realm, run `run tm_isl_jest.txt` and try each answer.
- Then `play` an Islamic ruler, give them a daughter courtier (`run tm_rise.txt` on a courtier won't work, so use `add_trait tm_daughter_of_the_knife <id>` on a female courtier), and run `run tm_khasi.txt`.
- **Opinion penalty:** hover over the Islamic ruler's opinion of any daughter. It should show *A Castrated Man in Law* (−10). This is the change most likely to fail silently, so a screenshot either way helps.

**D12. Same-sex marriage.** In all six faiths, check that two women, including a daughter and a cis woman, can marry, whatever the vanilla game rule says. For Ha-Nehpakhot this overrides the Judaism religion's own doctrine, so check it there especially.

**D13. Jewish and Indic neighbours.** These reactions apply to daughters of every faith, not only Ha-Nehpakhot. Hover the opinion of:
- a Rabbinic or Karaite character toward any daughter: *What Came Forth Male* (−10);
- a Ha-Nehpakhot character toward the same daughter: the −10 cancelled by *Turned, as Dinah Was* (+10);
- a Buddhist, Hindu or Jain character toward a daughter of the knife: *Unmanned by the Knife* (−15); toward any other daughter: *A Man Become a Woman* (−5).
Screenshot each. Full scenarios are F8, F9 and F11.

---

## E. Long AI run (no playing needed)

Start a new 867 game, pick any ruler, type `observe`, and run at full speed to about 1000 or as far as you can. Then:
- run `run tm_census.txt`;
- save the game and send the save and `error.log`.

This shows whether the AI ever uses the rites, Houses, fostering, Companions, the elective law and the court offices. It also catches errors that only show up after decades.

**This is now the most important test.** The first observe run (867–986) found the faiths dying out, and the growth engine is new and untuned (`docs/faith_design.md` §14). Please:
- send the last save (an autosave is fine; saves must be plain text, so keep *compressed saves* off and don't play ironman). Every 10 years each faith takes a census and keeps it in the save by decade: members, daughters, Marked, landed members and counties, and running totals of joins by the call (and how many were rulers), kahal joins, kahal matches, pilgrims to the kahal (and, for Bædling and Mālai, members with no court coming home), rites offered, daughters raised, deaths, and pool characters the game cleared. The characters made at game start for each seat are kept on lists too, and each foothold seat records how it started (a vassal of the faith, the lord's court, or no holder). One late save holds the whole run. To read it yourself: `python3 tools/census_report.py "<save>.ck3"`. These numbers are what the rates will be tuned on;
- note whether any faith **booms** (hundreds of members, or many counties) as well as whether any dies;
- check Phrygia at the end: is it still Dorleyite, and is the Mother of Mothers a theocracy? If Byzantium took it, does the Mother House holder have a claim on it?
- check that Arles has Ha-Nehpakhot courtiers at the count of Venaissin's court.

For Ha-Nehpakhot, which has no land of its own, also note:
- whether the three Arles characters are still alive and still in Provence, or have wandered off;
- how many daughters of the Turning exist (Character Finder, trait filter), and whether any AI took the Turning (it can only do so in February and March);
- whether any ruler got "A Book in Arabic", "A Fisica at Court" or "What Came Forth Male" (search `debug.log` for `tm_hipukh`).

Run a second, shorter observe from the 1066 bookmark, and if you can a third past 1323 (start at 1178 and run on), so the dated Revel, the *Touchstone* lines and the 1401 council can appear.

---

## F. Ha-Nehpakhot

Design a Ha-Nehpakhot ruler in or near Provence, or play the count of Venaissin (Arles) and `add_trait tm_transgender`, then convert to Ha-Nehpakhot from the faith screen. Give yourself `piety 500` and `gold 500`. The sect starts with no land: an elder daughter of the Turning and two Marked young men live unlanded in Arles.

Several things depend on the date, so test in three periods if you can: **before 1323** (the 867 bookmark), **1323–1400** (Kalonymus's lines and the young men's Revel), and **1401 on** (the council with women at Arles). Use an Occitan character for at least one run, for the Provençal blessing.

| Scenario | What it covers |
|---|---|
| F1 | The Adar window |
| F2 | The five-part rite, best case; re-embodiment; names; the Revel by date; the Provençal blessing |
| F3 | The worst case, and the unanswered-Adar bonus |
| F4 | Conversion of a Rabbinic or Karaite seeker |
| F5 | Before the Baylons: the four answers, the council, the lord's refusal of *niddui* |
| F6 | The Three Lamps (yearly) |
| F7, F13 | A Book in Arabic; A Fisica at Court |
| F8, F9 | A Jewish lord's ruling; Jewish opinions |
| F10 | Names and the faith screen |
| F11, F12 | Eastern opinions by gate; The Wills only in Byzantium |

**F1. The Adar window.** Outside February and March the decision *Keep the Fourteenth of Adar* should show but be greyed out, with the tooltip "It is Adar (February or March)". Wait, or use the console to advance the date, until February.
- **Check:** the decision becomes valid in February and March, and not in April.

**F2. The full rite, in the best case.** Keep a daughter of the Turning at court, and stand in Arles (whose county carries the ḥevrah's street bonus).
- Take the decision, **once with re-embodiment on and once with it off.**
- **Expect, in order:** "The Scroll" (go down to the women's synagogue), "The Revel" (keep the dress on), "The Prayer" (say it aloud), then on success "A Name for Shushan Purim" and, about a week later, "Before the Baylons".
- **Check:**
  - the elder in the portraits is your court's daughter of the Turning;
  - "The Scroll" offers "Go down to the women's synagogue" and "Go up to the men's synagogue", and its text says the women's synagogue is the room below the men's (no "gallery" anywhere);
  - the event texts say "the women of the lamp", never *ḥevrah*;
  - the prayer text mentions Kalonymus and the *Touchstone* only on or after 1323;
  - the Revel: from 1323 the young men dress up and "the rabbis grumble and let it pass"; before 1323 she alone wears the dress, and "Laugh with the others" is missing;
  - the naming event offers two choices: "A name from the scroll and the Torah" (Dinah, Esther, Estes or Sara) and "A name of the street" (Rosa, Mairona, Venguessona, Bella, Regina, Dulcia and others). **Screenshot any name that shows as a raw key;**
  - for an Occitan character the naming text quotes the blessing as *qui fis me fenna*;
  - its text includes the women's blessing, "who made me a woman".

**F3. The elder from the street, in the worst case.** Remove every daughter of the Turning from your court, play outside Provence, choose the men's side at the scroll and laugh off the revel.
- Repeat several times (`run tm_turning_now.txt` skips the window and the cooldown) and **record successes against failures.**
- **Check:** each failure adds one to the variable `tm_turning_prayers` (inspect it with the character debug view), and the odds rise with it. `run tm_turning_prayers.txt` adds three at once. On success the variable is cleared.

**F4. Conversion.** As a Marked Rabbinic (or Karaite) Jew, take the decision.
- **Check:** on success the new daughter's faith is Ha-Nehpakhot. On failure the faith stays as it was.

**F5. Before the baylons.** Try all four answers across several runs and screenshot each.
- "Answer with Dinah": on a win, the county you stand in should carry `tm_worthies_licence` for ten years, and a later Turning there should be likelier. On a loss, check the *Niddui* modifier (three years).
- "The Touchstone…" should appear only on or after 1323.
- **The council.** From 1401, in Arles (the county with the women of the lamp), the event text should say the baylons called the women of the street too, and "Answer with Dinah" should win noticeably more often. Before 1401, or elsewhere, the plain text.
- "I am the lady of the house" gives *Niddui* even though she gains piety.
- **The lord's licence.** Repeat a losing dispute in a county whose holder has *Patron of a Translation* (take it in F7 first, as that lord). The toast "The lord would not license the ban" should appear and *Niddui* should not.

**F6. The three lamps.** As a daughter of the Turning, wait for "The Three Lamps" (`tm_hipukh.0020`), or fire it with `event tm_hipukh.0020 <your id>`. Try all three options.
- **Check:**
  - "Teach the prayer" appears only when a Marked courtier who could seek the Turning is present, and that courtier then gets a better roll in F2;
  - "Spin with the women by moonlight" raises the opinion of every adult woman at court;
  - the tenet *The Three Lamps* reads that one whose days do not come keeps them "as the zekenah keeps them", and no Three Lamps text mentions blood.

**F7. A book in Arabic.** Play a ruler of any faith (try a Catholic one) with a daughter of the Turning at court. Wait for "A Book in Arabic" (`tm_hipukh.0030`), or fire it with `event tm_hipukh.0030 <your id>`. **Note:** fired from the console, the translator scope is missing and the event will not show; let the yearly pulse fire it, or report that it never appears.
- **Check:** commissioning costs 50 gold, gives *Patron of a Translation*, and licenses your capital county.

**F8. A Jewish lord's ruling.** Play a Rabbinic ruler (Khazaria in 867, or the Ruler Designer) with a daughter of any faith at court. Wait for "What Came Forth Male" (`tm_hipukh.0040`).
- **Check:** "What came forth male is male" gives her the opinion *Ruled Me a Man* toward you.

**F9. Opinions.** Hover a Rabbinic character's opinion of any daughter (knife, seiðr, embryo or Turning). It should include *What Came Forth Male* (−10). A Ha-Nehpakhot character's opinion should show it cancelled by *Turned, as Dinah Was* (+10). **This uses a tenet parameter in `triggered_opinion`, which is untested: report if either line is missing.**

**F10. Names and screen.** In the faith screen the faith should be *Ha-Nehpakhot*, its clergy *Zekenah*, and its holy sites Arles, Jerusalem, Narbonne, Montpellier and Hamadan. Screenshot it.

**F11. Eastern opinions by gate.** Hover a Buddhist or Hindu character's opinion of a daughter of the knife: it should show *Unmanned by the Knife* (−15). Of a daughter of seiðr, the embryo or the Turning: *A Man Become a Woman* (−5).

**F12. The Wills only in Byzantium.** As a Dorleyite vassal of a Catholic or a Slavic Orthodox liege, let the suppression ladder climb (`run tm_suppression_next.txt`). It should stop at the second rung ("assemblies banned") and never fire "The Wills". Under a Greek liege it should still reach "The Wills".

**F13. A fisica at court.** Play a ruler of any faith with a daughter of the Turning at court and wait for "A Fisica at Court" (`tm_hipukh.0031`); it shares the yearly roll with "A Book in Arabic", so either may come. Try all three options.
- **Check:** "Licence her" costs 50 gold and gives her *Licensed Fisica*; "women only" costs 25 and gives *Fisica of Women*; once licensed she is not offered again.
- **Note:** as with F7, firing it from the console leaves the physician scope empty and the event will not show; let the yearly pulse fire it.

---

## G. Growth (quick checks)

**G1. The call.** Start in 867 as any ruler. In the Character Finder, filter for *Marked by the Mother* and note a few Marked characters of other faiths in Anatolia, Scandinavia, China, Tamil or Kannada country, West Africa, or of a Jewish faith. Run `run tm_growth_now.txt` ten times. Some should have joined the nearest of the six. Marked characters elsewhere (France, northern India) should never change.

**G2. The rite for courtiers.** As a ruler of any of the six, `add_trait tm_transgender` on two male courtiers of your faith, then run `run tm_growth_now.txt` a few times. Within a few runs one should start the rite (the first event of the chain appears on the courtier; switch to them with `play <id>` to see it). A courtier of Ha-Nehpakhot should only start in February or March.

**G3. Adoption by the AI.** `play` an AI daughter who rules (or make one), give her a female courtier of her faith, go back to your own character and let a few years pass. She should take the courtier as a daughter. Check the courtier's family panel.

**G4. Phrygia.** At the 867 start, the Mother of Mothers should be a theocracy. Use `effect title:c_phrygia = { change_title_holder = { holder = <any Orthodox id> change = ... } }` or play on until Byzantium takes it, then run `run tm_growth_now.txt`: the Mother House holder should get a pressed claim on Phrygia.

---

## H. The Worn Garland

Play the lord of Kanchipuram, or design a Worn Garland ruler in Tamil country. `add_trait tm_transgender`, `piety 500`, `gold 500`. Put a few adult women at your court (they are the companions).

**H1. The Mārkaḻi window.** *Keep the Pāvai Vow* should be greyed out outside December and January, with the tooltip "It is Mārkaḻi (December or January)".

**H2. The vow, best case.** Five women at court, a daughter of God among them, at Kanchipuram. Take the decision.
- **Expect, about ten days apart:** "The Waking", "The Song" (choose either), "The Garland" (wear it), "The Dream", then "The Staff and the Name".
- **Check:** the debug tooltip shows `tm_pavai_companions` falling by one now and then; the more who hold, the likelier success; on success the naming offers names of the temple street (Arangam, Umai, Madevi and others).

**H3. The vow, worst case.** No women at court, away from Kanchipuram, offer the garland unworn. Repeat with `run tm_pavai_now.txt` and **record successes against failures**.

**H4. A name in stone.** As a ruler of the Garland, wait for "A Name in Stone" (`tm_garland.0020`). The 100-gold endowment should give *A Name in Stone* and mark your capital county.

**H5. A pandit's objection.** As a Hindu ruler not of the Garland, with a daughter of any faith at court, wait for "A Pandit's Objection" (`tm_garland.0030`).

**H6. Opinions.** A Vaiṣṇava or Śaiva character's opinion of a daughter of God should show *A Man Become a Woman* (−5); a Garland character's should cancel it with *A Soul Made Woman* (+5).

---

## I. Badenya

Design a Badenya ruler in Mali, or play Sibi (Kirina) (if its holder is not Badenya, `run tm_join_badenya.txt`). `add_trait tm_transgender`, `gold 500`, `prestige 500`. Have a mother, sister or aunt alive, or a woman at court who likes you (opinion 10+).

**I1. The crossing, best case.** Take *Go to the Smith*.
- **Expect:** "The Smith's Bargain" (give your manhood), about a week later "My Mother's Child" (a named woman claims you), then "The Word That Cools" (pay the jeli well), then the naming (Sogolon, Kolonkan, Tenenba and others).
- **Check:** the *Hot* modifier between the bargain and the word; it is gone after.

**I2. No one to claim her.** With no living close female kin and no woman at court who likes you, run `run tm_crossing_now.txt`. "My Mother's Child" should offer only "No one will claim me yet", and the chain should stop.

**I3. The jeli's price.** Choose "Pay what I can" several times. Roughly half should be praise and half a joke the court laughs at; both should still make you a daughter.

**I4. The djinn returns, once.** About a year after the bargain, "The Djinn Returns" (`tm_badenya.0015`) should fire, **on the new body if re-embodiment is on**. Pay or refuse. It must never fire a second time.

**I5. Naming feasts.** As a daughter of the House, wait for "A Naming Feast" (`tm_badenya.0020`) over several years: the first three should only let you serve; after that you may host.

**I6. The House buries its own.** `kill` a daughter of the House at your court. "The House Buries Its Own" should fire for you. **Check that it does not fire when a daughter is re-embodied** (the old body's death is not a burial).

**I7. God names.** In the faith screen and in any event mentioning the high god, Badenya's should be *Ala*; the devil *the bush spirits*.

## J. Stage 2 events (added 2026-10-20, untested)

Start the observe run only after these files are in place: new script files are not hot-loaded, and adding them mid-run crashed the game once.

- **Flyting (Bædling).** As a Bædling, use *Challenge to a Flyting* on a courtier, ideally one who is craven or deceitful. Check that each charge only scores when true, that *ragr* and "father's daughter" appear only against a Marked, declared or daughter character, that "Own the word" shows for those two, and that the score counts correctly over three rounds. Repeat in a hall of 5 or more and at a June thing (stakes ×1 and ×2), and with a woman of the faith at court, so the cup appears. In an observe run, confirm hostile Norse or English courtiers open flytings against Bædling daughters.
- **Four children for the Emperor (Adelphai Dorleyaiou).** Observe to 949, or set the date to 949 on a save. Before autumn 950 the Mother of Mothers should get *Four Children for the Emperor*: only her knife House's ransom option shows; four eunuch children aged 7–11 appear at her court; under Aunt Bea's House each is adopted by an older woman of the faith (a daughter first), otherwise by the Mother herself; it fires once only.
- **The Emperor halts at Dorylaion.** Hold Phrygia as a Dorleyaian vassal of the Emperor while he is at war. Within a few years *The Emperor Halts at Dorylaion* should fire; the petition option shows only after a suppression rung; with a daughter of the knife at court, hosting may lead to *The Chamber Asks*, and if she goes she moves to the Emperor's court.
- **The palace offices (Yutai Dao).** Make a daughter of the Way a vassal of the Tang emperor and fire `event tm_palace.0001`. Option (a) adds the seal modifier, removes `tm_house_named` from her House counties and schedules `tm_yutai.0010`, then `tm_palace.0002` in 3–6 years; option (c) is hidden under intrigue 10. Set the date to 903.2.1 while she holds office: `tm_palace.0003` fires once, and a courtier is sent on to a House.
- **The prayer book and the door (Ha-Nehpakhot).** Give a daughter of the Turning a living Jewish sibling and run `event tm_kahal.0019 <her id>`: the sibling gets 0001 in 7–30 days. "Not this year" leaves her untouched and puts `tm_kahal_book_declined` on the sibling; a scribe's copy gives her 0002 ("my sister"), the modifier and the opinion. Marry her off and check the wedding text. At a court with a Jewish woman run `event tm_kahal.0009 <her id>`: it waits for September or October, then fires 0010.
- **The kahal keeps its children.** At an AI Christian court with a Ha-Nehpakhot child, let the ruler appoint a Christian guardian with the faith-conversion option; within a year the convert flag should be gone, and the child should still be of the sect at 16. A player's own choice of conversion must stand.
- **The temple's deal (Mālai).** Play a Hindu ruler with an adult daughter of the Garland at court and fire `tm_kovil.0001` (or wait a few years after 1070). Each option's modifier should appear and gold come off the right purse. With the verse, wait for December or January for *The Seventh Verse*. Kill the holder with a living daughter of the Garland (born or adopted): the honour and *To Her Descendants* pass to the eldest; re-embodiment passes nothing on.
- **The New Roof (Badenya).** In the console, `set_global_variable = { name = tm_next_new_roof value = 1 }` (or wait for 874). Have a Badenya daughter at a Badenya ruler's court and advance to 1 January: *The New Roof* comes between March and May. Check option (a)'s gold and prestige and (b)'s gifts and opinions; each member gets *Under One Roof*, Same Roof and mutual "My Age-Mate", and no second gathering at the next roof. Option (c) gathers them seven years later. With the daughter at a non-Badenya lord's court, the eldest Badenya woman there hosts.

## K. The Crusader Dolls bookmark (added 2026-10-20, untested)

- At 867, a **Crusader Dolls** tab should appear in the left-hand list. Selecting it shows five rulers: Theia Beatrike (Mother House), Steinn (Gotland), Xun (Guasha), Cantirâdêvi (Candragiri) and Djeneba (Kirina). Each should be playable, hold the title shown and be of her or his faith. The art and portraits are placeholders.
- Theia, Cantirâdêvi and Djeneba are now historical characters (`history/characters/tm_characters.txt`); the start script hands them their titles. Check that Theia holds the Mother House and Phrygia under the Emperor as a theocracy, that both countesses are vassals of their lords, and that the start at 1066 or 1178 still makes stand-ins (the historical ones are dead by then).
- **Portraits (needs you, once):** start a game at this bookmark with the console enabled, run `dump_bookmark_portraits`, and copy the five `bookmark_tm_*.txt` files it writes (in the CK3 user folder) over the placeholders in `common/bookmark_portraits/`. The placeholders are vanilla portraits copied so the bookmark screen does not crash.

