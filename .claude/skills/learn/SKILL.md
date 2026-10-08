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
| `learn-sources` | setup, gaps, monthly audit — **background** | vetted `resources.md` |
| `learn-artifact` | once per subtopic — **background build + independent fact-check** | theory artifact |
| `learn-practice` | every session | `check` · `practice` · `timed` · `ticket`, counter |
| `learn-close` | once per subtopic | reference sheet, review queue, move on |

Shared files: [RULES.md](RULES.md) (terms and iron rules — read first), `formats/` (plan, hub,
resources, review queue, strand). Skill paths below are relative to `.claude/skills/`.

## Usage

```
learn                     continue: warm-up → strand → the next step of the current subtopic
learn plan                → learn-setup (new subject or rebuild the plan)
learn add-topic <topic>   → learn-setup add-topic
learn theory              → learn-artifact: issue (or prepare) the current subtopic's artifact
learn check | practice | timed | ticket   → learn-practice in that mode
learn close               → learn-close for the current subtopic
learn sources             → learn-sources (background): fill gaps / audit
learn status              one screen: current subtopic, stage, counters, due warm-ups, jobs
```

## Every session

1. **Sync and read.** Pull. Read [RULES.md](RULES.md), the plan, the current hub,
   `review-queue.md`, the tail of `log.md`.
2. **No plan yet** → hand over to `learn-setup` and stop here.
3. **Upgrade an older repo (once).** If the repo predates this version, bring it up before the
   step, telling the learner in one line:
   - no `## Mission` in the plan → a short mission interview (questions from `learn-setup` step 2);
   - no `resources.md` → launch `learn-sources` in the background, seeded with the plan's existing
     sources; meanwhile continue the session;
   - no `review-queue.md` → create it (format in `formats/review-queue.md`) with the items of
     subtopics already `done`;
   - hubs without `## Misconceptions` / `## Notes for the artifact` → add the empty sections when
     the hub is next touched.
4. **Warm-up** (first conversation of a study day, if any row is due). Take the due rows of
   `review-queue.md` (oldest due first, at most the config's count). One cold question per item,
   at the level the item was closed at, in a fresh form (not a task from its log). The learner
   answers in one batch; review per [RULES.md](RULES.md) (number + §2.N only). Update the queue
   (format file). A mistake → the item's extra pack goes first in today's practice. Skip the
   warm-up if the learner says they have no time — the rows stay due.
5. **Strand portion** (first conversation of a study day, if the subject has a strand): the next
   items per [formats/strand.md](formats/strand.md); update the strand file.
6. **Route by the current subtopic's stage** (hub first):
   - `not started` / `theory` → `learn-artifact` (issue the prepared artifact, or build it);
     during theory sessions just confirm what the learner reports and log it — no checking;
   - learner says theory is done → `learn-practice check`;
   - `practice` / `timed` / `project` → `learn-practice` in that mode;
   - last column closed → `learn-close`.
   Read that skill's `SKILL.md` and follow it.
7. **Background jobs** (launch, don't wait — see "Background agents" in RULES.md):
   - the current subtopic passed `check` and the next subtopic has no artifact → `learn-artifact`
     **prepare** for the next subtopic;
   - `resources.md` has a gap touching the current or next subtopic, or was last audited more than
     30 days ago → `learn-sources`.
   When a job finishes: look over what it wrote, note it in the hub/plan, commit. Tell the learner
   in one line only if it changes what they do.
8. **Close the session.** Log line, plan status in sync with the hub, `notes.py index` + `check`,
   commit with a message saying what moved.

## `learn status`

Current subtopic and stage; its counter column (open items with scores); warm-up rows due today
and this week; background jobs running or finished since last time; open gaps in `resources.md`.
No advice — facts only.
