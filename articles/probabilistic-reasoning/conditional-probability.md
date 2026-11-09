---
id: ct:conditional-probability
type: Concept
title: Conditional probability
aliases: [probability of A given B, P(A|B), relative probability]
domain: probabilistic-reasoning
summary: >-
  The probability that one event occurs given that another event occurs,
  standardly defined as the probability of both divided by the probability of
  the conditioning event (when that is above zero); the building block of
  Bayesian updating, independence and most statistical evidence.
level: introductory
evidenceStatus: normative
broader: [ct:probability-theory]
related: [ct:bayesian-reasoning, ct:base-rate-neglect, ct:natural-frequencies, ct:simpsons-paradox, ct:gamblers-fallacy, ct:conjunction-fallacy, ct:inverse-fallacy, ct:statistical-literacy]
requires: []
relations:
  - {predicate: formalizedBy, object: ct:andrey-kolmogorov, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:what-conditional-probability-could-not-be, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:joint-probability, source: s4, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Foundations of the Theory of Probability (English translation of Grundbegriffe der Wahrscheinlichkeitsrechnung, 1933)"
    publisher: Chelsea Publishing, New York (Kolmogorov, trans. ed. Morrison, 1950), Internet Archive scan
    url: https://dn790007.ca.archive.org/0/items/foundationsofthe00kolm/foundationsofthe00kolm.pdf
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Interpretations of Probability"
    publisher: Stanford Encyclopedia of Philosophy (Winter 2003 archive edition)
    url: https://plato.stanford.edu/archives/win2003/entries/probability-interpret/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s3
    title: "What Conditional Probability Could Not Be"
    publisher: Synthese 137, 273–323 (Hájek, 2003), course-hosted copy
    url: https://mail.joelvelasco.net/teaching/3865/hajekwhatcpcouldntbe.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Assessing Prospective Secondary School Teachers' Biases in Conditional Probability Reasoning"
    publisher: Bolema 26(44), 1207–1225 (Díaz, Contreras, Batanero & Roa, 2012)
    url: https://www.redalyc.org/pdf/2912/291226280007.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "The inverse fallacy: An account of deviations from Bayes's theorem and the additivity principle"
    publisher: Memory & Cognition 30(2), 171–178 (Villejoubert & Mandel, 2002), Kingston University repository record
    url: https://eprints.kingston.ac.uk/6308
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Conditional probability

A conditional probability is the probability of one event once we restrict attention to cases where another event holds: the probability of A *given* B, written P(A|B). In the standard treatment it equals the probability that both occur divided by the probability of B, and it is defined only when B has a probability above zero.[^s1][^s2] Much everyday statistical evidence is a conditional probability in disguise: a test's sensitivity is the chance of a positive result given disease.

## Origin

Gamblers and mathematicians reasoned about probabilities "after something has happened" long before anyone gave the idea a formal definition. The modern textbook definition comes from Andrey Kolmogorov's 1933 *Grundbegriffe der Wahrscheinlichkeitsrechnung*, translated into English in 1950 as *Foundations of the Theory of Probability*.[^s1] In its first chapter Kolmogorov defines the conditional probability of B given A as the ratio of P(AB) to P(A), provided P(A) is positive, and derives from it the multiplication theorem, the theorem of total probability and Bayes' theorem; he then characterizes independent events as those whose conditional probabilities equal their unconditional ones.[^s1] Philosophers note that this ratio is often called a definition but may only approximate the everyday concept, and some authors, including Popper and Rényi, instead take conditional probability as the primitive notion and axiomatize it directly.[^s2]

## How it works

Read P(A|B) as "of all the B cases, what share are also A?" Conditioning shrinks the reference group to B and asks how A is distributed inside it. Three rules follow from the ratio definition.[^s1]

1. **Multiplication:** P(A and B) = P(B) × P(A|B). The chance of both is the chance of the condition times the chance of the outcome within it.[^s1]
2. **Bayes' theorem:** P(B|A) = P(B) × P(A|B) / P(A). The two directions are linked, but only through the base rates P(A) and P(B), so they are generally different numbers.[^s1]
3. **Independence:** A and B are independent exactly when P(A|B) = P(A), that is, when learning B tells you nothing about A.[^s1]

Conditional probability is also the engine of Bayesian learning: an agent who becomes certain of evidence E should set its new probability for any claim X equal to its old P(X|E), a rule known as conditioning or conditionalization.[^s2]

**Workplace example.** An incident review finds that 80% of last quarter's production outages followed a Friday deployment, and someone proposes banning Friday releases because "Friday deploys usually cause outages." The 80% figure is P(Friday deploy | outage). The claim needs P(outage | Friday deploy). If the team ships 200 releases on Fridays and 10 outages occurred, of which 8 followed Friday releases, then only 8 of 200, or 4%, of Friday deploys were followed by an outage. That is a very different number from 80%. Swapping the condition and the outcome is the inverse fallacy.[^s5]

## How to apply it

- Say the probability out loud as "of all the ___, what share are ___?" and check that the first blank is the group the decision is actually about.[^s4]
- Before acting on P(A|B), ask for the base rates. Moving from P(B|A) to P(A|B) requires P(A) and P(B); without them the inversion is a guess.[^s1]
- Keep "given" apart from "and": P(A|B) is not the probability that A and B both happen.[^s4]
- Don't read conditioning as causation or as running forward in time. A later event can condition an earlier one, and a strong conditional link can be pure association.[^s4]
- Don't confuse independence with mutual exclusivity. Mutually exclusive events with positive probabilities are strongly dependent, since one rules the other out.[^s1][^s4]

## Evidence and limitations

People with mathematical training still stumble. A 2012 study gave seven items from a conditional-probability reasoning questionnaire to 196 prospective secondary-school mathematics teachers in Spain. More than half transposed the conditional on one item, roughly two in three on another item reasoned as if a conditioning event had to come earlier in time, and large minorities mixed up joint and conditional probability or treated independent events as mutually exclusive. Only 13 participants showed none of the biases, and 42.8% showed three or more.[^s4] Experimental work in cognitive psychology finds that when asked for P(H|D), people often report something close to P(D|H). In a study of 45 participants, the size of that inverse error predicted how far their answers strayed from Bayes' theorem and from the rule that P(H|D) and P(not-H|D) should sum to one.[^s5]

Philosophically, the ratio definition has a known gap. Alan Hájek argues that it fails whenever the conditioning event has zero, vague or undefined probability. For example, the chance that a point drawn at random from a continuous range equals some value x, given that it equals x, is plainly 1, yet the ratio is 0/0. He concludes that the ratio should be treated as a constraint that holds when both terms are well defined, with conditional probability itself as the primitive notion.[^s3] For everyday discrete problems this debate changes nothing; it matters in continuous models, decision theory and the foundations of statistics.[^s3]

## Connections

- **Formalized by Andrey Kolmogorov.** His 1933 axioms supply the ratio definition and derive the multiplication rule, total probability and Bayes' theorem from it.[^s1]
- **Challenged by "What Conditional Probability Could Not Be."** Hájek's 2003 paper argues that the ratio analysis breaks down for zero-, vague- and undefined-probability conditions and that conditional probability should be primitive.[^s3]
- **Commonly confused with joint probability.** Treating P(A|B) as P(A and B) was among the most frequent errors in the 2012 teacher study.[^s4]
- **Studied in cognitive psychology.** Experiments on the inverse fallacy measure how people's conditional judgments deviate from Bayes' theorem and additivity.[^s5]
- **Required by Bayesian reasoning, base-rate neglect, natural frequencies, Simpson's paradox and the gambler's fallacy.** Conditionalization, base rates and independence are all defined through conditional probability.[^s1][^s2]
- **Related to the inverse fallacy and the conjunction fallacy.** The inverse fallacy swaps condition and outcome; conjunction errors, also measured in the teacher study, misjudge the probability of "A and B" relative to its parts.[^s4][^s5]

## Sources

[^s1]: Kolmogorov, *Foundations of the Theory of Probability*, English translation ed. N. Morrison, Chelsea Publishing (1950), of *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933). https://dn790007.ca.archive.org/0/items/foundationsofthe00kolm/foundationsofthe00kolm.pdf (accessed 2026-11-09)
[^s2]: "Interpretations of Probability", Stanford Encyclopedia of Philosophy, Winter 2003 archive edition. https://plato.stanford.edu/archives/win2003/entries/probability-interpret/ (accessed 2026-11-09)
[^s3]: Hájek, "What Conditional Probability Could Not Be", *Synthese* 137 (2003): 273–323. https://mail.joelvelasco.net/teaching/3865/hajekwhatcpcouldntbe.pdf (accessed 2026-11-09)
[^s4]: Díaz, Contreras, Batanero & Roa, "Assessing Prospective Secondary School Teachers' Biases in Conditional Probability Reasoning", *Bolema* 26(44) (2012): 1207–1225. https://www.redalyc.org/pdf/2912/291226280007.pdf (accessed 2026-11-09)
[^s5]: Villejoubert & Mandel, "The inverse fallacy: An account of deviations from Bayes's theorem and the additivity principle", *Memory & Cognition* 30(2) (2002): 171–178. https://eprints.kingston.ac.uk/6308 (accessed 2026-11-09)
