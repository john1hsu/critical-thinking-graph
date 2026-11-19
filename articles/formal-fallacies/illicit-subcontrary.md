---
id: ct:illicit-subcontrary
type: FormalFallacy
title: Illicit subcontrary
aliases: [fallacy of illicit subcontrary, invalid subcontrary inference]
domain: formal-fallacies
summary: >-
  The square-of-opposition fallacy of treating the subcontrary I and O
  propositions as if they excluded each other: inferring that "Some S are not
  P" is false because "Some S are P" is true, or the reverse. Subcontraries
  cannot both be false but can both be true, so a true one settles nothing.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:square-of-opposition, ct:categorical-proposition, ct:existential-import, ct:rules-of-immediate-inference, ct:illicit-subalternation, ct:unwarranted-contrast, ct:method-of-counterexample]
requires: [ct:square-of-opposition, ct:categorical-proposition, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:subcontrariety, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-subalternation, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:unwarranted-contrast, source: s6, confidence: medium}
  - {predicate: contrastsWith, object: ct:existential-fallacy, source: s1, confidence: medium}
criticalQuestions:
  - Does the argument move from one "some" statement being true to its opposite-quality "some" statement being false?
  - Could some members of the class have the property while other members lack it, making both statements true at once?
  - Is the arguer treating "some" as if it meant "only some" or "not all", rather than "at least one"?
  - Is there separate evidence about the members not covered by the premise, or does the conclusion rest on the premise alone?
argumentMap:
  premises:
    - "Some of the pilot offices reported login errors after the update."
  conclusion: "So it is false that some of the pilot offices reported no login errors."
  verdict: invalid
  scheme: ct:subcontrariety
  objections:
    - "I and O statements can both be true; knowing that some offices had errors says nothing about whether others had none."
    - "Three offices with errors and five without would make the premise true and the conclusion false."
sameAs: []
sources:
  - id: s1
    title: "4.5 The Traditional Square of Opposition"
    publisher: "PHIL 1440 course notes, University of Colorado Boulder"
    url: https://rintintin.colorado.edu/~vancecd/phil1440/square.pdf
    type: academic
    accessed: 2026-11-19
  - id: s2
    title: "The Square of Opposition"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/square.html
    type: academic
    accessed: 2026-11-19
  - id: s3
    title: "Square of Opposition"
    publisher: "Internet Encyclopedia of Philosophy"
    url: https://iep.utm.edu/?p=2332
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s4
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Parsons, Fall 2006 archive)"
    url: https://plato.stanford.edu/archives/fall2006/entries/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s5
    title: "The Square of Opposition (Introduction to Logical Reasoning, lecture slides)"
    publisher: "David Emmanuel Gray, Northwestern University in Qatar / Carnegie Mellon University in Qatar"
    url: https://www.acsu.buffalo.edu/~degray/I2LR12-fall/Slides21.pdf
    type: academic
    accessed: 2026-11-19
  - id: s6
    title: "An Introduction to Logic: The Square of Opposition"
    publisher: "Kathy Eldred, open textbook (Pima Community College Pressbooks, 2024)"
    url: https://pimaopen.pressbooks.pub/intrologic/?p=818
    type: textbook
    accessed: 2026-11-19
created: 2026-11-19
---

# Illicit subcontrary

Illicit subcontrary is the formal fallacy of misusing the subcontrary relation on the traditional square of opposition. The particular affirmative I ("Some S are P") and the particular negative O ("Some S are not P") are subcontraries: they cannot both be false, although they may both be true.[^s2][^s5] The only valid subcontrary inference therefore runs from falsity to truth: if one of the pair is false, the other must be true.[^s1] The fallacy runs the other way, inferring that one subcontrary is false because the other is true, as if the two statements excluded each other. Course notes on the square name it, alongside illicit contrary and illicit subalternation, as one of the ways of applying the square's relations to reach a conclusion that does not follow.[^s1]

## Origin

The subcontrary pair goes back to Aristotle, although he did not state it outright. In *De Interpretatione* he set out the contradictory and contrary pairs, and Parsons argues that enough follows from those passages to show that I and O cannot both be false.[^s4] The square itself was circulating as a diagram by the second century CE, and Boethius built it into his logical writings, through which it reached medieval teaching.[^s4] Introductory logic courses still teach the square's relations as rules for immediate inference, and the Colorado notes list the misuse of each non-contradictory relation as its own named fallacy.[^s1][^s3]

