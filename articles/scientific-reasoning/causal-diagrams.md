---
id: ct:causal-diagrams
type: Method
title: Causal diagrams
aliases: [causal DAG, causal directed acyclic graph, directed acyclic graph (DAG) in causal inference, causal graph]
domain: scientific-reasoning
summary: >-
  Graphs in which arrows encode assumed direct cause-and-effect relations
  between variables, used to make causal assumptions explicit and to work out
  which variables must, and must not, be adjusted for when estimating an effect
  from observational data.
level: intermediate
evidenceStatus: normative
broader: [ct:causal-inference]
related: [ct:confounding, ct:selection-bias, ct:correlation-versus-causation, ct:simpsons-paradox, ct:randomized-controlled-trial, ct:mills-methods, ct:berksons-paradox, ct:argument-mapping]
requires: [ct:confounding]
relations:
  - {predicate: counteracts, object: ct:confounding, source: s3, confidence: high}
  - {predicate: detects, object: ct:selection-bias, source: s3, confidence: medium}
  - {predicate: appliedIn, object: ct:epidemiology, source: s4, confidence: high}
  - {predicate: introducedBy, object: ct:sewall-wright, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:judea-pearl, source: s2, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Causal Models"
    publisher: Stanford Encyclopedia of Philosophy (Hitchcock, first published 2018)
    url: https://plato.stanford.edu/entries/causal-models/
    type: scholarly-encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "Causal diagrams for empirical research"
    publisher: "Biometrika 82(4):669-710 (Pearl, 1995); author copy hosted by UC Irvine course page"
    url: https://www.ics.uci.edu/~dechter/courses/ics-295cr/2022-23_Q2_Winter/reading/biometrika_1995.pdf
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Causal Diagrams for Epidemiologic Research"
    publisher: "Epidemiology 10(1):37-48 (Greenland, Pearl and Robins, 1999); copy hosted on an Ohio State University course site"
    url: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/7/36891/files/2020/01/Greenland-Pearl-and-Robins-1999.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Use of directed acyclic graphs (DAGs) to identify confounders in applied health research: review and recommendations"
    publisher: "International Journal of Epidemiology 50(2):620-632 (Tennant et al., 2021), doi:10.1093/ije/dyaa213; White Rose Research Online record"
    url: https://eprints.whiterose.ac.uk/id/eprint/180527/
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Causal diagrams

A causal diagram is a picture of what you believe causes what. Each variable is a node, and an arrow from X to Y says that X is a direct cause of Y relative to the variables drawn; just as important, every missing arrow is a claim that there is no direct effect.[^s1][^s3] Because the arrows never loop back on themselves, such diagrams are usually called directed acyclic graphs (DAGs).[^s1] Their practical job is to turn vague worries about "other factors" into a definite map that tells an analyst which comparisons can and cannot support a causal conclusion from observational data.[^s2][^s3]

## Origin

Hitchcock traces graphical causal modelling to the geneticist Sewall Wright's path analysis of 1921, with later contributions from econometrics, epidemiology, philosophy and computer science; he singles out Spirtes, Glymour and Scheines (2000) and Judea Pearl (2009) as especially influential.[^s1] Pearl's 1995 *Biometrika* paper, titled "Causal diagrams for empirical research", proposed graphs as a nonparametric language for combining subject-matter knowledge with data, and gave the back-door and front-door criteria and a calculus of interventions for deciding whether an effect can be identified without an experiment.[^s2] In 1999 Sander Greenland, Pearl and James Robins introduced the method to epidemiologists, showing how diagrams settle which variables to measure and control.[^s3]

## How it works

Three structures do most of the work.[^s3]

- **Chain (A → M → B).** M lies on the causal pathway; adjusting for it removes part of the very effect you want to estimate.
- **Fork (A ← C → B).** C is a common cause. The open path through C creates an association between A and B that is not causal: confounding. Greenland and colleagues give a simple test: delete every arrow leaving the exposure, and if any unblocked path still links exposure and outcome, confounding is present.[^s3]
- **Collider (A → K ← B).** K is a common effect. The path is blocked as long as K is left alone, but conditioning on K (stratifying, matching, or studying only one level of it) opens the path and manufactures an association between A and B.[^s3]

The rule that ties these together is d-separation, which reads off from the graph which variables should be statistically independent given others.[^s1][^s3] Pearl's back-door criterion then says a set of variables is a sufficient adjustment set if it blocks every path into the exposure without including anything the exposure causes.[^s1][^s2] The graph also separates *seeing* from *doing*: the probability of an outcome after intervening on X, written with Pearl's do-operator, can differ from the probability after merely observing X, and the graph shows when the two coincide.[^s1]

A workplace example. An HR team notices that staff who took a voluntary leadership course were more often promoted and wants to credit the course. A diagram makes the competing stories explicit: ambition plausibly drives both enrolment and promotion (a fork), so ambition, or a good proxy such as prior performance ratings, must be adjusted for. The diagram also warns against a tempting move: restricting the analysis to employees who received a manager nomination, if nominations depend on both course attendance and ambition, would condition on a collider and create a spurious link.[^s3] The diagram does not say whether the course works; it says which comparison could tell.

## How to apply it

1. **Name the question**: one exposure, one outcome, and the effect you want (the estimand).[^s4]
2. **Draw from subject knowledge, not from the data.** Add every common cause of exposure and outcome you know of, including unmeasured ones; omitted arrows are the strongest assumptions, so justify each.[^s1][^s3]
3. **Find the back-door paths** and choose a minimal set of measured variables that blocks them, avoiding mediators and colliders.[^s2][^s3]
4. **Report the diagram and the adjustment set it implies**, so readers can dispute the assumptions rather than guess at them.[^s4]
5. **If no measured set suffices**, the diagram tells you what extra data or experiment would make the effect identifiable.[^s2]

Pitfalls: drawing arrows to fit the variables you happen to have, treating every available covariate as something to "control for", and forgetting that a diagram is only as good as the knowledge behind it.[^s3]

## Evidence and limitations

As a set of inference rules, causal diagrams are normative: they are mathematically proven consequences of stated assumptions, not empirical findings.[^s2] Their limits are therefore about those assumptions. Greenland, Pearl and Robins stress that the graphs are qualitative: they clarify which biases may exist but cannot by themselves establish causation from observational data or measure how large residual bias is.[^s3] Hitchcock notes that the underlying Markov condition can fail with badly defined or overly coarse variables, and that, without further assumptions, data alone usually narrow the possible graphs only to a family of equivalent ones.[^s1] Practice also lags theory: a 2021 review of 234 health studies that used DAGs found that only 48% reported the adjustment sets their diagrams implied and only 21% stated their target estimand, and that the diagrams varied widely in size and density.[^s4]

## Connections

Causal diagrams sit under **causal inference** and are the standard tool for formalising **confounding**: the fork structure and back-door test directly counteract confounded comparisons.[^s3] The collider rule explains **selection bias** and **Berkson's paradox**, where conditioning on a common effect creates a false association, so the method helps detect them.[^s3] By saying which variables to stratify on and which to leave alone, they help decide between aggregated and stratified tables in cases like **Simpson's paradox**, and their distinction between seeing and doing sharpens the old maxim about **correlation versus causation**.[^s1][^s3] They were **introduced** in path-analysis form by **Sewall Wright** and in their modern form by **Judea Pearl**, and are now widely **applied in epidemiology**.[^s1][^s2][^s4] A **randomized controlled trial** works, in graph terms, by cutting every arrow into the treatment, while **Mill's methods** tackle the same elimination problem without an explicit causal model; like an **argument map**, a DAG lays out assumptions so they can be checked one at a time.[^s1][^s3]

## Sources

[^s1]: Hitchcock, "Causal Models", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/causal-models/ (accessed 2026-11-11)
[^s2]: Pearl, "Causal diagrams for empirical research", *Biometrika* 82(4):669-710, 1995. https://www.ics.uci.edu/~dechter/courses/ics-295cr/2022-23_Q2_Winter/reading/biometrika_1995.pdf (accessed 2026-11-11)
[^s3]: Greenland, Pearl and Robins, "Causal Diagrams for Epidemiologic Research", *Epidemiology* 10(1):37-48, 1999. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/7/36891/files/2020/01/Greenland-Pearl-and-Robins-1999.pdf (accessed 2026-11-11)
[^s4]: Tennant et al., "Use of directed acyclic graphs (DAGs) to identify confounders in applied health research: review and recommendations", *International Journal of Epidemiology* 50(2):620-632, 2021. https://eprints.whiterose.ac.uk/id/eprint/180527/ (accessed 2026-11-11)
