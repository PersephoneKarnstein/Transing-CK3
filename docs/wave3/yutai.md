# Wave 3: Yutai Dao palace faction, stage 2 (`tm_yt2`), small version

Roadmap item: "Yutai Dao: a full palace faction against the scholar-officials". The user agreed to a small version first. Stage 1 (`tm_palace`: the offer, the censor's memorial, the 903 purge) is unchanged except for the hooks listed below. Not tested in game.

## What was built

**A standing tug-of-war value.** `tm_yt2_balance` runs from −3 to +3 and is kept on the throne's primary title (`top_liege.primary_title`), so it outlives an emperor. Above zero, the inner offices (the Northern Office) have the throne's ear. Below zero, the scholar-officials (the Southern Office) have it. Both names are the period's own: Meng Zhaotu in 881 (So 2000, p. 143). It exists only at celestial and meritocratic thrones with a daughter of the Way under them. It is created at 0 the first time a daughter is seen there.
- **Drift.** Once a year for each throne there is a 30% chance it moves one step toward 0. Office is the throne's to take back, and the officials' gains fade too.
- **Era bounds.** Before 960 the range is −3 to +3. From 960, under a celestial throne, the top is +2: Song eunuchs had no army of their own and rose and fell with their patrons (So 2000, pp. 577–579).
- **903.** The purge (`tm_palace.0003`, 903–904, celestial) sets the balance to −3.

**What the balance does.**
- **Offers** (`tm_palace.0001`): +3 to the yearly chance at +2 or more, −3 at −2 or less (base 5).
- **Memorials** (`tm_palace.0002`, the stage-1 event): fired again for a daughter in office when the court leans. At +2 or more the Southern Office answers the palace's gains (3%/year). At −1, −2 and −3 the officials press harder (6, 9 and 12%/year). Five-year cooldown per daughter, and the flavour budget applies. A memorial she weathers moves the balance +1. One she loses moves it −1.
- **Licences** (spent from the balance, below): a name-panel for one Sisters' House in the realm, and five years in which an adept under that throne can get past the month-3 clergy-roll inquiry (`tm_embryo.0010`, new option e).

**The decision `tm_yt2_work_offices_decision` "Work the Inner Offices"** is for a daughter of the Way who holds a palace seal and still meets `tm_palace_daughter_trigger`. Five-year cooldown; the AI checks every 60 months. It opens `tm_yt2.0001`, whose description shows which side has the throne's ear. The options:
- (a) **Tang, before 907, celestial: adopt grown followers across names**, as the Yang of the inner offices did. 50 gold, +25 prestige, balance +1. Source: Yang Fugong's fictive sons, governors and prefects, and his 600 eunuch sons as army supervisors (So 2000, pp. 152–153). The adoption is abstract: no characters are created.
- (b) **Song, from 971, celestial: register an adopted heir with the Court of Imperial Ceremonies.** 100 prestige, balance +1. From 1053 there is a 25% chance that the quota is full and nothing is gained. Sources: the 971 register and certificate, with death for a secret adoption (So 2000, p. 200); the quota of 180 in 1053 (p. 345).
- (c) **867–903, celestial: win over a commander of the Shence armies.** 100 gold, balance +2, and a 30% chance the throne hears of it (suspicion −15). Source: the commanders, not the commissioners, chose emperors (So 2000, p. 139).
- (d) **Any throne: sit in the ministers' audiences.** "Inner and outer officials are one body" (Du Cong under Yizong, So 2000, p. 138). +15 prestige, and for five years no memorials come to her (`tm_yt2_one_body`). The balance does not move.
- (e) **Spend on licences** (balance ≥ 1). Balance −1, +25 piety. One unnamed Sisters' House in the throne's realm, not her own, gets `tm_house_named`. The throne's title gets `tm_yt2_licences` for 5 years. Her own Houses stay stripped, as stage 1 decided: office costs the holder's name-panels. Sources: eunuch Commissioners of Merit oversaw both clergies (Rideout 1949, p. 56; Rideout's dating is loose, and the office is usually dated to the 780s); a name-panel guarded a house from confiscation (Gernet 1995, p. 43).
- (f) Not this year.

**`tm_yt2.0002` "The Clerk of Ceremonies"** (Song, from 971, celestial). A daughter of the Way who keeps a House is visited by a clerk of the Court of Imperial Ceremonies. He asks whether the society's adopted daughters are eunuchs' adoptees who need a certificate (So 2000, p. 200; So design row 10). The hostile voice is the clerk's. Options:
- Answer with the rectified names: a roll with learning ×2 for +25 piety, or −25 prestige and House strain +1.
- A friend in the inner offices files the question away (balance ≥ 1, spends 1).
- Buy the certificate and let him write what he likes: 50 gold, −25 piety.

Chance 2% a year, 20-year cooldown, flavour budget.

**`tm_yt2.0003` "The Censor's Brush"** is built for the earlier run in which a Yutai held the imperial Censor office. The throne keeps a ministry (`tgp_has_access_to_ministry_trigger`), and the holder of `title:e_minister_censor` is of the Way. While that is so, the Southern Office's memorials against her sisters (above) stop: they cannot pass her desk. Instead, with a chance of 10% a year per daughter in office (5-year cooldown on the daughter, 10-year cooldown on the Censor, and the Censor's flavour budget), the Censor gets the memorial that names her sister. In the record the censors were the eunuchs' opponents (Rideout 1953, pp. 47–48; So 2000, p. 139), so she sits on the other side of the court from her sister. Options:
- Send it up: +50 prestige, −25 piety, balance −1. The sister loses her seal and −30 opinion.
- Let it lie on her desk: balance +1, sister +20 opinion. 30% chance a minister asks after it: −50 prestige and the throne −15.
- Write to her sister first: the sister gives back the seal. Both get +25 piety, and the sister +10 opinion.

## Why not a vanilla faction
`common/factions/_factions.info` and the vanilla and TGP factions are war machines among vassals: a demand, an ultimatum, a casus belli, leaders. Many daughters in office are courtiers, not vassals. The fight in the sources is about offices, access and licences, not a war against the throne. A variable, a decision and three events are smaller, and they cannot break succession or start civil wars. The balance is per throne, so it fits the run's picture: 59 Yutai rulers, mostly under celestial government.

## Date gates
- Tang-only levers (Shence commander) end at 903. Tang adoption ends at 907.
- Nothing for 907–960: So skips the Five Dynasties.
- Song levers from 971 (register) and 1053 (quota). The +2 cap from 960.
- **Liao, the Ming, and meritocratic thrones in general get no period-specific levers.** No study of Liao or Jin eunuchs was found (china_reading_list.md, "Gap"). Grass's Ming Directorate of Imperial Horses ("Seal the Ledgers", 1403–1449) is a candidate for later. Meritocratic thrones (Korea, Dai Viet, Khitan, Xia) get only options (d) and (e).

## Files
- New: `common/scripted_effects/tm_yt2_effects.txt`, `common/scripted_triggers/tm_yt2_triggers.txt`, `common/decisions/tm_yt2_decisions.txt`, `events/tm_yt2_events.txt`, `localization/english/tm_yt2_l_english.yml` (it also holds the new key `tm_embryo.0010.e`).
- Changed:
  - `common/on_action/tm_palace_on_actions.txt`: calls `tm_yt2_yearly_effect`, which saves `scope:tm_palace_seat`; the purge sets −3; the offer chance has modifiers.
  - `events/tm_palace_events.txt`: 0002 option (a) moves the balance.
  - `events/tm_embryo_events.txt`: 0010 has a new option (e).

## Uncertain syntax
- `tm_yt2_north_effect = { AMOUNT = n }` with `change_variable = { add = $AMOUNT$ }`. ck3-tiger accepts it.
- `title:e_minister_censor.holder ?= { ... }` in a trigger when the title has no holder.
- `random_realm_county` from the throne is "based on top liege". It should cover the whole realm, the throne's own counties included.
- Saved scopes (`tm_palace_daughter`, `tm_palace_throne`, `tm_palace_seat`) carried into events fired from the yearly pulse with a delay.

## Test scenarios (TO-TEST style, for §J or a new section)
- **The inner offices at work.** As a daughter of the Way under the Tang emperor, fire `tm_palace.0001` and take the seal. The decision *Work the Inner Offices* should appear. Before 903 options (a) and (c) show; (e) is hidden until the balance is 1 or more. Check the balance with `h_china`'s variables (or the throne's primary title) in the console: (a) +1, (c) +2. Then (e): one other Sisters' House in the realm gains `tm_house_named`; her own does not.
- **Song levers.** Set the date to 1060 under the Song: (b) shows, (a) and (c) do not, and the balance cannot pass +2.
- **Memorials by balance.** Set the throne title's `tm_yt2_balance` to −3 and advance a few years: `tm_palace.0002` should return about once per decade at most for a daughter in office, and not within five years of option (d).
- **The Censor's Brush.** Make a member of the Way the Censor of the celestial ministry (appoint her spymaster), with a different daughter in office. No memorials should fire. Within some years `tm_yt2.0003` fires to the Censor. Check that each option's office loss and opinion changes reach the sister.
- **The clerk.** After 971, under a celestial throne, a daughter of the Way who holds a House should rarely get `tm_yt2.0002`. Option (b) shows only at balance 1 or more.
- **903.** Hold the seal on 903.2.1: the purge fires, and the throne title's balance is −3.
- **Month 3.** With `tm_yt2_licences` on the top liege's primary title, `tm_embryo.0010` shows option (e).

