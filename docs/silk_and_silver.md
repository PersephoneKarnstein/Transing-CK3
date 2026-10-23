# Silk & Silver: notes for Crusader Dolls

Speculative notes, written 2026-10-20, before release. *Silk & Silver* is the next major expansion. It comes out on 17 November 2026 with a free patch, and nothing here is final until then. The sources are the seven Silk & Silver dev diaries (DD1–DD7, April–October 2026) and the release announcement, read through Steam's news feed. The diaries say "Everything is subject to change" more than once, and a "more technical dev diary" on script and modifiers is still to come (DD2). Recheck everything below against the released files before writing any script.

## What the expansion adds

**Free in the patch (every player).** DD1 says the economy rework is free "as they are essential for the rebalancing of the game's economy".
- **Districts and buildings.** Every regular building is removed. Holdings get district slots, and buildings go inside districts. Special buildings stay, with changed effects.
- **Development is split in two.** *Settlement Size* runs 1–10 and sets the number of district slots. *Prosperity* drives tax and draws traders.
- **County control** drifts toward a baseline and no longer always reaches 100.
- **Popular opinion** runs from −100 to 100 and also drifts toward a baseline. A positive opinion now gives bonuses.
- **Mercenary limit.** A new cap on hired companies.
- **A Usury doctrine** in Rites: forbidden, "permitted with outsiders", or accepted (DD6). Under some faiths a borrower can *Denounce a Usurious Loan* and keep the gold.
- **Split income modifiers**, such as maritime income in place of general income (DD1).

**Trade (DD2, DD5).**
- **Markets.** There are over 900, one per de jure duchy, sitting in the duchy's capital barony.
- **Goods.** 40–50 trade goods in categories. The basic categories are Cereals, Meat, Beasts of Burden, Basic and Precious Metals, Carpentries and Stone. The others are:
  - Comforts, Salt, Clothes (Textiles, Furs, Leather) and Fabrics;
  - Dyes, Alum, and Luxury Items (Ceramics, Glass, Jewelry, Lacquerware, Silk);
  - Precious Stones (Gems, Amber, Ivory, Jade), Medicaments and Incense;
  - Luxury Consumables (Sugar, Spices), Books/Paper and Alcohol.
- **Production and needs.** Buildings produce goods and have *needs*, which give optional bonuses when supplied.
- **Routes:**
  - *Profit Routes*, run by merchants and republics;
  - *Distribution Routes*, run by dukes and above for basic goods between two markets they hold;
  - *Commission Routes*, which landed rulers offer to merchants.
- **Expertise and Acumen.** *Trade Expertise* lives on the company title, so it survives succession. *Acumen* rewards profit.
- **Competition.** Routes compete for market share through *Competitiveness*. A market's holder can grant *Monopolies*: "normal" ones take the surplus, "exploitative" ones take local needs as well.
- **Moving goods further.** *Entrepôts* (Cairo, Baghdad, Constantinople, Venice and points on the Silk Road) resell goods along a fixed direction, and market owners can set *tolls*.
- **Roads** form where routes run for years, and decay when trade stops.
- **Modding.** Goods are "entirely defined by script, so yes, modders, you can go wild" (DD2).

**The landless merchant government (DD3, DD6).**
- **Becoming a merchant.** A family *Company* based in a *Company Palace* (domicile), inside a city. You can make a merchant at game start anywhere, or take a *Become Merchant* decision, which is gated by culture (*Fortune Seekers* and *Saharan Traders* allow it). Patricians and adventurers can take the decision too.
- **Patron and Charter.** The *Patron* is the holder of the county where the palace stands, and the merchant becomes their *Beneficiary* (a tributary type). A good relationship can earn a *Merchant Charter*: one per patron, with several beneficiaries competing for it. The charter can be used to invest in the patron's land, or "abused" for prestige at the risk of prison.
- **Purposes** (final list): *Reputable*, *Artisan*, *Creditor* (which absorbed *War Profiteer*, so it also sponsors wars) and *Caravaneer*. Each has a capstone decision.
- **Contracts.** *Trade Opportunity*, *Unity* and *Luxury* contracts. Luxury contracts are the only source of domicile artifacts.
- **Company Size** runs from "Aspiring Business" to "Trade Empire" and unlocks charters from patrons of higher tiers.
- **People.** *Traders* are family or *Associates* (courtiers), assigned to routes, and rival companies can poach them.
- **House Unity.** High unity means blood and prestige. Low unity means "getting skilled characters involved in the Trade, no matter the blood ties" (DD3).
- **Rival houses.** House relations sour between companies selling in the same markets. The tools are *Challenge* and *Sabotage Competitor*, *Steal Market Insights*, *Merge Company* and *Hostile Takeover*.
- **Loans.** *Loan Gold* at open interest (25%), disguised interest (15%) or no interest. Repayment gives a strong hook, and the debt is inheritable.
- **Silk Road.** Merchants in the Silk Road region join a *Silk Road Situation* participant group. Its bonuses depend on the phase in their sub-region. Every Silk & Silver owner gets this, with or without All Under Heaven.

