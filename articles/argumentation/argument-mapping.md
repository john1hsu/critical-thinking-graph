---
id: ct:argument-mapping
type: Technique
title: Argument mapping
aliases: [argument diagramming, argument visualization, computer-aided argument mapping, CAAM, box-and-arrow argument diagrams]
domain: argumentation
summary: >-
  A technique for laying out the inferential structure of an argument as a
  box-and-arrow diagram, with the main conclusion at the top and reasons,
  co-premises and objections beneath it, so the structure can be inspected
  and evaluated.
level: introductory
evidenceStatus: mixed
broader: [ct:argumentation-theory]
related: [ct:argument, ct:toulmin-model, ct:informal-logic, ct:argumentation-schemes, ct:principle-of-charity, ct:enthymeme, ct:begging-the-question, ct:structured-analytic-techniques, ct:monroe-beardsley]
requires: [ct:argument]
relations:
  - {predicate: detects, object: ct:begging-the-question, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:toulmin-model, source: s1, confidence: high}
  - {predicate: introducedBy, object: ct:richard-whately, source: s1, confidence: medium}
  - {predicate: appliedIn, object: ct:intelligence-analysis, source: s1, confidence: medium}
  - {predicate: supportedBy, object: ct:cullen-2018-argument-visualization-study, source: s3, confidence: high}
sources:
  - id: s1
    title: "Using Computer-Aided Argument Mapping to Teach Reasoning"
    publisher: Studies in Critical Thinking, ed. J. A. Blair, Windsor Studies in Argumentation (Davies, Barnett & van Gelder)
    url: https://ecampusontario.pressbooks.pub/criticalthinking1234/chapter/introduction/
    type: textbook
    accessed: 2026-11-07
  - id: s2
    title: "Argument Maps Improve Critical Thinking"
    publisher: Teaching Philosophy 27(2) (Twardy, 2004), author's revised draft
    url: https://philarchive.org/archive/TWAAMIv1
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s3
    title: "Improving analytical reasoning and argument understanding: a quasi-experimental field study of argument visualization"
    publisher: npj Science of Learning 3, 21 (Cullen, Fan, van der Brugge & Elga, 2018)
    url: https://cogtoolslab.github.io/pdf/cullen_npjsol_2018.pdf
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "The evaluation of argument mapping as a learning tool: Comparing the effects of map reading versus text reading on comprehension and recall of arguments"
    publisher: Thinking Skills and Creativity 5(1), 16-22 (Dwyer, Hogan & Stewart, 2010)
    url: https://research.universityofgalway.ie/en/publications/the-evaluation-of-argument-mapping-as-a-learning-tool-comparing-t/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s5
    title: "An evaluation of argument mapping as a method of enhancing critical thinking performance in e-learning environments"
    publisher: Metacognition and Learning 7(3), 219-244 (Dwyer, Hogan & Stewart, 2012)
    url: https://eprints.teachingandlearning.ie/id/eprint/4011/
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Argument mapping

Argument mapping is the practice of drawing an argument as a box-and-line diagram that shows how its claims bear on one another. The main conclusion (the contention) sits at the top; reasons that support it, objections that oppose it, and rebuttals of those objections branch beneath, each written as a complete declarative sentence without "because" or "therefore".[^s1] The point is not decoration but inspection: once the inferential structure is visible, a reader can ask of each link whether it really supports what it points to. Most current practice uses dedicated software, which draws the diagram but does not judge validity, so the evaluation remains the user's job.[^s1]

## Origin

Davies, Barnett and van Gelder trace the idea to the nineteenth-century logic teaching of Richard Whately, then to the legal evidence charts of John Henry Wigmore in the early 1900s, Monroe Beardsley's numbered-premise diagrams of 1950, and Stephen Toulmin's 1958 layout, which added warrants, backing and rebuttals.[^s1] Stephen Thomas later distinguished linked from convergent reasons and added objections, and Michael Scriven proposed a mapping procedure in 1976.[^s1][^s2] Pen-and-paper maps were tedious to revise, so the method stayed niche until software appeared; Tim van Gelder's Reason!Able, used in courses from about 2000, made it practical to teach a whole course through mapping.[^s2]

## How it works

A map separates two kinds of support. Co-premises are claims that work only together (remove one and the inference fails), and are drawn as a single linked reason; independent reasons each support the conclusion on their own. Unstated assumptions are added in brackets, using simple rules of thumb: every key term in the conclusion should appear in some premise, and every premise term should connect to the conclusion.[^s1]

