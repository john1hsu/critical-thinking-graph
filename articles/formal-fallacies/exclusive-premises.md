---
id: ct:exclusive-premises
type: FormalFallacy
title: Exclusive premises
aliases: [fallacy of exclusive premises, two negative premises, fallacy of two negative premises, exclusive premisses]
domain: formal-fallacies
summary: >-
  The syllogistic fallacy of drawing a conclusion from two negative premises.
  Because each premise only excludes one class from the middle term, the
  premises fix no relation between the conclusion's two terms, so every
  categorical syllogism with two negative premises is invalid.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:rules-of-the-categorical-syllogism, ct:antilogism, ct:syllogism, ct:venn-diagram-test, ct:illicit-major, ct:undistributed-middle, ct:existential-fallacy, ct:method-of-counterexample, ct:john-buridan, ct:mental-model-theory]
requires: [ct:categorical-syllogism, ct:categorical-proposition, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:categorical-syllogism, source: s3, confidence: high}
  - {predicate: introducedIn, object: ct:prior-analytics, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s4, confidence: medium}
criticalQuestions:
  - Are both premises negative, so that each one only says which things are excluded from the middle class?
  - Does anything in the premises say how the conclusion's subject and predicate relate to each other directly?
  - Can you describe a case where both premises are true and the conclusion is false?
  - Did the arguer mean a stronger affirmative claim, such as "only X can do this", that should be stated and defended?
argumentMap:
  premises:
    - "No members of the security team can approve expenses."
    - "No interns are members of the security team."
  conclusion: "No interns can approve expenses."
  verdict: invalid
  scheme: ct:categorical-syllogism
  objections:
    - "The premises only say who is outside the security team; an intern could still approve expenses through a project budget role."
    - "Both premises would stay true even if every intern could approve expenses, so they cannot rule it out."
sameAs: []
sources:
  - id: s1
    title: "Prior Analytics, Book I (trans. A. J. Jenkinson)"
    publisher: "Aristotle, The Internet Classics Archive, MIT"
    url: https://classics.mit.edu/Aristotle/prior.1.i.html
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Medieval Theories of the Syllogism"
    publisher: "Stanford Encyclopedia of Philosophy (Lagerlund, rev. 2026)"
    url: https://plato.stanford.edu/entries/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s3
    title: "Syllogistic Fallacies: Exclusive Premisses"
    publisher: "Philosophy 103: Introduction to Logic, Lander University (Lee C. Archie)"
    url: https://philosophy.lander.edu/logic/exclusive_fall.html
    type: academic
    accessed: 2026-11-09
  - id: s4
    title: "Theories of the Syllogism: A Meta-Analysis"
    publisher: "Psychological Bulletin 138(3), 427-457 (Khemlani & Johnson-Laird, 2012), authors' copy"
    url: https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Exclusive Premisses"
    publisher: The Fallacy Files (Gary N. Curtis)
    url: https://fallacyfiles.org/exclprem.html
    type: community
    accessed: 2026-11-09
created: 2026-11-09
---

# Exclusive premises

The fallacy of exclusive premises, also called the fallacy of two negative premises, is committed by any categorical syllogism whose premises are both negative, that is, both E ("No A are B") or O ("Some A are not B") statements.[^s3][^s5] The rule it breaks is that at least one premise of a valid categorical syllogism must be affirmative. Because the fault lies in the form, every syllogism with two negative premises is invalid, whatever its subject matter and even when its conclusion happens to be true.[^s3][^s5]

## Origin

The pattern was first mapped by Aristotle. Working through the three figures of the syllogism in the *Prior Analytics*, he showed figure by figure that no syllogism results when both premises are privative, that is, when both deny a predicate of a subject.[^s1] Medieval logicians turned his case-by-case results into general rules. In the fourteenth century John Buridan derived the valid moods from rules of distribution and rejected every combination of two negative premises (EE, EO, OE and OO) outright.[^s2] Modern textbooks list the requirement as one of a handful of syllogistic rules and name the violation the fallacy of exclusive premises.[^s3][^s5]

## How it works

