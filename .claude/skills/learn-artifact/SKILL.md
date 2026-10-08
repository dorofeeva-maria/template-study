---
name: learn-artifact
description: Build, fact-check and issue the theory artifact of a subtopic in the learn framework — a visual HTML page grounded in resources.md, with inline citations, the shared stylesheet and self-check quiz. Building and fact-checking run as background agents; the next subtopic's artifact is prepared ahead. Called from learn ("learn theory").
---

# learn-artifact — the theory artifact

Read [../learn/RULES.md](../learn/RULES.md) first. Three modes: **prepare** (build + fact-check,
don't issue), **issue** (hand it to the learner), **theory session** (the learner self-studies).

## prepare — normally a background agent

Inputs: the subtopic M.K, its hub, the plan (map, palette, Mission), `resources.md`, earlier
artifacts, `artifacts/assets/`.

1. **Gather.** From `resources.md`, open the parts the hub's "Rests on" names; read them for this
   subtopic. Need a fact no listed source covers → search for one; add it only if it passes the bar
   of `learn-sources` (write it into `resources.md`); otherwise leave the point out and add a gap.
2. **Items.** Decide the §2 items (one paragraph = one trainable item), narrow and complete for the
   subtopic. Fold in the hub's `## Notes for the artifact`.
3. **Build** `artifacts/<slug>-<M.K>-<slug>.html` per the template below, from the shared
   components in `artifacts/assets/` (read them first; anything a second artifact could reuse
   goes into `assets/` as a component, not inline).
4. **Media.** Real images/screenshots first (download into `artifacts/media/`, no hotlinking,
   credit in the caption); draw your own diagram only if no real one exists and label it
   "diagram, not a screenshot". Audio/video: embed real clips with a player.
5. **Fact-check by a second, independent agent** (it did not write the page). Its prompt: "Read
   `.claude/skills/learn-artifact/SKILL.md` § Fact-check and check `<path>`." Fix every finding
   or drop the claim. Record `fact-checked YYYY-MM-DD` in the hub.
6. Fill the hub's `## Items` and an empty counter table with the plan's columns. Hub line:
   "Artifact: prepared YYYY-MM-DD". Plan status note "artifact prepared". Don't commit from a
   background agent — the main session commits.

## Fact-check (the second agent)

For every non-trivial claim in §1–§2 and every §3 quiz key: open the cited source and confirm it
says that. Check each URL loads; each image is what its caption says; formulas and examples are
correct (run code and compute numbers where possible); nothing in §3 needs knowledge outside §2.
Report a list: `location · claim · problem · what the source actually says`. Don't edit the file.

## issue

1. If the artifact is not prepared → do **prepare** now (inline, or background while the learner
   waits only if it is long).
2. If the hub got new `## Notes for the artifact` after it was prepared → update the page first.
3. In chat, **2–4 lines**: what it is, how to work (alone, on paper, as many sessions as needed;
   §3 is answered *with* the artifact open — processing, not recall; the quiz marks right/wrong
   only), the **primary source** to read alongside, and the **absolute link**
   (`file:///` + this repo's path on this device) so it opens in one click. Open it with a CLI
   command if possible.
4. Hub: "issued YYYY-MM-DD", stage `theory`; plan status; log; commit.

## theory session

The learner works alone. When they report, write what they did into the hub's log; no checking,
no comments on their notes. When they say theory is done → `learn-practice check`.

## Artifact template

A visual page linked to the shared components:

```html
<link rel="stylesheet" href="assets/learn.css">
<script src="assets/quiz.js" defer></script>
```

Everything else inline; only explicit player embeds may be external. Careful typography and a
readable grid; **visualise the core** (diagrams, tables, timelines where a picture explains
better); **one piece of information through several channels** from the subject's palette;
**formulas in proper textbook form** (MathML or rendered — the no-LaTeX rule is for chat only).

```
<page title> — <subject> · Topic M. <topic> · Subtopic M.K. <subtopic>

## 1. Introduction
2–3 sentences: how it continues the previous subtopics (links to real earlier artifacts — only if
that material really was there) and, very briefly, where it is used. A "Primary source" callout:
the one best thing to read or watch alongside (from resources.md).

## 2. Core theory
§2.1, §2.2… — a little text per item but deep and clear. Every non-trivial claim carries an
inline citation: a superscript link to its §4 entry, and that entry links the exact page/section.
Illustrative examples here (NOT practice tasks — those live in the hub and chat).

## 3. Questions and exercises
- Self-check questions whose answers are in the artifact (processing, not recall).
- A quiz block (component `quiz.js`): multiple choice, options of equal length and form, no
  formatting clues; the component shuffles them and marks right/wrong only — no explanations.
- 1–2 subtle questions toward the learner's own associations (where they already used it, when
  they will need it) — never "what does this remind you of", never a ready association.
- A couple of extension questions marked * (follow links, search).
- Exercises to practise on their own from every side.

## 4. Sources
Each entry from resources.md: a working URL to the exact part, what it is, what it covers here.
Plus a couple of deepening ones marked *.
```

**Not in the artifact:** the plan or prerequisites as a block, a long "why", instructions on notes,
ready associations, strand items, practice tasks, organisational info.
