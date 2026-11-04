---
id: ct:availability-heuristic
type: Heuristic
title: Availability heuristic
aliases: [availability, availability bias, availability rule]
domain: heuristics-and-dual-process
summary: >-
  The mental shortcut of judging how frequent or probable something is by how
  easily instances or associations come to mind, which works when ease of
  recall tracks real frequency and misleads when vividness, recency or media
  exposure drive recall instead.
level: introductory
evidenceStatus: mixed
broader: [ct:heuristic]
related: [ct:heuristics-and-biases-program, ct:representativeness-heuristic, ct:anchoring-and-adjustment-heuristic, ct:base-rate-neglect, ct:consider-the-opposite, ct:judgment-and-decision-making]
requires: [ct:heuristics-and-biases-program]
relations:
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: produces, object: ct:illusory-correlation, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:lichtenstein-1978-judged-frequency-of-lethal-events, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:ease-of-retrieval-effect, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:yeager-2019-national-sample-replications, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Availability: A heuristic for judging frequency and probability"
    publisher: Cognitive Psychology 5(2), 207-232 (Tversky & Kahneman, 1973), author-hosted copy
    url: https://noorsiddiqui.com/papers/TverskyKahneman.pdf
    type: primary
    accessed: 2026-11-04
  - id: s2
    title: "Judged frequency of lethal events"
    publisher: Journal of Experimental Psychology - Human Learning and Memory 4, 551-578 (Lichtenstein, Slovic, Fischhoff, Layman & Combs, 1978), University of Oregon Scholars' Bank
    url: https://scholarsbank.uoregon.edu/xmlui/handle/1794/22549
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s3
    title: "Ease of retrieval as information: Another look at the availability heuristic"
    publisher: Journal of Personality and Social Psychology 61(2), 195-202 (Schwarz, Bless, Strack, Klumpp, Rittenauer-Schatka & Simons, 1991), University of Michigan ISR record
    url: https://api.isr.umich.edu/?p=190598
    type: primary
    accessed: 2026-11-04
  - id: s4
    title: "Does ease mediate the ease-of-retrieval effect? A meta-analysis"
    publisher: Psychological Bulletin (Weingarten & Hutchinson, 2018), University of Pennsylvania ScholarlyCommons
    url: https://repository.upenn.edu/marketing_papers/382
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s5
    title: "Moderation of classic social psychological effects by demographics in the U.S. adult population"
    publisher: Journal of Personality and Social Psychology 117(6), e84-e99 (Yeager, Krosnick, Visser, Holbrook & Tahk, 2019), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6918461
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s6
    title: "Psychology of Intelligence Analysis"
    publisher: Center for the Study of Intelligence, CIA (Heuer, 1999)
    url: https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
    type: government
    accessed: 2026-11-04
created: 2026-11-04
---

# Availability heuristic

The availability heuristic is the habit of answering a hard question (how common is this? how likely is that?) with an easier one: how readily do examples come to mind? Tversky and Kahneman defined it as judging frequency or probability by the ease with which instances or associations can be retrieved or imagined.[^s1] Most of the time this is a sensible shortcut, because frequent events really are easier to recall. It misleads when something other than frequency makes an event memorable.[^s1]

## Origin

Amos Tversky and Daniel Kahneman introduced the heuristic in a 1973 *Cognitive Psychology* paper, written while they were developing the heuristics-and-biases program. Representativeness, their earlier proposal, judges by resemblance. Availability judges by ease of retrieval or construction.[^s1] Their rationale was ecological: over a lifetime people learn that common classes are recalled faster, likely events are easier to imagine, and things that often co-occur become strongly associated, so ease is usually a fair cue to frequency.[^s1]

## How it works

The 1973 paper used simple demonstrations. Most people judged that more English words begin with the letter K than have K in third position, although typical text holds roughly twice as many of the latter; words are simply easier to search by their first letter.[^s1] In another study, listeners heard a list of names in which one sex was represented by more famous people. Famous names were recalled more easily, and 80 of 99 participants judged the famous group to be the larger one even when it was smaller.[^s1] The paper also showed that a vivid recent event, such as seeing an overturned car, can temporarily raise one's estimate of accident risk.[^s1]

*Workplace example.* After a dramatic data-centre outage last quarter, an operations manager is asked to rank risks for next year. The outage tops the list because it is vivid and recent, while slow, unglamorous failures (a gradual rise in misconfigured access rights, say) rank low because no single memorable case stands out. The ranking reflects what is easy to recall, not what the incident logs show; Heuer noted that vividness, recency and personal impact all raise ease of recall without changing probability.[^s6]

