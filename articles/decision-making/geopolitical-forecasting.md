---
id: ct:geopolitical-forecasting
type: Field
title: Geopolitical forecasting
aliases: [political forecasting, forecasting tournaments, probabilistic geopolitical forecasting]
domain: decision-making
summary: >-
  The practice, and the research programme around it, of making explicit,
  numerical probability forecasts about future political, economic and
  security events, then scoring them against what actually happens so that
  forecasting skill can be measured, trained and aggregated.
level: introductory
evidenceStatus: mixed
broader: [ct:forecasting]
related: [ct:intelligence-analysis, ct:calibration, ct:calibration-training, ct:outside-view, ct:actively-open-minded-thinking, ct:brier-score, ct:wisdom-of-crowds, ct:chang-2016-forecasting-training-study, ct:overconfidence-effect, ct:hindsight-bias]
requires: [ct:calibration]
relations:
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:expert-political-judgment, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:philip-tetlock, source: s2, confidence: high}
  - {predicate: demonstratedBy, object: ct:mellers-2014-forecasting-tournament-study, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Psychological Strategies for Winning a Geopolitical Forecasting Tournament"
    publisher: "Psychological Science (Mellers, Ungar, Baron, Ramos, Gurcay, Fincher, Scott, Moore, Atanasov, Swift, Murray, Stone & Tetlock, 2014), eScholarship, University of California"
    url: https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Forecasting Tournaments: Tools for Increasing Transparency and Improving the Quality of Debate"
    publisher: "Current Directions in Psychological Science 23(4), 290-295 (Tetlock, Mellers, Rohrbaugh & Chen, 2014), Wharton School, University of Pennsylvania"
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Expert Political Judgment: How Good Is It? How Can We Know? (New Edition)"
    publisher: "Philip E. Tetlock, Princeton University Press (2005; new edition 2017)"
    url: https://press.princeton.edu/node/60674
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "ACE: Aggregative Contingent Estimation"
    publisher: "Intelligence Advanced Research Projects Activity (IARPA), Office of the Director of National Intelligence"
    url: https://www.iarpa.gov/research-programs/ace
    type: government
    accessed: 2026-11-17
  - id: s5
    title: "Long-Range Subjective-Probability Forecasts of Slow-Motion Variables in World Politics: Exploring Limits on Expert Judgment"
    publisher: "Futures and Foresight Science, accepted manuscript (Tetlock, Karvetski, Satopää & Chen), Wharton School, University of Pennsylvania"
    url: https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/Long-range-subjective-probability.pdf
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Geopolitical forecasting

Geopolitical forecasting is the attempt to put explicit probabilities on future political, economic and security events (will a ceasefire hold through March, will a country test a missile this year) and then to score those probabilities once the outcomes are known.[^s1] What makes it a field rather than punditry is the scoring: questions are written so that they resolve clearly, forecasts are numbers rather than words such as "possible", and accuracy is measured with a proper scoring rule such as the Brier score, on which 0 is perfect and 2 is maximally wrong.[^s1] That turns vague claims of expertise into track records that can be compared, trained and improved.[^s2]

## Origin

The modern field grew out of Philip Tetlock's long-running study of expert political judgment. Over roughly two decades he collected about 29,000 predictions from 284 specialists and compared them with informed non-specialists and simple statistical rules.[^s2][^s3] The experts often failed to beat those simple models and showed overconfidence, hindsight bias and self-serving excuses for misses; experts with a high need for closure did especially badly on long-range questions.[^s2] Borrowing Isaiah Berlin's metaphor, Tetlock found that "foxes", who draw on many ideas and adjust as events unfold, forecast better than "hedgehogs", who apply one big theory.[^s3] The book was published as *Expert Political Judgment* in 2005.[^s2][^s3]

The second phase was institutional. The US Intelligence Advanced Research Projects Activity launched the Aggregative Contingent Estimation (ACE) programme to make intelligence forecasts more accurate, precise and timely by eliciting probability judgments from many analysts and combining them mathematically, weighted by factors such as past performance and expertise.[^s4] ACE funded a tournament in which university-based teams competed on real, resolvable questions chosen by the intelligence community; Tetlock, Barbara Mellers and colleagues fielded one of these research groups.[^s1][^s2]

## How it works

Imagine a logistics firm that depends on a shipping lane through a contested strait. Instead of a briefing that says unrest is "a real possibility", the risk team asks a question that will clearly resolve: *Will commercial transit through the strait be suspended for seven or more consecutive days before 30 June?* Each analyst starts from a base rate (how often have comparable disruptions occurred in recent years?), adjusts for the specifics, posts a probability such as 15%, and revises it as news arrives. Teammates see one another's rationales and challenge them. When the deadline passes, every forecast is scored, so over dozens of questions the team learns who is well calibrated, who discriminates likely from unlikely events, and whether averaging the group beats its best individual.[^s1][^s2]

## How to apply it

1. **Write resolvable questions** with a clear event, threshold and deadline, so no one can later argue about what "unrest" meant.[^s1]
2. **Forecast in numbers** and update often; in the tournament the best forecasters revised far more frequently than others.[^s1]
3. **Start from reference classes and average several estimates**, the core of the short probability training that improved accuracy.[^s1]
4. **Work in teams that share reasoning**, then aggregate. Weighting forecasters by track record, giving more weight to recent forecasts and pushing the combined probability away from 50% produced the best aggregate forecasts.[^s1][^s4]
5. **Keep score.** A public record makes it harder to explain away misses and rewards cautious, well-calibrated claims.[^s2]

## Evidence

In the first two years of the IARPA tournament (2011 to 2013, about 2,200 and 1,600 forecasters, 199 questions), Mellers and colleagues randomly assigned forecasters to conditions.[^s1] About 45 minutes of probability training improved accuracy in both years, with benefits that carried over; working in teams had the largest effect; and the top 2% from year one, regrouped into "superforecaster" teams, beat every other group by a wide margin.[^s1] Most forecasters were nonetheless overconfident, and forecasts of 100% were the worst calibrated.[^s1]

The evidence status is *mixed* for three reasons. First, the superforecaster comparison was not randomised, and volunteers were self-selected and mostly American and male.[^s1] Second, tournament questions mostly resolve within a year, and the questions themselves were selected by the sponsor.[^s2] Third, skill fades with distance: in a proof-of-concept study of 5-, 10- and 25-year forecasts, accuracy declined as horizons lengthened. Nuclear-proliferation experts still beat generalists and base-rate extrapolation, but experts on border changes and secession had no advantage.[^s5] The authors warn against sweeping conclusions from so small a dataset.[^s5]

## Connections

- **Studied in** judgment and decision making, which treats forecasts as judgments that can be scored and debiased.[^s2]
- **Influenced by** Tetlock's *Expert Political Judgment* and by Tetlock himself, whose findings on expert accuracy motivated scored tournaments.[^s2][^s3]
- **Demonstrated by** the Mellers et al. (2014) tournament study, which showed that training, teaming and tracking raise accuracy.[^s1]
- **Applied in** intelligence analysis, the setting ACE was designed to improve.[^s4]
- **Related to** calibration and calibration training, the outside view, actively open-minded thinking, the wisdom of crowds and the Brier score, the tools and measures the field relies on; and to overconfidence and hindsight bias, the errors Tetlock's experts showed.[^s1][^s2]

## Sources

[^s1]: Mellers et al., "Psychological Strategies for Winning a Geopolitical Forecasting Tournament," *Psychological Science* (2014). https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf (accessed 2026-11-17)
[^s2]: Tetlock, Mellers, Rohrbaugh & Chen, "Forecasting Tournaments: Tools for Increasing Transparency and Improving the Quality of Debate," *Current Directions in Psychological Science* 23(4) (2014). https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf (accessed 2026-11-17)
[^s3]: Tetlock, *Expert Political Judgment: How Good Is It? How Can We Know?*, Princeton University Press (new edition 2017). https://press.princeton.edu/node/60674 (accessed 2026-11-17)
[^s4]: IARPA, "ACE: Aggregative Contingent Estimation." https://www.iarpa.gov/research-programs/ace (accessed 2026-11-17)
[^s5]: Tetlock, Karvetski, Satopää & Chen, "Long-Range Subjective-Probability Forecasts of Slow-Motion Variables in World Politics: Exploring Limits on Expert Judgment," *Futures and Foresight Science* (accepted manuscript). https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/Long-range-subjective-probability.pdf (accessed 2026-11-17)
