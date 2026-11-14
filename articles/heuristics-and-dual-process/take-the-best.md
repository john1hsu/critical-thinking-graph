---
id: ct:take-the-best
type: Heuristic
title: Take-the-best
aliases: [take the best heuristic, TTB heuristic]
domain: heuristics-and-dual-process
summary: >-
  A fast-and-frugal rule for deciding which of two options scores higher on a
  criterion: check cues one at a time in order of their validity, stop at the
  first cue that tells the options apart, and choose the option that cue
  favours, ignoring every remaining cue.
level: intermediate
evidenceStatus: contested
broader: [ct:fast-and-frugal-heuristics, ct:heuristic]
related: [ct:recognition-heuristic, ct:satisficing, ct:bounded-rationality, ct:overfitting, ct:herbert-simon]
requires: [ct:fast-and-frugal-heuristics]
relations:
  - {predicate: introducedBy, object: ct:gerd-gigerenzer, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:reasoning-the-fast-and-frugal-way, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:ecological-rationality, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:gigerenzer-brighton-2009-homo-heuristicus, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:newell-2005-re-visions-of-rationality, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Reasoning the fast and frugal way: Models of bounded rationality"
    publisher: Psychological Review 103(4), 650-669 (Gigerenzer & Goldstein, 1996), author's copy
    url: https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Challenging some common beliefs: Empirical work within the adaptive toolbox metaphor"
    publisher: Judgment and Decision Making 3(3), 205-214 (Bröder & Newell, 2008)
    url: https://dlab.sauder.ubc.ca/sjdm/journal/bn2/bn2.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Homo heuristicus: Why biased minds make better inferences"
    publisher: Topics in Cognitive Science 1, 107-143 (Gigerenzer & Brighton, 2009), course copy at UC Irvine
    url: https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Re-visions of rationality?"
    publisher: Trends in Cognitive Sciences (Newell, 2005), author's manuscript at UCL Discovery
    url: https://discovery-pp.ucl.ac.uk/14582/1/14582.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Bounded Rationality"
    publisher: Stanford Encyclopedia of Philosophy (Wheeler, 2018; rev. 2024)
    url: https://plato.stanford.edu/ENTRIES/bounded-rationality/
    type: scholarly-encyclopedia
    accessed: 2026-11-14
created: 2026-11-14
---

# Take-the-best

Take-the-best is a rule for paired comparisons, such as "which of these two cities is larger?" or "which of these two suppliers is more reliable?". Rather than weighing all the evidence, it looks at cues one at a time, starting with the cue that has most often pointed the right way, and decides on the first cue that distinguishes the two options.[^s1] Because a later cue can never overturn an earlier one, the rule is *noncompensatory*: it decides on one good reason instead of adding up many.[^s1][^s5]

## Origin

Gerd Gigerenzer and Daniel Goldstein, then at the Max Planck Institute for Psychological Research and the University of Chicago, introduced the algorithm in a 1996 *Psychological Review* paper titled "Reasoning the fast and frugal way".[^s1] It made Herbert Simon's bounded rationality precise: a satisficing procedure, specified step by step so it could be simulated, that stops searching once it can decide.[^s1] The paper launched the fast-and-frugal heuristics research program, and take-the-best became its most tested model.[^s3]

## How it works

The 1996 version has four steps.[^s1]

1. **Recognition:** if you recognise only one option, choose it; if you recognise neither, guess.
2. **Search:** otherwise, look up the best remaining cue, ranked by *validity* (how often that cue has picked the correct option when it discriminated).
3. **Stopping:** stop as soon as one option has a positive value on the cue and the other does not.
4. **Decision:** choose the option the cue favours; if no cue discriminates, guess.[^s1]

Workplace example: a team lead must choose between two contractors for a short job. Her cues, in the order they have predicted good outcomes in the past, are "has delivered for us before", "has a relevant certification" and "is the cheaper bid". Both contractors have worked for the team before, so that cue does not discriminate; only one holds the certification, so she stops there and picks that contractor, without weighing price at all. A weighted scoring sheet would combine all three cues and could let a big price gap override the certification.[^s1][^s3]

In the original test, the task was to judge which of the 83 German cities with more than 100,000 inhabitants was larger, using nine binary cues such as being a state capital or having a top-league soccer team.[^s1] Across 3,403 city pairs, take-the-best scored about 69% correct when all cue values were known, essentially level with multiple regression and weighted tallying, while looking up on average 5.9 cue values, under a third of the information the integration models used.[^s1] Variants that skip the validity ranking lost only about a point.[^s1]

## Evidence

The strongest support concerns *prediction*. In 20 data sets compiled by Czerlinski, Gigerenzer and Goldstein (1999), take-the-best made more accurate out-of-sample predictions than multiple regression on average while consulting about 2.4 cues against regression's 7.7.[^s3] Gigerenzer and Brighton (2009) explain this with the bias-variance trade-off: by ignoring dependencies between cues the rule estimates fewer parameters, so its predictions vary less from sample to sample, which matters most when data are sparse or noisy.[^s3] The Stanford Encyclopedia of Philosophy notes that the advantage over regression is clearest at small training samples.[^s5]

Whether people actually *use* the rule is more disputed. Reviewing a decade of experiments, Bröder and Newell (2008) found that strategy choice tracks payoffs (across 11 conditions, the share of take-the-best users correlated .83 with the rule's relative expected payoff) and that the rule became far more common when cues had to be retrieved from memory or information was costly.[^s2] Yet many participants still bought more information than the rule needs, kept old strategies after the environment changed, and showed an initial preference for compensatory, add-it-all-up deciding.[^s2] Newell (2005) concluded that only some people follow take-the-best some of the time, even in environments built to favour it, and proposed treating it as one setting of a single evidence-accumulation process rather than a separate tool.[^s4] Hence the *contested* status: the normative case that one-reason decisions can predict well is strong; the claim that minds default to them is not settled.[^s2][^s4]

## How to spot it

Look for a decision justified by a single decisive difference ("they're the only one with the certification") after earlier, more important criteria came out even. Signs of the rule are sequential checking of criteria, an early stop, and indifference to cues further down the list.[^s1][^s2] It is more likely when information is costly, held in memory rather than on a sheet, or needed quickly.[^s2]

## How to counter it

Take-the-best is not an error to be eliminated; the question is whether the environment suits it.[^s3] It does well when cue weights fall off steeply (each cue matters more than all later cues combined), when cues are redundant, and when data for estimating weights are thin.[^s3] It can do worse in compensatory environments, where several moderate cues jointly outweigh the top one, as when a large price gap should beat a small quality edge.[^s3] Before trusting a one-reason choice, check that your cue ranking comes from a real track record, ask whether lower cues could add up to override the first, and switch to a weighted comparison for high-stakes choices with plenty of reliable data.[^s2][^s3]

## Connections

- It is a narrower case of **fast-and-frugal heuristics** and of heuristics generally; its first step is the **recognition heuristic**.[^s1]
- It was **introduced by** Gerd Gigerenzer, with Daniel Goldstein, **in** "Reasoning the fast and frugal way" (1996), as a model of Herbert Simon's **bounded rationality** and **satisficing**.[^s1]
- Its accuracy is **explained by** **ecological rationality**: it succeeds when its simple structure fits the structure of the environment.[^s3]
- It is **supported by** Gigerenzer and Brighton's 2009 "Homo heuristicus" analysis, which ties its out-of-sample edge to reduced variance, the counterpart of **overfitting** in complex models.[^s3]
- It is **studied in** **judgment and decision making**, where strategy-classification experiments probe who uses it and when.[^s2]
- It is **challenged by** Newell's 2005 review, which found weak and individually variable evidence that people follow its search, stopping and decision rules.[^s4]

## Sources

[^s1]: Gigerenzer & Goldstein, "Reasoning the fast and frugal way: Models of bounded rationality", *Psychological Review* 103(4), 1996. https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf (accessed 2026-11-14)
[^s2]: Bröder & Newell, "Challenging some common beliefs: Empirical work within the adaptive toolbox metaphor", *Judgment and Decision Making* 3(3), 2008. https://dlab.sauder.ubc.ca/sjdm/journal/bn2/bn2.html (accessed 2026-11-14)
[^s3]: Gigerenzer & Brighton, "Homo heuristicus: Why biased minds make better inferences", *Topics in Cognitive Science* 1, 2009. https://sites.socsci.uci.edu/~lpearl/courses/readings/GigerenzerBrighton2009_HomoHeuristicus.pdf (accessed 2026-11-14)
[^s4]: Newell, "Re-visions of rationality?", *Trends in Cognitive Sciences*, 2005 (author's manuscript). https://discovery-pp.ucl.ac.uk/14582/1/14582.pdf (accessed 2026-11-14)
[^s5]: Wheeler, "Bounded Rationality", Stanford Encyclopedia of Philosophy, 2018 (rev. 2024). https://plato.stanford.edu/ENTRIES/bounded-rationality/ (accessed 2026-11-14)
