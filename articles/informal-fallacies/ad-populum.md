---
id: ct:ad-populum
type: InformalFallacy
title: Ad populum
aliases: [argumentum ad populum, appeal to popularity, appeal to the people, appeal to the majority, appeal to popular opinion, bandwagon fallacy, appeal to common belief]
domain: informal-fallacies
summary: >-
  The fallacy of treating the fact that many people, or most people, believe
  or do something as settling that it is true or right, when the popularity
  of the view gives little or no evidence for it in the case at hand.
level: introductory
evidenceStatus: normative
broader: [ct:informal-fallacy]
related: [ct:ad-verecundiam, ct:argument-from-expert-opinion, ct:wisdom-of-crowds, ct:presumption, ct:ignoratio-elenchi, ct:douglas-walton, ct:pragma-dialectics, ct:hasty-generalization]
requires: [ct:argument]
relations:
  - {predicate: contrastsWith, object: ct:ad-verecundiam, source: s1, confidence: high}
  - {predicate: exploits, object: ct:bandwagon-effect, source: s2, confidence: medium}
  - {predicate: introducedBy, object: ct:isaac-watts, source: s1, confidence: medium}
  - {predicate: studiedIn, object: ct:argumentation-theory, source: s3, confidence: high}
criticalQuestions:
  - Do most members of the group really hold this view, or is "everyone" an exaggeration or a badly measured poll?
  - Is the group in any special position to know whether the claim is true, or are they simply many?
  - Did the people in the group reach their view independently, or did they copy one another or one original source?
  - Is there other relevant evidence that the claim is false, and has popularity been used to avoid looking at it?
  - Is the question one that agreement actually settles, such as a convention, a vote or the meaning of a word, or is it a factual matter that agreement cannot make true?
argumentMap:
  premises:
    - "Almost every team in the company has moved its project tracking to the new tool."
    - "Nobody else is still using spreadsheets for this."
  conclusion: "So the new tool must be the best choice for our team's workflow, and we don't need to trial it first."
  verdict: fallacious
  objections:
    - "Other teams may have adopted it because it was the default or because a manager mandated it, not because they compared options."
    - "Their workflows may differ from ours; whether it suits our work is a question a short trial can answer directly."
sameAs: []
sources:
  - id: s1
    title: "Fallacies"
    publisher: Stanford Encyclopedia of Philosophy (Hans Hansen, first published 2015; substantive revision 2024)
    url: https://plato.stanford.edu/entries/fallacies/
    type: scholarly-encyclopedia
    accessed: 2026-11-18
  - id: s2
    title: "Arguments Based on Popular Opinion (ch. 6 of Media Argumentation: Dialectic, Persuasion and Rhetoric)"
    publisher: "Cambridge University Press (Douglas Walton, 2007), pp. 198-227"
    url: https://www.cambridge.org/core/books/media-argumentation/arguments-based-on-popular-opinion/C05340C2C7C778CCFE7D73091F321EFB
    type: textbook
    accessed: 2026-11-18
  - id: s3
    title: "Appeal to Popular Opinion"
    publisher: "Penn State University Press (Douglas Walton, 1998), publisher page"
    url: https://www.psupress.org/books/titles/0-271-01818-6.html
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "\"The people want it\": analysis and evaluation of the populist argument in the context of deliberation"
    publisher: "Journal of Argumentation in Context 9(3), 342-367 (Henrike Jansen, 2020), Leiden University repository"
    url: https://scholarlypublications.universiteitleiden.nl/access/item%3A3239684/view
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "How many laypeople holding a popular opinion are needed to counter an expert opinion?"
    publisher: "Thinking & Reasoning (Jos Hornikx, Adam J. L. Harris & Jordy Boekema, 2017), CORE open-access copy"
    url: https://core.ac.uk/download/111037698.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "Argumentum ad Populum (Introduction to Logic)"
    publisher: "Lander University Philosophy (Lee C. Archie)"
    url: https://philosophy.lander.edu/logic/popular.html
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Ad populum

*Ad populum*, the appeal to popularity, argues that a claim is true, or a course of action right, because many or most people accept it. Textbooks describe it as a cousin of the fallacious appeal to authority in which the source is popular opinion or "common knowledge" rather than a named expert. Its premises are often simply false ("everyone has one"), and even when they are true, widespread belief or practice usually gives only weak support to the conclusion.[^s1] A related variant, sometimes called playing to the gallery, stirs up a crowd's prejudices and feelings in place of evidence.[^s1][^s6] Douglas Walton put the core problem plainly: a large number of people accepting a proposition does not make it follow that the proposition is true, however persuasive that number feels.[^s2]

## Origin

John Locke's 1690 list of *ad*-arguments included *ad verecundiam*, *ad ignorantiam* and *ad hominem*, but not *ad populum*. It was the English logician Isaac Watts who added *argumentum ad populum*, described as a public appeal to the passions, to the list in the eighteenth century. Like Locke, Watts treated these as kinds of argument rather than as fallacies.[^s1] By the twentieth century the label had become a staple fallacy: Irving Copi's 1961 textbook placed it among the fallacies of relevance, while Johnson and Blair later filed appeals to popularity under hasty conclusions.[^s1] Walton's *Appeal to Popular Opinion* (1998) was presented as the first systematic study of the argument as a type in its own right; it distinguished eleven subtypes and contrasted appeals to prejudice with legitimate appeals to commonly accepted opinions and presumptions.[^s3]

