---
id: ct:ecological-rationality
type: Concept
title: Ecological rationality
aliases: [environment-relative rationality, mind-environment fit]
domain: heuristics-and-dual-process
summary: >-
  The view, developed by Gerd Gigerenzer, Peter Todd and the ABC Research
  Group, that a decision strategy is rational to the degree that it fits the
  information structure of the environment it is used in, so the same simple
  heuristic can be smart in one setting and error-prone in another.
level: intermediate
evidenceStatus: contested
broader: [ct:bounded-rationality]
related: [ct:fast-and-frugal-heuristics, ct:satisficing, ct:recognition-heuristic, ct:take-the-best, ct:overfitting, ct:heuristics-and-biases-program, ct:gerd-gigerenzer, ct:herbert-simon]
requires: [ct:bounded-rationality]
relations:
  - {predicate: introducedBy, object: ct:gerd-gigerenzer, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:peter-m-todd, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:herbert-simon, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:egon-brunswik, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:bias-variance-tradeoff, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:heuristics-and-biases-program, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:gigerenzer-brighton-2009-homo-heuristicus, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:hilbig-richter-2011-homo-heuristicus-outnumbered, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Environments that make us smart: Ecological rationality"
    publisher: Current Directions in Psychological Science 16(3), 167-171 (Todd & Gigerenzer, 2007), author's copy
    url: https://abcwest.cogs.indiana.edu/pmwiki/pdf/todd.currentdirections.2007.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Homo heuristicus: Why biased minds make better inferences"
    publisher: Topics in Cognitive Science 1, 107-143 (Gigerenzer & Brighton, 2009), course reading copy, UC Irvine
    url: https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Bounded Rationality"
    publisher: Stanford Encyclopedia of Philosophy (Wheeler, 2018; revised 2024)
    url: https://plato.stanford.edu/entries/bounded-rationality/
    type: scholarly-encyclopedia
    accessed: 2026-11-10
  - id: s4
    title: "Homo heuristicus outnumbered: Comment on Gigerenzer and Brighton (2009)"
    publisher: Topics in Cognitive Science 3 (Hilbig & Richter, 2011), authors' in-press copy, University of Würzburg
    url: https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/user_upload/Richter/hilbig_richter_inpress.pdf
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Ecological rationality

Ecological rationality is the idea that a way of deciding is not good or bad in itself but only relative to an environment: a strategy is rational to the extent that it exploits the way information is actually structured where it is used.[^s1] The question it asks of any heuristic is therefore not "does it obey logic or probability theory?" but "in which environments will it succeed, and in which will it fail?"[^s2] The concept has an explanatory side (how people with limited time and knowledge decide) and a normative side (which environments make a given rule work).[^s1]

## Origin

The framing was developed by Gerd Gigerenzer, Peter Todd and their colleagues at the Center for Adaptive Behavior and Cognition (ABC) at the Max Planck Institute for Human Development in Berlin, building on the group's 1999 book *Simple Heuristics That Make Us Smart*.[^s1] Its roots are older. Herbert Simon compared behaviour to a pair of scissors whose two blades are the mind and the environment; studying only the mental blade cannot explain how the scissors cut.[^s1] Egon Brunswik's lens model, in which an organism infers distant features of its world from imperfect nearby cues, supplied the second root, and philosophers now treat ecological rationality as one of the main strands of the broader bounded-rationality literature.[^s3]

## How it works

The analysis pairs a precisely specified rule with measurable features of an environment: how valid and how redundant the cues are, how unevenly their importance is distributed, how predictable the outcome is, and how much data a learner has.[^s1] Some fits identified by the program:

- When cue importance is very skewed, a one-reason rule such as Take The Best does well; when cues matter about equally, it does poorly and equal-weight tallying is better.[^s1]
- When outcomes are noisy and samples are small, simple rules can match or beat regression, neural networks and exemplar models at predicting *new* cases.[^s1][^s2]
- When options arrive one at a time and cannot be revisited, satisficing fits; when recognition correlates with size or success, the recognition heuristic fits.[^s1]

A workplace example: a hiring panel screening 300 applications for a sales role could weight 15 attributes in a scoring model, or shortlist on the two cues that have best predicted performance in past hires and stop there. Ecological rationality says neither choice is correct in the abstract. If one or two cues dominate and the panel has only a few dozen past hires to learn from, the short rule is likely to generalise better; if many small factors each matter, it will miss them.[^s1][^s2]

The same lens applies to environments people design. Todd and Gigerenzer report that only about 28% of Americans were potential organ donors against 99.9% of the French, a gap they attribute to opt-in versus opt-out defaults rather than to attitudes.[^s1] They also report that tennis novices' collective recognition picked 72% of Wimbledon 2003 men's winners versus 69% for expert ratings, a heuristic that works only because the best players tend to be the famous ones.[^s1]

## Evidence and limitations

The main formal argument rests on the bias-variance dilemma: prediction error combines a model's systematic bias with its variance across samples, so a deliberately biased but simple rule can beat a flexible, unbiased one when data are sparse.[^s2] Gigerenzer and Brighton reported that across 20 data sets from psychology, biology, sociology and economics, Take The Best was on average more accurate than regression and tallying while checking about 2.4 cues instead of about 7.7.[^s2] The Stanford Encyclopedia entry notes that this decomposition holds for squared-error loss and behaves differently under other loss functions, and that the word "bias" shifts meaning between statistics and psychology.[^s3]

The descriptive claim, that people actually pick the rule that suits their environment, is more contested. Hilbig and Richter reanalysed recognition data with a model that separates recognition use from use of other knowledge and estimated recognition use at about .80 rather than the .91 raw adherence rate; most individual participants did not behave like consistent one-reason users.[^s4] They also pointed out that the theory does not explain how people learn which environment they are in.[^s4] The originators acknowledge that the vocabulary for describing environments is still incomplete and that how strategies are selected remains an open question.[^s1] Because the normative "fit" result is well supported while the process claims are disputed, the status here is *contested*.

## How to apply it

Before trusting or rejecting a rule of thumb, ask what environment it is betting on: are a few cues dominant, is data scarce, is the future noisy? Test the rule on new cases, not on the past it was fitted to.[^s2] And when a heuristic fails, check whether the environment changed before concluding that the heuristic was irrational.[^s1]

## Connections

- Its parent is **bounded rationality**, and it is **influenced by** Herbert Simon's scissors image and by Egon Brunswik's lens model.[^s1][^s3]
- It was **introduced by** Gerd Gigerenzer and Peter Todd with the ABC Research Group and is **studied in** judgment and decision making.[^s1]
- It is **explained by** the bias-variance trade-off, which accounts for why simple rules can predict better, and **supported by** Gigerenzer and Brighton's 2009 *Homo heuristicus* comparisons.[^s2]
- It **contrasts with** the heuristics-and-biases program over which normative standard should judge human reasoning.[^s3]
- It is **challenged by** Hilbig and Richter's 2011 reanalysis of whether people actually use one-reason heuristics.[^s4]
- It is the evaluative standard behind fast-and-frugal heuristics, satisficing, the recognition heuristic and Take The Best, and is closely tied to the problem of overfitting.[^s1][^s2]

## Sources

[^s1]: Todd & Gigerenzer, "Environments that make us smart: Ecological rationality", *Current Directions in Psychological Science* 16(3), 2007. https://abcwest.cogs.indiana.edu/pmwiki/pdf/todd.currentdirections.2007.pdf (accessed 2026-11-10)
[^s2]: Gigerenzer & Brighton, "Homo heuristicus: Why biased minds make better inferences", *Topics in Cognitive Science* 1, 2009. https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf (accessed 2026-11-10)
[^s3]: Wheeler, "Bounded Rationality", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/bounded-rationality/ (accessed 2026-11-10)
[^s4]: Hilbig & Richter, "Homo heuristicus outnumbered: Comment on Gigerenzer and Brighton (2009)", *Topics in Cognitive Science* 3, 2011. https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/user_upload/Richter/hilbig_richter_inpress.pdf (accessed 2026-11-10)
