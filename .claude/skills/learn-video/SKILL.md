---
name: learn-video
description: Internal stage of the learn framework — start with learn. A narrated slide video of a subtopic's theory (lecture) or of a practice pack (each task read aloud, a pause to answer aloud, then the answer), for studying away from the screen. Called from learn ("learn video lecture", "learn video practice").
disable-model-invocation: true
---

# learn-video — lecture and practice videos

Read [../learn/RULES.md](../learn/RULES.md) first. A video is another way to take in what already
exists — the subtopic's artifact or a practice pack — never a new source of content: it adds no
facts, tasks or answers that are not there. Built only on the learner's request.

## What a video is like

- **Slow narration with pauses.** Short sentences; a pause (`P`, 1.5 s) between ideas; numbers,
  formulas and symbols spelled out as words ("H two O", "one point one").
- **Slides to glance at**: a title and at most 4–5 short bullets, or a simple inline SVG diagram
  (like the artifact's) — the learner may be doing something else and looks up now and then.
- **Questions with a pause to answer aloud** (7 s + 3 s per part of the task). In a lecture the
  answer follows, spoken and on the slide; in a practice video it never does (see `practice`).

## Modes

### `lecture` — the theory of the current subtopic

Source: its artifact, in §2 order. Opening slide (subtopic, what comes, how pauses work) → one or
two slides per §2 item → recap slide (`summary`) → 4–8 spoken questions on the theory, each with a
pause and the answer (the kind `check` asks: in your own words, why, tell apart) → closing slide.
It does **not** replace the theory session or `check`: it is a way to read the artifact; `check`
still runs per `learn-practice`.

### `practice` — a pack read aloud

Source: a pack written per `learn-practice` (`practice/<pack>.md`) — the same tasks, in order.
Only tasks that can be solved in the head and answered aloud; a task that needs writing or drawing
is left out and named on the closing slide ("tasks 7 and 9 — on paper"). **No answers in the
video**: each task is read, then the pause, then the next task — reviews never give the answer
(RULES.md), and the pack counts like a written one. The learner dictates or writes the answers
by task number (during the pauses or after); the closing slide says so. Then review them per
`learn-practice` › Review — the counter as for any pack.

## Steps

1. **Voice.** The module's `AGENTS.md` names the video voice (`Video voice: <macOS voice>, rate
   <words/min>`). None yet → `say -v '?'` on the Mac, play two or three samples in the module's
   language (Enhanced / Premium voices sound best; the learner downloads them in System Settings ›
   Accessibility › Spoken Content), let the learner choose, record it in `AGENTS.md`.
2. **Segments file** — `artifacts/media/<subtopic>-video-<lecture|practice>[-<pack>].segments.py`,
   committed (format below). Write the narration for the ear, not a copy of the artifact's text.
3. **Build** (macOS only):
   `python3 .claude/skills/learn-video/build.py <segments file> artifacts/media/<same name>.mp4`.
   Not on a Mac → stop after step 2 and tell the learner the build waits for a Mac.
4. **Check before handing over**: total length is printed (a lecture 10–20 min, a practice pack
   about 1 min per task); open 3–4 frames from `.video-cache/` (the opening, a question with and
   without its answer, the closing) — text fits, nothing cut off.
5. **Hand over**: link the mp4 from the hub (the subtopic's materials) and add a line to `log.md`.
   `.video-cache/` and `*.mp4` go into the module's `.gitignore` unless the learner wants the video
   on other devices (then commit the mp4 if it is under ~50 MB).
6. **After watching** (practice): the learner's answers by number → review per `learn-practice`.

## Segments file

A Python file defining these names; `build.py` reads it.

```python
VOICE = "Milena (Enhanced)"   # from AGENTS.md
RATE = 140                    # words per minute
KICKER = "Chemistry 1.1"       # small caption over slide titles
FOOT = "Chemistry · 1.1 · lecture"   # footer of every slide
ANSWER_WORD = "Answer."       # in the module's language; splits a question's text
THINK_LABEL = "… think and answer aloud"
SUMMARY_LABEL = "Summary"
P = "[[slnc 1500]]"           # `say` pause between ideas

def ans(parts):               # pause to answer aloud
    return f"[[slnc {7000 + 3000 * parts}]]"

S = []
def seg(title, bullets, text, kind="theory", answer=None, svg=None):
    S.append(dict(title=title, bullets=bullets, text=text, kind=kind, answer=answer, svg=svg))

seg("Chemistry · 1.1", ["Substance and body", "Questions at the end"], f"Chemistry, subtopic one point one. {P} …", "title")
seg("What chemistry studies", ["Physics — bodies", "Chemistry — substances"], f"Let's start … {P} …")
seg("Question 1", ["Is ice a substance or a body?"],
    f"Question one. Is ice a substance or a body? {ans(1)} Answer. Ice is a substance; an ice cube is a body.",
    "q", "a substance; an ice cube is a body")
```

Kinds: `title` (opening/closing), `theory` (default), `summary`, `q`. For `q` the slide shows
`bullets[0]` as the question. A lecture question also has `answer` (shown in green) and its text
contains `" " + ANSWER_WORD + " "` once — before it the question with its `ans()` pause, after it
the spoken answer. A practice task has neither: its text is the task and its `ans()` pause. Inline `svg` is drawn to the right of the bullets. After editing a segment, delete
its files in `.video-cache/<name>/` — or rely on the build: it re-renders a slide or a narration
whose text changed.
