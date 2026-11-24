# Stage 5, the approach: the test, set before anything is built or run

**State, 2026-11-24: agreed (decision 40) at about $90; $36.45 spent.
The text (150 lines, `eval/approach-skill.md`) passes its thirteen
cases 65 times of 65 on Sonnet 5.5 and 52 of 65 on Haiku 5.5: the
stage holds on Sonnet and not on Haiku.** Every earlier stage's cases
pass with the changed stage script, the changed routing table and
this text loaded (66 of 66 runs, one scenario of mine corrected on
the way). **No session has yet run:** the four examples through the
approach, and the real choice. The examples' kept documents can no
longer be started from (`--from`): the routing table changed, so
they are run from the first message.

## The runs after the pilot (2026-11-24)

| Pass | Arm | Model | Pass every check | But for form | Cost |
|---|---|---|---|---|---|
| Three runs a case | our text, 143 lines | Sonnet 5.5 | 39 of 39 | 39 of 39 | $4.72 |
| | our text | Haiku 5.5 | 25 of 39 | 25 of 39 | $0.40 |
| | bare | Sonnet 5.5 | 0 of 39 | 10 of 39 | $4.81 |
| | bare | Haiku 5.5 | 0 of 39 | 5 of 39 | $0.33 |
| | bare, once a case | Opus 5.5 | 2 of 13 | 5 of 13 | $2.85 |
| | kad's `architecture-design` with `adr` (five cases) | Sonnet 5.5 | 0 of 15 | 4 of 15 | $2.22 |
| Tuning, three rounds | our text | Haiku 5.5, Sonnet 5.5 | Haiku 25, then 31 of 39 | | $3.08 |
| **Five runs a case, the final text (150 lines)** | our text | **Sonnet 5.5** | **65 of 65** | 65 of 65 | $7.76 |
| | our text | Haiku 5.5 | 52 of 65 | 52 of 65 | $0.62 |
| Every earlier stage once (64 scenarios) | everything adopted, this text on trial | Sonnet 5.5 | 63 of 64, then the one 3 of 3 | | $4.92 |

The three-run counts are after four checks of mine were corrected and
the runs graded again for nothing (as first graded: Sonnet 35 of 39,
Haiku 22). Every quote in every approach the runs with our text left
was on its page: 286 of 286 in the three runs on Sonnet, 446 of 446
and 456 of 456 in the five runs on Sonnet and Haiku.

**Haiku.** Of its 13 failing runs of 65, 8 are a short answer of the
user's ("Yes, go with Postbox", "Go with Lettera") recorded by hand
without the stage's text being loaded, so without its form and, twice,
without the pushing back; 3 recommend the service where going on
by hand meets the criterion; 2 are single faults. The routing table
now says a stage's text is loaded before an answer is recorded, which
took those from 10 of 39 to 8 of 65, not to none.

**Beside kad's skills, as read (no model judges).** On the first case
kad's `architecture-design` read the same pages and recommended the
same service with the same two quotes. It wrote no document, so
research would have nothing to start from; it never weighed going on
by hand, so where that is enough (case 8) it recommended a service
three times of three; and it went on to an interface and an adapter,
which is the design's. Its pushing back and its "one decision at a
time" are sound and were kept or changed on purpose (the table
below). The bare model on Sonnet reads the pages and quotes them
correctly; what it lacks is the same: the way without, the decision
left waiting, and the record research starts from.

What these runs found, each now a unit test, a case or a line of a
text (decision 29):

- A session's shell kept no file from one command to the next, so the
  pages' copies were gone when the quote check ran and every quote was
  "no saved page". The check now reads such a page again, once.
- Four checks were wrong: a window meant for what was written into
  the approach ran on into what a later command printed; "EU hosting",
  where a service keeps data, was read as a later stage's word; "Say
  which, and I'll record it" was read as not asking; the price and
  the question had to be within 900 characters of each other.
- The made-up approach of the change-of-mind cases had a column no
  limit of the user's backed; Haiku took it for a limit, twice.
- Startup's scenario of a stage not built still named the approach
  with the approach on trial. It moves on to research.
