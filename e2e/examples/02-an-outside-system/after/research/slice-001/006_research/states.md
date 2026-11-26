# States

Walked from the planning documents alone: nothing is committed to, so no outside system's pages were read. In sources, "requirements" is 002_requirements.md, "problem" is 000_problem.md and "slice" is slice-001/004_slice.md.

## Client

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `becoming-client` | not said in the documents | not said in the documents | none | not said in the documents |
| `regular` | not said in the documents | the owner invoices the client for the month | none | problem, line 4; requirements, line 3 |
| `details-changed` | not said in the documents | not said in the documents | none | not said in the documents |
| `no-longer-client` | not said in the documents | not said in the documents | none | not said in the documents |

## Walk

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `on-sheet` | a walker writes the walk on a paper sheet | the walker keeps the sheet until the end of the month | the walker hands the sheet in -> `handed-in` | requirements, line 9 |
| `handed-in` | the sheet is handed in at the end of the month | the owner gets an invoice made from the walk | the owner gets the month's invoice -> `on-invoice`, or `no-list-price` where its length has no price | requirements, lines 3 and 9; slice, lines 9 and 10 |
| `on-invoice` | the owner gets the client's invoice for the walk's month | the owner sees it charged at the list price for its length | none | slice, line 9 |
| `no-list-price` | the walk's length has no price on the list | the owner is shown that the length has no list price; no price is charged | the owner adds the price (slice 4), then charges the walk -> `on-invoice` | slice, lines 10 and 22; requirements, line 5 |
| `sheet-lost` | a walker's sheet is lost | today the owner has to guess | none | problem, line 10 |
| `wrong-or-corrected` | not said in the documents | not said in the documents | none | not said in the documents |

## Price list entry

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `missing` | something to be charged is not on the list | the owner adds it before it is charged | the owner adds it -> `listed` | requirements, line 5 |
| `listed` | it is on the list; how the entries there now got there is not said in the documents | walks are charged at the list price for their length | none | requirements, line 3 |
| `price-changed` | not said in the documents; whether a price ever changes waits on question 2 | not said in the documents | none | requirements, line 19 |
| `removed-or-corrected` | not said in the documents | not said in the documents | none | not said in the documents |

What a row of the owner's price list means for the client named on it is not known (requirements, line 18). No state is drawn from that column.

## Invoice

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `being-made` | not said in the documents | not said in the documents | none | not said in the documents |
| `got` | the owner gets a client's invoice for a month | the owner sees the month's walks and their charges | the owner sends the payment link for it (slice 2) -> `link-sent` | slice, lines 9 and 20; requirements, line 4 |
| `has-unpriced-walk` | a walk on it has a length with no list price | the owner is shown that the length has no list price | none | slice, line 10 |
| `awaiting-check` | not said in the documents; whether there is a check waits on question 4 | not said in the documents | none | requirements, line 21 |
| `link-sent` | the owner sends the client the payment link through Tallypay | the owner can see that the client has not paid (slice 3) | none | requirements, lines 4 and 6 |
| `paid` | not said in the documents | not said in the documents | none | not said in the documents |
| `wrong` | an invoice is got wrong, as two or three are each month today | what can be put right waits on question 3 | none | problem, line 8; requirements, line 20 |
| `cancelled-or-replaced` | not said in the documents | not said in the documents | none | requirements, line 20 |

## For the owner's list
- `becoming-client` (client): no way out. How someone becomes a client is not said.
- `regular` (client): no way out. The documents do not say how someone stops being a client.
- `details-changed` (client): no way out. What happens when a client's details change is not said.
- `no-longer-client` (client): no way out. What is left of a former client is not said.
- `on-invoice` (walk): no way out. The documents do not say what can be done about a walk once it is on an invoice.
- `sheet-lost` (walk): no way out. The owner is left to guess the walks, as today.
- `wrong-or-corrected` (walk): no way out. What happens to a walk written down wrong is not said.
- `listed` (price list entry): no way out. The documents do not say how an entry is changed or taken off.
- `price-changed` (price list entry): no way out. It is not known which price a walk is then charged.
- `removed-or-corrected` (price list entry): no way out. What happens to walks charged from such an entry is not said.
- `being-made` (invoice): no way out. What an invoice is before the owner has it is not said.
- `has-unpriced-walk` (invoice): no way out. It is not said whether the invoice can be used, or is completed after the price is added.
- `awaiting-check` (invoice): no way out. It is not known whether an invoice waits for anyone.
- `link-sent` (invoice): no way out. How the invoice moves on from here is not said.
- `paid` (invoice): no way out. How an invoice comes to be paid, and what follows, is not said.
- `wrong` (invoice): no way out. It is not known what the owner can put right.
- `cancelled-or-replaced` (invoice): no way out. Whether an invoice can be ended or replaced is not said.
