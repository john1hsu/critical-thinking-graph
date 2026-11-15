---
id: ct:anchoring-and-adjustment-heuristic
type: Heuristic
title: Anchoring-and-adjustment heuristic
aliases: [adjustment and anchoring, insufficient adjustment model, anchor-and-adjust strategy]
domain: heuristics-and-dual-process
summary: >-
  The estimation strategy of starting from an initial value that is at hand
  (an anchor) and adjusting it step by step toward a plausible answer, which
  tends to stop too early and leave the final estimate biased toward the
  starting point.
level: intermediate
evidenceStatus: contested
broader: [ct:heuristic]
related: [ct:heuristics-and-biases-program, ct:availability-heuristic, ct:representativeness-heuristic, ct:bounded-rationality, ct:satisficing, ct:consider-the-opposite, ct:calibration]
requires: [ct:heuristics-and-biases-program]
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:judgment-under-uncertainty-heuristics-and-biases, source: s1, confidence: medium}
  - {predicate: produces, object: ct:anchoring-effect, source: s1, confidence: high}
  - {predicate: produces, object: ct:overconfidence-effect, source: s1, confidence: medium}
  - {predicate: demonstratedBy, object: ct:epley-gilovich-2001-self-generated-anchor-studies, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:selective-accessibility-model, source: s4, confidence: medium}
  - {predicate: explainedBy, object: ct:resource-rational-analysis, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:roseler-2025-insufficient-adjustment-test, source: s6, confidence: high}
  - {predicate: challengedBy, object: ct:roseler-2024-epley-gilovich-replication, source: s7, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Judgment under Uncertainty: Heuristics and Biases"
    publisher: Science 185(4157), 1124-1131 (Tversky & Kahneman, 1974), copy hosted by the University of Washington Department of Statistics
    url: https://sites.stat.washington.edu/peter/498.Sp16/Tversky.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Putting Adjustment Back in the Anchoring and Adjustment Heuristic: Differential Processing of Self-Generated and Experimenter-Provided Anchors"
    publisher: Psychological Science (Epley & Gilovich, 2001), Association for Psychological Science
    url: https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00372/
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "The Anchoring-and-Adjustment Heuristic: Why the Adjustments Are Insufficient"
    publisher: Psychological Science 17(4), 311-318 (Epley & Gilovich, 2006), Association for Psychological Science
    url: https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01704.x/
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "The Effect of Accuracy Motivation on Anchoring and Adjustment: Do People Adjust from Provided Anchors?"
    publisher: Journal of Personality and Social Psychology 99(6), 917-932 (Simmons, LeBoeuf & Nelson, 2010), author copy at Wharton
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Simmons-et-al.-2010.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "The anchoring bias reflects rational use of cognitive resources"
    publisher: Psychonomic Bulletin & Review 25(1), 322-349 (Lieder, Griffiths, Huys & Goodman, 2018), Princeton University research portal
    url: https://collaborate.princeton.edu/en/publications/the-anchoring-bias-reflects-rational-use-of-cognitive-resources/
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Falsifying the Insufficient Adjustment Model: No Evidence for Unidirectional Adjustment from Anchors"
    publisher: Meta-Psychology 9 (Röseler, Incerti, Rebholz, Seida & Papenmeier, 2025)
    url: https://open.lnu.se/index.php/metapsychology/article/view/4137/4300
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s7
    title: "Need for Cognition, Cognitive Load, and Forewarning do not Moderate Anchoring Effects: A Replication Study of Epley & Gilovich"
    publisher: Journal of Comments and Replications in Economics 3, 1-42 (Röseler et al., 2024), RePEc/IDEAS record
    url: https://ideas.repec.org/a/zbw/jcreco/304381.html
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Anchoring-and-adjustment heuristic

The anchoring-and-adjustment heuristic is a strategy for estimating an uncertain quantity: take a starting value that is already at hand, then move away from it until the answer seems reasonable. Tversky and Kahneman proposed that people estimate this way when they cannot calculate, and that the adjustment is typically too small, so the final answer stays biased toward where it began.[^s1] This article is about the proposed *process*. The resulting pull toward a prior number, the anchoring effect, is a separate node; the process is one of several rival explanations for it.[^s1][^s4]

## Origin

The heuristic was one of three that Amos Tversky and Daniel Kahneman set out in their 1974 *Science* paper on judgment under uncertainty, alongside representativeness and availability.[^s1] They argued that the starting point can come from how a problem is worded or from a partial calculation, and that different starting points produce different estimates. Their classic illustration had students spend five seconds estimating the product of the numbers 1 to 8. Those shown the descending sequence (8 × 7 × … × 1) gave a median of 2,250, those shown the ascending one gave 512, and the true value is 40,320. On their account, people multiply the first few terms and extrapolate, so the larger early products in the descending order give a higher, but still far too low, starting point.[^s1]

## How it works

The heuristic is a stepwise search. Begin at the anchor, ask whether the value is plausible, and keep moving if it is not. Epley and Gilovich's 2006 studies found that people stop as soon as they reach the edge of the range of values they find plausible, not its centre, which is why the adjustment falls short.[^s3]

A workplace example: a project manager asked how long a migration will take recalls that last year's similar job took eight weeks. She reasons that this one is larger, so "a bit more", and settles on ten weeks because ten no longer seems implausible. She never builds an estimate from the task list. If the job really needs sixteen weeks, ten is the first value she found acceptable, not her best estimate. Tversky and Kahneman added that anchoring on a single step's success rate makes people overrate the chance that a multi-step plan will go smoothly, and makes experts' confidence intervals too narrow.[^s1]

## Evidence

By 2001 the prevailing view doubted that adjustment explained anchoring at all. Experimenter-supplied anchors appeared to work instead by making anchor-consistent information more accessible.[^s2] Epley and Gilovich argued in 2001 that the answer depends on where the anchor comes from. When people generated their own anchor, their think-aloud reports described adjusting. Nodding the head, which encourages accepting values, kept their estimates closer to the anchor than shaking it, but only for self-generated anchors.[^s2] Their 2006 follow-ups added that people adjust further when they are able and willing to keep searching.[^s3]

Simmons, LeBoeuf and Nelson qualified this split in 2010. People do adjust effortfully from provided anchors too, but they are often unsure which way to move. Accuracy incentives pushed estimates further from the anchor only when the direction was clear, and could pull them back when it was not. The authors concluded that adjustment and selective accessibility are complementary, not competing, explanations.[^s4] Lieder and colleagues (2018) then recast the heuristic as a rational use of limited time. If each adjustment step costs time or effort, stopping early can be the best trade-off, and their model accounted for ten anchoring phenomena.[^s5]

The process account has not held up well in recent preregistered tests. A 2024 replication of three Epley and Gilovich studies (N = 657) still found robust anchoring, but need for cognition, cognitive load and forewarning made no difference to it with either kind of anchor.[^s7] In four 2025 studies (N = 898), limiting adjustment time did not make anchoring stronger, which a simple insufficient-adjustment model predicts. In one paradigm people even overshot, which suggests adjustment can run in both directions. The authors called for that version of the model to be abandoned or revised.[^s6] The anchoring effect is well established; this heuristic's account of *why* it happens remains contested.[^s6][^s7]

## How to spot it

- Your estimate began as "the last figure, plus or minus a bit" rather than being built from components or comparable cases.[^s1]
- You stopped when the number first felt acceptable, without asking what the most likely value is.[^s3]
- The starting value came from the wording of the question, a partial calculation, or a figure someone else mentioned.[^s1]

## How to counter it

Because adjustment stops at the first plausible value, keep going on purpose: ask whether the answer could be further still, and estimate the far end of the plausible range before choosing a point inside it.[^s3] Settle the *direction* of the error first. Incentives and effort only help once you know which way the truth lies.[^s4] Better still, skip the anchor by working from a task breakdown or a set of similar past cases, and set interval estimates wider than feels natural.[^s1] Listing reasons why the anchor may be wrong targets the accessibility route, which works alongside adjustment.[^s4]

## Connections

- **Introduced by** Amos Tversky and Daniel Kahneman, **in** the 1974 *Science* paper on judgment under uncertainty, where it also **produces** the anchoring effect and contributes to over-narrow confidence intervals, a form of the overconfidence effect.[^s1]
- **Demonstrated by** Epley and Gilovich's 2001 studies of self-generated anchors, which brought adjustment back as a live mechanism.[^s2]
- **Contrasts with** the selective-accessibility model; Simmons and colleagues treat the two as complementary.[^s4]
- **Explained by** resource-rational analysis, which presents early stopping as an efficient use of limited cognitive resources and links the heuristic to bounded rationality.[^s5]
- **Challenged by** Röseler and colleagues' 2024 moderator replications and their 2025 preregistered time-pressure tests.[^s7][^s6]

## Sources

[^s1]: Tversky & Kahneman, "Judgment under Uncertainty: Heuristics and Biases", *Science* 185 (1974). https://sites.stat.washington.edu/peter/498.Sp16/Tversky.pdf (accessed 2026-11-15)
[^s2]: Epley & Gilovich, "Putting Adjustment Back in the Anchoring and Adjustment Heuristic", *Psychological Science* (2001). https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00372/ (accessed 2026-11-15)
[^s3]: Epley & Gilovich, "The Anchoring-and-Adjustment Heuristic: Why the Adjustments Are Insufficient", *Psychological Science* 17 (2006). https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01704.x/ (accessed 2026-11-15)
[^s4]: Simmons, LeBoeuf & Nelson, "The Effect of Accuracy Motivation on Anchoring and Adjustment", *Journal of Personality and Social Psychology* 99 (2010). https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Simmons-et-al.-2010.pdf (accessed 2026-11-15)
[^s5]: Lieder, Griffiths, Huys & Goodman, "The anchoring bias reflects rational use of cognitive resources", *Psychonomic Bulletin & Review* 25 (2018). https://collaborate.princeton.edu/en/publications/the-anchoring-bias-reflects-rational-use-of-cognitive-resources/ (accessed 2026-11-15)
[^s6]: Röseler et al., "Falsifying the Insufficient Adjustment Model", *Meta-Psychology* 9 (2025). https://open.lnu.se/index.php/metapsychology/article/view/4137/4300 (accessed 2026-11-15)
[^s7]: Röseler et al., "Need for Cognition, Cognitive Load, and Forewarning do not Moderate Anchoring Effects", *Journal of Comments and Replications in Economics* 3 (2024). https://ideas.repec.org/a/zbw/jcreco/304381.html (accessed 2026-11-15)
