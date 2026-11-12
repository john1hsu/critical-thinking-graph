---
id: ct:prosecutors-fallacy
type: ProbabilisticFallacy
title: Prosecutor's fallacy
aliases: [prosecutor fallacy, false positive inversion]
domain: probabilistic-reasoning
summary: >-
  The error of treating the probability that incriminating evidence would turn
  up if the accused were innocent (for example, a random match probability) as
  if it were the probability that the accused is innocent given that evidence.
level: intermediate
evidenceStatus: normative
broader: [ct:probabilistic-fallacy, ct:inverse-fallacy]
related: [ct:conditional-probability, ct:base-rate-neglect, ct:bayesian-reasoning, ct:natural-frequencies, ct:legal-reasoning, ct:likelihood-ratio]
requires: [ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:william-c-thompson, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:thompson-schumann-1987-jury-fallacy-experiments, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:defense-attorneys-fallacy, source: s1, confidence: high}
  - {predicate: instanceOf, object: ct:inverse-fallacy, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:bayesian-reasoning, source: s3, confidence: medium}
criticalQuestions:
  - Is the figure being quoted the chance of the evidence if the person is innocent, or the chance the person is innocent given the evidence?
  - Before this evidence, how many people could plausibly have been responsible?
  - Out of everyone who could have produced this evidence by coincidence, how many would we expect to find?
  - How much more likely is the evidence if the person is responsible than if they are not?
  - Does the rest of the case make guilt likely or unlikely before this evidence is added?
argumentMap:
  premises:
    - "The badge reader logged a card whose partial ID matches this employee's card."
    - "Only 1 in 1,000 cards in the building system would share that partial ID by chance."
  conclusion: "So there is a 99.9% chance this employee entered the server room."
  verdict: fallacious
  scheme: ct:bayesian-reasoning
  objections:
    - "With about 5,000 cards on the system, roughly five would match by chance, so without other evidence the match alone points to one of about six cardholders."
    - "The 1-in-1,000 figure is the probability of a match if the employee did not enter, not the probability the employee did not enter given the match."
sameAs: []
sources:
  - id: s1
    title: "Interpretation of Statistical Evidence in Criminal Trials: The Prosecutor's Fallacy and the Defense Attorney's Fallacy"
    publisher: Law and Human Behavior 11(3), 167-187 (Thompson & Schumann, 1987), course copy hosted by Joel Velasco
    url: https://www.joelvelasco.net/teaching/122/thompson&schumann87-statisticslaw.pdf
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "A Systematic Account of Probabilistic Fallacies in Legal Fact-Finding"
    publisher: International Journal of Evidence & Proof 28(1), 45-64 (Dahlman, 2024), Lund University Publications
    url: https://lup.lub.lu.se/search/files/163710477/dahlman_2023_a_systematic_account_of_probabilistic_fallacies_in_legal_fact_finding.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Probabilities for propositions (section 4.16), Probability, statistics, and the likelihood ratio for non-experts"
    publisher: Leverhulme Research Centre for Forensic Science, University of Dundee (Gray)
    url: https://lrcfs-ap2.dundee.ac.uk/lr_book/prosecutor-fallacy.html
    type: textbook
    accessed: 2026-11-12
  - id: s4
    title: "Letter from the President of the Royal Statistical Society to the Lord Chancellor regarding the use of statistical evidence in court cases"
    publisher: Royal Statistical Society (Green, 23 January 2002)
    url: https://www.rss.org.uk/RSS/media/File-library/Membership/Sections/2020/Sally-Clark-RSS-letter-2002.pdf
    type: institutional
    accessed: 2026-11-12
  - id: s5
    title: "Lay Understanding of Forensic Statistics: Evaluation of Random Match Probabilities, Likelihood Ratios, and Verbal Equivalents"
    publisher: Law and Human Behavior 39(4), 332-349 (Thompson & Newman, 2015), Australian National University research portal
    url: https://researchportalplus.anu.edu.au/en/publications/lay-understanding-of-forensic-statistics-evaluation-of-random-mat/
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Prosecutor's fallacy

The prosecutor's fallacy is the mistake of reading the probability of the evidence given innocence as if it were the probability of innocence given the evidence. If a blood type found at a crime scene occurs in 10% of people, the fallacious step is to conclude that a matching defendant is 90% likely to be guilty, as though the match alone settled the question and the rest of the case did not matter.[^s1] In probability notation it swaps P(evidence | not guilty) for P(not guilty | evidence). Forensic texts describe it as illegitimately transposing the conditional, and stress that anyone, not only prosecutors, can commit it.[^s3]

## Origin

Psychologists William C. Thompson and Edward Schumann named the error in a 1987 article in *Law and Human Behavior*. The same article named its mirror image, the defense attorney's fallacy.[^s1][^s3] They framed both as ways lay jurors and lawyers might misread incidence-rate statistics such as blood-type or hair-sample frequencies, which were then becoming common in criminal trials.[^s1] Legal theorist Christian Dahlman later argued that the generic labels "inverse fallacy" and "transposed conditional" blur two distinct errors. He calls the prosecutor's version *false positive inversion*, swapping P(E | not-H) with P(not-H | E), and separates it from *true positive inversion*, swapping P(E | H) with P(H | E).[^s2]

## How it works

