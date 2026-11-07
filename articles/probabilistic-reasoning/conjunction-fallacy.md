---
id: ct:conjunction-fallacy
type: ProbabilisticFallacy
title: Conjunction fallacy
aliases: [conjunction effect, conjunction bias, Linda problem error, conjunction rule violation]
domain: probabilistic-reasoning
summary: >-
  The error of judging a combination of two events or attributes ("A and B")
  to be more probable than one of them alone, which breaks the rule that a
  conjunction can never be more likely than either of its parts.
level: introductory
evidenceStatus: mixed
broader: [ct:probabilistic-fallacy]
related: [ct:base-rate-neglect, ct:natural-frequencies, ct:heuristics-and-biases-program]
requires: []
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:tversky-kahneman-1983-linda-problem-study, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:chandrashekar-2021-conjunction-bias-replication, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:hertwig-gigerenzer-1999-conjunction-fallacy-revisited, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s4, confidence: medium}
criticalQuestions:
  - Is the detailed version of the claim really more likely than the shorter claim it contains?
  - If I strip out the extra detail, does every case that fits the detailed story still fit the short one?
  - Out of 100 comparable cases, how many would show A, and how many of those would also show B?
  - Am I rating how plausible or coherent the story sounds rather than how often it would happen?
argumentMap:
  premises:
    - "Our key vendor has thin margins and relies on a single overseas parts supplier."
    - "A story in which that supplier fails and the vendor then goes bankrupt fits these facts very well."
  conclusion: "The vendor is more likely to go bankrupt because its supplier fails than to go bankrupt at all, so we should budget for the first risk and not the second."
  verdict: fallacious
  objections:
    - "Every supplier-driven bankruptcy is also a bankruptcy, so 'bankrupt for any reason' must be at least as likely as 'supplier fails and vendor goes bankrupt'."
sources:
  - id: s1
    title: "Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment"
    publisher: Psychological Review 90(4), 293-315 (Tversky & Kahneman, 1983), UC San Diego course copy
    url: https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf
    type: primary
    accessed: 2026-11-07
  - id: s2
    title: "The 'conjunction fallacy' revisited: How intelligent inferences look like reasoning errors"
    publisher: Journal of Behavioral Decision Making 12(4), 275-305 (Hertwig & Gigerenzer, 1999), University of Basel edoc record
    url: https://edoc.unibas.ch/8522/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "Frequency estimation and semantic ambiguity do not eliminate conjunction bias, when it occurs: Replication and extension of Mellers, Hertwig, and Kahneman (2001)"
    publisher: Meta-Psychology 5 (Chandrashekar, Cheng, Fong, Leung, Wong, Cheng & Feldman, 2021)
    url: https://open.lnu.se/index.php/metapsychology/article/view/2474
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Commentary: Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment"
    publisher: Frontiers in Psychology 6, 1832 (Lewinski, 2015)
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01832/full
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s5
    title: "Explaining the Conjunction Fallacy"
    publisher: Proceedings of the Annual Meeting of the Cognitive Science Society 46 (Trpin & Hartmann, 2024), eScholarship, University of California
    url: https://escholarship.org/content/qt4bv1k9nw/qt4bv1k9nw.pdf?t=sgrift
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Conjunction fallacy

The conjunction fallacy is judging that two things together ("A and B") are more probable than one of them on its own. Probability theory rules this out: every case in which both A and B happen is also a case in which B happens, so the conjunction can never be more likely than either part. Amos Tversky and Daniel Kahneman, who named the error, grounded this conjunction rule in simple set inclusion and showed that intuitive judgments break it routinely when the combined description sounds more typical or more coherent.[^s1]

## Origin

Tversky and Kahneman reported the effect in a 1983 *Psychological Review* paper. They called a violation in a direct, side-by-side comparison a conjunction fallacy, and a violation that shows up only when different groups rate the parts separately a conjunction error.[^s1] Their best-known item is the Linda problem. Linda is described as a bright, outspoken former philosophy student concerned with social justice. Asked directly whether she is more likely to be "a bank teller" or "a bank teller and active in the feminist movement", 85% of 142 University of British Columbia undergraduates chose the conjunction.[^s1] A parallel problem about Bill, an unimaginative but numerate man, produced the same pattern for "accountant who plays jazz" versus "plays jazz", and probability rankings tracked resemblance rankings almost perfectly (correlations of .96 and .98).[^s1]

## How it works

