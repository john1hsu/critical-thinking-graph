---
id: ct:anchoring-effect
type: CognitiveBias
title: Anchoring effect
aliases: [anchoring bias, anchoring, anchoring and adjustment bias]
domain: cognitive-biases
summary: >-
  The tendency for a numerical estimate or judgment to be pulled toward a
  previously encountered value (the anchor), even when that value is
  uninformative or plainly arbitrary.
level: introductory
evidenceStatus: robust
broader: [ct:cognitive-bias]
related: [ct:heuristics-and-biases-program, ct:consider-the-opposite]
requires: []
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:anchoring-and-adjustment-heuristic, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:selective-accessibility-model, source: s4, confidence: medium}
  - {predicate: demonstratedBy, object: ct:englich-2006-judicial-anchoring-study, source: s4, confidence: high}
  - {predicate: supportedBy, object: ct:many-labs-1-replication-project, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:roseler-2025-insufficient-adjustment-test, source: s5, confidence: medium}
sources:
  - id: s1
    title: "Judgment under Uncertainty: Heuristics and Biases"
    publisher: Science 185(4157), 1124-1131 (Tversky & Kahneman, 1974), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/17835457/
    type: primary
    accessed: 2026-11-03
  - id: s2
    title: "A literature review of the anchoring effect"
    publisher: Journal of Socio-Economics 40(1), 35-42 (Furnham & Boo, 2011), RePEc record
    url: https://ideas.repec.org/a/eee/soceco/v40y2011i1p35-42.html
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s3
    title: "Investigating variation in replicability: A \"many labs\" replication project"
    publisher: Social Psychology 45(3), 142-152 (Klein et al., 2014), Penn State research portal
    url: https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s4
    title: "Playing Dice With Criminal Sentences: The Influence of Irrelevant Anchors on Experts' Judicial Decision Making"
    publisher: Personality and Social Psychology Bulletin 32, 188-200 (Englich, Mussweiler & Strack, 2006)
    url: https://journals.sagepub.com/doi/abs/10.1177/0146167205282152
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Falsifying the Insufficient Adjustment Model: No Evidence for Unidirectional Adjustment from Anchors"
    publisher: Meta-Psychology 9 (Röseler, Incerti, Rebholz, Seida & Papenmeier, 2025)
    url: https://open.lnu.se/index.php/metapsychology/article/view/4137/4300
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s6
    title: "Measures of Anchoring in Estimation Tasks (replication record)"
    publisher: FORRT Replication Atlas
    url: https://forrt.org/flora-replication-atlas/doi/10.1177/01461672952111004/
    type: community
    accessed: 2026-11-03
created: 2026-11-03
---

# Anchoring effect

The anchoring effect is the tendency for a numerical judgment to drift toward a number a person has just seen or considered, called the anchor. Estimates of prices, durations, probabilities or quantities end up closer to the anchor than they would otherwise be, and this happens even when the anchor is obviously irrelevant to the question.[^s1][^s2] Furnham and Boo's 2011 review describes it as one of the most robust effects in judgment research and catalogues its appearance across a wide range of tasks and domains.[^s2]

## Origin

Amos Tversky and Daniel Kahneman introduced the idea in their 1974 *Science* article on judgment under uncertainty. They proposed three heuristics that people use when they cannot calculate an answer: representativeness, availability, and adjustment from an anchor. The third is used for numerical predictions when some starting value is at hand, and like the others it is usually economical but produces systematic, predictable errors.[^s1] On their account, people start from the anchor and adjust away from it, but stop too soon, so the final estimate stays biased toward the starting point.[^s1]

## How it works

A typical experiment asks a comparative question first (is a given river longer or shorter than some stated length?) and then an absolute one (how long is it?). People given a high anchor give higher estimates than people given a low one.[^s5] The anchor does not have to be plausible or even meaningful. In a set of four studies, experienced judges and legal experts reading a case file moved their sentences toward a prosecutor's sentencing demand even when they were told the demand had been chosen at random, and even when they produced it themselves by rolling dice.[^s4]

A workplace version is a salary or budget negotiation. If the first figure on the table is a high asking price, the counter-offer and the final settlement tend to land closer to it than an independent valuation would suggest. The same pull operates when a project lead reuses last year's estimate as the starting point for this year's, or when a list price frames what counts as a discount.[^s2]

