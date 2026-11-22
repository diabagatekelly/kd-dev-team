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
