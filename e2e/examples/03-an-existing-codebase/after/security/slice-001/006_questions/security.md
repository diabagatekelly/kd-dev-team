# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | 004_slice.md line 4 says who records and who sees, and no document says by what means |
| network | yes | 000_problem.md line 17 leaves open whether singers can reach the hall's computer from home, and no document says the slice answers at no address |
| calls-out | no | 004_slice.md line 16: needs from outside, none |
| dependency | yes | no document says whether a component someone else wrote is added |
| several-people | yes | 000_problem.md line 14: the section leaders use the computer |
| unguessable | yes | no document says that no such value is made |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `singer-details` | `missing-view` | Someone not meant to see the list learns which named singers will be away on a given evening. | yes |
| `singer-details` | `saved-register` | Someone who gets at the computer or a copy of what it keeps reads singers' names together with when they were to be away. | yes |
| `singer-details` | `record-request` | Someone able to watch the request on its way reads which singer will be away and when. | yes |
| `singer-details` | `refusal-message` | Someone tries names to find out who is in the register. | no: the message tells only whether a name is there, and the register already shows its singers' names to whoever uses it (002_requirements.md line 11); who may use it is asked under authorization-01 and authorization-04 |
| `absence` | `record-request` | Someone records, or makes a section leader's computer send, a false or repeated absence, and the programme is changed for a singer who is coming. | yes |
| `absence` | `saved-register` | Someone changes or removes saved absences, and whoever arranges the programme plans for the wrong singers. | yes |
| `absence` | `missing-view` | Someone uses the list to change who is expected. | no: no criterion lets anything be changed from the list |
| `saved-register` | `record-request` | Someone sends a request made to change or destroy singers or attendance, and the choir's register is lost or wrong. | yes |
