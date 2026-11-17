---
id: ct:wisdom-of-crowds
type: Phenomenon
title: Wisdom of crowds
aliases: [wisdom of the crowd, crowd wisdom, wisdom-of-crowd effect, vox populi effect]
domain: decision-making
summary: >-
  The finding that the average (or median) of many independent individual
  estimates is often more accurate than most of the individuals who made them,
  because their errors partly cancel out; the effect weakens when judges share
  information, think alike or are swayed by one another.
level: introductory
evidenceStatus: robust
broader: [ct:group-decision-making]
related: [ct:dialectical-bootstrapping, ct:delphi-method, ct:geopolitical-forecasting, ct:richard-larrick, ct:groupthink, ct:overconfidence-effect, ct:calibration]
requires: [ct:judgment-and-decision-making]
relations:
  - {predicate: introducedBy, object: ct:francis-galton, source: s1, confidence: high}
  - {predicate: studiedIn, object: ct:judgment-and-decision-making, source: s3, confidence: high}
  - {predicate: supportedBy, object: ct:mannes-2014-wisdom-of-select-crowds-study, source: s4, confidence: high}
  - {predicate: challengedBy, object: ct:lorenz-2011-social-influence-study, source: s2, confidence: high}
  - {predicate: appliedIn, object: ct:forecasting, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Vox Populi"
    publisher: Nature 75, 450-451 (Galton, 7 March 1907), page scan on galton.org
    url: https://galton.org/cgi-bin/searchImages/search/essays/pages/galton-1907-vox-populi_1.htm
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "How social influence can undermine the wisdom of crowd effect"
    publisher: Proceedings of the National Academy of Sciences 108(22), 9020-9025 (Lorenz, Rauhut, Schweitzer & Helbing, 2011), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Intuitions About Combining Opinions: Misappreciation of the Averaging Principle"
    publisher: Management Science 52(1), 111-127 (Larrick & Soll, 2006), record on RePEc/EconPapers
    url: https://econpapers.repec.org/RePEc:inm:ormnsc:v:52:y:2006:i:1:p:111-127
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "The wisdom of select crowds"
    publisher: Journal of Personality and Social Psychology 107(2), 276-299 (Mannes, Soll & Larrick, 2014), Duke Scholars record
    url: https://scholars.duke.edu/individual/pub1040384
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "The Wisdom of Crowds: Why the Many Are Smarter Than the Few (review)"
    publisher: Publishers Weekly review of Surowiecki, Doubleday, 2004
    url: https://www.publishersweekly.com/978-0-385-50386-0
    type: news
    accessed: 2026-11-17
created: 2026-11-17
---

# Wisdom of crowds

The wisdom of crowds is the finding that pooling many people's independent estimates, usually by taking the mean or median, tends to produce an answer more accurate than most of the individual estimates, and sometimes more accurate than the group's best-regarded member.[^s4] The effect is statistical rather than mystical: each person's estimate mixes signal with idiosyncratic error, and when errors fall on both sides of the truth they partly cancel in the average.[^s3] It is therefore a property of how judgments are combined, and it holds only under conditions that keep those errors from lining up.[^s2]

## Origin

The classic demonstration is Francis Galton's short paper "Vox Populi," published in *Nature* in March 1907.[^s1] At the West of England Fat Stock and Poultry Exhibition in Plymouth, visitors paid to guess the dressed weight of an ox; Galton analysed 787 legible tickets and found that the median guess was 1,207 lb against a true weight of 1,198 lb, an error of under one percent.[^s1] He presented this as evidence about the reliability of collective judgment, not of any individual voter.[^s1] The label "wisdom of crowds" was popularised much later by the journalist James Surowiecki's 2004 book of that name, which argued that a crowd outperforms a few experts when it has diversity of opinion, independence, decentralisation and a good way of aggregating answers.[^s5]

## How it works

Richard Larrick and Jack Soll showed why averaging helps: whenever two judges' estimates *bracket* the truth, one too high and one too low, their average must be closer than the typical judge.[^s3] Averaging gains most when errors are large and uncorrelated, and least when everyone errs in the same direction.[^s3]

A workplace example: a product team must estimate how many support tickets a new feature will generate in its first month. Five engineers privately write down 300, 450, 520, 800 and 1,100. The real figure turns out to be 610. The individual errors range from 90 to 490 tickets, but the mean of 634 misses by only 24, closer than any single engineer. Had the lead engineer announced "about 450" first, the others' guesses would likely have clustered near that number, and the average would have inherited the lead's error instead of cancelling it.[^s2]

Larrick and Soll also found that people misjudge the principle: many believe averaging will merely match the average judge and prefer to pick out the "best" person instead, an intuition that weakens when bracketing is made obvious.[^s3]

## How to apply it

- Collect estimates independently and before discussion, so early speakers do not anchor the rest.[^s2]
- Use the median, or a geometric mean, when estimates are skewed; Lorenz and colleagues found the arithmetic mean performed poorly on their right-skewed data.[^s2]
- Prefer a diverse set of judges whose errors are unlikely to share a common cause.[^s3]
- When you have a record of past accuracy, average the top few judges rather than trusting one expert or the whole crowd; Mannes, Soll and Larrick found that a "select crowd" of about five performed well across many conditions.[^s4]

## Evidence

The averaging benefit is mathematically guaranteed under bracketing and has been observed widely in practice.[^s3] Mannes, Soll and Larrick (2014) analysed 90 archival datasets and ran simulations and three experiments; whole-crowd averages usually beat most individuals, and averaging the best five judges was accurate across a wide range of environments. Their participants nonetheless preferred following a single expert.[^s4]

The main limit is independence. In a 2011 experiment with 144 ETH Zurich students answering factual questions over five rounds, Lorenz and colleagues found that showing people others' estimates shrank the diversity of answers without making the group more accurate, pushed the true value towards the edge of the group's range, and raised participants' confidence, a combination they called the social influence, range reduction and confidence effects.[^s2] The authors concluded that independent estimates are valuable but hard to preserve wherever people can see one another's views.[^s2]

## Connections

- **Introduced by** Francis Galton, whose 1907 ox-weighing analysis is the standard first demonstration.[^s1]
- **Studied in** judgment and decision-making research on combining opinions, as in Larrick and Soll's work on the averaging principle.[^s3]
- **Supported by** the Mannes, Soll and Larrick (2014) archival and experimental study of crowd and select-crowd strategies.[^s4]
- **Challenged by** the Lorenz et al. (2011) experiment showing that social influence can undermine the effect while inflating confidence.[^s2]
- **Applied in** forecasting, where aggregating several judges' predictions is a standard way to improve accuracy.[^s4]
- Related to dialectical bootstrapping, which simulates a crowd inside one head; to the Delphi method, which aggregates anonymous expert rounds; and to groupthink and overconfidence, which describe what happens when a group's judgments stop being independent.[^s2]

## Sources

[^s1]: Galton, F. (1907). "Vox Populi." *Nature* 75, 450-451. https://galton.org/cgi-bin/searchImages/search/essays/pages/galton-1907-vox-populi_1.htm (accessed 2026-11-17)
[^s2]: Lorenz, J., Rauhut, H., Schweitzer, F. & Helbing, D. (2011). "How social influence can undermine the wisdom of crowd effect." *PNAS* 108(22), 9020-9025. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299 (accessed 2026-11-17)
[^s3]: Larrick, R. P. & Soll, J. B. (2006). "Intuitions About Combining Opinions: Misappreciation of the Averaging Principle." *Management Science* 52(1), 111-127. https://econpapers.repec.org/RePEc:inm:ormnsc:v:52:y:2006:i:1:p:111-127 (accessed 2026-11-17)
[^s4]: Mannes, A. E., Soll, J. B. & Larrick, R. P. (2014). "The wisdom of select crowds." *Journal of Personality and Social Psychology* 107(2), 276-299. https://scholars.duke.edu/individual/pub1040384 (accessed 2026-11-17)
[^s5]: Publishers Weekly, review of J. Surowiecki, *The Wisdom of Crowds* (Doubleday, 2004). https://www.publishersweekly.com/978-0-385-50386-0 (accessed 2026-11-17)
