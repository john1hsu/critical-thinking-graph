---
id: ct:hot-hand-fallacy
type: ProbabilisticFallacy
title: Hot-hand fallacy
aliases: [hot hand fallacy, hot-hand belief, belief in streak shooting, positive recency bias]
domain: probabilistic-reasoning
summary: >-
  The belief that a person who has just succeeded several times in a row is
  now more likely to succeed again, read from a short streak even when the
  sequence of outcomes is no more streaky than chance would produce.
level: intermediate
evidenceStatus: contested
broader: [ct:probabilistic-fallacy]
related: [ct:gamblers-fallacy, ct:law-of-small-numbers, ct:regression-to-the-mean, ct:selection-bias, ct:correcting-erroneous-perceptions-of-randomness]
requires: [ct:conditional-probability]
relations:
  - {predicate: introducedBy, object: ct:thomas-gilovich, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:gilovich-vallone-tversky-1985-hot-hand-study, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:law-of-small-numbers, source: s1, confidence: high}
  - {predicate: challengedBy, object: ct:miller-sanjurjo-2018-streak-selection-bias-study, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:avugos-2013-hot-hand-meta-analysis, source: s5, confidence: medium}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s4, confidence: medium}
criticalQuestions:
  - How long is the record behind this streak, and how often would a streak this long turn up by chance in a record that size?
  - Is there a plausible mechanism, such as confidence, warm-up or an easier stretch of cases, that could make success genuinely depend on recent success?
  - Has the streak been compared with the person's long-run success rate, or only with my impression of it?
  - If the streak measure was computed from the same short sequence, has it been corrected for streak selection bias?
  - Would I still back this person if I had not seen the last few outcomes?
argumentMap:
  premises:
    - "A recruiter has filled her last four open roles within a week each."
    - "Her long-run record is that about half of her roles fill within a week."
  conclusion: "She is on a hot streak, so the next hard-to-fill role is very likely to close within a week if we give it to her."
  verdict: fallacious
  objections:
    - "A run of four quick fills is common for someone with a 50% rate over a year of roles; the streak alone barely moves the estimate for the next role."
    - "If the recent roles were easier or in a hotter market, the streak reflects the cases, not a change in her skill."
sources:
  - id: s1
    title: "The hot hand in basketball: On the misperception of random sequences"
    publisher: Cognitive Psychology 17(3), 295-314 (Gilovich, Vallone & Tversky, 1985), CAUSE statistics education resource record
    url: https://www.causeweb.org/cause/node/5621
    type: academic
    accessed: 2026-11-15
  - id: s2
    title: "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers"
    publisher: Econometrica 86(6), 2019-2047 (Miller & Sanjurjo, 2018), CORE open-access copy
    url: https://core.ac.uk/download/168384492.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers"
    publisher: Econometrica 86(6), 2019-2047 (Miller & Sanjurjo, 2018), Econometric Society abstract page
    url: https://econometricsociety.org/publications/econometrica/2018/11/01/surprised-hot-hand-fallacy-truth-law-small-numbers
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "The hot hand fallacy and the gambler's fallacy: Two faces of subjective randomness?"
    publisher: Memory & Cognition 32(8), 1369-1378 (Ayton & Fischer, 2004), City, University of London author copy
    url: https://www.staff.city.ac.uk/~sj361/p1369.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "The \"hot hand\" reconsidered: A meta-analytic approach"
    publisher: Psychology of Sport and Exercise 14(1), 21-27 (Avugos, Köppen, Czienskowski, Raab & Bar-Eli, 2013), Ben-Gurion University research portal
    url: https://cris.bgu.ac.il/en/publications/the-hot-hand-reconsidered-a-meta-analytic-approach/
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Hot-hand fallacy

The hot-hand fallacy is the belief that someone who has just succeeded several times in a row has become more likely to succeed on the next try, so that a short streak is read as evidence of a temporary rise in skill. It is the mirror image of the gambler's fallacy: instead of expecting a run to reverse, the believer expects it to continue.[^s1][^s4] Whether the belief is actually a fallacy, rather than a sometimes-reasonable inference made from poor evidence, is now disputed (see Evidence).[^s2][^s3]

## Origin

The term comes from Thomas Gilovich, Robert Vallone and Amos Tversky's 1985 paper in *Cognitive Psychology*. They found that basketball players and fans widely believed in "streak shooting" and that coaches acted on it by feeding the ball to whoever had made the last few shots. Their shooting data, however, showed no reliable tendency for hits to follow hits.[^s1] They linked the belief to the gambler's fallacy and to a "belief in the law of small numbers", the expectation that short sequences should look like the long-run process, and suggested that runs of hits are simply more memorable than mixed sequences.[^s1]

## How it works

Random sequences contain more and longer runs than intuition suggests, so an observer who expects chance to look evenly mixed reads an ordinary run of hits as a change in the shooter.[^s1][^s4] Ayton and Fischer (2004) proposed that the expectation depends on the kind of process. In their experiments, people treated sequences from human performance as likely to continue (positive recency) and sequences from inanimate devices such as roulette as likely to alternate (negative recency). Highly streaky sequences were more often attributed to a skilled human than to chance.[^s4]

