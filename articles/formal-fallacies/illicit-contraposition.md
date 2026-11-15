---
id: ct:illicit-contraposition
type: FormalFallacy
title: Illicit contraposition
aliases: [fallacy of illicit contraposition, invalid contraposition, contraposition of E or I]
domain: formal-fallacies
summary: >-
  The formal fallacy of taking the contrapositive of a universal negative (E)
  or particular affirmative (I) categorical proposition as following from it,
  as in inferring "no non-P are non-S" from "no S are P". Contraposition
  preserves truth only for A and O statements.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:illicit-conversion, ct:categorical-proposition, ct:square-of-opposition, ct:existential-import, ct:venn-diagram-test, ct:method-of-counterexample, ct:modus-tollens, ct:obversion, ct:topics]
requires: [ct:categorical-proposition, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:contraposition, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-conversion, source: s2, confidence: high}
criticalQuestions:
  - Is the starting statement a "No S are P" or a "Some S are P" statement? If so, does its contrapositive really follow?
  - What does the original statement say about things that are neither S nor P, and does the conclusion claim more than that?
  - Can you name something that is neither S nor P which would make the conclusion false while the premise stays true?
  - If only a weaker claim is needed, would the obverse or the simple converse of the statement serve instead?
argumentMap:
  premises:
    - "No contractors are on the company payroll."
  conclusion: "So no one who is off the payroll is a non-contractor; everyone off the payroll is a contractor."
  verdict: invalid
  scheme: ct:contraposition
  objections:
    - "The premise only separates contractors from payroll staff; it says nothing about people who are neither, such as agency temps, interns paid by a university or visiting auditors."
    - "One agency temp who is off the payroll and is not a contractor keeps the premise true and makes the conclusion false."
sources:
  - id: s1
    title: "Lecture notes 5.3: Conversion, obversion and contraposition"
    publisher: "PHIL 240 Introduction to Logic, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/5.3.pdf
    type: academic
    accessed: 2026-11-15
  - id: s2
    title: "Chapter 11: Categorical Equivalence"
    publisher: "Critical Thinking, Logic, and Argument, AU Press (Athabasca University)"
    url: https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/041ee19f-22e4-4f3e-a817-cf21ee373d10
    type: textbook
    accessed: 2026-11-15
  - id: s3
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Parsons, Summer 2012 archive)"
    url: https://plato.stanford.edu/archives/sum2012/entries/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-15
  - id: s4
    title: "Topics, Book II, Chapter 8 (trans. W. A. Pickard-Cambridge)"
    publisher: "Aristotle, Logos Library"
    url: https://logoslibrary.org/aristotle/topics/208.html
    type: primary
    accessed: 2026-11-15
  - id: s5
    title: "Illicit Contraposition"
    publisher: "The Fallacy Files (Gary N. Curtis)"
    url: https://fallacyfiles.org/ilcontra.html
    type: community
    accessed: 2026-11-15
  - id: s6
    title: "Immediate Inferences"
    publisher: "Philosophy Pages (Garth Kemerling)"
    url: https://mail.philosophypages.com/lg/e07b.htm
    type: community
    accessed: 2026-11-15
created: 2026-11-15
---

# Illicit contraposition

Illicit contraposition is the formal fallacy of treating the contrapositive of a categorical statement as following from it when the statement is of a form that contraposition does not preserve. To contrapose a statement, you swap its subject and predicate and replace each with its complement, so "All crows are birds" becomes "All non-birds are non-crows".[^s1][^s6] For universal affirmative (A) and particular negative (O) statements the contrapositive is equivalent to the original. For universal negative (E) and particular affirmative (I) statements it is not, and drawing it anyway is the fallacy.[^s1][^s2][^s5]

## Origin

Aristotle already used the term-level move in the *Topics*: if man is an animal, what is not an animal is not a man, with the order of the terms reversed once they are negated, and he recommends it as a way to both attack and support a thesis.[^s4] Terence Parsons' SEP entry reports that "conversion by contraposition" as a rule for the A and O forms appears in twelfth-century tracts and is endorsed by Peter of Spain and William of Sherwood, while Aristotle did not list it among his conversions.[^s3] Modern textbooks present contraposition beside conversion and obversion as one of three immediate inferences, and teach that it holds in general for A and O but not for E and I.[^s1][^s2] Gary Curtis's Fallacy Files names the misuse illicit contraposition, classifies it as a quantificational formal fallacy and credits Patrick Hurley's logic textbook for the treatment.[^s5]

