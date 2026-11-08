---
id: ct:problem-of-induction
type: Concept
title: Problem of induction
aliases: [Hume's problem of induction, Humean problem of induction, justification of induction, inductive scepticism]
domain: philosophy-of-reasoning
summary: >-
  The philosophical problem, posed by David Hume, of justifying inferences from
  observed cases to unobserved ones: any argument that the future will resemble
  the past either cannot be deductive or must assume the very uniformity it is
  meant to prove.
level: intermediate
evidenceStatus: normative
broader: [ct:epistemology]
related: [ct:inductive-reasoning, ct:begging-the-question, ct:falsifiability, ct:karl-popper, ct:bayesian-reasoning, ct:philosophy-of-science]
requires: [ct:inductive-reasoning, ct:deductive-reasoning]
relations:
  - {predicate: introducedBy, object: ct:david-hume, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:a-treatise-of-human-nature, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:epistemology, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s1, confidence: medium}
  - {predicate: challengedBy, object: ct:fact-fiction-and-forecast, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Problem of Induction"
    publisher: Stanford Encyclopedia of Philosophy (Leah Henderson, first published 2018, revised 2022; Fall 2023 edition)
    url: https://plato.stanford.edu/archives/fall2023/entries/induction-problem
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "The Problem of Induction"
    publisher: Internet Encyclopedia of Philosophy (Stathis Psillos and Chrysovalantis Stergiou)
    url: https://iep.utm.edu/problem-of-induction/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s3
    title: "An Enquiry Concerning Human Understanding, Section IV: Sceptical Doubts concerning the Operations of the Understanding"
    publisher: David Hume (1748); course copy hosted for MITx 24.00x on edX
    url: https://courses.edx.org/asset-v1:MITx+24.00x+2T2018+type@asset+block/HumeSkepticalDoubts.pdf
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Nelson Goodman"
    publisher: Stanford Encyclopedia of Philosophy (Spring 2019 edition)
    url: https://plato.stanford.edu/archives/spr2019/entries/goodman/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
created: 2026-11-08
---

# Problem of induction

The problem of induction asks what, if anything, justifies inductive inference: reasoning from cases we have observed to cases we have not, whether the next instance, a future event or a general law.[^s1] Hume's everyday example is bread. Its colour and texture tell us nothing about the hidden powers that make it nourishing, yet having been fed by bread before, we confidently expect similar bread to feed us again.[^s3] The problem is not that such expectations are usually wrong. It is that no one has found a non-circular argument showing they are reasonable. For critical thinkers it marks the limit of what any track record can prove.

## Origin

David Hume stated the argument in *A Treatise of Human Nature* (1739, Book 1, Part iii, Section 6) and restated it more compactly in *An Enquiry Concerning Human Understanding* (1748, Section IV).[^s1] Hume himself seldom used the word "induction"; he framed the issue as one about inferences from cause to effect.[^s2] Earlier thinkers, from Bacon to Leibniz, had debated the reliability of induction, but the problem was not widely treated as a distinct, central puzzle until the twentieth century. Bertrand Russell in 1912 separated the psychological question of how we come to expect regularities from the logical question of whether those expectations are justified, and C. D. Broad in 1926 called the unsolved problem philosophy's "skeleton in the cupboard".[^s2]

## How it works

Hume's argument is a dilemma, often called Hume's fork. Every argument is either demonstrative, concerning relations of ideas, or probable, concerning matters of fact.[^s1] Inductive inference rests on what Henderson calls the Uniformity Principle: unobserved cases will resemble observed ones.[^s1] A demonstrative proof of that principle is impossible, because a change in the course of nature can be imagined without contradiction. A probable argument for it would appeal to experience, but every inference from experience already presupposes uniformity, so such an argument would assume the point at issue.[^s1][^s3] Hume's conclusion was that reason does not ground our inductive expectations; custom or habit does, as a natural instinct.[^s1]

A workplace version shows the bite. An operations team notes that the nightly deployment pipeline has not failed on a weekend in two years and decides to drop weekend on-call cover. The inference is sensible, but its support is entirely the past record plus the unstated premise that the coming weekends will resemble past ones. If someone asks why the record should continue, pointing to the record again answers nothing; that circularity is the logical shape of the problem.[^s1][^s3]

Nelson Goodman's "new riddle of induction" in *Fact, Fiction, and Forecast* (1954; Harvard edition 1955) sharpened the difficulty. Define an object as "grue" if it is examined before some future time and is green, or not so examined and is blue. Every green emerald seen so far supports "all emeralds are grue" as well as "all emeralds are green", yet the two predict different colours for emeralds examined later.[^s4] The same evidence fits rival generalisations, so even granting that induction works, we need a principled way to choose which patterns to project.[^s4][^s1] In the pipeline example, "the pipeline is reliable" and "the pipeline is reliable until its signing certificate expires" fit the record equally well.

## Responses

No answer commands general agreement, but the main families are these:[^s1][^s2]

- **Probabilistic.** Following Bayes (published 1764) and Laplace's rule of succession (1814), Bayesian accounts show how evidence can raise the probability of a prediction. Critics reply that the result depends on prior probabilities and modelling assumptions that are not themselves known a priori.[^s1]
- **Pragmatic vindication.** Hans Reichenbach granted Hume's argument but held that the straight rule of induction will find a limiting frequency if any method can; critics note that many rules share that long-run property and it says little about the short run.[^s1][^s2]
- **Dissolution.** P. F. Strawson (1952) argued that proportioning belief to evidence is simply what it means to be reasonable, so asking whether induction as a whole is reasonable is confused.[^s1][^s2]
- **Deductivism.** Karl Popper accepted that no finite set of observations verifies a universal law and proposed that science advances by testing and trying to falsify conjectures, not by inductive confirmation.[^s2]
- **Rule-circular and material accounts.** Some defend inductive justifications of induction as benignly circular; John Norton argues that inductive inferences are licensed by local facts, not a single formal schema.[^s1]

## How to apply it

The practical lesson is not to stop generalising but to know what a generalisation rests on. When a forecast or policy leans on a track record, ask which conditions produced the record and whether they still hold; a known mechanism carries more weight than a bare streak.[^s1] When the data fit one pattern, look for a rival, grue-like generalisation that fits equally well and predicts a different future, especially around known change points.[^s4] Treat conclusions from experience as revisable, which is the attitude Popper's falsificationism builds into method.[^s2]

## Connections

- **Introduced by David Hume** in *A Treatise of Human Nature* (1739), with the more widely read restatement in the *Enquiry* (1748).[^s1][^s3]
- **Studied in epistemology** as a central problem for theories of justification, and **in philosophy of science**, where it shapes debates about confirmation and theory choice.[^s2][^s1]
- **Challenged by Goodman's *Fact, Fiction, and Forecast*,** which argued that the old problem is a pseudo-problem, since deduction too is justified only by bringing rules and accepted inferences into agreement, and replaced it with the new riddle of projectibility.[^s4]
- **Related to inductive reasoning,** whose justification it questions, and to **begging the question,** the circularity Hume found in any experience-based defence of uniformity.[^s1][^s3]
- **Related to falsifiability and Karl Popper,** whose deductivist methodology was designed to avoid relying on induction, and to **Bayesian reasoning,** the leading probabilistic response.[^s2][^s1]

## Sources

[^s1]: Henderson, "The Problem of Induction", Stanford Encyclopedia of Philosophy (Fall 2023 edition; rev. 2022). https://plato.stanford.edu/archives/fall2023/entries/induction-problem (accessed 2026-11-08)
[^s2]: Psillos and Stergiou, "The Problem of Induction", Internet Encyclopedia of Philosophy. https://iep.utm.edu/problem-of-induction/ (accessed 2026-11-08)
[^s3]: Hume, *An Enquiry Concerning Human Understanding* (1748), Section IV, course copy for MITx 24.00x. https://courses.edx.org/asset-v1:MITx+24.00x+2T2018+type@asset+block/HumeSkepticalDoubts.pdf (accessed 2026-11-08)
[^s4]: "Nelson Goodman", Stanford Encyclopedia of Philosophy (Spring 2019 edition). https://plato.stanford.edu/archives/spr2019/entries/goodman/ (accessed 2026-11-08)