## Evidence

The core effect has held up under large-scale replication. The first Many Labs project, published in 2014, re-ran 13 classic and newer effects in 36 samples with 6,344 participants; ten replicated consistently.[^s3] Its anchoring items, taken from Jacowitz and Kahneman's 1995 estimation study, are recorded as a successful replication.[^s6][^s3] Furnham and Boo's review reports that mood, motivation, knowledge, ability and personality can moderate the size of the effect, but not eliminate it.[^s2] Englich and colleagues found that expertise and experience gave judges no protection.[^s4]

What is disputed is the mechanism, and how far the effect generalises beyond its classic format. In four preregistered studies (N = 898), Röseler and colleagues found that limiting the time people had to adjust did not strengthen anchoring, which the insufficient-adjustment account predicts it should. They argued that this account, at least in its current one-directional form, should be dropped. Their pooled estimate across paradigms also showed large heterogeneity: anchoring was large in classic open-ended numerical estimates but vanished, or even reversed into a contrast effect, in visual-scale and two-choice designs.[^s5] A competing account, selective accessibility, holds that considering the anchor makes anchor-consistent information easier to retrieve. Englich and colleagues found that high anchors made incriminating arguments more accessible to the judges in their study.[^s4]

## How to spot it

- A first number has been stated (an asking price, a prior forecast, a default value in a form) before you formed your own estimate.[^s2]
- Your estimate feels like an adjustment from that number rather than something built up from independent evidence.[^s1]
- The number came from a source with no bearing on the question, such as a random draw, an unrelated figure or an opposing negotiator.[^s4]

## How to counter it

The selective-accessibility finding suggests a practical remedy. If an anchor works by making anchor-consistent reasons easier to recall, then deliberately listing reasons why the true value might be far from the anchor should help offset that pull.[^s4] In practice that means writing down your own estimate before you see anyone else's figure, building estimates from base rates or comparable cases rather than from the number on the table, and in groups collecting estimates independently before discussing them. Because expertise alone does not protect people from anchoring, these steps matter as much for specialists as for novices.[^s4][^s2]

## Connections

- **Introduced by** Tversky and Kahneman in the 1974 *Science* paper that launched the heuristics-and-biases program, and **explained by** their anchoring-and-adjustment heuristic.[^s1]
- **Explained by** the selective-accessibility model, which locates the effect in biased retrieval of anchor-consistent evidence.[^s4]
- **Demonstrated by** Englich, Mussweiler and Strack's 2006 studies of judicial sentencing with arbitrary anchors.[^s4]
- **Supported by** the 2014 Many Labs multi-site replication project.[^s3]
- **Challenged by** Röseler and colleagues' 2025 preregistered tests, which question the insufficient-adjustment mechanism rather than the existence of the effect.[^s5]
- **Related to** consider-the-opposite, a debiasing technique aimed at the retrieval process that selective accessibility describes.[^s4]

## Sources

[^s1]: Tversky & Kahneman, "Judgment under Uncertainty: Heuristics and Biases", *Science* 185 (1974). https://pubmed.ncbi.nlm.nih.gov/17835457/ (accessed 2026-11-03)
[^s2]: Furnham & Boo, "A literature review of the anchoring effect", *Journal of Socio-Economics* 40 (2011). https://ideas.repec.org/a/eee/soceco/v40y2011i1p35-42.html (accessed 2026-11-03)
[^s3]: Klein et al., "Investigating variation in replicability: A 'many labs' replication project", *Social Psychology* 45 (2014). https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/ (accessed 2026-11-03)
[^s4]: Englich, Mussweiler & Strack, "Playing Dice With Criminal Sentences", *Personality and Social Psychology Bulletin* 32 (2006). https://journals.sagepub.com/doi/abs/10.1177/0146167205282152 (accessed 2026-11-03)
[^s5]: Röseler et al., "Falsifying the Insufficient Adjustment Model", *Meta-Psychology* 9 (2025). https://open.lnu.se/index.php/metapsychology/article/view/4137/4300 (accessed 2026-11-03)
[^s6]: FORRT Replication Atlas, record for Jacowitz & Kahneman (1995), "Measures of Anchoring in Estimation Tasks". https://forrt.org/flora-replication-atlas/doi/10.1177/01461672952111004/ (accessed 2026-11-03)
