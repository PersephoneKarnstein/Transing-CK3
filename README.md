<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">

![Crusader Kings III 1.20](https://img.shields.io/badge/Crusader%20Kings%20III-1.20.*-8a2be2)
![Status: alpha](https://img.shields.io/badge/status-alpha-orange)
![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue)
![Playtesters wanted](https://img.shields.io/badge/playtesters-wanted-f5a9b8)

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="docs/images/logo.png" alt="Logo" width="96" height="96">

  <h3 align="center">Transing CK3</h3>
  <p align="center">
    <em>Adelphai Dorleyaiou</em>, the Sisters of Dorylaion: four trans-women-centred faiths for Crusader Kings III.
    <br />
    <a href="#playtesters-wanted"><strong>Help playtest »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PersephoneKarnstein/Transing-CK3/issues/new?labels=bug">Report a bug</a>
    ·
    <a href="https://github.com/PersephoneKarnstein/Transing-CK3/issues/new?labels=enhancement">Suggest a feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of contents</summary>
  <ol>
    <li><a href="#about-the-project">About the project</a></li>
    <li><a href="#playtesters-wanted">Playtesters wanted</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#loading-the-mod-from-this-folder">Loading the mod from this folder</a></li>
        <li><a href="#what-to-test-and-how-to-report">What to test and how to report</a></li>
      </ul>
    </li>
    <li><a href="#dorleyism-the-sisters-of-dorylaion">Dorleyism: the Sisters of Dorylaion</a></li>
    <li><a href="#bædling-the-high-seat">Bædling: the High Seat</a></li>
    <li><a href="#the-way-of-the-jade-embryo">The Way of the Jade Embryo</a></li>
    <li><a href="#ha-nehpakhot-the-women-who-were-turned">Ha-Nehpakhot: the women who were turned</a></li>
    <li><a href="#shared-mechanics">Shared mechanics</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#bibliography">Bibliography</a></li>
  </ol>
</details>

## About the project

This mod adds four faiths built around trans women to Crusader Kings III. Each is grounded in a different historical setting and plays differently. Their tenets come from contemporary transfeminist writing: baedelism, third-wave transfeminism and transgender Marxism. A history pass then gives each a veneer of plausibility in its own place and period.

The four faiths answer the same three questions in different ways:

| Faith | How one becomes a daughter | How the line continues | How it meets the world | Home |
|---|---|---|---|---|
| **Dorleyism** | The knife, as a sacrament with a sponsor | A founding charter passes land to adopted daughters | Refuge, intake and church politics | Dorylaion, Phrygia |
| **Bædling** | Seiðr: a völva goes into trance for the seeker | The hall's fostered, sworn and adopted daughters | Outlawry, raiding and insult duels | Gotland |
| **Way of the Jade Embryo** | Ten months' inner gestation of one's own body | Adopted heirs, and temple societies that hold property in common | Palace factions against the scholar-officials | Dunhuang, at the Mogao caves |
| **Ha-Nehpakhot** | The Turning: a prayer said aloud at Purim | The women of the lamp, and the three women's commandments | The baylons' licence or their shunning; patronage by translating or medicine | The Jewish street of Arles |

What the mod is not:

- **No antagonist.** It does not add a hostile "anti-trans" nation or stage an allegorical clash of superpowers. It adds the faiths, and vanilla Christendom, the Caliphate and the Tang court react as they would.
- **Not trans men.** Trans-masculine content is out of scope. Someone else is very welcome to make it.
- **Vanilla castration still works as before.** Castrating someone with the base game's interaction does not turn them into a daughter.

> **Content note.** The mod deals with castration, with a penal path that transitions violent prisoners (the "Dorley precedent", after Alyson Greaves's *Welcome to Dorley Hall*), and with the transmisogyny of medieval law and custom. Event text is written without gore, but the subject matter is there.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Playtesters wanted

The mod is in alpha. Most of it has never run in a real campaign, and we need people to play it and tell us what breaks. You don't need any modding experience.

> **Playtesters: start with the [test guide](docs/TO-TEST.md).** It lists specific scenarios to set up, from a five-minute smoke test to long observer runs, with console helpers to skip the waiting, what you should see, and exactly what to send back. Pick any scenario; partial results and "it worked" are both useful.

### Prerequisites

- **Crusader Kings III 1.20.x.** The mod is written against 1.20.1.
- **DLC.** We test with all DLC enabled. Reports from players with fewer DLC are especially useful.
- **A new game.** The faiths are placed in the world at game start, so an existing save will not have them.

### Loading the mod from this folder

1. **Get the files.** Clone the repository, or download it as a ZIP from the green *Code* button and unzip it anywhere.
   ```sh
   git clone https://github.com/PersephoneKarnstein/Transing-CK3.git
   ```
2. **Find your mod folder.**

   | OS | Mod folder |
   |---|---|
   | Windows | `%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\mod` |
   | macOS | `~/Documents/Paradox Interactive/Crusader Kings III/mod` |
   | Linux | `~/.local/share/Paradox Interactive/Crusader Kings III/mod` |

3. **Create a launcher file there.** Copy `descriptor.mod` from the repository into the mod folder and rename it `transing_ck3.mod`. Then add one line at the end giving the full path to the folder you cloned or unzipped. Use forward slashes, even on Windows.
   ```
   path="C:/Users/you/Documents/Transing-CK3"
   ```
4. **Enable it.** Open the Paradox launcher, go to *Playsets*, add **Adelphai Dorleyaiou** to a playset, and make that playset active.
5. **Start a new game.** In the Ruler Designer you can choose the Kybeline culture and any of the four faiths. You can also convert to one in a normal game.

To update later, pull or re-download into the same folder. The launcher file does not need to change.

### What to test and how to report

Good first tests:

- **Ruler Designer.** Do all four faiths and the Kybeline culture appear?
- **The four rites.** As a Marked man, take each faith's decision: *Take the Knife*, *Ask a Völva to Sit for Me*, *Gestate the Jade Embryo* and *Keep the Fourteenth of Adar* (February or March only).
- **Re-embodiment.** After a rite, do your titles, marriage, children, adoptive parents and skills carry over?
- **Adoption.** Try *Take as Daughter* on a courtier, a ward and a guest.
- **Arrivals and Houses.** Found a Sisters' House. Over a long reign, do Marked travellers, cast-out women and friends of the House arrive? Does the House choose an Elder Sister, and split when it is strained? Give the county to a ruler of another faith and see whether they close it.
- **Declare Before Witnesses** and **The Sisters Choose** (an elective succession law): does the declared name survive the rite, and does the election pick sensible heirs?

When something breaks, [open an issue](https://github.com/PersephoneKarnstein/Transing-CK3/issues/new?labels=bug) and include:

- **What you did** and what you expected to happen.
- **Your error log.** It is `error.log` in the `logs` folder next to your mod folder.
- **A save**, if you can attach one.

**[docs/TO-TEST.md](docs/TO-TEST.md) lists specific scenarios to set up, with what to expect and what to send.** The game's console can run test scripts from `tools/run/`. Copy them into the `run` folder next to your mod folder, launch the game with `-debug_mode`, open the console with `~`, and type, for example, `run tm_census.txt`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Dorleyism: the Sisters of Dorylaion

*Adelphai Dorleyaiou.* A Christian heresy in Byzantine Anatolia, centred on the house at Dorylaion. The name is a pun on Dorley Hall.

The Sisters are nostalgic for a sect almost nobody remembers: the Mother's galli of Phrygia, whom they call *gallae*. They say the house at Pessinus never closed, and they remember it kinder than it was; Pessinus in fact belonged to priests titled Attis who passed the office from father to son. In their own voice they claim a line from Pessinus through the prophetesses of Pepouza, the women-led Montanist church of Phrygia, to Dorylaion. What they refuse is what the Byzantine court offers instead. "The court calls its eunuchs angels," they say, "and buys them as boys." The Emperor's law counts three kinds of people: men, women and eunuchs. The Sisters hold that one who takes the knife rises a daughter, not a third thing.

- **The gate: the knife.** *Take the Knife* takes two days, as the Mother's festival did: blood and mourning on the Day of Blood (24 March), then the knife, the knifer's question and a new name at the Hilaria, the festival of joy. Each faith picks one of three houses for who may be cut:
  - **Grandmother's House:** any captive, man or boy, in the old cruel way. She called them eunuchs, not daughters: unmanning them was the point.
  - **Aunt Bea's House:** only grown men proven violent, each under a sponsor who walked the same road, with a washout path for those who will not change. It holds that every woman it makes is a woman, claims no law for it, and admits that it keeps cells.
  - **Gift Alone:** only grown women who ask. "Even the Mother of God was asked." "A gift you cannot refuse is not a gift." The strongest doctrine over a long game.
- **The line.** Daughters choose their heirs rather than breed them. A woman of the House can foster a daughter, who belongs but does not inherit, or take her as a daughter with the written clause that makes her an heir. Each House has a Protectress from the founder's female line, as the convent charters passed protection of a convent "in perpetuity", and its sisters name three for Elder Sister and let the lot decide.
- **The court.** Dukes and above can appoint daughters of the knife and eunuchs to the offices the Byzantine court reserved for its eunuchs: Parakoimomene, Protovestiaria and Papias. Any woman can be Praiposita of the empress's chamber.
- **The world.** The *Rescue the Daughters* war frees captive daughters from a neighbour. A bishop may preach that the Sisters are "Cybele in Christian clothes", and under a lord of another Christian faith the old laws against heretics climb rung by rung, faster after the Komnenian turn of 1081: the books burned, the assemblies banned, and, under a Byzantine lord, the wills voided.
- **Tenets.** Day of Blood, Daughters Chosen Not Born, and Unbending Sisterhood.
- **Head of faith.** The Mother of Mothers, Theia Beatrike, an elder daughter seated at Dorylaion, with up to seven Companions, as the Montanist prophetesses had theirs.
- **Holy sites.** Dorylaion and Constantinople, Kyzikos, Ankyra, and ruined Pepouza.
- **The schism to come.** The main rite is Aristotelian: the cut body changes into the female condition. A planned Galenic splinter is the rite that agrees with the Emperor: the cut are "a third thing, neither". The Aristotelians call that "the old cage with a new name."

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Bædling: the High Seat

*Working name.* A Germanic pagan faith of Scandinavia and Anglo-Saxon England. It takes its name from *bædling*, a word of uncertain meaning that the Old English Canons of Theodore set apart from "other men" in their canons on sex between men; one glossary puts it beside *effeminati*, and the glossaries also keep *bæddel*. It joins that word to *seiðr* and *ergi*.

In the north the sanctioned crossing ran toward manhood. A man who went the other way was called *ragr*, yet Icelandic law outlawed not him but whoever said the word, and the man so named could kill the speaker. The Bædlings keep the other road. In the north castration punished thieves and unmade enemies; it was never a rite, so this faith does not use the knife.

- **The gate: seiðr.** *Ask a Völva to Sit for Me* is a three-day rite, like a wedding, built on the seeress in *Eiríks saga rauða*:
  - **The völva comes.** She is given the high seat and a feast.
  - **The warding songs.** Someone must sing the *varðlokkur*, which girls learn from their foster-mothers. A woman of the faith can teach them to a daughter or ward.
  - **The platform.** The völva goes up into trance while the seeker waits below.
  - **The odds.** The faith holds that the völva sees a daughter rather than makes one, and the odds turn on whether the song holds, not on the seeker's merit; it may fail until next winter. The rite follows the seeress in *Eiríks saga rauða*, which scholars think was largely invented to honour her host; the warding songs are the part most likely to be old. Völur also travel the halls in winter and can be asked to sit for anyone at court.
- **The declaration.** A new daughter declares herself before the thing, perhaps with a name fastened by a gift or the woman's form of her own. When someone shouts *ragr*, she can answer in verse, with steel, by owning seiðr as women's art, with "*ragr* is said of men", or not at all.
- **The line.** The hall's daughters are fostered, sworn and adopted. Two may bind themselves as sisters by the old oath.
- **The world.** A martial faith. The skalds fill Valhöll with dead men; the Bædlings say the Allfather's true host has none, and point to the shield-maidens at Brávellir. English courts call valkyries witches. The hall raids to bring its daughters home, and its clergy fight. The faith's devil is Níðhöggr, the malice-striker: its enemy is *níð* itself, the slander shouted at the thing.
- **Tenets.** Seiðr Unmans, Óðinn's Host, and Daughters of the Hall.
- **Holy sites.** Uppsala, Trondheim, York and Kyiv. Kyiv sits on the Varangian road south toward Dorylaion.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## The Way of the Jade Embryo

*Working name.* A Daoist faith of Tang China, seated at Dunhuang beneath the Mogao caves, where Daoist priestesses were ordained in the eighth century. In 867 the town's Daoist abbeys stand dark after Tibetan rule; relighting the Shenquan Abbey is the faith's first project.

Daoist inner alchemy teaches that an adept nurtures a holy embryo for ten months until it is born from her and becomes her true self. In the faith's own telling, Lord Lao once took the shape of Mother Li and sheltered in his own womb, and the masters say a man must reach a state of pregnancy before he becomes pure yang. The Way stops there, at the mother: its adepts are born as themselves. The palace counts the cut among its men and would count these women among them too. The Way answers with Confucius's rectification of names. A daughter named before witnesses is a daughter, and any eunuch who seeks the same is received as a sister. Its high god is the Queen Mother of the West, under whom the Tang master Du Guangting ranked every woman who attains the Way.

- **The gate: the jade embryo.** In *Gestate the Jade Embryo*, a guarantor vouches for the house that will shelter the adept, and a nüguan (a Daoist priestess) asks her "Will you ever repent?" Ten months follow:
  - **The first bathing** (month 3): a censor checking the clergy roll threatens to strike her off as a private nun.
  - **The White Tiger** (month 6): her family writes to summon her home. She can refuse ("Not yet! Don't rush me!") or go home to nurse her parents first.
  - **Birth from the crown** (month 10), and a name before witnesses.
  A physician may call it a "ghost fetus" and bring a purge. Nothing she has done is ever lost.
- **The line.** Under Song law a daughter, born or adopted, keeps a sonless house; the magistrate takes only what a house with no daughter leaves. The faith's temple and burial societies pay dues at every birth and death, keep a righteous store that lends at interest, and petition the throne for a name-panel that protects their Houses from confiscation. Waves of confiscation grow after the Yuan conquest.
- **The world.** A courtly faith of intrigue and stewardship. Prodigies are reported in the prefectures, and a king of the Way can ordain a woman by special edict, as the Song court once ordained a bearded woman. Buddhist neighbours read a daughter as a man reborn a woman for an old sin. A planned palace faction will contend with the scholar-officials.
- **Tenets.** The Jade Embryo, Rectified Names, and Temple Societies.
- **Holy sites.** The Mogao caves, Mount Longhu, Mount Qingcheng and the Southern Marchmount (Mount Heng in Hunan), the holy women's mountain.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Ha-Nehpakhot: the women who were turned

*Working name.* A small current inside Judaism, kept by the women of the lamp: women householders of the Jewish street of Arles who sit together in the women's synagogue, below the men's, and keep the alms of the synagogue lamp. (No medieval women-only confraternity is attested; Arles had a lamp alms, and in 1401 its council called five women to sit, "because what concerns all must be approved by all".) It holds no land at the start: it lives under other lords, as the Jews of Arles lived under their archbishop.

The rabbis divide the eunuch made "by the hands of heaven" from the one made "by human hands", and the made eunuch stays, in law, a man. No rabbinic text lets anyone pass from male to female, and a Jewish court would read a daughter of the knife as a man made a eunuch. The Talmud does tell how Leah prayed and the child in her womb was turned into a daughter, Dinah, though it adds that one does not cite miracles. In the winter of 1322–23 Kalonymus ben Kalonymus, who was born at Arles and worked there, wrote the satire *Even Boḥan* (*The Touchstone*) in Catalonia. In it he asks God, perhaps in jest, "would that You turn me from male to female", and he describes young Jewish men putting on women's dress for Purim. The Nehpakhot take all of this at its word, in their own voice. They say only the hands of heaven turn, so the faith uses no knife.

- **The gate: the Turning.** *Keep the Fourteenth of Adar* can only be taken in Adar (February or March). It is a five-part rite:
  - **The scroll.** An elder reads Esther in the women's synagogue, and beside "it was turned about" she reads the other turnings: Abraham from the furnace, the staff, the sea, and Dinah.
  - **The revel.** From 1323 the young men put on the woman's dress for the joke, and the rabbis grumble and let it pass (permission comes only in the 16th century). She keeps it on when the joke is over. Before 1323 the custom is unattested, so she is the only one in the dress.
  - **The prayer.** The men thank God each morning that He did not make them women. She asks aloud for the reverse.
  - **The name**, on Shushan Purim. The women teach her their blessing, "who made me a woman" (in Provence, in their own tongue: *qui fis me fenna*). It is written down only after 1453, in Provençal women's prayer books; that it is older is the faith's claim. She takes a name from the scroll (Dinah, Esther, Sara) or a name of the street, as the Jewish women of Provence were called in the notaries' books (Rosa, Mairona, Bella, Regina, Blanca, Gratiosa, Bonadonna and others).
  - **Before the baylons.** The dress has outlived Purim, and the baylons and council of the street must judge; from 1401 the council at Arles includes women, and that helps her. She can answer with Dinah, text against text, and win her county a licence; lose and be shunned (*niddui*); cite the *Touchstone*; claim the house as its lady and accept the shunning; or put the dress away. A community could shun only by its Christian lord's licence, so a lord who has taken her people under his protection refuses it, and the sentence falls.
  - **The odds.** The Turning rests on learning, the elder's and her own, and on patience. Every Adar's unanswered prayer makes the next more likely, as Leah's was answered in its time. A seeker of another Jewish faith who is turned joins the sect.
- **The line.** Womanhood is what she keeps: the three women's commandments Kalonymus wished for (the days of separation, the portion of the dough, the Sabbath lamp). One whose days do not come keeps them as the *zekenah*, the old woman past them, keeps them. An elder can teach the prayer to one who will need it, and the women spin together by moonlight.
- **The world.** A learned, landless faith. A lord of any faith with a daughter of the Turning at court may commission a translation from Arabic, as Robert of Naples employed Kalonymus, and take her people under protection; or licence her as a *fisica*, a physician, as Provençal women physicians were licensed. Jewish lords are asked to rule whether what came forth male is male. Jewish characters think less of daughters of every faith; the Nehpakhot think more.
- **Tenets.** The Turning, The Three Lamps, and Legalism.
- **Holy sites.** Arles, Jerusalem (whose county holds Hebron and Leah's tomb), Narbonne, Montpellier, and Hamadan, the tomb of Esther and Mordecai.
- **What it leaves out.** The old charge that medieval Jews ran the slave and eunuch trade is a historiographic motif, not a finding (Phelan 2023), so no Jewish character in the mod trades in slaves or eunuchs. The faith is not seated in Khazaria, and the narrator never says the Talmud recognised "six genders": those are legal categories for bodies, mostly intersex ones, and only a character may claim them. Nor does it use any of the medieval Christian tropes about Jewish bodies (the "male menses", the bloody flux) or the accusations about Purim.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Shared mechanics

- **Marked by the Mother.** A rare trait for men who are trans women before any rite. You can filter for it in the Character Finder to find people to recruit and adopt.
- **Re-embodiment.** After a rite, the daughter continues in a female body with the same face. Her titles, marriage, children, parents, adoptive parents, skills and lifestyle experience carry over. Re-embodied daughters are infertile. A game rule turns this off.
- **Take as Daughter.** Each faith's own adoption. Unlike vanilla adoption it accepts adults, and it ignores the rules that block children with landed relatives.
- **Declare Before Witnesses.** A Marked sister can take a daughter's name before any rite. The rite changes her body, not her name, and a failed or delayed rite never takes the name back.
- **Sisters' Houses.** A ruler can found a House in her capital county. It belongs to the county, not her family: a later ruler of another faith may let it stand or close it, and closing sends the sisters on to another House rather than deleting them. Each House chooses its own Elder Sister every five years, frays under strain (too few hands, war levies), and splits to found a daughter House next door. Houses draw arrivals and can send newcomers to your court. Cis women of the faith are sisters too, and men of the faith can stay as friends of the House.
- **The Sisters Choose.** An elective succession law: the ruler, the faith's clergy and its vassals choose an heir from among the ruler's born and adopted children, the women of the faith on the council, and the faithful vassals.
- **Jewish and Indic neighbours.** Jewish courts think less of a daughter of any faith ("what came forth male is male"), and a Jewish lord may be asked to rule on one at court; the Nehpakhot cancel it. Buddhist, Hindu and Jain courts read a daughter of the knife as a castrated man and think much less of her, and a daughter of the other gates as a man become a woman, which they mind less.
- **Islamic neighbours.** Islamic courts value a daughter as a trusted servant and think less of her as a ruler: their jesters may mock a daughter who rules, while an Islamic lord may come to trust one in his household.
- **The call.** Each year a Marked character of another faith may join the nearest of the four: Byzantium and Anatolia to Dorleyism, the North and the Baltic to the Bædlings, China and the Tarim to the Jade Embryo, and the Jewish faiths to Ha-Nehpakhot. A Sisters' House nearby, or a daughter at court, makes it likelier. Courtiers who are Marked, eunuchs or declared sisters may begin their faith's rite on their own, and a ruler with no heir of her faith looks for a daughter to take.
- **Arrivals.** Each year a Marked traveller, a woman turned out for bearing no children, or (where there is a House) a friend of the House may come to the court of a ruler of these faiths. Turning someone away sends them on to the next House.
- **Same-sex marriage.** All four faiths allow it, whatever the game rule says.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Dorleyism: faith, culture, the three houses of the knife, the Dorley prisoner path
- [x] Sisters' Houses, Declare Before Witnesses, The Sisters Choose
- [x] Bædling and the Way of the Jade Embryo: faiths, tenets and gates
- [x] Re-embodiment, Take as Daughter, arrivals
- [ ] Bædling: insult duels, feud and settlement, outlawry and landless war-bands, Spring the Cell
- [ ] Jade Embryo: the palace faction, temple societies against confiscation, omen events
- [ ] Dorleyism: the Galenic splinter rite; events from the reading (Liudprand's boys, Ignatios, the Tarsus boy-train, the Emperor at Dorylaion)
- [ ] Flavour achievement events, the Pope first
- [ ] Commissioned art for faith icons, traits and events

See the [open issues](https://github.com/PersephoneKarnstein/Transing-CK3/issues) for everything else.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Playtest reports are the most useful contribution right now. Pull requests are welcome too:

1. Fork the project.
2. Create a branch (`git checkout -b feature/your-idea`).
3. Commit your changes. Keep script `.txt` and localisation `.yml` files in UTF-8 **with** a byte-order mark.
4. Push the branch and open a pull request.

Design notes live in [`docs/`](docs). Start with [`docs/faith_design.md`](docs/faith_design.md) and [`docs/beliefs.md`](docs/beliefs.md). [CK3 Tiger](https://github.com/amtep/tiger) validates the scripts, though it still reports some false positives against the 1.20 religion files.

Art is wanted. The faith and trait icons are placeholders, and we would like to commission proper ones.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Released into the public domain under [the Unlicense](LICENSE). Do whatever you want with it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template), which this README is based on
- [CK3 Tiger](https://github.com/amtep/tiger), for script validation
- [Paradox Modding Toolkit](https://github.com/JDeffner/paradox-modding-toolkit), for editing and validation tools
- The trans writers on Bluesky and Tumblr whose public discussion of baedelism, third-wave transfeminism and transgender Marxism shaped the tenets. Their posts are not reproduced here.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Bibliography

Works the research for this mod read, in full or in named chapters. Works it only points to appear at the end of each group as "Cited in the notes, not read". Details come from the copies we read, with gaps filled from publisher and library records. Corrections are welcome.

Click a heading to expand it.

<details>
<summary><strong>Transfeminist theory and trans studies</strong> (10 works)</summary>

- Bettcher, Talia Mae. 2013. "Evil Deceivers and Make-Believers: On Transphobic Violence and the Politics of Illusion." In Stryker and Aizura (eds.), *The Transgender Studies Reader 2*.
- Bhatt, Talia. 2025. *Trans/Rad/Fem: Essays on Transfeminism, Book 1*. Self-published.
- Chu, Andrea Long. 2019. *Females*. Verso.
- Gleeson, Jules Joanne, and Elle O'Rourke (eds.). 2021. *Transgender Marxism*. Pluto Press. (Read in full: introduction, 14 chapters and Jordy Rosenberg's afterword.)
- Raha, Nat, and Mijke van der Drift. 2024. *Trans Femme Futures: Abolitionist Ethics for Transfeminist Worlds*. Pluto Press.
- Serano, Julia. 2016 [2007]. *Whipping Girl: A Transsexual Woman on Sexism and the Scapegoating of Femininity*. 2nd ed. Seal Press.
- Stryker, Susan. 2026. *Transgender History: A Resource for Today's Struggle—and Tomorrow's*. 3rd ed. Seal Press.
- Stryker, Susan, and Aren Z. Aizura (eds.). 2013. *The Transgender Studies Reader 2*. Routledge.
- Stryker, Susan, and Dylan McCarthy Blackston (eds.). 2022. *The Transgender Studies Reader Remix*. Routledge.
- Stryker, Susan, and Stephen Whittle (eds.). 2006. *The Transgender Studies Reader*. Routledge.

Cited in the notes, not read: Bhatt, Talia, *Brown/Trans/Les* (2026); Feinberg, Leslie, *Transgender Warriors* (in the Remix bibliography); Koyama, Emi, *The Transfeminist Manifesto* (2001); Lewis, Sophie, *Abolish the Family* (Verso 2022); O'Brien, M. E., *Family Abolition* (Pluto 2023).

</details>

<details>
<summary><strong>Byzantium, Cybele and the eunuch traditions</strong> (30 works)</summary>

- Betancourt, Roland. 2020. *Byzantine Intersectionality: Sexuality, Gender, and Race in the Middle Ages*. Princeton University Press.
- Burns, Krishni. 2025. *Bringing Their Mother Home: Roman Multiculturalism and the Mother of the Gods*. University of Michigan Press. (Open access.)
- Bury, J. B. 1911. *The Imperial Administrative System in the Ninth Century, with a Revised Text of the Kletorologion of Philotheos*. British Academy.
- Davis, Stephen J. 2002. "Crossed Texts, Crossed Sex: Intertextuality and Gender in Early Christian Legends of Holy Women Disguised as Men." *Journal of Early Christian Studies* 10.1: 1–36.
- Garland, Lynda. 1999. *Byzantine Empresses: Women and Power in Byzantium, AD 527–1204*. Routledge.
- Guilland, Rodolphe. 1943. "Les eunuques dans l'Empire byzantin." *Études byzantines* 1: 197–238.
- King, Helen. 2013. *The One-Sex Body on Trial: The Classical and Early Modern Evidence*. Ashgate.
- Latham, Jacob. 2012. "'Fabulous Clap-Trap': Roman Masculinity, the Cult of Magna Mater, and Literary Constructions of the *galli* at Rome." *Journal of Religion* 92.1: 84–122.
- Macrides, R. J. 1990. "Kinship by Arrangement: The Case of Adoption." *Dumbarton Oaks Papers* 44: 109–118.
- Neil, Bronwen, and Lynda Garland (eds.). 2013. *Questions of Gender in Byzantine Society*. Ashgate. (Routledge reprint 2016.)
- Neville, Leonora. 2019. *Byzantine Gender*. Past Imperfect. Arc Humanities Press.
- Rapp, Claudia. 2016. *Brother-Making in Late Antiquity and Byzantium: Monks, Laymen, and Christian Ritual*. Oxford University Press.
- Ringrose, Kathryn M. 2003. *The Perfect Servant: Eunuchs and the Social Construction of Gender in Byzantium*. University of Chicago Press.
- Roller, Lynn E. 1997. "The Ideology of the Eunuch Priest." *Gender & History* 9.3: 542–559.
- Roller, Lynn E. 1999. *In Search of God the Mother: The Cult of Anatolian Cybele*. University of California Press.
- Sidéris, Georges. 2010. "Les eunuques de Byzance (IVe–XIIe siècle) : de la société de cour à la société urbaine." In Élisabeth Malamut (ed.), *Dynamiques sociales au Moyen Âge*, 89–116. Presses universitaires de Provence.
- Sidéris, Georges. 2013. "Sur l'origine des anges eunuques à Byzance." In Constantin Zuckerman (ed.), *Constructing the Seventh Century*, Travaux et Mémoires 17: 539–558.
- Spencer-Hall, Alicia, and Blake Gutt (eds.). 2021. *Trans and Genderqueer Subjects in Medieval Hagiography*. Amsterdam University Press. (Open access.)
- Tougher, Shaun. 2008. *The Eunuch in Byzantine History and Society*. Routledge. (Read in the 2009 Taylor & Francis e-library edition.)
- Tougher, Shaun. 2013. "Bearding Byzantium: Masculinity, Eunuchs and the Byzantine Life Course." In Neil and Garland (eds.), *Questions of Gender in Byzantine Society*, 153–166.
- Tougher, Shaun (ed.). 2002. *Eunuchs in Antiquity and Beyond*. Classical Press of Wales and Duckworth.
- Trevett, Christine. 1996. *Montanism: Gender, Authority and the New Prophecy*. Cambridge University Press.
- *Primary sources in translation:*
  - Aristotle. *Generation of Animals*. Trans. Arthur Platt. In *The Works of Aristotle*, vol. V. Oxford, 1912.
  - Constantine Porphyrogennetos. *The Book of Ceremonies*. Trans. Ann Moffatt and Maxeme Tall. Byzantina Australiensia 18. 2012.
  - Galen. *On Semen* (*De semine*). Greek text (Kühn IV); the notes' renderings are our own and should be checked against De Lacy's translation (CMG V 3,1, 1992).
  - Gautier, Paul (ed. and trans.). 1985. "Le typikon de la Théotokos Kécharitôménè." *Revue des études byzantines* 43: 5–165.
  - Liudprand of Cremona. *The Complete Works*. Trans. Paolo Squatriti. Catholic University of America Press, 2007.
  - Paul of Aegina. *The Seven Books*, vol. II. Trans. Francis Adams. Sydenham Society, 1846.
  - Talbot, Alice-Mary (ed.). 1996. *Holy Women of Byzantium: Ten Saints' Lives in English Translation*. Dumbarton Oaks. (Open access.)
  - Thomas, John, and Angela Constantinides Hero (eds.). 2000. *Byzantine Monastic Foundation Documents*. 5 vols. Dumbarton Oaks. (Open access.)

Cited in the notes, not read: Kuefler, *The Manly Eunuch* (2001); Messis, *Les eunuques à Byzance* (2014); Mullett on Theophylact of Ochrid's *In Defence of Eunuchs* (read only through Tougher 2002). Further titles, with availability, are in `docs/research/byzantium_reading_list.md`.

</details>

<details>
<summary><strong>Islamic comparanda</strong> (10 works)</summary>

- Ayalon, David. 1999. *Eunuchs, Caliphs and Sultans: A Study in Power Relationships*. Jerusalem: Magnes Press.
- Davis, Natalie Zemon. 2006. *Trickster Travels: A Sixteenth-Century Muslim between Worlds*. Hill and Wang.
- de la Puente, Cristina. 2023. "Al-Ḥakam I in the Andalusi Sources: His Slaves, Eunuchs, and Concubines." *Slavery & Abolition* 44.4: 593–615.
- El-Azhari, Taef. 2019. *Queens, Eunuchs and Concubines in Islamic History, 661–1257*. Edinburgh University Press.
- Marmon, Shaun. 1995. *Eunuchs and Sacred Boundaries in Islamic Society*. Oxford University Press.
- Rowson, Everett K. 1991. "The Categorization of Gender and Sexual Irregularity in Medieval Arabic Vice Lists." In Julia Epstein and Kristina Straub (eds.), *Body Guards: The Cultural Politics of Gender Ambiguity*, 50–79. Routledge.
- Rowson, Everett K. 1991. "The Effeminates of Early Medina." *Journal of the American Oriental Society* 111.4: 671–693.
- Rowson, Everett K. 2003. "Gender Irregularity as Entertainment: Institutionalized Transvestism at the Caliphal Court in Medieval Baghdad." In Sharon Farmer and Carol Braun Pasternack (eds.), *Gender and Difference in the Middle Ages*, 45–72. University of Minnesota Press.
- Rowson, Everett K. 2008. "Homoerotic Liaisons among the Mamluk Elite in Late Medieval Egypt and Syria." In Babayan and Najmabadi (eds.), *Islamicate Sexualities: Translations across Temporal Geographies of Desire*, 204–238. Harvard University Press.
- Sanders, Paula. 1991. "Gendering the Ungendered Body: Hermaphrodites in Medieval Islamic Law." In Nikki R. Keddie and Beth Baron (eds.), *Women in Middle Eastern History: Shifting Boundaries in Sex and Gender*, 74–95. Yale University Press.

Cited in the notes, not read: Ayalon, David, "On the Eunuchs in Islam," *Jerusalem Studies in Arabic and Islam* 1 (1979): 67–124; El-Rouayheb, *Before Homosexuality*; Babayan and Najmabadi (eds.), *Islamicate Sexualities*.

</details>

<details>
<summary><strong>Northern Europe</strong> (28 works)</summary>

- Acker, Paul, and Carolyne Larrington (eds.). 2002. *The Poetic Edda: Essays on Old Norse Mythology*. Routledge Medieval Casebooks. Routledge.
- Ahola, Joonas. 2014. *Outlawry in the Icelandic Family Sagas*. PhD dissertation, University of Helsinki.
- Berry, Miles. 2022. "Gender Diversity and its Societal Place in Medieval Scandinavia." *Oregon Undergraduate Research Journal* 20.2: 134–154. (An undergraduate paper. The notes flag factual slips.)
- Birch, Eleanor. 2025. "Deviance or Devotion: Women Dressed as Men in Late Medieval England." *Fashion Theory* 29.5: 619–639.
- Blain, Jenny. 2002. *Nine Worlds of Seid-Magic: Ecstasy and Neo-Shamanism in North European Paganism*. Routledge. (Much of it concerns modern practice; the notes separate that from the medieval evidence.)
- Clover, Carol J. 1980. "The Germanic Context of the Unferþ Episode." *Speculum* 55.3: 444–468.
- Clover, Carol J. 1993. "Regardless of Sex: Men, Women, and Power in Early Northern Europe." *Speculum* 68.2: 363–387.
- Damico, Helen. 1984. *Beowulf's Wealhtheow and the Valkyrie Tradition*. University of Wisconsin Press.
- Evans, Gareth Lloyd, and Jessica Clare Hancock (eds.). 2020. *Masculinities in Old Norse Literature*. D. S. Brewer.
- Gade, Kari Ellen. 1986. "Homosexuality and Rape of Males in Old Norse Law and Literature." *Scandinavian Studies* 58.2: 124–141.
- Gardeła, Leszek, Sophie Bønding and Peter Pentz (eds.). 2023. *The Norse Sorceress: Mind and Materiality in the Viking World*. Oxbow Books. (Open access.)
- Jakobsson, Ármann. 2011. "Óðinn as mother: the old norse deviant patriarch." *Arkiv för nordisk filologi* 126. (Read in proof, paginated 01–012.)
- Jochens, Jenny. 1995. *Women in Old Norse Society*. Cornell University Press.
- Jochens, Jenny. 1996. *Old Norse Images of Women*. University of Pennsylvania Press.
- Karras, Ruth Mazo, and Katherine E. Pierpont. 2023. *Sexuality in Medieval Europe: Doing Unto Others*. 4th ed. Routledge.
- Meulengracht Sørensen, Preben. 1983. *The Unmanly Man: Concepts of Sexual Defamation in Early Northern Society*. Trans. Joan Turville-Petre. The Viking Collection 1. Odense University Press.
- Miller, William Ian. 1990. *Bloodtaking and Peacemaking: Feud, Law, and Society in Saga Iceland*. University of Chicago Press.
- Mitchell, Stephen A. 2011. *Witchcraft and Magic in the Nordic Middle Ages*. University of Pennsylvania Press.
- Price, Neil. 2019. *The Viking Way: Magic and Mind in Late Iron Age Scandinavia*. 2nd ed. Oxbow Books.
- Sayers, William. 2020. "The Etymologies of Old English *Bædling* 'Sodomite' and Modern English *Bad*." *ANQ* 33.1: 9–11.
- Solli, Brit. 2008. "Queering the Cosmology of the Vikings: A Queer Analysis of the Cult of Odin and 'Holy White Stones'." *Journal of Homosexuality* 54.1–2: 192–208.
- Tolley, Clive. 2009. *Shamanism in Norse Myth and Magic*, vol. 1. FF Communications 296. Academia Scientiarum Fennica.
- Tommony, Isabelle, with C. M. Forster. 2024. "Margins Undefined: the flexibility of gender boundaries in the European Middle Ages." *BILT Student Research Journal* 5: 2–9. (A peer-reviewed undergraduate journal from Bristol. Forster is credited on the version-of-record citation.)
- Wade, Erik. 2020. "The Beast with Two Backs: Bestiality, Sex Between Men, and Byzantine Theology in the *Paenitentiale Theodori*." *Journal of Medieval Worlds* 2.1–2: 11–26.
- *Primary sources in translation:*
  - Dennis, Andrew, Peter Foote and Richard Perkins (trans.). 1980–2000. *Laws of Early Iceland: Grágás I–II*. University of Manitoba Press.
  - Fulk, R. D., and Stefan Jurasinski (eds.). 2012. *The Old English Canons of Theodore*. Early English Text Society S.S. 25. Oxford University Press.
  - Kunz, Keneva (trans.). 2008. *The Vinland Sagas*. Introduction by Gísli Sigurðsson. Penguin Classics.
  - Saxo Grammaticus. *The Danish History, Books I–IX*. Trans. Oliver Elton (1894). Read in a public-domain electronic edition.

</details>

<details>
<summary><strong>Medieval Judaism</strong> (32 works)</summary>

For Ha-Nehpakhot, and for how Jewish courts answer every faith's daughters. The open-access English of Kalonymus's prayer (Open Siddur, CC BY-SA) was a reading aid only; every line in the mod is rendered afresh from the public-domain Hebrew.

- Assis, Yom Tov. 2000–2001. "El comportament sexual en la societat hispanojueva de l'edat mitjana." *Tamid* 3: 7–47.
- Baricci, Erica. 2014. "'Bendig tu…qui fis me fenna': donne, libri e letteratura nel Medioevo giudeo-provenzale." *Altre Modernità* 05/2014: 221–242.
- Baricci, Erica. 2023. "Canti e preghiere dal siddur giudeo-provenzale (Ms. Leeds, Brotherton Library, Roth 32)." *Specula* 6: 63–95.
- Baumgarten, Elisheva. 2016. "Prier à part ? Le genre dans les synagogues ashkénazes médiévales (XIIIe–XIVe siècle)." *Clio. Femmes, Genre, Histoire* 44: 43–62.
- Ben-Shalom, Ram. 2024. *The Jews of Provence and Languedoc: Renaissance in the Shadow of the Church*. Trans. Shmuel Sermoneta-Gertel. Littman Library of Jewish Civilization.
- Chotzner, J. 1900. "Kalonymos ben Kalonymos, a Hebrew Satirist of the Thirteenth Century." *Jewish Quarterly Review* 13.1: 128–146.
- Davidson, Israel. 1907. *Parody in Jewish Literature*. Columbia University Press.
- Fonrobert, Charlotte Elisheva. 2006. "The Semiotics of the Sexed Body in Early Halakhic Discourse." In Matthew Kraus (ed.), *How Should Rabbinic Literature Be Read in the Modern World?*, 79–104. Gorgias.
- Fonrobert, Charlotte Elisheva. 2007. "Regulating the Human Body: Rabbinic Legal Discourse and the Making of Jewish Gender." In *The Cambridge Companion to the Talmud and Rabbinic Literature*, 270–294. Cambridge University Press.
- Grabowski, Antoni. 2015. "Eunuch between Economy and Philology: The Case of *carzimasium*." *Mélanges de l'École française de Rome – Moyen Âge* 127.1.
- Gross, Heinrich. 1897. *Gallia Judaica: dictionnaire géographique de la France d'après les sources rabbiniques*. Léopold Cerf.
- Grossman, Avraham. 2004. *Pious and Rebellious: Jewish Women in Medieval Europe*. Trans. Jonathan Chipman. Brandeis University Press.
- Guerson, Alexandra, and Dana Wessell Lightfoot. 2019. "Crises and Community: Catalan Jewish Women and Conversas in Girona, 1391–1420." *Tamid* 14: 91–130.
- Hildenfinger, Paul. 1900–1904. "Documents relatifs aux Juifs d'Arles." *Revue des études juives* 41: 62–97; 47: 221–242; 48: 48–81, 265–272.
- Horowitz, Elliott. 2006. *Reckless Rites: Purim and the Legacy of Jewish Violence*. Princeton University Press.
- Kahn, Yoel H. 2011. *The Three Blessings: Boundaries, Censorship, and Identity in Jewish Liturgy*. Oxford University Press.
- Kalonymus ben Kalonymus. c. 1322. *Even Boḥan*. Lemberg, 1865.
- Lev, Sarra. 2024. *And the Sages Did Not Know: Early Rabbinic Approaches to Intersex*. University of Pennsylvania Press.
- Marienberg, Evyatar. 2004. "Menstruation in Sacred Spaces: Medieval and Early-Modern Jewish Women in the Synagogue." *Nordisk Judaistik* 25.1: 7–16.
- Neis, Rafael Rachel. 2023. *When a Human Gives Birth to a Raven: Rabbis and the Reproduction of Species*. University of California Press (Luminos).
- Phelan, Joseph. 2023. "The Jewish 'Monopoly' of the Slave Trade in the Early Middle Ages: The Origins of an Enduring Historical Motif." *Patterns of Prejudice* 57.3: 161–174.
- Renan, Ernest, and Adolf Neubauer. 1893. *Les écrivains juifs français du XIVe siècle*. Imprimerie nationale.
- Resnick, Irven M. 2000. "Medieval Roots of the Myth of Jewish Male Menses." *Harvard Theological Review* 93.3: 241–263.
- Roguin Maor, Noga, Ariel Roguin, and Nathan Roguin. 2021. "Medieval Roots of the Myth of Jewish Male Menstruation." *Rambam Maimonides Medical Journal* 12.4: e0033.
- Roos, Lena. 2017. "Cross-dressing among Medieval Ashkenazi Jews: Confirming Challenged Group Borders." *Nordisk Judaistik* 28.2: 4–22.
- Rosen, Tova. 2000. "Circumcised Cinderella: The Fantasies of a Fourteenth-Century Jewish Author." *Prooftexts* 20.1: 87–110.
- Rosen, Tova. 2003. *Unveiling Eve: Reading Gender in Medieval Hebrew Literature*. University of Pennsylvania Press.
- Shatzmiller, Joseph. 1994. *Jews, Medicine, and Medieval Society*. University of California Press.
- Shatzmiller, Joseph. 2023. *Collected Studies, Volume 1: The Jews of Provence*. Academic Studies Press.
- Stouff, Louis. 2014. *Arles au Moyen Âge finissant*. Presses universitaires de Provence.
- Strassfeld, Max K. 2013. "Classically Queer: Eunuchs and Androgynes in Rabbinic Literature." PhD dissertation, Stanford University.
- Strassfeld, Max K. 2022. *Trans Talmud: Androgynes and Eunuchs in Rabbinic Literature*. University of California Press.

Read but not used: Howard, *Hebrew Gospel of Matthew* (1995), which is Shem Tov ibn Shaprut's *Even Boḥan* (1380s), a different work from Kalonymus's.

Primary texts read through Sefaria: Mishnah and Tosefta Bikkurim; Babylonian Talmud, Berakhot 60a, Yevamot 64a–b (with Rashi) and Yevamot 80b; *Bereshit Rabbah* 60:16; *Sefer ha-Ḥinukh* 291, 542–543; Rashi on Deuteronomy 22:5; Maimonides, *Mishneh Torah* (Avodah Zarah 12, Ishut 4, Issurei Bi'ah 16); *Shulḥan Arukh*, Oraḥ Ḥayyim 696:8 with Isserles.

</details>

<details>
<summary><strong>Medieval trans studies</strong> (14 works)</summary>

The 2019 *Medieval Feminist Forum* special issue on medieval trans feminism, edited by M. W. Bychowski and Dorothy Kim, and three later surveys and re-readings.

- Boyd, David Lorenzo, and Ruth Mazo Karras. 1995. "The Interrogation of a Male Transvestite Prostitute in Fourteenth-Century London." *GLQ* 1.4: 459–465.
- Bychowski, M. W. 2019. "The Necropolitics of Narcissus: Confessions of Transgender Suicide in the Middle Ages." *Medieval Feminist Forum* 55.1: 207–248.
- DeVun, Leah. 2021. *The Shape of Sex: Nonbinary Gender from Genesis to the Renaissance*. Columbia University Press.
- Ellison, Joy, and Nicholas Hoffman. 2019. "The Afterward: Sylvia Rivera and Marsha P. Johnson in the Medieval Imaginary." *Medieval Feminist Forum* 55.1: 267–294.
- Gutt, Blake. 2019. "Medieval Trans Lives in Anamorphosis: Looking Back and Seeing Differently (Pregnant Men and Backward Birth)." *Medieval Feminist Forum* 55.1: 174–206.
- Henningsen, Kadin. 2019. "'Calling [herself] Eleanor': Gender Labor and Becoming a Woman in the Rykener Case." *Medieval Feminist Forum* 55.1: 249–266.
- Karras, Ruth Mazo, and Tom Linkinen. 2016. "John/Eleanor Rykener Revisited." In Doggett and O'Sullivan (eds.), *Founding Feminisms in Medieval Studies: Essays in Honor of E. Jane Burns*, 111–121. D. S. Brewer.
- Kim, Dorothy, and M. W. Bychowski. 2019. "Visions of Medieval Trans Feminism: An Introduction." *Medieval Feminist Forum* 55.1: 6–41.
- Lumbley, Coral. 2019. "Imperatrix, Domina, Rex: Conceptualizing the Female King in Twelfth-Century England." *Medieval Feminist Forum* 55.1: 64–99.
- McGucken, Stephenie. 2019. "Vice & Virtue As Woman?: The Iconography of Gender Identity in the Late Anglo-Saxon Psychomachia Illustrations." *Medieval Feminist Forum* 55.1: 42–63.
- Nestel, Meghan. 2019. "A Space of Her Own: Genderfluidity and Negotiation in *The Life of Christina of Markyate*." *Medieval Feminist Forum* 55.1: 100–134.
- Watt, Caitlin G. 2019. "'Car vallés sui et nient mescine': Trans Heroism and Literary Masculinity in *Le Roman de Silence*." *Medieval Feminist Forum* 55.1: 135–173.
- van der Lugt, Maaike. 2010. "Sex Difference in Medieval Theology and Canon Law: A Tribute to Joan Cadden." *Medieval Feminist Forum* 46.1: 101–121.
- Wingard, Tess. 2023. "The Trans Middle Ages: Incorporating Transgender and Intersex Studies into the History of Medieval Sexuality." *English Historical Review* 138.593: 933–951.

</details>

<details>
<summary><strong>China</strong> (53 works)</summary>

- Balkwill, Stephanie. 2016. "The *Sūtra on Transforming the Female Form*: Unpacking an Early Medieval Chinese Buddhist Text." *Journal of Chinese Religions* 44.2: 127–148.
- Bernhardt, Kathryn. 1999. *Women and Property in China, 960–1949*. Stanford University Press.
- Birge, Bettine. 2002. *Women, Property, and Confucian Reaction in Sung and Yüan China (960–1368)*. Cambridge University Press.
- Burton-Rose, Daniel. 2012. "Gendered Androgyny: Transcendent Ideals and Profane Realities in Buddhism, Classicism, and Daoism." In Chiang (ed.), *Transgender China*, 67–95.
- Cheng, Hsiao-wen. 2012. *Traveling Stories and Untold Desires: Female Sexuality in Song China, 10th–13th Centuries*. PhD dissertation, University of Washington.
- Cheng, Hsiao-wen. 2021. *Divine, Demonic, and Disordered: Women without Men in Song Dynasty China*. University of Washington Press.
- Chen Jinhua. 2002. "Śarīra and Scepter: Empress Wu's Political Use of Buddhist Relics." *Journal of the International Association of Buddhist Studies* 25.1–2: 33–150.
- Chiang, Howard. 2012. "How China Became a 'Castrated Civilization' and Eunuchs a 'Third Sex'." In Chiang (ed.), *Transgender China*, 23–66.
- Chiang, Howard (ed.). 2012. *Transgender China*. Palgrave Macmillan. (Chapters 1–5 read in full. Chapters 6–11 are modern and were only skimmed.)
- Dale, Melissa S. 2018. *Inside the World of the Eunuch: A Social History of the Emperor's Servants in Qing China*. Hong Kong University Press.
- Despeux, Catherine, and Livia Kohn. 2003. *Women in Daoism*. Three Pines Press.
- Faure, Bernard. 2003. *The Power of Denial: Buddhism, Purity, and Gender*. Princeton University Press.
- Galambos, Imre. 2020. *Dunhuang Manuscript Culture: End of the First Millennium*. De Gruyter. (Open access.)
- Geng Qiongke. 2025. "The Body, Gender, and Religious Practices: A Comparative Study of Daoist Inner Alchemy for Women and Buddhist Thoughts on the Female-to-Male Transformation." *Religions* 16.10: 1222.
- Gernet, Jacques. 1995. *Buddhism in Chinese Society: An Economic History from the Fifth to the Tenth Centuries*. Trans. Franciscus Verellen. Columbia University Press.
- Grass, Noa. 2024. "A Horse-Driven Court: Eunuchs and Horsemen in the Early-Ming Directorate of Imperial Horses." *Asia Major* 3rd ser. 37.2: 5–22.
- Hao Chunwen. 2010. "The Social Life of Buddhist Monks and Nuns in Dunhuang during the Late Tang, Five Dynasties, and Early Song." *Asia Major* 3rd ser. 23.2: 77–95.
- Hao Chunwen. 2021. "She Association Manuscripts from Dunhuang and the Study of Medieval She Association." Trans. Huang Bo. *Hualin International Journal of Buddhist Studies* 4.1: 59–98.
- Höckelmann, Michael. 2020. "Power Emasculated: Eunuchs, Great Clans and Political Reproduction under the Tang." *T'ang Studies* 38: 1–27. https://doi.org/10.1080/07375034.2020.1739705
- Hinsch, Bret. 2020. *Women in Tang China*. Rowman & Littlefield.
- Huang Yongfeng and Geng Qiongke. 2023. "Women Become Immortal through the Use of Procreation Ability: A Study on the Fertility Concept of Female Alchemy." *Religions* 14.6: 727.
- Jia Jinhua. 2018. *Gender, Power, and Talent: The Journey of Daoist Priestesses in Tang China*. Columbia University Press.
- Kirkland, Russell. 1992. Entries on Huang Ling-wei. *T'ang Studies* 10: 153–165.
- Levering, Miriam L. 1982. "The Dragon Girl and the Abbess of Mo-shan: Gender and Status in the Ch'an Buddhist Tradition." *Journal of the International Association of Buddhist Studies* 5.1: 19–35.
- Lo Tung-hwa 羅彤華. 2013. 〈唐代養子的類型及其禮法地位〉 [The Types and Confucian and Legal Status of the Adopted Child in the Tang]. 《臺大歷史學報》 52: 1–51.
- Lo, Vivienne, and Christopher Cullen (eds.). 2005. *Medieval Chinese Medicine: The Dunhuang Medical Manuscripts*. Routledge.
- McMahon, Keith. 2013. *Women Shall Not Rule: Imperial Wives and Concubines in China from Han to Liao*. Rowman & Littlefield.
- McMahon, Keith. 2016. *Celestial Women: Imperial Wives and Concubines in China from Song to Qing*. Rowman & Littlefield.
- Peach, Lucinda Joy. 2002. "Social Responsibility, Sex Change, and Salvation: Gender Justice in the Lotus Sūtra." *Philosophy East and West* 52.1: 50–74.
- Pregadio, Fabrizio. 2019. *The Way of the Golden Elixir: An Introduction to Taoist Alchemy*. 3rd ed. Golden Elixir Press.
- Rideout, J. K. 1949, 1953. "The Rise of the Eunuchs during the T'ang Dynasty," parts 1 and 2. *Asia Major* n.s. 1: 53–72; part 2: 42–58.
- Rong Xinjiang. 2013. *Eighteen Lectures on Dunhuang*. Trans. Imre Galambos. Brill.
- Rothschild, N. Harry. 2015. *Emperor Wu Zhao and Her Pantheon of Devis, Divinities, and Dynastic Mothers*. Columbia University Press.
- Schuster, Nancy. 1981. "Changing the Female Body: Wise Women and the Bodhisattva Career in Some Mahāratnakūṭasūtras." *Journal of the International Association of Buddhist Studies* 4.1: 24–69.
- Sommer, Matthew H. 2024. *The Fox Spirit, the Stone Maiden, and Other Transgender Histories from Late Imperial China*. Columbia University Press.
- So Wai Man. 2000. 《唐與北宋宦官研究》 [*A Study of Eunuchs in Tang and Northern Song China*]. MPhil thesis, University of Hong Kong.
- Tsai, Shih-shan Henry. 1991. "The Demand and Supply of Ming Eunuchs." *Journal of Asian History* 25.2: 121–146.
- Tsai, Shih-shan Henry. 1996. *The Eunuchs in the Ming Dynasty*. Albany: SUNY Press.
- Valussi, Elena. 2008. "Blood, Tigers, Dragons: The Physiology of Transcendence for Women." *Asian Medicine* 4: 46–85.
- Valussi, Elena. 2022. "Alchimia femminile. Brani dall'opera di Liu Yiming (1734–1821)." In Bianchi, Campo and Paolillo (eds.), *Scritti in memoria di Alfredo M. Cadonna*. Edizioni Ca' Foscari.
- Wang Mu. 2011. *Foundations of Internal Alchemy: The Taoist Practice of Neidan*. Trans. Fabrizio Pregadio. Golden Elixir Press.
- Wong, Alvin Ka Hin. 2012. "Transgenderism as a Heuristic Device: On the Cross-historical and Transnational Adaptations of the Legend of the White Snake." In Chiang (ed.), *Transgender China*, 127–158.
- Xin Yuerong and Xu Tao. 2026. "The Symmetrical, Integrated, and Pre-Sexual Body Concept: From the Vitality Narrative in Daoist Female Alchemy." *Religions* 17.2: 154.
- Zeitlin, Judith T. 1993. *Historian of the Strange: Pu Songling and the Chinese Classical Tale*. Stanford University Press.
- Zhang Yuanlin. "An Echo from the Ancient Past: Depictions of the Lotus Sutra in Dunhuang Murals." Trans. Ho Chiew Hui. *Journal of Oriental Studies* 28: 122–149.
- Zhou, Zuyan. 2012. "The Androgynous Ideal in Scholar-Beauty Romances: A Historical and Cultural View." In Chiang (ed.), *Transgender China*, 97–125.
- *Primary sources in translation or in the original:*
  - *The Lotus Sutra*, ch. 12. Trans. Tsugunari Kubo and Akira Yuyama (BDK, 2007) and Burton Watson (1993).
  - Confucius, *Analects* 12.11, 12.17, 13.3. Trans. James Legge.
  - The Five Phases treatises (*Wuxing zhi*) of the *Han shu*, *Xin Tang shu*, *Song shi* and *Yuan shi*, and *Taiping guangji* 367, read in Chinese.
  - British Library Or.8210/S.527: bylaws of a Dunhuang women's association, 959, read from the manuscript images.
  - Du Guangting. *Records of the Assembled Transcendents of the Fortified Walled City* (c. 913). Trans. Suzanne E. Cahill as *Divine Traces of the Daoist Sisterhood*. Three Pines Press, 2006.
  - McKnight, Brian E., and James T. C. Liu (trans.). 1999. *The Enlightened Judgments: Ch'ing-ming Chi, the Sung Dynasty Collection*. SUNY Press.
  - Ning Ke 寧可 and Hao Chunwen 郝春文 (eds.). 1997. 《敦煌社邑文書輯校》 [The Dunhuang association documents, collated]. Jiangsu guji.

Cited in the notes, not read: Furth, *A Flourishing Yin*; Jay, "Another Side of Chinese Eunuch History" (1993) and "Castration, Adoption, Marriage, and Burial"; Valussi, "Beheading the Red Dragon" (SOAS PhD, 2003). Further titles, with availability, are in `docs/research/china_reading_list.md`.

</details>

<details>
<summary><strong>South Asia</strong> (4 works)</summary>

For how Buddhist, Hindu, Jain and Delhi Sultanate courts read every faith's daughters.

- Cabezón, José Ignacio. 2017. *Sexuality in Classical South Asian Buddhism*. Wisdom Publications.
- Gyatso, Janet. 2003. "One Plus One Makes Three: Buddhist Gender, Monasticism, and the Law of the Non-excluded Middle." *History of Religions* 43.2: 89–115.
- Jackson, Peter. 1999. *The Delhi Sultanate: A Political and Military History*. Cambridge University Press.
- Zwilling, Leonard, and Michael J. Sweet. 2000. "The Evolution of Third-Sex Constructs in Ancient India: A Study in Ambiguity." In Leslie and McGee (eds.), *Invented Identities: The Interplay of Gender, Religion and Politics in India*, 99–132. Oxford University Press.

</details>

<details>
<summary><strong>The steppe, Korea and Southeast Asia</strong> (7 works)</summary>

- Andaya, Leonard Y. 2018. "The Bissu: Study of a Third Gender in Indonesia." In Zamfira, de Montlibert and Radu (eds.), *Gender in Focus*, 64–87. Budrich. (A reprint of Andaya 2000 in B. Andaya (ed.), *Other Pasts*.)
- Brewer, Carolyn. 1999. "Baylan, Asog, Transvestism, and Sodomy: Gender, Sexuality and the Sacred in Early Colonial Philippines." *Intersections* 2 (May). (A web text with numbered paragraphs and no page numbers.)
- Ismoyo, Petsy Jessy. 2020. "Decolonizing Gender Identities in Indonesia: A Study of Bissu 'The Trans-Religious Leader' in Bugis People." *Paradigma* 10.3: 277–288.
- Kennedy, Matthew. 1993. "Clothing, Gender, and Ritual Transvestism: The Bissu of Sulawesi." *Journal of Men's Studies* 2.1: 1–13.
- Kim Jae-myeong 김재명 (金載名). 2006. 「高麗 內侍制의 成立」 [The Formation of the Goryeo Naesi System]. 정신문화연구 29.2 (no. 103): 151–173. (The OCR copy lost every Arabic numeral, and the page numbers were reconstructed.)
- McCoy, Alfred W. 1982. "Baylan: Animist Religion and Philippine Peasant Ideology." *Philippine Quarterly of Culture and Society* 10.3: 141–194.
- Terbish, Baasanjav. 2023. *Sex in the Land of Genghis Khan: From the Times of the Great Conqueror to Today*. Lanham: Lexington Books / Rowman & Littlefield.

Cited in the notes, not read: Davies, Sharyn Graham, *Challenging Gender Norms: Five Genders among the Bugis in Indonesia* (2006).

</details>

<details>
<summary><strong>General and comparative history</strong> (10 works)</summary>

- Adkins, Evelyn. 2020. "The Politics of Transgender Representation in Apuleius' *Golden Ass* and *Loukios, or the Ass*." In Surtees and Dyer (eds.), *Exploring Gender Diversity in the Ancient World*, 157–168.
- Álvarez-Pedrosa, Juan Antonio (ed.). 2021. *Sources of Slavic Pre-Christian Religion*. Brill.
- Álvarez-Pedrosa, Juan Antonio, and Enrique Santos Marinas. 2023. *Rituals in Slavic Pre-Christian Religion: Festivals, Banqueting, and Divination*. Arc Humanities Press.
- Betancourt, Roland. 2021. "Where Are All the Trans Women in Byzantium?" In LaFleur, Raskolnikov and Kłosowska (eds.), *Trans Historical*.
- Krass, Andreas. 2012. "Saying It with Flowers: Post-Foucauldian Literary History and the Poetics of Taboo in a Premodern German Love Song." In Spector, Puff and Herzog (eds.), *After The History of Sexuality: German Genealogies With and Beyond Foucault*, 63–75. Berghahn.
- LaFleur, Greta, Masha Raskolnikov, and Anna Kłosowska (eds.). 2021. *Trans Historical: Gender Plurality Before the Modern*. Cornell University Press.
- Levin, Eve. 1989. *Sex and Society in the World of the Orthodox Slavs, 900–1700*. Cornell University Press.
- Puff, Helmut. 2012. "After the History of (Male) Homosexuality." In Spector, Puff and Herzog (eds.), *After The History of Sexuality*, 17–30. Berghahn.
- Surtees, Allison, and Jennifer Dyer (eds.). 2020. *Exploring Gender Diversity in the Ancient World*. Edinburgh University Press.
- Wiesner-Hanks, Merry E. 2011. *Gender in History: Global Perspectives*. 2nd ed. Wiley-Blackwell.

Cited in the notes, not read: Nanda, Serena, *Neither Man nor Woman: The Hijras of India* (1990); Reddy, Gayatri, *With Respect to Sex* (title as given, truncated in the notes).

</details>

<details>
<summary><strong>Fiction</strong> (1 work)</summary>

- Greaves, Alyson. 2022. *Welcome to Dorley Hall*. The Sisters of Dorley, book 1. Serialised online from 2022; print edition from Wilton Square Books. Read through the fan wiki *Dorleybase* (dorley.wiki), the publisher's description and reader reviews. See [`docs/dorley_precedent.md`](docs/dorley_precedent.md).

</details>

<details>
<summary><strong>Online discussion</strong> (9 works)</summary>

- Bhatt, Talia. 2024. "The Third Sex." Substack (taliabhattwrites.substack.com). The same text appears as a chapter of *Trans/Rad/Fem*.
- Bhatt, Talia. 2024. "Degendering and Regendering." Substack, 8 October 2024. The same text appears as a chapter of *Trans/Rad/Fem*.
- Gabriel, Kay. 2020. "Gender as Accumulation Strategy." *Invert Journal*. (Read through a Tumblr excerpt.)
- Richardson-Read, Nate. c. 2021. "Norse Myth: Queer Magic, Queer Deities, Gay Priest Cults and Cross-Dressing." Cailleach's Herbarium blog, Self-Making series, c. March 2021. **Marked popular/unverified.** The author calls it "a working theory of mine", and the notes say its Saxo claim about Freyr's priests at Uppsala still needs checking.
- Gleeson, Jules Joanne. 2017. "Transition and Abolition: Notes on Marxism and Trans Politics." *Viewpoint Magazine*.
- Public Bluesky and Tumblr discussion of baedelism and the bæddel movement, 2013–2026, surveyed for this project in October 2026. Individual posts are not reproduced or listed; the survey notes are kept privately.
- Public Bluesky and Tumblr discussion of third-wave transfeminism and the *Trans/Rad/Fem* circle, surveyed in October 2026. Notes kept privately.
- Public Bluesky and Tumblr discussion of transgender Marxism, surveyed in October 2026. Notes kept privately.
- Public Bluesky and Tumblr reader discussion of *The Sisters of Dorley*, 2025–2026. See [`docs/dorley_precedent.md`](docs/dorley_precedent.md).

</details>

<details>
<summary><strong>Primary sources cited through the literature</strong> (8 groups)</summary>

None of these were read directly. Each was used through the secondary works above, and the report that cites it is given in brackets.

- Norse and English: Snorri's *Ynglinga saga*; *Lokasenna*; *Þrymskviða*; *Ljósvetninga saga*; *Legenda aurea* and the Vernon MS; the Durham 1417 court record (Birch); the Old English glossaries for *bæddel* (Wade; Fulk and Jurasinski). *Grágás*, Saxo and the Canons of Theodore are now read in translation and listed under Northern Europe.
- Byzantine: Constantine VII, *De cerimoniis*; Philotheos, *Kletorologion* (899); Leo VI's Novels (26, 60); the *Ekloga*; John Malalas; Justinian, Novel 142; canon 1 of Nicaea; Laodicea; Theophylact of Ochrid, *In Defence of Eunuchs*; the *Kecharitomene* typikon; Paul of Aegina; Liudprand of Cremona; Matthaios Blastares, *Syntagma*; John Pediasimos, *Peri gamôn*; Harmenopoulos, *Hexabiblos*.
- Islamic: al-Jahiz, *Kitab al-Hayawan*; al-Mas'udi, *Muruj al-dhahab*; *Kitab al-Aghani*; *Kitab al-'Ayn* (Ayalon; Rowson).
- Chinese and Buddhist: *Soushenji*; the Lotus Sutra (Kumārajīva tr., 406); the *Saṃyutta Nikāya*; *Taiping guangji* (978); *Mingshi*; the Tang Code (Chiang ed.; Hoeckelmann; Tsai; Sommer).
- Mongol: *The Secret History of the Mongols*; Rashid al-Din; Juvaini; Carpini; Rubruck; Marco Polo; the *Yuanshi* (Terbish, who used English translations).
- Southeast Asian: *I La Galigo*; the Bugis *lontara'* chronicles; Pigafetta (1521) (McCoy; Kennedy; Andaya; Brewer).
- Classical and Latin: Apuleius, *Golden Ass*; Catullus; Ovid; Lucian; Firmicus Maternus; Matthew 19:12 (Surtees and Dyer; Karras and Pierpont; Tougher).
- Later medieval Western: *Roman de Silence* (Watt); the Eleanor Rykener deposition (1394) (Henningsen); Bracton, *De legibus et consuetudinibus Angliae*; *Fleta* (Trans Historical; Stryker; Karras and Pierpont).

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
