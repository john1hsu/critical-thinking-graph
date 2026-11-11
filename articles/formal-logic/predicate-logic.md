---
id: ct:predicate-logic
type: Field
title: Predicate logic
aliases: [first-order logic, quantificational logic, predicate calculus, first-order predicate calculus, FOL]
domain: formal-logic
summary: >-
  The branch of formal logic that analyses statements into names, predicates
  and relations, and adds the quantifiers "for all" and "there exists", so that
  it can judge the validity of inferences that turn on generality and on
  what is said about particular things.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-logic]
related: [ct:quantifier-shift-fallacy, ct:exists-forall-to-forall-exists-inference, ct:truth-tree, ct:categorical-proposition, ct:syllogism, ct:alfred-tarski, ct:validity, ct:logical-consequence]
requires: [ct:propositional-logic, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:gottlob-frege, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:charles-sanders-peirce, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:propositional-logic, source: s3, confidence: high}
  - {predicate: introducedIn, object: ct:begriffsschrift, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "The Emergence of First-Order Logic"
    publisher: Stanford Encyclopedia of Philosophy (William Ewald, 2018)
    url: https://plato.stanford.edu/ENTRIES/logic-firstorder-emergence/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "Classical Logic"
    publisher: Stanford Encyclopedia of Philosophy (Stewart Shapiro; Spring 2007 archive edition)
    url: https://plato.stanford.edu/archives/spr2007/entries/logic-classical/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s3
    title: "forall x: Calgary. An Introduction to Formal Logic (PDF edition)"
    publisher: "Open Logic Project (Magnus, Button, Loftis, Trueman, Thomas-Bolduc & Zach; CC BY 4.0)"
    url: https://forallx.openlogicproject.org/forallxyyc.pdf
    type: textbook
    accessed: 2026-11-11
  - id: s4
    title: "Turing Machines"
    publisher: Stanford Encyclopedia of Philosophy (Liesbeth De Mol, rev. 2025)
    url: https://plato.stanford.edu/ENTRIES/turing-machine/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s5
    title: "Supplement to Alonzo Church: The Entscheidungsproblem and related results"
    publisher: Stanford Encyclopedia of Philosophy
    url: https://plato.stanford.edu/ENTRIES/church/supplementA.html
    type: scholarly-encyclopedia
    accessed: 2026-11-11
created: 2026-11-11
---

# Predicate logic

Predicate logic, usually called first-order logic, extends propositional logic by looking inside sentences. Propositional logic treats "every invoice over the limit needs two approvals" as one unanalysed letter. First-order logic adds names for individual objects, predicates and relations that say things about them, an identity sign, and the two quantifiers ∀ ("for all") and ∃ ("there exists").[^s3] In the classical version, sentences are interpreted over a non-empty domain of objects. An argument is valid when no interpretation makes every premise true and the conclusion false.[^s2] "First-order" means the quantifiers range over individuals only, not over properties or predicates. Quantifying over properties belongs to second-order logic.[^s1]

## Origin

Gottlob Frege's *Begriffsschrift* (1879) introduced quantifiers and relations together, in a single step. It broke with the subject–predicate analysis that logic had used since Aristotle.[^s1] Working independently, Charles Sanders Peirce and his students developed a quantifier notation in 1883–1885 and coined the word "quantifier". Peirce also separated first-order from second-order quantification. Giuseppe Peano supplied the symbol ∃ in 1889.[^s1] Frege's own system was higher-order. First-order logic was carved out as a separate system only gradually, according to William Ewald's history. Leopold Löwenheim's 1915 theorem on countable models and Thoralf Skolem's refinements in the early 1920s were milestones. So was Hilbert and Ackermann's 1928 textbook, which posed completeness as an open problem. Kurt Gödel solved that problem in his 1929 dissertation.[^s1] By the end of the 1930s classical first-order logic had become the standard logic. Ewald credits its metatheory, its adequacy for formalising set theory, and philosophical doubts about higher-order quantification.[^s1]

## How it works

The forall x textbook motivates the subject with a simple argument: Willard is a logician; all logicians wear funny hats; so Willard wears a funny hat. Rendered as three unrelated sentence letters, the argument comes out invalid in propositional logic. First-order logic "splits the atom" and shows its form.[^s3] A workplace version: "Every invoice over the limit needs two approvals. Invoice 4471 is over the limit. So invoice 4471 needs two approvals." With predicates O(x) for "is over the limit" and T(x) for "needs two approvals", and the name *a* for the invoice, the premises are ∀x(O(x) → T(x)) and O(a). The conclusion is T(a). Instantiating the universal premise for *a* and applying modus ponens derives the conclusion, so the argument is valid.[^s3]

Relations and nested quantifiers are where the extra power, and the extra risk, show up. "Every project has someone who leads it", written ∀x∃y Leads(y, x), is not equivalent to "someone leads every project", written ∃y∀x Leads(y, x). Swapping the quantifiers turns a harmless claim into a much stronger one. The textbook uses this pair to illustrate the quantifier shift fallacy.[^s3] Translating a policy, requirement or contract clause into this notation is a practical way to find out which reading is meant before acting on it.

## Key results

Classical first-order logic has standard proof systems that are sound, so whatever they derive is valid. Gödel showed they are also complete: every valid argument can be derived.[^s2][^s1] It is compact: a set of sentences has a model whenever each finite subset does.[^s2] By the Löwenheim–Skolem theorems, a satisfiable set of sentences in a countable language has a countable model. If a theory has arbitrarily large finite models, it has infinite models of every infinite size. One consequence is that first-order sentences cannot pin down "countably infinite" or "uncountable".[^s2] Per Lindström proved in 1969 that no logic stronger than first-order logic keeps both compactness and the Löwenheim–Skolem property. Ewald reads this as part of the explanation for why first-order logic became the standard.[^s1]

Unlike propositional logic, first-order logic has no general decision procedure. In 1936 Alonzo Church and Alan Turing each showed independently that no effective method can decide, for every formula, whether it is derivable.[^s4][^s5] The theorems can still be listed one by one (they are recursively enumerable), and by completeness every valid argument eventually turns up in that list. What fails is any guarantee of an answer when the argument is invalid.[^s2][^s5]

## Limits

First-order logic is a model of reasoning, not a full transcript of it. Shapiro notes that philosophers disagree about how formal languages relate to everyday reasoning. Some think they reveal its underlying form; others treat them as idealised mathematical models of it.[^s2] The classical system builds in two-valued truth, excluded middle and double-negation elimination, all of which intuitionists reject.[^s2] Translations into the notation also require judgement. The textbook flags ambiguity, definite descriptions and names that refer to nothing as recurring trouble spots.[^s3]

## Connections

- **Broader field.** Predicate logic is the central system of modern formal logic. Its interpretation-based definition of validity generalises the truth-table test.[^s2][^s3]
- **Contrasts with propositional logic.** It keeps the connectives but analyses atomic sentences, which lets it validate arguments that propositional logic must reject.[^s3]
- **Introduced by Frege in the *Begriffsschrift*, with Peirce as a parallel influence.** Ewald credits Frege's 1879 book with the first quantifiers and Peirce's school with the notation and the first-order/second-order distinction.[^s1]
- **Quantifier errors.** The quantifier shift fallacy and its valid converse, the exists-forall to forall-exists inference, can only be stated and checked in its notation.[^s3]
- **Proof methods.** Truth trees extend to first-order logic. Because the logic is undecidable, no tree procedure can be guaranteed to settle every case.[^s4][^s5]

## Sources

[^s1]: Ewald, "The Emergence of First-Order Logic", *Stanford Encyclopedia of Philosophy* (2018). https://plato.stanford.edu/ENTRIES/logic-firstorder-emergence/ (accessed 2026-11-11)
[^s2]: Shapiro, "Classical Logic", *Stanford Encyclopedia of Philosophy* (Spring 2007 edition). https://plato.stanford.edu/archives/spr2007/entries/logic-classical/ (accessed 2026-11-11)
[^s3]: Magnus, Button et al., *forall x: Calgary. An Introduction to Formal Logic*, chs. 13, 23–25. https://forallx.openlogicproject.org/forallxyyc.pdf (accessed 2026-11-11)
[^s4]: De Mol, "Turing Machines", *Stanford Encyclopedia of Philosophy* (rev. 2025). https://plato.stanford.edu/ENTRIES/turing-machine/ (accessed 2026-11-11)
[^s5]: "Supplement to Alonzo Church: The Entscheidungsproblem", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/ENTRIES/church/supplementA.html (accessed 2026-11-11)
