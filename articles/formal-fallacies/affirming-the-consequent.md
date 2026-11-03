---
id: ct:affirming-the-consequent
type: FormalFallacy
title: Affirming the consequent
aliases: [fallacy of the consequent, converse error, fallacy of the converse]
domain: formal-fallacies
summary: >-
  The deductively invalid inference that takes a conditional "if P then Q"
  together with the truth of Q and concludes P, treating a sufficient
  condition as if it were also a necessary one.
level: introductory
evidenceStatus: normative
broader: [ct:formal-fallacy]
related: [ct:denying-the-antecedent, ct:deductive-reasoning, ct:modus-tollens]
requires: [ct:modus-ponens, ct:validity]
relations:
  - {predicate: invalidFormOf, object: ct:modus-ponens, source: s2, confidence: high}
  - {predicate: confusedWith, object: ct:modus-ponens, source: s3, confidence: high}
  - {predicate: confusedWith, object: ct:modus-tollens, source: s3, confidence: medium}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:conditional-perfection, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:inference-to-the-best-explanation, source: s4, confidence: medium}
criticalQuestions:
  - Besides the stated antecedent, what else could make the consequent true?
  - Does the conditional really run both ways, or has a one-way "if" been heard as "if and only if"?
  - How often does the consequent occur when the antecedent is false, and has that rate been checked?
  - Have rival explanations of the observed consequent been compared before accepting the antecedent?
argumentMap:
  premises:
    - "If the new release has a memory leak, the servers will slow down by the afternoon."
    - "The servers slowed down this afternoon."
  conclusion: "The new release has a memory leak."
  verdict: invalid
  scheme: ct:modus-ponens
  objections:
    - "A traffic spike, a failing disk or a database lock would also slow the servers."
    - "The slowdown matches the leak hypothesis but does not rule out any rival cause."
sources:
  - id: s1
    title: "On Sophistical Refutations (trans. W. A. Pickard-Cambridge)"
    publisher: Aristotle, Organon; Elpenor Greek texts edition
    url: https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/sophistical-refutations.asp?pg=8
    type: primary
    accessed: 2026-11-03
  - id: s2
    title: "3.3: Conditional Arguments"
    publisher: "Critical Reasoning: A User's Manual (Southworth & Swoyer), LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/03%3A_Conditionals_and_Conditional_Arguments/3.03%3A_Conditional_Arguments
    type: textbook
    accessed: 2026-11-03
  - id: s3
    title: "Basic structural fallacies"
    publisher: "How to Think Critically (Gibbons & Kingsbury, 2024), CAUL OER Collective"
    url: https://oercollective.caul.edu.au/howtothinkcritically/?p=63
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "Denying Antecedents and Affirming Consequents: The State of the Art"
    publisher: Informal Logic 35(1), 88-134 (Godden & Zenker, 2015), DOAJ record
    url: https://doaj.org/article/bc10621a4113470790144634f8b69ebc
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "A Meta-Analysis of Conditional Reasoning"
    publisher: International Conference on Cognitive Modeling (Ragni, Dames & Johnson-Laird, 2019), author's copy
    url: https://modeltheory.org/papers/2019meta-conditionals.pdf
    type: primary
    accessed: 2026-11-03
created: 2026-11-03
---

# Affirming the consequent

Affirming the consequent is the invalid argument form "If P then Q; Q; therefore P." The second premise affirms the consequent (Q) of the conditional, and the conclusion asserts its antecedent (P). The form is deductively invalid: both premises can be true while the conclusion is false, because the conditional only says that P is enough for Q, not that P is the only route to Q.[^s2][^s3] Every argument with this shape is invalid, whatever its content, which is what makes it a formal rather than an informal fallacy.[^s2]

## Origin

Aristotle described the error in *On Sophistical Refutations*, part of the *Organon*, as the refutation that depends on the consequent. He diagnosed it as the assumption that a relation of consequence converts, so that if one thing follows from another, the second is taken to follow from the first.[^s1] His examples are still the standard ones: people take yellow bile for honey because honey is yellow, and they infer rain from wet ground even though other causes can wet the ground.[^s1] Modern logic textbooks teach it alongside denying the antecedent as one of the two invalid look-alikes of the valid conditional forms.[^s2][^s3]

## How it works

