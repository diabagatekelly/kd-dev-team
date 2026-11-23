# End-to-end runs: the adopted stages together, on whole examples

Each stage's own test starts from documents written by hand. Here a
session goes from a first message through every adopted stage, each
stage reading what the one before actually wrote, in a conversation
as long as it takes (decision 28).

- `examples/NAME/brief.md`: every word the user will say. Their
  first message; a table of topics, each with what it covers and the
  answer, word for word; the line for what no topic covers; the line
  said when a document is first shown (a change of mind, an addition);
  how many of the requirements' questions are answered at first; and,
  where wanted, after which documents the user closes the session
  and comes back in a new one (example 2 does, after each of the
  first two).
  `examples/NAME/project/`, where there is one, is the project the
  session starts in.
  `examples/NAME/files/`, where there is one, holds files of the
  user's own: they are never put in the project, and after the run
  the plugin's own scan says whether a value of one was written
  down.
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

## How much is run, and when

The owner wants these suites neither slow nor dear (decision 31).
What is free is done first and always; what costs is run only on
what changed, and widened only when a stage is put to the owner.

| When | What is run | About |
|---|---|---|
| Every commit | every script's unit tests, on three systems | free, 2 minutes |
| A check is changed or added | `regrade.py`: the kept transcripts graded again by the checks as they stand | free, seconds |
| A scenario is new | one run on Haiku, to see that it builds and its checks can pass | under a cent |
| A text is changed (one batch for a round of fixes) | the changed and new scenarios five times, the rest of that stage once, on Sonnet | $1 to $3, 10 minutes |
| The routing table is changed (every stage loads it) | every stage's scenarios once | $4, 15 minutes |
| A fix came from an end-to-end example | that example, once | $1 to $2.50 |
| Before a stage is put to the owner | its changed scenarios five times, the rest once; the four examples once, side by side | $3 to $5 a stage, 10 minutes; all four stages with the examples, about $15 and 30 minutes |

A round of fixes is meant to stay under $3 and ten minutes. A pass
that would go past $12 is said, with its reason, before it is run.

`regrade.py PLUGIN TRACES NAME` was checked against the tool itself:
on 1,305 checks of kept runs its verdict was the tool's every time.

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
| Whether the folder recorded in one session is found by the next had never been run | looking over the tests | the driver lets a user come back in a new session (two unit tests); example 2 does after each document: three sessions, the folder and the next stage's document named each time |
| A full account in one message named one limit; the document was written at once and the user's other limits (phones only, who may see a door code) never reached any document | example 2, twice | problem text: every account gets the last question unless the user has said that is everything; problem scenario `08-a-full-account-not-said-to-be-all` |
| Told "say the word and I'll start", the scripted user said "I don't know." for five turns: no topic covered being asked to go on | example 2, third run | every brief has a `proceed` topic unless it sets its own: one unit test |
| `tools.txt` held only the last session's tool calls | example 2, third run | the driver keeps every session of a run |
| Nothing kept a file of the user's own (a sheet, an export) out of the documents; kad had a real row carried into a plan, its tests and its history twice | looking over the tests; the owner chose that the file stays on their machine | `startup/source.sh` (describe: the shape, never a cell; scan: where a value is written, never what), 15 unit tests; a line in the report; a rule in the routing table; requirements scenarios 11 and 12; example 2 has a made-up price list and every run is scanned |
| A session that could not do the research offered to correct the requirements instead ("I can do that"), and the check read it as offering another way to do the stage | the pass of 2026-11-23 | the check in startup scenario 21 narrowed to an offer of the stage's own work; the kept runs graded again |
| A page's text dropped where its links lead, so a session could not find the next page | research pilot, first runs | `research/page.py` keeps each link's address: unit test |
| A run's shell could not make the folder for saved pages; sessions took the whole project for read-only and stopped | research pilot, first runs | the copy is kept in the machine's temporary folder and said to be in order: unit test; research scenarios start with the folder there |
| A run stepped out of the project (`cd "$TMPDIR"`) before fetching, so the real web answered in place of the scenario's | research pilot, Haiku | the stand-in wrapper looks in the folder the command came from: `steps/06-research/eval/test_wrapper.py` |
| A real page's table cells ran together; the quote check missed quotes across a link's words, quotes starting mid-sentence and quotes with words before their address | research pilot, the real run | `research/page.py`: four unit tests |
| Nine facts of 88 carried an address and no quote; one quote was stitched with "..." | research pilot, the real run | two lines in the research text; the gate's quote check |
| Asked "what's next" after a merge, a session named the coming-back and waited for the word | slice pilot | the three cases that expect the check-off say "Go on to the next stage."; the driver gives a session four turns after the merge: `test_a_session_that_never_marks_the_merged_slice_is_given_four_turns` |
| One run of five marked the row below the chosen slice: the end of one row of the set was the end of another, and the edit landed on the wrong one | slice, five runs | slice text (the whole row is replaced); the checks `form-marks-the-chosen-slice` and `form-marks-no-other-slice` already caught it |
| Told not to write a criterion to look thorough, sessions wrote slices with no refusal at all | slice, five runs, as read | slice text (the essential refusals stay, one for a rule); the four cases with criteria five times again |
| A list of one item with eight questions open under it was cut into one slice that did not wait for them; once it was merged the box was checked and the activity called done | example 2, through a merge | `stage.sh` does not call an activity done while a question of the list is open, and names the requirements as next: three unit tests; slice text (the part of an item that waits for an answer is a row of its own) |
| Asked whether singers can reach the hall's computer from home, the scripted user gave its limits four times running: no topic covered the question as asked | example 3, through a merge | the brief has a topic for it |
| A second run in one unit test could not clear the first run's folder on Windows; tests that recorded the planning folder before making the repository failed there | CI, first push of the slice branch | the tests take a folder a run and make the repository first |
| An example run a second time in the same place was told its planning folder "no longer exists", with no command to record one: the session wrote every document without its number and never read the documents again | examples 2 and 3, run again | `stage.sh` gives the command that records a folder then too: `test_a_remembered_folder_that_is_gone_is_said` |
| A client's real name, which the user had given as an example, was the example in the chosen slice's criteria; the plugin's own scan found it | example 2, through a merge | slice text (a criterion's values are never a name or figure the user gave or a file of theirs holds); slice case 04b's user gives a real name, with a check |
