# Stage 3, requirements: the test, set before anything is built or run

**State, 2026-11-22:** the conditions, the bar and the ceiling are
agreed by the owner (decision 25). Tested: the text of 63 lines on
Sonnet 5.5 passes 60 of 60 at the gate and as read. The owner has
not yet said whether it holds.

## What it is

What a user needs to be able to do in the activity the scope map
marks "now", written to `002_requirements.md` as a list that is
checked off when work is merged (decision 23). Each item has a box
and a short name of its own; the acceptance criteria and the check-in
point at an item by that name.

It is the user's own list and deliberately light. The requirements
that come from the library of failures and from the state tables are
the questions and answers stages, after research and the slice
(`../../design/planning-phase.md`). What this stage owes them is the
list of outside systems and lasting things that research starts from.

```markdown
# Requirements: <the "now" activity>

- [ ] **short-name**: <Who> can <do what>, in one sentence.

## Out for now
## Limits that apply
## Not yet confirmed
## Outside systems and lasting things
```

## What the stage must do

1. **Work from the problem document and the "now" row only.** Nothing
   they answer is asked again; the other rows give no items.
2. **One line per requirement, with a box and a name:** something a
   named user needs to be able to do, one sentence, written unchecked.
3. **A name is short, unique in the document and never changed or
   reused,** so other documents can point at it.
4. **What, not how:** no technology, design, screen or estimate, no
   Given/When/Then, no thin path.
5. **Nothing invented.** Every item is the user's or follows from
   what they said; nothing such a product usually has.
6. **Out is said as out.** What the documents raise that belongs to
   another row, or that the user excluded, is under "Out for now",
   never in a box.
7. **A limit is given as what it forces here,** or as not applying:
   not quoted, and not a box.
8. **Open stays open.** An open question this activity leans on is
   under "Not yet confirmed" with what its answer would change, and
   is asked once; one it does not touch is left.
9. **An inventory research can start from:** the outside systems and
   lasting things, by their everyday names, or `none`.
10. **Show the list and ask once** what is missing, unwanted or not
    for now (draft first, not kad's questions first: the owner's
    choice). A correction is made in the document, and the other
    items keep their names.
11. **Stop there:** no slice, no criteria, the map not touched.
12. **The stage script counts** (`startup/stage.sh`, unit tests, no
    model): the items, how many are checked, any item with no name
    and any name used twice.

## Two measures, as for the last two stages

**The gate: free checks.** Six made-up scenarios in different fields:
the "now" row of a large problem; a one-row problem; a limit and an
open question the activity leans on; a technology floated and an open
question it does not touch; an outside system and a lasting thing;
the user's correction as a second turn. The checks: the document
under its name; the count of items in range; every item named, no
name twice, no box checked; no word of a solution or a criterion; no
item from another row, from a limit or from an open question; the
limit and the open question kept; the inventory holding what the
problem names; the session asks; the other names unchanged after a
correction; nothing later written and the map left alone.

Nothing tells the bare model or kad's skill to write a box or a name,
so they fail those checks (named `form-...`) by construction. The
gate is reported with and without them.

**Quality: read, with reasons** (decision 18), against what kad's
`requirements-refinement` writes for the same scenario on the same
model, on these points, fixed before any is read:

- every item is the user's; nothing invented;
- together the items cover the "now" activity and nothing beyond it;
- each is one thing a person could say yes or no to of built work:
  not two joined, and not an acceptance criterion;
- a name tells its item apart at a glance;
- a limit is what it forces here; the open question is left open with
  its bearing said;
- the inventory names what research would need and nothing else;
- short enough to take in at a glance.

kad's skill has no boxes and no names: on those the mark is the
condition itself. It also asks before it writes, so its arm's prompt
carries the user's answer to its five questions: "go by the
documents".

## Arms, models, bar, cost

Arms: the bare model (startup and the two earlier stages as adopted,
no text for this stage); kad's skill; a text of our own, as short as
holds (`eval/requirements-skill.md`, 60 lines to begin with, 63 tuned). Models:
Haiku 5.5, Sonnet 5.5, Opus 5.5; three runs a scenario, then ten on
the text that passes. A model holds when it passes every run of the
gate (60 of 60 at ten runs) and its lists read at least as well as
kad's. The text is carried only if the bare model does not hold
without it. Ceiling: $30, after a pilot on Haiku (each scenario once
on the three arms, 18 runs) whose real cost is reported first.

## The pilot (2026-11-22)

