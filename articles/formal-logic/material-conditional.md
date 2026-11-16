---
id: ct:material-conditional
type: Concept
title: Material conditional
aliases: [material implication, truth-functional conditional, Philonian conditional, horseshoe conditional]
domain: formal-logic
summary: >-
  The truth-functional "if P then Q" of classical logic, written P → Q or
  P ⊃ Q, which is false only when P is true and Q is false and true in every
  other case. It is equivalent to "not-P or Q".
level: introductory
evidenceStatus: normative
broader: [ct:conditional-statement]
related: [ct:truth-table, ct:modus-ponens, ct:necessary-and-sufficient-conditions, ct:commutation-of-conditionals, ct:eliminating-counterexamples, ct:logical-consequence, ct:stoic-logic, ct:diodorus-cronus, ct:sextus-empiricus, ct:conversational-implicature, ct:wason-selection-task, ct:conditional-perfection]
requires: [ct:truth-table]
relations:
  - {predicate: partOf, object: ct:propositional-logic, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:philo-the-dialectician, source: s2, confidence: medium}
  - {predicate: formalizedBy, object: ct:gottlob-frege, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:strict-conditional, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:counterfactual-conditional, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:conditional-probability, source: s5, confidence: high}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "The Logic of Conditionals"
    publisher: Stanford Encyclopedia of Philosophy (Hans Rott, 2021)
    url: https://plato.stanford.edu/entries/logic-conditionals/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s2
    title: "Dialectical School"
    publisher: Stanford Encyclopedia of Philosophy (Susanne Bobzien, 2004, rev. 2011; Summer 2021 archive)
    url: https://plato.stanford.edu/archives/sum2021/entries/dialectical-school/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s3
    title: "Truth-functional connectives (Chapter 10)"
    publisher: "forall x: Calgary. An Introduction to Formal Logic (Magnus, Button et al.; Open Logic Project)"
    url: https://forallx.openlogicproject.org/html/Ch10.html
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "On Assertion and Indicative Conditionals"
    publisher: "The Philosophical Review 88(4): 565-589 (Frank Jackson, 1979)"
    url: https://sites.unimi.it/zucchi/NuoviFile/jackson1979.pdf
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Conditionals and conditional probability"
    publisher: "Journal of Experimental Psychology: Learning, Memory, and Cognition 29(2): 321-335 (Evans, Handley & Over, 2003)"
    url: https://researchers.mq.edu.au/en/publications/conditionals-and-conditional-probability/
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Material conditional

The material conditional is the "if…then" of classical propositional logic, usually written P → Q or P ⊃ Q. It is truth-functional: its truth value depends only on the truth values of its antecedent P and its consequent Q. It is false in exactly one case, when P is true and Q is false, and true in the other three.[^s1][^s3] It therefore says the same thing as "not-P or Q", and it asserts no causal or explanatory link between the two parts.[^s3] It is the standard tool for representing conditional claims in logic, and it also produces well-known mismatches with how people use "if" in ordinary speech.[^s1]

## Origin

The idea is ancient. Philo the Dialectician, a logician of the early Hellenistic Dialectical school, held that a conditional is false only when it leads from a truth to a falsehood. This report survives through Sextus Empiricus. Bobzien notes that it comes very close to modern material implication, except that Philo let a conditional's truth change over time.[^s2] His teacher Diodorus Cronus demanded more: a conditional is true only if it neither was nor is possible for the antecedent to be true and the consequent false. That stronger reading anticipates the modern strict conditional.[^s2] In modern logic, the two-valued conditional became standard through Frege's 1879 logic and Whitehead and Russell's *Principia Mathematica* (1910). It was prized for its simplicity, its truth-functionality, its definability from negation and disjunction, and its fit with mathematical proof.[^s1]

## How it works

The textbook argument for the truth table, adapted from Dorothy Edgington, starts from a general claim such as "if any shape is grey, it is circular". If the claim has no counterexample, every instance must be true. That includes instances about shapes that are not grey, whether or not they are circular. Only a grey shape that is not circular makes an instance false.[^s3] So a false antecedent makes the conditional true, whatever the consequent.[^s3]

