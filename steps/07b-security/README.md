# The security pass (after stage 7)

**Being tested (decision 50); not yet put to the owner.** The owner decided it
(decisions 46, 48, 49): a security pass of its own, right after the
questions, that adds to the same list so that everything is answered
together; nothing kad's security skill did is to be lost; and it is
to be done by script wherever a script holds.

## The pilot (2026-11-25, $3.14 of about $105)

Each case once. With the text: Sonnet 5 of 8, Haiku 4 of 8. Bare:
Sonnet 1 of 8, Haiku 3 of 8. kad's skill on the first case writes
its own document and none of this stage's, as expected: 0 of 1.

What it met, and what each became (decision 29):

- **The script took no row from a slice with nothing sensitive**
  (case 02, both models): what is wanted had to be a class of
  sensitive values, and that slice has none. What is wanted may now
  be a thing the documents name, or `nothing`, dismissed with the
  reason: two unit tests, and the text says so.
- **The stop was taken where the documents only did not say**
  (case 05, Sonnet): asked how people sign in, the session found no
  document saying who the office is, wrote nothing and put two
  questions to the user. The text now keeps the stop for what the
  documents say is not there or is out; where they do not say, it
  is a question and the stage goes on.
- **Two checks:** a pattern with a flag the tool does not read (the
  skip recorded in their words, case 04b, both models: the file was
  right); the public key written with a space, in a row of its
  class (case 03, Haiku: rightly dismissed).
- Haiku did not stop on case 06 where the documents say nobody
  signs in: left to the three runs.

## Three runs, then five with the final text (2026-11-25; $49.42 in all)

Three runs ($8.87, and $2.65 for four cases again): with the text
Sonnet 18 of 24 and Haiku 22 of 24; bare 11 of 24 and 10 of 24. The
stop was moved first and kept for what the documents say is out; a
reply to "what do you need from me" now says that nothing is needed.

Five runs of the eight cases with that text ($6.94), then five more
of the cases a change touched ($2.64):

| | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|
| Five runs | 36 of 40 | 37 of 40 |
| The cases changed, five runs again | 15 of 15 | 15 of 15 |
| A case | $0.16 | $0.015 |

Each of the seven failures was read (decision 29):

- **Four were a check's wording** ("The pass doesn't ask anything of
  you", "What I need from you: nothing now", "This stage doesn't ask
  you for it"; an offer made as "reply skip"): the checks were
  widened, and the cases pass 5 of 5 on both models.
- **A public key with no row of its own** (case 03, Sonnet, 1 of 5):
  it was never asked about as a secret, and nothing recorded that it
  had been looked at. The text now gives a public value a row of its
  own, dismissed with the reason: 5 of 5 on both models after.
- **Haiku did not stop** where nobody signs in (case 06, 1 of 5): it
  read "settled before the slice" as a claim and went on, with the
  point in its reply. 5 of 5 on the run after; nothing changed for it.
- **Haiku did not say there was little to attack** (case 02, 1 of
  5): one row asked, four dismissed, the counts said. Left.

No run answered a question, asked the user a preference, or wrote
`questions.md` itself.

## What it is

A session writes one small file, `security.md`, beside `kept.md`:

- **six facts about the slice**, each `yes` or `no` with its source
  (used in a browser; answers at a network address; calls another
  system; adds a component someone else wrote; more than one person;
  makes a value meant to be unguessable). Where the documents do not
  say, `yes`;
- **what someone who means harm would want**: one row for each pair
  of something wanted (a class of sensitive values) and something
  come through (a request, a screen, an address that receives), with
  the worst reached from there, asked or dismissed with the reason.

`questions/questions.py draw` then draws the questions again:

- 28 fixed questions, only for the facts that hold (`F.`), each
  resting on a requirement of OWASP's verification standard 5.0.0,
  one on kad's own documents;
- a question a row asked (`T.`);
- two more exits for every class of sensitive values (`X.`): a
  reply that succeeded, and where it is stored with every copy.

