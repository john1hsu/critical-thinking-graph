---
id: ct:gamblers-fallacy
type: ProbabilisticFallacy
title: Gambler's fallacy
aliases: [Monte Carlo fallacy, fallacy of the maturity of chances, negative recency bias]
domain: probabilistic-reasoning
summary: >-
  The mistaken belief that, in a sequence of independent random events, an
  outcome becomes less likely after it has occurred several times in a row
  (or "due" after it has not), as if chance corrected itself in the short run.
level: introductory
evidenceStatus: robust
broader: [ct:probabilistic-fallacy]
related: [ct:regression-to-the-mean, ct:base-rate-neglect, ct:conjunction-fallacy]
requires: [ct:conditional-probability]
relations:
  - {predicate: explainedBy, object: ct:representativeness-heuristic, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:law-of-small-numbers, source: s3, confidence: high}
  - {predicate: introducedBy, object: ct:pierre-simon-laplace, source: s1, confidence: medium}
  - {predicate: contrastsWith, object: ct:hot-hand-fallacy, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:croson-sundali-2005-roulette-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:chen-moskowitz-shue-2016-sequential-decisions-study, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:many-labs-1-replication-project, source: s4, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s5, confidence: medium}
criticalQuestions:
  - Are these events actually independent, or is there a real mechanism linking one outcome to the next?
  - If I had walked in just now and not seen the streak, would my estimate for the next outcome be any different?
  - Am I expecting a short run to look like the long-run average?
  - Is my judgment on this case being pulled by how I decided the last few cases rather than by its own merits?
argumentMap:
  premises:
    - "The quality team's random spot-check has passed the last seven shipments in a row."
    - "Inspections fail about one time in ten over the long run, and each shipment is checked independently."
  conclusion: "The next shipment is now very likely to fail, so we should flag it before it is even inspected."
  verdict: fallacious
  objections:
    - "If each check is independent, the chance the next one fails is still about one in ten; seven passes do not create a debt that the next shipment must repay."
sources:
  - id: s1
    title: "The Gambler's Fallacy and the Hot Hand: Empirical Data from Casinos"
    publisher: Journal of Risk and Uncertainty 30(3), 195-209 (Croson & Sundali, 2005), UC Berkeley Statistics course copy
    url: https://www.stat.berkeley.edu/~aldous/157/Papers/croson.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "Decision-Making under the Gambler's Fallacy: Evidence from Asylum Judges, Loan Officers, and Baseball Umpires"
    publisher: NBER Working Paper 22026 (Chen, Moskowitz & Shue, 2016), published in The Quarterly Journal of Economics 131(3)
    url: https://www.nber.org/papers/22026
    type: primary
    accessed: 2026-11-07
  - id: s3
    title: "The retrospective gambler's fallacy: Unlikely events, constructing the past, and multiple universes"
    publisher: Judgment and Decision Making 4(5), 326-334 (Oppenheimer & Monin, 2009)
    url: https://dlab.sauder.ubc.ca/sjdm/journal/9609/jdm9609.html
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Investigating variation in replicability: A 'many labs' replication project"
    publisher: Social Psychology 45(3), 142-152 (Klein et al., 2014), Penn State research portal
    url: https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s5
    title: "Biases in casino betting: The hot hand and the gambler's fallacy"
    publisher: Judgment and Decision Making 1(1), 1-12 (Sundali & Croson, 2006)
    url: https://dlab.sauder.ubc.ca/sjdm/journal/06001/jdm06001.htm
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s6
    title: "Gambler's fallacy, hot hand and the law of small numbers (ST222 lecture notes)"
    publisher: Department of Statistics, University of Warwick (Brettschneider)
    url: https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/brettschneider/st222-resources-2017-18/st222_2016_week8_lec3.pdf
    type: academic
    accessed: 2026-11-07
  - id: s7
    title: "Gambler's Fallacy"
    publisher: Online Statistics Education, ch. 5.4 (David M. Lane, Rice University; XYZ Homework open edition)
    url: https://oer.xyzhomework.com/ebooks/html/online-statistics-education/ch05/5-4-gambler-s-fallacy.html
    type: textbook
    accessed: 2026-11-07
  - id: s8
    title: "Data from Investigating Variation in Replicability: A 'Many Labs' Replication Project"
    publisher: Journal of Open Psychology Data (Klein et al., 2014), CORE copy
    url: https://core.ac.uk/download/420823721.pdf
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Gambler's fallacy

The gambler's fallacy is the belief that a run of one outcome in an independent random process makes the opposite outcome more likely next time, as though the process owed a correction. After five heads, tails feels "due"; after a string of reds at roulette, black feels overdue. Formally, it is a belief in negative autocorrelation in a sequence whose trials are in fact independent.[^s1] A fair coin has no memory, so the probability of tails on the next flip is one half whatever came before.[^s6][^s7]

## Origin

Croson and Sundali credit Pierre-Simon Laplace's early nineteenth-century essay on probability with the first published description of the error.[^s1] Its modern explanation comes from Amos Tversky and Daniel Kahneman's 1971 "belief in the law of small numbers": people expect even short samples to look like the population they came from, so a short streak seems unrepresentative and in need of balancing.[^s1][^s3] The best-known illustration is often dated to Monte Carlo in 1913, when a roulette wheel reportedly landed on black 26 times running and players lost heavily betting that red had to come next; a 26-black run on such a wheel has a probability of roughly 1 in 67 million.[^s6]

## How it works

The error misapplies the law of large numbers. Over many fair coin flips the proportion of heads settles near 0.5, but this happens because early streaks are swamped by later flips, not because later flips compensate for them; in simulations the raw gap between heads and tails tends to grow even as the proportion converges.[^s7] Believers in the fallacy treat the long-run proportion as a quota that a short run must meet.[^s6][^s7]

