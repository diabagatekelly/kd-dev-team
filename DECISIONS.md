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

## 2026-11-23: what is tested where, for every stage

38. **Unhappy paths in the stage's cases; the happy path end to
    end; Haiku always tried with the final text** (the owner, on the
    slice stage's result: "I want to have confidence in what we
    build rather than trying to patch a bunch of holes after the
    fact", and no suite "that takes forever to run and eats up all
    my tokens"). For every new stage: unit tests for every branch of
    a script; cases for every behaviour, a change of mind or of
    scope included, five runs on Sonnet and five on Haiku with the
    final text before a model is settled; the same four examples
    carried on through the new stage, none new; and one pass of the
    four from the first message before the stage is put to the
    owner. A change scenario is a case, not an example. To keep an
    example cheap it is started from its documents as its last good
    run left them, refreshed when an earlier stage's text changes.

## 2026-11-23: the slice stage holds

39. **The slice stage holds with the text of 152 lines in
    `steps/04-slice/eval/slice-skill.md`, on the session's model,
    Sonnet 5.5** (the owner, on the result in
    `steps/04-slice/README.md`: Sonnet 83 of 85 over five runs of
    seventeen cases and 10 of 10 on the two its one slip touched,
    once fixed; every stage once, 64 of 64; the owner's three real
    lists cut no wider than kad's). Haiku was tried with the final
    text and does not hold (66 of 85): it gives way on a wider cut.

## 2026-11-23: the approach stage

40. **Stage 5, the approach, is tested as proposed in
    `steps/05-approach/README.md`** (the owner: "Yes and yes"), at
    about $90, with a pilot of about $6 first whose real cost is
    reported before the rest is run. And the point put to them with
    it: when the user names no candidate and says no to a search,
    the need stays `waiting`; the stage offers no name it happens to
    know, not even as an unchecked lead. Memory is not a source of
    candidates.

## 2026-11-24: the approach stage holds

41. **The approach stage holds with the text of 153 lines in
    `steps/05-approach/eval/approach-skill.md`, on the session's
    model, Sonnet 5.5** (the owner: "Yes let's hold", on the result
    in `steps/05-approach/README.md`: Sonnet 65 of 65 over five runs
    of thirteen cases with the final text, every quote on its page;
    every earlier stage once, 63 of 64 and the one a scenario at
    fault; the four examples through the approach; on the owner's
    real choice nothing stated without a quote). Haiku was tried
    with the final text and does not hold (57 of 65): it records a
    short answer by hand without the stage's text. The short read is
    six pages a candidate, the limits first, not the four proposed.

## 2026-11-24: research stays a stage, before the questions

42. **Research is done up front, as a stage of its own, and the
    approach stays as adopted** (the owner). Asked whether to write
    the questions first and look up only what they need, and whether
    the approach was overkill, the owner weighed it and kept both:
    the approach "is already built and cheap", and "having all the
    facts in a doc when we go to formulate and answer questions will
    add valuable big picture context". The comparison of the two
    orders on the first real plan (about $8) was offered and is not
    run. Whether every line of the approach's text earns its place
    has not been tested; it is not asked for.

## 2026-11-24: how the research stage is measured, in its new place

43. **Stage 6, research, is tested as proposed in
    `steps/06-research/README.md`** (the owner: "Fine" to the cost
    and to the third point, then "yes and yes"), at about $90, the
    pilot's real cost reported first ($5.23). With it, two points:
    the states of a lasting thing the product itself keeps are
    written here, from the planning documents alone, a gap written
    as "not said in the documents" for the questions stage; and a
    user who says to skip the reading is told once what that costs
    and offered the reading again, and if they insist every point
    is written open with its test and nothing as a fact. The owner
    asked how the states feed the questions and was told: sourced
    rows are facts, "not said" rows become questions answered as
    the planner's choice or the owner's decision, `to verify` rows
    become tests, a state with no way out goes to the owner's list.

44. **The research stage holds, on Sonnet 5.5** (the owner: "Yes",
    2026-11-24, after asking how much the missed facts matter and
    whether later stages would catch them). Its text is adopted
    (149 lines), its twelve cases join the regression build,
    startup's case of a stage not built moves on to the questions,
    and an end-to-end run merges a slice only once its research is
    written or there is nothing to research. Adopted knowing what
    it does not meet: on the plan it was tuned on, 76% of the key's
    facts by pattern against 80% (85% as read); on the other, 7 of
    11 in every run against two thirds. **The owner's condition:**
    before the questions, answers and tests stages (7 to 9) are put
    to the owner stacked on this one, it is verified that the gaps
    research leaves are closed by then: for both real plans, each
    fact of the key that a research run lacks is counted again
    after those stages, by the same keys, and any still missing is
    named with its kind. A provider-specific fact no general
    question prompts for (an identifier that changes later) is the
    kind expected to remain, and its fix belongs to the questions
    library.
## 2026-11-24: how the questions stage is measured

45. **Stage 7, the questions, is tested as proposed in
    `steps/07-questions/README.md`** (the owner: "Yes and yes, go
    ahead"), at about $135, with a pilot of about $10 first whose
    real cost is reported before the rest is run. Before the yes
    the owner set one rule: "Library first, then grid, obviously no
    question should be duplicated". And the point put to them with
    it: a user who says to skip the questions is told once what
    that costs and that the stage asks them nothing, and offered it
    again; if they insist, the library is not gone through, the
    folder records that it was skipped at their word, what the
    script draws with no judgement is drawn all the same, and the
    skipping goes to the owner's list as a risk accepted. (The
    second question was put as one way or the other; the yes is
    read as a yes to the way proposed.)

## 2026-11-25: a security pass of its own; kad's design skills kept

46. **Security has a dedicated pass, run right after the questions,
    which adds its own questions to the same list so that everything
    is answered together** (the owner: "it make sense to run it right
    after the questions so it can add its own and everything can be
    answered"). The start is kad's `security-requirements` and its
    persona, which held up in kad's audits (the built code's security
    scored 4.5, then 4 in every assessment; reliability 3 in five of
    six); stage 7's read against kad's documents found the questions
    weakest on security. If kad's text is kept, whether it can be
    trimmed is looked at, and tested like any other text. UX design
    is kept from kad too (`design-system`, `screen-design`,
    `accessibility-review`), and those, with the design and the
    stack, are revisited thoroughly when stages 10, 11 and onward
    are reached. Writing the slice up as a user story and creating
    the repository both need a place in the pipeline.

47. **The user story is written at stage 14, with the owner's list
    and the planning pull request; the repository's remote is made at
    stage 12** (the owner: "I'm ok with everything as described").
    The story is written once, when the slice has its answers and its
    security criteria, not early with placeholders as kad did. What
    kad's planning skills did that stages 1 to 9 do not is accepted
    as listed to the owner on 2026-11-25: what waits on stages 8, 12
    and 14 is owed by those stages; the scope map's "sequencing
    notes" and "model what any provider of the kind does" are not
    carried.

48. **The questions stage holds, on Sonnet 5.5** (the owner: "Stage 7
    holds, especially since the security skill is coming right after
    to close the last gaps"), with the text of 161 lines in
    `steps/07-questions/eval/questions-skill.md` and the script
    `questions/questions.py`: $118.39 of the $135 agreed. Its text is
    adopted and its ten cases join the regression build. Known and
    accepted with it: against kad's documents for the two real
    slices, 28 of 38 and 49 of 70 concerns are asked in all three
    drawings, the rest mostly security, which the security pass is
    to close and is to be counted again there; Haiku leaves a value
    out in three runs of five; a real drawing is 541 to 794 lines and
    whether the state lines earn their place is stage 8's to show.
    Of the security pass the owner asks: nothing kad's security
    skills did is to be lost, and it is to be made more efficient,
    by script or tool rather than agent wherever that holds.
  - Chosen without asking: an end-to-end run through a merge still
    makes the merge up once research is written, not once the
    questions are drawn: seven of the driver's tests assume it, and
    it is changed with the answers stage, when a build has something
    to wait for.
  - Owed: the three examples' documents kept after the questions
    (`--keep` replaces folders; the owner has not been asked to
    allow it).

49. **OWASP's verification standard feeds the library and the
    security pass, on the split put to the owner** (the owner:
    "Yes", twice: to reading it first, then to the split). Of its 345
    requirements (version 5.0.0): about 30 to 35 become library
    questions in four new kinds, triaged per slice like any other
    (sign-in and sessions, stored data, files taken in, misuse of the
    product's own rules); about 30 become fixed questions the script
    draws only when a fact about the slice is true (shown in a
    browser, answers at a network address, calls out, adds a
    dependency, more than one person, makes values meant to be
    unguessable); about 150 are answers or controls, left to stage 8
    and the build's reviews. It is therefore not used as a measure:
    the mark stays kad's two documents and the real defects. Each
    entry cites the requirement by number, asks in our own words and
    quotes a short phrase; the standard is CC BY-SA 4.0 and the
    library's README says so. Stage 7's cases are run again five
    times with the grown library, once, with the security pass's
    test.
  - Built 2026-11-25, free: the four kinds, 40 entries (12, 12, 8,
    8), every quote checked by script against the standard's own
    table; the library is 290. 204 of the 345 requirements were read
    line by line; the rest (encoding, password rules, multi-factor
    mechanics, tokens, OAuth, algorithms, GraphQL, WebRTC) were
    placed by their section titles.
  - A `kept.md` written before the library grew is refused by `draw`
    until the new entries are in a row: right, and met at once by the
    cases' own fixture, which now accounts for all 290.

50. **The security pass is tested as proposed in
    `steps/07b-security/README.md`** (the owner: "Go ahead"), at
    about $105, with a pilot of about $6 first whose real cost is
    reported before the rest is run.

51. **The security pass holds, on Sonnet 5.5** (the owner: "Yes it's
    fine"), with the text of 116 lines in
    `steps/07b-security/eval/security-skill.md` and the script's
    part of `questions/questions.py`: $98.59 of about $105. Its text
    is adopted and its eight cases join the regression build. Known
    and accepted with it: kad's security concerns for the two real
    slices are asked in all three runs for 16 of 19 and 26 of 32,
    counted before two fixed questions were added and not after;
    nine concerns of the second plan wait for a design to be chosen;
    a real slice draws about 700 questions; what no session has run
    is listed in the stage's README.

52. **While a project is planned, its VM may read any website; it is
    locked to its list again before anything is built** (the owner:
    "I like the option to allow all web reading during planning and
    then lock it down again for the build"). Planning stays inside
    the VM. Met with the fourth example, whose every candidate was
    "not read" behind the VM's list.
    - Chosen without asking: it is one rule of that project's VM
      alone, for the web's reading methods only (GET and HEAD, any
      host); sending, and anything that is not the web, stay
      refused (tried on the evaluation VM: a page read, a POST
      refused, a connection to another port given nothing). A VM is
      made with the rule; `startup/machine.sh web open|lock` adds
      and removes it, and the report says which holds. An address
      read can still carry a few words out: what is in the VM while
      planning is the planning documents, never a file of the
      user's.
    - The texts keep their one message asking for sites refused: it
      is what happens in a VM the user has locked.

53. **Stage 8, the answers, is tested as proposed in
    `steps/08-answers/README.md`** (the owner: "I agree go ahead"),
    at about $125, with a pilot of about $9 first. With it: **the
    owner's list is brought to them once, after the tests of open
    facts (stage 9) and before the design**, not at stage 14; and
    **a slice brings them at most 12 decisions** on the two real
    plans, each read for whether it is truly theirs.

54. **Research is done in two passes: up front as now, and again,
    together, for what the answers need of a thing committed to**
    (the owner: "isn't it better to batch the research when we have
    the questions for that slice that we know need to be answered
    by the external source"; "Yes" to building and testing it at
    about $30). It partly reverses decision 42. Met at stage 8:
    about one answer in five that spoke of the provider said what
    its research did not, on Sonnet and on Opus alike (Opus was
    tried at the owner's question, $5.77, and Sonnet kept), and
    several "tests" were only a page to read.
    - Chosen without asking: an answer that turns on such a thing
      and finds nothing in its research is `look up`, and nothing
      is drawn while one is left; research reads the pages kept,
      then the thing's own, and adds each finding as a new fact
      with its quote, or an open point; an answer that speaks of
      the thing gives the fact and the document's own words in
      quotes, which the script looks for in the document and the
      pages kept. One session does both, as the questions stage
      loads the security text.

55. **Stage 8, the answers, holds on Sonnet 5.5, with research in
    two passes** (the owner: "Yes it holds"), with the text of 144
    lines in `steps/08-answers/eval/answers-skill.md`, the script
    `answers/answers.py` and the second pass in research's text:
    $160.45 against the $125 first agreed. Its text is adopted and
    its eight cases join the regression build. Known and accepted
    with it: about one answer in fifteen that speaks of the
    provider still says what nothing read says, and others quote
    the wrong line of a fact that does say it; a slice's list for
    the owner was 14 and 17 in two real runs of six, 8 and 12 once
    technical choices and things already decided are taken off;
    some of kad's concerns are said in an answer with no criterion,
    and what a lock leaves after a crash or a close in progress
    does with late work is in no run; Haiku does not look anything
    up. A second reader of each claim against its quotation, and
    of the owner's list, is for stage 9. What no session has run is
    listed in the stage's README.

56. **Stage 9, the tests of open facts, is tested as proposed in
    `steps/09-open-facts/README.md`** (the owner: "Yes to all 3",
    2026-11-26), at about $170, with a pilot of about $12 first
    whose real cost is reported before the rest is run. With it:
    **a second reader of each claim against its quotation is built
    and measured**, a model reading a model inside the product,
    which grades nothing and decides nothing and can only send an
    answer back to be looked up; and **the stage sends to a
    provider's test environment, the one address the user allows,
    with a key the user types** (decision 52's "sends to none"
    holds for everything else). For the two real plans the owner
    allows the provider's sandbox address for the evaluation VM and
    types its test keys there.

57. **One more round of stage 9 before the owner says whether it
    holds** (the owner: "The round", 2026-11-26), about $25 past
    the $170 of decision 56: a test prints what the thing answered
    and not a sentence of its own; a test a run settled only in
    part is sorted again; an item taken off the owner's list always
    leaves its line. Then the cases five times and one real run a
    plan.

58. **Stage 9, the tests of open facts, holds on Sonnet 5.5** (the
    owner: "Go ahead", 2026-11-26, to the recommendation that it
    holds as it stands with its limits recorded, and to two small
    changes of the text left unrun), with the text of 193 lines in
    `steps/09-open-facts/eval/open-facts-skill.md`, the script
    `openfacts/openfacts.py` and the second reader's instructions
    in `openfacts/reader.md`: $212.77 against the $170 first agreed
    and the round of decision 57. Its text is adopted and its
    fifteen cases join the regression build. Known and accepted
    with it: 65 of 75 on the cases, not 75; a session calls almost
    nothing settled by a run in a test environment (1 of 12 in the
    last two real runs), writing what was shown into the answer;
    the same test is sorted differently from run to run; one key
    fact of the first plan (an identifier that changes when a
    connection is made again) is in no run, and is owed to the
    library as a question; the reader is never run inside a case,
    and no example takes a provider through the stage. The two
    changes made after the last run, and run by no session: the
    number of a fact a test showed is written as the next one, not
    as an example's; what a call of the thing takes, returns or
    refuses is settled by its test environment. What no session
    has run is listed in the stage's README.

59. **The pilot of stage 10, the design, is agreed** (the owner:
    "Yes, then run the pilot", 2026-11-28), at about $16, on the
    proposal in `steps/10-design/README.md`: its measure (a private
    key of defects a structure could have prevented, counted by
    reading, kad's own designs as the mark), a second short list
    of the owner's brought once when the design is drawn, and about
    $160 in all. The pilot's real cost is reported before anything
    else runs, and the rest is said again with it. Agreed with it,
    after the owner asked whether the screens belong to this stage
    and whether they change a structure: the order is kept (screens
    are stage 11), and the design names what the person sees as one
    tactical part, with what it reads and asks of the others; how
    it looks is not said there.

- The security pass as built (decisions 46, 48, 49), 2026-11-25,
  chosen without asking:
  - It writes one file, `security.md`, in the questions' own folder,
    and the questions are drawn again with it: one list, one mark.
    The stage script counts it done when the drawing carries that
    file's mark too.
  - Six facts, each yes or no with its source, and `yes` where the
    documents do not say; 28 fixed questions drawn only for the
    facts that hold.
  - Two more exits for every class of sensitive values: a reply
    that succeeded, and where it is stored with every copy.
  - A skip of the questions is not a skip of security: it is next
    all the same, and has the same rule of its own (once what it
    costs; on a second no, recorded and every fixed question drawn).
  - After a change to the documents the questions stage brings
    `kept.md` up to date and then loads the security text: one
    sentence added to stage 7's adopted text, tested with its
    re-run.
  - Its folder is `steps/07b-security`: the stages after it keep
    their numbers.
  - In testing ($98.59 of about $105): what is wanted may be a
    thing the documents name, or `nothing`, dismissed with its
    reason; the stop is looked for first and kept for what the
    documents say is out; a public value has a row of its own; the
    pass adds a sensitive value `kept.md` lacks; two fixed
    questions more where the slice calls another system (a person's
    sign-in for it; how a credential first reaches the product),
    30 in all, after the read beside kad's documents.
  - Stage 7's adopted text gained "with your file tool, not through
    the shell" where rows are edited: one Sonnet run of five edited
    them by script and stopped.
  - Left: two reliability questions kad's documents ask and the
    library lacks (expected and unexpected outcomes told apart in
    the records; one reference from the screen to the record).
    Haiku was run on the real plans beside Sonnet (12 cents): the
    same facts, about half the rows asked, and a readable list
    dismissed as needing "physical access". Sonnet is proposed.

- Stage 8, the answers, as built (2026-11-25), chosen without
  asking; its test, its cost and three points of the owner's are in
  `steps/08-answers/README.md`, and nothing paid has run:
  - An answer settles many questions, and a script keeps the count:
    a slice draws 280 to 700 questions, and a session is given them
    sixty at a time until none is left.
  - Five kinds: fact, not here, test, owner, chosen. The script
    refuses a fact resting on no document, a decision for the owner
    without options, a recommendation and what happens if left, a
    criterion on a guess or on a decision not yet taken, and a wait
    with no number.
  - One drawing beside the answers holds the criteria, the owner's
    list by harm, the tests by harm and the choices: the tests stage
    and the owner's list read it.
  - A criterion names the slice's item it is under, or a new one:
    this settles how an answer attaches to the checkable list.
  - A decision the owner takes is recorded on its answer in their
    words, and the report keeps the command that draws it whatever
    stage is next.
  - The stop for a criterion the facts make impossible is left to
    research, which already has it.
  - kad's three skills are not an arm of the cases: they are set
    beside ours on the two real plans.

- Stage 9, the tests of open facts, as built (2026-11-25), chosen
  without asking; its test, its cost and three points of the owner's
  are in `steps/09-open-facts/README.md`, and nothing paid has run:
  - A test is sorted one of four ways: a page would say it (looked
    up by research's second pass), one request to the thing's test
    environment settles it (run), only a person can make it, or it
    shows only in use. On three kept runs of the real plans, read,
    about one test in five can be run and two thirds of the gravest
    are the owner's own to make.
  - A test is run by a command, never by the session's own shell:
    it is sent only to an address the block names with the
    documentation's own words that say it is a test environment,
    what it printed is kept under a seal, and a result is given in
    those words. Never the real thing, even at the user's word:
    that test is theirs to make, and their word settles it.
  - A key is typed by the user at a hidden prompt in a terminal of
    the VM, kept outside the project, and taken out of whatever is
    kept. One pasted into the conversation is not used.
  - What a test shows is added to the thing's research document as
    a fact, under `## Shown by a test`, so the answer rests on it
    as on any fact and the answers' script is unchanged for it.
  - A test left open says what the slice does either way; the ones
    of high harm are shown to the owner with their list.
  - The owner's list is read in the same file: each decision that
    waits is theirs by one of four kinds, or taken off (a technical
    choice, already decided, the same as another) with its answer
    changed. More than twelve truly theirs stand, and are said.
  - The stage is not done while a decision waits: the list is
    brought, and the design does not start, until each is decided
    or left at the owner's word (`Decided: left`).
  - Answers that leave no test and no decision need no such stage:
    the stage script passes it over.
  - One command draws the answers and the open facts together.
  - The examples' user, asked for a key or a site for a test, has
    none; shown their list, takes what is recommended.
  - The second reader of a claim against its quotation is not
    built: it is the owner's first point.
  - Met while building, and put right with unit tests: a fact the
    second pass added made the questions stale and sent a session
    back to them (their mark now leaves out what research adds
    under its two later headings; one phrase of research's adopted
    text names the heading); the answers' script took the words
    between two quotations for a quotation. Both change adopted
    things: every earlier stage is run once, and the answers'
    look-up case five times, in stage 9's test.

- Stage 9 as run (decision 56), 2026-11-26, chosen without asking;
  $165.93 of about $170, put to the owner and not adopted:
  - The second reader is a session of the tool's own, started by
    the script with nothing but the claims and their words, twenty
    at a time, on Sonnet (Haiku left a fifth unread in one run and
    flagged nine in ten at first). The script keeps its verdicts
    with a mark of each claim, so a changed answer is read again;
    the drawing refuses a claim flagged or unread. On a machine
    with no reader the drawing says the claims were read by nobody
    but their writer, and the stage is not held.
  - A claim is an answer that names the thing committed to, or
    rests on a fact of its research document without naming it.
  - What the reader still names after a second reading is taken
    out of the answer; the choice and its criteria stay.
  - A test no page settled is sorted again and keeps the pages
    read; the script refuses it left as a page.
  - Before a decision is read as the owner's, the documents are
    looked in: what one already says is decided, scope or not.
  - A run refused for a key it names is told the names of the keys
    the machine has, never a value.
  - A decision the owner leaves is recorded as left, by the
    report's own line: the answers' adopted text is not changed.
  - The owner's sandbox keys were piped from their keychain into
    the evaluation VM at their word, shown nowhere.
  - The examples' documents are kept again after every stage (the
    owner's yes), the fourth's privately. A run that leaves no new
    document for eight turns is stuck.
  - Of an earlier stage: only a table headed "State" gives states.
  - Known and left, for the owner's word on whether the stage
    holds: a test's script may print a sentence of its own, and
    that sentence is then quoted as the result; the same test is
    sorted differently from run to run; an item taken off the
    owner's list by changing its answer alone leaves no line.

- The round (decision 57) as run, 2026-11-26; $212.77 in all, put
  to the owner and not adopted:
  - Each of the three changes is a refusal of the script as well as
    a sentence of the text. The list as it stood when the stage
    began is kept the first time the stage is asked, or read from
    the answers' own drawing.
  - Its first launch ran on the commit before it ($24.31, said to
    the owner at once). A paid launch now begins with a check, by
    checksum, that the VM, the built plugin and its texts are those
    of the commit, and runs nothing otherwise.
  - Of a research document the questions' mark covers only what
    they are drawn from (its open points and what it says of the
    planning documents), taken without Windows line ends.
  - Known and left: after the round a session calls almost nothing
    settled by a run in a test environment (1 of 12 run), writing
    what was shown into the answer and leaving the test a person's;
    the text's own example of a fact's number (`F31`) is copied in
    one run of five.

- Stage 10, the design, as built (2026-11-28), chosen without
  asking; its measure, its test, its cost and three points of the
  owner's are in `steps/10-design/README.md`, and nothing paid has
  run:
  - The session's judgement is one file of parts, boundaries and
    decisions; a script lists what has no home, refuses what does
    not hold and draws `NNN_designed.md`. Its folder is `designing/`:
    `design/` holds the plugin's own design document.
  - The unit of a home is the answer, not the criterion: a chosen
    answer with no criterion is read by nobody else, which is how
    "said with no criterion" is closed. A dismissed answer and a
    fact with no criterion need none.
  - A strategic part never names a thing committed to, and one
    tactical part isolates it: held by script, by the thing's name.
  - What the design says of a thing committed to rests on a research
    fact with its words, as an answer does, on an open test, or is
    named `unknown` with what is done either way.
  - **No technology is picked here.** A boundary says what the slice
    needs of whatever stands behind it and whether this slice forces
    a choice; the stack stage picks against it. kad's design chose
    the store and the screen's shape; here that would be a belief
    about a dependency nobody researched.
  - A dependency the user did not name: something the slice needs
    from outside goes back to the approach, which has its way to
    research; the way back from a technology picked is the stack
    stage's.
  - kad's approval of every decision one at a time is not carried
    (the design document's section 4). A decision is the owner's
    only as a cost in money, a risk no structure removes, or what
    cannot be taken back.
  - kad's three checks are answered yes or no on every chosen
    decision, and the script draws those with three yes as records.
    Where they are kept for good is stage 14's.
  - What keeps two things apart carries five orders of events, each
    required; a hole in a chosen decision is refused. Every design
    says whether anything runs at once, and "nothing" is refused
    where the answers settle a question about two things at once.
  - What goes back to an earlier stage keeps the design open; the
    stage script says so, and names no other stage as next for it.
  - Asked for a structure the principles argue against, the slice is
    designed as recommended and the cost said once; insisted on, it
    is recorded as the owner's.
  - kad's skill is not an arm of the cases; its designs of the two
    real plans are the mark. The key those are counted against (the
    defects a structure could have prevented, twelve and eight) is
    this session's own reading, fixed before any run, private.
  - A real run starts from a kept stage 9 run whose owner's list
    waits: the launcher's user takes what is recommended, as the
    examples' user does; it is nobody's real decision.
  - The examples are to be run from their kept answers: the open
    facts' kept documents are stale by that stage's last two
    sentences.

## Put off to the stage that needs them

- **Locking the web again before the build** (decision 52): the
  first build stage must not start while the VM can read any
  website. The command exists (`machine.sh web lock`, the user's to
  run outside the VM); what refuses the build stage until it is run,
  and how a session inside the VM knows, is owed to that stage.
- **How an outcome on the benchmark is tested** (research, questions,
  answers): put to the owner with the research stage's test and cost.
- **The numbers for the question measure** (how many questions a slice
  may bring; how often the owner taking the offered option is too
  often): with the answers stage.
- **A measure for each of the problem, scope, requirements, slice,
  design and screens stages:** agreed when each is reached.
- **Where the user finds `source.sh` on their own machine,** and when
  the scan is run (before the planning pull request is merged?):
  with the plugin's real install, which waits for the run on the
  owner's Mac.
- **Approaches the user considered and rejected:** kad's skill asked
  and recorded them; no stage here does yet.
- **A second slice that commits to a thing already researched**
  (whether the earlier document is carried forward, and what is read
  again): when an example reaches a second slice's research.
- **A dependency the user did not name:** for the design, settled
  as built (a need from outside goes back to the approach; no
  technology is picked there). What a pick of the stack stage does
  to get back to research is still owed, to that stage.
- **A screen that needs of the structure what the design does not
  give** (a view of two parts together, in a shape no part offers):
  the screens stage sends it back to the design, a `design:` line
  in its own "goes back", as the design does to the stages before
  it. A behaviour the screen would add goes back to the answers or
  the requirements instead. Owed to stage 11.
- **The architecture map** kad's design consulted first: no map
  exists before a build; owed when the build makes one.
- **A decision of the design taken mid-build under a delegation**
  (kad's): with the first build stage.
- **Where the design's decisions that earn a record are kept for
  good:** with the planning pull request (stage 14).

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
- The slice stage as built (`startup/`, `steps/04-slice/`),
  2026-11-23:
  - A slice's number in the set is its name: never changed or
    reused, and its own document is in the folder of that number
    (`slice-002/`). The chosen slice is the row whose state is
    `chosen`; every stage after the slice is read in its folder.
  - The stage script names both documents of the stage at once (the
    set, and where the chosen slice's own will go), so a session
    that has just been given the user's choice need not read the
    documents again.
  - A merged pull request says what it completes on one line of its
    description, `Completes: slice 2: item / 1, item / 2` (criteria
    of a slice) or `Completes: item` (an item outright). The
    delivery stage will write it; until then it is made up. The
    latest fifty merged pull requests are read.
  - A slice is built when merged work names every criterion of its
    document; a box is checked when every slice that holds its item
    is built. The script works that out and says exactly what to
    mark and check; the session makes the marks. A command that
    makes them itself is the next step if a session is seen to mark
    on say-so.
  - An issue is placed once any version of the set names it by its
    number. Issues are placed only once a set exists. The session
    may read one issue (`gh issue view`) and changes nothing on the
    tracker.
  - A coming-back that is due is named as the next stage, ahead of
    whatever the documents would name; the routing table is not
    changed for it.
  - Marking a slice, checking a box and recording an issue are made
    in the documents as they stand: only a change to the rows of the
    set is "a changed set" (corrected in place before any slice is
    built from it, a new numbered version after).
  - When every slice is built and every box checked the script says
    the activity is done and that the next "now" is the user's to
    name; redrawing the map and a list for the new "now" wait for
    the stages that own them.
  - The approach's and research's documents are named in the slice's
    folder (`slice-NNN/NNN_approach.md`, `slice-NNN/NNN_research/`)
    until those stages are built. The paused research stage's
    scenarios were moved there so that they still build; none was
    run.
  - Fourteen cases for the ten rows: rows 4, 6, 9 and 10 hold two
    situations each, and a proposal and the yes to it are two
    turns. The bar is every case in every run. Three more were
    added in the closing pass (decision 38): seventeen.
  - The bare arm's routing table says this one stage is done from
    the report alone (the table's last line would rightly stop it).
  - On the owner's real requirements: three of kad's requirements
    documents, each "confirmed in scope" bullet rewritten by hand as
    one named box, nothing added (private, in the audit repository
    under `04-slice/inputs`). The slice known to have been cut too
    wide came from a scope change mid-build, not from a list, so it
    cannot be given to this stage as an input.
  - An activity is not done while a question stands under "Not yet
    confirmed" in its list: the script names the requirements as
    next. The part of an item that waits for an answer is a row of
    its own in the set, so its box stays unchecked.
  - An issue no row covers is placed once the user has said in or
    out; until then it stays due.
  - Asked for a wider cut, the stage gives the size of each cut
    with what the wider one costs (taken from kad's skill).
  - A criterion's examples are never a name or figure the user
    gave: said in this stage's text as well as the routing table,
    since a run wrote one.
  - A coming-back is done on "go on", as any stage is; asked what
    is next, a session names it and waits.
  - Opus was run bare only, and Haiku on the first form of the text
    only: Sonnet holds with the text and is the session's model.
  - The slice text was loaded on trial (`slice=...`) until the owner
    said the stage holds (decision 39); it is in the adopted list
    since.
  - `e2e/tally.py` counts a pass with and without the checks of
    form; `e2e/run.py` carries an example on through a set, a chosen
    slice and one made-up merge (`--through requirements` for the
    earlier ending).
- The approach stage as proposed (`steps/05-approach/README.md`),
  2026-11-23, agreed the same day (decision 40):
  - Candidates come from the documents (a provider set as a limit),
    the user, or a search the user says yes to; never from memory.
    With neither, the need waits. At most three are kept a need.
  - The search is the tool's own web search, for names and addresses
    only. If it does not work from a session in the VM (the pilot
    checks), candidates come from the user alone.
  - A candidate's pages are read with `research/page.py`, four a
    candidate at most, and kept in the slice's `pages/` folder, one
    place for this stage and research.
  - A provider fixed by a limit still gets the short read, against
    what the slice needs of it.
  - The way that commits to nothing is a row of every table where
    there is one.
  - Every need of the slice is put to the user in one message, not
    one question a decision as kad did.
  - The one question also asks what the user has already ruled out,
    which gives "approaches the user considered and rejected" its
    home.
  - Every commitment is recorded; kad's three checks for whether a
    decision earns a record wait for the design and the stack.
  - The stage script skips the approach when the slice's needs are
    `none`, and keeps it as next while a need is `waiting`. The
    slice text and the routing table are not changed for it.
  - kad's arm is `architecture-design` with `adr`, on Sonnet, on the
    four cases it has something for. Opus is run bare once a case.
  - The outcome is counted on one real choice of the owner's, from
    kad's own records of it (private); the README names no provider.
- The approach stage as built, 2026-11-23:
  - A need the user meets themselves is written `Decision: without`,
    with nothing asked: there is nothing to commit to.
  - When a site is refused the document is still written, the
    candidate's row saying `not read`, the need `waiting`: the stage
    script then keeps the approach as next without being told why.
  - A change made in place leaves a line `Changed: <date>: <what and
    why>` under its need.
  - The stage script also says two things nobody asked for: that an
    approach's decisions and its "Committed to" disagree, and that
    research numbered before the approach now standing is older
    than it. Each thing committed to gets its research document's
    name from its own (`Postbox` is `postbox.md`).
  - The report names the page reader through the startup scripts'
    folder (`startup/../research/page.py`), so that every stage's
    canned reports stay free of this machine's paths.
  - Three of the slice stage's cases and one of its checks named the
    approach as the next stage for slices that need nothing from
    outside. They now name research; the slice text is unchanged.
    Those cases are run again with every earlier stage's.
  - The end-to-end driver's user, asked for a candidate, has none;
    asked whether to search, says no; asked to commit, takes what is
    recommended. A brief says otherwise where an example needs it. A
    run through the approach ends when no need waits, four turns
    after the approach was written if one still does, or a turn
    after the slice when it needs nothing.
  - A pass may allow the search tool (`ALLOW_TOOLS`), which only
    this stage's cases ask for.
- The approach stage as run, 2026-11-24:
  - The routing table gained one rule, for every stage: a stage's
    text is loaded before anything of it is written or recorded, and
    the user's answer to a stage's question, however short, is that
    stage's work. Haiku recorded short answers by hand without it.
    Every earlier stage's cases were run again with it.
  - The quote check reads again, once, a page that is quoted and has
    no saved copy, before calling the quote wrong: it uses the same
    reader, so a site not allowed is still not read.
  - The stage is put to the owner as holding on Sonnet 5.5 (65 of
    65) and not on Haiku 5.5 (57 of 65), after three rounds of tuning
    where two were planned; the third cost $0.43.
  - The short read is six pages a candidate, the user's limits
    first, where the proposal the owner agreed said four: on the
    real choice four left the price page unread in two runs of
    three. Said to the owner when the stage is put to them.
  - The five-run pass was run three times ($24 where $11 was
    guessed): the text changed twice after the first, once for the
    read and once for a page's instruction.
  - The examples could not start from their kept documents (the
    routing table changed), so the pass from the first message
    stood for both; it stopped at the approach, not at a merge.
- Research in its new place, as proposed (`steps/06-research/README.md`),
  2026-11-24; not yet agreed:
  - One document a thing committed to, under the name the stage
    script already gives; the states of every lasting thing in one
    `states.md` a slice, so that the questions stage's grid has one
    place to read.
  - A page the approach kept is given back from its copy by the page
    command itself: a script's work, by unit test, not a line of the
    text a session might skip.
  - After a change of mind the research folder is kept: the newly
    committed thing gets its document there, and the document of a
    thing no longer committed to is left with a first line saying it
    no longer stands. The stage script names research as next again
    until every thing committed to has its document.
  - When the full read shows the commitment cannot do what a
    criterion needs, research says so and changes nothing: the
    approach's change of mind and the slice stage already have that
    work.
  - The benchmark's approach documents are written by hand from
    kad's records of what was chosen (private).
  - Raw runs go to the audit repository under `06-research/`; the
    first pilot's stay under `04-research/`, the stage's number then.
  - Startup's scenario of a stage not built names the questions when
    research is on trial (`KD_TRIAL`), with a made-up research
    document; a unit test.
  - The cost put to the owner is about $90, not the $40 guessed at
    the first pilot, which predates decision 38.
- Research as built, free, 2026-11-24 (nothing paid run yet):
  - `states.md` is always written where the requirements' list of
    outside systems and lasting things is not `none`; when the slice
    touches none of them it says so in one line. A list that does
    not have that heading is taken to have something.
  - The stage script names the documents still to write on the line
    that names research as next, and a research document whose thing
    is no longer committed to as no longer standing.
  - A kept page is given back only from the slice's own `pages/`
    folder, never from the machine's folder for temporary files,
    which may hold another project's copy; `--again` asks the site.
  - When a second site is refused mid-read, what opened is written
    and the rest listed under "Not opened"; the stage script then
    counts research as written, and it is the user's "I've allowed
    it" that brings the session back to finish (the routing table's
    rule that an answer to a stage's question is that stage's work).
    Case 6b tests exactly that; the script is changed if it fails.
  - The cases' arms are `bare`, `text` and `kad` (kad's
    `domain-model`, on cases 4 and 5), as for the approach.
  - The end-to-end driver ends a run through research once a
    research document is written, or a turn after there is nothing
    to research; a run where none is ever written ends as stuck.
- Research as tuned and closed, 2026-11-24:
  - A page over 300 lines is given as its headings, each with its
    lines, and read a part at a time with `page.py lines`: a
    session's shell cut the real provider's reference pages, and
    the session then searched for the words it had thought of. The
    numbers (300 lines a page, 150 a part) are a first guess.
  - A twelfth case holds a fact deep in a long made-up page, so the
    bar at five runs is 60 of 60, not 55 of 55.
  - The text grew from 137 to 149 lines over two rounds: the
    reference pages are read whatever the criteria say; a long page
    by its parts; what names a thing on the other side and whether
    that name can change; how a failure is told from a success; an
    open point is searched for in the kept pages before it is left
    open.
  - Case 6b passed in every run on Sonnet, so the stage script still
    counts research as written when pages were refused, and the
    routing table's rule brings the session back.
  - The key's patterns are not changed after a run. Where a fact is
    in the documents in other words, both numbers are given: by the
    pattern, and as read.
  - A check that fails a good answer is corrected with a unit test
    and the kept runs graded again for nothing; the count as first
    graded is given beside the corrected one.
- The questions stage as proposed (`steps/07-questions/README.md`),
  2026-11-24; not yet agreed:
  - The stage leaves a folder, as research does: `kept.md` is the
    session's, `questions.md` is drawn by script and never written
    by hand. The stage script's name for it changes from a document
    to a folder when the stage is agreed.
  - The script is Python, like the page reader: planning runs in
    the project's VM, which is Linux.
  - A kind of action the slice does nothing of may be dropped whole
    with one reason, and entries may share a row: E3's triage wrote
    a line for each of the 250, which is most of what a run costs.
    Whether dropping by kind loses an entry a defect depended on is
    what the count on the two real plans shows.
  - A kept question applies only to a thing the documents or
    `kept.md` name: E3 lost the things a triage did not think of.
  - What the slice takes in is listed by the session and held to
    the criteria and research by script; no stage before this one
    lists fields, and changing research to list them would stale an
    adopted stage for a list this one can check.
  - Which ways a value can be wrong are drawn by its kind (a choice
    is not "too long"), every way for a kind called `other`: E2
    spent a third of its cells on what could not happen. The table
    of kinds is a first guess.
  - Settings get one rule, always drawn: a build reads settings no
    plan names (E4).
  - Two parts carried from kad by script and not by the session:
    each sensitive value against the five places it leaks to, and
    the seven questions kad's two skills asked the owner first.
  - An event of the state grid is each criterion of the slice, five
    that hold for anything (again, a reload, a restart, a second
    copy, time), and each thing committed to being down, slow or
    acting with its reply lost. A provider's errors by name are not
    events: research writes them as facts, and the library's
    questions on calls are applied to each request.
  - The library first, and no question twice (the owner, asked
    whether the stage uses the library: "Library first, then grid,
    obviously no question should be duplicated"). A grid's line is
    not drawn when a kept library question applied to the same
    thing already asks it. Chosen here: the library's line is the
    one that stands, naming each state of a lasting thing; "the
    same thing" is the same value or lasting thing, so a question
    kept for a request does not spare the lines of a thing's
    states; which entries ask the same as which column is a fixed
    table in the script, from a reading of the 250.
  - Whether the questions are stale is a mark of every document
    they were drawn from, kept in `questions.md`'s first lines.
  - A lasting thing the slice creates that the requirements' list
    does not name is walked: one sentence in research's text, and a
    check here. Research's cases are run again.
  - The requirements' own open questions are not carried into
    `questions.md`: they are the requirements stage's, and the
    slice already says which of its parts wait for them.
  - Arms: bare, our text, kad's two skills together on two cases,
    and E3's triage brief on the first real plan only, where it was
    measured. Opus only where Sonnet with the text does not hold.
  - The defects the triage is counted against came from wider
    slices than this plugin cuts: each is marked as within the thin
    slice or not before any run, and only those within count.
  - The two library entries the gap count is expected to call for
    are proposed after the count, not before: the library is not
    changed while it is being measured.
- The questions stage after its pilot, 2026-11-24:
  - Leaks are drawn for each class of sensitive values, not each
    value: 24 values against five places was 120 lines asking the
    same thing.
  - A question is dropped when its harm needs what the documents
    say the product does not have (many users, several people
    running it, more than one installation), with the document's
    line as the reason; where the documents do not say, it is
    kept. This narrows "when unsure, keep", for the owner's "198
    seems like a lot"; the count of tied defects kept is what
    holds it.
  - A kept question has a row and a reason of its own; only
    dropped ones share a row. Sharing saved cost and let twelve
    questions be kept as one.
  - Opus was tried at the owner's suggestion, once on each real
    plan beside Sonnet: it kept more and cost twice as much.
    Sonnet stays the model proposed.
  - After three runs of every case: `kept.md` lists what the slice
    creates and keeps, and the script refuses a thing listed with
    no table in `states.md`, and a criterion the file names
    nowhere. Both were left to the text and missed about half the
    time. This settles research's first open point as far as a
    script can: a thing kept that no list names is walked once a
    session lists it; whether it lists it stays judgement.
  - The routing table gained one rule: told to skip the next stage,
    that stage's text is loaded and takes it. Startup's cases are
    run again with it before the stage is put to the owner.
  - The earlier `kept.md` the changed-documents cases start from is
    one a session wrote, not one made up: a thin one was rewritten
    whole, and rightly.
  - A changed `kept.md` is edited in place, never written again
    whole: one Sonnet run of five reworded rows nothing had changed.
  - Haiku's misses on this stage (a value left out in three runs of
    five, the skip misrouted in one) are not chased with text: they
    are what the model choice is for.
- Put off: installing the plugin inside a new VM, and what of the
  planning folder's memory survives a VM being destroyed.
