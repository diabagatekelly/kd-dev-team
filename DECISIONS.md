# The owner's decisions

What the owner has decided about this plugin, newest section last. A
decision here is changed only by the owner. What was chosen without
asking is listed apart, so it can be overturned.

## Standing, carried from kad's handoff (2026-11-18 to 2026-11-21)

1. **One step at a time, each validated before the next is built on.**
   A bar is set before a run; a step holds when the owner says so.
2. **Any product, any field.** Nothing is shaped to the projects a step
   is tested on (`judge/wording_check.py` checks each frozen text).
3. **The owner is asked only what is theirs:** the problem and its
   scope; a rule of the product in their own field; a matter of taste,
   shown as real alternatives; a risk, cost or obligation they must
   accept. Never asked: what the library, a dependency's documentation
   or a test can answer; good practice; the solution to an identified
   technical problem. A preference is never asked before the fact it
   depends on is known.
4. **Every skill and step is tested before it is adopted, the bare
   model first.** A text is carried only for what it adds over the
   task and its inputs alone; the model for a step is chosen by
   measurement.
5. **The planning personas are kept.** What is weighed stage by stage
   is each persona's text and model.
6. **Privacy.** This repository is public: methods, scripts, prompts
   and results as counts. Anything that quotes a project goes to the
   owner's private audit repository, in a folder named after the step.
7. **Sessions run in a VM** set up by the plugin with permission, on
   any OS; locks on by default; a plain-words page for the user.

## 2026-11-21: where the plugin lives, the order, how a step is tested

8. **A repository of its own, public, named `kd-dev-team`.** The record
   of how the earlier steps were validated stays in
   `kad-dev-team-plugin` (`next-plugin/validation/`); only what the
   plugin uses came across, each with its tests. kad stays frozen at
   0.19.0 there and is not renamed.
9. **Pipeline order.** Startup first, then the problem, scope,
   requirements and on; not research first.
10. **Startup is a stage** (stage 0). No special command launches a
    session. At the start of a session the machine is inspected (a
    missing VM tool, a missing sign-in, an existing VM to harden), on
    any OS. Audit is on or off as the user chooses; with it on, the
    record is kept in a folder on the user's own machine unless they
    name a repository of their own. Once setup is done the user is
    asked where the planning documents are, or where to create them.
    What goes in the planning folder and what in the audit record is
    decided later.
11. **Routing at startup, in this order:** an open pull request that is
    ready to merge or has comments to address; open issues that would
    block the next slice, or that are critical or high, with the user
    asked whether to address them first; then the next item by the
    documents that exist.
12. **A script is tested by unit tests, no model:** a stand-in for the
    VM tool and for the tracker, on every commit, on macOS, Windows
    and Linux; one real check per machine with the owner present.
13. **A session's behaviour is tested with the plugin evaluation built
    into the tool, used narrowly:** free checks only (no model judge),
    small cases, inside a VM. Where its checks cannot see what matters,
    headless runs graded by our own script, said in the step's test
    before it runs.
14. **What startup must do** (the seven conditions in
    `steps/00-startup/README.md`), with no way to work without a VM.
15. **Startup's test:** two arms (the scripts' report alone; the report
    with a short routing table, run only where the first fell short);
    kad's orchestrator is not an arm for this step. The ladder is
    Haiku 5.5, Sonnet 5.5, Opus 5.5; Fable is not tried. 14 scenarios,
    three runs each. **Bar:** a model holds at 42 of 42 and the
    cheapest that holds is adopted; the table is carried only if it
    turns a failing model into one that holds; if none holds the step
    has failed. **Ceiling:** $76, after a pilot of 14 runs whose real
    cost is reported first. Whether the adopted model gets ten more
    runs per scenario is decided on the first result.

## 2026-11-21: how closely a session's words are held to the test

16. **Wording has room, so long as it conveys what is intended** (the
    owner, on the pilot, where three scenarios failed only on a closing
    offer such as "Shall I draft it?"). A closing offer to go on with
    the thing named is not a question outside the four. A check is on
    what the session did and conveyed, not on its exact words.

## 2026-11-21: startup holds

17. **Startup holds with Sonnet 5.5 and the routing table** (the
    owner, on the result in `steps/00-startup/README.md`). No model
    held on the report alone. With the table, over ten runs a
    scenario, Sonnet passed 140 of 140 and Haiku 136 of 140 with
    three real slips, so the table is carried and Sonnet is the
    cheapest model that holds. Opus was not run with the table.

## 2026-11-21: planning happens inside the VM

