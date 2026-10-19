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
- In the faith screen, check that *Dorleyism*, *Bædling* and *Way of the Jade Embryo* all exist with their icons and holy sites.
- Check the holy sites:
  - **Dorleyism:** Dorylaion, Constantinople, Kyzikos, Ankyra, Pepouza.
  - **Bædling:** Uppsala, Trondheim, York, Kyiv.
  - **Way of the Jade Embryo:** Mogao, Longhu, Qingcheng, Wudang.
- Send `error.log` even if nothing looks wrong.

**0.2 Starting presence.**
- Phrygia should be Dorleyite and held by Theia Beatrike, the Mother of Mothers, with three Elder Sisters at her court.
- Gotland should be Bædling, with a völva at court.
- Shazhou should follow the Way of the Jade Embryo, with a nüguan (a Daoist nun) at court.
- Hover over Theia's portrait and screenshot the debug tooltip.

**0.3 Census.** Run `run tm_census.txt`. Note the counts of Marked characters and daughters. They should be roughly 1% of adult men, and a handful of daughters.

**0.4 Ruler Designer.** Check that all three faiths and the Kybeline culture can be picked, and that the Marked trait costs nothing.

---

## A. Dorleyism

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

Play Gotland, or design a Bædling ruler. Then `add_trait tm_transgender` on yourself, `piety 500` and `gold 500`.

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

## C. Way of the Jade Embryo

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

**D1. Declare Before Witnesses.** As a Marked man in any of the three faiths, take *Declare Before Witnesses* and choose a name.
- Then go through your faith's rite (A1, B1 or C1), **once with re-embodiment on and once with it off.**
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

**D5. Sisters' Houses.** As any ruler of the three faiths, run `run tm_make_sisters.txt`, then take *Found a Sisters' House*.
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

**D9. The Sisters Choose.** As a duke or higher of any of the three faiths, change your realm's succession law to *The Sisters Choose*.
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

**D12. Same-sex marriage.** In all three faiths, check that two women, including a daughter and a cis woman, can marry, whatever the vanilla game rule says.

---

## E. Long AI run (no playing needed)

Start a new 867 game, pick any ruler, type `observe`, and run at full speed to about 1000 or as far as you can. Then:
- run `run tm_census.txt`;
- save the game and send the save and `error.log`.

This shows whether the AI ever uses the rites, Houses, fostering, Companions, the elective law and the court offices. It also catches errors that only show up after decades.
