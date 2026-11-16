---
id: ct:formal-modeling
type: Method
title: Formal modeling
aliases: [formal theory building, formalization of theories, mathematical and computational modeling, formal theory construction]
domain: scientific-reasoning
summary: >-
  Restating a theory as an explicit mathematical, logical or computational
  model, so that its constructs, assumptions, scope and predictions are fixed
  in a precise language and can be derived, inspected and tested rather than
  left to verbal interpretation.
level: intermediate
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:preregistration, ct:falsifiability, ct:replication-crisis, ct:ambiguity, ct:vagueness, ct:precising-definition, ct:operational-definition, ct:researcher-degrees-of-freedom, ct:ad-hoc-hypothesis, ct:formal-logic, ct:overfitting]
requires: [ct:hypothesis-testing]
relations:
  - {predicate: counteracts, object: ct:strategic-ambiguity, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:motte-and-bailey, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:verbal-theory, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:replication-crisis, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Strategic Ambiguity in the Social Sciences"
    publisher: Social Psychological Bulletin 18, e9923 (Frankenhuis, Panchanathan & Smaldino, 2023)
    url: https://spb.psychopen.eu/index.php/spb/article/download/9923/9923.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Invisible Hands and Fine Calipers: A Call to Use Formal Theory as a Toolkit for Theory Construction"
    publisher: Perspectives on Psychological Science 16(4), 725-743 (Robinaugh, Haslbeck, Ryan, Fried & Waldorp, 2021), doi:10.1177/1745691620974697; PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8273080
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "How Computational Modeling Can Force Theory Building in Psychological Science"
    publisher: Perspectives on Psychological Science 16(4), 789-802 (Guest & Martin, 2021); PhilArchive record
    url: https://philarchive.org/rec/GUEHCM
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Better methods can't make up for mediocre theory"
    publisher: Nature 575, 9 (Smaldino, World View column, 7 November 2019)
    url: https://media.nature.com/original/magazine-assets/d41586-019-03350-5/d41586-019-03350-5.pdf
    type: news
    accessed: 2026-11-16
created: 2026-11-16
---

# Formal modeling

Formal modeling is the practice of stating a theory in a precise language, such as mathematical equations, formal logic or computer code, instead of only in prose.[^s2] A verbal theory can be read in many ways and often does not determine which predictions it makes; a formal theory with the same structure lets researchers work out what the theory actually implies about the system it describes.[^s2] In the social sciences it has been promoted as a cure for theories that are vague, sometimes strategically so, because writing a model forces the theorist to name every construct, every relation between constructs and every assumption.[^s1]

## Origin

Formal models are old in physics, epidemiology and neuroscience, where theories of force, contagion or neural firing have long been written as equations; Paul Smaldino used that contrast in a 2019 *Nature* column to argue that psychology's methodological reforms would fall short without better theory.[^s4] Frankenhuis, Panchanathan and Smaldino note that calls for theoretical rigour in psychology predate the replication crisis, citing Meehl among others, and that formalization has since become a popular answer to the crisis.[^s1] Two 2021 papers in *Perspectives on Psychological Science* gave the case its current shape: Guest and Martin argued that computational modeling forces researchers to specify intuitions that otherwise stay unexamined, which they call "open theory",[^s3] and Robinaugh and colleagues presented formal theory as a toolkit for building theories, not merely testing them.[^s2]

## How it works

Robinaugh and colleagues formalised a well-known verbal account of panic attacks, in which bodily arousal and perceived threat feed each other in a vicious cycle.[^s2] The prose theory seemed clear, but writing it as equations exposed choices it never made: is each effect linear or does it rise steeply after a threshold, and is there a calming feedback term? Of four versions they built, only one produced a panic-like surge after a small perturbation, so the verbal theory alone could not say which behaviour it predicted.[^s2] A workplace analogue: a team holds that "recognition boosts motivation, which boosts output". Turning that into a simple model forces answers to questions the slogan hides, such as whether the effect saturates and how quickly it fades, and each answer yields a different forecast that the data can then contradict.[^s2]

Formal modeling also helps diagnose a theory that fails. When a model's implied pattern departs from the data, the discrepancy can point to the core theory or to auxiliary assumptions about measurement, and because both are written down, either can be inspected and revised.[^s2] Guest and Martin describe scientific inference as a path in which each step, from framework to theory to specification to implementation to hypothesis to data, constrains the next, and modeling makes those steps explicit and transparent.[^s3]

## How to apply it

1. Write down the constructs and the relations between them, then state every assumption the prose leaves implicit.[^s1]
2. Express the relations in a precise form (equations, a simulation or logical rules) and derive what the theory implies, including what it rules out.[^s2]
3. Compare the theory-implied pattern with robust empirical findings; treat mismatches as guides for revision, and check whether the fault lies in the core theory or in auxiliary assumptions.[^s2]
4. Publish the model with annotation so that others can examine, adapt or criticise it.[^s2]

Frankenhuis and colleagues offer a check for theoretical transparency in which formalization is one of six questions, and they note that a formal model makes several of the others easier to satisfy, such as stating scope and deriving falsifiable predictions.[^s1]

## Evidence and limitations

The case for formal modeling is largely methodological argument with illustrative models rather than trials comparing fields that do and do not formalise. Smaldino links the higher replication rate of cognitive than social psychology in a large project that replicated 100 psychology studies to stronger theory, but presents this as his own interpretation.[^s4] Frankenhuis and colleagues call formal models no panacea: models built on questionable assumptions are of limited use, a clear verbal theory can sometimes do the job, and clarity is not the same as testability.[^s1] Robinaugh and colleagues warn that formal theory can intimidate readers without modeling training and so become harder to criticise, that a first model reproducing a desired result invites wishful over-interpretation, and that models are only as good as the empirical findings used to build them.[^s2]

## Connections

Frankenhuis, Panchanathan and Smaldino treat formal models that state a theory's meaning and scope as a main remedy for strategic ambiguity, the practice of keeping a claim vague enough to escape refutation.[^s1] The same paper describes the motte-and-bailey, in which a speaker switches between a bold and a modest version of a theory; once a model fixes which version is being claimed, that switching becomes visible, which is why the node counteracts it, at medium confidence because the authors address the tactic through strategic ambiguity in general.[^s1] Formal theory contrasts with verbal theory, whose natural-language statement can hide assumptions and contradictions.[^s2] Guest and Martin predict that without formal modeling psychology will keep facing replicability crises, and they argue that modeling adds to the benefits of preregistration rather than replacing it.[^s3] Making assumptions explicit also makes a theory easier to falsify, which ties formal modeling to falsifiability and to precise, operational definitions of terms.[^s1]

## Sources

[^s1]: Frankenhuis, Panchanathan & Smaldino, "Strategic Ambiguity in the Social Sciences", Social Psychological Bulletin 18, e9923 (2023). https://spb.psychopen.eu/index.php/spb/article/download/9923/9923.pdf (accessed 2026-11-16)
[^s2]: Robinaugh, Haslbeck, Ryan, Fried & Waldorp, "Invisible Hands and Fine Calipers: A Call to Use Formal Theory as a Toolkit for Theory Construction", Perspectives on Psychological Science 16(4), 725-743 (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8273080 (accessed 2026-11-16)
[^s3]: Guest & Martin, "How Computational Modeling Can Force Theory Building in Psychological Science", Perspectives on Psychological Science 16(4), 789-802 (2021). https://philarchive.org/rec/GUEHCM (accessed 2026-11-16)
[^s4]: Smaldino, "Better methods can't make up for mediocre theory", Nature 575, 9 (2019). https://media.nature.com/original/magazine-assets/d41586-019-03350-5/d41586-019-03350-5.pdf (accessed 2026-11-16)
