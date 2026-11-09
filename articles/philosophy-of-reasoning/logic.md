---
id: ct:logic
type: Field
title: Logic
aliases: [study of inference, science of consequence]
domain: philosophy-of-reasoning
summary: >-
  The discipline that studies correct inference: which conclusions follow from
  which premises, why they follow, and how strongly; it includes formal
  (deductive) logic, inductive logic and informal logic as branches.
level: introductory
evidenceStatus: normative
broader: [ct:philosophy]
related: [ct:formal-logic, ct:informal-logic, ct:argumentation-theory, ct:argument, ct:validity, ct:soundness, ct:deductive-reasoning, ct:inductive-reasoning, ct:logical-consequence, ct:organon, ct:chrysippus, ct:epistemology]
requires: [ct:argument]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:stoic-logic, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:gottlob-frege, source: s4, confidence: high}
sources:
  - id: s1
    title: "Logical Consequence"
    publisher: Internet Encyclopedia of Philosophy (Matthew McKeon, Michigan State University)
    url: https://iep.utm.edu/logcon/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s2
    title: "forall x: Calgary, Chapter 2: The scope of logic"
    publisher: Open Logic Project, University of Calgary (Magnus, Button, Trueman & Zach)
    url: https://forallx.openlogicproject.org/html/Ch2.html
    type: textbook
    accessed: 2026-11-09
  - id: s3
    title: "Ancient Logic"
    publisher: Stanford Encyclopedia of Philosophy (Bobzien, Summer 2020 archive edition)
    url: https://plato.stanford.edu/archives/sum2020/entries/logic-ancient/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s4
    title: "Frege's Logic"
    publisher: Stanford Encyclopedia of Philosophy (Roy T. Cook, 2023)
    url: https://plato.stanford.edu/entries/frege-logic/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s5
    title: "Inductive Logic"
    publisher: Stanford Encyclopedia of Philosophy (James Hawthorne, Spring 2018 archive edition)
    url: https://plato.stanford.edu/archives/spr2018/entries/logic-inductive/
    type: scholarly-encyclopedia
    accessed: 2026-11-09
  - id: s6
    title: "Logic"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/topic/logic/Introduction
    type: encyclopedia
    accessed: 2026-11-09
created: 2026-11-09
---

# Logic

Logic is the study of correct reasoning, and above all of inference: the rule-governed step from one or more premises to a conclusion.[^s6] Its core question is what follows from what. Open textbooks put it in exactly those terms, and philosophers of logic call logical consequence, the relation between premises and what follows from them, arguably the discipline's central concept.[^s2][^s1] For critical thinking, logic supplies the standards against which an argument's structure is judged, separately from whether its claims happen to be true.[^s2]

## Origin

People argued well and badly long before anyone theorized about it. Aristotle in the fourth century BCE was the first to turn scattered observations about argument into a systematic discipline, with his syllogistic: a theory of deductive inference built on relations between terms. It dominated Western logic for roughly two thousand years.[^s3] A rival ancient tradition took propositions rather than terms as its building blocks. The Megarian Philo defined the conditional by the truth values of its parts, and the Stoic Chrysippus built a propositional logic around five basic valid argument forms.[^s3] Aristotle's followers collected his logical works as the *Organon*, the "tool", which reflects a long-running view that logic is an instrument for all inquiry rather than one subject among others.[^s3]

The modern discipline began in the nineteenth century, when logic was given algebraic and then fully symbolic treatment. Gottlob Frege's *Begriffsschrift* of 1879 is often credited with inventing modern quantificational logic. It replaced the old subject-predicate analysis of sentences with a function-argument analysis and set out an axiomatic proof system, so that it reached general claims that syllogistic and Boolean methods could not handle.[^s4]

## How it works

Logic studies the form of an inference, not its subject matter. An argument is valid when no possible case makes all its premises true and its conclusion false; it is formally valid when that holds because of its logical form alone, whatever the argument is about.[^s2] Whether the premises are actually true is not a question logic can settle. It can tell you that a conclusion would follow, and it can expose an inference that does not follow by finding a counterexample.[^s2]

