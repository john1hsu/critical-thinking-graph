---
id: ct:de-morgans-laws
type: Principle
title: De Morgan's laws
aliases: [De Morgan's rules, De Morgan rules, De Morgan equivalences, De Morgan duality]
domain: formal-logic
summary: >-
  The pair of logical equivalences stating that denying a conjunction is the
  same as asserting that at least one conjunct is false, and denying a
  disjunction is the same as asserting that every disjunct is false:
  not-(P and Q) equals not-P or not-Q, and not-(P or Q) equals not-P and not-Q.
level: introductory
evidenceStatus: normative
broader: [ct:propositional-logic]
related: [ct:truth-table, ct:disjunctive-syllogism, ct:affirming-a-disjunct, ct:conjunctive-syllogism, ct:george-boole, ct:formal-logic]
requires: [ct:truth-table]
relations:
  - {predicate: detects, object: ct:denying-a-conjunct, source: s5, confidence: medium}
  - {predicate: studiedIn, object: ct:propositional-logic, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:augustus-de-morgan, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:william-of-ockham, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Propositional Logic"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/prop-log?no_redirect=true
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "forall x: Calgary. An Introduction to Formal Logic (Fall 2025 edition), ch. 19.5 and 21.6"
    publisher: "P. D. Magnus, Tim Button, Robert Trueman and Richard Zach, Open Logic Project"
    url: https://forallx.openlogicproject.org/forallxyyc.pdf
    type: textbook
    accessed: 2026-11-13
  - id: s3
    title: "Augustus De Morgan"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/biography/Augustus-De-Morgan
    type: encyclopedia
    accessed: 2026-11-13
  - id: s4
    title: "The negations of conjunctions, conditionals, and disjunctions"
    publisher: "Acta Psychologica 151, 1-7 (Khemlani, Orenes & Johnson-Laird, 2014), authors' copy"
    url: https://modeltheory.org/papers/2014sentential-negation.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Denying a Conjunct"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/denyconj.html
    type: community
    accessed: 2026-11-13
created: 2026-11-13
---

# De Morgan's laws

De Morgan's laws are two equivalences of propositional logic that say how negation interacts with "and" and "or". The first says that "not (P and Q)" is equivalent to "not P, or not Q": to deny that two things are both true is to say that at least one of them is false. The second says that "not (P or Q)" is equivalent to "not P, and not Q": to deny that either is true is to say that both are false. In symbols, ¬(P ∧ Q) ↔ (¬P ∨ ¬Q) and ¬(P ∨ Q) ↔ (¬P ∧ ¬Q).[^s1][^s2] Because each side can be swapped for the other without changing truth value, the laws let a reasoner push a negation inside a compound sentence or pull it out again, turning a vague "it's not the case that…" into a precise list of what is actually being ruled out.[^s1]

## Origin

The equivalences are much older than their name. Britannica notes that William of Ockham stated them in words in the fourteenth century; the nineteenth-century London mathematician Augustus De Morgan (1806–1871) studied them systematically and gave them mathematical expression, which is why they carry his name.[^s3] De Morgan, professor of mathematics at University College London and first president of the London Mathematical Society, was one of the two writers, with George Boole, whose work drove the mid-nineteenth-century revival of logic beyond Aristotle's syllogistic.[^s3][^s1] In modern textbooks the laws appear as rules of replacement, or as derived rules of natural deduction that can be proved from the basic introduction and elimination rules for the connectives.[^s1][^s2]

## How it works

The laws can be checked with a four-row truth table. "Not (P and Q)" is false only in the row where P and Q are both true, and "not P or not Q" is false in exactly that row too; on the other three rows both are true. The same check confirms the disjunction law.[^s2] Since the two sides agree on every row, logicians call them equivalent, and a replacement rule may apply them to part of a longer formula, in either direction, which ordinary one-way inference rules cannot do.[^s1] The *forall x* textbook lists four De Morgan rules (from each side to the other, for conjunction and for disjunction) and shows that they add no new power: anything proved with them can be proved without them, only more slowly.[^s2]

A workplace example shows why this matters. A project lead says: "The delay wasn't caused by both the vendor and our own testing." Read through De Morgan's first law, that means only "either the vendor did not cause it, or our testing did not cause it, or neither did". It does not say that one of them *did* cause it. So when a colleague later shows that the vendor was not at fault and someone concludes "then it must have been our testing", the inference fails: the "not both" premise is satisfied when neither party is responsible. This is the fallacy of denying a conjunct, and the Fallacy Files spells out the same point, that a denied conjunction stays true when one conjunct is false, the other is false, or both are.[^s5]

## How to apply it

- **Rewrite every "not both" before you reason from it.** Translate "not (A and B)" into "not A or not B" and ask what that disjunction does and does not exclude. A conclusion that one of the two must hold needs an extra premise ("at least one of A or B").[^s5][^s2]
- **Rewrite every "neither… nor".** "Not (A or B)" is the strong claim "not A and not B"; it licenses dropping both options, not just one.[^s1]
- **Use the laws to simplify policies and conditions.** A rule such as "access is denied unless the user is staff or a contractor" negates a disjunction; restating it as "denied if not staff and not a contractor" makes the test explicit and easier to audit.[^s1][^s2]
- **Check with a truth table when unsure.** If a rewritten sentence and the original disagree on any row, the rewrite is wrong.[^s2]

## Evidence

Although the laws themselves are normative, research on how people actually understand denials shows why they are worth teaching. In a 2014 *Acta Psychologica* paper, Khemlani, Orenes and Johnson-Laird asked small online samples (22 and 21 adults) to judge or write denials of conjunctions, disjunctions and conditionals.[^s4] When choosing which cases were compatible with a denied conjunction, only 18% of responses were correct, and most participants picked the single case where both clauses were false. When asked to write a denial of "A and B" in their own words, none produced the De Morgan form "not A or not B"; about two-thirds wrote "not A and not B". Denials of disjunctions, by contrast, were mostly correct.[^s4] The authors read this as support for their mental-model theory, in which denying a conjunction is hard because it requires listing three possibilities, and as evidence against a rival theory that assumes people reason with De Morgan's laws directly.[^s4] The samples were small and recruited online, so the exact percentages should be treated as indicative, but the direction of the finding fits the common everyday slide from "not both" to "neither" or to "exactly one".

## Connections

- **Detects** denying a conjunct: rewriting "not both P and Q" as "not P or not Q" makes it plain that learning "not P" leaves Q undecided, which is the gap the fallacy ignores.[^s5][^s2]
- **Studied in** propositional logic, where the laws are standard equivalences and derived rules of natural deduction.[^s2][^s1]
- **Introduced by** Augustus De Morgan, who gave the laws their mathematical form, and, in verbal form, William of Ockham in the fourteenth century.[^s3]
- **Related** to the truth table, which verifies the laws; to disjunctive syllogism and affirming a disjunct, whose validity and invalidity turn on what "or" excludes; to the conjunctive syllogism, the valid "not both; P; so not Q" form; and to George Boole, De Morgan's contemporary in the algebra of logic.[^s1][^s2][^s5]

## Sources

[^s1]: "Propositional Logic", Internet Encyclopedia of Philosophy. https://iep.utm.edu/prop-log?no_redirect=true (accessed 2026-11-13)
[^s2]: Magnus, Button, Trueman and Zach, *forall x: Calgary. An Introduction to Formal Logic*, Fall 2025 edition, sections 19.5 and 21.6. Open Logic Project. https://forallx.openlogicproject.org/forallxyyc.pdf (accessed 2026-11-13)
[^s3]: "Augustus De Morgan", Encyclopaedia Britannica. https://britannica.com/biography/Augustus-De-Morgan (accessed 2026-11-13)
[^s4]: Khemlani, S., Orenes, I. and Johnson-Laird, P. N. (2014). "The negations of conjunctions, conditionals, and disjunctions." *Acta Psychologica* 151, 1–7. Authors' copy. https://modeltheory.org/papers/2014sentential-negation.pdf (accessed 2026-11-13)
[^s5]: Curtis, G. N., "Denying a Conjunct", The Fallacy Files. https://fallacyfiles.org/denyconj.html (accessed 2026-11-13)
