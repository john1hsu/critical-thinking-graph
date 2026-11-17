---
id: ct:peak-end-rule
type: Heuristic
title: Peak-end rule
aliases: [peak-end effect, peak-end heuristic]
domain: heuristics-and-dual-process
summary: >-
  The tendency to judge a past experience mainly by its most intense moment
  and by how it ended, roughly averaging the two, instead of summing or
  averaging every moment. Because length gets little weight, a longer episode
  with a milder ending can be remembered as better than a shorter one.
level: introductory
evidenceStatus: robust
broader: [ct:heuristic]
related: [ct:daniel-kahneman, ct:attribute-substitution, ct:affective-forecasting, ct:availability-heuristic, ct:prospect-theory]
requires: [ct:heuristic]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: produces, object: ct:duration-neglect, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:kahneman-1993-cold-water-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:redelmeier-katz-kahneman-2003-colonoscopy-trial, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:alaybek-2022-peak-end-meta-analysis, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "When More Pain Is Preferred to Less: Adding a Better End"
    publisher: Psychological Science 4(6), 401-405 (Kahneman, Fredrickson, Schreiber & Redelmeier, 1993), copy hosted by the University of Zurich
    url: https://ius.uzh.ch/dam/jcr:5ae9adc9-61ec-4174-b37c-4b752f36c23b/Kahnemann%20et%20al.%20-%20When%20More%20Pain%20is%20Preferred%20to%20Less%20(1993).pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Memories of colonoscopy: a randomized trial"
    publisher: Pain 104(1-2), 187-194 (Redelmeier, Katz & Kahneman, 2003), PubMed record
    url: https://pubmed.ncbi.nlm.nih.gov/12855328/
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "All's well that ends (and peaks) well? A meta-analysis of the peak-end rule and duration neglect"
    publisher: Organizational Behavior and Human Decision Processes 170, 104149 (Alaybek, Dalal, Fyffe et al., 2022), RePEc/IDEAS record
    url: https://ideas.repec.org/a/eee/jobhdp/v170y2022ics0749597822000334.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "A Meta-analysis of the Peak-End Rule and its Boundary Conditions (dissertation defense)"
    publisher: George Mason University, Industrial-Organizational Psychology program (Alaybek, 2020)
    url: https://io.gmu.edu/defenses/1259
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Peak-end rule

The peak-end rule describes how people summarize an experience after it is over. Instead of adding up or averaging every moment, the remembered judgment tracks roughly the average of the most intense moment (the peak) and the final moment (the end).[^s1] A companion pattern, duration neglect, follows from this: how long the episode lasted barely changes how good or bad it is remembered to be.[^s1][^s3] Kahneman and colleagues argued that this leads to choices that are plainly mistaken by the standard of the experience itself, such as preferring more pain to less.[^s1]

## Origin

The rule was named in work by Barbara Fredrickson and Daniel Kahneman on how people evaluate episodes, and was put to its sharpest test in a 1993 paper in *Psychological Science* by Kahneman, Fredrickson, Charles Schreiber and Donald Redelmeier.[^s1][^s3] The paper framed the result as a gap between what people live through and what they remember, and asked which of the two should guide choices such as medical treatment.[^s1]

## How it works

In the 1993 study, 32 students held one hand in 14 °C water for 60 seconds. On another trial they held the other hand in the same water for 60 seconds and then 30 seconds more while the temperature rose slightly, to about 15 °C. The longer trial contained all the pain of the shorter one plus extra discomfort, yet 22 of the 32 chose to repeat it; a replication with 37 people gave 24 of 37.[^s1] Both trials had the same peak, but the long one ended less painfully, so it was remembered as less bad. The authors stressed that participants knew which trial lasted longer; duration was available but simply received little weight.[^s1]

A workplace example: a team runs two all-day offsites. One is efficient but finishes with a tense budget argument; the other drags on an extra hour but closes with a relaxed dinner. In the post-event survey the longer, more tedious day may score higher, because people rate the ending and the best or worst moment, not the hours of slides. The meta-analysis authors use a workday as their own example of an episode judged this way.[^s3]

