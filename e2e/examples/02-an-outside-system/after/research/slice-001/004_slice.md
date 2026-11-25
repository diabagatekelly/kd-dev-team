# Slice 1: See a client's invoice for the month's regular and one-off walks, priced by length

## Thin path
The owner asks for one client's invoice for a month and is shown that month's regular and one-off walks, each priced by its length, with the total.

## Criteria
All clients, dates and prices here are invented.

- **monthly-client-invoice / 1**: Given a client with two 30-minute regular walks in March and a 30-minute price of 10.00, when the owner asks for that client's March invoice, then it shows both walks at 10.00 each and a total of 20.00.
- **monthly-client-invoice / 2**: Given a client with one 30-minute walk and one 60-minute walk in March, priced at 10.00 and 18.00, when the owner asks for that client's March invoice, then it shows each walk at the price for its length and a total of 28.00.
- **monthly-client-invoice / 3**: Given a client with one regular and one one-off 30-minute walk in March and a 30-minute price of 10.00, when the owner asks for that client's March invoice, then it shows both walks and a total of 20.00.
- **monthly-client-invoice / 4**: Given a client with one 30-minute walk on 31 March and one on 1 April, and a 30-minute price of 10.00, when the owner asks for that client's March invoice, then it shows only the 31 March walk and a total of 10.00.
- **monthly-client-invoice / 5**: Given a client with a 60-minute walk in March and no price for 60 minutes, when the owner asks for that client's March invoice, then the owner is told that price is missing and is shown no invoice.
- **monthly-client-invoice / 6**: Given a client with no walks in March, when the owner asks for that client's March invoice, then the owner is told there are no walks to invoice and is shown no invoice.

## Needs from outside
none

## Left for later
- Second dog from the same home at half price: slice 2. Usable without it: the owner can see invoices for one-dog walks, and works out second-dog invoices by hand as today.
- Late and early cancellations: slice 3. Usable without it: the owner can see invoices for months with no cancellations, and works out the others by hand as today.
- Payment link: slice 4. Usable without it: the owner sends the link through Tallypay as today.
- How walks get in each month: slice 1. Blocker: it is not known what the owner puts in or changes.
- Client prices and the kinds of walk: slice 1. Blocker: it is not known which price applies to a client's walk.
- Other charges, and whether extras are only extra walks: slice 1. Blocker: it is not known whether the total is complete.
- Changing or adding prices: slice 1. Blocker: it is not known whether the owner must be able to do this.
- What "Since" in the price list means: slice 1. Blocker: it is not known whether a month can need an old and a new price.
- Invoices per client: slice 1. Blocker: it is not known whether a client can have several invoices or share one.
- What must come across from today: slice 1. Blocker: it is not known what has to be there before the first invoice.

## Size
Criteria: 6.
