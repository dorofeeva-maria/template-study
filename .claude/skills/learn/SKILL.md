---
name: learn
description: Study this subject — the entry point of the learn framework. Starts every study session (warm-up on closed items, the strand portion), finds the current subtopic and stage, and hands over to learn-setup, learn-artifact, learn-practice or learn-close. Use for any study request in this repo ("let's study", "continue", "practice", "check me", "next").
---

# learn — the session entry point

One subject → a cumulative sequence of subtopics → each one taken through a full cycle until it is
automatic. This skill runs the **session**; the work of each stage lives in its own skill:

| Skill | Rhythm | Does |
|---|---|---|
| `learn` (this) | every session | warm-up, strand portion, routing, background jobs |
| `learn-setup` | once per subject (+ `add-topic`) | mission, sources kick-off, diagnostic, plan |
| `learn-sources` | setup, gaps, on request — **background** | vetted `resources.md` |
| `learn-artifact` | once per subtopic — **background build + independent fact-check** | theory artifact |
| `learn-practice` | every session | `check` · `practice` · `timed` · `ticket`, counter |
| `learn-close` | once per subtopic | reference sheet, review queue, move on |

The stage skills are internal: always start here, then read the stage skill's `SKILL.md` and
follow it. Shared files: [RULES.md](RULES.md) (terms, stages, iron rules, background agents —
read first) and `formats/` (plan, hub, resources, review queue, strand). Skill paths below are
relative to `.claude/skills/`.

## Usage

```
learn                     continue: warm-up → the next step of the current subtopic → strand
learn plan                → learn-setup (new subject or rebuild the plan)
learn add-topic <topic>   → learn-setup add-topic
learn theory              → learn-artifact: issue (or prepare) the current subtopic's artifact
learn check | practice | timed | ticket   → learn-practice in that mode
learn close               → learn-close for the current subtopic
learn sources [gap|audit] → learn-sources (background)
learn status              one screen: current subtopic, stage, counters, due warm-ups, jobs
```

## Every session

1. **Sync and read** (RULES.md › State): the plan, the current hub, `review-queue.md`, the tail of
   `log.md`. Leftover `*.draft.*` files from an earlier session → finish their review (fact-check
   if missing) before using them.
2. **No plan yet** → `learn-setup`; stop here.
3. **Upgrade an older repo (once).** See "Upgrading an older repo" below.
4. **Warm-up** — once per study day: offered in each conversation of the day until it is done or
   the learner declines it for today. Take the due rows of `review-queue.md` (oldest due first, at
   most the plan's count). One cold question per item, at the level of the hub's last column, in a
   fresh form (not a task from its log). The learner answers in one batch; review per RULES.md.
   Update the queue per `formats/review-queue.md`; a mistake starts that item's extra pack (see
   `learn-practice` › Review, route 2).
5. **Route by the current subtopic's stage** (hub first; stage list in RULES.md):
   - `not started` → `learn-artifact issue` (prepared artifact, or build it now);
   - `theory` → a theory session (`learn-artifact` › theory session); when the learner says theory
     is done → `learn-practice check`;
   - `check` / `practice` / `timed` / `project` → `learn-practice` in that mode;
   - all items closed in the last column → `learn-close`;
   - no current subtopic (all `done`/`before entry`, or only `paused`/`moved on` left) → ask the
     learner which to take up, or propose `learn-close` › end of the subject.
   An extra pack in progress (any subtopic) takes the first part of the session; the rest goes to
   the route above.
6. **Strand portion** — once per study day, if the subject has a strand: after the session's pack
   (never before a pack on the subtopic its items come from), per `formats/strand.md`.
7. **Background jobs** (RULES.md › Background agents; launch, don't wait):
   - the current subtopic passed `check` and the next subtopic has no artifact → `learn-artifact
     prepare` for it;
   - a gap in `resources.md` touches the current or next subtopic → `learn-sources gap`.
   When a job's report arrives: apply what it proposes (hub, plan, `resources.md`), launch the
   fact-check for a built draft, commit. Tell the learner in one line only if it changes what they
   do.
8. **End** (RULES.md › State): log line, plan status in sync with the hub, index, check, commit.

## Upgrading an older repo

Done once, when the repo predates this version; tell the learner in one line and keep it short.
1. **Mission** — draft it from what the plan already says (goal, north star, notes), then confirm
   it part by part with the learner. Prior knowledge goes into a `## Starting point` section (no
   diagnostic for a repo already under way).
2. **Config** — add the missing lines with defaults and say so: Warm-up (count, intervals).
3. **Sources** — no `resources.md` → `learn-sources build` in the background, seeded with the
   plan's sources and the §4 lists of existing artifacts. Until it returns, nothing in step 7
   depends on it.
4. **Old artifacts** — an issued artifact without inline citations or a `fact-checked` date →
   run the `learn-artifact` › Fact-check on it in the background; fix what it finds before the
   next pack on that subtopic. Old artifacts keep their inline styles; new ones link
   `artifacts/assets/`.
5. **Queue** — no `review-queue.md` → create it with the items of `done` subtopics.
6. **Hubs** — when a hub is next touched: add `## Notes for the artifact` and `## Misconceptions`
   (headings may be in the repo's language), and rewrite its counter header to the current rule
   (`learn-practice` › The counter).
7. **Leftovers** — run `python tools/notes.py check -v` and fix what it finds (stray tool tags,
   `[[wikilinks]]`, paths from an older layout, broken tables).

## `learn status`

Current subtopic and stage; its counter column (open items with scores); extra packs in progress;
warm-up rows due today and this week; background jobs running or reported; open gaps in
`resources.md`. Facts only.
