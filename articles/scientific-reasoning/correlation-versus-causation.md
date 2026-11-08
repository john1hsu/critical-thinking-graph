---
id: ct:correlation-versus-causation
type: Principle
title: Correlation versus causation
aliases: [correlation does not imply causation, correlation is not causation, association versus causation]
domain: scientific-reasoning
summary: >-
  The principle that a statistical association between two variables does not
  by itself show that one causes the other, because the pattern can also arise
  from a common cause, reverse causation, selection of the sample, or chance;
  causal conclusions need further evidence and explicit assumptions.
level: introductory
evidenceStatus: normative
broader: [ct:scientific-method, ct:inductive-reasoning]
related: [ct:post-hoc-ergo-propter-hoc, ct:cum-hoc-ergo-propter-hoc, ct:simpsons-paradox, ct:randomized-controlled-trial, ct:mills-methods, ct:bradford-hill-criteria, ct:regression-to-the-mean, ct:selection-bias, ct:argument-from-correlation-to-cause]
requires: []
relations:
  - {predicate: explainedBy, object: ct:confounding, source: s1, confidence: high}
  - {predicate: formalizedBy, object: ct:causal-diagrams, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:epidemiology, source: s3, confidence: high}
  - {predicate: influencedBy, object: ct:george-udny-yule, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Probabilistic Causation"
    publisher: Stanford Encyclopedia of Philosophy, Spring 2016 Edition (Hitchcock)
    url: https://plato.stanford.edu/archives/Spr2016/entries/causation-probabilistic/
    type: scholarly-encyclopedia
    accessed: 2026-11-08
  - id: s2
    title: "Thinking Clearly About Correlations and Causation: Graphical Causal Models for Observational Data"
    publisher: Advances in Methods and Practices in Psychological Science 1(1):27-42 (Rohrer, 2018), doi:10.1177/2515245917745629
    url: https://www.psychologicalscience.org/journals/ampps/2515245917745629/
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "\"The Environment and Disease: Association or Causation?\" (1965), by Austin Bradford Hill"
    publisher: Embryo Project Encyclopedia, Arizona State University (Abboud, 2017)
    url: https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "The association between exaggeration in health related science news and academic press releases: retrospective observational study"
    publisher: BMJ 349:g7015 (Sumner et al., 2014), PubMed 25498121
    url: https://www.pubmed.gov/25498121/
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "Correlations Genuine and Spurious in Pearson and Yule"
    publisher: Statistical Science 10(4):364-376 (Aldrich, 1995), University of Southampton ePrints
    url: https://eprints.soton.ac.uk/32919
    type: peer-reviewed
    accessed: 2026-11-08
created: 2026-11-08
---

# Correlation versus causation

The principle of correlation versus causation says that finding two things going together, in a dataset or in experience, is not enough to conclude that one produces the other. Philosophers of causation note that two effects of a shared cause can be correlated even though neither influences the other, so a correlation is compatible with several different causal structures.[^s1] Reaching a causal conclusion from observational data is possible, but only by adding assumptions grounded in knowledge of the domain; no mechanical statistical procedure supplies them.[^s2]

## Origin

The modern vocabulary comes from the founders of correlation statistics. Karl Pearson and George Udny Yule developed the standard ways of measuring and interpreting correlation around the turn of the twentieth century, and both also studied cases where conclusions drawn from a correlation proved unreliable, distinguishing genuine from spurious correlations.[^s5] In philosophy, Hans Reichenbach's 1956 book *The Direction of Time* gave the idea a precise form: if two events are correlated and neither causes the other, there should be a common cause that screens off the correlation, so that once the common cause is fixed the two events become independent.[^s1] In medicine, Austin Bradford Hill's 1965 address to the Royal Society of Medicine asked when an observed association between a workplace exposure and a disease should be read as causal, and offered nine viewpoints for judging it.[^s3]

## How it works

A correlation between X and Y can arise in several ways besides X causing Y. A **common cause** can drive both: the standard philosophical example is a drop in air pressure that makes a barometer reading fall and also brings a storm, so the barometer predicts the storm without causing it.[^s1] Causation can run in the **reverse direction**, which is why Hill asked whether the suspected factor came before the disease rather than resulting from it.[^s3] The sample itself can create a pattern: an unrepresentative sample, or statistically controlling for the wrong variable such as a collider or a mediator, can bias an estimate away from the true causal effect.[^s2] And a pattern can be produced by **chance**, which Hill noted significance tests address only partly, since a statistically significant link can still be too small to matter.[^s3] Aggregated data can even reverse direction once a hidden variable is taken into account, as in Simpson's paradox.[^s1]

Workplace example: an analyst notices that teams that use a new project-management tool hit more deadlines. Before crediting the tool, she asks whether better-resourced teams were simply first to adopt it (common cause), whether teams that were already on track had time to try new tools (reverse causation), and whether the comparison quietly dropped projects that were cancelled (selection). Each alternative predicts the same correlation, so the correlation alone cannot choose between them.[^s2]

## How to apply it

1. **List rival structures.** For any reported association, write down at least a common-cause, a reverse-causation and a selection explanation alongside the causal one.[^s2]
2. **Draw the assumed causal graph.** Graphical causal models make explicit which third variables should be controlled for and which should not, so adjustment does not introduce bias.[^s2]
3. **Weigh converging evidence.** Hill's viewpoints, including strength, consistency, temporality, dose-response gradient, plausibility and experimental evidence, are guides rather than rules; none is strictly necessary or sufficient on its own.[^s3]
4. **Prefer intervention where possible.** Setting a variable by intervention tells us something different from merely observing it, which is why experiments carry more causal weight than passive observation.[^s1]
5. **Check the wording.** When reading news or reports, compare causal verbs such as "boosts" or "prevents" with the design of the underlying study.[^s4]

## Evidence and limitations

The confusion is common in practice. A 2014 analysis of 462 press releases from 20 leading UK universities found that a third made causal claims stronger than the correlational research behind them supported, and when a release did so, 81% of the related news stories repeated the exaggeration, against 18% when the release was accurate.[^s4] The principle has limits of its own. It does not say correlations are useless: Hill's central example, the association between smoking and lung cancer studied with Richard Doll, was judged causal because its strength outweighed its low specificity.[^s3] Many causal questions can only be studied with observational data, so the slogan should not become a reason to dismiss such findings wholesale; the better question is which specific assumptions a causal reading needs and whether they are plausible.[^s2]

## Connections

Spurious correlation is **explained by** confounding: a common cause makes its effects co-vary, and conditioning on that cause removes the association.[^s1] The principle is **formalized by** causal diagrams, which show which statistical controls remove bias and which add it.[^s2] It is routinely **applied in** epidemiology, where the Bradford Hill criteria structure the move from association to causation.[^s3] Its history is **influenced by** George Udny Yule, who with Pearson worked out how genuine and spurious correlations differ.[^s5] Treating a mere correlation as proof of cause is the fallacy of cum hoc ergo propter hoc, a cousin of post hoc ergo propter hoc; interventions such as randomized controlled trials, and explicit causal assumptions when only observational data exist, are the ways to go further.[^s1][^s2]

## Sources

[^s1]: Hitchcock, "Probabilistic Causation", Stanford Encyclopedia of Philosophy, Spring 2016 Edition. https://plato.stanford.edu/archives/Spr2016/entries/causation-probabilistic/ (accessed 2026-11-08)
[^s2]: Rohrer, "Thinking Clearly About Correlations and Causation: Graphical Causal Models for Observational Data", *Advances in Methods and Practices in Psychological Science* 1(1):27-42, 2018. https://www.psychologicalscience.org/journals/ampps/2515245917745629/ (accessed 2026-11-08)
[^s3]: Abboud, "'The Environment and Disease: Association or Causation?' (1965), by Austin Bradford Hill", Embryo Project Encyclopedia, Arizona State University, 2017. https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill (accessed 2026-11-08)
[^s4]: Sumner et al., "The association between exaggeration in health related science news and academic press releases: retrospective observational study", *BMJ* 349:g7015, 2014. https://www.pubmed.gov/25498121/ (accessed 2026-11-08)
[^s5]: Aldrich, "Correlations Genuine and Spurious in Pearson and Yule", *Statistical Science* 10(4):364-376, 1995. https://eprints.soton.ac.uk/32919 (accessed 2026-11-08)
