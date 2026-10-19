# Phelan, "The Jewish 'monopoly' of the slave trade in the early Middle Ages" (2023): design reading

Source: Joseph Phelan, "The Jewish 'monopoly' of the slave trade in the early Middle Ages: the origins of an enduring historical motif", *Patterns of Prejudice* 57.3 (2023), pp. 161–174. doi:10.1080/0031322X.2023.2287871. Open access, CC BY 4.0.
Read from a text extraction kept outside the repo. The extraction (from the EPUB) carries no page numbers, so references are to Phelan's section headings and endnote numbers.

**What was read.** In full: the abstract, all four sections ("Henry Hart Milman, *The History of the Jews*", "Milman's successors", "Jewish historians", "The persistence of a historical motif") and notes 1–40.

**Relation to existing notes.**
- `hist_ayalon_eunuchs_caliphs.md` records Ibn Ḥawqal and al-Muqaddasī on Jewish castrators at Pechina.
- `isl_el_azhari_queens_eunuchs.md` repeats it: Saqaliba cut "by Jewish physicians" (El-Azhari p. 145).
- Grabowski 2015 argues for Jewish merchants behind Liutprand's *carzimasia*.
- Finding 5 of `comparanda_reading_list.md` names Toch 2013/2014 and this article as the reasons to keep all of this out of the mod.

Phelan is not about the Arabic or Latin primary sources. He is about how **modern historiography** turned thin evidence into a "fact". That is the frame the mod must not reproduce.

## 1. The argument in brief

- **The claim.** Nineteenth-century historians repeated "with unquestioning confidence" that Jews "were either dominant in or monopolized the slave trade in Europe" after Rome fell (introduction).
- **Toch's view, and Phelan's correction.** Toch traces the idea to a "twin parenthood": Graetz and the economist Wilhelm Roscher (n. 1). Phelan pushes it earlier. In English it already had "the status of established and uncontested fact" before Graetz was translated in the 1890s.
- **Origin: Milman, *History of the Jews* (1829).**
  - Milman asserts that the internal slave trade "fell almost entirely into the hands of the Jews" and cites no evidence (n. 9).
  - He imagines a Jew taking "a sort of revengeful satisfaction" in Christian ruin, buying "the fairest youths, and even high-born maidens" (n. 9).
  - His sources were Jost's *Geschichte der Israeliten* (1820–29) and Beugnot's *Les Juifs d'occident* (1824). Jost spoke of favourable circumstances. Milman added **motive**: vengeance (nn. 10–16).
- **The repeaters.**
  - Huie (1840) builds a "lurid fantasy" partly from *The Merchant of Venice* (n. 26).
  - Gosse (1851) has the trader "gloat" over Rome's ruin (n. 27).
  - The *Church Quarterly Review* (1888) repeats it (n. 28).
  - The appeal was **supersessionist**: Jewish suffering read as retribution.
  - The continental account (Depping 1844) is more local, but it still speculates that Jews hated Christians "par principe" (n. 30).
- **Jewish historians accepted it rather than question it.**
  - Katie Magnus (1888) admits it but makes Jews "the kindest of masters" (n. 31).
  - Joseph Jacobs embellishes. He glosses Gregory the Great's English slave boys as "Judæorum servi" (n. 32). He has a "Josce Jew of Gloucester" financing Strongbow's invasion of Ireland (n. 33).
  - Jacobs and Isidore Singer put it into the *Jewish Encyclopedia* ("Slave-trade", 1906) as settled fact: "Jews had become the chief traders" by Gregory's time. Via Graetz they add Byzantine Jews buying Slavs at Prague (Ibrahim ibn Ya'qub) and Spanish Jewish wealth from "Slavonian slaves" (nn. 34–35).
  - Phelan's explanation: an assimilationist wish to show Jews as "key players at decisive moments", a "perverse pride" (final section).
- **Conclusion.** The motif shows "the seemingly ineradicable tendency of historical interpretation to solidify into unarguable fact if placed in the right ideological solution" (final section).

