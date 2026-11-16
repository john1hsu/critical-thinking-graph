---
id: ct:calibration-training
type: Technique
title: Calibration training
aliases: [confidence calibration training, probability calibration training, training for calibration, calibration feedback training]
domain: debiasing-and-metacognition
summary: >-
  A debiasing technique in which people repeatedly state their confidence in
  answers or forecasts, are scored against the outcomes, and receive feedback
  on the gap, so that their stated confidence comes to match how often they
  are actually right. It reliably trims overconfidence but improves knowledge
  or discrimination much less.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:calibration, ct:metacognition, ct:brier-score, ct:hard-easy-effect, ct:statistical-reasoning-training]
requires: [ct:calibration]
relations:
  - {predicate: counteracts, object: ct:overconfidence-effect, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:dunning-kruger-effect, source: s1, confidence: medium}
  - {predicate: demonstratedBy, object: ct:lichtenstein-fischhoff-1980-training-for-calibration, source: s4, confidence: high}
  - {predicate: supportedBy, object: ct:stone-opel-2000-calibration-feedback-study, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:geopolitical-forecasting, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Training metacognition in the classroom: The influence of incentives and feedback on exam predictions"
    publisher: Metacognition and Learning 6(3), 303-314 (Miller & Geraci, 2011), South Dakota State University Open PRAIRIE record
    url: https://openprairie.sdstate.edu/psych_pubs/5
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Confidence Calibration in a Multiyear Geopolitical Forecasting Competition"
    publisher: Management Science 63(11), 3552-3565 (Moore, Swift, Minster, Mellers, Ungar, Tetlock, Yang & Tenney, 2017), copy hosted at UC Berkeley Statistics
    url: https://www.stat.berkeley.edu/~aldous/157/Papers/moore_swift.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Training to Improve Calibration and Discrimination: The Effects of Performance and Environmental Feedback"
    publisher: Organizational Behavior and Human Decision Processes 83(2), 282-309 (Stone & Opel, 2000), copy hosted at California State University, Long Beach
    url: https://home.csulb.edu/~cwallis/382/certainty/overconfidence/Training%20to%20Improve%20Calibration.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "How Well Do Probability Experts Assess Probabilities?"
    publisher: Decision Research technical report PTR-1092-80-8 for the Office of Naval Research (Lichtenstein & Fischhoff, 1980), Defense Technical Information Center
    url: https://apps.dtic.mil/sti/pdfs/ADA089619.pdf
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Calibration training

Calibration training is practice designed to make a person's stated confidence match their hit rate: when a calibrated judge says "70% sure", they are right about seven times in ten.[^s2] Trainees answer questions or make forecasts, attach a probability to each, are scored once the answers are known, and then see where their confidence ran ahead of, or behind, their accuracy.[^s3] It is a narrower thing than calibration itself, which is the property being measured; the training is the intervention meant to improve it.[^s2][^s3]

## Origin

Researchers at Decision Research, working under Office of Naval Research funding, studied the technique around 1980. In Sarah Lichtenstein and Baruch Fischhoff's 1980 training work, subjects completed either 3 or 11 sessions of 200 general-knowledge items each and received individual feedback on their calibration after every session.[^s4] In a follow-up test on 500 new items, the trained group was markedly better calibrated than an untrained group, and the authors judged the training moderately successful at reducing overconfidence.[^s4] Stone and Opel later noted that, in this early work, most of the gain arrived after the first intensive session.[^s3]

## How it works

Training works on the step where an internal feeling of certainty becomes a number. Imagine a project lead who, each Monday, writes down a probability that each of her team's tasks will ship by Friday. After a month she groups her forecasts: of the tasks she rated 90% likely, only 60% shipped. That feedback tells her that her "90%" really means "60%", and next month she uses lower numbers for similar tasks.[^s2][^s3]

Two kinds of feedback do different jobs. In a 2000 experiment, 84 students judged which art period paintings came from. Those given personalised calibration graphs and advice to avoid extreme probabilities became less overconfident on hard items, but no better at telling the periods apart. Those given an art-history lecture instead got better at telling them apart but became *more* overconfident, apparently overestimating how much they had learned.[^s3] The authors concluded that calibration and discrimination are separate skills needing separate training.[^s3]

## How to apply it

1. **Make predictions checkable.** Write each judgment as a probability on something that will be resolved, such as a deadline, an exam score or a forecast question.[^s2]
2. **Score and show the gap.** Compare average confidence with the share of correct answers, ideally in a calibration chart for each confidence band.[^s3]
3. **Give concrete, personal feedback.** In two semester-long classroom studies, students predicted their exam scores before each exam. An extra-credit incentive with minimal feedback did not help, but more concrete feedback improved low performers' predictions, whose overestimates had been largest.[^s1]
4. **Pair it with substantive learning.** Feedback on confidence alone did not improve students' exam scores, and it did not improve the art students' discrimination.[^s1][^s3]

Pitfalls: gains can be modest, and teaching content without feedback on confidence can raise overconfidence.[^s3][^s4]

## Evidence

The strongest field evidence comes from the IARPA-funded geopolitical forecasting tournament. Moore and colleagues (2017) analysed 494,552 forecasts by 2,860 forecasters on 344 questions over three years.[^s2] A one-hour online module, which covered probabilistic thinking, warned against overconfidence and included a quiz with accuracy feedback, cut individual forecasters' overconfidence from about 4.3 to 2.0 percentage points, with no sign of fading over the year.[^s2] Overall the forecasters were already fairly well calibrated, and the most confident forecasts remained the most overconfident.[^s2]

The evidence status here is *mixed*. Training reliably narrows the confidence-accuracy gap, but effects are modest, often confined to hard items, and do not by themselves improve knowledge, discrimination or performance.[^s1][^s3][^s4] Lichtenstein and Fischhoff also reported that no training had yet made people properly sensitive to task difficulty, the source of the hard-easy effect.[^s4]

## Connections

- **Broader:** a debiasing technique, aimed at the gap between confidence and accuracy.[^s2]
- **Counteracts** the overconfidence effect, as the one-hour forecasting module showed,[^s2] and, with medium confidence, the Dunning-Kruger effect: concrete feedback improved the exam predictions of low performers, who overestimated most.[^s1]
- **Demonstrated by** Lichtenstein and Fischhoff's 1980 training study, which used repeated sessions with individual feedback.[^s4]
- **Supported by** Stone and Opel's 2000 experiment, which showed that performance feedback improves calibration but not discrimination.[^s3]
- **Applied in** geopolitical forecasting, where tournament organisers trained forecasters and scored them with Brier scores.[^s2]
- **Requires** an understanding of calibration; **related to** metacognition, since predicting one's own score is a monitoring judgment,[^s1] and to the hard-easy effect, which training has struggled to remove.[^s4]

## Sources

[^s1]: Miller & Geraci, "Training metacognition in the classroom: The influence of incentives and feedback on exam predictions", Metacognition and Learning 6(3), 2011. https://openprairie.sdstate.edu/psych_pubs/5 (accessed 2026-11-16)
[^s2]: Moore et al., "Confidence Calibration in a Multiyear Geopolitical Forecasting Competition", Management Science 63(11), 2017. https://www.stat.berkeley.edu/~aldous/157/Papers/moore_swift.pdf (accessed 2026-11-16)
[^s3]: Stone & Opel, "Training to Improve Calibration and Discrimination: The Effects of Performance and Environmental Feedback", Organizational Behavior and Human Decision Processes 83(2), 2000. https://home.csulb.edu/~cwallis/382/certainty/overconfidence/Training%20to%20Improve%20Calibration.pdf (accessed 2026-11-16)
[^s4]: Lichtenstein & Fischhoff, "How Well Do Probability Experts Assess Probabilities?", Decision Research technical report PTR-1092-80-8, 1980. https://apps.dtic.mil/sti/pdfs/ADA089619.pdf (accessed 2026-11-16)
