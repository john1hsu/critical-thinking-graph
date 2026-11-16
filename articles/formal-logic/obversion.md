---
id: ct:obversion
type: ReasoningForm
title: Obversion
aliases: [permutation (logic), aequipollence, infinitation, obverse inference]
domain: formal-logic
summary: >-
  The immediate inference that changes the quality of a categorical
  proposition (affirmative to negative or back) and replaces its predicate
  with the predicate's complement, as in "All S are P" to "No S are non-P".
  It is valid for all four standard forms, A, E, I and O, provided the
  complement is formed correctly.
level: introductory
evidenceStatus: normative
broader: [ct:immediate-inference]
related: [ct:rules-of-immediate-inference, ct:conversion, ct:contraposition, ct:categorical-proposition, ct:square-of-opposition, ct:unwarranted-contrast, ct:illicit-contraposition, ct:venn-diagram-test, ct:existential-import, ct:john-buridan, ct:richard-whately]
requires: [ct:categorical-proposition]
relations:
  - {predicate: partOf, object: ct:contraposition, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:law-of-excluded-middle, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:law-of-non-contradiction, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:formal-logic, source: s2, confidence: high}
argumentMap:
  premises:
    - "All parcels in today's outbound batch have been weighed."
  conclusion: "No parcels in today's outbound batch are unweighed (non-weighed) parcels."
  verdict: valid
  objections:
    - "The step holds only if 'unweighed' names everything that is not weighed; a contrary such as 'overweight' would not do."
sameAs: []
sources:
  - id: s1
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Ciola; earlier versions by Parsons; substantive revision 2025)"
    url: https://plato.stanford.edu/ENTRIES/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s2
    title: "3.3 Operations on Categorical Propositions (An Introduction to Logic)"
    publisher: "Kathy Eldred, Pima Community College Open Press (2024, CC BY-NC 4.0)"
    url: https://pimaopen.pressbooks.pub/intrologic/?p=833
    type: textbook
    accessed: 2026-11-16
  - id: s3
    title: "Logic: Deductive and Inductive, Chapter VII: Immediate Inferences (1914)"
    publisher: "Carveth Read, via Lit2Go, University of South Florida"
    url: https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/462/chapter-7/
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "Further Immediate Inferences (Philosophy 103: Introduction to Logic)"
    publisher: Lander University Philosophy Department
    url: https://philosophy.lander.edu/logic/further.html
    type: academic
    accessed: 2026-11-16
  - id: s5
    title: "Lecture 22: Further Categorical Inferences (Introduction to Logical Reasoning)"
    publisher: "David Emmanuel Gray, Carnegie Mellon University in Qatar"
    url: https://www.acsu.buffalo.edu/~degray/CT13/Slides22.pdf
    type: academic
    accessed: 2026-11-16
created: 2026-11-16
---

# Obversion

Obversion is an immediate inference: it draws a conclusion from a single categorical proposition, with no second premise. It takes two steps. First, change the quality of the proposition, from affirmative to negative or from negative to affirmative, while keeping its quantity. Second, replace the predicate term with its complement, the class of everything that is not in the predicate class.[^s2][^s4] The result is called the obverse. Introductory logic texts treat a proposition and its obverse as logically equivalent, so obversion is the one immediate inference that holds for all four standard forms.[^s2][^s4][^s5]

## Origin

The SEP entry on the traditional square of opposition says Aristotle already discussed some instances of the move. Medieval logicians studied it through Aristotle's "infinite" negation, which makes a term from a term ("non-horse") rather than negating a whole sentence.[^s1] The same entry reports that John Buridan in the fourteenth century showed one direction fails when terms may be empty, and that some earlier medieval writers had accepted the faulty version.[^s1] Richard Whately's *Elements of Logic* (1827) included obversion and noted that it was in frequent use. Later English and American textbooks kept it under other names, including permutation and infinitation.[^s1] Carveth Read's *Logic: Deductive and Inductive* (1914) gives a further name, aequipollence, and the vocabulary still used today: the original proposition is the obvertend and the result is the obverse.[^s3]

## How it works

The four obverses are standard:[^s2][^s4][^s5]

