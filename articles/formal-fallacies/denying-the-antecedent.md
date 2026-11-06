---
id: ct:denying-the-antecedent
type: FormalFallacy
title: Denying the antecedent
aliases: [inverse error, fallacy of the inverse, denial of the antecedent]
domain: formal-fallacies
summary: >-
  The deductively invalid inference that takes a conditional "if P then Q"
  together with the falsity of P and concludes that Q is false, overlooking
  every other way Q could come about.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:affirming-the-consequent, ct:method-of-counterexample, ct:suppression-effect]
requires: [ct:modus-tollens, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:modus-tollens, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:modus-tollens, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:affirming-the-consequent, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:conditional-perfection, source: s4, confidence: medium}
criticalQuestions:
  - Apart from the stated antecedent, what else could bring about the consequent?
  - Does the speaker actually mean "only if", and if so, has that stronger claim been stated and defended?
  - How likely is the consequent when the antecedent is absent, and has anyone checked?
  - Could the antecedent be false while the consequent still turns out true in a realistic case?
argumentMap:
  premises:
    - "If the big client renews by Friday, the team will hit its quarterly target."
    - "The big client did not renew by Friday."
  conclusion: "The team will not hit its quarterly target."
  verdict: invalid
  scheme: ct:modus-tollens
  objections:
    - "Several smaller deals closing this month could make up the target without the renewal."
    - "The conditional names one sufficient route to the target, not the only one."
sources:
  - id: s1
    title: "On Sophistical Refutations (trans. W. A. Pickard-Cambridge)"
    publisher: Aristotle, Organon; Elpenor Greek texts edition
    url: https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/sophistical-refutations.asp?pg=8
    type: primary
    accessed: 2026-11-06
  - id: s2
    title: "Denial of the antecedent"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/denial-of-the-antecedent
    type: encyclopedia
    accessed: 2026-11-06
  - id: s3
    title: "Common Deductive Argument Forms"
    publisher: "PHIL 213 course materials, Southern Illinois University Edwardsville (W. Larkin)"
    url: https://www.siue.edu/~wlarkin/teaching/PHIL213/forms.html
    type: academic
    accessed: 2026-11-06
  - id: s4
    title: "Denying Antecedents and Affirming Consequents: The State of the Art"
    publisher: "Informal Logic 35(1), 88-134 (Godden & Zenker, 2015), ODU Digital Commons record, doi:10.22329/il.v35i1.4173"
    url: https://digitalcommons.odu.edu/philosophy_fac_pubs/46
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s5
    title: "Causal conditional reasoning and semantic memory retrieval: A test of the semantic memory framework"
    publisher: "Memory & Cognition 30(6), 908-920 (De Neys, Schaeken & d'Ydewalle, 2002)"
    url: https://link.springer.com/content/pdf/10.3758%2FBF03195776.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s6
    title: "A Meta-Analysis of Conditional Reasoning"
    publisher: International Conference on Cognitive Modeling (Ragni, Dames & Johnson-Laird, 2019), author's copy
    url: https://modeltheory.org/papers/2019meta-conditionals.pdf
    type: primary
    accessed: 2026-11-06
created: 2026-11-06
---

# Denying the antecedent

Denying the antecedent is the invalid argument form "If P then Q; not P; therefore not Q." The second premise rejects the if-clause of a conditional, and the conclusion rejects its then-clause.[^s2][^s3] The error is that a conditional only says P is one way of getting Q. Showing that P failed leaves open every other way Q might still happen. Britannica's example: if it rains the game is cancelled; it did not rain; so the game goes ahead. The game could still be cancelled for some other reason.[^s2] Because any argument of this shape can have true premises and a false conclusion, the mistake lies in the form itself, which makes it a formal fallacy.[^s2][^s3]

## Origin

Aristotle discussed the pattern in *On Sophistical Refutations* under the refutations that depend on the consequent. His case is Melissus, who held that whatever comes to be has a first beginning, that the universe never came to be, and so that the universe has no beginning and is eternal.[^s1] Aristotle replied that the conclusion does not follow. Granting that what comes to be always has a beginning does not make everything with a beginning something that came to be. Melissus had quietly run the conditional backwards.[^s1] Aristotle treated this as the same root error as inferring a cause from its sign, which is the sibling fallacy of affirming the consequent.[^s1] Modern logic courses pair the two invalid forms with the two valid conditional forms.[^s3]

## How it works

Denying the antecedent imitates modus tollens. Modus tollens denies the consequent and concludes against the antecedent ("If P then Q; not Q; so not P"), and it is valid. The fallacy keeps the conditional and the negation but moves the denial to the wrong clause.[^s3]

