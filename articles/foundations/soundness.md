---
id: ct:soundness
type: Concept
title: Soundness
aliases: [sound argument, sound deductive argument]
domain: foundations
summary: >-
  The property of a deductive argument that is valid and whose premises are all
  actually true; a sound argument therefore guarantees a true conclusion.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:validity, ct:method-of-counterexample, ct:aristotle, ct:principle-of-charity, ct:posterior-analytics]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: contrastsWith, object: ct:cogency, source: s4, confidence: high}
  - {predicate: confusedWith, object: ct:soundness-theorem, source: s1, confidence: medium}
  - {predicate: partOf, object: ct:argument-evaluation, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:posterior-analytics, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Validity and Soundness"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/page/val-snd/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "1.7: Soundness, in Introduction to Logic and Critical Thinking (2nd ed.)"
    publisher: Matthew Van Cleave, Humanities LibreTexts
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Introduction_to_Logic_and_Critical_Thinking_2e_(van_Cleave)/01%3A_Reconstructing_and_Analyzing_Arguments/1.07%3A_Soundness
    type: textbook
    accessed: 2026-11-03
  - id: s3
    title: "Logic Primer, section 1.1: Sentences, arguments, validity and soundness"
    publisher: Logic Primer (MIT Press), online edition hosted by Texas A&M University
    url: https://logic.tamu.edu/Primer/1.1.html
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "Introduction: soundness and cogency, in How to Think Critically"
    publisher: CAUL OER Collective (Council of Australian University Librarians)
    url: https://oercollective.caul.edu.au/howtothinkcritically/?p=103
    type: textbook
    accessed: 2026-11-03
  - id: s5
    title: "Soundness, in The Logic Notes"
    publisher: Australian National University
    url: https://users.cecs.anu.edu.au/~jks/LogicNotes/soundness.html
    type: academic
    accessed: 2026-11-03
  - id: s6
    title: "Posterior Analytics, Book I (trans. G. R. G. Mure)"
    publisher: Aristotle, Elpenor Greek texts library
    url: https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/posterior-analytics.asp?pg=3
    type: primary
    accessed: 2026-11-03
created: 2026-11-03
---

# Soundness

A deductive argument is sound when it passes two tests at once: it is valid, and every one of its premises is actually true. If either test fails, the argument is unsound.[^s1][^s2] Because validity guarantees that true premises carry their truth through to the conclusion, a sound argument always has a true conclusion. That is a consequence of the definition rather than part of it.[^s1][^s3] Soundness is the standard a deductive argument has to meet before it can be said to *prove* its conclusion, not merely to have the right shape.

## Origin

The idea that a good proof needs true starting points, and not just a correct form, is old. In *Posterior Analytics* I.2, Aristotle separated deduction in general from demonstration. Any deduction can have a correct form, but only one whose premises are true, primary, better known than the conclusion, and explanatory of it produces scientific knowledge.[^s6] Modern logic textbooks keep the core of that idea and drop most of Aristotle's extra conditions: a sound argument is simply a valid argument with all true premises.[^s2][^s3] The term also has a separate technical sense in mathematical logic. There, a proof system is called sound when everything it can derive is semantically valid, a property of whole calculi rather than of single arguments.[^s1][^s5]

## How it works

Soundness divides the work of evaluation in two. Form decides whether the premises would support the conclusion, and content decides whether the premises are in fact true. The Internet Encyclopedia of Philosophy says a deductive argument must be assessed in both ways.[^s1] Logic can settle the first question. The second usually needs evidence from outside logic, such as records, measurements, experts, or the relevant field of study.[^s2]

A workplace example shows the difference. "Every invoice over $10,000 needs sign-off from the finance director. This invoice is for $14,200. So this invoice needs the finance director's sign-off." The argument is valid. Whether it is sound depends on whether the policy really reads that way and whether the invoice amount is right. Checking the policy document and the invoice settles it. Now change one premise: "Every vendor on the approved list has passed a security audit. Acme is on the approved list. So Acme has passed a security audit." The form is just as valid. But suppose Acme was carried over from an older list without an audit. Then the first premise is false, and the argument is unsound even though nothing is wrong with its logic.[^s1][^s3]

Several consequences follow from the definition.

- **Every invalid argument is unsound**, even if all its premises happen to be true.[^s1]
- **An unsound argument can still have a true conclusion.** Showing that an argument fails does not show that its conclusion is false. It shows only that this argument does not establish it.[^s1]
- **To show an argument is unsound**, either show it is invalid, by describing a case where the premises are true and the conclusion false, or show that at least one premise is false.[^s3]

Soundness can also expire. When a premise describes a changing state of affairs, such as who holds a job or what a current policy says, an argument that was sound when written can become unsound later, while its form stays exactly the same.[^s4]

## How to apply it

1. **Reconstruct the argument.** State the premises and conclusion explicitly. Supply any unstated premise needed for validity, choosing the most plausible version.[^s2]
2. **Test validity first.** If you can describe a scenario where every premise is true and the conclusion false, stop: the argument is unsound, and the facts cannot rescue it.[^s1][^s3]
3. **Audit each premise.** Ask what evidence would confirm or refute it, and who is in a position to know. Some premises are obviously true, some need research, and some are contested enough that suspending judgment is the honest answer.[^s2][^s4]
4. **Date time-sensitive premises.** Note when a premise was true, so a later reader can check whether it still is.[^s4]
5. **Keep the verdicts separate.** Report "valid but one premise is doubtful" rather than "wrong." That tells others exactly where the disagreement lies.[^s1]

## Connections

- **Contrasts with cogency.** Cogency is the counterpart for non-deductive arguments: strong support plus true premises. A cogent argument makes its conclusion likely, while a sound argument makes it certain. A cogent argument can still have a false conclusion; a sound one cannot.[^s4]
- **Often confused with the soundness theorem.** In metalogic, "soundness" means that a proof system derives only valid results. That is a different property from an individual argument being valid with true premises.[^s1][^s5]
- **Part of argument evaluation.** Soundness is the combined verdict of the two checks used to evaluate a deductive argument: form and premise truth.[^s1]
- **Builds on validity.** Every sound argument is valid, but not every valid argument is sound. Soundness adds the factual test that validity leaves out.[^s2][^s3]
- **Related to Aristotle and the principle of charity.** Aristotle's account of demonstration required true premises as well as correct deductive form.[^s6] Reconstructing missing premises charitably comes before judging whether an argument is sound.[^s2]

## Sources

[^s1]: "Validity and Soundness", Internet Encyclopedia of Philosophy. https://iep.utm.edu/page/val-snd/ (accessed 2026-11-03)
[^s2]: Van Cleave, "1.7: Soundness", *Introduction to Logic and Critical Thinking*, 2nd ed., Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Introduction_to_Logic_and_Critical_Thinking_2e_(van_Cleave)/01%3A_Reconstructing_and_Analyzing_Arguments/1.07%3A_Soundness (accessed 2026-11-03)
[^s3]: *Logic Primer*, section 1.1, MIT Press, online edition at Texas A&M University. https://logic.tamu.edu/Primer/1.1.html (accessed 2026-11-03)
[^s4]: "Introduction: soundness and cogency", *How to Think Critically*, CAUL OER Collective. https://oercollective.caul.edu.au/howtothinkcritically/?p=103 (accessed 2026-11-03)
[^s5]: "Soundness", *The Logic Notes*, Australian National University. https://users.cecs.anu.edu.au/~jks/LogicNotes/soundness.html (accessed 2026-11-03)
[^s6]: Aristotle, *Posterior Analytics* I.2, trans. G. R. G. Mure. https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/posterior-analytics.asp?pg=3 (accessed 2026-11-03)
