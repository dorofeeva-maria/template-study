---
name: learn
description: Study this subject with the learn framework — build the plan, then take each subtopic through theory, check, leveled practice, timed practice and project to automaticity. Use for any study session in this repo ("let's study", "continue", "practice", "check me").
---

# learn — a subject-agnostic mastery framework

One subject → a cumulative sequence of subtopics → each subtopic goes through a full mastery
cycle until it is automatic. Maximum independent work by the learner, minimum text from the
assistant. Works across many sessions and devices: all state lives in this repo.

## Usage

```
learn                     continue: find the current subtopic and its stage, take the next step
learn plan                build the subject plan (topics/subtopics, task types, levels, strand, project, timer)
learn theory              produce or reopen the current subtopic's artifact + a short instruction in chat
learn check               the theory check (transition point)
learn practice            a pack of practice at the current level; review the answers sent
learn timed               practice under a timer
learn add-topic <topic>   insert a new topic into the plan where its prerequisites put it
```

Without a subcommand, decide the stage from the plan's status table and take the next sensible
step.

## Glossary

- **Subject** — a coherent field with its own goal (an exam section, a branch of physics, a
  programming language). One subject = one plan = this repo. Mastered in **under a year**.
- **Global subject** — something that would take more than a year. Not taken directly: split into
  smaller subjects in a logical learning order, tracked one at a time. Subjects are not numbered as
  units; the order 1…n lives **only in the global subject's split list**, quoted in the plan. A
  subject is self-contained: inside it (map, config, status, topics) nothing refers to the global
  subject except that list (the parts in order + where we are now).
- **Topic (M)** — a large section of the subject, numbered within the subject (1, 2, 3…).
- **Subtopic (M.K)** — the atomic unit of mastery: one narrow theme, taken through the full cycle.
  On the learner's request a subtopic is **replaced by several smaller subtopics**, never nested.
- **Item** — the smallest trainable unit: one rule / one paragraph / one formula that can be drilled
  in isolation. It is **one paragraph of the artifact's §2** and **one row of the counter table**.
- **Pack** — as many tasks as the learner does in ~40–60 minutes (one session). A **regular** pack
  covers the whole subtopic (items mixed by their score); an **extra** pack drills one item.
- **Task type** — the form of work: audio recording, problem solving, free text, multiple choice,
  coding, hands-on experience, a report… A subject has all **applicable** types and a narrower list
  of **target** types (what we study for).
- **Strand** — what is learned across all topics (vocabulary in languages; terms or formulas
  elsewhere; or nothing).
- **Project** — a line of **connected tasks** continuing each other across subtopics and topics.
  Kept in **one version**, done **after the last difficulty level**. Optional; decided in `plan`.
- **Theory artifact** — the subtopic's study material as a **self-contained visual HTML document**
  (typography, colour, diagrams, tables, embedded images/audio/video where useful), saved as a file
  in this repo, PDF if needed. **Not** a markdown note. One per subtopic, sections §1–§4 (template
  below). Opens in a browser; the subtopic hub links to it.

## Iron rules

- **Maximum independence.** The assistant gives material, tasks and structure. The learner reads,
  looks for answers in the material, works things out and **finds their own mistake**. Only steer
  the process.
- **No hints ANYWHERE** — not in tasks, strand items, the artifact or the review (no "look there",
  no nudges toward the answer). Instead of hints — **good material** to lean on.
- **Tasks test ONLY what is in the artifact's §2.** Never put an item into a pack that the current
  subtopic's theory has not covered. Before handing out a pack, check every task against §2.
- **Don't explain an untaught concept inline.** If a concept outside the artifact surfaces in an
  answer or mistake, do not explain it in chat. Move it to a future or separate subtopic (Backlog /
  `add-topic`), using the mistake as an illustrative example when that topic starts.
- **The counter never penalizes what was not taught.** A "mistake" on material not in the artifact
  is **cancelled** (remove the +1), not counted as a gap.
