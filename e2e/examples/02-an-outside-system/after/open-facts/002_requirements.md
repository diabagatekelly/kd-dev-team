# Requirements: invoice clients for the month

- [ ] **monthly-client-invoice**: The owner can give each client an invoice for the month, made from the walks on the walkers' sheets, with each walk charged at the list price for its length.
- [ ] **invoice-payment-link**: The owner can send each client a payment link through Tallypay for the month's invoice.
- [ ] **price-list-addition**: The owner can add to the price list something that is not on it yet, before it is charged.
- [ ] **see-who-unpaid**: The owner can see which clients have not paid, without digging for it.

## Out for now
- Walkers noting their walks in the product: the scope map marks this "next". For now each walker writes every walk on a paper sheet and hands the sheets in at the end of the month.
- Following up clients who have not paid on time: the scope map marks this "later". Nobody does it today.
- Prices of a client's own: there are none, and everyone pays the list price.
- Paying the walkers through this too: not decided, and no part of invoicing clients.
- Anyone but the owner doing the invoicing: asked who does it and who must not, the owner answered "Only me."

## Limits that apply
- We already use Tallypay as our card service, and we are staying with it: every payment link in this activity goes through Tallypay.

## Not yet confirmed
1. The price list has a "Client" column, with a different entry in each of its 12 rows, while everyone pays the list price and nobody has a price of their own. What is a client's name doing on a row of the price list, and what does the row mean for that client? (monthly-client-invoice, price-list-addition; could change what is charged or what is added to the list, or add an item.)
2. Does a price on the list ever change, and if so, which price is charged for walks done before the change? What does the "Since" column date? (price-list-addition, monthly-client-invoice; could add an item for changing prices or change what is charged.)
3. When an invoice is wrong, what must the owner be able to put right, both before and after the client has it? (monthly-client-invoice, invoice-payment-link; could add items for correcting, cancelling or replacing.)
4. Must the invoices be checked or approved before clients get them? (monthly-client-invoice; could add an item for checking them.)
5. Is it always one invoice for each client for the month, or can there be several, or one shared between clients? (monthly-client-invoice; could change it or add an item.)
6. Is there anything from how you invoice today that must come across, such as client details, the price list or unpaid invoices? (all items; could add an item.)

## Outside systems and lasting things
- Tallypay: the card service the payment links go through.
- Client: someone who is invoiced.
- Walk: what the month's invoices are made from.
- Price list: the prices walks are charged at.
- Invoice: what a client gets for the month.
- Payment link: what a client is sent through Tallypay.
