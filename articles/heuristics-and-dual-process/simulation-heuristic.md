---
id: ct:simulation-heuristic
type: Heuristic
title: Simulation heuristic
aliases: [mental simulation heuristic]
domain: heuristics-and-dual-process
summary: >-
  The tendency to judge how likely an outcome is, or how close it came to
  happening, by how easily one can mentally construct a scenario that leads to
  it or undoes it. Outcomes that are easy to imagine otherwise feel nearer,
  more probable and more emotionally charged.
level: intermediate
evidenceStatus: robust
broader: [ct:heuristic]
related: [ct:availability-heuristic, ct:counterfactual-thinking, ct:norm-theory, ct:hindsight-bias, ct:premortem, ct:heuristics-and-biases-program, ct:daniel-kahneman, ct:amos-tversky]
requires: [ct:heuristic, ct:availability-heuristic]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:judgment-under-uncertainty, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:availability-heuristic, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:kutscher-feldman-2019-exceptionality-replication, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The simulation heuristic"
    publisher: "Kahneman & Tversky, in Kahneman, Slovic & Tversky (eds.), Judgment under Uncertainty: Heuristics and Biases, ch. 14, pp. 201-208, Cambridge University Press, 1982 (doi:10.1017/CBO9780511809477.015)"
    url: https://www.cambridge.org/core/books/judgment-under-uncertainty/simulation-heuristic/9C6ED91A6429A8443641641DC41A52FE
    type: primary
    accessed: 2026-11-21
  - id: s2
    title: "The Functional Theory of Counterfactual Thinking"
    publisher: "Personality and Social Psychology Review 12(2), 168-192 (Epstude & Roese, 2008), PMC author manuscript"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2408534
    type: peer-reviewed
    accessed: 2026-11-21
  - id: s3
    title: "The impact of past behaviour normality on regret: replication and extension of three experiments of the exceptionality effect"
    publisher: "Cognition and Emotion 33(5), 901-914 (Kutscher & Feldman, 2019; doi:10.1080/02699931.2018.1504747), PhilArchive copy"
    url: https://philarchive.org/archive/KUTTIO-2
    type: peer-reviewed
    accessed: 2026-11-21
created: 2026-11-21
---

# Simulation heuristic

The simulation heuristic is the habit of answering questions about likelihood, causation and "near misses" by running a quick mental model of the situation and noticing how easily it produces one outcome rather than another.[^s1] If it is easy to imagine a scenario in which things turned out differently, the actual outcome feels fragile, the alternative feels close, and feelings such as frustration or regret grow stronger.[^s1][^s2]

## Origin

Daniel Kahneman and Amos Tversky proposed the heuristic in a short chapter of the 1982 volume *Judgment under Uncertainty: Heuristics and Biases*.[^s1] They presented it as an extension of their 1973 availability heuristic: availability concerned how easily past *instances* are retrieved from memory, whereas many judgments depend on how easily new *examples or scenarios* can be constructed, a process they argued had been neglected.[^s1] Their idea was that people consult something like a simulation model, and its output is an assessment of how readily the model generates different outcomes.[^s1] Kahneman and Dale Miller later developed the idea into norm theory (1986), which explains which features of a situation people tend to mentally "undo".[^s2][^s3]

## How it works

The mental model is cheap, so its outputs are shaped by how *mutable* the imagined facts are, not by their actual probability. Norm theory holds that unusual or exceptional events invite "if only" thoughts that restore the normal state of affairs, while routine events are rarely undone.[^s2][^s3] The classic illustration, discussed by Epstude and Roese, is a motorist injured on an atypical route home: people readily imagine "if only he had taken his usual road", and judge his misfortune as more avoidable and regrettable than an identical accident on his usual route.[^s2]

