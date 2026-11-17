---
id: ct:accuracy-prompts
type: Technique
title: Accuracy prompts
aliases: [accuracy nudge, accuracy focus, accuracy-nudge intervention]
domain: debiasing-and-metacognition
summary: >-
  A light-touch intervention that shifts attention to whether a claim is true,
  for example by asking people to rate or check a statement's accuracy when
  they first meet it, which blunts the boost that repetition gives to known
  falsehoods and modestly improves the quality of news people choose to share.
level: introductory
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:prebunking, ct:lateral-reading, ct:deliberate-reflection, ct:processing-fluency, ct:cognitive-reflection-test]
requires: []
relations:
  - {predicate: counteracts, object: ct:illusory-truth-effect, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:misinformation-and-disinformation, source: s2, confidence: medium}
  - {predicate: demonstratedBy, object: ct:brashier-eliseev-marsh-2020-accuracy-focus-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:pennycook-2021-accuracy-prompt-field-experiment, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:pennycook-rand-2022-accuracy-prompt-meta-analysis, source: s3, confidence: high}
  - {predicate: challengedBy, object: ct:roozenbeek-freeman-van-der-linden-2021-accuracy-nudge-replication, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "An initial accuracy focus prevents illusory truth"
    publisher: Cognition 194, 104054 (Brashier, Eliseev & Marsh, 2020), Duke Scholars
    url: https://scholars.duke.edu/publication/1406070
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Shifting attention to accuracy can reduce misinformation online"
    publisher: Nature (Pennycook, Epstein, Mosleh et al., 2021), MIT Media Lab
    url: https://www.media.mit.edu/publications/shifting-attention-to-accuracy-can-reduce-misinformation-online
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Accuracy prompts are a replicable and generalizable approach for reducing the spread of misinformation"
    publisher: Nature Communications 13 (Pennycook & Rand, 2022), DSpace@MIT
    url: https://dspace.mit.edu/handle/1721.1/144231
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "How accurate are accuracy-nudge interventions? A preregistered direct replication of Pennycook et al. (2020)"
    publisher: Psychological Science 32(7), 1169-1178 (Roozenbeek, Freeman & van der Linden, 2021), Vrije Universiteit Amsterdam research portal
    url: https://research.vu.nl/en/publications/how-accurate-are-accuracy-nudge-interventions-a-preregistered-dir/
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "When false claims are repeated, we start to believe they are true"
    publisher: British Psychological Society Research Digest
    url: https://www.bps.org.uk/research-digest/when-false-claims-are-repeated-we-start-believe-they-are-true
    type: institutional
    accessed: 2026-11-17
created: 2026-11-17
---

# Accuracy prompts

An accuracy prompt is a brief cue that turns a person's attention to the question "is this true?" at the moment they meet a claim. It can be as simple as asking someone to rate how accurate a statement is, to act as a fact checker, or to judge one sample headline before scrolling on. The technique is aimed at two related failures: believing a falsehood because it has become familiar through repetition, and passing on misinformation without ever stopping to evaluate it.[^s1][^s2]

## Origin

Two research lines converged on the idea around 2019–2021. Nadia Brashier, Elizabeth Eliseev and Elizabeth Marsh at Duke University asked whether the illusory truth effect could be stopped at first exposure; across four experiments published in *Cognition* in 2020, they had participants give truth ratings as "fact checkers" when they first read a statement.[^s1] In parallel, Gordon Pennycook, David Rand and colleagues argued that people often share false news not because they prefer it but because their attention is elsewhere, and they tested subtle accuracy cues in four survey experiments and a field experiment on Twitter, reported in *Nature* in 2021.[^s2]

## How it works

Repetition makes a statement easier to process, and that fluency is misread as a sign of truth.[^s1] In the Duke study design, one group rated how interesting each well-known statement was while another rated how true it was; later, both groups rated old and new statements. The interest group judged repeated false statements as truer than new ones, while the accuracy group showed no such boost, and the protection still held after a two-day delay.[^s5] Focusing on accuracy appears to make people retrieve what they already know at the first encounter, so a falsehood they could have rejected is tagged as false rather than merely as familiar.[^s1]

For sharing decisions the mechanism is attentional. Pennycook and colleagues found that whether a headline was true strongly affected people's accuracy judgments yet barely affected whether they said they would share it; a subtle prompt to think about accuracy raised the quality of what people later shared.[^s2]

A workplace example: an operations team receives a forwarded message claiming a supplier is about to go bankrupt, and the same rumour reappears in three chat channels. A team lead who adds a standing step to the triage checklist — "before reacting, write down whether you think this is accurate and why" — gives members the moment to notice that the supplier's recent filings contradict the rumour, before repetition makes it feel settled — the same first-exposure accuracy focus the Duke experiments used.[^s1]

## How to apply it

1. **Ask at first contact.** Put the accuracy question where a claim is first read: a rating box, a "true or false, and why?" line in a review template, or a check before forwarding. The Duke results concern the initial exposure, so a later prompt is not a substitute.[^s1]
2. **Keep it light and periodic.** In the sharing studies, prompts were subtle and did not need to be explicit warnings to help.[^s2]
3. **Pair it with knowledge or a lookup.** An accuracy focus protected only people who already had relevant knowledge; for obscure claims it did not help, and whether consulting outside sources fills that gap was left untested, so add a source check where the team lacks the background.[^s1][^s5]
4. **Expect a modest, not decisive, effect.** Treat it as one layer alongside prebunking and source checks rather than a fix on its own.[^s3][^s4]

Pitfalls: prompting people who lack the background to judge a claim gives a false sense of having checked it, and effect sizes in sharing studies are small.[^s4][^s5]

## Evidence

A 2022 meta-analysis by Pennycook and Rand pooled 20 of their group's experiments run between 2017 and 2020, with 26,863 participants. Accuracy prompts improved sharing discernment, chiefly by cutting intentions to share false headlines by roughly 10% relative to control. The effect was similar for political and COVID-19 headlines, did not fade across trials, and was larger for older, more reflective and more attentive participants.[^s3] Because these studies all come from the originating lab, independent tests matter. A preregistered two-stage direct replication by Roozenbeek, Freeman and van der Linden (2021) failed in its first stage (n = 701) and found only a small, uncorrected-significant interaction when the sample was pooled to 1,583, leading the authors to describe the effect as small; they also flagged an undisclosed change of hypothesis in the original preregistration.[^s4] For the illusory truth effect specifically, the accuracy-focus benefit replicated across four experiments in one lab but is limited to claims people already know about.[^s1] The overall picture is a real but modest and context-dependent effect, hence the `mixed` status.

## Connections

Accuracy prompts are a form of debiasing that **counteracts** the illusory truth effect when applied at first exposure, as shown in the Brashier, Eliseev and Marsh study.[^s1] They also **counteract** the spread of misinformation and disinformation, demonstrated in the Pennycook et al. survey and Twitter experiments.[^s2] The pooled meta-analysis **supports** the effect,[^s3] while the Roozenbeek, Freeman and van der Linden replication **challenges** its size and robustness.[^s4] The technique works by interrupting reliance on processing fluency as a truth cue,[^s1] and its benefit is larger for more reflective people, linking it to measures such as the Cognitive Reflection Test.[^s3] It complements prebunking, which warns people in advance, and lateral reading, which offers an outside check for unfamiliar claims where an accuracy focus alone did not help.[^s5]

## Sources

[^s1]: Brashier, Eliseev & Marsh, "An initial accuracy focus prevents illusory truth", *Cognition* 194 (2020). https://scholars.duke.edu/publication/1406070 (accessed 2026-11-17)
[^s2]: Pennycook, Epstein, Mosleh et al., "Shifting attention to accuracy can reduce misinformation online", *Nature* (2021). https://www.media.mit.edu/publications/shifting-attention-to-accuracy-can-reduce-misinformation-online (accessed 2026-11-17)
[^s3]: Pennycook & Rand, "Accuracy prompts are a replicable and generalizable approach for reducing the spread of misinformation", *Nature Communications* 13 (2022). https://dspace.mit.edu/handle/1721.1/144231 (accessed 2026-11-17)
[^s4]: Roozenbeek, Freeman & van der Linden, "How accurate are accuracy-nudge interventions?", *Psychological Science* 32(7) (2021). https://research.vu.nl/en/publications/how-accurate-are-accuracy-nudge-interventions-a-preregistered-dir/ (accessed 2026-11-17)
[^s5]: British Psychological Society Research Digest, "When false claims are repeated, we start to believe they are true". https://www.bps.org.uk/research-digest/when-false-claims-are-repeated-we-start-believe-they-are-true (accessed 2026-11-17)
