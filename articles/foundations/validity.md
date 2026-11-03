---
id: ct:validity
type: Concept
title: Validity
aliases: [deductive validity, logical validity, valid argument]
domain: foundations
summary: >-
  The property of a deductive argument whose form makes it impossible for all
  the premises to be true and the conclusion false; validity concerns the link
  between premises and conclusion, not whether the premises are actually true.
level: introductory
evidenceStatus: normative
broader: [ct:deductive-reasoning]
related: [ct:soundness, ct:method-of-counterexample, ct:modus-ponens, ct:belief-bias, ct:truth-table]
requires: [ct:argument]
relations:
  - {predicate: contrastsWith, object: ct:soundness, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:logical-consequence, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:inductive-reasoning, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:formal-logic, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Validity and Soundness"
    publisher: Internet Encyclopedia of Philosophy
    url: https://iep.utm.edu/val-snd
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s2
    title: "Logical Consequence (Summer 2006 edition)"
    publisher: Stanford Encyclopedia of Philosophy (JC Beall & Greg Restall)
    url: https://plato.stanford.edu/archives/sum2006/entries/logical-consequence/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
  - id: s3
    title: "forall x: Calgary, solutions to Chapter 2: The scope of logic"
    publisher: Open Logic Project
    url: https://forallx.openlogicproject.org/html/A2a.html
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "On the conflict between logic and belief in syllogistic reasoning"
    publisher: Memory & Cognition 11, 295-306 (Evans, Barston & Pollard, 1983)
    url: https://link.springer.com/article/10.3758/BF03196976
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data"
    publisher: Psychonomic Bulletin & Review 25(6), 2141-2174 (Trippas, Kellen, Singmann, Pennycook, Koehler, Fugelsang & Dubé, 2018)
    url: https://link.springer.com/article/10.3758/s13423-018-1460-7/fulltext.html
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Validity

A deductive argument is valid when its form makes it impossible for the premises to be true while the conclusion is false; any argument that fails this test is invalid.[^s1] Validity is therefore a claim about the connection between premises and conclusion, not about whether the premises are in fact true.[^s1][^s3] It is the first test critical thinkers apply to a deductive argument: if the conclusion does not follow, checking the facts in the premises cannot rescue it.

## Origin

The idea that some conclusions follow of necessity from premises goes back to Aristotle's syllogistic, an early framework in which a conclusion is drawn from a major and a minor premise; later accounts generalized this to any collection of premises.[^s2] Modern logic gives two precise reconstructions. On the model-theoretic account, which follows Alfred Tarski's 1936 definition, an argument is valid when no model makes the premises true and the conclusion false. On the proof-theoretic account, it is valid when the conclusion can be derived from the premises using primitive rules of inference. Soundness and completeness theorems show that the two accounts pick out the same arguments in standard logics, though philosophers still debate which is more basic.[^s2]

## How it works

Two features define validity. The first is necessity: the premises must guarantee the conclusion, which is what separates deductive validity from the merely probable support of inductive arguments.[^s2] The second is formality: on the dominant view among logicians, validity depends on logical form, the skeleton left when content words are replaced with placeholders, while truth depends on content.[^s1][^s2]

A workplace example shows why the distinction matters. "Every contractor must complete security training before getting building access. Dana got building access. So Dana completed security training." This argument is valid: if both premises are true, the conclusion cannot be false. Whether it proves anything depends on whether the policy is really enforced, which is a question about truth, not validity. Now reverse it: "Every contractor must complete training before getting access. Dana completed training. So Dana got access." That version is invalid, because Dana could have finished training and still be waiting for a badge. The second argument has the same shape as the invalid form in which the conclusion and a premise swap roles.[^s1]

Validity allows every combination of truth values except one. A valid argument can have false premises and a false conclusion, as in a textbook example concluding that all toasters are time-travel devices from two false premises about gold.[^s1] It can have false premises and a true conclusion. What it cannot have is true premises and a false conclusion.[^s1][^s3] Conversely, an invalid argument may happen to have a true conclusion; the premises simply fail to establish it.[^s3]

A **sound** argument is a valid one whose premises are all actually true, so a sound argument always has a true conclusion, and every invalid argument is unsound.[^s1] Two further consequences surprise newcomers. Adding a premise can never make a valid argument invalid, and an argument with contradictory premises counts as valid, because there is no case in which all its premises are true.[^s3]

## How to apply it

- **Separate the two questions.** Ask "if the premises were true, would the conclusion have to be true?" before asking "are the premises true?"[^s1][^s3]
- **Find the form.** Replace content words with letters and check whether the pattern is a known valid form or a known invalid one.[^s1]
- **Look for a counterexample.** Describe a situation where every premise holds and the conclusion fails; one such case shows the argument invalid.[^s3]
- **Watch for necessity that is not formal.** Arguments like "Juan is a bachelor, so he is not married" seem necessarily truth-preserving without having a valid form; logicians handle them by adding an implicit premise or by treating the necessity as non-logical.[^s1]

## Why people misjudge validity

Everyday reasoners often judge validity by whether they believe the conclusion. In three experiments, Evans, Barston and Pollard (1983) found a large belief bias in syllogism evaluation alongside a strong effect of actual logical validity, with belief bias larger on invalid syllogisms than on valid ones.[^s4] Later work refined that interpretation. A 2018 hierarchical Bayesian meta-analysis of 22 confidence-rating studies (993 participants) found that, at the group level, believability did not change people's ability to tell valid from invalid arguments; belief mainly shifted their willingness to say "valid." The authors argued the classic interaction is partly an artifact of the analysis, while noting individual differences such as cognitive ability may moderate it.[^s5] The practical lesson holds either way: a believable conclusion makes people more likely to accept an argument whether or not it is valid.[^s4][^s5]

## Connections

- **Contrasts with soundness.** Validity concerns form; soundness adds the requirement that the premises be true.[^s1]
- **Formalized by logical consequence.** Model-theoretic and proof-theoretic accounts of consequence give validity its precise definition.[^s2]
- **Contrasts with inductive reasoning.** Necessity marks deductive validity off from inductive support.[^s2]
- **Studied in formal logic.** The study of valid argument forms is what logicians call formal or symbolic logic.[^s1]
- **Related to belief bias and the method of counterexample.** Belief bias is the tendency to judge validity by the conclusion's believability, and a counterexample is the standard way to show an argument invalid.[^s3][^s4]

## Sources

[^s1]: "Validity and Soundness", Internet Encyclopedia of Philosophy. https://iep.utm.edu/val-snd (accessed 2026-11-03)
[^s2]: Beall & Restall, "Logical Consequence", Stanford Encyclopedia of Philosophy, Summer 2006 edition. https://plato.stanford.edu/archives/sum2006/entries/logical-consequence/ (accessed 2026-11-03)
[^s3]: *forall x: Calgary*, solutions to Chapter 2, "The scope of logic", Open Logic Project. https://forallx.openlogicproject.org/html/A2a.html (accessed 2026-11-03)
[^s4]: Evans, Barston & Pollard, "On the conflict between logic and belief in syllogistic reasoning", *Memory & Cognition* 11, 1983. https://link.springer.com/article/10.3758/BF03196976 (accessed 2026-11-03)
[^s5]: Trippas, Kellen, Singmann, Pennycook, Koehler, Fugelsang & Dubé, "Characterizing belief bias in syllogistic reasoning: A hierarchical Bayesian meta-analysis of ROC data", *Psychonomic Bulletin & Review* 25(6), 2018. https://link.springer.com/article/10.3758/s13423-018-1460-7/fulltext.html (accessed 2026-11-03)
