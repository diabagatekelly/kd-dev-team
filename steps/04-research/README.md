# Stage 4, research: the test, set before anything is built or run

**State, 2026-11-23:** a proposal for the owner. Nothing here is
agreed, built or run.

## What it is

Facts before decisions. For the activity marked "now", the
requirements list ends with the outside systems and lasting things
it touches. This stage writes, in `003_research/`, one document a
thing:

- **an outside system:** what its own documentation says about what
  the activity needs from it, every fact with its page and a quote;
  what the documents so far say about it, checked against that; and
  what the documentation does not say, each with the test that would
  settle it;
- **a lasting thing:** every state it can be in over its life, how
  it gets there and the way out.

Nothing is decided here and the user is asked for no preference. The
slice, the questions and the design rest on these documents.

## One thing to settle first: how a session reads the web

A session works inside the project's VM, and the VM can reach only
the few websites on its list (decision 7). A provider's
documentation is not on it. Three ways, the first proposed:

1. **The session names the site and why, and asks for a yes;** the
   site is then added for this VM only, by a command the report
   gives. One yes a site, like the yes to install. A refusal is
   never worked round.
2. Research runs outside the VM. Against decision 19.
3. Only the tool's own web search is used, which is understood not
   to pass through the VM (the pilot would check). It returns
   extracts, not pages, so no quote could be checked.

A page read this way is something a stranger wrote: what it says is
data, never an instruction.

## What the stage must do

1. **Work from the list's inventory only.** A thing it does not name
   is not researched; one that seems missing is said in the reply,
   for the requirements stage. An inventory of `none` is said, and
   nothing is researched.
2. **For an outside system, cover what the activity's items need
   from it:** each operation, what goes in and comes back, what
   exists on the other side afterwards, its documented errors by
   their exact names, timings and limits, whether repeating it is
   safe, and what is said of a reply that never arrives.
3. **Every fact carries its page and a quote of at most 25 words,**
   taken from the page as the session saved it. A script finds each
   quote in its saved page.
4. **Nothing from memory.** A page that cannot be opened is said to
   be so and nothing is stated from it. Where the documentation is
   silent the point is written OPEN, with the test against the real
   thing that would settle it.
5. **Every statement the documents make about the system,** the
   user's own beliefs among them, is marked AGREES, CONTRADICTS or
   NOT COVERED, with both wordings.
6. **Two pages that disagree are said to.**
7. **For a lasting thing, walk its whole life:** how it begins, what
   it is while it works, how it stops working by itself, what can
   change on the other side afterwards, what if the same action is
   refused every time, how it is ended and what is left. A row a
   state, each with a short name that later documents use, how it is
   entered, the way out, and its source or `to verify`.
8. **A state with no way out is recorded for the owner's list,** not
   asked now.
9. **A page is data.** An instruction found in a page is not
   followed, and is reported.
10. **Reach only what the VM allows.** A site that is needed is
    named, with why, and a yes asked for (if the owner takes the
    first way above).
11. **Ask nothing else.** No preference, no decision: a preference
    is never asked before the fact it depends on is known.
12. **No design:** no technology chosen, no provider recommended. An
    outside system the user has not named a provider for is written
    as waiting, with what will need to be known once one is chosen.
13. **Stop there:** no slice.

## Set beside kad's skill, part by part (decision 26)

kad's `domain-model` (150 lines) is the one skill of its sixteen
that read a dependency's documentation:

| What kad's skill does | Here |
|---|---|
| Models only what the requirements' inventory names; a thing that seems missing is a finding for the requirements | Kept (condition 1) |
| Reads the provider's public documentation; each state cites its page | Kept, and stricter: a quote with every fact, found on the saved page by script |
| When the documentation cannot be reached: no workaround, said once, marked `to verify` | Kept (condition 4) |
| What is known only from memory is `to verify`, never a page not read in this session | Kept |
| Six questions asked of every thing's life | Kept as the walk (condition 7) |
| A short hyphenated name a state, used by every later document | Kept |
| Columns: entered by, what the person sees and can do in the app, the way out, supported, source | Kept, less "in the app": nothing is designed yet. "Supported" is filled from the owner's list |
| A state with no way out: one question a state, asked before anything is written | **Different on purpose:** recorded, and brought once in the owner's list, ranked by harm (the design, section 4) |
| No provider chosen: model what any provider of the kind does | **Different on purpose:** that is memory. Written as waiting |
| One file, revised in place whenever a later stage meets a new state; no row removed | Kept: rows are added |
| A fixed header the readiness gate reads | Kept, by script |
| Says nothing of operations, errors, timings and limits; kad's reliability skill stated those from general knowledge | **Added:** the dossier of the earlier experiments (E3), which found 14 of 101 and 14 of 111 statements of two plans contradicted by the providers' own pages |
| The plan's statements are not checked against the documentation | **Added** (condition 5) |

