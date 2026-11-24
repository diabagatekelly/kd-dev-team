# Slices: Invoice each client for the month

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Get one client's invoice for the month from their regular weekly walks, each walk charged by its length | monthly-invoices, regular-walks, walk-pricing | nothing | chosen |
| 2 | Charge a second dog from the same home at half price | walk-pricing | 1 | open |
| 3 | Add a one-off extra walk to a client's month | one-off-extras | 1 | open |
| 4 | Change or stop a client's regular walks | regular-walks | 1 | open |
| 5 | Send a client their invoice with a Tallypay payment link | send-payment-links | 1 | open |
| 6 | Get every client's invoice for the month in one go | monthly-invoices | 1 | open |
| 7 | Send every client's payment link on a set day | send-payment-links | 5, 6 | open |
| 8 | Charge walks for clients the price list does not cover, and across a price change | walk-pricing | 1 | open |

## Where to start
- **Can be started now:** slice 1. It builds on nothing.
- **Can be started once slice 1 is built:** slices 2, 3, 4, 5 and 6. Slice 5 also needs Tallypay to make the link.
- **Waits for slices 5 and 6, and for an answer:** slice 7 leans on "when and how many at once" under "Not yet confirmed" in the requirements. It cannot be started until that is answered.
- **Cannot be started until answered:** slice 8 leans on "which clients the price list covers" and on "what a price's 'since' date means". Slice 1 stays clear of both: it charges a client the price list already holds, at one price for the whole month.
- **Recommended first: slice 1.** It shows the owner an invoice for one client, made from that client's walks and charged by length, in place of typing it by hand. It is the most the owner can be shown for the least, and every other slice builds on it.
