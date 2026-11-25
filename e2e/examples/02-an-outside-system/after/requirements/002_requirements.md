# Requirements: Invoice clients for the month

- [ ] **walker-walk-entry**: A walker can enter their own walks.
- [ ] **owner-walk-correction**: The business owner can correct the walks a walker has entered.
- [ ] **month-from-usual-walks**: A walker can start a month from the usual weekly walks.
- [ ] **monthly-client-invoice**: The business owner can get each client an invoice for that client's walks in a month.
- [ ] **invoice-payment-link**: The business owner can get each client a Tallypay payment link for their invoice.

## Out for now
- Chasing clients who haven't paid on time: the scope map marks it "later".

## Limits that apply
- Tallypay stays: the payment link for an invoice is a Tallypay one.
- The walkers will only use their phones: applies. Whatever a walker does here, including entering walks, must be possible on their phone.
- Clients' addresses and door codes seen only by the business owner and the walker for that client: applies. Nothing in entering walks or invoicing may show them to anyone else.

## Not yet confirmed
Each of these waits on your decision or answer. None is settled.

1. Where do the usual weekly walks come from, and who can change them? Also, is it right that the walker is the one who starts a month from them? Bears on **month-from-usual-walks**: the answer could add an item or change who it names.
2. Everyone pays the list price for the length of the walk, nobody has a price of their own, only the business owner changes prices, and anything not on the list is added to it first. Must the business owner be able to add and change prices in the product, and can anything besides walks go on an invoice? The price list also has a Client column, naming a different client in each of its 12 rows (see `sources.md`): what is it for, if nobody has a price of their own? Bears on **monthly-client-invoice**: the answer could add items or widen this one.
3. Can a walker put right a walk they entered, and until when can walks for a month be entered or changed? Bears on **walker-walk-entry** and **owner-walk-correction**: the answer could add an item.
4. Must the business owner be able to check or change invoices before clients get them? Bears on **monthly-client-invoice** and **invoice-payment-link**: the answer could add an item. **The business owner does not know yet.**
5. When an invoice turns out wrong after the client has it, what must the business owner be able to do? Bears on **monthly-client-invoice** and **invoice-payment-link**: the answer could add an item.
6. Does each client always get exactly one invoice a month, or are there cases such as one payer for several clients, or one client needing more than one invoice? Bears on **monthly-client-invoice**: the answer could change it or add an item.
7. Does anyone besides the business owner make or send invoices, or need to see them (apart from the client who gets one)? Bears on **monthly-client-invoice** and **invoice-payment-link**: the answer could change who they name or add an item.
8. Does anything that exists today have to come across, such as client details or earlier or unpaid invoices? Bears on **monthly-client-invoice** and **invoice-payment-link**: the answer could add an item.

## Outside systems and lasting things
- Tallypay
- Client
- Walk
- Usual weekly walk
- Invoice
