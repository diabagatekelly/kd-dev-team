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

## Put off to the stage that needs them

- **How an outcome on the benchmark is tested** (research, questions,
  answers): put to the owner with the research stage's test and cost.
- **The numbers for the question measure** (how many questions a slice
  may bring; how often the owner taking the offered option is too
  often): with the answers stage.
- **A measure for each of the problem, scope, requirements, slice,
  design and screens stages:** agreed when each is reached.

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
  fresh Windows machine and a Mac with nothing extra installed.
- This repository's layout.
