---
id: ct:likelihood-ratio
type: Framework
title: Likelihood ratio framework
aliases: [likelihood ratio, LR framework, likelihood-ratio approach to evidence evaluation, evaluative reporting]
domain: probabilistic-reasoning
summary: >-
  A way of weighing evidence by comparing how probable the same findings are
  under two competing propositions, P(E | H1) / P(E | H2), so that the strength
  of the evidence is reported separately from how probable either proposition is.
level: intermediate
evidenceStatus: normative
broader: [ct:bayesian-reasoning]
related: [ct:conditional-probability, ct:prosecutors-fallacy, ct:defense-attorneys-fallacy, ct:legal-reasoning, ct:natural-frequencies, ct:base-rate-neglect]
requires: [ct:conditional-probability]
relations:
  - {predicate: counteracts, object: ct:prosecutors-fallacy, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:bayesian-reasoning, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:legal-reasoning, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:thompson-newman-2015-lay-forensic-statistics-study, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Legal Probabilism"
    publisher: Stanford Encyclopedia of Philosophy (Di Bello, 2021)
    url: https://plato.stanford.edu/ENTRIES/legal-probabilism/
    type: scholarly-encyclopedia
    accessed: 2026-11-12
  - id: s2
    title: "ENFSI Guideline for Evaluative Reporting in Forensic Science (approved version 3.0)"
    publisher: European Network of Forensic Science Institutes (2015), copy hosted by Roebuck Forensics
    url: https://roebuckforensics.com.au/wp-content/uploads/2024/07/ENFSI-Guideline.pdf
    type: institutional
    accessed: 2026-11-12
  - id: s3
    title: "Relative support for competing propositions (section 5.1), Probability, statistics, and the likelihood ratio for non-experts"
    publisher: Leverhulme Research Centre for Forensic Science, University of Dundee (Gray)
    url: https://lrcfs-ap2.dundee.ac.uk/lr_book/relative-support-for-competing-propositions.html
    type: textbook
    accessed: 2026-11-12
  - id: s4
    title: "Lay Understanding of Forensic Statistics: Evaluation of Random Match Probabilities, Likelihood Ratios, and Verbal Equivalents"
    publisher: Law and Human Behavior 39 (Thompson & Newman, 2015), eScholarship, University of California
    url: https://escholarship.org/content/qt8g0729b9/qt8g0729b9.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "What is the best way to present likelihood ratios? A review of past research and recommendations for future research"
    publisher: Science and Justice 65(6), 101342 (Morrison, Bali, Martire, Grady & Thompson, 2025), Aston University research portal
    url: https://research.aston.ac.uk/en/publications/what-is-the-best-way-to-present-likelihood-ratios-a-review-of-pas/
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Likelihood ratio framework

The likelihood ratio (LR) framework weighs a piece of evidence by asking two questions instead of one: how probable are these findings if one proposition is true, and how probable are they if a competing proposition is true? The LR is the first probability divided by the second.[^s3] A value above 1 means the findings favour the first proposition, a value below 1 favours the second, and a value of exactly 1 means the evidence does not help choose between them.[^s1][^s3] The framework deliberately reports only the strength of the evidence. How probable each proposition is overall is a separate judgment that also depends on everything else known.[^s2]

## Origin

The framework comes from the odds form of Bayes' theorem: posterior odds equal the likelihood ratio multiplied by the prior odds.[^s1] The Stanford Encyclopedia of Philosophy credits legal scholar Richard Lempert (1977) with establishing the LR as the standard measure of whether evidence is relevant, and notes that later legal and forensic writers built on it.[^s1] In 2015 the European Network of Forensic Science Institutes (ENFSI) made it the basis of its guideline for evaluative reporting. The guideline requires experts to judge findings against at least one pair of competing propositions, typically one from each party.[^s2] It sets four requirements: balance, logic, robustness and transparency.[^s2]

## How it works

Take an everyday workplace case. A fraud analyst sees that a disputed expense claim was submitted from a device whose browser fingerprint matches a particular employee's laptop. Proposition 1 is that the employee submitted it; proposition 2 is that someone else did. Suppose a match is almost certain if the employee did it, while about 1 in 200 other devices in the company would match by coincidence. The LR is then roughly 200: the match is about 200 times more probable if the employee submitted the claim than if someone else did.[^s3] That says nothing yet about whether the employee probably did it. If several thousand staff could have submitted the claim and nothing else points to this person, the prior odds are low, and multiplying them by 200 can still leave the employee more likely innocent than guilty.[^s1]

This separation is what makes the framework a remedy for the prosecutor's fallacy. ENFSI's logic requirement says reports must address the probability of the findings given the propositions, never the reverse. It warns that reading a DNA random match probability as the chance the suspect is not the source is a transposed conditional, a risk it says is greatest after database searches.[^s2] The SEP likewise advises judging a low probability of evidence under one hypothesis by its likelihood ratio rather than on its own.[^s1]

## How to apply it

1. **State two competing propositions** at the same level, for example "this person is the source" versus "someone else is the source".[^s2]
2. **Estimate how probable the findings are under each** and divide. Report the number, a verbal equivalent, or both. ENFSI's indicative scale runs from "weak support" (2 to 10) through "moderate" (10 to 100) to "extremely strong support" (1,000,000 and above).[^s2]
3. **Leave the probability of the propositions to the decision maker**, who combines the LR with prior odds and the rest of the case.[^s2]
4. **Combine items carefully.** The SEP's worked example multiplies separate LRs for hair and DNA evidence, which assumes the items are independent; treating two dependent items, such as two cameras recording the same person, as independent overstates their joint strength.[^s1]

## Limitations

The LR is only as good as the propositions chosen. The SEP notes that an ad hoc alternative can push any evidence's LR to 1, and that a finding can favour one side about the source of a trace and the other about the offence itself.[^s1] Meester and Sjerps (2004), as summarised in the SEP, recommend pairing each LR with a sensitivity analysis over prior probabilities, conceding that an LR alone can be insufficiently informative.[^s1]

The framework also does not guarantee that listeners understand it. In a 2015 experiment with 541 online participants, Thompson and Newman found that people often misread match statistics as the probability that the defendant was the source. This error was endorsed by 86% of those who heard an LR and 78% of those who heard a random match probability, against 26% of those who heard a verbal statement.[^s4] A 2025 review in *Science and Justice* concluded that existing studies still cannot say which way of presenting LRs laypeople understand best, and that none had tested verbal LRs directly.[^s5] The framework disciplines how experts reason; it does not on its own fix how audiences hear the result.

## Connections

- **Explained by Bayesian reasoning.** The LR is the factor that converts prior odds into posterior odds in Bayes' theorem.[^s1]
- **Counteracts the prosecutor's fallacy.** ENFSI's logic requirement and transposed-conditional warning keep experts from stating the probability of a proposition when they have only measured the probability of findings.[^s2]
- **Applied in legal reasoning.** It is the standard measure of relevance and probative value in legal probabilism and forensic reporting.[^s1]
- **Challenged by Thompson and Newman's 2015 study**, which found that lay jurors still transposed conditionals when given LRs.[^s4]
- **Related to the defense attorney's fallacy**, which that study also found common, and to natural frequencies and base-rate neglect, other ways of keeping conditional probabilities straight.[^s4]

## Sources

[^s1]: Di Bello, "Legal Probabilism", Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/ENTRIES/legal-probabilism/ (accessed 2026-11-12)
[^s2]: European Network of Forensic Science Institutes, *ENFSI Guideline for Evaluative Reporting in Forensic Science*, version 3.0 (2015). https://roebuckforensics.com.au/wp-content/uploads/2024/07/ENFSI-Guideline.pdf (accessed 2026-11-12)
[^s3]: Gray, "Relative support for competing propositions", in *Probability, statistics, and the likelihood ratio for non-experts*, Leverhulme Research Centre for Forensic Science, University of Dundee. https://lrcfs-ap2.dundee.ac.uk/lr_book/relative-support-for-competing-propositions.html (accessed 2026-11-12)
[^s4]: Thompson & Newman, "Lay Understanding of Forensic Statistics: Evaluation of Random Match Probabilities, Likelihood Ratios, and Verbal Equivalents", *Law and Human Behavior* 39 (2015). https://escholarship.org/content/qt8g0729b9/qt8g0729b9.pdf (accessed 2026-11-12)
[^s5]: Morrison, Bali, Martire, Grady & Thompson, "What is the best way to present likelihood ratios? A review of past research and recommendations for future research", *Science and Justice* 65(6) (2025). https://research.aston.ac.uk/en/publications/what-is-the-best-way-to-present-likelihood-ratios-a-review-of-pas/ (accessed 2026-11-12)
