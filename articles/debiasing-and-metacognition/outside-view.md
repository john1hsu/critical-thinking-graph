---
id: ct:outside-view
type: Technique
title: Taking the outside view
aliases: [outside view, reference class forecasting, outside-view forecasting]
domain: debiasing-and-metacognition
summary: >-
  A forecasting and debiasing technique in which a person sets aside the
  details of the case at hand, first asks how similar cases have usually
  turned out, and then anchors the prediction on that distribution of
  outcomes before adjusting for what is special about the case.
level: introductory
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:base-rate-neglect, ct:regression-to-the-mean, ct:premortem, ct:natural-frequencies, ct:overconfidence-effect, ct:judgment-and-decision-making]
requires: [ct:base-rate-neglect]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:amos-tversky, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:representativeness-heuristic, source: s1, confidence: medium}
  - {predicate: counteracts, object: ct:base-rate-neglect, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:planning-fallacy, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:inside-view, source: s3, confidence: high}
  - {predicate: appliedIn, object: ct:project-management, source: s4, confidence: high}
  - {predicate: appliedIn, object: ct:geopolitical-forecasting, source: s5, confidence: high}
  - {predicate: supportedBy, object: ct:chang-2016-forecasting-training-study, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:love-ahiaga-dagbui-2018-cost-overrun-critique, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Intuitive Prediction: Biases and Corrective Procedures"
    publisher: Technical report, Decision Research for ARPA / Office of Naval Research (Kahneman & Tversky, 1977), DTIC
    url: https://apps.dtic.mil/sti/pdfs/ADA047747.pdf
    type: primary
    accessed: 2026-11-05
  - id: s2
    title: "On the Psychology of Prediction"
    publisher: Oregon Research Institute Research Bulletin No. 4 (Kahneman & Tversky, 1972), University of Oregon Scholars' Bank
    url: https://scholarsbank.uoregon.edu/items/098a706d-e32d-4d73-ba06-6dd92ae502a9/full
    type: primary
    accessed: 2026-11-05
  - id: s3
    title: "Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking"
    publisher: Management Science 39(1), 17-31 (Kahneman & Lovallo, 1993), IDEAS/RePEc record
    url: https://ideas.repec.org/a/inm/ormnsc/v39y1993i1p17-31.html
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s4
    title: "From Nobel Prize to Project Management: Getting Risks Right"
    publisher: Project Management Journal 37(3), 5-15 (Flyvbjerg, 2006), arXiv author copy
    url: https://arxiv.org/pdf/1302.3642
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s5
    title: "Developing expert political judgment: The impact of training and practice on judgmental accuracy in geopolitical forecasting tournaments"
    publisher: Judgment and Decision Making 11(5), 509-526 (Chang, Chen, Mellers & Tetlock, 2016)
    url: https://dlab.sauder.ubc.ca/sjdm/journal/16/16511/jdm16511.html
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s6
    title: "Five things you should know about cost overrun"
    publisher: Transportation Research Part A 118, 174-190 (Flyvbjerg et al., 2018), White Rose Research Online author copy
    url: https://eprints.whiterose.ac.uk/139423/3/CCT1%20Mgt%20ResponseLoveAhiaga-DagbuiTRA3.3Submit1-1.pdf
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Taking the outside view

Taking the outside view means forecasting a case by first asking how a class of similar cases has turned out, rather than by reasoning only from the case's own plan, story and features. Kahneman and Tversky framed the problem as two kinds of information: singular data about the particular case, and distributional data about outcomes across comparable cases. People lean heavily on the first and give too little weight to the second, even when the case data are thin.[^s1] The outside view deliberately puts the distribution first.

## Origin

The method began as a corrective procedure in a 1977 technical report Kahneman and Tversky wrote for a US defence research agency, the same report that named the planning fallacy as a result of neglecting distributional data.[^s1] It built on their earlier finding that intuitive predictions follow representativeness: people pick or rank outcomes by how well they match their impression of the case, with little regard for base rates or for how predictive the evidence is, so numerical forecasts fail to regress.[^s2] In 1993 Kahneman and Dan Lovallo contrasted this with the "inside view", which anchors forecasts on a specific plan and its scenarios and breeds bold, optimistic predictions.[^s3] Bent Flyvbjerg later turned the idea into reference class forecasting for large projects; the UK Department for Transport adopted reference-class cost uplifts in 2004, and the American Planning Association endorsed the method in 2005.[^s4]

## How it works

The inside view builds a forecast from the steps of the plan, which makes a vivid, coherent scenario feel likely. The outside view ignores those details at first and asks what usually happens to plans like this one.[^s3][^s4] Kahneman's own example: a team writing a school curriculum estimated 18 to 30 months to finish; when asked about comparable teams, an expert recalled that about 40% never finished and the rest took seven to ten years. The team set this aside and needed about eight years.[^s4]

The 1977 report gives a worked numerical version. An editor expects a manuscript to sell 12,000 copies, while books of its kind average 4,000. If the editor could rank pairs of manuscripts correctly 80% of the time, predictability is about 0.6, so the corrected forecast is 4,000 plus 0.6 times the 8,000 gap, or 8,800 copies.[^s1] The correction pulls an impression-driven forecast back toward the class average in proportion to how reliable the impression really is.[^s1]

## How to apply it

1. **Choose a reference class** of comparable past cases, balancing breadth against similarity.[^s1][^s4]
2. **Get the distribution** of outcomes in that class: its average and spread, or percentiles such as the 50th and 80th.[^s1][^s4]
3. **Make the case-specific estimate** from what you know about this case.[^s1]
4. **Judge predictability:** how well have such case details predicted outcomes before?[^s1]
5. **Adjust from the base rate toward your estimate** only as far as that predictability warrants, then position the case within the distribution.[^s1][^s4]

In a workplace setting, a manager who expects a software migration to take three months would first look up how long the organisation's last ten migrations took and start from that figure. The main pitfalls are picking a flattering reference class, having no comparable cases for a truly novel situation, and treating the base rate as a ceiling rather than a starting point.[^s1][^s4]

## Evidence

The originators stated in 1977 that their corrective procedure had not been systematically tested.[^s1] Later evidence is encouraging but uneven. In four years of geopolitical forecasting tournaments (2011–2015), a training module of under an hour that taught comparison classes and base rates improved accuracy by roughly 6–12% per year in randomised comparisons, and citing comparison classes was the reasoning habit most strongly tied to better scores, though that last link is correlational.[^s5] In infrastructure, the method is disputed: Love and Ahiaga-Dagbui argued in 2018 that cost-overrun data behind reference class forecasting are unrepresentative and that the method oversimplifies estimation, and Flyvbjerg and colleagues published a point-by-point rebuttal.[^s6] Hence the status here is *mixed*.

## Connections

- **Introduced by** Daniel Kahneman and Amos Tversky as a corrective for intuitive prediction.[^s1]
- **Counteracts** the representativeness heuristic, whose impression-matching forecasts ignore base rates and fail to regress, by forcing the reference-class distribution into the estimate.[^s1][^s2]
- **Counteracts** base-rate neglect and the planning fallacy, both traced to neglect of distributional data.[^s1]
- **Contrasts with** the inside view, the plan-based forecast that produces bold predictions.[^s3]
- **Applied in** project management as reference class forecasting and in geopolitical forecasting.[^s4][^s5]
- **Supported by** the Chang et al. forecasting-training study and **challenged by** Love and Ahiaga-Dagbui's critique of its use for cost overruns.[^s5][^s6]
- **Related to** regression to the mean, which the correction formula applies, and natural frequencies, another way of keeping base rates in view.[^s1]

## Sources

[^s1]: Kahneman & Tversky, "Intuitive Prediction: Biases and Corrective Procedures", technical report, 1977. https://apps.dtic.mil/sti/pdfs/ADA047747.pdf (accessed 2026-11-05)
[^s2]: Kahneman & Tversky, "On the Psychology of Prediction", Oregon Research Institute Research Bulletin No. 4, 1972. https://scholarsbank.uoregon.edu/items/098a706d-e32d-4d73-ba06-6dd92ae502a9/full (accessed 2026-11-05)
[^s3]: Kahneman & Lovallo, "Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking", Management Science 39(1), 1993. https://ideas.repec.org/a/inm/ormnsc/v39y1993i1p17-31.html (accessed 2026-11-05)
[^s4]: Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right", Project Management Journal 37(3), 2006. https://arxiv.org/pdf/1302.3642 (accessed 2026-11-05)
[^s5]: Chang, Chen, Mellers & Tetlock, "Developing expert political judgment", Judgment and Decision Making 11(5), 2016. https://dlab.sauder.ubc.ca/sjdm/journal/16/16511/jdm16511.html (accessed 2026-11-05)
[^s6]: Flyvbjerg et al., "Five things you should know about cost overrun", Transportation Research Part A 118, 2018. https://eprints.whiterose.ac.uk/139423/3/CCT1%20Mgt%20ResponseLoveAhiaga-DagbuiTRA3.3Submit1-1.pdf (accessed 2026-11-05)
