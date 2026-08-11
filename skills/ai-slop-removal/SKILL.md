---
name: ai-slop-removal
description: Detect and strip AI-generated writing patterns from any text, covering generic hooks, empty superlatives, rule-of-three, symmetric "not X but Y" constructions, em dashes, buzzword filler, fragment-for-drama, aphoristic closers, and the rest of the tells. Use whenever someone asks to remove AI slop, make writing sound human, de-AI a draft, or says something "sounds like ChatGPT." Also run it proactively before delivering any drafted prose (emails, LinkedIn or X posts, memos, reports, resumes, cover letters, decks, documentation) because these patterns are far cheaper to catch before the user reads them than after. If you are about to hand someone writing they will put their name on, run this first.
---

# Removing AI slop

## The operating test

AI slop is language optimized for sounding useful. Good writing is language optimized for conveying something specific.

Apply that sentence by sentence. If a sentence would survive being pasted into a different document on a different topic, it is slop. Delete it or replace it with something only a person who did the work would know.

## The failure mode to avoid

Most attempts at this go wrong in the same way: strip every adjective, chop every sentence to eight words, and produce clipped staccato prose. That is a different machine flavor, not human writing.

Humans vary rhythm. Some sentences run long because the thought is complicated, and the next one is four words. Some paragraphs are one line, most are four. Deletion alone produces flat text. The real repair is usually substitution: replace the abstraction with the concrete fact it was standing in for.

If you cannot find a concrete fact to put in its place, that is a signal the sentence had no content and should go entirely.

## Workflow

**1. Read for content first.** Before touching prose, ask what each paragraph claims. Slop tends to cluster where the writer had nothing to say. Fixing the writing there means finding something to say, not rewording.

**2. Run the mechanical pass.** `scripts/detect.py` catches what greps reliably: em dashes, buzzwords, transition openers, weightless intensifiers, symmetric constructions, closing questions, suspiciously short paragraphs. Run it, then judge each hit. The script flags candidates; it does not make decisions.

```bash
python scripts/detect.py draft.md
python scripts/detect.py draft.md --category structural
python scripts/detect.py draft.md --quiet          # counts only
```

The script cannot tell live prose from a quoted example, so a document that discusses slop will light up. Density per thousand words is the useful signal: clean prose sits near 2, a slop-heavy draft runs past 50.

**3. Do the judgment pass.** Read `references/patterns.md` for the full catalog with before-and-after examples. The patterns that matter most and that greps miss entirely: fake depth, generated lists, aphoristic closers, and the absence of concrete detail.

**4. Verify.** Re-read the output cold. Two questions:
- Does any sentence still work in a different document on a different topic?
- Did I over-correct into staccato?

**5. Report honestly.** Tell the person which specific lines changed and why. Do not claim a tool did the judgment work, because the script only flags candidates.

## The highest-yield patterns

Full catalog in `references/patterns.md`. If you only check six things, check these.

**No concrete detail.** The single biggest tell. "Agentic workflows improve enterprise efficiency" versus "we removed four manual review steps from loan onboarding by letting an agent classify exceptions before routing." Specificity is not decoration. It is the content.

**Symmetric constructions.** "It's not about X, it's about Y." "We don't need more models. We need better products." Works once in a piece. Three times and the machine is showing.

**Fake depth.** Sentences with the grammar of insight and none of the substance. "AI enables organizations to unlock new opportunities by leveraging intelligent automation to drive efficiencies." Translate it: AI helps companies automate work. Then ask whether that was worth saying.

**Rule of three.** "Faster, better, smarter." "Speed, scale and accuracy." Humans use triads. Machines reach for them by default. Count them: more than one or two in a page is a tell.

**Aphoristic closers.** Ending a section with a maxim that sounds earned and is not. "Specificity beats polish." "Trust is the real infrastructure." These feel like conclusions and assert nothing testable.

**Em dashes.** One in a document is fine. Ten is a signature. Most can become a comma, a colon, a full stop, or nothing.

## Register matters

Not every punchy line is slop, and sanding everything flat is its own failure.

A slide deck tolerates fragments and taglines that would be slop in a memo. A headline is allowed to be a headline. A closing line in a pitch can carry rhetorical weight if it makes a claim someone could argue with.

The test is whether the line **asserts something specific**. "I already do this job, from the other side of the table" is punchy and defensible, because it makes a checkable claim. "Trust is the new currency" is punchy and empty.

Preserve voice. The goal is writing that sounds like the person who wrote it, not writing that sounds like nobody.

## Reference files

- `references/patterns.md`: full catalog, roughly 30 patterns across four categories, each with a repair example. Read it during the judgment pass.
- `scripts/detect.py`: mechanical detector. Flags candidates by category, reports line numbers and density per thousand words.