The argument map above gives a sales-meeting version. A manager says a renewal from the biggest client by Friday would put the team over its quarterly target. The renewal slipped, so the manager announces that the target is lost. The premise only named one sufficient route to the target. A run of smaller deals could still close the gap, so the premises can be true while the conclusion is false.[^s2][^s3]

## How to spot it

Look for a conditional, followed by a statement that its if-clause is false, and a conclusion that its then-clause is false too. Typical wording runs "since X did not happen, Y will not happen either."[^s2][^s3] To test the form, keep its shape, assume both premises are true, and look for a situation where the conclusion still fails. A second cause of the consequent, like a cancellation for some reason other than rain, is almost always available.[^s2] Then ask whether the speaker actually meant "only if". In ordinary talk, an offer such as "if you mow the lawn, I'll pay you" is often heard as promising that no mowing means no pay. Godden and Zenker discuss this reading, which linguists call conditional perfection.[^s4]

## How to counter it

Name the other routes to the consequent and ask how likely each one is.[^s4] If the speaker means the stronger claim that P is necessary for Q, rewrite the premise as "only if P, then Q" or "if not P, then not Q." The argument then becomes valid, but now it stands or falls on that stronger premise, which needs its own support.[^s4] In planning and forecasting, losing one sufficient condition is a reason to reassess the odds of the outcome, not to treat it as settled.[^s4]

## Evidence

The form is endorsed often in laboratory tasks. A 2019 meta-analysis of 39 experiments with 2,378 participants found that 42 percent showed the most common response pattern: accepting all four conditional inferences, including this one. That pattern is valid only if the conditional is read as a biconditional.[^s6] Content matters too. In a 2002 study, De Neys, Schaeken and d'Ydewalle found that people accepted the inference much less often for causal conditionals that have many alternative causes. This fits earlier findings that thinking of alternative antecedents suppresses it.[^s5]

Philosophers disagree about whether the form can serve as a reasonable shortcut. Some have argued it is a defeasible but cogent probabilistic inference. Godden and Zenker's 2015 review argues that its strength always depends on unstated assumptions, such as how often the consequent occurs without the antecedent or whether conditional perfection applies, and that arguers should state those assumptions.[^s4] On every account, the form remains deductively invalid.[^s3][^s4]

## Connections

- **Invalid form of modus tollens.** Course materials pair it with modus tollens as that valid form's invalid counterpart, differing only in which clause is denied.[^s3]
- **Confused with modus tollens.** Godden and Zenker show how an argument that looks like denying the antecedent becomes a valid modus tollens if the speaker is read as asserting the converse conditional.[^s4]
- **Contrasts with affirming the consequent.** The two are the standard pair of invalid conditional forms and are usually taught together.[^s2]
- **Introduced by Aristotle in *Sophistical Refutations*.** Aristotle's analysis of Melissus diagnoses this pattern as an illegitimate conversion of a consequence.[^s1]
- **Explained by conditional perfection.** Hearing "if" as "if and only if" makes the inference seem valid.[^s4]
- **Detected by the method of counterexample and weakened by retrieving alternatives.** Supplying another cause of the consequent both refutes the form and lowers people's willingness to accept it.[^s2][^s5]

## Sources

[^s1]: Aristotle, *On Sophistical Refutations*, ch. 5, trans. W. A. Pickard-Cambridge. https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/sophistical-refutations.asp?pg=8 (accessed 2026-11-06)
[^s2]: "Denial of the antecedent", *Encyclopaedia Britannica*. https://www.britannica.com/topic/denial-of-the-antecedent (accessed 2026-11-06)
[^s3]: Larkin, "Common Deductive Argument Forms", PHIL 213, Southern Illinois University Edwardsville. https://www.siue.edu/~wlarkin/teaching/PHIL213/forms.html (accessed 2026-11-06)
[^s4]: Godden & Zenker, "Denying Antecedents and Affirming Consequents: The State of the Art", *Informal Logic* 35(1), 2015. https://digitalcommons.odu.edu/philosophy_fac_pubs/46 (accessed 2026-11-06)
[^s5]: De Neys, Schaeken & d'Ydewalle, "Causal conditional reasoning and semantic memory retrieval", *Memory & Cognition* 30(6), 2002. https://link.springer.com/content/pdf/10.3758%2FBF03195776.pdf (accessed 2026-11-06)
[^s6]: Ragni, Dames & Johnson-Laird, "A Meta-Analysis of Conditional Reasoning", ICCM 2019. https://modeltheory.org/papers/2019meta-conditionals.pdf (accessed 2026-11-06)
