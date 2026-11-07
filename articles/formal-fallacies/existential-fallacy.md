---
id: ct:existential-fallacy
type: FormalFallacy
title: Existential fallacy
aliases: [fallacy of existential assumption]
domain: formal-fallacies
summary: >-
  The formal fallacy of drawing a particular conclusion, which asserts that
  something exists, from universal premises that do not assert that their
  subject class has any members; under the modern (Boolean) reading of
  categorical propositions, a syllogism with two universal premises and a
  particular conclusion is invalid unless an existence premise is added.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:venn-diagram-test, ct:square-of-opposition, ct:syllogism, ct:illicit-major, ct:undistributed-middle, ct:method-of-counterexample]
requires: [ct:categorical-syllogism, ct:existential-import, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:existential-import, source: s2, confidence: high}
  - {predicate: confusedWith, object: ct:subalternation, source: s3, confidence: high}
criticalQuestions:
  - Do the premises say that anything in the subject class actually exists, or only what would be true of its members?
  - Could the subject class be empty, as with a rule about cases that have not happened yet?
  - If the class is known to have members, has that existence premise been stated so the argument can be checked?
  - Does a Venn diagram of the premises place an X in the region the particular conclusion needs?
argumentMap:
  premises:
    - "All employees who beat their quota this quarter will get a bonus."
    - "All employees who get a bonus will be named in the company newsletter."
  conclusion: "Some employees who beat their quota this quarter will be named in the newsletter."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "Both premises are rules about whoever beats quota; neither says that anyone did."
    - "If no one beat quota this quarter, both premises are true and the conclusion is false."
    - "Adding the premise that at least one employee beat quota makes the argument valid."
sources:
  - id: s1
    title: "Existential Fallacy"
    publisher: "Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/existential_fall.html
    type: academic
    accessed: 2026-11-07
  - id: s2
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Ciola, rev. 2025)"
    url: https://plato.stanford.edu/ENTRIES/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-07
  - id: s3
    title: "4.5 The Traditional Square of Opposition"
    publisher: "PHIL 1440 course notes, University of Colorado"
    url: https://rintintin.colorado.edu/~vancecd/phil1440/square.pdf
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "Existential Import Today: New Metatheorems; Historical, Philosophical, and Pedagogical Misconceptions"
    publisher: "History and Philosophy of Logic 36(1) (Corcoran & Masoud, 2015), PhilArchive record"
    url: https://philarchive.org/rec/COREIT
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s5
    title: "The Existential Fallacy"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://www.fallacyfiles.org/existent.html
    type: community
    accessed: 2026-11-07
created: 2026-11-07
---

# Existential fallacy

The existential fallacy is committed when a categorical argument reaches a particular conclusion ("some S are P"), which claims that at least one S exists, from universal premises that make no such claim.[^s1] Universal statements such as "all S are P" or "no S are P" say what holds of any member a class might have; they do not say the class has members. A particular conclusion therefore asserts more than the premises supply, and the argument is invalid unless independent information shows the subject class is non-empty.[^s1][^s5]

## Origin

Aristotelian and medieval logic generally treated the terms of categorical propositions as referring to existing things, and by the late Middle Ages it was a working principle that affirmative propositions carry existential import while negative ones do not.[^s2] On that assumption the traditional square of opposition licenses subalternation: from "every S is P" one may infer "some S is P."[^s2] Modern logic writes "every S is P" as a universally quantified conditional, which is vacuously true when nothing is S; on that reading most of the square's relations fall away, leaving only the contradictories, and subalternation needs an added existence premise.[^s2] The Boolean interpretation, named after George Boole and adopted by later nineteenth-century logicians, made subalternation and a handful of traditional syllogisms invalid, and introductory textbooks such as Copi and Cohen's added a rule forbidding a particular conclusion from two universal premises.[^s5]

## How it works

The fallacy appears in two shapes. The immediate-inference version moves from one universal to its particular subaltern: "All late submissions will be penalised, so some late submissions will be penalised." If no one submits late, the premise is true and the conclusion false.[^s3][^s5] The syllogistic version has two universal premises and a particular conclusion; Lander University's notes list moods such as AAI-3, EAO-1 and EAI-3 as examples.[^s1]

The argument map above is a workplace case. Both premises are policies about anyone who beats quota, so both can be true in a quarter when nobody does. The conclusion, though, says some quota-beaters exist and will be named. With no quota-beaters, the premises stay true and the conclusion fails, which is the mark of an invalid form.[^s1][^s5] Adding "at least one employee beat quota" repairs it, which is why the Lander notes call such arguments valid only conditionally.[^s1]

## How to spot it

- Check quantity. If both premises are universal (A or E) and the conclusion is particular (I or O), the argument needs an existence premise.[^s1]
- Draw the Venn diagram. Universal premises only shade regions; a particular conclusion needs an X. If the region the conclusion needs is unshaded and empty of any X, the conclusion cannot be read off.[^s1]
- Test with an empty class. Substitute a term known to be empty, as with "all unicorns are animals, so some animals are unicorns": true premise, false conclusion.[^s5]

## How to counter it

State the existence assumption openly. If the subject class is known to have members, the argument is better read as an enthymeme with a missing premise than as a fallacy, and supplying that premise makes it valid.[^s5] If membership is uncertain (future cases, hypothetical customers, ideal objects such as frictionless planes), keep the conclusion universal or conditional.[^s1][^s5] Corcoran and Masoud (2015) caution against the classroom slogan that modern logic has no existential import at all: they argue that some universal conditionals do imply their existential counterparts, depending on the antecedent predicate, so the question is case by case.[^s4]

## Connections

- **Invalid form of the categorical syllogism.** It mimics valid syllogistic moods but adds an existence claim the premises lack, which Lander's rule catches.[^s1]
- **Explained by existential import.** Whether such an inference is valid depends on whether universals are read as implying that their subject class has members.[^s2]
- **Confused with subalternation.** The immediate-inference version is traditional subalternation used without the existence assumption that made it valid; the Colorado notes give the unicorn example.[^s3]
- **Venn diagram test and square of opposition.** The diagram exposes the missing X, and the square is where the traditional and modern readings part ways.[^s1][^s2]

## Sources

[^s1]: "Existential Fallacy", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/existential_fall.html (accessed 2026-11-07)
[^s2]: Ciola, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/ENTRIES/square/ (accessed 2026-11-07)
[^s3]: "4.5 The Traditional Square of Opposition", PHIL 1440 course notes, University of Colorado. https://rintintin.colorado.edu/~vancecd/phil1440/square.pdf (accessed 2026-11-07)
[^s4]: Corcoran & Masoud, "Existential Import Today", History and Philosophy of Logic 36(1), 2015. https://philarchive.org/rec/COREIT (accessed 2026-11-07)
[^s5]: Curtis, "The Existential Fallacy", *The Fallacy Files*. https://www.fallacyfiles.org/existent.html (accessed 2026-11-07)