## How it works

An E statement such as "No contractors are on the payroll" tells you that two classes do not overlap. It says nothing about the region outside both classes. Its contrapositive, "No non-payroll people are non-contractors", amounts to saying that everyone off the payroll is a contractor, which is a claim about exactly that unexamined region.[^s2][^s5] The workplace map above shows the gap: agency temps or visiting auditors can be neither contractors nor payroll staff, so the premise is true and the conclusion false. The AU Press textbook makes the same point with pickles: no pickles are red, yet plenty of non-red things are not pickles.[^s2]

The I form fails for a similar reason. "Some apples are red" does not show that "some non-red things are non-apples", because the premise is silent about the rest of the universe of discourse.[^s2] Counterexamples here are harder to build, since the conclusion is false only when the two classes overlap and together exhaust everything, as in "some physical things are invisible" against "some visible things are non-physical".[^s5] Some particular E and I statements do have true contrapositives; the point is that the form does not guarantee it, so the original's truth leaves the contrapositive's truth open.[^s1][^s5]

## How to spot it

Look for an inference that reverses the order of two terms and puts "non-" (or "not", "anyone who isn't") in front of both. Then check the starting statement's form. If it begins "No ..." or "Some ... are ..." the contrapositive needs its own evidence.[^s1][^s2] Everyday versions often surface as "None of X are Y, so anyone who isn't Y must be X", which is the E contrapositive restated through obversion.[^s2][^s6] A Venn diagram makes the error visible: the E and I diagrams leave the area outside both circles blank, while the contrapositive asserts something about it.[^s5]

## How to counter it

Name one thing that is neither S nor P, and ask whether the premise rules it out. If it does not, the inference is invalid.[^s5] Then say what does follow. From an E statement, the traditional rule of contraposition by limitation allows only the particular "some non-P are not non-S", and only if the subject class has members.[^s6] Obversion and, for E and I, simple conversion are always available and may be all the argument needed.[^s6]

## Limitations and history

Validity here depends on how empty and universal terms are handled. Parsons reports that Buridan used examples such as "every man is a being" to argue that even A and O contraposition fail when a complement class is empty, and that later logicians restored the rule by assuming non-empty terms, an assumption Keynes described as made implicitly.[^s3] Modern textbooks that treat A and O contraposition as valid rely on such conventions about term complements and existential import.[^s1][^s3]

## Connections

- **Invalid form of contraposition.** Contraposition is a valid immediate inference for A and O statements; illicit contraposition applies the same operation to E and I statements, where it no longer preserves truth.[^s1][^s2]
- **Contrasts with illicit conversion.** The two errors are mirror images: conversion holds for E and I but fails for A and O, while contraposition holds for A and O but fails for E and I.[^s2][^s6]

## Sources

[^s1]: "Conversion, obversion and contraposition", PHIL 240 lecture notes 5.3, Texas A&M University. https://phil240.tamu.edu/LectureNotes/5.3.pdf (accessed 2026-11-15)
[^s2]: "Chapter 11: Categorical Equivalence", *Critical Thinking, Logic, and Argument*, AU Press. https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/041ee19f-22e4-4f3e-a817-cf21ee373d10 (accessed 2026-11-15)
[^s3]: Terence Parsons, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (Summer 2012 archive). https://plato.stanford.edu/archives/sum2012/entries/square/ (accessed 2026-11-15)
[^s4]: Aristotle, *Topics* II.8, trans. W. A. Pickard-Cambridge, Logos Library. https://logoslibrary.org/aristotle/topics/208.html (accessed 2026-11-15)
[^s5]: Gary N. Curtis, "Illicit Contraposition", The Fallacy Files. https://fallacyfiles.org/ilcontra.html (accessed 2026-11-15)
[^s6]: Garth Kemerling, "Immediate Inferences", Philosophy Pages. https://mail.philosophypages.com/lg/e07b.htm (accessed 2026-11-15)
