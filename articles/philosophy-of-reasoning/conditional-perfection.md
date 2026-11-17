---
id: ct:conditional-perfection
type: Phenomenon
title: Conditional perfection
aliases: [conditional strengthening, perfection of conditionals, biconditional reading of conditionals]
domain: philosophy-of-reasoning
summary: >-
  The tendency of listeners to hear a conditional "if P, then Q" as also
  conveying "if not P, then not Q", so that it is understood as the stronger
  "Q if and only if P". Described by Geis and Zwicky in 1971, it is treated as
  a defeasible pragmatic inference, not something the conditional logically
  entails.
level: intermediate
evidenceStatus: mixed
broader: [ct:conversational-implicature]
related: [ct:affirming-the-consequent, ct:denying-the-antecedent, ct:necessary-and-sufficient-conditions, ct:commutation-of-conditionals, ct:cancellability-test, ct:modus-ponens, ct:modus-tollens, ct:enthymeme]
requires: [ct:material-conditional]
relations:
  - {predicate: introducedBy, object: ct:arnold-zwicky, source: s2, confidence: high}
  - {predicate: explainedBy, object: ct:scalar-implicature, source: s2, confidence: medium}
  - {predicate: explainedBy, object: ct:exhaustification, source: s3, confidence: medium}
  - {predicate: contrastsWith, object: ct:material-conditional, source: s2, confidence: high}
  - {predicate: studiedIn, object: ct:pragmatics, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:psychology-of-reasoning, source: s4, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "Conditional Strengthening: A Case Study in Implicature"
    publisher: "Kai von Fintel, MIT (manuscript, September 2001), author's copy"
    url: https://web.mit.edu/fintel/fintel-2001-condstrength.pdf
    type: academic
    accessed: 2026-11-17
  - id: s2
    title: "Denying Antecedents and Affirming Consequents: The State of the Art"
    publisher: "Informal Logic 35(1), 88-134 (David Godden & Frank Zenker, 2015), Lund University Publications record"
    url: https://www.lunduniversity.lu.se/lup/publication/5eab0ec9-546b-4399-8129-5c043a272ee0
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Conditional inference and access to alternatives: The role of QUD and speaker knowledge in conditional perfection"
    publisher: "Journal of Semantics (Ebru Evcen, Alan Bale & David Barner), accepted manuscript, author's copy"
    url: https://ebruevcen.github.io/files/EvcenBaleBarner_inpress.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Semantics Processing of Conditional Connectives: German wenn 'if' Versus nur wenn 'only if'"
    publisher: "Journal of Psycholinguistic Research 50(6), 1337-1368 (Mingya Liu & Mathias Barthel, 2021), doi:10.1007/s10936-021-09812-0"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8660741
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Processing attenuating NPIs in indicative and counterfactual conditionals"
    publisher: "Frontiers in Psychology 13, 894396 (Juliane Schwab & Mingya Liu, 2022), doi:10.3389/fpsyg.2022.894396"
    url: https://www.frontiersin.org/articles/10.3389/fpsyg.2022.894396/pdf
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Conditional perfection

Conditional perfection is the everyday habit of hearing "if P, then Q" as if it also said "if not P, then not Q", which turns a one-way conditional into a two-way "Q if and only if P".[^s1][^s2] Logically, a conditional states only that P is sufficient for Q; it is silent about what happens when P is false. Listeners nonetheless often take it to name the only route to Q. Linguists and philosophers classify this as a pragmatic inference: it is drawn from the way something is said in context, and it can be withdrawn without contradiction.[^s1][^s2]

## Origin

The term comes from the linguists Michael Geis and Arnold Zwicky, who in a 1971 paper described a family of "invited inferences" and called this one the perfection of conditionals into biconditionals.[^s1][^s2] Their example was an offer of five dollars for mowing the lawn, which hearers take to mean no mowing, no five dollars.[^s1] Geis and Zwicky treated such inferences as justified unless the hearer has some reason to think otherwise, in the spirit of Grice's conversational implicatures.[^s2] Critics soon produced conditionals that invite no such reading, such as "if the manager quits, she will be replaced", which plainly does not suggest that she will be replaced only if she quits.[^s1]

## How it works

Suppose a team lead tells a contractor, "If you finish the data migration by Friday, you can bill the extra day." Almost everyone hears an implied "and if you don't finish by Friday, you can't." That reading is reasonable here, because the lead is answering an unspoken question about what the extra day depends on, and would have mentioned other ways to earn it if there were any.[^s1][^s3] Compare "If the build fails, the on-call engineer gets paged." No one infers that a passing build means nobody is ever paged, since other alerts obviously exist.

Two broad explanations compete. On the scalar account developed by Johan van der Auwera and Laurence Horn, a speaker who asserts one sufficient condition implicates, by the maxim of quantity, that stronger statements naming further sufficient conditions do not hold.[^s1][^s2] Kai von Fintel argued in 2001 that this delivers too much or too little, and proposed instead that perfection arises when the conditional answers a question asking for an exhaustive list of what brings Q about; when the conditional answers a different question, the inference lapses.[^s1] More recent work frames this as exhaustification: the conditional is read as giving the complete answer among the alternatives the context makes relevant.[^s3]

Perfection matters for critical thinking because it makes two formal fallacies look valid. If "if P then Q" is heard as "Q only if P", then denying the antecedent and affirming the consequent become enthymematic versions of modus tollens and modus ponens, with the converse conditional as the unstated premise.[^s2] Godden and Zenker's 2015 review accepts that reading where the conversation licenses the converse, but warns that perfection does not make these forms generally cogent: where context does not license it, the extra premise is simply unsupported.[^s2]

## How to spot and handle it

When a conclusion rests on "it didn't happen, so the result won't follow", ask whether the original conditional was meant as the only route to the result. Restating it with "only if" or "if and only if" and checking whether the speaker would accept that version usually settles the matter.[^s2] When you are the speaker, write "only if" or "if and only if" in policies, contracts and requirements when you mean them, and say "this is one way, not the only way" when you do not.[^s3] Because the inference is pragmatic, it can be cancelled explicitly ("if you finish by Friday you can bill the day, and you may also be able to bill it otherwise") without contradiction.[^s1][^s2]

## Evidence

Experiments show the inference is common but sensitive to context. In three preregistered online experiments, Evcen, Bale and Barner found perfected readings about 65% of the time when the conversation was about which conditions produce an outcome, against roughly 22% to 29% under other framings; perfection also dropped from about 72% to 21% when the speaker was known to lack full knowledge of the alternatives.[^s3] Liu and Barthel's 2021 studies of German "wenn" ("if") found that people endorse denying-the-antecedent inferences far less often than modus ponens, but reliably more than with an explicitly one-way connective, a residue they attribute to perfection; some of their effects shifted with the wording of the response options.[^s4] A 2022 rating study by Schwab and Liu with 59 analysed participants found perfection with counterfactual as well as indicative conditionals, though its predicted differences between the two were not reliably detected.[^s5] Earlier findings that promises and threats invite the most denying-the-antecedent and affirming-the-consequent responses fit the same picture, though they cannot show whether reasoners track conversational cues or other information.[^s2] Overall, the existence of the inference is well supported, while its rate and its best explanation remain under study, hence the status mixed.[^s2][^s3]

## Connections

Conditional perfection is a kind of conversational implicature and was **introduced by** Geis and Zwicky, Arnold Zwicky being one of the two linguists who named it.[^s2] It has been **explained by** scalar implicature in the work of van der Auwera and Horn,[^s2] and **explained by** exhaustification over contextually relevant alternatives in recent experimental work.[^s3] It **contrasts with** the material conditional, whose truth conditions say nothing about cases where the antecedent is false, so perfection adds content the logic does not supply.[^s2] It is **studied in** pragmatics, where it serves as a test case for theories of implicature,[^s1] and **studied in** the psychology of reasoning, which measures how often people draw it and what modulates it.[^s4] It explains why affirming the consequent and denying the antecedent often feel valid, connects to necessary and sufficient conditions and to commutation of conditionals, and can be diagnosed with the cancellability test.[^s2]

## Sources

[^s1]: von Fintel, "Conditional Strengthening: A Case Study in Implicature", MIT manuscript, September 2001. https://web.mit.edu/fintel/fintel-2001-condstrength.pdf (accessed 2026-11-17)
[^s2]: Godden & Zenker, "Denying Antecedents and Affirming Consequents: The State of the Art", *Informal Logic* 35(1):88-134, 2015. https://www.lunduniversity.lu.se/lup/publication/5eab0ec9-546b-4399-8129-5c043a272ee0 (accessed 2026-11-17)
[^s3]: Evcen, Bale & Barner, "Conditional inference and access to alternatives: The role of QUD and speaker knowledge in conditional perfection", *Journal of Semantics*, accepted manuscript. https://ebruevcen.github.io/files/EvcenBaleBarner_inpress.pdf (accessed 2026-11-17)
[^s4]: Liu & Barthel, "Semantics Processing of Conditional Connectives: German wenn 'if' Versus nur wenn 'only if'", *Journal of Psycholinguistic Research* 50(6):1337-1368, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8660741 (accessed 2026-11-17)
[^s5]: Schwab & Liu, "Processing attenuating NPIs in indicative and counterfactual conditionals", *Frontiers in Psychology* 13:894396, 2022. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.894396/pdf (accessed 2026-11-17)
