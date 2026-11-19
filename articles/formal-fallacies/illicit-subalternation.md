---
id: ct:illicit-subalternation
type: FormalFallacy
title: Illicit subalternation
aliases: [fallacy of illicit subalternation, invalid subalternation]
domain: formal-fallacies
summary: >-
  The square-of-opposition fallacy of running subalternation in the wrong
  direction: inferring a universal (A or E) is true because its particular (I
  or O) is true, or inferring a particular is false because its universal is
  false. Subalternation only carries truth down and falsity up.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:square-of-opposition, ct:categorical-proposition, ct:existential-import, ct:rules-of-immediate-inference, ct:unwarranted-contrast, ct:hasty-generalization, ct:method-of-counterexample]
requires: [ct:square-of-opposition, ct:categorical-proposition, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:subalternation, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:existential-fallacy, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:illicit-major, source: s5, confidence: medium}
criticalQuestions:
  - Does the conclusion claim something about every member of a class when the premise only reports some members?
  - Does the argument move from "not all" to "none", treating the falsity of a universal as the falsity of its particular?
  - Can you describe a case where the premise holds and the conclusion fails, such as a class where some but not all members have the property?
  - Is there independent evidence for the universal claim, or is the particular case doing all the work?
argumentMap:
  premises:
    - "Some of the laptops in the returns bin have cracked screens."
  conclusion: "So all of the laptops in the returns bin have cracked screens."
  verdict: invalid
  scheme: ct:subalternation
  objections:
    - "Subalternation runs from the universal to the particular; a true particular leaves the universal undetermined."
    - "The bin could hold one laptop with a cracked screen and nine returned for battery faults, which keeps the premise true and makes the conclusion false."
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
    url: https://iep.utm.edu/sqr-opp/?no_redirect=true
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s4
    title: "The Traditional Square of Opposition"
    publisher: "Stanford Encyclopedia of Philosophy (Parsons, Spring 2012 archive)"
    url: https://plato.stanford.edu/archives/spr2012/entries/square/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s5
    title: "Illicit Major and Illicit Minor"
    publisher: "Philosophy 103: Introduction to Logic, Lander University"
    url: https://philosophy.lander.edu/logic/illicit_fall.html
    type: academic
    accessed: 2026-11-19
  - id: s6
    title: "Week 2-B: The Traditional Square of Opposition"
    publisher: "Introductory logic course notes (Copi/Cohen sec. 5.4), DePaul University"
    url: https://condor.depaul.edu/mlarrabe/logic/wk2b.htm
    type: academic
    accessed: 2026-11-19
created: 2026-11-19
---

# Illicit subalternation

Illicit subalternation is the formal fallacy of using the subaltern relation of the traditional square of opposition in a direction it does not support. On the square, a universal statement (A, "All S are P", or E, "No S are P") is the superaltern of the particular statement of the same quality (I, "Some S are P", or O, "Some S are not P").[^s2][^s3] Subalternation licenses two moves only: truth flows down from universal to particular, and falsity flows up from particular to universal.[^s1][^s2] Reversing either move, by inferring a true universal from a true particular or a false particular from a false universal, is illicit subalternation. Course texts list it with illicit contrary and illicit subcontrary as the three ways of misapplying the square's relations, each of which yields an invalid argument.[^s1]

## Origin

The relations of the square trace back to Aristotle's *De Interpretatione*, chapters 6 and 7, which state the contradictory and contrary pairs; subalternation is not stated there as such but follows from them.[^s4] The square was drawn as a diagram in Boethius's commentaries around 500 CE and became standard in medieval teaching, where the universal was named the superaltern and the particular its subaltern.[^s2][^s4] Because the relation is defined as one-way, its misuse has been treated as an error for as long as the square has been taught; course notes keyed to Copi and Cohen's textbook stress that the reverse inference is not valid.[^s6]

## How it works

