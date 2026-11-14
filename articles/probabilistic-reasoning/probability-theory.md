---
id: ct:probability-theory
type: Field
title: Probability theory
aliases: [calculus of probability, mathematical probability, theory of probability]
domain: probabilistic-reasoning
summary: >-
  The branch of mathematics that studies uncertainty: it assigns numbers
  between 0 and 1 to events and fixes the rules (in modern form,
  Kolmogorov's 1933 axioms) by which those numbers must combine. It is the
  formal standard against which reasoning about chance and evidence is
  judged.
level: introductory
evidenceStatus: normative
broader: [ct:mathematics]
related: [ct:conditional-probability, ct:bayesian-reasoning, ct:statistical-reasoning, ct:expected-value, ct:conjunction-fallacy, ct:abraham-de-moivre, ct:christiaan-huygens, ct:interpretations-of-probability]
requires: []
relations:
  - {predicate: introducedBy, object: ct:blaise-pascal, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:pierre-de-fermat, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:andrey-kolmogorov, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:judgment-and-decision-making, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Interpretations of Probability"
    publisher: Stanford Encyclopedia of Philosophy (Hájek, 2002; revised 2023)
    url: https://plato.stanford.edu/ENTRIES/probability-interpret/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "The Sources of Kolmogorov's Grundbegriffe"
    publisher: Statistical Science 21(1), 70-98 (Shafer & Vovk, 2006), arXiv reprint of the published article
    url: https://arxiv.org/pdf/math/0606533
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Introduction to Probability (2nd ed.)"
    publisher: American Mathematical Society (Grinstead & Snell, 2003), Dartmouth CHANCE edition
    url: https://math.dartmouth.edu/~m20s16/prob.pdf
    type: textbook
    accessed: 2026-11-14
  - id: s4
    title: "Extensional vs. Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment"
    publisher: Office of Naval Research technical report (Tversky & Kahneman, 1983), published in Psychological Review 90(4)
    url: https://apps.dtic.mil/sti/pdfs/ADA131801.pdf
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Probability theory

Probability theory is the mathematical study of uncertainty. It treats the possible outcomes of an experiment as a sample space, calls subsets of that space events, and assigns each event a number between 0 and 1 so that certain rules hold: probabilities are never negative, the whole sample space has probability 1, and the probability of either of two incompatible events is the sum of their separate probabilities.[^s3] From these few rules follow the complement rule, the rule that a subset can never be more probable than the set containing it, and the general addition formula for overlapping events.[^s3] For critical thinkers the field matters less as a body of theorems than as a consistency standard: it says which combinations of uncertain beliefs hang together and which do not.[^s1][^s4]

## Origin

Gerolamo Cardano's sixteenth-century book on games of chance was the first systematic attempt to calculate probabilities, mostly by counting equally likely outcomes.[^s3] The field is usually dated to 1654, when Blaise Pascal and Pierre de Fermat corresponded about gambling questions raised by the Chevalier de Méré, including the "problem of points": how to divide the stakes fairly when a game is stopped before anyone has won.[^s3] Pascal solved it by working backwards through a table of averages; Fermat by listing the equally likely ways the game could have continued. Their problems shaped the later work of Huygens, Jacob Bernoulli and de Moivre.[^s3]

For almost three centuries the subject lacked agreed foundations. In 1900 David Hilbert listed the axiomatisation of probability among his famous open problems, and several mathematicians attempted it.[^s2] Andrey Kolmogorov's *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933) settled the matter by recasting probability as a special case of measure theory, drawing on Borel, Lebesgue and Fréchet. Shafer and Vovk's history credits the book with putting probability's modern formalism in place, while showing how much of its mathematics it synthesised rather than invented.[^s2]

## How it works

Kolmogorov's axioms require a field of events, non-negative probabilities, total probability 1 and additivity for disjoint events; a further continuity axiom makes additivity hold for countably infinite collections.[^s2] Kolmogorov defended that last assumption only as a convenient idealisation, and philosophers still dispute it.[^s2][^s1] Conditional probability, the probability of A given B, is defined as the probability of both divided by the probability of B, provided B has positive probability.[^s1]

The calculus constrains how probabilities relate but says nothing about what a probability *is*. Classical, logical, subjective (degree-of-belief), frequency and propensity interpretations each try to supply that meaning, and each meets known objections, such as the reference-class problem for frequencies.[^s1] Defenders of the subjective view argue, through Dutch book arguments due to Ramsey and de Finetti, that anyone whose degrees of belief break the axioms can be offered a set of bets they consider fair yet that lose in every outcome.[^s1]

A workplace example shows the rules at work. A project lead estimates a 60% chance that a supplier delivers on time and an 80% chance that the client signs off on time, then writes in the plan that "both happen" has a 70% chance. No meaning of probability can rescue that figure: the joint event is a subset of each part, so it cannot exceed 60%. If the two events are independent the joint chance is 48%, and dependence can push it no higher than 60%.[^s3]

## Probability theory as a standard for judgment

Amos Tversky and Daniel Kahneman called the conjunction rule, that "A and B" can never be more probable than A, the simplest and most basic qualitative law of probability.[^s4] In their 1983 studies, 85% of 142 undergraduates ranked the description of "Linda" as a feminist bank teller more probable than as a bank teller, and 36% of graduate students with several statistics courses did the same.[^s4] They concluded that intuitive judgment is often not extensional, relying on heuristics such as representativeness, so theories that assume coherent probability judgments are descriptively inadequate even though the rules remain normatively compelling.[^s4] This use of probability theory as a yardstick runs through judgment and decision-making research, and it is also where debates arise about whether a given task really calls for the probability calculus.[^s4][^s1]

## Limitations

The axioms guarantee coherence, not accuracy: a perfectly coherent forecaster can still be badly wrong.[^s1] Choosing an interpretation affects practice, since frequency views struggle with one-off events while subjective views must explain why some coherent priors are better than others.[^s1] Some formal choices, such as countable additivity and conditioning on events of probability zero, remain contested at the foundations.[^s2][^s1]

## Connections

Probability theory is a branch of mathematics whose founding problems came from Pascal and Fermat's 1654 correspondence[^s3] and whose modern axioms were set out by Kolmogorov.[^s2] It supplies the definition of conditional probability[^s1] and the formal core of Bayesian reasoning, statistical reasoning and expected value, which builds on the work of Huygens and de Moivre.[^s3] Its interpretations are a separate philosophical question.[^s1] In judgment and decision-making it serves as the normative benchmark, and violations of its rules, such as the conjunction fallacy, are the classic evidence for heuristics and biases.[^s4]

## Sources

[^s1]: Hájek, "Interpretations of Probability", Stanford Encyclopedia of Philosophy (2002; rev. 2023). https://plato.stanford.edu/ENTRIES/probability-interpret/ (accessed 2026-11-14)
[^s2]: Shafer & Vovk, "The Sources of Kolmogorov's Grundbegriffe", Statistical Science 21(1), 70-98, 2006. https://arxiv.org/pdf/math/0606533 (accessed 2026-11-14)
[^s3]: Grinstead & Snell, Introduction to Probability, 2nd ed., American Mathematical Society, 2003. https://math.dartmouth.edu/~m20s16/prob.pdf (accessed 2026-11-14)
[^s4]: Tversky & Kahneman, "Extensional vs. Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment", ONR technical report, 1983 (Psychological Review 90(4)). https://apps.dtic.mil/sti/pdfs/ADA131801.pdf (accessed 2026-11-14)
