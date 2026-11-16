---
id: ct:dunning-kruger-effect
type: CognitiveBias
title: Dunning-Kruger effect
aliases: [Dunning–Kruger effect, unskilled and unaware effect, dual burden of incompetence]
domain: cognitive-biases
summary: >-
  The finding that people who perform worst in a domain tend to overestimate
  their performance and relative standing the most, attributed by its
  discoverers to a "dual burden": the skills needed to do well are the same
  skills needed to recognise one's own errors.
level: introductory
evidenceStatus: contested
broader: [ct:overconfidence-effect]
related: [ct:calibration, ct:bias-blind-spot, ct:metacognition]
requires: [ct:cognitive-bias]
relations:
  - {predicate: introducedBy, object: ct:justin-kruger, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:david-dunning, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:kruger-dunning-1999-unskilled-and-unaware-studies, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:metacognition, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:regression-to-the-mean, source: s3, confidence: medium}
  - {predicate: supportedBy, object: ct:jansen-rafferty-griffiths-2021-rational-model-study, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:burson-larrick-klayman-2006-noise-plus-bias-study, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:gignac-zajenkowski-2020-dunning-kruger-artifact-critique, source: s4, confidence: medium}
sources:
  - id: s1
    title: "Unskilled and Unaware of It: How Difficulties in Recognizing One's Own Incompetence Lead to Inflated Self-Assessments"
    publisher: Journal of Personality and Social Psychology 77(6), 1121-1134 (Kruger & Dunning, 1999), copy at gwern.net
    url: https://www.gwern.net/doc/psychology/1999-kruger.pdf
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Skilled or unskilled, but still unaware of it: how perceptions of difficulty drive miscalibration in relative comparisons"
    publisher: Journal of Personality and Social Psychology 90(1), 60-77 (Burson, Larrick & Klayman, 2006), Duke Scholars record
    url: https://scholars.duke.edu/publication/782621
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "A rational model of the Dunning-Kruger effect supports insensitivity to evidence in low performers"
    publisher: Nature Human Behaviour 5, 2021 (Jansen, Rafferty & Griffiths), author's copy at Princeton Computational Cognitive Science Lab
    url: https://cocosci.princeton.edu/papers/DK_NHB_Final.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Reevaluating the Dunning-Kruger effect: A response to and replication of Gignac and Zajenkowski (2020)"
    publisher: Intelligence 96, 101717 (Dunkel, Nedelec & van der Linden, 2023), Erasmus University Rotterdam repository
    url: https://pure.eur.nl/ws/portalfiles/portal/146015357/1-s2.0-S0160289622000988-main.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Random Number Simulations Reveal How Random Noise Affects the Measurements and Graphical Portrayals of Self-Assessed Competency"
    publisher: Numeracy 9(1), Article 4 (Nuhfer, Cogan, Fleisher, Gaze & Wirth, 2016), University of South Florida Digital Commons
    url: https://digitalcommons.usf.edu/numeracy/vol9/iss1/art4/
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Dunning-Kruger effect

The Dunning-Kruger effect is the pattern in which the people who score lowest on a test of some skill overestimate both their score and their standing relative to others by the widest margin, while top scorers tend to slightly underestimate their standing.[^s1] Its discoverers explained it as a "dual burden": a person who lacks a skill both makes errors and lacks the very knowledge needed to notice them.[^s1] Later work agrees that the pattern shows up in data but disputes how much of it reflects a real metacognitive deficit rather than measurement noise and statistics.[^s2][^s4]

## Origin

Justin Kruger and David Dunning, then at Cornell University, reported the effect in a 1999 paper in the *Journal of Personality and Social Psychology*.[^s1] Across four studies, students judged the funniness of jokes, solved logical-reasoning items drawn from an LSAT preparation guide and Wason selection tasks, and answered grammar questions, then estimated their raw score and their percentile rank among peers.[^s1] In every study the bottom quartile scored around the 10th to 13th percentile yet placed itself, on average, above the 50th; in the grammar study, for instance, bottom scorers sat at the 10th percentile but put their test performance at about the 61st.[^s1]

## How it works

Picture a new analyst asked to review spreadsheet formulas. If she does not know that a lookup can silently return the wrong row, she will neither avoid that error nor spot it when checking her own work, so her work feels correct to her. A senior colleague who knows the pitfall catches more errors and also knows how many there were. Kruger and Dunning argued that this shared skill for producing and judging answers is why low performers' self-ratings stay high.[^s1]

Their original data also showed an asymmetry at the top. High performers underestimated their percentile because they assumed others found the test as easy as they did, a false-consensus error. After grading five peers' tests, top-quartile students raised their estimates, while bottom-quartile students barely changed theirs.[^s1] In a fourth study, a short logic-training packet sharply improved low scorers' ability to tell which of their own answers were right, and their self-estimates fell to more realistic levels.[^s1]