The argument map gives a workplace version. Seven independent spot-checks have passed, inspections fail about one time in ten, so a manager concludes the next shipment is very likely to fail. With independent checks, the chance is still about one in ten. Seven passes create no debt for the next shipment to repay.[^s6][^s7]

The same expectation runs backwards. Oppenheimer and Monin (2009) found that people who saw an unusual outcome inferred that more trials had come before it. Stanford students told they had walked in on a man rolling three sixes estimated 34.2 earlier rolls on average, compared with 10.6 for two sixes and 3.2 for two sixes and a three. The authors call this the retrospective gambler's fallacy.[^s3]

## How to spot it

Listen for "due", "overdue", "it has to turn" or "we've been lucky too long" applied to independent events.[^s6] A subtler sign is a decision that depends on the previous few decisions rather than the case at hand. Chen, Moskowitz and Shue (2016) found negative autocorrelation in refugee asylum rulings, loan application reviews and Major League Baseball pitch calls: after a run of approvals or strike calls, decision-makers became less likely to repeat that decision, regardless of the merits.[^s2] The pattern was stronger for less experienced decision-makers, after longer streaks, when consecutive cases were similar or close in time, and when incentives for accuracy were weaker.[^s2]

## How to counter it

First, ask whether the events really are independent; the fallacy is a belief in negative dependence where there is none, so a process with a real mechanism linking outcomes needs a different analysis.[^s1] Where they are independent, restate the question without the history ("what is the chance of a failure on any single check?") and look up the base rate.[^s7] In sequential review work, such as hiring, grading, credit or quality control, judge each case against a fixed standard or checklist, and avoid ordering cases so that similar ones arrive back to back; these are the conditions under which Chen and colleagues found the bias strongest.[^s2]

## Evidence

Field data show the fallacy in real betting. Croson and Sundali (2005) coded 24,131 bets by 139 players from 18 hours of roulette video at a Reno casino. Betting against a streak was no more common than chance after runs of one to four. After five identical outcomes it became significant, and after six or more, 85% of bets went against the streak.[^s1] A follow-up analysis found individual differences. Among classifiable gamblers, about as many bet on recently hit numbers as bet on numbers they considered due.[^s5] The retrospective form replicated in the Many Labs 1 project, which tested 13 effects in 36 samples with 6,344 participants; 10 replicated consistently, and the retrospective gambler's fallacy, one of the effects tested, was not among the failures.[^s4][^s8] The high-stakes field results are economically meaningful but come from observational data, and their authors could not fully rule out sequential contrast effects.[^s2]

## Connections

- **Explained by** the representativeness heuristic and the law of small numbers: short sequences are expected to resemble the long-run mix.[^s1][^s3]
- **Introduced by** Pierre-Simon Laplace, who gave the first published account according to Croson and Sundali.[^s1]
- **Contrasts with** the hot-hand fallacy, the opposite belief that streaks will continue (positive rather than negative autocorrelation).[^s1][^s6]
- **Demonstrated by** Croson and Sundali's 2005 roulette study and Chen, Moskowitz and Shue's 2016 study of judges, loan officers and umpires.[^s1][^s2]
- **Supported by** the Many Labs 1 replication of its retrospective form.[^s4][^s8]
- **Studied in** judgment and decision making, where casino and lab data are used to compare competing beliefs about streaks.[^s5]
- **Related to** regression to the mean, base-rate neglect and the conjunction fallacy, other errors in reasoning about chance.[^s6][^s7]

## Sources

[^s1]: Croson & Sundali, "The Gambler's Fallacy and the Hot Hand: Empirical Data from Casinos", Journal of Risk and Uncertainty 30(3), 2005. https://www.stat.berkeley.edu/~aldous/157/Papers/croson.pdf (accessed 2026-11-07)
[^s2]: Chen, Moskowitz & Shue, "Decision-Making under the Gambler's Fallacy: Evidence from Asylum Judges, Loan Officers, and Baseball Umpires", NBER Working Paper 22026 / Quarterly Journal of Economics 131(3), 2016. https://www.nber.org/papers/22026 (accessed 2026-11-07)
[^s3]: Oppenheimer & Monin, "The retrospective gambler's fallacy: Unlikely events, constructing the past, and multiple universes", Judgment and Decision Making 4(5), 2009. https://dlab.sauder.ubc.ca/sjdm/journal/9609/jdm9609.html (accessed 2026-11-07)
[^s4]: Klein et al., "Investigating variation in replicability: A 'many labs' replication project", Social Psychology 45(3), 2014. https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/ (accessed 2026-11-07)
[^s5]: Sundali & Croson, "Biases in casino betting: The hot hand and the gambler's fallacy", Judgment and Decision Making 1(1), 2006. https://dlab.sauder.ubc.ca/sjdm/journal/06001/jdm06001.htm (accessed 2026-11-07)
[^s6]: Brettschneider, ST222 lecture notes on the gambler's fallacy and the law of small numbers, University of Warwick. https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/brettschneider/st222-resources-2017-18/st222_2016_week8_lec3.pdf (accessed 2026-11-07)
[^s7]: Lane (project leader), "Gambler's Fallacy", Online Statistics Education, ch. 5.4, Rice University (XYZ Homework edition). https://oer.xyzhomework.com/ebooks/html/online-statistics-education/ch05/5-4-gambler-s-fallacy.html (accessed 2026-11-07)
[^s8]: Klein et al., "Data from Investigating Variation in Replicability: A 'Many Labs' Replication Project", Journal of Open Psychology Data, 2014. https://core.ac.uk/download/420823721.pdf (accessed 2026-11-07)
