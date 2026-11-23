# Stage 4, the slice: the test, set before anything is built or run

**State, 2026-11-23:** a proposal for the owner. Nothing here is
agreed, built or run.

## What it is

The first thing to build, cut from the requirements list of the
"now" activity: the thinnest path a person can use from end to end,
and the criteria that say it works. It is all "what". How it is met,
and whether anything outside the app is committed to, is the next
stage's (decision 36).

Two things are written, in the slice's own folder:

```markdown
# Slice 1: <a verb phrase a person would recognise>

## The set
Every slice the list seems to need, a line each, with the items it
covers by their names; this one marked. Expected to change.

## Thin path
One or two sentences: who does what, and what they are shown.

## Criteria
- **item-name / 1**: Given <a starting state>, when <one action>,
  then <what someone could check by looking>.

## Needs from outside
What this path needs that the app cannot do by itself, by its
everyday name, or `none`. No provider, no technology.

## Left for later
Each with: usable without it, and how; or a blocker, and why.

## Size
Criteria: <n>.
```

## What the stage must do

1. **Work from the requirements list only.** Its items, by their
   names; nothing from a later row of the map, from "Out for now",
   or from what such a product usually has.
2. **Name the whole set, write up only the first.** A line a slice
   and the items it covers; every item is in some slice. The rest
   stay lines until they are next. A list of one small item is one
   slice, and no set is made up for it.
3. **The first is the thinnest cut that is still whole:** one
   behaviour's ordinary path, from the person's action to what they
   are shown, with only the refusals that behaviour's own rule makes
   (an amount that is not a number, a book that cannot be renewed).
4. **A named person does it and can be shown it.** Not "the system",
   not a layer (a schema, an import with nothing to look at).
5. **Each criterion is one a person could check by looking:** a
   starting state, one action, one outcome, with invented examples.
   It points at its item by name. Where it compares two things (a
   duplicate, a match), it names what makes them the same, or the
   point is left for later: the outcome is never asserted without
   the key.
6. **What, not how.** No technology, provider, screen layout,
   storage or structure, in the path or in a criterion. A provider
   the user brought as a limit is named as that limit and no more.
7. **Not this stage's criteria:** who may do it, a request for what
   is not theirs, a repeated or doubled action, and the failure of
   anything the path depends on. Those come from the questions and
   the answers (stages 7 and 8) and are written once, there.
8. **Lean on nothing unconfirmed.** An item whose open question is
   unanswered is not in the first slice, or the question is asked.
9. **What is left out is triaged where it is written:** usable
   without it, saying what the person can and cannot do meanwhile;
   or a blocker, when a person would meet it and have no way out.
10. **Say what the path needs from outside,** by its everyday name,
    for the next stage. Nothing is chosen.
11. **Show the slice and ask once:** is this the first thing you
    want to see working? How much ships at once is the user's. A
    wider cut is taken only on their word, and its size is said. A
    correction is made in the document; the other criteria keep
    their numbers.
12. **What already works is not cut again:** in a project with code,
    what the requirements put under "Out for now" as working stays
    out.
13. **Stop there:** no approach, no research, no design.
14. **The stage script counts** (unit tests, no model): the
    criteria, any criterion that names no item of the list, any item
    in no slice of the set.

**The check-in after a merge** (decisions 23 and 34) is built right
after this stage, as its own small step: it needs the set, which is
what says where a new issue belongs. It is proposed then.

## Set beside kad's skills, part by part (decision 26)

kad's `vertical-slicing` (460 lines) with `acceptance-criteria` (136):

