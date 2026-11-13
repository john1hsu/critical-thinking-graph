---
id: ct:epidemiology
type: Field
title: Epidemiology
aliases: [epidemiological reasoning, population health science]
domain: scientific-reasoning
summary: >-
  The study of how health-related states and events are distributed in
  specified populations and what determines them, and the application of that
  study to controlling health problems; the basic science of public health and
  a training ground for reasoning about cause from observational data.
level: intermediate
evidenceStatus: robust
broader: [ct:public-health]
related: [ct:confounding, ct:selection-bias, ct:correlation-versus-causation, ct:causal-inference, ct:randomized-controlled-trial, ct:evidence-based-medicine, ct:falsifiability, ct:necessary-and-sufficient-conditions, ct:regression-to-the-mean]
requires: [ct:statistical-reasoning]
relations:
  - {predicate: contrastsWith, object: ct:clinical-medicine, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:john-snow, source: s2, confidence: high}
  - {predicate: influencedBy, object: ct:austin-bradford-hill, source: s4, confidence: high}
  - {predicate: influencedBy, object: ct:hypothesis-testing, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Principles of Epidemiology in Public Health Practice, Lesson 1: Introduction to Epidemiology, Section 1: Definition of Epidemiology"
    publisher: Centers for Disease Control and Prevention (3rd ed., archived)
    url: https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html
    type: government
    accessed: 2026-11-13
  - id: s2
    title: "A Rivalry of Foulness: Official and Unofficial Investigations of the London Cholera Epidemic of 1854"
    publisher: "American Journal of Public Health 88(10) (Paneth, Vinten-Johansen, Brody & Rip, 1998), UCLA Department of Epidemiology copy"
    url: https://epi-snow.ph.ucla.edu/articles/Paneth_Nigel_John_Snow_AJPH_1998.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Causation and Causal Inference in Epidemiology"
    publisher: "American Journal of Public Health 95(S1), S144-S150 (Rothman & Greenland, 2005), doi:10.2105/AJPH.2004.059204, University of Kent course copy"
    url: https://blogs.kent.ac.uk/jonw/files/2015/03/Rothman-Greenland-05-Causation-and-Causal-Inference-in-Epidemiology.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "When truth is unwelcome: the first reports on smoking and lung cancer"
    publisher: "Bulletin of the World Health Organization 83(2), 144-145 (Michael J. Thun, 2005)"
    url: https://scielosp.org/pdf/bwho/2005.v83n2/144-145/en
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Epidemiology

Epidemiology is the study of how health-related states or events are distributed in specified populations and what determines them, together with the use of that knowledge to control health problems.[^s1] The US Centers for Disease Control and Prevention (CDC) calls it the basic science of public health: a systematic, data-driven discipline that compares observed frequencies against suitable comparison groups, draws on biostatistics, and relies on causal reasoning.[^s1] Its subject matter is wider than infectious disease, taking in chronic illness, injuries, birth defects, behaviours such as seat-belt use, and genetic markers.[^s1] For critical thinking it matters because it is the discipline that has thought hardest about when an association seen in messy, non-experimental data justifies a causal conclusion.[^s3]

## Origin

A founding episode is John Snow's investigation of the London cholera epidemic of 1854. Snow traced a September outbreak around Golden Square to the Broad Street pump and correlated cholera deaths in South London with which water company supplied each household, a contrast he described as a naturally occurring experiment.[^s2] Paneth and colleagues, writing in the *American Journal of Public Health* in 1998, argue that Snow's strength lay in proposing a specific transmissible agent in faecally contaminated water and deriving predictions that could fail: brewery workers with their own water supply stayed well, while a victim in cholera-free Hampstead turned out to have drunk Broad Street water.[^s2] They contrast this hypothetico-deductive style with the official Board of Health inquiry, which gathered data inductively within the miasma theory and clarified far less.[^s2]

The field's modern case-control and cohort designs were proved on smoking. Richard Doll and Austin Bradford Hill began a case-control study in 1948 and published preliminary results in 1950, one of five such studies that year linking cigarettes to lung cancer in men; by Michael Thun's later estimate it implied a relative risk of about 14 for smokers versus never-smokers.[^s4] Because the result was received as provocative rather than conclusive, they launched the prospective British Doctors' Study, which confirmed the link and added heart disease, stroke and other harms.[^s4]

## How it works

The CDC breaks the definition into parts.[^s1] *Distribution* means frequency, expressed as rates relative to population size so that groups can be compared, and pattern, described by time, place and person. *Determinants* are the causes and risk factors that explain why illness is not random. *Descriptive* epidemiology characterises events by time, place and person; *analytic* epidemiology compares groups with different rates to find risk factors.[^s1] The perspective is collective: for an outbreak of diarrhoea, the clinician treats the patient, while the epidemiologist asks what the exposure was, who else was exposed, and how to stop further cases.[^s1]

A workplace example shows the reasoning. Several staff at a company report stomach illness after an off-site training day. A descriptive step tallies who fell ill, when symptoms began and which session each person attended. An analytic step compares attack rates between those who ate each catered dish and those who did not; if illness concentrates among people who ate the chicken salad while those who skipped it stay well, the salad becomes the leading hypothesis, and the predicted result of a lab test on leftovers can confirm or refute it.[^s1][^s2]

Rothman and Greenland's sufficient-component cause model frames the underlying logic. A sufficient cause is a minimal set of conditions that together produce disease; each member is a component cause, and most diseases have several such mechanisms.[^s3] Hence most risk factors are neither necessary nor sufficient on their own, yet removing any one can prevent the cases that depend on it, and the apparent strength of a factor depends on how common its complementary causes are in a given population.[^s3]

## Evidence and limitations

Epidemiology mostly works with observational data, so its central hazards are bias and confounding. Rothman and Greenland argue that causal claims can never be proven, following Hume, and that the job is better seen as estimating the size of an effect while quantifying its error from chance, bias and confounding.[^s3] They also review Hill's nine viewpoints, such as strength, consistency, temporality and dose-response gradient, and conclude that each has exceptions and none is necessary or sufficient, so using them as a checklist is unreliable; turning them into deductive tests of rival hypotheses is more defensible.[^s3] Social context can slow acceptance too: Thun notes that the 1950 smoking findings met resistance partly because most doctors of the day smoked.[^s4]

## Connections

- **Contrasts with clinical medicine.** The CDC frames the clinician's patient as the individual and the epidemiologist's patient as the community.[^s1]
- **Influenced by John Snow.** His 1854 cholera work is held up as a model of hypothesis-driven field investigation.[^s2]
- **Influenced by Austin Bradford Hill.** The Doll and Hill smoking studies established case-control and cohort designs for chronic disease.[^s4]
- **Influenced by hypothesis testing (the hypothetico-deductive method).** Rothman and Greenland defend a refutationist approach to causal inference, and Paneth and colleagues credit Snow's success to it.[^s2][^s3]
- **Related.** Confounding, selection bias and the gap between correlation and causation are its standing problems; randomised controlled trials and evidence-based medicine build on its methods; its component-cause model uses the language of necessary and sufficient conditions; and it requires basic statistical reasoning about rates and comparison groups.[^s1][^s3]

## Sources

[^s1]: CDC, "Principles of Epidemiology in Public Health Practice, Lesson 1, Section 1: Definition of Epidemiology". https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section1.html (accessed 2026-11-13)
[^s2]: N. Paneth, P. Vinten-Johansen, H. Brody & M. Rip, "A Rivalry of Foulness: Official and Unofficial Investigations of the London Cholera Epidemic of 1854", *American Journal of Public Health* 88(10), 1998. https://epi-snow.ph.ucla.edu/articles/Paneth_Nigel_John_Snow_AJPH_1998.pdf (accessed 2026-11-13)
[^s3]: K. J. Rothman & S. Greenland, "Causation and Causal Inference in Epidemiology", *American Journal of Public Health* 95(S1), 2005, S144-S150. https://blogs.kent.ac.uk/jonw/files/2015/03/Rothman-Greenland-05-Causation-and-Causal-Inference-in-Epidemiology.pdf (accessed 2026-11-13)
[^s4]: M. J. Thun, "When truth is unwelcome: the first reports on smoking and lung cancer", *Bulletin of the World Health Organization* 83(2), 2005, 144-145. https://scielosp.org/pdf/bwho/2005.v83n2/144-145/en (accessed 2026-11-13)
