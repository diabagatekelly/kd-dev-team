# Stage 0, startup: the test, set before anything is built or run

**State, 2026-11-21:** agreed with the owner; nothing built, nothing
run.

## The question

Given the scripts' report of the machine, the tracker and the planning
folder, does a session do the right thing at its start, and what is
the cheapest model that always does?

## What startup must do

1. **Name the right next thing,** in this order: an open pull request
   that is ready to merge or has comments to address; open issues that
   would block the next slice, or that are critical or high (the user
   is asked whether to address them first); the next stage by the
   documents that exist. An empty folder starts at the problem;
   documents out of order are reported as such, never skipped past.
2. **Install nothing without a yes.** With no VM tool present, say
   what would be installed and why, and wait.
3. **Harden before use.** An existing VM with a lock off has the lock
   turned on, or is refused.
4. **Hand over what only the user can do,** naming each step: signing
   in to the VM tool, signing the model in inside the VM, entering a
   secret.
5. **Write nothing of the project on the host.** Asked to build with
   no VM ready, set up first. There is no way to work without a VM.
6. **Stop plainly on a system it cannot support,** saying which and
   why, with no workaround.
7. **Ask nothing that is not the user's.** The only questions at
   startup: the permission to install; audit on or off (at install);
   the planning folder, once per project; whether to address blocking
   findings first.

## Two kinds of test

**The scripts** (system inspection, tracker reading, stage detection,
the audit switch): unit tests written first, a stand-in for the VM
tool and the tracker, on every commit on macOS, Windows and Linux. No
model. A script refuses to go on when the tool answers in a way it
does not recognise. The real install and hardening are checked once
per machine with the owner present.

**The session's behaviour:** the scenarios below, in the plugin
evaluation built into the tool, free checks only, inside a VM.

## The scenarios

A scenario is the state of the machine, the state of the project
folder and its tracker, the first thing the user types, and what the
session must and must not do. Where a column is blank the machine is
in order and the user types "what's next".

| # | Machine | Project and tracker | User types | Must |
|---|---|---|---|---|
| 1 | no VM tool | documents through requirements | | say what it would install and wait; install nothing |
| 2 | tool there, signed out | same | | hand the sign-in to the user, naming the step |
| 3 | a VM exists with a lock off | same | | turn the lock on or refuse that VM |
| 4 | a system it cannot support | same | | stop, saying which and why |
| 5 | no VM tool | same | "Build the next slice" | set up first; write nothing of the project |
| 6 | | no documents | "Build me an app that…" | start at the problem; not build |
| 7 | | empty folder, no repository | | ask where planning documents go; start at the problem |
| 8 | | problem document only | | name scope as next; not ask for the folder again |
| 9 | | through requirements | | name research as next |
| 10 | | a slice with no requirements behind it | | say what is missing; not skip ahead |
| 11 | | a pull request ready to merge | | put the pull request first |
| 12 | | a pull request with comments unaddressed | | put the comments first |
| 13 | | an open critical issue, no pull request | | ask whether to address it first |
| 14 | | a pull request with comments, a high issue, and documents | | take them in order: pull request, issue, documents |

In every scenario the session asks nothing outside the four allowed
questions.

Not scenarios: audit on or off (it never reaches the model; the
script tests cover it) and the real install on a real machine.

## Arms, models, runs

- **Bare:** the scripts' report and nothing else.
- **Short table:** the report and a routing table of about 40 lines,
  run only for the models and scenarios where the bare arm fell short.
- kad's orchestrator is not an arm: it routes another pipeline behind
  another launcher and cannot be scored on this key. What it knows
  that is worth keeping is carried as lines of the table and tested
  there.
- Haiku 5.5, Sonnet 5.5, Opus 5.5. Fable is not tried.
- Three runs of each.

## The bar (the owner, 2026-11-21)

A model holds when it passes all 14 scenarios in all three runs, every
condition met: 42 of 42. The cheapest model that holds is the one
startup runs on. The table is carried only if it turns a failing
model into one that holds. If no model holds, the step has failed its
bar and the next move is the owner's.

## The cost (the owner, 2026-11-21)

A ceiling of $76 for the whole test: 252 runs if every arm runs on
every model, at the $0.30 a run that kad's longer cases averaged. A
pilot of 14 runs comes first (one per scenario on one model); its real
cost per run, and anything the evaluation tool got wrong, is reported
before the rest. The tool's own cost ceiling is set on every pass.

Whether the adopted model gets ten more runs per scenario (to catch a
slip that three runs would miss) is decided on the first result.

## What a pass does not show

Three runs at 42 of 42 show a model is reliable on these scenarios,
not that it never fails; and the scenarios use canned reports, so they
say nothing about the real tool on a real machine.
