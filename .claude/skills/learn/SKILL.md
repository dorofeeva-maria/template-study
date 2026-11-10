---
name: learn
description: Study this subject — the entry point of the learn framework. Starts every study session, walks the next step of every subtopic in work (up to three in parallel — pretest, reading, self-check, check, packs), gives the strand portion, and hands over to learn-setup, learn-artifact, learn-practice or learn-close. Use for any study request in this repo ("let's study", "continue", "practice", "check me", "next").
---

# learn — the session entry point

One subject → a cumulative sequence of subtopics → each one taken through a full cycle until it is
automatic, up to three at a time (RULES.md › The pipeline). This skill runs the **session**; the
work of each stage lives in its own skill:

| Skill | Rhythm | Does |
|---|---|---|
| `learn` (this) | every session | the pipeline walk, strand portion, background jobs |
| `learn-setup` | once per subject (+ `add-topic`) | mission, sources kick-off, diagnostic, plan |
| `learn-sources` | setup, gaps, on request — **background** | vetted `resources.md` |
| `learn-artifact` | once per subtopic — **background build + independent fact-check** | pretest, theory artifact |
| `learn-practice` | every session | `check` · `practice` · `timed` · `ticket`, counter |
| `learn-close` | once per subtopic | reference sheet, topic map, next subtopic in |
| `learn-video` | on request (build on macOS) | narrated slide video: lecture or practice pack |

The stage skills are internal: always start here, then read the stage skill's `SKILL.md` and
follow it. Shared files: [RULES.md](RULES.md) (terms, stages, the pipeline, iron rules, background
agents — read first) and `formats/` (plan, hub, resources, strand). Skill paths below are
relative to `.claude/skills/`.

## Usage

```
learn                     continue: the next step of every subtopic in work, newest first → strand
learn plan                → learn-setup (new subject or rebuild the plan)
learn add-topic <topic>   → learn-setup add-topic
learn pretest [M.K]       → learn-artifact pretest (the newest subtopic in work by default)
learn theory [M.K]        → learn-artifact issue
learn check | practice | timed | ticket [M.K]   → learn-practice in that mode
learn close [M.K]         → learn-close
learn video lecture|practice [pack]  → learn-video (narrated slide video, built on a Mac)
learn sources [gap|audit] → learn-sources (background)
learn status              one screen: subtopics in work, stages, counters, limits, jobs
```

## Every session

1. **Sync and read** (RULES.md › State): the plan, the hubs in work, the tail of `log.md`.
   Leftover `*.draft.*` files from an earlier session → finish their review (fact-check if
   missing) before using them.
2. **No plan yet** → `learn-setup`; stop here.
3. **Upgrade an older repo (once).** See "Upgrading an older repo" below.
4. **Fill the pipeline.** Fewer subtopics in work than the plan's `In work` → the next `not
   started` subtopics in the plan's order enter at `pretest` (their artifacts prepared first, in
   the background).
5. **Walk the pipeline** (RULES.md › The pipeline). List the next available step of each subtopic
   in work, newest first, in one short message, then take them in that order; as much as fits
   the session, the rest next time:
   - `pretest` with a prepared artifact and no pretest given → `learn-artifact pretest`;
     pretest answered and the artifact deepened → `learn-artifact issue`;
   - `theory` → the learner reads (`learn-artifact` › theory session); when they say it is read
     → stage `self-check`;
   - `self-check` → the learner answers §3 on their own; when they say it is done →
     `learn-practice check`;
   - `check` / `practice` / `timed` / `project` → one pack in that mode (`learn-practice`);
   - all items closed in the last column → `learn-close`;
   - a stage the subtopic before it has not passed yet → skip it this session.
   An extra pack in progress takes the first part of the session. Nothing in work and nothing
   left `not started` → ask the learner which `paused`/`moved on` subtopic to take up, or propose
   `learn-close` › end of the subject.
6. **Strand portion** — once per study day, if the subject has a strand: after the session's
   packs, per `formats/strand.md`.
7. **Background jobs** (RULES.md › Background agents; launch, don't wait):
   - a subtopic will enter the pipeline next (a place frees soon, or one is free) and has no
     artifact → `learn-artifact prepare` for it;
   - the session ends and the newest subtopic in work has a prepared artifact without a pretest →
     give the pretest at the end of the session, so the deepening runs before the next one;
   - a gap in `resources.md` touches a subtopic in work or the next one → `learn-sources gap`.
   When a job's report arrives: apply what it proposes (hub, plan, `resources.md`), launch the
   fact-check for a built draft, commit. Tell the learner in one line only if it changes what they
   do.
8. **Limits.** For each subtopic in work that was touched this session and has its artifact read,
   add one to its session count in the hub; at the plan's limit with items still open → `moved on`
   (`learn-practice` › Moving on).
9. **End** (RULES.md › State): log line, plan status in sync with the hubs, index, check, commit.

## Upgrading an older repo

Done once, when the repo predates this version; tell the learner in one line and keep it short.
1. **Mission** — draft it from what the plan already says (goal, north star, notes), then confirm
   it part by part with the learner. Prior knowledge goes into a `## Starting point` section (no
   diagnostic for a repo already under way).
2. **Config** — add the missing lines with defaults and say so: `In work` (default 3); `Limit per
   subtopic` (default 4 sessions); Strand count per study day (default 5) if the subject has a
   strand and its Config gives no number.
3. **The pipeline (no warm-ups).** A repo with a `review-queue.md` or a Warm-up line in Config:
   remove the Warm-up line and any rule about warm-ups in Config and `AGENTS.md`; a per-subtopic
   limit of 1–2 sessions there becomes the `Limit per subtopic` line; put `Archived YYYY-MM-DD —
   warm-ups were removed; nothing reads this file.` under the queue's heading and leave the file.
   The current subtopic stays at its stage and becomes the first in work (a subtopic in `theory`
   whose artifact the learner already read → `self-check`); the next `not started` ones in the
   plan's order fill the pipeline at `pretest` (step 4). Session counts start from 0. The plan's
   Status marks the subtopics `in work` instead of one `current`.
4. **Sources** — no `resources.md` → `learn-sources build` in the background, seeded with the
   plan's sources and the §4 lists of existing artifacts. Until it returns, nothing in step 7
   depends on it.
5. **Old artifacts** — an issued artifact without inline citations or a `fact-checked` date →
   run the `learn-artifact` › Fact-check on it in the background; fix what it finds before the
   next pack on that subtopic. Old artifacts keep their inline styles; new ones link
   `artifacts/assets/`.
6. **Hubs** — when a hub is next touched: add `## Notes for the artifact` and `## Misconceptions`
   (headings may be in the repo's language), the `Sessions` line, and rewrite its counter header
   to the current rule (`learn-practice` › The counter).
7. **Leftovers** — run `python tools/notes.py check -v` and fix what it finds (stray tool tags,
   `[[wikilinks]]`, paths from an older layout, broken tables).

## `learn status`

Subtopics in work with stage, session count against the limit, counter column (open items with
scores); extra packs in progress; the next subtopic to enter; background jobs running or reported;
open gaps in `resources.md`. Facts only.
