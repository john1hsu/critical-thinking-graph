---
id: ct:affirmative-conclusion-from-a-negative-premise
type: FormalFallacy
title: Affirmative conclusion from a negative premise
aliases: [affirmative conclusion from a negative premiss, fallacy of drawing an affirmative conclusion from a negative premise, illicit negative]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy of drawing an affirmative conclusion (an A or I
  statement) from premises at least one of which is negative (E or O). A
  negative premise only separates classes, so it cannot supply the inclusion
  an affirmative conclusion asserts, and every such syllogism is invalid.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:rules-of-the-categorical-syllogism, ct:exclusive-premises, ct:categorical-proposition, ct:venn-diagram-test, ct:method-of-counterexample, ct:syllogism, ct:illicit-major]
requires: [ct:categorical-syllogism, ct:categorical-proposition, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s2, confidence: high}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:exclusive-premises, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:negative-conclusion-from-affirmative-premises, source: s4, confidence: high}
criticalQuestions:
  - Is either premise a negative statement ("No A are B" or "Some A are not B") while the conclusion says that something is included in a class?
  - Which premise is supposed to place the conclusion's subject inside its predicate class, and does any premise actually do that?
  - Can you describe a case where every premise is true and the affirmative conclusion is false?
  - Is the arguer relying on an unstated affirmative premise that should be stated and checked?
argumentMap:
  premises:
    - "Some new hires have not completed security training."
    - "All new hires are on the onboarding list."
  conclusion: "Some people on the onboarding list have completed security training."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "If everyone on the onboarding list is a new hire and none has finished training yet, both premises are true and the conclusion is false."
    - "The premises only report who has not been trained; nothing in them says anyone has been."
sameAs: []
sources:
  - id: s1
    title: "Prior Analytics, Book I (trans. A. J. Jenkinson), web edition page 42"
    publisher: "Aristotle, Elpenor Greek texts"
    url: https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/prior-analytics.asp?pg=42
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Fallacy of Affirmative Conclusion from a Negative Premiss"
    publisher: "Philosophy 103: Introduction to Logic, Lander University (Lee C. Archie)"
    url: https://philosophy.lander.edu/logic/conclusion_fall.html
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Affirmative Conclusion from a Negative Premiss"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/afromneg.html
    type: community
    accessed: 2026-11-14
  - id: s4
    title: "6.5 Rules for Evaluating Categorical Syllogisms (lecture notes)"
    publisher: "PHIL 240 Introduction to Logic, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.5.pdf
    type: academic
    accessed: 2026-11-14
  - id: s5
    title: "Rules for Valid Syllogisms (Logic Primer appendix)"
    publisher: "Logic Primer, Occidental College"
    url: https://sites.oxy.edu/traiger/logic/primer/appendix/rules_for_valid_syllogisms.html
    type: academic
    accessed: 2026-11-14
created: 2026-11-14
---

# Affirmative conclusion from a negative premise

The fallacy of an affirmative conclusion from a negative premise is committed by any categorical syllogism whose conclusion is affirmative (an A statement, "All S are P", or an I statement, "Some S are P") while at least one premise is negative (an E statement, "No A are B", or an O statement, "Some A are not B").[^s2][^s3] The rule it breaks is one of the two rules of quality: if either premise of a valid standard-form syllogism is negative, the conclusion must be negative too.[^s2] Because the fault lies in the form, every syllogism with this pattern is invalid, whatever its subject matter.[^s3]

## Origin

The principle goes back to Aristotle. In the *Prior Analytics* he observes that every syllogism needs at least one affirmative premise and that at least one premise must match the conclusion in being affirmative or negative.[^s1] Later logic textbooks turned these observations into a short checklist of rules for the categorical syllogism. The Fallacy Files traces its own treatment to standard modern texts such as Copi and Cohen's *Introduction to Logic*, and notes that the rule can be confirmed by inspecting all 256 forms of the categorical syllogism.[^s3] Course notes now usually state it as a counting rule: a valid syllogism has a negative premise if and only if it has a negative conclusion.[^s4][^s5]

