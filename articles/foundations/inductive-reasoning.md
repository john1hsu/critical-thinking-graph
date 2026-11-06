---
id: ct:inductive-reasoning
type: ReasoningMode
title: Inductive reasoning
aliases: [induction, inductive inference, inductive argument]
domain: foundations
summary: >-
  Reasoning in which the premises are meant to make the conclusion probable
  rather than guarantee it, typically by projecting from observed cases to
  unobserved cases, general claims or predictions.
level: introductory
evidenceStatus: normative
broader: [ct:reasoning]
related: [ct:deductive-reasoning, ct:argument, ct:validity, ct:hasty-generalization, ct:argument-from-analogy, ct:bayesian-reasoning, ct:david-hume]
requires: [ct:argument]
relations:
  - {predicate: contrastsWith, object: ct:deductive-reasoning, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: challengedBy, object: ct:problem-of-induction, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:similarity-coverage-model, source: s3, confidence: medium}
argumentMap:
  premises:
    - "In each of the last twelve quarterly releases, the mobile app saw a spike in support tickets during the first week."
    - "Next week's release follows the same process and ships to the same user base."
  conclusion: "Next week's release will probably also cause a first-week spike in support tickets."
  verdict: strong
  objections:
    - "If this release changes the process (for example, a staged rollout), the past pattern may no longer project."
    - "Twelve releases is a modest sample; a coincidence of scheduling could explain the pattern."
sources:
  - id: s1
    title: "Deductive and Inductive Arguments"
    publisher: Internet Encyclopedia of Philosophy (Shanahan)
    url: https://iep.utm.edu/deductive-inductive-arguments/
    type: scholarly-encyclopedia
    accessed: 2026-11-06
  - id: s2
    title: "The Problem of Induction"
    publisher: Stanford Encyclopedia of Philosophy (Henderson, rev. 2022)
    url: https://plato.stanford.edu/ENTRIES/induction-problem/
    type: scholarly-encyclopedia
    accessed: 2026-11-06
  - id: s3
    title: "Properties of inductive reasoning"
    publisher: Psychonomic Bulletin & Review 7(4), 569-592 (Heit, 2000)
    url: https://link.springer.com/content/pdf/10.3758/BF03212996.pdf
    type: peer-reviewed
    accessed: 2026-11-06
created: 2026-11-06
---

# Inductive reasoning

Inductive reasoning is reasoning whose premises are meant to make a conclusion probable rather than certain.[^s1] An inductive argument is strong when its premises, if true, make the conclusion likely, and cogent when it is strong and its premises are actually true.[^s1] Unlike deduction, induction is ampliative: its conclusion says more than the premises contain, which is why it can teach us something new and also why it can be wrong even when every premise is true.[^s1] Most everyday and workplace judgments, from forecasting demand to trusting that a supplier will deliver on time again, are inductive.

## Origin

Aristotle separated the syllogism, where a conclusion follows of necessity, from *epagôgê*, reasoning from particular cases to universals; the latter is the ancestor of what we now call induction.[^s1] Francis Bacon made induction the centrepiece of a reformed science in the *New Organon* (1620), while René Descartes preferred deductive method.[^s1] David Hume then posed the problem that has shadowed induction ever since: in the *Treatise of Human Nature* (1739) and the *Enquiry concerning Human Understanding* (1748) he argued that no non-circular reason shows the future will resemble the past.[^s2]

## How it works

Philosophers group several patterns under the heading of induction.[^s2] Simple enumerative induction moves from "all observed A's have been B" to "the next A will be B" or to "all A's are B".[^s2] Statistical inference moves from a population frequency to an individual case, as in "most members of this group have the trait, so this member probably does".[^s1][^s2] Predictions from a random sample, such as a poll, are another standard case.[^s1]

