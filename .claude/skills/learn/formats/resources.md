# Resources format — `resources.md`

The vetted sources this subject is taught from. Written by `learn-sources`; artifacts draw their
material from here. Frontmatter `type: resources`.

```md
---
title: <Subject> — resources
type: resources
updated: YYYY-MM-DD
tags: [learn]
---

# <Subject> — resources

<one-line TL;DR>

## Anchor
The one curriculum / textbook / official spec the plan is built on, with a working URL.

## Knowledge
- [Kind: Title — author/org](https://…) · checked YYYY-MM-DD
  What it covers; use for: which subtopics / questions. Why it is trusted (one phrase).

## Wisdom (communities)
- [Name](https://…) · checked YYYY-MM-DD
  What it is, how it is moderated; use for: testing the skill for real (feedback, mock
  interviews, critique).

## Gaps
- What the mission needs and no good source covers yet; which subtopics it affects.

## Removed
- Title — why removed (wrong, shallow, marketing, dead link) · YYYY-MM-DD
```

Rules:
- **High-trust only:** official specs and docs, recognised textbooks and courses, peer-reviewed
  work, experts with a track record, well-moderated communities. Marketing dressed as education
  stays out.
- **Every entry annotated and dated.** A bare link is useless in three months.
- **Every URL opened before it is listed** (it loads and says what the note claims).
- **Prune ruthlessly:** better five sharp sources than thirty mediocre ones. A removed source goes
  to `## Removed` with the reason, so it is not re-added.
- **Gaps are explicit.** They drive the next search and mark subtopics the plan cannot ground yet.
- If the learner does not want communities, write that under Wisdom and stop proposing them.