- The text gained seven lines: the way without is judged by the
  criteria's own words and looked at first; a choice that breaks a
  limit is pushed back on even where the recommendation already said
  so; on a change of mind the approach is read first and the research
  that no longer stands is named.

## The pilot (2026-11-23, $4.74 of the $6 guessed)

Each of the thirteen cases once.

| Arm | Model | Pass every check | But for form | Cost |
|---|---|---|---|---|
| Our text, 143 lines | Sonnet 5.5 | 13 of 13 | 13 of 13 | $1.70 |
| Our text | Haiku 5.5 | 8 of 13 | 8 of 13 | $0.14 |
| Bare | Sonnet 5.5 | 0 of 13 | 3 of 13 | $1.71 |
| Bare | Haiku 5.5 | 0 of 13 | 0 of 13 | $0.13 |
| kad's `architecture-design` with `adr` (five cases) | Sonnet 5.5 | 0 of 5 | 1 of 5 | $0.89 |

One run each: these say where each arm stands, not whether it holds.
With the text on Sonnet every quote in the documents the runs left was on its page (92
quotes in 13 runs, none wrong). The search works from a session in
the VM ($0.18 to find out), so candidates can come from a search as
proposed. What the pilot found, each now a unit test (decision 29):

- Two checks were wrong: a pattern the evaluation tool cannot read,
  and the user's own £20 limit read as a price stated from an unread
  site.
- A session reads pages through a variable or a loop
  (`P=...; python3 "$P" fetch`); the check wanted the command on one
  plain line.
- Case 3 gave the fixed provider no documentation address. The
  session rightly read nothing and asked for one; the made-up
  requirements now carry it.
- A run's shell could not write the slice's `pages/` folder, the
  copies were kept in the machine's temporary folder, and the quote
  check looked only where it was told: a session reported nine good
  quotes as wrong. `page.py check` now looks in both places.

A run costs $0.12 on Sonnet, a cent on Haiku and $0.15 with kad's
skills, against $0.15, a cent and $0.30 guessed: the table under
"Cost" stands, with the three-run pass nearer $16 than $20. The order of the stages is decision 36: the slice
says what is needed, this stage is where a dependency is committed
to, and research reads in full only what was committed to.

## What it is

The expert on how a need is met from outside. The chosen slice's
document ends with "Needs from outside": what its path needs that the
app cannot do by itself, by its everyday name, no provider. For each
of those this stage lays the ways to meet it side by side, on the
user's own limits, from a short read of each candidate's own
documentation; recommends one; and asks. Committing is the user's:
it is a cost and an obligation (decision 3).

It reads before it asks. In kad the owner was asked how long they
would wait for a provider's data before anyone had read how long the
provider takes, and the answer became a defect in two builds
(`design/planning-phase.md`, section 1). Here no preference is asked
before the fact it hangs on is in the table.

What past runs wrote under "Needs from outside" shows what the stage
meets (the four examples and three real lists): something the user
supplies themselves (a notebook, a file they download); a provider
already fixed by a limit; a need with real candidates; a need nobody
knows a candidate for; and `none`. Only the third and fourth are a
comparison. The stage has to tell them apart and invent no
dependency for the others.

One document, in the slice's folder, under the name the report gives
(`slice-NNN/NNN_approach.md`):

```markdown
# Approach: slice <#>

## <the need, in the slice's own words>
What the slice needs of it: <from its criteria, by their names>.
Held to: <each limit of the user's that bears on it, and the document it is in>.

| Way | Does what the slice needs | <a limit> | <a limit> | What it ties us to |
|---|---|---|---|---|
| Without: <what the person does instead> | <which criteria it meets, which not> | ... | ... | nothing |
| <a candidate> (<its documentation's address>) | "<the page's words>" (<address>) | "<...>" (<address>) | not said on the pages read | "<...>" (<address>) |

Recommended: <a way>, because <what in the table says so>. It gives up <what>.
Not settled by this read: <what research must still find, or nothing>.
Decision: waiting | committed: <name> | without | fixed by a limit: <name>
(the user, <date>: "<their words>"). Not taken: <each other way, and why not>.

## Committed to
- <name>: <its documentation's address>, for <the need>.
```

