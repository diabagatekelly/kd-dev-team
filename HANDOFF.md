# Handoff (2026-11-26)

For the session that takes the work on. Read `DECISIONS.md` first:
it is the record; this page only says where things stand.

## Where it stands

- Branch `open-facts-stage`, pull request #9, a draft with CI green
  on all three systems and no reviewer comments. Merging is the
  owner's. Stage 9 was built, tested and adopted on it. Once it is
  merged, the next stage starts on a new branch from main: a branch
  whose pull request is merged has no CI.
- **Adopted, all on Sonnet 5.5:** stages 0 to 9, with the security
  pass (7b) after the questions. Each stage's README under `steps/`
  has its test, what each run met and what no session has run.
- **Research is in two passes** (decision 54): up front, and again,
  together, for what the answers need of a thing committed to.
- **While a project is planned its VM reads any website and sends
  to none** (decision 52), but to a provider's test environment the
  user allows, with a key they type (decision 56).
- **A second reader, a model reading a model inside the product**
  (decision 56): each answer that speaks of a thing committed to is
  handed, with only the words it rests on, to a fresh session; what
  it flags is cut back or looked up. It grades nothing.
- **The owner's list is read and brought once, at the end of
  stage 9, before the design** (decision 53); the design does not
  start while a decision waits.
- **Next: stage 10, the design.** Nothing of it is built. No
  measure, no test and no cost are agreed.

## What stage 10 has to take on

From the design (`design/planning-phase.md`, row 10 and section 5)
and the decisions:

1. **Structure, boundaries, where each criterion lives.** kad's
   `architecture-design` (583 lines, with `adr`) is the start, and
   its synthesis file `kad-dev-team-plugin/.synthesis/software-architect.md`
   holds the principles it was built from: carry each or say why
   not (decision 46: kad's design skills are revisited thoroughly
   at stages 10 and 11).
2. **It has no measure yet.** The design's section 5 says so of
   the design and screens stages: each is agreed with the owner
   when the stage is reached, before its text is judged. Put a
   measure to them with the stage's test and cost.
3. **What it reads now that kad's design did not have:** the
   answers and their criteria (`NNN_answered.md`), the open facts
   with what the slice does either way (`NNN_tested.md`), the
   owner's decisions recorded on their answers, the research with
   what was looked up and what a test showed, and the states.
4. **Put off to it, in `DECISIONS.md`:** a dependency the user did
   not name (a library the design picks) has no way back to
   research; kad's three checks for whether a decision earns a
   record; nine security concerns of the second plan that wait for
   a design to be chosen (decision 51).
5. **Left by stages 8 and 9 for a design to meet:** some of kad's
   concerns are said in an answer with no criterion; what a lock
   leaves after a crash, and what a close in progress does with a
   retry or a login, are in no run; an answer cut back from "it
   does this" to "the product treats it as this" still leans on
   the thing, with no test opened.

## Known of stage 9 (decision 58)

- Sonnet passes 65 of 75 on its cases, not 75; Haiku does not hold
  the stage.
- A session calls almost nothing settled by a run in a test
  environment (1 of 12 in the last two real runs): it writes what
  was shown into the answer and leaves the test a person's. A
  slice comes out with 15 or 16 open facts.
- The same test is sorted differently from run to run.
- Two sentences of its text were changed after its last run, and
  no session has run them.
- The second reader never runs inside a case (the evaluation has
  no reader): it ran in the twelve real runs only.

## What is owed

- **A question for the library** that would have asked for an
  identifier that changes when a connection is made again: the one
  key fact of the first real plan that is in no run (decisions 44
  and 58). The library is not changed while it is being measured:
  propose it with the next stage that runs the questions.
- **No example takes a provider through research, the questions,
  the answers or the open facts:** each example's first slice
  commits to nothing outside. That path is in the cases and the
  real plans only.
- **Not run since the round of stage 9:** the examples, and every
  earlier stage's cases (they ran before the questions' mark
  changed for the last time; the unit tests show the cases'
  drawings unchanged).
- **No example reaches a merge.** `e2e/run.py --through merge`
  still waits only for research.
- **Nothing forces the web locked before a build** (decision 52):
  owed to the first build stage.
- **The run on the owner's Mac** is held off until they say.
- **The owner's sandbox keys** are in the evaluation VM
  (`~/.kd-dev-team/test-keys`), put there at their word; they were
  offered removal and have not asked for it.
- Put off to later stages, in `DECISIONS.md`: the user story (stage
  14), the repository's remote (stage 12), kad's screen skills
  (stage 11).

## How the work is done

The owner's standing rules are in the memory of this project and in
`DECISIONS.md`; in short:

- Ask the owner only what is theirs, one proposal at a time with
  its cost. Record the rest under "Chosen without asking".
- A stage is built free first (script, text, cases, unit tests),
  then its test and cost are proposed. Nothing paid runs before the
  owner's yes. A pilot first, its real cost reported.
- Evaluations run inside the VM `kd-startup-eval`, with free checks
  only and no model judge; quality is read, with reasons.
- **Before any paid launch, check that the VM is on the commit
  meant, by checksum of the built plugin, and run nothing
  otherwise; and wait for CI on that commit.** A round of $24 ran
  on the wrong commit on 2026-11-26. The memory's runbook says how.
- Decision 38 says what is tested where. Decision 29: whatever a
  run meets becomes a unit test, a case or a change to a text that
  is tested again.
- Keep a running total against the cost agreed; say before it is
  passed, and before any pass over about $15.
- This repository is public. Anything that quotes the owner's
  projects goes to the audit repository, in a folder named after
  the stage.
- After every push: CI is for that push, and the reviewer's
  comments are triaged unasked.
- kad is frozen beside this repository: change nothing of it.

## Where things are

| What | Where |
|---|---|
| A stage's text, cases and result | `steps/NN-name/eval/` and `steps/NN-name/README.md` |
| Scripts, with unit tests | `startup/`, `research/`, `questions/`, `answers/`, `openfacts/`, `library/` |
| Every adopted text loaded together | `e2e/make_plugin.py`, `e2e/regress.py` |
| The four examples and their driver | `e2e/examples/`, `e2e/run.py`, findings in `e2e/README.md` |
| A stage on trial before it is adopted | `e2e/regress.py NAME=TEXT`; `KD_TRIAL=NAME` moves startup's case of a stage not built |
| How a pass is launched, checked, copied out and counted; what each costs | the memory's "Evaluation VM runbook" |
| The two real plans, their keys, raw runs and reads | the audit repository, by stage; launch scripts in `NN-stage/in/` |

## Costs seen at stage 9 (Sonnet 5.5)

A case about 20 cents; five runs of the fifteen cases $15.50, on
Haiku $1.30. Every earlier stage once (ten) $15.64. A real run of
stage 9 from a kept stage 8 run $2.50 to $3.90 with the reader's
own calls, which are not in the session's own count. An example
from the first message through stage 9 $12 to $15. The stage in
all: $212.77, where about $170 was first agreed.
