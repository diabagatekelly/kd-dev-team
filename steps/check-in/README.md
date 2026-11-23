# The check-in after a merge: the test, set before anything is built or run

**State, 2026-11-23: parked** (decision 34). Nothing here is agreed,
built or run. The owner, on reading it: it is too early, and the
slice stage should say where a new issue belongs, not the owner.
It leans on a line the delivery stage writes, on a slice document
and on issues from a build, none of which exist. When it is taken
up, with or just after the slice stage, it is smaller than what
follows: the scripts say a check-in is due, check the boxes from
merged work and list the new issues; the slice stage's text places
each issue and records why, without asking; the owner is asked only
whether something no row covers is in or out, and which row is the
next "now". Conditions 6 and 7 below, and scenarios 5 to 10, change
with that. The comparison with kad stands.

The folder has no number: the check-in comes after the build, whose
stages are not numbered yet.

## What it is

The first thing a session does once work has been merged (decision
23). It answers three questions and writes down the answers:

1. **Is the work on the "now" activity done?** Every box of its
   requirements list checked.
2. **Is a new "now" due?** Only when it is done; which row comes
   next is the user's.
3. **Where does each new issue belong?** To the activity in hand, to
   the next, or between them.

**One reading to confirm.** Decision 23 says "slice". Here it is
taken as the whole list of the "now" activity: the thin cut of stage
5 may check only some of the boxes, so one list can take several
merges, and a check-in happens at each.

## What it needs from the stages around it

- **From the build, later:** a merged pull request names the items
  it completes, by the names on the list (one line of its
  description, `Completes: name, name`). Writing that line is the
  delivery stage's; until it exists the scenarios make it up.
- **From the scripts** (unit tests, no model): the tracker script
  reads merged pull requests and the names they give; the stage
  script says when a check-in is due, checks a box by its name,
  lists the open issues no check-in has placed yet, and names the
  document a changed map or list takes.
- **In the routing table:** one new row, after the open pull request
  and the critical issue, before the next stage by the documents.

## What the stage must do

1. **Happen when it is due, by the script, and not otherwise.** Due:
   a merged pull request names an item still unchecked, or an open
   issue has not been placed. Not due: nothing is said of it and
   nothing written.
2. **Check a box only for what merged work names,** with the command
   the report gives. Never on the user's say-so or its own
   judgment; a name the list does not hold is said, not guessed at.
3. **Say where the activity stands:** how many boxes are checked and
   which remain, by name.
4. **Call it done only when every box is checked and no open issue
   is placed in it.** (The second half is added to decision 23: an
   open fault against a checked item should not let the activity
   close.)
5. **Not ask whether the work is done.** The merge was the user's
   and is the answer.
6. **Place every new issue by the map's rows:** the activity in hand
   (the item it is about, or "no item covers it"), the next row, a
   later row, or between them when no row covers it. Each with its
   reason in the row's own words.
7. **Ask once, for all of it:** whether the placements are right
   and, for an issue no row covers, whether it is in or out. Scope
   is the user's; no row is invented before the answer.
8. **Ask for the new "now" only when the activity is done,**
   offering the row marked "next" and saying it is the user's call.
9. **Change the map only for what the merged work or a placed issue
   forces:** a row split, joined, added, dropped, moved, or a new
   "now". Otherwise say the map holds and write no map.
10. **Revise in place until something is built on a document; after
    that, a new numbered version, the earlier one left as it is.**
    A map is built on once a requirements list exists for it; a list
    once a slice is cut from it. The changed document ends with what
    changed and why, a line a change. Checking a box is not a
    revision: it is always done in the list itself.
11. **Add no item to the list itself.** An issue of this activity
    that no item covers is recorded as that, and the requirements
    stage is named as next, where the user confirms the item.
12. **Write the record:** one short numbered document a check-in
    (`NNN_check-in.md`): what was merged, the boxes checked, what
    remains, each issue and its place, whether the map held, and
    what comes next. The script reads it to know what is placed.
13. **Touch nothing on the tracker and start nothing:** no issue
    closed, labelled or begun; no requirements, no slice, no fix.

## Set beside what kad did at this point (decision 26)

kad had no skill for this. What happened after a merge was spread
over its orchestrator (2,100 lines), `scope-map`,
`requirements-refinement`, `vertical-slicing` and `delivery`:

