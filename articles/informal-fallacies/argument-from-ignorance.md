---
id: ct:argument-from-ignorance
type: InformalFallacy
title: Argument from ignorance
aliases: [appeal to ignorance, argumentum ad ignorantiam, ad ignorantiam]
domain: informal-fallacies
summary: >-
  The fallacy of concluding that a claim is false because it has not been
  proven true, or true because it has not been proven false, treating a lack of
  evidence as if it were evidence for the opposite.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:burden-of-proof, ct:presumption, ct:argumentation-schemes, ct:douglas-walton, ct:pragma-dialectics, ct:bayesian-reasoning, ct:ad-hominem]
requires: [ct:burden-of-proof]
relations:
  - {predicate: introducedBy, object: ct:john-locke, source: s1, confidence: medium}
  - {predicate: explainedBy, object: ct:burden-of-proof, source: s4, confidence: high}
  - {predicate: formalizedBy, object: ct:bayesian-reasoning, source: s2, confidence: high}
  - {predicate: contrastsWith, object: ct:presumption, source: s5, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s5, confidence: high}
criticalQuestions:
  - How thoroughly has anyone actually looked for evidence on this question?
  - If the claim were true, how likely is it that the search would have turned up evidence of it?
  - Who carries the burden of proof here, and is the arguer quietly shifting it to the other side?
  - Is "not yet known either way" an available position that the argument skips over?
  - Is the conclusion a practical precaution (act as if) or a claim about what is actually true?
argumentMap:
  premises:
    - "A colleague proposes moving the team's shared files to a new cloud storage tool."
    - "Nobody has shown that the new tool causes any problems."
  conclusion: "So the new tool is safe to adopt for all client files."
  verdict: fallacious
  objections:
    - "No one has tested it yet; a check that was never run cannot come back negative."
    - "The person proposing the change carries the burden of showing it is safe, not the sceptics of showing it is unsafe."
    - "A security review that looked for problems and found none would make the same conclusion reasonable."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, rev. 2024)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "A Normative Theory of Argument Strength"
    publisher: Informal Logic 26(1), 1-24 (Hahn & Oaksford, 2006)
    url: https://distantreader.org/stacks/journals/il/il-428.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "How Convinced Should We Be by Negative Evidence?"
    publisher: Proceedings of the Annual Meeting of the Cognitive Science Society 27 (Hahn, Oaksford & Bayindir, 2005)
    url: https://repositories.cdlib.org/content/qt9p43b3xm/qt9p43b3xm.pdf?t=op2n2e
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Conceptualizing Fallacies: The Informal Logic and Pragma-Dialectic Approaches to the Argumentum ad Ignorantiam"
    publisher: ISSA Proceedings 2002 (Wagemans), Rozenberg Quarterly
    url: https://rozenbergquarterly.com/issa-proceedings-2002-conceptualizing-fallacies-the-informal-logic-and-pragma-dialectic-approaches-to-the-argumentum-ad-ignorantiam/?print=pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Presumptions, and How They Relate to Arguments from Ignorance"
    publisher: Argumentation 33(4), 579-604 (Bodlović, 2019)
    url: https://link.springer.com/article/10.1007/s10503-019-09498-8
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s6
    title: "A Bayesian approach to the argument from ignorance"
    publisher: Canadian Journal of Experimental Psychology 58(2), 75-85 (Oaksford & Hahn, 2004), Birkbeck repository record
    url: https://eprints.bbk.ac.uk/16121/
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Argument from ignorance

The argument from ignorance moves from "it has not been shown that P" to "so not-P", or from "it has not been shown that not-P" to "so P". In its textbook form it is a fallacy because a lack of proof on one side is treated as proof of the other, skipping the honest middle position that the question is still open.[^s5] Not every inference from missing evidence is bad, though: when someone has searched well and evidence would very probably have turned up, its absence can be a good reason to doubt a claim.[^s2]

## Origin

John Locke named the *argumentum ad ignorantiam* in *An Essay Concerning Human Understanding* (1690, Book IV, chapter 17), as one of three "ad" arguments people use to win assent, alongside *ad verecundiam* and *ad hominem*.[^s1] Locke's version was dialectical: the speaker demands that the opponent accept the offered proof or produce a better one, and Locke held that failing to produce a better one does not oblige anyone to accept the first.[^s1] Locke did not call it a fallacy; later logic textbooks did, and the modern sense became inferring a proposition's truth from the absence of evidence against it; Copi's 1961 *Introduction to Logic* listed it among the fallacies of relevance.[^s1]

