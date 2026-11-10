---
id: ct:quantifier-shift-fallacy
type: FormalFallacy
title: Quantifier shift fallacy
aliases: [illicit quantifier shift, quantifier switch fallacy, fallacy of every and some]
domain: formal-fallacies
summary: >-
  The invalid inference from "every A stands in relation R to some B" to
  "some single B stands in relation R to every A", which swaps the order of a
  universal and an existential quantifier and so turns a weak claim into a
  much stronger one.
level: intermediate
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:amphiboly, ct:ambiguity, ct:method-of-counterexample, ct:peter-geach, ct:aristotle]
requires: [ct:predicate-logic, ct:validity]
relations:
  - {predicate: formalizedBy, object: ct:predicate-logic, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:quantifier-scope, source: s2, confidence: high}
criticalQuestions:
  - Does the premise allow a different B for each A, or does it really say one B serves them all?
  - Can you describe a case where every A has its own B but no single B works for every A?
  - If the conclusion needs one B for all, what separate evidence shows that such a B exists?
argumentMap:
  premises:
    - "Every project in the portfolio has someone on the finance team who can sign off its budget."
  conclusion: "Someone on the finance team can sign off every project's budget."
  verdict: invalid
  objections:
    - "Sign-off rights may be split by business unit, so each project has an approver but no one approves all of them."
    - "To show one person covers everything, check the approval matrix directly; the premise does not say so."
sources:
  - id: s1
    title: "Some Examples of Multiple Quantification"
    publisher: "A Modern Formal Logic Primer, Vol. II, ch. 3 (Paul Teller), LibreTexts Humanities"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/03%3A_Volume_II-_Predicate_Logic/3.03%3A_More_about_Quantifiers/3.3.01%3A_Some_Examples_of_Multiple_Quantification
    type: textbook
    accessed: 2026-11-10
  - id: s2
    title: "The Quantifier Shift Fallacy"
    publisher: "Introduction to Philosophy course notes, University of Arkansas (Richard Lee)"
    url: https://rlee.hosted.uark.edu/intrsp03/oh/quantifiershift.html
    type: academic
    accessed: 2026-11-10
  - id: s3
    title: "Aquinas's \"Third Way\""
    publisher: "Introduction to Philosophy course notes, University of Arkansas (Richard Lee)"
    url: https://rlee.hosted.uark.edu/intrsp07/oh/3rd-way-plus.html
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Aristotle's Illicit Quantifier Shift: Is He Guilty or Innocent"
    publisher: "Aristos 1(2), 1-18, University of Notre Dame Australia (Jack Green, 2015)"
    url: https://core.ac.uk/download/344751851.pdf
    type: academic
    accessed: 2026-11-10
  - id: s5
    title: "Quantifier-Shift Fallacy"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/quanshif.html
    type: community
    accessed: 2026-11-10
created: 2026-11-10
---

# Quantifier shift fallacy

The quantifier shift fallacy is the invalid step from a statement of the form "for every x there is some y such that x is related to y" to "there is some y such that every x is related to it". In predicate-logic notation it moves from ∀x∃y Rxy to ∃y∀x Rxy.[^s2][^s5] The premise lets the y vary from one x to the next; the conclusion demands a single y that serves every x. Because the fault lies in the order of the quantifiers rather than in the subject matter, every argument of this shape is invalid, even when its conclusion happens to be true.[^s1][^s2]

## Origin

Mixed quantifiers only became fully explicit with modern predicate logic, where the order in which "every" and "some" are written fixes what a sentence says.[^s1] The name "quantifier shift" is used in philosophical reference works, and the logician Peter Geach used it in a 1980 essay titled "History of a fallacy" in a way suggesting he coined it.[^s5] The error itself is much older. Geach and G. E. M. Anscombe charged Aristotle with it at the opening of the *Nicomachean Ethics*, reading him as moving from "every action aims at some good" to "there is one good at which all actions aim". A 2015 study by Jack Green argues that the charge fails once Aristotle's "the good" is read as a formal notion rather than a single object, which shows that whether a historical text commits the fallacy can itself be disputed.[^s4]