- **Associations and notes are the learner's.** Never say what to put in notes, which connections
  to build, what to associate with — that is the learner's own elaboration. At most 1–2 subtle
  guiding questions at the end of the artifact so they make the link to their own life.
- **Minimum text, maximum practice.** Long text only in the theory artifact. Practice = tasks and a
  short review. No lectures, no repeating the topic, no thinking aloud.
- **Theory is self-study.** In a theory session: give the artifact + a short instruction **in chat**;
  the learner works alone on paper for the whole session and reports what they did. The assistant
  **does not check** notes or answers — only at the `check` transition point.
- **The learner sets the pace.** A cycle or a stage takes as many sessions as it takes.
- **The measure is retention and automaticity**, not smoothness in the session (fluency is not
  learning).
- **Explicit cycle, planned up front.** No scattered tasks outside the plan — put them into the plan
  first. Keep the hub counters current. The order of units is fixed in the plan; mark deviations.
- **Ground the plan in an established curriculum or official source** (official docs, a recognised
  course, the exam's official domains) — never in guesses. Name the anchor source first; each hub
  states which part of the source it rests on; a topic the source doesn't cover is marked so,
  not improvised.
- **Don't inflate mastery.** "Done with an example in front of me" is familiarity, not
  automaticity. Automaticity = reproducing it cold, without hints or example. Counters move only by
  that criterion; one good attempt with an example never closes an item.
- **A weak foundation is not a gate.** Hands-on work and foundations go in parallel. Unknown terms
  while working stay a "black box": one word into the hub's log, studied later as a topic.
- **Every pack is full session volume**, even a "finishing" pack for one or two remaining items:
  more tasks on the same items, variations, interleaving with closed items.
- **The learner reads what builds understanding** (papers, textbooks) themselves; technical
  instructions (README, setup) the assistant may digest for them.

## State (all in this repo, so it works on any device)

Before any step: the repo may be ahead on another device — pull first; then reread the plan and
the status.

- **Plan** → `<slug>-plan.md`. The map (Topics M → Subtopics M.K, numbered within the subject),
  prerequisites, **applicable and target task types** per subtopic, the **status table** (stage +
  level), the **subject config** (difficulty ladder, strand, project, timer, **artifact format
  palette**), and a **Backlog** (topics to add: mistakes outside the plan, "for later"). If the
  subject is part of a global subject: a separate section with its name, the **numbered list of
  parts** and the **current position**. **Every subtopic links to its hub page.**
- **Subtopic hub** → `<M.K>-<slug>.md`, one per subtopic: status (stage/level), **link to the theory
  artifact**, and the assistant's **working log** — tasks given, examples, the **per-item counter
  table**, which strand items were woven in, progress.
- **Theory artifact** → `artifacts/<slug>-<M.K>-<slug>.html` (or `.pdf`), one per subtopic. Only
  useful theory, no organisational info. Self-contained (inline styles/scripts, no external
  dependencies except explicit audio/video embeds). Linked from the hub.
- **Practice tasks and examples** live in the hub's log and are given **in chat** — never in the
  artifact. The artifact holds only *illustrative* examples.
- **Strand** (if any) → `<slug>-strand.md`: every item given, **in order of issue**, each with when
  it was given and **when it was last woven into a task** (rotate old ones back, lose none).
- **Log** → `log.md`: one line per meaningful session —
  `YYYY-MM-DD · <M.K> <stage> · what was done/decided · pages`.
- New pages (plan, hubs, strand) have frontmatter `title`, `type`, `updated`, `tags`. After adding
  pages run `python tools/notes.py index`; before committing `python tools/notes.py check`.

## The plan (`learn plan`)

Try to determine everything, but **confirm the map and every parameter 2–8 with the learner one by
one, offering choices** (with the assistant's question tool if it has one), not as one final list.
Move on only with a yes on each.

**Scope first.** If mastering it would take **more than a year**, call it a **global subject**:
propose a split into smaller subjects in learning order and take the **first** as this repo's
subject. Record the split list in the plan (the only mention of the global subject). When this
subject is finished, propose the **next** part as a new subject repo, carrying the same list with
"where we are now" updated.

1. The subject's slug.
2. **A cumulative sequence of topics and subtopics** built on real textbooks, curricula or official
   specs — not invented, and not from the learner's guesses (their words are input, not a spec).
   Each subtopic is narrow but substantial, with explicit **prerequisites**, ordered so each stands
   on the previous ones.
3. **Task types** — all applicable, and the **target** ones (see *Task types*).
4. **Difficulty ladder:** number of levels L1…Ln and the criteria of each (along the common axes of
   Stage 3). Fixed here; does not change during the cycle.
5. **Strand** — yes/no and what. For professional or technical subjects a vocabulary strand of the
   field's terms is recommended (cards in English: the subject and English at once).
6. **Project** — applicable or not; if yes, it comes after the last level.
7. **Timer** — does this subject need timed practice.
8. **Artifact format palette** — which channels fit the subject: prose · tables ·
   diagrams/schemes/timelines · images/screenshots · **embedded audio** · **embedded video**
   (including lecture or example clips) · interactive/code. One piece of information through
   **different channels and associations**. Fixed per subject; Stage 1 picks from it per subtopic.
9. **Confirmation** of the map and each parameter 2–8. Only then is the plan approved.

## Strand

What is learned **across all topics** and woven into tasks from time to time. What the items are,
**how many per session**, **in what order** and **how the learner repeats them** (e.g. flashcards
in an app) — all set in `plan` and kept in the subject config.

- **Every session, give the next portion of items in chat** (count from the config); the learner
  copies them. **Format:** each item as **Front** and **Back** on separate lines, ready to paste.
- Language strands: **Front — an example sentence with `______` in place of the target word**,
  **Back — the word, part of speech, meaning**. Never a bare "word — translation". Technical
  strands: Front — the term, Back — an English definition.
- Keep the strand file: every item in order of issue + when last woven in (rotation, nothing lost).
- Order of introduction — by the config's criterion (usually needed/frequent first, hard-but-needed
  not at the very start).
- **Weave items already given into practice and later topics — silently, without emphasis.**
- Topics at the junction of strand and theory (connectors, terms): explain usage in the topic and
  add them to the strand.

## Task types

Depend on subject and goal: audio recording, problem solving, free text, multiple choice, coding,
hands-on, report… A subject has all **applicable** types and a narrower list of **target** ones;
apply to a subtopic only the types that really fit.

Early levels — training / real-life types; upper levels reach the **target** types. Tasks in a
pack **may** be connected (continue each other, e.g. in coding) but need not be. Connection of
packs **across subtopics and topics = the project** (one version, after the last level).

### A target task is a real task, not an exercise

At **target levels** (the upper L, and the project) a task is **a realistic instance of the real
work**: for code — a **work ticket** (as from a client or product owner) in a real project repo;
for writing — a real letter or post answering an incoming request; for any subject — the form the
task takes in life, at work or in the exam.

- **A request, not an instruction.** Say **what is needed and why** (value, context) + **acceptance
  criteria** (an observable result). **Never** dictate the implementation: no file names,
  signatures, names, algorithm or steps.
- **Real size.** A whole piece of functionality the size of a work ticket (2–3 related acceptance
  criteria), not a mini-snippet.
- **Context may go beyond what was covered.** Real work touches untaught things; the learner works
  them out (reading primary sources themselves).
- **Only the studied part is assessed.** Counters move only on applications of **§2 items of the
  current subtopic**; the rest of the ticket is just real work — not tested, not penalized.
- Review a ticket like a code review: build, tests, remarks. Check that the ticket really exercises
  the current subtopic's items.

Training levels stay narrow exercises within the artifact — the contrast is intended.

## The mastery cycle of a subtopic

### Stage 1 — Theory (self-study, any number of sessions)

First session of a subtopic: **generate the artifact** (template below) in `artifacts/`, give a
**short instruction in chat** (what it is, how to work — 2–4 lines, not in the artifact). The
instruction contains the **absolute file link** to the artifact (`file:///` + this repo's path on
the current device), so it opens in a browser in one click. Then the learner works alone: reads,
processes, takes handwritten notes, builds their own connections, and reports what they did — **no
checking of notes**. Every session give the next strand portion in chat.

**§3 questions inside the theory** are answered **using the theory** (looking at the artifact) —
that is processing the material, not cold recall. Say so in the instruction. Cold recall happens
only at Stage 2.

### Stage 2 — Theory check (transition point, `check`)

A separate check by the assistant (not reading the notes): questions and problems on the material.
Review the answers. If it doesn't pass — **a different approach**, not the same questions:
re-explain to the gap, tasks that analyse exactly the weak spot. Repeat until it passes. Only then
practice.

### Stage 3 — Practice without a timer, by difficulty level

- **Where tasks come from.** Never write the whole bank up front. Take the subject's ladder (levels
  L1…Ln + criteria) and which task types belong to which level. Each session **generate a fresh pack
  at the current level** (~one hour), weighted toward items still "open" in the counter. Log tasks
  given, their target item and results in the hub — no repeats, progress visible across devices.
