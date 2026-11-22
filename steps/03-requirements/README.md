# Stage 3, requirements: the test, set before anything is built or run

**State, 2026-11-22:** the conditions, the bar and the ceiling are
agreed by the owner (decision 25). Nothing has run yet.

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
holds (`eval/requirements-skill.md`, 60 lines to begin with). Models:
Haiku 5.5, Sonnet 5.5, Opus 5.5; three runs a scenario, then ten on
the text that passes. A model holds when it passes every run of the
gate (60 of 60 at ten runs) and its lists read at least as well as
kad's. The text is carried only if the bare model does not hold
without it. Ceiling: $30, after a pilot on Haiku (each scenario once
on the three arms, 18 runs) whose real cost is reported first.

## What a pass does not show

The scenarios are made-up problems of a page and at most two turns.
Whether a list drawn this way stays the right list through research,
a slice and a build is seen only at the check-in stage and in use.
