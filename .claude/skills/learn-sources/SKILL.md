---
name: learn-sources
description: Find, verify and curate the vetted sources of this subject in resources.md (knowledge, communities, gaps) for the learn framework. Runs as a background agent — at setup, when a gap touches a subtopic, and as a monthly audit of links. Called from learn or learn-setup.
---

# learn-sources — the vetted sources

Read [../learn/RULES.md](../learn/RULES.md) and
[../learn/formats/resources.md](../learn/formats/resources.md) first.

**Why this exists:** the assistant's memory of a subject is not a source. Everything the learner
is taught comes from what is listed here, and every listed thing was opened and checked.

Usually run as a **background agent**: the prompt names the mode and the inputs (subject,
mission, subtopics, gap). Write only `resources.md`; return a short report (what was added,
removed, which gaps remain). Don't talk to the learner, don't commit.

## Modes

### `build` — at setup, or when `resources.md` does not exist

1. Read the plan's Mission (and, for an older repo, its `## Sources` section and the §4 lists of
   existing artifacts — those are the first candidates, still to be checked).
2. **Anchor first.** Find the official or recognised curriculum the plan should rest on: the
   exam's official spec and practice material, the official docs/tutorial of a technology, a
   standard textbook or a university course with an open syllabus. Prefer one anchor; name a
   second only if the mission needs two halves.
3. **Knowledge.** 5–12 sources that cover the mission: primary first (official docs, specs,
   textbooks, papers, the exam board's own pages), then recognised experts and courses. For each:
   open it, confirm it loads and says what you will claim, note what it covers and which
   subtopics/questions it serves.
4. **Wisdom.** 1–4 communities where the skill is tested for real (well-moderated forums,
   subreddits, Discord/Slack groups with rules, local clubs, mock-interview exchanges, tutors).
   Note moderation and what to use them for. Skip if the learner opted out.
5. **Gaps.** What the mission needs that nothing good covers.
6. Write `resources.md` per the format.

### `gap <subtopic or question>`

Search specifically for the gap; add what passes the bar; leave the gap open (with what was tried)
if nothing does. Report which subtopics can now be grounded.

### `audit` — monthly, or when asked

Open every URL. Dead or moved → fix the link or move the entry to `## Removed`. Re-read the
annotation against the page; prune what turned out shallow, wrong or off-mission. Update the
`checked` dates and the frontmatter `updated`.

## The bar

- Official / primary > recognised textbook or course > named expert with a track record >
  everything else. Popularity is not trust.
- Current: for exams and fast-moving tech, check the version/date (the exam format of this year,
  the library's current major version).
- No paywall-only source as the sole cover of a subtopic, unless the learner already has access.
- Never list a URL you did not open. Never invent a title, author, edition or page number.
