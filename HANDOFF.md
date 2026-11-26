# Handoff (2026-11-25)

For the session that takes the work on. Read `DECISIONS.md` first:
it is the record; this page only says where things stand.

## Where it stands

- Branch `questions-stage`, draft pull request #8. Merging is the
  owner's. Stages 7, 7b and 8 were built and adopted on it.
- **Adopted, all on Sonnet 5.5:** stages 0 to 8, with the security
  pass (7b) after the questions. Each stage's README under `steps/`
  has its test, what each run met and what no session has run.
- **Research is in two passes** (decision 54): up front, and again,
  together, for what the answers need of a thing committed to.
- **While a project is planned its VM reads any website and sends
  to none** (decision 52): `startup/machine.sh web open|lock`.
- **Stage 9, the tests of open facts, is adopted on Sonnet 5.5**
  (decision 58), at $212.77. Its README has every result, where the
  bar is not met and what no session has run. Two sentences of its
  text changed after the last run and were run by no session.
- **Next: stage 10, the design.** Nothing of it is built, no
  measure and no cost are agreed (the design's section 5: its
  measure is agreed with the owner when the stage is reached). kad's
  `architecture-design` and its synthesis file are the start; the
  open facts and the owner's decisions are what it now reads.
- **Owed to the library:** a question that would have asked for an
  identifier that changes when a connection is made again
  (decision 58; the one key fact in no run).

## What stage 9 took on (kept for the record)

As built: 1 and 2 by the script and the text; 4 by the list read in
the same file and brought at the stage's end; 3 is not built (the
owner's to say); 5 is counted on the real runs once they are made.

From the design (`design/planning-phase.md`) and from what stage 8
left (decisions 53 and 55):

1. **The tests.** Stage 8 draws them into `NNN_answered.md` under
   "To test, by harm": 10 to 18 a slice on the two real plans. The
   design has them run against the dependency's test environment in
   the VM, the ones with real harm first.
2. **Tests that are a page to read.** Two to eight a run are things
   a documentation page says. The second research pass should take
   them; one run in six looked up only one subject.
3. **A second reader** of each answer that speaks of a thing
   committed to, against the words it quotes: about one in fifteen
   still says what nothing read says, and five to nine in thirty
   quote the wrong line of a fact that does say it. This is a model
   reading a model inside the product. The owner's "no model judge"
   has been about grading the tests of a stage: put it to them.
4. **The owner's list, read before it is brought.** It was 14 and
   17 in two real runs of six: technical choices, things already
   decided and the same decision twice. The agreed number is 12 a
   slice. After stage 9 the list is brought to the owner once,
   before the design (decision 53).
5. **Research's condition** (decision 44) is counted a last time
   after this stage, by the two keys.

Known and left by stage 8: some of kad's concerns are said in an
answer with no criterion; what a lock leaves after a crash, and
what a close in progress does with a retry or a login, are in no
run; expected and unexpected outcomes are told apart in no record.

## What is owed

- **The four examples are caught up** (2026-11-26): kept after
  every stage through the open facts, the fourth's in the audit
  repository (`e2e/kept/04-similar-verses/`). No example's slice
  commits to a provider, so none takes one through stage 9.
- **Changed in adopted things while building stage 9, and run by
  no session since:** the questions' mark (what research adds under
  its two later headings no longer stales them), one phrase of
  research's text, the answers' script (quote marks in pairs), the
  made-up web (a host may ask for a key: rerun `setup-vm.sh` in the
  VM). Stage 9's test runs every earlier stage once for them.
- **No example reaches a merge.** `e2e/run.py --through merge`
  still waits only for research.
- **Nothing forces the web locked before a build** (decision 52):
  owed to the first build stage.
- **The run on the owner's Mac** is held off until they say.
- Put off to later stages, in `DECISIONS.md`: the user story (stage
  14), the repository's remote (stage 12), kad's design skills
  revisited (stages 10 and 11).

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
| Scripts, with unit tests | `startup/`, `research/`, `questions/`, `answers/`, `library/` |
| Every adopted text loaded together | `e2e/make_plugin.py`, `e2e/regress.py` |
| The four examples and their driver | `e2e/examples/`, `e2e/run.py`, findings in `e2e/README.md` |
| A stage on trial before it is adopted | `e2e/regress.py NAME=TEXT`; `KD_TRIAL=NAME` moves startup's case of a stage not built |
| How a pass is launched, copied out and counted; what each costs | the memory's "Evaluation VM runbook" |
| The two real plans, their keys, raw runs and reads | the audit repository, by stage; launch scripts in `NN-stage/in/` |

## Costs seen at stage 8 (Sonnet 5.5)

A case 15 cents; five runs of the eight cases about $6.60, on Haiku
55 cents. A real slice of 600 to 800 questions $1.65 to $2.20 and
six and a half to nine minutes. Every earlier stage once about $14
and rising with each stage. An example from the first message $8 to
$18.
