---
name: scope-map
description: Draw or re-read the scope map, the product manager's picture of the whole product. Use when the startup report names "scope map" as the next stage, when the user corrects the map, or when a slice is done and the map is to be re-read.
---

# The scope map

The whole product at a glance, from the problem document: the few
things a user does, in the order they do them. It is the picture to
come back to after each slice, and it is expected to change.

```markdown
# Scope map: <short name>

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | <activity> | <one line> | now |
| 2 | <activity> | <one line> | next |
| 3 | <activity> | <one line> | later |

## Holds for every activity
Each limit of the whole problem, from the problem document.

## Open
Each open question of the problem document, still open.
```

**Drawing it.** Read the problem document and nothing else. A row is
something a user does and would name themselves, never a part of
what gets built. A problem that is one activity gets one row, and you
say so. Exactly one row is "now": by the document, the one that
hurts most or that the rest lean on. No technology, design, estimate,
date or acceptance criterion, including one the user floats in
passing.

**Limits and open questions.** A limit on the whole problem goes
under "Holds for every activity", never in a row. An open question
stays under "Open": do not settle it by adding a row or leaving one
out.

**Then ask once.** Show the rows and ask whether anything is missing,
unwanted or in the wrong order: what is in, what is out and what
comes first are the user's. Apply their correction to the document.

**Re-reading after a slice.** Set what the slice found against the
rows. Where it contradicts them, change the rows (split, join, add,
drop, move), and say what changed and why. Where nothing contradicts
them, say the map holds and change nothing.

**Stop there.** Save it as the document the startup report names for
this stage. No requirements and no slice.