## 2. What matters for the design

1. **The motif has two parts: a role and a motive.** The role is that Jews ran the trade in human beings. The motive is revenge and gloating on Christians, with buying "youths and high-born maidens" as the image. The mod must avoid **both**. The motive is the older libel, and it fits a fantasy of captive daughters all too easily.
2. **The "rescue" frame invites it.** The Dorleyite *Rescue the Daughters* casus belli (`docs/faith_design.md`, the "mirror" bullet near the top and decisions table row 11) frees captive daughters from a holder. If the holder can be a Jewish ruler (Khazaria, `kabarism`), the game would show "Christians freeing captives from Jews". That is the Milman picture.
3. **The positive apologetic is also out.** Magnus's "kindest masters" and Jacobs's "key players" are the same motif turned to pride. A Jewish faith or sect must not be made attractive by being good at owning or trading people, or by financing wars (Jacobs's Strongbow story).
4. **The eunuch-making strand is the same motif, sharper.** The Pechina castrators (Ayalon; El-Azhari p. 145) and the Verdun *carzimasia* (Grabowski) feed this exact narrative: Jews making eunuchs of Christian boys. The texts the mod already cites carry the claim, but the mod must not dramatise it. It is also halakhically impossible for a pious character (`jud_rabbinic_primary_texts.md` §7: Issurei Bi'ah 16:10–13 forbids castration, and even asking a gentile to castrate).

## 3. Corrections to current docs

- **None to the reading list's verdict**, which already says to keep this out. Two refinements:
  - Finding 5 should add that the motif carries a **motive** (revenge) as well as a role. The ban covers any event text implying Jewish hatred of Christians as the driver of any trade.
  - `isl_el_azhari_queens_eunuchs.md` and `hist_ayalon_eunuchs_caliphs.md` record the Pechina/"Jewish physicians" claim as data. Each should carry a one-line pointer here: data from hostile or distant sources, contested by Toch; never to be used in loc.

## 4. Design rules (what the mod must not do)

1. **No Jewish slave traders, slave owners, eunuch-makers or eunuch-traders.** This covers characters, events, modifiers, decision text, character flavour, artifact descriptions and loading tips.
2. **No Jewish financiers of wars or crusades** in event text (cf. Jacobs's Josce of Gloucester), and no moneylender-funds-the-war events targeting Jewish characters.
3. **The *Rescue the Daughters* CB must not target Jewish-faith holders.** Add `NOT = { religion = religion:judaism_religion }` (check the exact key) to the target or defender trigger. Alternatively, write a custom invalidation so that it never fires against `kabarism`/Khazaria or any Jewish courtier holding a prisoner.
4. **No Khazar seat, and no Khazar-origin story,** for the Jewish sect (already a hard rule).
5. **No revenge motive.** No loc line may give a Jewish character satisfaction at Christian or Muslim ruin, or hatred of Christians as a reason for action. Jewish characters' reactions to the trans faiths come from **halakha** (`jud_rabbinic_primary_texts.md`), not from enmity.
6. **No "Jews as conduit" for Saqaliba or Slavic captives** in any Dorleyite, Bædling or Jade Embryo content about captives or eunuch origins. If a captive's provenance must be named, use the general trade (Venetian, Frankish, Arab, Byzantine; El-Azhari p. 254 names Venetian merchants). Never name Jews.
7. **The narrator never repeats the *Jewish Encyclopedia* or Graetz claims** (Prague, Andalusia) as fact, even in footnotes or tooltips.
8. **Sect content stays inside the community.** The *Ha-Nehpakhot* chain deals with prayer, names, dress and the *kahal*'s response. It has no economic role.

## 5. Open question for the user

- Should the mod carry a **README line** that names Phelan and Toch and explains why the eunuch-trade material in the Byzantine and Islamic notes is never applied to Jewish characters? It would be transparent. It would also put the libel in front of players who would otherwise never meet it.
