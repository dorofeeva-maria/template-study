# Subject

> Replace this heading and the line below with the subject's name, its goal, and the anchor source
> (the course, textbook or official spec the plan is built on). Also state the language notes are
> written in.

One subject, studied with the `learn` framework until each subtopic is automatic.

## How to work here

- **Study sessions start with the `learn` skill** (`.claude/skills/learn/SKILL.md`): it runs the
  session and hands each stage to its own skill (`learn-setup`, `learn-sources`, `learn-artifact`,
  `learn-practice`, `learn-close`). The iron rules are in `.claude/skills/learn/RULES.md` — read
  them before any study step.
- **Start from the plan**: `<slug>-plan.md` — its Mission says why, its status table shows the
  current subtopic and stage. A fresh repo has no plan yet: run `learn plan`.
- **Sources**: `resources.md` holds the vetted sources the subject is taught from. Material comes
  from there, not from memory.
- **Write as you go.** Results, counters, decisions and the learner's feedback go into the plan,
  the hub or `log.md` in the same turn, not at the end.
- **Rules the learner adds** while studying this subject (how they want tasks, cards, reviews)
  go into the *Subject rules* section below, one bullet each with the reason.
- **Files:** lowercase ASCII kebab-case; hubs `<M.K>-<slug>.md`; `resources.md`;
  `review-queue.md` (warm-up schedule); artifacts in `artifacts/`, their images in
  `artifacts/media/`, shared stylesheet and components in `artifacts/assets/` (link them, don't
  copy); reference sheets of closed subtopics in `reference/`. Large or device-only files
  (recordings) go into `.gitignore`.
- **Notes** (plan, hubs, strand, resources, review queue) start with frontmatter (`title`, `type`, `updated: YYYY-MM-DD`,
  optional `tags`) and a one-line TL;DR.
- **Links** are relative markdown links within this repo: `[text](1.2-some-subtopic.md)`. They
  never leave the repo.
- **`index.md`** is generated: `python tools/notes.py index` after adding or renaming notes.
- **`log.md`**: one line per meaningful session, newest at the bottom.
- **Commit** after each session with a message saying what moved, in this repo's language. If
  you study on more than one device, pull before you start and push when done.

## Subject rules

> Replace with the rules specific to this subject, or delete this section.

## Processes

- `learn` — the study session entry point; routes to the stage skills below.
- `learn-setup` — once per subject: mission, diagnostic, plan; `add-topic`.
- `learn-sources` — vetted sources in `resources.md` (runs in the background).
- `learn-artifact` — the theory artifact of a subtopic: build, independent fact-check, issue.
- `learn-practice` — check, practice, timed, ticket; the counter.
- `learn-close` — reference sheet, review queue, next subtopic.

## Tools

- `python tools/notes.py check -v` — frontmatter, broken links, stale index. Read-only.
- `python tools/notes.py index` — rebuild `index.md`.
- `python tools/notes.py compact-log --keep 50` — archive old `log.md` entries, then summarise the
  archived block keeping every decision and the current state.