- **Difficulty is subject-agnostic.** Common axes: (a) number of items in play — one in isolation →
  several together; (b) nesting — an item alone → inside a big real task; (c) cognitive level —
  recognise/reproduce → apply → analyse/transfer; (d) novelty — familiar setting → unfamiliar
  context; (e) framing — simplified/training → target format (exam or real life). Higher level =
  more on every axis. Typical growth: one item in isolation in a training type → several items in a
  realistic task → the full target type on unfamiliar material; then the same under a timer.
- Start simple — **not necessarily in the target format**; early levels may use real-life tasks
  (mark "not the target format"). Grow to the hardest target tasks.
- Pack size — see the glossary. No rambling, no repeating the topic. Unfinished — continue from the
  same point next time.
- One topic may use **several task types** where they genuinely apply; never force a type that
  doesn't fit.
- The learner sends answers **as one batch**. Review:
  - **Correct** — just mark it, don't explain why.
  - **Problems** — highlight, do **not** write the theory out; point to the theory item (**§2.N**).
    Then for each problem, the algorithm below.

**For each problem** (branch by which subtopic the mistake belongs to):

1. **The CURRENT subtopic** → the main work. Update the counter; **the share of tasks on this item in
   the next packs grows with its score**. A critical item (score ≥10) — see the counter.
