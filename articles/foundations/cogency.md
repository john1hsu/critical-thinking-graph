---
id: ct:cogency
type: Concept
title: Cogency
aliases: [cogent argument, uncogent argument]
domain: foundations
summary: >-
  The property of a non-deductive argument that is inductively strong and whose
  premises are all actually true; in informal logic, more broadly, an argument
  whose premises are acceptable, relevant and sufficient for its conclusion.
level: introductory
evidenceStatus: normative
broader: [ct:inductive-reasoning]
related: [ct:soundness, ct:validity, ct:argument, ct:informal-logic, ct:informal-fallacy]
requires: [ct:argument, ct:inductive-reasoning]
relations:
  - {predicate: partOf, object: ct:argument-evaluation, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:informal-logic, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:bayesian-reasoning, source: s3, confidence: medium}
  - {predicate: introducedIn, object: ct:logical-self-defense, source: s3, confidence: medium}
argumentMap:
  premises: ["The supplier delivered on time in each of the past twenty quarters.", "Nothing about the supplier's operations has changed."]
  conclusion: "The supplier will probably deliver on time next quarter."
  verdict: strong
  objections: ["A strong track record does not rule out a one-off disruption next quarter."]
sameAs: []
sources:
  - id: s1
    title: "5.2: Cogency and Strong Arguments, in Critical Reasoning and Writing"
    publisher: Noah Levin (Golden West College), Humanities LibreTexts
    url: https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/05%3A_Inductive_Arguments/5.02%3A_Cogency_and_Strong_Arguments
    type: textbook
    accessed: 2026-11-08
  - id: s2
    title: "Introduction: soundness and cogency, in How to Think Critically"
    publisher: CAUL OER Collective (Council of Australian University Librarians)
    url: https://oercollective.caul.edu.au/howtothinkcritically/?p=103
    type: textbook
    accessed: 2026-11-08
  - id: s3
    title: "A probabilistic analysis of argument cogency (author's copy)"
    publisher: David Godden and Frank Zenker, Synthese 195(4), 2018, doi 10.1007/s11229-016-1299-2, via PhilArchive
    url: https://philarchive.org/archive/GODAPA-5
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Logically Defending for Publication: An Analysis of the Review Process of Logical Self-Defense (ISSA Proceedings 2010)"
    publisher: Takuzo Konishi, Rozenberg Quarterly
    url: https://rozenbergquarterly.com/?p=7190
    type: academic
    accessed: 2026-11-08
created: 2026-11-08
---

# Cogency

Cogency is the standard a good non-deductive argument meets. In the textbook sense, an argument is *strong* when its premises, if true, would make the conclusion very likely, and *cogent* when it is strong and all of its premises are in fact true.[^s1] Cogency is to inductive and other non-deductive arguments what soundness is to deductive ones: a sound argument is valid with true premises, a cogent argument is strong with true premises.[^s2] An argument that is weak, or that rests on even one false premise, is uncogent.[^s1]

## Origin

The strong/cogent pairing is the standard vocabulary of introductory logic textbooks, which use it to give inductive arguments an evaluative term parallel to "valid" and "sound".[^s1][^s2] Informal logic gave the word a broader meaning. In *Logical Self-Defense* (1977), Ralph Johnson and J. Anthony Blair proposed three criteria for a good argument: its premises must be acceptable, relevant to the conclusion, and jointly sufficient to support it, now known as the RSA criteria.[^s3] Johnson and Blair wrote the book partly because they found existing fallacy-based textbooks unclear about what makes an argument fail, and the RSA triad went on to shape both informal-logic teaching and theory.[^s4] In that tradition cogency, meaning well-reasoned in the broad sense, replaces soundness as the general standard of a good argument.[^s3]

## How it works

A procurement analyst argues: "Over the past twenty quarters this supplier delivered on time every quarter, and nothing about its operations has changed; so next quarter's delivery will probably be on time" (see the argument map). The premises, if true, make the conclusion likely, so the argument is strong; if they are also true, it is cogent.[^s1] It becomes uncogent in two different ways. If the record covered only two quarters, the inference would be weak even with true premises; if the supplier had in fact missed three deadlines, the argument would rest on a false premise even though its form is strong.[^s1]

Because cogency only makes a conclusion probable, a cogent argument can still have a false conclusion: the supplier might be late anyway. That outcome does not retroactively make the argument uncogent, but evaluators should still check whether they have independent reason to doubt the conclusion.[^s2]

## How to apply it

1. Ask the strength question first: assuming every premise is true, how likely would the conclusion be?[^s1]
2. Then ask the truth question: are the premises actually true, or at least acceptable given what you know?[^s2][^s3]
3. In the informal-logic version, check each RSA condition separately: is each reason acceptable, is it relevant to this claim, and do the reasons together give enough support?[^s3]
4. Finally, look for outside evidence against the conclusion before acting on it.[^s2]

## Evidence and limitations

The RSA criteria are usually treated as individually necessary and jointly sufficient for cogency, but informal logicians have revised the list: Johnson later added premise truth, and Vorobej replaced acceptability with truth.[^s3] In a 2018 *Synthese* paper, Godden and Zenker gave the criteria a Bayesian analysis and argued that cogency depends on how much the reason changes one's commitment, how sensitive and selective the reason is for the claim, one's prior commitment to the claim, and context-dependent acceptability thresholds.[^s3] On their analysis the three criteria are not fully independent of one another, which challenges how they are often taught.[^s3]

## Connections

- **Broader: inductive reasoning.** Cogency is the success standard for inductive arguments, whose premises aim to make conclusions probable.[^s1]
- **Related: soundness and validity.** Strength and cogency mirror validity and soundness for non-deductive arguments.[^s2]
- **Part of argument evaluation.** Judging cogency combines an assessment of inferential strength with an assessment of premise truth.[^s2]
- **Applied in informal logic.** The RSA criteria make cogency the field's general standard of a good argument.[^s3]
- **Formalized by Bayesian reasoning.** Godden and Zenker restate acceptability, relevance and sufficiency in probabilistic terms.[^s3]
- **Introduced in *Logical Self-Defense*.** Johnson and Blair's 1977 textbook introduced the RSA account of cogency.[^s3][^s4]
- **Related: informal fallacies.** The RSA criteria can also be used to classify fallacies without relying on the deduction-induction distinction.[^s4]

## Sources

[^s1]: Noah Levin, "5.2: Cogency and Strong Arguments", *Critical Reasoning and Writing*, Humanities LibreTexts. https://human.libretexts.org/Bookshelves/Philosophy/Logic_and_Reasoning/Critical_Reasoning_and_Writing_(Levin_et_al.)/05%3A_Inductive_Arguments/5.02%3A_Cogency_and_Strong_Arguments (accessed 2026-11-08)
[^s2]: "Introduction: soundness and cogency", *How to Think Critically*, CAUL OER Collective. https://oercollective.caul.edu.au/howtothinkcritically/?p=103 (accessed 2026-11-08)
[^s3]: David Godden and Frank Zenker, "A probabilistic analysis of argument cogency", *Synthese* 195(4), 2018, author's copy on PhilArchive. https://philarchive.org/archive/GODAPA-5 (accessed 2026-11-08)
[^s4]: Takuzo Konishi, "Logically Defending for Publication: An Analysis of the Review Process of *Logical Self-Defense*", ISSA Proceedings 2010, Rozenberg Quarterly. https://rozenbergquarterly.com/?p=7190 (accessed 2026-11-08)
