---
id: ct:deductive-reasoning
type: ReasoningMode
title: Deductive reasoning
aliases: [deduction, deductive inference, deductive argument]
domain: formal-logic
summary: >-
  Reasoning in which the premises are meant to guarantee the conclusion, so
  that if the argument is valid it is impossible for the premises to be true
  and the conclusion false.
level: introductory
evidenceStatus: normative
broader: [ct:reasoning]
related: [ct:validity, ct:soundness, ct:modus-ponens, ct:belief-bias, ct:affirming-the-consequent]
requires: [ct:argument]
relations:
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: medium}
  - {predicate: formalizedBy, object: ct:logical-consequence, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s4, confidence: high}
  - {predicate: explainedBy, object: ct:mental-model-theory, source: s4, confidence: medium}
argumentMap:
  premises:
    - "Every purchase over the department's approval limit needs sign-off from finance."
    - "This laptop order is over the department's approval limit."
  conclusion: "This laptop order needs sign-off from finance."
  verdict: valid
  scheme: ct:modus-ponens
  objections:
    - "The conclusion is only as reliable as the premises: if the limit was raised last quarter, the argument stays valid but becomes unsound."
sources:
  - id: s1
    title: "Deductive and Inductive Arguments"
    publisher: Internet Encyclopedia of Philosophy (Shanahan)
    url: https://iep.utm.edu/deductive-inductive-arguments/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "Logical Consequence"
    publisher: Stanford Encyclopedia of Philosophy (Sagi; Beall, Restall & Sagi; rev. 2024)
    url: https://plato.stanford.edu/ENTRiES/logical-consequence/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s3
    title: "2.4: Deductive Validity"
    publisher: "An Introduction to Philosophy (W. Russ Payne), Humanities LibreTexts"
    url: https://human.libretexts.org/Bookshelves/Philosophy/Introduction_to_Philosophy/An_Introduction_to_Philosophy_(Payne)/02%3A_How_Philosophy_is_Done/2.04%3A_Deductive_Validity
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "Deductive Reasoning"
    publisher: Annual Review of Psychology 50, 109-135 (Johnson-Laird, 1999), course copy
    url: https://pages.ucsd.edu/~scoulson/203/johnson-laird.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "On the conflict between logic and belief in syllogistic reasoning"
    publisher: Memory & Cognition 11, 295-306 (Evans, Barston & Pollard, 1983)
    url: https://link.springer.com/article/10.3758/BF03196976
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Deductive reasoning

Deductive reasoning is reasoning in which the premises are intended to guarantee the conclusion rather than merely make it probable.[^s1] A deductive argument is valid when it is impossible for all its premises to be true while its conclusion is false, and sound when it is valid and its premises are in fact true.[^s1][^s3] Validity is the strictest standard of support an argument can meet, but it says nothing on its own about whether the premises are true: a valid argument can start from false premises and reach a false conclusion.[^s3]

## Origin

Aristotle drew the first systematic line between two kinds of reasoning in the logical works later collected as the *Organon*: the syllogism (*sullogismos*), in which a conclusion follows of necessity from what is laid down, and *epagôgê*, reasoning from particular cases to universals, the ancestor of induction.[^s1] The contrast was argued over again in the early modern period, when Francis Bacon championed induction in the *New Organon* (1620) and René Descartes favoured deduction in the *Discourse on the Method* (1637).[^s1] In the twentieth century Alfred Tarski's 1936 work gave the model-theoretic definition of logical consequence that logicians still use: a conclusion follows when every model that makes the premises true also makes the conclusion true.[^s2]

## How it works

Philosophers describe valid deduction as necessary truth preservation in virtue of form, knowable without empirical investigation.[^s2] Form matters because the same pattern guarantees its conclusion whatever the content: any argument of the shape "every A is B; this is an A; so this is B" is valid.[^s2][^s3] Logicians capture this in two ways. The model-theoretic account treats validity as the absence of a counterexample, and the proof-theoretic account treats it as the existence of a step-by-step proof from premises to conclusion.[^s2]

