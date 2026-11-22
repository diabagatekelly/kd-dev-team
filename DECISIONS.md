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
- Put off: installing the plugin inside a new VM, and what of the
  planning folder's memory survives a VM being destroyed.