## Evidence

The effect has carried over to clinical settings. In a 2003 randomized trial, 682 colonoscopy patients were assigned either a normal procedure or one with a short extra interval at the end in which the scope stayed still. The extended group rated the final moments as less painful (1.7 versus 2.5 on a 10-point scale), the whole procedure as less unpleasant, and had higher odds of returning for a repeat colonoscopy over about five years of follow-up.[^s2]

The broadest test is a 2022 meta-analysis in *Organizational Behavior and Human Decision Processes* that pooled 174 effect sizes. It found a large peak-end effect on retrospective evaluations (r ≈ 0.58), robust across the boundary conditions tested, and a near-zero effect of total duration, supporting duration neglect.[^s3] The earlier dissertation version, covering 85 studies of peak effects and 95 of end effects, likewise reported a large effect that held across most demographic and methodological moderators.[^s4] Evidence status is therefore set to robust.

There are limits. The meta-analysis found the peak-end composite to be about as predictive as the overall average of moments, so it is not the only thing memory tracks.[^s3] The original authors noted that duration may matter when an episode runs far longer or shorter than expected, that the trend of an experience also shapes evaluations, and that beginnings can sometimes dominate.[^s1]

## How to spot it

- A retrospective rating ("How was the project?") is driven by one dramatic moment or the last week, not the whole period.[^s1][^s3]
- People prefer to repeat a longer, objectively worse option because it ended well.[^s1]
- Decisions about future experiences rely on memory of past ones, so whatever distorts memory distorts the choice.[^s2]

## How to counter it

When the total matters (workload, cumulative risk, a long negotiation), record moment-by-moment or periodic ratings during the experience rather than relying only on an end-of-period summary.[^s1][^s3] Ask explicitly how long a bad stretch lasted, since duration is known but neglected.[^s1] Conversely, designers of services and procedures can ethically use the rule, for instance by tapering discomfort at the end, while staying alert to the dilemma the original authors raised about adding experience only to improve memory.[^s1][^s2]

## Connections

- **Introduced by** Daniel Kahneman with Fredrickson and colleagues, in the 1993 cold-water study.[^s1]
- **Produces duration neglect**, the near-zero weight given to an episode's length in remembered evaluations.[^s1][^s3]
- **Demonstrated by** the 1993 cold-water experiment and by the 2003 randomized colonoscopy trial.[^s1][^s2]
- **Supported by** the 2022 meta-analysis of 174 effect sizes.[^s3]
- **Studied in** judgment and decision-making research on retrospective evaluation.[^s3]
- **Related to** attribute substitution (a summary is judged from a few accessible moments), the availability heuristic, affective forecasting and prospect theory, all part of Kahneman's program.[^s1]

## Sources

[^s1]: Kahneman, Fredrickson, Schreiber & Redelmeier, "When More Pain Is Preferred to Less: Adding a Better End", *Psychological Science* 4(6), 1993. https://ius.uzh.ch/dam/jcr:5ae9adc9-61ec-4174-b37c-4b752f36c23b/Kahnemann%20et%20al.%20-%20When%20More%20Pain%20is%20Preferred%20to%20Less%20(1993).pdf (accessed 2026-11-17)
[^s2]: Redelmeier, Katz & Kahneman, "Memories of colonoscopy: a randomized trial", *Pain* 104(1-2), 2003. https://pubmed.ncbi.nlm.nih.gov/12855328/ (accessed 2026-11-17)
[^s3]: Alaybek et al., "All's well that ends (and peaks) well? A meta-analysis of the peak-end rule and duration neglect", *Organizational Behavior and Human Decision Processes* 170, 2022. https://ideas.repec.org/a/eee/jobhdp/v170y2022ics0749597822000334.html (accessed 2026-11-17)
[^s4]: Alaybek, "A Meta-analysis of the Peak-End Rule and its Boundary Conditions", George Mason University dissertation defense, 2020. https://io.gmu.edu/defenses/1259 (accessed 2026-11-17)
