---
id: ct:dialectical-bootstrapping
type: Technique
title: Dialectical bootstrapping
aliases: [wisdom of the inner crowd technique, dialectical estimate averaging]
domain: debiasing-and-metacognition
summary: >-
  A technique for improving a single person's numerical estimate: make a first
  estimate, assume it is wrong and say why, make a second estimate from that
  different angle, then average the two so that partly independent errors
  cancel.
level: intermediate
evidenceStatus: contested
broader: [ct:debiasing]
related: [ct:consider-the-opposite, ct:wisdom-of-crowds, ct:anchoring-effect, ct:calibration, ct:outside-view, ct:overconfidence-effect]
requires: [ct:consider-the-opposite]
relations:
  - {predicate: introducedBy, object: ct:stefan-herzog, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:ralph-hertwig, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:anchoring-and-adjustment-heuristic, source: s3, confidence: medium}
  - {predicate: explainedBy, object: ct:wisdom-of-crowds, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:herzog-hertwig-2009-dialectical-estimates-study, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:vul-pashler-2008-crowd-within-study, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:white-antonakis-2013-dialectical-bootstrapping-reanalysis, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:gomilsek-2024-fermian-guesstimation-study, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Wisdom of Many in One Mind: Improving Individual Judgments With Dialectical Bootstrapping"
    publisher: Psychological Science 20(2), 231-237 (Herzog & Hertwig, 2009), author copy at the Max Planck Society repository
    url: https://pure.mpg.de/pubman/item/item_2504710_7/component/file_2520393/SH_Wisdom_2009.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Measuring the Crowd Within: Probabilistic Representations Within Individuals"
    publisher: Psychological Science 19(7), 645-647 (Vul & Pashler, 2008), course copy at Johns Hopkins University
    url: https://perception.jhu.edu/chaz/teaching/courses/tp/files/readings/9/Vul_Pashler_2008_Psychological_Science_Measuring_the_Crowd_Within_Probabilistic_Representations_Within_Individuals.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Harnessing the wisdom of the inner crowd"
    publisher: Trends in Cognitive Sciences 18(10), 504-506 (Herzog & Hertwig, 2014), author copy at the Max Planck Society repository
    url: https://pure.mpg.de/pubman/item/item_2097012_6/component/file_2097011/SH_Harnessing_2014.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "The Crowd-Within and the Benefits of Dialectical Bootstrapping: A Reply to White and Antonakis (2013)"
    publisher: Psychological Science 24, 117-119 (Herzog & Hertwig, 2013), author copy at the Max Planck Society repository
    url: https://pure.mpg.de/pubman/item/item_2097272_10/component/file_3565967/Herzog_The_2013_VerlPDF_final_LS.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "Fermian guesstimation can boost the wisdom-of-the-inner-crowd"
    publisher: Scientific Reports 14, 5014 (Gomilsek, Hoffrage & Marewski, 2024)
    url: https://www.nature.com/articles/s41598-024-53639-3.pdf
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Dialectical bootstrapping

Dialectical bootstrapping is a way for one person to get some of the benefit of asking a second person. You make an estimate, then deliberately assume it is off, think about why, and produce a second estimate from that different footing. Averaging the two tends to beat the first estimate alone, because the second draws on partly different knowledge and so its errors only partly overlap with the first.[^s1] The name points to the method's two roots: a dialectical move (argue against your own first answer) and bootstrapping (improve a judgment using only the judge's own resources).[^s1]

## Origin

Stefan Herzog and Ralph Hertwig, then at the University of Basel, introduced the term in a 2009 paper in *Psychological Science*.[^s1] They built on the wisdom-of-crowds result that averaging many people's estimates usually beats the typical individual, and on Vul and Pashler's 2008 finding that even two guesses from the same person, averaged, are more accurate than one.[^s1][^s2] Vul and Pashler had found that the benefit grew when the second guess came three weeks later, and they suggested an immediate second guess stays tied to the first.[^s2] Herzog and Hertwig's contribution was a way to loosen that tie at once, using a consider-the-opposite prompt instead of waiting.[^s1]

## How it works

Averaging only helps when two estimates can fall on opposite sides of the truth, so that their errors cancel. If the second estimate simply repeats the reasoning behind the first, both err in the same direction and averaging changes little.[^s1][^s3] The dialectical prompt asks the person to question the assumptions behind the first answer, which makes it more likely the second answer comes from a different line of thought.[^s3]

