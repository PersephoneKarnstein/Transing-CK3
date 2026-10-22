# Wave 5: the faith's voice is a daughter's (succession and the Elder Sister)

The user, after the run-5 review: "we're building *trans-women religions*, not just trans-affirming ones that provide
transition care." The faiths' own offices should belong to trans women. Cis women stay members and sisters.

## What the run showed (867 start, saves at 1104, 1117 and 1197)
- No ruler of the six faiths ever passed **The Sisters Choose** (`tm_sisters_elective_succession_law`): the law had
  no AI weight, and vanilla AI does not weigh title laws (no vanilla title succession law has `ai_will_do`).
  Mālai grew to 208 rulers through royal houses whose kings were mostly men.
- 17 of the 23 Mothers of Mothers were cis women; none of the last 17 was a daughter.
- The Elder Sister: three named by learning and diplomacy, a daughter +5, then a uniform lot.

## Built
1. **The Sisters Choose taken up by AI rulers.** `common/on_action/tm_succ_on_actions.txt` (yearly_playable_pulse):
   an AI ruler of the six faiths, feudal, clan or tribal, duke or above, not at war, whose primary title follows no
   law of its own (no elective law, nor the head of faith's, a noble family's, the land's, or the celestial
   ministries'), and who has a daughter of her faith among the law's candidates (her child, born or taken, a
   councillor or a vassal), takes the law: 10% a year, 20% if she is a daughter herself, at the law's prestige cost
   (`add_title_law_effects`). Triggers in `common/scripted_triggers/tm_succ_triggers.txt`. The law also gets an
   `ai_will_do` (10 with a daughter candidate) in case the AI does weigh it.
2. **Marked sisters on the council are candidates.** `tm_sisters_elective.txt`: the council set admits
   `has_trait = tm_transgender` (coded male before her gate). They already had the +40.
3. **The Elder Sister is a daughter when one is eligible.** `events/tm_house_events.txt` tm_house.0010: daughters
   and Marked sisters rank +100 among the nominees, and the lot falls among the daughters and Marked sisters named;
   cis sisters stand only when none is eligible.

## Not changed
- Ordinary inheritance: vanilla family succession stays as it is. The law is an option the realm takes.
- A player ruler is never given the law; she can pass it herself.

## Test scenarios
- **S1. AI takes the law.** New 867 game, observe. Use the console to give an AI Bædling or Mālai duke a
  daughter of her faith as courtier and adopt her (Take as Daughter), or make one her councillor. Within about ten
  years her primary title should show The Sisters Choose (title laws tab), and her prestige should drop by the law's
  cost. Check a king of an elective realm (the Holy Roman Empire, or Scandinavia after its elective decision) is
  never changed.
- **S2. No daughter, no law.** An AI ruler of the faiths with no daughter among the candidates never takes it.
- **S3. Marked councillor.** Appoint a Marked courtier of the faith to the council of a ruler under the law: she
  should appear among the candidates in the succession window.
- **S4. Elder Sister.** A House with one daughter, one Marked sister and three learned cis sisters at court: at the
  next choice (every five years, or `trigger_event tm_house.0010` on the holder with the county saved) the new Elder
  Sister is the daughter or the Marked sister. With no daughter or Marked sister eligible, a cis sister is chosen.

## README text (Shared mechanics), to replace the two bullets
- **The Sisters Choose.** An elective succession law: the ruler, the faith's clergy and its vassals choose an heir
  from among the ruler's born and adopted children, the women and Marked sisters of the faith on the council, and the
  faithful vassals; a daughter or Marked sister weighs most. AI rulers of the faiths take it up when a daughter
  stands among those candidates.
- **Sisters' Houses** (sentence change): "Each House chooses its own Elder Sister every five years, a daughter or
  Marked sister when one is eligible, ..."
