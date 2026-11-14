---
id: ct:delphi-method
type: Method
title: Delphi method
aliases: [Delphi technique, Delphi process, Delphi study, Delphi survey, modified Delphi, e-Delphi]
domain: decision-making
summary: >-
  A structured way to elicit and combine expert judgment in which a panel
  answers questionnaires anonymously over several rounds, receiving a
  facilitator's summary of the group's answers and reasons between rounds,
  until the estimates stabilise and are aggregated statistically.
level: intermediate
evidenceStatus: mixed
broader: [ct:expert-elicitation, ct:group-decision-making]
related: [ct:delphi-report-on-critical-thinking, ct:structured-analytic-techniques, ct:argument-from-expert-opinion, ct:anchoring-effect, ct:intelligence-analysis]
requires: [ct:judgment-and-decision-making]
relations:
  - {predicate: introducedBy, object: ct:olaf-helmer, source: s5, confidence: high}
  - {predicate: introducedBy, object: ct:norman-dalkey, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:groupthink, source: s4, confidence: medium}
  - {predicate: counteracts, object: ct:bandwagon-effect, source: s6, confidence: medium}
  - {predicate: contrastsWith, object: ct:nominal-group-technique, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:wisdom-of-crowds, source: s3, confidence: medium}
  - {predicate: appliedIn, object: ct:forecasting, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:medicine, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "An Experimental Application of the DELPHI Method to the Use of Experts"
    publisher: Management Science 9(3), 458-467 (Dalkey & Helmer, 1963), record on RePEc/IDEAS
    url: https://ideas.repec.org/a/inm/ormnsc/v9y1963i3p458-467.html
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Expert Opinions in Forecasting: The Role of the Delphi Technique"
    publisher: In J. S. Armstrong (ed.), Principles of Forecasting, Kluwer, pp. 125-144 (Rowe & Wright, 2001), author's chapter copy hosted on gwern.net
    url: https://Www.Gwern.net/doc/statistics/prediction/2001-rowe.pdf
    type: textbook
    accessed: 2026-11-14
  - id: s3
    title: "Forecasting: Principles and Practice (2nd ed.), section 4.3 The Delphi method"
    publisher: OTexts (Hyndman & Athanasopoulos, 2018)
    url: https://otexts.com/fpp2/delphimethod.html
    type: textbook
    accessed: 2026-11-14
  - id: s4
    title: "Delphi methodology in healthcare research: How to decide its appropriateness"
    publisher: World Journal of Methodology 11(4), 116-129 (Nasa, Jain & Juneja, 2021)
    url: https://www.wjgnet.com/2222-0682/full/v11/i4/116.htm?s=qc
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Norman C. Dalkey oversees a Delphi Experiment"
    publisher: INFORMS, History of O.R. Excellence (RAND Corporation slideshow)
    url: https://informs.org/Explore/History-of-O.R.-Excellence/Non-Academic-Institutions/RAND-Corporation/RAND-Slideshow/Norman-C.-Dalkey-oversees-a-Delphi-Experiment
    type: institutional
    accessed: 2026-11-14
  - id: s6
    title: "Group Judgment Technology: Project Scope and Research Plan (CCBS-TM-2)"
    publisher: ARPA-sponsored research plan (Shure & Dalkey, c. 1972), Defense Technical Information Center
    url: https://apps.dtic.mil/sti/pdfs/AD0741668.pdf
    type: government
    accessed: 2026-11-14
created: 2026-11-14
---

# Delphi method

The Delphi method is a procedure for getting a usable group judgment out of a panel of experts without putting them in the same room. A facilitator sends the panel a questionnaire, collects the answers and the reasons behind them, summarises the spread of opinion, and sends the summary back for a revised answer; the cycle repeats until answers stop moving, and the final estimates are combined statistically.[^s3] Its defining features are anonymity, iteration, controlled feedback and a statistical group response.[^s4]

## Origin

The method was developed at the RAND Corporation in the 1950s and 1960s by Olaf Helmer, Norman Dalkey and colleagues as a way to build consensus within a group, with participants kept apart rather than debating around a table.[^s5] Its first published account was Dalkey and Helmer's 1963 *Management Science* paper, which described an experiment using a series of intensive questionnaires with controlled opinion feedback to reach the most reliable consensus of a group of experts.[^s1] The name alludes to the oracle of Delphi in Greek mythology, and early applications were military forecasting problems.[^s4] A later ARPA-funded research plan led by Dalkey explained that anonymity, iteration and feedback had been introduced as intuitive fixes for familiar faults of face-to-face groups: dominant individuals, group pressure, bandwagon effects and irrelevant talk.[^s6]

## How it works

Each element targets a specific failure of ordinary meetings. Anonymity stops seniority or personality from setting the answer and gives every panellist an equal say; feedback shows each expert where they sit in the distribution and why others disagree; iteration lets people revise privately, so changing one's mind costs no face.[^s3] Aggregation then exploits the finding that pooled estimates from a group are usually more accurate than a typical individual's.[^s6]

*Workplace example.* A hospital operations team must estimate how many extra ICU beds it will need next winter. Instead of a meeting where the chief of medicine speaks first, a facilitator emails eight clinicians, two planners and a data analyst. Round one produces estimates from 6 to 30 beds, each with a short rationale. The facilitator circulates the median (14), the interquartile range and anonymised reasons, flagging the outliers. In round two the analyst's point about a new respiratory vaccine pulls several high estimates down, while one nurse's point about staffing shortfalls holds others up; the range narrows to 10–18. After a third round barely changes anything, the team plans on the median and treats the remaining spread as a measure of uncertainty.[^s3]

## How to apply it

1. **Frame the question.** Word items clearly and neutrally, avoid emotive terms and leave out irrelevant detail, since early wording anchors everything after.[^s2]
2. **Choose the panel.** Use experts with relevant knowledge from different angles; forecasting guidance suggests roughly 5–20 people.[^s2] Health-research Delphi panels are often larger, typically 10–100.[^s4]
3. **Fix the stopping and consensus rules in advance.** Definitions of consensus vary widely, with percentage-agreement thresholds from 50% to 97%, often chosen arbitrarily, so state the rule before round one.[^s4]
4. **Feed back reasons as well as numbers.** Share the mean or median together with all panellists' rationales, not statistics alone.[^s2]
5. **Stop when answers stabilise.** Two or three rounds usually suffice; more rounds mainly drive panellists to drop out.[^s3]
6. **Aggregate.** Weight panellists equally or use the median or a trimmed mean, watching for extreme values.[^s2]

**Variants.** In estimate–talk–estimate, panellists discuss between rounds but still submit estimates anonymously, which speeds clarification at the risk of letting the loudest voice dominate.[^s3] Online "e-Delphi" panels widen recruitment but tend to lose more panellists between rounds.[^s4]

## Evidence

Rowe and Wright's 2001 review of controlled studies found Delphi more accurate than simple statistical averages of the same panel in 12 studies, less accurate in 2, and tied in 2; against interacting committees it won 5, lost 1 and tied 2.[^s2] Accuracy often improved across rounds as estimates converged, but not always: in some studies gains stopped after a few rounds or reversed.[^s2] Many of these studies used students and almanac questions, so they may not generalise to real expert panels, and the authors warn that statistical feedback can itself recreate the conformity pressure Delphi was designed to remove.[^s2] Early RAND work similarly found only a slight edge for anonymous feedback over face-to-face discussion, with larger gains from group size and extra factual information.[^s6] In applied health research, a 2021 review found no standard quality criteria; of 34 COVID-19 Delphi studies from 2020, none met all nine of the authors' quality points and only two checked whether responses were stable.[^s4] Hence the rating here is *mixed*: a useful, often modestly better way to pool expert judgment, whose value depends heavily on design and reporting.

## Connections

- **Introduced by** Olaf Helmer and Norman Dalkey at RAND.[^s5] [^s1]
- **Counteracts** groupthink and the bandwagon effect by removing face-to-face pressure and attributing no answer to a named person.[^s4] [^s6]
- **Contrasts with** the nominal group technique, which adds structured face-to-face discussion and so lets vocal members gain more influence.[^s2]
- **Explained by** the wisdom-of-crowds principle that aggregated group estimates tend to beat individual ones.[^s3]
- **Applied in** forecasting and in medicine, where it is widely used to build expert consensus when direct evidence is thin.[^s3] [^s4]
- **Related to** the Delphi Report on critical thinking, an expert-consensus statement built with this method; to argument from expert opinion, whose critical questions about expertise apply to choosing panellists;[^s4] and to the anchoring effect, since first-round wording and summaries shape later rounds.[^s2]

## Sources

[^s1]: Dalkey, N. & Helmer, O. (1963). "An Experimental Application of the DELPHI Method to the Use of Experts." *Management Science* 9(3), 458-467. https://ideas.repec.org/a/inm/ormnsc/v9y1963i3p458-467.html (accessed 2026-11-14)
[^s2]: Rowe, G. & Wright, G. (2001). "Expert Opinions in Forecasting: The Role of the Delphi Technique." In J. S. Armstrong (ed.), *Principles of Forecasting*, 125-144. Kluwer. https://Www.Gwern.net/doc/statistics/prediction/2001-rowe.pdf (accessed 2026-11-14)
[^s3]: Hyndman, R. J. & Athanasopoulos, G. (2018). *Forecasting: Principles and Practice*, 2nd ed., section 4.3 "The Delphi method." OTexts. https://otexts.com/fpp2/delphimethod.html (accessed 2026-11-14)
[^s4]: Nasa, P., Jain, R. & Juneja, D. (2021). "Delphi methodology in healthcare research: How to decide its appropriateness." *World Journal of Methodology* 11(4), 116-129. https://www.wjgnet.com/2222-0682/full/v11/i4/116.htm?s=qc (accessed 2026-11-14)
[^s5]: INFORMS. "Norman C. Dalkey oversees a Delphi Experiment." History of O.R. Excellence, RAND Corporation slideshow. https://informs.org/Explore/History-of-O.R.-Excellence/Non-Academic-Institutions/RAND-Corporation/RAND-Slideshow/Norman-C.-Dalkey-oversees-a-Delphi-Experiment (accessed 2026-11-14)
[^s6]: Shure, G. H. & Dalkey, N. C. (c. 1972). *Group Judgment Technology: Project Scope and Research Plan* (CCBS-TM-2). ARPA / Defense Technical Information Center. https://apps.dtic.mil/sti/pdfs/AD0741668.pdf (accessed 2026-11-14)
