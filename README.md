# kd-dev-team

A Claude Code plugin for planning and building a product of any kind,
one validated step at a time. **Nothing here is a plugin yet:** there
is no manifest, no skill and no agent. Each stage is tested before it
is adopted, the bare model first, against a bar set before the run; a
stage's text enters the plugin only when its test has been read and
the owner says it holds.

It follows `kad-dev-team` (frozen at 0.19.0 in the
`kad-dev-team-plugin` repository), where the experiments behind this
design are recorded under `next-plugin/validation/`.

## Start here

1. `DECISIONS.md`: what the owner has decided, what is put off, and
   what was chosen without asking.
2. `design/planning-phase.md`: the stages of the planning phase and
   how each is tested.
3. `steps/`: one folder per stage, in pipeline order, each with its
   test and bar written before anything runs, then its result. The
   first is `steps/00-startup/`.

## What is built

| Folder | Holds |
|---|---|
| `startup/` | stage 0's scripts, each with unit tests and stand-ins for the VM tool and the tracker: `machine.sh` (the system, the VM tool, its sign-in, its locks; `secure` and `install`), `tracker.sh` (open pull requests and issues, and what merged pull requests say they complete), `stage.sh` (the next stage by the documents that exist; the requirements and the set of slices counted; when a coming-back to the slices is due, and exactly what to mark), `audit.sh` (the audit switch), `report.sh` (the one report a session is given) and `source.sh` (the shape of a file of the user's, never a cell; where a value of it is written down). Adopted with the routing table in `steps/00-startup/eval/routing-table.md`, on Sonnet 5.5 (decision 17); the test and its result are in `steps/00-startup/` |

| `steps/04-slice/eval/slice-skill.md` | stage 4's text, 152 lines, adopted on Sonnet 5.5 (decision 39): the set of slices, a recommended start, criteria for the chosen slice, pushback on a wider cut, the coming-back after a merge |
| `steps/05-approach/eval/approach-skill.md` | stage 5's text, 153 lines, adopted on Sonnet 5.5 (decision 41): each thing the chosen slice needs from outside compared on the user's limits from the candidates' own pages, one way recommended, the commitment asked and recorded |
| `research/` | for stage 6, not adopted: `page.py` reads a page of documentation as text through the VM's allowed sites, keeps a copy and checks every quote in a research document against its saved page; unit tests |
| `e2e/` | the adopted stages run together on whole examples: a driver with a scripted user, the examples, and the table of what each run found and the test it became |
| `steps/01-problem/eval/problem-skill.md` | stage 1's text, 51 lines: adopted on the session's model, Sonnet 5.5 (decision 20) |
| `steps/02-scope-map/eval/scope-map-skill.md` | stage 2's text, 56 lines, the drawing of the scope map: adopted on Sonnet 5.5 (decision 24) |
| `steps/03-requirements/eval/requirements-skill-kinds.md` | stage 3's text, 94 lines, the requirements of the map's "now" activity as a list to check off, with the planner's questions from a walk of nine kinds of gap: adopted on Sonnet 5.5 (decision 28); `startup/stage.sh` counts the list |

## Where the work stands (2026-11-23)

Stages 0 to 5 hold (startup, the problem, the scope map, the
requirements, the slice, the approach), all on Sonnet 5.5. After the owner said
each of the first four holds, they were run together, end to end,
and their texts changed from what those runs found (decisions 28 to
32). Where each stands:

| Stage | Its text | Scenarios | The pass of 2026-11-23, every adopted text loaded (Sonnet) |
|---|---|---|---|
| 0 Startup | routing table, 53 lines | 21 | 21 of 21 once; scenarios 03, 19, 20 and 21 five times, 19 of 20 by the checks and 20 of 20 as read |
| 1 Problem | 51 lines | 8 | 8 of 8 once; scenarios 05, 07 and 08 five times, 15 of 15 |
| 2 Scope map | 56 lines | 6 | 6 of 6 once; scenarios 05 and 06 five times, 10 of 10 |
| 3 Requirements | 93 lines | 12 | 12 of 12 once; scenarios 05 and 08 to 12 five times, 29 of 30 |
| 4 Slice | 152 lines | 17 | not in that pass: adopted later the same day (below) |

