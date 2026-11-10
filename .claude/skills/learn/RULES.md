# learn — terms and iron rules

Shared by every `learn-*` skill. Each rule lives here once; the skills point to it. Read this file
before any study step. Where the plan's Config sets something, the plan overrides the defaults in
the skills and formats.

## Terms

- **Subject** — a coherent field with its own goal (an exam section, a branch of physics, a
  programming language). One subject = one plan = this repo. Mastered in **under a year**.
- **Global subject** — something that would take more than a year. Not taken directly: split into
  smaller subjects in learning order, studied one at a time. The order lives **only** in the split
  list quoted in the plan; nothing else in the subject refers to the global subject.
- **Mission** — why the learner studies this subject: the real-world outcome, what success looks
  like, constraints, what is out of scope. The compass for every choice of what to teach next.
- **Topic (M)** — a large section of the subject, numbered within it (1, 2, 3…).
- **Subtopic (M.K)** — the atomic unit of mastery: one narrow theme, taken through the full cycle.
  On request a subtopic is **replaced by several smaller ones**, never nested.
- **Item** — the smallest trainable unit: one paragraph of the artifact's §2 = one row of the
  counter (§2.N).
- **Pack** — as many tasks as the learner does in ~20–30 minutes, all on **one** subtopic. A
  **regular** pack covers the whole subtopic (items weighted by their score); an **extra** pack
  drills one item.
- **Task type** — the form of work (audio recording, problem solving, free text, multiple choice,
  coding, hands-on, report…). A subject has all **applicable** types and a narrower list of
  **target** types.
- **Strand** — what is learned across all topics (vocabulary, terms, formulas — or nothing).
- **Project** — connected tasks continuing each other across subtopics; one version, after the
  last level. Optional.
- **Resources** — `resources.md`: the vetted sources the subject is taught from (Knowledge), the
  communities where the skill is tested for real (Wisdom), and the known gaps.
- **Theory artifact** — the subtopic's study material: a visual HTML page in `artifacts/`.
- **Reference sheet** — the compressed, printable essence of a **closed** subtopic in
  `reference/`; the page the learner comes back to.
- **In work** — the subtopics being studied at the same time (at most the plan's `In work`
  count, default 3), each at its own stage. See › The pipeline.
- **Pretest** — cold questions on a subtopic's artifact before the learner reads it; not scored.
  Shows where the artifact must explain more.
- **Study day** — one calendar day of study, however many conversations it has.

## Stages of a subtopic

One list, used by the plan's status table and the hubs (a repo may write them in its own
language; the meaning is this list):

| Stage | Means | Set by |
|---|---|---|
| `not started` | not in work yet (its artifact may be prepared) | setup |
| `pretest` | in work: pretest given; the artifact is deepened by its result | learn-artifact pretest |
| `theory` | artifact issued; the learner reads it | learn-artifact issue |
| `self-check` | artifact read; the learner answers its §3 (questions, quiz, exercises) | learn-artifact |
| `check` | the theory check is running (may span sessions) | learn-practice |
| `practice` / `timed` / `project` | counter columns in progress | learn-practice |
| `moved on (open: §2.x…)` | the limit was reached with items still open; out of work | learn-practice |
| `paused` | started, deliberately set aside; the plan says why | the learner |
| `done` | every item closed in the last column | learn-close |
| `before entry` | before the entry point set by the setup diagnostic | setup |

The subtopics **in work** are those from `pretest` to the last counter column; `moved on`,
`paused`, `done` and `not started` ones are not.

## The pipeline

Subtopics are studied in parallel, so practice on one never blocks the next.
- **At most `In work` subtopics** (Config, default 3), in the plan's order. A place frees when one
  becomes `done` or `moved on`; the next `not started` subtopic in the plan's order enters at
  `pretest`.
- **A stage opens after the subtopic before it passed it.** Of two subtopics in work, the later
  one may enter a stage (or a counter column) only once the earlier one has finished that stage
  or column. Both may move in the same session (read artifact 1, then artifact 2).
- **The session** walks the next available step of every subtopic in work, **newest subtopic
  first** (pretest, reading), then the older ones; as much as fits, the rest next time. Each pack
  stays on one subtopic; packs of different subtopics alternate across the session and the days.
- **Limit per subtopic** (Config, default 4 sessions): every session in which the subtopic was
  worked on in any way counts, but none counts until its artifact has been read (stage past
  `theory`). Reached with items still open → `moved on`; its open items go to the strand (cards)
  if the subject has one. It is a safety valve, not the normal end.
- **No warm-ups.** Closed subtopics and open items of `moved on` ones are repeated only through
  the strand (cards).

## Iron rules

- **Maximum independence.** The assistant gives material, tasks and structure. The learner reads,
  looks for answers in the material, works things out and **finds their own mistake**. Only steer
  the process.
