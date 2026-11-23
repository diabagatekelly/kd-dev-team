# Stage 4, the slice: the test, set before anything is built or run

**State, 2026-11-23:** agreed by the owner in this, its second form
(decision 37). The first form was changed on the owner's reading:
follow the principles kad's skill was built on; push back when a
slice is made wider; cut the whole set and recommend where to start;
and the check-in after a merge is this stage's, set included.
Criteria only for the slice being worked on.

**Tested (2026-11-23):** the text of 150 lines in
`eval/slice-skill.md` passes every case on Sonnet 5.5 in its last
five runs; no model holds without it; on the owner's three real
lists no first slice is wider than kad's and every item has a home.
The result is below the agreed test, from "Built" on. **Whether the
stage holds is the owner's to say.** It cost $82 against the $70
agreed: the end-to-end examples came to $34, not the $10 guessed.

## What it is

The expert on what to build first. From the requirements list of the
"now" activity it cuts **the set**: every slice that list needs, each
thin and whole, with what each builds on. It recommends where to
start; the user chooses; the chosen slice gets its criteria. It is
all "what": how a slice is met, and whether anything outside the app
is committed to, is the next stage's (decision 36).

It comes back **after every merge**, and whenever work on a slice
turns up something that changes the "what": it checks off what was
built, says where each new issue belongs, and says whether the list
and the set still hold, proposing a new set when they do not.

Two documents:

```markdown
# Slices: <the "now" activity>

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | <a verb phrase a person would recognise> | name, name | nothing | built / chosen / open |

## Where to start
Which can be started now, which is recommended and why.

## What changed
A line a change, with its reason (from the second version on).
```

```markdown
# Slice 2: <the verb phrase>

## Thin path
One or two sentences: who does what, and what they are shown.

## Criteria
- **item-name / 1**: Given <a starting state>, when <one action>,
  then <what someone could check by looking>.

## Needs from outside
What this path needs that the app cannot do by itself, by its
everyday name, or `none`. No provider, no technology.

## Left for later
Each with the slice of the set that takes it, and: usable without
it, and how; or a blocker, and why.

## Size
Criteria: <n>.
```

## The principles, from kad's synthesis

