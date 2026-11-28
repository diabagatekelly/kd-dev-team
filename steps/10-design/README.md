# Stage 10: the design

**Proposed (2026-11-28). Built free; nothing paid has run, and no
session has run any of it.** Its measure, its test and its cost are
below, for the owner's yes. The design document
(`design/planning-phase.md`, section 5) says this stage has no
measure until one is agreed with them: it is the first point.

## What it is

The slice says what ships; the answers say what it does in every
case and what is still not known. This stage decides how it is made
up, before any code: its parts, which of them must not know what
stands behind them, what crosses between them, and which part is the
home of each thing the earlier stages settled.

- **The session's judgement is one file,** `NNN_design.md` in the
  slice's folder: an order of importance, a block a part (`C1`), a
  boundary (`B1`) and a decision (`D1`), and six short sections.
- **A script does the rest.** `designing/design.py next` lists what
  has no home yet, sixty at a time; `draw` refuses what does not
  hold and draws `NNN_designed.md`: each part with the criteria it
  is the home of in full, the decisions that earn a record, each
  order of events of what keeps two things apart, what is leaned on
  and not known, what waits for the owner and what goes back. The
  stage script counts the stage done while that drawing carries the
  mark of the answers' drawing, the open facts' and the design, no
  decision of the design waits and nothing goes back.

**What has a home** is what kad's design never had to read:

| Settled before | Where it is read | Its home |
|---|---|---|
| a criterion of the slice | the slice | a part's `Home of` |
| an answer that is chosen, with or without a criterion | the answers | a part's `Home of`: what is only said is then read by the builder |
| a fact with a criterion; a decision the owner took | the answers | the same |
| an open fact, with what the slice does either way | the open facts | the part that does it |
| a state of a lasting thing | research's `states.md` | the part that `Holds` it |
| a class of sensitive values | the questions' `kept.md` | every part that `Sees` it |
| a thing committed to | the approach | the one tactical part that `Isolates` it |

Or a line under `## No home`, with why. On the two real plans, asked
of their last stage 9 runs for nothing: 111 and 180 things.

## What is a script and what is a text

| Part | Done by |
|---|---|
| What has no home yet; a home given to nothing the slice has; `No home` with no reason | script |
| A strategic part that names a thing committed to, or uses a tactical part; a boundary owned by the side behind it; what crosses naming the thing | script, refused |
| A thing committed to that no part isolates, or that a part speaks of leaning on nothing | script, refused |
| A fact leaned on that its research document does not have, in words it does not hold, or that is an open point; an open test that is not one | script, refused |
| What is leaned on and not known, with nothing said of either way | script, refused |
| A part named for a technical role (handler, service, manager, ...) that is not the wiring | script, refused |
| Code, a file of the code, a signature (but for code already there, named as it is) | script, refused |
| A decision with no way not taken, no cost, or a check that is not yes or no; which decisions earn a record (three yes) | script |
| What keeps two things apart with an order of events missing; a hole (both go on, nobody would know, stuck until someone sees to it) in a decision that is chosen | script, refused |
| Answers that settle a question about two things at once, and nothing kept apart | script, refused |
| `Tests` that do not fake a thing committed to; nothing said of later slices, of importance, of whether anything runs at once | script, refused |
| Whether the stage is done, how many decisions wait, what goes back; the command that draws a finished design again | stage script |
| Which parts there are, which side each is on, what is strategic; what a part leans on; what keeps two things apart and what each order leaves; what is the owner's; neither too much nor too little | text (240 lines) |

43 unit tests for the script (`designing/test_design.py`), 10 for the
stage script, 2 for the driver, 16 for the cases.

## Set beside kad

kad's `architecture-design` (583 lines, with `adr`) and the
principles it was built from
(`kad-dev-team-plugin/.synthesis/software-architect.md`). Each is
carried, or not, with why.

