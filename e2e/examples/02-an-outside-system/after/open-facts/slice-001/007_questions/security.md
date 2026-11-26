# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | monthly-client-invoice / 1: the owner gets and is shown an invoice; no document says in what, so it counts as yes |
| network | yes | monthly-client-invoice / 1: no document says where the product runs or is reached from, so it counts as yes |
| calls-out | no | 005_approach.md, "Committed to": "Nothing." |
| dependency | yes | monthly-client-invoice / 1: no document says what the product is made from, so it counts as yes |
| several-people | no | 002_requirements.md, "Out for now": only the owner does the invoicing |
| unguessable | yes | monthly-client-invoice / 1: no document says how the owner is known to the product, so a session or other such value counts as yes |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `client-details` | `invoice-view` | A stranger reads when a client's dog was walked, and uses it to work out when the client is likely to be away from home. | yes |
| `client-details` | `invoice-request` | A stranger asks for one client's invoice after another and collects who the clients are and when their dogs are walked. | yes |
| `client-details` | `walks-intake` | Someone who can reach the way walks come in reads the walks and clients already taken in. | yes |
| `client-details` | `price-list-intake` | The client entries in the owner's price list are taken in with the prices, and someone else reads them. | yes |
| invoice | `walks-intake` | Someone adds, changes or removes walks, so a client is charged for walks they did not have or is not charged for ones they did. | yes |
| price-list-entry | `price-list-intake` | Someone puts in an altered price list, and clients are charged wrong amounts. | yes |
| walk | `invoice-request` | Someone uses the request for an invoice to change or remove the walks it is made from. | yes |
| invoice | `invoice-view` | Someone alters what the owner is shown, and the owner takes a wrong charge to be right. | yes |
| `nothing` | `invoice-month` | The month asked for is an ordinary calendar month, and knowing it gives nothing away. | no: it is no secret and reveals nothing about a client by itself |