A syllogism needs its middle term to link the minor term (the conclusion's subject) to the major term (its predicate). A negative premise can only say that one class is shut out from another, in whole or in part. With two negative premises, the middle term is shut away from both end terms, and nothing says how those two classes stand to each other.[^s3] A Venn diagram makes the gap visible: after both premises are drawn, the region where the subject and predicate overlap is left unmarked, so the premises allow it to be empty or occupied.[^s3][^s5]

The argument map above has this shape. It says security team members cannot approve expenses and interns are not on the security team. Both statements describe exclusions from the security team, and neither speaks about interns and expense approval directly. An intern who approves expenses through a project budget role makes both premises true and the conclusion false, so the form is invalid.[^s3][^s5] A textbook counterexample makes the same point with obvious content: no reptiles are mammals; no dogs are reptiles; so no dogs are mammals. True premises, false conclusion.[^s5]

## How to spot it

Classify each premise. If both are E or O statements, the syllogism commits the fallacy, and you do not need to check distribution or draw a diagram.[^s3] In the mood notation, look at the first two letters: any mood beginning EE, EO, OE or OO is invalid.[^s2][^s3] In everyday talk, the warning sign is a conclusion drawn from two statements that each say only what something is not, since negative premises tell you little about what a thing is.[^s3]

The error is easy to miss in practice. A 2012 meta-analysis by Khemlani and Johnson-Laird pooled six experiments in which participants drew conclusions from all 64 pairs of syllogistic premises. For the double-negative pairs, which support no valid conclusion, the correct answer that nothing follows was given about half the time overall. The rate varied widely with the arrangement of terms, and for some pairs an invalid negative conclusion was chosen about as often as the correct response.[^s4] The authors note that only some reasoners come to grasp the general principle that two negative premises yield nothing.[^s4]

## How to counter it

Ask what the premises say about the two end terms directly. If the answer is nothing, offer a counterexample in which both exclusions hold and the conclusion fails, such as an intern with a separate approval route.[^s3][^s5] If the arguer meant a stronger claim, for example that only security team members can approve expenses, have them state it. "Only security team members can approve expenses" amounts to the affirmative claim that all who can approve are security team members. With one affirmative premise the rule is no longer broken, and in this case the argument becomes valid, but it now rests on a stronger premise that has to be defended.[^s3]

Keep the rule in its scope. It is a rule of categorical logic. In other systems an argument with two negative premises can be valid, so a negative premise pair outside a categorical syllogism is not automatically fallacious.[^s5]

## Connections

- **Invalid form of the categorical syllogism.** It breaks the rule that at least one premise of a valid standard-form syllogism be affirmative.[^s3]
- **Introduced in the *Prior Analytics*.** Aristotle's treatment of the three figures first established that two privative premises yield no syllogism.[^s1]
- **Explained by the distribution of terms.** Buridan's distribution rules, under which negatives distribute their predicates, led him to reject every combination of only negative premises.[^s2]
- **Studied in the psychology of reasoning.** Experiments on syllogistic inference show how often people draw conclusions from double-negative premises that support none.[^s4]
- **Related to the rules of the categorical syllogism and the Venn diagram test.** The rule checklist names this fallacy directly, and a diagram shows the unmarked overlap that makes the form invalid.[^s3][^s5]

## Sources

[^s1]: Aristotle, *Prior Analytics*, Book I, trans. A. J. Jenkinson, The Internet Classics Archive, MIT. https://classics.mit.edu/Aristotle/prior.1.i.html (accessed 2026-11-09)
[^s2]: H. Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/entries/medieval-syllogism/ (accessed 2026-11-09)
[^s3]: L. C. Archie, "Syllogistic Fallacies: Exclusive Premisses", Philosophy 103: Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/exclusive_fall.html (accessed 2026-11-09)
[^s4]: S. Khemlani and P. N. Johnson-Laird, "Theories of the Syllogism: A Meta-Analysis", *Psychological Bulletin* 138(3), 427-457 (2012). https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf (accessed 2026-11-09)
[^s5]: G. N. Curtis, "Exclusive Premisses", The Fallacy Files. https://fallacyfiles.org/exclprem.html (accessed 2026-11-09)
