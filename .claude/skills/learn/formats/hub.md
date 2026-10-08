# Hub format — `<M.K>-<slug>.md`

One per subtopic; the source of truth for its progress. Frontmatter `type: hub`.

```md
---
title: <M.K> <Subtopic> — hub
type: hub
updated: YYYY-MM-DD
tags: [learn]
---

# <M.K> <Subtopic> — hub

<one-line TL;DR>

- **Stage / level:** …
- **Rests on:** <resource and the exact part> · **Primary source to read:** <one>
- **Artifact:** [<title>](artifacts/<slug>-<M.K>-<slug>.html) — prepared YYYY-MM-DD · issued YYYY-MM-DD · fact-checked YYYY-MM-DD
- **Reference sheet:** (after close) [..](reference/<slug>-<M.K>-<slug>.html)

## Notes for the artifact
Things to cover in more depth, collected before the artifact exists or before it is issued
(mistakes from earlier subtopics, learner requests). Each with date and origin.

## Items (= counter rows)
1. **§2.1** — short name
…

## Counter
Start 5 · mistake +1 · correct −1 (at most −1 per item per pack; closing needs correct answers on
two different days) · ≤0 closed · ≥10 critical.

| Item | L1 | L2 | … | T1 | … |
|------|----|----|---|----|---|

## Misconceptions
`YYYY-MM-DD · §2.N · what the learner believed (in their words) · how it showed up · resolved YYYY-MM-DD`
Only real misconceptions — a wrong mental model, not a slip. They predict future stumbling blocks.

## Log
`YYYY-MM-DD · stage · tasks given (short) · items each targeted · result · counter changes`
Black-box terms met in hands-on work: one word each.
```
