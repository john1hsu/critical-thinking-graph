---
id: ct:begging-the-question
type: InformalFallacy
title: Begging the question
aliases: [petitio principii, circular argument, circular reasoning, circulus in probando, assuming the conclusion]
domain: informal-fallacies
summary: >-
  The fallacy of offering, as support for a conclusion, premises that already
  assume that conclusion, so the argument may be valid yet gives a doubter no
  independent reason to accept it.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:argument, ct:validity, ct:burden-of-proof, ct:sophistical-refutations, ct:prior-analytics, ct:charles-hamblin, ct:douglas-walton, ct:falsifiability, ct:bayesian-reasoning]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s1, confidence: high}
  - {predicate: confusedWith, object: ct:ignoratio-elenchi, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:inference-to-the-best-explanation, source: s3, confidence: medium}
  - {predicate: formalizedBy, object: ct:bayesian-reasoning, source: s3, confidence: medium}
criticalQuestions:
  - If I set the conclusion aside, is there any reason left for believing the premises?
  - Would someone who doubts the conclusion already accept each premise, or only someone who agrees?
  - Does a key term or label in the premises quietly carry the conclusion inside it?
  - Traced step by step, does the chain of support loop back to the claim it is meant to prove?
  - Is this really an argument meant to persuade, or an explanation or definition where a loop is harmless?
argumentMap:
  premises:
    - "Our vendor's uptime reports are accurate."
    - "We know the reports are accurate because the vendor's own audit, which relies on those same uptime logs, says so."
  conclusion: "So the vendor met its 99.9% uptime commitment and the service credit claim should be rejected."
  verdict: fallacious
  objections:
    - "The audit draws on the very logs whose accuracy is in dispute, so it cannot independently confirm them."
    - "Independent monitoring data or customer incident tickets would supply a reason the doubting party could accept."
sources:
  - id: s1
    title: "A Question of Begging"
    publisher: Informal Logic 8(1) (Basu, 1986)
    url: https://distantreader.org/stacks/journals/il/il-2677.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "Epistemic and Dialectical Models of Begging the Question"
    publisher: Synthese 152(2), 237-284 (Walton, 2006)
    url: https://dc2.philarchive.org/rec/WALEAD-5
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "A Normative Theory of Argument Strength"
    publisher: Informal Logic 26(1), 1-24 (Hahn & Oaksford, 2006)
    url: https://distantreader.org/stacks/journals/il/il-428.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Petitio Principii (Begging the Question or Circular Argument)"
    publisher: Introduction to Logic, philosophy.lander.edu (Lander University)
    url: https://philosophy.lander.edu/logic/circular.html
    type: academic
    accessed: 2026-11-07
  - id: s5
    title: "Begging the Question"
    publisher: PHL 4 course handout, California State University, Sacramento
    url: https://www.csus.edu/indiv/m/mayesgr/phl4/handouts/phl4begques.htm
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Begging the question

Begging the question (Latin *petitio principii*) is the fallacy of supporting a conclusion with premises that already assume it. The argument can be perfectly valid, since a conclusion trivially follows from itself, yet it proves nothing, because the conclusion receives no support from an independent source.[^s4] The reason offered may restate the conclusion in other words, presuppose it without saying so, or loop back to it through a chain of intermediate claims.[^s5]

## Origin

The idea goes back to Aristotle. The Greek phrase he used means roughly "asking for the starting point", which Latin rendered as *petitio principii*; the English "begging the question" is usually read as begging for the very proposition at issue.[^s1] In the *Prior Analytics* Aristotle treats it as a failure of demonstration, trying to prove through itself something that is not self-evident, while the *Topics* lists five ways to commit it in debate: assuming the point directly, assuming a universal to prove a particular, assuming particulars to prove a universal, assuming each part of a conjunction to prove the whole, and assuming one of two statements that imply each other to prove the other.[^s1] Richard Robinson argued that these two accounts are incompatible; Dilip Basu (1986) replied that Aristotle had a single notion, assuming the conclusion, with several ways of committing it, and noted the parallel Indian notion of *siddhasadhana*, "establishing the established".[^s1] Modern treatments by Charles Hamblin and by John Woods and Douglas Walton revived the debate over what exactly goes wrong.[^s1][^s2]

## How it works