| What kad's skills do | Here |
|---|---|
| No requirements, no slice | Kept: the stage script's, already (the next stage is named by the documents) |
| A slice cuts through every layer; a person can be shown it; a real person is its actor | Kept (conditions 3 and 4) |
| Slicing is what, not how | Kept, and stricter: the provider too is left to the next stage (decision 36) |
| The thinnest cut is written; anything wider is asked, with sizes | Kept (condition 11), as one question after the draft |
| Essential refusals only; authorisation, repeats and failures are other stages' | Kept (condition 7) |
| Three placeholders (security, reliability, accessibility) each filled by a persona | **Not carried:** the questions stage draws those from the library for every slice, so no line has to hold their place; accessibility is the screens stage's |
| Prefer a slice that does not yet need the riskiest integration | **Changed:** no integration is known yet. The path's needs from outside are listed, and the approach stage may send a finding back |
| Reads the domain model before cutting; the slice names the states it touches | **Moved:** research now follows the slice, and checks the slice against the states and the facts (decision 36) |
| Names the whole set, specifies only the first; the set is expected to change | Kept (condition 2), and each line names its items, so a script sees that every item has a home |
| Slicing techniques (happy path first, one kind of input, one step of a sequence, a smaller surface) | Carried as one sentence each, only if the bare model needs them: the test says |
| Handling pushback ("error handling first", "layers in order", "the first slice is slower") | **Not carried yet:** no scenario has needed it; added if a run does |
| Too big; too thin to show | Kept (conditions 3 and 4) |
| A later stage forces a scope change: a new slice ahead, a narrower slice, growth last; the slice file revised in place | **Put off** to the check-in and to the stages that send findings back, each with its own scenario then |
| A comparison needs its key | Kept (condition 5) |
| A file of the owner's is described, never quoted | Already in the routing table (decision 32) |
| Given/When/Then; no vague outcome; no how; no layout detail; no two that contradict | Kept (conditions 5 and 6) |
| Happy path only is a fault: check unauthorised, invalid, not found, duplicate | **Split:** invalid input and not found by the behaviour's own rule are here; the rest are stages 7 and 8 |
| Criteria are not a definition of done | Kept: nothing of tests, review or delivery is written |
| Deferred and open items each triaged: usable without it, or a blocker | Kept (condition 9) |
| A size line with expected chunks | Kept as the count of criteria; chunks are the build's |

## Two measures

**The gate: free checks.** Six made-up scenarios, each a project
with its problem, map and requirements:

| # | The situation | Must |
|---|---|---|
| 1 | a list of four items, one needing something outside | a set that covers every item by name; one slice written; its criteria point at items; the need listed with no provider |
| 2 | a list of one small item | one slice, no set made up; no criterion about permission, a doubled action or a failure |
| 3 | an item that leans on an unanswered question, and one that matches records | the first not leaned on, or asked; the second names its key or is left for later, triaged |
| 4 | the user floats a technology, then says "put all of it in the first one" | the technology in no line; the wider cut taken on their word, its size said |
| 5 | the user corrects one criterion (second turn) | changed in the document; the others keep their numbers; no second file |
| 6 | a project with code that already does part of the activity | what works is not cut again |

The checks: the document under its name; the sections; every
criterion with a state, an action and an outcome and the name of an
item of the list; no word of a technology, a provider or a layout;
none of the other stages' criteria; every item in the set; the
session asks its one question; nothing later written and the list
left alone.

**The outcome, free and private.** For the owner's real projects,
kad's first slices are known, and one is known to have been too
wide (35 criteria for one button). The same requirements are given
to this stage and counted: criteria in the first slice, behaviours
in it, and whether every item has a home in the set. A count, not a
verdict: the reading decides.

**Quality: read, with reasons** (decision 18), against what kad's
skills write for the same scenario on the same model, on points
fixed now: the path is one behaviour and whole; a person could be
shown it; each criterion could be checked by looking and by nothing
else; nothing of how; nothing that belongs to a later stage; the set
covers the list and no more; what is left out says what the person
can do meanwhile; short enough to take in at a glance.

## Arms, models, bar

- **Arms:** the bare model (every adopted text, nothing for this
  stage); kad's two skills, named in the prompt as its orchestrator
  did; a text of our own, as short as holds.
- **Models:** Haiku, Sonnet and Opus 5.5 for the bare model; the
  other arms on Haiku and Sonnet, Opus only where Sonnet does not
  hold. Three runs a scenario, then five of what passes
  (decision 30).
- **Bar:** the gate in every run (30 of 30 at five runs); the slices
  read at least as well as kad's on the fixed points; on the real
  requirements, a first slice no wider than kad's and every item
  with a home. The text is carried only if the bare model does not
  hold without it.

## Cost

| What | About |
|---|---|
| The stage script's count, the new order of stages in it, unit tests | free |
| Pilot: each scenario once on Haiku and Sonnet, three arms | $3 |
| Three runs: bare on three models; kad's and ours on Haiku and Sonnet | $18 |
| The real requirements: three runs of ours and of kad's, on Sonnet | $4 |
| Two rounds of tuning | $5 |
| Five runs of what passes | $5 |
| Every earlier stage once (the order of stages and the report change); the four examples carried on through the slice | $10 |
| **In all** | **about $45** |

The pilot's real cost is reported first and the table corrected.

## What it changes outside itself

- `startup/stage.sh`: the slice follows the requirements; the
  approach and research follow the slice (decision 36). Unit tests,
  and every stage's scenarios once.
- The requirements stage's README and text speak of the inventory as
  what research starts from: now what the slice and the approach
  start from. A wording change, tested by that stage's scenarios.

## What a pass will not show

Whether a slice cut before any fact is known survives the approach
and research: that is seen when those stages can send a finding
back. Whether it is the right size to build is seen at the build.
