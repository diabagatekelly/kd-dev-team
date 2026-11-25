# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | carry-over-list / 1 has a person carry over and be shown the list; the documents do not say it is without a web browser |
| network | yes | carry-over-list / 1; the documents do not say that the product answers no requests at a network address |
| calls-out | no | slice-001/004_slice.md, line 12: under "Needs from outside", "none" |
| dependency | yes | carry-over-list / 1; the documents do not say that no component written by someone else is added |
| several-people | yes | 000_problem.md, line 13: "The committee are five volunteers"; 002_requirements.md, line 20, leaves open who else may see places or the list |
| unguessable | yes | 002_requirements.md, line 9, keeps names from being shown to everyone; the documents do not say that no code, link or session is made |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `waiting-person-details` | `shown-list` | Someone who should not see the list reads the names of the people waiting and where each one stands. | yes |
| `waiting-person-details` | `carry-over` | Someone other than the person carrying the notebook over gets the names and their order while they are being carried over. | yes |
| `waiting-list` | `carry-over` | Someone who should not be able to carry over adds, replaces or reorders people, so that someone moves ahead of those who have waited longer. | yes |
| `waiting-list` | `carry-over` | A person allowed to carry over puts a friend higher than the notebook does, nobody can tell, and those waiting lose their turn. | yes |
| `waiting-list` | `shown-list` | The person checking is shown an order that differs from the one kept, accepts it as matching the notebook, and a wrong order stands. | yes |
