---
id: ct:random-sampling
type: Method
title: Random sampling
aliases: [probability sampling, random selection, simple random sampling]
domain: scientific-reasoning
summary: >-
  Choosing the members of a sample by a chance mechanism that gives every
  member of the population a known (often equal) chance of selection, so that
  the sample is likely to resemble the population and the size of its sampling
  error can be estimated.
level: introductory
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:randomized-controlled-trial, ct:insensitivity-to-sample-size, ct:law-of-small-numbers, ct:statistical-reasoning-training, ct:nonresponse-bias]
requires: [ct:inductive-reasoning]
relations:
  - {predicate: counteracts, object: ct:hasty-generalization, source: s2, confidence: medium}
  - {predicate: counteracts, object: ct:selection-bias, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:convenience-sampling, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:purposive-selection, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:jerzy-neyman, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:survey-research, source: s5, confidence: high}
sources:
  - id: s1
    title: "1.3: Data, Sampling, and Variation in Data and Sampling (Introductory Statistics, OpenStax)"
    publisher: OpenStax / LibreTexts (Illowsky & Dean)
    url: https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_1e_(OpenStax)/01%3A_Sampling_and_Data/1.03%3A_Data_Sampling_and_Variation_in_Data_and_Sampling
    type: textbook
    accessed: 2026-11-10
  - id: s2
    title: "Logical Reasoning, Chapter 6: Inductive Reasoning and Arguments"
    publisher: Oklahoma State University Libraries open edition (Dowden, California State University Sacramento)
    url: https://open.library.okstate.edu/logicandcriticalthinkingexercises/?p=73
    type: textbook
    accessed: 2026-11-10
  - id: s3
    title: "On the Two Different Aspects of the Representative Method: The Method of Stratified Sampling and the Method of Purposive Selection"
    publisher: Journal of the Royal Statistical Society 97(4):558-625 (Neyman, 1934)
    url: https://errorstatistics.com/wp-content/uploads/2019/01/neyman-1934.pdf
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "'President' Landon and the 1936 Literary Digest Poll: Were Automobile and Telephone Owners to Blame?"
    publisher: Social Science History 36(1):23-54 (Lusinchi, 2012)
    url: https://pdixon.stat.iastate.edu/stat587/resources/president-landon-and-the-1936-literary-digest-poll-were-automobile-and-telephone-owners-to-blame.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Report of the AAPOR Task Force on Non-Probability Sampling"
    publisher: American Association for Public Opinion Research (Baker, Brick et al., 2013)
    url: https://www.aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13.pdf
    type: institutional
    accessed: 2026-11-10
  - id: s6
    title: "1.5: Experimental Design and Ethics (Introductory Statistics, OpenStax)"
    publisher: OpenStax / LibreTexts (Illowsky & Dean)
    url: https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_1e_(OpenStax)/01%3A_Sampling_and_Data/1.05%3A_Experimental_Design_and_Ethics
    type: textbook
    accessed: 2026-11-10
created: 2026-11-10
---

# Random sampling

Random sampling picks the cases you will examine by chance rather than by judgment or convenience. In its simplest form every member of the population starts with an equal chance of being chosen, and every possible group of the chosen size is equally likely to be drawn, as with names from a hat or a random-number generator.[^s1] More broadly, a probability sample is any design in which each member's chance of selection is known, so it can be used in weighting and in estimating error.[^s5] It is the standard practical answer to the question every inductive generalization raises: is this sample likely to look like the whole?[^s2]

## Origin

Early twentieth-century survey statisticians argued over two versions of the "representative method": drawing units at random, or hand-picking units that match the population on known averages (purposive selection). In a 1934 paper read to the Royal Statistical Society, Jerzy Neyman settled the debate for most statisticians.[^s3] He showed that random selection, unlike purposive choice, gives a basis for calculating how accurate an estimate is, and he introduced confidence intervals to express that accuracy without assuming a prior distribution.[^s3] His test case was an Italian study that had hand-picked 29 of 214 census districts to mirror the nation; the chosen districts matched on the control variables but missed badly on others, and Neyman judged the approach closer to a gamble than a method.[^s3] He recommended stratified random sampling for general use.[^s3]

## How it works

A sample can mislead in two ways. *Sampling error* is the luck of the draw, and it shrinks as the sample grows; *sampling bias* arises when some members of the population are less likely to be picked than others, and a bigger sample does not cure it.[^s1] Randomization attacks bias: because nobody's preferences, habits or accessibility decide who gets in, the favoured or easy-to-reach members of a population are not systematically over-counted.[^s2] It also balances, on average, characteristics nobody thought to measure, which is the property that lets statisticians attach a margin of error to the result.[^s5][^s3]

