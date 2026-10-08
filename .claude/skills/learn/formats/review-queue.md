# Review queue format — `review-queue.md`

Items of closed subtopics, scheduled for cold warm-up questions.
Filled by `learn-close`; read and updated by `learn` every study day.
Frontmatter `type: review-queue`.

```md
---
title: <Subject> — review queue
type: review-queue
updated: YYYY-MM-DD
tags: [learn]
---

# <Subject> — review queue

Warm-up schedule for items of closed subtopics.

| Item | Hub | Step | Due | History |
|------|-----|------|-----|---------|
| 1.1 §2.3 zero article | [1.1](1.1-articles.md) | 2 | 2026-10-18 | 10-08 ✓ · 10-11 ✓ |
```

- **Step** indexes the interval list in the plan's Config. A new row: step 0, Due = closing day +
  interval[0].
- Warm-up answer correct → step + 1, Due = today + interval[new step]. A correct answer past the
  last step **retires** the row (moved to `## Retired`); the item is still woven into later tasks.
- Mistake → step 0, Due = today + interval[0], and the item's extra pack starts
  (`learn-practice` › Review, route 2). A warm-up answer does not change the extra pack's score.
- History: `MM-DD ✓|✗`, newest last.