The best-known textbook case is the third of Thomas Aquinas's "five ways". One step infers from "each thing at some time does not exist" that "at some time nothing exists". Logic teachers flag this step as a quantifier shift: each thing could fail to exist at a different time without there ever being a moment when everything is absent.[^s3][^s2]

## How it works

The premise and conclusion differ in strength. "Everyone is loved by someone" only says no one goes unloved, and different people may be loved by different lovers. "Someone loves everyone" says a single person loves all. The second implies the first, but the first does not imply the second.[^s1] So the inference from ∃y∀x to ∀x∃y is valid, while the reverse is not. The Fallacy Files suggests that this resemblance between a valid and an invalid direction is why the slip comes so easily.[^s5]

The argument map above shows the pattern at work. Every project has a finance team member who can sign off its budget, but rights may be split by business unit, so each project has its own approver. The premise is then true and the conclusion, that one person can sign off every budget, is false. A simple counterexample proves the form invalid.[^s2] Lee's example has the same shape: each university class has a teacher who teaches it, but it does not follow that one teacher teaches every class.[^s2] Mathematics gives a clean case too: every integer has a larger integer, yet there is no integer larger than all of them.[^s5]

## How to spot it

Look for an argument that starts from "each", "every" or "all" combined with "a", "some" or "an" inside the claim, and ends with "one", "the same" or "a single" thing that applies across the board.[^s2][^s5] Rewriting both sentences with explicit quantifiers helps, because the scope order then shows on the page: ∀ before ∃ in the premise, ∃ before ∀ in the conclusion.[^s1] Ordinary English often leaves scope unclear, so the shift can hide inside a sentence that reads naturally both ways.[^s5]

## How to counter it

Ask whether the premise lets the "some" vary with the "every". If it does, build a counterexample in which each case gets its own item, such as a different teacher for each class or a different approver for each project.[^s2] Then point out that the conclusion needs extra evidence: to show one approver covers every budget, you have to check for that person directly, not infer them from coverage of each budget one at a time.[^s1][^s2] When reading a historical argument, also consider a charitable reading in which no shift is made, as Green does for Aristotle, before calling the fallacy.[^s4]

## Connections

- **Formalized by predicate logic.** Predicate logic makes quantifier order explicit and shows that ∃y∀x implies ∀x∃y but not the reverse.[^s1]
- **Explained by quantifier scope.** The fallacy is a change in which quantifier takes wider scope, from the universal in the premise to the existential in the conclusion.[^s2][^s5]
- **Related to amphiboly and ambiguity.** Scope ambiguity in English sentences lets the shift pass unnoticed, so the error sits on the border between formal and informal fallacy.[^s5]
- **Related to the method of counterexample.** A case where each A has its own B and no B serves all is the standard way to show invalidity.[^s2]
- **Related to Peter Geach and Aristotle.** Geach probably coined the name and, with Anscombe, charged Aristotle with it, a charge later disputed.[^s4][^s5]

## Sources

[^s1]: P. Teller, "Some Examples of Multiple Quantification", *A Modern Formal Logic Primer*, Vol. II, LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/A_Modern_Formal_Logic_Primer_(Teller)/03%3A_Volume_II-_Predicate_Logic/3.03%3A_More_about_Quantifiers/3.3.01%3A_Some_Examples_of_Multiple_Quantification (accessed 2026-11-10)
[^s2]: R. Lee, "The Quantifier Shift Fallacy", course notes, University of Arkansas. https://rlee.hosted.uark.edu/intrsp03/oh/quantifiershift.html (accessed 2026-11-10)
[^s3]: R. Lee, "Aquinas's 'Third Way'", course notes, University of Arkansas. https://rlee.hosted.uark.edu/intrsp07/oh/3rd-way-plus.html (accessed 2026-11-10)
[^s4]: J. Green, "Aristotle's Illicit Quantifier Shift: Is He Guilty or Innocent", *Aristos* 1(2), 1-18 (2015). https://core.ac.uk/download/344751851.pdf (accessed 2026-11-10)
[^s5]: G. N. Curtis, "Quantifier-Shift Fallacy", The Fallacy Files. https://fallacyfiles.org/quanshif.html (accessed 2026-11-10)
