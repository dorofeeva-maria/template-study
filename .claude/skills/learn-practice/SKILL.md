---
name: learn-practice
description: Internal stage of the learn framework — start with learn. The working loop of a subtopic — the theory check, leveled practice packs, timed practice and target tickets; reviews without answers; the per-item counter; misconceptions; mistakes routed by subtopic. Called from learn ("learn check", "learn practice", "learn timed", "learn ticket").
disable-model-invocation: true
---

# learn-practice — check, practice, timed, ticket

Read [../learn/RULES.md](../learn/RULES.md) first (review wording, exceptions, stages). The hub is
the source of truth; its layout is in [../learn/formats/hub.md](../learn/formats/hub.md).

## Modes

### `check` — the transition from theory to practice

Set stage `check` when the learner says self-check is done (it may span sessions). Questions on the
**theory itself**, cold (the learner answers without the artifact), covering every §2 item: state
a definition or rule in their own words, explain why it holds, name its conditions and limits,
tell apart what is easily confused, say which rule a given statement rests on. **No exercises** —
nothing to compute, solve, write or build: applying the theory is practice and starts at L1. An
example may appear only as the object of a question about the theory ("is this true, and by
which rule?"), never as something to work out. Two more kinds in every check:
- **One coherent explanation** of the whole subtopic, as to someone hearing of it for the first
  time, without the artifact (text or voice). Where it breaks off or hides behind a term, the
  learner marks the spot themselves; review it per item like any answer.
- **Link questions** (2–3): what this is a special case of, why it is so and not otherwise, how
  it differs from an item of an earlier subtopic (only items already taught). The learner
  builds the link; never suggest it.
It **passes** when every §2 item is answered correctly cold within one batch; `check` does
not touch the counter. Review per RULES.md. If it doesn't pass —
**a different approach**, not the same questions: the learner rereads those §2 items (rereading
is theirs), then new questions that analyse exactly the weak spot from another angle. Repeat until
it passes. Then stage `practice`, level L1.

### `practice` — untimed, by level

- **Never write the bank up front.** Each session, generate a **fresh pack at the current level**
  (~20–30 minutes, one subtopic) from the plan's ladder and the task types of that level, weighted by the counter
  (below). Weave in strand items silently — only items whose idea is in the §2 of this subtopic, an earlier one or a
  finished subtopic. Before handing out, verify every task against §2 (RULES.md).
- Early levels may be training formats (mark "not the target format"); upper levels reach the
  target types. Several task types where they genuinely apply; never force one.
- Log in the hub: tasks given, the item each targets. No repeats across sessions (including the
  artifact's §3 questions).
- Unfinished pack → continue from the same point next time.

### `timed` — after all untimed levels are closed (if the subject has a timer)

The same items under a timer: measure the starting time, then cut it gradually to the target.
Each timer step is its own counter column.

### `ticket` — target level and project

At target levels a task is **a realistic instance of the real work**: a work ticket in a real
repo, a real letter answering a real-looking request, the exam task in its real form.
- **A request, not an instruction:** what is needed and why (value, context) + 2–3 acceptance
  criteria (an observable result). Never dictate the implementation: no file names, signatures,
  names, algorithm or steps.
- **Real size:** a whole piece of functionality, not a mini-snippet. Context may go beyond what
  was covered — the learner works it out from primary sources.
- **Only the §2 items of the ticket's subtopic are assessed** (plus open items of `moved on`
  subtopics it really exercises); the rest is real work — not tested, not penalized.
- Review like a code review limited to verifiable facts: does it build, do tests pass, which
  criteria are not met (by number). No hints on how to fix, no design advice toward untaught
  topics. Check that the ticket really exercised its items.
- Training levels stay narrow exercises within the artifact — the contrast is intended.
- Project tasks (if the subject has one) come after the last level, connecting the subtopic to
  its neighbours; one version.

## Review (every mode)

The learner sends answers **as one batch**. Wording per RULES.md (`N ✓`, `N — §2.K`,
`N — not scored`). Route each problem by where it belongs:
1. **The subtopic of the pack** → the counter (below).
2. **A finished subtopic** (in a ticket) → a line in that hub's log, and the item goes to the
   strand (cards) if the subject has one.
3. **A future subtopic** → `not scored`. Add to that hub's `## Notes for the artifact`: cover this
   in more depth, use this mistake as an example (date + origin).
4. **A `before entry` subtopic or outside the plan** → `not scored`; propose reopening it /
   `add-topic`.

**Misconception?** When a mistake shows a wrong mental model (not a slip) and the learner's own
words make it visible, add a line to the hub's `## Misconceptions`. Mark it resolved when the item
closes.

## The counter

One table in the hub; rows = items (§2.N); columns = L1…Ln, then T1… if timed, plus `Extra` when
an extra pack runs. Cells: `score · last-5 · last ✓ date · last ✗ date`, where last-5 is the
results of the item's last (up to) 5 tasks in that column, oldest first (e.g. `✓✓✗✓✓`).
- Start **2**, status open.
- **Change per pack** for an item: after the pack, take the item's **last 5 tasks** in the column —
  all from this pack if it had 5+ on the item, otherwise reaching back into earlier packs; fewer
  than 5 so far → all there are. **≥80% right → −1**, **<80% right → +1**. One step per pack,
  whatever the number of tasks. So a mistake early on counts in full, and a rare mistake after
  a run of right answers does not hold the item back (it is still written down).
- **≤0 → closed** in that column: no more tasks on it there.
- **≥5 → critical:** reread §2.N + 2–3 check questions (not counted); extra pack on that item
  until **<5**.
- **Share in a regular pack** = the item's score ÷ the sum of scores of the open items in the
  column (an open item never has a share below one task).
- **Next column** when all items of the current one are closed.
- Last column closed → hand over to `learn-close`.

## Moving on with items still open

**Limit per subtopic** (RULES.md › The pipeline; Config, default 4 sessions): when a subtopic
reaches it with items still open, or the learner chooses to leave it (e.g. the target level is
left for real tickets): stage `moved on (open: §2.x…)` in the hub and the plan, with the reason;
its open items go to the strand (cards) if the subject has one; the next `not started` subtopic
enters the pipeline. Later tasks may target those items and count them (RULES.md ›
exceptions). When the last of them closes → `learn-close`.
