---
id: ct:representativeness-heuristic
type: Heuristic
title: Representativeness heuristic
aliases: [representativeness, judgment by representativeness]
domain: heuristics-and-dual-process
summary: >-
  The mental shortcut of judging how probable it is that a case belongs to a
  category, or that a sample came from a process, by how closely it resembles
  the category's stereotype or the process's typical output, which neglects
  base rates, sample size and the reliability of the evidence.
level: introductory
evidenceStatus: mixed
broader: [ct:heuristic]
related: [ct:heuristics-and-biases-program, ct:availability-heuristic, ct:anchoring-and-adjustment-heuristic, ct:base-rate-neglect, ct:regression-to-the-mean, ct:natural-frequencies, ct:judgment-and-decision-making]
requires: [ct:heuristics-and-biases-program]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: produces, object: ct:insensitivity-to-sample-size, source: s2, confidence: high}
  - {predicate: produces, object: ct:illusion-of-validity, source: s2, confidence: high}
  - {predicate: explains, object: ct:conjunction-fallacy, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: ct:tversky-kahneman-1983-linda-problem-study, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:availability-heuristic, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:gerd-gigerenzer, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:hertwig-gigerenzer-1999-conjunction-fallacy-revisited, source: s5, confidence: medium}
  - {predicate: supportedBy, object: ct:chandrashekar-2021-conjunction-bias-replication, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Subjective probability: A judgment of representativeness"
    publisher: Cognitive Psychology 3, 430-454 (Kahneman & Tversky, 1972), copy hosted on a UC San Diego faculty page
    url: https://pages.ucsd.edu/~mckenzie/Kahneman&Tversky1972CogPsych.pdf
    type: primary
    accessed: 2026-11-05
  - id: s2
    title: "Judgment under uncertainty: Heuristics and biases"
    publisher: Science 185(4157), 1124-1131 (Tversky & Kahneman, 1974), copy hosted on an NC State course page
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf
    type: primary
    accessed: 2026-11-05
  - id: s3
    title: "Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment"
    publisher: Psychological Review 90(4), 293-315 (Tversky & Kahneman, 1983), copy hosted on a UC San Diego faculty page
    url: https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf
    type: primary
    accessed: 2026-11-05
  - id: s4
    title: "On narrow norms and vague heuristics: A reply to Kahneman and Tversky (1996)"
    publisher: Psychological Review 103(3), 592-596 (Gigerenzer, 1996), copy hosted on an NC State course page
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1996.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s5
    title: "The 'conjunction fallacy' revisited: How intelligent inferences look like reasoning errors"
    publisher: Journal of Behavioral Decision Making 12(4), 275-305 (Hertwig & Gigerenzer, 1999), University of Basel edoc record
    url: https://edoc.unibas.ch/8522/
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s6
    title: "Frequency estimation and semantic ambiguity do not eliminate conjunction bias, when it occurs: Replication and extension of Mellers, Hertwig, and Kahneman (2001)"
    publisher: Meta-Psychology 5 (Chandrashekar, Cheng, Fong, Leung, Wong, Cheng & Feldman, 2021)
    url: https://open.lnu.se/index.php/metapsychology/article/view/2474
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Representativeness heuristic

The representativeness heuristic answers a hard question (how likely is it that this person belongs to that group, or that this result came from that process?) with an easier one: how much does it look like it? Kahneman and Tversky proposed that people judge the probability of an uncertain event by how similar it is to its parent population and how well it reflects the salient features of the process that produced it.[^s1] Resemblance is often a useful cue, but it carries no information about how common a category is, how large a sample was, or how reliable a description is, so judgments built on it neglect exactly those factors.[^s2]

## Origin

Daniel Kahneman and Amos Tversky introduced the heuristic in a 1972 *Cognitive Psychology* paper, the first major statement of what became the heuristics-and-biases program.[^s1] Their 1974 *Science* article then set it beside availability and anchoring as one of three general-purpose shortcuts for judging under uncertainty, and listed the systematic errors each one produces.[^s2]

## How it works

The 1972 paper used simple sampling problems. Told that 72 surveyed families of six children had the birth order G B G B B G, 75 of 92 participants judged the order B G B B B B less likely, although the two exact sequences are about equally probable; the second just looks less like a random mix of boys and girls.[^s1] In the hospital problem, people were asked whether a hospital with about 45 births a day or one with about 15 would record more days on which over 60% of babies were boys. The small hospital should, because small samples vary more, yet most answers were "about the same": sample size barely moved the judgments.[^s1][^s2]

The best-known demonstration is the 1983 Linda problem. Linda is described as a bright former philosophy student concerned with social justice. In one sample, 85% of undergraduates ranked "bank teller and active feminist" as more probable than "bank teller", breaking the rule that a conjunction cannot be more likely than either of its parts. The added detail made the description more representative of Linda, and resemblance overrode the inclusion relation.[^s3]

*Workplace example.* A hiring panel meets a candidate who is outgoing, competitive and quick with stories, and rates her highly likely to become a top salesperson because she fits their picture of one. The panel has not asked how many hires with this profile actually reached the top tier (the base rate), how much one interview predicts later performance, or whether the impression rests on a single strong conversation. Tversky and Kahneman found the same pattern when people predicted teachers' success five years out from one practice lesson: predictions were as extreme as the lesson ratings themselves.[^s2]

## How to spot it

Ask whether a probability judgment is really a similarity judgment. In the 1974 study, people's rankings of how likely a described man was to be a librarian, farmer or salesman matched their rankings of how much he resembled each stereotype exactly.[^s2] Warning signs include confident predictions from a vivid profile, a sense that a streak of losses means a win is "due" (the gambler's fallacy), surprise when an extreme result is followed by an ordinary one, and causal stories invented to explain what is merely regression to the mean.[^s2] Rising confidence as details pile up, even when they are redundant or unreliable, is the illusion of validity.[^s2]

