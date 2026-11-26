# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | The documents do not say how the list keeper uses it (slice-001/004_slice.md, Thin path) |
| network | yes | The documents do not say whether it answers requests at a network address (slice-001/004_slice.md, Thin path) |
| calls-out | no | "Outside systems: none." (002_requirements.md); the slice's "Needs from outside" is "none" |
| dependency | yes | The documents do not say what it is made from (slice-001/004_slice.md) |
| several-people | yes | "The committee can see the waiting list." and "A person on the waiting list can see where they stand on it" (002_requirements.md) |
| unguessable | yes | The documents do not say whether it makes any such value (slice-001/004_slice.md) |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `waiting-details` | `list-view` | Someone not entitled to the list reads the names and places of the people waiting. | yes |
| `waiting-details` | `carry-across` | Someone who can watch the list being carried across learns who is waiting and in what order. | yes |
| `waiting-details` | `stored-list` | Someone who reaches the kept list or a copy of it takes everyone's names and places. | yes |
| `waiting-list` | `carry-across` | Someone moves a friend higher or leaves a person out as the list is carried across, so that person loses their turn for a plot. | yes |
| `waiting-list` | `carry-across` | Someone sends a different list, or an old one again, and it replaces the true order for everyone waiting. | yes |
| `waiting-list` | `list-view` | Someone makes the list keeper be shown an order other than the one kept, so a wrong order is taken to be right. | yes |