kad's skill was built from a table of principles drawn from three
sources (`.synthesis/product-slicer.md` in kad's repository). All of
them are carried, as the stage's own judgment:

- a slice cuts through every layer and is not a task list;
- too big (the whole feature at once) and too thin to show are both
  faults;
- the actor is a real person, not "the system" or "a developer";
- the ways to find a thin cut: the ordinary path first; one kind of
  input at a time; one step of a sequence usable by itself; the same
  capability over a smaller surface; targets of speed and the like
  later;
- handling errors is tiered across slices, not all or nothing:
  the essential ones with the first slice, the common ones next,
  the rare ones later;
- shared groundwork is not a slice: it rides with the first slice
  that needs it, sized to that slice;
- a slice's size is relative to who builds it, not an absolute
  smallest;
- criteria are Given/When/Then, judged by whether they can be
  tested, not by the keywords; they say what, not how; no layout
  detail; none contradicts another; not the ordinary path alone;
- criteria are not a definition of done;
- the answers to pushback ("error handling first", "the layers must
  be built in order", "the first slice takes longer").

One of kad's resolutions changes place, not substance: the need for
a security, reliability and accessibility review of whatever a slice
ships. kad held it with three placeholder lines; here the questions
stage draws those for every slice from the library, so nothing can
ship without them and no line has to hold their place.

## What the stage must do

**Cutting**

1. **Work from the requirements list only.** Its items, by their
   names; nothing from a later row of the map, from "Out for now",
   or from what such a product usually has.
2. **Cut the whole set.** Every slice the list needs, a row each: a
   verb phrase, the items it covers, and what it builds on. Every
   item is in some slice. A list of one small item is one slice, and
   no set is made up for it.
3. **Each slice is thin and whole,** by the principles above: one
   behaviour from the person's action to what they are shown, with
   only the refusals that behaviour's own rule makes.
4. **Say the order that is forced and the order that is free:**
   which slices can be started now, which must wait for which, and
   which one it recommends first, with the reason.
5. **The user chooses where to start;** only the chosen slice gets
   its criteria. The others stay rows until they are next: building
   one changes what the rest should be.
6. **Each criterion is one a person could check by looking:** a
   starting state, one action, one outcome, with invented examples,
   pointing at its item by name. A comparison (a duplicate, a match)
   names what makes two things the same, or is left for later.
7. **What, not how.** No technology, provider, layout, storage or
   structure. A provider the user brought as a limit is named as
   that limit and no more.
8. **Not this stage's criteria:** who may do it, a request for what
   is not theirs, a doubled action, the failure of anything the path
   depends on. Those are written once, by the questions and answers.
9. **Lean on nothing unconfirmed.** A slice whose item has an open
   question cannot be started until it is answered, and the set says
   so.
10. **What a slice leaves out is triaged where it is written,** with
    the slice that takes it: usable without it, or a blocker.
11. **Say what the chosen path needs from outside,** by its everyday
    name, for the next stage. Nothing is chosen.

**Holding the line**

12. **Push back when the user widens a slice, joins two or wants
    groundwork first.** Say what the wider cut costs (what is shown
    later, what is built before anything is learned) and what the
    thin one gives, and offer the thin cut again. Once. If the user
    still wants it, it is theirs: the set is changed, the size is
    said and the reason recorded in the user's words.
13. **Agree when the user is right:** a slice too thin to show, or
    two that cannot be told apart by a person, are joined without
    argument.

**Coming back: after a merge, or when work changes the "what"**

14. **Happen when due, by the script:** a merged pull request names
    criteria or items not yet checked off, an open issue has not
    been placed, or the user says work has turned something up.
15. **Check off only what merged work names:** the slice as built,
    and each item of the list whose slices are all built. Never on
    say-so.
16. **Place every new issue without asking:** in the slice in hand,
    in a later slice of the set, in a later row of the map, or in
    none. Each with its reason, recorded. Only an issue no row
    covers is put to the user: in or out.
17. **Say whether the list still holds.** A change to it is named
    for the requirements stage, where the user confirms it; this
    stage adds no item.
18. **Say whether the set still holds,** and when it does not,
    propose the new set: slices split, joined, added, dropped or
    reordered, each change with its reason, the built ones left as
    they are. The user agrees before it replaces the old one.
19. **Recommend what to start next,** as at the first cut. When
    every slice is built and every box checked, say the activity is
    done and ask which row of the map is the next "now".
20. **A changed set is a new numbered version** once a slice has
    been built from the old one (decision 21); before that it is
    corrected in place.

**Always**

21. **Stop there:** no approach, no research, no design; nothing on
    the tracker closed, labelled or begun.
22. **The stage script counts** (unit tests, no model): the slices
    and their states; any item in no slice; any criterion that names
    no item; whether a coming-back is due.

## Set beside kad's skills, part by part (decision 26)

kad's `vertical-slicing` (460 lines) with `acceptance-criteria` (136):

| What kad's skills do | Here |
|---|---|
| No requirements, no slice | Kept: the stage script's, already (the next stage is named by the documents) |
| A slice cuts through every layer; a person can be shown it; a real person is its actor | Kept (conditions 3 and 4) |
| Slicing is what, not how | Kept, and stricter: the provider too is left to the next stage (decision 36) |
| The thinnest cut is written; anything wider is asked, with sizes | **Stronger:** the stage pushes back on a wider cut, once, with what it costs (condition 12) |
| Essential refusals only; authorisation, repeats and failures are other stages' | Kept (condition 8) |
| Three placeholders (security, reliability, accessibility) each filled by a persona | **Not carried:** the questions stage draws those from the library for every slice, so no line has to hold their place; accessibility is the screens stage's |
| Prefer a slice that does not yet need the riskiest integration | **Changed:** no integration is known yet. The path's needs from outside are listed, and the approach stage may send a finding back |
| Reads the domain model before cutting; the slice names the states it touches | **Moved:** research now follows the slice, and checks the slice against the states and the facts (decision 36) |
| Names the whole set, a line each, specifies only the first, which the skill picks; the set is expected to change | **Changed** (the owner): each row also says what it builds on; the stage recommends a start and the user chooses; the set has its own document, and coming back to it after a merge is this stage's (conditions 2, 4, 5, 18) |
| Slicing techniques (happy path first, one kind of input, one step of a sequence, a smaller surface, targets later) | Kept (the principles) |
| Handling pushback ("error handling first", "layers in order", "the first slice is slower"); errors tiered across slices; groundwork rides with the first slice that needs it | Kept (the principles, condition 12), with a scenario |
| Too big; too thin to show | Kept (conditions 3 and 4) |
| A later stage forces a scope change: a new slice ahead, a narrower slice, growth last; the slice file revised in place | Kept in the coming-back (condition 18): a new slice before growth. Findings sent back by later stages get their scenarios when those stages exist |
| A comparison needs its key | Kept (condition 6) |
| A file of the owner's is described, never quoted | Already in the routing table (decision 32) |
| Given/When/Then; no vague outcome; no how; no layout detail; no two that contradict | Kept (conditions 6 and 7) |
| Happy path only is a fault: check unauthorised, invalid, not found, duplicate | **Split:** invalid input and not found by the behaviour's own rule are here; the rest are stages 7 and 8 |
| Criteria are not a definition of done | Kept: nothing of tests, review or delivery is written |
| Deferred and open items each triaged: usable without it, or a blocker | Kept (condition 10) |
| A size line with expected chunks | Kept as the count of criteria; chunks are the build's |
| After a slice is built: stop, never offer the next; whether it is built is the user's word; only Critical and High issues are routed | **Different on purpose** (decisions 22, 23, 34): by script from what merged work names; every issue placed; the next slice recommended |

## Two measures

**The gate: free checks.** Ten made-up scenarios, each a project
with its problem, map and requirements; the last four also have
slices, a tracker's answer and merged work:

| # | The situation | Must |
|---|---|---|
| 1 | a list of four items, one needing something outside | a set covering every item; what each slice builds on; a start recommended and the choice asked; no criteria yet |
| 2 | (second turn) the user chooses | that slice written: criteria pointing at items, none of the later stages'; the need from outside listed with no provider |
| 3 | a list of one small item | one slice, no set made up |
| 4 | an item leaning on an unanswered question, and one that matches records | the first cannot be started, and said; the second names its key or is left for later, triaged |
| 5 | the user says "put all of it in the first one", and floats a technology | pushes back once with the cost; the technology in no line |
| 6 | (second turn) the user insists; in another, says "error handling first" | the wider cut taken, its size and their reason recorded; errors tiered, not all first |
| 7 | a merge names the criteria of one slice; no issue | checked off; the set holds and is not rewritten; the next slice recommended |
| 8 | a merge, and three issues: one of the slice in hand, one of a later slice, one no row covers | each placed with its reason, nothing asked for the first two; in or out asked for the third |
| 9 | the user, mid-slice: work has shown two slices are one, and an item was wrong | a new set proposed with what changed, built slices untouched; the item's change named for the requirements stage, not made |
| 10 | the last slice merged; and one where nothing is due | the activity said to be done and the next "now" asked; in the other, no check-in |

The checks: the documents under their names; the set's columns;
every item in the set; criteria with a state, an action, an outcome
and an item's name; no word of a technology, a provider or a layout;
none of the other stages' criteria; the one question asked and none
that is not the user's; which boxes and slices are checked off; the
earlier set unchanged when a new version is written; the tracker's
tool never used to change anything; nothing later written.

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
- **Bar:** the gate in every run (50 of 50 at five runs); the slices
  read at least as well as kad's on the fixed points; on the real
  requirements, a first slice no wider than kad's and every item
  with a home. The text is carried only if the bare model does not
  hold without it.

## Cost

| What | About |
|---|---|
| The stage script (the new order of stages, the counts, when a coming-back is due), the tracker script reading merged work; unit tests | free |
| Pilot: each scenario once on Haiku and Sonnet, three arms | $5 |
| Three runs: bare on three models; kad's and ours on Haiku and Sonnet | $30 |
| The real requirements: three runs of ours and of kad's, on Sonnet | $4 |
| Two rounds of tuning | $8 |
| Five runs of what passes | $9 |
| Every earlier stage once (the order of stages and the report change); the four examples carried on through a set, a chosen slice and one merge | $14 |
| **In all** | **about $70** |

The pilot's real cost is reported first and the table corrected.
kad's arm is run on the cutting scenarios only: it had nothing for
the coming-back.

## What it changes outside itself

- The parked proposal in `steps/check-in/` is replaced by the
  coming-back here; its comparison with kad stays as the record.
- A merged pull request names what it completes (`Completes:`
  and the criteria or items): writing that line is the delivery
  stage's, later; until then the scenarios make it up.
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

## Built (2026-11-23)

**The scripts** (`startup/`, unit tests first: 157 for the folder, on
three systems).

- `stage.sh` takes the new order (decision 36): problem, scope map,
  requirements, the set of slices, the chosen slice, approach,
  research, and on. It names both documents of this stage at once:
  the set (`003_slices.md`), and where the chosen slice's own will
  go (`slice-NNN/004_slice.md`, NNN the slice's number in the set).
- It counts the set: slices by state, a requirement in no slice, an
  item the list does not hold, a state it does not know, two slices
  chosen at once, the chosen slice's criteria and any that names no
  item. It says how a changed set is written: corrected in place
  until a slice is built from it, a new numbered version after.
- It says when a coming-back is due and exactly what to do: mark a
  slice built when merged work names every criterion of its
  document; check a box when every slice of its item is built (or
  merged work names the item outright); and the open issues that no
  version of the set has placed. Merged work that names part of a
  slice, or a criterion no document holds, is said and nothing is
  due for it. When what is due finishes the list, it says the
  activity is done. A set it cannot read is refused, not passed
  over.
- `tracker.sh` reads the latest fifty merged pull requests and the
  line of each that says what it completes (`Completes: slice 2:
  item / 1, item / 2`), and gives them and the open issues to the
  stage script.

**Every earlier stage once with the new scripts** (Sonnet, every
adopted text loaded): startup 21 of 21, the problem 8 of 8, the
scope map 6 of 6, the requirements 12 of 12; $3.07. Three of
startup's scenarios changed with the order: after the requirements
the slice is named, never research (09, 14), and the stage that is
not built is the slice (21) until this text is adopted. The
requirements text says the slice and the approach start from its
inventory, not research.

**The cases.** The ten rows are fourteen cases
(`eval/make_cases.py`): rows 4, 6, 9 and 10 hold two situations
each, and a proposal and the yes to it are two turns. The bar is
every case in every run (70 of 70 at five runs). Each check was
graded for nothing on a document written by hand, a good one and a
faulty one, before any run (`eval/test_cases.py`). Checks named
`form-...` are on what nothing tells the bare model or kad's skills
to write (the table and its columns, a criterion's name, the
headings); every count is given with and without them
(`e2e/tally.py`).

## The pilot (2026-11-23): $3.69

Each case once on Haiku and Sonnet for the three arms, kad's on the
eight cutting cases: 72 runs. For the setup, not the result.

| Arm | Haiku 5.5 | Sonnet 5.5 |
|---|---|---|
| Bare | 1 of 14 (2 but for form), $0.08 | 5 of 14 (8), $1.06 |
| kad's two skills | 0 of 8 (1), $0.08 | 1 of 8 (3), $1.25 |
| Our text, first form (141 lines) | 8 of 14 (8), $0.08 | 9 of 14 (9), $1.15 |

A run costs about half a cent on Haiku and $0.08 on Sonnet ($0.16
with kad's two skills, which are six hundred lines).

**What it met, and what each became** (decision 29):

| Met | Now |
|---|---|
| Asked "what's next" after a merge, a session named the coming-back and waited for the word, as it does for any stage; the three cases that expect the check-off failed on every arm but one | those cases say "Go on to the next stage."; the case where nothing is due still asks "what's next" |
| "I need your yes first" has no question mark, and was failed as not asking | the check takes a request for the yes; a unit test with those words |
| "1 of 4 is checked off", said of the list, was failed as checking something off | the check is on what the session did; a unit test with those words |
| A pattern that counted rows could be matched in so many ways that a short document took minutes to fail (found by the unit test, before any run) | rows are counted by where they start; the test runs in seconds |
| One transcript held a line whose message is plain text, and grading it again stopped there | `e2e/regrade.py` and `e2e/run.py` pass over it: two unit tests |
| A fault in reading the set left the stage script's report silent and wrong (found while it was written) | the script refuses: a unit test |
| A second command in the VM stopped it, and a pass started in the background inside it was lost (no cost) | the pass is kept attached to the command that starts it; written in the runbook |

Graded again with the corrected checks, for nothing: our text on
Sonnet passes 11 of 14; the three left are the cases that asked
"what's next". Bare on Sonnet gives way at once when the user asks
for everything in one slice (the set rewritten, the floated tool
written into it) and writes a new set before the user has agreed to
it. kad's skills write the first slice with the set, unasked, and
on the wider cut change the set without saying what it costs.

## Cost, corrected from the pilot

| What | First guess | Now |
|---|---|---|
| Pilot | $5 | $3.69, spent |
| Three runs: bare on three models; kad's and ours on Haiku and Sonnet | $30 | $17: three passes, the dearest (bare, with Opus) about $9.50 |
| The real requirements: three lists, three runs of ours and of kad's, on Sonnet | $4 | $5 |
| Two rounds of tuning | $8 | $5 |
| Five runs of what passes | $9 | $6 |
| Every earlier stage once with the new scripts | $14 with the examples | $3.07, spent |
| Every earlier stage once more with the text loaded; the four examples carried on through a set, a chosen slice and one merge | | $13 |
| **In all** | **about $70** | **about $53** |

No one pass is over $15.

## The first full pass (2026-11-23): $18.73

Three runs a case, 42 runs a cell (kad's on the eight cutting
cases, 24); runs that pass every check, and in brackets with the
checks of form set aside:

| Arm | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| Bare | 6 (11) | 9 (18) | 8 (18) |
| kad's two skills (596 lines) | 0 (3) of 24 | 3 (9) of 24 | not run |
| Our text, first form (141 lines) | 34 (34) | 39 (39), 42 as read | not run |

**No model holds bare**, form aside. On Sonnet and on Opus, in
every run of three: asked for everything in one slice, the set is
rewritten at once and the floated tool written into it, with no
word of what that costs; a rule that compares records is asserted
with no word of what makes two the same; criteria are prose with no
starting state; told that two slices are one, a new set is written
before the user has agreed, and the item changed in the list. Opus
wrote the set again as a new document after a merge in 7 runs of
9.

**kad's skills fail the gate by what they were built to do:** the
first slice is written with the set, before any choice (their own
rule), and what a slice needs from outside is not listed. Asked
for a wider cut, they do push back.

**Our text's three failures on Sonnet were one check:** the issue no
row covers was left out of the set until the user answered in or
out, which is right, and the check wanted it recorded. Corrected,
with a unit test, and graded again for nothing: 42 of 42.

## Read against kad's on Sonnet, on the fixed points

Our 42 documents and kad's 24, counted by script and a third of
each read in full.

- **One behaviour, whole, that a person could be shown.** Both.
  For the rota, kad's first slice and ours are the same cut (one
  person's shifts entered and emailed to them).
- **Each criterion checkable by looking.** Both write a state, an
  action and an outcome with invented values. Ours name the item
  each belongs to, which kad's do not.
- **Nothing of how; nothing of a later stage.** Both leave out who
  may do it, a doubled action and a failed delivery, and say so
  under what is left for later. kad's holds three placeholder
  lines; ours does not need them (decision 37).
- **The set covers the list and no more.** Ours: every item in a
  row in every run, by script. kad's set is a numbered list inside
  the slice with no items against it, so whether it covers the
  list cannot be checked by script.
- **What is left out says what the person can do meanwhile.** Both,
  in the same two sentences. kad's are longer and sometimes find a
  real gap (a shift that runs past midnight).
- **At a glance.** Ours: a set of 140 to 200 words and a slice of
  250 to 420. kad's: one document of 400 to 720.
- **Width.** In the first pass ours was wider than kad's: 6 to 7
  criteria for the rota's first slice against 4 to 5, with a
  refusal for every field left empty. Tuned (below), ours is 5.
- **Where kad's was better, and what was taken from it:** asked for
  a wider cut it puts the two cuts side by side with their sizes.
  Ours said the cost in words. The text now gives the size of each
  cut, with a check. kad's also flags a decision it made for the
  user to look at ("the full name is the key"); ours leaves such a
  rule for later as a blocker, which is condition 6 as agreed.

## Tuning, and five runs (2026-11-23)

| Text | What changed | Run | Result | Cost |
|---|---|---|---|---|
| 145 lines | no section left empty; no criterion to look thorough; an issue no row covers placed once answered | every case five times | 69 of 70 | $6.11 |
| 147 lines | the essential refusals stay, one for a rule; a chosen slice is marked by its whole row | the four cases with criteria five times, every case once | 34 of 34 | $3.35 |
| 149 lines | the size of each cut when a wider one is asked for; the part of an item that waits for an answer is a row of its own | the four cases those touch five times, every case once | 34 of 34 | $3.16 |

- **The one failure of 70 was real:** a session marked the row
  below the chosen one, because the end of one row of the set was
  the end of another. The text now says to replace the whole row.
- **The first tuning cut too far:** told not to write a criterion to
  look thorough, sessions wrote slices with no refusal at all ("the
  list gives no rule that would refuse anything"). The gate passed
  them; the reading did not. The second form keeps the essential
  refusals.
- **Where it stands, on Sonnet:** each of the fourteen cases has
  passed its last five runs with the text as it was for that case,
  and all fourteen passed once with the final text: 70 of 70 in
  that sense. The text is 149 lines, a third of them the two
  templates. Haiku was run on the first form only (34 of 42): it
  gives way on the wider cut in every run.

## The owner's real requirements (private): $6.02

Three real lists (7, 18 and 3 items), three runs each of our text
and of kad's skills, on Sonnet, from the slice stage on with a
scripted user who takes the recommended start. The documents are in
the audit repository (`04-slice/`); here, counts.

| List | kad's first slice when the project was planned | kad's skills now | Our text |
|---|---|---|---|
| 7 items | 8 criteria | 5 to 6 | 4 to 5 criteria; a set of 5 or 6 slices |
| 18 items | 21 criteria | 6 to 7 | 6 to 7 criteria; a set of 9 slices |
| 3 items | 5 criteria | 3 to 5 | 3 to 4 criteria; a set of 3 or 4 slices |

Every item has a home in the set in 9 runs of 9, by script. No
first slice is wider than kad's. For the list whose slice kad cut
at 21 criteria, ours is 7, for one behaviour (pick a category for a
transaction and see where it rolls up), and the other seventeen
items are in eight named rows that say what each waits for. The
slice known as "35 criteria for one button" came from a change of
scope during a build and has no list to give this stage.

## With everything loaded, and the examples

**Every earlier stage once with the slice text loaded** (Sonnet):
startup 21 of 21, the problem 8 of 8, the scope map 6 of 6, the
requirements 12 of 12; $3.13. Startup's scenario of a stage that is
not built now stops at the approach.

**The four examples, carried through a set, a chosen slice, a
made-up merge and the coming-back** (`e2e/run.py`): all four got
there; $17.37. In each the documents are numbered in order, the
merged slice is marked built, only the box whose slices are all
built is checked, no file of the user's was opened and no value of
one written down.

What they found (`../../e2e/README.md`):

- **An activity called done with questions open.** Example 2's list
  was one item with eight questions under it. The slice was cut so
  as not to wait for them, merged, its box checked, and the session
  said the activity was done. The stage script now does not call an
  activity done while a question of the list is open, and names
  the requirements as next (three unit tests); the text says the
  part of an item that waits for an answer is a row of its own.
- **A folder that is gone.** Run a second time in the same place,
  two examples were told their planning folder no longer exists,
  with no command to record one, and wrote every document without
  its number. The script now gives the command (a unit test).
- **A scripted user that loops.** Example 3 cost $7.99 the first
  time: asked one thing its brief had no topic for, the user gave
  its limits four times. The brief has the topic now.
- **A real name in a criterion.** Example 2's user had given a
  client's name as an example, and the chosen slice's criteria used
  it; the plugin's own scan found it. The text now says a
  criterion's values are never a name or figure the user gave, and
  case 04b's user gives one, with a check: the two cases with
  criteria five times, 10 of 10, $1.07 (the text is 150 lines).

Examples 2 and 3 were run again after those fixes: once stuck on
the folder that was gone ($9.00), then through the merge in fresh
places ($7.29). In both, the part of an item that waits for an
answer is now a row of its own, and its box stays unchecked after
the first merge.

## What the stage cost

| What | Guess after the pilot | Spent |
|---|---|---|
| Every earlier stage once with the new scripts | $3.07 | $3.07 |
| Pilot | $3.69 | $3.69 |
| Three runs, three arms | $17 | $18.73 |
| The real requirements | $5 | $6.02 |
| Tuning, and five runs of what passes | $11 | $13.69 |
| Every earlier stage once more, the text loaded | $3 | $3.13 |
| The four examples through a merge, and two of them twice more | $10 | $33.66 |
| **In all** | **about $53** | **$81.99** |

The cases came in as guessed. The examples did not: a run through
a merge is $1.70 to $8, not the $2.50 the earlier stages cost, and
two were run three times. The pass that first ran them was $20.50,
over the $15 that is said beforehand, and it was not said. From
here an example through a merge is counted at $4, and its user's
brief is checked for a topic for each open question before it runs.

## What a pass has not shown

- Opus was not run with the text, nor Haiku with its final form:
  Sonnet holds, and it is the session's model.
- The cases after the retunes were run five times only where the
  text changed for them, and once elsewhere: no single pass of 70
  runs was made with the final text.
- The made-up merge names every criterion of the slice. A real
  delivery's line, and a merge that names part of a slice, are
  covered by the script's unit tests only.
- An issue is placed by its title and what `gh issue view` shows;
  no run needed to read one.