With the slice adopted, every stage's scenarios ran once with every
text and script as they now stand: 64 of 64 (startup 21, the
problem 8, the scope map 6, the requirements 12, the slice 17).

That pass is the one the texts were owed after the end-to-end runs
changed them: 107 runs and the four examples, side by side, 18
minutes, $14.33 ($7.45 the scenarios, $6.88 the examples). By the
checks 105 of 107; one of the two was a check that failed a good
answer (an offer to correct the requirements, read as an offer to do
the research another way), corrected and graded again. The one real
miss: in one run of requirements scenario 12, `sources.md` said
where the user keeps their file and not its name. Startup's scenario
03, which once said a row's number to the user, did not in five runs.
The four examples each reached the requirements with their documents
numbered in order, no file of the user's opened and no value of one
written down. The owner has said all four stages still hold
(decision 33).

**Stage 4, the slice, holds** (decision 39,
`steps/04-slice/README.md`), on Sonnet 5.5 like the four before it. Built in the order the
stages now have (decision 36): the requirements say what, the
slices are cut from them, and a dependency is chosen after.

- `startup/stage.sh` has the new order, counts the set of slices and
  says when a coming-back is due and exactly what to mark;
  `startup/tracker.sh` reads what merged pull requests say they
  complete. Every earlier stage's scenarios passed once with them
  (47 of 47), and once more with the slice text loaded (47 of 47).
- Seventeen cases for the ten rows of the test. No model holds
  without a text (Sonnet 9 of 42, Opus 8, Haiku 6); kad's two
  skills pass 3 of 24, by what they were built to do. With the text
  of 152 lines (`steps/04-slice/eval/slice-skill.md`), five runs a
  case: Sonnet 83 of 85, and 10 of 10 on the two cases its one slip
  touched once that was fixed; Haiku 66 of 85, giving way when the
  user asks for a wider cut.
- On three of the owner's real requirements lists (counted
  privately): first slices of 4 to 5, 6 to 7 and 3 to 4 criteria
  where kad's were 8, 21 and 5, and every item with a home in the
  set in 9 runs of 9.
- The four end-to-end examples go through a set, a chosen slice, a
  made-up merge and the coming-back, and can now start from their
  documents after the requirements (about $0.70 a run, not $2 to
  $8).
- Every stage's scenarios passed once with the final scripts and
  texts (64 of 64).
- $111 against $70 agreed: the examples cost three times the guess,
  and the closing pass the owner asked for was $29.
- What is tested where, for every stage from here: decision 38.

**Stage 5, the approach, holds** (decision 41,
`steps/05-approach/README.md`), on Sonnet 5.5: where a dependency is
committed to. Its text is adopted and its thirteen cases join the
regression build (77 scenarios over six stages).

- Sonnet 65 of 65 over five runs of thirteen cases with the final
  text, every quote on its page; Haiku 57 of 65, and does not hold.
- $75.11 against $90 agreed.
- The examples' kept documents reach the approach
  (`examples/NAME/after/approach/`); a run through a merge waits for
  the approach to be decided.

**Next:**

1. **Research (stage 6): its test in its new place is proposed to
   the owner** (`steps/06-research/README.md`, 2026-11-24): eleven
   cases, the benchmark on two real plans, about $90, a pilot of
   about $5 first. Nothing paid is run until it is agreed. Done
   free: its cases' made-up approach is in the form stage 5 settled,
   and startup's scenario of a stage not built moves on when
   research is on trial.

The parked check-in
proposal (`steps/check-in/README.md`) is replaced by the slice
stage's coming-back.

