# Slices: Invoice clients for the month

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Enter a walk as a walker | walker-walk-entry | nothing | chosen |
| 2 | Correct a walker's entry | owner-walk-correction | 1 | open |
| 3 | Make a client's invoice from a month's walks | monthly-client-invoice | 1 | open |
| 4 | Get a Tallypay payment link for an invoice | invoice-payment-link | 3 | open |
| 5 | Get invoices and their payment links to clients | monthly-client-invoice, invoice-payment-link | 3, 4 | open |
| 6 | Start a month from the usual weekly walks | month-from-usual-walks | 1 | open |

## Where to start
- Recommended first: slice 1. It shows a walker's walk recorded from their phone, it needs no other slice, and every other slice builds on it, directly or through another.
- Slice 1 can be started now. Slices 2 and 3 can be started once 1 is built, and slice 4 once 3 is. Their ordinary path does not depend on an unanswered question; the answers may still add to them or to the requirements.
- Slice 3 covers only walks at the list price for their length, as one invoice for one client. Anything else on an invoice, changing prices in the product and other invoicing arrangements wait on questions 2 and 6.
- Slice 5 cannot be started: whether the business owner must check or change invoices before clients get them is not decided (question 4). Questions 5, 7 and 8 also bear on it.
- Slice 6 cannot be started: where the usual weekly walks come from, who changes them and who starts a month from them are unanswered (question 1).