Haiku 5.5, each of the six scenarios once on the three arms, kad's
arm three times over: 30 runs, $0.16. For the setup, not the result:

- **kad's skill was not invoked on Haiku when left to its
  description,** as a second turn or as a first. Its arm's prompt now
  names the skill, as kad's orchestrator does, and carries the
  answer to its questions; it is then used in all six.
- Our text passed 6 of 6. The bare model and kad's skill passed
  none, and apart from the box and the name: the bare model asked
  nothing in four of six, kept a floated technology, listed no
  outside system, and on the user's correction rewrote the list
  under names of its own; kad's skill, given a floated technology or
  a correction, asked again and wrote nothing.
- A check on a document that was never written fails with the rest,
  so a run that writes nothing shows many failures for one cause.

## The first full pass (2026-11-22)

Three runs of the six scenarios, 18 runs a cell; passes of the gate,
and in brackets with the box-and-name checks set aside:

| Arm | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| Bare | 2 (2) | 3 (7) | 2 (4) |
| kad's skill (269 lines) | 0 (7) | 0 (4) | not run |
| Our text, first (60 lines) | 17 | 18 | not run |
| Our text, tuned (63 lines) | 13 | 18 | not run |

**The gate.** No model holds bare, with or without the box and the
name: most bare runs ask nothing and list no outside system, and on
Haiku and Opus the floated technology is kept in every run. kad's
skill, given a correction, asked again and wrote nothing in all six
runs. Our first text's one miss on Haiku is real: the floated
technology carried into the document as a question to confirm.

**Read against kad's on Sonnet, on the fixed points** (our 18 lists
in full; four of kad's in full, the rest by length).

