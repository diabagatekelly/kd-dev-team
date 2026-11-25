# States

## Invoice

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `being-made` | the owner asking for a client's invoice for a month | not said in the documents | not said in the documents | not said in the documents |
| `not-made` | asking when a needed price is missing, or when the client has no walks that month; the same again each time while that is so | see that the price is missing, or that there are no walks to invoice; no invoice is shown | not said in the documents | slice-001/004_slice.md lines 13 and 14 |
| `shown` | the owner asking for a client's invoice for a month | see the month's walks, each priced by its length, and the total | not said in the documents | slice-001/004_slice.md line 4 |
| `out-of-date` | not said in the documents (walks or prices changing after the invoice was shown) | not said in the documents | not said in the documents | not said in the documents |
| `awaiting-approval` | not said in the documents | not said in the documents | not said in the documents | not said in the documents; open as question 4, 002_requirements.md line 18 |
| `with-client` | the client getting the invoice with a payment link (slice 4) | not said in the documents | not said in the documents | 002_requirements.md line 3 |
| `wrong` | an invoice turning out to be wrong, before or after the client has it | not said in the documents | not said in the documents | 000_problem.md line 7; 002_requirements.md line 19 |
| `unpaid` | not said in the documents | seeing who has not paid, and chasing late payers, are a later activity | not said in the documents | 001_scope-map.md line 7 |
| `paid` | not said in the documents | not said in the documents | not said in the documents | not said in the documents |
| `ended` | not said in the documents (cancelled, replaced or no longer needed, and what is kept) | not said in the documents | not said in the documents | not said in the documents |

## For the owner's list
No way out is said for any of these states. This does not mean there can be none.

- `being-made`: no way out. The documents do not say what the owner has while waiting.
- `not-made`: no way out. The owner has the reason and no invoice.
- `shown`: no way out. The owner has the walks, prices and total; the documents do not say whether they are kept.
- `out-of-date`: no way out. The documents do not say what the owner is left with.
- `awaiting-approval`: no way out. The documents do not say that this state exists.
- `with-client`: no way out. The client has the invoice and payment link.
- `wrong`: no way out. The owner has said "I don't know" to what is needed.
- `unpaid`: no way out. Following it up is a later activity.
- `paid`: no way out. The documents do not say what is left.
- `ended`: no way out. The documents do not say what is left.