| kad's principle | Here |
|---|---|
| Importance is the harm of a defect, stated for this slice, not a fixed list of layers | carried: `## Importance`, required; the text says this slice's own order |
| Strategic or tactical: would it change if the store, framework or service were swapped | carried, in those words |
| Dependency Rule; an interface lives with its caller | carried, and held by script: a strategic part uses strategic parts and boundaries it owns |
| The wiring may know both sides | carried: a third side, `wiring` |
| Look in both directions: what a shared type itself depends on | carried, as one sentence |
| A dependency is not always an import: a shape distorted to match the store or provider | carried, as one sentence; a script cannot see it |
| Good Fences: only plain data crosses; a translation at the edge | carried; the script refuses what crosses naming the thing committed to |
| Invasive Species: a library isolated by how costly it is to leave | carried for what the approach commits to (one part isolates it, by script). The tiers for a library are not: no library is picked here (below) |
| Screaming Architecture: strip the technical word, does the product remain; do not invent a name; wiring excepted | carried; the names that fail outright are refused by script |
| YAGNI both ways; never against a boundary the Dependency Rule needs; two real cases now | carried, as "neither too much nor too little" |
| Conceptual only: no paths, signatures or code | carried, by script |
| Technology at a boundary: the deferral test | carried: `Technology: forced / not forced`, each with its reason |
| **A boundary that forces a technology is decided here** | **changed:** the design says what the slice `Needs` of whatever stands behind a boundary; the stack stage picks against it. A technology picked here would be a belief about a dependency nobody researched (principle 2 of the design document) |
| Every criterion and failure path has a home; states have homes | carried and widened (the table above), by script, where kad's gate matched half of a path's words anywhere in the document |
| Check it the way the gate will, before saving (incident 47) | the script is the gate: nothing is drawn that it refuses |
| Two things at once: the interleavings before the decision | carried: five orders, each required by script; a hole in a chosen decision refused; `## At once` required of every design, and refused as "nothing" where the answers settle a question about two things at once |
| The tests and fixtures line (incident 24) | carried: `Real:` and `Faked:`, the thing committed to among the faked, by script |
| Kept for later slices | carried; the script names the slices that build on this one |
| Fixing a violation found in existing code: locate, the boundary, now or later as a decision | carried, shorter: `## Already there` |
| Check the architecture map first (`map-query`) | not yet: no map exists before a build. A project with code has the code read. Owed when the build makes a map |
| **Approval for every real decision, one at a time** | **not carried.** The design document's section 4: a technical problem that has been identified is solved, recorded and can be overturned. kad's own count: 108 of 149 questions were design decisions and technical forks taken as offered, and its incident 42 says the same. What is the owner's is brought once (the second point below) |
| A stage is the expert and pushes back once | carried: asked for a structure the principles argue against, the slice is designed as recommended, the cost said once; if they insist it is theirs, recorded in their words |
| A consequence that changes a confirmed requirement is handed back, not accepted here | carried, and widened: `## Goes back`, to the requirements, the slice, the approach, research or the answers; the stage is not done while one stands |
| A decision that clears three checks becomes an ADR, written by another persona | changed: every decision is recorded where it is taken, with its three checks answered yes or no; the script draws those with three yes as records of their own. Where they are kept for good is the planning pull request's (stage 14) |
| A runtime-safety question is put to the security persona | not needed: the security pass's criteria are answers, and each has its home here |
| A mid-build decision under a delegation | the build's: owed to the first build stage |
| A file the owner provides is described, never quoted | already every stage's, in the routing table |
| The review's principles (smells, severity, legacy code, a balanced stance) | the review's, when it is built |

## What was put off to this stage, and what stages 8 and 9 left

| Left | Here |
|---|---|
| A dependency the user did not name has no way back to research | Two cases. Something the slice needs from outside that the approach lacks goes back to the approach (`## Goes back`), which has its way to research. A technology behind a boundary is not picked here: the design says what is needed of it, and the way back from a pick is the stack stage's to give |
| kad's three checks for whether a decision earns a record | on every chosen decision, by script |
| Nine concerns of the second plan that wait for a design to be chosen (a lock file, a claim, a retry during the close) | the five orders of events, required of whatever keeps two things apart; counted on the real plan |
| Concerns said in an answer with no criterion | every chosen answer has its home, criterion or not, and is drawn under its part |
| What a lock leaves after a crash; a close in progress | `Crash:` a line a step; a start and a close still in progress named in the text among the two things at once |
| An answer cut back to "the product treats it as", still leaning on the thing | `Leans on: unknown:` with `Either way:`, counted and drawn; whether a session finds them is case 07 and the read of the real plans |

## What the stage must do

1. Everything settled before has a home, or a reason for none.
2. One tactical part alone knows each thing committed to; what the
   design says of it rests on its research's words or an open test.
3. What fails, and each open fact, has a home, with what is left.
4. What keeps two things apart is walked through every bad order
   before it is chosen; a hole is closed or is the owner's.
5. A decision is taken and recorded, with what was not taken and
   what it costs; never asked, unless it is the owner's.
6. Nothing for a case that may come; a boundary where two real
   cases are.
7. Asked for a structure the principles argue against: designed as
   recommended, the cost said once; their word then stands.
8. What is another stage's goes back and is not settled here.
9. What is leaned on and not known is named, with what is done
   either way.
10. In a project with code: read first, used under its name, a
    fault located and decided.
11. The owner's decisions of the design are brought once, and
    recorded in their words.
12. Told to skip: once what it costs, then recorded and drawn.
13. Changed after: only what the change brings.

## Cases (fourteen; `eval/make_cases.py`)

The made-up playhouse's slice that takes a payment through a
provider, as the tests of open facts leave it: two tests open, one
decision the owner took, and six answers that matter, two of them
failures with no criterion.

| Case | Shows |
|---|---|
| 01 a slice designed | 1, 2, 3, 5 |
| 02 two things at once | 4 |
| 03 a lock the user proposes | 4, 7 |
| 04a a part for a case that may come; 04b the user insists | 6, 7 |
| 05 a need from outside the approach lacks | 8 |
| 06 asked for what is out | 8 |
| 07 leaned on and not known | 9 |
| 08 a project that already has code | 10 |
| 09a skip the stage; 09b the user insists | 12 |
| 10 the answers changed after | 13 |
| 11a the owner's decision is brought once; 11b the owner decides | 11 |

