# Requirements: Invoice each client for the month

- [ ] **monthly-invoices**: The business owner can get, for each client, an invoice for the month made from that month's walks, without typing it by hand.
- [ ] **send-payment-links**: The business owner can have each client receive a Tallypay payment link for their invoice.
- [ ] **regular-walks**: The business owner can state a client's regular weekly walks once, change them, or stop them, so that each month's invoice includes them without being typed again.
- [ ] **one-off-extras**: The business owner can add a one-off extra walk to a client's month.
- [ ] **walk-pricing**: The business owner can have each walk charged by its length (30 or 60 minutes, priced differently), with a second dog from the same home at half price.

## Out for now
- Keeping a record of each walk, so no walker's sheet is lost or guessed (activity 1 on the scope map, "next").
- Chasing clients who have not paid (activity 3, "later").

## Limits that apply
- Staying with Tallypay: the payment link each client receives is a Tallypay one.

## Not yet confirmed
1. **Which clients the price list covers** (bears on **walk-pricing**): the price list has one row for each of 12 different clients, against about sixty clients in all. If the other clients are priced some other way, or not yet listed, an item for pricing them is added.
2. **What a price's "since" date means** (bears on **walk-pricing**): each price has a date it applies from. If a price changes part-way through a month, the walks before and after may be charged differently; if not, a month is always charged at one price.
3. **Putting a mistake right** (bears on **monthly-invoices** and **send-payment-links**): whether an invoice or link already sent may need to be corrected or cancelled, and by whom. If so, an item is added.
4. **When and how many at once** (bears on **send-payment-links**): whether all sixty or so go out together on a set day each month, or one at a time as each is ready.
5. **What else exists today that must come across** (bears on **regular-walks**): whether a client list, with each client's regular walks, exists that the new way must start from. The price list is the one thing named so far (see `sources.md`).

## Outside systems and lasting things
- Tallypay: the card service that makes the payment links.
- Client: about sixty regular clients, each invoiced monthly.
- Walk: what a walker did for a client, as written on the paper sheets today; a regular walk repeats weekly until changed or stopped, and an extra is one-off.
- Invoice: one per client per month.
- Price list: the owner's list of prices, kept in a file on their own machine (described in `sources.md`).
