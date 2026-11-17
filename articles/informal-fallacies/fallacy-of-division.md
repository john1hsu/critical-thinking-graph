---
id: ct:fallacy-of-division
type: InformalFallacy
title: Fallacy of division
aliases: [division fallacy, whole-to-part fallacy, fallacy of division (whole to parts)]
domain: informal-fallacies
summary: >-
  The fallacy of inferring that each part or member of a whole or group has a
  property because the whole or group has it, when the property belongs to
  the whole only collectively and does not carry down to its parts.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy, ct:fallacy-of-ambiguity]
related: [ct:fallacy-of-composition, ct:distributive-collective-distinction, ct:equivocation, ct:fallacy-of-accident, ct:ecological-fallacy, ct:sophistical-refutations, ct:aristotle, ct:richard-whately, ct:hasty-generalization]
requires: [ct:argument, ct:informal-fallacy]
relations:
  - {predicate: confusedWith, object: ct:fallacy-of-composition, source: s1, confidence: high}
  - {predicate: instanceOf, object: ct:fallacy-of-ambiguity, source: s1, confidence: medium}
  - {predicate: introducedIn, object: ct:sophistical-refutations, source: s2, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: high}
criticalQuestions:
  - Is the property true of the group taken as a single unit (collectively), or of every member taken one at a time (distributively)?
  - Does the property arise from how the parts are combined or how many there are, so that no single part could have it on its own?
  - Is there direct evidence about the particular part or member, rather than only about the whole it belongs to?
  - Could the whole have the property because of some members only, while others contribute nothing to it or even work against it?
  - Is a key term, such as "balanced", "important" or "successful", being used in a different sense for the parts than for the whole?
argumentMap:
  premises:
    - "The regional sales division beat its annual revenue target by 12 percent."
    - "Each sales representative works in the regional sales division."
  conclusion: "Each sales representative in the division beat their individual revenue target."
  verdict: fallacious
  objections:
    - "The division total can exceed target because two or three large accounts closed, while several representatives still fell short."
    - "Beating a division target is a fact about summed revenue; it says nothing about how that sum was spread across people."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hansen, substantive revision 2024)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-17
  - id: s2
    title: "Composition and Division"
    publisher: "Christian Plantin, Dictionnaire de l'argumentation 2021, ICAR (CNRS / Université Lyon 2)"
    url: https://icar.cnrs.fr/dicoplantin/composition-and-division-e/
    type: academic
    accessed: 2026-11-17
  - id: s3
    title: "Collective Responsibility and the Fallacies of Composition and Division"
    publisher: "Trudy Govier, OSSA 4 Conference Archive (2001), University of Windsor, via CORE"
    url: https://core.ac.uk/download/72768211.pdf
    type: academic
    accessed: 2026-11-17
  - id: s4
    title: "Distributive Fallacy - Division"
    publisher: "Fallacies tutorial, Palomar College faculty pages"
    url: https://www.palomar.edu/users/bthompson/Division.html
    type: academic
    accessed: 2026-11-17
  - id: s5
    title: "Ecological Inference and the Ecological Fallacy"
    publisher: "David A. Freedman, Technical Report 549, Department of Statistics, UC Berkeley (1999); International Encyclopedia of the Social & Behavioral Sciences"
    url: https://www.stat.berkeley.edu/~census/549.pdf
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Fallacy of division

The fallacy of division is the error of concluding that a part or member has some property because the whole or group it belongs to has that property, when the property does not actually pass down.[^s1][^s4] Hansen's example reverses a familiar one: a research team may be excellent as a team, but it does not follow that every member is an excellent researcher, since some essential members may do supporting or administrative work.[^s1] It is the mirror image of the fallacy of composition, which runs from parts to whole, and the two are usually taught and confused as a pair.[^s1][^s2]

## Origin

Aristotle discussed "combination" and "division" in *On Sophistical Refutations* among the fallacies that depend on language. His division example is the number five: five is two and three, two is even and three is odd, so someone might infer that five is both even and odd.[^s1] Hansen cautions that Aristotle's versions concern meaning changes made by grouping or separating words, and so differ considerably from the modern part-whole fallacy.[^s1] Plantin's dictionary of argumentation adds that the *Rhetoric* (II, 24) treats division as a line of argument that one side may use and the other condemn, with the example of splitting an act into separately defensible steps to block judgment of the whole.[^s2]

Later logicians kept the pair. The Port-Royal *Logic* retained it from Aristotle's list; Richard Whately called composition and division "semi-logical" fallacies, logical failures whose detection needs knowledge of the terms and subject matter; J. S. Mill grouped them with fallacies of confusion; and Irving Copi's textbook placed them among the fallacies of ambiguity alongside equivocation, amphiboly and accent, the classification most later textbooks follow.[^s1]

