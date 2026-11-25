# Stage 8: the answers

**Being tested (decision 53: about $125, the pilot first).** The
owner agreed its three points on 2026-11-25.

## What it is

The questions are drawn (stage 7) and the security pass has added
its own. This stage settles every one of them and writes the
criteria that follow. A real slice draws about 700 questions and a
small one about 280, so the unit of work is not the question:

- **an answer settles many questions.** A session writes one file,
  `NNN_answers.md` in the slice's folder: a block an answer, of one
  of five kinds, with the ids of the questions it settles
  (`L.entry.*`, `S.thing.state.*` take a whole group);
- **a script keeps the count.** `answers/answers.py next` lists the
  questions no answer settles yet, sixty at a time; `draw` refuses
  what does not hold and, once none is left, writes
  `NNN_answered.md` beside it: the criteria, the owner's list by
  harm, what is to be tested by harm, and what was chosen without
  asking. The stage script counts the stage done while that drawing
  carries the mark of the questions and the answers as they stand.

The five kinds, asked in this order:

| Kind | When | What it must say |
|---|---|---|
| `fact` | a document of the slice says it | the document, by name: a criterion, a research fact, a line of the requirements |
| `not here` | the question does not arise in this slice | why, in a line |
| `test` | it turns on how something outside behaves, and no page read says | the test that would settle it, and the harm if the guess is wrong; no criterion on the guess |
| `owner` | a rule of their own field, taste, a risk, cost or obligation to accept, what is in or out | two options or more, one recommended, what happens if it is left, the harm; no criterion until they decide |
| `chosen` | everything else: good practice applied, a technical problem solved | what is chosen, and why |

A decision the owner takes is recorded on its answer (`Decided:`,
in their words, with the date), its criteria are written, and the
answers are drawn again: the report keeps that command whatever
stage is next.

## What is a script and what is a text