The argument map above shows a workplace version. A partial card ID that only 1 in 1,000 cards would share by chance sounds damning. But the 1-in-1,000 figure answers "how likely is this match if the employee is not the one?", not "how likely is it that the employee is not the one?". With 5,000 cards on the system, about five other cardholders would match by coincidence. If nothing else singles out this employee, the match narrows the field to roughly six people, not to one.[^s1] Dahlman gives a numerical illustration of how large the gap can be: with a 1% prior, a 90% true-positive rate and a 10% false-positive rate, the probability of guilt after a positive identification is about 8%, not the roughly 90% the inversion suggests.[^s2] The same arithmetic appears in medical testing, where a test with 95% sensitivity and specificity for a condition affecting 1% of people still leaves a positive scorer only about 28% likely to have it.[^s3]

The best-known real case is the trial of Sally Clark in England. An expert squared an estimated rate of sudden infant death to claim a 1-in-73-million chance of two such deaths in one family. In 2002 the Royal Statistical Society told the Lord Chancellor that the calculation was invalid, because it wrongly assumed the two deaths were independent. It added that reading the figure as the chance the deaths were accidental was the prosecutor's fallacy. The proper comparison was how likely two deaths were under each explanation, double sudden infant death or double murder.[^s4]

## How to spot it

Listen for a small probability of coincidence turned straight into a large probability of guilt or responsibility ("only a one-in-a-million chance it's someone else").[^s1] Check which way the conditional runs: an expert's match statistic is conditioned on the innocence hypothesis, so it cannot by itself say how likely that hypothesis is.[^s3] Be most suspicious when the other evidence is weak, because Thompson and Schumann note the error misleads most when the prior probability of guilt is low.[^s1] In investigations, audits and fraud reviews, the same pattern appears whenever a rare match is treated as identifying a culprit without asking how many others could produce it.[^s2]

## How to counter it

Ask the expert to state both probabilities: how likely the evidence is if the person is responsible, and how likely it is if they are not. The ratio of these two numbers, the likelihood ratio, measures the evidence's strength. Judging the probability of the propositions themselves is left to the fact finder, who must combine that strength with everything else in the case.[^s3] Restating a rate as counts of people also helps: in Thompson and Schumann's first experiment, 22.2% of participants committed the prosecutor's fallacy when a 2% hair-match rate was given as a conditional probability, against 4.2% when it was given as a percentage plus a count of people in a city of one million.[^s1] Avoid overcorrecting into the defense attorney's fallacy, which treats a match as worthless because many people share the trait; a match that narrows a million possible sources to a few thousand is still strong evidence.[^s1]

## Connections

- **Instance of the inverse fallacy.** It is the special case of swapping a conditional in which the evidence is conditioned on innocence; Dahlman treats it as one of two inversion sub-types.[^s2]
- **Introduced by William C. Thompson** with Edward Schumann, whose 1987 experiments also **demonstrated** how jurors handle such statistics.[^s1]
- **Contrasts with the defense attorney's fallacy.** In their second experiment, 66% of 73 participants made at least one defense attorney's error, against only 4% for the prosecutor's error; overall, people tended to underuse statistical evidence.[^s1] A 2015 study of 541 online participants likewise found that misreadings matching the defense attorney's fallacy and the related source probability error were common and shaped verdicts.[^s5]
- **Contrasts with Bayesian reasoning**, which updates a prior probability of a proposition by the likelihood of the evidence under competing propositions instead of reading one conditional probability as the answer.[^s3]
- **Related to base-rate neglect and conditional probability.** Dahlman argues base-rate neglect follows from both inversions, and is a separate error only when a fact finder ignores base rates in its own right.[^s2]

## Sources

[^s1]: Thompson & Schumann, "Interpretation of Statistical Evidence in Criminal Trials: The Prosecutor's Fallacy and the Defense Attorney's Fallacy", *Law and Human Behavior* 11(3) (1987): 167–187. https://www.joelvelasco.net/teaching/122/thompson&schumann87-statisticslaw.pdf (accessed 2026-11-12)
[^s2]: Dahlman, "A Systematic Account of Probabilistic Fallacies in Legal Fact-Finding", *International Journal of Evidence & Proof* 28(1) (2024): 45–64. https://lup.lub.lu.se/search/files/163710477/dahlman_2023_a_systematic_account_of_probabilistic_fallacies_in_legal_fact_finding.pdf (accessed 2026-11-12)
[^s3]: Gray, "Probabilities for propositions", in *Probability, statistics, and the likelihood ratio for non-experts*, Leverhulme Research Centre for Forensic Science, University of Dundee. https://lrcfs-ap2.dundee.ac.uk/lr_book/prosecutor-fallacy.html (accessed 2026-11-12)
[^s4]: Green, letter to the Lord Chancellor on the Sally Clark case, Royal Statistical Society, 23 January 2002. https://www.rss.org.uk/RSS/media/File-library/Membership/Sections/2020/Sally-Clark-RSS-letter-2002.pdf (accessed 2026-11-12)
[^s5]: Thompson & Newman, "Lay Understanding of Forensic Statistics: Evaluation of Random Match Probabilities, Likelihood Ratios, and Verbal Equivalents", *Law and Human Behavior* 39(4) (2015): 332–349. https://researchportalplus.anu.edu.au/en/publications/lay-understanding-of-forensic-statistics-evaluation-of-random-mat/ (accessed 2026-11-12)