- A: "All S are P" becomes "No S are non-P."[^s2][^s4]
- E: "No S are P" becomes "All S are non-P."[^s2][^s4]
- I: "Some S are P" becomes "Some S are not non-P."[^s2][^s4]
- O: "Some S are not P" becomes "Some S are non-P."[^s2][^s4]

The argument map above shows a workplace case. A dispatch supervisor knows every parcel in today's batch has been weighed, so she can say with equal right that none of them is unweighed. In a Venn diagram, both statements shade the same region: the part of the parcel circle that lies outside the weighed circle.[^s5] The two sentences describe one state of affairs from opposite sides of the predicate's boundary.

Read grounds the move in two classical laws. Affirmative obversion rests on the law of contradiction: whatever is P cannot also be non-P. Negative obversion rests on the law of excluded middle: whatever is not P must be non-P.[^s3] Obversion also appears inside other inferences. Read describes the contrapositive as the converse of the obverse, so contraposition is obversion and conversion done in sequence, and it needs no separate justification.[^s3]

## How to apply it

1. Identify the form (A, E, I or O) and keep the quantity ("all", "no", "some") unchanged except as the A/E switch requires.[^s2]
2. Flip the quality: insert or remove the negative.[^s3]
3. Replace the predicate with its exact complement, usually by prefixing "non-". Lander's course notes advise against relying on prefixes such as "in-" or "un-", since "inflammable" does not mean "non-flammable".[^s4]
4. Check that the complement is not merely a contrary. Eldred's textbook stresses that the complement of a class is everything outside it, not its opposite, and Read notes that a contradictory term covers all the contraries.[^s2][^s3] "Not hot" licenses "non-hot", not "cold".
5. Read the result back. "Some S are not non-P" is clumsy but means the same as "Some S are P".[^s2]

The common pitfall is doing only one of the two steps. Changing the quality without complementing the predicate turns "Some invoices were paid late" into "Some invoices were not paid late", which is a different claim. The two particular forms are subcontraries that can both be true, so neither follows from the other.[^s1] Complementing the predicate without changing the quality produces the same kind of error in reverse.

## Limitations

The textbook equivalences assume that complements are well defined and that classes are not empty. The SEP entry reports that the traditional rules hang together only if empty and universal terms are excluded, an assumption most nineteenth-century authors left unstated.[^s1] Buridan's counterexamples show that the negative-to-affirmative direction can fail when a term has no instances.[^s1] Context also matters. Lander's notes point out that finding the true complement of a phrase such as "objects to be admired" can take judgment, not just a prefix.[^s4]

## Connections

- **Part of contraposition.** Read defines the contrapositive as the converse of the obverse, so obversion is one of the two steps that make up contraposition.[^s3]
- **Explained by the law of non-contradiction and the law of excluded middle.** Read derives affirmative obversion from the first and negative obversion from the second.[^s3]
- **Studied in formal logic.** Obversion is a standard operation in introductory categorical logic, alongside conversion and contraposition.[^s2][^s5]
- **Related to unwarranted contrast.** The fallacy moves from "some S are P" to "some S are not P", keeping obversion's change of quality but dropping the complement; the subcontrary relation shows the result does not follow.[^s1][^s2]
- **Related to the square of opposition and existential import.** The SEP traces obversion's history through the same medieval debates about empty terms that shaped the square.[^s1]

## Sources

[^s1]: G. Ciola (earlier versions by T. Parsons), "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy, substantive revision 2025. https://plato.stanford.edu/ENTRIES/square/ (accessed 2026-11-16)
[^s2]: K. Eldred, "3.3 Operations on Categorical Propositions", *An Introduction to Logic*, Pima Community College Open Press, 2024. https://pimaopen.pressbooks.pub/intrologic/?p=833 (accessed 2026-11-16)
[^s3]: C. Read, *Logic: Deductive and Inductive*, Chapter VII "Immediate Inferences", 1914, Lit2Go, University of South Florida. https://etc.usf.edu/lit2go/37/logic-deductive-and-inductive/462/chapter-7/ (accessed 2026-11-16)
[^s4]: "Further Immediate Inferences", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/further.html (accessed 2026-11-16)
[^s5]: D. E. Gray, "Lecture 22: Further Categorical Inferences", Introduction to Logical Reasoning, Carnegie Mellon University in Qatar. https://www.acsu.buffalo.edu/~degray/CT13/Slides22.pdf (accessed 2026-11-16)
