---
name: design
description: Decide how the chosen slice is made up before any code exists - its parts, what crosses between them, where each criterion, open fact and state has its home, and the decisions taken on the way. Use when the startup report names "design" as the next stage, when the user answers anything this stage said or decides something on the design's list, when they ask for a structure of their own, and when the user says to skip the design.
---

# Design

The slice says what ships. The answers say what it does in every
case, and what is still not known. This stage decides how it is made
up: which parts there are, which of them must not know what stands
behind them, what crosses between them, and which part is the home
of each thing already settled, so that none of it is left to whoever
builds it.

Your judgement is one file, the design, at the path the report
names. A script says what has no home yet, refuses what does not
hold, and draws `designed.md` beside it. You never write that
drawing. The file is written and changed with your file tool,
whatever the shell says of the folder.

Say how the slice is made up, never how it is written: no code, no
file of the code, no signature. A structure stays true when the code
changes; a line of code in a design is out of date the day it is
built.

**Read first.** The chosen slice and the set it is from, the
requirements' limits, the approach, every research document,
`states.md`, `security.md`, then `answered.md` and `tested.md`: the
criteria, what the owner decided, what was chosen, and each open
fact with what the slice does either way. Then the report's `next`
command: it lists everything settled that has no home yet, sixty at
a time. Where the project already has code, read what the slice will
touch before naming anything new: a part that is already there is
used, under the name it has.

**Importance, before any part.** Order the slice's concerns by the
harm a defect there would do, most important first, under `##
Importance`: this slice's own order, not a usual one. Then for each
concern ask: if the store, the framework or the outside service were
swapped, would it change? No: it is strategic, and knows none of
them. Yes: it is tactical, and can be swapped.

**A part.**

```markdown
## C1: <named for what it is in the product>
Side: strategic | tactical | wiring
Does: <what it is responsible for>
Home of: renew-and-pay / 1, A12, A20-A24, T2
Holds: a renewal payment: pending, settled
Sees: credentials
Uses: C2, B1
Implements: B1
Isolates: PayRight
Leans on: payright F6 "<its document's own words>"; T2
```

- **Its name** is a thing or an act of the product. Take away a word
  like handler, controller, service, manager, repository or utils:
  if nothing of the product is left, the part has no reason of its
  own to exist yet; join it to the part it serves. Only `wiring`,
  which makes the parts and hands each what it uses, keeps a
  technical name.
- **A strategic part uses only strategic parts and boundaries it
  owns.** It never names a thing the slice is committed to, and
  nothing of that thing's shape is in what it holds: a field that is
  there only because the provider or the store has it is the same
  fault with no name to give it away.
- **One tactical part isolates each thing committed to** and is the
  only part that knows it. It turns what the thing says into the
  product's own words, and a failure into one of the product's own
  outcomes; nothing of the thing's own, least of all an error that
  carries a request, goes further in.
- **`Home of`** names what the part is the home of: a criterion of
  the slice, an answer (its criteria, and what it says the product
  does where it has no criterion: that is read by nobody else), an
  open test. **`Holds`** names the states of a lasting thing it
  keeps and moves. **`Sees`** names each class of sensitive values
  that passes through it: the fewer parts, the better.
- **What the person sees is a part too.** Where the slice has a
  screen, a command or a message it sends, one tactical part is it:
  it shows what the strategic parts say and passes on what the
  person asks, and decides nothing. Its `Does` names what it reads
  and what it asks, of which part (`Uses`), in the product's words:
  every value a criterion says is shown. Where one view needs
  things of two parts together, say which part gives them together.
  No layout, no component: how it looks is the next stage's, and no
  strategic part says how a thing is shown.
- **What fails has a home too.** For each thing that can fail or
  stop half way, one part records it and says what state is left:
  no reply; a save that fails after the step that cannot be taken
  back; the product stopped between two steps; a start that finds
  what it stored unreadable, of an older layout, or its address
  taken; a setting that is there and wrong; a fault nobody foresaw
  inside a request; one bad item among many from outside (the one
  set aside, or the whole refused: say which); a loop over what the
  outside gives, bounded in count and in time where the promise is
  made; what trying again removes and what it keeps. Name the case,
  not only the concern. A design whose parts cover only what works
  has left the rest to the builder.

**A boundary** is where a strategic part asks for something it must
not know how to get.

```markdown
## B1: <what is asked across it, in the product's words>
Owned by: C1
Crosses: <plain data, named>
Needs: <what the slice needs of whatever stands behind it>
Technology: forced: <what in this slice forces a choice now> | not forced: <why one held in memory satisfies this slice's tests>
```

It belongs to the side that calls through it; the other side
implements it. Only plain data crosses, in both directions. Look
both ways: what a boundary names must itself name nothing tactical.
`Needs` says what whatever is chosen must do (keep it through a
restart; of two that claim at once, give it to one): the stack is
chosen against it later, not here. `forced` only where this slice
cannot be tested without the real choice.

**Neither too much nor too little.** A boundary, a setting or a way
to extend is there for two real cases the slice has now, or because
a strategic part would otherwise know something tactical; never for
a case that may come. And where the slice already has two real
variations, or a part that will change on its own, the boundary is
there now: "simple for now" with the need in plain sight is the same
mistake.

**What the design leans on.** Whatever a part or a decision says of
a thing committed to rests on a fact of its research document, with
that document's own words in quotes, or on an open test (`T2`): then
the part does what `tested.md` says the slice does either way. Where
the design needs the thing to behave some way and neither says so,
do not assume it: `Leans on: unknown: <what is assumed>` with
`Either way: <what the part does so that it is safe whichever is
true>`. An answer that says "the product treats it as" is such a
lean: find it and name it.

