---
name: learn-artifact
description: Internal stage of the learn framework — start with learn. Build, fact-check and issue the theory artifact of a subtopic — a visual HTML page grounded in resources.md, with inline citations, the shared stylesheet and self-check quiz. The build and the fact-check run as background agents; the next subtopic's artifact is prepared ahead. Called from learn ("learn theory").
disable-model-invocation: true
---

# learn-artifact — the theory artifact

Read [../learn/RULES.md](../learn/RULES.md) first (iron rules; background agents). Modes:
**prepare** (build a draft + fact-check, don't issue), **issue** (hand it to the learner),
**theory session** (the learner self-studies).

## prepare

**Build** — normally a background agent. Inputs: the subtopic M.K, its hub (read-only), the plan
(map, palette, Mission), `resources.md`, earlier artifacts, `artifacts/assets/`.

1. **Gather.** From `resources.md`, open the parts the hub's "Rests on" names; read them for this
   subtopic. A fact no listed source covers → search for one that passes the `learn-sources` bar
   and **report** it (the main session adds it to `resources.md`); if none, leave the point out
   and report a gap.
2. **Items.** Decide the §2 items (one paragraph = one trainable item), narrow and together
   covering the subtopic fully. Fold in every note in the hub's `## Notes for the artifact` that
   has no `→ folded` mark, and list them in the report.
3. **Write** `artifacts/<subject-slug>-<M.K>-<subtopic-slug>.draft.html` per the template below, built from the
   components in `artifacts/assets/` (read them first). Don't edit `assets/`: if a reusable
   component is missing, write it inline and propose it in the report.
4. **Media.** Real images/screenshots first (download into `artifacts/media/`, no hotlinking,
   credit in the caption); draw your own diagram only if no real one exists and label it
   "diagram, not a screenshot". Audio/video: real clips with an embedded player (players have a
   button; no "ready?" questions).
5. **Report** to the main session: the draft's path, the §2 items (for the hub's `## Items`),
   sources to add, gaps, notes folded, components proposed, anything you could not do.

**Then the main session:**
6. Launches the **fact-check** as a separate agent (it did not write the page): "Read
   `.claude/skills/learn-artifact/SKILL.md` › Fact-check and check `<draft path>`". Without
   subagents: a separate pass after the build, and the hub says "self-checked" instead of
   "fact-checked".
7. Fixes every finding (or drops the claim), renames the draft to `.html`, applies the report:
   hub `## Items` + an empty counter with the plan's columns, `→ folded YYYY-MM-DD` on the notes
   used, `resources.md` additions and gaps, the hub line "Artifact: prepared YYYY-MM-DD ·
   fact-checked YYYY-MM-DD", plan status note "artifact prepared". Commit.

## Fact-check (the second agent)

For every non-trivial claim in §1–§2 and every §3 quiz key: open the cited source and confirm it
says that. Check each URL loads; each image is what its caption says; formulas and examples are
correct (run code and compute numbers where possible); nothing in §3 needs knowledge outside §2;
no hints toward §3 answers leak into §2 wording. Report a list:
`location · claim · problem · what the source actually says`. Don't edit the file.

## issue

1. Not prepared → **prepare** now (in the foreground if the learner is waiting).
2. Any note in the hub's `## Notes for the artifact` without `→ folded` → update the page (and
   the items/counter rows if an item is added), mark the note folded.
3. In chat, **2–4 lines**: what it is, how to work (alone, on paper, as many sessions as needed;
   §3 is answered *with* the artifact open — processing, not recall; the quiz marks right/wrong
   only), the **primary source** to read alongside, and the **absolute link** (`file:///` + this
   repo's path on this device) so it opens in one click. Open it with a CLI command if possible.
4. Hub: "issued YYYY-MM-DD", stage `theory`; plan status; log; commit.

## theory session

The learner works alone. When they report, write what they did into the hub's log; no checking,
no comments on their notes. When they say theory is done → `learn-practice check`.

## Artifact template (one for all; only useful content, no organisational info)

A visual HTML page. It links the shared components and keeps everything else inline; only explicit
player embeds may be external. It opens from the repo (the links are relative); for a copy outside
the repo, print it to PDF from the browser.

```html
<link rel="stylesheet" href="assets/learn.css">
<script src="assets/quiz.js" defer></script>
```

Careful typography and a readable grid; **visualise the core of the theory** (diagrams, tables,
timelines where a picture explains better than text); highlight what matters (cards, callouts,
colour accents — not garish); **one piece of information through different channels** from the
subject's palette; **formulas in proper textbook form** (MathML or rendered — the no-LaTeX rule is
for chat only).

**Accuracy (critical).** The artifact is a textbook page: no invented facts. Every non-trivial
fact — especially about an interface, a format or the rules of a task — comes from a source in
`resources.md` and is cited inline. Don't fill in details "as it usually is"; in doubt, check or
don't claim it.

```
<page title> — <subject> · Topic M. <topic> · Subtopic M.K. <subtopic>

## 1. Introduction
2–3 sentences: how it continues the previous subtopics (links to real earlier artifacts — only if
that information really was there, without spelling the connection out) and, very briefly, where
it is used. No forced phrasing, no long "why". A `.primary` callout (its `.label` in the page's
language): the one best thing to read or
watch alongside (from resources.md).

## 2. Core theory
§2.1, §2.2… — a little text per item but deep and clear: explain the topic fully, deep enough that
after §3 the learner feels they own it. Every non-trivial claim carries an inline citation
(`<sup class="cite"><a href="#src-N" aria-label="source N">N</a></sup>`) to its §4 entry, and
that entry links the exact page/section. Text + table/diagram/illustration where it helps +
audio/video when useful. Illustrative examples here (NOT practice tasks — those live in the hub
and chat).

## 3. Questions and exercises
- Self-check questions whose answers are in the artifact (processing, not recall); enough to be
  sure of deep understanding.
- A quiz block (`quiz.js`): multiple choice, options of equal length and form, no formatting
  clues, the correct one in a varying position in the source; the component shuffles them and
  marks right/wrong only — no explanations.
- 1–2 subtle questions toward the learner's own associations (where they already used it, when
  they will recall it, what it really connects to) — never "what does this remind you of", never
  a ready association.
- A couple of extension questions marked * (follow links, search on their own).
- Enough exercises to practise the topic on their own from every side.

## 4. Sources
`<ol class="src">`, each `<li id="src-N">` from resources.md: a working URL to the exact part,
what it is, which part is useful here. Plus a couple of deepening ones marked * — also from
resources.md (add them there first). Tables and diagrams need citations too.
```

**Not in the artifact:** the plan or prerequisites as a block, a long "why/where", instructions on
processing or notes, ready associations, strand items (chat), practice tasks (hub + chat),
procedural instructions (chat).