19. **A planning session runs inside the project's VM** (the owner,
    on finding that startup named the next stage and stopped outside
    one). Startup, outside, makes the project's VM with the user's
    yes and hands over the one command that continues inside it;
    everything from the problem onward happens there. Startup was
    reopened for it; the result is in `steps/00-startup/README.md`.
    The owner has said the reopened step holds, with Sonnet 5.5 and
    the table of ten rows.

## 2026-11-21: how the problem stage is measured

18. **The problem stage: free checks as a gate against drift; quality
    read by the planner, with reasons** (the owner, wary of a model
    judge after kad's noisy one). The mark is what kad's
    `problem-framing-doc` produced, which the owner liked: at least
    that good, with the least text that holds. The text is tuned
    until it gets there. The test is in `steps/01-problem/README.md`.

## 2026-11-21: the problem stage holds

20. **The problem stage holds with the text of 49 lines in
    `steps/01-problem/eval/problem-skill.md`, on the session's model,
    Sonnet 5.5** (the owner, on the result in
    `steps/01-problem/README.md`). It holds on Haiku too; the stage
    is not pinned to it, because the saving is small and this is the
    stage that talks with the user most.

## 2026-11-22: numbered documents; the scope map as a living picture

21. **Planning documents are numbered in the order they are made:**
    `000_problem.md`, `001_scope-map.md` and so on (the owner), so
    the sequence shows in the folder.
    A document takes the next number in the folder when it is made,
    and is found by its name. A map changed after a slice is a new
    document, such as `013_scope-map-v002.md`, and the earlier map
    is kept, so the folder shows when the picture changed.
22. **Stage 2 is the product manager's map, kept alive** (the owner,
    who wants the big picture to go back to after slice 1 and knows
    it will change). After the client describes the product, the
    product manager acts next: the map is the handful of things a
    user does, in the user's order, each one line, marked now, next
    or later. It is not a plan made once: it is re-read with the
    user each time a slice is done, and changed when the slice
    taught otherwise. The client's part: what is in, what is out,
    which activity comes first. The test is in
    `steps/02-scope-map/README.md`.

## 2026-11-22: a slice is checked off, not guessed at

23. **Whether a slice is done is decided at a check-in when work is
    merged, not by the scope map alone** (the owner, on the first
    full pass, where the map had no way to say an activity was
    finished). The check-in is informed by the merged work and by
    issues filed during the build that fit neither the slice in hand
    nor the next. Given new information, the map's part is to say
    whether it belongs to the slice in hand, to the next, or between
    them. A slice's requirements are a checkable list, used for the
    acceptance criteria and for the map, so that "done" is every
    item checked. Where the check-in and the tracking of the list
    sit in the routing is not decided yet.

## 2026-11-22: the drawing of the scope map holds

24. **The scope-map stage holds as the drawing of the map, with the
    text of 49 lines in `steps/02-scope-map/eval/scope-map-skill.md`,
    on the session's model, Sonnet 5.5** (the owner, on the result in
    `steps/02-scope-map/README.md`: 50 of 50 at the gate and as
    read). The re-read after a slice is not part of it: it is the
    check-in stage of decision 23, built after requirements.

## 2026-11-22: how the requirements stage is measured

25. **Stage 3 is the user's own list for the map's "now" activity,
    drafted first and shown once** (the owner, on the proposal in
    `steps/03-requirements/README.md`): a checkable list, each item
    with a box and a short name, and the outside systems and lasting
    things that research starts from. It is light on purpose: the
    requirements that come from the library of failures and the state
    tables stay where the design has them, in the questions and
    answers stages after research and the slice. Measured as stages 1
    and 2 were (decision 18); ceiling $30.

## 2026-11-22: the planner's own questions are written down

26. **The requirements list holds the planner's own questions, and
    nothing kad's skills did at a stage is lost unnoticed** (the
    owner, on stage 3's result: such questions "could point to
    things I didn't think of"). Each stage's text is set beside
    kad's skill part by part, and each part is kept, added or said
    to be left out with the reason; for stage 3 the table is in
    `steps/03-requirements/README.md`.

## 2026-11-22: questions by a walk; thoroughness before cost

