# States

Nothing outside the product is committed to for this slice, so no page was read. Every row comes from the planning documents alone; where they say nothing the row says so.

## Singer

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `in-register` | a section leader adding them under a voice part | a section leader can record an absence for them | not said in the documents | 002_requirements.md, Out for now: "section leaders add singers by voice part" |
| `not-in-register` | never added | a section leader who records an absence for that name is shown there is no such singer | by being added -> `in-register` | 004_slice.md, criterion 2: "no singer called Gwen Pryce in the register" |

## Rehearsal

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `coming` | a Thursday date not yet reached | a section leader can record an absence for it | by itself -> `passed` | 004_slice.md, criterion 1: "a rehearsal on 2026-12-03 that has not happened yet" |
| `passed` | its date going by | a section leader who records an absence for it is shown the date has passed | none needed: it is over | 004_slice.md, criterion 3: "a rehearsal date that has already passed" |
| `after-tuesday-evening` | the Tuesday evening before the Thursday going by | not said in the documents: whether a word that comes now is refused or taken | not said in the documents | 002_requirements.md, Not yet confirmed 1: "singers are to tell us by Tuesday evening for the Thursday" |

## A singer's absence for a rehearsal

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `away` | a section leader recording the absence | the section leader is shown the singer is down as away | not said in the documents: whether it can be taken back or changed | 004_slice.md, criterion 1: "down as away for 2026-12-03"; 002_requirements.md, Not yet confirmed 3 |
| `not-recorded` | the name is not in the register, or the date has passed | nothing is down for that name and date | by a section leader recording it with a name and date that are accepted -> `away` | 004_slice.md, criteria 2 and 3: "no absence is down" |

## For the owner's list
- `away`: no way out is said in the documents. A singer who is down as away for a rehearsal stays so if plans change, until the owner says whether it can be taken back.
- `after-tuesday-evening`: no way out is said in the documents. It is not said whether a word that comes now is refused or taken.
