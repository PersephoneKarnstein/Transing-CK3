<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">

![Crusader Kings III 1.20](https://img.shields.io/badge/Crusader%20Kings%20III-1.20.*-8a2be2)
![Status: alpha](https://img.shields.io/badge/status-alpha-orange)
![Playtesters wanted](https://img.shields.io/badge/playtesters-wanted-f5a9b8)

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="docs/images/logo.png" alt="Logo" width="96" height="96">

  <h3 align="center">Transing CK3</h3>
  <p align="center">
    <em>Adelphai Dorleyaiou</em>, the Sisters of Dorylaion: three trans-women-centred faiths for Crusader Kings III.
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
    <li><a href="#bæddel-the-high-seat">Bæddel: the High Seat</a></li>
    <li><a href="#the-way-of-the-jade-embryo">The Way of the Jade Embryo</a></li>
    <li><a href="#shared-mechanics">Shared mechanics</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#bibliography">Bibliography</a></li>
  </ol>
</details>

## About the project

This mod adds three faiths built around trans women to Crusader Kings III. Each is grounded in a different historical setting and plays differently. Their tenets come from contemporary transfeminist writing: baedelism, third-wave transfeminism and transgender Marxism. A history pass then gives each a veneer of plausibility in its own place and period.

The three faiths answer the same three questions in different ways:

| | Dorleyism | Bæddel | Way of the Jade Embryo |
|---|---|---|---|
| **How one becomes a daughter** | The knife, as a sacrament with a sponsor | Seiðr: going under beneath the völva's high seat | Ten months' inner gestation of one's own body |
| **How the line continues** | A founding charter passes land to adopted daughters | The hall's fostered, sworn and adopted daughters | Adopted heirs, and temple societies that hold property in common |
| **How it meets the world** | Refuge, intake and church politics | Outlawry, raiding and insult duels | Palace factions against the scholar-officials |
| **Home** | Dorylaion, Phrygia | Gotland | Dunhuang, at the Mogao caves |

What the mod is not:

- **No antagonist.** It does not add a hostile "anti-trans" nation or stage an allegorical clash of superpowers. It adds the faiths, and vanilla Christendom, the Caliphate and the Tang court react as they would.
- **Not trans men.** Trans-masculine content is out of scope. Someone else is very welcome to make it.
- **Vanilla castration still works as before.** Castrating someone with the base game's interaction does not turn them into a daughter.

> **Content note.** The mod deals with castration, with a penal path that transitions violent prisoners (the "Dorley precedent", after Alyson Greaves's *Welcome to Dorley Hall*), and with the transmisogyny of medieval law and custom. Event text is written without gore, but the subject matter is there.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Playtesters wanted

The mod is in alpha. Most of it has never run in a real campaign, and we need people to play it and tell us what breaks. You don't need any modding experience.

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
5. **Start a new game.** In the Ruler Designer you can choose the Kybeline culture and any of the three faiths. You can also convert to one in a normal game.

To update later, pull or re-download into the same folder. The launcher file does not need to change.

### What to test and how to report

Good first tests:

- **Ruler Designer.** Do all three faiths and the Kybeline culture appear?
- **The three rites.** As a Marked man, take each faith's decision: *Take the Knife*, *Go Under the High Seat* and *Gestate the Jade Embryo*.
- **Re-embodiment.** After a rite, do your titles, marriage, children, adoptive parents and skills carry over?
- **Adoption.** Try *Take as Daughter* on a courtier, a ward and a guest.
- **Arrivals and refuges.** Over a long reign, do Marked travellers and cast-out women arrive at your court?

When something breaks, [open an issue](https://github.com/PersephoneKarnstein/Transing-CK3/issues/new?labels=bug) and include:

- **What you did** and what you expected to happen.
- **Your error log.** It is `error.log` in the `logs` folder next to your mod folder.
- **A save**, if you can attach one.

The game's console can run test scripts from `tools/run/`. Copy them into the `run` folder next to your mod folder, launch the game with `-debug_mode`, open the console with `~`, and type, for example, `run tm_census.txt`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Dorleyism: the Sisters of Dorylaion

*Adelphai Dorleyaiou.* A Christian heresy in Byzantine Anatolia, centred on the house at Dorylaion. The name is a pun on Dorley Hall.

The Sisters are nostalgic for a sect almost nobody remembers, the gallae of the Mother at Pessinus, a day's ride away. They say that house never closed, and they remember it kinder than it was. What they refuse is what the Byzantine court offers in its place. The court calls its eunuchs angels and buys them as boys. The Sisters want neither the title nor the market. One who takes the knife rises a daughter, not a third thing.

- **The gate: the knife.** *Take the Knife* is a sacrament with a sponsor, ending in a new name. Each faith picks one of three houses for who may be cut:
  - **Grandmother's House:** any captive, in the old cruel way.
  - **Aunt Bea's House:** only violent prisoners, each under a sponsor who walked the same road, with a washout path for those who will not change.
  - **Gift Alone:** only those who ask.
- **The line.** Daughters choose their heirs rather than breed them. Inheritance runs through adopted daughters, on the model of Byzantine convent charters that passed estates to women "in perpetuity."
- **The world.** A ruler can petition the Mother House to declare their house a refuge. Marked travellers and women turned out by their families then come far more often, and the house can send to the Mother House for newcomers. The *Rescue the Daughters* war frees captive daughters from a neighbour.
- **Tenets.** Day of Blood, Daughters Chosen Not Born, and Unbending Sisterhood.
- **Head of faith.** The Mother of Mothers, Theia Beatrike, an elder daughter seated at Dorylaion.
- **The schism to come.** The main rite is Aristotelian: the cut are women. A planned Galenic splinter takes the court's view that the cut are "a kind of their own." The Aristotelians call that "the old cage with a new name."

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Bæddel: the High Seat

*Working name.* A Germanic pagan faith of Scandinavia and Anglo-Saxon England. It merges *bæddel*, an attested Old English word, with *seiðr* and *ergi*.

In the north the sanctioned crossing has always run toward manhood. A man who went the other way was *ergi*, outlawed by law and killed by custom. The Bæddels keep the other road. Our sources find no castration in the north at all, so this faith does not use the knife.

- **The gate: seiðr.** In *Go Under the High Seat*, the völva sings and the seeker goes under. The spirits may refuse, and then you try again next winter. A daughter then declares herself before the thing. When someone shouts *ergi*, she answers in verse, with steel, or not at all.
- **The line.** The hall's daughters are fostered, sworn and adopted. Two may bind themselves as sisters by the old oath.
- **The world.** A martial faith. Óðinn's host has no men in it. The hall raids to bring its daughters home, and its clergy fight.
- **Tenets.** Seiðr Unmans, Óðinn's Host, and Daughters of the Hall.
- **Holy sites.** Uppsala, Trondheim, York and Kyiv. Kyiv sits on the Varangian road south toward Dorylaion.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## The Way of the Jade Embryo

*Working name.* A Daoist faith of Tang China, seated at Dunhuang beneath the Mogao caves. Cave 331 there holds a mural of the Lotus Sutra's dragon girl, who changed her body in an instant. Empress Wu Zetian paid for it.

Daoist inner alchemy teaches that an adept gestates an immortal embryo for ten months and is born from it. The Way turns the work the other way: the adept gestates her own body and is born as herself. The palace calls such women eunuchs so that it need not call them women. The Way answers with Confucius's rectification of names. A daughter named before witnesses is a daughter, and any eunuch who seeks the same is received as a sister.

- **The gate: the jade embryo.** In *Gestate the Jade Embryo*, a guarantor vouches for the adept and a nüguan asks her "Will you ever repent?" Ten months follow, with trials in the third and sixth months. Either trial can lose the embryo, and then the work begins again. Birth comes from the crown of the head, and a name is given before witnesses.
- **The line.** Temple and burial societies hold their sisters' goods in common against crown confiscation. They adopt the heirs who will keep the rites.
- **The world.** A courtly faith of intrigue and stewardship. A planned palace faction will contend with the scholar-officials inside the imperial court.
- **Tenets.** The Jade Embryo, Rectified Names, and Temple Societies.
- **Holy sites.** The Mogao caves, Mount Longhu, Mount Qingcheng and Mount Wudang.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Shared mechanics

- **Marked by the Mother.** A rare trait for men who are trans women before any rite. You can filter for it in the Character Finder to find people to recruit and adopt.
- **Re-embodiment.** After a rite, the daughter continues in a female body with the same face. Her titles, marriage, children, parents, adoptive parents, skills and lifestyle experience carry over. Re-embodied daughters are infertile. A game rule turns this off.
- **Take as Daughter.** Each faith's own adoption. Unlike vanilla adoption it accepts adults, and it ignores the rules that block children with landed relatives.
- **Arrivals.** Each year a Marked traveller, or a woman turned out for bearing no children, may come to the court of a ruler of these faiths.
- **Same-sex marriage.** All three faiths allow it, whatever the game rule says.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Dorleyism: faith, culture, the three houses of the knife, the Dorley prisoner path, refuges
- [x] Bæddel and the Way of the Jade Embryo: faiths, tenets and gates
- [x] Re-embodiment, Take as Daughter, arrivals
- [ ] Bæddel: insult duels, landless war-band play, Christian outlawry pressure
- [ ] Jade Embryo: the palace faction, temple societies against confiscation, omen events
- [ ] Dorleyism: daughters in court offices, the court's tolerance decaying after 1066, the Galenic splinter rite
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

No license has been chosen yet. Until one is added, all rights are reserved by the author.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template), which this README is based on
- [CK3 Tiger](https://github.com/amtep/tiger), for script validation
- [Paradox Modding Toolkit](https://github.com/JDeffner/paradox-modding-toolkit), for editing and validation tools
- The trans writers on Bluesky and Tumblr whose public discussion of baedelism, third-wave transfeminism and transgender Marxism shaped the tenets. Their posts are not reproduced here.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Bibliography

Works the research for this mod read, in full or in named chapters. Works it only points to appear at the end of each group as "Cited in the notes, not read". Details are given as our notes record them, and a missing detail is marked rather than guessed. Corrections are welcome.

### Transfeminist theory and trans studies

- Bettcher, Talia Mae. 2013. "Evil Deceivers and Make-Believers: On Transphobic Violence and the Politics of Illusion." In Stryker and Aizura (eds.), *The Transgender Studies Reader 2*.
- Bhatt, Talia. 2025. *Trans/Rad/Fem: Essays on Transfeminism, Book 1*. (No publisher given in the notes. Read in full, with a second pass on the chapters "The Third Sex" and "Degendering and Regendering".)
- Chu, Andrea Long. 2019. *Females*. Verso.
- Gleeson, Jules Joanne, and Elle O'Rourke (eds.). 2021. *Transgender Marxism*. Pluto Press. (Read in full: introduction, 14 chapters and Jordy Rosenberg's afterword.)
- Raymond, Janice G. "Sappho by Surgery: The Transsexually Constructed Lesbian-Feminist." In Stryker and Whittle (eds.), *The Transgender Studies Reader* (2006). (Original date not given in the notes.)
- Stryker, Susan. 2026. *Transgender History*. 3rd ed. Seal Press. (The front matter gives the subtitle "A Resource for Today's Struggle—and Tomorrow's".)
- Stryker, Susan, and Aren Z. Aizura (eds.). 2013. *The Transgender Studies Reader 2*. (details incomplete: no publisher recorded)
- Stryker, Susan, and Dylan McCarthy Blackston (eds.). 2022/2023. *The Transgender Studies Reader Remix*. Routledge.
- Stryker, Susan, and Stephen Whittle (eds.). 2006. *The Transgender Studies Reader*. Routledge.

Cited in the notes, not read: Bhatt, Talia, *Brown/Trans/Les* (2026); Feinberg, Leslie, *Transgender Warriors* (in the Remix bibliography); Koyama, Emi, *The Transfeminist Manifesto* (2001); Lewis, Sophie, *Abolish the Family* (Verso 2022); O'Brien, M. E., *Family Abolition* (Pluto 2023); Raha, Nat, and Mijke van der Drift, *Trans Femme Futures* (Pluto 2024); Serano, Julia, *Whipping Girl* (2007).

### Byzantium, Islam and the eunuch traditions

- Ayalon, David. 1999. *Eunuchs, Caliphs and Sultans: A Study in Power Relationships*. Jerusalem: Magnes Press.
- Marmon, Shaun. 1995. *Eunuchs and Sacred Boundaries in Islamic Society*. Oxford University Press.
- Neil, Bronwen, and Lynda Garland (eds.). 2013. *Questions of Gender in Byzantine Society*. Ashgate. (Routledge reprint 2016.)
- Neville, Leonora. 2019. *Byzantine Gender*. Past Imperfect. Arc Humanities Press.
- Rapp, Claudia. 2016. *Brother-Making in Late Antiquity and Byzantium: Monks, Laymen, and Christian Ritual*. Oxford University Press.
- Rowson. 1991. "The Effeminates of Early Medina." *Journal of the American Oriental Society* 111.4: 671–693. (details incomplete: author's given name not recorded)
- Tougher, Shaun. 2008. *The Eunuch in Byzantine History and Society*. Routledge. (Read in the 2009 Taylor & Francis e-library edition.)
- Tougher, Shaun. 2013. "Bearding Byzantium: Masculinity, Eunuchs and the Byzantine Life Course." In Neil and Garland (eds.), *Questions of Gender in Byzantine Society*, 153–166.

Cited in the notes, not read: Ayalon, David, "On the Eunuchs in Islam," *Jerusalem Studies in Arabic and Islam* 1 (1979): 67–124; Kuefler, *The Manly Eunuch* (2001); Messis, *Les eunuques à Byzance* (2014); Mullett on Theophylact of Ochrid's *In Defence of Eunuchs*; Ringrose, *The Perfect Servant* (2003); Sanders, Paula, "Gendering the Ungendered Body: Hermaphrodites in Medieval Islamic Law" (1991).

### Northern Europe

- Berry, Miles. 2022. "Gender Diversity and its Societal Place in Medieval Scandinavia." *Oregon Undergraduate Research Journal* 20.2: 134–154. (An undergraduate paper. The notes flag factual slips.)
- Birch, Eleanor. 2025. "Deviance or Devotion: Women Dressed as Men in Late Medieval England." *Fashion Theory* 29.5: 619–639.
- Jakobsson, Ármann. 2011. "Óðinn as mother: the old norse deviant patriarch." *Arkiv för nordisk filologi* 126. (Read in proof, paginated 01–012.)
- Karras and Pierpont. 2023. *Sexuality in Medieval Europe: Doing Unto Others*. 4th ed. Routledge. (details incomplete: authors' given names not recorded)
- Tommony, Isabelle, with C. M. Forster. 2024. "Margins Undefined: the flexibility of gender boundaries in the European Middle Ages." *BILT Student Research Journal* 5: 2–9. (A peer-reviewed undergraduate journal from Bristol. Forster is credited on the version-of-record citation.)

### China, the steppe and Southeast Asia

- Andaya, Leonard Y. 2018. "The Bissu: Study of a Third Gender in Indonesia." In Zamfira, de Montlibert and Radu (eds.), *Gender in Focus*, 64–87. Budrich. (A reprint of Andaya 2000 in B. Andaya (ed.), *Other Pasts*.)
- Brewer, Carolyn. 1999. "Baylan, Asog, Transvestism, and Sodomy: Gender, Sexuality and the Sacred in Early Colonial Philippines." *Intersections* 2 (May). (A web text with numbered paragraphs and no page numbers.)
- Burton-Rose, Daniel. 2012. "Gendered Androgyny: Transcendent Ideals and Profane Realities in Buddhism, Classicism, and Daoism." In Chiang (ed.), *Transgender China*, 67–95.
- Chiang, Howard (ed.). 2012. *Transgender China*. Palgrave Macmillan. (Chapters 1–5 read in full. Chapters 6–11 are modern and were only skimmed.)
- Chiang, Howard. 2012. "How China Became a 'Castrated Civilization' and Eunuchs a 'Third Sex'." In Chiang (ed.), *Transgender China*, 23–66.
- Dale. 2018. *Inside the World of the Eunuch*. HKU Press. (details incomplete: the author's given name and any subtitle are not recorded)
- Hoeckelmann, Michael. 2020. "Power Emasculated: Eunuchs, Great Clans and Political Reproduction under the Tang." *Tang Studies*, 1–27. DOI 10.1080/07375034.2020.1739705. (details incomplete: volume and issue not recorded)
- Ismoyo, Petsy Jessy. 2020. "Decolonizing Gender Identities in Indonesia: A Study of Bissu 'The Trans-Religious Leader' in Bugis People." *Paradigma* 10.3: 277–288.
- Kennedy, Matthew. 1993. "Clothing, Gender, and Ritual Transvestism: The Bissu of Sulawesi." *Journal of Men's Studies* 2.1: 1–13.
- Kim Jae-myeong 김재명 (金載名). 2006. 「高麗 內侍制의 成立」 [The Formation of the Goryeo Naesi System]. 정신문화연구 29.2 (no. 103): 151–173. (The OCR copy lost every Arabic numeral, and the page numbers were reconstructed.)
- McCoy, Alfred W. 1982. "Baylan: Animist Religion and Philippine Peasant Ideology." *Philippine Quarterly of Culture and Society* 10.3: 141–194.
- Sommer. 2024. *The Fox Spirit, the Stone Maiden, and Other Transgender Histories from Late Imperial China*. Columbia University Press. (details incomplete: author's given name not recorded)
- Terbish, Baasanjav. 2023. *Sex in the Land of Genghis Khan: From the Times of the Great Conqueror to Today*. Lanham: Lexington Books / Rowman & Littlefield.
- Tsai, Shih-shan Henry. 1991. "The Demand and Supply of Ming Eunuchs." *Journal of Asian History* 25.2: 121–146.
- Tsai, Shih-shan Henry. 1996. *The Eunuchs in the Ming Dynasty*. Albany: SUNY Press.
- Wong, Alvin Ka Hin. 2012. "Transgenderism as a Heuristic Device: On the Cross-historical and Transnational Adaptations of the Legend of the White Snake." In Chiang (ed.), *Transgender China*, 127–158.
- Zhou, Zuyan. 2012. "The Androgynous Ideal in Scholar-Beauty Romances: A Historical and Cultural View." In Chiang (ed.), *Transgender China*, 97–125.

Cited in the notes, not read: Davies, Sharyn Graham, *Challenging Gender Norms: Five Genders among the Bugis in Indonesia* (2006); Furth, *A Flourishing Yin*; Jay, "Castration, Adoption, Marriage, and Burial" (1993).

### General and comparative history

- Adkins, Evelyn. 2020. "The Politics of Transgender Representation in Apuleius' *Golden Ass* and *Loukios, or the Ass*." In Surtees and Dyer (eds.), *Exploring Gender Diversity in the Ancient World*, 157–168.
- Betancourt, Roland. 2021. "Where Are All the Trans Women in Byzantium?" In LaFleur, Raskolnikov and Kłosowska (eds.), *Trans Historical*.
- LaFleur, Greta, Masha Raskolnikov, and Anna Kłosowska (eds.). 2021. *Trans Historical: Gender Plurality Before the Modern*. Cornell University Press.
- Surtees, Allison, and Jennifer Dyer (eds.). 2020. *Exploring Gender Diversity in the Ancient World*. Edinburgh University Press.
- Wiesner-Hanks, Merry E. 2011. *Gender in History: Global Perspectives*. 2nd ed. Wiley-Blackwell.

Cited in the notes, not read: Nanda, Serena, *Neither Man nor Woman: The Hijras of India* (1990); Reddy, Gayatri, *With Respect to Sex* (title as given, truncated in the notes); Roller, Lynn, *In Search of God the Mother: The Cult of Anatolian Cybele* (1999).

### Fiction

- Greaves, Alyson. 2022. *Welcome to Dorley Hall*. Book 1 of *The Sisters of Dorley*. First published as a serial on AO3, Scribblehub and Patreon, with a print edition. A second volume, *Secrets of Dorley Hall*, was launching in November 2026. Read through the fan wiki *Dorleybase* (dorley.wiki), the publisher's blurb, Goodreads reviews and the review essay "Making Women Out of Men" (*Every Book a Doorway*). See [`docs/dorley_precedent.md`](docs/dorley_precedent.md).
- Peters, Torrey. Her line on T4T is quoted second-hand from a Tumblr reblog, where it is marked as a novel quotation. (details incomplete: the novel's title is not given)

### Online discussion

- Bhatt, Talia. 2024. "The Third Sex." Substack (taliabhattwrites.substack.com). The same text appears as a chapter of *Trans/Rad/Fem*.
- Bhatt, Talia. 2024. "Degendering and Regendering." Substack, 8 October 2024. The same text appears as a chapter of *Trans/Rad/Fem*.
- Gabriel, Kay. 2020. "Gender as Accumulation Strategy." *Invert Journal*. (Read through a Tumblr excerpt.)
- Richardson-Read, Nate. c. 2021. "Norse Myth: Queer Magic, Queer Deities, Gay Priest Cults and Cross-Dressing." Cailleach's Herbarium blog, Self-Making series, c. March 2021. **Marked popular/unverified.** The author calls it "a working theory of mine", and the notes say its Saxo claim about Freyr's priests at Uppsala still needs checking.
- "Transition and Abolition: Notes on Marxism and Trans Politics." 2017. *Viewpoint Magazine*. (The notes give no author.)
- Public Bluesky and Tumblr discussion of baedelism and the bæddel movement, 2013–2026, surveyed for this project in October 2026. Individual posts are not reproduced or listed; the survey notes are kept privately.
- Public Bluesky and Tumblr discussion of third-wave transfeminism and the *Trans/Rad/Fem* circle, surveyed in October 2026. Notes kept privately.
- Public Bluesky and Tumblr discussion of transgender Marxism, surveyed in October 2026. Notes kept privately.
- Public Bluesky and Tumblr reader discussion of *The Sisters of Dorley*, 2025–2026. See [`docs/dorley_precedent.md`](docs/dorley_precedent.md).

### Primary sources cited through the literature

None of these were read directly. Each was used through the secondary works above, and the report that cites it is given in brackets.

- Norse and English: *Grágás*; Snorri's *Ynglinga saga*; *Lokasenna*; *Þrymskviða*; *Ljósvetninga saga*; Saxo Grammaticus, *Gesta Danorum*; *Legenda aurea* and the Vernon MS; the Durham 1417 court record (Birch); Old English glossaries and penitentials for *bæddel* and *bædling* (the online survey).
- Byzantine: Constantine VII, *De cerimoniis*; Philotheos, *Kletorologion* (899); Leo VI's Novels (26, 60); the *Ekloga*; John Malalas; Justinian, Novel 142; canon 1 of Nicaea; Laodicea; Theophylact of Ochrid, *In Defence of Eunuchs*; the *Kecharitomene* typikon; Paul of Aegina; Liudprand of Cremona; Matthaios Blastares, *Syntagma*; John Pediasimos, *Peri gamôn*; Harmenopoulos, *Hexabiblos*.
- Islamic: al-Jahiz, *Kitab al-Hayawan*; al-Mas'udi, *Muruj al-dhahab*; *Kitab al-Aghani*; *Kitab al-'Ayn* (Ayalon; Rowson).
- Chinese and Buddhist: *Soushenji*; the Lotus Sutra (Kumārajīva tr., 406); the *Saṃyutta Nikāya*; *Taiping guangji* (978); *Mingshi*; the Tang Code (Chiang ed.; Hoeckelmann; Tsai; Sommer).
- Mongol: *The Secret History of the Mongols*; Rashid al-Din; Juvaini; Carpini; Rubruck; Marco Polo; the *Yuanshi* (Terbish, who used English translations).
- Southeast Asian: *I La Galigo*; the Bugis *lontara'* chronicles; Pigafetta (1521) (McCoy; Kennedy; Andaya; Brewer).
- Classical and Latin: Apuleius, *Golden Ass*; Catullus; Ovid; Lucian; Firmicus Maternus; Matthew 19:12 (Surtees and Dyer; Karras and Pierpont; Tougher).
- Later medieval Western: *Roman de Silence*; the Eleanor/John Rykener deposition (1394); Bracton, *De legibus et consuetudinibus Angliae*; *Fleta* (Trans Historical; Stryker; Karras and Pierpont).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
