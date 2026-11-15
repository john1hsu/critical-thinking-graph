---
id: ct:probabilistic-fallacy
type: Concept
title: Probabilistic fallacy
aliases: [probabilistic fallacies, probability fallacy, fallacy of probabilistic reasoning]
domain: probabilistic-reasoning
summary: >-
  A reasoning error in judging, combining or interpreting probabilities that
  violates the rules of probability theory, such as ignoring base rates,
  transposing a conditional probability, rating a conjunction above one of its
  parts, or expecting chance to correct itself.
level: introductory
evidenceStatus: normative
broader: [ct:fallacy]
related: [ct:base-rate-neglect, ct:conjunction-fallacy, ct:gamblers-fallacy, ct:hot-hand-fallacy, ct:prosecutors-fallacy, ct:inverse-fallacy, ct:insensitivity-to-sample-size, ct:law-of-small-numbers, ct:regression-to-the-mean, ct:natural-frequencies, ct:likelihood-ratio, ct:formal-fallacy, ct:informal-fallacy, ct:heuristics-and-biases-program]
requires: [ct:probability-theory, ct:conditional-probability]
relations:
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:bayesian-reasoning, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:gerd-gigerenzer, source: s4, confidence: high}
sources:
  - id: s1
    title: "Judgment under Uncertainty: Heuristics and Biases"
    publisher: "Science 185(4157), 1124-1131 (Tversky & Kahneman, 1974), course reading copy, NC State University"
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Extensional versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment"
    publisher: "Psychological Review 90(4), 293-315 (Tversky & Kahneman, 1983), course copy, UC San Diego"
    url: https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Interpretation of Statistical Evidence in Criminal Trials: The Prosecutor's Fallacy and the Defense Attorney's Fallacy"
    publisher: "Law and Human Behavior 11(3), 167-187 (Thompson & Schumann, 1987)"
    url: https://www.joelvelasco.net/teaching/122/thompson&schumann87-statisticslaw.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "How to Make Cognitive Illusions Disappear: Beyond 'Heuristics and Biases'"
    publisher: "European Review of Social Psychology 2, 83-115 (Gigerenzer, 1991), course reading copy, NC State University"
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1991.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "On the Reality of Cognitive Illusions"
    publisher: "Psychological Review 103(3), 582-591 (Kahneman & Tversky, 1996), course reading copy, NC State University"
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Kahneman+Tversky-cognitive-illusions-1996.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Probability, statistics, and the likelihood ratio for non-experts: 4.16 Probabilities for propositions (prosecutor's fallacy)"
    publisher: "Leverhulme Research Centre for Forensic Science, University of Dundee (Gray, 2020-2021)"
    url: https://lrcfs-ap2.dundee.ac.uk/lr_book/prosecutor-fallacy.html
    type: academic
    accessed: 2026-11-15
created: 2026-11-15
---

# Probabilistic fallacy

A probabilistic fallacy is a mistake in reasoning about chance: a judgment about how likely something is, or an inference from probabilistic evidence, that breaks the rules of probability theory. Classic members of the family are neglecting base rates, misjudging how much a small sample can show, expecting a random process to "even out", failing to anticipate regression to the mean, and misjudging compound events.[^s1] Others are rating a conjunction as more likely than one of its own parts[^s2] and reading the probability of the evidence given a hypothesis as if it were the probability of the hypothesis given the evidence.[^s3][^s6] Unlike a formal fallacy, the error is not an invalid deductive form; unlike most informal fallacies, it has a precise yardstick, because the correct answer can usually be calculated.[^s2][^s6]

## Origin

Probability errors were noticed long before they were catalogued, but the modern family took shape in the heuristics-and-biases research of Amos Tversky and Daniel Kahneman. Their 1974 *Science* article traced a series of systematic errors in intuitive probability judgment, including insensitivity to prior probability and sample size, misconceptions of chance and of regression, and biased estimates of conjunctive and disjunctive events, to a few judgmental heuristics.[^s1] Their 1983 paper named and dissected the conjunction fallacy and framed the general contrast between extensional reasoning, which respects set inclusion, and intuitive reasoning, which follows similarity.[^s2] In 1987 William Thompson and Edward Schumann coined the prosecutor's fallacy and the defense attorney's fallacy to describe how statistical evidence is misread in court.[^s3][^s6]

## How it works

Most members share a pattern: an intuitive impression stands in for the quantity that probability theory says matters. Under representativeness, people judge how probable an outcome is by how much it resembles a stereotype or a typical random sequence, which pushes base rates and sample size out of view.[^s1] In Tversky and Kahneman's Linda problem, 85% of 142 students judged "bank teller and feminist" more probable than "bank teller", although a conjunction can never be more probable than either of its parts.[^s2] Their physician samples erred too, so expertise in a field did not protect against the error.[^s2]

A workplace example shows the conditional-probability version. A fraud filter flags 95% of fraudulent payments and wrongly flags 5% of legitimate ones, and about 1 payment in 100 is fraudulent. An analyst concludes that a flagged payment is 95% likely to be fraud. That transposes the conditional and ignores the base rate. Out of 10,000 payments, about 95 of the 100 frauds are flagged, but so are about 495 of the 9,900 legitimate ones, so only about 16% of flags are fraud. The Dundee forensic primer works the same arithmetic for a diagnostic test and lands on roughly 28% rather than 95%.[^s6]

## How to spot it

Ask what the stated number is conditional on and whether the claim has quietly swapped it around.[^s3][^s6] Ask for the base rate and the sample size before trusting a striking percentage.[^s1] When a detailed, story-like scenario seems more likely than a plain one, check whether it is really a conjunction of the plain one with extra conditions.[^s2] When someone predicts that a run of outcomes is "due" to reverse, ask whether the events are actually independent.[^s1] When performance falls after praise or rises after criticism, consider regression to the mean before inventing a cause.[^s1]

## How to counter it

Recasting single-case probabilities as counts out of a concrete population makes class inclusion visible. In Tversky and Kahneman's own health-survey problem, conjunction errors fell from 65% with percentages to 25% with frequency questions.[^s2] Gerd Gigerenzer reported larger reductions, with frequency versions of the Linda problem cutting violations to around 20%.[^s4] In courts and forensic reporting, the recommended discipline is to state how probable the evidence is under each competing proposition, the likelihood ratio, and leave the probability of the propositions themselves to the fact finder.[^s6]

## Evidence and limitations

The individual errors are well documented, but how to interpret them is disputed. Gigerenzer argued that many so-called fallacies are judged against a narrow Bayesian norm for single events, a norm frequentist statisticians would reject, and that they shrink or vanish when questions are asked in frequency terms.[^s4] Kahneman and Tversky replied in 1996 that frequency formats reduce some errors without making them disappear, and that base-rate neglect and conjunction errors persist in several frequency and within-subject designs.[^s5] Context matters as well: in Thompson and Schumann's mock-juror studies, the prosecutor's fallacy was more common when the statistic was phrased as a conditional probability, while the opposite error of discounting matching evidence turned out to be the more persuasive one.[^s3] These were student samples rather than real juries.[^s3]

## Connections

This node is the umbrella for the graph's probability-specific errors, including base-rate neglect, the conjunction fallacy, the gambler's and hot-hand fallacies, insensitivity to sample size and the prosecutor's or inverse fallacy.[^s1][^s2][^s3] Several are **explained by the representativeness heuristic**,[^s1] and the family is **studied in judgment and decision making**.[^s1] Its modern framing as a fallacy family was **introduced by Amos Tversky** with Daniel Kahneman.[^s2] It **contrasts with Bayesian reasoning**, the normative standard Thompson and Schumann used to judge how jurors should weigh matching evidence.[^s3] Its status as a set of genuine errors is **challenged by Gerd Gigerenzer**, whose frequency-format critique drew the 1996 reply.[^s4][^s5] Natural frequencies and the likelihood ratio are practical remedies.[^s2][^s6]

## Sources

[^s1]: Tversky & Kahneman, "Judgment under Uncertainty: Heuristics and Biases", *Science* 185, 1124-1131 (1974). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf (accessed 2026-11-15)
[^s2]: Tversky & Kahneman, "Extensional versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment", *Psychological Review* 90(4), 293-315 (1983). https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf (accessed 2026-11-15)
[^s3]: Thompson & Schumann, "Interpretation of Statistical Evidence in Criminal Trials", *Law and Human Behavior* 11(3), 167-187 (1987). https://www.joelvelasco.net/teaching/122/thompson&schumann87-statisticslaw.pdf (accessed 2026-11-15)
[^s4]: Gigerenzer, "How to Make Cognitive Illusions Disappear: Beyond 'Heuristics and Biases'", *European Review of Social Psychology* 2, 83-115 (1991). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1991.pdf (accessed 2026-11-15)
[^s5]: Kahneman & Tversky, "On the Reality of Cognitive Illusions", *Psychological Review* 103(3), 582-591 (1996). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Kahneman+Tversky-cognitive-illusions-1996.pdf (accessed 2026-11-15)
[^s6]: Gray, *Probability, statistics, and the likelihood ratio for non-experts*, section 4.16, Leverhulme Research Centre for Forensic Science, University of Dundee. https://lrcfs-ap2.dundee.ac.uk/lr_book/prosecutor-fallacy.html (accessed 2026-11-15)