**Two things at once.** Read the slice for this as a fact, before
any decision: can two things run over the same state at the same
time (two copies of the product, a request and an event, a scheduled
run and one started by hand, a retry and the first try, a start and
a close still in progress)? Under `## At once`: `Nothing: <why>`, or
the decisions that keep them apart. Such a decision is walked
through its bad orders before it is chosen, a line each:

```markdown
Keeps apart: <the two things, and what keeps them apart>
Two at once: <both check before either writes>
Crash: <after the claim is taken and before the work; in the middle; after the work and before the release: a line a step>
Stopped while waiting: <asked to stop while it waits for the claim, the other side, a timer or a call>
Leftover: <a marker left behind, or removed or changed by hand while its owner runs>
Reused name: <the marker names an owner that died, and the name now belongs to something alive>
```

A claim is taken where the thing starts, in one step with what it
checks (say what), never after the step that cannot be taken back.
Each line says what state is left and who would notice. "Cannot happen"
only with its reason. If a line comes to both going on, nobody
knowing, or stuck until someone sees to it, change what keeps them
apart until none does. If none can be found, the decision is the
owner's, the hole said as what they would accept.

**A decision** is a point where more than one reasonable structure
was possible. Applying a rule above is not one.

```markdown
## D1: <the decision, said as the decision>
Kind: chosen
Says: <what is chosen>
Instead of: <each way not taken, with the concrete reason>
Because: <why>
Costs: <what it makes harder, or closes off>
Architectural: yes | no: <does it touch the structure, a technology or something every part follows>
Significant: yes | no: <would going back be costly, or will others follow it>
Non-obvious: yes | no: <could a reasonable person expect another way>
```

Decide, record, go on: a technical choice is never put to the user.
Each of the three is yes or no, on the side it falls; the script
keeps those with three as records of their own.

**The owner's** (`Kind: owner`, with `Options:` two or more,
`Recommended:`, `If left:`, `Harm:`) is only: a cost in money; a
risk no structure removes; what cannot be taken back once people's
data is in it. A decision that deletes what is kept of a person's
data, or leaves no way to give it back, is the owner's every time,
however clear the better option looks: replacing kept rows by
newer ones deletes them, and what ending a thing (a disconnect, a
removal) does with what was kept of it is always said, by an answer
or by such a decision. Never a choice between two sound structures.

**What is another stage's goes back, and is not settled here.**
Under `## Goes back`, a line each, the stage first:

- `requirements:` or `slice:` a consequence of the design that
  changes something they confirm (a limit, what is in or out);
- `approach:` the slice needs something from outside that the
  approach does not have: it is committed to there, and researched,
  before the design leans on it. A boundary with nothing committed
  to behind it does not settle it;
- `research:` a state the slice needs that `states.md` lacks, when
  a person is shown it or can act in it. A state only a decision's
  own mechanism passes through (a claim taken, a request sent and
  not yet answered) is that decision's, said in its orders;
- `answers:` two answers that cannot both hold.

What an earlier stage already recorded and settled (a statement of
the plan that research checked, a risk the owner accepted) does not
go back a second time.

Asked for something the requirements or the slice put out: nothing
of it is designed. Say that it is out, and whose it is to change.

**The rest of the file.**

- `## Tests`: `Real:` the store (under a temporary folder) and each
  part behind its real entry. `Faked:` only what is outside: each
  thing committed to, at its wire; the clock; chance. Never a part
  of the slice's own.
- `## Kept for later slices`: `next` names the slices that build on
  this one. What they will read of it (an identifier, a position
  reached, where a thing came from, a state), or `none: <why>`.
- `## Already there` (a project with code): what exists that the
  slice touches; for a fault found there, where the boundary should
  be, and a decision: put right now, or left and said.
- `## No home`: `- <ids>: <why nothing in this slice is its home>`:
  wording alone, a state the slice never reaches. A thing wrongly
  put here is built by nobody.

**The work.** Run `next`. Give what it lists its homes; run it
again, until none is left. Then run `draw`: put right what it names
and draw again. Where it says the drawing could not be written, say
so and leave it.

**Then, once.** If things go back, say each with the stage whose it
is, and stop: the design is taken up again when that stage has
changed its document. If decisions wait for the owner, show them,
the gravest first: what is to decide, the options, the one
recommended and why, what happens if it is left; ask for all in one
message, and stop. What they decide is recorded on that decision,
`Decided: <the choice> (the user, <date>: "<their words>")`, and
drawn again.

**The user asks for a structure the above argues against** (a part
for a case that may come; the provider called from everywhere; a
lock with a hole): design the slice as you recommend, and say once
what their way would cost, in this slice's own terms, and that it is
theirs to insist on. A lock or a claim they propose is walked
through its orders like any other, and the holes said. If they then
insist, it is theirs: `Kind: owner`, their way among the options,
`Decided:` in their words, its cost said in `If left`, and the parts
changed to match.

**Told to skip this stage.** Write nothing yet. Say once what
skipping costs (how the slice is made up, and where each criterion
and open fact lives, is then settled by whoever builds it, one file
at a time) and that the design asks almost nothing of them; offer it
again. If they still say no, the file is one line, `Skipped at the
user's word, <date>: "<their words>"`, and you run `draw`. Do not
start the next stage.

**Written before, and something changed.** `next` lists what has no
home now. Change only that, in place; never write the file again
whole.

**Stop there.** Say, in the command's own numbers, how many parts
and boundaries, what has its home and what has none, the decisions
and which earn a record, what is leaned on and not known, and what
waits for the owner or goes back. No screen, no stack, no code.