The argument map gives a workplace version. A recruiter who fills about half of her roles within a week has just filled four in a row that fast, and a manager concludes she is "hot" and will almost certainly close the next difficult role quickly. A run of four is unremarkable in a year's worth of roles at that rate, and the recent roles may simply have been easier. The streak by itself barely changes the forecast for the next case.[^s1][^s4]

## How to spot it

Watch for "she's on fire", "we're on a roll" or "ride the hot hand" used to justify a decision about the next case, especially when the evidence is a handful of recent outcomes.[^s1] Typical settings are allocating work to whoever had the latest wins, doubling down on a fund manager after a few good quarters, or judging a new process by its first few results. The tell is that the streak is being compared with an impression of the person's normal rate rather than with their measured long-run rate and with how often such streaks occur by chance.[^s1][^s4]

## How to counter it

Start from the person's long-run success rate and ask how often a streak of this length would arise by chance in a record that size; long streaks are common in long records.[^s1] Ask whether a real mechanism could make success depend on recent success, because the error lies in reading dependence into outcomes that do not show it, not in believing that performance ever varies.[^s2][^s4] When analysing streak data yourself, beware of computing "success rate after a streak" within short sequences: that statistic is biased downward under pure chance, so it should be corrected or replaced by permutation tests.[^s2]

## Evidence

For three decades the original finding held up. A 2013 meta-analysis by Avugos and colleagues screened about 250 papers and pooled 56 effect sizes from 30 sports studies published between 1985 and 2012. The mean effect was small (0.02) and not significant, which the authors read as support for the conclusion that a general hot hand in sport probably does not exist.[^s5]

Joshua Miller and Adam Sanjurjo (2018) then showed that the standard measure carried a hidden bias. In a finite sequence of fair coin flips, the expected proportion of heads on flips that follow a head is below one half; with three flips it is 5/12. They call this streak selection bias, and it grows with streak length and shrinks with sequence length.[^s2][^s3] In the 1985 controlled shooting study of 26 Cornell players, a player with a fixed 50% rate taking 100 shots would be expected to shoot about 8 percentage points worse after three hits than after three misses. Against that benchmark the players' small positive difference becomes an average hot-hand effect of about 13 percentage points, statistically significant, and permutation tests that avoid the bias agree.[^s2] The authors conclude that the canonical study's conclusion reverses, and that belief in a hot hand is not clearly a cognitive illusion, though people may still overestimate its size.[^s2][^s3] The meta-analysis above predates this correction, so its pooled null may itself be biased toward zero.[^s2][^s5] The present consensus is therefore contested: streak-reading from short records remains error-prone, but the strong claim that hot hands never exist is no longer secure.[^s2][^s4]

## Connections

- **Introduced by** Thomas Gilovich and Amos Tversky (with Robert Vallone) and **demonstrated by** their 1985 basketball study.[^s1]
- **Explained by** the law of small numbers: short runs are expected to look like the long-run mix, so ordinary streaks look meaningful.[^s1]
- **Challenged by** Miller and Sanjurjo's 2018 streak-selection-bias analysis, which reverses the original study's conclusion.[^s2][^s3]
- **Supported by** the 2013 sports meta-analysis that found no pooled hot-hand effect, though it used pre-correction measures.[^s5]
- **Studied in** judgment and decision making as one of two opposite beliefs about randomness, alongside the gambler's fallacy.[^s4]
- **Related to** the gambler's fallacy (its negative-recency mirror image), regression to the mean, selection bias and techniques for correcting erroneous perceptions of randomness.[^s1][^s2][^s4]

## Sources

[^s1]: Gilovich, Vallone & Tversky, "The hot hand in basketball: On the misperception of random sequences", Cognitive Psychology 17(3), 1985 (CAUSE resource record). https://www.causeweb.org/cause/node/5621 (accessed 2026-11-15)
[^s2]: Miller & Sanjurjo, "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers", Econometrica 86(6), 2018 (CORE copy). https://core.ac.uk/download/168384492.pdf (accessed 2026-11-15)
[^s3]: Miller & Sanjurjo, "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers", Econometrica 86(6), 2018 (Econometric Society page). https://econometricsociety.org/publications/econometrica/2018/11/01/surprised-hot-hand-fallacy-truth-law-small-numbers (accessed 2026-11-15)
[^s4]: Ayton & Fischer, "The hot hand fallacy and the gambler's fallacy: Two faces of subjective randomness?", Memory & Cognition 32(8), 2004. https://www.staff.city.ac.uk/~sj361/p1369.pdf (accessed 2026-11-15)
[^s5]: Avugos, Köppen, Czienskowski, Raab & Bar-Eli, "The 'hot hand' reconsidered: A meta-analytic approach", Psychology of Sport and Exercise 14(1), 2013. https://cris.bgu.ac.il/en/publications/the-hot-hand-reconsidered-a-meta-analytic-approach/ (accessed 2026-11-15)
