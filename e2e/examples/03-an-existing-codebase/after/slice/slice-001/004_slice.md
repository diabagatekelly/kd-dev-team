# Slice 1: A section leader records that a singer who phoned will miss a rehearsal

## Thin path
A section leader at the hall's computer picks a singer and a Thursday rehearsal and records that the singer will miss it, and is shown that the absence is down for that singer on that date.

## Criteria
- **record-for-singer / 1**: Given a section leader at the hall's computer, who is not asked for a password, and a singer "Mira Quinn" in the register as a tenor with no absence recorded for Thursday 3 December, when the leader records that Mira Quinn will miss that rehearsal, then the leader is shown that Mira Quinn is down as absent for 3 December.
- **record-for-singer / 2**: Given an absence recorded for Mira Quinn on Thursday 3 December, when a section leader later looks at the absences for that date, then Mira Quinn is listed among them.
- **record-for-singer / 3**: Given no singer called "Oriel Banks" is in the register, when a section leader tries to record an absence for Oriel Banks on Thursday 3 December, then the leader is shown that there is no such singer, and no absence is recorded.

## Needs from outside
none

## Left for later
- A singer telling us themselves: slice 2. Blocker: it waits on whether singers can reach the hall's computer from home.
- Stopping a recording made after the Tuesday evening cut-off: slice 3. Blocker: it waits on whether the cut-off also applies when a section leader records the absence.

## Size
Criteria: 3.
