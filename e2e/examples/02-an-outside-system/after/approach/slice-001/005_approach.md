# Approach: slice 1

## The owner's price list, which holds the prices for each client's walks
What the slice needs of it: the price of a 30-minute and a 60-minute walk for the client being invoiced (walk-pricing / 1, monthly-invoices / 1), and, where it holds none, that the owner can be told so (walk-pricing / 2).
Held to: no limit of the user's bears on it (the Tallypay limit, in 000_problem.md and 002_requirements.md, concerns the payment link, which this slice leaves out).

| Way | Does what the slice needs | What it ties us to |
|---|---|---|
| Without: the owner keeps the price list and supplies it, as they do today (described in `sources.md`) | Meets walk-pricing / 1, walk-pricing / 2 and monthly-invoices / 1: none of these says the prices are found by themselves, and the list is the owner's own | nothing |

Recommended: without. The need is a list the owner already keeps and supplies, so there is nothing to compare and nothing to sign up for. It gives up nothing.
Not settled by this read: nothing here. Which clients the list covers and what its "since" date means are open questions under "Not yet confirmed" in the requirements, and slice 8 takes them.
Decision: without
Not taken: no candidate. The need is met by the owner supplying their own list.

## Committed to
Nothing.