A workplace example shows the division of labour. In a release review, someone argues: "Every release that skipped QA shipped with a bug. This release shipped with a bug. So it skipped QA." Logic does not need to know anything about this company to judge the argument. A case where some release went through QA and still had a bug makes both premises true and the conclusion false, so the inference is invalid.[^s2] Checking whether the first premise is true is a separate, empirical job for the team's records.[^s2]

Two ways of making "follows from" precise run through modern logic. A model-theoretic account says a conclusion follows when no interpretation of the non-logical vocabulary makes the premises true and the conclusion false. A deductive (proof-theoretic) account says it follows when it can be derived from the premises in a correct deductive system.[^s1] Which words count as logical vocabulary (and, not, or, if-then, the quantifiers, identity) is still debated.[^s1]

## Branches

- **Formal (deductive) logic** studies inferences whose premises would guarantee their conclusions, using precise artificial languages; it includes propositional, predicate and modal logic.[^s2][^s6]
- **Inductive logic** studies arguments whose premises give only partial support. Deductive entailment is all-or-nothing and truth-preserving, while inductive support comes in degrees, is often measured with probabilities, and can be overturned by new evidence.[^s5]
- **Informal logic** and argumentation theory analyse and evaluate everyday arguments in natural language, including the informal fallacies.[^s2][^s6]
- **Philosophy of logic** asks what consequence is and which expressions count as logical, while **applied logic** carries the tools into other fields.[^s6][^s1]

## Limitations

Logic is necessary but not sufficient for good reasoning. A valid argument can still have a false conclusion if a premise is false, and soundness needs both validity and true premises.[^s2] Deductive standards also do not tell you how strongly evidence supports a hypothesis, which is why inductive and probabilistic logic exist as separate projects.[^s5] Treating the gaps as failures of logic, rather than as questions for evidence, is a common category error.[^s2]

## Connections

- **Broader: philosophy.** Logic began as a philosophical discipline, and the nature of consequence remains a philosophical question.[^s1][^s3]
- **Introduced by Aristotle.** He made logic a systematic discipline with the syllogistic.[^s3]
- **Influenced by Stoic logic.** Chrysippus' propositional logic of indemonstrable forms was the main ancient alternative to term logic.[^s3]
- **Influenced by Gottlob Frege.** His *Begriffsschrift* is often treated as the start of modern quantificational logic.[^s4]
- **Related to epistemology.** Logic asks whether a conclusion would follow; whether the premises are true is a matter for evidence and inquiry.[^s2]
- **Requires argument; related to formal logic, informal logic, argumentation theory, validity, soundness, deductive and inductive reasoning, logical consequence and the *Organon*.** These are its subject matter, its branches and its founding texts.[^s1][^s2][^s3][^s5]

## Sources

[^s1]: M. McKeon, "Logical Consequence", Internet Encyclopedia of Philosophy. https://iep.utm.edu/logcon/ (accessed 2026-11-09)
[^s2]: P. D. Magnus, T. Button, R. Trueman & R. Zach, *forall x: Calgary*, ch. 2 "The scope of logic", Open Logic Project. https://forallx.openlogicproject.org/html/Ch2.html (accessed 2026-11-09)
[^s3]: S. Bobzien, "Ancient Logic", Stanford Encyclopedia of Philosophy (Summer 2020 archive). https://plato.stanford.edu/archives/sum2020/entries/logic-ancient/ (accessed 2026-11-09)
[^s4]: R. T. Cook, "Frege's Logic", Stanford Encyclopedia of Philosophy (2023). https://plato.stanford.edu/entries/frege-logic/ (accessed 2026-11-09)
[^s5]: J. Hawthorne, "Inductive Logic", Stanford Encyclopedia of Philosophy (Spring 2018 archive). https://plato.stanford.edu/archives/spr2018/entries/logic-inductive/ (accessed 2026-11-09)
[^s6]: "Logic", Encyclopaedia Britannica. https://britannica.com/topic/logic/Introduction (accessed 2026-11-09)
