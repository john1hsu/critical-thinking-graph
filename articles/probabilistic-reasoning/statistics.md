---
id: ct:statistics
type: Field
title: Statistics
aliases: [statistical science, the discipline of statistics]
domain: probabilistic-reasoning
summary: >-
  The science of collecting, analysing, presenting and interpreting data:
  describing what a body of data shows and drawing inferences from samples to
  the populations or processes that produced them, with probability used to
  measure how far those inferences can be trusted.
level: introductory
evidenceStatus: normative
broader: [ct:mathematics]
related: [ct:statistical-reasoning, ct:statistical-literacy, ct:probability-theory, ct:null-hypothesis-significance-testing, ct:hypothesis-testing, ct:random-sampling, ct:p-hacking, ct:replication-crisis, ct:karl-pearson, ct:forecasting, ct:overfitting]
requires: [ct:probability-theory]
relations:
  - {predicate: formalizedBy, object: ct:probability-theory, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:ronald-fisher, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:scientific-method, source: s3, confidence: high}
  - {predicate: contrastsWith, object: ct:statistical-reasoning, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Statistics"
    publisher: Encyclopaedia Britannica (The Editors of Encyclopaedia Britannica)
    url: https://www.britannica.com/science/statistics
    type: encyclopedia
    accessed: 2026-11-18
  - id: s2
    title: "Statistical Methods for Research Workers, Chapter 1: Introductory"
    publisher: "Oliver and Boyd (R. A. Fisher, 1925), Classics in the History of Psychology, York University"
    url: https://psychclassics.yorku.ca/Fisher/Methods/chap1.htm
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Statistical Thinking in Empirical Enquiry"
    publisher: "International Statistical Review 67(3), 223-265 (Wild & Pfannkuch, 1999), University of Auckland IASE copy"
    url: https://www.stat.auckland.ac.nz/~iase/publications/isr/99.Wild.Pfannkuch.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "The ASA's Statement on p-Values: Context, Process, and Purpose"
    publisher: "The American Statistician 70(2), 129-133 (Wasserstein & Lazar, 2016), doi:10.1080/00031305.2016.1154108, UC Berkeley course copy"
    url: https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Statistics

Statistics is the discipline concerned with gathering data, summarising it, and reasoning from it to conclusions that go beyond the data in hand.[^s1] It has two broad halves. Descriptive statistics condenses data into tables, graphs and summary numbers such as the mean, median and standard deviation, looking at one variable at a time or at the relationships among several. Inferential statistics uses a sample to make claims about a larger population, chiefly through estimation and hypothesis testing, and relies on probability to say how precise and reliable those claims are.[^s1] For critical thinking, statistics is the field that supplies the formal standards behind everyday judgments about averages, trends, risks and "what the data show".

## Origin

Much of the early push for the field came from governments that needed census figures and information about economic activity, while the probability methods it now depends on were first worked out to analyse games of chance.[^s1] The modern discipline took shape in the early twentieth century. In *Statistical Methods for Research Workers* (1925), R. A. Fisher described statistics as the study of populations, of variation and of methods for reducing data, and treated a set of observations as a random sample from a hypothetical larger population whose unknown parameters the statistics estimate.[^s2] He divided the work of reducing data into three problems: specifying the mathematical form of the population, estimating its parameters, and finding how those estimates and tests of fit are distributed across repeated samples.[^s2] That framing, in which variation is the object of study rather than a nuisance, still organises introductory courses.

## How it works

Statistical work is usually described as an investigative cycle rather than a set of formulas. Wild and Pfannkuch (1999), drawing on interviews with students and professional statisticians, adapted the PPDAC cycle: define the Problem, Plan how to collect data, gather the Data, carry out the Analysis, and draw Conclusions that feed new questions.[^s3] Alongside the cycle they identified ways of thinking they regard as fundamentally statistical: recognising that data are needed instead of anecdote, changing how data are represented to see them better (which they call transnumeration), paying attention to variation, reasoning with statistical models, and integrating the numbers with knowledge of the real-world context.[^s3]

A workplace example: a support manager hears that the new ticketing system has made replies slower. The statistical response is to ask what "slower" means (median time to first reply?), plan a comparison over comparable weeks, pull the logs rather than rely on a few memorable complaints, plot the distributions for before and after, and ask whether the difference is larger than ordinary week-to-week variation and whether something else, such as a holiday backlog, changed at the same time.[^s3] Each step guards against a familiar reasoning error, from hasty generalisation over vivid cases to mistaking noise for a signal.

## Evidence and limitations

Statistical tools are only as good as their interpretation. In 2016 the American Statistical Association issued its first formal statement on a specific statistical practice, prompted by widespread misuse of p-values and concern about reproducibility.[^s4] Its six principles include that a p-value is not the probability that a hypothesis is true, that decisions should not rest only on whether a result crosses a significance threshold, that valid inference needs full reporting of all analyses run, and that a p-value does not measure the size or importance of an effect.[^s4] The statement is a reminder that the discipline's methods can be applied mechanically in ways its own practitioners reject, and that reading a statistical claim critically means asking how the data were produced as well as what the test says.[^s4]

## Connections

- **Probability theory** is the mathematical machinery statistics uses to quantify uncertainty in inferences, which is why this node is `formalizedBy` it and lists it as a prerequisite.[^s1]
- **Ronald Fisher** shaped the field's modern self-understanding through his account of populations, variation, data reduction and the problems of specification, estimation and distribution.[^s2]
- **Scientific method**: statistics is applied throughout empirical enquiry, from planning data collection to drawing conclusions, as the PPDAC cycle makes explicit.[^s3]
- **Statistical reasoning** contrasts with statistics as a discipline: Wild and Pfannkuch separate the field's techniques from the thinking processes and dispositions people bring to data, which is the subject of that node.[^s3]
- **Null-hypothesis significance testing**, **p-hacking** and the **replication crisis** are where misuse of statistical methods meets research credibility, the concern behind the ASA statement.[^s4]

## Sources

[^s1]: Encyclopaedia Britannica, "Statistics". https://www.britannica.com/science/statistics (accessed 2026-11-18)
[^s2]: R. A. Fisher, *Statistical Methods for Research Workers* (1925), ch. 1, via Classics in the History of Psychology. https://psychclassics.yorku.ca/Fisher/Methods/chap1.htm (accessed 2026-11-18)
[^s3]: C. J. Wild & M. Pfannkuch, "Statistical Thinking in Empirical Enquiry", *International Statistical Review* 67(3), 1999. https://www.stat.auckland.ac.nz/~iase/publications/isr/99.Wild.Pfannkuch.pdf (accessed 2026-11-18)
[^s4]: R. L. Wasserstein & N. A. Lazar, "The ASA's Statement on p-Values: Context, Process, and Purpose", *The American Statistician* 70(2), 2016. https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf (accessed 2026-11-18)
