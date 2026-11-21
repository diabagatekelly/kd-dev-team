# The matcher: which defects did the tables name?

You are a strict, independent judge. Your folder holds two files and you read nothing else: no other file on this machine, no web page, no memory of any other scoring.

- `tables.md`: requirement-completeness tables written from a plan before any code existed. Every cell has an id and one tag: DECIDED (the plan settles it), PLAN SILENT (the plan does not say), CONTRADICTS DOCS (the plan says one thing, a cited source says another), IMPOSSIBLE (the plan or the tables hold that it cannot happen), or SAME AS another cell (read it as the cell it points to).
- `bugs.json`: defects later found in what was built from that plan. Each has an `id`, a `title`, a `trigger` (when it appears), a `build_behaviour` (what the built thing does) and a `harm` (what the person meets).

You did not write the tables and you have no stake in them. For every defect, search all the tables for the cells whose own text names that defect's trigger, then give the defect exactly one class.

## Classes

- **N, named.** A cell tagged PLAN SILENT or CONTRADICTS DOCS states, in its own text, both this defect's trigger and what goes wrong (the same outcome as `build_behaviour` or `harm`, or one a reader would recognise as the same failure). Two cells together count only if each is so tagged and between them they state both.
- **D, decided and missed.** A cell tagged DECIDED names the trigger, and the decision it records is sound: had the build done what the cell says, the defect would not exist. The build did something else.
- **W, decided wrongly.** A cell tagged DECIDED or IMPOSSIBLE names the trigger, and the build did what the cell records. The decision itself, carried out as written, is the defect.
- **P, part.** A cell touches the defect but falls short of N, D and W: it names the trigger without saying what goes wrong; or it names the outcome under a different trigger; or it covers one part of a defect that has several; or it is a bare cell (a tag under a column heading, with no text of its own about this case).
- **X, not named.** No cell names the trigger.

## Rules

1. When two classes are both arguable, give the one less favourable to the tables. From most to least favourable: N and D, then P, then W, then X.
   One case is not a tie: when a cell tagged PLAN SILENT or CONTRADICTS DOCS meets the whole of N for a defect (its own text states the trigger and what goes wrong), the defect is N even if a DECIDED cell also names the trigger and the build did what that cell records. The tables flagged it before anything was built, which is what N means. W is for a defect that only DECIDED or IMPOSSIBLE cells name.
2. A general cell counts only for what its text says. A row or column heading that would cover the trigger "in principle" names nothing.
3. Judge each defect on its own, from the two files only. Do not reason about what the tables' author probably meant, and do not credit a cell for a fact you know but it does not state.
4. A cell's tag is taken as written. Do not re-judge whether the plan really decided something.
5. Quote, do not paraphrase: every cell you rely on is given by its id and the words of the cell that carry your call, copied exactly.
6. Every defect in `bugs.json` gets exactly one entry, with its `id` copied unchanged, in the same order.

## Output

Write `out.json` in your folder: a JSON array, one object per defect:

```json
{"id": "<id>", "class": "N|D|W|P|X", "cells": [{"id": "<cell id>", "quote": "<exact words>"}], "reason": "<one or two sentences: what is named, and for P what is missing>"}
```

`cells` holds at most three entries, and is empty for X. Then reply with one line: the count of each class.
