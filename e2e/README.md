# End-to-end runs: the adopted stages together, on whole examples

Each stage's own test starts from documents written by hand. Here a
session goes from a first message through every adopted stage, each
stage reading what the one before actually wrote, in a conversation
as long as it takes (decision 28).

- `examples/NAME/brief.md`: every word the user will say. Their
  first message; a table of topics, each with what it covers and the
  answer, word for word; the line for what no topic covers; the line
  said when a document is first shown (a change of mind, an addition);
  and how many of the requirements' questions are answered at first.
  `examples/NAME/project/`, where there is one, is the project the
  session starts in.
- `run.py`: runs one example. The session is the tool run headless
  with the assembled plugin. The user is a script: it says only what
  the brief holds. A model is used for one thing, to say which of the
  brief's topics the session's message asks about; it never writes an
  answer, and what it picked is kept beside each turn in
  `turns.json`, so a wrong pick can be seen. Nothing here judges a
  run: it is read afterwards, in its transcript and its documents.
- `make_plugin.py`: assembles everything adopted so far into one
  plugin (rebuilt each time, not kept in git).
- `machine/`: the made-up machine the stand-in tools answer as:
  inside the project's VM, a tracker with nothing open.

To add an example, add a folder with a brief. To run one, inside the
evaluation VM, after `steps/00-startup/eval/setup-vm.sh`:

    python3 -I e2e/make_plugin.py
    python3 -I e2e/run.py e2e/examples/01-a-one-line-idea --out /tmp/e2e/01-run1

A run leaves `transcript.md`, `turns.json`, `tools.txt` (every tool
call the session made), `summary.json` (turns,
questions put, how many were asked that no topic covers, whether the
documents are numbered in order, cost, how it ended) and the project with its planning documents. The
examples are made-up and may be quoted here; raw runs go to the
audit repository under `e2e/runs`.

The driver's unit tests: `python3 -I -m unittest` in this folder.

## What the runs found, and the test each became

Every problem a run meets ends in a unit test, an evaluation
scenario or a change to a text that is then tested again (decision
29). One line a finding.

| Found | By | Became |
|---|---|---|
| The made-up machine was "inside a VM" but the stand-in VM tool was still on the path, so the live report said otherwise | example 1, first run | `run.py` takes the absent tools off the path: `test_an_absent_tool_is_off_the_path_and_its_neighbours_stay` |
| A report with a part the script could not read had no row in the routing table; the session went on to the planning conversation without a verified machine | example 1, first run | routing table row 0; startup scenario `19-a-part-not-read` |
| The session asked for the planning folder and never recorded it; the three documents were written without their numbers and the stage script found none of them | example 1, second run | `stage.sh` prints the command that records the folder (and makes it), four unit tests; routing table row 7; startup scenario `20-the-folder-named`; the driver's `numbered_in_order` |
| A session that finished a stage had no way to learn the next stage's document: the report is given once, at the start | example 1, second run | `stage.sh` prints the command that reads the documents again; routing table row 10; the driver's `numbered_in_order` (no stage scenario: a canned report cannot answer a live re-read) |
| A command the report prints is run in the session's own shell, which is not told where the plugin keeps its data, so the folder would be recorded where the next report does not look | reading the script for the two above | each printed command carries the data folder: `test_a_command_the_report_gives_reaches_the_same_record_as_the_report` |
| The first reply listed what the product might be ("plot allocation, waiting lists, rent, a noticeboard..."), in both runs | example 1 | routing table ("never suggest what the product might be or do"); a check in startup scenario 20 |
| A terse user's short answers were written up as the whole problem: the plots given to friends and the evening a week on the phone never came out | example 1, second run | problem text (one last question for an account given answer by answer); problem scenario `07-answer-by-answer` |
| Requirements written as "I can ...", in the problem document's voice, so who does it is not said | example 1, second run | requirements text (who by role); check `form-who-is-named-by-role` on every requirements scenario |
| Asked to go on past the last stage built, the session offered to do the research "informally" | example 1, second run | routing table (a stage with no text is not built: say so and stop); startup scenario `21-a-stage-not-built` |
| The earlier stages had never been run with the later texts loaded | looking over the tests | `regress.py` rebuilds every stage's scenarios with everything adopted, with a unit test |

Seen and left: the first list of requirements had one item and four
questions, and grew to three items from the answers, which is the
stage working as meant.

| The user was a second model answering from a prose brief: asked what it did not know, it said "nothing" though the brief held an unknown, and its wording changed from run to run | example 1, second run; the owner | the user is a script that says only the brief's own words (`Brief.reply`, ten unit tests); a model only sorts the question into the brief's topics |
| Given the folder by its full path, the stage script refused it though it was inside the project; the session then waited for a folder for 25 turns | example 4, first scripted run | `stage.sh` takes a full path inside the project: `test_a_full_path_inside_the_project_is_recorded_as_the_folder_inside_it` |
| A run whose user could only repeat itself went on to 30 turns (twice; $14) | examples 3 and 4, first scripted runs | the driver ends a stuck run: `test_it_ends_when_the_user_has_only_the_same_thing_to_say` |
| The brief's "Planning is fine." read as no folder at all to one session and as a folder named `Planning` to another, which the driver then did not find | examples 3 and 4 | the two briefs say "Put them in a folder called planning." |
| The sorter took things the session stated for questions, so the user answered what nobody asked ("No reason, a friend mentioned it.") | example 2 | the sorter is told what counts as a question, told that a request without a question mark is still a question |
| A user who gave one limit in a full account was never asked for the others; a privacy limit and "phones only" never reached the documents | example 2 | problem text: the last question also asks what limits what can be done (problem scenario 07 re-run) |
| In the evaluation a session that read the documents again was told no folder was chosen (2 runs of 21, twice) | the pass over every stage | each scenario records its folder in the project, where the session's shell can read it (`scaffold` in the startup case builder) |
| A check for "suggests the product" fired on a session saying "I won't suggest what the product might be"; three other checks failed good answers | the pass over every stage | the four checks corrected in the case builders |
| "Give me the path" has no question mark; the driver took it for nothing asked and the user said "Go on." until the run was ended as stuck | example 3, second scripted run | every message goes to the sorter: `test_a_request_with_no_question_mark_still_reaches_the_sorter` |
| For "practise the verses I get wrong" the list had three items and seven questions, and none asked what practising is: what the person does and is shown | example 4, second scripted run | requirements text: a ninth kind, **does**; requirements scenario `08-a-verb-that-does-not-say` |
| The two ways a teacher tests today ("carry on a verse", "name the surah") were written as items, while the question of what practising should be stood open beneath them | example 4, third scripted run | requirements text (nothing from how it is done today; an item that would assume an open question's answer waits); requirements scenario `09-today-is-not-what-is-wanted` |
| In a project that already had code the session read none of it, and asked the user whether the register holds the singers and their voice parts, which the code shows | example 3, third scripted run, read in full | requirements text (where the project has code, read what it does for this activity; ask nothing it shows; what already works is no item); requirements scenario `10-a-project-with-code` |
| A run kept no record of what the session did, so whether it had read the code could only be found by hand | example 3 | the driver writes `tools.txt`, every tool call of the session: three unit tests |