In risk perception the pattern is systematic. In a 1978 study, Lichtenstein and colleagues asked people to estimate how often various causes of death occur. Estimates followed a consistent scale but were biased: rare causes were overestimated and common ones underestimated, and at any given true frequency some causes were inflated. The authors traced the distortions to unequal exposure, memorability and imaginability, and participants could not correct for them even when warned.[^s2]

## Evidence

The core demonstrations are classic findings, but the mechanism has been refined and debated. Schwarz and colleagues (1991) separated the *content* recalled from the *feeling* of recalling it. People asked to list 12 examples of their own assertive behaviour, a hard task, then rated themselves as less assertive than people asked for just 6. The effect vanished when the difficulty was given another explanation.[^s3] This ease-of-retrieval account treats availability as a metacognitive experience rather than a count of what comes to mind.[^s3]

A 2018 meta-analysis of 263 studies found that the standard few-versus-many manipulation yields a medium-sized effect. Subjective ease mediated only about a third to a half of it, and publication bias inflated the standard effect by up to about a third.[^s4] Replication of the flagship paradigm is shaky: in a 2019 national probability sample, the recall task still felt harder with 12 examples, but the predicted reversal in self-ratings did not appear. It was the only canonical effect in that project that failed to replicate.[^s5] The fair summary is that availability as a source of frequency and risk errors is well supported, while the specific ease-of-retrieval paradigm is smaller and more fragile than early studies suggested.[^s2][^s4][^s5]

## How to spot it

Ask where an estimate came from. If the answer is "I can think of several cases", the judgment is probably running on availability.[^s1] Watch for estimates that track how vivid, recent or personally striking events are, rather than records; Heuer warned intelligence analysts that these factors shape recall independently of actual probability.[^s6] Mismatches between perceived and recorded frequency, such as dramatic causes of death rated above common ones, are a strong signal.[^s2]

## How to counter it

Replace recall with counts. Look up base rates, incident logs or reference-class data before ranking risks, because people do not correct availability errors just by being told about them.[^s2] Heuer's advice to analysts was to treat an easily imagined scenario as a warning sign and to assess explicitly the variables that will drive the outcome.[^s6] Techniques that ask people to generate counter-examples help only when the counter-examples come easily; asking for too many can backfire through the same ease-of-retrieval mechanism.[^s3][^s4]

## Connections

- **Introduced by** Amos Tversky and Daniel Kahneman in their 1973 paper, which placed it beside representativeness in the heuristics-and-biases program.[^s1]
- **Produces** illusory correlation: the 1973 paper explained why people overestimate how often strongly associated items occur together by the ease of the association.[^s1]
- **Demonstrated by** the 1978 study of judged frequency of lethal events, which linked systematic errors in risk estimates to exposure, memorability and imaginability.[^s2]
- **Explained by** the ease-of-retrieval effect, Schwarz and colleagues' account that the felt ease of recall, not the amount recalled, drives the judgment.[^s3]
- **Challenged by** the 2019 national-sample replications, in which the classic ease-of-retrieval reversal did not reproduce.[^s5]
- **Related to** base-rate neglect, since an easily recalled case can crowd out the base rate, as in the 1973 paper's example of a clinician judging suicide risk from memorable patients; and to consider-the-opposite, a debiasing technique whose success depends on how easily counter-reasons come to mind.[^s1][^s4]

## Sources

[^s1]: Tversky & Kahneman, "Availability: A heuristic for judging frequency and probability", Cognitive Psychology 5 (1973). https://noorsiddiqui.com/papers/TverskyKahneman.pdf (accessed 2026-11-04)
[^s2]: Lichtenstein, Slovic, Fischhoff, Layman & Combs, "Judged frequency of lethal events" (1978). https://scholarsbank.uoregon.edu/xmlui/handle/1794/22549 (accessed 2026-11-04)
[^s3]: Schwarz et al., "Ease of retrieval as information: Another look at the availability heuristic" (1991). https://api.isr.umich.edu/?p=190598 (accessed 2026-11-04)
[^s4]: Weingarten & Hutchinson, "Does ease mediate the ease-of-retrieval effect? A meta-analysis" (2018). https://repository.upenn.edu/marketing_papers/382 (accessed 2026-11-04)
[^s5]: Yeager et al., "Moderation of classic social psychological effects by demographics in the U.S. adult population" (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6918461 (accessed 2026-11-04)
[^s6]: Heuer, Psychology of Intelligence Analysis, CIA Center for the Study of Intelligence (1999). https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (accessed 2026-11-04)
