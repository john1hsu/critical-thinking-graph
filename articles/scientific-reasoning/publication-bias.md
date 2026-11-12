---
id: ct:publication-bias
type: Phenomenon
title: Publication bias
aliases: [file drawer problem, file-drawer effect, positive-results bias, non-publication bias]
domain: scientific-reasoning
summary: >-
  The distortion of a research literature that arises when whether a study is
  written up and published depends on the direction or strength of its
  results, so that significant, favourable findings are over-represented and
  null or unfavourable ones stay in the file drawer.
level: intermediate
evidenceStatus: robust
broader: [ct:reporting-bias]
related: [ct:selection-bias, ct:replication-crisis, ct:null-hypothesis-significance-testing, ct:systematic-review, ct:meta-analysis, ct:preregistration, ct:suppressed-evidence, ct:power-analysis, ct:conflict-of-interest]
requires: [ct:null-hypothesis-significance-testing]
relations:
  - {predicate: instanceOf, object: ct:reporting-bias, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:turner-2008-antidepressant-selective-publication-study, source: s4, confidence: high}
  - {predicate: demonstratedBy, object: ct:franco-2014-tess-file-drawer-study, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:schmucker-2014-non-publication-cohort-review, source: s5, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Publication bias"
    publisher: "Catalogue of Bias, Centre for Evidence-Based Medicine, University of Oxford (DeVito & Goldacre, 2019)"
    url: https://catalogofbias.org/biases/publication-bias/
    type: academic
    accessed: 2026-11-12
  - id: s2
    title: "Publication Decisions and Their Possible Effects on Inferences Drawn from Tests of Significance - or Vice Versa"
    publisher: Journal of the American Statistical Association 54(285), 30-34 (Sterling, 1959); scanned copy hosted by gwern.net
    url: https://www.Gwern.net/doc/statistics/bias/publication/1959-sterling.pdf
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Publication bias in the social sciences: Unlocking the file drawer"
    publisher: Science 345(6203), 1502-1505 (Franco, Malhotra & Simonovits, 2014); author copy hosted by gwern.net
    url: https://Www.Gwern.net/doc/statistics/bias/publication/2014-franco.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Selective Publication of Antidepressant Trials and Its Influence on Apparent Efficacy"
    publisher: New England Journal of Medicine 358(3), 252-260 (Turner, Matthews, Linardatos, Tell & Rosenthal, 2008); abstract via QxMD Read
    url: https://read.qxmd.com/read/18199864/selective-publication-of-antidepressant-trials-and-its-influence-on-apparent-efficacy
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "Extent of Non-Publication in Cohorts of Studies Approved by Research Ethics Committees or Included in Trial Registries"
    publisher: PLOS ONE 9(12), e114023 (Schmucker, Schell, Portalupi et al., OPEN consortium, 2014)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4275183/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "The File Drawer Problem (Publication Bias)"
    publisher: "Common Mistakes in Using Statistics, Department of Mathematics, University of Texas at Austin"
    url: https://web.ma.utexas.edu/users/mks/statmistakes/filedrawer.html
    type: academic
    accessed: 2026-11-12
created: 2026-11-12
---

# Publication bias

Publication bias occurs when the chance that a study is published depends on what it found.[^s1] Studies with statistically significant or favourable results reach journals more often than studies with null or unfavourable results, so the published record is a filtered sample of the research actually done.[^s1] The Catalogue of Bias at Oxford classes it as a form of reporting bias, closely related to the wider problem of dissemination bias.[^s1] When the filter screens out non-significant studies it is often called the "file drawer problem", after the place where unpublished results end up.[^s6]

## Origin

The statistician Theodore Sterling raised the alarm in 1959. He examined four psychology journals from 1955–56 and found that of 294 reports using significance tests, 286 rejected the null hypothesis and only 8 did not; none of the 362 reports was a replication.[^s2] He argued that if non-significant results go unpublished, others may repeat an experiment until chance produces a significant result, which then gets printed and is rarely checked again.[^s2] The stated significance level of a published study therefore understates the real risk of a Type I error, and Sterling suspected the same practice in biology, medicine and sociology.[^s2] For reviews and meta-analyses, Robert Rosenthal later proposed a "fail-safe number": how many unpublished null studies would be needed to overturn a meta-analytic result.[^s6]

## How it works

Imagine twenty teams in different companies each test whether a new onboarding email raises customer retention, and the email in fact does nothing. At the conventional 5% threshold, about one team will see a "significant" lift by chance.[^s6] That team writes a conference talk; the other nineteen shelve their flat results as uninteresting. A manager who reads the literature sees one clean success and no failures, and reasonably but wrongly concludes the email works. Nothing dishonest happened in any single study; the distortion comes from which results travelled.[^s2][^s6]

The same filter inflates effect sizes, not just false positives. In the FDA's files on 12 antidepressants, 74 trials were registered, but 31% of them (3,449 participants) never appeared in print.[^s4] Almost every trial the FDA judged positive was published, while most negative or questionable trials were either unpublished or written up so as to read as positive.[^s4] The journals made 94% of trials look positive against 51% in the FDA record, and the published effect size was 32% larger overall.[^s4]

Much of the filtering happens before a journal sees a manuscript. Franco, Malhotra and Simonovits followed 221 survey experiments run through the NSF-funded TESS programme, a known population of completed, peer-reviewed studies.[^s3] Strong results had roughly a 60% chance of publication against about 20% for null results, and 65% of null results were never even written up; among papers that were written up, result strength did not predict acceptance.[^s3] Researchers abandoned null projects because they expected them to have little publication potential.[^s3]

## Evidence

Publication bias is one of the best-documented problems in research methodology.[^s1] A 2014 systematic review by Schmucker and colleagues pooled cohorts of studies tracked from ethics-committee approval or trial registration: only about 46% of approved studies and 54% of registered trials were published, and approved studies with significant results had 2.8 times the odds of publication (95% CI 2.2–3.5).[^s5] The Catalogue of Bias cites further cases, including NIH-funded psychotherapy trials for depression in which adding unpublished data cut the pooled effect by a quarter.[^s1]

Its consequences are harder to size than its prevalence. Most research has measured how often results go unpublished rather than how much that changes conclusions, and the direction and magnitude of the bias in any given field are difficult to estimate.[^s1] Detection tools are imperfect: funnel plots and asymmetry tests need careful interpretation, and the fail-safe number has been criticised because it assumes the unpublished studies themselves average a null effect.[^s1][^s6]

## How to spot it and what reduces it

- **Ask what is missing.** Compare published studies with trial registries, regulatory reviews and conference abstracts; systematic reviewers are advised to search beyond journal databases and contact trialists.[^s1]
- **Be wary of a literature with no failures.** A run of uniformly positive, small studies is itself a warning sign, as Sterling's near-100% rejection rate showed.[^s2]
- **Prefer registered and preregistered work.** Registration with mandatory results reporting, pre-analysis plans, two-stage review and outlets for null results all aim at the file drawer, though compliance with reporting rules has been patchy.[^s1][^s3]

## Connections

- **Instance of reporting bias,** the family of biases in which what is reported depends on the results.[^s1]
- **Demonstrated by Turner and colleagues' 2008 antidepressant study,** which compared FDA records with the journals and showed both missing trials and inflated effects.[^s4]
- **Demonstrated by Franco, Malhotra and Simonovits's 2014 TESS study,** which traced the file drawer to authors not writing up null results.[^s3]
- **Supported by Schmucker and colleagues' 2014 review** of non-publication across ethics-committee and registry cohorts.[^s5]
- **Related to selection bias:** both distort estimates by filtering which cases are observed, but here the filter acts on whole studies after the results are known.[^s1][^s6]
- **Related to the replication crisis, preregistration and systematic reviews:** it inflates false positives and effect sizes in what later fails to replicate, preregistration and registries are the main structural fixes, and systematic reviews must search for missing results to avoid inheriting it.[^s1][^s3]
- **Requires null-hypothesis significance testing,** because the filter usually operates on whether a result crossed the significance threshold.[^s2]
- **Related to suppressed evidence:** the everyday fallacy of leaving out unfavourable facts mirrors, at the level of one arguer, what publication bias does to a whole literature.[^s1]

## Sources

[^s1]: DeVito & Goldacre, "Publication bias", Catalogue of Bias, Centre for Evidence-Based Medicine, University of Oxford (2019). https://catalogofbias.org/biases/publication-bias/ (accessed 2026-11-12)
[^s2]: Sterling, "Publication Decisions and Their Possible Effects on Inferences Drawn from Tests of Significance - or Vice Versa", Journal of the American Statistical Association 54:30-34 (1959). https://www.Gwern.net/doc/statistics/bias/publication/1959-sterling.pdf (accessed 2026-11-12)
[^s3]: Franco, Malhotra & Simonovits, "Publication bias in the social sciences: Unlocking the file drawer", Science 345:1502-1505 (2014). https://Www.Gwern.net/doc/statistics/bias/publication/2014-franco.pdf (accessed 2026-11-12)
[^s4]: Turner, Matthews, Linardatos, Tell & Rosenthal, "Selective Publication of Antidepressant Trials and Its Influence on Apparent Efficacy", New England Journal of Medicine 358:252-260 (2008). https://read.qxmd.com/read/18199864/selective-publication-of-antidepressant-trials-and-its-influence-on-apparent-efficacy (accessed 2026-11-12)
[^s5]: Schmucker et al., "Extent of Non-Publication in Cohorts of Studies Approved by Research Ethics Committees or Included in Trial Registries", PLOS ONE 9(12):e114023 (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4275183/ (accessed 2026-11-12)
[^s6]: "The File Drawer Problem (Publication Bias)", Common Mistakes in Using Statistics, Department of Mathematics, University of Texas at Austin. https://web.ma.utexas.edu/users/mks/statmistakes/filedrawer.html (accessed 2026-11-12)
