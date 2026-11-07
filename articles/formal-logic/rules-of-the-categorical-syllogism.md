---
id: ct:rules-of-the-categorical-syllogism
type: Technique
title: Rules of the categorical syllogism
aliases: [syllogistic rules, rules for valid syllogisms, rule method for testing syllogisms]
domain: formal-logic
summary: >-
  A checklist test for categorical syllogisms: a standard-form syllogism is
  valid exactly when it satisfies a short set of rules about distribution,
  negative premises and quantity, and each broken rule names the formal
  fallacy committed, from the undistributed middle to the existential fallacy.
level: intermediate
evidenceStatus: normative
broader: [ct:categorical-syllogism]
related: [ct:venn-diagram-test, ct:syllogism, ct:port-royal-logic, ct:illicit-minor, ct:validity, ct:method-of-counterexample]
requires: [ct:categorical-syllogism, ct:distribution-of-terms, ct:validity]
relations:
  - {predicate: detects, object: ct:existential-fallacy, source: s5, confidence: high}
  - {predicate: detects, object: ct:undistributed-middle, source: s3, confidence: high}
  - {predicate: detects, object: ct:illicit-major, source: s3, confidence: high}
  - {predicate: explainedBy, object: ct:distribution-of-terms, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:venn-diagram-test, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Distributive Terms, Truth, and the Port Royal Logic"
    publisher: "History and Philosophy of Logic (John N. Martin, 2012), author's copy, University of Cincinnati"
    url: https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s2
    title: "Medieval Theories of the Syllogism"
    publisher: "Stanford Encyclopedia of Philosophy (Lagerlund, rev. 2026)"
    url: https://plato.stanford.edu/ENTRIES/medieval-syllogism/
    type: scholarly-encyclopedia
    accessed: 2026-11-07
  - id: s3
    title: "Rules for categorical syllogisms (lecture notes 6.5)"
    publisher: "PHIL 240 Introduction to Logic, Texas A&M University"
    url: https://phil240.tamu.edu/LectureNotes/6.5.pdf
    type: academic
    accessed: 2026-11-07
  - id: s4
    title: "Categorical Syllogism, Venn Diagrams and Rules for Testing for Validity"
    publisher: "Critical thinking course notes, Florida International University faculty pages"
    url: https://faculty.fiu.edu/~harrisk/Notes/Critical%20Thinking/Categorical%20Syllogisms%20and%20Rules.htm
    type: academic
    accessed: 2026-11-07
  - id: s5
    title: "Rules and Fallacies"
    publisher: "Philosophy Pages"
    url: https://mail.philosophypages.com/lg/e08b.htm
    type: community
    accessed: 2026-11-07
created: 2026-11-07
---

# Rules of the categorical syllogism

The rules of the categorical syllogism are a short checklist that decides whether a standard-form syllogism is valid without drawing anything. Each rule states a necessary condition for validity, and together they are sufficient: a syllogism that breaks none of them is valid, and one that breaks any of them is not.[^s1][^s5] Because each rule matches a named formal fallacy, the checklist also tells you what went wrong, not just that something did.[^s3][^s5]

## Origin

The rules grew out of medieval work on distribution. Medieval logicians taught that a universal proposition distributes its subject and a negative proposition distributes its predicate, and later supposition theory gave that a semantic account.[^s1][^s2] In the fourteenth century John Buridan used distribution to test moods: he required the middle term to be distributed and rejected every combination of two negative premises; Abelard had earlier given nine rules for the figures.[^s2] The best-known compact list comes from the Port-Royal *Logic*, which gave six rules and argued that a mood is valid if and only if it breaks none of them. John Martin's 2012 study traces several of those rules to ancient and medieval sources and the two distribution rules to sixteenth-century texts, and calls the list an early form of a decision procedure for the moods.[^s1]

Modern textbooks keep the same idea with one change. Traditional logic assumed every term names something that exists; modern logic drops that assumption, so it adds a rule that two universal premises cannot yield a particular conclusion.[^s3][^s5]

## How it works

A common modern version has six rules, each paired with a fallacy:[^s3][^s5]

1. Exactly three terms, each used in one sense (four terms, or equivocation).[^s3][^s5]
2. The middle term is distributed in at least one premise (undistributed middle).[^s3][^s5]
3. A term distributed in the conclusion is distributed in its premise (illicit major or illicit minor).[^s3][^s5]
4. At least one premise is affirmative (exclusive premises).[^s3][^s5]
5. A negative premise requires a negative conclusion, and a negative conclusion requires a negative premise.[^s3][^s5]
6. Two universal premises cannot give a particular conclusion (existential fallacy).[^s3][^s5]

Take a workplace case. "All approved vendors have passed a security review. All vendors on the new shortlist have passed a security review. So all vendors on the new shortlist are approved vendors." The middle term, "vendors who passed a security review", sits in the predicate of two universal affirmatives, so it is never distributed. Rule 2 fails and the argument commits the undistributed middle; shortlisted vendors may have passed review without being approved.[^s3][^s5] Now take "All vendors added to next year's shortlist must pass a security review. All vendors who pass a security review will be audited. So some vendors on next year's shortlist will be audited." Rules 1 to 5 pass, but rule 6 flags it: if no vendor is ever added, both premises are true and the conclusion is false.[^s4][^s5]

## How to apply it

- Put the argument in standard form: major premise, minor premise, conclusion, each an A, E, I or O proposition.[^s4]
- Name the major, minor and middle terms, and confirm each keeps one meaning.[^s3][^s4]
- Mark the distributed terms: subjects of universals (A, E) and predicates of negatives (E, O).[^s2][^s4]
- Run the rules in order. Failing any of the distribution or negation rules makes the argument invalid.[^s4]
- If the argument passes everything except the quantity rule, it is valid only on the assumption that the relevant class has members. The FIU notes call this conditional validity and list the moods it covers; state the existence premise or weaken the conclusion.[^s4]

Pitfalls: the rules only work on standard-form categorical syllogisms, so ordinary sentences must be translated first, and a mistranslation produces a wrong verdict. A pass shows validity only; the premises still need checking for truth.[^s3][^s4]

## Evidence and limitations

As a normative test the rules are well grounded. Martin's reconstruction argues that the six Port-Royal rules decide validity for the moods and for finite categorical arguments generally, though he warns against crediting the seventeenth-century authors with the modern idea of an effective procedure.[^s1] The Philosophy Pages summary notes that out of 256 possible forms only 15 survive the rules on the modern reading.[^s5] The rule lists differ between textbooks: some split the negation rule in two or add "no conclusion from two particular premises," which follows from the others.[^s4][^s5] And the existence rule depends on the logical standpoint: on the traditional reading it is not needed.[^s3]

## Connections

- **Detects the existential fallacy.** The quantity rule is the one that catches a particular conclusion drawn from universal premises.[^s5][^s4]
- **Detects the undistributed middle and illicit major.** These are the violations of the middle-term and conclusion-distribution rules.[^s3]
- **Explained by distribution of terms.** Most of the rules are stated in terms of which terms are distributed, the doctrine Martin traces from medieval logic to Port-Royal.[^s1][^s2]
- **Contrasts with the Venn diagram test.** Both decide the same question; diagrams show the class relations, while the rules give a verbal checklist that names the error.[^s4]

## Sources

[^s1]: Martin, "Distributive Terms, Truth, and the Port Royal Logic", *History and Philosophy of Logic*, 2012. https://homepages.uc.edu/~martinj/Papers/Distributive%20Terms,%20Truth%20and%20The%20Port%20Royal%20Logic%20-%20HPL%20(web%20version).pdf (accessed 2026-11-07)
[^s2]: Lagerlund, "Medieval Theories of the Syllogism", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/ENTRIES/medieval-syllogism/ (accessed 2026-11-07)
[^s3]: "Rules for categorical syllogisms", PHIL 240 lecture notes 6.5, Texas A&M University. https://phil240.tamu.edu/LectureNotes/6.5.pdf (accessed 2026-11-07)
[^s4]: "Categorical Syllogism, Venn Diagrams and Rules for Testing for Validity", Florida International University faculty notes. https://faculty.fiu.edu/~harrisk/Notes/Critical%20Thinking/Categorical%20Syllogisms%20and%20Rules.htm (accessed 2026-11-07)
[^s5]: "Rules and Fallacies", *Philosophy Pages*. https://mail.philosophypages.com/lg/e08b.htm (accessed 2026-11-07)
