---
id: ct:debiasing-training-games
type: Technique
title: Debiasing training games
aliases: [serious games for bias mitigation, game-based bias training, Sirius debiasing games]
domain: debiasing-and-metacognition
summary: >-
  Interactive "serious games" that teach people to recognise and reduce
  specific cognitive biases by having them make biased-prone judgments inside
  a story, then giving personalised feedback, explanation and practice; a
  single session has reduced biases such as the bias blind spot in
  laboratory tests for weeks afterwards.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:consider-the-opposite, ct:metacognition, ct:structured-analytic-techniques]
requires: []
relations:
  - {predicate: counteracts, object: ct:bias-blind-spot, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s2, confidence: medium}
  - {predicate: counteracts, object: ct:fundamental-attribution-error, source: s1, confidence: medium}
  - {predicate: counteracts, object: ct:anchoring-effect, source: s1, confidence: low}
  - {predicate: introducedBy, object: ct:carey-morewedge, source: s3, confidence: medium}
  - {predicate: demonstratedBy, object: ct:morewedge-2015-debiasing-training-experiments, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:sellier-2019-debiasing-transfer-field-study, source: s2, confidence: medium}
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Debiasing Decisions: Improved Decision Making With a Single Training Intervention"
    publisher: Policy Insights from the Behavioral and Brain Sciences 2(1) (Morewedge, Yoon, Scopelliti, Symborski, Korris & Kassam, 2015), City Research Online
    url: https://openaccess.city.ac.uk/id/eprint/12324/1/Debiasing_Decisions_PIBBS.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s2
    title: "Debiasing training transfers to improve decision making in the field"
    publisher: Psychological Science 30(9), 1371-1379 (Sellier, Scopelliti & Morewedge, 2019), City Research Online
    url: https://openaccess.city.ac.uk/id/eprint/22233/1/DebiasingTrainingTransfers_InPress.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s3
    title: "The Design and Development of Serious Games Using Iterative Evaluation"
    publisher: Games and Culture 12(3), 252-268 (Symborski, Barton, Quinn, Korris, Kassam & Morewedge, 2017), Crossref record
    url: https://api.crossref.org/works/10.1177%2F1555412016673262
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "Teaching Decision Making With Serious Games: An Independent Evaluation"
    publisher: Games and Culture 12(3), 233-251 (Rhodes, Kopecky, Bos, McKneely, Gertner, Zaromb, Perrone & Spitaletta, 2017), Crossref record
    url: https://api.crossref.org/works/10.1177%2F1555412016686642
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Retention and Transfer of Cognitive Bias Mitigation Interventions: A Systematic Literature Study"
    publisher: Frontiers in Psychology 12, 629354 (Korteling, Gerritsma & Toet, 2021), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8397507
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s6
    title: "The Assessment of Biases in Cognition (ABC): Development and Evaluation of an Assessment Instrument for the Measurement of Cognitive Bias"
    publisher: MITRE Technical Report MTR160163 (Gertner, Zaromb, Schneider, Roberts & Matthews, 2016)
    url: https://www.mitre.org/sites/default/files/publications/pr-16-0956-the-assessment-of-biases-in-cognition.pdf
    type: institutional
    accessed: 2026-11-04
created: 2026-11-04
---

# Debiasing training games

Debiasing training games are "serious games" built to teach people to notice and reduce particular cognitive biases. Instead of reading about a bias, the player makes judgments inside an interactive story where that bias is likely to show up, then gets an after-action review that names the bias, explains it, shows the player's own biased answers and offers practice with feedback.[^s1][^s3] The best-studied examples cut measured bias, including the bias blind spot, after a single session of roughly an hour.[^s1]

## Origin

The approach grew out of the Sirius program of the US Intelligence Advanced Research Projects Activity (IARPA), which asked teams to build training that would reduce six biases thought to harm intelligence analysis: confirmation bias, fundamental attribution error, the bias blind spot, anchoring, representativeness and social projection.[^s1][^s6] One team, including the psychologist Carey Morewedge and the game developer Carl Symborski, designed the *Missing* games around bias-mitigation theory and an instructional framework, and revised them through repeated rounds of experiments and playtesting.[^s3] To judge all funded games on the same yardstick, MITRE and ETS built a separate standardised test, the Assessment of Biases in Cognition, with equivalent forms for use before and after training.[^s6]

## How it works

In *Missing: The Pursuit of Terry Hughes*, the player investigates a missing neighbour. Along the way the game asks for judgments that tempt players to seek only confirming clues, to explain a character's behaviour by personality while ignoring the situation, or to rate themselves as less biased than others. At the end of each episode, the game reviews the player's choices, explains the relevant bias with examples, and gives practice items with personalised feedback; a later version added extra practice for players who kept answering in a biased way.[^s1] A comparison video taught the same biases by explanation alone.[^s1]