A workplace example: two teams both miss a client deadline by one day. Team A was delayed by a single late approval that a manager could easily have signed earlier; Team B was delayed by a slow, steady slippage across every task. Reviewers tend to feel Team A "almost made it" and that its failure was more avoidable, even though both teams missed by the same margin, because one vivid alternative is easy to simulate for A and hard to construct for B. The judgment of closeness and blame then tracks ease of imagining, not the underlying process.[^s1][^s2]

Counterfactuals come in two directions. *Upward* counterfactuals imagine a better outcome and, when they focus on one's own choices, produce regret; *downward* counterfactuals imagine a worse outcome and tend to produce relief.[^s2]

## Evidence

The original chapter offered vignette demonstrations rather than a large experimental programme, and its core claim is a theoretical account of how scenario construction feeds judgment.[^s1] The best-tested derived prediction is the exceptionality effect from norm theory. In a pre-registered replication with two online samples of 342 participants each (2018-2019), Kutscher and Feldman reproduced Kahneman and Miller's hitchhiker and car-accident scenarios: roughly 92% and 81% of participants judged the person whose outcome followed an exceptional action as more regretful, matching or exceeding the original effects.[^s3] A related prediction did not hold: Miller and McFarland's finding that victims of exceptional circumstances are awarded more compensation failed to replicate (effects near zero), although the same victims were still judged to feel more regret.[^s3] The emotional and "closeness" effects therefore look robust, while downstream effects on consequential judgments such as compensation are weaker than first reported.

Later research has also reframed counterfactual simulation as often useful rather than only a bias. Epstude and Roese's functional theory argues that upward counterfactuals sit in a regulatory loop after a failed goal and can raise intentions to perform better next time.[^s2]

## How to spot it

Watch for reasoning that leans on how *easily* a different ending can be pictured: "it was so close", "if only one thing had been different", or blame that concentrates on a single unusual step.[^s2] Be suspicious when a vivid, easily undone event attracts most of the explanation, or when a forecast feels likely only because a story about it is easy to tell.[^s1]

## How to counter it

- Ask what the base rate or measured margin actually was, independently of how easy the alternative is to imagine.[^s1]
- Deliberately simulate the hard-to-imagine alternatives too: for routine, diffuse causes, list several ways the outcome could have been avoided.[^s2]
- Use upward counterfactuals for their functional value: convert "if only" into a concrete plan for next time rather than a verdict of blame.[^s2]
- When judging others, check whether an outcome is being treated as more avoidable merely because it followed an unusual action.[^s3]

## Connections

The heuristic is a sibling and extension of the **availability heuristic**: both rely on ease of bringing something to mind, but the simulation heuristic concerns constructing scenarios rather than retrieving instances.[^s1] It was **introduced by** Kahneman and Tversky in *Judgment under Uncertainty*, part of the **heuristics and biases program**.[^s1] It grounds research on **counterfactual thinking** and **norm theory**, now studied within **judgment and decision making** and social psychology.[^s2] Its exceptionality predictions are **supported by** Kutscher and Feldman's pre-registered replication.[^s3] Techniques such as the **premortem** harness deliberate simulation of failure, and **hindsight bias** is a neighbouring distortion in how past outcomes are judged.

## Sources

[^s1]: Kahneman & Tversky, "The simulation heuristic", in *Judgment under Uncertainty: Heuristics and Biases*, Cambridge University Press, 1982. https://www.cambridge.org/core/books/judgment-under-uncertainty/simulation-heuristic/9C6ED91A6429A8443641641DC41A52FE (accessed 2026-11-21)
[^s2]: Epstude & Roese, "The Functional Theory of Counterfactual Thinking", *Personality and Social Psychology Review*, 2008. https://pmc.ncbi.nlm.nih.gov/articles/PMC2408534 (accessed 2026-11-21)
[^s3]: Kutscher & Feldman, "The impact of past behaviour normality on regret", *Cognition and Emotion*, 2019. https://philarchive.org/archive/KUTTIO-2 (accessed 2026-11-21)
