# Strand format and rules — `<subject-slug>-strand.md`

What is learned across all topics. Configured in the plan; a portion is given by `learn` once per
study day; items are woven into tasks by `learn-practice`. Frontmatter `type: strand`.

```md
---
title: <Subject> — strand
type: strand
updated: YYYY-MM-DD
---

# <Subject> — strand

<one-line TL;DR: what the items are, how many per study day>

| # | Front | Back | Given | Last woven in |
```

Escape `|` inside cells as `\|` (a bare `|v|` breaks the table).

- **One portion per study day** (today's date already in Given → no portion), count from the
  config, given **in chat** after the pack (`learn` step 6); the learner copies the cards. Each item as **Front** and **Back** on separate lines, ready to paste.
- Language strands: Front — an example sentence with `______` in place of the target word; Back —
  the word, part of speech, meaning. Never a bare "word — translation". Technical strands: Front —
  the term, Back — an English definition.
- Items stay close to what is being studied; order of introduction by the config's criterion
  (needed/frequent first, hard-but-needed not at the very start).
- Every item is kept in order of issue with when it was given and when it was last woven into a
  task (update that cell only when you weave it); when choosing what to weave, prefer the oldest
  "last woven" among items already taught; lose none.
- **Weave given items into practice silently**, without emphasis.
- Topics at the junction of strand and theory (connectors, terms): explain usage in the artifact
  and add them to the strand.
