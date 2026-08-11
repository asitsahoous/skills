# Pattern catalog

Four categories. Structural patterns govern how a piece is built, lexical ones show up in word choice, rhetorical ones are sentence-shape tics, and conversational ones are specific to chat and assistant output.

Each entry gives the tell and a repair. The repair is almost always substitution rather than deletion.

**Contents**
- [Structural](#structural)
- [Lexical](#lexical)
- [Rhetorical](#rhetorical)
- [Conversational and assistant-specific](#conversational-and-assistant-specific)
- [Domain variants](#domain-variants)

---

## Structural

### 1. Generic opening hook
Opens with a statement that could introduce almost any piece.

> In today's rapidly evolving landscape, artificial intelligence is transforming industries.

Repair: start at the actual observation. "Reducto raised $75M eleven months after their Series A. Nobody in document extraction has moved that fast."

### 2. Predictable paragraph architecture
Observation, explanation, implication, future prediction. Repeated for every paragraph. On social platforms: hook, three bullets, reflection, question.

Repair: vary it. Lead with the conclusion sometimes. End on evidence sometimes. Let one paragraph be a single sentence and the next run six.

### 3. Generated lists
Interchangeable items that could belong to any list on any topic.

> Benefits include improved efficiency, enhanced productivity, reduced costs, and better decision making.

Repair: cut to the items that are actually true here, name them specifically, and accept that a list of two is fine.

### 4. Padded enumeration
Three real points split into seven to fill a numbered list. Watch for adjacent items that restate each other.

Repair: merge. A tight list of three beats a padded list of seven.

### 5. Perfect balance
Pros, cons, balanced conclusion, no position taken.

Repair: have an opinion. Where genuinely uncertain, say what would change your mind rather than presenting both sides as equally weighted.

### 6. Universal conclusion
> The future is exciting. This is only the beginning. We're just getting started.

Repair: end on the last real point. Most pieces do not need a conclusion at all.

### 7. Over-structuring
Headers, bold, and bullets applied to what is really three paragraphs of prose. Structure signals rigor when there is none.

Repair: if a section is two sentences, it is not a section.

### 8. Bold inflation
So much bolded that nothing stands out.

Repair: bold at most one thing per screen, and only when a reader skimming needs to land there.

### 9. Retrospective summary
Ending by restating what was just said, in a piece short enough that the reader remembers.

Repair: delete. Summaries earn their place in long documents only.

---

## Lexical

### 10. Empty superlatives
groundbreaking, transformative, revolutionary, game-changing, cutting-edge, next-generation, powerful, seamless

> A revolutionary retrieval system.

Repair: replace the adjective with the fact that made you reach for it. "Retrieval latency dropped from 450ms to 90ms."

### 11. Corporate buzzwords
leverage, empower, unlock, harness, optimize, streamline, robust, scalable, holistic, best-in-class, mission-critical

Repair: most have a plain equivalent. Leverage becomes use. Unlock becomes enable, or nothing.

### 12. Weightless intensifiers
genuinely, actually, truly, really, simply, essentially, fundamentally, importantly

These signal emphasis without adding meaning, and often signal the opposite — a writer propping up a claim that cannot stand alone.

Repair: delete. If the sentence weakens, the sentence was weak.

### 13. Adjective stacking
> a robust, scalable, production-ready architecture

Repair: pick the one that matters, or replace all three with a number.

### 14. Excessive transitions
Furthermore, Moreover, Additionally, However, Ultimately, In conclusion

Repair: delete most. Human writing jumps. Where a transition is genuinely needed, "but" and "so" usually do it.

### 15. Em dashes
> The real challenge isn't the model—it's the data.

One per document reads as style. Ten reads as a signature.

Repair: comma, colon, full stop, or restructure. Note that some users ban them outright; check standing instructions.

### 16. Hedge stacking
roughly, approximately, arguably, somewhat, potentially, in some cases — layered to simulate care.

Repair: one hedge, or state the uncertainty concretely. "I could not verify this" beats "this is arguably somewhat uncertain."

### 17. Agentless assertion
> It is widely regarded that... Many experts believe... It is often said...

Repair: name who, or drop the claim.

---

## Rhetorical

### 18. Symmetric construction
> It's not about X. It's about Y.
> We don't need more models. We need better products.

The highest-frequency tell in current AI prose.

Repair: state the positive claim directly. "We need better products" carries the whole meaning.

### 19. Manufactured contrast pair
Two clauses, subjects swapped, second adds nothing.

> Four reads as volume. One reads as judgment.

Repair: keep one clause. "A stack of four memos reads as volume rather than judgment."

### 20. Rule of three
> Faster. Better. Smarter.
> Speed, scale and accuracy.

Repair: two items, or four. Break the cadence deliberately.

### 21. Excessive parallelism
> We need faster models. We need better data. We need stronger evaluation.

Repair: vary the sentence openings. Combine two of them.

### 22. Fragment for drama
A very short sentence on its own line to manufacture weight.

> HP builds the input.

Occasionally effective. Repeated, it becomes a verbal tic.

Repair: fold into the surrounding paragraph unless it is genuinely the pivot of the argument, and then use it once.

### 23. Aphoristic closer
Ending a section with a portable-sounding maxim that asserts nothing checkable.

> Specificity beats polish.
> Trust is the real infrastructure.

Repair: end on the concrete point instead. If the maxim is the only thing there, the section had no content.

### 24. Signposting your own cleverness
> Here's the thing. That's the whole point. That's what makes it work.

Repair: delete. If the point lands, it lands without being announced.

### 25. Concessive pivot theatre
> X is real. But the deeper question is X.

Simulates nuance while returning to the same claim.

Repair: only concede when the concession changes the conclusion.

### 26. Fake depth
Grammar of insight, no information.

> AI enables organizations to unlock new opportunities by leveraging intelligent automation to drive efficiencies across business processes.

Repair: translate to plain words. "AI helps companies automate work." Then decide whether that was worth a sentence.

### 27. Overexplaining
Eighty words to say something that takes twelve.

Repair: write the twelve-word version and see what is actually lost.

### 28. Analogy reflex
Reaching for a metaphor when plain description is shorter and clearer. "Think of it like a Swiss Army knife for data."

Repair: describe the thing. Keep the analogy only when it does work no description can.

### 29. Fake novelty
> Nobody talks about this. Here's the secret. Most people don't know...

Usually followed by something everyone knows.

Repair: drop the frame. If it is genuinely novel, the content shows it.

### 30. Artificial optimism
Every release is incredible, every company is innovating.

Repair: be skeptical where skepticism is warranted. Name what could go wrong.

### 31. No concrete detail
The largest single tell.

> Agentic workflows improve enterprise efficiency.

versus

> We removed four manual review steps from loan onboarding by letting an agent classify exceptions before routing them.

Repair: names, numbers, dates, specific outcomes. If none are available, that is worth knowing before publishing.

---

## Conversational and assistant-specific

### 32. Sycophantic opener
> Great question! That's a really interesting point.

Repair: answer.

### 33. Restating the prompt
> You're asking about how to structure the memo. Let me address that.

Repair: delete. Start with the answer.

### 34. Narrating instead of doing
> Let me break this down for you. I'll walk you through the key considerations.

Repair: break it down.

### 35. Reflexive closing offer
Ending every turn with "Want me to...?" or "Let me know if you'd like...".

Repair: offer when there is a genuine next step, not by default.

### 36. Fake curiosity
> Thoughts? What do you think? Would love your perspective.

Appended automatically to posts.

Repair: ask a real question or end.

### 37. Fake personal story
> I recently realized... I had an interesting conversation...

No details follow.

Repair: include the specifics that make it believable, or cut the frame. "I was scrolling after dinner and found an NVIDIA engineer explaining KV cache in two minutes" is credible because of the detail.

### 38. Hedge sandwich
Disclaimer, advice anyway, disclaimer.

> I'm not a lawyer, but you should probably X, though do consult a lawyer.

Repair: give the useful information once, state the limit once, in that order.

---

## Domain variants

**Technical writing.** Claims of state-of-the-art, production-ready, enterprise-grade, scalable architecture with no numbers attached. Every architecture diagram drawn as the same vertical stack. Repair: benchmarks, versions, latency figures, failure modes.

**Social posts.** The template is recognisable from three lines in: short hook, line break, false modesty, three lessons, inspirational close, question. Repair: break the template anywhere. Start mid-thought. End without a question.

**Resumes and professional documents.** Process verbs standing in for outcomes (evaluate, serve as, leverage, drive). Caveat bullets that argue a point rather than state one. Repair: outcomes and coverage, not activity.

**Images.** Hyper-smooth skin, perfect symmetry, unnaturally clean environments, orange and teal cinematic grading, excessive glow, malformed text, every face a stock model.

---

## What authentic writing has instead

- One concrete observation in place of a sweeping claim
- Specific numbers, names, dates, examples
- A clear position, even a debatable one
- Irregular rhythm rather than uniform sentence length
- Fewer adjectives, more evidence
- Real trade-offs and stated uncertainty
- Details only someone who did the work would include