## How it works

The inference has the shape "the whole has F, so each part has F". Whether it goes wrong depends on the property. Palomar College's tutorial frames the error as a slide from a class taken collectively to its members taken distributively: cows are important to Wisconsin's economy, and Bossie is a cow, but Bossie alone is not important to that economy, because cows matter only in large numbers.[^s4] The same tutorial notes that some whole-to-part inferences are fine: if a car's comprehensive insurance covers the whole car, it covers each component.[^s4] The trouble comes with emergent properties, which the whole has because of how its parts interact or add up.[^s4]

The argument map above is a workplace version. "Beat its target" is true of the division's summed revenue, a collective fact; the conclusion turns it into a claim about each representative, which the premises cannot support, since the total can come from a few large deals.[^s1][^s4] Govier gives a case where a word shifts sense as well: a well-balanced choir has its vocal sections in proportion, which says nothing about whether any singer is a well-balanced person.[^s3]

A statistical cousin is the ecological fallacy, assuming that a relationship seen across groups holds for the individuals in them. Freedman recounts Robinson's 1950 finding that across US states in 1930 the share of foreign-born residents correlated at about 0.53 with literacy, while the individual-level correlation was about -0.11.[^s5] Like division, it moves from aggregate facts to claims about members, though its mechanism is confounding and aggregation rather than a shift in a word's sense.[^s5]

## How to spot it

- Look for a move from a claim about a team, company, country, class or system to a claim about one of its members or components.[^s1][^s3]
- Ask whether the property is collective or distributive. Govier argues the inference is fallacious when the attribution is fundamentally collective, when it is true of only some or most members, or when the term is equivocal; only on a fully universal distributive reading does it go through.[^s3]
- Check for emergent or sum-dependent properties such as size, total output, importance or performance, which can belong to the whole without belonging to any part.[^s4]
- Watch for terms that change meaning between levels, the feature that led Copi to class division as a fallacy of ambiguity.[^s1][^s3]

## How to counter it

Ask what makes the whole have the property and whether that reason applies to the part in question.[^s4] Ask for direct evidence about the member rather than inferring it from the group; Freedman notes that aggregate data can offer clues about individuals but support such conclusions only weakly.[^s5] In disputes about blame or credit, Govier's approach is to state explicitly which reading of a collective claim is intended, since collective responsibility does not automatically transfer to every individual.[^s3]

## Limitations

Not every whole-to-part argument is fallacious: properties that are true of every member by definition, or that hold of the whole only because they hold of each part, do transfer.[^s3][^s4] Plantin observes that the same division move can serve as a refutation for one side and a legitimate demonstration for the other, so the charge must be argued case by case.[^s2]

## Connections

- **Confused with** the fallacy of composition, its part-to-whole mirror image; the SEP and Plantin treat the two as a pair that differ only in direction.[^s1][^s2]
- **Instance of** the fallacies of ambiguity in Copi's classification, which the SEP reports most textbooks follow.[^s1]
- **Introduced in** Aristotle's *On Sophistical Refutations*, where division appears among the verbal fallacies, though in a form different from the modern one.[^s1][^s2]
- **Studied in** argumentation theory, where Govier's analysis of collective responsibility applies it to real disputes over blame and apology.[^s3]
- **Related** to the distributive-collective distinction, equivocation, the fallacy of accident and the ecological fallacy, which makes a parallel group-to-individual move with statistical data.[^s1][^s5]

## Sources

[^s1]: H. Hansen, "Fallacies", Stanford Encyclopedia of Philosophy, substantive revision 2024. https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-17)
[^s2]: C. Plantin, "Composition and Division", *Dictionnaire de l'argumentation 2021*, ICAR. https://icar.cnrs.fr/dicoplantin/composition-and-division-e/ (accessed 2026-11-17)
[^s3]: T. Govier, "Collective Responsibility and the Fallacies of Composition and Division", OSSA 4 Conference Archive, University of Windsor, 2001. https://core.ac.uk/download/72768211.pdf (accessed 2026-11-17)
[^s4]: "Distributive Fallacy - Division", fallacies tutorial, Palomar College faculty pages. https://www.palomar.edu/users/bthompson/Division.html (accessed 2026-11-17)
[^s5]: D. A. Freedman, "Ecological Inference and the Ecological Fallacy", Technical Report 549, Department of Statistics, UC Berkeley, 1999. https://www.stat.berkeley.edu/~census/549.pdf (accessed 2026-11-17)