The fallacy borrows the look of modus ponens. Modus ponens affirms the antecedent ("If P then Q; P; so Q") and is valid; affirming the consequent swaps which part is affirmed and which is concluded.[^s2][^s3] A textbook illustration: if a shape is a square, its sides are equal; this shape's sides are equal; so it is a square. An equilateral triangle shows the premises true and the conclusion false.[^s3]

The argument map above gives a workplace version. An engineer reasons that a memory leak would slow the servers, the servers slowed, so there must be a leak. The observation fits the hypothesis, but a traffic spike, a failing disk or a lock in the database would produce the same symptom, so the premises do not settle the cause.[^s2][^s4]

## How to spot it

Look for a conditional followed by a confirmation of its "then" clause and a conclusion that returns to the "if" clause. Diagnostic and troubleshooting talk is full of it: a symptom that a cause would produce is offered as proof of that cause.[^s4] The standard test is the method of counterexample: assume the premises are true and try to describe a situation in which the conclusion is false. For this form one always exists unless the consequent can only arise from the antecedent.[^s2]

## How to counter it

Ask what else could make the consequent true, and how often that happens.[^s4] If the speaker really means "only if" (a biconditional), make that premise explicit so it can be examined; the argument then becomes valid but rests on a stronger, often doubtful, claim.[^s4] In inquiry, treat a confirmed prediction as one piece of evidence and compare rival hypotheses rather than accepting the first one the evidence fits.[^s4]

## Evidence

People endorse the form often. A 2019 meta-analysis of 39 experiments (2,378 participants) found that the single most common response pattern, shown by about 42 percent of participants, was to accept all four conditional inferences, including affirming the consequent and denying the antecedent, a pattern that is valid only if the conditional is read as a biconditional.[^s5] Godden and Zenker's 2015 review attributes much of this to conditional perfection, the pragmatic tendency to strengthen "if" into "if and only if", which is common in promises and threats.[^s4] They also argue that the form can work as a defeasible shortcut: its strength rises as the cases where Q occurs without P become rare, and falls as alternative causes multiply. Its cogency therefore depends on assumptions the conditional itself does not state.[^s4] It remains deductively invalid in every case.[^s2]

## Connections

- **Invalid form of modus ponens.** It is the invalid counterpart of the valid conditional form that affirms the antecedent.[^s2]
- **Confused with modus ponens and modus tollens.** Textbooks note that it is often mistaken for one of the two valid conditional forms; its sibling fallacy, denying the antecedent, imitates modus tollens.[^s3]
- **Introduced by Aristotle in *Sophistical Refutations*.** Aristotle named the fallacy of the consequent and explained it as a false belief that consequence converts.[^s1]
- **Explained by conditional perfection.** Reading a one-way conditional as a biconditional makes the inference feel valid.[^s4]
- **Contrasts with inference to the best explanation.** Reasoning from an observed prediction back to a hypothesis has the shape of this fallacy in crude form; it becomes reasonable only when rival explanations and their prior plausibility are weighed, as inference to the best explanation requires.[^s4]

## Sources

[^s1]: Aristotle, *On Sophistical Refutations*, trans. W. A. Pickard-Cambridge. https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/sophistical-refutations.asp?pg=8 (accessed 2026-11-03)
[^s2]: Southworth & Swoyer, "Conditional Arguments", *Critical Reasoning: A User's Manual*, LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning%3A_A_User's_Manual_(Southworth_and_Swoyer)/03%3A_Conditionals_and_Conditional_Arguments/3.03%3A_Conditional_Arguments (accessed 2026-11-03)
[^s3]: Gibbons & Kingsbury, "Basic structural fallacies", *How to Think Critically* (2024). https://oercollective.caul.edu.au/howtothinkcritically/?p=63 (accessed 2026-11-03)
[^s4]: Godden & Zenker, "Denying Antecedents and Affirming Consequents: The State of the Art", *Informal Logic* 35(1), 2015. https://doaj.org/article/bc10621a4113470790144634f8b69ebc (accessed 2026-11-03)
[^s5]: Ragni, Dames & Johnson-Laird, "A Meta-Analysis of Conditional Reasoning", ICCM 2019. https://modeltheory.org/papers/2019meta-conditionals.pdf (accessed 2026-11-03)
