---
id: ct:contingency-table
type: Technique
title: Contingency table
aliases: [2 × 2 table, fourfold table, two-by-two table]
domain: probabilistic-reasoning
summary: >-
  A table that cross-tabulates two yes/no variables so that all four
  combinations (and their totals) are visible at once, used to judge whether
  two things are associated and to read conditional probabilities in either
  direction without confusing one for its inverse.
level: introductory
evidenceStatus: mixed
broader: [ct:statistical-reasoning]
related: [ct:conditional-probability, ct:natural-frequencies, ct:inverse-fallacy, ct:base-rate-neglect, ct:bayesian-reasoning, ct:correlation-versus-causation, ct:illusory-correlation, ct:simpsons-paradox, ct:truth-table, ct:carroll-diagram]
requires: [ct:conditional-probability]
relations:
  - {predicate: detects, object: ct:inverse-fallacy, source: s1, confidence: medium}
  - {predicate: counteracts, object: ct:causal-illusion, source: s3, confidence: medium}
  - {predicate: supportedBy, object: ct:binder-krauss-bruckmaier-2015-visualization-study, source: s2, confidence: high}
  - {predicate: challengedBy, object: ct:jenkins-ward-1965-contingency-judgment-study, source: s4, confidence: medium}
  - {predicate: contrastsWith, object: ct:frequency-tree, source: s3, confidence: medium}
  - {predicate: formalizedBy, object: ct:george-udny-yule, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "An Eye-Tracking Study of Statistical Reasoning With Tree Diagrams and 2 × 2 Tables"
    publisher: "Bruckmaier, Binder, Krauss & Kufner, Frontiers in Psychology 10:632 (2019)"
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00632/pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Effects of visualizing statistical information – an empirical study on tree diagrams and 2 × 2 tables"
    publisher: "Binder, Krauss & Bruckmaier, Frontiers in Psychology 6:1186 (2015)"
    url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01186/pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Presentation format influences the strength of causal illusions"
    publisher: "Barreiro, Del Carpio, Rodríguez-Ferreiro & Barberia, Memory & Cognition 53, 2347–2363 (2025); University of Barcelona repository"
    url: https://diposit.ub.edu/items/1d41ae70-1740-4000-abcb-84a9cfb0d209/full
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Judgment of Contingency Between Responses and Outcomes"
    publisher: "Jenkins & Ward, Psychological Monographs: General and Applied 79(1), Whole No. 594 (1965)"
    url: https://pages.ucsd.edu/~mckenzie/Jenkins&Ward1965PsychMonographs.pdf
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "A Cross-Study Analysis of Covariation Judgments"
    publisher: "Lipe, Center for Decision Research, University of Chicago (Office of Naval Research technical report, 1982)"
    url: https://apps.dtic.mil/sti/pdfs/ADA136989.pdf
    type: academic
    accessed: 2026-11-16
  - id: s6
    title: "Yule, George Udny"
    publisher: "J. D. North, Complete Dictionary of Scientific Biography (2008), via MacTutor, University of St Andrews"
    url: https://mathshistory.st-andrews.ac.uk/DSB/Yule.pdf
    type: academic
    accessed: 2026-11-16
created: 2026-11-16
---

# Contingency table

A contingency table, in its simplest 2 × 2 form, crosses two yes/no variables (exposed or not, outcome or not) so that every case falls into one of four cells, with row and column totals alongside.[^s4] Its value for critical thinking is that it puts the cells people tend to ignore on the page next to the one they tend to notice, and it lets a reader compute a conditional probability in either direction by choosing the right row or column.[^s1] Used this way it is a practical check on two classic failures: seeing a link that is not there, and swapping a probability for its inverse.[^s2][^s3]

## Origin

Fourfold tables were a working tool of late-nineteenth-century statistics. According to J. D. North's entry in the *Dictionary of Scientific Biography*, George Udny Yule proposed a coefficient of association for 2 × 2 contingency tables in 1900, which drew a long protest from Karl Pearson.[^s6] The table entered psychology as a way to describe how people judge relationships: Herbert Jenkins and William Ward's 1965 monograph laid out responses and outcomes as cells a, b, c and d and defined contingency as the difference between the outcome rate with and without the response, now usually written ΔP.[^s4] Today 2 × 2 tables are part of the German school mathematics curriculum, and Binder and colleagues note that they have the advantage of being easy to construct.[^s2]

## How it works

Suppose a payments team is told that a fraud filter catches 90% of fraudulent transactions and wrongly flags 5% of legitimate ones, and that 1 in 100 transactions is fraudulent. Out of 10,000 transactions the table reads: flagged and fraudulent 90, flagged and legitimate 495, not flagged and fraudulent 10, not flagged and legitimate 9,405. The question "how likely is a flagged transaction to be fraud?" is answered by the flagged row alone: 90 of 585, about 15%, not 90%. Answering 90% is the "Fisherian" error that Bruckmaier and colleagues catalogue, which consists of reporting the sensitivity instead of the posterior and is the inverse fallacy in applied form.[^s1] Filling the table with natural frequencies, as here, matters: in Binder, Krauss and Bruckmaier's 2015 study of 259 students aged 16 to 18, correct answers rose from 26% with natural frequencies alone to 51% when a table or tree was added, but stayed between 2% and 6% when the same information was given as probabilities.[^s2]

The same layout guards against seeing a pattern in cell a alone. If 30 of 40 projects that used a new planning tool shipped on time, that sounds persuasive until the second row shows that 60 of 80 projects without the tool also shipped on time. Both rates are 75%, so ΔP is zero.[^s4] Jenkins and Ward found that people's judgments of control tracked the number of successes (r = .70) and barely tracked actual contingency, so they often reported control where there was none.[^s4]

## How to apply it

1. Name the two binary variables and draw the four cells before looking at any summary claim.[^s4]
2. Fill the cells with counts, converting percentages to natural frequencies from a round reference population.[^s2]
3. Before computing, say which row or column the question conditions on; that is the step that prevents answering with the inverse.[^s1]
4. For an association claim, compare the outcome rate across rows rather than counting cell a.[^s4][^s5]
5. Where possible show counts as icons rather than bare numbers, or try a frequency tree, which in recent experiments produced weaker causal illusions.[^s3]

## Evidence and limitations

The evidence that tables help is real but uneven. Binder and colleagues found no statistical difference between 2 × 2 tables and tree diagrams, and the benefit depended heavily on using natural frequencies.[^s2] An eye-tracking study by Bruckmaier and colleagues suggested that tables and trees steer people away from different errors: tables seemed to protect against the Fisherian error and trees against reading off a joint frequency, but it had only 24 participants and reported no inferential tests.[^s1] Barreiro and colleagues (2025) found that icon-based contingency tables and frequency trees weakened causal illusions compared with trial-by-trial presentation, whereas numeric tables did not.[^s3] Older work is a caution against assuming the table does the thinking: Jenkins and Ward saw the same bias when frequencies were summarised in a table questionnaire, and Marlys Lipe's 1982 cross-study analysis concluded that people weighted the four cells unequally, leaning on cells a and b, rather than using all of them as the statistical model requires.[^s4][^s5]

## Connections

- **Detects the inverse fallacy.** Choosing the conditioning row or column makes the difference between P(fraud | flag) and P(flag | fraud) visible; Bruckmaier and colleagues report that 2 × 2 tables helped participants avoid the Fisherian error.[^s1]
- **Counteracts causal illusions.** Barreiro and colleagues found weaker causal illusions with icon-based contingency tables than with trial-by-trial data.[^s3]
- **Supported by Binder, Krauss and Bruckmaier (2015).** Visualizations roughly doubled correct Bayesian answers when natural frequencies were used.[^s2]
- **Challenged by Jenkins and Ward (1965).** Their subjects misjudged contingency even when frequencies were summarised for them, so the table is an aid, not a cure.[^s4]
- **Contrasts with the frequency tree.** The two formats perform similarly in some studies but differ in which errors they prevent and in how strongly they reduce causal illusions.[^s1][^s3]
- **Formalized by George Udny Yule.** Yule's 1900 coefficient of association gave the fourfold table a summary measure of association.[^s6]

## Sources

[^s1]: Bruckmaier, Binder, Krauss & Kufner, "An Eye-Tracking Study of Statistical Reasoning With Tree Diagrams and 2 × 2 Tables", *Frontiers in Psychology* 10:632 (2019). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00632/pdf (accessed 2026-11-16)
[^s2]: Binder, Krauss & Bruckmaier, "Effects of visualizing statistical information – an empirical study on tree diagrams and 2 × 2 tables", *Frontiers in Psychology* 6:1186 (2015). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01186/pdf (accessed 2026-11-16)
[^s3]: Barreiro, Del Carpio, Rodríguez-Ferreiro & Barberia, "Presentation format influences the strength of causal illusions", *Memory & Cognition* 53 (2025). https://diposit.ub.edu/items/1d41ae70-1740-4000-abcb-84a9cfb0d209/full (accessed 2026-11-16)
[^s4]: Jenkins & Ward, "Judgment of Contingency Between Responses and Outcomes", *Psychological Monographs* 79(1) (1965). https://pages.ucsd.edu/~mckenzie/Jenkins&Ward1965PsychMonographs.pdf (accessed 2026-11-16)
[^s5]: Lipe, "A Cross-Study Analysis of Covariation Judgments", Center for Decision Research, University of Chicago (1982). https://apps.dtic.mil/sti/pdfs/ADA136989.pdf (accessed 2026-11-16)
[^s6]: North, "Yule, George Udny", *Complete Dictionary of Scientific Biography* (2008), via MacTutor. https://mathshistory.st-andrews.ac.uk/DSB/Yule.pdf (accessed 2026-11-16)
