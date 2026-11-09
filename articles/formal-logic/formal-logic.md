---
id: ct:formal-logic
type: Field
title: Formal logic
aliases: [symbolic logic]
domain: formal-logic
summary: >-
  The branch of logic that studies deductive inference by abstracting from what
  statements are about to the structures (logical forms) they share, and that
  states those forms in precisely defined artificial languages so that validity
  can be tested by form alone.
level: introductory
evidenceStatus: normative
broader: [ct:logic]
related: [ct:propositional-logic, ct:predicate-logic, ct:syllogism, ct:truth-table, ct:formal-fallacy, ct:informal-logic, ct:soundness, ct:method-of-counterexample, ct:alfred-tarski]
requires: [ct:validity, ct:deductive-reasoning]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: influencedBy, object: ct:stoic-logic, source: s1, confidence: medium}
  - {predicate: influencedBy, object: ct:george-boole, source: s4, confidence: high}
  - {predicate: influencedBy, object: ct:gottlob-frege, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:computer-science, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Logical Form"
    publisher: Stanford Encyclopedia of Philosophy (Pietroski, Spring 2024 edition)
    url: https://plato.stanford.edu/archives/spr2024/entries/logical-form/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s2
    title: "Classical Logic"
    publisher: Stanford Encyclopedia of Philosophy (Kouri Kissel, rev. 2026)
    url: https://plato.stanford.edu/entries/logic-classical/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s3
    title: "forall x: Calgary. An Introduction to Formal Logic"
    publisher: "Magnus, Button, Loftis, Trueman, Thomas-Bolduc & Zach, University of Calgary / Open Logic Project (Fall 2021, CC BY 4.0)"
    url: https://forallx.openlogicproject.org/forallxyyc.html
    type: textbook
    accessed: 2026-11-09
  - id: s4
    title: "George Boole"
    publisher: Stanford Encyclopedia of Philosophy (Jackson, rev. 2026)
    url: https://plato.stanford.edu/entries/boole/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s5
    title: "Formal logic"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/formal-logic
    type: encyclopedia
    accessed: 2026-11-09
created: 2026-11-09
---

# Formal logic

Formal logic is the part of logic that studies deductive arguments by setting aside what they are about and examining the structure they share. Britannica describes it as the abstract, a priori study of propositions and deductive arguments, closer to pure mathematics than to any empirical science, which extracts the logical forms that particular statements embody.[^s5] Its central idea is that some inferences are secure because of their form: any argument fitting the pattern "if A then B; A; so B" is valid whatever A and B say, while "B if A; B; so A" is risky whatever they say.[^s1] The field is "formal" in a second sense too: it states those patterns in artificial languages defined by explicit rules, so that its expressions cannot be ambiguous.[^s3]

## Origin

Pietroski traces the idea of logical form back to antiquity. Aristotle's syllogistic treated the step from premises like "every S is P" to a conclusion as a matter of structure, and the Stoics stated propositional patterns using placeholders such as "the first" and "the second".[^s1] Medieval logicians analysed sentences as subject-predicate structures built from terms and logical words.[^s1] In the nineteenth century George Boole's *Mathematical Analysis of Logic* (1847) and *Laws of Thought* (1854) recast logic as an algebra of classes, replacing the catalogue of valid syllogisms with general procedures that could handle arguments of any complexity; Jackson calls him a founder of the algebraic tradition in logic.[^s4] The decisive break came with Gottlob Frege's *Begriffsschrift* (1879), which analysed sentences into function and argument with quantifiers binding variables, letting logic represent relations and multiple quantifiers that the subject-predicate model could not.[^s1] In the twentieth century Whitehead and Russell's *Principia Mathematica* (1910-13) supplied an axiomatic system for the propositional calculus that textbooks still present.[^s5]

## How it works

A formal system has three parts: an artificial language, a deductive system of rules for deriving sentences, and a model-theoretic semantics that says when sentences are true; logicians then study these as mathematical objects, proving properties such as soundness and completeness.[^s2] Using it on a real argument takes two steps. First, symbolise: assign sentence letters (and, in first-order logic, names, predicates and quantifiers) to the parts of the English argument through a symbolisation key.[^s3] Second, test the resulting form, for example with a truth table or a natural-deduction proof; an argument is valid when no case makes all the premises true and the conclusion false, and such a case is a counterexample.[^s3]

Consider a team lead reasoning: "If the build passes and the reviewer approves, we ship today. The build passed. The reviewer approved. So we ship today." Writing P for "the build passes", R for "the reviewer approves" and S for "we ship today" gives (P and R) → S, P, R, therefore S. A truth table shows no row where all premises are true and S false, so the inference is valid by form; whether the team actually ships still depends on whether the conditional premise is true.[^s3] Formal logic certifies the step, not the premises, which is why validity and soundness are separate verdicts.[^s5]

## How to apply it

Formalise when an argument is long, nested or contested, because ordinary wording often hides structure: Pietroski notes that surface grammar can mislead and that sentences like "someone likes everyone" carry quantifier-scope distinctions that only a formal representation makes explicit.[^s1] Choose the weakest system that captures what matters: propositional logic when only "and", "or", "not" and "if" are doing the work, predicate logic when the argument turns on "all", "some" or relations.[^s3] Keep the symbolisation key consistent within one argument, and when English is ambiguous, symbolise each reading separately and test each.[^s3] If a form fails, construct the counterexample row and translate it back into plain language; that is usually the most persuasive way to show someone why an argument does not follow.[^s3]

## Evidence and limitations

As a set of standards, formal logic is normative rather than empirical, but its reach is limited. Symbolisation drops nuance and tone, cannot capture non-truth-functional words such as "because", and must pick one reading of an ambiguous sentence.[^s3] Some arguments are valid for reasons of meaning rather than form ("it is green all over, so it is not red all over"), and good inductive arguments are not deductively valid at all, so formal tools set them aside.[^s3] How formal languages relate to natural language is itself disputed: they have been treated as displaying hidden logical form, as replacements for or regimentations of ordinary language, or as idealised mathematical models of it.[^s2] Quine argued that regimentation is normative and holistic, so there may be no single fact about which form a speaker's sentence has.[^s1]

## Connections

- **Broader: logic; requires validity and deductive reasoning.** Formal logic is the branch of logic that tests deductive validity by form, so both notions are prerequisites.[^s3]
- **Introduced by Aristotle, influenced by Stoic logic.** Aristotle's syllogistic treated inference as structural, and the Stoics stated propositional patterns with placeholders.[^s1]
- **Influenced by George Boole.** Boole's algebra of logic began the mathematical treatment of logical form.[^s4]
- **Influenced by Gottlob Frege.** Frege's quantifier-variable analysis in the *Begriffsschrift* underlies modern predicate logic.[^s1]
- **Applied in computer science.** Kouri Kissel notes that logic is central to computer science as well as to mathematics and philosophy.[^s2]
- **Related.** Propositional (truth-functional) and first-order predicate logic are its core textbook systems, and truth tables and counterexamples are its basic tests of validity.[^s3] The syllogism is its oldest system, and formal fallacies are the invalid patterns that only look like valid forms.[^s1] Informal logic is the natural-language counterpart that addresses the limits described above.

## Sources

[^s1]: Pietroski, "Logical Form", Stanford Encyclopedia of Philosophy (Spring 2024 edition). https://plato.stanford.edu/archives/spr2024/entries/logical-form/ (accessed 2026-11-09)
[^s2]: Kouri Kissel, "Classical Logic", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/logic-classical/ (accessed 2026-11-09)
[^s3]: Magnus et al., *forall x: Calgary. An Introduction to Formal Logic*, University of Calgary / Open Logic Project. https://forallx.openlogicproject.org/forallxyyc.html (accessed 2026-11-09)
[^s4]: Jackson, "George Boole", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/boole/ (accessed 2026-11-09)
[^s5]: "Formal logic", Encyclopaedia Britannica. https://www.britannica.com/topic/formal-logic (accessed 2026-11-09)
