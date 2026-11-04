---
id: ct:base-rate-neglect
type: ProbabilisticFallacy
title: Base-rate neglect
aliases: [base rate fallacy, base-rate fallacy, base rate neglect, prior neglect]
domain: probabilistic-reasoning
summary: >-
  The error of judging how likely something is from case-specific evidence
  alone while ignoring or underweighting how common it is in the first place
  (its base rate or prior probability).
level: introductory
evidenceStatus: mixed
broader: [ct:probabilistic-fallacy]
related: [ct:heuristics-and-biases-program, ct:conjunction-fallacy, ct:natural-frequencies]
requires: [ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:kahneman-tversky-1972-lawyer-engineer-study, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:bayesian-reasoning, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:koehler-1996-base-rate-fallacy-reconsidered, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: medium}
criticalQuestions:
  - Before looking at this evidence, how common is the outcome in the relevant population?
  - How often would this same evidence show up if the outcome were absent (the false-positive rate)?
  - Out of 1,000 comparable cases, how many would show the evidence and actually have the outcome?
  - Is the base rate I am using drawn from a reference class that really fits this case?
argumentMap:
  premises:
    - "The screening tool flags 99% of compromised accounts."
    - "It wrongly flags only 2% of legitimate accounts."
    - "This account was flagged."
  conclusion: "This account is about 98% likely to be compromised."
  verdict: fallacious
  scheme: ct:bayesian-reasoning
  objections:
    - "Only about 1 in 1,000 accounts is compromised, so most flags are false alarms and the real probability is under 5%."
sources:
  - id: s1
    title: "On the Psychology of Prediction"
    publisher: Oregon Research Institute Research Bulletin 12(4) (Kahneman & Tversky, 1972), University of Oregon Scholars' Bank
    url: https://scholarsbank.uoregon.edu//bitstreams/2fbae090-7a99-4301-8402-26e6e3a4c00c/download
    type: primary
    accessed: 2026-11-04
  - id: s2
    title: "The base-rate fallacy in probability judgments"
    publisher: Acta Psychologica 44(3), 211-233 (Bar-Hillel, 1980), Hebrew University research portal
    url: https://cris.huji.ac.il/en/publications/the-base-rate-fallacy-in-probability-judgments/
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s3
    title: "How to improve Bayesian reasoning without instruction: Frequency formats"
    publisher: Psychological Review 102(4), 684-704 (Gigerenzer & Hoffrage, 1995), UC San Diego course copy
    url: https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "The base rate fallacy reconsidered: Descriptive, normative, and methodological challenges"
    publisher: Behavioral and Brain Sciences 19(1), 1-17 (Koehler, 1996), Cambridge University Press
    url: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/base-rate-fallacy-reconsidered-descriptive-normative-and-methodological-challenges/5C0138815B364140B87110364055683B
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies: Frequency Phobia in Spite of Probability Blindness"
    publisher: Frontiers in Psychology 9, 1833 (Weber, Binder & Krauss, 2018)
    url: https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01833/text
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Base-rate neglect

Base-rate neglect is the error of judging the probability of an outcome from the evidence about a particular case while ignoring, or giving too little weight to, how common that outcome is to begin with. The base rate is the prior probability: the share of the relevant population that has the property before any case-specific information arrives. Probability theory says the two must be combined, and Bayes' theorem is the rule for doing so; base-rate neglect is judging as if the prior did not matter.[^s1][^s3] Maya Bar-Hillel's 1980 review described the pattern as a general tendency to let individuating information about a case override population statistics, with consequences for clinical, legal and social judgment.[^s2]

## Origin

Daniel Kahneman and Amos Tversky documented the effect in "On the Psychology of Prediction", issued as an Oregon Research Institute research bulletin in 1972.[^s1] In their best-known study, participants read short personality sketches said to be drawn from a group of engineers and lawyers. One group was told the pool held 30 engineers and 70 lawyers; another was told the reverse. Bayes' rule says the two groups' answers should differ sharply, yet the stated proportions barely moved the estimates (mean judgments of about 55% versus 50%).[^s1] With no sketch at all, people used the base rates correctly. Given a sketch written to be uninformative, they answered 50% in both groups, discarding the prior they had just used.[^s1] Kahneman and Tversky called the failure to combine priors with specific evidence one of the most significant departures of intuition from the normative theory of prediction.[^s1]

## How it works

