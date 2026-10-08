# Product Discovery — Worked Example
Product: Clausehound (fictional) — AI contract review for in-house legal teams.
## Inputs
### Product description
Clausehound reviews vendor agreements and NDAs in minutes. Upload a contract and get a clause-level risk summary, suggested redlines, and a negotiation playbook. Built for in-house legal teams handling high volumes of routine agreements.
### User reviews (sample)
1. “Cut our NDA turnaround from three days to twenty minutes. It flagged a liability cap issue our outside counsel missed.” — General Counsel, Series C SaaS company
2. “The redlines are a decent first pass, but I rewrite about half of them. It struggles with our bespoke IP clauses.” — Senior Corporate Counsel, fintech
3. “Legal loves it. Procurement keeps uploading the wrong template version and blaming the tool.” — Head of Legal Ops, healthcare company
4. “We ran it alongside outside counsel for a quarter. It missed jurisdiction-specific data clauses twice.” — Deputy General Counsel, enterprise software
## Discovery report
### Problem statement
In-house legal teams are a bottleneck on routine agreements. NDAs and vendor contracts wait days for review while deals stall, and outside counsel is too expensive for low-risk paperwork.
### Target users and personas
- General Counsel at growth-stage companies: owns risk, measured on turnaround time.
- Senior corporate counsel: does the actual redlining, cares about draft quality.
- Head of Legal Ops: owns tooling and process, cares about adoption and templates.
### Pain points
- Review queues: routine agreements sit for days waiting for a lawyer.
- Inconsistent redlines across matters and team members.
- Outside counsel spend on work that is low risk and repetitive.
- Missed edge cases: jurisdiction-specific clauses slip through both humans and the tool.
### Current solutions and workarounds
- Playbooks in shared docs that go stale.
- Outside counsel for overflow, at high cost.
- Paralegals doing first-pass review manually.
### Unmet needs
- Reliable handling of bespoke and jurisdiction-specific clauses (reviews 2 and 4).
- Guardrails against user error, like wrong template versions (review 3).
- A way to measure whether the tool’s redlines get accepted or rewritten, so quality improves.
### Generated ideas
1. Clause library learning: track which redlines lawyers accept versus rewrite, and tune suggestions per company.
2. Template guardrails: detect when an uploaded document does not match the expected template and warn before review.
3. Jurisdiction packs: add-on clause packs for data privacy and employment terms by state and country.
4. Outside-counsel mode: a diff view comparing the tool’s output with counsel’s markup, for calibration.
### Recommendations
- Ship the template guardrail first: it addresses the most visible failure and needs no model work.
- Build the accept-versus-rewrite telemetry before tuning anything: without it, idea 1 is guesswork.
- Treat jurisdiction packs as the expansion wedge: it is the clearest gap versus both humans and competitors.
- Do not chase full autonomy yet: reviews 2 and 4 show trust is the binding constraint, and trust comes from measured accuracy.
