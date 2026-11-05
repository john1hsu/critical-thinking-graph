---
id: ct:hypothesis-testing
type: Method
title: Hypothesis testing
aliases: [hypothetico-deductive method, hypothetico-deductivism, H-D method, testing hypotheses]
domain: scientific-reasoning
summary: >-
  The method of evaluating a conjecture by deducing observable consequences
  ("test implications") from it, together with auxiliary assumptions, and
  then checking whether they occur: a failed prediction counts against the
  hypothesis, a successful one lends it support without proving it.
level: introductory
evidenceStatus: normative
broader: [ct:scientific-method]
related: [ct:falsifiability, ct:affirming-the-consequent, ct:ad-hoc-hypothesis, ct:null-hypothesis-significance-testing, ct:positive-test-strategy, ct:christiaan-huygens]
requires: [ct:modus-tollens, ct:deductive-reasoning]
relations:
  - {predicate: partOf, object: ct:scientific-method, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:philosophy-of-science, source: s1, confidence: high}
  - {predicate: influencedBy, object: ct:william-whewell, source: s2, confidence: medium}
  - {predicate: challengedBy, object: ct:duhem-quine-thesis, source: s1, confidence: high}
  - {predicate: contrastsWith, object: ct:inference-to-the-best-explanation, source: s2, confidence: medium}
  - {predicate: counteracts, object: ct:confirmation-bias, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Confirmation"
    publisher: Stanford Encyclopedia of Philosophy (Crupi, rev. 2025)
    url: https://plato.stanford.edu/entries/confirmation/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s2
    title: "Scientific Method"
    publisher: Stanford Encyclopedia of Philosophy (Andersen, rev. 2026)
    url: https://plato.stanford.edu/entries/scientific-method/
    type: scholarly-encyclopedia
    accessed: 2026-11-04
  - id: s3
    title: "Confirmation, disconfirmation, and information in hypothesis testing"
    publisher: Psychological Review 94(2), 211-228 (Klayman & Ha, 1987)
    url: https://pages.ucsd.edu/~mckenzie/KlaymanHaPsychReview1987.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s4
    title: "On the failure to eliminate hypotheses in a conceptual task"
    publisher: Quarterly Journal of Experimental Psychology 12(3), 129-140 (Wason, 1960)
    url: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/wason-qjep1960.pdf
    type: primary
    accessed: 2026-11-04
created: 2026-11-04
---

# Hypothesis testing

Hypothesis testing, in its classic hypothetico-deductive (H-D) form, evaluates a conjecture by working out what should be observable if it were true and then looking. Evidence confirms a hypothesis, relative to some auxiliary assumptions, when the hypothesis and the auxiliaries together entail that evidence but the auxiliaries alone do not; it disconfirms the hypothesis when they entail the opposite of what is observed.[^s1] Philosophers sometimes describe this as "deduction in reverse": the logic runs forward from hypothesis to prediction, while the support runs backward from observation to hypothesis.[^s1] This article covers the general reasoning method; the statistical procedure of null-hypothesis significance testing is a related but separate topic.

## Origin

The idea that science proceeds by framing hypotheses and deducing their consequences was championed in the nineteenth century by William Whewell, against John Stuart Mill's more inductivist picture, and was developed further in the twentieth century by Jean Nicod and others.[^s2] Carl Hempel's *Philosophy of Natural Science* (1966) made it a textbook standard, using Ignaz Semmelweis's investigation of childbed fever to show how candidate explanations are rejected when their test implications fail and supported, though never proven, when those implications hold.[^s2] Hempel added that the strength of that support depends on the quantity, variety and precision of the confirming evidence.[^s2] Karl Popper's falsificationism shares the H-D structure of deriving observable consequences but puts the weight on refutation, since no run of successes can establish a theory's truth.[^s2]

## How it works

The method has an asymmetry built into its logic. When a prediction fails, the inference to "something is wrong" has the valid form of modus tollens. When a prediction succeeds, concluding that the hypothesis is therefore true would commit the fallacy of affirming the consequent, which is why a passed test counts only as support.[^s2] Strong tests are ones where the predicted outcome would be unlikely if the hypothesis were false.

**Workplace example.** An operations team suspects that a spike in late deliveries is caused by a new routing algorithm. A test implication follows: if the algorithm is the cause, depots still on the old algorithm should show no comparable spike, and late deliveries at switched depots should fall if routing is reverted for a week. If unswitched depots spiked just as much, the hypothesis is in trouble, assuming the auxiliaries hold (similar weather, staffing and order volumes). If only switched depots spiked and the rollback fixed it, the hypothesis gains support, but a rival such as a coincident driver-shift change has not yet been ruled out, so the test supports the hypothesis only relative to those background assumptions.[^s1]

## How to apply it

1. State the hypothesis precisely enough that it forbids some outcomes.[^s1]
2. Derive concrete test implications, and list the auxiliary assumptions each one depends on.[^s1]
3. Prefer tests whose outcome you expect could come out *against* you. In Wason's 2-4-6 task, participants told that 2, 4, 6 fits a hidden rule mostly proposed triples that fit their own guess; only 6 of 29 announced the correct rule ("any increasing sequence") on their first attempt, and successful participants generated more instances that their own hypothesis said should fail.[^s4]
4. Do not assume negative tests are always better. Klayman and Ha showed that testing cases where you expect the property to occur is often a sound heuristic, and fails mainly when your hypothesis is narrower than the truth, as in the 2-4-6 task; the useful question is which test could reveal you are wrong.[^s3]
5. When a test fails, check the auxiliaries honestly, but distrust rescues that only save the hypothesis without making new predictions.[^s2]
6. Treat a passed test as one piece of support and look for varied, independent tests before acting with confidence.[^s2]

## Evidence and limitations

As a normative method, hypothesis testing is judged by philosophical analysis, and its simple form has known problems. Because predictions always depend on auxiliaries, a suitable choice of auxiliary assumptions can make almost any evidence confirm almost any hypothesis, which is the Duhemian challenge; scientists did not, for example, count the successes of particle theorists in optics as confirming their view.[^s1] Naive H-D also implies that evidence confirming a hypothesis confirms that hypothesis conjoined with any irrelevant claim (the "tacking" problem), and it cannot tell "all ravens are black" apart from gerrymandered rivals.[^s1] Refinements that require novel predictions, eliminate rival hypotheses, or favour simpler or more explanatory hypotheses each address some of these problems but face their own difficulties.[^s1] Some philosophers propose inference to the best explanation as an alternative account, and others note that much experimentation is exploratory rather than a test of a prior hypothesis.[^s2]

On the psychological side, Wason's 1960 study showed that untrained reasoners often seek only confirming instances,[^s4] while Klayman and Ha argued that much of what is labelled confirmation bias reflects a general positive test strategy that works well under many realistic conditions.[^s3]

## Connections

Hypothesis testing is a **part of the scientific method** and was advanced by **William Whewell** against inductivist rivals; it is often **contrasted with inference to the best explanation**.[^s2] It is **studied in the philosophy of science** under the heading of confirmation theory and is **challenged by the Duhem-Quine thesis**, since auxiliary assumptions can always absorb a failed prediction.[^s1] It **requires modus tollens and deductive reasoning**, and it explains why a passed test does not prove a hypothesis: concluding otherwise would be **affirming the consequent**.[^s2] It closely relates to **falsifiability**, Popper's refutation-first version of the same structure.[^s2] Deliberately seeking tests that could fail **counteracts confirmation bias**, as Wason's 2-4-6 results suggest,[^s4] though Klayman and Ha's analysis of the **positive test strategy** shows that confirming-style tests are not always the culprit.[^s3]

## Sources

[^s1]: Crupi, V., "Confirmation", Stanford Encyclopedia of Philosophy (rev. 2025). https://plato.stanford.edu/entries/confirmation/ (accessed 2026-11-04)
[^s2]: Andersen, H., "Scientific Method", Stanford Encyclopedia of Philosophy (rev. 2026). https://plato.stanford.edu/entries/scientific-method/ (accessed 2026-11-04)
[^s3]: Klayman, J., & Ha, Y.-W. (1987). "Confirmation, disconfirmation, and information in hypothesis testing", Psychological Review 94(2), 211-228. https://pages.ucsd.edu/~mckenzie/KlaymanHaPsychReview1987.pdf (accessed 2026-11-04)
[^s4]: Wason, P. C. (1960). "On the failure to eliminate hypotheses in a conceptual task", Quarterly Journal of Experimental Psychology 12(3), 129-140. https://bear.warrington.ufl.edu/brenner/mar7588/Papers/wason-qjep1960.pdf (accessed 2026-11-04)
