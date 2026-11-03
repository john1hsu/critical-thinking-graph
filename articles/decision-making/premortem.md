---
id: ct:premortem
type: Technique
title: Premortem
aliases: [pre-mortem, project premortem, premortem analysis, pre-mortem analysis]
domain: decision-making
summary: >-
  A plan-evaluation technique in which a team, before committing to a plan,
  imagines that it has already been carried out and has failed, then has each
  member independently write down the reasons it failed so those risks can be
  addressed in advance.
level: introductory
evidenceStatus: mixed
broader: [ct:structured-analytic-techniques, ct:debiasing]
related: [ct:consider-the-opposite, ct:devils-advocacy, ct:hindsight-bias]
requires: []
relations:
  - {predicate: introducedBy, object: ct:gary-klein, source: s1, confidence: high}
  - {predicate: explainedBy, object: ct:prospective-hindsight, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:overconfidence-effect, source: s3, confidence: medium}
  - {predicate: counteracts, object: ct:groupthink, source: s1, confidence: medium}
  - {predicate: demonstratedBy, object: ct:gallop-bischoff-2016-premortem-risk-study, source: s3, confidence: medium}
  - {predicate: contrastsWith, object: ct:worst-case-scenario-analysis, source: s2, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Pre-empting project failure by using a premortem technique"
    publisher: British Journal of Hospital Medicine 78(10), 584-585 (Mills & McKimm, 2017), Swansea University Cronfa repository
    url: https://cronfa.swan.ac.uk/Record/cronfa37562/Download/0037562-10012018105306.pdf
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s2
    title: "Improving Planning: Quantitative Evaluation of the Premortem Technique in Field and Laboratory Settings"
    publisher: Michigan Technological University, MS thesis (Peabody, 2017; advisor E. Veinott)
    url: https://digitalcommons.mtu.edu/etdr/374
    type: academic
    accessed: 2026-11-03
  - id: s3
    title: "The premortem"
    publisher: Jason Collins, Course notes on behavioural economics and corporate decision making, ch. 30
    url: https://corporate.jcx.au/premortem
    type: academic
    accessed: 2026-11-03
  - id: s4
    title: "Strategic decisions: When can you trust your gut?"
    publisher: McKinsey Quarterly (interview of Daniel Kahneman and Gary Klein by Sibony & Lovallo, March 2010)
    url: https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/strategic-decisions-when-can-you-trust-your-gut
    type: news
    accessed: 2026-11-03
  - id: s5
    title: "Premortem debiasing and self-serving attributions (conference poster)"
    publisher: Gandhi, Duke & Schweitzer (2021), SJDM poster archive hosted by the UBC Sauder Decision Lab
    url: https://dlab.sauder.ubc.ca/sjdm/presentations/2021-Poster-Gandhi-Linnea-debiasing-premortem-selfserving~.pdf
    type: preprint
    accessed: 2026-11-03
created: 2026-11-03
---

# Premortem

A premortem is a structured way to stress-test a plan before anyone is committed to it. Instead of asking "what might go wrong?", the facilitator tells the group to assume the project has already been carried out and has failed badly, and asks each person to explain why.[^s1] It is the mirror image of a postmortem: the failure analysis is done while the plan can still be changed.[^s4]

## Origin

The technique was devised by the applied psychologist Gary Klein, who popularised it in a short 2007 *Harvard Business Review* piece on project premortems.[^s1] Klein grounded it in a 1989 study by Deborah Mitchell, J. Edward Russo and Nancy Pennington in the *Journal of Behavioral Decision Making*, which found that people asked to imagine an event had already happened, rather than that it might happen, generated roughly 30% more reasons for the outcome.[^s3] Daniel Kahneman later endorsed the method in a 2010 joint interview with Klein, calling it cheap to run and likely to pay off.[^s4]

## How it works

The premortem works on two levels. Cognitively, it swaps an uncertain question ("could this fail?") for a certain one ("it failed; why?"), a shift called prospective hindsight that makes failure stories easier to construct.[^s3] Socially, it changes what earns credit in the room: people are rewarded for spotting problems others missed rather than for defending the plan, and doubters can voice concerns without openly challenging the leader.[^s4] Proponents present it as a guard against groupthink and overconfidence and as a safe channel for dissent.[^s1]

*Workplace example.* A product team is about to launch a new self-service billing portal next quarter. The project lead says: "It is six months from now and the launch was a disaster. Take three minutes and write down every reason why." Working alone, one engineer writes that the data migration corrupted legacy invoices; a support lead writes that call volumes tripled because the help pages were not ready; finance notes that a regulatory sign-off was never scheduled. None of these had been raised in the planning meetings. The team adds a migration dry run, a support readiness milestone and a compliance review to the plan, without abandoning the launch itself.[^s4]

## How to apply it

1. **Brief the plan.** Make sure everyone understands the plan being evaluated.[^s1]
2. **Declare the failure.** State that the plan has been executed and has failed, so participants reason from a certain outcome rather than a possibility.[^s4]
3. **Write independently.** Give each person a few minutes to list reasons for the failure on their own before any discussion, which protects minority views from being swamped.[^s1]
4. **Collate.** Go round the group collecting one reason at a time until the list is exhausted; tools such as SWOT or a risk register can help organise it.[^s1]
5. **Act.** Revise the plan to remove or mitigate the most serious threats, and keep the list to review as the project unfolds.[^s1]

**When to use it:** just before a significant commitment, when a group has converged on a plan and enthusiasm is high. Kahneman expected it to kill plans only rarely; its usual product is a set of improvements to a plan that still goes ahead.[^s4] **Pitfalls:** time can be spent on risks that never materialise,[^s1] and failure stories may drift toward blaming external luck rather than the team's own choices (see Evidence).[^s5]

## Evidence

The evidence base is small, mostly from lab tasks and student samples, so the technique is rated *mixed* here. In a 2010 ISCRAM conference study by Veinott, Klein and Wiggins, 178 students evaluating a pandemic lockdown plan lowered their confidence about twice as much after a premortem as after listing pros and cons or cons alone.[^s3] A 2016 controlled study by Gallop and Bischoff with 101 experienced programme managers and engineers found that premortem teams identified more high-quality risks, including "black swan" risks missed in the real historical case, than brainstorming teams.[^s3] A 2017 Michigan Tech thesis found that Army cadet teams using the premortem made fewer errors and showed less fixation than teams using a standard military evaluation, without extra planning time; against a worst-case-scenario method, results were mixed, with the premortem producing more failure reasons only for a complex, unfamiliar plan.[^s2]

The most important caveat comes from three pre-registered online studies plus a pilot (about 2,300 participants in total) presented by Gandhi, Duke and Schweitzer in 2021: the premortem reduced overconfidence, but it also increased self-serving attributions, with people blaming imagined failures on luck or circumstances outside their control, and it did not make them more willing to act to improve their results.[^s5] Note also that the 1989 prospective-hindsight study counted reasons rather than judging their quality, so claims that the premortem improves people's ability to identify the *right* risks go beyond that original evidence.[^s3]

## Connections

- **Introduced by** Gary Klein, whose 2007 *Harvard Business Review* article set out the procedure.[^s1]
- **Explained by** prospective hindsight, the finding that imagining an outcome as already certain makes reasons for it easier to generate.[^s3]
- **Counteracts** the overconfidence effect: the premortem reliably lowered confidence in plans in controlled comparisons.[^s3]
- **Counteracts** groupthink by giving dissenters a protected, expected way to raise doubts.[^s1]
- **Demonstrated by** Gallop and Bischoff's 2016 study of risk identification by experienced engineers.[^s3]
- **Contrasts with** worst-case-scenario analysis, which steers people toward different categories of failure reasons.[^s2]
- **Related to** consider-the-opposite and devil's advocacy, which likewise make the case against a current view explicit, and to hindsight bias, the after-the-fact certainty that the premortem borrows deliberately before the fact.[^s3]

## Sources

[^s1]: Mills, J. & McKimm, J. (2017). "Pre-empting project failure by using a premortem technique." *British Journal of Hospital Medicine* 78(10), 584-585. https://cronfa.swan.ac.uk/Record/cronfa37562/Download/0037562-10012018105306.pdf (accessed 2026-11-03)
[^s2]: Peabody, M. (2017). *Improving Planning: Quantitative Evaluation of the Premortem Technique in Field and Laboratory Settings*. MS thesis, Michigan Technological University. https://digitalcommons.mtu.edu/etdr/374 (accessed 2026-11-03)
[^s3]: Collins, J. "The premortem." *Course notes on behavioural economics and corporate decision making*, ch. 30. https://corporate.jcx.au/premortem (accessed 2026-11-03)
[^s4]: Sibony, O. & Lovallo, D. (2010). "Strategic decisions: When can you trust your gut?" Interview with Daniel Kahneman and Gary Klein. *McKinsey Quarterly*. https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/strategic-decisions-when-can-you-trust-your-gut (accessed 2026-11-03)
[^s5]: Gandhi, L., Duke, A. & Schweitzer, M. (2021). Poster on premortem debiasing and self-serving attributions, SJDM poster archive. https://dlab.sauder.ubc.ca/sjdm/presentations/2021-Poster-Gandhi-Linnea-debiasing-premortem-selfserving~.pdf (accessed 2026-11-03)
