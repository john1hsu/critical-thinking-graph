---
id: ct:insensitivity-to-sample-size
type: CognitiveBias
title: Insensitivity to sample size
aliases: [sample size neglect, sample-size insensitivity, neglect of sample size]
domain: cognitive-biases
summary: >-
  The tendency to judge how likely a sample result is, or how much a sample
  proves, by how closely it resembles the population while ignoring how many
  cases it contains, so that small samples are trusted too much and their
  greater variability goes unnoticed.
level: introductory
evidenceStatus: contested
broader: [ct:cognitive-bias]
related: [ct:law-of-small-numbers, ct:gamblers-fallacy, ct:hasty-generalization, ct:base-rate-neglect, ct:regression-to-the-mean, ct:statistical-reasoning-training, ct:heuristics-and-biases-program]
requires: [ct:representativeness-heuristic]
relations:
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:judgment-under-uncertainty-heuristics-and-biases, source: s2, confidence: medium}
  - {predicate: demonstratedBy, object: ct:kahneman-tversky-1972-hospital-problem-study, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:sedlmeier-gigerenzer-1997-sample-size-intuitions-review, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Subjective probability: A judgment of representativeness"
    publisher: Cognitive Psychology 3, 430-454 (Kahneman & Tversky, 1972), copy hosted on a UC San Diego faculty page
    url: https://pages.ucsd.edu/~mckenzie/Kahneman&Tversky1972CogPsych.pdf
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Judgment under uncertainty: Heuristics and biases"
    publisher: Science 185(4157), 1124-1131 (Tversky & Kahneman, 1974), copy hosted on an NC State course page
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Intuitions about sample size: The empirical law of large numbers"
    publisher: Journal of Behavioral Decision Making 10, 33-51 (Sedlmeier & Gigerenzer, 1997), CORE open-access copy
    url: https://core.ac.uk/download/288620432.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Revisiting the 'belief in the law of small numbers': replication and extensions of problems reviewed in Tversky and Kahneman (1971)"
    publisher: The University of Hong Kong, HKU Scholars Hub (Hong, 2023, MSocSc thesis, Registered Report)
    url: https://hub.hku.hk/handle/10722/335948
    type: academic
    accessed: 2026-11-09
  - id: s5
    title: "Revisiting the 'Belief in the law of small numbers': Conceptual replication and extensions (Stage 1 recommendation)"
    publisher: Peer Community in Registered Reports (recommender M. Syed, 2023)
    url: https://rr.peercommunityin.org/articles/rec?id=410
    type: institutional
    accessed: 2026-11-09
created: 2026-11-09
---

# Insensitivity to sample size

Insensitivity to sample size is the tendency to judge a sample by how well it matches the population it came from, while giving little or no weight to how many observations it contains.[^s2] Statistically, small samples swing much further from the population value than large ones, and a result drawn from many cases is stronger evidence than the same proportion drawn from a few. People who neglect sample size therefore treat a striking result from ten cases as seriously as one from a thousand, and are surprised when small-sample extremes fail to hold up.[^s1][^s2]

## Origin

Daniel Kahneman and Amos Tversky reported the effect in their 1972 *Cognitive Psychology* paper on judgment by representativeness.[^s1] Nine groups of respondents estimated sampling distributions for samples of 10, 100 and 1,000 drawn from the same populations, and their median estimates were essentially identical across the three sizes.[^s1] The authors concluded that the principle that sampling variance falls as samples grow does not seem to be part of people's intuitive repertoire.[^s1] Tversky and Kahneman gave the bias its name in their 1974 *Science* review, listing it among the errors produced by the representativeness heuristic.[^s2]

## How it works

The classic demonstration is the hospital problem. A town has a large hospital with about 45 births a day and a small one with about 15. Over a year, each logs the days on which more than 60% of babies were boys. Which logs more such days?[^s2] The small hospital should, because a day's births form a smaller sample that strays from 50% more often. Yet in the 1974 report, 53 of 95 undergraduates said "about the same", and only 21 chose the small hospital.[^s2] A second example in the same paper involves draws from an urn: most people judge 4 red out of 5 as stronger evidence for a mostly-red urn than 12 red out of 20, although the larger sample supports it twice as strongly in odds terms.[^s2]

The explanation offered is that a sample proportion is judged by its resemblance to the population, and resemblance does not depend on the number of cases.[^s1][^s2] Tversky and Kahneman linked this to a broader belief they called the "law of small numbers": even trained research psychologists expected small samples to be highly representative and overestimated how well their findings would replicate.[^s2]

A workplace example: a regional manager sees that the smallest branch had both the best and the worst customer-satisfaction scores of the year, and starts drafting a case study on its leadership swings. The scores may say little more than that a branch with forty survey responses a month will produce more extreme averages, in both directions, than one with four hundred.[^s2]

## Evidence

The original findings held up in later work on tasks of the same kind, but their scope has been disputed. Peter Sedlmeier and Gerd Gigerenzer's 1997 review separated two task types.[^s3] In *frequency-distribution* tasks, people judge which sample gives a more accurate estimate; in *sampling-distribution* tasks, like the hospital problem, they must reason about how variable many samples are.[^s3] Across 35 three-option choice studies, the median rate of correct answers was 76% for frequency-distribution tasks but only 33%, chance level, for sampling-distribution tasks.[^s3] They argued that people do hold an "empirical law of large numbers" (bigger samples are more trustworthy), so the conclusion that people ignore sample size in general overreaches.[^s3]

A related registered-report replication from the University of Hong Kong (2023, N = 1,089 online participants) re-ran problems from Tversky and Kahneman's 1971 work on the law of small numbers with lay respondents.[^s4][^s5] Four of five tendencies replicated, such as overestimating the chance that a small-sample finding will replicate. When the sample sizes were multiplied by 10 and 100, however, participants' estimates generally rose, suggesting partial rather than total insensitivity.[^s4] The status is best read as contested: robust failures on variability judgments, real but imperfect sensitivity on accuracy judgments.[^s3][^s4]

## How to spot it

- A conclusion rests on a percentage or average with no count attached, such as "80% of users loved it".[^s2]
- The most extreme results, top and bottom, come from the smallest units: small schools, small branches, short trial periods.[^s2]
- A small pilot is expected to replicate at full scale with the same effect size.[^s2][^s4]
- A question asks how often something will happen across many samples, the task type where intuition fails most.[^s3]

## How to counter it

Ask "out of how many?" before interpreting any proportion, and compare extreme results with the size of the unit that produced them.[^s2] Reframe sampling questions as accuracy questions where possible, since people handle "which sample gives a better estimate?" far better than questions about distributions of many samples.[^s3] When deciding how many cases a study, survey or pilot needs, calculate it rather than estimate it, because intuition underestimates how noisy small samples are.[^s2][^s4]

## Connections

- **Broader: cognitive bias.** It is a systematic error in judging samples, listed by Tversky and Kahneman among the biases of representativeness.[^s2]
- **Requires and is explained by the representativeness heuristic.** Judging a sample by resemblance makes its size seem irrelevant.[^s1][^s2]
- **Introduced by Kahneman and Tversky** in their 1972 paper, and named in their 1974 *Science* article *Judgment under Uncertainty: Heuristics and Biases*.[^s1][^s2]
- **Demonstrated by the 1972 hospital problem study,** where most respondents saw no difference between a large and a small hospital.[^s1]
- **Challenged by Sedlmeier and Gigerenzer's 1997 review,** which limits the failure mainly to sampling-distribution tasks.[^s3]
- **Related to the law of small numbers, gambler's fallacy, hasty generalization, base-rate neglect and regression to the mean,** all of which involve expecting small samples to mirror their populations or misreading chance variation.[^s2][^s4]
- **Related to statistical reasoning training,** a remedy that teaches statistical rules explicitly; the gap it targets is the variability reasoning that sampling-distribution tasks demand and intuition lacks.[^s3]

## Sources

[^s1]: D. Kahneman & A. Tversky, "Subjective probability: A judgment of representativeness", *Cognitive Psychology* 3, 1972, 430–454. https://pages.ucsd.edu/~mckenzie/Kahneman&Tversky1972CogPsych.pdf (accessed 2026-11-09)
[^s2]: A. Tversky & D. Kahneman, "Judgment under uncertainty: Heuristics and biases", *Science* 185(4157), 1974, 1124–1131. https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf (accessed 2026-11-09)
[^s3]: P. Sedlmeier & G. Gigerenzer, "Intuitions about sample size: The empirical law of large numbers", *Journal of Behavioral Decision Making* 10, 1997, 33–51. https://core.ac.uk/download/288620432.pdf (accessed 2026-11-09)
[^s4]: C. K. Hong, "Revisiting the 'belief in the law of small numbers': replication and extensions of problems reviewed in Tversky and Kahneman (1971)", MSocSc thesis, The University of Hong Kong, 2023. https://hub.hku.hk/handle/10722/335948 (accessed 2026-11-09)
[^s5]: M. Syed (recommender), Stage 1 recommendation for Hong & Feldman, "Revisiting the 'Belief in the law of small numbers': Conceptual replication and extensions", Peer Community in Registered Reports, 2023. https://rr.peercommunityin.org/articles/rec?id=410 (accessed 2026-11-09)