A workplace example: an operations manager wants to know how satisfied the company's 4,000 field technicians are with a new scheduling app. Asking the technicians who happen to visit head office, or reading the comments people volunteered in the app, is convenience or self-selected sampling, which the textbooks flag as often unreliable.[^s1] Instead she exports the staff list, has a script draw 300 names at random, and follows up with non-responders. Because the draw ignored region and seniority, she can also check that the sample's mix of regions resembles the workforce, and, if one small region matters, stratify by region and sample randomly within each stratum.[^s1][^s3]

Random sampling is not the same thing as random assignment. Random sampling decides *who is studied* and supports generalizing to a population; random assignment decides *which treatment each subject gets* and spreads lurking variables evenly across groups, which supports causal conclusions.[^s6]

## How to apply it

1. **Define the population and get a list (frame) of it.** Members missing from the frame have no chance of selection, a coverage problem randomness cannot fix.[^s5]
2. **Use a real chance mechanism**, such as a random-number generator or a systematic draw from a random start; stratify when key subgroups must be represented.[^s1]
3. **Choose a size from the margin of error you can tolerate.** Larger samples are less likely to be distorted by bad luck, though cost limits them.[^s2]
4. **Chase non-response.** A random draw protects only those who answer; high non-response erodes its advantage.[^s5]
5. **Know when it matters less.** If background knowledge shows the population is uniform on the trait, a small non-random sample may do.[^s2]

## Evidence and limitations

The 1936 *Literary Digest* poll is the classic cautionary tale: about 10 million ballots mailed, 2.4 million returned, and a confident forecast that Alf Landon would beat Franklin Roosevelt, who in fact won about 61 percent of the vote.[^s4] Textbooks usually blame a frame of telephone and car owners, but a 2012 reanalysis of Gallup data found those owners actually favoured Roosevelt and traced the failure mainly to non-response bias.[^s4] Either way, the lesson holds: sheer size cannot rescue a sample whose members were not selected, or did not respond, by chance. The American Association for Public Opinion Research's 2013 task force found no single theoretical framework that justifies inference from non-probability samples such as opt-in panels, while also warning that a probability design alone does not guarantee a valid survey.[^s5]

## Connections

Random sampling **counteracts** hasty generalization: that fallacy, technically, is generalizing from a sample unlikely to be representative, and random selection is the first technique statisticians use to obtain a representative one.[^s2] It **counteracts** selection bias, since a chance mechanism keeps some members from being systematically less likely to be chosen.[^s1] It **contrasts with** convenience sampling, a non-random method that can be highly biased,[^s1] and with purposive selection, the hand-picked alternative Neyman criticized; Neyman also **formalized** its theory of estimation, making **Jerzy Neyman** the key figure in its history.[^s3] It is **applied in** survey research, where probability designs remain the benchmark against which opt-in methods are judged.[^s5] It relates to randomized controlled trials (random assignment rather than selection),[^s6] to insensitivity to sample size and the law of small numbers (the sampling-error half of the problem),[^s1] and to non-response bias, which undid the *Literary Digest* poll.[^s4]

## Sources

[^s1]: Illowsky & Dean, "1.3: Data, Sampling, and Variation in Data and Sampling", *Introductory Statistics* (OpenStax), LibreTexts. https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_1e_(OpenStax)/01%3A_Sampling_and_Data/1.03%3A_Data_Sampling_and_Variation_in_Data_and_Sampling (accessed 2026-11-10)
[^s2]: Dowden, "Inductive Reasoning and Arguments", *Logical Reasoning*, Oklahoma State University Libraries open edition. https://open.library.okstate.edu/logicandcriticalthinkingexercises/?p=73 (accessed 2026-11-10)
[^s3]: Neyman, "On the Two Different Aspects of the Representative Method", *Journal of the Royal Statistical Society* 97(4):558-625, 1934. https://errorstatistics.com/wp-content/uploads/2019/01/neyman-1934.pdf (accessed 2026-11-10)
[^s4]: Lusinchi, "'President' Landon and the 1936 Literary Digest Poll", *Social Science History* 36(1):23-54, 2012. https://pdixon.stat.iastate.edu/stat587/resources/president-landon-and-the-1936-literary-digest-poll-were-automobile-and-telephone-owners-to-blame.pdf (accessed 2026-11-10)
[^s5]: Baker, Brick et al., "Report of the AAPOR Task Force on Non-Probability Sampling", AAPOR, 2013. https://www.aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13.pdf (accessed 2026-11-10)
[^s6]: Illowsky & Dean, "1.5: Experimental Design and Ethics", *Introductory Statistics* (OpenStax), LibreTexts. https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_1e_(OpenStax)/01%3A_Sampling_and_Data/1.05%3A_Experimental_Design_and_Ethics (accessed 2026-11-10)
