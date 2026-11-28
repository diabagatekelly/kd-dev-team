# Slices: invoice clients for the month

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Give a client the month's invoice at list prices | monthly-client-invoice | nothing | chosen |
| 2 | Send a client the payment link for an invoice | invoice-payment-link | 1 | open |
| 3 | See which clients have not paid | see-who-unpaid | 2 | open |
| 4 | Add something missing from the price list, then charge it | price-list-addition | 1 | open |
| 5 | Invoice walks from before and after a price change | monthly-client-invoice | 1 | open |

## Where to start
Slice 1 is chosen and started at the owner's word. Its criteria are written, but its build waits on questions 1, 4 and 5. No other slice can be started yet. The numbers below are those of the questions under "Not yet confirmed" in the requirements.

- Slice 1 waits on question 1 (what a client's name on a price list row means, which could change what is charged), question 4 (checking before clients get invoices) and question 5 (one, several or shared invoices).
- Slice 2 waits for slice 1.
- Slice 3 waits for slice 2.
- Slice 4 waits for slice 1 and on questions 1 and 2.
- Slice 5 waits for slice 1 and on question 2 (whether prices change, and which price is then charged).

Questions 3 (putting a wrong invoice right) and 6 (what must come across) hold back no slice as listed, but their answers could add items.

Recommended first, and chosen: slice 1. It shows the owner a month's invoice made from walks and list prices, and every other slice builds on it, directly or through another.

## What changed
- Slice 1 was started before questions 1, 4 and 5 were answered, and what waits is marked in its document. The owner's words: "Start it now, and mark what waits on my decision."
