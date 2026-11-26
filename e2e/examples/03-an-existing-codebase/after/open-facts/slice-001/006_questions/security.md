# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | slice-001/004_slice.md line 4 has people recording and looking, and no document says whether a web browser is used |
| network | yes | 002_requirements.md line 17 puts the register on the hall computer, and no document says whether it answers at a network address |
| calls-out | no | 002_requirements.md line 32: "Outside systems: none." |
| dependency | yes | no document says whether a component someone else wrote is added; slice-001/004_slice.md line 16 speaks only of what the path needs from outside |
| several-people | yes | 000_problem.md line 17: the section leaders use the computer the register is on |
| unguessable | yes | 002_requirements.md line 16 says the register as it stands has no accounts; no document says the slice makes no value that has to be impossible to guess |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `singer-details` | `absence-view` | someone who should not see it reads which named singers will be away on which date, some of whom may be in their eighties | yes |
| `singer-details` | `saved-register` | someone who gets the saved register, or any copy of it, learns the singers' names and when each said they would be away | yes |
| `singer-details` | `record-request` | the next person at the computer sees who was just being recorded as away | no: it shows no more than the view does, which is asked about in its own row |
| `singer-details` | `refusal-message` | someone tries names to learn who is in the choir | no: the message tells only whether a name is in the register, which the register's report by voice part already lists (002_requirements.md line 12) |
| A singer's word that they will miss a rehearsal | `record-request` | someone records absences that no singer sent, so the programme is changed or a piece dropped for a part that would have been there, and singers are shown as missing who are coming | yes |
| A singer's word that they will miss a rehearsal | `saved-register` | someone changes or removes what is saved, so the programme is planned on wrong numbers and nobody can tell that it was altered | yes |
| nothing | `refusal-message` | what the message could be used to change or send again was considered | no: it records nothing and says only that there is no such singer or that the rehearsal has passed |