Kahneman and Tversky's explanation was representativeness: people judge probability by how well the case resembles a stereotype, and resemblance carries no information about how common the category is.[^s1] Bar-Hillel proposed a relevance account instead. People rank information by how relevant it seems and let the more relevant item dominate. Base rates feel low in relevance unless they refer to a narrow subgroup containing the case or can be read causally; when both items seem equally relevant, people do combine them.[^s2]

A workplace example shows the stakes. A security tool flags 99% of compromised accounts and wrongly flags 2% of legitimate ones. An analyst sees a flag and concludes the account is about 98% likely to be compromised (see the argument map). But if only 1 in 1,000 accounts is actually compromised, then out of 100,000 accounts about 99 compromised ones are flagged alongside roughly 1,998 legitimate ones, so a flag means compromise less than 5% of the time. Gigerenzer and Hoffrage's mammography problem has the same structure: with a 1% prevalence, 80% sensitivity and a false-positive rate near 10%, the chance of cancer after a positive test is under 8%.[^s3]

## How to spot it

Watch for a confident probability that is built only from a test's accuracy, a witness's reliability or how well a case "fits a profile", with no mention of how often the outcome occurs.[^s1][^s2] Rare targets (fraud, a disease in a screening population, a hire who will become a star) combined with a reasonably accurate signal are the classic setting, because the false positives from the large majority can swamp the true positives from the small minority.[^s3]

## How to counter it

Restate the problem as natural frequencies: imagine a concrete number of cases and count how many have the outcome and show the evidence. Gigerenzer and Hoffrage found that across 15 problems people gave Bayesian answers 16% to 28% of the time with probability formats and 46% to 50% of the time with frequency formats, without any instruction.[^s3] Their explanation is that frequencies carry the base rate inside the counts and need fewer computational steps.[^s3] The critical questions above walk through the same count.

## Evidence

The effect is real but depends on format and context. A 2017 meta-analysis by McDowell and Jacobs, as summarised by Weber and colleagues, found about 4% correct answers with probabilities and 24% with natural frequencies, so most people still fail even in the easier format.[^s5] Jonathan Koehler's 1996 target article argued that the fallacy has been overstated. On his review, people rarely ignore base rates entirely; they weight them more when base rates are learned from experience, framed as frequencies, reliable and diagnostic. He also argued that real decisions seldom match the tidy Bayesian textbook problem, so labelling departures from it as errors can be inappropriate.[^s4] The safer conclusion is that base rates are underweighted in many described-problem settings, not that they are always ignored.[^s4][^s5]

## Connections

- **Introduced by** Daniel Kahneman and Amos Tversky, whose 1972 prediction studies, including the lawyer–engineer study, first demonstrated it.[^s1]
- **Explained by** the representativeness heuristic: resemblance to a stereotype crowds out category frequency.[^s1]
- **Contrasts with** Bayesian reasoning, the normative combination of prior and evidence that frequency formats make easier.[^s3]
- **Challenged by** Koehler's 1996 reassessment of how often and how badly people neglect base rates.[^s4]
- **Studied in** judgment and decision making, where it bears on clinical, legal and social inference.[^s2]
- **Related to** the heuristics-and-biases program and the conjunction fallacy, and **requires** conditional probability.[^s1][^s3]

## Sources

[^s1]: Kahneman & Tversky, "On the Psychology of Prediction", Oregon Research Institute Research Bulletin 12(4), 1972. https://scholarsbank.uoregon.edu//bitstreams/2fbae090-7a99-4301-8402-26e6e3a4c00c/download (accessed 2026-11-04)
[^s2]: Bar-Hillel, "The base-rate fallacy in probability judgments", Acta Psychologica 44(3), 1980. https://cris.huji.ac.il/en/publications/the-base-rate-fallacy-in-probability-judgments/ (accessed 2026-11-04)
[^s3]: Gigerenzer & Hoffrage, "How to improve Bayesian reasoning without instruction: Frequency formats", Psychological Review 102(4), 1995. https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf (accessed 2026-11-04)
[^s4]: Koehler, "The base rate fallacy reconsidered", Behavioral and Brain Sciences 19(1), 1996. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/base-rate-fallacy-reconsidered-descriptive-normative-and-methodological-challenges/5C0138815B364140B87110364055683B (accessed 2026-11-04)
[^s5]: Weber, Binder & Krauss, "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies", Frontiers in Psychology 9, 2018. https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01833/text (accessed 2026-11-04)
