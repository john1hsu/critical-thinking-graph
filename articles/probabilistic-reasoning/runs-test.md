---
id: ct:runs-test
type: Method
title: Runs test
aliases: [Wald-Wolfowitz runs test, Wald–Wolfowitz test, one-sample runs test, runs test for randomness]
domain: probabilistic-reasoning
summary: >-
  A nonparametric significance test that counts the runs (unbroken stretches of
  the same outcome) in a two-valued sequence and compares the count with what a
  random process would produce, so that too few runs signals streakiness and too
  many signals alternation.
level: intermediate
evidenceStatus: normative
broader: [ct:hypothesis-testing]
related: [ct:hot-hand-fallacy, ct:gamblers-fallacy, ct:law-of-small-numbers, ct:correcting-erroneous-perceptions-of-randomness, ct:power-analysis, ct:statistical-reasoning]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: detects, object: ct:hot-hand-fallacy, source: s4, confidence: medium}
  - {predicate: introducedBy, object: ct:abraham-wald, source: s2, confidence: high}
  - {predicate: introducedBy, object: ct:jacob-wolfowitz, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:statistical-process-control, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Runs Test for Detecting Non-randomness (section 1.3.5.13)"
    publisher: NIST/SEMATECH e-Handbook of Statistical Methods, National Institute of Standards and Technology
    url: https://itl.nist.gov/div898/handbook/eda/section3/eda35d.htm
    type: government
    accessed: 2026-11-16
  - id: s2
    title: "Wald-Wolfowitz Test"
    publisher: The SAGE Encyclopedia of Social Science Research Methods (Lewis-Beck, Bryman & Liao, eds.), SAGE Publications
    url: https://sk.sagepub.com/ency/edvol/embed/socialscience/chpt/waldwolfowitz-test
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s3
    title: "Guide to the Statistical Tests (NIST SP 800-22 test suite)"
    publisher: NIST Computer Security Resource Center, Random Bit Generation project
    url: https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software/guide-to-the-statistical-tests
    type: government
    accessed: 2026-11-16
  - id: s4
    title: "Streaks in skilled performance"
    publisher: Psychonomic Bulletin & Review 2(2), 260-265 (Gilden & Gray Wilson, 1995), University of Colorado course-reading copy
    url: https://home.cs.colorado.edu/~mozer/Teaching/syllabi/7782/readings/gilden%20wilson%20pbr.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers"
    publisher: Econometrica 86(6), 2019-2047 (Miller & Sanjurjo, 2018), arXiv author copy
    url: https://arxiv.org/pdf/1902.01265
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Computing the Z Statistic for the One Sample Runs Test (chapter 25)"
    publisher: Applied Statistics in Healthcare Research (Montelpare et al., 2020), University of Prince Edward Island Robertson Library Pressbooks
    url: https://pressbooks.library.upei.ca/montelpare/?p=594
    type: textbook
    accessed: 2026-11-16
created: 2026-11-16
---

# Runs test

The runs test is a simple nonparametric check on whether a sequence of two kinds of outcome (hit/miss, heads/tails, above/below the median) looks like the product of a random process. A run is an unbroken stretch of the same outcome bounded by the other one, so the sequence H H T H H H has three runs. The test counts the runs and asks whether that count is unusually low, which means the outcomes clump into streaks, or unusually high, which means they alternate more than chance would.[^s1][^s3] For critical thinkers its value is that it replaces an impression of "streakiness" with a comparison against what chance actually produces.[^s1][^s4]

## Origin

The two-sample form is credited to Abraham Wald and Jacob Wolfowitz (1940). Their question was whether two independent samples come from the same population: pool the values, sort them, label each by its sample of origin, and count the runs of labels. Well-mixed labels give no reason to think the populations differ, while long blocks of one label suggest they do.[^s2] The same run count, applied to a single ordered sequence, became the standard one-sample test of randomness found in engineering and statistics handbooks.[^s1][^s6] It also survives as one of the tests in NIST's suite for checking random-number generators, where it flags bit streams that switch between 0 and 1 too quickly or too slowly.[^s3]

## How it works

Let n1 and n2 be the counts of the two outcomes and R the observed number of runs. Under the null hypothesis that the order is random, the expected number of runs is 2·n1·n2/(n1 + n2) + 1, and the handbook gives a matching formula for its variance. The test statistic is Z = (R − expected R) / standard deviation of R. When both counts exceed 10, Z is compared with the standard normal distribution, so at the 5% level |Z| above 1.96 indicates non-randomness; smaller samples use tables of exact critical values.[^s1][^s2] A negative Z (too few runs) means outcomes cluster; a positive Z (too many runs) means they alternate.[^s1][^s4]

A workplace example. A support lead tracks whether each day's tickets met the service-level target over 24 working days: 12 days met, 12 missed. The team feels it goes through "hot" and "cold" spells. With 12 and 12, the expected count is 2·12·12/24 + 1 = 13 runs and the standard deviation is about 2.4. If the log shows only 8 runs, Z is about −2.1, so the spells are probably real and worth investigating (a staffing rota, a weekly release). If it shows 12 or 14 runs, the record is about as mixed as coin flips, and a four-day bad patch inside it is not evidence of anything.[^s1][^s6] The UPEI textbook works the same calculation for 20 coin tosses and finds a Z near zero.[^s6]

## How to apply it

1. **Code the sequence into two categories**, for example success/failure, or values above/below the median for numerical data.[^s1]
2. **Count each outcome and the runs**, then compute the expected runs, the standard deviation and Z, or use exact tables when either count is 10 or fewer.[^s1][^s2]
3. **Read the direction**: too few runs suggests momentum, drift or batching; too many suggests over-correction or a forced alternation.[^s1][^s3]
4. **Act on the result**: in process monitoring, a failed randomness check means the simple "constant level plus noise" model does not hold and a time-series model is needed.[^s1]

Pitfalls. The test is deliberately general, and its generality costs power: it is not very powerful against any particular departure from randomness.[^s2] Miller and Sanjurjo note that the runs test, the serial-correlation test and the one-shot conditional-probability test amount to roughly the same test, and that these tests lack the power to detect hot-hand shooting because one hit is only a weak signal of a change in underlying ability.[^s5] A non-significant result in a short record is therefore weak evidence that no streakiness exists. Gilden and Wilson add that run counts depend on the hit rate, so for unequal rates they used the exact distribution and pooled z scores across many sequences instead of judging one short series.[^s4]

## Evidence and use in the hot-hand debate

Gilovich, Vallone and Tversky's 1985 study of basketball shooting analysed run counts and serial correlations alongside conditional hit rates and found no excess streakiness, which grounded the claim that belief in the hot hand is a misperception of random sequences.[^s4][^s5] Gilden and Wilson (1995) applied runs z scores to 300-putt golf sequences from 40 players and found significantly fewer runs than a random process would produce, with 12.5% of sequences beyond z = −2 against about 2.3% expected by chance; darts streaks appeared only at intermediate difficulty. They concluded that streaks in skilled performance are not always illusory.[^s4] Miller and Sanjurjo's 2018 reanalysis later reversed the basketball conclusion using bias-corrected conditional-probability and permutation tests, while noting that runs-type tests were underpowered for the question.[^s5] The lesson for practice is that the runs test is a good first screen against reading patterns into noise, but it should not be treated as proof that no pattern exists.[^s4][^s5]

## Connections

- **Narrower than** hypothesis testing: it is a significance test whose null hypothesis is a random ordering.[^s1]
- **Introduced by** Abraham Wald and Jacob Wolfowitz in their 1940 two-sample test.[^s2]
- **Detects** the hot-hand fallacy: counting runs against the chance benchmark is how researchers check whether perceived streaks are present in the data.[^s4][^s5]
- **Applied in** statistical process control, where randomness is a core assumption for judging whether a process is in control, and in testing random-number generators.[^s1][^s3]
- **Related to** the gambler's fallacy and the law of small numbers, the intuitions about runs that the test checks against arithmetic; to techniques for correcting erroneous perceptions of randomness; and to power analysis, since low power is its main limitation.[^s1][^s5]

## Sources

[^s1]: NIST/SEMATECH, "Runs Test for Detecting Non-randomness", e-Handbook of Statistical Methods, section 1.3.5.13. https://itl.nist.gov/div898/handbook/eda/section3/eda35d.htm (accessed 2026-11-16)
[^s2]: "Wald-Wolfowitz Test", The SAGE Encyclopedia of Social Science Research Methods. https://sk.sagepub.com/ency/edvol/embed/socialscience/chpt/waldwolfowitz-test (accessed 2026-11-16)
[^s3]: NIST CSRC, "Guide to the Statistical Tests", Random Bit Generation project. https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software/guide-to-the-statistical-tests (accessed 2026-11-16)
[^s4]: Gilden & Gray Wilson, "Streaks in skilled performance", Psychonomic Bulletin & Review 2(2), 1995. https://home.cs.colorado.edu/~mozer/Teaching/syllabi/7782/readings/gilden%20wilson%20pbr.pdf (accessed 2026-11-16)
[^s5]: Miller & Sanjurjo, "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers", Econometrica 86(6), 2018 (arXiv copy). https://arxiv.org/pdf/1902.01265 (accessed 2026-11-16)
[^s6]: Ritchie, "Computing the Z Statistic for the One Sample Runs Test", in Montelpare et al., Applied Statistics in Healthcare Research, UPEI Pressbooks, 2020. https://pressbooks.library.upei.ca/montelpare/?p=594 (accessed 2026-11-16)