2. **An item of a FINISHED subtopic** → highlight it; run an **extra pack on that item only** in
   its hub: score starts at **10** (critical at once) → reread theory (§2.N) + 2–3 check questions +
   packs on that item only until the score reaches **0**. Then back to current practice.
3. **A FUTURE subtopic** (not studied yet) → don't review or drill it now. Note in that future hub:
   cover this item in its artifact in more depth, and use this mistake as an illustrative example.
4. **Outside the plan entirely** → propose `add-topic` to insert the topic where its prerequisites
   put it; don't review it now.

**The counter** — one table in the hub's log; it also tracks progress through levels.

- **Rows** = the subtopic's items (one §2 paragraph = one item §2.N).
- **Columns** = practice stages in order: one per level **L1…Ln** (no timer), then the **timer steps**
  (T1, T2… to the target) if the subject needs a timer. Each item has its own score and status in
  each column.
- **Start:** score **5**, status **open**.
- **Mistake** → **+1**; **correct** → **−1**.
- **Score ≤0 → closed:** no more tasks on that item in that column.
- **Score ≥10 → critical:** (1) reread theory §2.N + **2–3 check questions**; (2) **extra pack on
  that item only** until the score is **<10**.
- **Share of an item in a regular pack** = its score ÷ the sum of scores of all open items in the
  column.
