---
id: ct:mills-methods
type: Method
title: Mill's methods
aliases: [Mill's canons, Mill's methods of induction, methods of experimental inquiry, Mill's canons of induction]
domain: scientific-reasoning
summary: >-
  Five eliminative rules for identifying causes, set out by John Stuart Mill in
  1843: the methods of agreement, difference, joint agreement and difference,
  residues, and concomitant variation, each of which rules out candidate causes
  by comparing cases where an effect does and does not occur.
level: introductory
evidenceStatus: normative
broader: [ct:inductive-reasoning, ct:scientific-method]
related: [ct:randomized-controlled-trial, ct:confounding, ct:correlation-versus-causation, ct:hypothesis-testing, ct:william-whewell, ct:causal-diagrams]
requires: []
relations:
  - {predicate: counteracts, object: ct:post-hoc-ergo-propter-hoc, source: s4, confidence: high}
  - {predicate: counteracts, object: ct:false-cause, source: s4, confidence: high}
  - {predicate: introducedBy, object: ct:john-stuart-mill, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:a-system-of-logic, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "A System of Logic, Ratiocinative and Inductive, Vol. 1 (3rd ed.), Book III, ch. VIII: Of the Four Methods of Experimental Inquiry"
    publisher: John Parker, London (John Stuart Mill, 1851), Project Gutenberg edition
    url: https://www.gutenberg.org/files/26495/26495.txt
    type: primary
    accessed: 2026-11-08
  - id: s2
    title: "Mill's Methods of Induction"
    publisher: The Encyclopedia of Philosophy, Macmillan (J. L. Mackie, 1967), via Encyclopedia.com
    url: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/mills-methods-induction
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s3
    title: "Experiment in Biology"
    publisher: Stanford Encyclopedia of Philosophy, Winter 2024 Edition (Marcel Weber)
    url: https://plato.stanford.edu/archives/win2024/entries/biology-experiment/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s4
    title: "Causal Reasoning (ch. 10 of The Logic Book: Critical Thinking)"
    publisher: Affordable Learning Georgia (OpenALG), Manifold Scholarship
    url: https://alg.manifoldapp.org/read/the-logic-book-clayton/section/782338cf-0681-4a96-8f8d-9e7b5812d666
    type: textbook
    accessed: 2026-11-08
  - id: s5
    title: "Mill's methods"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/print/article/1528471
    type: encyclopedia
    accessed: 2026-11-08
created: 2026-11-08
---

# Mill's methods

Mill's methods are a family of rules for finding out which of the circumstances surrounding an effect actually cause it. They work by comparison: line up cases in which the effect occurs, and cases in which it does not, and see which candidate factor survives.[^s5] Mill called them methods of *elimination*, because each one narrows the field by excluding circumstances that cannot be the cause.[^s1][^s2] They remain the standard textbook answer to the question "how would you show that A caused B, rather than merely came before it?"[^s4]

## Origin

John Stuart Mill set the methods out in *A System of Logic, Ratiocinative and Inductive* (1843), Book III, chapters 8 to 10.[^s2][^s5] He titled the central chapter "Of the Four Methods of Experimental Inquiry", counting agreement, difference, residues and concomitant variation, with the joint method of agreement and difference as a combination of the first two; later textbooks usually list five.[^s1][^s5] J. L. Mackie's 1967 survey notes that critics from William Whewell and W. S. Jevons to Cohen and Nagel doubted that the methods could prove anything or help with discovery.[^s2]

## How it works

Each method states a pattern of cases and the causal conclusion it licenses.[^s2][^s5]

- **Agreement.** If several cases of the effect share only one circumstance, that circumstance is probably the cause.[^s2]
- **Difference.** If a case where the effect occurs and a case where it does not are alike in every respect but one, the factor present only in the first is the cause or an indispensable part of it.[^s1][^s2]
- **Joint method.** Agreement among positive cases combined with its absence among negative cases, used when a single clean contrast is unavailable.[^s2][^s5]
- **Residues.** Subtract the part of an effect already explained by known causes and attribute what remains to the remaining circumstances.[^s2][^s5]
- **Concomitant variation.** If an effect rises and falls in step with a factor, the two are causally connected in some way.[^s5]

Mill ranked difference above the rest: he held that only it can establish causes directly, while agreement mainly suggests candidates for a later test of difference.[^s1] A controlled experiment, with a treated group and an otherwise identical control group, is the method of difference put into practice.[^s2][^s3]

Consider a workplace case. An online shop's checkout conversions fall on the Wednesday after a Tuesday software release, and the team is ready to roll the release back. That is post hoc reasoning. Applying the methods, an analyst checks agreement (do all affected sessions share the new release, or do they share a payment provider?) and then difference (did customers routed to the old version through a staged rollout convert normally on the same day?). If the old-version group dropped too, the release is eliminated and attention moves to whatever both groups had in common.[^s1][^s4]

## How to apply it

1. **List the candidate causes** you can think of. The methods only eliminate from a list you supply; they cannot conjure the right factor if it is missing.[^s2][^s4]
2. **Gather positive and negative cases.** Agreement needs several cases with the effect; difference needs at least one similar case without it.[^s1]
3. **Prefer a test of difference.** Where you can intervene, split a homogeneous group and change one factor in half of it. Weber's laboratory example divides a well-mixed bacterial culture, adds a suspected antibiotic to one portion and only buffer to the other, so that hidden differences between the two portions are unlikely.[^s3] The OpenALG textbook notes that this usually needs a deliberate experiment rather than data already on hand.[^s4]
4. **Use residues and concomitant variation as supplements.** Variation that tracks a factor is suggestive, but the textbook warns it should never be the only evidence.[^s4]
5. **Treat conclusions as provisional.** The methods are better at ruling a suspect out than at proving one guilty, and they cannot tell you whether you have found the full cause.[^s4]

## Evidence and limitations

As rules of method, Mill's canons are normative rather than empirical claims, and their weaknesses are well mapped. Mackie lists the plurality of causes (the same effect arising from different causes, which defeats agreement), the intermixture of effects (causes that act only in combination), and the deeper point that every method assumes the cause lies within a list of factors that the method itself cannot justify.[^s2] Weber reconstructs the method of difference as a deduction whose premises include homogeneity of the compared situations and a deterministic cause, and argues that such premises are vindicated by the success of experimental practice rather than proven.[^s3] He also reports the view, associated with Nancy Cartwright, that these methods refine existing causal knowledge rather than extracting causes from bare associations.[^s3] Mackie defends the methods as genuinely used in discovery and as self-correcting when their assumptions fail.[^s2]

## Connections

Mill's methods **counteract post hoc ergo propter hoc** and the wider **false cause** family: the OpenALG textbook presents them as the systematic way to gather evidence for or against a causal assumption so that a reasoner does not leap from sequence or coincidence to cause.[^s4] They were **introduced by John Stuart Mill** in ***A System of Logic*** (1843).[^s1][^s2] They are a form of **inductive reasoning** and part of the **scientific method**; the **randomized controlled trial** can be read as a refined method of difference, and **confounding** names exactly the hidden extra difference that the method's homogeneity assumption rules out.[^s2][^s3] **William Whewell** was among their earliest critics, and modern **causal diagrams** address the same problem of separating **correlation from causation** with richer tools.[^s2][^s3]

## Sources

[^s1]: Mill, *A System of Logic, Ratiocinative and Inductive*, Vol. 1, 3rd ed., Book III, ch. VIII, John Parker, 1851 (Project Gutenberg). https://www.gutenberg.org/files/26495/26495.txt (accessed 2026-11-08)
[^s2]: Mackie, "Mill's Methods of Induction", *The Encyclopedia of Philosophy*, Macmillan, 1967 (via Encyclopedia.com). https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/mills-methods-induction (accessed 2026-11-08)
[^s3]: Weber, "Experiment in Biology", Stanford Encyclopedia of Philosophy, Winter 2024 Edition. https://plato.stanford.edu/archives/win2024/entries/biology-experiment/ (accessed 2026-11-08)
[^s4]: "Causal Reasoning", ch. 10 of *The Logic Book: Critical Thinking*, Affordable Learning Georgia (OpenALG). https://alg.manifoldapp.org/read/the-logic-book-clayton/section/782338cf-0681-4a96-8f8d-9e7b5812d666 (accessed 2026-11-08)
[^s5]: "Mill's methods", Encyclopaedia Britannica. https://www.britannica.com/print/article/1528471 (accessed 2026-11-08)
