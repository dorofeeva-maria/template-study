---
name: learn-practice
description: The working loop of a subtopic in the learn framework — the theory check, leveled practice packs, timed practice and target tickets; reviews without answers; the per-item counter; misconceptions; mistakes routed by subtopic. Called from learn ("learn check", "learn practice", "learn timed", "learn ticket").
---

# learn-practice — check, practice, timed, ticket

Read [../learn/RULES.md](../learn/RULES.md) and [../learn/formats/hub.md](../learn/formats/hub.md)
first. The hub is the source of truth.

## Modes

### `check` — the transition from theory to practice

Questions and problems on the material, cold (the learner answers without the artifact). Cover
every §2 item. Review: question number + §2.N, nothing else. If it doesn't pass — **a different
approach**, not the same questions: send the learner back to those §2 items (rereading is theirs),
then new questions that analyse exactly the weak spot from another angle. Repeat until it passes.
Then stage `practice`, level L1. Tell `learn` it may prepare the next artifact.

### `practice` — untimed, by level

- **Never write the bank up front.** Each session, generate a **fresh pack at the current level**
  (~one hour), from the plan's ladder and the task types of that level, weighted by the counter:
  an item's share = its score ÷ the sum of open items' scores in the column. Weave strand items in
  silently. Before handing out, verify every task against §2 (RULES.md).
- Early levels may be training formats (mark "not the target format"); upper levels reach the
  target types. Several task types where they genuinely apply; never force one.
- Log in the hub: tasks given, the item each targets. No repeats across sessions.
- Unfinished pack → continue from the same point next time.

### `timed` — after all untimed levels are closed (if the subject has a timer)

The same items under a timer: measure the starting time, then cut it gradually to the target.
Each timer step is its own counter column.

### `ticket` — target level and project

At target levels a task is **a realistic instance of the real work**: a work ticket in a real
repo, a real letter answering a real-looking request, the exam task in its real form.
- **A request, not an instruction:** what is needed and why + 2–3 acceptance criteria (observable).
  Never dictate the implementation (no file names, signatures, steps).
- **Real size;** context may go beyond what was covered — the learner works it out from primary
  sources. **Only the current subtopic's §2 items are assessed**; the rest is not penalized.
- Review like a code review limited to verifiable facts: does it build, do tests pass, which
  criteria are not met (by number). Check the ticket really exercised the current items.
- Project tasks (if the subject has one) come after the last level, connecting the subtopic to
  its neighbours; one version.

## Review (every mode)

The learner sends answers **as one batch**.
- **Correct** — mark it, don't explain.
- **Problem** — task number + §2.N. Then route it:
  1. **Current subtopic** → counter (below). The item's share in the next packs grows with its score.
  2. **A finished subtopic** → an **extra pack on that item only** in its hub: score starts at
     **10** → the learner rereads §2.N + 2–3 check questions + packs on that item until **0**.
     Reset the item's row in `review-queue.md` to step 0. Then back to current practice.
  3. **A future subtopic** → don't review it. Add to that hub's `## Notes for the artifact`: cover
     this in more depth, use this mistake as an example.
  4. **Outside the plan** → propose `add-topic`; don't review it now.
- **Misconception?** When a mistake shows a wrong mental model (not a slip), and the learner's own
  words make it visible, add a line to the hub's `## Misconceptions`. Mark it resolved when the
  item closes.

## The counter

One table in the hub; rows = items (§2.N), columns = L1…Ln, then T1… if timed.
- Start **5**, status open. Mistake **+1**; correct **−1**.
- **At most −1 per item per pack** (a mistake still counts +1 each time). An item cannot close on
  the day it was opened or failed: closing needs correct answers on **two different days**.
- **≤0 → closed** in that column: no more tasks on it there.
- **≥10 → critical:** reread §2.N + 2–3 check questions; extra pack on that item until **<10**.
- **Next column** when all items of the current one are closed.
- Last column closed → hand over to `learn-close`.

## Moving on with items still open

If the learner starts the next subtopic while some items are still open (e.g. the target level is
left for real tickets), record that in the plan, keep those rows, and keep counting them when a
later task really exercises them.