| Part | Done by |
|---|---|
| Which questions are still unsettled; that each is settled once | script |
| A question the drawing does not ask; an answer that settles nothing | script, refused |
| A fact that rests on no document of the slice | script, refused |
| A decision for the owner with one option, no recommendation, or nothing said of leaving it | script, refused |
| A criterion on a guess or on a decision not yet taken | script, refused |
| A criterion that is not Given, when, then; one under no item of the slice | script, refused |
| A wait, a retry or a giving up with no number (kad's `numbers-on-waits`) | script, refused |
| The owner's list and the tests, ranked by harm; the choices in one record | script, drawn |
| Which kind an answer is; what it says; which questions it truly settles; the criteria's words | text (114 lines) |

35 unit tests for the script (`answers/test_answers.py`), 5 for the
stage script, 2 for the driver, 9 for the cases.

## Set beside kad's skills, part by part (decision 26)

kad's `reliability-requirements` (392 lines), `security-requirements`
(344) and `acceptance-criteria` (136) did this step.

| What kad's skills do | Here |
|---|---|
| Ask the owner first (an hour unavailable, a target, who notices; sensitive data, users, obligations) | drawn as the seven questions of every slice (stage 7); answered from the documents where they say, the owner's otherwise, on their one list |
| Failure modes, and the decision each leads to | the library's questions and the two grids (stage 7); each settled by an answer |
| Threat pass, the five exits | the security pass (07b); each line settled by an answer |
| Given/When/Then, outcome not mechanism, success and failure paths | the text's criteria rules; the form is checked by script |
| Assert absence for a sensitive value | the text; one case checks it |
| A number on every wait, or "unbounded, owner approved" | script, refused |
| A permanent refusal names a way out | the text; dead ends come drawn from research's states |
| Forks with a recommendation and what was rejected, approved before written | `owner` answers: options, recommended, if left; never marked decided by the session |
| "Proportional: few failure modes, few criteria" | an answer settles many questions; `not here` with its reason |
| Design notes: wording, record fields | `Says`, not criteria |
| Edits the slice's placeholder with a pointer | the drawing is the pointer; no other document is changed |
| `readiness_check.py` on waits and unusable replies | `answers.py draw` |
| Stop and hand back when the slice cannot hold | left to research, which already sends an impossible criterion back |

Not carried: asking the owner before writing (kad asked five or six
questions first on the same documents, 2026-11-25); the owner's
decisions one at a time through the conversation.

## What the stage must do

1. Every drawn question is settled by exactly one answer.
2. A fact rests on a document of the slice, never on belief.
3. What no page says about an outside system is to test, with no
   criterion on the guess.
4. A technical solution or good practice is chosen and recorded,
   never asked.
5. What is the owner's has options, a recommendation, what happens
   if left, and its harm, and is not asked in the conversation.
6. A criterion is Given, when, then, of an outcome; a sensitive
   value by its absence; a wait with its number.
7. Nothing else is changed; the drawing is never written by hand.
8. Asked what is needed: nothing now.
9. Told to skip: once what it costs, then recorded and drawn.
10. A decision the owner takes is recorded in their words, against
    the recommendation too, and its criteria written.
11. Questions changed after: only what the change brings.

## Cases (seven; `eval/make_cases.py`)

Two made-up slices. The one that quotes a price draws 29 questions
and is answered from nothing. The one with a provider draws 387 and
starts with answers "written before" for all but the few a case is
about: 387 from nothing in every run would cost what an example
costs.

| Case | Shows |
|---|---|
| 01 a small slice from nothing | 1, 2, 4, 5, 6, 7 |
| 02 the kinds told apart (eight questions left) | 2, 3, 4, 5, 6 |
| 03 asked what is needed | 8 |
| 04a skip the stage; 04b the user insists | 9 |
| 05 the owner decides against the recommendation | 10 |
| 06 the questions changed after | 11 |

## Three points that are the owner's

1. **When the owner's list is brought.** The design has it at stage
   14, with the planning pull request. But the design, the screens
   and the stack (10 to 12) are then made on what was recommended,
   and done again where the owner decides otherwise. Recommended:
   brought once, after the tests of open facts (stage 9), before
   the design. Until then this stage only writes the list.
2. **How many decisions a slice may bring.** The earlier experiment
   marked 20 and 26 for the owner on the two real plans; kad asked
   149 questions over planning and build. Recommended bar: at most
   12 a slice on the two real plans, each read for whether it is
   truly one of the four kinds.
3. **The cost below**, and the pilot first.

## Arms, models, bar

- **Arms:** bare (the report and its commands, nothing for this
  stage) and our text. kad's three skills are not an arm: they ask
  the owner first and write other documents; they are set beside
  ours on the two real plans, read with reasons (no model judge).
- **Models:** Haiku and Sonnet 5.5, three runs bare and with the
  text, then five on each with the final text (decision 38).
- **Bar:**
  - every case in every run: 35 of 35 at five runs;
  - no run asks the user a preference or writes the drawing itself;
  - on the two real plans, three runs each: every question settled;
    no fact resting on belief, read in a sample of thirty a run; the
    owner's list within the number agreed, each item one of the
    four kinds;
  - **research's condition (decision 44):** each fact of the two
    keys that a research run lacked is counted again; any still
    missing is named with its kind;
  - kad's concerns for the same slices (07b's read): each has a
    criterion, a test or an item on the owner's list; the nine that
    wait for a design are named;
  - every earlier stage's cases still pass once with it on trial.

## Cost

| What | About |
|---|---|
| Built so far: script, stage script, driver, text, cases, unit tests | free |
| **Pilot:** each case once on Haiku and Sonnet, bare and with the text; one real run on one plan | **$9** |
| Three runs: bare and ours on both models | $15 |
| One round of tuning | $7 |
| Five runs with the final text, both models, and half again for what a late change stales | $18 |
| Every earlier stage once with it on trial (now nine stages) | $14 |
| The two real plans, three runs each, from the security pass's runs | $21 |
| The four examples once from the first message through this stage | $40 |
| **In all** | **about $125** |

The examples pass is over $15 and is said again before it is run.
From kept documents it would be about $10 instead of $40; the
standing rule is the first message.

## What a pass will not show

- Whether the tests of open facts change the answers: stage 9.
- Whether the criteria are enough to build from: the build.
- A slice of 700 questions answered from nothing costs a session
  about $3 by estimate; the pilot's real run gives the real figure.
