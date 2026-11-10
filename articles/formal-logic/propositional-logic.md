---
id: ct:propositional-logic
type: Field
title: Propositional logic
aliases: [sentential logic, statement logic, propositional calculus, sentential calculus, truth-functional logic]
domain: formal-logic
summary: >-
  The branch of formal logic that treats whole statements as unanalysed units
  and studies how connectives such as "not", "and", "or", "if…then" and "if and
  only if" combine them, and which inferences are valid purely in virtue of
  that connective structure.
level: introductory
evidenceStatus: normative
broader: [ct:formal-logic]
related: [ct:truth-table, ct:truth-tree, ct:modus-ponens, ct:modus-tollens, ct:disjunctive-syllogism, ct:material-conditional, ct:chrysippus, ct:emil-post, ct:validity, ct:soundness, ct:affirming-the-consequent]
requires: [ct:validity, ct:deductive-reasoning]
relations:
  - {predicate: influencedBy, object: ct:stoic-logic, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:george-boole, source: s1, confidence: medium}
  - {predicate: influencedBy, object: ct:gottlob-frege, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:predicate-logic, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:computer-science, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Propositional Logic"
    publisher: Internet Encyclopedia of Philosophy (Kevin C. Klement)
    url: https://iep.utm.edu/propositional-logic-sentential-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "Propositional Logic"
    publisher: Stanford Encyclopedia of Philosophy (Curtis Franks, 2023)
    url: https://plato.stanford.edu/entries/logic-propositional/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s3
    title: "forall x: Calgary. An Introduction to Formal Logic (Fall 2021)"
    publisher: "Open Logic Project (Magnus, Button, Loftis, Trueman, Thomas-Bolduc & Zach; CC BY 4.0)"
    url: https://forallx.openlogicproject.org/forallxyyc.html
    type: textbook
    accessed: 2026-11-10
  - id: s4
    title: "Post, Emil Leon"
    publisher: "Complete Dictionary of Scientific Biography (Hubert C. Kennedy, 2008), via MacTutor, University of St Andrews"
    url: https://mathshistory.st-andrews.ac.uk/DSB/Post.pdf
    type: encyclopedia
    accessed: 2026-11-10
created: 2026-11-10
---

# Propositional logic

Propositional logic, also called sentential or statement logic, studies how complete statements are joined or modified to form compound statements, and what follows logically from those combinations. It treats each simple statement as a single indivisible unit and looks only at the connectives between them.[^s1] The Stanford Encyclopedia of Philosophy describes the subject as the study of how connectives such as "and" and "not" fix the truth or assertability conditions of sentences, examined apart from other logical operators.[^s2] In the classical version the connectives are truth-functional: the truth value of a compound depends only on the truth values of its parts. That makes propositional logic the simplest setting in which validity can be tested mechanically.[^s1][^s3]

## Origin

Aristotle noticed that connectives carry logical weight, but he built his logic around terms rather than whole statements.[^s2] The first sustained logic of statements came from the Stoics in the third century BCE. Diodorus Cronus and Philo argued over when a conditional is true. Chrysippus (c. 280–205 BCE) set out basic inference patterns that correspond to modus ponens and modus tollens.[^s1] Medieval logicians such as Abelard and Ockham refined this work. In the nineteenth century George Boole and Augustus De Morgan developed an algebra of logic that can be read as a propositional calculus.[^s1] Gottlob Frege's *Begriffsschrift* (1879) gave the first modern formal deduction system for it.[^s1][^s2] Whitehead and Russell's *Principia Mathematica* (1910) followed. In 1921 Emil Post's dissertation applied truth tables systematically and proved that the *Principia* propositional calculus is both consistent and complete. Hubert Kennedy's biographical entry counts it among the first decisive results of finitistic metamathematics.[^s4] Gerhard Gentzen's natural deduction systems of the mid-1930s became the template for most textbook proof methods.[^s1]

## How it works

The language has sentence letters (A, B, C…) that stand for simple claims, plus five standard connectives: negation (¬), conjunction (∧), inclusive disjunction (∨), the conditional (→) and the biconditional (↔). Brackets mark the scope of each connective.[^s3] An argument is valid when no assignment of truth values makes every premise true and the conclusion false. Validity therefore depends on form, not on whether the premises are actually true.[^s3] There are two complementary ways to establish it. Semantic methods, such as truth tables, check every assignment. Proof systems, such as natural deduction, derive the conclusion step by step using rules like modus ponens and disjunctive syllogism.[^s1][^s3]

A workplace example shows the payoff. A release manager reasons: "If the tests pass and the security review is signed off, we ship Friday. We are not shipping Friday. So the tests did not pass." Symbolize the claims as (T ∧ R) → F, ¬F, therefore ¬T. Modus tollens validly yields only ¬(T ∧ R), meaning *not both* conditions held. By De Morgan's law that is ¬T ∨ ¬R. The row where T is true and R is false makes both premises true and the conclusion false, so the argument is invalid. The tests may have passed while the security sign-off was missing.[^s1][^s3] Putting the reasoning into symbols exposes the gap that the everyday wording concealed.

## Key results

Classical propositional logic has unusually clean metatheory. Its standard proof systems are sound and complete: exactly the truth-functionally valid formulas can be derived.[^s1][^s2] It is decidable, because a truth table always settles validity in a finite number of steps.[^s1] It is also functionally complete with small sets of connectives. {¬, ∧} and {¬, ∨} can express every truth function, and Sheffer and Peirce showed that a single connective ("not both") is enough.[^s2] Decidable does not mean cheap, though. The table doubles in size with every new letter.[^s1] Stephen Cook proved in 1971 that the satisfiability problem (SAT) is NP-complete. Whether SAT can be solved in polynomial time is the open P versus NP question.[^s2]

## Limits

Propositional logic cannot see inside a sentence. Inferences that depend on subjects, predicates or quantifiers such as "all" and "some" (for example "every auditor is certified; Lee is an auditor; so Lee is certified") come out invalid when each clause becomes an unrelated letter. Predicate logic was developed to handle such cases.[^s1][^s3] Non-truth-functional words such as "because" and "necessarily" also fall outside it.[^s3] The material conditional counts every conditional with a false antecedent as true, which fits ordinary "if" sentences poorly. That mismatch has motivated relevance logics and probabilistic accounts of conditionals.[^s1][^s2] Intuitionistic and many-valued logics reject classical principles such as excluded middle or two-valued truth. Post's 1921 paper itself introduced many-valued truth tables.[^s2][^s4]

## Connections

- **Broader field.** Propositional logic is the simplest branch of formal logic. Its validity tests serve as the template for richer systems.[^s2][^s3]
- **Influenced by Stoic logic, Boole and Frege.** Klement traces the field from Chrysippus's inference patterns through Boole's algebra to Frege's 1879 calculus, and Franks dates the modern formal system to Frege.[^s1][^s2]
- **Contrasts with predicate logic.** The forall x textbook motivates first-order logic directly from the arguments that truth-functional logic cannot capture.[^s3]
- **Applied in computer science.** Franks notes Claude Shannon's 1940 use of propositional logic to describe switching circuits, and SAT's central place in complexity theory.[^s2]
- **Methods and forms.** Truth tables and truth trees are its decision procedures. Modus ponens, modus tollens and disjunctive syllogism are its valid forms, and affirming the consequent is the classic invalid look-alike.[^s1][^s3]

## Sources

[^s1]: Klement, "Propositional Logic", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/propositional-logic-sentential-logic/ (accessed 2026-11-10)
[^s2]: Franks, "Propositional Logic", *Stanford Encyclopedia of Philosophy* (2023). https://plato.stanford.edu/entries/logic-propositional/ (accessed 2026-11-10)
[^s3]: Magnus, Button et al., *forall x: Calgary. An Introduction to Formal Logic* (Fall 2021). https://forallx.openlogicproject.org/forallxyyc.html (accessed 2026-11-10)
[^s4]: Kennedy, "Post, Emil Leon", *Complete Dictionary of Scientific Biography* (2008), via MacTutor. https://mathshistory.st-andrews.ac.uk/DSB/Post.pdf (accessed 2026-11-10)
