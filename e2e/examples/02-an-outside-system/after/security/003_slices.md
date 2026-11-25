# Slices: invoice the clients

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | See a client's invoice for the month's regular and one-off walks, priced by length | monthly-client-invoice | nothing | chosen |
| 2 | Charge a second dog from the same home at half price | monthly-client-invoice | 1 | open |
| 3 | Charge a cancelled walk only when notice was late | monthly-client-invoice | 1 | open |
| 4 | Get a client their invoice with a Tallypay payment link | monthly-client-invoice | 1 | open |

## Where to start
Slice 1 is chosen. Its build waits for answers, and no other slice can be started yet. The numbers below are those of the questions under "Not yet confirmed" in the requirements.

- Slice 1 waits for: how walks get in (1), client prices and the kinds of walk (2), other charges and what extras are (3), changing prices (6), what "Since" means (7), invoices per client (8) and what must come across (9). Its late-cancellation part of question 1 belongs to slice 3.
- Slice 2 waits for slice 1, and for client prices (2).
- Slice 3 waits for slice 1, and for how late cancellations are known (1).
- Slice 4 waits for slice 1, and for approval and who may see invoices (4) and wrong invoices (5).

Chosen first, as recommended: slice 1. It shows the owner a priced invoice, which they now type by hand, and the other slices build on it.