**Republics (DD4, DD6, DD7).**
- **The city.** Republics are city-states with patrician houses and an *Assembly* that votes on laws and decrees. Its membership, majority and remit are themselves laws.
- **Succession and titles.** Rulers are elected. Despotic laws can make the ruler hereditary, and the ruler's title changes with them (Doge → Prince).
- **Administration types** include Maritime and Communal. Count-tier republics are Communal only.
- **Growth.** Republics rise in tier through capital Settlement Size, not through de jure titles.
- **House politics:**
  - *House Ambitions*: Commerce, Aggrandizement, Communal, Signorial and Agitation.
  - *Patrician Rating*.
  - *Civic Works*.
  - A *Capital Uprising* faction when popular opinion is low.
- **Trade Posts.** A district a republic can hold in someone else's county, one per county. It brings the *Conquer Trade County* CB.
- **Trade Leagues.** A confederation of republics. Its CBs are *Trade War*, *Proclaim Commune* (free a ruler's land as a league republic) and *Enforce a Monopoly*. The Hanseatic League has its own decision and the *Kontor* building.
- **Italy.** A Guelphs & Ghibellines situation, Italian traditions (*Contado*, *Civic Religion*, *Roman Law*) and a Carnival activity.
- **Bookmarks.** *1066 Channels of Commerce* and *1178 Guelphs & Ghibellines*.

**The diaries' own historical reference points.** DD1 cites "the Jewish families in Cairo that traded goods far and wide, or the trade guilds of southern India". DD3 shows "Wuhsha's Domicile at Game Start": Wuhsha was an eleventh-century Jewish businesswoman of Cairo known from the Geniza. DD5 cites "the Cairene Geniza" as the model for cooperation between merchants. So vanilla will already depict Jewish merchant houses, led by a woman, at the 1066 start. That sets the baseline our own content sits beside.

## What it breaks or forces (compatibility)

These are checks to make on release day, in order.
1. **`supported_version`.** The patch will probably be 1.21, so bump the version after testing. Workshop users will update the game before we do.
2. **The Usury doctrine.** If the new doctrine group has no default, all six faiths fail validation. Each needs a deliberate choice; see the recommendations below.
3. **`development_growth_factor`** appears in `common/modifiers/tm_modifiers.txt` (two modifiers, both using the `county_modifier_development_positive` icon). Development is being split, so this modifier probably gets renamed or removed. It most likely maps to Prosperity growth.
4. **`domain_tax_mult`** appears in the court position (`tm_court_positions.txt`), and **`monthly_income_mult`** in three tenets (`tm_tenet_types.txt`). Both may survive. DD1 talks of splitting general modifiers, so check them.
5. **`building_gfx = byzantine_building_gfx`** in `tm_cultures.txt` (kybeline). Building art may move to districts.
6. **Kovil and Byzantine events.** `tm_kovil_*` (the temple's deal) and `tm_byzr_*` mention holdings and temples. They need checks for any building or holding assumptions.
7. **Control and opinion.** Our footholds (Gotland, Candragiri, Kirina) assume county control returns to 100. Under the new baseline system, a freshly converted county may stay at low control for good. Watch the observe runs.
8. **DLC gating.** The mod must keep working without Silk & Silver. Anything below that touches merchants, republics or trade has to sit behind the DLC-feature check the release introduces (its name is not yet known).
9. **Run xTiger** against the new game files and compare with the baseline of 21 reports.

## Ideas, faith by faith

### Ha-Nehpakhot: a house in the street (strongest fit, most care needed)

**Why it fits.** Ha-N's structural problem is that it holds no land and has to be carried by births, matches and pilgrims (see the faith page's *Growth*). The merchant government is a landless dynasty structure with continuity built in:
- **Expertise survives succession.** Trade Expertise lives on the company title, not on a person.
- **The company takes in members.** Associates are courtiers who work the company.
- **Chosen family suits low House Unity.** Low unity explicitly rewards skilled outsiders "no matter the blood ties", which matches adopted daughters.
- **The patron is the lord the sect already serves.** The count of Venaissin, or whoever holds Arles, is Ha-N's existing protector.

**The Charter is the licence.** The faith page already models Provençal privileges granted for a term: Gordes in 1312, ten years, renewable (Shatzmiller 2023, p. 182), and the ban licensed by the lord (Shatzmiller 2023, pp. 86–89). A *Merchant Charter* from the patron is the same shape. One possible design: while the kahal's company holds the patron's charter, that county counts as licensed for the Turning. That would replace or stack with the ten-year licence won before the baylons.

**It also answers the open TODO of an unlanded start.** A Ha-N merchant at Arles could be the sixth bookmark character, if the game allows merchants at 867. That needs checking: vanilla's merchant bookmark is 1066.

**Goods with documented support:**
- **Textiles (drapery).** Venguessona Nathan, a widow, was a draper with a shop in the Jewish market. The baylons met in her house (Ben-Shalom 2024, pp. 120–121; Hildenfinger, *REJ* 47: 224–226).
- **Medicaments.** Jewish women physicians appear in "dozens of the documents" (Shatzmiller 1994, p. 109). The fisica event is already in the mod.
- **Books/Paper.** Translators (Kalonymus at Arles, 1307–17) and the women's prayer book (Leeds Roth 32) are both in the faith page already.

So the house is a draper's and an apothecary's company, plus a scriptorium. Its purpose leans **Artisan** (books as artifacts) or **Reputable**, and its trade stays **regional**: Arles–Montpellier–Narbonne–Marseille, matching the holy sites and Ben-Shalom's Provence-Languedoc frame.

**Guardrails against antisemitic stereotypes.** Each S&S feature is mapped to the stereotype it could feed:

| S&S feature | Stereotype it can feed | What we do |
|---|---|---|
| *Creditor* purpose, *Loan Gold*, the usury doctrine | The Jewish moneylender and usurer | Ha-N's company never takes Creditor, and our events never show it lending at interest. This holds even though Arles women did lend: 11 of 43 Jewish lenders in 1436–40 were women (Ben-Shalom 2024, p. 120). The project's existing rule stays: "no moneylending as trait or motive" (research note on Ben-Shalom). |
| Creditor absorbed *War Profiteer* ("sponsor wars") | Jews financing wars and crusades | Already banned in the research notes ("No Jewish financiers of wars or crusades"). Same rule, now with a mechanic attached. |
| *Trade Empire* size, monopolies, *exploitative monopolies* | Jewish control of markets or of "the economy" | No events of ours that celebrate cornering a market. AI tuning is probably unnecessary: in the observe runs Ha-N barely survives, so a Ha-N trade empire would take a skilled player and a long campaign. That is the player's story, not the mod's framing. Recheck once the DLC is out. |
| Long-distance and Silk Road networks, Radhanites | A worldwide Jewish network | Routes stay in Provence and Languedoc. Ha-N's pilgrim pull is already limited to Marked young women. Never frame it as a network of money. |
| Slaves as trade goods (none in the published list) | The Radhanite slave-trade motif (Phelan 2023) | Already banned. If any mod or later DLC adds slaves as a good, no Jewish character trades them. |
| *Abuse Charter*, *Hostile Takeover*, *Sabotage*, *Steal Market Insights* | Jewish disloyalty to protectors, cunning, secrecy | No flavour events in which the kahal betrays its patron, and no AI weights of ours pushing Ha-N toward these. |
| Wealth as the reason a lord tolerates the kahal | "Court Jew" as purchased protection | Our text grounds protection in service (medicine, translation, books), as the faith page already does. Gold never buys the license in our own events. |
| Vanilla *Denounce a Usurious Loan* | Hostile clergy voiding Jewish debts | That is vanilla content. If we write anything around it, the hostile voice is attributed and never the narrator's. |

**The usury doctrine.** Recommendation: whatever doctrine vanilla gives its Jewish faiths, Ha-N matches it. Giving the sect a stricter doctrine than its parent religion would cast it as "the good Jews" by contrast, which is its own antisemitic trope. The sect is defined by its gender theology, not by being better at money than other Jews.

**Reading to do before writing.** Raw texts stay gitignored as usual, and notes hold short quotes only.
- Julie L. Mell, *The Myth of the Medieval Jewish Moneylender* (2 vols, 2017–18). It argues directly against the stereotype and is the best guard for the Creditor question.
- Michael Toch, *The Economic History of European Jews: Late Antiquity and Early Middle Ages* (2013). It is sceptical of the Radhanite and long-distance-trader picture.
- S. D. Goitein, *A Mediterranean Society*, vols 1 and 3, for Geniza business partnerships and Wuhsha.
- Jessica Goldberg, *Trade and Institutions in the Medieval Mediterranean* (2012), for how Geniza merchants actually cooperated. That is the positive model DD5 points to.

### Bædling: Gotland and its silver

**Silver hoards.** Gotland has the densest concentration of Viking-age silver hoards in Scandinavia (to verify with a source before using it in text), so the expansion's very title lands on our seat. Possible uses:
- a Precious Metals or Amber identity for the Gotland market;
- a *Luxury Contract* or event in which the hall buries or raises a hoard;
- a domicile artifact.

**The Hansa threat.** Trade Leagues and the Hanseatic League decision put a strong league of republics in the Baltic. Its *Proclaim Commune* CB can turn a non-republic ruler's land into a league republic, and Visby was historically a Hanseatic town. In later starts this is a real risk to the seat. Watch in observe runs whether the AI targets Gotland. If it does, the earlier "faith rules Gotland" decision may need a defensive answer. That must not be a size cap.

**A Gutnish commune.** Medieval Gotland governed itself through its own thing under loose Swedish overlordship (the *Gutasaga* tradition; to source). A late decision could let Bædling Gotland become a Communal republic, with its thing as the Assembly. The flyting would then serve as Assembly politics. This is optional, gated behind the DLC, and only worth it if republics turn out to suit a pagan tribal seat.

### Yutai Dao: on the Silk Road itself

**The setting.** Shazhou/Dunhuang sits in the Hexi corridor. The *Silk Road Situation* participant group, Silk Road entrepôts, and the Silk and Jade goods (Khotan jade) all fall on its doorstep. Yutai Dao is already the mod's most stable faith, so it doesn't need a boost. It does have the most flavour on offer:
- nüguan or Marked courtiers as Traders;
- a Caravaneer house whose route bonuses follow the Silk Road phase;
- Luxury Contracts bringing back silk or jade artifacts for an abbey.

**Women's associations.** The Dunhuang manuscripts include charters of lay associations (*she* 社), including women's associations (to verify a specific manuscript before use). Such an association, rather than a company, could be the kind of mutual body the faith wraps around a daughter.

**Restraint.** It's a courtly faith of intrigue and stewardship, so Acumen and Negotiate Deals fit it better than war.

### Cūṭikkoṭutta Mālai: the guilds of the south

**The diary's own hook.** DD1 names "the trade guilds of southern India" as a model. These are the Ainnurruvar (the Five Hundred of Ayyavole) and the Manigramam, whose inscriptions record gifts to temples.
- **The temple-gift mechanic.** The faith already turns gold given to a temple into an inscription and lasting piety. S&S's *Sponsor Construction* interaction, and the Charter's "reinvest into Prosperity" path, are that same act seen from the merchant's side.
- **A Kanchipuram house.** A merchant house there, with the Candragiri countess as patron, could fund the inscriptions that the faith's event chain already writes.

**Goods.** Textiles, Cotton, Dyes, Spices and Incense all fit.

**Reading:** Meera Abraham, *Two Medieval Merchant Guilds of South India* (1988); Kenneth R. Hall, *Trade and Statecraft in the Age of the Cōḷas* (1980); Leslie Orr, *Donors, Devotees, and Daughters of God* (2000), for women donors.

**Care.** Avoid casting caste as an economic engine, and avoid making temple women into trade goods or "dancing girls". Orr's work exists precisely to correct that picture.

### Badenya: gold and salt

**A ready-made tradition.** *Saharan Traders* is a vanilla tradition with a Become Merchant decision, longer routes and expertise in salt, precious stones and precious metals. The Bure goldfields lie near Kirina and Niani (to source; Gomez 2018 probably covers it). The Mande-speaking traders, the Wangara and later Dyula, are the obvious historical merchants here.

**No captives.** A Badenya house never trades in captives or slaves, whatever the period's trans-Saharan trade carried (Badenya Guardrails 1 and 13, [docs/faiths/badenya.md](faiths/badenya.md#guardrails)).

**One caution about the Dyula.** They were Muslim, so a Badenya merchant house should not be presented as "the Dyula". A Badenya-faith house among Mande traders is enough.

**Fit with existing content.** Commission routes and the jeli's praise economy fit together: gold paid for praise is already a Badenya theme. Smiths belong to a nyamakala group, not a merchant one, so keep the faith's smith out of the merchant role.

### Adelphai Dorleyaiou: the road and the City

**Roads.** Dorylaion was an army camp on the road east, as the faith page notes. S&S roads form where trade runs for years, so a route through Phrygia would literally pave the Mother House's road. Ideas: the Mother House as patron of caravans, or a *Kybeline* tradition tweak that gives *esteemed hospitality* a road or route bonus.

**The City.** Constantinople is a vanilla entrepôt. The guilds in the *Book of the Eparch* (silk dealers, among others) are a possible source if we want guild flavour (to read).

**Restraint.** The carzimasia event already keeps "the merchants of Verdun" unnamed by faith. Keep it that way, and never attach the child-eunuch trade to a Jewish merchant house.

## Mechanics shared by several faiths

- **Associates and the Marked.** A merchant company's Associates are courtiers. Our growth engine already moves Marked characters into courts (`tm_surv_gather_effect`, the call). Under S&S, a company of the faith would be a natural home court, and the homecoming's choice of home court might weight a company's head. Keep growth slow ([[feedback-growth-tuning]]: small faiths grow slowly, no visible caps).
- **Popular opinion as the world's reaction.** Now that opinion is bounded and gives bonuses, a daughter's public naming could move it a little. That would be a light way to show the world reacting without an antagonist nation.
- **Trade Opportunity schemes as rite steps.** Pilgrimage-like steps (the völva's journey, the guarantor's travel in Yutai Dao) could borrow the S&S scheme with its Push for Advantages button, if it turns out to be scriptable.
- **One choice per faith for usury:**
  - *Ha-N* follows vanilla Judaism.
  - *Adelphai* follows Orthodox Christianity.
  - *Bædling*, *Badenya* and *Mālai* follow their parent religions.
  - *Yutai Dao* follows vanilla Taoism.

  Each faith takes its parent's position unless a source gives a reason to differ.

## Open questions for after release

- **Merchants at 867.** Can a merchant (landless, with a domicile) exist at the 867 start in history files? This decides whether Ha-N gets its unlanded bookmark start through S&S.
- **The decision gate.** Is *Become Merchant* gated only by culture tradition? Ha-N takes the county's culture, so we may need our own faith-gated decision rather than an override of the vanilla one. Overriding risks breaking compatibility.
- **The trigger name.** What is the DLC-feature trigger for Silk & Silver content?
- **Where Expertise lives.** Can company Expertise sit on a title we create (a "house in the street" title), as vanilla merchants' does?
- **Vanilla's Jewish faiths.** Which usury doctrine does vanilla give them? And does the 1066 bookmark place Jewish merchant houses in Provence, where our kahal would meet them?
