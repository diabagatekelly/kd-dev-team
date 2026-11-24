# The next plugin's planning phase: a design for the owner's review

Written 2026-11-21, at the owner's word ("Yes; and we can review it"),
ahead of the order in kad's `TODO.md` (which put a design after V8): the
owner wants to start on the planning phase now and to test each step
well before building on it. Nothing in this document is built. It
covers planning only; the build and the review end are sketched where
planning hands over to them.

Brought into this repository on 2026-11-21, when the owner settled
section 7 (`../DECISIONS.md`). Three things changed with it: a stage 0
(startup) comes before the problem, the stages are taken in pipeline
order, and section 5's question of how runs are made is answered for
scripts and for a session's behaviour. The experiments named E1 to E5
and V0, V1 are recorded in the `kad-dev-team-plugin` repository under
`next-plugin/validation/`.

## 1. What kad's planning taught us

**The questions it asked the owner.** In the 32 recorded sessions the
owner answered 149 questions.

| | Questions |
|---|---|
| The first option offered was taken | 108 (72%) |
| Of the 68 that marked an option "recommended", the recommended one was taken | 56 (82%) |
| The owner picked another option or wrote their own answer | 41 (28%) |

The 41 where the owner steered are of five kinds: the problem itself
and who uses it; a rule of the product in the owner's own field (how a
transfer or a shared charge is treated); how they want to experience
something (which of three looks, how to be told a login has lapsed);
whether to ship with something known to be wrong (two Highs standing,
an advisory); and corrections to the process (where files live). The
108 are overwhelmingly design decisions and technical forks. One of
the 41 shows a second failure: the owner was asked how long they were
willing to wait for a bank's transactions, before anyone had read how
long the provider takes. A preference was asked for where a fact was
needed first, and the answer became a defect in both builds.

(The count is from the sessions recorded in audit mode, planning and
build together, matched on the option's label; it is a fair picture,
not an exact census.)

**Where its facts came from.** Of 16 planning skills only one
(`domain-model`) tells the agent to read a dependency's documentation
and cite it. The reliability skill states how a provider's refusals
behave as general knowledge; the research step of E3 found that belief
contradicted by the provider's own pages on both plans.

**What it produced.** A first slice's plan of about 760 lines in 12
documents, from 16 skills and a 2,100-line orchestrator. Its lists of
failure cases were short and written into each skill.

**What the experiments found** (E1 to E5): a triage of a
250-question library, a cited dossier of every dependency, then answers
per thing, names 17 of 43 known defects against 11 for the earlier
tables, in the same number of cells, and flags before the build the
defects that came from wrong beliefs about a dependency. One cold read
finds about half of what four find.

## 2. Principles

1. **Any product, any field.** No text names a field of business; the
   library and the dossier carry what is specific.
2. **Facts before decisions.** Nothing is decided on a belief about a
   dependency; it is cited, or tested, or marked as untested.
3. **The owner is asked only what is theirs.** See section 4.
4. **A script where a script will do.** Rows, columns, inventories and
   checks are generated or verified without a model.
5. **Nothing is adopted untested.** Each step's text and model are
   chosen by measurement, one step at a time. See section 5.

## 3. The stages, in order