The original explanation is the representativeness heuristic: people answer "how probable?" by asking "how well does this fit?", and adding a fitting detail raises the fit while it can only lower the probability.[^s1] The same paper showed the effect well beyond personality sketches. Internists ranked a typical symptom combined with an atypical one above the atypical symptom alone in 91% of judgments on average. Professional forecasters at a 1982 congress rated a complete break in US–Soviet diplomatic relations at 0.14%, but rated that same break following a Soviet invasion of Poland at 0.47%.[^s1] A plausible cause makes the combined story more vivid, so a detailed scenario can feel more probable than its bare outcome.[^s1]

The argument map shows the workplace version. A risk team reasons that a key vendor is more likely to fail because its single supplier collapses than to fail at all, because the supplier story fits what they know. But every supplier-driven bankruptcy is a bankruptcy, so the unconditional risk is at least as large, and budgeting only for the vivid route leaves the other routes uncovered. This is the scenario trap Tversky and Kahneman warned about in forecasting.[^s1]

## How to spot it

Watch for estimates that rise as a story gains detail, for scenarios in a plan or risk register that are rated more likely than the outcomes they contain, and for profiles that feel convincing because each added trait fits.[^s1] In Tversky and Kahneman's data, statistical training helped mainly when the comparison was transparent; even social-science graduate students with several statistics courses committed the fallacy 36% of the time on the Linda problem.[^s1]

## How to counter it

Give the question an extensional framing. In Tversky and Kahneman's health-survey problem, conjunction errors fell from 65% when people gave percentages to 25% when asked "how many of 100 men", and to 11% when they first counted the broader group and then the subset.[^s1] Checking whether the short claim includes the long one, and pricing each step of a scenario separately before multiplying, does the same work. The critical questions above walk through these checks.[^s1][^s3]

## Evidence

The effect is reproducible but sensitive to wording and content. A 2021 pre-registered close replication with 1,032 participants found a conjunction effect for the Linda profile and no support for the idea that ambiguity in the word "and" causes it. A parallel profile about a man named James showed no effect at all, which the authors read as a sign that conjunction effects are real yet context-dependent.[^s3]

The interpretation is disputed. Ralph Hertwig and Gerd Gigerenzer (1999) argued that many participants read "probability" in the Linda problem in ordinary, non-mathematical senses, such as plausibility, and that contexts and frequency wording that push a mathematical reading reduce violations; on their view, some apparent errors are sensible inferences scored against content-blind norms.[^s2] Others treat the error as a genuine reasoning bias, and a 2015 commentary notes that people still favour conjunctive bets even when the presentation is transparent.[^s4] Formal accounts continue to appear: Trpin and Hartmann (2024) proposed that people judge which hypotheses best explain the evidence, a modelling account that the authors flag as not yet tested experimentally.[^s5]

## Connections

- **Introduced by** Amos Tversky and Daniel Kahneman, whose 1983 Linda-problem study is the landmark **demonstration**.[^s1]
- **Explained by** the representativeness heuristic: resemblance to a description displaces the inclusion rule.[^s1]
- **Supported by** the 2021 Meta-Psychology replication, which found the Linda effect again while showing it does not appear for every profile.[^s3]
- **Challenged by** Hertwig and Gigerenzer's semantic account of how people read "probability".[^s2]
- **Studied in** judgment and decision making, where it remains a standard test case for theories of probability judgment.[^s4][^s5]
- **Related to** base-rate neglect and natural frequencies (frequency formats reduce both errors) and to the heuristics-and-biases program that produced it.[^s1][^s2]

## Sources

[^s1]: Tversky & Kahneman, "Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment", Psychological Review 90(4), 1983. https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf (accessed 2026-11-07)
[^s2]: Hertwig & Gigerenzer, "The 'conjunction fallacy' revisited: How intelligent inferences look like reasoning errors", Journal of Behavioral Decision Making 12(4), 1999. https://edoc.unibas.ch/8522/ (accessed 2026-11-07)
[^s3]: Chandrashekar et al., "Frequency estimation and semantic ambiguity do not eliminate conjunction bias, when it occurs", Meta-Psychology 5, 2021. https://open.lnu.se/index.php/metapsychology/article/view/2474 (accessed 2026-11-07)
[^s4]: Lewinski, "Commentary: Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment", Frontiers in Psychology 6, 2015. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01832/full (accessed 2026-11-07)
[^s5]: Trpin & Hartmann, "Explaining the Conjunction Fallacy", Proceedings of the Annual Meeting of the Cognitive Science Society 46, 2024. https://escholarship.org/content/qt4bv1k9nw/qt4bv1k9nw.pdf?t=sgrift (accessed 2026-11-07)
