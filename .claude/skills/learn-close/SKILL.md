---
name: learn-close
description: Internal stage of the learn framework — start with learn. Close a mastered subtopic — write its printable reference sheet, mark it done, let the next subtopic into the pipeline; at the end of a topic, the learner's topic map from memory. Called from learn when the last counter column is closed ("learn close").
disable-model-invocation: true
---

# learn-close — end of a subtopic's cycle

Read [../learn/RULES.md](../learn/RULES.md) first. Run only when every item is closed in the
**last** column of the hub's counter (a `moved on` subtopic: when its last open item closes).

1. **Reference sheet** → `reference/<subject-slug>-<M.K>-<subtopic-slug>.html`, linked to
   `../artifacts/assets/learn.css`. The compressed essence for quick lookup — the page the learner
   will come back to: the rule table, the formula set, the syntax, the algorithm or flow, the key
   distinctions; one screen, prints on one A4 sheet. Only what the artifact's §2 holds, in the
   same terms, with the same citations. No exercises, no associations, no notes advice. It is
   written **after** mastery on purpose: it doesn't replace the learner's own notes during
   theory. Link it from the hub.
2. **Strand.** If the subject has a strand, make sure every item of this subtopic that the
   strand can hold (a formula, a rule, a term) is in it — closed subtopics are repeated only
   there.
3. **Misconceptions.** Mark resolved ones resolved; an unresolved one goes into the next related
   subtopic's `## Notes for the artifact`.
4. **Status.** Hub and plan: `done`. The place in the pipeline frees: the next `not started`
   subtopic in the plan's order enters at `pretest` (RULES.md › The pipeline). Mark deviations from
   the plan's order.
5. **Topic map** — when this was the last subtopic of topic M: the learner draws or writes, without
   any materials, a map of the topic — its subtopics, their key ideas and how they connect — then
   compares it with the artifacts on their own. The map is theirs: not reviewed, not corrected;
   log that it was done.
6. **Mission check** (one line to the learner, only if relevant): is one of the "success looks
   like" points now reachable? Suggest the Wisdom community from `resources.md` where it can be
   tried for real. If the mission seems to have shifted, propose an update (RULES.md › The
   mission steers).
7. **End of the subject** (nothing left `not started`, `moved on` or `paused`): if it is part of a
   global subject, propose the next part as a new subject repo, carrying the split list with
   "where we are now" updated.
8. End per RULES.md › State.
