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
| `startup/` | stage 0's scripts, each with unit tests and stand-ins for the VM tool and the tracker: `machine.sh` (the system, the VM tool, its sign-in, its locks; `secure` and `install`), `tracker.sh` (open pull requests and issues), `stage.sh` (the next stage by the documents that exist), `audit.sh` (the audit switch), `report.sh` (the one report a session is given) and `source.sh` (the shape of a file of the user's, never a cell; where a value of it is written down). Adopted with the routing table in `steps/00-startup/eval/routing-table.md`, on Sonnet 5.5 (decision 17); the test and its result are in `steps/00-startup/` |

| `e2e/` | the adopted stages run together on whole examples: a driver with a scripted user, the examples, and the table of what each run found and the test it became |
| `steps/01-problem/eval/problem-skill.md` | stage 1's text, 51 lines: adopted on the session's model, Sonnet 5.5 (decision 20) |
| `steps/02-scope-map/eval/scope-map-skill.md` | stage 2's text, 56 lines, the drawing of the scope map: adopted on Sonnet 5.5 (decision 24) |
| `steps/03-requirements/eval/requirements-skill-kinds.md` | stage 3's text, 94 lines, the requirements of the map's "now" activity as a list to check off, with the planner's questions from a walk of nine kinds of gap: adopted on Sonnet 5.5 (decision 28); `startup/stage.sh` counts the list |

## Where the work stands (2026-11-23)

Stages 0 to 3 hold (startup, the problem, the scope map, the
requirements), all on Sonnet 5.5. After the owner said each holds,
all four were run together, end to end, and their texts changed from
what those runs found (decisions 28 to 32). Where each stands:

| Stage | Its text | Scenarios | The pass of 2026-11-23, every adopted text loaded (Sonnet) |
|---|---|---|---|
| 0 Startup | routing table, 52 lines | 21 | 21 of 21 once; scenarios 03, 19, 20 and 21 five times, 20 of 20 |
| 1 Problem | 51 lines | 8 | 8 of 8 once; scenarios 05, 07 and 08 five times, 15 of 15 |
| 2 Scope map | 56 lines | 6 | 6 of 6 once; scenarios 05 and 06 five times, 10 of 10 |
| 3 Requirements | 93 lines | 12 | 12 of 12 once; scenarios 05 and 08 to 12 five times, 29 of 30 |

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
written down. Whether each stage still holds is the owner's to say.

**Next, in this order:**

1. **The owner's word on that pass,** stage by stage.
2. **The check-in after a merge** (decision 23): is the slice done, is
   a new "now" due, does a new issue belong to this slice, the next
   or between them. Its conditions, bar and cost are put to the
   owner before anything is built. It needs a new row in the routing
   table and a reading of merged pull requests by the scripts; the
   stage script already counts the requirements list's boxes. Its
   two first scenarios (a slice that contradicts the map, one that
   does not) were written for stage 2 and taken out; they are in the
   history of `steps/02-scope-map/eval/make_cases.py`. A map changed
   there is a new numbered version, the earlier one kept (decision
   21); kad's rule to revise in place until something is built on a
   document, then supersede it, belongs here too.
3. Then research (stage 4), in pipeline order.

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
- `python3 -I e2e/run.py e2e/examples/NAME --out FOLDER` runs one
  example end to end with its scripted user, after
  `python3 -I e2e/make_plugin.py`.
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
  `startup/` and `steps/03-requirements/eval/`.
- No text names a field of business; `judge/wording_check.py` checks a
  frozen text before its hash is taken.