## How it works

The fallacy works by turning a gap in knowledge into a finding. In the workplace example above, a colleague argues that a new cloud storage tool is safe for client files because nobody has shown it causes problems. If no one has looked, the silence is uninformative, and the person proposing the change is the one who owes the evidence.[^s4] Compare a security team that tested the tool carefully and found nothing: here a hidden premise, "if there were a serious flaw, this review would very likely have found it," turns the inference into something close to modus ponens, which Walton treats as the mark of a reasonable argument from ignorance.[^s4]

Two broad families of non-fallacious cases are usually distinguished. Epistemic cases infer that something is probably absent after a thorough search, such as concluding water is uncontaminated after experts tested it and found nothing.[^s5] Practical cases justify acting with caution when the stakes are high, such as treating a gun as loaded when there is no evidence it is unloaded.[^s5] The practical conclusion is "act as if", not "it is so".

## How to spot it

Look for a conclusion that rests only on what nobody has proven, with no description of who looked or how hard.[^s4] Watch for burden shifting, in which the person making a claim demands that sceptics disprove it.[^s4] Ask whether the arguer has ruled out "we don't yet know" without saying why; pragma-dialectical theorists call this absolutizing the failure of a defence.[^s4]

## How to counter it

Name the missing search: ask what investigation was done and how sensitive it was.[^s2] Return the burden of proof to the person who made the claim, and offer suspended judgment as a legitimate outcome rather than accepting either verdict.[^s4] If a decision cannot wait, separate the practical question (what precaution is sensible given the stakes) from the factual one (what is actually true).[^s5]

## Evidence

Bayesian accounts treat the argument's strength as a matter of degree rather than form. On this view, how much a negative result counts depends on the test's sensitivity and selectivity and on prior belief; the "ghosts exist because no one has disproved them" case is weak because of its content, not its structure.[^s2] Oaksford and Hahn reported an experiment in which people's ratings of such arguments tracked these factors.[^s6] In a 2005 follow-up with 73 and 72 Cardiff participants, the same lab reproduced its earlier three findings: positive evidence was rated somewhat more convincing than negative evidence, reliable sources far more than unreliable ones, and stronger prior belief slightly more.[^s3] A second experiment found that even the classic "not disproved, so true" structure was rated fairly convincing when the search domain was nearly closed, such as a library catalogue.[^s3] These are small, mostly student samples from one research group, so the findings support the normative argument more than they settle how people reason in general.[^s3]

## Connections

The fallacy is best explained through the **burden of proof**: both Walton's informal logic and pragma-dialectics treat it as mishandling who must defend a claim.[^s4] Its graded strength has been **formalized in Bayesian reasoning** by Hahn and Oaksford.[^s2] It **contrasts with presumption**: Bodlović argues that, despite Walton's view of the argument as presumptive reasoning, it is a negative inference with different defeaters and obligations.[^s5] It is a standing topic in **argumentation theory**,[^s5] and the term was **introduced by John Locke**, who also named the related **ad hominem**.[^s1]

## Sources

[^s1]: Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (rev. 2024). https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-13)
[^s2]: Hahn & Oaksford, "A Normative Theory of Argument Strength", Informal Logic 26(1), 2006. https://distantreader.org/stacks/journals/il/il-428.pdf (accessed 2026-11-13)
[^s3]: Hahn, Oaksford & Bayindir, "How Convinced Should We Be by Negative Evidence?", Proceedings of the Cognitive Science Society 27, 2005. https://repositories.cdlib.org/content/qt9p43b3xm/qt9p43b3xm.pdf?t=op2n2e (accessed 2026-11-13)
[^s4]: Wagemans, "Conceptualizing Fallacies: The Informal Logic and Pragma-Dialectic Approaches to the Argumentum ad Ignorantiam", ISSA Proceedings 2002. https://rozenbergquarterly.com/issa-proceedings-2002-conceptualizing-fallacies-the-informal-logic-and-pragma-dialectic-approaches-to-the-argumentum-ad-ignorantiam/?print=pdf (accessed 2026-11-13)
[^s5]: Bodlović, "Presumptions, and How They Relate to Arguments from Ignorance", Argumentation 33(4), 2019. https://link.springer.com/article/10.1007/s10503-019-09498-8 (accessed 2026-11-13)
[^s6]: Oaksford & Hahn, "A Bayesian approach to the argument from ignorance", Canadian Journal of Experimental Psychology 58(2), 2004. https://eprints.bbk.ac.uk/16121/ (accessed 2026-11-13)