Consider a workplace example. A team lead argues that a reporting dashboard is reliable "because the numbers match the finance export, and the finance export is right because it agrees with the dashboard." Drawn as a map, the arrow from the dashboard back to the finance export closes a loop: the conclusion appears as its own support. Davies and colleagues note that mapping exposes exactly this kind of circular, question-begging support, and also makes weak or irrelevant reasons easier to see.[^s1] Once the loop is drawn, the useful question is which independent check, such as a sample of source invoices, could break it.

## How to apply it

1. Write the contention as one full sentence at the top. 2. Ask "why should I believe this?" and add each reason as its own box. 3. For every reason, check whether it needs a partner premise to reach the conclusion, and add the hidden one. 4. Add the strongest objections and any replies. 5. Evaluate each link: is the premise acceptable, and does it support the claim above it?[^s1] Use mapping for contested decisions, document reviews and teaching analysis. Twardy reports that students often confused explanations with reasons and that any set of syntactic mapping rules can be gamed, so a tidy map is not proof of a good argument; Neil Thomason's maxim that walking in a circle gets you nowhere was added for that reason.[^s2]

## Evidence

The evidence is encouraging but not conclusive. A first-year course Twardy co-taught around mapping software gained about 0.72 standard deviations on the California Critical Thinking Skills Test against typical gains near 0.3, but with no control group and teacher, text and software confounded.[^s2] Davies and colleagues cite a 2015 meta-analysis by van Gelder in which intensive mapping courses gained around 0.8 SD, roughly twice standard courses, though many comparisons use external benchmarks.[^s1] In a 2018 Princeton field study, 105 seminar students gained d = 0.71 over 56 waitlisted controls on LSAT logical-reasoning items; assignment was not random, and the authors could not separate visualization from intensive feedback. They also note that studies using both tests found gains about three times smaller on the LSAT than on the CCTST.[^s3] In a 400-student experiment, reading a map instead of prose improved recall of an argument but not comprehension.[^s4] An eight-week e-learning course with mapping improved Halpern test scores relative to a no-instruction control, mainly overall and in argument analysis.[^s5] Hence `mixed`: real gains, with uncertainty about how much is due to mapping itself.

## Connections

Mapping **helps detect begging the question**, because a circular chain of support shows up as a loop in the diagram.[^s1] It is **influenced by the Toulmin model**, whose warrants and rebuttals shaped modern map conventions, and is traced back to **Richard Whately**, who is credited as its earliest exponent.[^s1] It has been **applied in intelligence analysis**, where pre- and post-test studies with analysts are reported.[^s1] Its strongest controlled evidence, the **Cullen et al. 2018 field study**, supports it while leaving its active ingredient open.[^s3] It builds on the concept of an **argument** and complements the **principle of charity** and **argumentation schemes**, which say what to put in the boxes and which questions to ask of each link.[^s1][^s2]

## Sources

[^s1]: Davies, Barnett & van Gelder, "Using Computer-Aided Argument Mapping to Teach Reasoning", in Studies in Critical Thinking, ed. J. A. Blair. https://ecampusontario.pressbooks.pub/criticalthinking1234/chapter/introduction/ (accessed 2026-11-07)
[^s2]: Twardy, "Argument Maps Improve Critical Thinking", Teaching Philosophy 27(2) (2004), author's draft. https://philarchive.org/archive/TWAAMIv1 (accessed 2026-11-07)
[^s3]: Cullen, Fan, van der Brugge & Elga, "Improving analytical reasoning and argument understanding: a quasi-experimental field study of argument visualization", npj Science of Learning 3, 21 (2018). https://cogtoolslab.github.io/pdf/cullen_npjsol_2018.pdf (accessed 2026-11-07)
[^s4]: Dwyer, Hogan & Stewart, "The evaluation of argument mapping as a learning tool", Thinking Skills and Creativity 5(1), 16-22 (2010). https://research.universityofgalway.ie/en/publications/the-evaluation-of-argument-mapping-as-a-learning-tool-comparing-t/ (accessed 2026-11-07)
[^s5]: Dwyer, Hogan & Stewart, "An evaluation of argument mapping as a method of enhancing critical thinking performance in e-learning environments", Metacognition and Learning 7(3), 219-244 (2012). https://eprints.teachingandlearning.ie/id/eprint/4011/ (accessed 2026-11-07)
