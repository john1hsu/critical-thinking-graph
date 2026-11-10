---
id: ct:law-of-small-numbers
type: CognitiveBias
title: Law of small numbers
aliases: [belief in the law of small numbers, representativeness of small samples, small-sample representativeness belief]
domain: probabilistic-reasoning
summary: >-
  The mistaken intuition, named by Tversky and Kahneman in 1971, that even a
  small random sample will closely resemble the population it came from, so
  that small-sample results look more stable, more conclusive and more likely
  to replicate than sampling theory allows.
level: intermediate
evidenceStatus: contested
broader: [ct:cognitive-bias]
related: [ct:insensitivity-to-sample-size, ct:gamblers-fallacy, ct:hasty-generalization, ct:regression-to-the-mean, ct:random-sampling, ct:hot-hand-fallacy, ct:statistical-reasoning-training]
requires: [ct:representativeness-heuristic, ct:random-sampling]
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: medium}
  - {predicate: formalizedBy, object: ct:matthew-rabin, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:hong-2023-law-of-small-numbers-replication, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:benjamin-2019-errors-in-probabilistic-reasoning, source: s4, confidence: medium}
  - {predicate: studiedIn, object: ct:behavioral-economics, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Belief in the law of small numbers"
    publisher: Psychological Bulletin 76(2), 105-110 (Tversky & Kahneman, 1971), hosted copy
    url: https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Inference by believers in the law of small numbers"
    publisher: UC Berkeley Department of Economics working paper (Rabin, 2000; published in Quarterly Journal of Economics 117(3), 2002), eScholarship
    url: https://escholarship.org/content/qt4sw8n41t/qt4sw8n41t.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Revisiting the 'belief in the law of small numbers': replication and extensions of problems reviewed in Tversky and Kahneman (1971)"
    publisher: The University of Hong Kong, HKU Scholars Hub (Hong, 2023, MSocSc thesis, Registered Report)
    url: https://hub.hku.hk/handle/10722/335948
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Errors in probabilistic reasoning and judgment biases"
    publisher: National Bureau of Economic Research Working Paper 25200 (Benjamin, 2018; chapter for the Handbook of Behavioral Economics)
    url: https://www.nber.org/papers/w25200.pdf
    type: academic
    accessed: 2026-11-10
  - id: s5
    title: "Revisiting the 'Belief in the law of small numbers': Conceptual replication and extensions (Stage 1 recommendation)"
    publisher: Peer Community in Registered Reports (recommender M. Syed, 2023)
    url: https://rr.peercommunityin.org/articles/rec?id=410
    type: institutional
    accessed: 2026-11-10
created: 2026-11-10
---

# Law of small numbers

The law of small numbers is a tongue-in-cheek name for a mistaken intuition: that a random sample, however small, should look like the population it was drawn from.[^s1] The real law of large numbers guarantees that only large samples settle near the population value; the "law of small numbers" is the unwarranted belief that the same holds for a handful of cases.[^s1] People who hold it treat a striking result from a few observations as solid, expect it to repeat, and explain away deviations instead of blaming chance.[^s1][^s2]

## Origin

Amos Tversky and Daniel Kahneman, then at the Hebrew University of Jerusalem, coined the term in a 1971 *Psychological Bulletin* paper.[^s1] Their evidence came from questionnaires given to research psychologists at meetings of the Mathematical Psychology Group and the American Psychological Association.[^s1] In the best-known item, a researcher has a significant result from 20 subjects and runs 10 more; respondents estimated the chance that the new group alone would also be significant. The median answer was about .85, against a correct value of roughly .48, and only 9 of 84 respondents gave an answer between .40 and .60.[^s1] The authors argued that the error is a product of judging samples by how representative they look, and that the gambler's fallacy flows from the same belief that chance corrects itself in the short run.[^s1]

## How it works

Tversky and Kahneman listed four consequences for researchers who believe in the law of small numbers: they stake hypotheses on samples too small to detect them, overrate early trends, expect significant findings to replicate too readily, and attribute surprising deviations to causes rather than sampling error, so the belief is rarely corrected.[^s1] They tied this to the low statistical power of much published psychology, citing Jacob Cohen's 1962 review in which the average power to detect a medium effect was only .48.[^s1]

Economist Matthew Rabin later gave the bias a formal model. His agent treats independent signals as if they were drawn without replacement from a small urn that must reflect the true rate, so each outcome makes its repeat seem less likely.[^s2] The model reproduces the gambler's fallacy and predicts over-inference: after only two strong years from a fund manager or analyst, the agent concludes the person is unusually skilled, and across many managers sees far more real differences in ability than exist, which Rabin called fictitious variation.[^s2]

A workplace example: a team pilots a new onboarding checklist with eight hires, and six reach full productivity faster than the usual average. The manager announces a 75% success rate and budgets a company-wide rollout expecting the same result. With eight cases, a run like this is well within what chance alone produces, and the full-scale numbers will very likely be closer to the old average, which the manager may then blame on poor execution rather than on the pilot's size.[^s1][^s2]

## Evidence

The original study was a survey of a self-selected professional audience, and it went unreplicated for decades.[^s1][^s5] A 2023 Registered Report at the University of Hong Kong re-ran seven of the 1971 problems with 1,089 American online participants.[^s3] Four tendencies replicated, including overestimating the chance that a small-sample result will replicate; the predicted underestimation of the sample size needed for a replication did not.[^s3] When the scenarios' sample sizes were multiplied by 10 and 100, estimates generally rose, suggesting people are not wholly blind to sample size.[^s3]

Daniel Benjamin's 2018 review for the *Handbook of Behavioral Economics* found the gambler's fallacy, the bias's central prediction, well supported in surveys, incentivized experiments and field data.[^s4] He judged the evidence for over-inference from small samples weak, noted that the 1971 survey answers may be confounded by other statistical misunderstandings, and reported that people more often under-infer in experiments.[^s4] He also found gambler's-fallacy patterns that no consistent law-of-small-numbers model can produce, so the belief is at best a partial explanation.[^s4] The status is best read as contested: the expectation of local balance is robust, while the broader claim of systematic over-inference is disputed.[^s3][^s4]

## How to spot it

- A conclusion or a rollout plan rests on a pilot, a first quarter or a single cohort, with no estimate of how much the result could vary by chance.[^s1]
- Someone expects a small study's effect to reappear at the same size when repeated.[^s1][^s3]
- A short streak is read as proof of skill, or as a sign that the opposite outcome is due.[^s2]
- A disappointing follow-up is explained by a new cause rather than sampling error.[^s1]

## How to counter it

Before collecting data, estimate the sample needed to detect a realistic effect and report statistical power, as Tversky and Kahneman urged.[^s1] Report confidence intervals and effect sizes rather than a bare pass or fail on significance, because intervals show how wide the plausible range from a small sample is.[^s1] When judging people or units from a short track record, ask how much spread pure chance would produce across all of them before ranking anyone.[^s2] Tversky and Kahneman doubted that experience alone corrects the intuition and recommended deliberate training in sampling variability.[^s1]

## Connections

- **Broader: cognitive bias.** It is a systematic error in intuitive judgments about samples.[^s1]
- **Introduced by Amos Tversky and Daniel Kahneman** in their 1971 *Psychological Bulletin* paper.[^s1]
- **Explained by the representativeness heuristic,** which the authors proposed as its source: samples are judged by resemblance to the population.[^s1]
- **Formalized by Matthew Rabin,** whose urn model derives the gambler's fallacy and over-inference.[^s2]
- **Supported by Hong's 2023 Registered Report replication,** which reproduced four of five tested tendencies.[^s3]
- **Challenged by Benjamin's 2018 review,** which finds the over-inference evidence weak.[^s4]
- **Studied in behavioral economics,** where Rabin's model and Benjamin's review place it.[^s2][^s4]
- **Related to insensitivity to sample size, the gambler's fallacy, the hot-hand fallacy, hasty generalization, regression to the mean, random sampling and statistical reasoning training,** all of which concern how much a small sample can show.[^s1][^s2][^s4]

## Sources

[^s1]: A. Tversky & D. Kahneman, "Belief in the law of small numbers", *Psychological Bulletin* 76(2), 1971, 105–110. https://literature.wolkersdorfer.info/literature/Belief%20in%20the%20law%20of%20small%20numbers.pdf (accessed 2026-11-10)
[^s2]: M. Rabin, "Inference by believers in the law of small numbers", UC Berkeley working paper, 2000 (published in *Quarterly Journal of Economics* 117(3), 2002). https://escholarship.org/content/qt4sw8n41t/qt4sw8n41t.pdf (accessed 2026-11-10)
[^s3]: C. K. Hong, "Revisiting the 'belief in the law of small numbers': replication and extensions of problems reviewed in Tversky and Kahneman (1971)", MSocSc thesis, The University of Hong Kong, 2023. https://hub.hku.hk/handle/10722/335948 (accessed 2026-11-10)
[^s4]: D. J. Benjamin, "Errors in probabilistic reasoning and judgment biases", NBER Working Paper 25200, 2018. https://www.nber.org/papers/w25200.pdf (accessed 2026-11-10)
[^s5]: M. Syed (recommender), Stage 1 recommendation for Hong & Feldman, "Revisiting the 'Belief in the law of small numbers': Conceptual replication and extensions", Peer Community in Registered Reports, 2023. https://rr.peercommunityin.org/articles/rec?id=410 (accessed 2026-11-10)
