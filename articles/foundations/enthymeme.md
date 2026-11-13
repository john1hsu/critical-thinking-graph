---
id: ct:enthymeme
type: Concept
title: Enthymeme
aliases: [incomplete argument, argument with a missing premise, rhetorical syllogism]
domain: foundations
summary: >-
  An argument in which a premise, or sometimes the conclusion, is left unstated
  because the audience is expected to supply it; finding and fairly filling that
  gap is a core step in reconstructing and evaluating everyday arguments.
level: introductory
evidenceStatus: normative
broader: [ct:argument]
related: [ct:principle-of-charity, ct:argument-mapping, ct:straw-man-fallacy, ct:syllogism, ct:categorical-syllogism, ct:undistributed-middle, ct:douglas-walton, ct:validity]
requires: [ct:argument, ct:validity]
relations:
  - {predicate: introducedBy, object: ct:aristotle, source: s5, confidence: high}
  - {predicate: introducedIn, object: ct:aristotles-rhetoric, source: s5, confidence: high}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: high}
  - {predicate: formalizedBy, object: ct:argumentation-schemes, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Supplement to Aristotle's Rhetoric: Enthymeme and Inference"
    publisher: Stanford Encyclopedia of Philosophy (Christof Rapp, 2022)
    url: https://plato.stanford.edu/ENTRIES/aristotle-rhetoric/enthymeme-inference.html
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "Supplement to Aristotle's Rhetoric: Brevity and the Enthymeme"
    publisher: Stanford Encyclopedia of Philosophy (Christof Rapp, 2022)
    url: https://plato.stanford.edu/ENTRIES/aristotle-rhetoric/brevity-enthymeme.html
    type: scholarly-encyclopedia
    accessed: 2026-11-13
  - id: s3
    title: "Argumentation schemes and enthymemes"
    publisher: Douglas Walton and Chris Reed, Synthese 145(3), 339-370 (2005), University of Dundee research portal
    url: https://discovery.dundee.ac.uk/en/publications/argumentation-schemes-and-enthymemes/
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Schemes and Enthymemes, ch. 6 of Argumentation Schemes"
    publisher: Douglas Walton, Chris Reed and Fabrizio Macagno, Cambridge University Press (2008)
    url: https://www.cambridge.org/core/books/argumentation-schemes/schemes-and-enthymemes/8C7B59E1AEB52B8578CA57A4364C651E
    type: textbook
    accessed: 2026-11-13
  - id: s5
    title: "Rhetoric, Book I (trans. W. Rhys Roberts)"
    publisher: Aristotle, The Internet Classics Archive (MIT)
    url: https://classics.mit.edu/Aristotle/rhetoric.1.i.html
    type: primary
    accessed: 2026-11-13
  - id: s6
    title: "Are 'Gap-Fillers' Missing Premisses?"
    publisher: Wayne Grennan, Informal Logic 16(3), 185-196 (1994)
    url: https://distantreader.org/stacks/journals/il/il-2456.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s7
    title: "Enthymemes"
    publisher: Lee C. Archie, Philosophy Department, Lander University
    url: https://philosophy.lander.edu/logic/enthy.html
    type: academic
    accessed: 2026-11-13
created: 2026-11-13
---

# Enthymeme

An enthymeme is an argument with a gap: one of its premises, or occasionally its conclusion, is not stated, because the speaker expects the listener to fill it in.[^s7] Most real arguments are like this. "Don't hire him, he's been late to every interview" leaves unsaid the bridge claim that habitual lateness predicts poor performance. Because the unstated part is often where the weakest assumption hides, spotting enthymemes and supplying their missing pieces fairly is one of the first skills of argument analysis.[^s3][^s4]

## Origin

The term comes from Aristotle's *Rhetoric*. He calls the enthymeme a rhetorical syllogism, the orator's counterpart to a deduction in logic, just as the example is the orator's counterpart to induction.[^s5] In Book I, chapter 2 he notes that enthymemes are built from fewer propositions than a full syllogism and that a premise everyone already knows need not be said: to argue that Dorieus won a crown, it is enough to say he won at Olympia, since the audience knows the Olympic prize is a crown.[^s5]

Scholars disagree about what Aristotle meant. Christof Rapp's Stanford Encyclopedia supplement records a debate over whether the enthymeme is a genuine deduction or only a deduction in a loose sense: Myles Burnyeat read Aristotle's phrase "a sort of syllogism" as signalling a relaxed form of inference, while Rapp defends the traditional view that enthymemes can be real deductions whose conclusions hold "for the most part".[^s1] Rapp also argues that Aristotle's advice about brevity, to avoid remote premises and not spell out every step, does not by itself make the enthymeme logically incomplete; the familiar reading of it as a "truncated syllogism" with a suppressed premise is the later textbook sense that critical-thinking courses now use.[^s2][^s7]

## How it works

Traditional logic texts classify enthymemes by what is missing. In a first-order enthymeme the major (general) premise is omitted; in a second-order one the minor (particular) premise is omitted; in a third-order one the conclusion itself is left for the audience to draw.[^s7] A worked workplace example:

- Stated: "The vendor missed the last three delivery dates, so we shouldn't renew their contract."[^s7]
- Missing premise candidates: (a) "Any vendor who misses three deadlines should not be renewed"; (b) "A vendor whose recent record shows repeated missed deadlines is likely to keep missing them, and reliability matters most for this contract."[^s6]

Candidate (a) makes the argument deductively valid but is a sweeping rule the speaker may not hold. Candidate (b) is closer to what a manager plausibly means and turns the argument into a defeasible prediction that can be weighed against, say, a new account manager or a price advantage.[^s3][^s6] The choice changes how the argument should be judged: the same words can look valid but unsound, or reasonable but rebuttable.[^s6][^s7]

## How to apply it

1. **Name the conclusion and the stated reasons**, then ask what extra claim would be needed to get from one to the other.[^s7]
2. **Supply the weakest premise that closes the gap.** Logic texts advise against adding an assumption stronger than necessary, because an inflated premise turns the reconstruction into a straw man.[^s7] Wayne Grennan likewise argues that the narrowest, most defensible generalization is the charitable choice, and that a deductive "gap-filler" can attribute to the arguer a universal claim they would reject.[^s6]
3. **Stay faithful to the text and context.** Walton, Reed and Macagno stress that different readers can supply different missing premises, so the reconstruction should be anchored in what the speaker plausibly meant.[^s4]
4. **Use argumentation schemes as a guide.** If the stated material matches a known scheme, such as argument from expert opinion or from sign, the scheme's template shows which premise is missing; Walton and Reed found that some real enthymemes are best completed deductively and others with defeasible schemes.[^s3][^s4]
5. **Then evaluate.** A reconstruction can be valid yet unsound because the supplied premise is false or doubtful; making it explicit is what exposes that.[^s7]

## Limitations

Reconstruction is interpretation, so there is rarely one correct missing premise.[^s4] Grennan questions whether the general "major premise" is really part of the argument at all, suggesting it is better treated as backing for the arguer's implicit claim that the reasons support the conclusion; on that view, insisting on a premise that makes every argument formally valid sets the bar too high and misdescribes arguments that are valid by meaning or by fact.[^s6] Charity applied mechanically to weak arguments can also backfire, producing a version the arguer never offered.[^s3]

## Connections

An enthymeme is a kind of argument whose assessment depends on validity once the missing part is restored.[^s7] It was introduced by Aristotle in the *Rhetoric* as the rhetorical counterpart of the syllogism; classic textbook examples are categorical syllogisms with one line dropped, and filling the gap can reveal an undistributed middle.[^s5][^s7] Modern argumentation theory, notably Douglas Walton with Chris Reed, uses argumentation schemes to model how missing premises should be supplied.[^s3][^s4] Fair completion is governed by the principle of charity, over-completion risks a straw man, and argument mapping makes the supplied premise visible on the map.[^s4][^s6][^s7]

## Sources

[^s1]: Christof Rapp, "Supplement to Aristotle's Rhetoric: Enthymeme and Inference", Stanford Encyclopedia of Philosophy (2022). https://plato.stanford.edu/ENTRIES/aristotle-rhetoric/enthymeme-inference.html (accessed 2026-11-13)
[^s2]: Christof Rapp, "Supplement to Aristotle's Rhetoric: Brevity and the Enthymeme", Stanford Encyclopedia of Philosophy (2022). https://plato.stanford.edu/ENTRIES/aristotle-rhetoric/brevity-enthymeme.html (accessed 2026-11-13)
[^s3]: Douglas Walton and Chris Reed, "Argumentation schemes and enthymemes", Synthese 145(3), 339-370 (2005), doi:10.1007/s11229-005-6198-x. https://discovery.dundee.ac.uk/en/publications/argumentation-schemes-and-enthymemes/ (accessed 2026-11-13)
[^s4]: Douglas Walton, Chris Reed and Fabrizio Macagno, "Schemes and Enthymemes", ch. 6 of *Argumentation Schemes*, Cambridge University Press (2008). https://www.cambridge.org/core/books/argumentation-schemes/schemes-and-enthymemes/8C7B59E1AEB52B8578CA57A4364C651E (accessed 2026-11-13)
[^s5]: Aristotle, *Rhetoric* Book I, trans. W. Rhys Roberts, The Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/rhetoric.1.i.html (accessed 2026-11-13)
[^s6]: Wayne Grennan, "Are 'Gap-Fillers' Missing Premisses?", Informal Logic 16(3), 185-196 (1994). https://distantreader.org/stacks/journals/il/il-2456.pdf (accessed 2026-11-13)
[^s7]: Lee C. Archie, "Enthymemes", Philosophy Department, Lander University. https://philosophy.lander.edu/logic/enthy.html (accessed 2026-11-13)
