---
id: ct:forecasting
type: Field
title: Forecasting
aliases: [forecasting science, forecasting methods, judgmental and statistical forecasting]
domain: decision-making
summary: >-
  The practice, and the body of research around it, of predicting future
  quantities and events as accurately as the available information allows,
  using statistical models, structured human judgment or both, and of
  checking those predictions against what actually happens.
level: introductory
evidenceStatus: mixed
broader: [ct:judgment-and-decision-making, ct:statistics]
related: [ct:geopolitical-forecasting, ct:brier-score, ct:calibration, ct:outside-view, ct:planning-fallacy, ct:delphi-method, ct:wisdom-of-crowds, ct:overconfidence-effect, ct:the-robust-beauty-of-improper-linear-models]
requires: [ct:probability-theory]
relations:
  - {predicate: studiedIn, object: ct:statistics, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s5, confidence: medium}
  - {predicate: influencedBy, object: ct:j-scott-armstrong, source: s1, confidence: medium}
  - {predicate: demonstratedBy, object: ct:makridakis-2018-m4-competition, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: ct:grove-2000-clinical-versus-mechanical-prediction-meta-analysis, source: s4, confidence: high}
  - {predicate: appliedIn, object: ct:strategic-decision-making, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Golden Rule of Forecasting: Be Conservative"
    publisher: "Journal of Business Research 68(8), 1717-1731 (Armstrong, Green & Graefe, 2015), Wharton School, University of Pennsylvania"
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2016/10/Golden-Rule-of-Forcasting_Be-Conservative_2.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Forecasting: Principles and Practice (2nd ed.), section 1.2: Forecasting, planning and goals"
    publisher: "Rob J Hyndman & George Athanasopoulos, OTexts (2018)"
    url: https://otexts.com/fpp2/planning.html
    type: textbook
    accessed: 2026-11-18
  - id: s3
    title: "The M4 Competition: Results, findings, conclusion and way forward"
    publisher: "International Journal of Forecasting 34(4), 802-808 (Makridakis, Spiliotis & Assimakopoulos, 2018), University of Nicosia research portal"
    url: https://pure.unic.ac.cy/en/publications/the-m4-competition-results-findings-conclusion-and-way-forward/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Clinical versus mechanical prediction: A meta-analysis"
    publisher: "Psychological Assessment 12(1), 19-30 (Grove, Zald, Lebow, Snitz & Nelson, 2000), University of Minnesota Experts"
    url: https://experts.umn.edu/en/publications/clinical-versus-mechanical-prediction-a-meta-analysis/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Forecasting Tournaments: Tools for Increasing Transparency and Improving the Quality of Debate"
    publisher: "Current Directions in Psychological Science 23(4), 290-295 (Tetlock, Mellers, Rohrbaugh & Chen, 2014), Wharton School, University of Pennsylvania"
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Forecasting

Forecasting is predicting the future as accurately as possible with all the information at hand: past data, plus anything already known about what is coming, such as a scheduled price change or a planned product launch.[^s2] As a field it covers two broad families of method, statistical models that extrapolate or explain data and structured ways of eliciting and combining human judgment, and a research tradition that asks which of them actually work by scoring forecasts against outcomes.[^s1][^s3] For critical thinkers it is the place where claims about the future stop being opinions and become track records.[^s5]

Hyndman and Athanasopoulos draw a distinction that much everyday reasoning blurs. A forecast is what you expect to happen; a goal is what you want to happen; a plan is the set of actions meant to close the gap between the two.[^s2] They note that organisations often set goals with no forecast of whether they are realistic, and they sort forecasting needs by horizon: short-term (staff rotas, production and transport schedules), medium-term (buying materials, hiring, equipment) and long-term (strategic planning).[^s2]

## Origin

Forecasting grew out of statistics and economics, but its modern identity as an evidence-based field rests on large empirical comparisons. Spyros Makridakis's "M" competitions pit many methods against one another on thousands of real time series. The fourth, reported in 2018, found that 12 of the 17 most accurate entries were combinations of mostly statistical methods, that the winner was a hybrid of statistical and machine-learning ideas about 10% more accurate than the combination benchmark, and that the six pure machine-learning entries did poorly, with none beating that benchmark.[^s3] On the judgmental side, J. Scott Armstrong and colleagues spent decades turning experimental comparisons into codified principles, summarised in 2015 as a single "golden rule".[^s1] Psychology contributed a third strand: a 2000 meta-analysis by Grove and colleagues of clinical versus mechanical prediction found formulas about 10% more accurate than expert judgment on average, clearly better in roughly a third to a half of studies, and clearly worse in only 6-16%.[^s4] Philip Tetlock's forecasting tournaments, run for the US intelligence community from 2011, extended scoring to one-off geopolitical questions.[^s5]

## How it works

Armstrong, Green and Graefe's Golden Rule is to be conservative: a forecast should be consistent with cumulative knowledge about the present and the past, and should use methods already validated for the situation.[^s1] Their 2015 review turned the rule into a checklist of 28 guidelines and reported that 102 of 105 papers with experimental comparisons favoured the conservative procedure, and that ignoring a single guideline raised forecast error by roughly a third to two-fifths on average.[^s1] The guidelines that matter most in practice are familiar critical-thinking moves:

- **Start from analogies.** Ask several independent experts for similar past cases and their outcomes before reasoning from the specifics.[^s1]
- **Damp trends** when the series is unstable, when the horizon is long, or when the trend runs against known causal forces.[^s1]
- **Combine** forecasts from independent judges and dissimilar methods; the review reports typical error reductions of around 15-22% from combining.[^s1]
- **Avoid unstructured adjustments.** Managers routinely override statistical forecasts; in one study cited in the review they adjusted 99.7% of 8,411 pharmaceutical sales forecasts.[^s1]

A workplace example: a team asked for next quarter's support-ticket volume extrapolates the last two months' 30% growth straight up. A conservative forecaster first asks how ticket volume behaved after comparable launches, damps the short trend toward the longer-run rate, and averages a simple model with independent estimates from team members instead of letting one manager adjust the numbers by feel. That keeps the forecast (what will probably happen) separate from the goal (what the team wants to happen).[^s1][^s2]

Evaluation closes the loop. Tetlock and colleagues argue that verbal forecasts such as "might happen" are almost unfalsifiable, because they fit a wide span of probabilities and leave room for excuses after the fact.[^s5] Tournaments require numerical probabilities scored with Brier scores, which creates accountability.[^s5] In the Good Judgment Project, debiasing training, teaming and recruiting better forecasters each added roughly 10% to accuracy, and improved statistical aggregation added about 35%.[^s5]

## Evidence and limitations

The headline findings are consistent across traditions: simple, combined and conservative methods tend to beat complex single models and unaided intuition.[^s1][^s3][^s4] But effects depend on context. Grove's meta-analysis also found studies where clinicians did better, and pooled advantages hide wide variation across domains.[^s4] Armstrong's review is a synthesis by advocates of the approach, and its own tables report slightly different paper counts and average effects (32% to 44%), so its figures are best read as an order of magnitude.[^s1] Competition results reflect the series chosen, and M4's machine-learning verdict described the entries submitted in 2018, not the field's ceiling.[^s3] Tournament gains were measured on questions that resolve within months; how far they carry over to long-range questions is less clear.[^s5]

## Connections

- **Studied in statistics.** Hyndman and Athanasopoulos's textbook treats forecasting as a statistical discipline built on data, models and known future events.[^s2]
- **Studied in judgment and decision making.** Tetlock and colleagues present tournaments as a psychological tool for testing whose probability judgments are accurate.[^s5]
- **Influenced by J. Scott Armstrong.** His evidence-based principles, condensed into the Golden Rule, shaped how the field tests and codifies judgmental methods.[^s1]
- **Demonstrated by the M4 competition.** Its results show that combinations and hybrids beat most single methods on real series.[^s3]
- **Demonstrated by the clinical-versus-mechanical meta-analysis.** Grove and colleagues' pooled results show formulas outperforming unaided expert prediction on average.[^s4]
- **Applied in strategic decision making.** Long-term forecasts feed strategic planning about markets, environment and internal resources.[^s2]
- **Related nodes.** Geopolitical forecasting is the tournament-based branch for one-off events, the Brier score is its scoring rule, and the outside view and Delphi method correspond to the analogy and structured-expert guidelines above.[^s1][^s5]

## Sources

[^s1]: Armstrong, Green & Graefe, "Golden Rule of Forecasting: Be Conservative", Journal of Business Research 68(8), 2015. https://faculty.wharton.upenn.edu/wp-content/uploads/2016/10/Golden-Rule-of-Forcasting_Be-Conservative_2.pdf (accessed 2026-11-18)
[^s2]: Hyndman & Athanasopoulos, Forecasting: Principles and Practice, 2nd ed., OTexts, section 1.2. https://otexts.com/fpp2/planning.html (accessed 2026-11-18)
[^s3]: Makridakis, Spiliotis & Assimakopoulos, "The M4 Competition: Results, findings, conclusion and way forward", International Journal of Forecasting 34(4), 2018. https://pure.unic.ac.cy/en/publications/the-m4-competition-results-findings-conclusion-and-way-forward/ (accessed 2026-11-18)
[^s4]: Grove, Zald, Lebow, Snitz & Nelson, "Clinical versus mechanical prediction: A meta-analysis", Psychological Assessment 12(1), 2000. https://experts.umn.edu/en/publications/clinical-versus-mechanical-prediction-a-meta-analysis/ (accessed 2026-11-18)
[^s5]: Tetlock, Mellers, Rohrbaugh & Chen, "Forecasting Tournaments: Tools for Increasing Transparency and Improving the Quality of Debate", Current Directions in Psychological Science 23(4), 2014. https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf (accessed 2026-11-18)
