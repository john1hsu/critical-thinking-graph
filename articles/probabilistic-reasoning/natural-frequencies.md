---
id: ct:natural-frequencies
type: Technique
title: Natural frequency format
aliases: [natural frequencies, frequency formats, natural frequency representation, natural sampling format]
domain: probabilistic-reasoning
summary: >-
  A way of presenting or re-expressing risk information as counts of cases
  drawn from one concrete reference group (for example "8 of the 10 people
  with the condition test positive") instead of as conditional probabilities,
  so that the base rate stays visible and Bayesian updating becomes simple
  counting.
level: introductory
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:bayesian-reasoning, ct:base-rate-neglect, ct:risk-communication, ct:nested-sets-hypothesis]
requires: [ct:conditional-probability]
relations:
  - {predicate: counteracts, object: ct:base-rate-neglect, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:gerd-gigerenzer, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:ulrich-hoffrage, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:gigerenzer-hoffrage-1995-frequency-formats-study, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:risk-communication, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:nested-sets-hypothesis, source: s5, confidence: medium}
  - {predicate: supportedBy, object: ct:mcdowell-jacobs-2017-natural-frequencies-meta-analysis, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "How to improve Bayesian reasoning without instruction: Frequency formats"
    publisher: Psychological Review 102(4), 684-704 (Gigerenzer & Hoffrage, 1995), UC San Diego course copy
    url: https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s2
    title: "Communicating statistical information"
    publisher: Science 290(5500), 2261-2262 (Hoffrage, Lindsey, Hertwig & Gigerenzer, 2000), Max Planck Society repository
    url: https://pure.mpg.de/pubman/item/item_2102628_7/component/file_2102627/UH_Communicating_2000.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s3
    title: "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies: Frequency Phobia in Spite of Probability Blindness"
    publisher: Frontiers in Psychology 9, 1833 (Weber, Binder & Krauss, 2018)
    url: https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01833/text
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "When intuitive Bayesians need to be good readers: The problem-wording effect on Bayesian reasoning"
    publisher: Cognition 245, 105722 (Sirota, Navarrete & Juanchich, 2024), University of Essex repository
    url: https://repository.essex.ac.uk/37751/1/1-s2.0-S0010027724000088-main.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Base-rate respect: From statistical formats to cognitive structures"
    publisher: Behavioral and Brain Sciences 30(3) (Barbey & Sloman, 2007, authors' response), Cambridge University Press
    url: https://core-cms.cambridgecore.org/core/journals/behavioral-and-brain-sciences/article/baserate-respect-from-statistical-formats-to-cognitive-structures/9DAADA1F4F18D0E10457D548E02A78F1
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Natural frequency format

A natural frequency format states statistical information as counts from a single, concrete group of cases rather than as conditional probabilities. Instead of "the prevalence is 1%, the test detects 80% of cases and gives a false alarm 9.6% of the time", it says: out of 1,000 people, 10 have the condition; 8 of those 10 test positive; 95 of the other 990 also test positive.[^s1] Each count is nested inside the one before it, so the base rate is never dropped, and the probability of having the condition after a positive result is simply 8 out of the 8 + 95 who tested positive, about 8%.[^s1] Used deliberately, re-expressing a problem this way is one of the best-studied remedies for base-rate neglect.[^s1][^s3]

## Origin

Gerd Gigerenzer and Ulrich Hoffrage introduced the idea in a 1995 *Psychological Review* paper on improving Bayesian reasoning without any instruction.[^s1] They distinguished three formats that carry the same numbers. A standard probability format gives single-event probabilities about one person; a relative frequency format gives percentages of a group; a natural frequency format gives raw counts as they would accumulate by observing cases one at a time, which they called natural sampling.[^s1] Only the last changes the arithmetic, because counts obtained by natural sampling already reflect the base rate.[^s1]

## How it works

In the probability format, Bayes' theorem requires multiplying and adding fractions. In the natural frequency format, it collapses to dividing one count by the sum of two counts, using whole numbers and fewer steps.[^s1] Gigerenzer and Hoffrage also offered an evolutionary argument: humans and other animals learned about risk from encountered cases, not from percentages, so the mind should handle counts more easily.[^s1] That second claim is more speculative than the computational one.

A workplace example: a factory inspection camera catches 90% of defective parts, wrongly rejects 5% of good parts, and about 2% of parts are defective. A shift lead sees a rejection and assumes the part is almost certainly bad. Recast it: of 1,000 parts, 20 are defective and the camera rejects 18 of them; of the 980 good parts, it also rejects 49. So only 18 of 67 rejected parts, roughly 27%, are actually defective, which is a reason to re-inspect rejects rather than scrap them. The calculation follows the same nested-count steps Gigerenzer and Hoffrage used for their screening problems, so anyone can check it.[^s1]

## How to apply it

1. **Pick a round reference group** large enough that the smallest subgroup is a whole number (100, 1,000 or 10,000 cases).[^s2]
2. **Split by the base rate first:** how many in the group have the condition and how many do not.[^s1]
3. **Split each branch by the evidence:** how many with the condition show the signal (true positives) and how many without it show it anyway (false positives).[^s1]
4. **Answer as "out of":** true positives divided by all positives.[^s1]
5. **When communicating to others**, give the counts rather than percentages or relative risk reductions, and teach people to translate probabilities into counts rather than to plug numbers into Bayes' rule.[^s2]

Pitfalls: normalised frequencies (every subgroup rescaled to 100) remove the base-rate information and lose the benefit, and awkward wording can erase it even when the counts are correct.[^s1][^s4]

## Evidence

In Gigerenzer and Hoffrage's first study, 60 students solved 15 problems; Bayesian answers rose from 16% under the standard probability format to 46% under the standard frequency format, and up to 50% with a shorter frequency menu.[^s1] Hoffrage and colleagues reported in *Science* in 2000 that only 1 of 24 physicians answered a colorectal cancer screening question correctly with probabilities, against 16 of 24 with natural frequencies; with DNA match evidence, correct inferences rose from 13% to 68% among trainee judges and from under 1% to 44% among law students.[^s2]

The gains are real but smaller than early results suggested. A 2017 meta-analysis by McDowell and Jacobs, as summarised by Weber and colleagues in 2018, found about 4% correct with probabilities and 24% with natural frequencies, so most people still fail; Weber's team found many participants converted the counts back into probabilities.[^s3] A 2024 set of seven experiments with 4,909 adults found that natural frequencies helped only when the problem was clearly worded; with standard wording they did no better than probabilities.[^s4] Hence the status here is *mixed*.

There is also a dispute over why the format works. Barbey and Sloman argued that the benefit comes from making the nested relations between sets transparent, not from frequencies as such, and defended a dual-process reading against the natural frequency hypothesis.[^s5]

## Connections

- **Counteracts** base-rate neglect by keeping the prior inside the counts.[^s1]
- **Introduced by** Gerd Gigerenzer and Ulrich Hoffrage, and **demonstrated by** their 1995 frequency-formats study.[^s1]
- **Applied in** risk communication in medicine and law, such as screening results and DNA evidence.[^s2]
- **Supported by** the McDowell and Jacobs meta-analysis, which confirms a benefit while showing most people still err.[^s3]
- **Challenged by** the nested-sets hypothesis, which credits set structure rather than frequency itself.[^s5]
- **Related to** Bayesian reasoning, the normative standard it makes tractable, and **requires** conditional probability.[^s1]

## Sources

[^s1]: Gigerenzer & Hoffrage, "How to improve Bayesian reasoning without instruction: Frequency formats", Psychological Review 102(4), 1995. https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf (accessed 2026-11-04)
[^s2]: Hoffrage, Lindsey, Hertwig & Gigerenzer, "Communicating statistical information", Science 290, 2000. https://pure.mpg.de/pubman/item/item_2102628_7/component/file_2102627/UH_Communicating_2000.pdf (accessed 2026-11-04)
[^s3]: Weber, Binder & Krauss, "Why Can Only 24% Solve Bayesian Reasoning Problems in Natural Frequencies", Frontiers in Psychology 9, 2018. https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01833/text (accessed 2026-11-04)
[^s4]: Sirota, Navarrete & Juanchich, "When intuitive Bayesians need to be good readers", Cognition 245, 2024. https://repository.essex.ac.uk/37751/1/1-s2.0-S0010027724000088-main.pdf (accessed 2026-11-04)
[^s5]: Barbey & Sloman, "Base-rate respect: From statistical formats to cognitive structures", Behavioral and Brain Sciences 30(3), 2007. https://core-cms.cambridgecore.org/core/journals/behavioral-and-brain-sciences/article/baserate-respect-from-statistical-formats-to-cognitive-structures/9DAADA1F4F18D0E10457D548E02A78F1 (accessed 2026-11-04)