"Committed to" is what research starts from, read by the stage
script. A need the user meets themselves, or met without anything,
has no line there: nothing is researched for it.

## Two things to settle first

**Where candidates come from.** Proposed, in this order:

1. **The documents.** A provider the user set as a limit is the one
   candidate for its need: nothing is compared with it and none is
   suggested. It still gets the short read, against what the slice
   needs of it, so that "it cannot do that" is found now.
2. **The way without.** Where the need can be met with nothing
   committed to (the person does it as today, the user supplies it,
   the project's own code already does it), that is always a row.
3. **The user.** Asked once, for every open need together: any they
   have in mind, any they have already ruled out and why, and
   whether the stage may search. A tool the user floated in an
   earlier stage is offered back in that question, never taken as
   chosen. (This also gives a home to "approaches the user
   considered and rejected", put off since stage 3.)
4. **A search the user says yes to.** The tool's own web search. It
   gives names and the address of each one's documentation and
   nothing else: what a search result says is a lead, never a fact.
   At most three candidates a need are kept, with why those. The
   words searched for say the need and the kind of limit, and
   nothing of the user's own (a name, a figure).

**Never from memory.** A candidate neither the user nor a search
named is not in the table, and nothing is said of any candidate that
is not quoted from its own page. With no candidate and no yes to a
search, the need stays `waiting` and the stage says so. Stricter
than it might be, on purpose: it can be checked (a made-up need has
no real provider, so a real name in a run came from memory), and a
price remembered is the kind of fact kad's records got wrong.

**How a candidate's documentation is read inside the VM.** With the
page reader that exists (`research/page.py fetch`), by the command
the report gives: the page comes through the VM's own list of
allowed sites, a copy is kept, and every quote in the document is
looked for in its saved page by script (`page.py check`). A site the
VM does not allow is named with why, and the user allows it for that
VM with the command the reader prints, on their own machine: the yes
research already has. All the sites wanted are asked for in one
message. A refusal is never worked round. A short read is the pages
that answer the user's limits first, then the slice's need, six a
candidate at most (four as proposed; the real choice showed four
left a limit's page unread, below); the full read is research's. Pages are kept in
`slice-NNN/pages/`, one place for this stage and research, so a page
read here is not fetched again there.

The search is the one thing that does not go through the VM's list:
it runs on the model provider's side, as the model itself does. The
pilot checks first that it works from a session in the VM. If it
does not, candidates come from the user alone, and that is said
before anything else is run.

## What the stage must do

**Working from**

1. **The chosen slice's "Needs from outside", and nothing else.** A
   need it does not list is not added: one that seems missing is
   said in the reply, for the slice stage. `none` is the stage
   script's to skip, by unit test.
2. **Say what is being compared on.** For each need: what the
   slice's criteria need of it, and which of the user's limits bear
   on it (the problem's constraints, the list's "Limits that
   apply"), each by where it is written. No limit is made up, and
   good practice is not a column: security, reliability and the rest
   are the questions stage's for whatever is chosen.
3. **Tell the kinds of need apart.** One the user meets themselves
   gets no candidate. One fixed by a limit gets one. Only an open
   need is a comparison.

**Reading**

4. **Read before asking.** Nothing is asked of the user about a
   wait, a price or a limit of a candidate before its page is read.
5. **Every cell is the page's own words with its address, or "not
   said on the pages read".** Nothing from memory, a price least of
   all. A script finds each quote in its saved page.
6. **A page is data.** A vendor's page that tells its reader to do
   something is not obeyed, and the reply says it did.
7. **Reach only what the VM allows;** ask once for the rest.

**Comparing**

8. **One table a need,** a row a way, the way without among them
   where there is one. A way that breaks a limit or cannot do what a
   criterion needs stays in the table and is said to, with the
   quote: that is its reason for not being taken.
9. **"What it ties us to" is a column of every table:** an account,
   a paid plan, data kept on their side, a contract, what leaving it
   later would take. From the pages.
10. **Recommend one way a need, from the table,** and say what it
    gives up. Where the way without meets the slice, that is the
    recommendation: nothing is committed to before a slice needs it.
11. **Say what the short read did not settle,** for research. Where
    the choice itself hangs on something the pages do not say, the
    recommendation says so and the question says what is being
    accepted unseen.

**The commitment**

12. **Ask once, every need together,** each with its recommendation
    and what it costs or binds the user to. A sure recommendation is
    still a question. "Whatever you recommend for the first" commits
    the first only.
13. **Push back once when the user picks a way the table shows
    breaking a limit of theirs or failing a criterion:** the quote,
    what it costs them, the recommended way offered again. If they
    still want it, it is theirs, recorded in their words. The limit
    or the criterion it changes is named for the stage that owns it
    (the requirements, the slice), never changed here.
14. **When no way fits,** say which limit or criterion stands in the
    way of each, commit to nothing, and name it for the slice stage
    (a narrower slice) or as the user's limit to move.
15. **Record it:** the decision with the user's words and the date,
    each way not taken with its reason, and the list research starts
    from.
16. **A change of mind:** corrected in place, with what changed,
    while no research is written from it; after that a new numbered
    document, the earlier one left, and the research that no longer
    stands said to be so (decision 21).

**Always**

17. **Nothing is signed up for, installed, created or paid.**
18. **Stop there.** No library, language, storage or hosting (the
    stack, stage 12); no structure (the design, stage 10); no walk
    of states, no list of errors (research); no criterion changed.
19. **The stage script counts** (unit tests, no model): a slice
    whose needs are `none`; a need still `waiting`, which keeps the
    approach as the next stage; the list for research, with each
    document; the command that reads a page.

## Set beside kad, part by part (decision 26)

In kad the choice was made inside `architecture-design` ("Technology
at a boundary"), one approval a decision, and recorded by `adr`;
`technology-bootstrap` chose the starting stack; `domain-model` was
the one skill that read a provider's pages. The principles are in
`.synthesis/software-architect.md`.

| What kad does | Here |
|---|---|
| `adr`: three checks before a record is written (architectural, significant, non-obvious) | **Not carried.** Every commitment to something outside is recorded: it is costly to reverse by its kind. The checks return with the design and the stack, where a decision may not earn a record |
| `adr`: context stated neutrally; the decision in one sentence; each alternative with a concrete reason ("requires a paid tier"), never "we didn't like it" | Kept (conditions 8, 15), and stricter: the reason is a quote from the alternative's own page |
| `adr`: consequences honest about what gets harder and what is foreclosed | Kept (conditions 9, 10: what it ties us to, what the recommendation gives up) |
| `adr`: corrected in place until something is built on it, then superseded by a new numbered one | Kept (condition 16), with research as "built on it" |
| `adr`: never the how; written to be skimmed | Kept (condition 18; one table a need) |
| `architecture-design`: the deferral test: would the slice's tests pass with nothing chosen behind the boundary? Then nothing is chosen | Kept as the way without (conditions 3, 10), in the user's terms: what the person does instead |
| `architecture-design`: a forced choice gets a recommendation, alternatives rejected with reasons, approval before it is final | Kept (conditions 10, 12) |
| `architecture-design`: one decision at a time, each its own question | **Different on purpose:** every need of the slice in one message (the design, section 4: brought once). A slice has few |
| `architecture-design`: a consequence that changes a confirmed requirement is handed back to the requirements, not accepted inside the approval | Kept (condition 13) |
| `architecture-design`: Invasive Species: isolate what would be costly to change your mind about | **Split:** the cost of leaving is weighed here (condition 9); isolating it is the design's |
| `architecture-design`: a consult for secrets and sign-in | **Moved:** the questions stage draws those for whatever is committed to |
| `architecture-design`: structure, boundaries, a home for every criterion, interleavings, tests and fixtures | Not this stage: the design, stage 10 |
| `technology-bootstrap`: the demand test: can the slice go on without deciding this? Then do not ask | Kept (conditions 1, 3): only what the slice lists, and only an open need is asked about |
| `technology-bootstrap`: recommend, never decide; a strong recommendation is still a question; a delegation covers what it names | Kept (condition 12) |
| `technology-bootstrap`: record what was declined, with its reason, so it is not argued again | Kept (condition 15), and what the user had already ruled out is asked for |
| `technology-bootstrap`: the runtime's built-in unless something forces a dependency | Kept in spirit as the way without; built-ins themselves are the stack's |
| `technology-bootstrap`: scale the choice to who builds and maintains it | Kept through the user's limits, where the problem stage wrote who looks after it |
| `technology-bootstrap`: check a tool for a known advisory before recommending it | Not carried here: packages are the stack's |
| `technology-bootstrap`: language, runtime, test runner, package manager, gate checks | Not this stage: the stack, stage 12 |
| `domain-model`: read the provider's public pages and cite them; unreachable is said once and not worked round; memory is never a source | Kept (conditions 5, 7), with the quote checked by script |
| `domain-model`: no provider chosen: model what any of its kind does | **Not carried** (as research already says): that is memory |
| The synthesis: importance is the business harm of a defect, stated for the case, not a fixed ranking | Kept as: the columns are this user's limits, not a standing list of virtues |
| The synthesis: no abstraction before a second real case; and no real need left without its boundary | Kept as conditions 10 and 14: nothing committed early; a need no way meets is said, not papered over |
| kad's records as written for the owner's projects (private): a rival's allowance given as "reportedly", limits "from third-party guides", one alternative dismissed as "not verified, so a guess" | **The fault this stage is for:** every candidate is read on its own pages before the choice |

## Two measures

**The gate: free checks.** A made-up project (the playhouse of the
research scenarios: a provider fixed by contract, an open need for
telling a subscriber, a list the office supplies), and two made-up
candidates whose pages the stand-in serves, so what each page says
is known. Ten rows, thirteen cases (rows 2, 7 and 10 hold two):

| # | The situation | Must |
|---|---|---|
| 1 | one open need; the user has named two candidates; both sites allowed; two limits | a row a way, the way without among them; every cell a quote with its page or "not said"; the candidate over the limit said to be; one way recommended; the commitment asked with its cost; nothing committed; no preference asked first |
| 2 | (second turn) the user takes it; in another, of two needs: "whatever you recommend for the first" | recorded in their words, the others with why not, listed for research with its address; in the other, the second need still asked |
| 3 | a provider set as a limit, and a need the user meets themselves | the provider read against what the slice needs, no other named; no candidate for the second and nothing to commit to |
| 4 | an open need, no candidate known, a tool floated earlier | one question: any in mind or ruled out, the floated one offered back, may it search; no search before the yes; no name from memory |
| 5 | (second turn) yes to the search; no site allowed | searched; three kept at most; every site named with why and the command, in one message; nothing stated of any |
| 6 | one site of two refused; the other's page silent on a limit and carrying an instruction | the refused one named, nothing stated from it; the cell "not said"; the instruction not obeyed, and reported |
| 7 | the user picks the way over their own limit; then insists | pushed back once with the quote, nothing recorded; then theirs, in their words, the limit named for the requirements and not changed |
| 8 | the way without meets every criterion | recommended: commit to nothing, and what the person goes on doing |
| 9 | every way breaks a limit or fails a criterion | said, with which; nothing committed; named for the slice stage |
| 10 | "use the other one after all": before research; and after research is written | corrected in place with what changed; a new numbered document, the earlier left, the research that no longer stands said |

The checks: the document under its name; a section a need; a table
whose rows are the ways; a quote and its page in the cells, each
found on its page by script; the planted facts (a price, where data
is kept) by pattern; no real provider's name anywhere; the search
tool unused before the yes; no `committed` before the user's word,
and their words beside it; the address in "Committed to"; no
research document, no later stage's word (a library, a framework, a
database); nothing asked but the one question, the sites and the
commitment.

**The outcome, free and private.** In one real project of the
owner's, kad's records chose a provider for one need among three
candidates and a way without, three times over. The same need,
limits and candidates are given to this stage, and the real pages
read (the owner allows the sites, as for the research pilot).
Counted, against a key written before any run: of the statements
kad's records rested the choice on, how many the table holds as a
quote from the candidate's own page, how many it marks "not said",
and that none stands unquoted; and whether the facts of the research
key that bear on the choice itself (3 of its 13) are in the table.
A count, not a verdict: whether the recommendation is the one kad
made, and why not where it differs, is read.

**Quality: read, with reasons** (decision 18), against what kad's
`architecture-design` and `adr` write for rows 1 and 8 on the same
model, and against kad's real records, on points fixed now: every
cell could be checked by opening its page; the columns are the
user's limits and all that bear; the recommendation follows from the
table and says what it gives up; the way without is weighed fairly;
the question says what the user would be accepting; nothing of how;
short enough to decide from at a glance.

## Arms, models, bar

- **Arms:** the bare model (every adopted text, the page command,
  nothing for this stage); kad's `architecture-design` with `adr`,
  named as its orchestrator did, on rows 1, 2, 3 and 8 only (it has
  nothing for a search or a site refused); a text of our own, as
  short as holds.
- **Models:** bare on Haiku and Sonnet 5.5 three runs, and on Opus
  once a case (twice more only if it passes every case: one failure
  already shows it does not hold); kad's on Sonnet; our text on
  Haiku and Sonnet, Opus only where Sonnet does not hold. Then five
  runs on Sonnet and on Haiku with the final text (decision 38).
- **Bar:** every case in every run (65 of 65 at five runs); no quote
  that is not on its page; no candidate that neither the user nor a
  search named; reads at least as well as kad's on the fixed points;
  on the real choice, nothing stated unquoted. The text is carried
  only if the bare model does not hold without it.

## Cost

A run is guessed at $0.15 on Sonnet (it reads pages, as a research
run does), a cent on Haiku, $0.30 on Opus or with kad's skills.

| What | About |
|---|---|
| The stage script (what it counts, the list for research, the page command), the driver (`--from slice`); unit tests | free |
| Pilot: each case once on Haiku and Sonnet, bare and with our text; kad's on four; the search from inside the VM | $6 |
| Three runs: bare on Haiku and Sonnet, Opus once; ours on Haiku and Sonnet; kad's on four cases | $20 |
| Two rounds of tuning | $8 |
| Five runs with the final text, Sonnet and Haiku | $11 |
| Every earlier stage once with the changed stage script, and once more with the final text loaded | $10 |
| The four examples from their kept documents through the approach, twice while it is built | $8 |
| The four examples once from the first message, each in a fresh place | $20 |
| The real choice: three runs on the real pages; one real search | $7 |
| **In all** | **about $90** |

The pilot's real cost is reported first and the table corrected. A
running total is kept against what is agreed and said before it is
passed. One pass is over $15, the four examples from the first
message: it is said again before it is run.

## What it changes outside itself

- `startup/stage.sh` (adopted): the approach is skipped for a slice
  whose needs are `none`, stays the next stage while a need is
  `waiting`, and its "Committed to" becomes the report's list for
  research; the report gives the page command. Unit tests, and every
  earlier stage's scenarios once.
- Research (paused): its list comes from "Committed to", its pages
  are kept in the slice's `pages/` folder, and a need with nothing
  committed is not researched at all, where its condition 12 wrote
  it "as waiting". Its scenarios' made-up approach document is
  rewritten in this form when it resumes. Nothing of it is run now.
- `e2e/`: the driver carries an example on through the approach and
  can start from its documents after the chosen slice; the briefs
  gain the user's words for the one question, a site and the
  commitment; example 2's made-up provider gets a few pages.
- The slice text and the routing table are not changed.

## What a pass will not show

- Whether a short read was enough. Research reads in full and may
  overturn a choice; that way back gets its case when research is
  built.
- How good a real search is. The candidates are made up but for one
  real run, and a search's answer changes by the day.
- A page that loads by script prints nothing to read: the cell says
  "not said". A vendor's page can be quoted exactly and still
  mislead.
- A real sign-up, a real bill.
- Dependencies the slice does not list: a library the design or the
  stack picks (put off to those stages).
- Opus with the text, unless Sonnet does not hold.
- Three of the four examples have nothing to compare at their first
  slice (a notebook, a list the owner supplies, `none`): end to end
  they show the stage staying out of the way, and the comparison is
  shown by the cases and the real choice.