The argument map above gives a workplace case. If every purchase over the approval limit needs finance sign-off, and this order is over the limit, then it needs sign-off; there is no way for both premises to hold and the conclusion to fail.[^s3] Whether the conclusion is actually true depends on whether the premises are, so a stale policy figure would leave the argument valid but unsound.[^s3] Deduction is often called explicative rather than ampliative: the conclusion makes explicit what the premises already contain, whereas inductive conclusions go beyond their evidence.[^s1] A related mark is that adding premises cannot weaken a valid deduction, while new evidence can strengthen or undermine an inductive argument.[^s1]

## How to apply it

1. Reconstruct the argument: state each premise and the conclusion explicitly, including any unstated premise the reasoning depends on.[^s3]
2. Test validity with the counterexample method: imagine the premises true and try to describe a situation in which the conclusion is false. If you can, the argument is invalid.[^s3]
3. Test soundness separately by checking each premise against the evidence; only a sound argument gives a good reason to accept its conclusion.[^s3]
4. Do not let the label do the work. Because there is no settled way to classify arguments as deductive or inductive, one practical approach is to ask first whether an argument is valid and sound, and only then whether it is inductively strong and cogent.[^s1]

## Evidence

How well people actually deduce is an empirical question. Johnson-Laird's 1999 review in the *Annual Review of Psychology* concluded that untrained reasoners have a modest deductive competence that serves them in daily life but fails in predictable ways in the laboratory.[^s4] On his mental model theory, people reason by imagining the possibilities the premises allow; problems that need several models are harder than those that need one, and reasoners tend to represent only what is true in each possibility, which produces systematic "illusory" inferences.[^s4] Prompting people to look for counterexamples improves performance on some tasks.[^s4]

Prior beliefs also intrude. In three experiments Evans, Barston and Pollard (1983) found that people judged syllogisms partly on logic and partly on whether the conclusion was believable, and that this belief bias was stronger for invalid arguments than for valid ones.[^s5] Mental logic (formal rule) theories and knowledge-based accounts compete with mental models as explanations of these patterns, and Johnson-Laird allowed that reasoning may draw on a mixture of mechanisms.[^s4]

## Connections

- **Contrasts with inductive reasoning.** Deduction aims at conclusions guaranteed by the premises; induction aims at conclusions made probable by them, though the IEP stresses that how to draw this line is disputed.[^s1]
- **Introduced by Aristotle.** His separation of the syllogism from reasoning from particulars is the earliest systematic version of the distinction.[^s1]
- **Formalized by logical consequence.** Modern logic defines valid deduction through model-theoretic or proof-theoretic accounts of logical consequence.[^s2]
- **Studied in cognitive psychology.** Experimental work on syllogisms, conditionals and the selection task measures how ordinary reasoners deduce and where they go wrong.[^s4]
- **Explained by mental model theory.** Johnson-Laird's theory accounts for which deductions people find easy or hard and for characteristic errors.[^s4]
- **Related to belief bias and affirming the consequent.** Believable conclusions are accepted from invalid arguments, and formal fallacies such as affirming the consequent are the invalid look-alikes of valid deductive forms like modus ponens.[^s3][^s5]

## Sources

[^s1]: Shanahan, "Deductive and Inductive Arguments", Internet Encyclopedia of Philosophy. https://iep.utm.edu/deductive-inductive-arguments/ (accessed 2026-11-03)
[^s2]: Sagi (Beall, Restall & Sagi), "Logical Consequence", Stanford Encyclopedia of Philosophy, rev. 2024. https://plato.stanford.edu/ENTRiES/logical-consequence/ (accessed 2026-11-03)
[^s3]: Payne, "Deductive Validity", *An Introduction to Philosophy*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Introduction_to_Philosophy/An_Introduction_to_Philosophy_(Payne)/02%3A_How_Philosophy_is_Done/2.04%3A_Deductive_Validity (accessed 2026-11-03)
[^s4]: Johnson-Laird, "Deductive Reasoning", *Annual Review of Psychology* 50 (1999), 109-135. https://pages.ucsd.edu/~scoulson/203/johnson-laird.pdf (accessed 2026-11-03)
[^s5]: Evans, Barston & Pollard, "On the conflict between logic and belief in syllogistic reasoning", *Memory & Cognition* 11 (1983), 295-306. https://link.springer.com/article/10.3758/BF03196976 (accessed 2026-11-03)