## Evidence

The basic pattern replicates at scale. Jansen, Rafferty and Griffiths (2021) tested about 3,500 online participants in each of two domains, grammar and logic, and again found that low scorers overestimated their scores and high scorers slightly underestimated them.[^s3] Their Bayesian model treats self-assessment as a blend of a prior belief about one's ability with noisy judgments of each answer, which on its own pulls every estimate toward the average. A model in which low performers are also less sensitive to their own errors fitted both datasets better, though the authors note the two models differ mainly in sparsely populated tails.[^s3]

Critics argue that much of the pattern is built into the method. Burson, Larrick and Klayman (2006) ran 12 tasks in three studies and found that on moderately difficult tasks the best and worst performers were about equally miscalibrated, and on hard tasks the best performers were *less* accurate; a simple noise-plus-bias model accounted for the results.[^s2] Nuhfer and colleagues (2016) used random-number simulations to show that common ways of graphing self-assessment, such as quartile column charts and plots of error against score, can produce misleading patterns from noise alone.[^s5] Gignac and Zajenkowski (2020) found a Dunning-Kruger pattern for intelligence with the usual quartile comparison but none with tests they judged more appropriate; a 2023 reanalysis of almost 14,000 young adults detected a statistically significant effect with those tests, but it explained only about 1% of variance.[^s4] Given this dispute, the evidence status here is *contested*: overestimation by low scorers is reliable, but the size of any skill-specific blindness beyond regression and noise is debated.[^s2][^s3][^s4]

## How to spot it

- Notice confident self-ratings from people new to a task, especially where feedback is slow or absent, since without the relevant skill errors are hard to see.[^s1]
- Before concluding that a group "doesn't know what it doesn't know", check whether the chart merely sorts people by score and plots their error; that format can show the pattern from random noise.[^s5]
- Remember that task difficulty shifts the picture: on hard tasks, even top performers can misjudge their standing badly.[^s2]

## How to counter it

- Teach the underlying skill. In Kruger and Dunning's training study, brief instruction improved low performers' ability to judge their own answers and lowered their inflated estimates.[^s1]
- Let people see others' work. Exposure to peers' answers corrected top performers' underestimates in the original studies, though not bottom performers' overestimates.[^s1]
- Rely on external scoring and calibration records rather than self-assessment where accuracy matters, because self-estimates of everyone regress toward the average.[^s2][^s3]

## Connections

- **Broader:** a form of the overconfidence effect, specifically overestimation and overplacement concentrated among low performers.[^s1]
- **Introduced by** Justin Kruger and David Dunning, and **demonstrated by** their four 1999 studies on humour, logic and grammar.[^s1]
- **Explained by** metacognition, in the original account: the deficit lies in monitoring one's own performance.[^s1] Also **explained by** regression to the mean, which Jansen and colleagues' Bayesian model shows produces part of the pattern for every performer.[^s3]
- **Supported by** Jansen, Rafferty and Griffiths' 2021 large-sample replication and model comparison, which favoured reduced error sensitivity in low performers.[^s3]
- **Challenged by** Burson, Larrick and Klayman's 2006 noise-plus-bias study[^s2] and by Gignac and Zajenkowski's 2020 artifact critique, whose replication found only a very small effect.[^s4]
- **Related to** calibration, since the effect is measured as a gap between estimated and actual scores,[^s3] and to the bias blind spot. Noise in such measurements can itself mimic the pattern.[^s5]

## Sources

[^s1]: Kruger & Dunning, "Unskilled and Unaware of It", Journal of Personality and Social Psychology 77(6), 1999. https://www.gwern.net/doc/psychology/1999-kruger.pdf (accessed 2026-11-16)
[^s2]: Burson, Larrick & Klayman, "Skilled or unskilled, but still unaware of it", Journal of Personality and Social Psychology 90(1), 2006. https://scholars.duke.edu/publication/782621 (accessed 2026-11-16)
[^s3]: Jansen, Rafferty & Griffiths, "A rational model of the Dunning-Kruger effect supports insensitivity to evidence in low performers", Nature Human Behaviour, 2021. https://cocosci.princeton.edu/papers/DK_NHB_Final.pdf (accessed 2026-11-16)
[^s4]: Dunkel, Nedelec & van der Linden, "Reevaluating the Dunning-Kruger effect", Intelligence 96, 2023. https://pure.eur.nl/ws/portalfiles/portal/146015357/1-s2.0-S0160289622000988-main.pdf (accessed 2026-11-16)
[^s5]: Nuhfer, Cogan, Fleisher, Gaze & Wirth, "Random Number Simulations Reveal How Random Noise Affects the Measurements and Graphical Portrayals of Self-Assessed Competency", Numeracy 9(1), 2016. https://digitalcommons.usf.edu/numeracy/vol9/iss1/art4/ (accessed 2026-11-16)