A workplace example: a project lead estimates that a data migration will take 30 working days. She then assumes this is wrong, notes that the last two migrations ran long because of undocumented legacy fields and a slow vendor sign-off, and arrives at 46 days. Averaging gives 38 days. If the true figure turns out to be 41, the average is closer than her first estimate, even though she never asked anyone else; this is the same procedure the original study used, applied to a planning estimate.[^s1]

In the original study, 101 students estimated dates of historical events. Averaging a first estimate with a dialectical second estimate cut error by about 4.1 percentage points on the authors' measure, against about 0.3 points for simply estimating again; averaging with another person's estimate did better still, at about 7.1 points.[^s1] Roughly seven in ten participants gained, and about a quarter got slightly worse.[^s1]

## How to apply it

1. Write down your first estimate and keep it in view.[^s1]
2. Assume it is wrong. List concrete reasons why, and decide whether it is more likely too high or too low.[^s1]
3. Make a second estimate that follows from those reasons, not a small nudge from the first.[^s3]
4. Average the two rather than picking the one you prefer; people's choices between their own estimates rarely beat a plain average.[^s3]
5. Where time allows, separate the two estimates by a delay, which also makes the second more independent.[^s2][^s3]

Pitfalls: the method works best for quantities with a clear numeric answer such as dates, proportions or durations, and results for other kinds of judgments have been mixed.[^s3] An inner crowd of two is still weaker than asking a second informed person.[^s1][^s5]

## Evidence

The basic "crowd within" effect, where averaging repeated estimates from one person improves accuracy, has support across several labs.[^s4][^s3] Whether the dialectical prompt adds much beyond plain repetition is disputed. White and Antonakis reanalysed the 2009 data in 2013 and argued that, once identical repeat answers are handled differently, the dialectical advantage disappears; Herzog and Hertwig replied that some measures still show it, and conceded the gain depends on the measure.[^s4] A 2024 study found consider-the-opposite roughly indistinguishable from a control condition in untrimmed data, but the best of three strategies after outliers were trimmed, and it again found that asking another person helped more than asking oneself.[^s5]

## Connections

- **Introduced by** Stefan Herzog and Ralph Hertwig in their 2009 paper.[^s1]
- **Counteracts** the anchoring-and-adjustment heuristic: earlier estimates hold strong control over later ones, and consider-the-opposite or a delay loosens that pull so the second estimate is not just a small adjustment from the first.[^s3][^s2]
- **Explained by** the wisdom of crowds: gains come from error cancellation when estimates are averaged.[^s1]
- **Demonstrated by** Herzog and Hertwig's 2009 date-estimation experiment.[^s1]
- **Supported by** Vul and Pashler's 2008 crowd-within study.[^s2]
- **Challenged by** White and Antonakis's 2013 reanalysis and by the mixed 2024 results of Gomilsek, Hoffrage and Marewski.[^s4][^s5]
- **Requires** consider the opposite, the prompt used to produce the second estimate.[^s1]

## Sources

[^s1]: Herzog & Hertwig, "The Wisdom of Many in One Mind: Improving Individual Judgments With Dialectical Bootstrapping", *Psychological Science* 20(2) (2009). https://pure.mpg.de/pubman/item/item_2504710_7/component/file_2520393/SH_Wisdom_2009.pdf (accessed 2026-11-15)
[^s2]: Vul & Pashler, "Measuring the Crowd Within: Probabilistic Representations Within Individuals", *Psychological Science* 19(7) (2008). https://perception.jhu.edu/chaz/teaching/courses/tp/files/readings/9/Vul_Pashler_2008_Psychological_Science_Measuring_the_Crowd_Within_Probabilistic_Representations_Within_Individuals.pdf (accessed 2026-11-15)
[^s3]: Herzog & Hertwig, "Harnessing the wisdom of the inner crowd", *Trends in Cognitive Sciences* 18(10) (2014). https://pure.mpg.de/pubman/item/item_2097012_6/component/file_2097011/SH_Harnessing_2014.pdf (accessed 2026-11-15)
[^s4]: Herzog & Hertwig, "The Crowd-Within and the Benefits of Dialectical Bootstrapping: A Reply to White and Antonakis (2013)", *Psychological Science* 24 (2013). https://pure.mpg.de/pubman/item/item_2097272_10/component/file_3565967/Herzog_The_2013_VerlPDF_final_LS.pdf (accessed 2026-11-15)
[^s5]: Gomilsek, Hoffrage & Marewski, "Fermian guesstimation can boost the wisdom-of-the-inner-crowd", *Scientific Reports* 14 (2024). https://www.nature.com/articles/s41598-024-53639-3.pdf (accessed 2026-11-15)
