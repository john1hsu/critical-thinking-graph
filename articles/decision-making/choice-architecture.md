---
id: ct:choice-architecture
type: Technique
title: Choice architecture
aliases: [nudging, nudge interventions, choice environment design]
domain: decision-making
summary: >-
  The deliberate design of the setting in which people choose, such as
  defaults, the order and grouping of options, how options are described
  and what feedback is given, to steer decisions predictably without
  forbidding any option or materially changing incentives.
level: introductory
evidenceStatus: contested
broader: [ct:debiasing]
related: [ct:status-quo-bias, ct:framing-effect, ct:behavioral-economics, ct:bounded-rationality, ct:judgment-and-decision-making]
requires: [ct:cognitive-bias]
relations:
  - {predicate: introducedBy, object: ct:richard-thaler, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:cass-sunstein, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:public-policy, source: s1, confidence: high}
  - {predicate: exploits, object: ct:status-quo-bias, source: s4, confidence: medium}
  - {predicate: exploits, object: ct:framing-effect, source: s2, confidence: medium}
  - {predicate: supportedBy, object: ct:mertens-2022-nudging-meta-analysis, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:jachimowicz-2019-default-effects-meta-analysis, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:maier-2022-nudging-publication-bias-reanalysis, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Choice Architecture"
    publisher: "Thaler, Sunstein & Balz, chapter in E. Shafir (ed.), The Behavioral Foundations of Public Policy (2012), Harvard Law School bibliography record"
    url: https://hls.harvard.edu/bibliography/choice-architecture
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains"
    publisher: "PNAS 119(1), e2107346118 (Mertens, Herberz, Hahnel & Brosch, 2022), PubMed Central"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "No evidence for nudging after adjusting for publication bias"
    publisher: "PNAS 119(31), e2200300119 (Maier, Bartoš, Stanley, Shanks, Harris & Wagenmakers, 2022), PubMed Central"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "When and why defaults influence decisions: a meta-analysis of default effects"
    publisher: "Behavioural Public Policy 3(2), 159-186 (Jachimowicz, Duncan, Weber & Johnson, 2019), RePEc/IDEAS record"
    url: https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Choice architecture

**Choice architecture** is the design of the environment in which a decision is made. Every choice is presented somehow: one option is pre-selected, options appear in some order, outcomes are described in some words. Because those features shape what people pick, whoever arranges them is a "choice architect", whether they intend to be or not.[^s1] An intervention that uses this lever to steer behaviour while leaving every option open is usually called a **nudge**.[^s1][^s2]

## Origin

The term was popularised by the economist Richard Thaler and the legal scholar Cass Sunstein, who paired it with a policy stance they called *libertarian paternalism*: design choice settings so that people are guided toward options they themselves would judge better, without forcing any particular outcome.[^s1] In a chapter written with John Balz for Eldar Shafir's 2012 volume *The Behavioral Foundations of Public Policy*, they set out a toolkit: defaults, anticipating errors, making the mapping from options to outcomes clearer, giving feedback, structuring complex choices, and using incentives.[^s1]

## How it works

Choice architecture works by building on predictable features of judgment rather than on new information or new payoffs. Mertens and colleagues' 2022 meta-analysis sorts interventions into three families: **decision information** (changing how options are described, for example reframing or making consequences visible), **decision structure** (changing how options are arranged, such as defaults, ordering or effort), and **decision assistance** (helping people follow through, such as reminders and commitment devices).[^s2]

Defaults are the best-known structural tool. A 2019 meta-analysis by Jachimowicz, Duncan, Weber and Johnson found defaults worked better when people read the pre-set option as the designer's recommendation (endorsement) or as the status quo they already hold (endowment).[^s4]

A workplace example: a company wants staff to choose a sensible pension plan. Under an opt-in form, employees must find and tick the plan themselves; many never do. The choice architect instead pre-selects a diversified plan, lists the options in order of risk with plain-language descriptions of what each would pay at retirement, and sends a yearly statement showing progress. No plan is banned and no bonus is paid, yet the design pulls choices toward the pre-set plan because accepting it takes no effort and reads as the employer's advice.[^s1][^s4]

## How to apply it

1. **Notice that you are already a choice architect.** Any form, menu, meeting agenda or software setting has a default and an order; decide them on purpose.[^s1]
2. **Choose the default deliberately**, matching it to what most people would pick after reflection, and make opting out easy.[^s1][^s4]
3. **Clarify the mapping** from options to outcomes in units people care about, and give feedback after the choice.[^s1]
4. **Structure complex choices** by grouping or filtering options when the menu is large.[^s1]
5. **Test it.** Effects vary widely by setting, and some nudges backfire, so run a pilot or comparison rather than assuming the result.[^s2]

Pitfalls: a design that serves the architect rather than the chooser turns the same tools into manipulation; and a nudge that worked in one domain may not transfer to another.[^s2][^s4]

## Evidence

The effect of defaults is relatively well supported. The 2019 meta-analysis pooled 58 studies with 73,675 participants and found a sizeable average effect (d = 0.68), though some studies showed no effect and two showed the reverse; defaults did better in consumer choices than in environmental ones.[^s4]

The case for nudges in general is disputed. Mertens and colleagues (2022) pooled 455 effect sizes from 214 publications, over two million participants, and reported a small-to-medium average effect (d about 0.45), largest for food choices and smallest for finance, with structural interventions outperforming information and assistance.[^s2] They also found evidence of publication bias and said the true effect was probably smaller.[^s2] A reanalysis by Maier and colleagues the same year applied robust Bayesian meta-analysis and concluded that once publication bias is corrected, the average effect is close to zero; evidence against an effect was strongest for information, assistance and finance nudges, while results for structural nudges were inconclusive.[^s3] Both groups saw very large heterogeneity, so some specific nudges may work well even if the average does not.[^s2][^s3] Hence the status here is *contested*.

## Connections

Choice architecture is a form of **debiasing** that changes the environment rather than the person; it was introduced as a policy idea by **Richard Thaler** and **Cass Sunstein** and is applied chiefly in **public policy**.[^s1] Defaults lean on **status quo bias**, since people often read the pre-set option as what they already have.[^s4] Information nudges that reframe options draw on the **framing effect**.[^s2] The **Mertens 2022** and **Jachimowicz 2019** meta-analyses support its effectiveness, while the **Maier 2022** reanalysis challenges the general claim.[^s2][^s3][^s4]
## Sources

[^s1]: Thaler, Sunstein & Balz, "Choice Architecture", in Shafir (ed.), *The Behavioral Foundations of Public Policy* (2012), Harvard Law School bibliography record. https://hls.harvard.edu/bibliography/choice-architecture (accessed 2026-11-14)
[^s2]: Mertens, Herberz, Hahnel & Brosch, "The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains", *PNAS* 119(1) (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589 (accessed 2026-11-14)
[^s3]: Maier et al., "No evidence for nudging after adjusting for publication bias", *PNAS* 119(31) (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501 (accessed 2026-11-14)
[^s4]: Jachimowicz, Duncan, Weber & Johnson, "When and why defaults influence decisions: a meta-analysis of default effects", *Behavioural Public Policy* 3(2) (2019). https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html (accessed 2026-11-14)
