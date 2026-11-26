# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | Not said in the documents: walker-walk-entry / 1 says only that the walker is on their phone. |
| network | yes | Not said in the documents: walker-walk-entry / 1 has a walker enter from a phone, and no line rules out a network address. |
| calls-out | no | slice-001/004_slice.md line 11: what the slice needs from outside is "none". |
| dependency | yes | Not said in the documents. |
| several-people | yes | 000_problem.md line 4: "four walkers". |
| unguessable | yes | Not said in the documents how a walker is told apart (walker-walk-entry / 1: "their walks"). |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `client-details` | `walks-list` | Someone who is not that client's walker reads which clients are walked and on which days, and learns about those clients' routines. | yes |
| `client-details` | `entry-screen` | A walker, or someone holding a walker's phone, sees clients that the walker does not walk for. | yes |
| `client-details` | `save-request` | Someone who reads or alters an entry on its way learns which client is walked, and on which day. | yes |
| `client-details` | `installation` | Someone who reaches where the product keeps its data, its copies or its records reads details of every client. | yes |
| `walk` | `save-request` | Someone adds walks that never happened, or repeats a real one, and a client is later billed for them. | yes |
| `walk` | `walker-access` | Someone enters walks as another walker, and the record blames that walker for walks they did not enter. | yes |
| `client-details` | `walker-access` | Someone who gets a walker's access, or a former walker who keeps it, reads that walker's clients. | yes |
| `walk` | `entry-screen` | Someone holding a walker's unlocked phone enters false walks that are later billed to clients. | yes |
| `walk` | `installation` | Someone who reaches the running product or its data changes or destroys walks, so clients are billed wrongly or the month's record is lost. | yes |
| nothing | `client-needed-message` | It says only that a client is needed; whatever else the walker sees on that screen is covered by the entry screen's row. | no: the message in walker-walk-entry / 2 names no client and carries nothing a person gave. |
