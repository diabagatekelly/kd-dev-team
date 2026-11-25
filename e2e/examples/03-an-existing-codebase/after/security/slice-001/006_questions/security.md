# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | slice-001/004_slice.md, line 4, does not say how a section leader records an absence; 002_requirements.md, line 16, says the program today is run by typed commands, which does not settle it for this slice |
| network | yes | 000_problem.md, line 21, leaves open whether singers can reach the hall's computer from home; no document says this slice answers no requests at a network address |
| calls-out | no | slice-001/004_slice.md, line 13: what the slice needs from outside is "none" |
| dependency | yes | No line of the documents says the slice adds no component someone else wrote (slice-001/004_slice.md) |
| several-people | yes | 000_problem.md, line 17: section leaders use the computer; record-phoned-absence / 1: one records for a singer |
| unguessable | no | record-phoned-absence / 1 and / 2 make only a recorded absence and what the section leader is shown; 002_requirements.md, line 16: the program "has no accounts" |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `singer-s-absence-from-a-rehearsal-told-in-advance` | `phone-call` | Someone phones as a singer who means to come, and that singer is recorded as absent, so the programme may be changed for no reason. | yes |
| `singer-details` | `phone-call` | A caller learns from a section leader whether a named singer will be away. | yes |
| `singer-s-absence-from-a-rehearsal-told-in-advance` | `record-action` | Someone other than a section leader records false absences, and a voice part appears short when it is not. | yes |
| `singer-details` | `record-action` | Someone tries names to learn who is in the choir. | yes |
| `singer-details` | `confirmation` | Someone who sees the screen or what it leaves behind learns that a named singer will be away on a given evening. | yes |
| `singer-details` | `refusal` | From which names are refused and which are not, an outsider learns who sings in the choir. | yes |
| `singer-details` | `saved-register` | Someone who reaches the saved register or a copy of it learns who the singers are and when they will be away. | yes |
| `register` | `record-action` | What someone gives as a name or date damages the register, and the section leaders lose its singers and attendance. | yes |
