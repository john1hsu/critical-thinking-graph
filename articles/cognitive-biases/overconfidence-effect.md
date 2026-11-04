---
id: ct:overconfidence-effect
type: CognitiveBias
title: Overconfidence effect
aliases: [overconfidence bias, overconfidence]
domain: cognitive-biases
summary: >-
  The tendency for confidence in one's judgments, performance or estimates to
  exceed their actual accuracy, studied in three forms: overestimation of one's
  own performance, overplacement relative to others, and overprecision
  (excessive certainty that one's beliefs are correct).
level: introductory
evidenceStatus: mixed
broader: [ct:cognitive-bias]
related: [ct:premortem, ct:consider-the-opposite, ct:actively-open-minded-thinking, ct:calibration, ct:hard-easy-effect]
requires: []
relations:
  - {predicate: demonstratedBy, object: ct:soll-klayman-2004-interval-estimates-study, source: s4, confidence: high}
  - {predicate: demonstratedBy, object: ct:haran-2010-spies-experiments, source: s5, confidence: high}
  - {predicate: explainedBy, object: ct:regression-to-the-mean, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:probabilistic-mental-models-theory, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:juslin-2000-hard-easy-critique, source: s3, confidence: medium}
sources:
  - id: s1
    title: "The trouble with overconfidence"
    publisher: Psychological Review 115(2), 502-517 (Moore & Healy, 2008), author's copy at Ohio State University
    url: https://www.asc.ohio-state.edu/economics/healy/papers/Moore_Healy-TroubleWithOverconfidence.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s2
    title: "Probabilistic Mental Models: A Brunswikian Theory of Confidence"
    publisher: Psychological Review 98(4), 506-528 (Gigerenzer, Hoffrage & Kleinbölting, 1991), CORE repository copy
    url: https://core.ac.uk/download/285615452.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s3
    title: "Naive Empiricism and Dogmatism in Confidence Research: A Critical Examination of the Hard-Easy Effect"
    publisher: Psychological Review 107(2), 384-396 (Juslin, Winman & Olsson, 2000), CORE repository copy
    url: https://core.ac.uk/download/193675108.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "Overconfidence in interval estimates"
    publisher: Journal of Experimental Psychology - Learning, Memory, and Cognition 30(2), 299-314 (Soll & Klayman, 2004), Duke Scholars record
    url: https://scholars.duke.edu/publication/799402
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "A simple remedy for overprecision in judgment"
    publisher: Judgment and Decision Making 5(7), 467-476 (Haran, Moore & Morewedge, 2010)
    url: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/34DDFA0D8B602B6089A1B6BEEF22A486/S1930297500001637a.pdf/a-simple-remedy-for-overprecision-in-judgment.pdf
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Overconfidence effect

The overconfidence effect is the gap between how sure people are and how often they are right. Moore and Healy (2008) showed that research under this one label actually measures three different things: *overestimation* (thinking you did better than you did), *overplacement* (thinking you are better than others) and *overprecision* (being too sure that your beliefs are accurate).[^s1] In their review, roughly 64% of empirical studies examined overestimation, 31% overprecision and about 5% overplacement, often without saying which one they meant.[^s1]

## Origin

The effect grew out of calibration research, in which people answer general-knowledge questions and rate their confidence, or give intervals meant to capture a true value with a stated probability. Moore and Healy trace the classic finding of too-narrow intervals to work such as Alpert and Raiffa's, and cite later studies in which nominal 90% intervals captured the truth only about 30% to 50% of the time.[^s1] From the early 1990s an ecological school led by Gerd Gigerenzer argued that much of this apparent bias came from the way test questions were chosen rather than from a flaw in reasoning.[^s2] Moore and Healy's 2008 *Psychological Review* paper then separated the three forms and proposed a single account of how they relate.[^s1]

## How it works

Take a team lead asked for a range she is 90% sure will contain the launch date of a software release. She answers "between 10 and 14 weeks." If, across many such forecasts, the actual date lands inside her ranges only half the time, she is overprecise: her intervals are too narrow for the confidence she claims. Soll and Klayman (2004) found this pattern consistently, with true answers falling inside "X% sure" intervals far less often than X%, and with intervals in some conditions only about 40% as wide as good calibration would require.[^s4] They found much less overconfidence when the same people simply chose between two possible answers, which shows how much the measurement format matters.[^s4]

Overestimation and overplacement behave differently. Moore and Healy found that on hard quizzes people overestimated their own score but placed themselves *below* others, while on easy quizzes they underestimated their score but placed themselves *above* others.[^s1] Their Bayesian explanation is that people blend a prior expectation with a noisy signal of their own performance, so their estimates regress toward the prior. Because they know even less about others, their estimates of others regress further, which produces opposite errors on easy and hard tasks.[^s1]

## Evidence

Overprecision is the most durable form. In Moore and Healy's own experiment, participants' 90% intervals contained the correct answer 73.1% of the time, and hit rates rose after participants received information about their performance but still stayed below the stated confidence.[^s1] Haran, Moore and Morewedge (2010) found 90% interval hit rates of about 74%, 29% and 54% across three experiments on temperatures and historical dates.[^s5]

Overconfidence in two-alternative general-knowledge questions is more disputed. Gigerenzer, Hoffrage and Kleinbölting (1991) argued that people infer answers from cues that are valid in their everyday environment, so they look overconfident mainly when experimenters pick unusually tricky items. In their first experiment, overconfidence was 13.8% on a selected question set but close to zero on randomly sampled city pairs.[^s2] Juslin, Winman and Olsson (2000) reviewed this literature and found overconfidence of about .09 for selected item samples but about .01 for representative ones. They also argued that, once scale-end effects and linear dependency are corrected for, the hard-easy effect becomes small and non-significant.[^s3] They limited their conclusion to general-knowledge tasks.[^s3] Overall, the evidence is best summarized as *mixed*: overprecision in interval estimates is robust, while overestimation and overplacement depend heavily on task difficulty and item selection.[^s1][^s3]

## How to spot it

- Ask how often your past "90% sure" ranges actually contained the outcome. A hit rate well below 90% signals overprecision.[^s1][^s5]
- Watch for task difficulty. On hard tasks, people tend to overestimate their own results; on easy tasks, they tend to rate themselves above others.[^s1]
- Ask whether a quiz or test uses deliberately tricky items. A finding of overconfidence on such a selected set may not hold in everyday conditions.[^s2][^s3]

## How to counter it

- Change the elicitation format. With SPIES (Subjective Probability Interval Estimates), the full range of possible values is divided into bins and the judge assigns a probability to each. In Haran and colleagues' first experiment, SPIES reached a hit rate of 88.4% against a 90% target, compared with 73.8% for ordinary intervals.[^s5] Intervals drawn up after using SPIES were also wider, suggesting the habit carries over.[^s5]
- Prefer a choice between explicit options over an open-ended range when possible, since two-choice formats show much less overconfidence.[^s4]
- Keep score. Comparing forecasts with outcomes turns the vague feeling of certainty into a measurable hit rate.[^s1]

## Connections

- **Broader:** a cognitive bias, and the textbook example of poor calibration.[^s1]
- **Demonstrated by** Soll and Klayman's 2004 interval-estimate studies, which found systematically too-narrow intervals.[^s4] It is also **demonstrated by** Haran, Moore and Morewedge's 2010 experiments, where ordinary 90% intervals fell well short of their stated confidence.[^s5]
- **Explained by** regression toward the mean: Moore and Healy's model attributes the opposite errors on easy and hard tasks to imperfect signals that regress toward prior expectations.[^s1]
- **Explained by** probabilistic mental models theory, which traces apparent overconfidence to cue use and unrepresentative item selection.[^s2]
- **Challenged by** Juslin, Winman and Olsson's 2000 critique of the hard-easy effect, which found near-zero overconfidence with representative items.[^s3]
- **Related to** the premortem, consider-the-opposite and actively open-minded thinking, which this graph records as remedies for overconfidence. SPIES is a further, format-based remedy.[^s5]

## Sources

[^s1]: Moore & Healy, "The trouble with overconfidence", Psychological Review 115(2), 2008. https://www.asc.ohio-state.edu/economics/healy/papers/Moore_Healy-TroubleWithOverconfidence.pdf (accessed 2026-11-04)
[^s2]: Gigerenzer, Hoffrage & Kleinbölting, "Probabilistic Mental Models: A Brunswikian Theory of Confidence", Psychological Review 98(4), 1991. https://core.ac.uk/download/285615452.pdf (accessed 2026-11-04)
[^s3]: Juslin, Winman & Olsson, "Naive Empiricism and Dogmatism in Confidence Research", Psychological Review 107(2), 2000. https://core.ac.uk/download/193675108.pdf (accessed 2026-11-04)
[^s4]: Soll & Klayman, "Overconfidence in interval estimates", JEP: Learning, Memory, and Cognition 30(2), 2004. https://scholars.duke.edu/publication/799402 (accessed 2026-11-04)
[^s5]: Haran, Moore & Morewedge, "A simple remedy for overprecision in judgment", Judgment and Decision Making 5(7), 2010. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/34DDFA0D8B602B6089A1B6BEEF22A486/S1930297500001637a.pdf/a-simple-remedy-for-overprecision-in-judgment.pdf (accessed 2026-11-04)
