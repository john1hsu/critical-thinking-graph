---
id: ct:categorical-syllogism
type: ReasoningForm
title: Categorical syllogism
aliases: [standard-form categorical syllogism, Aristotelian syllogism, mood and figure]
domain: formal-logic
summary: >-
  A deductive argument made of exactly three categorical propositions (two
  premises and a conclusion) using exactly three terms, each appearing twice;
  its form is fixed by its mood and figure, and validity depends on that form
  alone.
level: introductory
evidenceStatus: normative
broader: [ct:syllogism]
related: [ct:rules-of-the-categorical-syllogism, ct:venn-diagram-test, ct:distribution-of-terms, ct:square-of-opposition, ct:john-buridan, ct:belief-bias, ct:antilogism]
requires: [ct:categorical-proposition, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s5, confidence: high}
argumentMap:
  premises:
    - "No contractors have administrator access."
    - "All summer interns are contractors."
  conclusion: "No summer interns have administrator access."
  verdict: valid
  objections:
    - "The form (EAE-1, Celarent) is valid, but if any intern was hired as a regular employee the second premise is false and the conclusion is unproven."
sameAs: []
sources:
  - id: s1
    title: "History of logic: Syllogisms"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/history-of-logic/Syllogisms
    type: encyclopedia
    accessed: 2026-11-10
  - id: s2
    title: "Medieval Theories of the Syllogism"
    publisher: Stanford Encyclopedia of Philosophy (Lagerlund, Spring 2005 archive edition)
    url: https://plato.stanford.edu/archives/spr2005/entries/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s3
    title: "6.1 Standard Form, Mood, and Figure (lecture notes)"
    publisher: "PHIL 240 Introduction to Logic, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.1.pdf
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Categorical Syllogisms (Introduction to Philosophy, ch. 2: Logic)"
    publisher: "Lumen Learning for El Paso Community College (adapted from Kemerling, Philosophy Pages, CC BY-SA)"
    url: https://courses.lumenlearning.com/elpaso-introphilosophy/?p=395
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Presentation format and syllogistic reasoning"
    publisher: "Psicologica 34, 313-326 (Espino & Santamaria, 2013)"
    url: https://www.uv.es/revispsi/articulos2.13/10Espino.pdf
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Categorical syllogism

A categorical syllogism is a deductive argument built from exactly three categorical propositions, two premises and a conclusion, which together use exactly three terms, each of them twice.[^s3] Every statement has one of four shapes: A (all S are P), E (no S are P), I (some S are P) or O (some S are not P). Because the argument's form is fully captured by which shapes appear and where the shared term sits, every syllogism with the same form is valid or every one is invalid.[^s4]

## Origin

Aristotle built the first theory of these arguments, a logic of terms in which a middle term links two premises and then drops out of the conclusion. He sorted them into three figures by where the middle term sits and claimed that every syllogism falls into one of them.[^s1] Later logicians added a fourth figure for arrangements Aristotle mentioned but did not group separately; his successor Theophrastus had folded those into the first figure instead.[^s1] Lagerlund's survey of the medieval tradition shows the fourth-figure moods being listed and debated from Aristotle's *Prior Analytics* onward: Abelard treated them as first-figure moods with a converted conclusion, and Buridan defined them as first-figure arguments with transposed premises.[^s2] Medieval teachers also gave each valid mood a Latin mnemonic name, such as Barbara, Celarent or Ferio.[^s2]

## How it works

Putting an argument into standard form is the first step. The conclusion's predicate is the major term and its subject the minor term; the term found in both premises but not the conclusion is the middle term. The premise containing the major term is the major premise and is written first, followed by the minor premise and then the conclusion.[^s3][^s4]

The form then gets a two-part label. The **mood** lists the letters of the major premise, minor premise and conclusion in that order, such as EAE. The **figure** records the middle term's position: first figure M-P / S-M, second P-M / S-M, third M-P / M-S, fourth P-M / M-S.[^s3] With four statement types in three slots and four figures, there are 256 possible forms.[^s4] Lecture notes from a Texas A&M logic course give the standard counts: on the modern reading only 15 are valid, while Aristotle's assumption that every term names a non-empty class adds nine more, for 24.[^s3] Mood alone does not settle validity. "No birds are mammals; all dogs are mammals; so no dogs are birds" is EAE-2 and valid, but "No mammals are birds; all mammals are animals; so no animals are birds" is EAE-3 and invalid.[^s3]

