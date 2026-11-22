# Stage 2, the scope map: the test, set before anything is built or run

**State, 2026-11-22:** the shape is the owner's (decision 22); the
conditions below are proposed with it and nothing is built.

## What it is

The product manager's picture of the whole product, drawn once the
problem is written and kept alive after it: the handful of things a
user does, in the order the user does them, each with one line, and
marked now, next or later. Only the activity marked "now" goes on to
requirements and a slice. It is written to `001_scope-map.md` and
re-read with the user each time a slice is done.

## What the stage must do

1. **Work from the problem document.** Nothing it answers is asked
   again, and nothing outside it is added.
2. **Name what users do, not what is built.** Each line is an
   activity a user would recognise, with one line of what it covers:
   not a technical layer, and no technology or design the problem
   document does not state.
3. **A name and a line, nothing more:** no acceptance criteria, no
   estimates, no dates.
4. **Mark each now, next or later,** with one activity as "now", and
   say that which comes first is the user's to change.
5. **A limit on everything is not an activity.** A constraint of the
   whole problem is stated as holding for every activity, neither
   made into one nor attached to one.
6. **Open stays open.** An open question of the problem document is
   carried as open, not quietly decided by putting something in or
   leaving it out.
7. **A small problem gets a small map:** one activity, said to be
   one, and no map invented around it.
8. **Show it and ask once** whether anything is missing, unwanted or
   in the wrong order: what is in and out is the user's.
9. **Change it when a slice taught otherwise.** Re-read after a
   slice, with what the slice found, it writes the changed map as a
   new document under the next number (`013_scope-map-v002.md`: an
   activity split, joined, added, dropped or moved), keeps the
   earlier one, and says what changed and why; where nothing
   contradicts it, it says the map holds and writes nothing. A
   correction the user makes when first shown the map is made in
   the map itself: nothing has been built on it yet.
10. **Stop there:** no requirements, no slice.

## Two measures, as for the problem stage

**The gate: free checks.** Made-up problem documents in different
fields: a large problem; a small one; a limit on everything; an open
question; a technology the user floats in passing; the user's
correction as a second turn; a slice done that contradicts the map;
a slice done that does not. The checks: the document exists under
its name, the count of activities is in range, the three marks are
used and one is "now", no technology, estimate or criterion is in
it, the whole-problem limit is not an activity, the open question is
still open, the map changes (or does not) on the re-read, nothing
else is written.

**Quality: read, with reasons** (decision 18), against what kad's
`scope-map` writes for the same scenario on the same model, on these
points, fixed before any is read:

- the activities cover the whole problem and nothing beyond it;
- each is something a user does, in the user's order;
- "now" is a sensible place to start, and said to be the user's call;
- the whole-problem limit and the open question are handled as above;
- on a re-read, the change follows from what the slice found;
- short enough to take in at a glance.

kad's skill has no now, next or later and no re-read step, so on
those two points the mark is the condition itself.

## Arms, models, bar, cost

Arms: the bare model (startup and the problem stage as adopted, no
text for this stage); kad's skill; a text of our own, as short as
holds. Models: Haiku 5.5, Sonnet 5.5, Opus 5.5; three runs, then ten
on the text that passes. A model holds when it passes every run of
the gate and its maps read at least as well as kad's. Ceiling: $25,
after a pilot on Haiku whose real cost is reported first.

## The pilot (2026-11-22)

Haiku 5.5, each of the seven scenarios once on the three arms, run
twice: 42 runs, $0.17. For the setup, not the result:

- **Asked "what's next", a session names the scope map and offers to
  draw it;** it does not start. That is startup doing what its table
  says. The scenarios now begin with "Go on to the next stage."
- A check took a file being read for a file being written, and the
  check that keeps the routing table's row numbers from the user
  fired on the map's own rows: both corrected.
- The check on the slice that contradicts the map wanted joining
  moved earlier; a run that folded signing up on the spot into the
  borrowing row is as good an answer, and the check now takes both.
- On the second run our text passed 5 of 7, kad's skill and the bare
  model 0 of 7 (neither marks now, next and later, which nothing
  tells them to). kad's steps on the large problem are parts of a
  system ("member register", "tool catalogue"); our text's rows are
  things a user does.

## What a pass does not show

A map is tested on made-up problems of a page; whether it stays true
over a real product's life is seen only by using it.
