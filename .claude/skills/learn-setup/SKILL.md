---
name: learn-setup
description: Once per subject in the learn framework — interview for the mission, start the background source search, run a cold diagnostic, build the plan (map, task types, ladder, strand, project, timer, palette) with the learner's confirmation; also add-topic. Called from learn ("learn plan", "learn add-topic"), or when the repo has no plan.
---

# learn-setup — mission, sources, diagnostic, plan

Read [../learn/RULES.md](../learn/RULES.md) and [../learn/formats/plan.md](../learn/formats/plan.md)
first. Confirm with the learner **one decision at a time, offering choices** (with the question
tool if there is one), never as one final list. Move on only with a yes.

## 1. Scope

What is the subject? If mastering it would take **more than a year**, it is a **global subject**:
propose a split into smaller subjects in learning order and take the **first** as this repo's
subject. The split list goes into the plan (its only mention).

## 2. Mission

Interview until each part is concrete; push back on vagueness ("learn X" is not a mission):
- **Why** — what changes in the learner's life or work when they have this?
- **Success looks like** — 2–4 things they will be able to do, observable.
- **Constraints** — time per week, deadline (exam date?), devices, preferences.
- **Out of scope** — adjacent things not to chase now.
- **Prior knowledge** — what they already know or have done in this field, how deep; what they
  know they get wrong.

Write the Mission into the plan file right away (the plan may be otherwise empty).

## 3. Sources — in the background

As soon as the mission is written, launch `learn-sources` as a background agent with the subject,
the mission and any sources the learner named. Continue with the learner meanwhile. The map
(step 5) waits for its `## Anchor` and `## Knowledge`.

## 4. Diagnostic (cold, ~20 minutes)

Find the starting point instead of assuming it.
- Draft the topic list from what is already known about the source (or wait for the anchor).
- Give **one batch** of short cold tasks: 1–2 per likely-known topic, from easy to the target
  format, plus 2–3 on the claimed prior knowledge. No hints; the learner may answer "don't know".
- Review per RULES.md: number + what was shown, no answers.
- Write `## Starting point` in the plan: what was done cold (evidence: task + answer quality),
  claims and depth, misconceptions seen (the learner's words).
- A subtopic whose tasks were all solved cold at the target level may be proposed as
  `skipped (diagnostic)` — the learner decides. Skipped subtopics still get a hub (items listed
  from the anchor source) and go into `review-queue.md` at step 0, so warm-ups verify them over
  time. A warm-up mistake on a skipped subtopic reopens it (`not started`).

## 5. The map

A **cumulative sequence of topics and subtopics** grounded in the anchor and the Knowledge
resources — not invented, not from the learner's words alone. Each subtopic narrow but
substantial, with explicit prerequisites, ordered so each stands on the previous. For each: which
part of which resource it rests on; a subtopic no source covers is marked `no source — gap` (and
the gap goes to `resources.md`). The mission decides what is in and what is out of scope.
Starting point decides where the learner enters.

## 6. Parameters — one by one

1. Slug of the subject.
2. Task types — all applicable, and the target ones (target = the real form: the exam task, the
   work ticket, the real letter).
3. Difficulty ladder L1…Ln and the criteria of each; which task types belong to which level.
4. Strand — yes/no, what, how many per study day, order, how repeated (for professional or
   technical subjects: a vocabulary strand of the field's terms in English is recommended).
5. Project — yes/no and what (comes after the last level of each subtopic).
6. Timer — yes/no, start and target.
7. Artifact palette — channels that fit the subject.
8. Warm-up — questions per study day and intervals (defaults in the plan format).

## 7. Write it down

Plan (all sections), one hub per subtopic (format `formats/hub.md`, items left empty until the
artifact exists — except skipped subtopics), `<slug>-strand.md` if any, `review-queue.md`,
`log.md` line. Replace the placeholders in `AGENTS.md` and `README.md` with the subject's real
purpose, anchor source and language. `notes.py index` + `check`, commit.

Then hand back to `learn`: the first subtopic's artifact is built by `learn-artifact` (start it in
the background right after the map is confirmed, so it is ready by the end of setup).

## `add-topic <topic>`

A topic from the Backlog or a mistake outside the plan. Ask `learn-sources` (background) whether
`resources.md` covers it; place it where its prerequisites put it (renumber only subtopics not yet
started; mark the insertion in the plan's notes); create hubs; confirm with the learner; commit.

## Rebuilding a plan

If the learner asks to rebuild: keep the Mission and Starting point unless they change them, keep
hubs with progress (stage past `theory`) as they are, mark removed subtopics in the Backlog with
why. Never delete a hub that has counter history.