- **Extra pack (one item)**: when an item is **critical**, or on a **mistake in a finished
  subtopic**.
- **Next column** (level / timer step) — when **all items of the current column are closed**.
- **The subtopic is closed** when all items are closed in the **last column**.

### Stage 4 — Timed practice (if the subject needs it)

All untimed levels closed → the same items **under a timer**: measure the starting time, then cut it
down gradually to the target. **Each timer step is its own counter column** (same mechanics).

### Stage 4.5 — Project (if the subject has one)

Project tasks come **after the last difficulty level** of a subtopic (one version), connecting it to
neighbouring subtopics and topics.

### Stage 5 — End of the cycle

All items closed in the last column → the subtopic is **automatic** (it bounces back, it is used in
real life and in the exam). Mark it done, keep weaving it into future tasks, move to the next one.

## Artifact template (one for all; only useful content, no organisational info)

A **visual self-contained HTML** saved as a file (`.html`), PDF if needed. Not markdown.
Presentation: careful typography and a readable grid; **visualise the core of the theory** —
diagrams, tables, timelines where a picture explains better than text; highlight what matters
(cards, callouts, colour accents — not garish); **multi-format — one piece of information through
different channels**: embedded images/screenshots, **audio and video with an embedded player**.
Players have a button; no need to ask "ready?". **Formulas in proper textbook form** (rendered /
MathML / image); the no-LaTeX rule is only for the console/chat. Everything inline, no external
dependencies (except explicit player embeds); responsive width for reading on a laptop.

**Accuracy (critical).** The artifact is a textbook page: **no invented facts**. Every non-trivial
fact (especially about an interface, format or rules of a task) is **verified against sources** and
cited in §4. Don't fill in interface details "as it usually is". In doubt — check the web or don't
claim it.

**Images.** First look for and embed a **real image from the web** (a screenshot of the task, etc.).
Draw your own diagram **only if no real one exists**, and label it "diagram, not a screenshot".
Download real images into `artifacts/media/` (no blind hotlinking).

Content structure (strict):

```
<page title> — <subject> · Topic M. <topic> · Subtopic M.K. <subtopic>

## 1. Introduction
2–3 sentences: how it continues the previous subtopics (links to real earlier artifacts — only if
that information really was there, without spelling the connection out) and, very briefly, where it
is used. No forced phrasing, no long "why".

## 2. Core theory
Numbered items (§2.1, §2.2…), a little text per item but deep and clear — explain the topic fully.
Multi-format: text + table/diagram/illustration where it helps + audio/video when useful.
Illustrative examples right here (NOT the practice examples — those stay in the hub).
Deep enough that after the questions below the learner feels they own the topic.

## 3. Questions and exercises
- Enough self-check questions — the answers **are in the artifact** (answered using the theory:
  processing, not cold recall); enough to be sure of deep understanding.
- 1–2 subtle questions toward associations: NOT "what does this remind you of", but ones that make
  the learner think where they already used it, when they will recall it, what it really connects to.
- A couple of extension questions marked * — follow links, search on their own.
- Enough exercises to practise the topic on their own from every side.

## 4. Sources
Real textbooks/specs/materials. Each with a **working URL**, not only a title (the link is the point:
the learner checks where it came from), what the source is and **which part** is useful. Plus a
couple of extending/deepening ones marked *.
```

Not in the artifact: place in the plan or prerequisites as a block, a long "why/where" (only 2–3
sentences in §1), instructions on processing or notes, ready-made associations, strand items (they
go to chat), practice examples, procedural instructions (chat).

## Generalisation

The framework is subject-agnostic. Per subject, `plan` fixes: (a) the sources of the plan;
(b) applicable and target task types; (c) number and criteria of levels; (d) whether there is a
strand and what it is; (e) whether there is a project; (f) whether a timer is needed.