Picture a regional operations team before its quarterly supplier review. Rather than circulating a slide on "common biases," the training lead has each analyst play the game individually. One analyst discovers, from her own scores, that she rated herself far less biased than colleagues while showing the same confirmation pattern she criticised in them. That personal, scored evidence is what the game supplies and a lecture does not.[^s1][^s3]

## How to apply it

1. Name the specific biases the team's decisions are most exposed to; the evidence is per bias, not for "bias" in general.[^s1][^s5]
2. Choose interactive training that makes people commit to judgments first and then shows them their own errors with feedback and practice; in direct comparisons games outperformed videos on reducing bias, though videos taught definitions as well or better.[^s1][^s4][^s5]
3. Measure before and after with items that differ from the training content, and recheck weeks later.[^s1][^s6]
4. Pair training with procedures, such as seeking disconfirming evidence in written analyses, because transfer to real decisions is the weakest link.[^s2][^s5]

A common pitfall is treating a high quiz score on bias definitions as success: in both 2015 experiments the video taught definitions better right after training, yet reduced bias less than the game.[^s1][^s4]

## Evidence

Morewedge and colleagues (2015) ran two experiments with about 240 lab participants each. Averaged across the targeted biases, the game reduced bias by about 46% immediately and 35% two months later in the first experiment, and by about 32% immediately and 24% three months later in the second. The video also worked, but less well in most comparisons.[^s1] For the bias blind spot specifically, the game produced large reductions (d of about 0.9 to 1.0) that held at two months, against medium effects for the video.[^s1] An independent evaluation by a separate team found games better than video for procedural skill in mitigating bias, not for factual knowledge, with effects persisting after a delay.[^s4]

The main field test, at HEC Paris in 2019, found that 290 business students who had played the game before an unannounced case analysis were less likely to pick the hypothesis-confirming, inferior option (about 59% versus 72%) and wrote fewer confirming arguments.[^s2] Its authors note that students were not randomly assigned and that one case at one school is a narrow test.[^s2] A 2021 systematic review of 12 studies judged serious games the most successful bias-mitigation interventions, with retention up to 12 weeks, but found far transfer to real decisions tested only once and concluded that the evidence for real-life improvement is still insufficient.[^s5] Most positive results come from the Sirius program itself, the measures were mostly custom questionnaires, and samples were small and local, so the status here is mixed.[^s5][^s1]

## Connections

- **Counteracts** the bias blind spot, with the largest and most durable game effect reported for that bias in the 2015 experiments.[^s1]
- **Counteracts** confirmation bias in a field decision task, with reduced confirmatory reasoning the likely route.[^s2]
- **Counteracts** the fundamental attribution error and, more weakly, anchoring, where the anchoring scale was less reliable.[^s1]
- **Introduced by** Carey Morewedge's team under IARPA Sirius, using iterative design and evaluation.[^s3]
- **Demonstrated by** the 2015 laboratory experiments and the 2019 field-transfer study.[^s1][^s2]
- **Applied in** intelligence analysis, the setting whose biases the program targeted.[^s6]
- **Broader:** debiasing; **related** to consider-the-opposite, which the game's emphasis on disconfirming evidence resembles, and to metacognition and structured analytic techniques.[^s2][^s5]

## Sources

[^s1]: Morewedge et al., "Debiasing Decisions: Improved Decision Making With a Single Training Intervention", *Policy Insights from the Behavioral and Brain Sciences* 2 (2015). https://openaccess.city.ac.uk/id/eprint/12324/1/Debiasing_Decisions_PIBBS.pdf (accessed 2026-11-04)
[^s2]: Sellier, Scopelliti & Morewedge, "Debiasing training transfers to improve decision making in the field", *Psychological Science* 30 (2019). https://openaccess.city.ac.uk/id/eprint/22233/1/DebiasingTrainingTransfers_InPress.pdf (accessed 2026-11-04)
[^s3]: Symborski et al., "The Design and Development of Serious Games Using Iterative Evaluation", *Games and Culture* 12 (2017). https://api.crossref.org/works/10.1177%2F1555412016673262 (accessed 2026-11-04)
[^s4]: Rhodes et al., "Teaching Decision Making With Serious Games: An Independent Evaluation", *Games and Culture* 12 (2017). https://api.crossref.org/works/10.1177%2F1555412016686642 (accessed 2026-11-04)
[^s5]: Korteling, Gerritsma & Toet, "Retention and Transfer of Cognitive Bias Mitigation Interventions: A Systematic Literature Study", *Frontiers in Psychology* 12 (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8397507 (accessed 2026-11-04)
[^s6]: Gertner et al., "The Assessment of Biases in Cognition (ABC)", MITRE Technical Report MTR160163 (2016). https://www.mitre.org/sites/default/files/publications/pr-16-0956-the-assessment-of-biases-in-cognition.pdf (accessed 2026-11-04)
