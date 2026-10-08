# Review queue format — `review-queue.md`

Items of closed (or diagnostic-skipped) subtopics, scheduled for cold warm-up questions.
Filled by `learn-close` and `learn-setup`; read and updated by `learn` every study day.
Frontmatter `type: review-queue`.

```md
---
title: <Subject> — review queue
type: review-queue
updated: YYYY-MM-DD
tags: [learn]
---

# <Subject> — review queue

| Item | Hub | Step | Due | History |
|------|-----|------|-----|---------|
| 1.1 §2.3 zero article | [1.1](1.1-articles.md) | 2 | 2026-10-15 | 10-08 ✓ · 10-11 ✓ |
```

- **Step** indexes the interval list in the plan's config (default 1-3-7-14-30-60 days). A new
  row starts at step 0 → due the next day.
- Warm-up answer correct → step +1, Due = today + interval. After the last step the row is
  **retired** (moved to `## Retired`); the item is still woven into later tasks.
- Mistake → step 0, due tomorrow, and the item gets an extra pack (see `learn-practice`,
  "mistake in a finished subtopic").
- History: `MM-DD ✓|✗`, newest last.