The valid inferences are easy to state. If "all pizza is delicious" is true, then "some pizza is delicious" is true; if "some people can fly" is false, then "all people can fly" is false.[^s1] The other two cases are undetermined: a false A tells us nothing about I, and a true I tells us nothing about A. The same holds for E and O.[^s2] Illicit subalternation treats one of those undetermined cases as settled.

It takes two forms. The upward form infers a universal from a particular, as in the argument map: some returned laptops have cracked screens, therefore all of them do. A true particular is compatible with a false universal, so the conclusion does not follow.[^s2][^s6] The downward form infers the falsity of a particular from the falsity of a universal: "It's false that every branch hit its sales target, so it's false that some branch hit it." Not all is not the same as none, so a false A leaves I open.[^s2][^s3]

The analysis assumes the traditional reading, on which the subject class has members. On the modern Boolean reading, universals lack existential import and even the valid direction of subalternation fails: "all unicorns have horns" can be true while "some unicorns have horns" is false.[^s3][^s4] The reverse inferences that make up this fallacy are invalid on both readings.[^s1][^s3]

## How to spot it

Look for a single statement used to justify another that differs only in quantity: "some" becoming "all" or "every", "some ... not" becoming "none", or "not all" becoming "not any".[^s2][^s6] Workplace versions include generalising from a few complaints to "every customer is unhappy", and turning "not every test passed" into "no tests passed". If the premise and conclusion share subject, predicate and quality but the conclusion is the stronger universal, or the denial reaches down to the particular, the inference runs against the subaltern relation.[^s1][^s2]

## How to counter it

Place the two statements on the square and check the direction. Truth may move from A to I or from E to O; falsity may move from I to A or from O to E; nothing else follows.[^s1][^s2] Then build a counterexample in which the premise holds and the conclusion fails, such as a returns bin where one laptop is cracked and the rest are not.[^s6] If the universal claim matters, it needs evidence about the whole class, not about some of its members.

## Connections

- **Invalid form of subalternation.** Subalternation validly passes truth from a universal to its particular and falsity from a particular to its universal; illicit subalternation runs the same relation the other way, where the result is undetermined.[^s2][^s3]
- **Contrasts with the existential fallacy.** Both concern the line between universal and particular, but the existential fallacy uses the valid direction of subalternation on an empty subject class, while illicit subalternation uses the invalid direction; course texts list them as separate errors.[^s1][^s4]
- **Contrasts with illicit major.** The Lander notes compare the illicit major, which moves from some of a class in a premise to all of it in a conclusion, with going from a true subaltern to an undetermined superaltern; illicit subalternation is the single-statement version of the same overreach.[^s5][^s2]
- **Related to unwarranted contrast and hasty generalization.** Unwarranted contrast misuses the subcontrary relation between I and O, and the upward form of illicit subalternation mirrors the informal leap from some cases to all.[^s1][^s5]

## Sources

[^s1]: "4.5 The Traditional Square of Opposition", PHIL 1440 course notes, University of Colorado Boulder. https://rintintin.colorado.edu/~vancecd/phil1440/square.pdf (accessed 2026-11-19)
[^s2]: "The Square of Opposition", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/square.html (accessed 2026-11-19)
[^s3]: "Square of Opposition", Internet Encyclopedia of Philosophy. https://iep.utm.edu/sqr-opp/?no_redirect=true (accessed 2026-11-19)
[^s4]: Terence Parsons, "The Traditional Square of Opposition", Stanford Encyclopedia of Philosophy (Spring 2012 archive). https://plato.stanford.edu/archives/spr2012/entries/square/ (accessed 2026-11-19)
[^s5]: "Illicit Major and Illicit Minor", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/illicit_fall.html (accessed 2026-11-19)
[^s6]: "Week 2-B: The Traditional Square of Opposition", introductory logic course notes (Copi/Cohen sec. 5.4), DePaul University. https://condor.depaul.edu/mlarrabe/logic/wk2b.htm (accessed 2026-11-19)
