---
id: ct:categorical-proposition
type: Concept
title: Categorical proposition
aliases: [categorical statement, categorical sentence, A E I O propositions, standard-form categorical proposition]
domain: formal-logic
summary: >-
  A statement that relates two classes by saying that all, none or some of the
  members of a subject class are or are not included in a predicate class; its
  four standard forms, A, E, I and O, are the building blocks of syllogistic
  logic.
level: introductory
evidenceStatus: normative
broader: [ct:proposition]
related: [ct:square-of-opposition, ct:distribution-of-terms, ct:categorical-syllogism, ct:existential-import, ct:existential-fallacy, ct:venn-diagram-test, ct:syllogism]
requires: []
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:formal-logic, source: s4, confidence: high}
  - {predicate: formalizedBy, object: ct:george-boole, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Aristotle: Logic"
    publisher: Internet Encyclopedia of Philosophy (Louis F. Groarke, St. Francis Xavier University)
    url: https://iep.utm.edu/aristotle-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "History of logic: Aristotle"
    publisher: Encyclopaedia Britannica
    url: https://www.Britannica.Com/topic/history-of-logic/Aristotle
    type: encyclopedia
    accessed: 2026-11-10
  - id: s3
    title: "Standard Form Categorical Propositions: Quantity, Quality, and Distribution"
    publisher: Lander University, Introduction to Logic course site (updated 2021)
    url: https://philosophy.lander.Edu/logic/prop.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "5b.1: The Basics (Thinking Well: A Logic and Critical Thinking Textbook, 4th ed.)"
    publisher: Andrew Lavin, Butte College, Humanities LibreTexts (CC BY 4.0)
    url: https://human.libretexts.org/Bookshelves/Philosophy/Thinking_Well_-_A_Logic_And_Critical_Thinking_Textbook_4e_(Lavin)/05b:_Categorical_Logic/5b.1:_The_Basics
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Venn diagrams for categorical propositions (PHIL 1440 handout)"
    publisher: University of Colorado, philosophy course materials
    url: https://rintintin.colorado.edu/~vancecd/phil1440/Venn1.pdf
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Categorical proposition

A categorical proposition is a simple statement that relates two classes of things: it says that the members of a subject class are, wholly or partly, included in or excluded from a predicate class.[^s3][^s4] Four relations are possible, complete inclusion, complete exclusion, partial inclusion and partial exclusion, and each gets a standard form.[^s3] Unlike a conditional or compound statement, a categorical proposition attaches no "if" to its claim; it simply affirms or denies a predicate of all or some of a subject.[^s2]

## Origin

Aristotle analysed these statements in the works later grouped as the *Organon*. The *Prior Analytics* is the main treatment, where he builds the syllogistic out of statements that a predicate belongs to every, to some, or to no member of a subject; *De Interpretatione* sets out how affirmative and negative statements with the same terms oppose one another.[^s2] Groarke's account describes the underlying shape as "S is P": a subject term, a predicate term and a linking copula, sorted by whether the claim is universal or particular and affirmative or negative.[^s1] Aristotle also recognised indefinite statements, which syllogistic treated like particulars, and singular statements such as "Socrates is an animal", which it largely set aside.[^s2] The vowel labels A, E, I and O are medieval: A and I come from the Latin *affirmo* ("I affirm") and E and O from *nego* ("I deny").[^s1][^s2][^s3]

## How it works

A standard-form categorical proposition has four parts in a fixed order: a quantifier ("all", "no" or "some"), a subject term, a copula ("are" or "are not") and a predicate term.[^s3][^s4] Two questions fix its type. **Quantity** asks whether it is about every member of the subject class (universal) or at least one member (particular); **quality** asks whether it includes or excludes (affirmative or negative).[^s3][^s4]

- **A, universal affirmative:** All S are P (total inclusion).[^s4]
- **E, universal negative:** No S are P (total exclusion).[^s4]
- **I, particular affirmative:** Some S are P (partial inclusion).[^s4]
- **O, particular negative:** Some S are not P (partial exclusion).[^s4]

In logic "some" means only "at least one", so an I statement does not hint that an O statement is also true.[^s3] The logical subject and predicate are whatever sits between the quantifier and the copula and whatever follows the copula, which may differ from the grammatical subject and predicate.[^s3]

A workplace example: a finance policy says, "Every invoice over the limit needs a second approval." In standard form that is an A proposition: "All invoices over the limit are documents needing a second approval." An auditor's finding, "Some invoices over the limit are not documents with a second approval", is the matching O proposition. Because A and O are contradictories, exactly one of the two can be true, so a single verified counterexample is enough to show the policy is not being met in full.[^s1][^s5]

## How to apply it

To put an everyday claim into standard form, supply the missing quantifier, turn adjectives and verbs into noun phrases ("are documents needing approval" rather than "need approval"), and use the copula "are".[^s3][^s4] Watch for ambiguous phrasings: "all S is not P" can mean "no S is P" or only "some S is not P", and when context does not settle it the weaker O reading is usually the safer one.[^s3] Once claims are in standard form, you can test arguments built from them with Venn diagrams: universals are drawn by shading a region empty, particulars by placing an X in a region to show it has at least one member.[^s5]

## Limitations: existential import

The traditional and modern readings disagree about empty classes. Aristotle's system assumes that a universal claim about a subject implies the subject exists, so "all S are P" entails "some S are P".[^s1] Following George Boole, most modern courses read universal statements as making no existence claim: "all unicorns are magical" only says that any unicorns there are would be magical, while particular statements always assert that something exists.[^s5] On the modern reading, inferring "some S are P" from "all S are P" commits the existential fallacy, and only the contradictory pairs of the traditional square survive unchanged.[^s1][^s5] When you translate a claim, it is worth asking whether its subject class is known to have members.

## Connections

- **Broader: proposition.** A categorical proposition is the subject-predicate kind of statement, as opposed to conditional or compound ones.[^s2]
- **Introduced by Aristotle, in the *Prior Analytics*.** He analysed the forms there and their oppositions in *De Interpretatione*; the A/E/I/O labels came later.[^s1][^s2]
- **Studied in formal logic.** The four forms open the categorical-logic unit of introductory textbooks.[^s4]
- **Formalized by George Boole.** The Boolean reading, which strips universals of existential import, underlies the Venn-diagram treatment used in modern courses.[^s5]
- **Related: square of opposition, distribution of terms, existential import and the existential fallacy.** The square maps the truth relations among the four forms, distribution classifies their terms, and existential import is where traditional and modern readings part.[^s1][^s3][^s5]
- **Related: categorical syllogism, syllogism and the Venn diagram test.** Syllogisms are arguments made of three categorical propositions, and Venn diagrams test them.[^s2][^s5]

## Sources

[^s1]: Groarke, "Aristotle: Logic", Internet Encyclopedia of Philosophy. https://iep.utm.edu/aristotle-logic/ (accessed 2026-11-10)
[^s2]: "History of logic: Aristotle", Encyclopaedia Britannica. https://www.Britannica.Com/topic/history-of-logic/Aristotle (accessed 2026-11-10)
[^s3]: "Standard Form Categorical Propositions: Quantity, Quality, and Distribution", Introduction to Logic, Lander University. https://philosophy.lander.Edu/logic/prop.html (accessed 2026-11-10)
[^s4]: Lavin, "5b.1: The Basics", Thinking Well: A Logic and Critical Thinking Textbook (4th ed.), Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Thinking_Well_-_A_Logic_And_Critical_Thinking_Textbook_4e_(Lavin)/05b:_Categorical_Logic/5b.1:_The_Basics (accessed 2026-11-10)
[^s5]: "Venn diagrams" handout, PHIL 1440, University of Colorado. https://rintintin.colorado.edu/~vancecd/phil1440/Venn1.pdf (accessed 2026-11-10)
