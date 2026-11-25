# Stage 7, the questions: the test, set before anything paid is run

**State, 2026-11-24: agreed (decision 45), built, and the pilot
run: $5.97 of about $135.** The text was changed after the pilot
for what it found; nothing has run with the changed text yet.

## The pilot (2026-11-24, $5.97)

Each of the ten cases once; kad's two skills on two cases; one real
run on the first plan, on top of a kept research run.

| Arm | Model | Pass every check | Cost |
|---|---|---|---|
| Our text, 112 lines | Sonnet 5.5 | 6 of 10 | $2.32 |
| Our text | Haiku 5.5 | 7 of 10 | $0.22 |
| Bare | Sonnet 5.5 | 3 of 10 | $2.55 |
| Bare | Haiku 5.5 | 2 of 10 | $0.19 |
| kad's two skills (two cases) | Sonnet 5.5 | 0 of 2 | $0.27 |
| One real run, our text | Sonnet 5.5 | below | $0.42 |

One run each: these say where each arm stands, not whether it
holds. A case costs $0.23 on Sonnet and 2 cents on Haiku, a real
run $0.42: less than the $0.35 and $1.50 guessed.

- **The script's part worked as built.** In every run that reached
  it the command checked `kept.md`, refused what was wrong and drew;
  no session wrote the drawing by hand. In the cases a session's
  shell may not write the project, so the command says the drawing
  was not kept; in the real run it wrote the file, and the script's
  own check passes on it.
- **The real run** (97 seconds): every defect the earlier judges
  tied to the library has a kept entry, 18 of 18 fully tied and 8
  of 8 partly; a line for 4 of 4 of the malformed-value defects;
  of the three facts that research run lacks, one is asked for and
  two have no general question, as read beforehand.
- **Too many lines.** That run drew 1,027: 641 from the library
  (198 of 250 entries kept, each applied to three things or more),
  126 of values, 120 of leaks, 108 of states. Case 1, three
  criteria, drew 1,060. The bare model, told nothing, applied a
  question to fewer things (232 library lines on case 1). The first
  text said to name "every such thing"; a session did.
- **With the text, Sonnet failed four cases:** told to skip the
  stage, it did not load the text at all (both turns); it did not
  see that a renewal recorded by a criterion had no states; and one
  check of mine failed a row that had rightly gained a thing.
- **kad's skills** wrote nothing in either case: they stopped to
  ask their questions first, as built.
- **Haiku with the text** took the request to skip for the approach
  stage's work, and loaded that text.

What the pilot changed (decision 29):

| What it met | Now |
|---|---|
| Each kept question applied to five things: over a thousand lines for a small slice | the text: the fewest things that cover a question, not a criterion and the thing it acts on; case 1 checks that the library's part is under 500 lines |
| 120 lines of leaks: 24 values marked sensitive, each against five places | leaks are drawn for each class of sensitive values, not each value: the script, with unit tests; the text names the class |
| Told to skip, the stage's text was never loaded | the text's own description says it is used when the user says to skip the questions or go past them |
| A thing a criterion records had no states and was not noticed | the text: before anything else, each criterion is gone through for what it creates or keeps |
| A row left as it was, with one more thing, failed a check on its exact words | the check looks for the row and its criterion: unit test |
| My count of the malformed-value key read the file as one text, and its patterns begin at a line's start: 0 of 4 | counted by `outcome.py lines`, with a unit test; the key is unchanged; 4 of 4 |

## What it is

The pivot from kad. There, the failure cases were short lists
written into each skill from general knowledge, and the owner was
asked as the work went (149 questions, the first option taken 72%
of the time). Here the questions come from a library of 250 ways
software commonly fails and from grids drawn by script; **nothing is
answered at this stage and the user is asked nothing.** Answering is
stage 8, testing what no page says is stage 9, and what is truly the
owner's reaches them once, as one list, at stage 14.

The stage leaves a folder, `slice-NNN/NNN_questions/`, with two
files:

- **`kept.md`, written by the session:** what the slice takes in,
  and which of the library's questions matter for it, each with the
  things it applies to.
- **`questions.md`, drawn by script from `kept.md` and the slice's
  documents:** every question the answers stage must answer, a line
  each, each with a name that does not change.

## What is a script and what is a text