| What kad did | Here |
|---|---|
| The tracker is read before any document: an open pull request first | Kept, already in startup (rows 8 and 9) |
| Each open Critical or High issue: one question, three answers (fix in the open slice's round, fix first on its own, accept as known; a Critical is never accepted) | Startup's question is kept (address it first?). **Added:** every new issue is placed, whatever its severity. kad routed only the top two; a Medium filed at delivery was read by no later stage. "Accept as known" is **not carried yet:** it is a risk the owner accepts, and belongs with the owner's list |
| Whether a slice is built: "no fixed convention for detecting this mechanically", so the user's word is taken | **Different on purpose:** by script, from what merged pull requests name on the checkable list (decision 23) |
| After a slice is built: stop, and never offer the next step of the map; the user must ask | **Different on purpose:** the session says where the list stands and, when it is done, asks which row is the next "now" (decision 22: the map is re-read with the user after each slice) |
| The next unit is the lowest-numbered step with no requirements | **Different on purpose:** the row the user marks "now" |
| Revise the map only when a slice proves a boundary wrong (one step is two, two are one, a step nobody named); never on a hunch | Kept (condition 9) |
| Revise a document in place while it is still its own; once a later stage has relied on it, write a new numbered version | Kept, as one rule for the map and the list (condition 10); "relied on" is found by script, not judged |
| Supersede only when the change alters what the later stage decided | **Simpler here:** any change of content after something is built on it is a new version. A session then never has to judge what a later stage decided |
| The old version is edited to say `Superseded by ...`; a `Status` line in every document | **Not carried:** the highest number is the current one, by script, and the earlier file is not touched (decision 21) |
| A project kept in git may revise everything in place | **Not carried:** decision 21 wants the folder to show when the picture changed |
| The finder of a problem reports; the owner of the invalidated document revises it (backward routing), one step at a time | Kept (condition 11): the check-in records, the requirements stage changes the list |
| A capability added mid-flight has no confirmed "what" behind it: the user's to decide | Kept (conditions 7 and 11) |
| An append-only log, an entry a route | The check-in record, one a check-in (condition 12) |
| Deferrals of a slice listed in the pull request, standing Mediums filed as issues, Lows not filed | The delivery stage's, **not built yet**; the check-in reads whatever is open |
| A slice file is always revised in place | **Put off** to the slice stage |

## Two measures, as for stages 1 to 3

**The gate: free checks.** Thirteen made-up scenarios, each a
project with its three documents, a tracker's answer and the
report:

| # | The situation | Must |
|---|---|---|
| 1 | a merge names two of four items; no issue | check those two; say which remain; map holds, none written; no new "now" asked |
| 2 | a merge names the last items | say it is done; ask which row is next, offering "next"; write no map before the answer |
| 3 | (second turn of 2) the user names the new "now" | a new version of the map, the earlier untouched, ending with what changed; no requirements |
| 4 | (second turn) the user corrects that new map before anything is built on it | the correction made in that version; no third version |
| 5 | an issue against an item of this activity, every box checked | placed here; not called done |
| 6 | an issue of this activity that no item covers | recorded as that; requirements named as next; no item written |
| 7 | an issue that belongs to the "next" row | placed there; not started; the list untouched |
| 8 | an issue no row covers | "between"; asks in or out; no row before the answer |
| 9 | an issue that shows two rows are one (from the scope-map stage's removed scenario) | after the user's yes, a new version of the map with the rows joined, and why |
| 10 | three issues, one of each kind | each placed, asked once |
| 11 | nothing merged since the last check-in, every issue placed | no check-in; the next stage named |
| 12 | a merge names an item the list does not hold | said; nothing checked for it |
| 13 | the user says "it's all done, tick everything"; the merge names two | only the two checked, and said why |

The checks: which boxes are checked in the list; whether a map or a
list was written, under which name, and the earlier one unchanged;
the record's lines; the tracker's tool never used to change
anything; the question asked, and none asked that is not the user's.

**Quality: read, with reasons** (decision 18). kad wrote nothing at
this point to read against, so the mark is the conditions
themselves, on these points, fixed now:

- every checked box traces to a merged pull request;
- each placement follows from the words of a row or an item;
- the user is asked only for placements, in or out, and the next
  "now";
- a changed map changes what was found and nothing else;
- the record can be taken in at a glance and invents nothing.

## Arms, models, bar

- **Arms:** the bare model first (the report with its new lines and
  commands, every adopted text, nothing for this stage); then a text
  of our own, as short as holds, tuned on the reading. kad's
  orchestrator is not an arm, for the reason it was not at startup.
- **Models:** Haiku, Sonnet and Opus 5.5. Three runs a scenario on
  each arm, then five on what passes, before it is put to the owner
  (decision 30).
- **Bar:** a model holds at 65 of 65 at the gate over five runs and
  when every record and changed map of those runs reads as the
  points say. The text is carried only if the bare model does not
  hold without it. The session's model is Sonnet 5.5; Haiku and Opus
  are run to know.

## Cost

| What | About |
|---|---|
| The scripts and their unit tests | free |
| Pilot: each scenario once on Haiku, both arms | $0.20 |
| Three runs: bare on three models, the text on Haiku and Sonnet | $14 |
| Two rounds of tuning on the reading | $6 |
| Five runs of what passes, on Sonnet | $6 |
| Every earlier stage once, since the routing table changes | $4 |
| One end-to-end example carried through a check-in, twice | $4 |
| **In all** | **about $35, two hours of runs** |

A ceiling of $40 is proposed, the pilot's real cost reported first.
Whether the ceiling is dropped for this stage, as for stage 3, is
the owner's (decision 27).

## What it changes outside itself

The routing table gains a row, so every stage's scenarios run once
(in the cost above). The requirements text gains the way back from
condition 11, with one scenario, run five times. The stage script
takes the highest-numbered list and map as the current ones.

## What a pass will not show

No build exists yet, so the merged pull requests are made up, and
whether the line a real delivery writes is the right contract is
seen only when that stage is built. A project with no tracker read
has no check-in at all until another way to learn of a merge is
chosen.
