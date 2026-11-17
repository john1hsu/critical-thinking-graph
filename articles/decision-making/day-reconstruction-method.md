---
id: ct:day-reconstruction-method
type: Method
title: Day reconstruction method
aliases: [DRM, day reconstruction method (DRM)]
domain: decision-making
summary: >-
  A survey method in which people rebuild the previous day as a sequence of
  episodes and then rate what they did, with whom, and how they felt in each
  one, so that experienced well-being is measured episode by episode instead
  of through a single retrospective summary that memory distorts.
level: intermediate
evidenceStatus: mixed
broader: [ct:self-report-measurement]
related: [ct:peak-end-rule, ct:daniel-kahneman, ct:affective-forecasting, ct:judgment-and-decision-making]
requires: [ct:peak-end-rule]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:peak-end-rule, source: s4, confidence: medium}
  - {predicate: counteracts, object: ct:duration-neglect, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: ct:experience-sampling-method, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:dockray-2010-drm-ema-comparison, source: s3, confidence: high}
  - {predicate: studiedIn, object: ct:behavioral-economics, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A Survey Method for Characterizing Daily Life Experience: The Day Reconstruction Method"
    publisher: Science 306(5702), 1776-1780 (Kahneman, Krueger, Schkade, Schwarz & Stone, 2004), copy hosted at the University of Vermont
    url: https://pdodds.w3.uvm.edu/files/papers/others/2004/kahneman2004a.pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Developments in the Measurement of Subjective Well-Being"
    publisher: Journal of Economic Perspectives 20(1), 3-24 (Kahneman & Krueger, 2006), Princeton Open Access Repository
    url: https://oar.princeton.edu/rt4ds/file/6371/Kahneman-2006-Developments+in+the+measurement.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "A Comparison of Affect Ratings Obtained with Ecological Momentary Assessment and the Day Reconstruction Method"
    publisher: Social Indicators Research 99(2), 269-283 (Dockray, Grant, Stone, Kahneman, Wardle & Steptoe, 2010), University College Cork research portal
    url: https://research.ucc.ie/en/publications/a-comparison-of-affect-ratings-obtained-with-ecological-momentary/
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Ambulatory and diary methods can facilitate the measurement of patient reported outcomes"
    publisher: Quality of Life Research 25(3), 497-506 (Schneider & Stone, 2016), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4689672
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Day reconstruction method

The day reconstruction method (DRM) is a structured survey for finding out how people actually feel during ordinary life. Respondents first rebuild yesterday as a series of episodes, like scenes in a film, and only then rate each episode for what they were doing, where, with whom, and how strongly they felt a list of positive and negative emotions.[^s1] Because the ratings are tied to specific, recent, time-stamped episodes, the method aims to capture experienced well-being while avoiding much of the distortion that enters when people summarize a period from memory.[^s1][^s2]

## Origin

The DRM was introduced in a 2004 *Science* paper by the psychologist Daniel Kahneman, the economist Alan Krueger, David Schkade, Norbert Schwarz and Arthur Stone.[^s1] It grew out of Kahneman's distinction between *experienced utility*, the moment-by-moment flow of pleasure and pain, and *remembered utility*, the verdict people give after an episode ends.[^s2] Earlier experiments had shown that remembered verdicts give little weight to duration and lean heavily on the most intense moment and the ending, so a question like "how was your week?" is not a neutral readout of the week.[^s2] The real-time alternative, experience sampling, beeps people several times a day; it is the benchmark but is costly and hard to run on large samples, and the DRM was designed as a cheaper approximation to it.[^s1][^s2]

## How it works

The original study asked 909 employed women in Texas to fill out a booklet. They answered general life-satisfaction questions, then wrote a diary of the previous day broken into episodes (typically 15 minutes to 2 hours, about 14 per person), noting start and end times. For each episode they reported the activity, location, companions, and the intensity of several feelings on a 0-6 scale.[^s1] Reconstructing the context first is meant to cue concrete memories rather than stereotyped beliefs about how one "usually" feels about an activity.[^s1]

A workplace example: a team lead wants to know whether a new hybrid schedule improved staff experience. Asking "how satisfied are you with the new schedule?" invites an answer coloured by the last stressful meeting or the most memorable bad commute. A DRM-style check instead asks staff to reconstruct one recent workday, episode by episode, and rate each one. The team can then compute how much of the day was spent in an unpleasant state and where that time concentrates. Kahneman and Krueger proposed exactly this metric, the U-index: the share of time in which a person's strongest feeling is negative.[^s2] Because it counts minutes, a long, mildly irritating commute weighs more than a short, intense spike, which is what a remembered summary tends to get wrong.[^s2]

## How to apply it

1. Fix a recent reference period, usually the previous day, so memories are fresh.[^s1]
2. Have people list episodes with start and end times before they rate anything.[^s1]
3. Rate each episode separately on several specific feelings, not one global "how was it?".[^s1]
4. Aggregate by time, for example with a duration-weighted average or the U-index.[^s2]
5. Compare groups or conditions, not individual days, since single-day measures are noisy.[^s2]

Pitfalls: completion took 45-75 minutes in the original study, which limits use in quick surveys and clinics.[^s1][^s4] Activity comparisons are not causal, because people choose their activities, and the list of feelings needs tailoring to the question.[^s2]

## Evidence

Validation has centred on agreement with real-time measures. The 2004 study found that DRM data reproduced diurnal patterns known from experience sampling, such as tiredness bottoming out around midday.[^s1] In a 2010 study of 94 working women who gave six momentary ratings a day and then completed a DRM for the same hours, the two methods produced similar affect profiles, with attenuation-corrected between-person correlations from 0.58 (stress on a working day) to 0.90 (happiness on a leisure day).[^s3] Agreement is good but not perfect, and the DRM is still a memory-based reconstruction rather than a live reading, so it is rated *mixed* here.[^s2][^s4] A 2016 review notes that retrospective reports over longer windows drift upward for negative states and are pulled toward peaks and end points, which is the gap that short-window and episode-based methods are meant to close.[^s4]

## Connections

- **Introduced by** Daniel Kahneman and colleagues in 2004.[^s1]
- **Counteracts** the peak-end rule: rating short, recent episodes reduces the pull of peaks and endings that shapes longer recall.[^s4]
- **Counteracts** duration neglect: by recording how long each episode lasted and weighting by time, it restores the duration information that remembered verdicts drop.[^s2]
- **Contrasts with** the experience sampling method, the real-time benchmark it approximates at lower cost.[^s1]
- **Supported by** the 2010 Dockray et al. comparison with momentary assessment.[^s3]
- **Studied in** behavioral economics and well-being research, where Kahneman and Krueger presented it to economists as a practical way to measure experienced utility.[^s2]

## Sources

[^s1]: Kahneman, Krueger, Schkade, Schwarz & Stone, "A Survey Method for Characterizing Daily Life Experience: The Day Reconstruction Method", *Science* 306 (2004). https://pdodds.w3.uvm.edu/files/papers/others/2004/kahneman2004a.pdf (accessed 2026-11-17)
[^s2]: Kahneman & Krueger, "Developments in the Measurement of Subjective Well-Being", *Journal of Economic Perspectives* 20(1) (2006). https://oar.princeton.edu/rt4ds/file/6371/Kahneman-2006-Developments+in+the+measurement.pdf (accessed 2026-11-17)
[^s3]: Dockray et al., "A Comparison of Affect Ratings Obtained with Ecological Momentary Assessment and the Day Reconstruction Method", *Social Indicators Research* 99 (2010). https://research.ucc.ie/en/publications/a-comparison-of-affect-ratings-obtained-with-ecological-momentary/ (accessed 2026-11-17)
[^s4]: Schneider & Stone, "Ambulatory and diary methods can facilitate the measurement of patient reported outcomes", *Quality of Life Research* 25 (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4689672 (accessed 2026-11-17)
