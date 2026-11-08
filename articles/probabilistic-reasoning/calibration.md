---
id: ct:calibration
type: Concept
title: Calibration
aliases: [probability calibration, calibrated probability assessment, forecast reliability, calibration of confidence]
domain: probabilistic-reasoning
summary: >-
  The match between stated confidence and actual hit rate: a judge is well
  calibrated when, across many judgments given the same probability, that
  share of them turns out true. It is one component of probabilistic accuracy,
  distinct from resolution, and is measured with scoring rules such as the
  Brier score.
level: intermediate
evidenceStatus: normative
broader: [ct:metacognition]
related: [ct:overconfidence-effect, ct:hard-easy-effect, ct:bayesian-reasoning, ct:baruch-fischhoff, ct:sarah-lichtenstein, ct:sherman-kent, ct:intelligence-analysis, ct:hindsight-bias, ct:debiasing]
requires: [ct:bayesian-reasoning]
relations:
  - {predicate: formalizedBy, object: ct:brier-score, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:forecast-resolution, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:geopolitical-forecasting, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:weather-forecasting, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Calibration of Probabilities: The State of the Art (Technical Report DDI-3)"
    publisher: "Lichtenstein, Fischhoff & Phillips, Oregon Research Institute for DARPA/ONR, August 1976 (DTIC ADA033248)"
    url: https://apps.dtic.mil/sti/pdfs/ADA033248.pdf
    type: primary
    accessed: 2026-11-08
  - id: s2
    title: "Psychological Strategies for Winning a Geopolitical Forecasting Tournament"
    publisher: "Psychological Science 25(5) (Mellers, Ungar, Baron et al., 2014), eScholarship author copy"
    url: https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Simplifying and generalising Murphy's Brier score decomposition"
    publisher: "Quarterly Journal of the Royal Meteorological Society (Siegert), University of Exeter repository copy"
    url: https://ore.exeter.ac.uk/rest/bitstreams/141507/retrieve
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Brier score"
    publisher: "Glossary of Meteorology, American Meteorological Society"
    url: https://glossary.ametsoc.org/wiki/brier-score/
    type: institutional
    accessed: 2026-11-08
created: 2026-11-08
---

# Calibration

Calibration is the agreement between how confident someone says they are and how often they turn out to be right. Take every statement a person rated 80% likely. If about 80% of them come true, the person is well calibrated at that level. If fewer come true, they are overconfident; if more, underconfident.[^s1] Calibration is a property of a *set* of judgments, not of a single forecast. One 80% call that misses proves nothing, but a long record of 80% calls that land only half the time does.[^s1]

## Origin

The idea came out of weather forecasting, where agencies such as the U.S. Weather Bureau issued probabilities of precipitation.[^s1] In 1950 Brier proposed scoring such forecasts by the average squared gap between each stated probability and the outcome, coded 1 if the event happened and 0 if not.[^s3] A perfect forecaster scores 0, and higher scores are worse.[^s4] In 1973 Murphy split this score into parts. *Reliability* is the meteorologists' word for calibration. *Resolution* measures whether forecasts separate likelier from less likely situations. The third part, *uncertainty*, reflects how hard the events are to predict in the first place.[^s3]

Psychologists took the concept up in the 1970s. Sarah Lichtenstein, Baruch Fischhoff and Lawrence Phillips's 1976 review for DARPA and the Office of Naval Research collected the evidence to date. It became the reference point for later calibration research in judgment and decision making.[^s1]

## How it works

Suppose a product team lead gives a probability for each sprint goal being met: 90% for some goals, 60% for others. After a year, she groups the goals by stated probability and checks each group's hit rate. If her 90% goals were met only 65% of the time, she is overconfident at the top of the scale. Plotting stated probability against observed frequency gives a *reliability diagram*; perfect calibration falls on the diagonal.[^s3]

Calibration is not the whole of accuracy. A lead who says "70%" for every goal, in a team that meets 70% of its goals, is perfectly calibrated. But she has zero resolution, because her forecasts never tell the good bets from the bad ones.[^s3] The Brier score rewards both properties at once. Its decomposition shows which one a forecaster is missing.[^s3]

For quantities rather than events, the same logic applies to ranges. A person's 98% intervals should miss the true value about 2% of the time. In the studies Lichtenstein and colleagues reviewed, 20% to 50% of true values fell outside such ranges.[^s1]

## How to apply it

1. **State numbers, not words.** Phrases like "likely" cannot be scored. Record a probability, a deadline and a clear resolution rule for each forecast.[^s2]
2. **Keep score.** Log forecasts and outcomes, then compute hit rates by probability bin or a Brier score. Calibration needs many judgments, so review in batches rather than after each surprise.[^s3]
3. **Get feedback.** In one study the reviewers cite, out-of-range surprises fell from 50% to 6% over four sessions with feedback. Most training gains were more modest, though.[^s1]
4. **Watch item difficulty.** People tend to be overconfident on hard questions and underconfident on easy ones, so a single overall calibration figure can hide errors in both directions.[^s1]

## Evidence and limitations

Lichtenstein and colleagues found weather forecasters well calibrated on rain probabilities. Most other groups were poorly calibrated, usually overconfident. On tasks at the edge of knowledge, such as predicting stock movements, there was essentially no calibration at all.[^s1] Calibration can be trained. In the IARPA geopolitical forecasting tournament, Mellers and colleagues (2014) gave forecasters about 45 minutes of probability training. It covered reference classes, averaging several estimates, and traps such as base-rate neglect. Over two years and about 200 questions, trained forecasters had better Brier scores and better calibration than untrained ones.[^s2] Most forecasters were still overconfident, especially when they gave certainties early in a question's life.[^s2] The best performers' edge came mainly from resolution rather than calibration, a reminder that calibration alone is not skill.[^s2]

There are limits. Calibration scores need many resolved forecasts with clear outcomes, which some fields rarely produce.[^s3] Tournament volunteers and laboratory trivia also differ from experts in real settings, so effect sizes may not transfer.[^s2]

## Connections

- **Broader:** a form of metacognitive accuracy, since it asks whether a judge's confidence tracks their own correctness.[^s1]
- **Formalized by** the Brier score, whose reliability term measures calibration directly.[^s3]
- **Contrasts with** forecast resolution, the ability to tell likelier events from less likely ones. A forecaster can have either without the other.[^s3]
- **Studied in** judgment and decision making, from the 1976 review onward.[^s1]
- **Applied in** weather forecasting, where it began and where forecasters are well calibrated,[^s1] and in geopolitical forecasting tournaments that train and score analysts.[^s2]
- **Related to** the overconfidence effect and the hard-easy effect, the main patterns of miscalibration;[^s1] to Bayesian reasoning and probability training, which Mellers and colleagues used to improve it;[^s2] to Baruch Fischhoff and Sarah Lichtenstein, who led the 1976 review;[^s1] and to hindsight bias, Sherman Kent, intelligence analysis and debiasing, which concern how forecasts are expressed, judged and improved.[^s1][^s2]

## Sources

[^s1]: Lichtenstein, S., Fischhoff, B. & Phillips, L. D. (1976). *Calibration of Probabilities: The State of the Art*, Technical Report DDI-3, Oregon Research Institute. https://apps.dtic.mil/sti/pdfs/ADA033248.pdf (accessed 2026-11-08)
[^s2]: Mellers, B., Ungar, L., Baron, J. et al. (2014). "Psychological Strategies for Winning a Geopolitical Forecasting Tournament." *Psychological Science* 25(5). https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf (accessed 2026-11-08)
[^s3]: Siegert, S. "Simplifying and generalising Murphy's Brier score decomposition." *Quarterly Journal of the Royal Meteorological Society*. https://ore.exeter.ac.uk/rest/bitstreams/141507/retrieve (accessed 2026-11-08)
[^s4]: American Meteorological Society, "Brier score", *Glossary of Meteorology*. https://glossary.ametsoc.org/wiki/brier-score/ (accessed 2026-11-08)