## How it works

The point to remember is that subcontraries are not opposites in the way contradictories are. Contradictories always take opposite truth values, but subcontraries differ only in quality, and both can hold at once.[^s2][^s3] "Some students are hard workers" and "Some students are not hard workers" are both true of an ordinary class.[^s5] A true I can sit beside a false O ("some dogs are mammals"), and a true O can sit beside a false I ("some women are not Catholic priests").[^s6] Because all three combinations are possible, a true subcontrary leaves the other undetermined.[^s6]

The argument map shows the error in a workplace report. Learning that some pilot offices had login errors after an update is taken to show that it is false that some had none. But the offices could split, with three having errors and five running cleanly, which makes the premise true and the conclusion false.[^s2][^s5] The mirror image is just as invalid: "Some invoices were not approved, so it's false that some were approved." Only the falsity of a subcontrary licenses a conclusion: if it is false that some lunches are free, then some lunches are not free.[^s3]

These results assume the traditional reading, on which the subject class has members. With an empty subject such as unicorns, both "some unicorns have horns" and "some unicorns do not have horns" are false, so the modern Boolean square drops the subcontrary relation and keeps only contradiction.[^s3][^s5] The illicit inference fails on either reading, since it was never valid even when the class has members.[^s1][^s3]

## How to spot it

Look for a "some" statement used to rule out its opposite-quality partner: "some of X are Y, so it's wrong that some of X aren't", or the reverse.[^s2][^s6] It often rides on the everyday hearing of "some" as "only some" or "not all". In logic, "some" means at least one, so a true I says nothing about the matching O or A.[^s6] Phrases such as "so it can't be that any are not" or "which rules out exceptions" signal the move.

## How to counter it

Place both statements on the square and check which relation joins them. If they share subject and predicate but differ in quality and are both particular, they are subcontraries, and the only valid step is from a false one to a true one.[^s1][^s2] Then describe a mixed case in which some members have the property and some lack it; that makes both statements true and shows the conclusion does not follow.[^s5] If the arguer wants to deny the other subcontrary, they need direct evidence about the members the premise does not cover.

## Connections

- **Invalid form of subcontrariety.** The valid subcontrary inference passes from the falsity of I or O to the truth of the other, because the two cannot both be false; illicit subcontrary passes from truth to falsity, where the relation is silent.[^s2][^s1]
- **Contrasts with illicit subalternation.** Both misapply a relation of the square, but illicit subalternation reverses the one-way link between a universal and its particular, while illicit subcontrary treats two compatible particulars as incompatible; the Colorado notes list them as separate fallacies.[^s1]
- **Contrasts with unwarranted contrast.** Unwarranted contrast infers that the other subcontrary is true ("some are, so some are not"); illicit subcontrary infers that it is false. Both go wrong for the same reason: a true I or O fixes nothing about its partner.[^s6]
- **Contrasts with the existential fallacy.** The existential fallacy is about empty subject classes, the case in which the square's relations, the subcontrary one included, break down; illicit subcontrary is invalid even when the class has members.[^s1][^s3]

## Sources

[^s1]: "4.5 The Traditional Square of Opposition", PHIL 1440 course notes, University of Colorado Boulder. https://rintintin.colorado.edu/~vancecd/phil1440/square.pdf (accessed 2026-11-19)
[^s2]: "The Square of Opposition", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/square.html (accessed 2026-11-19)
[^s3]: "Square of Opposition", Internet Encyclopedia of Philosophy. https://iep.utm.edu/?p=2332 (accessed 2026-11-19)
[^s4]: Terence Parsons, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (Fall 2006 archive). https://plato.stanford.edu/archives/fall2006/entries/square/ (accessed 2026-11-19)
[^s5]: David Emmanuel Gray, "The Square of Opposition", Introduction to Logical Reasoning lecture slides, Northwestern University in Qatar / Carnegie Mellon University in Qatar. https://www.acsu.buffalo.edu/~degray/I2LR12-fall/Slides21.pdf (accessed 2026-11-19)
[^s6]: Kathy Eldred, *An Introduction to Logic* (open textbook, 2024), "The Square of Opposition". https://pimaopen.pressbooks.pub/intrologic/?p=818 (accessed 2026-11-19)