- **No hints anywhere** — not in tasks, strand items, artifacts or reviews (no "look
  there", no nudges toward the answer). Instead of hints — **good material** to lean on.
- **Never trust your own memory of the subject.** Material comes from the sources in
  `resources.md`; every non-trivial claim in an artifact carries a link to its source. A claim no
  vetted source supports is not made. Gaps are written into `resources.md`, not filled by guessing.
- **Tasks test only what is in the §2 of the subtopic the task is on.** Before handing out any task, write
  down for yourself which §2 items each task needs — every part, including the last step; a task
  that needs anything else is changed or dropped. Where the task can be run (code), run your own
  solution first if you can. Exceptions, and only these: the setup **diagnostic** (no artifact
  exists yet); the **pretest** (before reading); open items of **`moved on`** subtopics,
  which a later task may target and count; tickets, whose untaught context is real work, not
  assessed.
- **Task wording states the goal and the constraints, never the technique.** No phrases pointing
  to the way to solve it ("so that a typo becomes an error", "without nesting it in an `if`", "if
  you can't, explain why", a list of the exact bugs to fix).
- **Reviews never give the answer.** Allowed per task, and nothing else: `N ✓`; `N — §2.K` (a
  problem on that item); `N — not scored` (the answer leaned on something outside that
  §2; no further words); in the diagnostic and the pretest, just `N ✓` / `N ✗`. Facts the learner can
  verify may be added: "the build fails", "test X fails", "acceptance criterion 2 is not met". Not
  the right answer, not why, not which direction to look. Holds for diagnostics, pretests,
  `check`, practice and tickets.
- **Don't explain an untaught concept inline.** If a concept outside the artifact surfaces, move it
  to a future or new subtopic (note in that hub, or `add-topic`); don't explain it in chat.
- **The counter never penalizes what was not taught.** A "mistake" on untaught material is
  cancelled (`not scored`), not counted.
- **Associations and notes are the learner's.** Never say what to put in notes, which connections
  to build or what to associate with. At most 1–2 subtle questions at the end of the artifact.
- **Minimum text, maximum practice.** Long text only in the artifact. Chat = tasks, short
  instructions, short reviews. No lectures, no repeating the topic, no thinking aloud.
- **Theory is self-study.** The assistant does not check notes; understanding is checked only at
  `check`.
- **The learner sets the pace.** A stage takes as many sessions as it takes.
- **The measure is retention and automaticity**, not smoothness in the session. Fluency in the
  moment is not learning; storage over days is. A session that felt hard is not a bad session.
- **Don't inflate mastery.** "Done with an example in front of me" is familiarity, not
  automaticity. Automaticity = reproducing it cold, without hints or example. Counters move only
  by that criterion; one good attempt with an example never closes an item.
- **Explicit cycle, planned up front.** No tasks outside the plan — put them into the plan first.
  The order of subtopics is fixed in the plan; deviations are marked there.
- **A weak foundation is not a gate.** Hands-on work and foundations go in parallel; an unknown
  term stays a "black box" (one line in the hub's log), studied later as a topic.
- **Every pack is full session volume**, even a "finishing" pack for one or two remaining items:
  more tasks on the same items, variations, interleaving with closed items.
- **The learner reads what builds understanding** (papers, textbooks) themselves; technical
  instructions (README, setup) the assistant may digest for them.
- **The mission steers.** When choosing what to add, drop or deepen, trace it to the mission.
  Changing the mission needs the learner's yes.

## State and housekeeping

- All state lives in this repo, so study works on any device. Before any step: pull (the repo may
  be ahead on another device), then reread the plan and the hubs in work.
- **The hub is the source of truth for progress.** If the plan's status table disagrees, say so in
  one line and fix the plan.
- **Write as you go**: results, counters, decisions go into the files in the same turn.
- Dates: check the weekday with a tool before writing one; never guess it.
- New pages have frontmatter `title`, `type`, `updated` (optional `tags`) and a one-line TL;DR. At the end
  of every session: log line, `python tools/notes.py index`, `python tools/notes.py check`, commit
  with a message saying what moved.
- `log.md`: one line per meaningful session —
  `YYYY-MM-DD · <M.K> <stage> · what was done/decided · pages`.

## Background agents

Where the assistant can launch subagents, some work runs in the background. Subagents cannot
launch other subagents, cannot ask the learner, and may be refused tools that need approval (a new
web domain, a download) — then they report what they could not do.
- A background agent writes **only its own new files**: a draft artifact
  `artifacts/<name>.draft.html` and its images in `artifacts/media/`, or `resources.draft.md`.
  It never edits hubs, the plan, `resources.md`, `artifacts/assets/` or anything the main session
  may be editing. Everything else (new sources, hub items, status lines) goes into its **report**,
  and the main session applies it.
- The **main session** launches every agent (including the fact-checker after a build returns),
  reviews the result, renames a draft to its final name only after the fact-check, and commits.
  An unreviewed `.draft.*` file is never issued.
- Without subagents, do the same work inline, in the same order.