27. **The planner's questions are arrived at by a fixed walk where
    that finds more, and the owner will answer them** (the owner:
    "I'm not opposed to answering questions so we have a good
    understanding of what we are building"; and, asked whether to
    test a grid of gap kinds on a raised ceiling: "Yes, and we can
    drop the budget, it's more important to me that we make this
    plugin well tested and make this planning really solid to
    support clean bug-less building"). The ceiling is dropped for
    stage 3; a pilot and the real cost are still reported. Whether
    it is dropped for the stages after is asked when the next one is
    proposed.

## 2026-11-22: the requirements stage holds

28. **The requirements stage holds with the text of 84 lines in
    `steps/03-requirements/eval/requirements-skill-kinds.md`, on the
    session's model, Sonnet 5.5** (the owner, on the result in
    `steps/03-requirements/README.md`: 70 of 70 as read, 89% of the
    known gaps raised). Before the check-in stage is begun, the
    owner wants a pause for two things: the tests of stages 0 to 3
    looked over for gaps, and the four stages run end to end on a
    few real examples.

## 2026-11-22: every problem becomes a test

29. **Whatever problem is met results in a test added or fixed, an
    evaluation added or fixed, or a skill changed and tested again**
    (the owner, during the end-to-end runs). The end-to-end examples
    are kept and re-run as stages are added; the owner gives ideas
    for them. Each finding and the test it became is listed in
    `e2e/README.md`.

## 2026-11-22: how many runs

30. **Five runs, not ten** (the owner). Five for a scenario that is
    new or whose text has just changed, and five again before the
    owner is asked whether a stage holds; the other scenarios of a
    stage get one run as a check that nothing else moved, and the
    fixes from one round of reading are batched into one pass. (The
    owner first chose ten before a stage is put to them, and changed
    it to five on 2026-11-23, when a ten-run pass over the four
    stages came to about 75 minutes and $25.)

## 2026-11-22: the suites stay quick and cheap

31. **The tests and the end-to-end runs are not to take forever or
    cost much: a good balance** (the owner). The balance chosen is
    the table in `e2e/README.md`, "How much is run, and when": what
    is free first (unit tests; kept runs graded again when a check
    changes), then only what changed, and the wide pass only before
    a stage is put to the owner. The owner can change any row.

## 2026-11-22: a file of the user's stays on their machine

32. **A file of the user's own (a sheet, an export) is never brought
    into the project's VM** (the owner, choosing between that and
    copying it in under a rule and a scan). The user describes it on
    their own machine with `startup/source.sh describe`, which prints
    its columns and counts and never a cell, and pastes that into
    the session; the session lists the file in `sources.md` and
    writes every example with invented values. The same script's
    `scan`, run on the user's machine, says where a value of the file
    has been written, never what. The real run on the owner's Mac
    (the plugin installed, a real VM) is held off for now.

## 2026-11-23: the four stages hold again; the check-in waits for the slice

33. **Stages 0 to 3 still hold with their texts as changed by the
    end-to-end runs** (the owner, on the pass in `README.md`: 105 of
    107 by the checks, 106 as read, the four examples clean). The
    one real miss, a `sources.md` that did not name the user's file
    in one run of five, is left unless it comes back.
