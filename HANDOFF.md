# Handoff (2026-11-28)

For the session that takes the work on. Read `DECISIONS.md` first:
it is the record; this page only says where things stand.

## Where it stands

- Pull request #9 (stage 9) is merged. Branch `design-stage` from
  main, a draft pull request: stage 10 is built free on it and
  **proposed, not agreed**. Merging is the owner's.
- **Adopted, all on Sonnet 5.5:** stages 0 to 9, with the security
  pass (7b) after the questions. Each stage's README under `steps/`
  has its test, what each run met and what no session has run.
- **Stage 10, the design:** `steps/10-design/README.md` is the
  proposal: a measure (a private key of what a structure could have
  prevented in the two real builds, counted beside kad's own
  designs), fourteen cases, about $160, a pilot of about $16 first,
  and three points of the owner's. **Nothing paid has run, and no
  session has run any of it. Check `DECISIONS.md` for their yes
  before any launch.**
- Research is in two passes (decision 54). While a project is
  planned its VM reads any website and sends to none (decision 52),
  but to a provider's test environment the user allows (decision
  56). A second reader reads each claim against its words (decision
  56). The owner's list is brought once, at the end of stage 9
  (decision 53).

## Stage 10 as built

- `designing/design.py next|draw|state` (43 unit tests); the text
  `steps/10-design/eval/design-skill.md`; fourteen cases
  (`eval/make_cases.py bare|text`, 16 unit tests).
- The stage script counts the design by its drawing's mark, what
  waits and what goes back. On trial: `design=steps/10-design/eval/design-skill.md`
  after `e2e/regress.py` or `e2e/make_plugin.py`; `KD_TRIAL=design`
  moves startup's case of a stage not built to the screens;
  `e2e/run.py --through design`.
- What it chose without asking is in `DECISIONS.md` ("Stage 10, the
  design, as built"). The largest: no technology is picked in the
  design (a boundary says what is needed; the stack stage picks),
  and no decision of structure is put to the user.
- Private, in the audit repository under `10-design/`: the key and
  kad's count against it (`README.md`), `in/preflight.sh SHA`,
  `in/pilot10.sh RUNS TAG`, `in/real10.sh NAME PLANNING ARM`. Real
  runs start from `09-open-facts/runs/real4/kv1` and `kw1`.
- After the owner's yes: wait for CI on the commit, copy `in/` to
  the VM, run the preflight, then the pilot; report its real cost
  before anything else.

## After stage 10

Stage 11, the screens (kad's `design-system`, `screen-design`,
`accessibility-review`, revisited thoroughly: decision 46), has no
measure yet. Stage 12, the stack, owes: picking against what each
boundary of the design needs, and the way back to research for what
it picks.

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
  drawings unchanged). Both are in stage 10's proposed test. The
  examples' kept documents after the open facts are stale; those
  after the answers are not.
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
| Scripts, with unit tests | `startup/`, `research/`, `questions/`, `answers/`, `openfacts/`, `designing/`, `library/` |
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
