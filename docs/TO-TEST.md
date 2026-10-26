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
- send the last save (an autosave is fine; saves must be plain text, so keep *compressed saves* off and don't play ironman). Every 10 years each faith takes a census and keeps it in the save by decade: members, daughters, Marked, landed members and counties, and running totals of joins by the call (and how many were rulers), kahal joins, kahal matches, pilgrims (members gathered to a court of their faith, for all six faiths, and to the kahal), rites offered, daughters raised, deaths of members seen at a census, and pool deaths (everyone else, including characters the game cleared). The characters made at game start for each seat are kept on lists too, and each foothold seat records how it started (a vassal of the faith, the lord's court, or no holder). One late save holds the whole run. To read it yourself: `python3 tools/census_report.py "<save>.ck3"`. These numbers are what the rates will be tuned on;
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
- **The kahal keeps its children** (now for all six faiths; see T5). At an AI Christian court with a Ha-Nehpakhot child, let the ruler appoint a Christian guardian with the faith-conversion option; within a year the convert flag should be gone, and the child should still be of the sect at 16. A player's own choice of conversion must stand.
- **The temple's deal (Mālai).** Play a Hindu ruler with an adult daughter of the Garland at court and fire `tm_kovil.0001` (or wait a few years after 1070). Each option's modifier should appear and gold come off the right purse. With the verse, wait for December or January for *The Seventh Verse*. Kill the holder with a living daughter of the Garland (born or adopted): the honour and *To Her Descendants* pass to the eldest; re-embodiment passes nothing on.
- **The New Roof (Badenya).** In the console, `set_global_variable = { name = tm_next_new_roof value = 1 }` (or wait for 874). Have a Badenya daughter at a Badenya ruler's court and advance to 1 January: *The New Roof* comes between March and May. Check option (a)'s gold and prestige and (b)'s gifts and opinions; each member gets *Under One Roof*, Same Roof and mutual "My Age-Mate", and no second gathering at the next roof. Option (c) gathers them seven years later. With the daughter at a non-Badenya lord's court, the eldest Badenya woman there hosts.

## K. The Crusader Dolls bookmark (added 2026-10-20, untested)

- At 867, a **Crusader Dolls** tab should appear in the left-hand list. Selecting it shows five rulers: Theia Beatrike (Mother House), Steinunn (Gotland), Huijing (Guasha), Cantirâdêvi (Candragiri) and Djeneba (Kirina). Each should be playable, hold the title shown and be of her or his faith. The art and portraits are placeholders.
- Theia, Cantirâdêvi and Djeneba are now historical characters (`history/characters/tm_characters.txt`); the start script hands them their titles. Check that Theia holds the Mother House and Phrygia under the Emperor as a theocracy, that both countesses are vassals of their lords, and that the start at 1066 or 1178 still makes stand-ins (the historical ones are dead by then).
- **Portraits (needs you, once):** start a game at this bookmark with the console enabled, run `dump_bookmark_portraits`, and copy the five `bookmark_tm_*.txt` files it writes (in the CK3 user folder) over the placeholders in `common/bookmark_portraits/`. The placeholders are vanilla portraits copied so the bookmark screen does not crash.


## October reading revisions (added 2026-10-21, untested in-game)

Design: `faith_design.md` §16. With `-debug_mode`, event IDs show on each window; fire any event with `event <id>`.

