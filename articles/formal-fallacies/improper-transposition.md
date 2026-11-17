---
id: ct:improper-transposition
type: FormalFallacy
title: Improper transposition
aliases: [negating antecedent and consequent, fallacy of negating antecedent and consequent, inferring the inverse of a conditional]
domain: formal-fallacies
summary: >-
  The formal fallacy of inferring "if not p, then not q" from "if p, then q":
  both parts of a conditional are negated but left in place, producing its
  inverse. Valid transposition (contraposition) also swaps the parts; the
  inverse is not equivalent to the original, so the premise can be true while
  the conclusion is false.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:denying-the-antecedent, ct:commutation-of-conditionals, ct:illicit-contraposition, ct:conditional-perfection, ct:necessary-and-sufficient-conditions, ct:material-conditional, ct:method-of-counterexample, ct:truth-table]
requires: [ct:propositional-logic, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:contraposition, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:denying-the-antecedent, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:commutation-of-conditionals, source: s1, confidence: medium}
  - {predicate: confusedWith, object: ct:biconditional, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:conditional-perfection, source: s5, confidence: medium}
criticalQuestions:
  - Does the conclusion keep the premise's if-clause and then-clause in the same order but put "not" in front of both?
  - Is there some other route, besides p, by which q could come about, so that "if not p, then not q" fails?
  - Did the speaker mean "only if" or "if and only if"? If so, has that stronger claim been stated and supported on its own?
  - Would the valid contrapositive, "if not q, then not p", give the arguer what they actually need?
argumentMap:
  premises:
    - "If an expense claim is over 500 dollars, it needs a director's sign-off."
  conclusion: "If an expense claim is not over 500 dollars, it does not need a director's sign-off."
  verdict: invalid
  scheme: ct:contraposition
  objections:
    - "The policy may also require a director's sign-off for any foreign travel claim, whatever its amount."
    - "The rule names one condition that triggers sign-off; it does not say that it is the only one."
sameAs: []
sources:
  - id: s1
    title: "Fallacies (Encyclopedia of Philosophy, 1967)"
    publisher: "J. L. Mackie, The Encyclopedia of Philosophy (Macmillan), via Encyclopedia.com"
    url: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/fallacies
    type: scholarly-encyclopedia
    accessed: 2026-11-17
  - id: s2
    title: "Improper Transposition"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/imptrans.html
    type: community
    accessed: 2026-11-17
  - id: s3
    title: "2.5 Equivalent Statements"
    publisher: "Contemporary Mathematics, OpenStax (Rice University)"
    url: https://openstax.org/books/contemporary-mathematics/pages/2-5-equivalent-statements
    type: textbook
    accessed: 2026-11-17
  - id: s4
    title: "2.2: Logically Equivalent Statements"
    publisher: "Ted Sundstrom, Mathematical Reasoning: Writing and Proof (Grand Valley State University), Mathematics LibreTexts"
    url: https://math.libretexts.org/Bookshelves/Mathematical_Logic_and_Proof/Book%3A_Mathematical_Reasoning_-_Writing_and_Proof_(Sundstrom)/2%3A_Logical_Reasoning/2.2%3A_Logically_Equivalent_Statements
    type: textbook
    accessed: 2026-11-17
  - id: s5
    title: "Semantics Processing of Conditional Connectives: German wenn 'if' Versus nur wenn 'only if'"
    publisher: "Journal of Psycholinguistic Research 50(6), 1337-1368 (Liu & Barthel, 2021), PubMed Central"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8660741
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Improper transposition

Improper transposition is the invalid immediate inference "If p, then q; therefore, if not p, then not q." The arguer negates both parts of a conditional but leaves them where they were, so the conclusion is the conditional's *inverse*.[^s2] Its mirror image, "If not p, then not q; therefore, if p, then q", is the same mistake run backwards.[^s2] A conditional and its inverse are not logically equivalent: in a truth table they disagree whenever exactly one of p and q is true.[^s3] Because the gap lies in the form and not in the subject matter, the error is a formal fallacy.[^s1] Curtis's stock counterexample makes the point vividly: guillotining the king would kill him, but sparing the guillotine does not make him immortal.[^s2]

## Origin

The fallacy has no single discoverer; it belongs to the family of errors catalogued for hypothetical (conditional) reasoning. In his 1967 article on fallacies for Macmillan's *Encyclopedia of Philosophy*, J. L. Mackie listed it as "negating antecedent and consequent". He grouped it with asserting the consequent, denying the antecedent and converting a conditional, as formal fallacies that mimic or distort a valid form.[^s1] The valid form it mimics is transposition, "if p then q, therefore if not q then not p".[^s1] Curtis's *Fallacy Files* uses the name "improper transposition" and keeps Mackie's label as an alias.[^s2]

