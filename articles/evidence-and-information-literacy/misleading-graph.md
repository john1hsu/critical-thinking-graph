---
id: ct:misleading-graph
type: Phenomenon
title: Misleading graph
aliases: [deceptive visualization, misleading data visualization, misinformative visualization, distorted chart, chart distortion]
domain: evidence-and-information-literacy
summary: >-
  A chart or data graphic whose design choices, such as a truncated axis,
  area or 3-D encodings, a dual axis or a selectively chosen data window,
  leave viewers with an impression of the data that the underlying numbers do
  not support, whether the distortion is deliberate or accidental.
level: introductory
evidenceStatus: robust
broader: [ct:misinformation-and-disinformation]
related: [ct:statistical-literacy, ct:numeracy, ct:suppressed-evidence, ct:framing-effect, ct:media-literacy, ct:how-to-lie-with-statistics]
requires: [ct:numeracy]
relations:
  - {predicate: demonstratedBy, object: ct:correll-2020-truncated-y-axis-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:yang-2021-truncated-bar-graph-study, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:lo-2022-misinformative-visualizations-study, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:edward-tufte, source: s4, confidence: medium}
  - {predicate: studiedIn, object: ct:information-visualization, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Truncating the Y-Axis: Threat or Menace?"
    publisher: Proceedings of ACM CHI 2020 (Correll, Bertini & Franconeri), Tableau Research publication page
    url: https://www.tableau.com/research/publications/truncating-y-axis-threat-or-menace
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "Truncating bar graphs persistently misleads viewers"
    publisher: Journal of Applied Research in Memory and Cognition 10(2), 298-311 (Yang, Vargas Restrepo, Stanley & Marsh, 2021), Duke University Scholars record
    url: https://scholars.duke.edu/publication/1474486
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "Misinformed by Visualization: What Do We Learn From Misinformative Visualizations?"
    publisher: Computer Graphics Forum 41(3), EuroVis 2022 (Lo, Gupta, Shigyo, Wu, Bertini & Qu)
    url: https://diglib.eg.org/bitstream/handle/10.1111/cgf14559/v41i3pp515-525.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Tufte's principles of graphical integrity (CS 7450 Information Visualization lecture notes)"
    publisher: Georgia Institute of Technology (John Stasko, 2013)
    url: https://faculty.cc.gatech.edu/~stasko/7450/13/Notes/tufte.pdf
    type: academic
    accessed: 2026-11-19
  - id: s5
    title: "Darrell Huff and Fifty Years of How to Lie with Statistics"
    publisher: Statistical Science 20(3) (Steele, 2005), University of Pennsylvania repository
    url: https://repository.upenn.edu/handle/20.500.14332/47737
    type: peer-reviewed
    accessed: 2026-11-19
created: 2026-11-19
---

# Misleading graph

A misleading graph is a chart whose visual form tells a different story from its numbers. The data may be accurate and every label correct, yet a design choice (an axis that starts far above zero, quantities drawn as areas or 3-D shapes, two series forced onto mismatched scales, or a time window picked to flatter a trend) makes a difference look larger, smaller or more certain than it is.[^s3] Visualization researchers deliberately include accidental cases under the same heading: what matters to the reader is the false impression, not whether the designer meant it.[^s3]

## Origin

Popular awareness of chart tricks owes much to Darrell Huff's *How to Lie with Statistics*, illustrated by Irving Geis, which a 2005 note in *Statistical Science* described as having outsold every other statistics text over the previous fifty years; its treatment of misleading graphs is one of the topics that note highlights.[^s5] Edward Tufte later gave the idea a measurable form under the heading of graphical integrity: a graphic should be drawn so that the size of a visual mark is directly proportional to the quantity it represents, and his "lie factor" divides the size of the effect shown in the graphic by the size of the effect in the data, so a value far from 1 signals distortion.[^s4] Tufte's teaching example produces a lie factor of about 9.4, a graphic exaggerating its underlying change roughly ninefold.[^s4]

## How it works

Most distortions break the proportionality Tufte asked for. A truncated y-axis is the classic case. Suppose a team dashboard shows customer-satisfaction scores of 81 percent last quarter and 84 percent this quarter, plotted on bars whose axis runs from 80 to 85. The new bar is four times taller than the old one, so a meeting can leave with the sense of a dramatic turnaround from what is a three-point change that may be within survey noise.[^s1][^s4] Area and volume encodings mislead in a similar way, because doubling the height of an icon also enlarges its width and so its area, and readers respond to the whole shape.[^s4] Other common devices include dual axes that let a designer line up two unrelated series, inconsistent tick intervals, and selectively chosen data ranges, which turn the chart into a visual version of [suppressed evidence](suppressed-evidence.md).[^s3]

Truncation is not always dishonest. Correll and colleagues argue that a non-zero baseline can be the right choice when small changes are the meaningful ones, and that the useful question is what size of effect the designer intends viewers to perceive, not a blanket honest-versus-dishonest rule.[^s1]

## How to spot it

- Read the axes before the shapes: where is zero, are tick steps even, and does a second axis use a different scale?[^s4][^s3]
- Compute a rough lie factor: compare the ratio of bar heights or areas with the ratio of the numbers printed on the labels.[^s4]
- Ask what is missing: earlier years, a comparison group or the full range of the series.[^s3][^s4]
- Treat 3-D effects, pictograms and dual axes as prompts to read the numbers directly.[^s3]

## Evidence

The core effect is well replicated. In crowdsourced experiments presented at CHI 2020, Correll, Bertini and Franconeri found that starting the y-axis higher reliably made viewers judge differences as larger, in line charts as well as bar charts; explicit truncation cues such as broken-axis marks did not remove the bias, nor did asking people to estimate the actual values.[^s1] Yang and colleagues' five studies (2021) found the same "truncation effect" in 83.5 percent of participants; it survived instruction about truncated axes, was not predicted by graph literacy, and appeared in doctoral students from quantitative fields as well as the humanities, though quantitative students were slightly more resistant when given no warning.[^s2]

How common are such charts? Lo and colleagues (EuroVis 2022) gathered 129,125 images from search engines and social media in 2021, examined about 6,500 of them and tagged 1,143 visualizations with at least one problem, organising 74 issue types into 12 categories. Truncated axes were the most frequent issue, followed by 3-D effects, missing titles and dual axes, while inverted axes, prominent in earlier research, were comparatively rare.[^s3] A limitation is that perception studies mostly use simple bar and line charts and judgments of effect size made in seconds; less is known about how distortions in rarer chart types shape decisions over time.[^s1][^s3]

## Connections

Misleading graphs are a visual branch of [misinformation and disinformation](misinformation-and-disinformation.md): Lo and colleagues frame them as misinformative visualizations and supply the largest survey of how often each trick occurs.[^s3] The phenomenon is demonstrated by the truncation experiments of Correll, Bertini and Franconeri[^s1] and of Yang and colleagues,[^s2] and it is studied chiefly in information visualization research.[^s1] Tufte formalized the idea of graphical distortion through the lie factor.[^s4] Spotting these charts is part of [statistical literacy](statistical-literacy.md) and rests on basic [numeracy](numeracy.md), although Yang's results show that knowledge alone does not neutralise the visual impression.[^s2] Selective data windows connect it to [suppressed evidence](suppressed-evidence.md),[^s3] and Huff's popular book remains the classic introduction to the topic.[^s5]

## Sources

[^s1]: Correll, Bertini & Franconeri, "Truncating the Y-Axis: Threat or Menace?", Proceedings of ACM CHI 2020. https://www.tableau.com/research/publications/truncating-y-axis-threat-or-menace (accessed 2026-11-19)
[^s2]: Yang, Vargas Restrepo, Stanley & Marsh, "Truncating bar graphs persistently misleads viewers", Journal of Applied Research in Memory and Cognition 10(2), 2021. https://scholars.duke.edu/publication/1474486 (accessed 2026-11-19)
[^s3]: Lo, Gupta, Shigyo, Wu, Bertini & Qu, "Misinformed by Visualization: What Do We Learn From Misinformative Visualizations?", Computer Graphics Forum 41(3), 2022. https://diglib.eg.org/bitstream/handle/10.1111/cgf14559/v41i3pp515-525.pdf (accessed 2026-11-19)
[^s4]: Stasko, "Tufte" lecture notes, CS 7450 Information Visualization, Georgia Institute of Technology, 2013. https://faculty.cc.gatech.edu/~stasko/7450/13/Notes/tufte.pdf (accessed 2026-11-19)
[^s5]: Steele, "Darrell Huff and Fifty Years of How to Lie with Statistics", Statistical Science 20(3), 2005. https://repository.upenn.edu/handle/20.500.14332/47737 (accessed 2026-11-19)