The script refuses a fact left out or without a source, a class
nobody is said to want, a thing nothing comes through and a name
`kept.md` does not have. The stage script names `security` as next
once the questions are drawn, and counts it done when the drawing
carries the mark of `security.md` too. The text is 116 lines
(kad's skill: 344).

## Set beside kad's skill, part by part (decision 26)

kad's `security-requirements` (344 lines), its persona and its table
of principles:

| What kad's skill does | Here |
|---|---|
| First response is questions to the owner: what is sensitive, who sees whose, obligations, what exists | Drawn for every slice at stage 7 (`W.`), answered from the documents first; the rest reaches the owner once, in the list |
| The threat pass: what an attacker wants, by name | The table's "Wanted", held by script to the classes `kept.md` lists |
| ... where untrusted input or identity crosses in | `kept.md`'s values and other things, each with its source by script; every other thing is come through or dismissed, by script |
| ... the worst reachable from each | The table's "Worst from there": the one part that is a session's reasoning |
| What was considered and dismissed, with the reason | `no: <reason>`, refused by script without one |
| A value public by design is not a secret | Kept (a case) |
| Each sensitive class traced to five exits | By script since stage 7; two exits added (a reply that succeeded, stored copies) |
| Prefer that the sensitive thing never enters | Stage 8: an answer |
| A value of the owner's file reaching the repository: scanned | Startup's `source.sh`; the readiness stage runs it |
| Given/When/Then, observable, the failure path covered, design notes apart, a count | Stage 8 |
| Forks put to the owner one at a time, approval before the document | **Different on purpose:** nothing asked here; one list at stage 14 |
| The slice cannot be made safe without something nobody scoped: stop, one recommendation, the slicer's to decide | Kept (a case) |
| A control with nowhere to live is a finding for the design | Stage 10 |
| Consulted mid-design on where a secret lives; a decision mid-build under a delegation | Not this stage: the design and the build |
| Little security surface: say so, write few | Kept (a case) |
| Edits only its own file | Kept, and `kept.md`'s lists where a thing is missing from them |
| The principles of least privilege, of identifiers that narrow a search, of supply chain | The library's `secrets` kind and the fact `dependency`; the build's reviews for the rest |

kad's two faults here are not carried: it edited other stages'
documents, and it once wrote a criterion without reading the two
documents that already broke it (the text says what to read first).

## What the stage must do

1. Write `security.md` with every fact, each with its source.
2. Say `yes` where the documents do not say.
3. Name what is wanted and through what by `kept.md`'s names; every
   class and every other thing in a row.
4. Dismiss with a reason; a value public by design is dismissed.
5. Draw with the command; never write `questions.md`.
6. Answer nothing: no control, fix, criterion or recommendation.
7. Ask the user nothing.
8. Say so when there is little to attack, and not pad.
9. Write nothing when the slice cannot be made safe as cut: say
   what is missing, what it forces, one recommendation.
10. Told to skip: once what it costs, offered again; on a second no,
    recorded in their words and every fixed question drawn.
11. After a change to the documents: `kept.md` first (stage 7), then
    this file for what the change brings, the other rows left.
12. Change no other document.

## Cases (eight; `eval/make_cases.py`)

| Case | Shows |
|---|---|
| 01 a provider, a credential, an address that receives | conditions 1 to 7, 12 |
| 02 little to attack | 8 |
| 03 a value public by design | 4 |
| 04a told to skip, 04b the user insists | 10 |
| 05 asked what is needed | 7 |
| 06 it cannot be made safe as cut | 9 |
| 07 a criterion added after | 11 |

Unit tests: 13 for the script's part (`questions/test_questions.py`),
7 for the stage script (`startup/test_stage.py`), 2 for the driver
(`e2e/test_run.py`), 9 for the cases' fixtures and checks.

## Arms, models, bar

- **Arms:** bare (the report and its commands, nothing for this
  stage); kad's `security-requirements` on the first case and on the
  two real plans; our text.
- **Models:** Haiku and Sonnet 5.5, three runs bare and with the
  text, then five on each with the final text (decision 38).
- **Bar:**
  - every case in every run: 40 of 40 at five runs;
  - no run answers, asks the user, or writes `questions.md` itself;
  - on the two real plans, three runs each: every security concern
    kad's two documents name is asked in every run, the six that
    exist only once a lock file is chosen left out (they were 8 of
    16 and 19 of 30 before this pass);
  - the reliability concerns asked before are still asked;
  - nothing kad's skill produces on the same slices is absent from
    the questions: read, with the reasons (no model judge);
  - stage 7's ten cases still pass five runs with the grown library.

OWASP's standard is not a measure here: the questions were built
from it (decision 49).

## Cost

A case is taken at $0.25 on Sonnet (it reads the documents and
`kept.md` and writes a small file) and 2 cents on Haiku.

| What | About |
|---|---|
| Built so far: script, stage script, driver, text, cases, unit tests | free |
| **Pilot:** each case once on Haiku and Sonnet, bare and with the text; kad's on one; one real run | **$6** |
| Three runs: bare and ours on both models | $13 |
| One round of tuning | $5 |
| Five runs with the final text, both models, and half again for what a late change stales | $16 |
| Stage 7's cases five times with the library of 290, both models | $20 |
| Every earlier stage once with it on trial | $11 |
| The two real plans: stage 7 again (their kept files predate the new kinds), then this pass, three runs each; kad's skill once on each | $8 |
| The four examples once from the first message through this pass | $26 |
| **In all** | **about $105** |

That is twice the $50 first guessed: $20 of it is stage 7's own
re-run for the grown library, and $26 the examples, which cost $20
for three last time and cannot start from kept documents (none are
kept after the questions, and two texts have changed since). The
examples pass is over $15 and is said again before it is run.

## What a pass will not show

- Whether the added questions are answered well: stage 8.
- A slice with sign-in of its own, or files taken in: the made-up
  playhouse and the two real plans have neither, so the kinds
  `sign-in` and `file-intake` are triaged but mostly dropped.
- Whether six facts are the right six: a first cut from OWASP's
  chapters and kad's documents.
- The 141 requirements of the standard placed by their section
  titles and not read line by line.