## Ready-to-paste text

**README, Yutai Dao bullet (replace "The palace offices" bullet):**
- **The palace offices.** Under a celestial or meritocratic throne the eunuchs' side of the court may offer a daughter a post: power, at the cost of her Houses' name-panels, a censor's memorial, and the purge of 903. With the seal she can work the inner offices against the scholar-officials, the Northern Office against the Southern. She can adopt followers as the Tang eunuch houses did, register an heir under Song law, win a Shence commander before 903, sit with the ministers, or spend the palace's standing on name-panels and licences for the society. When the scholar-officials have the throne's ear, their memorials come faster. A censor of the Way may hold them on her desk, or send them up.

**README, "The world" bullet:** replace "A planned palace faction will contend with the scholar-officials." with "A palace faction contends with the scholar-officials."

**README Roadmap:** change "- [ ] Yutai Dao: a full palace faction against the scholar-officials" to "- [x] Yutai Dao: a palace faction against the scholar-officials (small version; Liao and Ming levers not built)".

**TODO, under "Stage 2, first pass" or a new wave-3 heading:**
- [ ] Yutai palace faction (`tm_yt2`): the balance on the throne's title, *Work the Inner Offices*, the Clerk of Ceremonies (971+), the Censor's Brush, the licences option at month 3. Not built: Liao and Ming levers ("Seal the Ledgers", Grass 2024), Cui Yin's 902 proposal (So row 9), the Boy from Min (Rideout row 3), the Commissioner of Merit's repair levy (Rideout row 6).

**TODO, "Stage 2 inputs from the China reading":** tick the palace-faction line when tested.

## Decisions (user, 2026-10-21)

- **The Censor's Brush is celestial only.** It needs the throne's ministry, which only the celestial emperor keeps; meritocratic thrones never see it.
- The small version stands for now (README roadmap: built, small version; Liao and Ming levers not built).
