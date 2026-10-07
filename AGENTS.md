# Subject

> Replace this heading and the line below with the subject's name, its goal, and the anchor source
> (the course, textbook or official spec the plan is built on). Also state the language notes are
> written in.

One subject, studied with the `learn` framework until each subtopic is automatic.

## How to work here

- **Study sessions follow the `learn` skill** (`.claude/skills/learn/SKILL.md`): plan, theory,
  check, practice, timed practice, project. Read it before any study step.
- **Start from the plan**: `<slug>-plan.md` — its status table shows the current subtopic and
  stage. A fresh repo has no plan yet: run `learn plan`.
- **Write as you go.** Results, counters, decisions and the learner's feedback go into the plan,
  the hub or `log.md` in the same turn, not at the end.
- **Rules the learner adds** while studying this subject (how they want tasks, cards, reviews)
  go into the *Subject rules* section below, one bullet each with the reason.
- **Files:** lowercase ASCII kebab-case; hubs `<M.K>-<slug>.md`; artifacts in `artifacts/`, their
  images in `artifacts/media/`. Large or device-only files (recordings) go into `.gitignore`.
- **Notes** (plan, hubs, strand) start with frontmatter (`title`, `type`, `updated: YYYY-MM-DD`,
  optional `tags`) and a one-line TL;DR.
- **Links** are relative markdown links within this repo: `[text](1.2-some-subtopic.md)`. They
  never leave the repo.
- **`index.md`** is generated: `python tools/notes.py index` after adding or renaming notes.
- **`log.md`**: one line per meaningful session, newest at the bottom.
- **Commit** after each session with a message saying what moved.

## Subject rules

> Replace with the rules specific to this subject, or delete this section.

## Processes

- `learn` — the study framework (`.claude/skills/learn/SKILL.md`).

## Tools

- `python tools/notes.py check -v` — frontmatter, broken links, stale index. Read-only.
- `python tools/notes.py index` — rebuild `index.md`.
- `python tools/notes.py compact-log --keep 50` — archive old `log.md` entries, then summarise the
  archived block keeping every decision and the current state.
