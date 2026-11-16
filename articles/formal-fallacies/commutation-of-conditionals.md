---
id: ct:commutation-of-conditionals
type: FormalFallacy
title: Commutation of conditionals
aliases: [converting a conditional, conversion of a conditional, swapping a conditional]
domain: formal-fallacies
summary: >-
  The formal fallacy of inferring "if q then p" from "if p then q", swapping
  a conditional's antecedent and consequent as though the relation ran both
  ways. A conditional and its converse are not logically equivalent, so the
  premise can be true while the conclusion is false.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:affirming-the-consequent, ct:illicit-conversion, ct:denying-the-antecedent, ct:inverse-fallacy, ct:method-of-counterexample, ct:necessary-and-sufficient-conditions, ct:material-conditional, ct:conditional-perfection]
requires: [ct:propositional-logic, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:contraposition, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:affirming-the-consequent, source: s4, confidence: medium}
  - {predicate: confusedWith, object: ct:biconditional, source: s5, confidence: medium}
  - {predicate: introducedBy, object: ct:aristotle, source: s2, confidence: medium}
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: medium}
criticalQuestions:
  - Does the conclusion simply reverse the if-clause and then-clause of a conditional that was given as a premise?
  - Is there a realistic case where the original conditional holds but the reversed one fails, because the consequent has some other cause?
  - Was the original statement meant as "if and only if", and if so, has that two-way claim been stated and supported?
  - Would the contrapositive ("if not q then not p"), rather than the converse, give the arguer what they actually need?
argumentMap:
  premises:
    - "If a support ticket is marked urgent, it is answered within an hour."
  conclusion: "If a support ticket is answered within an hour, it was marked urgent."
  verdict: invalid
  scheme: ct:contraposition
  objections:
    - "Routine tickets are also answered within an hour whenever the queue is short."
    - "The policy guarantees speed for urgent tickets; it says nothing about which tickets get fast answers."
sources:
  - id: s1
    title: "On Sophistical Refutations, Part 5 (trans. W. A. Pickard-Cambridge)"
    publisher: Aristotle; The Internet Classics Archive, MIT
    url: https://classics.mit.edu/Aristotle/sophist_refut.1.1.html
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, rev. 2024)
    url: https://plato.stanford.edu/ENTRiES/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s3
    title: "1.1.7: More forms of implication"
    publisher: "Delftse Foundations of Computation (Hugtenburg & Yorke-Smith, TU Delft Open), Engineering LibreTexts"
    url: https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Delftse_Foundations_of_Computation/01%3A_Logic/1.01%3A_Propositional_Logic/1.1.07%3A_More_forms_of_implication
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "Commutation of Conditionals"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/commcond.html
    type: community
    accessed: 2026-11-16
  - id: s5
    title: "The Abstract Selection Task: New Data and an Almost Comprehensive Model"
    publisher: "Journal of Experimental Psychology: Learning, Memory, and Cognition 33(4), 680-703 (Klauer, Stahl & Erdfelder, 2007), author's copy"
    url: https://methexp.uni-koeln.de/files/Klauer-Stahl-Erdfelder-2007.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Commutation of conditionals

Commutation of conditionals is the invalid immediate inference "If p, then q; therefore, if q, then p." The arguer takes a conditional and concludes its converse, with the two parts swapped.[^s4] A conditional and its converse are not logically equivalent: one can be true while the other is false. Asserting both at once is a stronger claim, the biconditional "p if and only if q".[^s3] Rain makes the streets wet, but wet streets do not guarantee rain, since a burst pipe or a street sweeper would do the same.[^s4] Because the gap lies in the form and not in the subject matter, the mistake is a formal fallacy.[^s3][^s4]

## Origin

Aristotle described the error in *On Sophistical Refutations* as the refutation that depends on the consequent. People assume that consequence is convertible: because B follows whenever A holds, they suppose A must hold whenever B does. His examples are inferring rain from wet ground and mistaking yellow bile for honey because both are yellow.[^s1] Hansen's survey for the Stanford Encyclopedia notes that Aristotle listed this among the fallacies not dependent on language and gave the case of a hot man who need not have a fever, although a feverish man is hot. Modern readers often treat this fallacy as an early version of affirming the consequent.[^s2] Curtis argues that Aristotle's wording, about reversing the relation of consequence, fits commuting a conditional at least as closely.[^s4]

