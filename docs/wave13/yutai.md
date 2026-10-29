# Yutai Dao, wave 13: the levers, the women's chains and regency rules (`tm_yt4`)

Roadmap items (`docs/TODO.md`, China reading): "Event chains: Xue Xuantong (874–883), Wang Fengxian (d. 886), the abbess of Mo-shan; three routes into the abbeys; Liao Empress Chengtian", "Regency rules by culture (Song curtain; Liao/Yuan command)", and the wave 3 levers left unbuilt (`docs/wave3/yutai.md`, "Date gates"). Built 2026-10-28, not tested in game. ck3-tiger: 23 reports, the same 23 as before; none in the new files.

It builds on the palace faction of wave 3 (`tm_yt2`: the balance on the throne's title, the seal, the Censor), stage 1 (`tm_palace`: the offer, the memorial, the purge of 903) and the Sisters' Houses (`tm_house`, `tm_house_named`, `tm_house_strain`).

## Files

New, each with a BOM:
- `events/tm_yt4_events.txt`
- `common/on_action/tm_yt4_on_actions.txt`
- `common/scripted_effects/tm_yt4_effects.txt`
- `common/scripted_triggers/tm_yt4_triggers.txt`
- `common/modifiers/tm_yt4_modifiers.txt`
- `localization/english/tm_yt4_l_english.yml`

Changed, one line: `common/scripted_effects/tm_yt2_effects.txt`, in `tm_yt2_yearly_effect`, calls `tm_yt4_palace_year_effect = yes` before the wave 4 block. That is how the palace levers reach a daughter of the Way under a celestial or meritocratic throne with the saved scopes `tm_palace_throne` and `tm_palace_seat`, without a second loop over every character.

## Rules kept

- **No historical figure is claimed by the narrator.** Cui Yin, Lady Xue (Xue Xuantong), Wang Fengxian, the abbess Liaoran and the Empress Chengtian are people a daughter of the Way reads with, hears, meets or is compared with. None is of the Way, and no text says any of them was trans. Every answer a daughter gives is about herself: "to be born as myself" (Lady Xue), "the register decides whether I am a woman" (Wang Fengxian), "I have one, and I chose it" (Mo-shan), "Mine made me myself" (Chengtian).
- **Eunuchs are men unless they say otherwise**, as in `tm_yt2` and the Rideout note §1.7. The boy from Min is a boy; what he becomes "is his own to say".
- **Nothing violent on screen.** Cui Yin's plan is reported as a memorial. The killing at Yangzhou in 887 is reported as the court's account. What was done to the tribute boy is in the past and never described: the event names the tribute and a song about a father and a son. No suicide content: Lady Xue's elixir is left out, and her household's account is told as they would tell it. The Liao captive boys of 986 are not used at all.
- **No third gender in the narrator's voice.** The abbess's "neither male nor female in form" is her words about the Chan mind, in quotation; the daughter's answer separates herself from it.
- **No pain test, stepping back honoured.** Every event has a quiet way out that costs nothing or lowers stress, and in the regency's end, stepping down first is rewarded as well as the emperor's robes.
- **Hostile voices are named.** The monk at Mo-shan, the husband at Hezhong (reported), the ministers with "the hen does not announce the dawn", the court's men who call Wang Fengxian a sorceress.
- **Growth.** No caps and no persecution mechanic. Three events add a character to a House's court (the boy, a woman by one of the three routes); each keeps her own faith.

## 1. The levers

### 1a. Cui Yin's proposal (0001), 901–902
**Source.** In 901 the chief minister Cui Yin asked to give the Shence armies to ministers; the generals refused, "we have never heard of a scholar commanding an army". He then asked the throne "to kill all eunuchs and let palace women run the inner offices", and the inner offices answered by placing literate women around the emperor as informers (So 2000, pp. 160–161; So note, design row 9). The purge followed in the first month of 903 (p. 161).

**What the player sees.** A daughter of the Way under a celestial throne, 901.1.1 to 902.12.31, once (40% a year from the palace pulse, flavour budget). Two desc variants: with a seal in the inner offices, or without.
- *Keep a seal for the palace women*: +50 prestige, *A Seal for the Palace Women* (+2 stewardship, +0.2 prestige a month, 5 years), the balance −1 (the Southern Office gains). A daughter who held the inner offices' seal gives it back, so the purge of 903 does not find her in office.
- *I will not keep a seal that is paid for with their lives*: +50 piety, −10 stress.
- *Sit by the throne and listen, as the inner offices ask* (in office only): *At the Throne's Side* (+2 intrigue, 5 years), balance +1; 30% the throne notices (suspicion −15).
- *This is the court's quarrel, not the society's*: −5 stress.

### 1b. The Boy from Min (0002), to 906
**Source.** By 846–859 every circuit paid a yearly tribute of boys, "known as Szu Pai", mostly from Lingnan and Min, "the eunuch nursery"; most were sold by their parents (Rideout 1949, p. 55 and n. 7). Liu Zongyuan, Han Yu and others redeemed slaves at their own cost (p. 55 n. 6). Gu Kuang's poem of a son of Min parting from his father (n. 7) is the "song of Min". Palace boys were brought up Buddhist (p. 56). Rideout design row 3: never assume what he is.

**What the player sees.** A ruler of the Way who keeps a House under a celestial throne (or on it), before 907, 3% a year, once per 25 years, flavour budget. A boy of about ten, left at the House's gate by the tribute escort, sick from the road. He is created with the vanilla eunuch trait, Buddhist, of the House county's culture. The text says nothing of what was done to him; it gives his mother's name, his village, the song, and a question about the kitchen garden.
- *He stays, as a son of the House, as he is*: he joins the court (+30 opinion), +25 piety. Tooltip: "The House takes him as he is. What he becomes is his own to say."
- *Buy back the rest of this year's boys* (100 gold): he stays, the others go home with tea merchants at the House's cost, +60 piety.
- *Send him home to Min* (25 gold): +20 piety.

### 1c. The Commissioner of Merit's levy (0003), to 906
**Source.** Eunuch Commissioners of Merit and Works (*gongde shi*) had "an almost complete official control" over both clergies and took commissions on enforced monastery repairs; such missions paid "never less than one thousand string of cash" (Rideout 1949, p. 56; 1953, pp. 46–47; design row 6). Gao Lishi founded a Daoist monastery (1949, p. 68 n. 13): a patron could also come from the palace. Rideout dates the control loosely to Xuanzong; the office is usually dated to the 780s, so 867–907 is inside it either way.

**What the player sees.** The same House keepers, before 907, 3% a year, once per 20 years, flavour budget.
- *Pay the levy* (50 gold): +10 prestige.
- *Put the House's goods in the burial society's store*: 60 (+2 × stewardship) the commissioner counts an empty hall, +25 piety; otherwise −50 prestige and House strain +1.
- *Ask a patron in the inner offices* (balance ≥ 1 at her throne): the balance −1, +10 prestige.

### 1d. Seal the Ledgers (0004), 1403–1449
**Source.** Grass 2024, the only source note for a Ming lever. The Directorate of Imperial Horses and its Braves "took orders only from their eunuch commanders and the emperor himself" (p. 14), outside the Ministry of War (p. 13). In 1444 its eunuchs were accused of seizing land and running "a temple and a kiln" on it; the emperor pardoned them, granted the land, and ordered a yearly inspection by a scrutiny official and a censor (p. 20). A revenue official: "the few became many, and the dead were made alive" (p. 21). Tumu, 1449 (p. 22). Grass design rows 1–2. A Sisters' House on the stables' land is design.

**What the player sees.** A daughter of the Way with a seal in the inner offices, under a celestial throne, 1403–1449, 5% a year, once per 20 years, flavour budget.
- *Put the House's land on the Directorate's books* (holds a House): her Houses get `tm_house_named`. 70%: the ministries never ask, balance +1. 30%: the 1444 pattern, pardon and grant with a censor's inspection: still named, −50 prestige, balance −1.
- *Draw on the stables' grain*: +100 gold; 25% a revenue official counts (−50 prestige).
- *Open the ledgers to the ministries*: +25 prestige, +25 piety, balance −1.
- *Not this year.*

Note: stage 1 strips the name-panels of a daughter who takes office. This option is a back door to them in the one window the source supports. Decide whether that is too generous (open decision 1).

## 2. The women's chains

### 2a. Lady Xue at Hezhong (0010, 0011), 874–885
**Source.** Xue Xuantong (c. 828–882), wife of Feng Hui, Lesser Governor of Hezhong. After twenty years of marriage she lived chastely and "used illness as her pretext for dwelling alone", chanting the *Huangting jing*; in 874 Lady Wei came down and taught her; her husband "regularly slandered and ridiculed her" (Cahill 2006, pp. 189–190; Cheng 2021, p. 135). In 881 she sent a divine escort away: "Not yet! I will only depart next spring from my private residence. Don't rush me!" (p. 191). In 882 she washed her own hair and face, the rite female kin perform on a corpse; her coffin later held "her empty burial garments and quilt" (pp. 191–192). In 883 Governor Zhou Bao memorialised the court at Chengdu, whose rescript ordered the history officials to record her and money for "repairing Daoist altars" where she lived (p. 193). Cahill names the emperor Yizong; in 883 it was Xizong (her own p. 12). The text names no emperor. Cahill design row 13 ("The Woman at Hezhong").

**What the player sees.**
- **0010 "A Letter from Hezhong"** (874–881; a daughter of the Way under a celestial throne; 6% a year, once, flavour budget). The letter is design: her household asks a woman of the Way to read the Yellow Court scripture with her for a winter; her husband's mocking line is at the bottom.
  - *Go to Hezhong. If she asks why I came to the Way, I will tell her: to be born as myself*: *A Winter of the Yellow Court* (+1 learning, +0.2 piety a month, 10 years), +20 piety.
  - *Send a copy in my own hand*: +10 piety, −10 stress.
  - *I will not come between them*: nothing.
- **0011 "Her Burial Garments"** (882–885; only after either of the first two answers; 50% a year, no flavour budget, as a chain under way). Her household's account: the escort sent away, the washing, the empty coffin, the rescript.
  - *Gold for her altars, and a sister to keep them* (25 gold): +40 piety.
  - *Write down our winter of reading for the history officials*: +30 prestige, +200 learning experience.
  - *Keep what she said: Not yet. Don't rush me*: −15 stress.

The elixir she took before her death is left out under the no-suicide rule.

### 2b. Wang Fengxian (0020, 0021), to 900
**Source.** Cahill 2006, pp. 180–185: a weavers' daughter of Dangtu whose hair, cut to the neck in girlhood, never grew back; people called her Guanyin; to an official, the common folk "flatter me with the name of Guanyin"; Du's comment, "there is no obstacle between names and the Way", and the ox and the horse; the governor Du Shenquan meant to send her "as tribute for the consorts' apartments", and she used "the excuse of having short hair" and hid in a Buddhist temple for years; from 860 to 888 she preached in Huai and Zhe, and warlords with "white swords" knelt as disciples. Cahill design row 7 (the debate with Rectified Names). Jia 2018, pp. 201–203: in the histories she is a "sorceress" and "evil nun" who in Yangzhou in 887 told the rebel generals "a great man must die", after which Gao Pian and his kin were killed and "all rewards and punishments … were decided by her"; Du rewrote her as a saint who died on Mount Qianqing in 886. Jia design row 18: the faith does not claim her.

**What the player sees.**
- **0020 "The Preacher of Dangtu"** (to 885; 4% a year, once, flavour budget). She asks a sister of the Way what she makes of "no obstacle between names and the Way".
  - *"For you a name is no obstacle. For me the register decides whether I am a woman, so I keep mine right."*: +30 piety.
  - *Ask how she kept out of the consorts' apartments*: the short hair and the temple (tooltip), +200 intrigue experience, +10 prestige.
  - *Listen to the end, and go home*: −10 stress.
- **0021 "Two Accounts"** (887–900, after 0020; 30% a year, a chain). The disciples' account (transformed on Mount Qianqing without falling ill, at 48) and the court's (the oracle at Yangzhou a year later). The House keeps a book of women met on the roads; she was never one of its own.
  - *Her disciples' account*: +20 piety. *The court's account, and who gives it*: +20 prestige. *Both, and we do not know*: +300 learning experience.

Du's book is of c. 913, so before then the saint's account is her disciples' word, and the event says so.

### 2c. Half a ladle at Mo-shan (0025), to 895
**Source.** Levering 1982, pp. 27–29: the abbess Moshan Liaoran and the monk Guanxi Zhixian, who came to overturn her platform ("Why didn't you cover it?"; "(S)he has neither male nor female form"; "Why doesn't she transform herself?"; "She is not a spirit, nor a ghost. What would you have her become?"). He served three years as her gardener and spoke of "another half-ladle" from Mo-shan (p. 28). The nun before Tankong: "Even if I were to change, I would still be a fox spirit!" (p. 25). Levering design rows 2, 3, 6: use Mo-shan only for her refusal to perform proof; the Way's doctrine stays "born as herself". The dates (Zhixian d. 895; Liaoran active 860s–880s) are standard reference dates the note marks unverified.

**What the player sees.** A daughter of the Way under a celestial throne, to 895, 3% a year, once, flavour budget. She is among the abbess's guests when the exchange happens; then the monk turns to her: "Change your form for me, then, if you are what you say."
- *"If I changed for you, you would call me a fox."*: +25 prestige.
- *"Your teacher's mind has no form. I have one, and I chose it. I have nothing to prove to you."*: +30 piety.
- *Say nothing. Bow to the abbess, not to him*: −10 stress.

All three: *Half a Ladle at Mo-shan* (+2 learning, −5% stress gain, 10 years).

### 2d. The three routes into the abbeys (0030–0032)
**Source.** McMahon design row 6, three paths matching three pressures:
1. **Registered in the guan to be taken later** (0030): Xuanzong had his son's wife "registered as a Daoist nun in 741" and took her into the harem in 745 (WSNR 217; Despeux and Kohn 2003, p. 123). The note's line: "The guan is not your anteroom. She came here to stay."
2. **A consort set aside** (0031): sonless consorts "placed in a nunnery" after Taizong's death (WSNR 188); in 1429 Empress Hu was made to step down with the title "Tranquil and Loving Master of Immortality" (CW 91); aging palace women released into convents, "half of them used to be singers and dancers in the palace" (Jia 2018, p. 31; Jia design row 10: mutual aid, not pity).
3. **Refuge from the levirate** (0032): the Jurchen mother of Jin Shizong "avoided marriage to her husband's younger brother by shaving her head and becoming a nun", a choice that "became common among widows" (CW 44); Sorghaghtani refused the levirate and asked for her own domain (CW 62).

**What the player sees.** A ruler of the Way who keeps a House and has a lord above her, under a celestial or meritocratic throne; 4% a year, once per 15 years, flavour budget. Routes 1 and 2 are equally likely; route 3 only where her capital county is of a Mongolic-heritage (Khitan, Mongol) or Jurchen culture, and then it is as likely as the other two together. A woman is created (from the House county's people, or the capital county's for route 3), keeping her own faith.
- **0030 "Not Your Anteroom"** (17–26): her lord's letter asks the House to register a young woman until he sends for her. *Register her, and the guan is no one's anteroom* (she joins the court, +25 opinion; the lord −15; +20 piety); *Register her as he asks, and send her on* (she goes to the lord's court, lord +15, −20 piety); *Refuse to register her for him* (she goes home, lord −10, +10 piety).
- **0031 "A Consort Set Aside"** (35–55; a Ming variant from 1368 with the Daoist title): *a room and the House's work, as any sister has* (joins the court, House strain +1, +25 piety); *the best room, and her own counsel* (25 gold; joins, lord +10, +20 prestige); *the House cannot feed another; write to a House that can* (−10 piety).
- **0032 "His Horses, Not Me"** (24–40): *take her vows at the House* (joins the court, +30 piety, −15 prestige); *write for her: a household of her own* (+20 prestige); *the House cannot stand against her husband's clan* (−15 piety).

### 2e. The Empress Chengtian (0035), 982–1009
**Source.** McMahon WSNR 260–262 and 272; CW 9. Chengtian (954–1009), regent from 982 for her son; Jingzong's edict let her use the imperial "I" (*zhen*); she "performed a rite normally limited to emperors when assuming the throne, the ritual of rebirth (*zaisheng yi*)", in a special building the ruler entered "in order to be reborn"; she rode with the army that routed the Song in 986; Khitan regents used no curtain. McMahon design row 3: "Do not claim that Chengtian had any gender meaning", and verify the rite's details against Wittfogel and Feng before writing them in.

Checked 2026-10-28 against Wittfogel and Feng 1949 and *Liaoshi* 53 (note: `docs/research/cn_wittfogel_feng_liao.md`). They confirm McMahon: the rebirth was "normally reserved for the emperor alone", and Chengtian obtained it in 984 and twice in 986, the year of the campaign against the Song (pp. 202–203). The rite itself (*Liaoshi* 53, trans. pp. 273–274) gives the details now in the text: every twelve years, a building beside one for the emperor's mother, three forked timbers, a midwife, swaddling clothes, a new name chosen from seven. **Left out on purpose:** the old man's closing cry, "A boy is born". Neither source says what was cried for her, and with it the event would hand her rite the gender meaning McMahon warns against.

**What the player sees.** A daughter of the Way whose top liege is of Khitan culture, 982–1009, 8% a year, once, flavour budget. From 987 the desc adds 986: reborn twice, and the ride against the Song. A Khitan officer asks whether the Way's rebirth is the same rite as hers.
- *"Hers made her a ruler. Mine made me myself, and I needed no throne for it."*: +30 prestige.
- *Ask him how the rite is kept*: +300 learning experience; he tells what an officer may (the twelve years, the timbers, the midwife, the new name).
- *Say nothing. It is her day, not mine*: −10 stress.

## 3. Regency rules by culture

**Source.** McMahon design row 1 (and rows 2, 14). The Song made the curtain law for Empress Liu (regent 1022–1033): rule labelled "temporary", court every five days, never alone, the boy beside her "behind a curtained divide", no imperial "I" (CW 11–12); earlier curtains: Chu Suanzi (WSNR 147), Wu (WSNR 190). Khitan and Mongol women regents "did not use a curtain" (WSNR 272; CW 59); Chengtian had the "I" and the army (WSNR 261). Mongol custom: the widow took over the household (CW 62). The Jin had no women regents (CW 43–45). The Ming founder ruled that women "were never to involve themselves in politics" (CW 78), and Dowager Zhang refused the curtain as against the ancestral mandate and ruled informally (CW 93).

**Vanilla mechanics used.** Regencies in 1.20 are diarchies (`common/diarchies/diarchy_types/00_regencies.txt`: `temporary_regency` and `regency`, both with the hidden parameter `diarchy_is_regency`). The mod appends to vanilla's `on_entered_diarchy`, `on_diarch_change` and `on_left_diarchy` (`common/on_action/diarchy_on_action.txt`) and reads `has_active_diarchy`, `has_diarchy_active_parameter = diarchy_is_regency` and `diarch`. No diarchy type, mandate or interaction is overridden.

**Who.** Only regencies that concern the Way: the regent or the ruler is of Yutai Dao. The regent must be a woman who is the ruler's mother, a grandmother, or a wife (or former wife) of his father, the "dowager" of the sources. Other Chinese courts are untouched.

**The three rules** (a character modifier on the regent while the regency lasts):

| Ruler's court | Modifier | Effect |
|---|---|---|
| Mongolic heritage (Khitan, Mongol and the rest) | *Face to Face* | +2 martial, +1 diplomacy, +0.3 prestige a month |
| Celestial government or Chinese heritage, before 1368 | *Behind the Curtain* | +1 diplomacy, +1 stewardship, −2 martial ("she does not take the field"), +0.2 prestige a month |
| The same, from 1368 | *Without the Curtain* | +2 intrigue, +1 diplomacy |
| Anything else (Jurchen included, Korea, Dai Viet) | none | — |

When a curtain regency ends with both alive, **0041 "The Curtain Comes Down"** goes to the former regent. The ministers' line is "the hen does not announce the dawn" (WSNR 15–16), and a minister once took the curtain down without asking (Han Qi, 1065; CW 16).
- *Take it down myself, before they ask*: +25 piety, +25 prestige, −20 stress, the ruler +20 opinion.
- *One rite first, in the emperor's robes, at the ancestral temple* (Empress Liu, 1033; CW 13): +100 prestige, the ruler −15 opinion.
- *Let the minister take it down. That is his part*: +10 prestige, −10 stress.

Not built from row 1: blocking army command outright (no modifier does it; the martial malus stands in), the legitimacy and scholar-official opinion terms, and the "refuse to step down" event (a regency's end is the engine's; the mod does not extend one).

## 4. Numbers in one place

| Event | Who | Window | Chance a year | Cooldown | Budget |
|---|---|---|---|---|---|
| 0001 | daughter of the Way, celestial throne | 901–902 | 40% | once | yes |
| 0002 | House keeper, celestial | to 906 | 3% | 25 years | yes |
| 0003 | House keeper, celestial | to 906 | 3% | 20 years | yes |
| 0004 | daughter in office, celestial | 1403–1449 | 5% | 20 years | yes |
| 0010 | daughter of the Way, celestial | 874–881 | 6% | once | yes |
| 0011 | after 0010 a/b | 882–885 | 50% | once | no (chain) |
| 0020 | daughter of the Way, celestial | to 885 | 4% | once | yes |
| 0021 | after 0020 | 887–900 | 30% | once | no (chain) |
| 0025 | daughter of the Way, celestial | to 895 | 3% | once | yes |
| 0030–0032 | House keeper under a lord | any | 4% | 15 years | yes |
| 0035 | daughter at a Khitan court | 982–1009 | 8% | once | yes |
| 0041 | former curtain regent | on regency's end | — | — | no |

"Daughter of the Way" here is `tm_world_daughter_trigger` (a daughter of any gate, or a declared sister) of faith `tm_yutai`. Courtiers are reached from their ruler's `yearly_playable_pulse`, as wave 11 does.

## 5. Not built, and why

- **Liao and Jin levers for the palace faction.** No study of Liao or Jin eunuchs was found (`china_reading_list.md`, "Gap"; So 2000 has nothing on them). McMahon's Liao material is about empresses, not eunuch offices. Chengtian's order to castrate about a hundred captured boys (WSNR 261–262) is in the note but is not a lever, and it is not used in any form.
- **A Yuan lever.** No source note on Yuan eunuch offices.
- **Five Dynasties (907–960).** So skips them; nothing new.
- **Rideout's other levers** (Control the Channel, Counterweight, Army Supervisor, Impeach the Beardless; design row 5): not asked for in this wave.
- **The Song "Which Platform?" and the Ming *nüguan* pun** (Cheng row 6; McMahon row 7): not asked for.
- **Swords of the Women's Bureau** (Dowager Zhang and Wang Zhen, CW 94–95; McMahon row 11): it would put a sword to a man's throat on screen. Not built.
- **The Severed Hand (926), Chengtian Rides (986) as events, Three Courts of Women** (McMahon rows 4, 12): Chengtian appears only as 0035, and the 986 ride only in its text.
- **Tumu (1449) as an event** (Grass row 4): the window of 0004 ends there; nothing fires at Tumu.
- **The Liao boys of 986 and the Southern Han castration-for-office rumour as month-3 variants** (McMahon row 5): not built. They would bring the cutting of captives into the gate's text.
- **Zu Shu, Cao Wenyi, Sun Bu'er and the Yuan abbesses** (Despeux and Kohn row 13): not in this wave's list.

## 6. Open decisions for the user

**User, 2026-10-28:** questions 1–6 accepted as built; question 7 resolved from the sources (below).

1. **Seal the Ledgers as a back door to name-panels.** Option (a) of 0004 names her Houses although she holds office, which stage 1 says costs the name-panels. Keep, or make it a 20-year protection instead of `tm_house_named`?
2. **The boy's eunuch trait.** The tribute boy is created with the vanilla `eunuch_1` trait so that he is what the record says he was, with nothing described. If you would rather he carried no trait at all (leaving the past entirely to the text), it is one line.
3. **Cui Yin and the purge.** Taking the palace women's seal returns her inner-offices seal, so the purge of 903 (tm_palace.0003) passes her by. That reads as "she chose the winning side". Acceptable?
4. **Regencies of the Way only.** The rules touch only regencies where the regent or ruler is of the Way. Widening them to every Chinese and Khitan court would change vanilla China; I kept it narrow.
5. **Jurchen courts get no rule** (the Jin had no women regents, CW 43–45), but route 3 (the levirate refuge) does fire in Jurchen counties, after the Jin widow of CW 44. Agree?
6. **Mo-shan's dates** are reference dates the Levering note marks unverified (Linji d. 866/867, Zhixian d. 895). The event's window (to 895) depends on them.
7. ~~**Chengtian's rite.**~~ Resolved 2026-10-28: Wittfogel and Feng and *Liaoshi* 53 read; the event now gives the rite's details and the 984/986 dates, without the closing cry (§2e).

## Uncertain syntax (check in game)

- Appending `on_actions` to vanilla's `on_entered_diarchy`, `on_diarch_change` and `on_left_diarchy`; whether `scope:old_diarch` is set in all three cases, and whether `diarch` is filled when `on_entered_diarchy` fires.
- `any_former_spouse` on a dead father, to find his widow; `scope:tm_yt4_liege.father.mother ?= this` in a trigger.
- `has_diarchy_active_parameter = diarchy_is_regency` for both `temporary_regency` and `regency` (vanilla's death.txt reads it that way).
- `trait = eunuch_1` inside `create_character` for a child.
- `random_list` with a `trigger` on one entry (route 3).
- `top_liege.primary_title = { tm_yt2_spend_effect = yes }` from a House keeper who is herself the top liege.

## Ready to paste

### (a) `tools/census_report.py`, after the wave 12 block

```python
    # Yutai Dao, wave 13 (tm_yt4_tally_effect): the levers, the women's chains and the regency rules.
    print('== Yutai Dao: wave 13 ==')
    ysteps = ('cui_took', 'cui_refused', 'cui_listened', 'cui_aside', 'boy_kept', 'boy_ransomed', 'boy_home',
              'levy_paid', 'levy_hidden', 'levy_found', 'levy_patron', 'ledgers_sealed', 'ledgers_audited',
              'ledgers_grain', 'ledgers_opened', 'ledgers_declined', 'xue_read', 'xue_wrote', 'xue_declined',
              'xue_altar', 'xue_record', 'xue_kept', 'wang_names', 'wang_levy', 'wang_listened', 'wang_saint',
              'wang_oracle', 'wang_both', 'moshan_fox', 'moshan_form', 'moshan_bowed', 'anteroom_kept',
              'anteroom_complied', 'anteroom_refused', 'consort_kept', 'consort_honoured', 'consort_sent',
              'widow_vows', 'widow_household', 'widow_refused', 'chengtian_answered', 'chengtian_asked',
              'chengtian_silent', 'regent_face', 'regent_curtain', 'regent_no_curtain', 'curtain_stepped',
              'curtain_robes', 'curtain_minister')
    print('  '.join(f'{s} {int(gvars.get(f"tm_yt4_n_{s}") or 0)}' for s in ysteps))
    print('cui_*: Cui Yin\'s memorial, 901-902 (took the palace women\'s seal, refused, listened for the inner offices,\n'
          'stood aside); boy_*: a tribute boy at the House gate before 907 (kept, the year\'s boys ransomed, sent home);\n'
          'levy_*: the Commissioner of Merit\'s repair levy (paid, hidden in the society store or found, a palace patron);\n'
          'ledgers_*: Seal the Ledgers, 1403-1449; xue_*: Lady Xue at Hezhong 874-881 and the news of 882-885; wang_*:\n'
          'Wang Fengxian heard, and which account the House wrote; moshan_*: the answer at Mo-shan; anteroom_* / consort_* /\n'
          'widow_*: the three routes into the abbeys; chengtian_*: the hut of rebirth, 982-1009; regent_*: Way regencies\n'
          'by rule (face to face, curtain, without the curtain); curtain_*: how a curtain regency ended.')
    print()
```

### (b) `docs/TO-TEST.md`

`## AP. Yutai Dao, wave 13: the levers, the women's chains and regency rules (added 2026-10-28, untested in-game; docs/wave13/yutai.md)`

- [ ] **AP1. Cui Yin's memorial.** 901, a daughter of the Way under the Tang emperor: fire tm_yt4.0001 with `scope:tm_palace_throne` and `scope:tm_palace_seat` (or wait for the palace pulse). With a seal: option c shows, and option a removes `tm_palace_office`; then on 903.2.1 the purge (tm_palace.0003) does not fire for her. Without a seal: c is hidden. Check the balance on the throne's title: a −1, c +1.
- [ ] **AP2. The Boy from Min.** Before 907, a ruler of the Way with a House under a celestial throne: fire 0002 with `scope:tm_yt4_house_county`. A boy of 9–12, Mahayana, with the eunuch trait, appears; a and b add him to the court, b only with 100 gold; c leaves him in the pool. The text never describes what was done to him.
- [ ] **AP3. The Commissioner's levy.** Same ruler: fire 0003; option c only with the balance ≥ 1 at her throne (and it spends 1); option b's failure raises `tm_house_strain` on the House county.
- [ ] **AP4. Seal the Ledgers.** 1420, a daughter in office under a celestial throne who holds a House: fire 0004 with the palace scopes; option a sets `tm_house_named` on her House counties in both outcomes; without a House, option a is hidden and the no-House desc shows. Not offered before 1403 or from 1450.
- [ ] **AP5. Lady Xue.** 875, a daughter of the Way under the Tang: fire 0010; a gives *A Winter of the Yellow Court* and the flag `tm_yt4_xue_met`; c sets no flag. Set the date to 883 and advance: 0011 fires once (only with the flag). No elixir in the text; no emperor named.
- [ ] **AP6. Wang Fengxian.** 870: fire 0020 (option b's tooltip tells the short-hair story); then 888: 0021 fires for her once. The House never claims her.
- [ ] **AP7. Mo-shan.** 880: fire 0025; all three options give *Half a Ladle at Mo-shan*. The narrator never calls the daughter "neither"; only the abbess's quoted words do.
- [ ] **AP8. The three routes.** A count of the Way with a House, vassal of a celestial emperor: fire 0030 and 0031 (with `scope:tm_yt4_lord` and `scope:tm_yt4_house_county`): the woman joins the right court per option; 0031 shows the Ming desc from 1368. A House keeper whose capital is Khitan or Jurchen: 0032.
- [ ] **AP9. Chengtian.** 990, a daughter of the Way at a Khitan emperor's court: fire 0035; the 986 line shows from 987.
- [ ] **AP10. Regency rules.** A child ruler of the Way under a celestial government, whose mother is regent (console: start a regency): she gets *Behind the Curtain*; a Mongol or Khitan child ruler's mother gets *Face to Face*; after 1368 a Han ruler's mother gets *Without the Curtain*. A regent who is not his mother, grandmother or father's wife gets nothing. Change the regent: the modifier moves. End a curtain regency with both alive: the modifier goes and 0041 fires to her.
- [ ] **AP11. Observe run (867 → c. 1100, then a late run to 1453).** The census "Yutai Dao: wave 13": `xue_*`, `wang_*`, `moshan_*` above 0 in the early decades; `boy_*` and `levy_*` only before 907; `cui_*` only 901–902; `ledgers_*` only 1403–1449; `regent_*` whenever a Way regency happens. No error.log lines from tm_yt4.

### (c) `docs/TODO.md`

- Line 99, "Event chains: Xue Xuantong (874–883), Wang Fengxian (d. 886), the abbess of Mo-shan; three routes into the abbeys; Liao Empress Chengtian": change to `- [x] ... (built in wave 13, tm_yt4; tick when tested: docs/wave13/yutai.md)`.
- Line 100, "Regency rules by culture (Song curtain; Liao/Yuan command)": change to `- [x] Regency rules by culture: curtain, face to face, without the curtain after 1368, for regencies of the Way (wave 13, tm_yt4; untested)`.
- Under "Yutai Dao palace faction (added 2026-10-21)", replace the "Not built" sentence with: "Built in wave 13 (`tm_yt4`): Cui Yin's 902 proposal, the Boy from Min, the Commissioner of Merit's repair levy, and Grass's Ming 'Seal the Ledgers' (1403–1449). Still not built: Liao, Jin and Yuan levers (no source on their eunuchs)."
- New heading: `## Yutai Dao, wave 13 (added 2026-10-28, untested in-game; docs/wave13/yutai.md)` with:
  - [ ] Yutai wave 13 (`tm_yt4`): the levers (0001–0004), Lady Xue (0010–0011), Wang Fengxian (0020–0021), Mo-shan (0025), the three routes into the abbeys (0030–0032), Chengtian (0035), regency rules by culture and the curtain's end (0041)
  - [ ] Not built from wave 13's notes: Liao, Jin and Yuan levers; Swords of the Women's Bureau; the Severed Hand; Tumu; month-3 variants from the Liao boys or Southern Han; Rideout's other levers
  - [ ] Decide wave 13's open questions (docs/wave13/yutai.md §6)

### (d) README

**Yutai Dao section**, add after the paragraph ending "the danger of the purge of 903.":

> Its daughters meet the women of their century. A governor's wife at Hezhong, Lady Xue, who keeps a room of her own and the Yellow Court scripture, asks a sister to read with her through a winter; years later her household tells of an escort sent away with "Not yet! Don't rush me!" and a coffin that held only her garments. A preacher of Dangtu, Wang Fengxian, says there is no obstacle between names and the Way, and a daughter answers that for her the register decides. At Mo-shan a monk demands that a daughter change her form as proof, after the abbess has refused the same demand. At the Khitan court a regent is reborn in a ruler's rite, and an officer asks if the Way's birth is the same. Women come to the Houses by the old routes into the abbeys: registered to be taken later, set aside by the palace, or fleeing a husband's kinsman. The palace offers its own levers: Cui Yin's plan of 902 to give the inner offices to palace women, a tribute boy from Min left at the House's gate, a eunuch commissioner's repair levy, and in the early Ming the stables' sealed ledgers. When a woman of the Way rules as regent, her court's custom decides how: behind a curtain under the Song, face to face at Khitan and Mongol courts, and without the curtain under the Ming. None of these historical women is claimed by the narrator. (So 2000; Rideout 1949, 1953; Grass 2024; Du Guangting, trans. Cahill 2006; Jia 2018; Levering 1982; McMahon 2013, 2016)

**Roadmap**: change "- [ ] Yutai Dao: the Liao and Ming levers, Cui Yin's 902 proposal, the Boy from Min, the repair levy; the women's chains; regency rules by culture" to "- [x] Yutai Dao: Cui Yin's 902 proposal, the Boy from Min, the repair levy, the Ming ledgers; the women's chains; regency rules by culture (wave 13; Liao, Jin and Yuan levers not built)".

**Bibliography**: nothing new; every source is already listed (So, Rideout, Grass, Cahill, Jia, Levering, McMahon 2013 and 2016).