## The measure, proposed

No key existed for a design: the benchmark counts defects that
reached a build, and none of the 43 of the two real builds was ever
sorted by cause. So, before any run, each was read for whether a
structure could have prevented it, and the ones that could are a
key, kept privately and not changed after a run (the audit
repository, `10-design/README.md`).

- **The key: twelve items for the first plan, eight for the
  second.** By kind: a failure no part owned (a start that cannot go
  on, a fault inside a request, access gained at the provider and
  not kept); two things over one state with a bad order (two copies,
  two first connects at once, a claim taken at the wrong moment); a
  provider's own shape or error let through; a rule with its home in
  the wrong place; something a later slice needed. Defects of a
  wrong belief about the provider alone, of wording or of a
  setting's spelling are not in it.
- **Counted by reading, with reasons, no model judging:** an item is
  held (a part is its home and what is left is said), part, or
  absent.
- **kad's own designs, counted the same way, are the mark:** 1 held,
  4 part, 7 absent of twelve; 1 held, 5 part, 2 absent of eight.
- **The nine concerns** of the second plan that no run of stages 7
  to 9 could ask: each answered in an order of events, said
  elsewhere, or not there.
- **What reaches the owner:** kad put eight and seven decisions of
  its two designs to the owner or took them as recommended.

## Three points that are the owner's

1. **The measure above, and its bars** (below). The other way is to
   judge a design only by its build, which no stage can do yet.
2. **The design asks nothing about structure, and may bring a
   second, short list.** Decision 53 has the owner's list brought
   once, before the design. A design can still find something that
   is theirs: a cost in money, a risk no structure removes, what
   cannot be taken back once people's data is in it. As built, those
   are gathered and brought once when the design is drawn, and the
   stage is not done while one waits. The other way: they join the
   owner's list of stage 14, and the design is called done with them
   open.
3. **The cost below**, and the pilot first.

## Arms, models, bar

- **Arms:** bare (the report and its commands, nothing for this
  stage) and our text. kad's skill is not an arm of the cases: it
  asks approval of every decision, which every check here would
  fail by design; its two designs are the mark on the real plans.
- **Models:** Haiku and Sonnet 5.5. Bare once, in the pilot, and
  three times only if it passes more than a third of the cases
  there; the text three times, then five with the final text
  (decision 38). Opus only where Sonnet with the text does not hold.
- **Bar:**
  - every case in every run: 70 of 70 at five runs;
  - in no run a file of code written, an earlier document changed,
    the drawing written by hand, or a technical choice put to the
    user;
  - on the two real plans, three runs each from the same stage 9
    run: drawn within five turns; **every item of the key about two
    things at once held in every run** (three and one); **of the
    rest, at least half held in every run, and none absent in all
    three**; of the nine concerns, at least six answered in every
    run;
  - at most two decisions a run brought to the owner, each read:
    none that is a technical choice;
  - what is leaned on and not known, read: none that a research
    fact does say;
  - whether the three runs of a plan agree (the parts, the
    boundaries, what keeps copies apart): reported with no bar, this
    being its first count;
  - every earlier stage's cases still pass once with it on trial.

## Cost

| What | About |
|---|---|
| Built so far: script, stage script, driver, text, cases, unit tests, the private key | free |
| **Pilot:** each case once on Haiku and Sonnet, bare and with the text; one real run on each plan | **$16** |
| Three runs with the text on both models | $16 |
| One round of tuning | $10 |
| Five runs with the final text, both models, and half again for what a late change stales | $40 |
| Every earlier stage once with it on trial (eleven stages): the stage script changed; it is also the pass owed since stage 9's last changes | $17 |
| The two real plans, three runs each, before and after the tuning | $42 |
| The four examples from their kept answers through stage 9 and the design (stage 9's two unrun sentences run with them) | $18 |
| **In all** | **about $160** |

A case is guessed at 35 cents on Sonnet (the answers' was 15, the
open facts' 20, and this one writes more), a real run at $3.50: the
pilot gives the real figures, reported before anything else runs.
The last three stages ended a quarter over what was first agreed;
the total is said again before it passes $160, and before any pass
over about $15.

## Owed, and not in this proposal

- **No example takes a provider through stages 6 to 10.** A fifth
  example that does would cost about $20 from its first message. The
  two real plans already carry a real provider through every stage,
  each stage on what the one before wrote; the example would add
  only the scripted user's path. Not recommended now.
- **A library question for an identifier that changes when a
  connection is made again** (decisions 44 and 58): the library is
  changed with the next stage that runs the questions' cases five
  times, which this one does not.

## What no session has run

All of it: the text, the cases, the script's refusals as a session
meets them, a real plan, an example. In particular nothing shows yet
whether a session can give 111 or 180 things a home in one sitting,
sixty at a time.

## What a pass will not show

- Whether a build made from the design has fewer structural
  findings: the build.
- Whether the parts are the right ones: the script holds direction,
  homes and words, not judgement; that is read on the real plans.
- Whether a technology the stack stage picks meets what a boundary
  needs: stage 12.