| Part of `questions.md` | Drawn from | Who decides what is in it |
|---|---|---|
| A line for each kept library question and each thing it applies to | `kept.md` | the session, checked by script |
| Each value taken in, against the ways a value of its kind can be wrong (empty, missing, malformed, at the edge, outside, too long, twice, naming what does not exist, unusual characters) | `kept.md`'s table of values | the session lists the values; the script crosses them |
| One rule for every setting the build will read (missing, empty, malformed, outside) | nothing: always drawn | the script. A build reads settings no plan names (E4), so the rule is asked once |
| Each class of sensitive values against the five places it can leak to (logs, an error's own message, an error shown, monitoring, test data) | the values the session gives a class | the session marks; the script crosses |
| Each state of each lasting thing, against each event: each criterion of the slice, the same action again, a reload partway, a restart, a second copy or person at once, time passing, and each thing committed to being down, slow, or acting with its reply lost | research's `states.md`, the slice, the approach | the script alone |
| Seven questions asked of every slice (what an hour's outage costs, the target, who notices; what is sensitive, who may see whose, what binds, what an attacker wants) | nothing: always drawn | the script. In kad these were asked of the owner first; here they are answered at stage 8 from the documents, and only otherwise the owner's |
| What research left open: every open point with its test, every statement the pages contradict or do not cover, every state `not said` or `to verify`, every dead end for the owner's list | research's documents | the script alone |

**The session's judgement is two things only.** Which library
questions matter (E3: a triage kept every entry a real defect
depended on, in three runs of three, at 40% of the size of crossing
everything), and what the slice takes in (E3's weak point: it
listed the values it thought of, and missed two). So the script
holds the session to the documents:

- every one of the 250 entries is kept or dropped, once; a kind of
  action the slice does nothing of may be dropped whole, with the
  reason; a kept entry applies to at least one thing;
- a thing is a criterion, a lasting thing, a thing committed to, a
  value from the table, or another thing `kept.md` lists (a request,
  a screen, a stored file): never a name from nowhere;
- every value has a kind the script knows and a source that exists
  (a criterion, or a research document);
- `questions.md` is exactly what the script draws from the documents
  as they stand. A session cannot write it by hand, and once a
  document of the slice changes the stage script says the questions
  are stale.

**The library first, and no question twice.** The session goes
through the library before anything is drawn, and the script then
draws only what the library left unasked. A line of a grid is not
drawn when a kept library question, applied to the same thing,
already asks it: the reply that never arrives is one question of a
thing, not one from the library and one more for each of its
states. The library's line stands, names each state of a lasting
thing so that it is answered for each, and the script says how many
lines it spared. Which library questions ask the same as which
column is a fixed table in the script (17 columns, 32 entries), a
unit test holding it to the real library; an entry that is dropped,
or kept for another thing, spares nothing, so the grid still
catches what the triage let go. No entry is judged twice and no
line has the same name as another.

`questions/questions.py` (`things`, `library`, `draw`, `check`,
`state`), 67 unit tests, no model.

**Sized for nothing on what is kept.** Without the library's part
and the values, which need a session, and so before any line is
spared as already asked:

| | Lasting things | States | Lines of state against event | Carried from research |
|---|---|---|---|---|
| Example 1 | 1 | 5 | 45 | 5 |
| Example 2 | 3 | 8 | 72 | 12 |
| Example 3 | 3 | 7 | 56 | 5 |
| Example 4 | 0 | 0 | 0 | 0 |
| The first real plan, three research runs | 1 | 12 to 14 | 144 to 168 | 19 to 27 |
| The second real plan, three research runs | 1 or 2 | 14 to 20 | 210 to 300 | 20 to 22 |

With the library's part at E3's size (345 to 493 lines) and the
values, a real slice comes to roughly 650 to 950 lines, against 675
and 283 cells for the frozen tables and 1,172 for E2. Whether that
is too many to answer is the answers stage's measure; here it is
reported.

## What the stage must do

1. **Work from the report's commands and the documents.** The
   library is read with the command the report gives, every entry.
2. **Account for every entry,** kept with the things it applies to,
   or dropped with why it cannot arise in this slice. When unsure,
   kept: a question wrongly dropped is lost for good.
3. **List what the slice takes in:** each value a person gives, each
   field of a reply the criteria use (from research's facts), each
   value read back from where it was stored; its kind, where it
   comes from, whether it is sensitive, its source.
4. **Draw with the command,** and put right what it refuses.
5. **Answer nothing, decide nothing, ask nothing.** A contradiction
   research found is carried, not resolved. No preference is asked.
6. **Name a lasting thing the criteria keep that `states.md` has no
   table for,** and have it walked by research's rules before the
   grid is drawn: never states from what such things usually do.
7. **An answer the user gives to an earlier stage's open question**
   is recorded by that stage's text, said, and the questions are
   drawn after.
8. **After a changed slice or approach** (the report says stale):
   look again only at what the change brings or removes; draw again.
9. **Change no other document** of the slice. No criterion, no
   design, no recommendation.

## A point that is the owner's

**A user who says "skip the questions, it is a small thing".**
Proposed, as for research's reading: said once what it costs (on
the two real plans, questions drawn this way named 17 of 43 known
defects before the build, against 11 for the earlier tables) and that this stage asks them nothing; the
stage offered again. If they still say no, it is theirs: the library
is not gone through, the folder records that it was skipped at their
word and when, and what a script draws with no judgement (the
states against events, what research left open, the seven
questions) is drawn all the same. The skipping is carried to the
owner's list as a risk accepted. The other way: the stage cannot be
skipped at all.

## The two things research's examples left open

- **A lasting thing the slice creates that the requirements' list
  does not name.** Proposed: it is walked. Research's text gains one
  sentence (a thing a criterion creates and keeps is walked whether
  or not the list names it, and said in the reply), since the state
  grid has a hole without it; and this stage checks for the hole
  (condition 6, case 4). Research's two cases of states are run
  again five times and its others once.
- **The user answers an earlier stage's open question mid-stage.**
  Proposed: condition 7, case 5. The routing table already says an
  answer to a stage's question is that stage's work; the case shows
  whether that is enough.

## Set beside kad's two skills, part by part (decision 26)

kad's `reliability-requirements` (392 lines) and
`security-requirements` (344), and the principle tables they were
built from (`.synthesis/devsecops-engineer.md`).

| What kad's skills do | Here |
|---|---|
| The first response is questions to the owner: what an hour's outage costs, a target, who notices; what is sensitive, who sees whose, obligations, what exists | **Different on purpose.** The seven are drawn for every slice and answered at stage 8 from the documents first; what the documents do not say is the owner's, once, in the list |
| Failure modes named from the skill's own list: slow, down, a reply that lies or cannot be used, interrupted partway, the same thing twice | **Replaced:** the library's kinds on calls, received data, updates and long operations, triaged; the events down, slow and reply lost against every state |
| A reply the slice cannot use gets its own row | **By script:** each field received against each way of being wrong |
| Retry only what is transient; a refusal is not retried | Asked (the library's questions on which refusals are final and when trying stops); decided at stage 8 |
| A refusal that never clears: what the person can still do, or a dead end the owner accepts | Kept: research walks it, the script carries every dead end to the owner's list |
| Every state the slice can leave a thing in is a failure mode; a state the model lacks goes back to the model | Kept and widened: every state against every event, by script; condition 6 is the way back |
| Stated as general knowledge how a provider's refusals behave | **Not carried:** research's facts and open points, carried by script |
| Read the security criteria first; where the two disagree, say which wins | Both halves are one set of questions about the same things, so stage 8 answers them together |
| Degrade or fail loudly, for each failure mode; expected against unexpected failures | Stage 8: these are answers. The questions that ask them are the library's |
| What must be observable, by the question to be answered and not by coverage | The library's kind on what is recorded, triaged like any other |
| Every retry, wait and give-up has its number | Stage 8, from research's facts; the questions that ask for each number are here |
| The threat pass: what an attacker wants, where untrusted input crosses in, the worst reachable from there | The first is one of the seven; the second is the table of values, held to the criteria and research by script; the third is stage 8 |
| Each sensitive class traced to five exits | **By script:** each sensitive value against the five |
| Prefer a criterion that the sensitive thing never enters | Stage 8 |
| A value of the owner's file reaching the repository: scanned when the criterion is written | Already a script of startup's (`source.sh`); the readiness stage runs it |
| What was considered and dismissed, with the reason | Kept: every dropped row has its reason, and the script refuses one without |
| Few real failure modes: say so and write few | Kept: a kind the slice does nothing of is dropped whole |
| Forks put to the owner one at a time, approval before the document | **Different on purpose:** nothing asked here; one list at stage 14 |
| Given/When/Then criteria, design notes apart, a count | Stage 8 |
| The slice cannot meet its target without something nobody scoped: handed back to the slicer | Stage 8, where a target exists |
| Consulted mid-design; a decision mid-build under a delegation | Not carried here: the design and the build are later stages |
| The principles of supply chain, alerts, rollout and review | Not this stage: they belong to the stack, the build and the reviews |

## Three measures

**The gate: free checks, on made-up documents.** The playhouse and
PayRight of the approach's and research's cases, as research would
leave them. Ten cases:

| # | The situation | Must |
|---|---|---|
| 1 | one thing committed to and researched (facts, a contradiction, two open points); a thing held there and one the product keeps; a credential and a person's details among what is taken in | every entry accounted for; the kinds the slice does nothing of dropped with a reason true of it; the planted entries kept and applied to the right thing; the planted values listed, the sensitive ones marked; drawn by the command and passing its check; nothing asked, answered or decided; no other document changed |
| 2 | nothing committed to; only things the product keeps, some rows `not said` | the kinds on outside systems dropped for that reason; every state drawn, the `not said` rows carried; no provider named, nothing fetched |
| 3 | the slice touches no lasting thing | the values and the library still done; the script says so in a line |
| 4 | a criterion keeps a thing `states.md` has no table for | named first, with the criterion; its table added by research's rules, each row sourced or `not said`; then drawn with it |
| 5 | the user answers one of the requirements' open questions in the message that says to go on | recorded in the requirements; said; no criterion written here; the questions drawn |
| 6 | "what do you need from me? just ask me how failures should be handled" | nothing asked; said that the documents and tests answer first and what is theirs comes once, as a list; the questions drawn |
| 7a | "skip this, it is a small slice, go on to the design" | said once what it costs, the stage offered again; nothing recorded yet (waits on the owner's point) |
| 7b | (next turn) the user insists | recorded as skipped at their word; what the script draws alone is drawn; no design started |
| 8a | a criterion was added to the slice after the questions were drawn | a kind dropped before and now needed is kept; the earlier rows left; drawn again, the earlier names unchanged |
| 8b | the approach changed and research was written again for another thing | nothing left that applies to the old thing; drawn again |

**The outcome on the two real plans: free too, and private.** The
stage is run on top of each of the three kept research runs of each
plan (the audit repository, `07-questions/`). Counted by script,
each key written before any run:

- **The triage keeps what real defects depended on.** E1's judges
  tied 18 of the first plan's defects fully to library entries and 8
  partly; 7 and 4 on the second. The slices in this plugin's form
  are thinner than the plans those defects came from, so each defect
  is marked beforehand as within the thin slice or not, and only
  those within are counted.
- **The values reach the malformed-value defects.** The four
  defects of the first plan about one malformed setting or field,
  all four lost by E2's grid and two of them by E3 as well: is
  there a line for each.
- **The gaps research leaves (the owner's condition, decision
  44).** For each run, each fact of the key that run's research
  lacks is looked for again: *asked for*, when a kept question
  applied to the thing concerned can only be answered with that
  fact (stage 8 must then find it on a page or mark it for a test,
  and stage 9 run the test); or *not asked for*, named with its
  kind. The same count is made again after stages 8 and 9. The
  final runs lack seven facts between them. By a first reading against the
  library (the key of which entries ask for which fact is written,
  privately, before the pilot): five have a general question that asks
  for them (how long a first reply may take, what a reply holds,
  whether access lapses by itself, how an outage is told from a
  refusal, a limit no retry clears). Two have none: **a name the
  other side gives a thing that later changes, and whose screen a
  person's own login for the outside system is typed into.** Those
  are the kind expected to remain, and what the library would need
  is two entries, each resting on a public page like the other 250,
  in kinds that are already at the checker's limit of twelve: the
  limit is raised when they are proposed, after the count.
- **Size and steadiness:** entries kept, lines in all, lines spared
  as already asked, and how many entries all three runs keep.

**Quality: read, with reasons** (decision 18). The mark is kad's own
reliability and security documents for the same two slices: each
failure mode and criterion of theirs is looked for among the
questions (asked of the same thing, or not), and what the questions
ask that kad's never did is counted. On points fixed now: a kept
question applies to a thing a builder would recognise; a dropped
row's reason is true of the slice; nothing is answered; the drawn
file could be handed to the answers stage as it is.

## Arms, models, bar

- **Arms:** the bare model (every adopted text and the report with
  its commands, nothing for this stage); the triage brief of E3 as
  it was measured, on the first real plan only; kad's two skills on
  cases 1 and 2; our text, as short as holds.
- **Models:** Haiku and Sonnet 5.5, three runs bare and with the
  text; then five runs on each with the final text (decision 38).
  Opus only where Sonnet with the text does not hold (about $20
  more, said first).
- **Bar:**
  - every case in every run: 50 of 50 at five runs;
  - in every run, `questions.md` passes the script's check: every
    entry accounted for, every thing known, drawn and not written;
  - no run asks the user a question or records an answer;
  - read on the two real plans: no two lines of a `questions.md`
    ask the same thing of the same thing (any pair found is added
    to the script's table, with a unit test);
  - on both real plans, every run keeps an entry for every fully
    tied defect within the slice, and for all but one at most of
    the partly tied (E3's bar);
  - a line for at least three of the four malformed-value defects;
  - every fact research lacks that a general question asks for is
    asked for in every run; the others are named;
  - the questions read no worse than kad's two documents on the
    same slices: nothing kad named goes unasked.

## Cost

A case is taken at $0.35 on Sonnet and 3 cents on Haiku: twice a
research case, since every session reads 250 entries and writes a
row for most. A real run at $1.50. The pilot's real cost is
reported before anything else is run, and resets these.

| What | About |
|---|---|
| The script, the stage script, the driver (`--through questions`), the cases; unit tests | free |
| **Pilot:** each case once on Haiku and Sonnet, bare and with our text; kad's on two; one real run on the first plan | **$10** |
| Three runs: bare and ours on Haiku and Sonnet; kad's on two cases | $23 |
| Two rounds of tuning | $12 |
| Five runs with the final text, Sonnet and Haiku, and half as much again for what a late change stales | $29 |
| Every earlier stage once with the changed stage script and once with the final text on trial (89 cases each); research's cases after its one sentence | $17 |
| The two real plans: six runs with the text; three with E3's brief and one bare on the first | $15 |
| The four examples from their kept documents through the questions, twice while it is built | $4 |
| The four examples once from the first message, each in a fresh place | $24 |
| **In all** | **about $135** |

That is more than research ($84 of $90): the cases cost about
twice as much each, and the examples go one stage further. The pass
of the four examples from the first message is over $15 and is said
again before it is run. A running total is kept against what is
agreed and said before it is passed.

## What it changes outside itself

- `startup/stage.sh` (adopted): the questions are a folder; done
  when `questions.md` is drawn from the documents as they stand,
  next again when stale; the report gives the commands. Unit tests,
  and every earlier stage's cases once.
- Research's text (adopted): one sentence (above). Its cases again.
- `e2e/`: the driver carries an example on through the questions
  and starts from its documents after research.
- Startup's case of a stage not built names the answers when the
  questions are on trial (`KD_TRIAL`): a unit test.
- The library is not changed for the test. The entries the count
  shows missing are proposed afterwards.
- The routing table is not changed unless a run shows it must be.

## What a pass will not show

- Whether the questions can be answered well, and how many reach
  the owner: stage 8's measure.
- None of the four examples commits to anything at its first slice:
  end to end they show the product's own things and no dependency.
  The path with a dependency is the cases' and the two real plans'.
- The real plans are one field and one kind of provider; the
  defects they are counted against came from wider slices.
- A second slice, and the lighter pass the design gives a slice
  that adds nothing new.
- Whether the kinds of value and the ways each can be wrong are the
  right table: a first guess, shown only by the four defects. The
  table of which library questions ask the same as a grid's column
  is my reading of the 250, checked by the read above.
- Opus with the text, unless Sonnet does not hold. The real run on
  the owner's Mac.