- *Every item the user's.* Ours: nearly; on the one-row problem two
  items were made from the reason and the cost ("send in much less
  than the hour", "include the two new staff"), and one list made
  the privacy limit an item ("the secretary can see every child").
  kad's adds nothing to the scope, which it gives as one to three
  bullets restating the map's row.
- *Covers the activity; each one thing to say yes or no to.* Ours:
  two to five items, each from a line of the problem document.
  kad's bullets are the row again and could not be checked off one
  by one. Ours is closer to the condition; kad's was not written to.
- *Limits and the open question.* Both say what a limit forces.
  kad's goes further (the privacy limit means knowing which coach
  has which team) and sometimes into design ("reachable over a
  network"). Both leave the fee question open and say what its
  answer changes.
- *The inventory.* Both name the provider and the lasting thing;
  both sometimes list what is used today (the wall chart, the paper
  ledger).
- *At a glance.* Ours 130 to 220 words, kad's 250 to 620.
- **Where kad's is better:** it writes down the planner's own
  questions, some of them good ("in time": by when?). Ours records
  only the problem document's open questions.

**Tuned on that reading** (60 to 63 lines): a reason, a measure or a
limit gives no item; a floated technology is left out of the whole
document; what is used today is not in the inventory.

## Ten runs of the tuned text (2026-11-22)

| Model | Gate | Cost |
|---|---|---|
| Sonnet 5.5 | 60 of 60 | $4.48 |
| Haiku 5.5 | 53 of 60 | $0.31 |

- **Sonnet, as read** (every item, inventory and open question of
  the sixty tallied by script, the unusual ones read): 60 of 60 meet
  the conditions. Lists run two to five items. No item comes from
  another row, a limit, the cost or the open question; the fee
  question is under "Not yet confirmed" in ten of ten with what its
  answer changes; the inventory is the provider and the season
  ticket in ten of ten, and email in ten of ten. Two things to know:
  three of the ten lists for the one-row problem have an item that
  is a step on the way ("the manager can give the product next
  week's shifts"), which the gate does not see; and names differ
  from run to run (`see-who-has`, `who-has-tool`), which is fine
  within a document and means a list is not regenerated once
  something points at it.
- **Haiku does not hold:** seven failures, among them a reply that
  asks nothing, the open question not asked, a list of one item for
  the season ticket, and a correction made without the text.

**What holds.** The tuned text on Sonnet 5.5. It is carried because
no model holds without it.

**Cost of the stage:** $13.66 of $30 (pilot $0.16; first pass $7.26;
the tuned text $1.45; ten runs $4.79).

**Not re-run:** the startup report now carries the count line when a
requirements document exists; stage 0's scenarios that have one were
not run again with it.

## Set beside kad's skill, and the planner's own questions (2026-11-22)

The owner, on the result: kad's skills worked well at these stages,
so nothing of theirs should be lost unnoticed, and the list should
write down the planner's own questions, which can point at what the
owner had not thought of (decision 26). kad's
`requirements-refinement`, part by part:

| What kad's skill does | Here |
|---|---|
| Asks five questions before writing | Drafts, shows, asks once (decision 25) |
| Asks nothing the documents answer | Kept (condition 1) |
| Each constraint: what it forces here, or why not | Kept (condition 7) |
| A constraint that forces something nobody scoped is a finding, and asked | **Was missing; added** (condition 13) |
| Each open question the unit leans on, with what its answer changes | Kept (condition 8) |
| The planner's own questions under "Not yet confirmed" | **Was missing; added** (condition 13) |
| An answer that skips a question does not answer it; ask again only what was passed over | **Was untested; added** (condition 14, scenario 7) |
| Outside systems and lasting things, names only | Kept (condition 9) |
| No thin path, no criteria, no chunking | Kept (conditions 4 and 11) |
| "Why this, why now", the simplest version that feels like progress, approaches rejected | **Not carried:** the map's "now" holds the priority and the slice stage owns the simplest version; approaches rejected have no home yet |
| A file of the owner's is described, never quoted (`sources.md`, a scan) | **Not carried yet:** a mechanism of its own with a script, wanted by every stage that reads such a file |
| Revise in place until something is built on it, then supersede | **Not carried yet:** belongs with the check-in stage (decisions 21 and 23) |

Added to what the stage must do:

13. **Write down the planner's own questions:** what the documents
    leave unsaid that would add, remove or change an item, and what
    a limit forces that nobody asked for. Only what the user alone
    can answer, never how it is built; each with what its answer
    would change; none settled by an item.
14. **An answer settles only what it speaks to:** a question it
    passes over stays in the document and is asked again.

A seventh scenario (the user answers one question of two) and one
more point for the reading: the planner's questions are ones only
the user can answer and whose answer changes the list, not filler
and not design. The text also takes the scope map's rule that a step
on the way is not an item. It is 72 lines.

## The questions by a walk, not by chance: the test, set before it runs (2026-11-22)

**Why.** The list drives what follows: research starts from its
inventory, the slice and its criteria from its items, and "done" is
every box checked. The later stages deepen what is on the list; they
do not find what is missing from it. So the planner's questions are
the cheap place to find a gap, the owner is willing to answer them
(the cap of three is gone), and the owner asked for a more
deterministic way to arrive at them (decision 27).

**The first three runs with free-form questions** (21 of 21 at the
gate, $1.67): four to six questions a list, most of them the user's
alone to answer and bearing on an item; some filler ("roughly how
many children?") and some on the how ("how is a subscriber told?").
Which questions were raised differed from run to run.

**Three arms**, the text otherwise the same:

- `free` (74 lines): the planner notes what the documents leave
  unsaid, as it comes.
- `kinds` (84 lines): every item is walked against eight kinds of
  gap (who; who else; which, one or several; when; from where; what
  a word covers; putting a mistake right; what comes across from
  today).
- `grid` (89 lines): the same walk, written into the document as a
  table, a row an item and a cell a kind (`said`, `-` or `?`), so a
  script can see that every item was walked.

**The measure, free** (`eval/gaps.py`, unit-tested): 26 gaps over
the four scenarios that draw a list from made-up documents, each
something those documents leave unsaid that would add, remove or
change an item. Eighteen were raised by some free-form run; eight
were found by walking the kinds by hand before any run of the other
two arms, so the measure does not only reward what free-form already
finds. A gap counts as raised when a question under "Not yet
confirmed" speaks to it, by pattern. Ten runs a scenario on Sonnet
5.5: how many of the 260 are raised, and how many gaps are raised in
at least eight runs of ten.

**The bar.** The gate as before, 70 of 70. A heavier arm is carried
over a lighter one only if it raises at least ten points more of the
gaps, or makes at least three more of them reliable (eight runs of
ten), and its questions read no worse: the user's alone to answer,
bearing on an item, no more filler. The patterns are loose, so the
count is a guide and the reading decides a close call.

**Cost.** The owner has dropped the ceiling for this stage (decision
27); the cost is still reported. About $5.50 an arm.

## What a pass does not show

The scenarios are made-up problems of a page and at most two turns.
Whether a list drawn this way stays the right list through research,
a slice and a build is seen only at the check-in stage and in use.
