# Slice 1: Get one client's invoice for the month from their regular weekly walks, each walk charged by its length

## Thin path
The business owner states a client's regular weekly walks, asks for that client's invoice for a month, and is shown the invoice: each walk the month holds, charged by its length, and the total.

## Criteria
- **regular-walks / 1**: Given a client with no regular walks stated, when the owner states one 30-minute walk every Tuesday, then the client's regular walks show "Tuesday, 30 minutes".
- **regular-walks / 2**: Given a client with no regular walks stated, when the owner states a 45-minute walk, then it is refused with a message that walks are 30 or 60 minutes, and the client's regular walks stay empty.
- **walk-pricing / 1**: Given a client whose only regular walk is 60 minutes every Thursday, priced at 18.00, and a month with five Thursdays, when the owner asks for the client's invoice for that month, then it shows 5 walks of 60 minutes at 18.00 each, total 90.00.
- **walk-pricing / 2**: Given a client with a regular 30-minute walk for which the price list holds no price for that client, when the owner asks for the invoice, then no invoice is made and the owner is told which walk has no price.
- **monthly-invoices / 1**: Given a client with a 30-minute walk every Monday priced at 10.00 and a 60-minute walk every Thursday priced at 18.00, and a month with four Mondays and four Thursdays, when the owner asks for the client's invoice for that month, then it shows 4 walks of 30 minutes at 10.00 and 4 walks of 60 minutes at 18.00, total 112.00.
- **monthly-invoices / 2**: Given a client with no regular walks stated, when the owner asks for the client's invoice for a month, then no invoice is made and the owner is told there are no walks to invoice.

## Needs from outside
The owner's price list, which holds the prices for each client's walks.

## Left for later
- A second dog from the same home at half price: slice 2. Usable without it: invoices for clients with one dog.
- One-off extra walks: slice 3. Usable without it: invoices from regular walks only.
- Changing or stopping a client's regular walks: slice 4. Usable without it: a client's regular walks can be stated, and the invoice follows them as stated.
- Sending the client a Tallypay payment link: slice 5. Usable without it: the owner has the invoice to send some other way for now.
- Invoices for every client at once: slice 6. Usable without it: one client's invoice at a time.
- Clients the price list does not cover, and a price that changes part-way through a month: slice 8. Usable without it: invoices for clients the price list holds, at one price for the whole month.

## Size
Criteria: 6.
