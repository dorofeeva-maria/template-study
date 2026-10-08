# Plan format — `<slug>-plan.md`

The map and the configuration of the subject. Written by `learn-setup`; the status table is kept
current by every skill. Frontmatter `type: plan`.

```md
---
title: <Subject> — plan
type: plan
updated: YYYY-MM-DD
tags: [learn]
---

# <Subject> — plan

<one-line TL;DR>

## Mission
- **Why:** 1–3 sentences — the real outcome (what changes in life/work), not "to understand X".
- **Success looks like:** 2–4 observable things the learner will be able to do.
- **Constraints:** time, budget, devices, preferences.
- **Out of scope:** adjacent things deliberately not chased now.

## Global subject            (only if this subject is part of one)
Numbered list of the parts in learning order + **we are here**.

## Starting point
Result of the setup diagnostic: what the learner already does cold (with evidence), what they
claimed to know (and how deep), misconceptions seen. Subtopics skipped by diagnostic are named.

## Map
Topics M → subtopics M.K. Per subtopic: name, prerequisites, applicable and target task types,
which part of which resource it rests on (or "no source — gap"), link to its hub.

## Status
| M.K | Stage | Level | Notes |
Stage: `not started` · `theory` · `check` · `practice` · `timed` · `project` · `done` ·
`skipped (diagnostic)`. Level = current counter column. Notes: artifact prepared/issued, decisions.

## Config
- **Difficulty ladder:** L1…Ln with the criteria of each (axes: items in play, nesting, cognitive
  level, novelty, framing). Which task types belong to which level.
- **Strand:** yes/no; what the items are; how many per study day; order of introduction; how the
  learner repeats them.
- **Project:** yes/no; what it is.
- **Timer:** yes/no; starting measure and target.
- **Artifact palette:** channels that fit the subject (prose · tables · diagrams/timelines ·
  images · embedded audio · embedded video · interactive/code · quizzes).
- **Warm-up:** questions per study day (default 3–5); intervals (default 1-3-7-14-30-60 days).

## Backlog
Topics to add later: mistakes outside the plan, "for later". Each with where it came from.
```

Rules: the map is grounded in the anchor sources of `resources.md` (never in guesses or in the
learner's words alone). Every subtopic links to its hub. Keep the Mission short — if it runs past
a screen it has become a plan.