## How it works

The fallacy imitates a valid move. Contraposition also swaps the two parts of a conditional but negates both, giving "if not q, then not p", and that contrapositive is equivalent to the original.[^s3] Commutation does the swap without the negations, so the result says something new that the premise never claimed.[^s3][^s4]

In the argument map above, a help desk promises that urgent tickets are answered within an hour. A manager reviewing a fast-answered ticket concludes it must have been urgent. Yet routine tickets also get quick replies when the queue is short. The policy states a sufficient condition for a fast answer, not a necessary one. The valid inference available is the contrapositive: a ticket that waited more than an hour was not marked urgent, assuming the policy holds.[^s3]

## How to spot it

Look for a conclusion that is itself a conditional and that reuses the premise's two clauses in reverse order.[^s4] It differs from affirming the consequent. That fallacy adds a premise asserting q and concludes p outright, whereas commutation draws the general reversed rule.[^s4] Test the form by keeping the premise true and imagining a case where q holds through some other route while p is false.[^s4] Curtis notes one exception: when the two components are logically equivalent, the converse holds too. Mathematical definitions written as "if" usually mean "if and only if", so converting them there is harmless.[^s4]

## How to counter it

Ask whether the speaker meant a two-way claim. If so, state the biconditional explicitly and support each direction separately.[^s3] If only the one-way conditional is supported, offer the contrapositive as the conclusion the evidence licenses.[^s3] Curtis suggests the error may persist because "and", "or" and "if and only if" are all commutative, so the habit of swapping freely carries over to "if".[^s4]

## Evidence

Reversed readings of a conditional are measurable in the laboratory. In a 2007 study modelling the abstract selection task, Klauer, Stahl and Erdfelder included a parameter for reading the rule in the reverse direction. They estimated it at roughly 10 to 18 percent for "if" rules in control groups, and at over half for rules phrased with "only if".[^s5] Their estimates also suggested about half of responses reflected a biconditional reading, which nearly always took the two-directional form that includes the converse.[^s5] These are model estimates for one task, not direct counts of people committing the fallacy, but they indicate that treating "if" as running both ways is common and sensitive to wording.[^s5]

## Connections

- **Invalid form of contraposition.** Contraposition swaps and negates the parts and is equivalent to the original; commutation swaps without negating and is not.[^s3]
- **Contrasts with affirming the consequent.** Both reverse the direction of consequence; affirming the consequent draws a categorical conclusion from an extra premise, commutation draws the converse conditional.[^s4]
- **Confused with the biconditional.** Reading "if" as "if and only if" makes the converse look like part of what was said.[^s3][^s5]
- **Introduced by Aristotle in *Sophistical Refutations*.** His refutation from the consequent turns on treating consequence as convertible.[^s1][^s2]
- **Related to the inverse and to denying the antecedent.** Swapping a conditional is distinct from negating both parts in place, the inverse "if not p, then not q", which is also not equivalent to the original.[^s3]

## Sources

[^s1]: Aristotle, *On Sophistical Refutations*, Part 5, trans. W. A. Pickard-Cambridge, The Internet Classics Archive. https://classics.mit.edu/Aristotle/sophist_refut.1.1.html (accessed 2026-11-16)
[^s2]: Hansen, "Fallacies", *Stanford Encyclopedia of Philosophy* (rev. 2024). https://plato.stanford.edu/ENTRiES/fallacies/ (accessed 2026-11-16)
[^s3]: Hugtenburg & Yorke-Smith, "More forms of implication", *Delftse Foundations of Computation*, TU Delft Open. https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Delftse_Foundations_of_Computation/01%3A_Logic/1.01%3A_Propositional_Logic/1.1.07%3A_More_forms_of_implication (accessed 2026-11-16)
[^s4]: Curtis, "Commutation of Conditionals", The Fallacy Files. https://fallacyfiles.org/commcond.html (accessed 2026-11-16)
[^s5]: Klauer, Stahl & Erdfelder, "The Abstract Selection Task: New Data and an Almost Comprehensive Model", *JEP: LMC* 33(4), 2007. https://methexp.uni-koeln.de/files/Klauer-Stahl-Erdfelder-2007.pdf (accessed 2026-11-16)
