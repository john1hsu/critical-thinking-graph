---
id: ct:mediating-assessments-protocol
type: Technique
title: Mediating assessments protocol
aliases: [MAP, mediating assessments, mediating-assessments protocol, Kahneman-Lovallo-Sibony protocol]
domain: decision-making
summary: >-
  A structured decision procedure from Kahneman, Lovallo and Sibony (2019) that
  breaks a complex judgment into a few attributes defined in advance, has each
  one assessed separately and on the facts, and holds back the overall,
  intuitive verdict until every assessment is in, to curb halo effects,
  premature coherence and noise.
level: intermediate
evidenceStatus: mixed
broader: [ct:debiasing]
related: [ct:structured-analytic-techniques, ct:premortem, ct:delphi-method, ct:outside-view, ct:wisdom-of-crowds, ct:groupthink, ct:judgment-and-decision-making, ct:anchoring-effect]
requires: [ct:halo-effect]
relations:
  - {predicate: introducedBy, object: ct:daniel-kahneman, source: s1, confidence: high}
  - {predicate: introducedIn, object: ct:a-structured-approach-to-strategic-decisions, source: s2, confidence: high}
  - {predicate: counteracts, object: ct:halo-effect, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:noise-in-judgment, source: s1, confidence: medium}
  - {predicate: counteracts, object: ct:overconfidence-effect, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:kuncel-2013-mechanical-versus-holistic-meta-analysis, source: s3, confidence: medium}
  - {predicate: contrastsWith, object: ct:weighted-additive-rule, source: s1, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A Structured Approach to Strategic Decisions"
    publisher: "MIT Sloan Management Review 60(3), 67-73 (Daniel Kahneman, Dan Lovallo & Olivier Sibony, Spring 2019)"
    url: https://sloanreview.mit.edu/article/a-structured-approach-to-strategic-decisions/
    type: primary
    accessed: 2026-11-19
  - id: s2
    title: "Making better decisions every time"
    publisher: "Sydney Business Insights, University of Sydney Business School (12 May 2019; interview with Dan Lovallo)"
    url: https://sbi.sydney.edu.au/making-better-decisions-every-time/
    type: academic
    accessed: 2026-11-19
  - id: s3
    title: "Mechanical versus clinical data combination in selection and admissions decisions: A meta-analysis"
    publisher: "Journal of Applied Psychology 98(6), 1060-1072 (Kuncel, Klieger, Connelly & Ones, 2013); University of Minnesota course reading copy"
    url: https://goal-lab.psych.umn.edu/orgpsych/readings/12.%20Judgment%20&%20Decision%20Making/Kuncel,%20Klieger,%20Connelly%20&%20Ones%20(2013).pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Bias Busters: Avoiding snap judgments"
    publisher: "McKinsey Quarterly (Tim Koller, Dan Lovallo & Phil Rosenzweig, 6 November 2019)"
    url: https://mckinsey.de/capabilities/strategy-and-corporate-finance/our-insights/bias-busters-avoiding-snap-judgments
    type: news
    accessed: 2026-11-19
created: 2026-11-19
---

# Mediating assessments protocol

The mediating assessments protocol (MAP) is a way of organising a big, one-off or recurring judgment, such as an acquisition, a hire or an investment, so that the overall verdict is built from separate, fact-based ratings of a few predefined attributes rather than from a single early impression.[^s1] The "mediating assessments" are those intermediate ratings: they stand between the raw evidence and the final decision, and the final, intuitive judgment is deliberately held back until all of them are complete.[^s1][^s2]

## Origin

Daniel Kahneman, Dan Lovallo and Olivier Sibony set out the protocol in "A Structured Approach to Strategic Decisions", published in *MIT Sloan Management Review* in spring 2019.[^s1] The University of Sydney Business School, where Lovallo works, presented it the same year as a general tool for hiring, project approval, technology investment and mergers.[^s2] The authors trace the idea to structured job interviews and to Kahneman's redesign of Israeli army recruit interviews in the 1950s, in which interviewers scored six separate traits and only then formed an overall view; combining the trait scores with that delayed intuition predicted later performance best.[^s1] Their stated aim was to carry the logic of the structured interview, common in hiring, into strategic decisions where it was rarely used.[^s1][^s2]

## How it works

The authors start from two kinds of error. Biases push judgments in a consistent direction, while noise is unwanted variability, so that different people, or the same person on different days, reach different verdicts from the same facts.[^s1] A central cause of both is what they call excessive coherence: people form a story early from limited information and then read later facts to fit it, so a single vivid strength spreads to every other attribute, which is the halo effect.[^s1]

MAP breaks that chain in three steps.[^s1][^s2]

1. **Define the assessments in advance.** Pick a handful of attributes that matter most, much as a job description lists required competencies.[^s1]
2. **Assess each attribute independently and on the facts.** Each rating draws only on the evidence relevant to that attribute, ideally on a scale anchored to comparable past cases (for example, percentiles against earlier candidates or deals), and without being swayed by the other attributes or by colleagues' views.[^s1][^s2]
3. **Delay the holistic judgment.** Only when the full profile of ratings is visible does the group discuss and decide; intuition is still used, but late. A known deal-breaker can be checked first and end the process early.[^s1]

A workplace example: a product committee choosing between two vendors defines four attributes up front, such as security, total cost, integration effort and vendor stability. A different reviewer rates each from the evidence pack, and the meeting goes through the ratings one at a time before anyone says which vendor they prefer. A slick demo can now raise the integration score, if it shows integration, but cannot quietly lift the security score as well.[^s1]

## How to apply it

- Keep the list short and fix it before evidence arrives; adding criteria afterwards invites rationalising a favourite.[^s1]
- Split each due-diligence report or interview guide into sections that match the attributes and end each with its own rating, considered on that section's evidence alone.[^s1]
- Collect ratings independently before discussion, and ban summary narratives or "overall" opinions until every rating is on the table.[^s1][^s4]
- Prefer comparative or percentile scales to vague words like "good", which different raters read differently.[^s1][^s2]
- The authors advise against fixed numerical weights, leaving the final integration to judgment; teams that must document weights, such as public procurement panels, will need to adapt this step.[^s1]

## Evidence and limitations

Direct evidence for MAP itself is thin. The 2019 article reports the early experience of one venture-capital firm, which used percentile ratings of founding teams partly to stop an impressive product demo inflating the team's scores; the firm found decisions were no slower, but the authors say measurable gains will take years to show.[^s1] The supporting case rests mainly on neighbouring research. A 2013 meta-analysis of 25 samples from 17 studies found that combining predictors by formula beat holistic expert combination for every criterion, for example a validity of .44 versus .28 for job performance, and recommended that experts collect relevant information while the combination step is structured.[^s3] MAP keeps a final intuitive step, so it is a hybrid rather than a pure formula, and the authors accept that it reduces bias and noise without eliminating them.[^s1] Executives attached to gut feel may resist it as mechanical.[^s1][^s2]

## Connections

- **Introduced by Daniel Kahneman**, with Lovallo and Sibony, in *A Structured Approach to Strategic Decisions* (2019).[^s1][^s2]
- **Counteracts the halo effect** by rating attributes one at a time on their own evidence, the purpose the authors give for the venture firm's percentile ratings.[^s1]
- **Counteracts noise in judgment**: independent ratings on shared scales are meant to make evaluators who should be interchangeable agree more often.[^s1]
- **Counteracts overconfidence**, which Lovallo names, with optimism, as the main obstacle the protocol addresses in managers who trust intuition too much.[^s2]
- **Supported by** the Kuncel et al. (2013) meta-analysis showing that structured combination of information outpredicts holistic expert judgment.[^s3]
- **Contrasts with the weighted additive rule**: both decompose a decision into attributes, but MAP deliberately avoids explicit weights and ends with a judgment rather than a computed score.[^s1]
- It **requires** an understanding of the halo effect, the failure its sequencing is built to block.[^s1] It is related to the **premortem** and the **Delphi method**, other structured ways of gathering views independently before a group converges, and to the **outside view**, since anchoring ratings to past comparable cases brings reference-class information into each assessment.[^s1][^s4]

## Sources

[^s1]: Kahneman, Lovallo & Sibony, "A Structured Approach to Strategic Decisions", MIT Sloan Management Review 60(3), 2019. https://sloanreview.mit.edu/article/a-structured-approach-to-strategic-decisions/ (accessed 2026-11-19)
[^s2]: Sydney Business Insights, "Making better decisions every time", University of Sydney Business School, 2019. https://sbi.sydney.edu.au/making-better-decisions-every-time/ (accessed 2026-11-19)
[^s3]: Kuncel, Klieger, Connelly & Ones, "Mechanical versus clinical data combination in selection and admissions decisions: A meta-analysis", Journal of Applied Psychology 98(6), 2013. https://goal-lab.psych.umn.edu/orgpsych/readings/12.%20Judgment%20&%20Decision%20Making/Kuncel,%20Klieger,%20Connelly%20&%20Ones%20(2013).pdf (accessed 2026-11-19)
[^s4]: Koller, Lovallo & Rosenzweig, "Bias Busters: Avoiding snap judgments", McKinsey Quarterly, 2019. https://mckinsey.de/capabilities/strategy-and-corporate-finance/our-insights/bias-busters-avoiding-snap-judgments (accessed 2026-11-19)
