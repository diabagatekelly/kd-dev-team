# End-to-end runs: the adopted stages together, on whole examples

Each stage's own test starts from documents written by hand. Here a
session goes from a first message through every adopted stage, each
stage reading what the one before actually wrote, in a conversation
as long as it takes (decision 28).

- `examples/NAME/brief.md`: who the user is, their first message,
  what they know and do not know, and how they behave (a change of
  mind, an answer skipped). `examples/NAME/project/`, where there is
  one, is the project the session starts in.
- `run.py`: runs one example. The session is the tool run headless
  with the assembled plugin; the user is a second session with no
  tools that answers from the brief and nothing else. The stand-in
  user is not a judge: a run is read afterwards, in its transcript
  and its documents.
- `make_plugin.py`: assembles everything adopted so far into one
  plugin (rebuilt each time, not kept in git).
- `machine/`: the made-up machine the stand-in tools answer as:
  inside the project's VM, a tracker with nothing open.

To add an example, add a folder with a brief. To run one, inside the
evaluation VM, after `steps/00-startup/eval/setup-vm.sh`:

    python3 -I e2e/make_plugin.py
    python3 -I e2e/run.py e2e/examples/01-a-one-line-idea --out /tmp/e2e/01-run1

A run leaves `transcript.md`, `summary.json` (turns, questions put,
cost, how it ended) and the project with its planning documents. The
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
stage working as meant. The stand-in user, asked what it did not
know, said "nothing" though its brief held an unknown: a limit of
the stand-in, not of the plugin.
