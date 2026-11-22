# Stage 1, the problem: the test, set before anything is built or run

**State, 2026-11-21:** the conditions, the gate and how quality is
read are set below (the owner, decision 18). Nothing is built. The
stage runs inside the project's VM (decision 19), so its scenarios
start from the report a session is given there.

## What the stage must do

1. **Ask, not invent.** Given only an idea, it asks the user about
   the problem and writes nothing.
2. **Ask about the problem, not the solution:** what costs time or
   money today, who it affects, why now, the hard limits. Not the
   kind of product, its sign-in or its technology.
3. **Ask only for what is missing.** Nothing the user already said is
   asked again.
4. **Write the user's account and nothing more.** Once the account is
   complete it writes `problem.md` in the planning folder, with the
   user's facts in it and no solution or technology the user did not
   name.
5. **Keep unknowns as open questions.** What the user does not know
   yet is recorded as open, not filled in.
6. **Flag two problems as two,** and do not write one long document.
7. **Stop there.** It does not go on to scope or to building.

Conditions 1 and 2 come from startup's runs (a problem written from
the session's own assumptions; questions about the solution). The
rest are carried from kad's `problem-framing-doc`.

## Two measures

**The gate: free checks, to catch drift.** Scenarios in the plugin
evaluation, as for startup: made-up products in different fields; a
bare idea, a full account, an account with a solution floated and no
reason given (two turns: the question, then the document), an "I do
not know yet", two problems in one. The checks: whether a file was
written and when, the seeded facts of the account present in it,
words of a solution the user never used absent from it, nothing else
written. No model judge: kad's judge on this document's "why now"
failed four documents of six and passed two worded the same way.

**Quality: read, with reasons.** The checks cannot say a problem is
framed well. For each arm that passes the gate, every document it
wrote is read in full and set beside the document kad's skill writes
for the same scenario on the same model, and the reading says which
is better and why, on these points, fixed before any is read:

- every statement is the user's, or follows from what they said;
- the current way of doing things is named in concrete terms;
- nothing is invented: no figure, no reason, no limit;
- no solution, and a floated one is not carried as the plan;
- the open questions are ones a first slice waits on, not filler;
- one page, and quick to take in.

The reading is reported to the owner with its reasons; the documents
themselves are made-up and may be quoted here.

## Arms, models, bar

- **Arms:** the bare model (startup's report and table, nothing for
  this stage); kad's skill as it stands, the mark to reach; a new
  text, as short as holds, tuned until it is at least as good as
  kad's on the reading. Each tuning pass is shown apart from the
  others.
- **Models:** Haiku 5.5, Sonnet 5.5, Opus 5.5; three runs. Haiku is
  run through the gate, which costs cents; its documents are read
  only if it passes.
- **Bar:** a model holds when it passes every run of the gate and its
  documents read at least as well as kad's. The cheapest that holds
  is adopted. The new text is carried only if the bare model does not
  hold without it.
- **Cost:** a ceiling of $30 (proposed to the owner with the
  conditions), after a pilot on Haiku whose real cost is reported
  first.

## The pilot (2026-11-21)

Haiku 5.5, each of the six scenarios once, the bare arm and kad's
skill: 12 runs, $0.05. The bare arm passed 3 of 6 and kad's skill 4
of 6. The pilot is for the setup, not the result:

- The setup works: the skill is invoked, the second turn follows the
  saved first turn, documents are written and read by the checks.
- **Nothing told a session what the document is called.** Bare, it
  wrote `01-problem.md`; with kad's skill, a name of its own. Every
  check on the document then failed, and the script that finds the
  next stage would not have found it. The report now names the
  document with the stage ("its document: planning/problem.md"),
  by script, for every arm.
- Bare Haiku wrote the document where it should have asked (the
  floated solution) and put two problems in one document.

## What a pass does not show

The scenarios stand for points in a conversation of at most two
turns, not a long one with a real person; and the reading is one
reader's, with its reasons given so the owner can disagree.