A workplace example: a release policy says, "If the build fails, the release is postponed." Read materially, the policy is broken only by a failed build followed by a release on schedule. A week with a green build tells you nothing against it, whether the release shipped or was delayed for some other reason. This is useful when checking compliance, because you only need to search for one kind of case.[^s3] The same reading explains why the material conditional licenses modus ponens and modus tollens but not the converse, since "if Q then P" has a different falsifying case.[^s1][^s3]

## Limitations and the paradoxes

Because a false antecedent or a true consequent is enough to make P → Q true, the material reading yields the "paradoxes of material implication". C. I. Lewis pointed out in 1912 that any conditional follows from the falsity of its antecedent and from the truth of its consequent. Hugh MacColl had already noted in 1908 that, for any two sentences, one must "imply" the other.[^s1] Lewis responded by proposing a non-truth-functional strict conditional.[^s1] Counterfactuals show the gap clearly. Two subjunctive conditionals can have false antecedents and false consequents while one is true and the other false, so English "would" conditionals are not truth-functional.[^s3] Quine observed that, read materially, every counterfactual would be vacuously true.[^s1]

Indicative conditionals are disputed. Frank Jackson defended the view that indicative "if P, Q" has exactly the truth conditions of P → Q. On his account, the odd cases are true but unassertable. "If" signals that the conditional is robust, meaning it would stay probable even if one learned P. Jackson argued that a purely Gricean "assert the stronger claim" maxim cannot explain the data on its own.[^s4] Critics reply with Adams's thesis, which says the probability of a conditional is the conditional probability of Q given P. For a fair die, "if it lands even, it lands six" has probability 1/3, but the material conditional has probability 2/3.[^s1]

## Evidence

The psychology of reasoning tests how people actually interpret "if". In three experiments published in 2003, Evans, Handley and Over gave participants the frequencies of the four possible cases and asked them to judge the probability of "if p then q". The material conditional's probability did not predict the judgments. About half the participants tracked the conditional probability, and most of the rest tracked the probability of the conjunction "p and q".[^s5] These findings support treating the material conditional as a normative logical tool rather than a description of everyday understanding.[^s5][^s1]

## Connections

- **Part of propositional logic.** It is one of the core connectives of truth-functional logic and is defined by its truth table.[^s3]
- **Introduced (in ancient form) by Philo the Dialectician**, whose truth condition is the closest ancient match to the modern definition.[^s2]
- **Formalized by Gottlob Frege**, whose 1879 logic, along with *Principia Mathematica*, made the two-valued conditional standard.[^s1]
- **Contrasts with the strict conditional**, Lewis's modal answer to the paradoxes, which Diodorus anticipated.[^s1][^s2]
- **Contrasts with the counterfactual conditional**, which no truth table can capture.[^s3]
- **Contrasts with conditional probability.** Adams's thesis and the 2003 experiments link the meaning of "if" to P(Q|P), not to the probability of not-P or Q.[^s5][^s1]
- **Studied in the psychology of reasoning**, where the material reading serves as the baseline that people's judgments depart from.[^s5]
- **Related:** necessary and sufficient conditions and commutation of conditionals, since P → Q makes P sufficient and Q necessary and cannot be safely reversed.[^s3]

## Sources

[^s1]: Rott, "The Logic of Conditionals", Stanford Encyclopedia of Philosophy, 2021. https://plato.stanford.edu/entries/logic-conditionals/ (accessed 2026-11-16)
[^s2]: Bobzien, "Dialectical School", Stanford Encyclopedia of Philosophy, Summer 2021 edition. https://plato.stanford.edu/archives/sum2021/entries/dialectical-school/ (accessed 2026-11-16)
[^s3]: Magnus, Button et al., "Truth-functional connectives", *forall x: Calgary*, ch. 10. https://forallx.openlogicproject.org/html/Ch10.html (accessed 2026-11-16)
[^s4]: Jackson, "On Assertion and Indicative Conditionals", *The Philosophical Review* 88(4), 1979. https://sites.unimi.it/zucchi/NuoviFile/jackson1979.pdf (accessed 2026-11-16)
[^s5]: Evans, Handley & Over, "Conditionals and conditional probability", *Journal of Experimental Psychology: LMC* 29(2), 2003. https://researchers.mq.edu.au/en/publications/conditionals-and-conditional-probability/ (accessed 2026-11-16)
