---
id: ct:argumentation-schemes
type: Framework
title: Argumentation schemes
aliases: [argument schemes, argumentation scheme theory, Walton's argumentation schemes, presumptive argument schemes]
domain: argumentation
summary: >-
  A framework from informal logic that catalogues the recurring patterns of
  everyday, defeasible argument (from expert opinion, analogy, consequences and
  so on) and pairs each with critical questions that test whether a particular
  instance holds.
level: intermediate
evidenceStatus: normative
broader: [ct:argumentation-theory]
related: [ct:informal-logic, ct:toulmin-model, ct:pragma-dialectics, ct:informal-fallacy, ct:argument-mapping, ct:defeasible-reasoning, ct:argument-from-expert-opinion, ct:argument-from-analogy, ct:argument-from-consequences, ct:burden-of-proof]
requires: [ct:argument]
relations:
  - {predicate: influencedBy, object: ct:topics, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:the-new-rhetoric, source: s1, confidence: medium}
  - {predicate: introducedBy, object: ct:douglas-walton, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s1, confidence: high}
  - {predicate: appliedIn, object: ct:artificial-intelligence, source: s2, confidence: high}
  - {predicate: supportedBy, object: ct:nussbaum-2018-critical-questions-study, source: s5, confidence: medium}
  - {predicate: challengedBy, object: ct:lumer-2022-epistemological-appraisal-of-schemes, source: s4, confidence: high}
argumentMap:
  premises:
    - "Our security lead says the new vendor library contains a critical vulnerability."
    - "Our security lead is an expert in application security."
  conclusion: "The vendor library presumably contains a critical vulnerability, so we should not ship it yet."
  verdict: strong
  scheme: ct:argument-from-expert-opinion
  objections:
    - "If other security specialists who reviewed the library disagree, or the claim rests on an outdated version of the code, the presumption weakens and must be re-examined."
sameAs: []
sources:
  - id: s1
    title: "Argumentation Schemes: History, Classifications, and Computational Applications"
    publisher: "IfCoLog Journal of Logics and Their Applications 4(8) (Macagno, Walton & Reed, 2017), PhilArchive copy"
    url: https://philarchive.org/archive/MACASH-10
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s2
    title: "Argumentation Schemes, chapter 12: Schemes in Computer Systems"
    publisher: Cambridge University Press (Walton, Reed & Macagno, 2008)
    url: https://www.cambridge.org/core/books/abs/argumentation-schemes/schemes-in-computer-systems/D32DCDC5EDD13E149BBFE4AE56CD9E83
    type: primary
    accessed: 2026-11-05
  - id: s3
    title: "Review of Argumentation Schemes (Walton, Reed & Macagno)"
    publisher: Notre Dame Philosophical Reviews (Groarke, 2009)
    url: https://ndpr.nd.edu/reviews/argumentation-schemes/
    type: academic
    accessed: 2026-11-05
  - id: s4
    title: "An Epistemological Appraisal of Walton's Argument Schemes"
    publisher: "Informal Logic 42(1), 203-290 (Lumer, 2022), PhilArchive copy"
    url: https://philarchive.org/archive/LUMAEA
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s5
    title: "Using Critical Questions to Evaluate Written and Oral Arguments in an Undergraduate General Education Seminar"
    publisher: "Reading and Writing 32, 1531-1552 (Nussbaum, Dove, Slife & Kardash, 2018), UNLV repository record"
    url: https://oasis.library.unlv.edu/edpsych_fac_articles/320
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s6
    title: "A Classification System for Argumentation Schemes"
    publisher: "Argument and Computation 6(3), 219-245 (Walton & Macagno, 2015), PhilArchive copy"
    url: https://philarchive.org/archive/WALACS-7
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Argumentation schemes

Argumentation schemes are stereotyped patterns of everyday inference, such as arguing from what an expert says, from a similar case, or from the likely consequences of an action. Macagno, Walton and Reed describe them as combining a content relation (cause, authority, similarity) with a type of reasoning and a logical rule, and they stress that schemes are defeasible: they create a presumption in favour of the conclusion that new information can overturn.[^s1] Each scheme comes with a set of critical questions that probe its weak points, which makes the framework a practical checklist for evaluating ordinary arguments rather than a test of deductive validity.[^s1][^s6]

## Origin

The idea is old. Macagno, Walton and Reed trace schemes to the *topoi* of Aristotle's *Topics* and *Rhetoric*, general principles from which premises for dialectical and rhetorical arguments could be drawn; Cicero later reduced them to about twenty *loci*, and Boethius sorted them into intrinsic, extrinsic and intermediate groups.[^s1] By their account the topical tradition was largely eclipsed in the early modern period and revived in the twentieth century through Hastings (1963), Perelman and Olbrechts-Tyteca's *New Rhetoric*, Kienpointner (1992), Walton's mid-1990s book on presumptive reasoning, and Grennan (1997).[^s1] The standard modern reference is *Argumentation Schemes* by Douglas Walton, Chris Reed and Fabrizio Macagno (Cambridge University Press, 2008), which Groarke's review describes as a compendium of sixty-five schemes, each paired with critical questions.[^s2][^s3]

## How it works

A scheme names the premises and conclusion of a common argument type. In the worked example above, a team reasons from expert opinion: the security lead says a vendor library has a critical flaw, she is an expert in that field, so the flaw is presumably real. Walton and Macagno note that this scheme specifically requires the source to be an expert, which separates it from the broader argument from a position to know, where the source merely has access to the facts.[^s6] The conclusion is reasonable but not guaranteed, so the next step is to ask the scheme's critical questions.

Critical questions do several jobs. Macagno, Walton and Reed list four: challenging a premise, pointing to an exception, stating conditions for the scheme's proper use, and suggesting a counterargument.[^s1] They also differ in force: some defeat the argument as soon as they are asked, while others shift the burden of proof back to the arguer only when backed by evidence.[^s1] For the expert example, a reviewer would ask whether the source really is an expert in this specific domain, whether she is honest and reliable, and whether her claim fits what other experts say; Walton and Macagno argue that treating an expert as infallible is exactly what turns this ordinarily reasonable pattern into the fallacious appeal to authority.[^s6]

Because schemes are explicit templates, they are easy to formalise. Walton, Reed and Macagno devote a chapter to their use in software, from argument-diagramming tools such as Araucaria to automated reasoning and communication between software agents.[^s2] Macagno and colleagues add that schemes have been modelled as defeasible rules in AI-and-law systems such as Verheij's ArguMed and in structured frameworks such as ASPIC+, and are now used in argument mining.[^s1]

## How to apply it

1. Reconstruct the argument as premises and a conclusion, then identify which scheme it most resembles (expert opinion, analogy, cause to effect, consequences, practical reasoning).[^s1]
2. Check that each premise is true or well supported, then ask the scheme's critical questions in turn; an unanswered question signals where the presumption is weakest.[^s1][^s6]
3. Decide where the burden now sits: if a question is answered with evidence against the argument, the arguer must respond before the conclusion is accepted.[^s1]
4. When an argument fits several schemes, analyse it under each; Groarke points out that real arguments rarely match a single template exactly.[^s3]

## Evidence and limitations

As a standard of good reasoning, the framework is normative, but its teaching value has been tested. In a 2018 quasi-experimental study of three undergraduate seminar sections, students who used argument diagrams with a box of critical questions drawn from the argument-from-consequences scheme came to include more refutations tied to those questions than a comparison section; the gain carried over to an unprompted in-class essay but not to a later course paper.[^s5] This small, single-course result is suggestive rather than conclusive.

The theory itself is disputed. Groarke's review argues that the list of schemes is large but not comprehensive, that the criteria for what counts as a scheme are unclear, and that similar schemes can be hard to tell apart.[^s3] Classification is unsettled too: Macagno and colleagues find that existing typologies each mix criteria, and Walton and Macagno propose a provisional system that still needs empirical testing.[^s1][^s6] The most sustained critique, Lumer's 2022 appraisal in *Informal Logic*, argues that the schemes lack an epistemological theory explaining why they work, that by his count about three quarters of 104 schemes do not guarantee an acceptable conclusion, and that critical questions are useful heuristics for finding weaknesses but prove nothing on their own.[^s4]

## Connections

- **Broader: argumentation theory; studied in argumentation theory.** Schemes are one of the core analytic tools that argumentation theorists and informal logicians develop and debate.[^s1]
- **Influenced by the *Topics* and *The New Rhetoric*.** Aristotle's topoi are the acknowledged ancestors of modern schemes, and Perelman and Olbrechts-Tyteca's catalogue of argument types was part of their twentieth-century revival.[^s1]
- **Introduced by Douglas Walton.** Walton's presumptive-reasoning work and the 2008 compendium he co-wrote shaped the modern, critical-question-based version of the framework.[^s1]
- **Applied in artificial intelligence.** Schemes are used in argument-diagramming software, multi-agent communication, AI-and-law reasoning and argument mining.[^s2][^s1]
- **Supported by Nussbaum and colleagues (2018).** Teaching critical questions increased students' use of targeted refutations in discussion and writing.[^s5]
- **Challenged by Lumer (2022).** Lumer's epistemological appraisal questions whether the schemes are justified or effective as evaluation tools.[^s4]
- **Related.** Individual schemes such as argument from expert opinion, analogy and consequences are instances of the framework; informal fallacies are often analysed as misuses of schemes; the Toulmin model and argument mapping are neighbouring tools for laying out an argument's structure.[^s6][^s1]

## Sources

[^s1]: Macagno, Walton & Reed, "Argumentation Schemes: History, Classifications, and Computational Applications", IfCoLog Journal of Logics and Their Applications 4(8) (2017). https://philarchive.org/archive/MACASH-10 (accessed 2026-11-05)
[^s2]: Walton, Reed & Macagno, *Argumentation Schemes*, ch. 12 "Schemes in Computer Systems", Cambridge University Press (2008). https://www.cambridge.org/core/books/abs/argumentation-schemes/schemes-in-computer-systems/D32DCDC5EDD13E149BBFE4AE56CD9E83 (accessed 2026-11-05)
[^s3]: Groarke, review of *Argumentation Schemes*, Notre Dame Philosophical Reviews (2009). https://ndpr.nd.edu/reviews/argumentation-schemes/ (accessed 2026-11-05)
[^s4]: Lumer, "An Epistemological Appraisal of Walton's Argument Schemes", Informal Logic 42(1), 203-290 (2022). https://philarchive.org/archive/LUMAEA (accessed 2026-11-05)
[^s5]: Nussbaum, Dove, Slife & Kardash, "Using Critical Questions to Evaluate Written and Oral Arguments in an Undergraduate General Education Seminar", Reading and Writing 32, 1531-1552 (2018). https://oasis.library.unlv.edu/edpsych_fac_articles/320 (accessed 2026-11-05)
[^s6]: Walton & Macagno, "A Classification System for Argumentation Schemes", Argument and Computation 6(3), 219-245 (2015). https://philarchive.org/archive/WALACS-7 (accessed 2026-11-05)
