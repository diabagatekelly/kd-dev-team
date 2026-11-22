# Stage 2, the scope map: the test, set before anything is built or run

**State, 2026-11-22:** the drawing of the map is tested, ten runs a
scenario, and the owner has said it holds, on Sonnet 5.5 with the
text of 49 lines (decision 24). The re-read after a slice
(condition 9, second half) has moved to a check-in stage of its own,
built after requirements (decision 23).

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

## The first full pass (2026-11-22)

Three runs of the seven scenarios, 21 runs a cell; passes of the gate:

| Arm | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| Bare | 6 | 6 | 4 |
| kad's skill | 0 | 1 | not run |
| Our text, first | 21 | 19 | not run |
| Our text, tuned | 20 | 20 | not run |

Cost so far, the pilot included: $9.60 of $25.

**The gate.** The bare model and kad's skill fail mostly on what
nothing tells them to do: mark now, next and later, and ask. Their
other failures are real: a map of three to six sections for the
one-activity problem (kad's skill writes no map there and sends the
problem on), the floated technology written in, a changed map
written over the first.

**Read against kad's, on the fixed points.**

- *Covers the problem and nothing beyond.* Ours: four rows for the
  lending problem, each from a line of the problem document. kad's:
  five to seven steps, with a "tool catalogue" and "leaving the paper
  ledger" the problem document does not ask for. Ours is closer.
- *Something a user does, in the user's order.* Ours: "borrow and
  return a tool", "reserve a tool". kad's: "membership", "repairs",
  ordered by what the build needs first. Ours meets the point; kad's
  was not written to.
- *"Now" is sensible and the user's call.* Every map of ours starts
  where the document says it hurts most, says why in the reply, and
  asks. kad's has an order and no start.
- *The limit and the open question.* Both arms keep them out of the
  rows. kad's files the open question under "out of scope", which
  half decides it; ours leaves it open.
- *At a glance.* Ours runs 130 to 190 words, kad's 180 to 290, the
  bare model's 290 to 470.

**Tuned after the first reading** (the text went from 49 to 55
lines): the reason for doing it now was being listed as a limit; rows
were sometimes sorted by mark, not by the user's order; a changed map
now ends with what changed, a line a change. One check wanted the
word "return" and failed "lend and take back a tool": widened.

**What does not hold yet: the re-read after a slice.** Two of the
six tuned runs of the slice that contradicts the map failed, and for
one reason. The map has no way to say an activity is finished: with
slice 1 built, Sonnet marked the row "done in slice 1" on its own,
and Haiku stopped to ask how two rows could both be "now". The
condition as written (one "now", three marks) does not cover a map
after its first slice. That is put to the owner before the ten runs.

## The stage split, and ten runs of the drawing (2026-11-22)

The owner's answer to the re-read (decision 23): whether a slice is
done is decided at a check-in when work is merged, from a checkable
list of requirements, not by the map alone. That cannot be tested
before requirements exist, so this stage is the drawing of the map:
the first five scenarios, and a text of 48 lines without the re-read
paragraph. The stage script no longer sends a planned slice back to
the map.

Ten runs a scenario, 50 a model:

| Model | Gate | Cost |
|---|---|---|
| Haiku 5.5 | 49 of 50 | $0.24 |
| Sonnet 5.5 | 50 of 50 | $3.55 |

- **Haiku's one failure is real:** on the user's correction it edited
  the map without the text and left two rows "now".
- **Sonnet, as read:** 49 of 50. One map for the one-activity problem
  has two rows, the first "gets the rota from the wall chart into the
  system", which is a part of what gets built; the gate allows two
  rows and passed it. The other nine have one row. On the other four
  scenarios every map has rows a user would name, in the user's
  order, one "now" where the document says it hurts most, the limits
  and the open question in their sections, and no Airtable.

**The two-row map, fixed.** A map that splits one activity into a
step of the build and the rest would send a slice on that delivers
nothing the user wanted. The text now says a row ends in something
the user wanted and a step on the way is not a row (49 lines), and
the gate for the one-activity problem is one row exactly. All five
scenarios again, ten runs each:

| Model | Gate | Cost |
|---|---|---|
| Haiku 5.5 | 49 of 50 | $0.24 |
| Sonnet 5.5 | 50 of 50 | $3.55 |

Sonnet, as read: 50 of 50. Every map of the one-activity problem is
one row, sending the rota to the staff; no row on any map is a step
of the build. Haiku's one failure is again the user's correction made
without the text.

Cost of the stage: $17.18 of $25.

## After the end-to-end runs (2026-11-22)

The text is unchanged. With every adopted text loaded, the five
scenarios on Sonnet, three runs each: 15 of 15, $1.12. In the
end-to-end runs each map was drawn from the problem document the
session itself had written, and took the user's change of what comes
first.

## Set beside kad's skill, part by part (2026-11-22, decision 26)

kad's `scope-map` (122 lines):

| What kad's skill does | Here |
|---|---|
| No map for a small problem: straight to slicing | **Different on purpose:** one row, said to be one (decision 22) |
| A step is a name and one line: no criteria, no estimate, no note on order bolted to a line | Kept |
| No technology or approach the problem document does not name | Kept |
| A limit on the whole problem is not a step, and is applied at each step's requirements, not "later" | Kept: "Holds for every activity", and the requirements stage says what each forces |
| A limit is judged by what it protects, not by the step its sentence names | **Was missing; added, differently:** kad's planner decides it is a limit on the whole; here it is kept under the limits as worded and the user is asked which they meant (scenario 06) |
| "Out of scope", where a missing step would otherwise be read as a gap | **Was missing; added:** what the user takes out goes under "Out" (a check in scenario 05) |
| "Sequencing notes": why this order | **Not carried:** the rows keep the user's order and which is "now" is the user's call; the reason is given in the reply |
| Steps are parts of a solution, ordered by the build | **Different on purpose:** rows are what a user does (decision 22) |
| Revise in place until something is built on it, then a new numbered version; revise when a slice proves a boundary wrong, not on a hunch | **Not carried yet:** the check-in stage (decisions 21 and 23) |

The text is 58 lines with the two additions.

## What a pass does not show

A map is tested on made-up problems of a page; whether it stays true
over a real product's life is seen only by using it.
