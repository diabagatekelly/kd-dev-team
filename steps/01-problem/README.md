# Stage 1, the problem: the test, set before anything is built or run

**State, 2026-11-21:** tested. No model holds bare; with a text of
49 lines (`eval/problem-skill.md`) Haiku passes 60 of 60 and Sonnet
59 of 60 by the checks over ten runs a scenario, and its documents
read at least as well as those of kad's skill (the result is near
the end). The owner has said the stage holds, on the
session's model, Sonnet 5.5 (decision 20). The stage
runs inside the project's VM (decision 19).

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

## The result (2026-11-21)

**The gate, three runs a scenario (18 runs an arm and model).**

| Arm | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| Bare | 9 | 8 | 10 |
| kad's skill (72 lines) | 15 | 18 | 18 |
| Our text, first version | 18 | 18 | not run |
| Our text, second version (49 lines) | 18 | 18 | not run |

No model holds bare. Given a floated solution and no reason, every
bare run of nine wrote the document where it should have asked; and
every bare run of nine put two problems in one document. kad's skill
on Haiku failed three runs: one document under a name of its own,
two holding both problems.

**Ten runs a scenario, our second version.**

| Model | By the checks | As read | Cost |
|---|---|---|---|
| Haiku 5.5 | 60 of 60 | 60 of 60 | $0.23 |
| Sonnet 5.5 | 59 of 60 | 60 of 60 | $3.65 |

Sonnet's one miss asked its question as a statement ("I need to know
how your club organises the weekend runs today, and what goes
wrong"), which the check's question mark did not see.

**The reading.** kad's nine documents on Sonnet and our text's
eighteen of the three-run passes on Haiku and Sonnet were read in
full, against the six points; the sixty of the ten-run passes were
scanned by script (the four headings, the length, words of
conclusion or solution, the count of open questions) and the ones it
flagged were read.

| Point | Bare (Sonnet) | kad's skill (Sonnet) | Our text, second version |
|---|---|---|---|
| Every statement the user's | no: sections of its own ("who is affected", "what solved looks like") | mostly: four of nine add a conclusion of the writer's to "why now" ("every extra class adds more chances to overbook") | yes in those read; one title implies a cause the user did not give |
| The current way, concretely | yes | yes | yes |
| Nothing invented | no: a year put on "March", a deadline made a limit | two small things ("payments are taken separately from booking", a date) | nothing found |
| No solution | none as a plan; goals that lean on one | none | none |
| Open questions a slice waits on | the user's, and a paragraph on each | the user's; in three of nine, one to four of the writer's own, some useful (why the double bookings happened), some filler (how many bookings a year) | the user's only |
| One page, quick to take in | no: 320 to 470 words | yes: 105 to 200 words | yes: 110 to 150 words |

So our text reads at least as well as kad's and keeps closer to what
the user said. The one real difference is a choice: kad's skill lets
the writer add open questions of its own; ours records only what the
user said is unknown, on the view that a question the planner has is
asked, not parked in a document. The first version of our text
already passed the gate; the second was tuned on the reading alone
(cause kept with effect in one bullet, the user's own voice, no
conclusion drawn from their facts).

**What holds.** Our text holds on Haiku and on Sonnet. Haiku is the
cheapest that holds.

**Cost:** $13.46 of the $30 ceiling (pilot $0.05; bare and kad's on
three models $7.20; our text, two versions, $2.33; the ten-run
passes $3.88).

## What a pass does not show

The scenarios stand for points in a conversation of at most two
turns, not a long one with a real person; and the reading is one
reader's, with its reasons given so the owner can disagree.
