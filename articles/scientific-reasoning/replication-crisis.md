---
id: ct:replication-crisis
type: Phenomenon
title: Replication crisis
aliases: [replicability crisis, reproducibility crisis, credibility crisis in science]
domain: scientific-reasoning
summary: >-
  The discovery, concentrated in the 2010s, that a large share of published
  scientific findings, especially in psychology and biomedicine, do not
  reappear when independent teams repeat the studies with new data, and that
  the effects that do reappear are usually much smaller than first reported.
level: intermediate
evidenceStatus: robust
broader: [ct:scientific-method]
related: [ct:researcher-degrees-of-freedom, ct:power-analysis, ct:null-hypothesis-significance-testing, ct:preregistration, ct:p-hacking, ct:publication-bias, ct:systematic-review, ct:daniel-kahneman]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: demonstratedBy, object: ct:open-science-collaboration-2015-reproducibility-project, source: s1, confidence: high}
  - {predicate: supportedBy, object: ct:why-most-published-research-findings-are-false, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:publication-bias, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:researcher-degrees-of-freedom, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:gilbert-2016-comment-on-reproducibility, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Estimating the reproducibility of psychological science"
    publisher: Science 349(6251), aac4716 (Open Science Collaboration, 2015); author copy, Utrecht University repository
    url: https://dspace.library.uu.nl/bitstream/1874/329878/1/aac4716.full.pdf
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Why Most Published Research Findings Are False"
    publisher: PLoS Medicine 2(8), e124 (Ioannidis, 2005); copy hosted by Carnegie Mellon University, Department of Statistics
    url: https://www.stat.cmu.edu/~ryantibs/journalclub/ioannidis_2005.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Replicability, Robustness, and Reproducibility in Psychological Science"
    publisher: Annual Review of Psychology 73, 719-748 (Nosek, Hardwicke, Moshontz, Allard, Corker, Dreber et al., 2022)
    url: https://annualreviews.org/doi/pdf/10.1146/annurev-psych-020821-114157
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "New Report Examines Reproducibility and Replicability in Science, Recommends Ways to Improve Transparency and Rigor in Research"
    publisher: National Academies of Sciences, Engineering, and Medicine (news release, May 2019)
    url: https://www.nationalacademies.org/news/2019/05/new-report-examines-reproducibility-and-replicability-in-science-recommends-ways-to-improve-transparency-and-rigor-in-research
    type: institutional
    accessed: 2026-11-12
created: 2026-11-12
---

# Replication crisis

The replication crisis is the name given to the realisation that many published scientific findings do not hold up when other researchers repeat the work with fresh data. Systematic replication projects in the 2010s found that only a minority to a modest majority of sampled findings reappeared, and that replicated effects were typically about half the size originally reported.[^s1][^s3] Replication here means testing a prior claim with new data; it differs from reproducibility (rerunning the same analysis on the same data) and robustness (reanalysing the same data a different way).[^s3][^s4] For a critical thinker, the lesson is that a single statistically significant study is weaker evidence than its headline suggests.

## Origin

An early and much-cited warning came from epidemiologist John Ioannidis, who argued in *PLoS Medicine* in 2005 that, under realistic assumptions, most claimed research findings in many fields are likely to be false.[^s2] His model showed that the probability a "significant" finding is true falls when studies are small, true effects are small, many hypotheses are tested with little prior plausibility, designs and analyses are flexible, financial or ideological interests are present, and many competing teams chase the same question.[^s2] In psychology, attention sharpened in the early 2010s after papers such as Simmons, Nelson and Simonsohn (2011) showed how analytic flexibility could make false hypotheses look supported; Nosek and colleagues later described the decade as one of crisis or renaissance, depending on perspective.[^s3]

The landmark test was the Reproducibility Project: Psychology, published by the Open Science Collaboration in *Science* in 2015. Some 270 contributors repeated 100 studies from three leading 2008 journals; 97% of the originals had reported significant results, but only 36% of the replications did, and the average effect size roughly halved.[^s1]

## How it works

The crisis is less about fraud than about ordinary incentives and statistics interacting. Journals favour novel, positive results; studies are often underpowered; and researchers have many defensible choices about exclusions, measures and analyses. Together these let chance findings and inflated effects into print, while null results stay in file drawers.[^s2][^s3] Later replications, run with larger samples and fixed plans, then regress toward the true (often smaller or zero) effect.

A workplace example: an HR team reads a single study, with 40 participants, reporting that a ten-minute mindset exercise raised productivity by a large margin. The replication-crisis lens prompts checks before a company-wide rollout. Was the study preregistered? Has an independent team replicated it with a large sample? Was the effect surprising, or an interaction that holds only for one subgroup? In the 2015 project, surprising effects and interaction effects replicated markedly less often, and stronger original evidence (smaller p-values, larger effects) predicted success.[^s1] A prudent team would run a small pilot of its own or wait for a well-powered replication.

## Evidence

The core finding has itself replicated across projects. A 2022 *Annual Review of Psychology* synthesis of 307 replications in psychology reported that 64% were significant in the same direction, with effects about 68% as large as the originals; rates varied widely, from about 90% for a set of personality associations to 36% in the 2015 project and 62% for 21 social-science experiments from *Nature* and *Science*.[^s3] Cognitive psychology replicated better than social psychology in the 2015 sample (about 50% versus 25%).[^s1] A 2019 congressionally mandated National Academies report found that systematic efforts to reproduce computational results failed more than half the time, mainly because data, code and workflows were insufficiently documented.[^s4]

Limitations matter. The 2015 authors cautioned that a failed replication does not prove an original false, since samples or procedures may differ, and that their sample of studies may not generalise.[^s1] The National Academies report declined to call the situation a crisis, noting that the true extent of non-replicability across science is unknown and that some non-replication is a normal route to discovery.[^s4] Gilbert and colleagues (2016) argued that the 2015 failures reflected low-fidelity, underpowered replications; Nosek and colleagues report that later high-powered replications with expert-reviewed protocols produced little or no increase in effect sizes, which weakens that defence.[^s3]

## Connections

The phenomenon was **demonstrated by** the Open Science Collaboration's 2015 Reproducibility Project, the first large, systematic estimate of replicability in psychology.[^s1] It is **supported by** Ioannidis's 2005 paper, which predicted low reliability of published findings from first principles.[^s2] It is **explained by** publication bias and questionable research practices that inflate effect sizes and false-positive rates,[^s3] and by researcher degrees of freedom, the flexibility in design, outcomes and analysis that Ioannidis identified as a driver of bias.[^s2] Its severity has been **challenged by** Gilbert and colleagues' 2016 critique of replication fidelity, though later evidence has not borne that critique out.[^s3] Reforms aimed at it include preregistration, registered reports, larger samples guided by power analysis, and open data and code; audits suggest adoption has been slow.[^s3] Because it rests on how p-values behave, it presupposes an understanding of null-hypothesis significance testing.

## Sources

[^s1]: Open Science Collaboration, "Estimating the reproducibility of psychological science", *Science* 349 (2015). https://dspace.library.uu.nl/bitstream/1874/329878/1/aac4716.full.pdf (accessed 2026-11-12)
[^s2]: Ioannidis, "Why Most Published Research Findings Are False", *PLoS Medicine* 2(8) (2005). https://www.stat.cmu.edu/~ryantibs/journalclub/ioannidis_2005.pdf (accessed 2026-11-12)
[^s3]: Nosek et al., "Replicability, Robustness, and Reproducibility in Psychological Science", *Annual Review of Psychology* 73 (2022). https://annualreviews.org/doi/pdf/10.1146/annurev-psych-020821-114157 (accessed 2026-11-12)
[^s4]: National Academies of Sciences, Engineering, and Medicine, "New Report Examines Reproducibility and Replicability in Science" (2019). https://www.nationalacademies.org/news/2019/05/new-report-examines-reproducibility-and-replicability-in-science-recommends-ways-to-improve-transparency-and-rigor-in-research (accessed 2026-11-12)