## How it works

An affirmative conclusion says that the minor term (the conclusion's subject) is wholly or partly included in the major term (its predicate). To establish an inclusion, the premises must chain inclusions through the middle term, and only affirmative statements assert inclusion.[^s2] A negative premise can only say that one class is shut out from another, wholly or in part. Once one link in the chain is a separation, the premises cannot put the subject inside the predicate class.[^s2]

The argument map above shows the pattern in a workplace setting. Its first premise is an O statement (some new hires have not completed training), its second is an A statement (all new hires are on the onboarding list), and its conclusion is an I statement (some people on the list have completed training). Nothing in the premises says that anyone has been trained. If everyone on the list is a new hire and none has finished training, both premises are true and the conclusion false.[^s2] Lander University's course uses the same mood, OAI in the third figure, with a political-affiliation example.[^s2] A textbook counterexample with obvious content makes the point: no tigers are wolves; some felines are tigers; so some felines are wolves.[^s4]

## How to spot it

Classify the conclusion and each premise by quality. If the conclusion is A or I and any premise is E or O, the syllogism commits the fallacy; no distribution check or diagram is needed.[^s2][^s3] In mood notation, any mood whose last letter is A or I and whose first two letters include an E or O is invalid on this ground, as in AEA, IOI or EEA.[^s2] In ordinary talk, watch for a positive claim ("some of them do", "all of them are") supported by evidence that only says what certain things are not.[^s3] A Venn diagram of the premises shows the gap: nothing is placed in the region where the subject and predicate overlap.[^s2][^s3]

## How to counter it

Ask which premise puts the conclusion's subject inside its predicate class. If none does, offer a counterexample in which the premises hold and the conclusion fails, such as an onboarding list made up entirely of untrained new hires.[^s2][^s3] If the arguer has an affirmative claim in mind, such as that some listed people are long-standing staff who have been trained, ask them to state it as a premise so it can be checked. Keep the rule in its scope: it is a rule of categorical syllogistic, not a general test for every argument with a negative premise.[^s3]

## Connections

- **Invalid form of the categorical syllogism.** It breaks the quality rule that a negative premise requires a negative conclusion.[^s2]
- **Introduced in the *Prior Analytics*.** Aristotle stated that at least one premise must share the conclusion's quality.[^s1]
- **Contrasts with exclusive premises.** That fallacy concerns two negative premises regardless of the conclusion; an argument can commit both at once, as when an affirmative conclusion follows two negative premises.[^s3]
- **Contrasts with a negative conclusion from affirmative premises.** The same counting rule, read in the other direction, rules out a negative conclusion drawn from two affirmative premises.[^s4][^s5]
- **Related to the rules of the categorical syllogism and the Venn diagram test.** The rule checklist names this violation directly, and a diagram shows the unmarked overlap.[^s2][^s5]

## Sources

[^s1]: Aristotle, *Prior Analytics*, Book I, trans. A. J. Jenkinson, Elpenor web edition, page 42. https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/prior-analytics.asp?pg=42 (accessed 2026-11-14)
[^s2]: L. C. Archie, "Fallacy of Affirmative Conclusion from a Negative Premiss", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/conclusion_fall.html (accessed 2026-11-14)
[^s3]: G. N. Curtis, "Affirmative Conclusion from a Negative Premiss", The Fallacy Files. https://fallacyfiles.org/afromneg.html (accessed 2026-11-14)
[^s4]: "6.5 Rules for Evaluating Categorical Syllogisms", PHIL 240 lecture notes, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.5.pdf (accessed 2026-11-14)
[^s5]: "Rules for Valid Syllogisms", Logic Primer appendix, Occidental College. https://sites.oxy.edu/traiger/logic/primer/appendix/rules_for_valid_syllogisms.html (accessed 2026-11-14)
