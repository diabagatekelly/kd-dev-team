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

## Where the work stands (2026-11-22)

Stages 0 to 3 hold. Next, in this order:

1. **A pause the owner asked for** (decision 28), under way: the
   tests of stages 0 to 3 looked over for gaps, and the four stages
   run end to end on four examples with a scripted user (`e2e/`).
   Every problem a run meets becomes a test, an evaluation or a
   change to a text (decision 29); the table is in `e2e/README.md`.
   As it stands: every stage's scenarios pass with everything
   adopted loaded (132 runs on Sonnet), and all four examples reach
   the requirements with their documents numbered in order. Still
   owed from the look over the tests: the plugin made
   installable and run once in a real VM, which the owner has
   held off for now.
2. **The check-in after a merge** (decision 23): is the slice done, is
   a new "now" due, does a new issue belong to this slice, the next
   or between them. It needs a new row in the routing table and a
   reading of merged pull requests by the scripts. Its two first
   scenarios (a slice that contradicts the map, one that does not)
   were written for stage 2 and taken out; they are in the history of
   `steps/02-scope-map/eval/make_cases.py`. A map changed there is a
   new numbered version, the earlier one kept (decision 21).

How a stage is run: the scenarios are built by the stage's
`eval/make_cases.py ARM` and run inside the evaluation VM by
`steps/00-startup/eval/run-pass.sh` with `ARM_PLUGIN` pointing at the
stage's arm, after `setup-vm.sh`. kad's skill, where it is an arm, is
copied into the VM by hand and never committed.

Owed, none of it blocking: a PowerShell twin of the scripts; one real
check of the VM and its install on each kind of machine, with the
owner present; the plugin installed inside a newly made VM; what of
the planning folder's memory survives a VM being destroyed.

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
