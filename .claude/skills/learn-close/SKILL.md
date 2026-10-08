---
name: learn-close
description: Internal stage of the learn framework — start with learn. Close a mastered subtopic — write its printable reference sheet, put its items into the warm-up review queue, mark it done and move to the next subtopic. Called from learn when the last counter column is closed ("learn close").
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
2. **Review queue.** Add one row per item to `review-queue.md`, step 0
   ([../learn/formats/review-queue.md](../learn/formats/review-queue.md)).
3. **Misconceptions.** Mark resolved ones resolved; an unresolved one goes into the next related
   subtopic's `## Notes for the artifact`.
4. **Status.** Hub and plan: `done`. If this was the current subtopic, the next one in the plan's
   order that is `not started` becomes current (it stays `not started` until its artifact is
   issued). Mark deviations from the plan's order.
5. **Mission check** (one line to the learner, only if relevant): is one of the "success looks
   like" points now reachable? Suggest the Wisdom community from `resources.md` where it can be
   tried for real. If the mission seems to have shifted, propose an update (RULES.md › The
   mission steers).
6. **End of the subject** (nothing left `not started`, `moved on` or `paused`): if it is part of a
   global subject, propose the next part as a new subject repo, carrying the split list with
   "where we are now" updated.
7. End per RULES.md › State.
