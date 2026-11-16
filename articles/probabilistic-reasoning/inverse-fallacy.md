---
id: ct:inverse-fallacy
type: ProbabilisticFallacy
title: Confusion of the inverse
aliases: [inverse fallacy, transposed conditional, transposing the conditional, inverse probability error]
domain: probabilistic-reasoning
summary: >-
  The error of treating a conditional probability P(A | B) as if it equalled
  its inverse P(B | A), for example reading the chance that a test is positive
  given a disease as the chance of the disease given a positive test.
level: intermediate
evidenceStatus: normative
broader: [ct:probabilistic-fallacy]
related: [ct:conditional-probability, ct:prosecutors-fallacy, ct:base-rate-neglect, ct:bayesian-reasoning, ct:natural-frequencies, ct:contingency-table, ct:null-hypothesis-significance-testing, ct:likelihood-ratio, ct:illicit-conversion, ct:gerd-gigerenzer]
requires: [ct:conditional-probability]
relations:
  - {predicate: contrastsWith, object: ct:base-rate-neglect, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:villejoubert-mandel-2002-inverse-fallacy-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:eddy-1982-mammography-study, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:bayesian-reasoning, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s1, confidence: medium}
criticalQuestions:
  - Which event is the probability conditioned on, and is that the event we actually know has happened?
  - Is the quoted figure the chance of the evidence given the hypothesis, or the chance of the hypothesis given the evidence?
  - How common is the hypothesis before any evidence comes in?
  - How often does the same evidence turn up when the hypothesis is false?
  - If we restate the numbers as counts out of a concrete group, what fraction of the positives are true positives?
argumentMap:
  premises:
    - "Our security vendor reports that 90% of phishing emails trigger its 'suspicious link' alert."
    - "This email from a supplier triggered the alert."
  conclusion: "So there is a 90% chance this supplier email is phishing."
  verdict: fallacious
  scheme: ct:bayesian-reasoning
  objections:
    - "The 90% figure is P(alert | phishing), not P(phishing | alert); the answer also depends on how rare phishing is and how often clean mail trips the alert."
    - "If 1 in 100 emails is phishing and 5% of clean emails trigger the alert, then of 1,000 emails about 9 phishing and about 50 clean ones are flagged, so only about 15% of alerts are phishing."
sameAs: []
sources:
  - id: s1
    title: "The inverse fallacy: An account of deviations from Bayes's theorem and the additivity principle"
    publisher: Memory & Cognition 30(2), 171-178 (Villejoubert & Mandel, 2002)
    url: https://link.springer.com/article/10.3758%2FBF03195278?LI=true
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Probabilistic reasoning in clinical medicine: Problems and opportunities"
    publisher: "Judgment under Uncertainty: Heuristics and Biases, ch. 18, pp. 249-267, Cambridge University Press (Eddy, 1982)"
    url: https://www.cambridge.org/core/books/abs/judgment-under-uncertainty/probabilistic-reasoning-in-clinical-medicine-problems-and-opportunities/661E12D1ECD669EDB5B410407A4BB570
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "How to improve the diagnostic inferences of medical experts"
    publisher: "Experts in Science and Society, pp. 249-268, Kluwer (Hoffrage & Gigerenzer, 2004), Max Planck Society repository"
    url: https://pure.mpg.de/pubman/item/item_2101266_7/component/file_2563079/az0400101.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "The ASA's statement on p-values: Context, process, and purpose"
    publisher: The American Statistician 70(2), 129-133 (Wasserstein & Lazar, 2016), UC Berkeley course copy
    url: https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Confusion of the inverse

Confusion of the inverse, also called the inverse fallacy or transposing the conditional, is the mistake of answering a question about P(hypothesis | data) with a number that really describes P(data | hypothesis). Villejoubert and Mandel define it as the tendency to give, when asked for a posterior probability, an estimate that tracks the inverse conditional probability instead.[^s1] The two quantities share the same events but condition on different ones, and they can differ enormously whenever the hypothesis is rare or the data are common for other reasons.[^s3]

## Origin

The error was documented in medicine before it had a settled name. In a 1982 chapter of Kahneman, Slovic and Tversky's *Judgment under Uncertainty*, physician and decision analyst David Eddy argued that many doctors make serious probabilistic errors when interpreting mammograms, and that these errors can harm the quality of care.[^s2] Hoffrage and Gigerenzer's account of that work reports that when given a 1% prevalence of breast cancer, a hit rate near 80% and a false-positive rate of 9.6%, 95 of 100 physicians estimated the chance of cancer after a positive mammogram at 70-80%, where Bayes' rule gives under 8%. Eddy's diagnosis was that most had confused the test's sensitivity with its positive predictive value.[^s3] Psychologists Gaëlle Villejoubert and David Mandel later gave the error a formal account in *Memory & Cognition* (2002), arguing that it should be treated separately from base-rate neglect.[^s1]

