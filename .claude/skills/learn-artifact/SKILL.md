---
name: learn-artifact
description: Internal stage of the learn framework — start with learn. Build, fact-check, pretest, deepen and issue the theory artifact of a subtopic — a visual HTML page grounded in resources.md, with inline citations, the shared stylesheet and self-check quiz. The build and the fact-check run as background agents; artifacts are prepared ahead of the pipeline. Called from learn ("learn pretest", "learn theory").
disable-model-invocation: true
---

# learn-artifact — the theory artifact

Read [../learn/RULES.md](../learn/RULES.md) first (iron rules; the pipeline; background agents).
Modes: **prepare** (build a draft + fact-check, don't issue), **pretest** (cold questions before
reading, then deepen the artifact where they failed), **issue** (hand it to the learner),
**theory session** and **self-check** (the learner works alone).

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
no hints toward §3 answers leak into §2 wording; every formula derived from geometry has its
detailed labelled diagram. Report a list:
`location · claim · problem · what the source actually says`. Don't edit the file.

## pretest

The first stage of a subtopic in work. The artifact is prepared (fact-checked), not yet issued.
1. **Questions.** Cold questions on the theory of every §2 item, of the kind `check` asks (state
   it in your own words, why it holds, tell apart, which rule) — at least one per item, about
   10–15 minutes in all. Built from the prepared page; nothing from it shown. The learner may
   answer "don't know". Stage `pretest`; log the questions in the hub.
2. **Review**: `N ✓` / `N ✗` only (RULES.md). Not scored, no counter.
3. **Deepen** (background agent on the page, then fact-check the changes): for every item with ✗
   or "don't know", explain it much more: every term it uses that no earlier artifact explained is
   introduced and explained where it first appears; a labelled diagram wherever the item has a
   structure, a process, a geometry or a data flow that can be drawn (not text alone); a worked
   example step by step; more channels from the palette. Items answered ✓ stay as they are. No
   hint toward the pretest answers beyond what the explanation itself is.
4. Hub log: `pretest · ✗ on §2.x… · deepened`. Then **issue**.

Give the pretest at the end of a session when you can, so the deepening runs before the next one.

## issue

1. Not prepared → **prepare** now (in the foreground if the learner is waiting); no pretest yet →
   **pretest** first.
2. Any note in the hub's `## Notes for the artifact` without `→ folded` → update the page (and
   the items/counter rows if an item is added), mark the note folded.
3. In chat, **2–4 lines**: what it is, how to work (read alone, on paper, as many sessions as
   needed; §3 is the next stage, self-check), the **primary source** to read alongside, and the **absolute link** (`file:///` + this
   repo's path on this device) so it opens in one click. Open it with a CLI command if possible.
4. Hub: "issued YYYY-MM-DD", stage `theory`; plan status; log; commit.

## theory session

The learner reads alone. When they report, write what they did into the hub's log; no checking,
no comments on their notes. When they say the artifact is read → stage `self-check`.

## self-check

The learner answers §3 (questions, quiz, exercises) on their own, from memory first and looking
into the page only for what they cannot recall; the quiz marks right/wrong only. Nothing is
checked or scored; log what they report. When they say it is done → `learn-practice check`.

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
colour accents — not garish); **one piece of information through as many channels of the
subject's palette as apply to it** (a channel is left out only where it does not apply; channels
follow the content, never a learner "type"); **every term is explained where it first appears**
unless an earlier artifact of this subject explained it (then link there); **formulas in proper textbook form** (MathML or rendered — the no-LaTeX rule is
for chat only). Diagrams are inline SVG drawn with the `learn.css` diagram classes (`.ax`, `.ln`,
`.c1`…, text `.m`, `.a1`…) and never hard-coded colours, so they stay legible in the dark theme.
**A formula derived from geometry** (a cross-section, coordinates of a point, a triangle) gets its
own detailed diagram next to it: every point, radius, angle, axis and segment the formula is built
from is drawn and labelled with the formula's symbols, and the caption walks the derivation step by
step. Words alone are not enough: without the picture the learner has to draw it on paper first.
Set `<html lang="…">` to the page's language: the quiz labels follow it. A subject-specific
interactive widget stays inline in its artifact (or in the module's own files), not in `assets/`.

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
- Self-check questions whose answers are in the artifact; enough to be
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
