# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | Not said in the documents; slice-001/004_slice.md line 4 says only that the owner asks and is shown an invoice. |
| network | yes | Not said in the documents; slice-001/004_slice.md line 4 does not say where the owner asks from. |
| calls-out | no | slice-001/004_slice.md, "Needs from outside": "none". |
| dependency | yes | Not said in the documents; slice-001/004_slice.md names no components. |
| several-people | yes | Not settled: 002_requirements.md line 18 leaves open who does invoicing and whether walkers see invoices. |
| unguessable | yes | Not said in the documents; 002_requirements.md line 18 leaves access open, so a session or code is not ruled out. |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `client-details` | `invoice-request` | Someone who is not allowed asks for client after client and learns who uses the business, when their dogs were walked and what they were charged. | yes |
| `client-details` | `invoice-view` | Someone who gets at a shown or leftover invoice learns when a client's home is likely to have had a walker call. | yes |
| `client-details` | `stored-walks` | Someone who reads the stored walks learns the visiting pattern of many households and could pick times to target a home. | yes |
| `client-details` | `stored-prices` | Someone who reads the stored prices learns what particular clients are charged. | yes |
| `client-details` | `refusal-message` | Someone who is not allowed learns from a missing-price message that a client had a walk of a certain length that month. | yes |
| `client-details` | `no-walks-message` | Someone who is not allowed learns that a client had no walks in a month, which may suggest when that household changed its routine. | yes |
| `invoice` | `stored-walks` | Someone adds, removes or alters walks, so a client is overcharged or the business loses money without noticing. | yes |
| `invoice` | `stored-prices` | Someone alters a price, so clients are shown wrong totals and the owner relies on them. | yes |
| `invoice` | `invoice-request` | Someone sends a request carrying their own walks, prices or total, so the owner is left with a false invoice. | yes |
| `invoice` | `invoice-view` | Someone changes what is shown on its way to the owner, so the owner bills the wrong amount by hand. | yes |
| `nothing` | `refusal-message` | Changing the message was considered: on its own it makes no invoice and moves no money. | no: it only reports a missing price; what it reveals has its own row. |
| `nothing` | `no-walks-message` | Changing the message was considered: on its own it makes no invoice and moves no money. | no: it only reports that there are no walks; what it reveals has its own row, and altered walks are covered under stored walks. |