## How it works

Transposition, also called contraposition, does two things at once: it swaps the antecedent and consequent and negates both. The result, the contrapositive, is equivalent to the original conditional.[^s2][^s4] Improper transposition performs only the negation, without the swap.[^s2] Textbook treatments show what goes wrong. Of the three standard variations of a conditional, only the contrapositive is equivalent to it. The inverse is equivalent to the converse instead, so inferring the inverse commits to the same reversed claim as converting the conditional.[^s3] Sundstrom's truth-table method gives a quick check: a conditional is false only when its antecedent is true and its consequent false, and its variations can be compared row by row.[^s4]

In the argument map above, a finance policy says claims over 500 dollars need a director's sign-off. An employee concludes that smaller claims never do. Yet the same policy could require sign-off for foreign travel at any amount, so the premise is true and the conclusion false. The rule states a sufficient condition for sign-off, not a necessary one.[^s2][^s3] The conclusion the rule does license is the contrapositive: a claim that needed no sign-off was not over 500 dollars.[^s4]

## How to spot it

Look for a conclusion that is itself a conditional and repeats the premise's two clauses in the same order, each with a "not" attached.[^s2] It differs from denying the antecedent, which adds a separate premise that p is false and draws the categorical conclusion that q is false. Improper transposition draws the general negated rule.[^s2] Curtis observes that the fallacy is most persuasive when the premise's converse happens to be true as well, since the inverse then really does hold.[^s2] It also often hides in replies that rebut the wrong conditional. Someone told that a qualification is necessary answers that it is not sufficient, quietly turning "if not p, then not q" into "if p, then q".[^s2]

## How to counter it

Name a case where p is false and q is still true. One such case refutes the inference.[^s2] Then ask whether the speaker meant a two-way claim. Mackie notes that these conditional fallacies become valid if the premise is read as a biconditional, so the real question is whether "if and only if" was stated and supported.[^s1] If only the one-way rule is supported, offer the contrapositive, which follows validly.[^s4]

## Evidence

Psycholinguistic research suggests why the inverse feels natural. Geis and Zwicky's 1971 idea of conditional perfection holds that listeners often enrich "if p, then q" into "if not p, then not q".[^s5] In a 2021 study of German speakers, Liu and Barthel found that after a negated antecedent about 85 percent of sentence completions for a plain "if" conditional were negative. They concluded that for plain "if" the negated reading is a pragmatic inference, not part of the word's meaning.[^s5] That makes the error understandable in conversation, but it remains invalid as a matter of logical form.[^s1][^s5]

## Connections

- **Invalid form of contraposition.** It negates both parts without the swap that makes transposition valid.[^s1][^s2]
- **Contrasts with denying the antecedent.** Both negate the antecedent; denying the antecedent concludes "not q" from an extra premise, improper transposition concludes a negated conditional.[^s2]
- **Contrasts with commutation of conditionals.** The inverse is equivalent to the converse, so both fallacies make the same reversed claim by different routes.[^s1][^s3]
- **Confused with the biconditional.** Read as "if and only if", the premise would license the inverse.[^s1]
- **Explained by conditional perfection.** Listeners' tendency to strengthen "if" invites the negated reading.[^s5]

## Sources

[^s1]: Mackie, "Fallacies", *The Encyclopedia of Philosophy* (Macmillan, 1967), via Encyclopedia.com. https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/fallacies (accessed 2026-11-17)
[^s2]: Curtis, "Improper Transposition", The Fallacy Files. https://fallacyfiles.org/imptrans.html (accessed 2026-11-17)
[^s3]: "2.5 Equivalent Statements", *Contemporary Mathematics*, OpenStax. https://openstax.org/books/contemporary-mathematics/pages/2-5-equivalent-statements (accessed 2026-11-17)
[^s4]: Sundstrom, "Logically Equivalent Statements", *Mathematical Reasoning: Writing and Proof*, Grand Valley State University. https://math.libretexts.org/Bookshelves/Mathematical_Logic_and_Proof/Book%3A_Mathematical_Reasoning_-_Writing_and_Proof_(Sundstrom)/2%3A_Logical_Reasoning/2.2%3A_Logically_Equivalent_Statements (accessed 2026-11-17)
[^s5]: Liu & Barthel, "Semantics Processing of Conditional Connectives: German *wenn* 'if' Versus *nur wenn* 'only if'", *Journal of Psycholinguistic Research* 50(6), 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8660741 (accessed 2026-11-17)
