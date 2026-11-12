---
id: ct:logical-consequence
type: Concept
title: Logical consequence
aliases: [entailment, semantic consequence, logical entailment, follows-from relation]
domain: foundations
summary: >-
  The relation that holds between a set of premises and a conclusion when, by
  logic alone, the premises cannot all be true while the conclusion is false;
  it is the relation that a valid argument's premises bear to its conclusion.
level: intermediate
evidenceStatus: normative
broader: [ct:logic]
related: [ct:validity, ct:soundness, ct:soundness-theorem, ct:method-of-counterexample, ct:propositional-logic, ct:predicate-logic, ct:prior-analytics, ct:aristotle, ct:reasoning]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:alfred-tarski, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:material-conditional, source: s4, confidence: high}
  - {predicate: formalizedBy, object: ct:natural-deduction, source: s2, confidence: medium}
  - {predicate: formalizedBy, object: ct:truth-table, source: s4, confidence: high}
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:formal-logic, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:the-concept-of-logical-consequence, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Logical Consequence"
    publisher: Internet Encyclopedia of Philosophy (Matthew McKeon)
    url: https://iep.utm.edu/logcon/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "Logical Consequence (Spring 2006 edition)"
    publisher: Stanford Encyclopedia of Philosophy (JC Beall & Greg Restall)
    url: https://plato.stanford.edu/archives/spr2006/entries/logical-consequence/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s3
    title: "Logical Consequence: A Defense of Tarski"
    publisher: Journal of Philosophical Logic 25, 617-677 (Greg Ray, 1996)
    url: https://dx.doi.org/10.1007/BF00265256
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "forall x: Calgary, Chapter 12: Semantic concepts"
    publisher: Open Logic Project (Magnus, Button, Trueman & Zach)
    url: https://forallx.openlogicproject.org/html/Ch12.html
    type: textbook
    accessed: 2026-11-12
created: 2026-11-12
---

# Logical consequence

A sentence is a logical consequence of a set of sentences when logic alone rules out the set being true while the sentence is false.[^s1] Logicians often call it the central concept of their discipline, because it is what an argument claims when it says its conclusion "follows" from its premises.[^s1] Where validity is a property of a single argument, logical consequence is the underlying relation between premises and conclusion; an argument is valid exactly when its conclusion stands in this relation to its premises.[^s2] Logicians write it with a double turnstile, so that "A, B ⊨ C" says that C follows from A and B.[^s4]

## Origin

Aristotle's *Prior Analytics* already describes a syllogism as discourse in which, once certain things are laid down, something further follows of necessity from them, needing no extra term.[^s1] The modern framing comes from Alfred Tarski's 1936 paper "On the Concept of Logical Consequence," which picked out three marks of the ordinary notion: the relation is modal (it holds necessarily, not just as things happen to be), formal (it depends only on the logical form of the sentences), and a priori (it can be known without sensory evidence).[^s1] Tarski defined consequence as the absence of a counterexample: no model makes the premises true and the conclusion false.[^s2] That model-theoretic definition became the textbook standard.

## How it works

There are two precise ways to cash out "follows from." On the **model-theoretic** account, X follows from a set K when every model of K is also a model of X, written K ⊨ X.[^s1] On the **proof-theoretic** (deductive) account, X follows from K when X can be derived from K in a correct deductive system using primitive inference rules, written K ⊢ X; in natural deduction those rules are often thought to fix what the connectives mean.[^s1][^s2] A soundness proof shows that whatever is derivable is a semantic consequence, and a completeness proof shows the converse; for the standard logics both hold, so the two accounts pick out the same arguments, though philosophers disagree about which is more fundamental.[^s1][^s2]

For sentential logic the test is mechanical. A set of sentences entails a conclusion when no row of the truth table (no valuation) makes every premise true and the conclusion false; for example, "if not L then J or L" together with "not L" entails J, since the only row making both premises true also makes J true.[^s4] A logical truth is the limiting case: a sentence that follows from the empty set of premises.[^s2]

Consider a finance team's approval rule: "Every invoice over the threshold needs two sign-offs. This invoice has one sign-off. So this invoice is not over the threshold." The conclusion is a logical consequence of the premises, because no situation makes both premises true and the conclusion false. Whether the reviewer may relax depends on a separate question, whether the system really enforces the rule, which concerns the truth of the premises rather than the consequence relation.[^s1][^s2]

## Why it matters for critical thinking

- **"Follows from" is not "if-then."** The turnstile is a claim made about sentences in the metalanguage, whereas the conditional arrow is a connective inside the object language that builds a longer sentence. Because everyday "implies" blurs the two, careful textbooks avoid the word.[^s4]
- **Necessity, not likelihood.** Deductive consequence requires that true premises guarantee the conclusion; inductive support only makes it probable.[^s2]
- **Form, not subject matter.** Because consequence is formal, a counterexample with the same form but different content refutes a claimed entailment.[^s1][^s2]

## Debates and limits

Not everyone accepts that Tarski's definition captures the ordinary concept. John Etchemendy argued in *The Concept of Logical Consequence* that the account cannot capture the necessity built into the everyday notion, that it diverges from the model-theoretic account and rests on an unsustainable line between logical and non-logical terms.[^s1][^s3] Greg Ray's 1996 reply examined four of these charges and argued each was mistaken, holding that Tarski's account and the model-theoretic one come to the same thing.[^s3] Other open questions include which expressions count as logical constants (Tarski later proposed invariance under permutations of objects), whether consequence can have several conclusions as in Gentzen's systems, and whether more than one consequence relation is correct, the view called logical pluralism.[^s2]

## Connections

- **Introduced by Alfred Tarski.** His 1936 paper supplied the modal, formal and a priori marks and the model-based definition.[^s1]
- **Confused with the material conditional.** Entailment is a relation between sentences; the conditional is a connective within one.[^s4]
- **Formalized by truth tables and natural deduction.** Truth tables test sentential entailment, and proof systems give the deductive characterization.[^s2][^s4]
- **Contrasts with inductive reasoning.** Deductive consequence demands necessity; inductive support does not.[^s2]
- **Studied in formal logic.** Its precise definitions, and the soundness and completeness results linking them, belong to formal logic.[^s1]
- **Challenged by Etchemendy's critique.** *The Concept of Logical Consequence* disputes the adequacy of the Tarskian definition; Ray's reply defends it.[^s3]

## Sources

[^s1]: McKeon, "Logical Consequence", Internet Encyclopedia of Philosophy. https://iep.utm.edu/logcon/ (accessed 2026-11-12)
[^s2]: Beall & Restall, "Logical Consequence", Stanford Encyclopedia of Philosophy, Spring 2006 edition. https://plato.stanford.edu/archives/spr2006/entries/logical-consequence/ (accessed 2026-11-12)
[^s3]: Ray, "Logical Consequence: A Defense of Tarski", *Journal of Philosophical Logic* 25, 1996. https://dx.doi.org/10.1007/BF00265256 (accessed 2026-11-12)
[^s4]: Magnus, Button, Trueman & Zach, *forall x: Calgary*, Chapter 12, "Semantic concepts", Open Logic Project. https://forallx.openlogicproject.org/html/Ch12.html (accessed 2026-11-12)
