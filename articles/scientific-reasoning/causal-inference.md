---
id: ct:causal-inference
type: Field
title: Causal inference
aliases: [causal analysis, causal reasoning from data, inference of cause and effect]
domain: scientific-reasoning
summary: >-
  The study and practice of drawing justified conclusions about cause and
  effect, rather than mere association, from experiments, observational data
  and explicit background assumptions, using tools such as potential outcomes,
  randomization, structural causal models and causal diagrams.
level: intermediate
evidenceStatus: normative
broader: [ct:inductive-reasoning]
related: [ct:causal-diagrams, ct:confounding, ct:selection-bias, ct:randomized-controlled-trial, ct:mills-methods, ct:simpsons-paradox, ct:necessary-and-sufficient-conditions, ct:statistical-reasoning]
requires: [ct:correlation-versus-causation, ct:conditional-probability]
relations:
  - {predicate: influencedBy, object: ct:donald-rubin, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:judea-pearl, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:austin-bradford-hill, source: s3, confidence: medium}
  - {predicate: appliedIn, object: ct:epidemiology, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:associational-inference, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Causal inference in statistics: An overview"
    publisher: "Statistics Surveys 3:96-146 (Pearl, 2009), doi:10.1214/09-SS057; UCLA Cognitive Systems Laboratory reprint R-350"
    url: https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Statistics and Causal Inference"
    publisher: "Journal of the American Statistical Association 81(396):945-960 (Holland, 1986); copy hosted on a Columbia University course page"
    url: https://www.cs.columbia.edu/~blei/fogm/2023F/readings/Holland1986.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "\"The Environment and Disease: Association or Causation?\" (1965), by Austin Bradford Hill"
    publisher: "Embryo Project Encyclopedia, Arizona State University (Abboud, 2017)"
    url: https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill
    type: academic
    accessed: 2026-11-14
created: 2026-11-14
---

# Causal inference

Causal inference is the discipline concerned with moving from evidence to claims of the form "X makes a difference to Y". Its starting point is a sharp line between associational concepts, such as correlation, regression and conditional independence, which can be read off a probability distribution, and causal concepts, such as intervention, effect and confounding, which cannot.[^s1] Judea Pearl draws the practical moral that no causal conclusion follows from associations alone: every causal claim rests on some assumption that the observational data cannot test, and the job of the field is to make those assumptions explicit and work out what follows from them.[^s1] It is practised across statistics, epidemiology, economics and the social sciences, and it underpins the everyday critical-thinking rule that correlation does not establish causation.

## Origin

The modern field grew from two converging traditions. The first is the potential-outcomes model associated with Donald Rubin, which Paul Holland systematised in a 1986 *Journal of the American Statistical Association* paper.[^s2] In that model a causal effect is always a comparison: the difference between the outcome a unit would show under a treatment and the outcome it would show under a control.[^s2] Holland named the central obstacle the *Fundamental Problem of Causal Inference*: for any one unit only one of those outcomes is ever observed, so individual effects can never be seen directly.[^s2] He also defended the motto, credited to himself and Rubin, that there is no causation without manipulation, which excludes fixed attributes that could never be altered for the same unit.[^s2]

The second tradition is structural and graphical. Pearl's 2009 survey presents structural causal models, sets of equations each describing one causal mechanism paired with a diagram, as a framework that unifies structural equation modelling, potential outcomes and graphical models.[^s1] An older, informal strand comes from epidemiology: in 1965 Austin Bradford Hill, drawing on the smoking and lung-cancer studies he ran with Richard Doll, proposed nine viewpoints (strength, consistency, specificity, temporality, dose-response gradient, plausibility, coherence, experiment and analogy) for judging whether an association is causal.[^s3]

## How it works

The field offers two broad routes to an answer. The *statistical solution* gives up on individual effects and targets an average causal effect over a population; random assignment makes the treated and untreated groups comparable, so the simple difference in their average outcomes estimates that average effect.[^s2] When randomization is impossible, analysts must instead argue from assumptions. Pearl formalises an intervention with the *do*-operator: setting X to a value means replacing the equation that normally determines X, and the resulting distribution, written P(y | do(x)), generally differs from the ordinary conditional P(y | x).[^s1] His back-door criterion then says which measured variables are enough to adjust for: a set qualifies if it contains no consequence of X and blocks every path that enters X from behind.[^s1] Pearl also warns that adjusting for too many covariates can introduce bias rather than remove it.[^s1]

A workplace example shows the difference. A company notices that staff who attended an optional time-management course hit more of their targets. Read associationally, the course "works". A causal analyst asks what would have happened to those same people without the course. Perhaps motivated employees both sign up and hit targets, so motivation confounds the comparison. Randomly offering the course to half of a team would break that link; failing that, the analyst would draw a diagram, measure plausible common causes such as prior performance, and state openly that the estimate holds only if no unmeasured cause remains.[^s1][^s2]

## How to apply it

1. State the causal question as a contrast: the effect of *this* treatment compared with *that* alternative, in a defined population.[^s2]
2. Ask whether the data come from random assignment. If not, write down the assumed causal structure, ideally as a diagram, before looking at results.[^s1]
3. Choose adjustment variables by the structure, not by habit, and avoid conditioning on consequences of the treatment.[^s1]
4. For observational evidence, weigh the association against Hill's viewpoints, remembering that he offered them as aids to judgment, not a checklist: an absence of specificity or of a known mechanism does not rule causation out.[^s3]
5. Report which assumptions are untestable and how conclusions would change if they failed.[^s1][^s2]

## Limitations

Causal inference cannot escape assumptions; it can only make them visible. Holland stresses that homogeneity and invariance assumptions used by experimental scientists are untestable, though they can be made plausible.[^s2] Even randomized trials can fail to identify an effect when people do not take the treatment they were assigned, and Pearl notes that only bounds may then be available without further assumptions.[^s1] The manipulation requirement is itself contested, because it makes questions about the effects of attributes such as sex hard to pose within the potential-outcomes model.[^s2]

## Connections

Causal inference is a specialised branch of inductive reasoning, since its conclusions go beyond the data and are defeasible. It turns the principle of correlation versus causation into methods, and its main enemies are confounding, selection bias and reversals such as Simpson's paradox, which it treats as consequences of causal structure rather than of statistics alone.[^s1] It contrasts with associational inference, which Pearl treats as a different kind of analysis answering different questions.[^s1] Its potential-outcomes core was shaped by Donald Rubin, as Holland's account makes clear,[^s2] and its graphical side by Judea Pearl.[^s1] Causal diagrams, randomized controlled trials and Mill's methods are its tools, and epidemiology is the field where it is most routinely applied, with Austin Bradford Hill's viewpoints still taught as a bridge from association to causation.[^s3]

## Sources

[^s1]: Pearl, "Causal inference in statistics: An overview", *Statistics Surveys* 3 (2009). https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf (accessed 2026-11-14)
[^s2]: Holland, "Statistics and Causal Inference", *Journal of the American Statistical Association* 81 (1986). https://www.cs.columbia.edu/~blei/fogm/2023F/readings/Holland1986.pdf (accessed 2026-11-14)
[^s3]: Abboud, "The Environment and Disease: Association or Causation? (1965), by Austin Bradford Hill", Embryo Project Encyclopedia, Arizona State University. https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill (accessed 2026-11-14)
