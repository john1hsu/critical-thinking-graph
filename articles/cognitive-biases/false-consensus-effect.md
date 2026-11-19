---
id: ct:false-consensus-effect
type: CognitiveBias
title: False consensus effect
aliases: [false-consensus bias, false consensus bias]
domain: cognitive-biases
summary: >-
  The tendency to overestimate how many other people share one's own beliefs,
  preferences and behaviours, so that people who make a choice judge it more
  common than people who make the opposite choice do.
level: introductory
evidenceStatus: robust
broader: [ct:cognitive-bias]
related: [ct:bias-blind-spot, ct:naive-realism, ct:overconfidence-effect, ct:groupthink, ct:consider-the-opposite]
requires: []
relations:
  - {predicate: introducedBy, object: ct:lee-ross, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:ross-greene-house-1977-false-consensus-studies, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:many-labs-2-replication-project, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:availability-heuristic, source: s1, confidence: medium}
  - {predicate: challengedBy, object: ct:engelmann-strobel-2000-false-consensus-incentives-study, source: s3, confidence: medium}
  - {predicate: challengedBy, object: ct:galesic-olsson-rieskamp-2013-false-consensus-study, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "False Consensus Effect (chapter in Open Social Psychology)"
    publisher: Open Social Psychology, ed. Rima-Maria Rahal (Zubrod, Berkessel & Kolozsvári), FORRT open textbook
    url: https://forrt.org/open-social-psychology/chapter16.html
    type: textbook
    accessed: 2026-11-19
  - id: s2
    title: "Many Labs 2: Investigating Variation in Replicability Across Samples and Settings"
    publisher: Advances in Methods and Practices in Psychological Science (Klein et al., 2018), copy hosted by University of North Texas
    url: https://psychology.unt.edu/system/files/Many%20labs%202.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "The False Consensus Effect Disappears if Representative Information and Monetary Incentives Are Given"
    publisher: Experimental Economics 3(3), 241-260 (Engelmann & Strobel, 2000), Cambridge Core
    url: https://www.cambridge.org/core/journals/experimental-economics/article/false-consensus-effect-disappears-if-representative-information-and-monetary-incentives-are-given/F5A6ECD267C1572F14A66F9C4EF2413F
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "False Consensus About False Consensus"
    publisher: Proceedings of the Annual Meeting of the Cognitive Science Society 35 (Galesic, Olsson & Rieskamp, 2013), eScholarship (University of California)
    url: https://escholarship.org/content/qt2t1036d4/qt2t1036d4.pdf?t=os5zwb
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s5
    title: "We think you agree: The detrimental impact of the false consensus effect on behavior"
    publisher: Current Psychology 21(4), 293-318 (Bauman & Geher, 2002), SpringerLink
    url: https://link.springer.com/article/10.1007/s12144-002-1020-0
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s6
    title: "A short note on the rationality of the false consensus effect"
    publisher: University of Heidelberg, Alfred-Weber-Institute working paper (Vanberg)
    url: https://www.uni-heidelberg.de/md/awi/professuren/fiwi/falseconsensus.pdf
    type: academic
    accessed: 2026-11-19
created: 2026-11-19
---

# False consensus effect

The false consensus effect is the tendency to overestimate how widely other people share our own opinions, preferences and behaviour.[^s1] It is measured as a gap between groups: people who make a given choice estimate that choice to be more common among their peers than people who make the opposite choice estimate it to be.[^s4] Each side, in effect, sees itself as the normal majority.

## Origin

Lee Ross, David Greene and Pamela House named the effect in a 1977 article in the *Journal of Experimental Social Psychology*, subtitled an egocentric bias in social perception and attribution.[^s1] In their first study, students read short scenarios that each ended in a choice between two actions, estimated what percentage of their peers would pick each option, and then gave their own choice. Their own choice strongly predicted their estimates, and they also judged people who chose the other option as having more extreme, revealing personality traits.[^s1] Ross linked the finding to attribution: if my choice is what most people would do, then someone who chooses differently must be telling us something unusual about themselves.[^s1]

## How it works

Imagine a product team deciding whether to drop a rarely used settings menu. The designer who never touches the menu assumes most users ignore it too; the engineer who relies on it daily assumes most users would miss it. Both are reasoning from a sample of one (themselves) plus the people around them, and both overestimate support for their own view.[^s1]

Several mechanisms have been proposed. One's own choices and the reasons for them come to mind more easily, so they feel more typical, a route through the availability heuristic.[^s1] People also tend to spend time with similar others, so the social world they sample from really does lean their way.[^s1] Motivational accounts add that believing one's choices are common helps them feel normal and correct.[^s1] Galesic and colleagues argue that much of the effect comes from estimating population frequencies by recalling one's own social circle, which is a sampling problem rather than a pure distortion.[^s4]

## Evidence

A 1985 meta-analysis by Mullen and colleagues pooled 115 hypothesis tests from 23 studies and found a highly significant effect of moderate size; method details such as the order of choice and estimate questions moderated its strength.[^s1] In the Many Labs 2 project (published 2018), many labs re-ran two of the original 1977 scenarios with more than 7,000 participants each. Both replicated, with effect sizes (d of about 1.18 and 0.95) at least as large as the originals.[^s2] That is why this node is marked robust: the projection of one's own choice onto others reproduces reliably and at scale.

Whether the effect is an *error* is more disputed. Robyn Dawes argued in 1989 that using one's own choice as a data point about an unknown population can be rational, and later formal work shows that Bayesian updaters with private information should produce exactly this correlation between choice and estimate.[^s6] The 1977 measure shows that choices and estimates co-vary, not that anyone's estimate is wrong.[^s4] In an incentivised economics experiment, Engelmann and Strobel (2000) found no false consensus effect when participants were paid for accurate estimates and shown representative information about others' choices; participants actually gave their own choice too little weight.[^s3] Galesic, Olsson and Rieskamp (2013) found that the direction and size of the effect, including flips into false uniqueness, changed with the response format, suggesting part of it is a measurement artifact.[^s4] The practical reading: projection is reliable, but it becomes a real bias mainly when people have little information about others and do not correct for how unrepresentative their own circle is.

The effect matters for behaviour. In studies of college students, false consensus predicted intentions on social issues, and students often showed the bias for potentially harmful behaviours.[^s5]

## How to spot it

- You are estimating "what most people think" without data, using yourself or your team as the reference.[^s4]
- You explain disagreement by assuming the other side is unusual, uninformed or extreme, rather than simply different.[^s1]
- Your information comes from a self-selected circle, such as colleagues, a customer advisory board or a curated feed.[^s1]

## How to counter it

- Replace introspection with data: survey a representative sample, look at usage logs, or ask people outside your circle. Engelmann and Strobel's result suggests the effect largely disappears when representative information is available and accuracy is rewarded.[^s3]
- Deliberately expose yourself to the opposing case. In Bauman and Geher's second study, watching a video that presented both sides of an issue reduced the false consensus effect.[^s5]
- Write down your estimate of support before discussing a proposal, then compare it with the actual count. This turns a hidden assumption into a checkable prediction.[^s4]

## Connections

Lee Ross introduced the effect and the term, with Greene and House, in the 1977 studies that demonstrate it.[^s1] The Many Labs 2 replication supports it at large scale.[^s2] It is partly explained by the availability heuristic, since one's own choices and reasons are easiest to bring to mind.[^s1] Its status as an error is challenged by Engelmann and Strobel's incentivised experiment[^s3] and by Galesic, Olsson and Rieskamp's evidence that it depends on response format.[^s4] It is related to the bias blind spot and to naive realism, which share the assumption that one's own view is the objective, normal one, and to overconfidence and groupthink, where unchecked assumptions of agreement stop a group from testing its views; consider-the-opposite is a natural remedy given the evidence that exposure to the other side reduces it.[^s5]

## Sources

[^s1]: Zubrod, Berkessel & Kolozsvári, "False Consensus Effect", in *Open Social Psychology* (ed. Rahal), FORRT. https://forrt.org/open-social-psychology/chapter16.html (accessed 2026-11-19)
[^s2]: Klein et al., "Many Labs 2: Investigating Variation in Replicability Across Samples and Settings", *Advances in Methods and Practices in Psychological Science* (2018). https://psychology.unt.edu/system/files/Many%20labs%202.pdf (accessed 2026-11-19)
[^s3]: Engelmann & Strobel, "The False Consensus Effect Disappears if Representative Information and Monetary Incentives Are Given", *Experimental Economics* 3(3) (2000). https://www.cambridge.org/core/journals/experimental-economics/article/false-consensus-effect-disappears-if-representative-information-and-monetary-incentives-are-given/F5A6ECD267C1572F14A66F9C4EF2413F (accessed 2026-11-19)
[^s4]: Galesic, Olsson & Rieskamp, "False Consensus About False Consensus", *Proceedings of the Cognitive Science Society* 35 (2013). https://escholarship.org/content/qt2t1036d4/qt2t1036d4.pdf?t=os5zwb (accessed 2026-11-19)
[^s5]: Bauman & Geher, "We think you agree: The detrimental impact of the false consensus effect on behavior", *Current Psychology* 21(4) (2002). https://link.springer.com/article/10.1007/s12144-002-1020-0 (accessed 2026-11-19)
[^s6]: Vanberg, "A short note on the rationality of the false consensus effect", University of Heidelberg working paper. https://www.uni-heidelberg.de/md/awi/professuren/fiwi/falseconsensus.pdf (accessed 2026-11-19)