## How to counter it

Put the missing quantities back in. Start from the base rate for the category, then ask how much the specific evidence should shift it, and how large and reliable the sample behind it is.[^s2] Recasting a question as counts ("of 100 people who fit this description, how many…?") helps: in Tversky and Kahneman's health-survey problem, conjunction errors fell from 65% with percentages to 25% with a "how many of 100" format, and to 11% when the frequency question was combined with judging the broader group first.[^s3] Expect regression after extreme performances before crediting praise or blame for the change.[^s2]

## Evidence

The core phenomena are well documented, but both their size and their interpretation are debated. Gigerenzer argued in 1996 that representativeness is a vague, one-word label with no process model, so it can be fitted after the fact to opposite results, and that the norms used to score answers ignore content and the meaning of words such as "probable".[^s4] Hertwig and Gigerenzer (1999) showed that many participants read "probability" in the Linda problem in non-mathematical ways, and that wording which pushed a mathematical reading reduced violations; on their account, frequency formats work by narrowing the meaning rather than by adding extensional cues.[^s5]

A 2021 pre-registered replication with 1,032 participants found the Linda conjunction effect again and found no support for semantic ambiguity as its cause, but a parallel profile produced no effect at all, which the authors read as evidence that conjunction errors are real yet context-sensitive.[^s6] Overall the heuristic is a useful description of how resemblance displaces statistical reasoning, with effects that depend heavily on wording and format.[^s3][^s5][^s6]

## Connections

- **Introduced by** Daniel Kahneman and Amos Tversky in their 1972 paper on subjective probability.[^s1]
- **Produces** insensitivity to sample size and the illusion of validity, two of the errors the 1974 article attributed to representativeness.[^s2]
- **Explains** the conjunction fallacy: the 1983 paper traced the Linda error to resemblance overriding the conjunction rule, and is the landmark **demonstration** of the heuristic.[^s3]
- **Contrasts with** the availability heuristic, which judges by ease of recall rather than by resemblance.[^s2]
- **Challenged by** Gerd Gigerenzer's critique of vague heuristics and narrow norms, and by Hertwig and Gigerenzer's semantic account of the Linda problem.[^s4][^s5]
- **Supported by** the 2021 Meta-Psychology replication, which reproduced the Linda effect while showing its limits.[^s6]
- **Related to** base-rate neglect, regression to the mean and natural frequencies, the format that reduces representativeness errors.[^s2][^s3]

## Sources

[^s1]: Kahneman & Tversky, "Subjective probability: A judgment of representativeness", Cognitive Psychology 3 (1972). https://pages.ucsd.edu/~mckenzie/Kahneman&Tversky1972CogPsych.pdf (accessed 2026-11-05)
[^s2]: Tversky & Kahneman, "Judgment under uncertainty: Heuristics and biases", Science 185 (1974). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Tversky+Kahneman-heuristics-biases-1974.pdf (accessed 2026-11-05)
[^s3]: Tversky & Kahneman, "Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment", Psychological Review 90 (1983). https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf (accessed 2026-11-05)
[^s4]: Gigerenzer, "On narrow norms and vague heuristics: A reply to Kahneman and Tversky (1996)", Psychological Review 103 (1996). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1996.pdf (accessed 2026-11-05)
[^s5]: Hertwig & Gigerenzer, "The 'conjunction fallacy' revisited: How intelligent inferences look like reasoning errors", Journal of Behavioral Decision Making 12 (1999). https://edoc.unibas.ch/8522/ (accessed 2026-11-05)
[^s6]: Chandrashekar et al., "Frequency estimation and semantic ambiguity do not eliminate conjunction bias, when it occurs", Meta-Psychology 5 (2021). https://open.lnu.se/index.php/metapsychology/article/view/2474 (accessed 2026-11-05)
