---
name: learn-setup
description: Internal stage of the learn framework — start with learn. Once per subject — interview for the mission, start the background source search, run a cold diagnostic, build the plan (map, task types, ladder, strand, project, timer, palette) with the learner's confirmation; also add-topic. Called from learn ("learn plan", "learn add-topic"), or when the repo has no plan.
disable-model-invocation: true
---

# learn-setup — mission, sources, diagnostic, plan

Read [../learn/RULES.md](../learn/RULES.md) and [../learn/formats/plan.md](../learn/formats/plan.md)
first. Confirm with the learner **one decision at a time, offering choices** (with the question
tool if there is one), never as one final list. Move on only with a yes.

## 1. Scope

What is the subject? If mastering it would take **more than a year**, it is a **global subject**:
propose a split into smaller subjects in learning order and take the **first** as this repo's
subject. The split list goes into the plan (its only mention).

**Slug** — right after the scope: a short kebab-case name of the subject; files are
`<subject-slug>-plan.md`, `<subject-slug>-strand.md`, artifacts
`artifacts/<subject-slug>-<M.K>-<subtopic-slug>.html`.

## 2. Mission

Interview until each part is concrete; push back on vagueness ("learn X" is not a mission):
- **Why** — what changes in the learner's life or work when they have this?
- **Success looks like** — 2–4 things they will be able to do, observable.
- **Constraints** — time per week, deadline (exam date?), devices, preferences, **languages**
  (of chat, notes, artifacts, tasks).
- **Out of scope** — adjacent things not to chase now.
- **Prior knowledge** — what they already know or have done in this field, how deep; what they
  know they get wrong. (Goes into `## Starting point`, not into the Mission.)

Write the Mission (and the prior knowledge into Starting point) into the plan file right away
(the plan may be otherwise empty).

## 3. Sources — in the background

As soon as the mission is written, launch `learn-sources build` as a background agent with the
subject, the mission and any sources the learner named. Continue with the learner meanwhile. The
map (step 5) waits for its report; apply it (`resources.md`) first.

## 4. Diagnostic (cold, ~20 minutes)

Find the starting point instead of assuming it. The diagnostic is the one place where tasks
precede an artifact (RULES.md › exceptions).
- Draft the topic list from the anchor source (wait for the sources report if needed).
- Give **one batch** of short cold tasks: 1–2 per likely-known topic, from easy to the target
  format, plus 2–3 on the claimed prior knowledge. No hints; the learner may answer "don't know".
- Review per RULES.md: `N ✓` / `N ✗`, nothing else.
- Write `## Starting point` in the plan: what was done cold (evidence: task + answer quality),
  claims and depth, misconceptions seen (the learner's words). A misconception or gap that
  belongs to a later subtopic also goes into that hub's `## Notes for the artifact` (once the
  hubs exist, step 7).
- Propose the **entry point**: the first subtopic the learner does not already do cold at the
  target level. Earlier subtopics become `before entry` — no artifact, no counter, no warm-ups.
  The learner decides. A later mistake that lands in a `before entry` subtopic is routed like a
  mistake outside the plan: propose to reopen it as `not started` (insert it before the current
  one or after it, the learner decides).

## 5. The map

A **cumulative sequence of topics and subtopics** grounded in the anchor and the Knowledge
resources — not invented, not from the learner's words alone. Each subtopic narrow but
substantial, with explicit prerequisites, ordered so each stands on the previous. For each: which
part of which resource it rests on; a subtopic no source covers is marked `no source — gap` (and
the gap goes to `resources.md`). The mission decides what is in and what is out of scope.
Starting point decides where the learner enters.

## 6. Parameters — one by one

1. Task types — all applicable, and the target ones (target = the real form: the exam task, the
   work ticket, the real letter).
2. Difficulty ladder L1…Ln and the criteria of each; which task types belong to which level.
   Levels grow along common axes: (a) items in play — one in isolation → several together;
   (b) nesting — an item alone → inside a big real task; (c) cognitive level —
   recognise/reproduce → apply → analyse/transfer; (d) novelty — familiar setting → unfamiliar
   context; (e) framing — simplified/training → target format (exam or real life). Higher level
   = more on every axis. Typical growth: one item in isolation in a training type → several items
   in a realistic task → the full target type on unfamiliar material; then the same under a timer.
   Early levels may be real-life rather than target-format tasks. Fixed here; it does not change
   during the cycle.
3. Strand — yes/no, what, how many per study day, order, how repeated (for professional or
   technical subjects: a vocabulary strand of the field's terms in English is recommended).
4. Project — yes/no and what (comes after the last level of each subtopic).
5. Timer — yes/no, start and target.
6. Artifact palette — channels that fit the subject.
7. Warm-up — questions per study day and intervals (defaults in the plan format).

## 7. Write it down

Plan (all sections; the entry subtopic marked current), one hub per subtopic (format
[../learn/formats/hub.md](../learn/formats/hub.md), items left empty until the artifact exists),
`<subject-slug>-strand.md` if any, an empty `review-queue.md`. Replace the placeholders in `AGENTS.md`
and `README.md` with the subject's real purpose, anchor source and language. End per RULES.md ›
State.

Right after these files are written, launch `learn-artifact prepare` for the entry subtopic in the
background, so it is ready by the end of setup. Then hand back to `learn`.

## `add-topic <topic>`

A topic from the Backlog or a mistake outside the plan. Run `learn-sources gap` (background) to see
whether `resources.md` covers it; place it where its prerequisites put it (renumber only subtopics not yet
started; mark the insertion in the plan's notes); create hubs; confirm with the learner; commit.

## Rebuilding a plan

If the learner asks to rebuild: keep the Mission and Starting point unless they change them, keep
hubs with progress (stage past `theory`) as they are, mark removed subtopics in the Backlog with
why. Never delete a hub that has counter history.
