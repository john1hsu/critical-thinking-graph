---
id: ct:structured-analytic-techniques
type: Technique
title: Structured analytic techniques
aliases: [SATs, structured analytic technique, structured analytical techniques, analytic tradecraft techniques]
domain: decision-making
summary: >-
  A family of step-by-step procedures, developed mainly in US intelligence
  analysis, that externalise an analyst's reasoning (listing assumptions,
  laying evidence against rival hypotheses, arguing the other side, imagining
  alternative futures) so that mind-sets can be exposed and challenged; widely
  taught, but with thin and mixed evidence that they improve accuracy.
level: intermediate
evidenceStatus: contested
broader: [ct:debiasing]
related: [ct:tradecraft-primer, ct:key-assumptions-check, ct:analysis-of-competing-hypotheses, ct:devils-advocacy, ct:premortem, ct:sherman-kent, ct:groupthink, ct:calibration]
requires: [ct:cognitive-bias]
relations:
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s5, confidence: medium}
  - {predicate: introducedBy, object: ct:richards-heuer, source: s2, confidence: medium}
  - {predicate: introducedBy, object: ct:jack-davis, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:artner-girven-bruce-2016-rand-sat-assessment, source: s4, confidence: low}
  - {predicate: challengedBy, object: ct:mandel-tetlock-2018-correcting-judgment-correctives, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:mandel-karvetski-dhami-2018-ach-trial, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis"
    publisher: US Government, Central Intelligence Agency, Center for the Study of Intelligence (March 2009)
    url: https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf
    type: government
    accessed: 2026-11-07
  - id: s2
    title: "Boosting intelligence analysts' judgment accuracy: What works, what fails?"
    publisher: "Judgment and Decision Making 13(6), 607-621 (Mandel, Karvetski & Dhami, 2018)"
    url: https://cambridge.org/core/services/aop-cambridge-core/content/view/1530E9DAE8F42B2E8FC2B5FE374DB50F/S1930297500006628a.pdf/boosting-intelligence-analysts-judgment-accuracy-what-works-what-fails.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "Correcting Judgment Correctives in National Security Intelligence"
    publisher: Frontiers in Psychology 9, 2640 (Mandel & Tetlock, 2018)
    url: https://frontiersin.org/article/10.3389/fpsyg.2018.02640/full
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Assessing the Value of Structured Analytic Techniques in the U.S. Intelligence Community"
    publisher: RAND Corporation, RR-1408 (Artner, Girven & Bruce, 2016), report page
    url: https://www.rand.org/pubs/research_reports/RR1408.html
    type: institutional
    accessed: 2026-11-07
  - id: s5
    title: "Effects of task structure and confirmation bias in alternative hypotheses evaluation"
    publisher: "Cognitive Research: Principles and Implications 9, 37 (Dhami, Belton, De Werd, Hadzhieva & Wicke, 2024)"
    url: https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-024-00560-y.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s6
    title: "Improving the Analysis of Foreign Affairs: Evaluating Structured Analytic Techniques"
    publisher: "Stephen Coulthart, PhD dissertation, University of Pittsburgh (2015), D-Scholarship record"
    url: https://d-scholarship.pitt.edu/26055/
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Structured analytic techniques

Structured analytic techniques (SATs) are a toolkit of explicit, repeatable procedures for working through an analytic problem on paper or as a team instead of entirely in one's head. Their common aim is to drag an analyst's working model of a situation into the open, where its assumptions, evidence and blind spots can be inspected and argued over.[^s1] The US Government's 2009 primer on the subject frames them as aids for challenging judgments, surfacing mind-sets, sparking creativity and handling uncertainty, and is explicit that they do not guarantee a correct answer.[^s1]

## Origin

SATs grew out of US intelligence practice. Mandel, Karvetski and Dhami credit the former CIA analysts Richards Heuer and Jack Davis with introducing them, and note that the techniques began as optional tricks of the trade before intelligence reforms in the early 2000s pushed them into the centre of analytic training.[^s2] Heuer's 1999 *Psychology of Intelligence Analysis* supplied the psychological rationale and, as Dhami and colleagues describe, his analysis of competing hypotheses (ACH) was designed specifically to blunt confirmation bias.[^s5] The 2009 *Tradecraft Primer* then gathered a dozen core techniques into one short handbook, drawing on Heuer and on a 2004 Sherman Kent Center occasional paper; it notes that some techniques came from business and academia while others are peculiar to intelligence work.[^s1] Many intelligence services now train analysts in them.[^s5]

## How it works

The rationale is cognitive. Analysts face ambiguous, incomplete information and lean on mental models that help them notice what they expect, resist revising a view, and discount evidence that does not fit; the primer lists anchoring, availability and overconfidence among the resulting biases.[^s1] SATs interrupt that process by forcing each step into an external, checkable form. The primer sorts them into three groups: diagnostic techniques that make reasoning and gaps visible (key assumptions check, quality of information check, indicators of change, ACH); contrarian techniques that attack the prevailing view (devil's advocacy, Team A/Team B, high-impact/low-probability analysis, "what if?" analysis); and imaginative techniques that widen the space of possibilities (brainstorming, outside-in thinking, red team analysis, alternative futures).[^s1]

A workplace example: a product team has concluded that a recent rise in customer cancellations was caused by a price increase. A key assumptions check writes down what that story takes for granted (no competitor launched, the billing change did not create errors, the cancelling customers were price-sensitive). An ACH matrix then lists rival explanations (price, a buggy release, a competitor's promotion) as columns and scores each piece of evidence against all of them, so attention goes to the evidence that discriminates between hypotheses rather than evidence that fits the favoured one. Finally a "what if?" exercise asks what would have to be true for the buggy release to be the real cause, and which signposts would show it.[^s1]

## How to apply it

1. **Match the technique to the stage.** The primer suggests brainstorming, key assumptions checks, outside-in thinking and high-impact/low-probability analysis when a project starts; contrarian methods while hypotheses are forming; ACH and indicators throughout as information arrives; and a final re-check of assumptions, plus devil's advocacy if a consensus has gone long unchallenged, before the judgment is released.[^s1]
2. **Budget for the heavy ones.** Team A/Team B suits long-running, high-stakes disputes because it needs significant resources, and alternative futures analysis suits highly uncertain situations with serious consequences.[^s1]
3. **Record the outputs.** The payoff the primer promises is transparency: readers can see which assumptions, uncertainties and indicators would change the conclusion.[^s1]
4. **Don't stop at structure.** Mandel and Tetlock recommend pairing any technique with accuracy tracking and with statistical corrections such as recalibration and averaging several independent judgments.[^s3]

Pitfalls: Mandel and Tetlock argue that procedures leaving many judgment calls to the user (for instance, what counts as evidence "consistent" with a hypothesis in ACH) can add noise, and that warnings against overconfidence can tip analysts into underconfidence.[^s3]

## Evidence and limitations

The evidence base is thin and mixed, so the status here is contested. A RAND pilot study for the US Department of Defense found that the intelligence community promotes SATs heavily but has done little to test whether they improve quality; in its small sample, products that used SATs considered a wider range of outcomes, but the authors called their findings preliminary.[^s4] Coulthart's 2015 dissertation, which reviewed more than 2,000 studies on twelve core techniques, judged the support moderate to strong for only three: ACH, brainstorming and devil's advocacy.[^s6] Controlled trials of ACH are less encouraging. In a 2018 experiment with 50 UK intelligence analysts, those trained and required to use ACH were no more accurate than untrained controls and showed somewhat larger probability-coherence errors.[^s2] A 2024 pair of studies found that an ACH-style matrix did not reduce reliance on confirming evidence, whereas a matrix with hypotheses in rows did, and that most military analysts already weighed evidence on both sides.[^s5] Critics conclude that SATs were adopted largely on face validity and call for experimental testing before further rollout.[^s3]

## Connections

- **Applied in intelligence analysis.** The techniques were codified for, and are mainly taught to, intelligence analysts.[^s1]
- **Counteracts confirmation bias (contested).** ACH, the flagship technique, was built to counter confirmation bias, though recent trials question how well the standard matrix does so.[^s5]
- **Introduced by Richards Heuer and Jack Davis.** The JDM study credits both CIA veterans with introducing SATs.[^s2]
- **Supported by the RAND assessment (weakly).** RAND's pilot found SAT-based products explored more possible outcomes, while stressing that the evidence was preliminary.[^s4]
- **Challenged by Mandel and Tetlock (2018) and by the 2018 ACH trial.** The review argues SATs are untested and neglect noise; the trial found ACH training did not improve accuracy.[^s3] [^s2]
- **Broader: debiasing; related techniques.** SATs are a family of debiasing procedures whose members include the key assumptions check, ACH, devil's advocacy and the premortem; the primer itself is the canonical handbook.[^s1]

## Sources

[^s1]: US Government, *A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis* (CIA Center for the Study of Intelligence, March 2009). https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf (accessed 2026-11-07)
[^s2]: Mandel, Karvetski & Dhami, "Boosting intelligence analysts' judgment accuracy: What works, what fails?", *Judgment and Decision Making* 13(6), 607-621 (2018). https://cambridge.org/core/services/aop-cambridge-core/content/view/1530E9DAE8F42B2E8FC2B5FE374DB50F/S1930297500006628a.pdf/boosting-intelligence-analysts-judgment-accuracy-what-works-what-fails.pdf (accessed 2026-11-07)
[^s3]: Mandel & Tetlock, "Correcting Judgment Correctives in National Security Intelligence", *Frontiers in Psychology* 9, 2640 (2018). https://frontiersin.org/article/10.3389/fpsyg.2018.02640/full (accessed 2026-11-07)
[^s4]: Artner, Girven & Bruce, *Assessing the Value of Structured Analytic Techniques in the U.S. Intelligence Community*, RAND RR-1408 (2016). https://www.rand.org/pubs/research_reports/RR1408.html (accessed 2026-11-07)
[^s5]: Dhami, Belton, De Werd, Hadzhieva & Wicke, "Effects of task structure and confirmation bias in alternative hypotheses evaluation", *Cognitive Research: Principles and Implications* 9, 37 (2024). https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-024-00560-y.pdf (accessed 2026-11-07)
[^s6]: Coulthart, *Improving the Analysis of Foreign Affairs: Evaluating Structured Analytic Techniques*, PhD dissertation, University of Pittsburgh (2015). https://d-scholarship.pitt.edu/26055/ (accessed 2026-11-07)