34. **The check-in after a merge is built with or just after the
    slice stage, not before research** (the owner, on its first
    proposal: "I could see the vertical slicing skill playing a role
    in deciding if something fits in the current slice, the next
    slice, or between, rather than asking me"). Where a new issue
    belongs is the slice stage's to say and record; the owner is
    asked only what is theirs. Research is next, in pipeline order.

## 2026-11-23: how the research stage is measured

35. **Stage 4, research, is tested as proposed in
    `steps/06-research/README.md`** (the owner; the stage was the fourth then). A session reads a
    site the VM does not allow only after naming it and why and
    getting the user's yes, for that VM only. A state with no way
    out is recorded and brought once in the owner's list, not asked
    state by state as kad did. The outcome on the benchmark: a key,
    written before any run and kept private, of the facts two real
    plans got wrong about their providers; counted in a dossier
    written from the requirements-level documents alone; no model
    judge. The gate is six scenarios on a made-up provider (the
    owner asked why eight and took five; a sixth, the site not
    allowed, was added for the yes). A pilot of about $5 first, its
    real costs reported and the table corrected; the ceiling is
    named by the owner then.

## 2026-11-23: the order of the stages, after the research pilot

36. **The slice comes before any dependency is chosen, and research
    after the choice** (the owner). The requirements say what is
    needed, not how: a provider is a "how", and is in the
    requirements only where the user brought one as a constraint.
    The pilot showed it: the owner's real requirements named no
    provider, so research straight after them had nothing to read.
    The order is now: 0 startup, 1 problem, 2 scope map,
    3 requirements, 4 slice (with the check-in after a merge),
    5 approach (for each thing the slice needs that the app cannot
    do itself, the ways to meet it compared on the user's limits
    from a short read of each candidate's documentation; committing
    to a dependency is the owner's), 6 research (the full document
    for each dependency committed to, and the states of each lasting
    thing; a criterion of the slice that the facts make impossible
    goes back to the slice), 7 questions, 8 answers, 9 tests of open
    facts, 10 design (structure and boundaries), 11 screens,
    12 stack and repository, 13 readiness, 14 the owner's list and
    the planning pull request. Research stays at its pilot and is
    finished in its new place; the slice is built next. The owner
    names no ceiling for research: costs are still reported, and a
    pass over about $15 is still said first.

## 2026-11-23: the slice stage

37. **Stage 4, the slice, is tested as proposed in
    `steps/04-slice/README.md`, in its second form** (the owner). It
    carries every principle kad's skill was built from
    (`.synthesis/product-slicer.md` in kad's repository). It cuts
    the whole set of slices for the "now" activity, each row with
    the items it covers and what it builds on, recommends where to
    start, and the user chooses. Criteria are written only for the
    slice being worked on, to stay agile. When the user widens a
    slice the stage pushes back once, with the cost: the user may be
    wrong and leans on the stage as the expert; after that their
    word stands. The check-in after a merge (decisions 23 and 34) is
    this stage's: it checks off what merged work names, places every
    new issue without asking unless no row covers it, says whether
    the requirements and the set still hold, and proposes a new set
    when they do not; the same when work mid-slice changes the
    "what". The gate is ten scenarios; about $70, a pilot of $5
    first.

## Put off to the stage that needs them

- **How an outcome on the benchmark is tested** (research, questions,
  answers): put to the owner with the research stage's test and cost.
- **The numbers for the question measure** (how many questions a slice
  may bring; how often the owner taking the offered option is too
  often): with the answers stage.
- **A measure for each of the problem, scope, requirements, slice,
  design and screens stages:** agreed when each is reached.
- **How an answer of the answers stage attaches to the checkable
  list** (a criterion under the named item it belongs to, or an item
  of its own): with the answers stage. Stage 3 owes it only names
  that do not change.
- **Where the user finds `source.sh` on their own machine,** and when
  the scan is run (before the planning pull request is merged?):
  with the plugin's real install, which waits for the run on the
  owner's Mac.
- **Approaches the user considered and rejected:** kad's skill asked
  and recorded them; no stage here does yet.
- **A dependency the user did not name** (a library the design or
  the stack picks) has no way back to research in the order as
  written: with the design and stack stages.

## Chosen without asking; the owner can overturn any of these

- Claude models only; no other harness than Claude Code.
- The system inspection, the stage detection and the tracker reading
  are scripts; the model receives one report and acts on it.
- Audit on or off is an option of the plugin, asked at install and
  changed with the tool's own configuration command.
- The planning folder is asked once per project and remembered.
- GitHub is the first code host supported.
- At startup only issues that carry a severity are ranked; others are
  counted and shown.
- The language of the scripts is settled by test: it must run on a
  fresh Windows machine and a Mac with nothing extra installed. No one
  language does (2026-11-21, from the tools' documentation): a Mac has
  a shell and no PowerShell; Windows has PowerShell, and a shell only
  where Git for Windows is installed, which the tool recommends but
  does not require. The scripts are in plain shell, tested on macOS,
  Linux and Windows with Git for Windows; a PowerShell twin, held to
  the same tests, is owed for Windows without it and is written in the
  session on that machine.
- Startup's scripts (`startup/`), 2026-11-21:
  - A stage is found by its document's name in the planning folder
    (decision 21): `problem`, `scope-map`, `requirements`, a file in
    `research/`, then in the latest `slice-NNN/` folder `slice`,
    `questions`, `answers`, `open-facts`, `design`, `screens`,
    `stack`, `readiness`, `owner-list`. Numbers run on through the
    slice folders, so a first slice's documents are 004 to 012.
    Names other than the owner's first two stand until the stage
    that writes each is built.
  - When every document of a slice exists, the next stage named is
    the scope map, re-read with the user before the next slice.
  - The planning folder is remembered in the plugin's own data folder,
    by the project's root, so nothing is written in the project.
  - An issue is ranked when a label of it says critical, high, blocker
    or blocking.
  - A pull request has comments to address when a review thread is
    unresolved, changes are requested, or someone else has commented
    since its last commit; it is ready to merge when it has none of
    those, is not a draft, has no conflict, no failing or running
    check and no review still required.
  - A system is supported when the VM tool's install page lists it:
    macOS 14 or later on Apple silicon, Windows 11 on Intel or AMD,
    Ubuntu 24.04 or later. Linux inside Windows (WSL) is not listed and
    is treated as not supported.
  - On Linux the install asks for an administrator's password, so the
    script hands the command to the user and does not run it.
- This repository's layout.
- One VM per project, named `kd-`, the folder's name and a number
  made from its path, so two folders of one name never share a VM.
  Always a private copy of the repository, never the user's folder.
- Making the VM makes the folder a git repository first where it is
  not one (`git init`, nothing committed): the VM tool copies a
  repository, and the yes covers both.
- Outside the VM the tracker and the documents are not read at all;
  the report says they are read inside.
- A session knows it is inside a VM by the folder the VM tool mounts
  there, and only where the VM tool itself is not installed.
- A startup report with a part that could not be read (a line
  REFUSED) stops the session: it says what was not read and does
  nothing else, not even the planning conversation, until the report
  reads (routing table, row 0; found by the first end-to-end run).
- In an end-to-end run the user is a script that says only the
  words written in the example's brief (the owner asked for a user
  that does not drift); a model only says which of the brief's
  topics a message asks about, and its pick is kept with the turn.
- `startup/source.sh`, 2026-11-22: it reads delimited text (.csv,
  .tsv, .txt) and refuses a workbook, asking for the sheet saved as
  CSV (a workbook cannot be read with what a fresh Mac and a fresh
  Windows machine both have); a screenshot or a PDF is not read at
  all. A value is looked for when it would tell a reader something:
  text of five characters or more, a number with a decimal part or
  of five digits or more; a column's name is not a value. The rule
  for the session is said once, in the routing table, not in each
  stage's text.
- The requirements list (`steps/03-requirements/`), 2026-11-22:
  - An item is a line `- [ ] **its-name**: ...`; a name is lower case
    words joined by hyphens.
  - A limit of the whole problem is not a box: it holds for every
    item, and the criteria carry it.
  - The stage writes every box unchecked; checking belongs to the
    check-in after a merge.
  - The list is for the "now" row only; a later "now" gets a list of
    its own, decided with the check-in.
  - The stage script reports the count on every startup report once
    the document exists; it does not read the inventory until the
    research stage needs it.
- The pass of 2026-11-23: startup's scenario 03 was run five times
  with the 14 new or changed scenarios, since one run says little of
  a slip seen once. The 14 were taken as startup 19 to 21, problem
  05, 07 and 08, scope map 05 and 06, requirements 05 and 08 to 12.
- The check-in's folder, `steps/check-in/`, has no number: it comes
  after the build, whose stages are not numbered yet.
- Research (`research/`, `steps/06-research/`), 2026-11-23:
  - The page script is Python: research runs inside the project's
    VM, which is Linux. That a new VM has Python is to be checked in
    the real run.
  - A page is read with `curl`, so the VM's own list decides what is
    reached; the page is kept as text beside the research documents
    and every quote is looked for in it.
  - The VM cannot widen its own list: the yes for a site is a
    command the user runs in a terminal on their own machine.
  - A fact is written with its quote and its page together,
    `"quote" (address)`, which is what the script looks for.
  - In the scenarios the report's two new lines (what is to be
    researched, each with its document, and the command that reads a
    page) are added by hand: the stage script does not print them
    until the stage is agreed.
  - An inventory of `none` is to be the stage script's to skip, by a
    unit test, not a session's scenario.
  - After the pilot: Opus is run at the gate and on the benchmark
    only where Sonnet with the text does not hold (the bare model on
    Sonnet already lacks what nothing tells it: the marks, the open
    points, the quote with every fact).
  - The quote check takes a quote with the first address after it on
    its line, without regard to case, and reads across a link's
    words.
- The new order (decision 36), 2026-11-23:
  - `steps/04-research/` is renamed `steps/06-research/` now; the
    stage script's order (`startup/stage.sh`, adopted, with its
    scenarios) changes when the slice stage is built, and every
    earlier stage is run once then.
  - Where the approach stage's candidates come from (the user, or a
    search they say yes to) is settled when that stage is built.
- The slice stage (decision 37), 2026-11-23:
  - The set is a document of its own (`NNN_slices.md`), a new
    numbered version once a slice has been built from it; a slice's
    own document is in its folder.
  - kad's three placeholder lines (security, reliability,
    accessibility) are not carried: the questions stage draws those
    for every slice.
  - kad's arm is run on the cutting scenarios only; it had nothing
    for the coming-back.
- Put off: installing the plugin inside a new VM, and what of the
  planning folder's memory survives a VM being destroyed.
