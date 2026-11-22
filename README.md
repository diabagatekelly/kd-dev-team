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
| `startup/` | stage 0's scripts, each with unit tests and stand-ins for the VM tool and the tracker: `machine.sh` (the system, the VM tool, its sign-in, its locks; `secure` and `install`), `tracker.sh` (open pull requests and issues), `stage.sh` (the next stage by the documents that exist), `audit.sh` (the audit switch) and `report.sh` (the one report a session is given). Adopted with the routing table in `steps/00-startup/eval/routing-table.md`, on Sonnet 5.5 (decision 17); the test and its result are in `steps/00-startup/` |

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
  `python3 -I -m unittest` inside `library/`, `briefs/`, `judge/` and
  `startup/`.
- No text names a field of business; `judge/wording_check.py` checks a
  frozen text before its hash is taken.
