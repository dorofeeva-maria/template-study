---
name: learn-close
description: Close a mastered subtopic in the learn framework — write its printable reference sheet, put its items into the warm-up review queue, mark it done and move to the next subtopic. Called from learn when the last counter column is closed ("learn close").
---

# learn-close — end of a subtopic's cycle

Read [../learn/RULES.md](../learn/RULES.md) first. Run only when every item is closed in the
**last** column of the hub's counter (or the learner decides to move on — see learn-practice,
"Moving on"; then close only the closed items and leave the rest counting).

1. **Reference sheet** → `reference/<slug>-<M.K>-<slug>.html`, linked to
   `../artifacts/assets/learn.css`. The compressed essence for quick lookup — the page the learner
   will come back to: the rule table, the formula set, the syntax, the algorithm or flow, the
   key distinctions; one screen, prints on one A4 sheet. Only what the artifact's §2 holds, in
   the same terms, with the same citations. No exercises, no associations, no notes advice. It
   is written **after** mastery on purpose: it doesn't replace the learner's own notes during
   theory. Link it from the hub.
2. **Review queue.** Add one row per item to `review-queue.md`, step 0 (format
   `../learn/formats/review-queue.md`).
3. **Misconceptions.** Mark resolved ones resolved; an unresolved one stays and is noted in the
   next subtopic's `## Notes for the artifact` if it is related.
4. **Status.** Hub stage `done`; plan status `done`, the next subtopic becomes current (`theory`,
   or `not started` if its artifact isn't prepared). Mark deviations from the plan's order.
5. **Mission check (one line to the learner, only if relevant):** is one of the "success looks
   like" points now reachable? Suggest the Wisdom community from `resources.md` where it can be
   tried for real. If the mission has shifted, propose an update — change it only with a yes.
6. **End of the subject** (last subtopic done): if it is part of a global subject, propose the
   next part as a new subject repo, carrying the split list with "where we are now" updated.
7. Log line, `notes.py index` + `check`, commit.