## How it works

The argument map above shows a workplace version. A vendor's statement that 90% of phishing emails trigger an alert is a fact about phishing emails: P(alert | phishing). The question the security team needs answered is the reverse, P(phishing | alert). That depends on two further numbers the 90% hides: how rare phishing is, and how often clean mail triggers the same alert. With 1% phishing and a 5% false-alarm rate, about 9 of every 1,000 emails are flagged phishing and about 50 are flagged clean mail, so only around 15% of alerts are real.[^s3] Treating 90% as the answer swaps the conditional, and it also quietly drops the base rate.[^s1]

The same swap is common in research. The American Statistical Association's 2016 statement stresses that a p-value is not the probability that the studied hypothesis is true or that chance alone produced the data; it describes how the data relate to a specified hypothetical explanation.[^s4] Reading "p = 0.03" as "a 3% chance the null hypothesis is true" is confusion of the inverse applied to significance testing.[^s4] In court, reading a random-match probability as the probability of innocence is the special case known as the prosecutor's fallacy.

## How to spot it

Translate every probability claim into words that say what it is conditioned on: "of the people who have X, how many show Y?" versus "of the people who show Y, how many have X?".[^s3] Be suspicious whenever a test's accuracy, a detector's hit rate or a p-value is quoted as if it were the probability of the conclusion.[^s4] The error is most damaging when the hypothesis is rare, because then even a small false-positive rate produces more false alarms than true hits.[^s3] Villejoubert and Mandel also found that people's estimates for a hypothesis and its complement need not sum to one, so non-additive answers are another symptom.[^s1]

## How to counter it

Restate the problem as natural frequencies: counts out of one concrete group, such as 1,000 emails or 10,000 patients. In Hoffrage and Gigerenzer's study of 48 physicians, only 10% of answers were Bayesian when the information came as probabilities, against 46% when it came as natural frequencies, and the frequency format sharply reduced the number of physicians who mistook sensitivity for predictive value.[^s3] Ask explicitly for both directions of the conditional and for the base rate, and compute P(hypothesis | data) with Bayes' rule or a likelihood ratio instead of reading it off a single quoted figure.[^s3] For statistical results, report effect sizes and interval estimates alongside p-values, and do not describe a p-value as the probability that a finding is a fluke.[^s4]

## Connections

- **Contrasts with base-rate neglect.** The two often occur together, but Villejoubert and Mandel found that deviations from Bayes' theorem were predicted by how far the inverse probabilities themselves deviated from the normative answer, and argue the inverse fallacy should be distinguished from base-rate neglect.[^s1]
- **Demonstrated by Villejoubert and Mandel's 2002 study** of 45 participants, which also linked the fallacy to violations of additivity for conditional probabilities.[^s1]
- **Demonstrated by Eddy's 1982 mammography work**, the classic report of physicians confusing sensitivity with positive predictive value.[^s2][^s3]
- **Contrasts with Bayesian reasoning**, which combines the base rate with both the hit rate and the false-alarm rate to reach the posterior that the inverse fallacy skips.[^s3]
- **Studied in judgment and decision making**, alongside other departures from probability theory.[^s1]
- **Related to the prosecutor's fallacy**, its legal instance, and to the p-value misreadings of null-hypothesis significance testing.[^s4]

## Sources

[^s1]: Villejoubert & Mandel, "The inverse fallacy: An account of deviations from Bayes's theorem and the additivity principle", *Memory & Cognition* 30(2) (2002): 171–178. https://link.springer.com/article/10.3758%2FBF03195278?LI=true (accessed 2026-11-16)
[^s2]: Eddy, "Probabilistic reasoning in clinical medicine: Problems and opportunities", in Kahneman, Slovic & Tversky (eds.), *Judgment under Uncertainty: Heuristics and Biases*, Cambridge University Press (1982): 249–267. https://www.cambridge.org/core/books/abs/judgment-under-uncertainty/probabilistic-reasoning-in-clinical-medicine-problems-and-opportunities/661E12D1ECD669EDB5B410407A4BB570 (accessed 2026-11-16)
[^s3]: Hoffrage & Gigerenzer, "How to improve the diagnostic inferences of medical experts", in Kurz-Milcke & Gigerenzer (eds.), *Experts in Science and Society*, Kluwer (2004): 249–268. https://pure.mpg.de/pubman/item/item_2101266_7/component/file_2563079/az0400101.pdf (accessed 2026-11-16)
[^s4]: Wasserstein & Lazar, "The ASA's statement on p-values: Context, process, and purpose", *The American Statistician* 70(2) (2016): 129–133. https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf (accessed 2026-11-16)