The argument map shows EAE-1, the mood the mnemonics call Celarent. "Contractors" is the middle term, subject of the major premise and predicate of the minor premise, so the form is first figure. The mnemonic names encode more than the mood. Their vowels give the three letters, the opening consonant names the first-figure mood a proof reduces to, and letters such as *s*, *p*, *m* and *c* record which conversion, premise swap or indirect proof the reduction uses.[^s1] Aristotle took the first-figure moods as basic and proved the rest through conversion, apart from Baroco and Bocardo, which need proof by contradiction. Britannica's history calls the result the first deductive system in the history of logic.[^s1]

## How to apply it

Name the conclusion and its two terms, find the middle term, and restate each sentence as an A, E, I or O proposition with the same terms throughout. Then order the premises and read off the mood and figure.[^s4] Check that label against the list of valid forms, or test it with the Venn diagram method or the syllogistic rules. If the form is invalid, confirm it by finding substitute terms that make both premises true and the conclusion false: the Lumen text uses terriers, dogs and mammals to break an AAA-3 argument.[^s4] If the form is valid only on the traditional count of 24, the argument assumes some class has members, so check that assumption separately.[^s3] Finally, judge whether the premises are true, since a valid form guarantees nothing about them.

## Evidence and limitations

Validity of a mood is a normative matter, but how people handle these arguments has been studied for decades. A robust finding is the figural effect: the order of terms in the premises steers the direction of the conclusion people draw. Espino and Santamaria's 2013 review cites Johnson-Laird and Bara's 1984 experiment, where premises arranged A-B, B-C drew A-C conclusions in 78% of answers, and their own study replicated that pattern (66% A-C).[^s5] They also report that reasoners find a syllogism easier when its valid conclusion runs in the direction the figure suggests.[^s5] Psychologists number figures by term order rather than by the textbook scheme, so a "figure 4" in that research is not the textbook fourth figure. Logically, the categorical syllogism's reach is narrow: it handles only arguments that reduce to three class terms, and medieval writers already kept extending it with indirect moods and new proof methods.[^s2]

## Connections

- **Introduced by Aristotle.** Aristotle defined the middle-term structure and the figures and proved the non-first-figure moods by reduction.[^s1]
- **Introduced in the Prior Analytics.** Medieval commentators listed the moods and fourth-figure variants from the *Prior Analytics*, and Lagerlund traces their debates over it.[^s2]
- **Studied in cognitive psychology.** Experiments on figural effects measure how term order shapes the conclusions people draw.[^s5]
- **Broader: syllogism; requires categorical propositions and validity.** It is the term-based branch of the syllogism family. Analysing one presupposes the A/E/I/O statement forms and the notion of validity.[^s3]
- **Related tests and history.** The rules of the categorical syllogism and the Venn diagram test are the standard ways to check a mood and figure.[^s4] Buridan's indirect moods extended the medieval count of valid forms.[^s2]

## Sources

[^s1]: "History of logic: Syllogisms", Encyclopaedia Britannica. https://britannica.com/topic/history-of-logic/Syllogisms (accessed 2026-11-10)
[^s2]: Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (Spring 2005 archive), sections 1, 4 and 8. https://plato.stanford.edu/archives/spr2005/entries/medieval-syllogism/ (accessed 2026-11-10)
[^s3]: "6.1 Standard Form, Mood, and Figure", PHIL 240 Introduction to Logic lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.1.pdf (accessed 2026-11-10)
[^s4]: "Categorical Syllogisms", *Introduction to Philosophy*, ch. 2, Lumen Learning / El Paso Community College (adapted from Kemerling, Philosophy Pages). https://courses.lumenlearning.com/elpaso-introphilosophy/?p=395 (accessed 2026-11-10)
[^s5]: Espino & Santamaria, "Presentation format and syllogistic reasoning", Psicologica 34, 313-326 (2013). https://www.uv.es/revispsi/articulos2.13/10Espino.pdf (accessed 2026-11-10)
