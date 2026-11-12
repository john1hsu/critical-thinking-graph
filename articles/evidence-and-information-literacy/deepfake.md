---
id: ct:deepfake
type: Phenomenon
title: Deepfake
aliases: [deep fake, deepfakes, AI-generated synthetic media, synthetic media forgery]
domain: evidence-and-information-literacy
summary: >-
  A video, photo, audio recording or other media item that has been fabricated or
  manipulated with machine learning so that it looks or sounds authentic, for
  example showing a real person saying or doing something they never did.
level: introductory
evidenceStatus: mixed
broader: [ct:misinformation-and-disinformation]
related: [ct:lateral-reading, ct:source-credibility, ct:prebunking, ct:primary-and-secondary-sources]
requires: []
relations:
  - {predicate: explainedBy, object: ct:generative-adversarial-network, source: s5, confidence: high}
  - {predicate: demonstratedBy, object: ct:kobis-2021-fooled-twice-deepfake-study, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: ct:groh-2022-deepfake-detection-crowds-study, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:diel-2024-deepfake-detection-meta-analysis, source: s3, confidence: high}
  - {predicate: exploits, object: ct:overconfidence-effect, source: s1, confidence: medium}
  - {predicate: amplifies, object: ct:liars-dividend, source: s4, confidence: medium}
  - {predicate: studiedIn, object: ct:cognitive-psychology, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Fooled twice: People cannot detect deepfakes but think they can"
    publisher: iScience 24(11), 103364 (Köbis, Doležalová & Soraperra, 2021), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8602050
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Deepfake detection by human crowds, machines, and machine-informed crowds"
    publisher: Proceedings of the National Academy of Sciences 119(1), e2110013119 (Groh, Epstein, Firestone & Picard, 2022), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740705
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Human performance in detecting deepfakes: A systematic review and meta-analysis of 56 papers"
    publisher: Computers in Human Behavior Reports 16, 100538 (Diel, Lalgi, Schröter, MacDorman, Teufel & Bäuerle, 2024), DOAJ record
    url: https://doaj.org/article/a2803c8a1b9441458f000fd0fe82ea47
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security"
    publisher: California Law Review 107 (Chesney & Citron, 2019)
    url: https://www.californialawreview.org/print/deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security
    type: primary
    accessed: 2026-11-12
  - id: s5
    title: "Science & Tech Spotlight: Deepfakes (GAO-20-379SP)"
    publisher: U.S. Government Accountability Office (2020)
    url: https://www.gao.gov/products/GAO-20-379SP
    type: government
    accessed: 2026-11-12
created: 2026-11-12
---

# Deepfake

A deepfake is a video, photo or audio recording that seems real but has been manipulated or generated with artificial intelligence, typically to make a real person appear to say or do something they never said or did.[^s5] Chesney and Citron use the term broadly for hyper-realistic digital falsification of images, video and audio.[^s4] For critical thinkers the concept matters less as a technology than as a stress test of a long-standing habit: treating a recording as direct evidence of what happened.

## Origin

Chesney and Citron trace the wave of public attention to a Reddit user who posted a tool for inserting celebrities' faces into pornographic videos, and they note that the term itself came from that community.[^s4] The U.S. Government Accountability Office (GAO) reported in 2020 that most deepfake content online was still pornographic and disproportionately targeted women, while warning of uses in disinformation.[^s5] Chesney and Citron's 2019 *California Law Review* article became the standard legal and policy analysis, cataloguing harms to individuals (extortion, sabotage of reputations) and to society (distorted public debate, manipulated elections, eroded trust in institutions and journalism).[^s4]

## How it works

Deepfakes are made with artificial neural networks trained on large numbers of images, usually of faces. GAO describes two common designs: autoencoders, which learn to rebuild a face from a compressed representation, and generative adversarial networks (GANs), in which one network produces fakes while a second tries to tell them from real samples, so each round of feedback makes the output more convincing.[^s5] Basic tools are widely available, though realistic results generally need large image sets.[^s5]

A workplace example: a finance clerk receives a short video call, apparently from a senior manager, asking for an urgent payment to a new supplier. The face and voice look right, so the clerk treats the call as proof of the instruction; impersonation for fraud is one of the harms Chesney and Citron anticipate.[^s4] The critical-thinking error is not failing to spot visual glitches, which people are poor at,[^s1] but letting a single unverified recording stand in for authorisation. The robust move is to verify the request through an independent channel, such as calling the manager back on a known number, before acting, since even perfect detection tools would not help a viewer who never checks.[^s5]

## How to spot and respond to it

- Shift from inspecting the media to checking its provenance: who first published it, and what do other sources say about it? This is the logic of lateral reading.[^s4][^s5]
- Treat a high-stakes recording that arrives through one unverified channel as a claim to be confirmed, not as evidence in itself.[^s4]
- Distrust your own confidence. People who feel sure they can spot fakes are often no better than chance.[^s1]
- Use automated detection as one input, not a verdict. Machine predictions help when correct but can mislead people when wrong.[^s2]
- Remember the reverse risk: a genuine recording can be dismissed as "probably a deepfake".[^s4]

## Evidence

In a preregistered experiment with 210 mostly UK participants, Köbis, Doležalová and Soraperra (2021) found that people identified 16 short videos correctly only 57.6% of the time, barely above chance. Neither an awareness prompt nor a financial incentive improved accuracy. Participants labelled about two-thirds of clips authentic even though half were fake, and they overestimated their own accuracy.[^s1] The authors read this as a "seeing is believing" default rather than the excessive scepticism the liar's-dividend idea would predict.[^s1]

Groh and colleagues (2022) tested over 15,000 people. In a side-by-side task most participants beat a leading detection model, but when judging single videos only a minority did; averaged crowd judgements came close to the model. Showing people the model's prediction raised accuracy when the model was right and lowered it when the model was wrong. Inverting or misaligning faces hurt humans more than the model, suggesting people rely on specialised face processing.[^s2]

A 2024 meta-analysis by Diel and colleagues pooled 56 papers and 86,155 participants. Overall detection accuracy was 55.5%, with a confidence interval that included chance; images and text fared worst and audio best. Feedback training, AI support and caricaturing fakes raised accuracy to about 65%.[^s3] Evidence status is *mixed* because human detection varies widely by medium, task format and assistance, and because the studies mostly use short clips of unknown people without the context real viewers have.[^s2][^s3]

## Connections

- **Broader:** misinformation and disinformation; a deepfake is a fabricated message that can be spread with or without intent to deceive.[^s5]
- **Explained by** generative adversarial networks, the adversarial training method that makes fakes progressively harder to tell from real media.[^s5]
- **Demonstrated by** the Köbis 2021 "fooled twice" experiment and the Groh 2022 crowd-versus-machine study; **supported by** the Diel 2024 meta-analysis of human detection.[^s1][^s2][^s3]
- **Exploits** the overconfidence effect: viewers' confidence in spotting fakes outruns their accuracy, which leaves them more exposed.[^s1]
- **Amplifies** the liar's dividend: as awareness of deepfakes spreads, people caught on genuine recordings can more easily claim the evidence was faked.[^s4]
- **Studied in** cognitive psychology, which examines how people judge the authenticity of media.[^s1]
- **Related to** lateral reading, source credibility and prebunking, which move scrutiny from the artefact to its source, and to the distinction between primary and secondary sources, since a recording can only serve as primary evidence once its authenticity is established.[^s4]

## Sources

[^s1]: Köbis, Doležalová & Soraperra, "Fooled twice: People cannot detect deepfakes but think they can", *iScience* 24(11), 103364 (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8602050 (accessed 2026-11-12)
[^s2]: Groh, Epstein, Firestone & Picard, "Deepfake detection by human crowds, machines, and machine-informed crowds", *PNAS* 119(1), e2110013119 (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8740705 (accessed 2026-11-12)
[^s3]: Diel, Lalgi, Schröter, MacDorman, Teufel & Bäuerle, "Human performance in detecting deepfakes: A systematic review and meta-analysis of 56 papers", *Computers in Human Behavior Reports* 16, 100538 (2024). https://doaj.org/article/a2803c8a1b9441458f000fd0fe82ea47 (accessed 2026-11-12)
[^s4]: Chesney & Citron, "Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security", *California Law Review* 107 (2019). https://www.californialawreview.org/print/deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security (accessed 2026-11-12)
[^s5]: U.S. Government Accountability Office, "Science & Tech Spotlight: Deepfakes", GAO-20-379SP (2020). https://www.gao.gov/products/GAO-20-379SP (accessed 2026-11-12)
