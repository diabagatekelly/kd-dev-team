# Slice 1: A section leader records that a singer who phoned will miss a rehearsal

## Thin path
A section leader, at the hall's computer, records that a singer who phoned them will miss a given rehearsal, and is shown that the singer is down as away for that rehearsal.

## Criteria
- **record-phoned-absence / 1**: Given a singer called Fern Walsh in the register and a rehearsal on 2026-12-03 that has not happened yet, when a section leader records an absence for Fern Walsh for 2026-12-03, then they are shown that Fern Walsh is down as away for 2026-12-03.
- **record-phoned-absence / 2**: Given no singer called Gwen Pryce in the register, when a section leader records an absence for Gwen Pryce for 2026-12-03, then they are shown that there is no such singer, and no absence is down for that name.
- **record-phoned-absence / 3**: Given a singer called Fern Walsh in the register and a rehearsal date that has already passed, when a section leader records an absence for Fern Walsh for that date, then they are shown that the date has passed, and no absence is down for it.

## Needs from outside
none

## Left for later
- Singers telling us themselves, with no password: slice 2. Usable without it: section leaders record an absence for a singer who phones them.
- Seeing who will be away, by voice part, before the night: scope map row 2, not yet in the set of slices. Usable without it: the section leader is shown each absence as it is recorded.
- Who else may tell us for a singer, how far ahead and until when, several rehearsals at once, taking an absence back, late or early, and a reason: each waits on a question under "Not yet confirmed" in the requirements, and no slice takes them yet. Usable without them: a section leader records one absence for one singer for one rehearsal.

## Size
Criteria: 3.
