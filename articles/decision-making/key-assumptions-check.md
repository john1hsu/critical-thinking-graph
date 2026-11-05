---
id: ct:key-assumptions-check
type: Technique
title: Key assumptions check
aliases: [key assumption check, KAC, assumptions check]
domain: decision-making
summary: >-
  A structured analytic technique in which an analyst or team writes down the
  current line of reasoning, lists every stated and unstated premise it rests
  on, challenges each one, and keeps only those that must hold for the
  judgment to stand, together with the signs that would show they have failed.
level: introductory
evidenceStatus: contested
broader: [ct:structured-analytic-techniques, ct:debiasing]
related: [ct:analysis-of-competing-hypotheses, ct:devils-advocacy, ct:premortem, ct:consider-the-opposite]
requires: [ct:argument]
relations:
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s1, confidence: high}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s2, confidence: medium}
  - {predicate: influencedBy, object: ct:linchpin-analysis, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:artner-girven-bruce-2016-rand-sat-assessment, source: s3, confidence: low}
  - {predicate: challengedBy, object: ct:mandel-tetlock-2018-correcting-judgment-correctives, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis"
    publisher: US Government, Central Intelligence Agency, Center for the Study of Intelligence (March 2009)
    url: https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf
    type: government
    accessed: 2026-11-05
  - id: s2
    title: "Psychology of Intelligence Analysis"
    publisher: Richards J. Heuer Jr., Center for the Study of Intelligence, Central Intelligence Agency (1999)
    url: https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
    type: primary
    accessed: 2026-11-05
  - id: s3
    title: "Assessing the Value of Structured Analytic Techniques in the U.S. Intelligence Community"
    publisher: RAND Corporation, RR-1408-OSD (Artner, Girven & Bruce, 2016)
    url: https://apps.dtic.mil/sti/tr/pdf/AD1024447.pdf
    type: institutional
    accessed: 2026-11-05
  - id: s4
    title: "Correcting Judgment Correctives in National Security Intelligence"
    publisher: Frontiers in Psychology 9, 2640 (Mandel & Tetlock, 2018)
    url: https://frontiersin.org/article/10.3389/fpsyg.2018.02640/full
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Key assumptions check

A key assumptions check is a short, explicit review of the working assumptions on which a judgment depends. The analyst or team writes out the current conclusion, lists the premises (spoken and unspoken) that must be true for it to hold, and then interrogates each one.[^s1] Its target is the hidden assumption: because people often hold their premises without noticing them, those premises are rarely examined or challenged, and an error in one can quietly undermine an otherwise careful analysis.[^s1]

## Origin

The idea grows out of intelligence-analysis practice at the US Central Intelligence Agency. In his 1999 book *Psychology of Intelligence Analysis*, the CIA veteran Richards Heuer argued that every analyst works through a mental model or mind-set, that an assumption is one component of such a model, and that objectivity comes from making assumptions and reasoning as explicit as possible so others can challenge them.[^s2] The same book credits Douglas MacEachin's "linchpin" approach of the 1990s, which required analysts to spell out the assumptions an argument turns on.[^s2] The technique was codified under its present name in the US Government's 2009 *Tradecraft Primer*, which classes it as a diagnostic technique alongside the quality-of-information check, indicators of change and analysis of competing hypotheses.[^s1]

## How it works

Heuer's diagnosis is that mind-sets form quickly but resist change: new information tends to be absorbed into the existing model rather than prompting a review of its premises, and experienced analysts can be especially prone to this.[^s2] The key assumptions check interrupts that process by turning implicit premises into a written list that can be tested one item at a time, which clarifies the logic of the argument, exposes faulty reasoning and identifies the developments that would justify dropping an assumption.[^s1]

The *Primer* illustrates the method with a 2002 serial-shooting investigation, in which investigators early on worked from a composite picture of the offender and his vehicle. Rating each element separately (highly likely, likely, merely possible) would have shown that some, such as the type of vehicle, rested on thin and conflicting eyewitness reports and should not have been used to narrow the search.[^s1]

*Workplace example.* A retail chain's planning team concludes that opening five stores in a new region will break even within two years. A one-hour check surfaces the assumptions underneath: rents will stay near current quotes; the regional distribution centre has spare capacity; local shoppers will respond to the brand as existing customers do; and no major competitor will enter. Challenging them, the team finds the capacity figure dates from before last year's growth and the customer-response assumption rests on a single survey of existing shoppers. The plan survives, but with a capacity audit before signing leases and a list of warning signs (competitor permits, early sales below target) to watch, as the *Primer*'s final step recommends.[^s1]

## How to apply it

The *Primer* recommends running the check at the start of a project, where an individual or team can usually finish in an hour or two, and again before judgments are finalised.[^s1]

1. **Write down the current analytic line** so everyone sees the same conclusion.[^s1]
2. **List every premise**, stated or unstated, that must be accepted for that line to be true.[^s1]
3. **Challenge each one.** Ask why it must be true, whether it holds under all conditions, how confident the team is and why, whether it was true in the past but may be less so now, and whether its failure would change the conclusion.[^s1]
4. **Refine the list** to the assumptions that must hold, and note the conditions or information that would show each one has failed.[^s1]

**Pitfalls:** a check run by the people who own the conclusion can simply re-endorse it, which is why Heuer pairs explicit assumptions with outside challenge;[^s2] and the method leaves many choices to the analyst, so two teams may produce quite different lists.[^s4]

## Evidence

Direct evidence is thin, so the technique is rated *contested* here. A 2016 RAND pilot review of intelligence products (29 CIA assessments, 14 National Intelligence Council products and 20 other papers) judged one CIA assessment built largely around a key assumptions check to be effective forward-looking analysis, and found that products using structured techniques were better at separating assumptions from judgments, most clearly where assumption checks were explicit.[^s3] The authors stressed that their sample was small and their ratings qualitative, and that there was little or no evidence on whether individual techniques actually reduce the cognitive pitfalls they target.[^s3]

In a 2018 perspective in *Frontiers in Psychology*, David Mandel and Philip Tetlock argued that structured analytic techniques spread through endorsement rather than experimental testing, may add noise because analysts apply them inconsistently, and can inflate confidence; they did not critique the key assumptions check individually, but their objections apply to the family as a whole.[^s4]

## Connections

- **Broader:** one of the structured analytic techniques, grouped by the *Primer* as diagnostic, and a form of debiasing.[^s1]
- **Applied in** intelligence analysis, where it is used at the start and end of analytic projects.[^s1]
- **Counteracts** confirmation bias in Heuer's sense: it forces analysts to re-examine premises instead of fitting new information to an existing mind-set.[^s2]
- **Influenced by** MacEachin's linchpin analysis, which first required key assumptions to be spelled out.[^s2]
- **Supported by** the 2016 RAND pilot review, weakly and qualitatively.[^s3]
- **Challenged by** Mandel and Tetlock's 2018 critique of untested judgment correctives.[^s4]
- **Related to** analysis of competing hypotheses and devil's advocacy, which the *Primer* lists beside it as ways of challenging mind-sets, and to the premortem and consider-the-opposite, which likewise make the case against a current view explicit.[^s1]

## Sources

[^s1]: US Government (2009). *A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis*. CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf (accessed 2026-11-05)
[^s2]: Heuer, R. J., Jr. (1999). *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (accessed 2026-11-05)
[^s3]: Artner, S., Girven, R. S. & Bruce, J. B. (2016). *Assessing the Value of Structured Analytic Techniques in the U.S. Intelligence Community*. RAND RR-1408-OSD. https://apps.dtic.mil/sti/tr/pdf/AD1024447.pdf (accessed 2026-11-05)
[^s4]: Mandel, D. R. & Tetlock, P. E. (2018). "Correcting Judgment Correctives in National Security Intelligence." *Frontiers in Psychology* 9, 2640. https://frontiersin.org/article/10.3389/fpsyg.2018.02640/full (accessed 2026-11-05)
