---
id: ct:brier-score
type: Concept
title: Brier score
aliases: [Brier scoring rule, quadratic scoring rule, quadratic probability score]
domain: probabilistic-reasoning
summary: >-
  A strictly proper scoring rule for probability forecasts: the mean squared
  difference between each forecast probability and the outcome coded 1 if the
  event happened and 0 if not. Zero is perfect and lower is better, so it
  rewards forecasters who are both well calibrated and discriminating.
level: intermediate
evidenceStatus: normative
broader: [ct:forecasting, ct:proper-scoring-rule]
related: [ct:calibration, ct:forecast-resolution, ct:geopolitical-forecasting, ct:calibration-training, ct:overconfidence-effect, ct:philip-tetlock, ct:sarah-lichtenstein, ct:actively-open-minded-thinking]
requires: [ct:probability-theory]
relations:
  - {predicate: instanceOf, object: ct:proper-scoring-rule, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:glenn-brier, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:logarithmic-scoring-rule, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:weather-forecasting, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:geopolitical-forecasting, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "A Brief on Brier Scores"
    publisher: "University of Virginia Library StatLab (Goldstein-Greenwood, 2021)"
    url: https://library.virginia.edu/data/articles/a-brief-on-brier-scores
    type: academic
    accessed: 2026-11-18
  - id: s2
    title: "Strictly Proper Scoring Rules, Prediction, and Estimation (Technical Report 463R)"
    publisher: "Gneiting & Raftery, Department of Statistics, University of Washington, 2005 (DTIC ADA454828); published in JASA 2007"
    url: https://apps.dtic.mil/sti/pdfs/ADA454828.pdf
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Simplifying and generalising Murphy's Brier score decomposition"
    publisher: "Quarterly Journal of the Royal Meteorological Society (Siegert), University of Exeter repository copy"
    url: https://ore.exeter.ac.uk/rest/bitstreams/141507/retrieve
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "The Psychology of Intelligence Analysis: Drivers of Prediction Accuracy in World Politics"
    publisher: "Journal of Experimental Psychology: Applied 21(1) (Mellers, Stone, Atanasov et al., 2015), Wharton author copy"
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---the-psychology-of-intelligence-analysis.pdf
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Brier score

The Brier score is a way to grade probability forecasts once the outcomes are known. For each forecast, take the stated probability, subtract the outcome (1 if the event happened, 0 if it did not), square the difference, and average those squared errors over all forecasts.[^s1] A forecaster who said 90% for an event that happened is penalised 0.01; one who said 60% is penalised 0.16. A score of 0 is perfect and lower is always better.[^s1] Because it turns "how good are your probabilities?" into a number, it is the standard yardstick for calibration, forecasting tournaments and any claim that someone's judgment is better than chance.[^s4]

## Origin

The rule was proposed by the meteorologist Glenn W. Brier in a 1950 *Monthly Weather Review* article, "Verification of forecasts expressed in terms of probability", written as weather services began issuing probabilities of rain rather than yes-or-no calls.[^s1][^s2] Brier stated it for several mutually exclusive outcome classes, summing the squared errors over every class.[^s1] Statisticians later recognised it as the first and best-known member of the family now called *proper scoring rules*; the term "proper" was coined by Winkler and Murphy in 1968, building on ideas Good set out in 1952.[^s2] In 1973 Murphy showed how the score splits into interpretable parts, which is why meteorologists still use it to diagnose forecast systems.[^s3]

## How it works

Two versions are in common use. The binary form averages (forecast − outcome)² over events and runs from 0 to 1; a fence-sitter who always says 50% scores 0.25.[^s1] Brier's original multi-category form sums over all outcome classes and runs from 0 to 2; applied to yes/no events it simply doubles the binary score, so it matters which version a report uses.[^s1] Forecasting research on world events has used the 0-to-2 form, averaging scores over every day a question was open and then across questions.[^s4]

*Workplace example.* A project lead says each quarter how likely each of five milestones is to ship on time: 90%, 80%, 70%, 60% and 30%. Four ship and the 30% one slips. Her squared errors are 0.01, 0.04, 0.09, 0.16 and 0.09, for a binary Brier score of 0.078. A colleague who said 50% for everything scores 0.25 whatever happens. A *Brier skill score* compares a forecaster with such a reference: 1 − (her score ÷ reference score), so 0 means no better than the reference and negative values mean worse.[^s1]

The key property is that the rule is *strictly proper*: a forecaster's expected score is best only when they report exactly the probability they believe.[^s2] Shading a 70% belief up to 90% to sound decisive, or down to 50% to stay safe, costs points on average. That is what makes it a fair incentive as well as a measure.[^s2][^s4]

Murphy's decomposition writes the score as **reliability − resolution + uncertainty**.[^s3] *Reliability* is the gap between each stated probability and how often events given that probability actually happened, so it is zero for a perfectly calibrated forecaster. *Resolution* rewards forecasts that move away from the base rate in the right direction. *Uncertainty* depends only on how often the event occurs and is outside the forecaster's control.[^s3] A lead who says 70% for every milestone in a team that hits 70% of them has perfect reliability but zero resolution.

## How to apply it

1. Write questions that resolve clearly by a date, and record a number, not a word such as "likely", for each.[^s4]
2. Fix the version (0-to-1 or 0-to-2) before scoring and state it with the result.[^s1]
3. Compare against a reference such as always forecasting the base rate, via a skill score, and against the same questions; people who pick their own questions should be compared within question.[^s1][^s4]
4. Use the decomposition to see whether a weak score comes from miscalibration or from lack of resolution.[^s3]

## Evidence and limitations

In a large geopolitical forecasting tournament reported in 2015, participants averaged about 0.30 on the 0-to-2 scale against 0.53 for uniform guessing. Individual scores were highly consistent across questions (Cronbach's alpha 0.88), and the best and worst forecasters identified early stayed apart for two years, which the authors read as skill rather than luck.[^s4] Lower Brier scores went with probability training, teamwork, frequent belief updating and actively open-minded thinking.[^s4]

The score has limits. Skill scores built on it are not strictly proper, and they explode toward minus infinity when the reference score is near zero.[^s1][^s2] The decomposition is exact only when forecasts take a few distinct values; binned continuous forecasts leave a residual, and too many bins over-fit.[^s3] Compared with the logarithmic score, it punishes a confident miss less harshly: the log score becomes infinite when a forecaster gives 0% to something that happens, while the Brier score stays bounded.[^s1]

## Connections

- **Instance of** a proper scoring rule, the class of rules under which honest reporting maximises expected score; the Brier score is its quadratic member.[^s2]
- **Introduced by** Glenn W. Brier in his 1950 *Monthly Weather Review* paper.[^s2]
- **Contrasts with** the logarithmic scoring rule, which is unbounded when a zero-probability event occurs.[^s1]
- **Applied in** weather forecasting, where Murphy's decomposition diagnoses reliability and resolution, and in geopolitical forecasting tournaments that scored thousands of volunteers.[^s3][^s4]
- **Related to** calibration, which it formalises through its reliability term, and forecast resolution, the other part of accuracy it rewards; to calibration training and actively open-minded thinking, which improved scores; and to overconfidence, which it penalises.[^s3][^s4]

## Sources

[^s1]: Goldstein-Greenwood, J. "A Brief on Brier Scores." University of Virginia Library StatLab, 2021. https://library.virginia.edu/data/articles/a-brief-on-brier-scores (accessed 2026-11-18)
[^s2]: Gneiting, T. & Raftery, A. E. "Strictly Proper Scoring Rules, Prediction, and Estimation." Technical Report 463R, University of Washington, 2005. https://apps.dtic.mil/sti/pdfs/ADA454828.pdf (accessed 2026-11-18)
[^s3]: Siegert, S. "Simplifying and generalising Murphy's Brier score decomposition." *Quarterly Journal of the Royal Meteorological Society*. https://ore.exeter.ac.uk/rest/bitstreams/141507/retrieve (accessed 2026-11-18)
[^s4]: Mellers, B. et al. "The Psychology of Intelligence Analysis: Drivers of Prediction Accuracy in World Politics." *Journal of Experimental Psychology: Applied* 21(1), 2015. https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---the-psychology-of-intelligence-analysis.pdf (accessed 2026-11-18)