| # | Stage | Produces | From kad |
|---|---|---|---|
| 0 | Startup | the machine inspected (VM tool, sign-in, locks), audit on or off, the planning folder known, and the next thing to do named: an open pull request first, then blocking issues, then the next stage by the documents that exist | new; replaces kad's launcher and its orchestrator's first steps (`../steps/00-startup/README.md`) |
| 1 | Problem | the problem, why now, constraints | `problem-framing-doc`, kept |
| 2 | Scope | the steps of a large problem | `scope-map`, kept |
| 3 | Requirements | who needs what, in and out of scope, and an inventory a script can read: dependencies, lasting things | `requirements-refinement`, kept; the inventory made machine-readable |
| 4 | Slice | the whole set of thin slices of the "now", what each builds on, a recommended start; criteria for the chosen one only; after each merge, what is done, where each new issue belongs, and whether the list and the set still hold (decision 37) | `vertical-slicing`, `acceptance-criteria`, kept |
| 5 | Approach | for each thing the slice needs that the app cannot do itself: the ways to meet it, compared on the user's limits from a short read of each candidate's documentation; committing to a dependency is the owner's | new (decision 36); in kad the choice was made inside the design and recorded as an `adr` |
| 6 | Research | per dependency committed to: a dossier of cited facts, the plan's statements checked against them, open points with the test that would settle each; per lasting thing: its states | `domain-model`, kept and joined by the new dossier step |
| 7 | Questions | the library's questions that matter for the slice, each with the things it applies to; two grids by script (each received field against the ways a value can be wrong; each state against each event) | new |
| 8 | Answers | every question answered per thing, as a fact, a choice the planner records, or a decision for the owner | replaces the lists inside `reliability-requirements`, `security-requirements`; those two skills become the answering of their areas |
| 9 | Tests of open facts | the "needs a test" answers with real harm, run against the dependency's test environment in the VM | new |
| 10 | Design | structure, boundaries, where each criterion lives | `architecture-design`, kept; its interleavings fed by stage 7 |
| 11 | Screens | design system, screen, accessibility check on the rendered screen | `design-system`, `screen-design`, `accessibility-review`, kept |
| 12 | Stack and repository | what the slice forces, nothing more | `technology-bootstrap` (to be freed of one runtime's names), `repo-bootstrap`, `adr` |
| 13 | Readiness | scripts: every kept question answered, every fact sourced, every quote found on its page, every criterion with a home | the readiness gate, kept and extended |
| 14 | The owner's list, then the planning pull request | one short list of decisions, ranked by harm; the plan merged before any build | the planning pull request, kept |

Not carried over: the orchestrator as a whole (only this route, as a
small table), the block of text copied into five skills (kept once),
and the examples from one field.

A slice that adds no dependency, no lasting thing, no stored data and
no secret runs a lighter pass: the dossier is reused, stage 7 covers
only what changed, and only new cells are answered.

## 4. What reaches the owner

**Asked** (the five kinds the owner really steered, less process):

- the problem, who it is for, what is in and out;
- a rule of the product in the owner's own field, where the plan cannot
  know what is right;
- a matter of taste or of how the owner wants to experience the
  product, shown as real alternatives;
- a risk, a cost or an obligation the owner must accept (shipping with
  a known fault, spending money, a commitment about people's data).

**Never asked:**

- anything the library, the dossier or a test can answer;
- good practice in user experience, accessibility and security: it is
  applied;
- the solution to a technical problem that has been identified: the
  planner chooses, records the choice and its reason, and goes on;
- where files go and how the work is organised: a convention, stated
  once.

**How.** A preference is never asked for before the fact it depends on
is known (stage 6 comes before any question about waits, limits or
what a dependency allows). Decisions for the owner are gathered and
brought once per slice as a short list ranked by harm, each with what
happens if it is left, not one at a time as the work proceeds. Every
choice the planner made without asking is in one record the owner can
read afterwards and overturn.

**The measure** (proposed; the owner sets the numbers): how many
questions a slice brings (E3's answering marked 20 and 26, against
kad's much larger count), and of those, how often the owner takes the
option offered without change. If the owner takes the offered option
nearly every time, the question should not have been asked: the aim is
that most questions asked are ones where the owner's answer could not
have been predicted.

## 5. How each step is tested before it is adopted

kad's skills were written, then gated on whether the agent behaved as
the text said. Their wording was never tested against doing without
it, and every task ran on one model. For each stage here:

1. **An outcome to measure**, fixed before the runs (the table below).
2. **The bare model first, always** (the owner, 2026-11-21: "we should
   always start with the bare model(s) to see if the skill even earns
   its place"): the task and its inputs and nothing else. Only where
   that falls short is a text tried: a short brief (the briefs of E3
   are about 40 lines), then kad's skill where one exists. A text is
   carried only for what it adds over the bare model.
3. **A ladder of models:** the same step on a cheaper model, the usual
   one and the strongest, and the cheapest that holds the bar is taken.
4. **Three runs of each,** so a difference is told from chance.
5. **Plans it was not tuned on:** the third project's slices 2, 3 and
   4 are held out and used only to confirm.
6. **Cost and time** from the transcripts, beside every result.
7. **In the VM,** so runs are isolated and repeatable.

How the runs are made and judged (the owner, 2026-11-21): a script is
tested by unit tests and no model; a session's behaviour by the
plugin evaluation built into the tool, with small cases and its free
checks only, inside a VM, falling back to headless runs graded by our
own script where those checks cannot see what matters; an outcome on
the benchmark is decided when the research stage is reached. See
`../DECISIONS.md`.

| Stage | The outcome measured |
|---|---|
| Research | of the contradictions known for a plan, how many a dossier finds; whether repeats find the same ones; every quote on its page |
| Questions | does the triage keep the entries real defects depended on; how many cells |
| Answers | defects named, and named or part, by the judge of V1 (second version) |
| What reaches the owner | number of questions; on a sample, how many the owner says were theirs and how many of the planner's choices they would have wanted to make |
| Tests of open facts | how many can be run at all; how many answers they change |
| Readiness | the scripts' own unit tests; seeded faults in a plan are caught |
| Problem, scope, requirements, slice, design, screens | to be designed with the owner, stage by stage: these have no key yet |

The last row is honest about a gap: the benchmark measures defects
that reached a build, which says little about whether a problem was
framed well or a slice cut thin. Each of those stages needs its own
measure before its text is judged.

**The layers of checks that stay once the plugin exists:** script
tests on every commit; the readiness scripts on every plan; the cheap
step checks when a brief changes; the benchmark when the answering or
research changes; the held-out plans before a version is called
better; a real slice now and then.

## 6. Order of work

Pipeline order (the owner, 2026-11-21, against this document's first
proposal to begin with research): stage 0, then 1, 2, 3 and on, one
stage at a time, each with its test read by the owner before the
next. The order itself changed on 2026-11-23 (decision 36): the slice
before any dependency is chosen, research after. Stage 4 has its measure and holds
(`../steps/04-slice/README.md`, decision 39). Stage 5 holds (`../steps/05-approach/README.md`, decision 41), and so does stage 6 (`../steps/06-research/README.md`, decision 44), with the owner's condition that the gaps research leaves are shown closed once stages 7 to 9 are stacked on it. Stages 10 and 11 have no measure yet: each is agreed
with the owner when the stage is reached, before its text is judged.

## 7. For the owner to decide

All four of this section's first questions are answered or put off
to the stage that needs them: `../DECISIONS.md`.
