# Slice 1: Give a client the month's invoice at list prices

## Thin path
The owner gets a client's invoice for a month, made from the walks on the walkers' sheets, and is shown each walk charged at the list price for its length.

## Criteria
All lengths and prices here are invented.

- **monthly-client-invoice / 1**: Given a price list with 7.00 for a 20-minute walk and 13.00 for a 45-minute walk, unchanged throughout, and sheets showing that a client had one walk of each length in a month and one more 20-minute walk in the month before, when the owner gets that client's invoice for the later month, then it shows only that month's two walks, charged at 7.00 and 13.00.
- **monthly-client-invoice / 2**: Given sheets showing that a client had a walk of a length that has no price on the list, when the owner gets that client's invoice for that month, then no price is charged for that walk and the owner is shown that its length has no list price.

## Needs from outside
- The walks on the walkers' paper sheets.
- The owner's price list.

## Left for later
- What a row of the price list means for the client named on it, which waits on the owner (requirements question 1): slice 1. Blocker: it could change what a client is charged. The criteria follow what the owner has said, that everyone pays the list price and nobody has a price of their own.
- Checking or approving invoices before clients get them, which waits on the owner's decision (question 4): slice 1. Blocker: it is not known whether an invoice may go to a client unchecked.
- Several invoices for a client, or one shared between clients, which waits on the owner's decision (question 5): slice 1. Blocker: it is not known what one invoice covers. The criteria show one client's own invoice and settle neither.
- Sending the payment link: slice 2. Usable without it: the owner can send payment links through Tallypay as today.
- Seeing which clients have not paid: slice 3. Usable without it: the owner can get each month's invoices; nobody chases late payers today.
- Adding a missing price to the list and then charging it: slice 4. Usable without it: the owner is shown which walk has no list price.
- Walks from before and after a price change (question 2): slice 5. Usable without it: the owner can invoice walks whose prices have not changed.

## Size
Criteria: 2.