**Watched, not changed:** in one run of five, `sources.md` said
where the user keeps their file and not its name. The routing
table's rule is changed only if that comes back. In one run of six
the problem stage wrote its document before its last question.

**How the work is done** (the owner's standing rules, all in
`DECISIONS.md`): the owner is asked only what is theirs, one
proposal at a time with its cost; a stage is tested before it is
adopted, the bare model first, against a bar set before the run;
each stage's text is set beside kad's skill part by part (decision
26); every problem met becomes a test, an evaluation or a change to
a text (decision 29); five runs for what changed and before a
stage is put to the owner, never ten (decision 30); the suites stay quick and
cheap (decision 31, the table in `e2e/README.md`).

**How a stage is run.** Inside the evaluation VM `kd-startup-eval`,
free checks only, no model judge:

- `python3 -I e2e/regress.py` builds every stage's adopted arm with
  every adopted text loaded; a stage's own `eval/make_cases.py ARM`
  builds one arm. `steps/00-startup/eval/run-pass.sh MODEL RUNS NAME
  CEILING` runs one, with `ARM_PLUGIN` pointing at the stage's
  plugin and `CASES='stage-NN*'` for one scenario, after
  `setup-vm.sh`.
- `python3 -I e2e/regrade.py PLUGIN TRACES NAME` grades kept runs
  again by the checks as they stand, for nothing: a corrected check
  is shown right this way, never by running the scenario again.
  `python3 -I e2e/tally.py RESULT.json` counts a pass, with and
  without the checks of form.
- `python3 -I e2e/run.py e2e/examples/NAME --out FOLDER` runs one
  example end to end with its scripted user, through a set of
  slices, a chosen slice, its approach and one made-up merge, after
  `python3 -I e2e/make_plugin.py`.
- `--from requirements` (or `slice`, or `approach`) starts an example
  from the documents its last good run left (`--keep STAGE` on that
  run keeps them); it is refused once an earlier stage's text or the
  routing table has changed.
- A text not yet adopted is loaded on trial with `NAME=TEXT` after
  either of `e2e/regress.py` and `e2e/make_plugin.py`.
- The VM stops when the command that started it returns: a pass is
  kept attached to that command, never left running behind it.
- kad's skill, where it is an arm, is copied into the VM by hand and
  never committed. Raw runs go to the audit repository.

**Owed, none of it blocking:** the adopted pieces assembled into the
real plugin and run once in a real VM on the owner's Mac (held off
by the owner; it also settles where the user finds `source.sh` on
their own machine, and installing the plugin inside a new VM); a
PowerShell twin of the scripts; one real check of the VM and its
install on each kind of machine, with the owner present; what of
the planning folder's memory survives a VM being destroyed; the
cause of a fault in the evaluation where a session's shell twice
could not see the recorded folder (worked round in the scenarios'
set-up, not found).

## What came across from the earlier work

None of it is adopted; each is a candidate or a tool for testing one.

| Folder | Holds |
|---|---|
| `library/` | 250 ways software commonly fails, by kind of action, from public pages, with its checker |
| `briefs/` | the three briefs tried for the research, questions and answers stages (triage, dossier, answers), with the scripts that check and count their output |
| `judge/` | the prompt that matches a method's output against known defects (its hash beside it), the script that counts agreement, and the check that no frozen text names one field of business |
| `vm/` | the trial script that sets up a locked-down VM for a session (macOS only so far) and the plain-words safety page |

## Rules

- This repository is public: methods, scripts, prompts, and results as
  counts and costs. Nothing that quotes a real project is kept here.
- Every script has unit tests, written first. Run them with
  `python3 -I -m unittest` inside `library/`, `briefs/`, `judge/`,
  `startup/`, `research/`, `steps/03-requirements/eval/`,
  `steps/04-slice/eval/`, `steps/05-approach/eval/`,
  `steps/06-research/eval/` and `e2e/`.
- No text names a field of business; `judge/wording_check.py` checks a
  frozen text before its hash is taken.
