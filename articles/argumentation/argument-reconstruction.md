---
id: ct:argument-reconstruction
type: Technique
title: Argument reconstruction
aliases: [standardization, standardizing an argument, standardizing arguments, putting an argument in standard form, standard-form reconstruction, casting an argument, logical reconstruction of arguments]
domain: argumentation
summary: >-
  The technique of restating an argument found in ordinary text or talk as an
  explicit list of numbered premises and a conclusion: cutting noise,
  clarifying vague or ambiguous wording so each term keeps one sense,
  supplying unstated premises charitably, and checking that the result is
  faithful to the arguer, so the argument can then be evaluated.
level: introductory
evidenceStatus: normative
broader: [ct:informal-logic]
related: [ct:argument-mapping, ct:argument-evaluation, ct:enthymeme, ct:principle-of-charity, ct:precising-definition, ct:fallacy-of-four-terms, ct:argumentation-schemes, ct:straw-man-fallacy, ct:validity]
requires: [ct:argument]
relations:
  - {predicate: detects, object: ct:fallacy-of-ambiguity, source: s1, confidence: medium}
  - {predicate: detects, object: ct:equivocation, source: s3, confidence: medium}
  - {predicate: studiedIn, object: ct:informal-logic, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:argument-mapping, source: s1, confidence: medium}
  - {predicate: influencedBy, object: ct:principle-of-charity, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Informal Logic"
    publisher: Stanford Encyclopedia of Philosophy (Groarke, rev. 2021, Fall 2025 edition)
    url: https://plato.stanford.edu/archives/fall2025/entries/logic-informal/
    type: scholarly-encyclopedia
    accessed: 2026-11-16
  - id: s2
    title: "Chapter 3: Standard Form and Validity, in Critical Thinking, Logic, and Argument"
    publisher: AU Press, Athabasca University (open textbook)
    url: https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/28889b5a-c485-4292-aeea-48ff2b9c9674
    type: textbook
    accessed: 2026-11-16
  - id: s3
    title: "Chapter 14: Fallacies of Ambiguity, in Critical Thinking, Logic, and Argument"
    publisher: AU Press, Athabasca University (open textbook)
    url: https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/f8c8bad3-17e2-4cfd-b50b-6b6880d40052
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "Using Your Own Paraphrases of Premises and Conclusions to Reconstruct Arguments in Standard Form"
    publisher: Matthew Van Cleave, Introduction to Logic and Critical Thinking (LibreTexts open textbook, CC BY)
    url: https://human.libretexts.org/Courses/Lake_Tahoe_Community_College/PHI-104%3A_Critical_Thinking/01%3A_Reconstructing_and_Analyzing_Arguments/1.05%3A_Using_Your_Own_Paraphrases_of_Premises_and_Conclusions_to_Reconstruct_Arguments_in_Standard_Form
    type: textbook
    accessed: 2026-11-16
  - id: s5
    title: "Six Steps of Critical Thinking"
    publisher: Informal Logic 20(1), Teaching Supplement (Craig Walton, 2000)
    url: https://distantreader.org/stacks/journals/il/il-2260.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Chapter 3: Reconstruction, in How to Think Critically"
    publisher: Gibbons & Kingsbury, CAUL OER Collective (open textbook, 2024)
    url: https://oercollective.caul.edu.au/howtothinkcritically/?p=69
    type: textbook
    accessed: 2026-11-16
created: 2026-11-16
---

# Argument reconstruction

Argument reconstruction, often called *standardization*, is the step between reading an argument and judging it. Real arguments arrive buried in rhetoric, digressions and unstated assumptions, and their premises or conclusions are often unclear. Reconstruction cleans the argument up so it is as clear and straightforward as possible before anyone evaluates it.[^s6] Groarke's SEP entry describes standardizing as making an argument's premises, conclusion and inferences explicit. It involves discarding noise and repetition, restating rhetorical questions as claims, clarifying incomplete, vague or ambiguous statements, and recognizing unstated components.[^s1] The output is usually a numbered list of premises above a line, with the conclusion below.[^s2][^s4]

## Origin

Attention to unstated parts of arguments is ancient. Discussions of the enthymeme, a syllogism with a missing premise, are the earliest case the SEP entry notes, and it credits Whately (1826) and Wigmore (1913) with early diagramming of argument structure.[^s1] Standardization became a routine classroom procedure as informal logic grew into a field that studies real-life arguments.[^s1] Michael Scriven's textbook *Reasoning* (1976) taught argument analysis as a fixed sequence of steps. Craig Walton's 2000 teaching supplement in *Informal Logic* adapts Scriven's five-step procedure into six. It begins by clarifying meaning and paraphrasing, then numbers the essential claims, diagrams their structure and inserts missing premises in brackets.[^s5] Groarke's own BLAST framework for informal logic lists standardizing as its "S" step.[^s1]

## How it works

Reconstruction has four linked moves.[^s1][^s5]

1. **Find the conclusion and the reasons.** The conclusion is fixed by its logical role, not its position in the text. Indicator words such as "because" and "therefore" help, but people use them loosely.[^s2]
2. **Cut and paraphrase.** Drop material that does no work, merge repeated claims, and restate the rest in clear, complete sentences. There is never only one correct paraphrase, but some are better than others, and a good one keeps the argument's logic intact.[^s4] Walton's procedure lets the analyst reword only where the author's meaning and intent stay unchanged.[^s5]
3. **Fix the meaning of terms.** Where a word or sentence allows two readings, choose one and use it in every premise and in the conclusion. An argument works only when all parties use the same terms in the same way.[^s3]
4. **Supply what is missing, charitably.** Add unstated premises or conclusions the arguer plausibly relied on, marked as implicit. The principle of charity favours the most credible interpretation, often by attributing the *logical minimum*: the weakest unstated premise that links the stated reasons to the conclusion.[^s1] Charity has a limit. The analyst must not add new or better reasons the arguer never offered.[^s6]

A workplace example: a manager writes, "Remote staff are less visible, and promotions go to visible contributors. Draw your own conclusions." Reconstructed, the argument reads: (1) Remote staff are less visible to leadership. (2) Promotions go mainly to people visible to leadership. (C, implicit) Remote staff are less likely to be promoted. Step 3 then catches a problem. In premise 1, "visible" means physically seen in the office. In premise 2, it may mean having one's work noticed. If the two senses differ, the chain breaks. Written out with one sense throughout, the argument either loses a true premise or stops following.[^s1][^s3]

## How to apply it

- Number every premise and the conclusion so each can be questioned separately.[^s2][^s4]
- Put implicit premises in brackets so readers can see what you added and challenge it.[^s1][^s5]
- When a key term occurs twice, substitute one paraphrase in both places and reread. A syllogism whose middle term shifts sense shows four terms on paper, not three.[^s3]
- If the text allows more than one reasonable structure, record the alternatives rather than forcing one. Readers' reconstructions differ because the text leaves room for interpretation.[^s1][^s6]
- Then evaluate the reconstruction for premise acceptability and inferential support, not the original wording.[^s1]

## Limitations

Reconstruction is interpretation, so it can go wrong in two directions. Too little charity produces a straw man. Too much rebuilds a stronger argument than the arguer made.[^s6] The SEP entry adds that a plain list of premises does not show *how* they support the conclusion, for example whether premises are linked or independent. That is why it pairs standardized lists with key-component tables and diagrams.[^s1] Walton's course drops fallacy labels altogether, on the view that a careful reconstruction already exposes weak reasoning.[^s5] Its claims are normative guidance on method rather than findings tested in experiments.

## Connections

Argument reconstruction is a technique *studied in* *informal logic*.[^s1] It *detects* the *fallacy of ambiguity* because standardizing requires clarifying ambiguous claims before evaluation.[^s1] For the same reason it *detects* *equivocation*: fixing one sense per term exposes a shifted term, the *fallacy of four terms* in syllogistic form.[^s3] It *contrasts with* *argument mapping*: a standardized list states the components, and a map shows their inferential links.[^s1] It is *influenced by* the *principle of charity*, which guides how unstated premises are supplied.[^s1][^s5] *Precising definitions* are the usual tool for step 3, and *argumentation schemes* help find what an *enthymeme* leaves unsaid.

## Sources

[^s1]: Groarke, "Informal Logic", Stanford Encyclopedia of Philosophy (rev. 2021; Fall 2025 ed.). https://plato.stanford.edu/archives/fall2025/entries/logic-informal/ (accessed 2026-11-16)
[^s2]: "Standard Form and Validity", ch. 3 of *Critical Thinking, Logic, and Argument*, AU Press. https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/28889b5a-c485-4292-aeea-48ff2b9c9674 (accessed 2026-11-16)
[^s3]: "Fallacies of Ambiguity", ch. 14 of *Critical Thinking, Logic, and Argument*, AU Press. https://read.aupress.ca/read/24c4c0bd-f19f-4b14-8080-258a1e169ca6/section/f8c8bad3-17e2-4cfd-b50b-6b6880d40052 (accessed 2026-11-16)
[^s4]: Van Cleave, "Using Your Own Paraphrases of Premises and Conclusions to Reconstruct Arguments in Standard Form", *Introduction to Logic and Critical Thinking*, LibreTexts. https://human.libretexts.org/Courses/Lake_Tahoe_Community_College/PHI-104%3A_Critical_Thinking/01%3A_Reconstructing_and_Analyzing_Arguments/1.05%3A_Using_Your_Own_Paraphrases_of_Premises_and_Conclusions_to_Reconstruct_Arguments_in_Standard_Form (accessed 2026-11-16)
[^s5]: Craig Walton, "Six Steps of Critical Thinking", *Informal Logic* 20(1), Teaching Supplement (2000). https://distantreader.org/stacks/journals/il/il-2260.pdf (accessed 2026-11-16)
[^s6]: Gibbons & Kingsbury, "Reconstruction", ch. 3 of *How to Think Critically*, CAUL OER Collective (2024). https://oercollective.caul.edu.au/howtothinkcritically/?p=69 (accessed 2026-11-16)