Logic texts separate an immediate form, in which a single premise paraphrases the conclusion, from a mediate circle (*circulus in probando*) in which the conclusion returns through a series of subconclusions, as in "the soul is simple because it is immortal, and immortal because it is simple".[^s4] A third variant is the question-begging epithet: a loaded label that smuggles the conclusion into the premises, such as calling a proposal "reckless" to show it should be rejected.[^s4]

The argument map above shows a workplace case. A customer disputes a vendor's uptime figures, and the vendor answers that its audit confirms them, but the audit was built from the same logs under dispute. Each step may be true, yet nothing in the reasoning gives the doubting customer a reason they did not already have to reject.[^s5][^s2] A related pattern that Sacramento State's course handout calls *a priorism* defines a claim so that nothing could count against it, for example treating every denial as further proof of a cover-up.[^s5]

## How to spot it

Ask whether the reason means the same thing as the conclusion once wording and technical terms are replaced with plain language: "he fears heights because he has acrophobia" only renames the fear.[^s5] Lay long arguments out step by step to see whether the support loops back; ask whether a person who doubts the conclusion would accept the premises; and ask what evidence would count against the claim. If nothing could, the claim may be true by definition rather than by evidence.[^s5] Ask the arguer for support for the premises: if they can only repeat the conclusion, the circle is exposed.[^s4]

## How to counter it

Name the loop without assuming bad faith, then ask for a reason that does not depend on the conclusion, such as independent data, a third-party check, or a premise both sides already accept.[^s4][^s5] Context matters: the same words may or may not beg the question depending on the dialogue and what each side has already granted, so a charge of circularity should rest on clear evidence rather than suspicion.[^s4] Do not mistake a circular explanation or a coherent system of mutually supporting beliefs, which the Lander text calls a "virtuous circle", for a vicious circular argument.[^s4]

## Evidence

Because this is a normative category, the scholarly debate concerns what makes circularity bad, not whether people commit it. Walton (2006) describes a split between an epistemic account, which locates the fault in what the arguer knows or believes, and a dialectical account, which locates it in a dialogue where one side fails to meet its burden of proof; he argues the two can be reformulated to coexist, and identifies the line between argument and explanation as a central technical problem.[^s2] Ulrike Hahn and Mike Oaksford (2006) argue that self-dependent justification is not always wrong: the structure of "God exists because the Bible says so, and the Bible is God's word" matches accepted scientific inferences, such as identifying an electron from cloud-chamber tracks that count as evidence only given the theory of electrons. In their Bayesian account, a bare restatement changes no one's degree of belief and is maximally weak, while other self-dependent arguments can still raise the probability of the hypothesis.[^s3]

## Connections

Aristotle **introduced** the fallacy in his logical and dialectical works, which is why it sits beside the other refutations catalogued in the *Sophistical Refutations* and in the *Prior Analytics*.[^s1] It is often **confused with ignoratio elenchi** (missing the point), name-calling and circular explanations, though each fails differently.[^s4] It **contrasts with inference to the best explanation**, which can share the same self-dependent structure and still be strong when the probabilities support it, and Hahn and Oaksford's work **formalizes** that difference in **Bayesian** terms.[^s3] The dialectical reading ties it to the **burden of proof** in argument and to Walton's argumentation-theoretic tools, while the *a priorist* variant connects it to **falsifiability**.[^s2][^s5]

## Sources

[^s1]: Basu, "A Question of Begging", Informal Logic 8(1) (1986). https://distantreader.org/stacks/journals/il/il-2677.pdf (accessed 2026-11-07)
[^s2]: Walton, "Epistemic and Dialectical Models of Begging the Question", Synthese 152(2), 237-284 (2006). https://dc2.philarchive.org/rec/WALEAD-5 (accessed 2026-11-07)
[^s3]: Hahn & Oaksford, "A Normative Theory of Argument Strength", Informal Logic 26(1), 1-24 (2006). https://distantreader.org/stacks/journals/il/il-428.pdf (accessed 2026-11-07)
[^s4]: "Petitio Principii (Begging the Question or Circular Argument)", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/circular.html (accessed 2026-11-07)
[^s5]: "Begging the Question", PHL 4 handout, California State University, Sacramento. https://www.csus.edu/indiv/m/mayesgr/phl4/handouts/phl4begques.htm (accessed 2026-11-07)