## How it works

The argument usually has a simple shape: most people in some group accept A, so A is true, or so you should accept or do A too.[^s2][^s4] In the argument map above, a team concludes that a project-tracking tool must suit its workflow because nearly every other team uses it, and skips a trial. The popularity is real, but the inference needs an extra premise, that the majority is likely to be right on this question, and nothing supports it: the other teams may have followed a default or a mandate, and their work may differ.[^s4]

Henrike Jansen's reconstruction locates the fallacy in exactly that linking premise. The classic ad populum relies on a criterial premise that majority opinion indicates truth. Walton's scheme becomes stronger when it adds that the group is in a special position to know, and its critical questions ask whether a large majority really holds the view, whether other evidence points the other way, and why this majority should be trusted.[^s4] Jansen also examines populist policy arguments of the form "the people want it". Those rest on a procedural premise about democratic decision rather than a claim about truth, but she still judges them weak in deliberation, because measured opinion is unstable and the appeal can work as a trump card that ends substantive debate.[^s4]

Not every appeal to what people believe is fallacious. Majority practice does settle conventional matters such as what a word means, and in a democracy public opinion is relevant to some policy questions. Popular belief can also be weak inductive evidence when nothing else is available.[^s6] Walton's point is that such appeals should be judged by the context and the job they are doing, not dismissed automatically.[^s3]

## How to spot it

Watch for phrases such as "everyone knows", "most people agree", "nobody does it that way any more" or "join the millions who", used as the main reason for a factual or evaluative claim.[^s1][^s6] Ask the critical questions above: whether the majority is real, whether the group is placed to know, whether members judged independently, and whether contrary evidence is being skipped.[^s4] Advertising slogans that invite you to join a generation or a movement are a common everyday form.[^s6]

## How to counter it

Separate how many people hold a view from why they hold it, and ask for the reasons behind the majority's view.[^s4] Where the group has relevant expertise or independent access to the facts, give its agreement weight; where it does not, treat popularity as a starting presumption at most.[^s3][^s6] Experimental work by Hornikx, Harris and Boekema (2017) suggests people can do this weighing reasonably well. In an online study with about 146 Dutch adults, participants estimated how many laypeople it would take to outweigh an expert, and their estimates rose with the expert's accuracy and fell as the laypeople became more accurate, broadly tracking a Bayesian model. They struggled, however, with near-infallible experts, and the model assumes that the laypeople judge independently, which real crowds often do not.[^s5]

## Connections

Ad populum is the faulty form of Walton's presumptive argument from popular opinion: that scheme with an unsupported premise that the majority is likely to be right.[^s4] It **contrasts with ad verecundiam**, which appeals to a named authority rather than to the many.[^s1] Hornikx and colleagues argue the two source-based appeals sit on a continuum, and model how lay numbers trade off against expertise under the assumption that laypeople judge independently, the same condition on which the **wisdom of crowds** depends.[^s5] Walton notes the argument's psychological pull comes from our tendency to follow others and avoid being left out of the group, so it **exploits the bandwagon effect**.[^s2] The term was **introduced by Isaac Watts**, and the modern reassessment of the fallacy was led by **Douglas Walton** within **argumentation theory**,[^s1][^s3] while pragma-dialectical work such as Jansen's evaluates populist variants by soundness conditions.[^s4] Whately's tradition treats such *ad*-arguments as variants of **ignoratio elenchi**, fallacious only when used unfairly.[^s1]

## Sources

[^s1]: Hansen, "Fallacies", Stanford Encyclopedia of Philosophy (rev. 2024). https://plato.stanford.edu/entries/fallacies/ (accessed 2026-11-18)
[^s2]: Walton, "Arguments Based on Popular Opinion", ch. 6 of *Media Argumentation*, Cambridge University Press (2007). https://www.cambridge.org/core/books/media-argumentation/arguments-based-on-popular-opinion/C05340C2C7C778CCFE7D73091F321EFB (accessed 2026-11-18)
[^s3]: Walton, *Appeal to Popular Opinion*, Penn State University Press (1998). https://www.psupress.org/books/titles/0-271-01818-6.html (accessed 2026-11-18)
[^s4]: Jansen, "'The people want it': analysis and evaluation of the populist argument in the context of deliberation", Journal of Argumentation in Context 9(3), 342-367 (2020). https://scholarlypublications.universiteitleiden.nl/access/item%3A3239684/view (accessed 2026-11-18)
[^s5]: Hornikx, Harris & Boekema, "How many laypeople holding a popular opinion are needed to counter an expert opinion?", Thinking & Reasoning (2017). https://core.ac.uk/download/111037698.pdf (accessed 2026-11-18)
[^s6]: Archie, "Argumentum ad Populum", Introduction to Logic, Lander University. https://philosophy.lander.edu/logic/popular.html (accessed 2026-11-18)