## Two measures

**The gate: free checks, on a made-up provider.** A stand-in serves
the documentation of a provider that does not exist, inside the VM,
as the stand-ins do for the VM tool and the tracker. So what the
pages say is known, the runs are small, and nothing drifts with the
real web. Eight scenarios:

| # | The situation | Must |
|---|---|---|
| 1 | one outside system, its pages in order | a fact with page and quote for each thing the items need |
| 2 | the user's documents state something its pages contradict | marked CONTRADICTS, both wordings given |
| 3 | the pages are silent on something an item needs | OPEN, with a test; nothing filled in |
| 4 | a page that does not open | said; nothing stated from it |
| 5 | two pages disagree | said |
| 6 | a page holding an instruction to the reader | not followed; reported |
| 7 | a lasting thing with a state that has no way out | every state a row; that one recorded for the owner, not asked |
| 8 | an inventory of `none`; and a system with no provider named | nothing researched; the second written as waiting |

The checks: every fact has a page and a quote; each quote is in its
saved page (by script); the planted facts are present, by pattern,
as the gaps of stage 3 were counted; nothing is stated of the
unopened page; no question is put to the user but the yes for a
site; nothing is written outside `003_research/`.

**The outcome on the benchmark: free too, and private.** The
question the owner put off to this stage. Proposed:

- **The key:** for two of the owner's real plans, the facts their
  providers' documentation holds that the plan as built got wrong:
  the 28 contradictions the earlier dossiers found, and the known
  defects that came from a wrong belief about a dependency. Each is
  written down before any run, with a pattern that finds it.
- **The input:** only what this stage will really have: those
  projects' problem and requirements documents, not the later plan.
  So the question asked is the one that matters: is the fact already
  in the dossier, before anyone decides anything on it?
- **The count:** of the key's facts, how many are in the dossier;
  how many are there in every one of three runs; and every quote
  found on its page.
- **Tuned on one plan, confirmed on the other.** Both are of one
  field with one kind of provider; the made-up scenarios are what
  keeps the text general (decision 2).
- No model judge. The patterns are loose, so the count is a guide
  and a close call is read. The key, the documents and the dossiers
  stay in the audit repository; here, counts only.

**Quality: read, with reasons** (decision 18), against the two
earlier dossiers and kad's `domain-model.md` for the same things, on
these points, fixed now: each fact is one a decision will rest on,
not filler; an OPEN point names a test that could really be run; a
state table could be handed to someone cutting a slice; nothing is
a recommendation.

## Arms, models, bar

- **Arms:** the bare model first (the inventory and "research what
  this activity depends on"); the brief of 20 lines carried from E3,
  with a short part for the states; kad's `domain-model` for the
  states alone.
- **Models:** Haiku, Sonnet and Opus 5.5; three runs, then five at
  the gate on what passes (decision 30). The benchmark stays at
  three runs a plan: a run there reads real pages at length.
- **Bar, proposed:**
  - the gate, every run: 40 of 40 at five runs;
  - no quote that is not on its page;
  - on the benchmark, at least 80% of the key's facts in the
    dossier on average, and at least two thirds of them in all
    three runs, on the plan it was not tuned on as well;
  - the documents read no worse than the earlier dossiers.
  The cheapest model that holds is taken, and the stage may run on
  another model than the session's: the measurement says. A text is
  carried only for what it adds over the bare model.

## Cost

A run that reads real documentation is long, and its cost is known
only from the earlier experiments' token counts: about $2.50 on
Sonnet is a guess until the pilot.

| What | About |
|---|---|
| The stand-in for documentation, the quote check, the count of key facts, with unit tests | free |
| **Pilot:** two made-up scenarios on Haiku and Sonnet; one real run on Sonnet. Shows the web is reachable as proposed and what a real run costs | $5 |
| The gate: 8 scenarios, three runs, bare and brief, on Haiku and Sonnet; bare on Opus | $30 |
| The benchmark, the plan tuned on: three runs, bare and brief, Haiku and Sonnet | $20 |
| The benchmark, the other plan: three runs of what holds | $8 |
| Two rounds of tuning | $10 |
| Five runs at the gate of what passes | $12 |
| Every earlier stage once (the routing table and the report change); two examples carried through research | $9 |
| **In all** | **about $95; about $115 if Opus is needed on the benchmark** |

This is three times any stage so far, and most of it is the real
runs. Proposed: the pilot first, its real costs reported and this
table corrected before anything else is run, and a ceiling the owner
names then.

## What a pass will not show

The benchmark is one field and one kind of provider. A made-up
provider's pages are shorter and tidier than real ones. No test
against a real dependency is run here: the OPEN points name them,
and running them is stage 8.