- **Rescue the Daughters**: win the war and check each freed woman goes to your court or home by her own choice (a player-controlled woman gets `tm_mech.0001`), and piety is 25 per woman, capped at 300.
- **Set Down the Name** (decision, declared sisters): no faith penalty; Declare Before Witnesses is offered again; hostile kin get "Set Down Her Name".
- **Teach Her the Answers** (interaction): the seeker gets `tm_taught_answers_modifier`; the embryo, Turning, pāvai and crossing rolls rise; `tm_mech.0030` (examiner suspects coaching) sometimes follows.
- **Marriage**: marry a daughter; the spouse becomes a friend of the House. Re-embody a married man: `tm_mech.0040` then `tm_mech.0041` for the spouse; a vanilla-faith spouse hears the annulment line.
- **Re-embodiment grievances**: someone who disliked the old body keeps "An Old Grievance, Still Held".
- **Dorley washout** (`tm_dorley.0200`): execution only under Grandmother's House; release sends the novice to the friends of the House.
- **Houses**: "The Same Door" (`tm_house.0065`), the released prisoner (`tm_house.0061`), The House Grows Respectable (`tm_life.0001`, a House 25 years old).
- **Hostile world** (`tm_world.0001–0050`): Whispers and the child-lifter tale (never for Ha-Nehpakhot or Grandmother's House realms), Many Ledgers, the physician's record, the copyist, A Question in Hall, The Court Wonders, the Abbess's Feast, the Qadi's Ruling (Sunni and Shi'i voices; al-Nu'man only after 960), Those Without Desire, The Women's Hour.
- **Life** (`tm_life.*`): novice and declared waiting moments; "lady"; The Old Likeness and A Name of Her Own about one and two months after a rite; grandchildren; mourning; burial under the birth name; Kin, People or Sisters; the Badenya senior mother and the feast server's earnings; the Garland companions and the barred seeker; foot-binding (Yutai, from 1200 only); the expansion sermon (first duchy per faith).
- **Intersex birth** (`tm_life.0040`, 2% per birth at a court of the six) and the choice at 16 (`tm_life.0041`): the sex the game uses never changes, and the child never gets the Marked trait.
- **Saints**: at 867, the five foremothers show in the faith's saints list with tombs at Dorylaion, Ankyra, Kyzikos, Pepouza and Midaion.
- **Marked rate** is 1.5% (was 1%): check `tm_census.txt` early and late in a run.

## Round 2 (added 2026-10-21, untested in-game)

- **Flavour budget**: game rule *Crusader Dolls Flavour Events* (rare / normal / frequent). With `-debug_mode`, hover a character for `tm_flavour_cooldown`.
- **We Stay** (`tm_house.0051`, `0052`): order a House closed with a sister at court.
- **Sister-Making** with a Marked, declared or House-member adult; check +15 at her gate and the sponsor reward when she rises.
- **At Home in Her Body** modifier after any gate.
- **Refugees**: close a House; the receiving county gets `tm_refugee_carried`.
- **Dorley intake**: only violent men go to the cells; a Marked or declared prisoner gets *Welcome Her to the House*.
- **Stepping back** from any gate refunds the cost and adds no stress.
- **New events**: The Same Roof (`tm_house.0070`), I Simply Cannot (`tm_life.0035`), the frightened courtier (`tm_life.0090`), Elder in Years (variant in `tm_life.0050`), Ruled as a Man (`tm_world.0070`), The Confessor's Book (`tm_world.0060`, Catholic, 1000–1346), Women Without a Rule (`tm_world.0061`, from 1312), A Woman in the Line (`tm_world.0051`), the mask law (`tm_world.0080`, from 1325).
- **Keep Quiet in This Land** (decision): hostile `tm_world` events halve; she can't be Elder Sister.
- **Learned answers**: `tm_byz.0001` option e, `tm_hipukh.0003` option e (learning ≥ 12).

---

## L. Bædling: Spring the Cell, outlawry and landless bands (added 2026-10-21, untested)

Design: [docs/wave3/baedling.md](wave3/baedling.md). Start a fresh game with these files in place.

**Spring the Cell**

**L1. The scheme.** As a Bædling ruler, imprison nothing yourself. Via console, have a neighbouring Catholic count imprison a daughter of seiðr. Open the count's interactions.
- **Expect:** *Spring the Cell (Scheme)* shows, and the agent slots list Marked Guard ×2, Faithful Servant, Friend of the House and Lookout.
- **Send:** a screenshot of the agent slots, with their names and contributions.

**L2. Success.** Let a phase complete. "A Night for It" offers tonight or wait. Choose tonight with high odds.
- **Expect:** the prisoner is released and appears at the nearest House holder's court (or yours if none). The jailer gets "An Empty Cell"; with low secrecy it names you and adds "Emptied My Prison".

**L3. Failure.** "The Door Held" offers give up or go again; the jailer gets "Footsteps in the Yard".

**L4. The AI plots.** Put a Marked prisoner in an AI dungeon with a sworn sister of hers (an AI ruler of the faith) in range.
- **Expect:** within a few years the sister owns a Spring the Cell scheme against the jailer (character window, schemes).

**L5. Freed another way.** Free the prisoner by other means: the scheme ends with "Spring the Cell Ends".

**Outlawry**

**L6. The suit.** Set the date to 1100 or later. A Catholic Norwegian or Swedish count (you) keeps a Bædling daughter of seiðr as a courtier, and his chaplain dislikes her.
- **Expect:** in time the count gets "A Suit at Law" with the church's charge. Quashing costs piety and the chaplain's opinion.

**L7. Her answer.** Let the suit run. The AI daughter takes the oath, the ring or the woods.
- **Ring:** she leaves for a faith court outside the realm with "Lesser Outlaw" (3 years).
- **Woods, if she can fight:** a new adventurer camp led by her, with "Outlaw".

**L8. The outlaw at the door.** As a Bædling ruler with a House, receive the lesser outlaw: "An Outlaw at the Door" offers keep or send on.

**L9. Settlement.** A full outlaw band with 100 gold or more: the accuser gets "The Outlaw's Price". Accepting lifts the sentence.

**L10. Forgiven for the war.** Hire the outlaw band for a war on the accuser's side: the accuser's top liege gets "Forgiven for the War", once.

**L11. The high seat.** An outlaw band takes any county: the outlaw modifier is gone.

**L12. No suit.** Before 1100, or under a pagan or English lord, no suit ever fires.

**Landless bands**

**L13. Answer the Hall's Call.** Play a Bædling adventurer with prestige level 1 or more, at peace, camped within reach of Gotland held by a Catholic.
- **Expect:** "Answer the Hall's Call" shows, costs 250 prestige, and opens a claim war for Gotland.
- **Check:** whether the war's own cost is charged on top of the decision's prestige.

**L14. Settling.** Win: "Settling the Hall" (10 years) on you and "Our Own Came Home" (20 years) on Gotland. Take a county by vanilla invasion instead: you get "Settling the Hall" only, unless the county keeps the faith or has a House.

**L15. Observe run.** AI faith bands far from any welcoming county start travelling toward one, about one band in seven a year. Bands in reach of a weaker AI holder use the decision.

**L16. Rescue the Daughters as a band.** As a landless band of any of the six faiths, find a neighbouring county where two or more daughters, Marked women or declared sisters of your faith live under a lord of another faith, or whose lord holds one of them prisoner. A declared sister counts in both cases.
- **Expect:** *Rescue the Daughters* is offered to the band (never to nomads). Win it: you hold the county, your camp is gone, you have the *adventurer* trait and your followers *adventurer_follower*, and "Settling the Hall" applies.
- **Send:** `error.log` and a screenshot of your realm after the war. The landing path is not vanilla's, so this is the step most likely to fail.

---

## M. Yutai Dao: the palace faction (added 2026-10-21, untested)

Design: [docs/wave3/yutai.md](wave3/yutai.md). The balance is the variable `tm_yt2_balance` on the throne's primary title; hover that title in debug mode to read it.

**M1. The inner offices at work.** As a daughter of the Way under the Tang emperor, fire `event tm_palace.0001 <your id>` and take the seal.
- **Expect:** the decision *Work the Inner Offices* appears. Before 903 options (a) and (c) show; (e) is hidden until the balance is 1 or more.
- **Check:** (a) moves the balance +1, (c) +2. Then (e): one other Sisters' House in the realm gains `tm_house_named`; her own does not.

**M2. Song levers.** Set the date to 1060 under the Song: (b) shows, (a) and (c) do not, and the balance cannot pass +2.

**M3. Memorials by balance.** Set the throne title's `tm_yt2_balance` to −3 and advance a few years.
- **Expect:** `tm_palace.0002` returns about once a decade at most for a daughter in office, and never within five years of option (d).

**M4. The Censor's Brush.** Under a celestial throne, make a member of the Way the Censor of the ministry (appoint her spymaster), with a different daughter in office.
- **Expect:** no memorials fire. Within some years `tm_yt2.0003` fires to the Censor.
- **Check:** each option's office loss and opinion changes reach the sister. Under a meritocratic throne the event never fires.

**M5. The clerk.** After 971, under a celestial throne, a daughter of the Way who holds a House should rarely get `tm_yt2.0002`. Option (b) shows only at balance 1 or more.

**M6. 903.** Hold the seal on 903.2.1: the purge fires, and the throne title's balance is −3.

**M7. Month 3.** With `tm_yt2_licences` on the top liege's primary title, `tm_embryo.0010` shows option (e).

---

## N. Adelphai Dorleyaiou: the Galenic rite and the reading (added 2026-10-21, untested)

Design: [docs/wave3/dorley.md](wave3/dorley.md).

**N1. Found the Galenic Rite.** Play a Dorleyaian count under an Orthodox liege and set the date past 886.
- **Expect:** the decision shows (never for the Mother of Mothers). Take it: the rite exists, you are of it, and so is your capital county if it is Dorleyaian.
- **Check:**
  - the new rite's name, colour and icon (screenshot the faith screen);
  - your House of the knife matches your old rite (try with Gift Alone);
  - the faith's three tenets still show on the new rite;
  - your liege has +15 "Counts as the Emperor Counts";
  - the Mother of Mothers gets *A Sister Counts Three* within a month;
  - the found decision disappears for everyone, *Join* appears for other Dorleyaians, and *Return* appears for you. Return: back to the main rite, and the Mother +15.

**N2. Before 886** the found decision does not show.

**N3. The heresy laws, Galenic.** As a Galenic ruler under an Orthodox liege, fire `event tm_byz.0010 <your id>` and `event tm_byz.0012 <your id>`.
- **Expect:** the Galenic answers show. At 0012, adopted daughter-children gain −15 of you and `tm_wills_registered` is set.

**N4. Ignatios.** New 867 game as any Dorleyaian player: *The Patriarch Without a Beard* arrives around 20 November 867, once, also to the Mother of Mothers. A later start never sees it.

**N5. The train to Tarsus.** Before 990, as a Dorleyaian ruler in Anatolia with Cilicia held by a Muslim, fire `event tm_dl2.0020 <your id>`.
- **Expect:** only your House's option shows, plus the strategos under a Christian top liege, plus "Past the Gates".
- **Check:**
  - Gift Alone and Aunt Bea's House: three boys aged 8–12 (two of them eunuchs) adopted at court;
  - Aunt Bea's House: a greedy Sunni merchant in your dungeon, and the prisoner interaction shows only if he happens to qualify;
  - Grandmother's House: two eunuch boys, and dread;
  - it fires at most once in 20 years per ruler, not after 990, and not without a Muslim holder of Cilicia.

**N6. The book.** After 1107, fire `event tm_dl2.0030 <your id>` as a Galenic ruler (option a) and as an Aristotelian (option b). Learning 10 or more adds option c. Once per ruler.

**N7. Athos.** Set the date to 1083 on an observe save: *The Holy Mountain Closes* fires once by 1090.

**N8. The steward.** After 1120, with a Sisters' House in Anatolia, fire `event tm_dl2.0050 <your id>`.
- **Expect:** an Orthodox eunuch courtier appears. (a) converts and becomes a friend of the House; (b) converts and gets the courtier rite offer (`tm_growth.0001`); (c) sends the steward to the pool.

**N9. The Consul's Letter.** Set the date to 1070 as a Dorleyaian ruler of the main rite and fire `event tm_dl2.0060 <your id>`.
- **Expect:** options a and c show, b does not. As a Galenic ruler: b and c.
- **Check:** the text never calls Psellos a Sister or names what he was. It fires once per ruler, never before 1063 or after 1078, and the Mother House's holder sees it more often in observe runs.

**N10. Budget.** With the rare flavour rule, Tarsus, the book and the steward never come within two years of another flavour event.

---

## O. Deeds of the House (added 2026-10-21, untested)

Design: [docs/wave3/achievements.md](wave3/achievements.md). The deeds fire a few days after the Rite of the Knife, and only for players. They do not use the flavour budget. Since wave 4 the debug interaction that forces the programme on a prisoner skips the deeds: "run the programme" here means the real programme, the Dorley path, or `run tm_programme_prisoners.txt`.

**O1. The Pope, re-embodiment on.** Aunt Bea's House. Capture the Pope (console: imprison him; give him `wrathful`), take him into the House, and wait for `tm_dorley.0100`.
- **Expect:** `tm_ach.0001` three days after the knife, with the Dorley text and the pre-1250 line.
- **Check:** "the Unmaker"; memories on both; Catholic rulers at −40; the adopt option (Daughters Chosen); the new body holds `k_papal_state`. Set the year past 1250 and repeat for the line about the chroniclers' woman pope.

**O2. The Pope, re-embodiment off.** As O1: the same deed, with the old body still Pope.

**O3. The Patriarch, then both.** The Patriarch through the Dorley path: `tm_ach.0010`. Then the Pope too: `tm_ach.0060` about ten days after the second deed.

**O4. Grandmother's House.** Castrate the Pope with the vanilla interaction. Within a quarter, `tm_ach.0002` with the Pope text. Repeat with the Patriarch.

**O5. The vizier.** Capture the councillor of a Muslim ruler; check the variable `tm_ach_vizier_of`; run the programme.
- **Expect:** in `tm_ach.0020`, "send her back" puts her at her master's court, and he holds a favour hook on you. Test before and after 1064.

**O6. The khan's son.** A khan's son (nomadic, or Turkic tribal) through the programme: `tm_ach.0030`, then `tm_ach.0031` two months later; try both options. A khan himself: the envoy speaks for her heir.

**O7. The poet.** A court poet or musician through the programme or the offered rite: `tm_ach.0050`, all three options.

**O8. Six Hundred.** Set the house variable `tm_ach_knife_daughters` to 49 and raise one more daughter: `tm_ach.0040` comes to every player of the house.

**O9. No deed.** The voluntary rite as a player who holds no notable title: no deed, only the house count rises.

**O10. The decision.** *Deeds of the House* is hidden with no deeds; afterwards it lists exactly the deeds earned.

**O11. AI captor.** An AI captor finishes a Pope programme: no event, no flag, only the house count.

---

## P. Ha-Nehpakhot: the street (stage 2, added 2026-10-21, untested)

Design: [docs/stage2/ha-nehpakhot.md](stage2/ha-nehpakhot.md). These are flavour events: free the flavour budget first if you fire them from the console.

**P1. By moonlight.** Give a daughter of the Turning a court with women of her faith and fire `event tm_hn2.0001 <her id>`.
- **Check:** each option, and `tm_hevrah_taught` on a seeker pupil. Before 1105 the Sarah option has the Talmud text. Before 1323 the desc has no *Touchstone* line.

**P2. The talk travels.** Set `tm_hn2_spindle_talk` on her and fire `event tm_hn2.0002 <her id>` at 1066, 1200 and 1350.
- **Check:** the Talmud and Rashi variants, the Torah and Ḥinukh lines, the roll, and the *Teach Her the Answers* bonus.

**P3. Spindle to hearing.** Win 0002.a and check `tm_hn2_spindle_heard` on her county. Then run a seeker's Turning to `tm_hipukh.0003` in that county.
- **Expect:** the tooltip for a and e shows +10, and the county variable is gone after the hearing. A second hearing there has no bonus.

**P4. The adornment.** Marry a daughter of the Turning at 1100, 1200 and 1330, and check the desc variant each time. On the spouse, give the necklace.
- **Check:** the artifact's name, desc, icon and modifier, and that it does not decay. A second marriage offers none.

**P5. Before the bailiff.** At 1300, a daughter with a rival, living in a county held by a Christian lord.
- **Check:** the "served" option with and without `tm_translation_patron_modifier` on the county's holder. Before 1260 the event does not fire.

**P6. Carnival.** A member at a Christian Occitan court after 1400. The hidden wait reaches February; check each option. Before 1400 it does not fire.

**P7. The lord's licence.** A landed ruler of the sect, outside the Maghreb and the Sahel, with a shunned daughter at court (give her `tm_niddui_modifier`). Fire `event tm_hn2.0040 <your id>`.
- **Check:** each option, and the desc at 1200, 1350 and 1420.

**P8. A seat below.** From 1409, a seeker of the sect at the count of Venaissin's court gets the Arles desc; elsewhere the plain desc. Buy the seat: her next Turning prayer shows +10 for the seat. Before 1409 it does not fire.

**P9. Catalan names.** A seeker at Barcelona (or of Catalan culture) after 1390 who is turned.
- **Expect:** at the naming the scroll, Provençal and Catalan options all show, and the Catalan option gives a name from the list (Dolça and Estel·lina drawn correctly). In Provence the Catalan option is hidden.

---

## Q. Ha-Nehpakhot in the Maghreb and the Sahel (added 2026-10-21, untested)

Design: [docs/wave3/ha-nehpakhot-maghreb.md](wave3/ha-nehpakhot-maghreb.md). "The West" means a county de jure in the Maghreb empire, Mali, Kanem-Bornu, Dagomba or Bono.

**Q1. The ban under a Muslim lord.** A seeker in Fes (Muslim holder) loses `tm_hipukh.0003`.
- **Expect:** she gets the ban, and the street's judges are "the elders and the dayyan". Thirty days later the holder sees `tm_hn3.0010`.
- **Check:** without a protector or a Jewish friend at his court, option c is hidden. Give his court a courtier with `tm_hn3_physician_modifier`: c shows and lifts the ban, and Jews of other faiths at both courts get −10 of her. Option a leads to `tm_hn3.0011` within a month; b gives *The Ban Enforced*.

**Q2. The ban under a ruler of the sect.** A ruler of the sect with her capital in `k_maghreb` and a shunned daughter at court.
- **Expect:** the yearly pulse gives `tm_hn3.0020`, not `tm_hn2.0040`. Take a: courtier bans are lifted, and a new loss in 0003 in her realm shows the toast and no ban.
- **Check:** the decision appears only without the decree and with Jews of another faith at court.

**Q3. Provence unchanged.** The same in Arles: `tm_turning_niddui_effect` and `tm_hn2.0040` as before, and the judges named by Arles dates.

**Q4. The rehearing.** `tm_hn3.0011` with and without a Jewish female friend: check +15 in the tooltip.

**Q5. The physician.** A Muslim lord with his capital at Kairouan in 1030: the Maghreb desc with the nagid line in the present tense, and no vizier option. At 1100: the past tense, the vizier option and its line. A Christian lord: the old event.

**Q6. Names.** A seeker of Berber culture who is turned: the Maghreb option shows, and the names display (Sitt al-Kull and the others).

**Q7. The Purim fire.** A seeker at Tunis in 1000, 1100, 1180 and 1300: three different lines; the option gives +10 at 0001. A seeker at Fes sees neither.

**Q8. The attire.** A daughter at Marrakesh marries: the attire option replaces the necklace; the artifact is created, and `tm_hn2.0011` reads the attire text without the Kalonymus line. A second marriage offers neither.

**Q9. The story.** A daughter at a court in Gao after 1062: `tm_hn3.0030` fires (raise the chance to test). Before 1062, never.

**Q10. The rope.** A seeker at Fes after 1160 with `tm_turning_prayers`: the rope line follows the elder's desc.

**Q11. The refuge.** A ruler of the sect with her capital in Fes in 1150: the decision shows; at 1100 and 1240 it is hidden.
- **Expect:** taking it adds a married Rabbanite couple at court. They keep their own faith (shelter is not conversion), like her (+25), and carry `tm_hn3_refugee`. The census `kahal_joins` does not rise at once; the kahal of her town (T1) may draw them in later.

**Q12. The hush.** Take the decision, then check the opinions and the modifier. A daughter who arrives later gets the modifier at the next yearly pulse.

**Q13. Robes of Honour.** A female ruler at Kairouan in 1010 with a daughter of learning 10 or more; also a male ruler with a female regent. After October 1023 it does not fire.

---

## R. The Worn Garland: shares, gifts and other courts (stage 2, added 2026-10-21, untested)

Design: [docs/stage2/worn-garland.md](stage2/worn-garland.md).

**R1. A share.** Kanchipuram start: give a daughter of the Garland at a Hindu court 100 gold, and fire `event tm_ml2.0001 <lord id>`.
- **Check:** the share, the county's *A Temple Street* modifier, and 8 gold a year while she lives there.

**R2. Away.** Move her to another court. After three yearly pulses, check `tm_ml2.0004` and who gets the share.

**R3. Passing on.** Kill a shareholder with an adopted daughter; then one with no daughter but another daughter of the Garland in the county. Check `tm_ml2.0003`'s two texts.

**R4. The gift and the staff.** Fire `event tm_ml2.0010 <her id>` and choose the Lady (from 1119).
- **Check:** the share, the staff event (`tm_ml2.0011`), and the nickname with the fee and without it.

**R5. Food and Clothing.** Fire `event tm_ml2.0030 <lord id>` on a Hindu lord with a daughter child. Check each option, and that it never fires twice for her.

**R6. Jain and Shaiva courts.** A Jain lord, and a Shaiva lord (Kannada culture after 1160, Tamil after 1135): check `tm_ml2.0031` and both texts of `tm_ml2.0040`.

**R7. The Order's Terms.** A Śvetāmbara lord (`rite:svetambara`, for example in Gujarat) with a daughter at court whose stewardship is 12 or more: fire `tm_ml2.0031`.
- **Expect:** option d shows, and `tm_ml2.0032` reaches her; check both answers. Repeat with a Digambara lord, and with a daughter whose stewardship and learning are under 12: option d must not show.

**R8. Before 1070.** Kill a shareholder who has an adopted daughter: the share goes to a woman the street chooses, not to the daughter. Fire `tm_ml2.0001` before 1070: the "buy" options must not show.

---

## S. Badenya: at court (stage 2, added 2026-10-21, untested)

Design: [docs/stage2/badenya.md](stage2/badenya.md).

**S1. The sister's line.** Give a Badenya count a sister with an adult child of the faith, then kill the count (`kill <id>`).
- **Expect:** the heir gets *The Sister's Line* in 5–10 days.
- **Check:** (a) gold moves to the sister's child; (b) prestige; (c) an unpressed claim on the dead count's primary title and the −30 opinion.
- Make the sister's child the heir (for example, a childless ruler under partition with the nephew as heir) and check *The Sister's Child* instead.
- Repeat with a Muslim heir: the text should be the neutral variant, with the jurist's view.
- Check the Ghana tense switch at 1077.

**S2. A hot realm.** The Badenya heir has "A Hot Realm". *Hot Words* comes in 2–13 months about half the time. Check that the jelimuso option needs a Badenya woman or daughter at court, and that it cools the realm.

**S3. Praise before the court.** Fire `event tm_bd2.0020 <your id>` on a Badenya ruler with a Badenya court chaplain.
- **Check:** the three descriptions (a king before 1330, 1330–1351, and from 1352; a count at any date), the mother's-name line with and without a known mother, and that option a cools a hot realm.

**S4. Associate in rule.** Before 1352 the decision is hidden. From 1352, a Badenya ruler with a wife, a sister at court or a mother at court: take the decision.
- **Check:** each candidate option, and "Not yet" (prestige refunded); only women are offered, cis and trans; the modifier; +15 opinion from vassals of the faith; −10 from Muslim vassals, and the qadi's line.
- Fire `event tm_bd2.0041 <your id>` (with the flavour budget free): new vassals of the faith gain the opinion.
- Set her aside by decision. Name another, kill her (`kill`), and check *One Name at the Feast* and that the vassal opinions are gone. Name another, then kill the ruler and check the associate loses the modifier.

**S5. Uninvited praise.** `event` is not enough here, because it needs the newborn's scopes. Let a Badenya ruler have a child with the flavour budget free: the event comes eight days after the birth about one time in seven.

---

## T. Survival balance (added 2026-10-21, untested)

Design: [docs/wave3/survival.md](wave3/survival.md). The census counters are read with `python3 tools/census_report.py "<save>.ck3"`.

**T1. The kahal of her town.** Give Ha-Nehpakhot a landed ruler (play one, or `set_character_faith` on a count).
- Run this about 30 times, or wait ten years:
  `effect = { every_living_character = { limit = { faith = faith:tm_nehpakhot is_landed = yes } tm_surv_kahal_draw_effect = yes } }`
- **Expect:** a young courtier of the sect appears at her court now and then. Run `run tm_census_log.txt` before and after: the faith's `tm_n_kahal_joins` rises.

**T2. Take in.** As a ruler, run:
  `effect = { create_character = { age = 20 faith = faith:catholic save_scope_as = x } scope:x = { tm_surv_kahal_take_in_effect = { COURT = root } } }`
- **Expect:** x is of the sect and at your court.

**T3. The gathering.** Move a daughter of the Adelphai to the pool (`move_to_pool`) far from Phrygia.
- **Expect:** within about five years (20% a year) she is a courtier of the nearest ruler of her faith, or of the Mother of Mothers. A lowborn ordinary member in the pool stays put. Try a guest as well: a daughter visiting a court of another faith should also be gathered.

**T4. A dead ruler's household.** A ruler of Badenya with an unmarried daughter of the House at court and a Sunni heir: kill the ruler (`kill`).
- **Expect:** within a month the daughter is at the nearest Badenya court. With a Badenya heir, nothing moves.

**T5. Children.** As for the kahal before (§J), with a child of Badenya at an AI Sunni court: the convert flag on the guardian should be gone within a year.

**T6. The death counter.** In the next observe run, Yutai `deaths` should stay below about a third of members a decade; compare `pool_deaths`.

---

## U. Landless bands: the patent and the robe, and the companions choose (wave 4, added 2026-10-21, untested)

Design: [docs/wave4/bands.md](wave4/bands.md). Start a fresh game with these files in place. The offers use the flavour budget; free it first if you hurry them by console.

**The patent and the robe**

**U1. A long camp.** Make a Bædling adventurer (you) and camp for five years in a county of an AI count who holds two or more counties. To hurry it: `effect = { set_variable = { name = tm_band_camp_years value = 5 } }`.
- **Expect:** within a few years either "An Offer of Land" (a Western lord: the charter text) or "Asked to Move On".
- **Check:** accepting makes you his vassal in the offered county (vanilla's letter 0301), with "Settling the Hall" from wave 3.

**U2. The land's own words.** Repeat U1 in three places.
- Anatolia under a Byzantine count: the treaty text before 1300, the district command from 1300.
- Iran under a Muslim lord: "The Patent and the Robe", with the robe option.
- Near Dunhuang under a Chinese lord: "The Rallied Township", with "Enter us on the register".

**U3. Service.** Hire your band to an AI ruler through a war contract and win.
- **Expect:** `tm_band_served` is on you after the war, and the next years bring that ruler's offer (25% a year).

**U4. Patience.** When the AI lord asks you to move on, choose "We go".
- **Expect:** your camp travels to a neighbouring realm. You gain prestige, an unpressed claim on the county, and his +25 opinion.
- **Check:** some years later the same lord offers you land ("Some years ago I asked…").

**U5. We stay.** Choose "We stay" against an AI lord.
- **Expect:** vanilla's eviction letter follows; refusing it gives him vanilla's apprehend war.

**U5b. A player lord.** As a count with two or more counties and a faith band camped five years in your county.
- **Expect:** "A Band on My Land", within the flavour budget.

**The companions choose**

**U6. The hand-over.** Play a faith band whose leader has low skills (console `add_martial_skill = -10` and so on) and a camp officer of the faith with a leadership value of 30 or more.
- **Expect:** within a few years, "The Companions Choose". Take "Then she leads": you play on as her.
- **Check:** the camp (domicile, buildings, provisions), the men-at-arms, the gold and the courtiers moved with the title. The old leader is in the camp with "Stepped Down with Honour".
- **Send:** if the domicile did not move, report it at once. The effect must then change (see "The engine question" in the note).

**U7. Not yet.** Choose "Not yet".
- **Expect:** nothing changes; the companion has −10 opinion of you; no new event for ten years.

**U8. Observe run.** AI bands rarely change leaders (about one weak-led band in twenty a year). No player is ever replaced without the event.

---

## V. Bædling: Open Ports, the Island Changes Hands and the Peace of the Island (wave 4, added 2026-10-21, untested)

Design: [docs/wave4/gotland.md](wave4/gotland.md). Start a fresh game with these files in place.

**Open Ports**

**V1. The decision.** As a coastal Danish or Swedish king at war, with a Bædling band camped nearby (console: create a Bædling adventurer near your capital).
- **Expect:** *Open the Ports* shows. It is valid only with that band in reach, and costs 100 prestige.

**V2. A player band.** Play the band instead.
- **Expect:** the "Open Ports" contract message, and *Stand with Us* on the contract board with the king as employer. Accepting joins the war and shows the toast "We Hold the Letters".

**V3. An AI band.** With an AI band in reach.
- **Expect:** it gets "Open Ports" (0100) and usually takes the letters if it is brave or ambitious and has 200 or more strength.
- **Check:** it is in the war on the king's side.

**V4. Seize an Island Seat.** While licensed, the band's adventurer decisions show *Seize an Island Seat*.
- **Expect:** it costs 150 prestige and declares a claim war, on Gotland first if it is in reach.

**V5. The licence lapses.** End the war (white peace).
- **Expect:** the band gets "The Licence Lapses", and the former enemy has "Raided Under Licence". *Seize an Island Seat* is gone.

**V6. The island seat and the fleet.** A licensed band that takes Gotland gets "A Harbour of Our Own".
- **Expect:** five or more years after the lapse, an AI king of another faith may gather a fleet (0130). *Hold* starts his claim war; *Pay* costs 100 gold.

**The Island Changes Hands**

**V7. The transfer.** Put Bædling courtiers on Gotland (at the holder's court), then hand Gotland to a Catholic by console (`create_title_and_vassal_change`), or conquer it.
- **Expect:** the ablest Bædling there gets "The Island Changes Hands". Inheritance never fires it.

**V8. The dates.** Set the year to 1361 with a Danish top liege; to 1391 with a holder who has the *adventurer* trait; to 1398 with a Christian theocracy; to 1407 under Denmark.
- **Expect:** each shows its own opening. Other cases show the generic one.

**V9. The voice.** A Catholic chaplain after 1200 speaks the crusade line in quotes, as his own. Before 1200 he calls only for the font. A Norse pagan lord has no voice line.

**V10. The levy.** Choose the levy.
- **Expect:** the result event shows held or broken; the county gets the matching modifier; Bædling fervour +3. The new lord gets "The Farmers Take Up Arms".

**V11. The ships.** Choose the ships.
- **Expect:** the members who are not rulers leave for the nearest Bædling court or camp.

**V12. No one there.** No members on the island, but a county that kept the faith.
- **Expect:** no event shows, and a modifier appears (usually *Kept Quiet*).

**The Peace of the Island**

**V13. The oath.** Gotland held by a Catholic, with Bædling courtiers there or a Bædling band camped nearby.
- **Expect:** within some years "The Peace of the Island" fires once. Swearing adds the county modifier and mutual +20 opinions.
- **Check:** before 1161 the opening text is the generic one.

---

## W. Under a lord's word, and No Service in the Prince's Wars (wave 4, added 2026-10-21, untested)

Design: [docs/wave4/protection.md](wave4/protection.md). These are flavour events: free the flavour budget first if you fire them by console.

**Under Her Chivalry**

**W1. The Fityan.** A Muslim count with his capital at Nishapur in 900, with a daughter of any of the six faiths at court. Set the chance to 100.
- **Expect:** `tm_fut.0001` fires; option a gives *Javanmard*.
- **Check:** the same at Fes, or at Nishapur in 1100: it never fires.

**W2. Entrust, plain.** A Muslim lord at Kairouan with a Badenya or Ha-Nehpakhot daughter as his guest.
- **Expect:** `tm_fut.0010` to her shows the plain text ("Put myself under [his] word"). Ask: `tm_fut.0011` goes to him. Give the word: she joins his court with *Under a Lord's Word* and the variable; he has *A Free Man's Word*.
- **Check:** she has `tm_world_quarters_asked` and `tm_fut_quarters_held`.

**W3. Entrust, fata.** The same at Nishapur in 900 with a *Javanmard* lord: the *fata* texts show.

**W4. The household.** With the daughter sheltered, force the `tm_world.0041` pulse chance.
- **Expect:** she is never picked (the lead's guard in `tm_world_on_actions.txt`). Remove his word: after two years she can be picked.

**W5. Refusing.** `tm_fut.0011` option b while he has *A Free Man's Word*.
- **Expect:** the modifier is removed, and −50 prestige.

**W6. The demand.** A sheltered daughter; his liege is Christian or Muslim.
- **Expect:** `tm_fut.0020` with the liege as demander. Option b shows only with *Javanmard*. Option c sends her to the nearest court of her faith (or the pool): no prisoner, and never to the demander.
- **Check:** with a Jewish liege, the demander falls to a neighbour, or there is no event.

**No Service in the Prince's Wars**

**W7. Terms, AI.** A Catholic count in Provence with two Ha-Nehpakhot courtiers. Raise the pulse chance.
- **Expect:** `tm_fut.0030` fires with the plain scribe line.
- **Check:** an Orthodox prince of Smolensk in 1230 gets the Smolensk line; in 1200, the plain line.

**W8. Terms, player.** Play that count.
- **Expect:** *Grant Terms to Her People* appears on a Ha-Nehpakhot courtier, and not on others. After granting, it is invalid ("already granted").

**W9. Knights.** After the grant, members with high prowess are not on the knights' list.
- **Expect:** `tm_fut.0032` option a puts one back. A member who moves to another court loses the modifier at that ruler's next yearly pulse, and can be a knight again.

**W10. The quarrel.** `tm_fut.0033` option b.
- **Expect:** the terms, the service modifier and the members' modifiers are gone; members −20.

**W11. Budget.** No lord gets more than one `tm_fut` event a year from the pulse.

---

## X. The Worn Garland: the market and the road (wave 4, added 2026-10-21, untested)

Design: [docs/wave4/garland.md](wave4/garland.md).

**X1. The market lamp.** A landless Garland daughter with 50 gold, in a county with a city. Fire `event tm_ml2.0010 <her id>`.
- **Expect:** option e shows. Take it: 40 gold gone, the permanent modifier, the county marked a temple street and `tm_ml3_market_lamp`.
- **Check:** move her; the modifier stays. A landed daughter, or a county with no city: option e is hidden. Fire it twice: +25 prestige the second time, and no second modifier.

**X2. The quarter that dwindled.** After 970, a Hindu lord whose capital has development under 12, with a Garland courtier who has no share. Fire `event tm_ml3.0010 <lord id>` and settle her.
- **Expect:** the share; 4 gold a year for ten years, then 8.
- **Check:** before 970 it never fires from the pulse.

**X3. The contract.** A player adventurer of the Garland camped in Tamil country.
- **Expect:** *Heroes of the Road* appears on the contract map from a Hindu or Jain ruler with a city county. Accept: 0020, then 0021, then 0022.
- **Check:** both toll branches, and that the contract completes (gold, prestige) or fails.

**X4. The AI contract.** An AI Garland adventurer in the Deccan. Run yearly pulses.
- **Expect:** it takes the contract and the chain completes.

**X5. The guild town.** Set `tm_ml3_caravans = 2` and complete one more caravan.
- **Expect:** the nickname; `tm_ml3.0030` to the employer (two counties or more); the offer; `tm_ml3.0031` to the band. Both "hold" options settle the band as his vassal in his farthest county, with *A Guild Town*. The dues option needs 50 gold.
- **Check:** declining changes nothing. An employer with one county gets no 0030.

**X6. Vannadu.** After 1220, a Garland countess holding a county with `tm_ml3_erivira` joins a faction.
- **Expect:** `tm_ml3.0040`; leaving the faction works; she is not asked again for 20 years.

---

## Y. Yutai Dao: Hide the Name and the Sogdians of Dunhuang (wave 4, added 2026-10-21, untested)

Design: [docs/wave4/yutai-sogdians.md](wave4/yutai-sogdians.md).

**Y1. Hide the Name, Sogdian.** Make a courtier of the Way of Sogdian culture under a Han lord (`set_culture` in the console).
- **Expect:** the decision *Hide the Name* shows. Take (b): the Guiji text, 25 gold gone, and she has `tm_yt3_name_hidden` and `tm_world_keep_quiet`. *Speak Aloud Again* shows.
- **Check:** use it. Keep Quiet ends, `tm_yt3_name_hidden` stays, and *Hide the Name* does not come back.

**Y2. Hide the Name, hostile court.** A daughter of the Way under a lord whose faith is hostile to the Way, or who has −20 opinion of her.
- **Expect:** the decision shows with the court description. Option (c) shows only if she is a councillor or knight, or her liege has 50 opinion of her or more.

**Y3. Not shown.** An independent ruler; a member of the Way who is not Sogdian, under a friendly lord; a Sogdian member under a Sogdian lord: no decision.

**Y4. After 903.** Hold a palace seal on 903.2.1 (`tm_palace.0003`).
- **Expect:** in 904 the yearly pulse brings `tm_yt3.0001` once, with the purge text, if she is still under a liege.

**Y5. The banquet.** Rule Shazhou with a Sisters' House after 900. Fire `tm_yt3.0010`, or let the pulse fire it (about once in 25 years).
- **Expect:** option (a) lowers the House strain by 1; half the time a Sogdian woman of the county's faith joins the court.
- **Check:** she is not of the Way.

**Y6. No Reply from There.** Fire `tm_yt3.0020` as a Shazhou ruler of the Way.
- **Expect:** if any Sogdian ruler exists (Transoxiana in 867), (a) sends her to that court, and that ruler's opinion of you rises by 15. Option (c) shows only if her learning is 8 or more.
- **Check:** she never has the Way's faith.

**Y7. Budget.** Neither 0010 nor 0020 fires while `tm_flavour_cooldown` is set.

## Z. Wave 5: the faith's voice is a daughter's; Bonadonna (added 2026-10-21, untested)

**Z1. Bonadonna on the bookmark.** Start the Crusader Dolls bookmark at 867. Bonadonna (Ha-Nehpakhot, Advanced) appears beside Arles in a physician's robes, with quill and book (portrait dumped 2026-10-22).
- **Expect:** playing her, she is a landless adventurer whose camp, *Women of the Lamp*, has the Scholars purpose and sits at Venaissin. The two Marked youths are in her camp; the physician's household (father, mother, three children) is at the count of Venaissin's court. There is no second, generated elder.
- **Expect (AI):** observing, the camp takes learning and stewardship contracts like any scholars' camp.

**Z2. Later start.** Start at 1066 or 1178: Bonadonna is dead, the camp does not exist, and the old setup runs (a generated elder and the youths at the count of Venaissin's court).

**Z3. Difficulty labels.** On the bookmark, Steinunn, Huijing and Cantirâdêvi are Medium; Theia Beatrike, Djeneba and Bonadonna are Advanced.

The succession scenarios (S1–S4) are in docs/wave5/succession.md; the offices' in docs/wave5/offices.md.

## AA. Adelphai Dorleyaiou: the Women's Chamber (wave 5, added 2026-10-22, untested)

**AA1. The chamber writes.** Observe 867 for 20-30 years. Unlanded daughters of the Sisters get *The Chamber Writes*; those who accept move to the emperor's court with *Post in the Chamber*.
- **Expect:** only daughters; never a Companion of the Mothers; never a cis or Marked sister.

**AA2. The estate.** A daughter in post at balance +2 under an AI emperor takes *Work the Chamber* and asks for an estate: she becomes a count of the faith. Check her government and error.log.

**AA3. The ladder.** At the chamber's ear the heresy laws stop for Dorleyite rulers under that throne; at the Patriarch's they come faster.

The full scenarios (C1-C6) are in docs/wave5/chamber.md.

**AA4. The counts.** An observe run to 1173 (run 9) showed no daughter invited in the last fifteen years and none in post, with three eligible daughters under Sabas, one of them eligible for 62 years. The roll logic is the same that set the invitation marker in run 8, so it may be chance at 5% a year, but the save cannot tell. From now `tools/census_report.py` prints the chamber's run-wide counts (rolled, fired, took, stayed, lost, estate).
- **Expect:** by 1000, with 3-9 daughters a decade, rolled in the tens; fired close to rolled; took roughly half of fired. Rolled 0 means the roll is not reached; rolled without fired means the event's trigger fails.

**AA5. AI daughters work the chamber.** The AI weighs decisions only for rulers, so no AI daughter in post ever took *Work the Chamber*: run 11, to 1361, had 64 letters, 28 posts and no chrysobull or estate. The yearly effect now works it for her (20% a year, at most once in five years). Expect `worked` in the tens over a long run, and some `chrysobull`; `estate` needs balance +2 and 200 prestige, so it stays rare.

## AC. Rulers from outside the community (added 2026-10-23, untested)

**AC1. The window fires.** In a long observe run, `tools/census_report.py` "Rulers converting in" shows `all` above zero for the Garland and Yutai. If all six stay at 0 while the faiths still grow, the AI converts by another road and the turning-away never runs (docs/faith_design.md §17). Run 12 failed this (9 in all, on `on_faith_conversion`); the hook is now `on_rite_change`. Expect tens or more a century wherever a faith is growing, and no seat holder at the start turned back (the mod's own conversions set `tm_conv_ours`).

**AC2. Turned away.** `turned away` is about a third of `outsiders`. A turned-away ruler keeps her old faith. Vassals or courtiers the game converted with her in the same stroke keep the new one.

**AC3. Not killed off.** Against run 11 (Garland 316 counties, Yutai 272 at 1361), the two large faiths are somewhat smaller, not gone; the four small ones are unchanged.

**AC4. Steinunn and Huijing** (added 2026-10-23). Start the bookmark at 867.
- Gotland: Steinunn holds the county, independent or under the same liege as Steinn was; Steinn is at her court, a Bædling, and her heir.
- Guasha: Huijing holds the duchy and its counties under Hexi, as Xun did; Xun is dead; Chengxun (7) is at her court, her adopted son and ward, of Yutai Dao, and her designated heir. The Suo noble-family estate went to Xun's heirs, not to her. Guasha is an appointed governorship (meritocratic), so the game may still appoint someone else when she dies.
- The selector shows her *of the Jade Embryo* with the tiger, and Steinunn *of Gute* with the whirl.
- The selector's map banner for Huijing is the tiger; in play, Guasha shows vanilla's Sha seal and Huijing's own arms the tiger.
- The two portraits are dumped (2026-10-23). Hovering each lights up her county: the highlight images are named for the bookmark entry (`gfx/interface/bookmarks/bm_867_crusader_dolls_bookmark_tm_<name>.dds`), renamed from Steinn's and Xun's.

## AF. After the 1140 observe run (added 2026-10-24, untested)

**AF1. Raised in the faith.** A child born at a court of another faith to a mother of the six and a father who keeps that court, in his house, takes the father's faith; with a matrilineal marriage, or no father at the court, the mother's. In a long run Yutai Dao should no longer hold the Mandate through a consort's son, and Yutai rulers in China should hold about as many counties as there are Yutai counties there, not ten times as many.
**AF2. The cup.** A landless adventurer of the Bædling who inherits her company's title still drinks the bragarfull, with no legitimacy error in error.log.
**AF3. Pardon.** No `tm_bae2_accuser.top_liege` context-switch errors in error.log.
**AF4. The council, forced.** As a landed Adelphai ruler, `run tm_council_now.txt` (from `tools/run/`). If no Galenic rite exists, another ruler founds it. The host gets *The Council of the Two Schools* (`tm_dl4.0001`); the most learned landed ruler of each wing gets her champion's event (0010 or 0011) 5-10 days later; the vote (0020) comes at day 40. The Athos option shows from 1083, Theophylact's from 1107. With no landed ruler on one side, debug.log says `TMDL4 FAIL`.
**AF5. After the vote.** If the Mother's book is kept, every landed Galenic ruler gets *After the Council* (0030); a player of the faith who did not host gets the result (0021). If the council breaks, the two champions have *Broke the Council* towards each other, and the next council can come after 15 years, not 25.
**AF6. The council, unforced.** In an observe run where the Galenic rite is founded, a council comes about ten years or more after the founding. The census's *Council of the Two Schools* line counts councils and outcomes. Neither wing should win every time.

**AF6b. Landless champions** (after run 15). With the Galenic rite founded and living members in both wings, a council comes even when one wing (or the faith) has no landed ruler; a courtier can be a champion. The census counts it under *called*.

**AF8. Ha-Nehpakhot mothers** (after run 15). A child of a Ha-Nehpakhot mother and a father of another faith, born into the father's house at his court, is born Ha-Nehpakhot. The Yutai rule is unchanged: a Yutai consort's son in a Han house is not born Yutai.

**AF9. The camp passes to the community** (after run 15). An AI Ha-Nehpakhot camp leader whose heir is a child or of another faith adopts a grown woman of the community in her camp and names her heir (`tm_hn_camp_heir_yearly`). Check in game that adopting an adult works and that the camp passes to her on the leader's death, not to the blood heir. If `set_designated_heir` does not hold for a camp, the fix needs another road.

**AF7. The Galenic teacher.** In a long observe run (867 to past 1000), the Galenic rite is founded even when the faith has no landed ruler besides the Mother of Mothers. The census's *Council of the Two Schools* section prints "Galenic rite: founded YEAR by a teacher's event" or "by decision". It should not come early in every run: about 2 in 100 a year from 886, with twenty quiet years after a teacher declines. If a courtier founded it, the faith view shows 2 rites, and landed rulers join it later by decision.

## AE. The small roadmap items (added 2026-10-24, untested)

**AE1. Galenic.** In a long observe run the Galenic rite is founded at least sometimes (save: a rite with `tm_body_galenic`). With it founded, the three Dorleyaian tenets show on the Galenic rite in the faith view, and the suppression ladder fires about half as often for its rulers.
**AE2. Tenets.** A reformed Garland, Ha-Nehpakhot or Badenya faith without the temple street, the three lamps or the House burying its own gets no shares, no three-lamps event and no burial event; the founding faiths still do.
**AE3. Two Parties.** A daughter under a ban at a vassal's court is freed when her liege issues the decree, and by the yearly check after.
**AE4. Rabbinic lord.** A Rabbinic Jewish ruler outside the Maghreb with a banned daughter at court gets `tm_hn2.0040`; lifting the ban displeases his own Jewish courtiers. No such event for a Rabbinic ruler in the Maghreb or the Sahel.
**AE5. Adornment.** A daughter of the Turning with none sees Commission the Adornment (50 gold); afterwards she has one adornment and the decision is gone. In the Maghreb she gets the attire.
**AE6. Garland.** A Garland ruler who is a daughter with 30 gold never gets `tm_garland.0020` (only `tm_ml2.0010`). A kovil honour holder with no daughter passes it to a daughter living in her county if it has a temple street (event shows the street text).
**AE7. Bædling.** `tm_bae5.0001`–`0030`: the níð-pole names the raiser and gives him "Raised a Níð-Pole"; option c enters a wrong in the Account (census `nid_poles` counts poles). The first cup comes from the wife or a woman of the faith at court. The bragarfull fires on inheriting a primary title, with the "chosen" text for a heir not born to the one before. Wulfstan's sermon only in Anglo-Saxon or English counties after 1014.
**AE8. Dress clause and island.** A dress-clause charge is brought only by a councillor, a landed vassal or the lord (or one of high prestige). An AI band does not settle on Gotland while the Peace of the Island holds.
**AE9. Badenya.** A Nubian heir answering the sister's line from 1155 sees the Dongola line. A passed-over sister's child gets "Passed Over"; letting it rest removes the claim. Taking a kingdom by conquest gives "A Hot Realm". A Muslim West African ruler with a Badenya jelimuso at court gets Praise Before the Court with the guest text.

## AD. The Account, the níð suit, reprieve (added 2026-10-23, untested)

**AD1. A wrong.** As a Bædling ruler, imprison a courtier of another house who is not an outlaw, or have one of your house killed outside a war (console `kill` with a killer is not enough: use a murder scheme). The head of each house, if a player, gets a toast: *A Gift Unpaid* / *A Gift Given*. The census "The Account" shows `wrongs`.

**AD2. Offer Bót.** As the wrongdoer's house, the interaction *Offer Bót* appears on a ruler of the wronged house, priced 50/100/150/200 a wrong by her rank. Accepted: gold paid, she gains prestige, both get *Settled the Account*, and a new wrong within ten years makes you a truce-breaker (major prestige loss, −40 opinion). Watch for AI offers (`tm_feud.0010`).

**AD3. Requital.** After AD1, wrong the other house back: the census counts a `requitals`, and the Account goes down by one rather than opening a second one.

**AD4. The three words.** Lose or win a flyting in a hall (five or more present) where the flyter's charge is *ragr*. Three days later *The Three Words* fires. Suing goes to the lord of the hall (*A Suit for Words*): outlawed, he leaves the court (a band if he is a fighter); arbitrated, he pays 50 gold (100 at the thing). No suit if he is a ruler or the lord himself. Alone (no witnesses), nothing.

**AD5. Reprieve.** Make an outlaw kill an outlaw (or kill one as her sworn sister). At the next New Year she moves one step: passage (a lord who takes her in owes the accuser nothing), then lesser outlawry, then free. A player outlaw gets *Named at the Thing*.

**AD6. Spring the Cell.** A discovered rescue (`tm_bae2.0011`) adds a wrong against the rescuer's house.

## AB. Badenya guardrails (added 2026-10-22, untested)

**AB1. Scenes that skip her.** Through the run, check that *The Court Wonders* (tm_world.0030), the trusted-servant event (tm_isl.0001) and the jester's mimicry (tm_isl.0002) never fire for a Badenya daughter or a daughter of a sub-Saharan heritage, and that tm_isl.0001 never fires at a West African court. Other daughters still get them.

**AB2. The satire result.** Pay the jeli what you can in *The Word That Cools* (tm_badenya.0012) and *Uninvited Praise* (tm_bd2.0030) until the satire comes up: the line mocks the purse, not her.

**AB3. The burial.** In *The House Buries Its Own* (tm_badenya.0030), giving her to her blood kin costs 20 piety.

**AB4. The claiming mother.** The woman who claims her in tm_badenya.0011 is never a prisoner or a concubine.

The full list is in docs/faiths/badenya.md, "Guardrails".

## AG. Ha-Nehpakhot: the batlle, the berurim, after the fall, a household of the street (wave 6, added 2026-10-25, untested)

Design: `docs/wave6/ha-nehpakhot.md`. The census prints run-wide counts under "Ha-Nehpakhot: households and falls".

- **AG1. Send for a Household.** Play a ruler of Ha-Nehpakhot (the 867 bookmark's Bonadonna leads a landless camp). The decision shows, costs 50 gold, and brings a man, his wife and their child (2–9) to her court as Rabbanite Jews of `sephardi` culture (from Barcelona); married, the child theirs. It is greyed out for ten years after. In an observe run: `households` above 0, and some `household_joins` over the decades.
- **AG2. The batlle.** At 1260 or later, a daughter of the Turning with a rival, in a county of Aragon, Barcelona or Valencia under a Christian lord: *Before the Batlle*, "to the batlle of …". Elsewhere it still reads "bailiff".
- **AG3. The berurim.** A Turning in the Crown of Aragon from 1270: the hearing reads "The berurim of the street"; at Arles, the worthies, rectors or baylons by date as before.
- **AG4. After the fall.** Give a lord `tm_translation_patron_modifier` (or let *A book in Arabic* fire), keep a daughter of the Turning at his court, and kill him: within a month *After the Fall* fires; her county has `tm_hn4_after_fall` for a year; option a or c sets `tm_hn4_sheltered`; option b's win removes the county variable. `falls` counts it.
- **AG5. Errors.** No new error.log lines from `tm_hn4_*` files; the bailiff's and judges' loc show no raw `Custom(...)` keys.


## AH. Bædling: the sorcery law, the feud, outlawry and lore (wave 7, added 2026-10-25, untested)

Design: `docs/wave7/baedling.md`. The census prints three "wave 7" sections.

**AH1. The suit and outlawry**

1. **Norway 1150 suit.**
   - (b): no gold paid at once. Fourteen days later the accuser gets 0105, then the ring is paid (lord and accuser get 5 each) and she goes abroad.
   - (c): she forms a band only after 0105.
2. **Court fails:** a House member in a House county with 2 sworn sisters at court has about a 70% fail chance. The sentence lapses, the accuser loses prestige, and she has no modifier.
3. **Accuser dies inside the fortnight:** no 0105; the flag clears after 30 days.
4. **Magnus 1180:** with a Norwegian lord who has a chaplain, the chaplain gets half and the lord half.
5. **Iceland:** a seeress charged under a lord with an Icelandic capital gets the "no suit" text. Set `tm_bae2_last_seeker` by console to check the client branch: 0101 goes to the client, with the twelve-jurors option.
6. **Penance:** from 1300, (d) gives the modifier, the condition var and exile. A second suit under a Norwegian lord (from 1300) gives "Take her into my keeping", and she is imprisoned. Spring the Cell can target that jailer.
7. **Ride:** a full outlaw band player with 2 sworn sisters sees the decision; the accuser gets 0130 with ride text and price 50. Refusing costs 2 × minor prestige.
8. **Harbouring:** a full outlaw courtier of a House holder adds strain +1 a year and +5/−5 prestige; 0115 fires. Check the house relation on refuse when one party is Bædling.
9. **Holm:** a full outlaw band camped 3 years in a mountain or island county (e.g. Gotland) gets the modifier and the county modifier.

**AH2. The feud**

1. **Escalation:** a Bædling count's house wronged by a baron's house, then a requital on that house's duke (adult) shows "It Overbalances", and the Account flips. A requital on an unlanded child is equal or lower, never higher.
2. **Self-judgment:** as a player who owes, Grant Self-Judgment to an AI.
   - Prestige cost is taken.
   - 0040 fires and the toast arrives.
   - Each option settles the Account (`tm_acc_settled`, 10 years).
   - The heavy option gives "Uneven" from same-faith or Germanic rulers in range.
3. **Refused Account:** an AI arrogant Norse Christian ruler imprisons or raids a Bædling queen.
   - The toast shows his line.
   - `tm_acc_refused` is on her house.
   - His next wrong is not written.
   - Her house's next wrong against his gives "Answered with Honour" opinions and the prestige swap.
4. **Fostering:** Offer Bót with the foster option.
   - The child becomes the ward and moves to court.
   - The truce lasts 15 years.
   - The actor loses minor prestige.
   - The option is greyed out when no child qualifies.
5. **Truce broken:** the victim's house head gets "Bót Spent on Spears" for 2 years.
6. **Avenge Her:** kill a full-outlaw Bædling who has a sworn sister. 0060 reaches the sister in 7 days; "take up" writes the Account against the killer's house, and no truce-breaker penalty applies.
7. **Suit-bearer:**
   - A níð suit under a Catholic lord with a husband at court: the bearer portrait appears in 0020 and 0021.
   - The same with no eligible man: the option is greyed out ("No man would carry it").
   - Under a Bædling lord: no bearer is needed.

**AH3. The era and lore**

1. Start 867 and run to 995+ with a Bædling courtier in Norway under a Christian king, to see 0001. Check that the Norway variant shows, and that "leave" moves her out of the realm.
2. Iceland, 1000–1010: the Iceland variant shows.
3. From 1300, a Bædling vassal holding a House under a Catholic king gets 0010. Each option works; strain rises on obey or on a lost argument.
4. 1343: Bædlings in Norway or Iceland get 0020 once (1343 text). 1407: the 1407 text. The fear modifier lasts 5 years.
5. A Norse lord with a daughter of seiðr at court and a rival gets 0100. Vassals of another faith take −10. "Own it" appears only for a Bædling lord, and the Account entry is made.
6. The warding shirt interaction appears on a sister, ward or friend of the House; costs 30 gold; has a 3-year cooldown; the modifier lasts 5 years.
7. Give a Bædling ruler Gotland (`c_gutland`) by console: 0204 fires once, and the county modifier lasts 10 years. Repeat for the other four sites.
8. 1350+: put a declared or Marked woman of any of the six faiths in an English county. In 0300, the broiderer's name is never Eleanor, Anne or Elizabeth, and "I have my own" opens `tm_house.0001`. 0301 sometimes follows and ends open.

## AI. Galenic rite divergence (added 2026-10-25, untested)

- [ ] **AI1.** Faith Details > Rites: the Galenic Rite shows Divergence 25%, not 0%. `doctrine_tm_body` is a sequence group, so divergence is the difference of its doctrines (Aristotelian 0, Galenic 25); both were 25 before. Check an existing save too, to see whether divergence is recomputed on load.
- [ ] **AI2.** The teacher's students: found the rite (decision or `event tm_dl2.0003`). Up to three adult non-ruler members of the main rite take the Galenic rite with her, her own court first, and each has +20 opinion of her. The census prints `students`.
- [ ] **AI3.** The school's reach: in an observe run past the founding, the census shows `school_joins` above 0 and "now N of M Galenic". The rite keeps members after its founder dies, and the Council of the Two Schools is called (`called` > 0). Watch the share: if it passes about a third, build a flow back. In the run-17 save (rite founded, no members) the yearly roll should revive the rite at the base chance.
- [ ] **AI4.** Offer Bót's fostering is now a checkbox (`send_options_exclusive = no`): the error "Exclusive send options should at least be two" is gone, and the box can be ticked or left.
- [ ] **AI5.** Wider suit-bearers: a níð suit under a Catholic lord with a man of the six faiths at court, or a man with opinion 20+ of her, finds him as bearer. The greyed-out text lists the new kinds. Run 18 showed the search itself only looked at friends of a House (2 borne, 50 with no bearer); fixed to search every courtier at her court and the lord's. Next run: `nid_borne` well above 2.
- [ ] **AI6.** Send for him: with no man at either court and a husband or brother elsewhere, 0020 shows the far-kin desc line and option c. In 60–150 days, a toast says he came (then 0021 fires with him as bearer) or will not come. Census: `nid_kin_sent` = `nid_kin_came` + `nid_kin_refused` (minus any lapsed because she, the speaker or the lord died).
- [ ] **AI7.** "þing" renders in every event that used "the thing" (feud, flyting, seiðr 0003, bae5). Check the Þ in "Before the Þing" and "Named at the Þing".

## AJ. Adelphai: the Tower on the Condition (wave 8, added 2026-10-25, untested)

- [ ] **AJ1.** Petition: an Adelphai sister at an Orthodox count's court in Asia Minor. With the global cooldown clear, the count gets *A Tower on the Condition* for his least-developed non-capital county. Grant: a House is founded there, tolerated by him; the county shows "A Tower Being Rebuilt"; she is Keeper of the Tower, pays 50 gold if she has it, has +25 opinion of him. He is never asked twice.
- [ ] **AJ2.** The condition: with two sisters at his court for five years, *The Tower Stands* fires and the county shows "The Sisters' Tower". With fewer than two for two years running, *The Tower Stands Empty*: take it back closes the House (sisters go elsewhere); one more year resets the count.
- [ ] **AJ6.** The sisters come (after run 18): at the grant, up to two members not at a court of the faith move to the lord's court (`came` in the census); a tower short of hands draws one more at 25% a year. Wives of rulers and councillors stay put. In an observe run, `kept` above 0.
- [ ] **AJ3.** A kept tower's county passing to another Christian lord: 0050 shows the tower line, and AI lords mostly let it stand.
- [ ] **AJ4.** The herders (0020) on a kept tower: the modifier lasts twenty years; no repeat in that county for thirty.
- [ ] **AJ5.** Observe run: the census "Tower on the Condition" counts; does a granted tower draw sisters (gathering), and do the Adelphai hold more members than in runs 16–17 (13–18)?