The argument map above shows a workplace example. Twelve releases in a row produced a first-week spike in support tickets, the next release follows the same process, so another spike is probable. The premises do not guarantee the conclusion; they make it likely, so the right verdict is "strong", not "valid".[^s1] Two features distinguish this from deduction. First, the strength comes in degrees: more releases, or releases under more varied conditions, would make the projection stronger.[^s1][^s3] Second, induction is open to new evidence: learning that this release uses a staged rollout could weaken the conclusion even though no original premise became false.[^s1]

## How to apply it

1. State the projection explicitly: what has been observed, and what unobserved case, generalization or forecast is being inferred from it.[^s1]
2. Check the sample. Ask how many cases support the claim and how varied they were; psychological research shows people treat both larger and more diverse samples as stronger evidence, which matches normative advice.[^s3]
3. Check that the property projects. Stable, causally grounded properties generalize better than incidental ones; whether a feature is likely to carry over depends on why it occurred in the observed cases.[^s3]
4. Look for defeaters: information that the new case differs in a way that matters. A strong argument becomes weak if such a difference turns up.[^s1]
5. Hold the conclusion with matching confidence. Because induction never guarantees its conclusion, the honest output is a probability or a "likely", not a certainty.[^s1][^s2]

## Evidence

Normatively, induction faces Hume's dilemma. A demonstrative argument cannot establish that nature is uniform, since its denial is not contradictory, and any probable argument for uniformity already assumes it, so the justification looks circular.[^s2] Hume concluded that custom or habit, not reason, drives our inductive inferences.[^s2] Responses include Bayesian accounts built on Laplace's rule of succession, Reichenbach's pragmatic vindication of the "straight rule", and Goodman's "grue" riddle, which shows that the same evidence can support incompatible projections, so each inference needs its own grounds for which predicates to project.[^s2]

Descriptively, cognitive psychologists have mapped how people judge inductive strength. Heit's 2000 review in *Psychonomic Bulletin & Review* found reliable effects of premise-conclusion similarity, premise typicality, sample size and premise diversity in adults.[^s3] It also documented departures from normative standards, such as cases where adding a premise lowers judged strength and an inclusion fallacy in category judgments.[^s3] The similarity-coverage model of Osherson and colleagues (1990) explains many of these patterns as a blend of similarity and how well the premises cover the relevant category.[^s3] Heit cautioned that diversity effects are inconsistent in children and across cultures, and that much of the evidence comes from American college students.[^s3]

## Connections

- **Contrasts with deductive reasoning.** Deduction aims at conclusions the premises guarantee; induction aims at conclusions they make probable, and the IEP notes that drawing this line precisely is disputed.[^s1]
- **Introduced by Aristotle.** His *epagôgê*, reasoning from particulars to universals, is the earliest systematic treatment of induction.[^s1]
- **Challenged by the problem of induction.** Hume's argument that induction cannot be justified without circularity is the central philosophical critique.[^s2]
- **Studied in cognitive psychology.** Experiments on category-based induction measure how people judge argument strength and where they diverge from norms.[^s3]
- **Explained by the similarity-coverage model.** Osherson and colleagues' model accounts for similarity, typicality and diversity effects in human induction.[^s3]
- **Related to hasty generalization, argument from analogy and Bayesian reasoning.** Hasty generalization ignores the sample-size and diversity considerations that make an induction strong;[^s3] analogy is a related way of projecting from known to unknown cases, and Bayesian accounts are among the main attempts to put inductive inference on a probabilistic footing.[^s2]

## Sources

[^s1]: Shanahan, "Deductive and Inductive Arguments", Internet Encyclopedia of Philosophy. https://iep.utm.edu/deductive-inductive-arguments/ (accessed 2026-11-06)
[^s2]: Henderson, "The Problem of Induction", Stanford Encyclopedia of Philosophy, rev. 2022. https://plato.stanford.edu/ENTRIES/induction-problem/ (accessed 2026-11-06)
[^s3]: Heit, "Properties of inductive reasoning", *Psychonomic Bulletin & Review* 7(4) (2000), 569-592. https://link.springer.com/content/pdf/10.3758/BF03212996.pdf (accessed 2026-11-06)
