# Answers: slice 1

## A1: A client named on a price list row changes no charge
Kind: fact
Says: Everyone pays the list price for the length of the walk and nobody has a price of their own, so a client named on a price list row changes nothing anyone is charged. Why the list has that column is not known, and no charge depends on it.
Rests on: 002_requirements.md, line 11
Under: monthly-client-invoice
Criterion: Given an invented price list row that gives 7.00 for a 20-minute walk and names one client, when another client's 20-minute walk is invoiced, then it is charged 7.00.
Settles: C.states.price-list-entry.listed

## A2: Checking invoices before clients get them
Kind: owner
Says: To decide: whether an invoice waits for the owner's check before it can go to a client.
Rests on: how the owner wants to work (requirements line 22)
Options: the owner looks over each invoice before it goes | an invoice may go without being looked over
Recommended: the owner looks over each one, because two or three invoices are wrong each month today; it costs time at each month's end
If left: the slice cannot be built, and nothing says whether an invoice waits
Harm: high
Settles: S.invoice.awaiting-check.*, C.states.invoice.awaiting-check, C.states.dead-end.13
Decided: the owner looks over each invoice before it goes (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given an invoice the owner has not yet marked as looked over, when it is shown, then it is shown as not yet checked and not ready for the client.

## A3: How many invoices a client has, and shared ones
Kind: owner
Says: To decide: whether a client always has exactly one invoice a month, may have several, or may share one.
Rests on: a rule of the owner's own business (requirements line 23)
Options: exactly one for each client each month | a client may have several | clients may share one
Recommended: exactly one each, unless the owner knows of a case where that fails, because it is the simplest to check against the sheets
If left: the slice cannot be built, since what one invoice covers is unknown
Harm: high
Settles: S.invoice.being-made.second
Decided: exactly one invoice for each client each month (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given two clients who each had two walks in a month, when the owner gets one client's invoice for that month, then there is one invoice, holding both of that client's walks and none of the other's.

## A4: Which price is charged when a price changes
Kind: owner
Says: To decide: whether prices change or are corrected, and which price a walk is then charged, including on an invoice already got.
Rests on: a rule of the owner's own business (requirements line 20)
Options: the price in force on the day of the walk | the price on the list when the invoice is got
Recommended: the price on the day of the walk, because a client then pays what applied when the walk happened
If left: only walks whose prices have not changed can be relied on (slice 5 waits)
Harm: high
Settles: S.price-list-entry.price-changed.*, S.price-list-entry.removed-or-corrected.*, C.states.price-list-entry.price-changed, C.states.price-list-entry.removed-or-corrected, C.states.dead-end.8, C.states.dead-end.9, C.states.dead-end.10, L.sync-06.price-list-entry, L.lifecycle-07.price-list-entry
Decided: the price in force on the day of the walk (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given a 20-minute walk priced at 7.00 up to the 15th of a month and 8.00 from the 16th, when the owner gets the invoice for a client with such a walk on the 10th and another on the 20th, then they are charged 7.00 and 8.00.

## A5: An invoice with a walk that has no list price
Kind: owner
Says: To decide: whether an invoice holding an unpriced walk can be treated as ready for the client.
Rests on: a rule of the owner's own business; the slice says only that no price is charged and the owner is shown why (monthly-client-invoice / 2)
Options: it is not ready until every walk on it has a price | it is usable with the unpriced walk left uncharged
Recommended: not ready until every walk has a price, because otherwise a walk can go uncharged without anyone meaning it to
If left: the owner is shown the unpriced walk but nothing says whether the invoice may be used
Harm: high
Settles: S.invoice.has-unpriced-walk.monthly-client-invoice-1, L.lifecycle-08.invoice, C.states.dead-end.12
Decided: an invoice is not ready until every walk on it has a price (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given an invoice with one walk that has no list price, when the owner looks it over, then it cannot be marked ready for the client and the owner is shown that the walk needs a price first.

## A6: Putting right a wrong walk or invoice
Kind: owner
Says: To decide: what the owner must be able to correct, take back, cancel or replace, before and after the client has an invoice, and whether any of it is part of this slice.
Rests on: what is in or out (requirements line 21)
Options: correct or remove a walk and get the invoice again, before the client has it | that, and also replace an invoice the client already has | no correcting in the product for now
Recommended: correcting a walk and getting the invoice again, in this slice, because a mistyped walk would otherwise stay wrong; replacing a sent invoice can wait until invoices are sent
If left: a walk entered wrongly has no stated way back
Harm: high
Settles: S.walk.wrong-or-corrected.*, S.invoice.wrong.*, S.invoice.cancelled-or-replaced.*, L.user-action-08.walks-intake, L.lifecycle-10.walk, C.states.walk.wrong-or-corrected, C.states.invoice.cancelled-or-replaced, C.states.dead-end.5, C.states.dead-end.7, C.states.dead-end.16, C.states.dead-end.17
Decided: the owner can correct or remove a walk and get the invoice again before the client has it, in this slice; replacing an invoice the client already has can wait until invoices are sent (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: new: walk-correction
Criterion: Given an invoice the client does not have, holding a walk entered with the wrong length, when the owner corrects the walk and gets the invoice again, then it shows the walk once, at the list price for the corrected length.

## A7: A lost walker's sheet
Kind: owner
Says: To decide: what clients are charged when a sheet is lost.
Rests on: a rule of the owner's own business (problem line 10)
Options: charge only walks there is a record of | let the owner put in walks they have worked out, marked as not from a sheet
Recommended: walks worked out by the owner are marked as such, because a guess can then be told from a record if a client asks
If left: the owner guesses, as today
Harm: medium
Settles: S.walk.sheet-lost.*, C.states.dead-end.6
Decided: the owner may put in walks they have worked out, marked as not from a sheet (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given a walk the owner put in as worked out because a sheet was lost, when the invoice holding it is shown, then that walk is marked as not from a sheet.

## A8: How long client details and walks are kept
Kind: owner
Says: To decide: how long a client's details, walks, invoices and any records naming them are kept, what happens when someone stops being a client, and by when removal is complete.
Rests on: an obligation the owner must accept; no document says
Options: keep while a client, then remove after a period the owner names once they know what they are obliged to keep | keep until the owner removes them by hand
Recommended: a named period after someone stops being a client, because details not held cannot be seen by others; the owner should first find out what they must keep
If left: everything is kept with no end
Harm: medium
Settles: L.lifecycle-06.client, L.lifecycle-11.client, L.stored-data-09.client, L.logging-12.client, C.states.client.no-longer-client, C.states.dead-end.2, C.states.dead-end.4
Decided: keep while a client, then remove after a named period once someone stops being a client; the period is not yet named and waits on the owner finding out what they must keep, as does how someone is marked as having left and by when removal is complete, so no criterion with a figure is written yet (the user, 2026-11-26: "I take what you recommend for each of them.")

## A9: Laws and terms that bind the handling
Kind: owner
Says: To decide: which laws, contracts or promises to clients bind how client details, walks and invoices are handled. No document names any.
Rests on: an obligation the owner must accept
Options: the owner finds out which apply where the business operates | the owner accepts going on without having checked
Recommended: find out before real client details go into the product, because meeting an obligation afterwards may mean changing what is already stored
If left: the product may be built without meeting an obligation
Harm: high
Settles: W.obligations
Decided: find out which laws, contracts and promises apply before real client details go into the product; the finding out is still to be done (the user, 2026-11-26: "I take what you recommend for each of them.")

## A10: How reliable and how quick it must be
Kind: owner
Says: To decide: how long the product may be unusable, and how slow getting an invoice may be, before the owner would say it does not work.
Rests on: how fast and reliable it must be is not said in any document
Options: out for up to a day is tolerable, and an invoice should appear within 10 seconds | it must be back within an hour at month's end | the owner names other figures
Recommended: up to a day and within 10 seconds, because invoicing is monthly and the sheets remain
If left: there is no figure to test against
Harm: low
Settles: W.target
Decided: being unusable for up to a day is tolerable, and an invoice should appear within 10 seconds (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given a client's month of walks put in, when the owner asks for the invoice, then it appears within 10 seconds.

## A11: Spare copies, and the key that opens them
Kind: owner
Says: To decide: how much of what the owner has put in may be lost if the machine or the key to the protected data is lost, and whether the owner keeps a spare copy of the data and a recovery copy of the key. Without the key the stored data cannot be read.
Rests on: how reliable it must be, and a cost and a duty the owner must accept
Options: a spare copy no more than a day old, kept apart from the machine and tried before real use, with a recovery copy of the key that the owner keeps safe and apart | no spare copy and no recovery copy: everything is put in again from the sheets and the price list
Recommended: the spare copy and the recovery key, because sheets have been lost before and may not be there to put walks in again
If left: nobody is responsible for either copy, and a lost machine or key may lose the stored data for good
Harm: medium
Settles: L.durable-write-10.walk, L.startup-read-10.walk, L.stored-data-04.walk
Decided: a spare copy no more than a day old, kept apart from the machine and tried before real use, with a recovery copy of the key that the owner keeps safe and apart (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given the machine and its key lost, when the latest spare copy is brought back with the owner's recovery copy of the key, then everything saved more than a day before the loss is there.

## A12: What comes across from today
Kind: owner
Says: To decide: whether client details, the price list or unpaid invoices must be brought into the product.
Rests on: what is in or out (requirements line 24)
Options: bring in the price list and client details only | also bring in unpaid invoices | bring in nothing, and put in what is needed by hand
Recommended: the price list and client details, because the slice needs prices and needs to tell clients apart; unpaid invoices matter only from slice 3
If left: nothing says what the product starts with
Harm: medium
Settles: C.states.client.becoming-client, C.states.client.regular, C.states.dead-end.1
Decided: bring in the price list and client details only (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given the price list and client details brought in at the start, when the owner opens the product before putting in any walk, then those prices and clients are there and no invoice from before, paid or unpaid, is.

## A13: Telling clients apart
Kind: owner
Says: To decide: what tells one client from another when sheets name them alike or differently.
Rests on: a rule of the owner's own business; no document says how a client is told apart
Options: each client is set up once and the owner picks which one a walk is for | whatever name is on the sheet is the client
Recommended: set up once and picked, because two spellings would otherwise make two clients and two alike would be merged; picking takes a little longer
If left: walks can be billed to the wrong client
Harm: high
Settles: L.user-input-04.client-identity, L.user-input-09.client-identity, L.text-01.client-identity, L.text-02.client-identity, L.text-10.client-identity, C.states.client.details-changed, C.states.dead-end.3
Decided: each client is set up once and the owner picks which one a walk is for (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: monthly-client-invoice
Criterion: Given the clients already set up, when the owner puts in a walk, then it can be saved only for a client picked from them, and no new client is made from what is typed there.

## A14: What a walker's sheet says for each walk
Kind: test
Says: Not known: what a walker writes for each walk (whose it is, the date, the length), how each is written, and whether any is ever left off.
Rests on: requirements line 9 says only that each walker writes every walk on a sheet
Test: the owner looks over a recent month's sheets on their own machine or desk and says what is written for each walk and what is sometimes missing, with no names.
Harm: high
Settles: L.user-input-02.walks-intake, V.walk-date.malformed

## A15: Whether the price list's walks are lengths
Kind: test
Says: Not known: whether the four different entries in the list's Walk column are lengths, whether every length walked has one, and whether any length has two prices.
Rests on: sources.md gives only the column names and counts
Test: the owner looks at the Walk and Price columns and says what the Walk entries stand for and whether each has a single price, with no names or real figures.
Harm: high
Settles: V.walk-length.malformed, V.walk-length.characters

## A16: How prices are written
Kind: test
Says: Not known: the currency of the prices, how many decimal places they carry and how they are written in the list.
Rests on: sources.md says only that the Price column holds numbers
Test: the owner says which currency and how many decimal places the list uses.
Harm: medium
Settles: L.presentation-05.list-price, L.user-input-12.list-price, L.presentation-03.invoice-view

## A17: How much one month holds
Kind: test
Says: Not known: the most walks one client has in a month, and the number of walks in all.
Rests on: problem line 4 gives about sixty clients and line 13 says cover roughly doubles in summer
Test: the owner counts the walks on one busy month's sheets, in all and for the busiest client.
Harm: low
Settles: L.limits-04.invoice-request

## A18: The ordinary invoice
Kind: fact
Says: Getting a client's invoice for a month shows only that month's walks, each at the list price for its length.
Rests on: monthly-client-invoice / 1
Settles: S.client.regular.monthly-client-invoice-1, S.walk.handed-in.monthly-client-invoice-1, S.walk.on-invoice.monthly-client-invoice-1, S.price-list-entry.listed.monthly-client-invoice-1, S.invoice.being-made.monthly-client-invoice-1, S.invoice.got.monthly-client-invoice-1

## A19: A length with no list price
Kind: fact
Says: No price is charged for a walk whose length has no list price, and the owner is shown that it has none.
Rests on: monthly-client-invoice / 2
Settles: S.client.regular.monthly-client-invoice-2, S.walk.handed-in.monthly-client-invoice-2, S.walk.on-invoice.monthly-client-invoice-2, S.walk.no-list-price.monthly-client-invoice-1, S.walk.no-list-price.monthly-client-invoice-2, S.price-list-entry.missing.monthly-client-invoice-1, S.price-list-entry.missing.monthly-client-invoice-2, S.price-list-entry.listed.monthly-client-invoice-2, S.invoice.being-made.monthly-client-invoice-2, S.invoice.got.monthly-client-invoice-2, S.invoice.has-unpriced-walk.monthly-client-invoice-2, V.walk-length.dangling

## A20: Only the owner invoices
Kind: fact
Says: Only the owner does the invoicing; walkers and everyone else do not.
Rests on: 002_requirements.md, line 13
Settles: L.authorization-01.invoice, L.authorization-01.client, W.who-sees

## A21: Only list prices are charged
Kind: chosen
Says: Every charge comes from the list price for the walk's length. Nothing that arrives with a walk can set or change its price, and the rule holds wherever an invoice is made, not only on screen. Only a walk's client, date and length can be put in with it.
Rests on: requirements lines 3 and 11
Under: monthly-client-invoice
Criterion: Given a list price of 7.00 for a 20-minute walk, when a 20-minute walk is put in along with a price of 1.00 by any route, then the client's invoice charges it 7.00.
Settles: L.misuse-02.invoice, L.misuse-07.walks-intake

## A22: Getting an invoice changes nothing
Kind: chosen
Says: Asking for an invoice only reads clients, walks and prices. Asking again, or twice at once, shows the same invoice from the same walks and prices and makes no second charge. The request cannot change or remove a walk or price, whatever is sent with it. While it is being made the owner sees that it is.
Rests on: a request that only reads is safe to repeat and gives nothing to tamper through
Under: monthly-client-invoice
Criterion: Given a client's month with two walks, when the owner asks for its invoice twice in quick succession, then one invoice with those two walks is shown, each walk once.
Settles: L.user-action-01.invoice-request, L.user-action-02.invoice-view, T.walk.invoice-request, S.client.regular.again, S.client.regular.reopened, S.client.regular.restart, S.client.regular.second, S.client.regular.time, S.walk.handed-in.again, S.walk.on-invoice.again, S.walk.no-list-price.again, S.price-list-entry.listed.again, S.price-list-entry.missing.again, S.invoice.being-made.again, S.invoice.got.again, S.invoice.has-unpriced-walk.again

## A23: An invoice is made from one moment and says when
Kind: chosen
Says: An invoice is made from the walks and prices as they stood together at one moment, and shows when that was. If a walk or price of it changes afterwards, the shown invoice is marked out of date the next time it is looked at, including after stepping back or in another window, and is not presented as current. A client and month with no walks say so rather than showing an empty or old invoice.
Rests on: an old invoice taken for current is how a wrong charge goes out
Under: monthly-client-invoice
Criterion: Given an invoice on show, when one of its walks is changed elsewhere and the owner returns to or reloads it, then it is not shown as current without the change.
Settles: L.sync-04.invoice-view, L.concurrency-03.invoice, L.concurrency-04.invoice, L.concurrency-06.invoice-view, L.user-action-07.invoice-view, L.user-action-03.invoice-view, L.durable-write-08.invoice, L.lifecycle-03.invoice, S.walk.on-invoice.reopened, S.walk.on-invoice.time, S.invoice.got.reopened, S.invoice.got.restart, S.invoice.got.second, S.invoice.has-unpriced-walk.reopened, S.invoice.has-unpriced-walk.restart, S.invoice.has-unpriced-walk.second, S.invoice.being-made.reopened, S.invoice.being-made.restart

## A24: A month with nothing to invoice
Kind: chosen
Says: Where a client has no walks put in for the month asked for, the owner is told so. A walk not yet put in, such as one still on a sheet, cannot be on an invoice; the invoice lists every walk it is made from so the owner can compare it with the sheets.
Rests on: the product knows only what has been put into it
Under: monthly-client-invoice
Criterion: Given a client with no walks put in for a month, when the owner asks for that month's invoice, then the owner is told there are no walks and no charge is shown.
Settles: S.walk.on-sheet.*, S.client.becoming-client.monthly-client-invoice-1, S.client.becoming-client.monthly-client-invoice-2, V.walk-date.empty, C.states.invoice.being-made, C.states.dead-end.11

## A25: New, changed and former clients
Kind: chosen
Says: A month's walks are invoiced the same way whether the client is new, has changed details or has since left: the walks stay with the same client. Nothing about a client changes by itself or because an invoice is got.
Rests on: the walks happened and the item charges the month's walks (requirements line 3)
Under: monthly-client-invoice
Criterion: Given a client who has left after having a walk last month, when the owner gets last month's invoice, then the walk is on it.
Settles: S.client.becoming-client.again, S.client.becoming-client.reopened, S.client.becoming-client.restart, S.client.becoming-client.second, S.client.becoming-client.time, S.client.details-changed.*, S.client.no-longer-client.*

## A26: Waiting walks and entries stay as they are
Kind: chosen
Says: Time passing, reopening or restarting changes no walk and no price entry. A walk with no list price stays shown as unpriced until its length has a price. Nothing is removed or priced by itself.
Rests on: a change nobody made would alter a charge unnoticed
Under: monthly-client-invoice
Criterion: Given a walk shown as having no list price, when the product is closed and opened again, then the walk is still there and still shown as having no list price.
Settles: S.walk.handed-in.reopened, S.walk.handed-in.time, S.walk.no-list-price.reopened, S.walk.no-list-price.time, S.price-list-entry.missing.reopened, S.price-list-entry.missing.restart, S.price-list-entry.missing.time, S.price-list-entry.listed.reopened, S.price-list-entry.listed.restart, S.price-list-entry.listed.time

## A27: One current price list
Kind: chosen
Says: The owner's own list is the one that stands. The product shows when its copy of the prices was last brought in, shows the prices it holds so the owner can compare them, and keeps no change of its own in this slice. A list is taken in whole or not at all; a new one that is refused or cut off leaves the earlier one in use. A length given twice with different prices is refused. Two attempts to change the list at once leave one whole list.
Rests on: a part-replaced or doubled list charges wrong amounts
Under: monthly-client-invoice
Criterion: Given prices already in use, when bringing in a new list is cut off partway, then all the earlier prices are still in use and the owner is shown that the new list was not taken in.
Settles: L.sync-01.price-list-entry, L.durable-write-06.price-list-entry, L.long-operation-04.price-list-intake, S.price-list-entry.missing.second, S.price-list-entry.listed.second

## A28: Noticing a wrong or altered price
Kind: chosen
Says: Prices can be changed only by the signed-in owner. Each time prices change the product records when and what changed, and the owner can see the prices in use with that time. A price altered outside the product's own ways is treated as damage: no invoice is made from it. Earlier lists stay recoverable from the record.
Rests on: a wrong price is charged to every walk of that length
Under: monthly-client-invoice
Criterion: Given prices in use, when the owner brings in a list with one price different, then the owner is shown which price changed before any invoice uses it.
Settles: L.durable-write-09.price-list-entry, L.startup-read-09.price-list-entry, T.price-list-entry.price-list-intake

## A29: Walks are saved safely
Kind: chosen
Says: A walk is shown as saved only once it will survive a restart or power cut. A cut-off save leaves a walk whole or absent. A save that fails, for lack of space or any storage error, says the walk was not saved, leaves earlier walks as they were, and is not reported saved on a mere retry: what is stored is read back first. The owner sees which walks are saved after returning.
Rests on: a walk wrongly believed saved goes uncharged
Under: monthly-client-invoice
Criterion: Given saved walks, when saving another fails, then the owner is told that walk was not saved and the earlier walks are unchanged.
Settles: L.durable-write-01.walk, L.durable-write-02.walk, L.durable-write-04.walk, L.durable-write-05.walk, L.durable-write-12.walks-intake

## A30: Where walks are stored, as one whole
Kind: chosen
Says: Walks, clients and prices are kept only on storage that keeps confirmed saves through a power cut, never somewhere the platform may clear by itself, and are copied, moved and restored together as one whole. A part-restored or damaged set is detected and refused.
Rests on: parts restored apart would disagree; clearable storage loses walks silently
Under: monthly-client-invoice
Criterion: Given saved data with part of it missing, when the product is opened, then it says the data is incomplete and makes no invoice.
Settles: L.durable-write-03.walk, L.durable-write-11.walk, L.startup-read-07.walk

## A31: Damaged, foreign or unwritable saved data
Kind: chosen
Says: At start, data that is damaged, unreadable or not the product's own is never overwritten or silently replaced by an empty start: the product says what is wrong and makes no invoice. A true first run is told apart from data that cannot be opened. An unfinished save is discarded whole and the owner told. Data that can be read but not changed is shown as read only, with nothing reported saved. A later version's data that this version does not understand is refused, not rewritten.
Rests on: starting fresh over damaged data destroys what could be recovered
Under: monthly-client-invoice
Criterion: Given saved data that cannot be opened, when the product starts, then it says so, does not present itself as new, and leaves the data as it was.
Settles: L.startup-read-01.walk, L.startup-read-02.walk, L.startup-read-03.walk, L.startup-read-04.walk, L.startup-read-05.walk, L.sync-09.walk

## A32: Two copies or devices at once
Kind: chosen
Says: There is one set of saved data, and changes to it are taken one at a time. A second copy that would write to it separately is refused.
Rests on: two writers can silently undo each other's walks
Under: monthly-client-invoice
Criterion: Given the product in use on the saved data, when a second copy tries to change the same data separately, then its change is refused and it says why.
Settles: L.concurrency-12.walk

## A33: Putting walks in
Kind: chosen
Says: The owner puts walks in, one saved at a time, each saved as soon as it is confirmed. Leaving, closing, a discarded screen or an ended session loses at most the one walk not yet confirmed, and on return the owner sees what is saved for that month. Stopping is simply not entering more. Entering a walk replaces no earlier one; changing a saved walk is only the correction of A6.
Rests on: only the owner invoices; saving each walk leaves little to lose and nothing half done
Under: monthly-client-invoice
Criterion: Given five walks confirmed and a sixth half entered, when the product is closed and reopened, then the five are shown as saved and the sixth is not.
Settles: L.lifecycle-01.walks-intake, L.user-action-05.walks-intake, L.user-action-10.walks-intake, L.user-action-06.walks-intake, L.user-action-09.walks-intake, L.user-action-11.walks-intake, L.long-operation-06.walks-intake, L.long-operation-03.walks-intake, L.long-operation-08.walks-intake

## A34: No long walk intake in this slice
Kind: not here
Says: Walks are saved one at a time (A33), so there is no long-running intake to show progress for, stall, finish unseen, queue behind another or keep a result of.
Rests on: the choice in A33
Settles: L.long-operation-01.walks-intake, L.long-operation-02.walks-intake, L.long-operation-05.walks-intake, L.long-operation-07.walks-intake, L.long-operation-09.walks-intake, L.long-operation-10.walks-intake, L.long-operation-11.walks-intake, L.long-operation-12.walks-intake

## A35: The same walk twice
Kind: chosen
Says: A walk for the same client, date and length as one already saved is not refused, since two such walks may both have happened; the owner is told of the match and must say it is a second walk before it is saved.
Rests on: refusing could lose a real walk and accepting silently could charge twice
Under: monthly-client-invoice
Criterion: Given a saved walk, when the owner puts in one with the same client, date and length, then it is saved only after the owner confirms it is a second walk.
Settles: L.user-input-09.walk, V.walk-length.twice

## A36: A walk must be complete and sensible
Kind: chosen
Says: A walk needs a client, a date and a length. One lacking any, with a date that is not a real date or is after today, is not saved; the message beside the field says which is wrong and what to do, and what was typed stays. The same rules hold however a walk arrives, not only on screen. A walk whose length has no price is saved and shown as unpriced.
Rests on: monthly-client-invoice / 2 needs unpriced walks kept; the rest stops walks that cannot be charged rightly
Under: monthly-client-invoice
Criterion: Given the owner putting in a walk with no date, when they confirm it, then it is not saved and the message at the date says a date is needed.
Settles: L.user-input-05.walks-intake, L.user-input-06.walks-intake, L.user-input-11.walk, L.lifecycle-05.walk, V.client-identity.missing, V.walk-date.missing, V.walk-date.outside, V.walk-length.empty, V.walk-length.missing

## A37: Dates and months
Kind: chosen
Says: A walk's date is the calendar date on the sheet, with no time or zone, never converted, and shown with the day, the month in words and the year. The month is decided by that date, not by when it was put in. The first and last days of a month belong to it. Dates are typed in one stated form or picked, so no day and month can be swapped.
Rests on: a date shifted or misread moves a charge into another month
Under: monthly-client-invoice
Criterion: Given walks dated 31 March and 1 April, when the owner gets March's invoice, then it shows the walk of 31 March and not that of 1 April.
Settles: L.time-07.walk-date, L.time-08.walk-date, L.time-12.walk, L.user-input-12.walk-date, V.walk-date.edge, L.presentation-01.invoice-view

## A38: Choosing the month
Kind: chosen
Says: The owner always sees and chooses the month and year; the device's clock only suggests the last finished month. No month, a month not understood or a future month gives no invoice and says why. A month still running can be asked for and is marked as not finished, so an early request is not taken as complete. A month before any walk shows there are no walks. A wrong device clock cannot move a walk, only the suggestion and these two marks.
Rests on: the owner's choice must settle the month, not the clock
Under: monthly-client-invoice
Criterion: Given the current month, when the owner gets a client's invoice for it, then the invoice is marked as for a month not yet finished.
Settles: L.time-01.invoice-month, L.misuse-01.invoice-request, V.invoice-month.empty, V.invoice-month.missing, V.invoice-month.malformed, V.invoice-month.edge, V.invoice-month.outside

## A39: Walk length values
Kind: chosen
Says: A length is picked from the lengths on the price list, or put in as another length, which is then shown as unpriced. Zero, negative or implausibly long lengths, over 24 hours, are refused with a message at the field.
Rests on: picking avoids two spellings of one length; monthly-client-invoice / 2 needs other lengths kept
Under: monthly-client-invoice
Criterion: Given the owner putting in a walk, when they give a length of zero, then it is not saved and the message at the length says why.
Settles: V.walk-length.edge, V.walk-length.outside, V.walk-length.long

## A40: Price values
Kind: chosen
Says: A price must be a number above zero. An empty, missing, non-numeric, zero or negative value refuses the whole list, naming the row by its number and not by the client; the earlier prices stay in use. Prices are held and shown exactly as the list gives them, never rounded or approximated. No upper limit is set, since the currency is not known; a mistyped large price shows among the changed prices before use (A28).
Rests on: a mistyped price would be charged on every such walk, and this holds whatever currency and decimal places the list uses
Under: monthly-client-invoice
Criterion: Given prices in use, when a list with an empty price is brought in, then it is refused with the row's number and the earlier prices stay in use.
Settles: L.user-input-08.list-price, V.list-price.empty, V.list-price.missing, V.list-price.malformed

## A41: Client text
Kind: chosen
Says: Text naming a client may be up to 200 characters, counted as the characters a person sees; longer is refused with the limit shown, never cut. Letters of any language, spaces, apostrophes, hyphens and ordinary punctuation are accepted; control and unseen characters are removed. Spaces at either end are removed and runs of spaces become one; empty is refused. Shown text is always treated as text, never as instructions or page content. Long names wrap on the invoice.
Rests on: usual safe handling of names
Under: monthly-client-invoice
Criterion: Given a client name containing page markup, when it is shown on an invoice, then the markup appears as the characters typed and does nothing.
Settles: L.user-input-01.client-identity, L.user-input-03.client-identity, L.user-input-07.client-identity, L.user-input-10.client-identity, L.text-03.client-identity, L.text-05.client-identity

## A42: Finding and ordering
Kind: chosen
Says: A client is picked from a list in alphabetical order that can be searched, ignoring capitals, accents and extra spaces; similar matches are all shown for the owner to choose. Walks on an invoice are ordered by date, in date order across the whole month, and every walk can be reached by scrolling, with none left out.
Rests on: ordering by date matches checking against sheets
Under: monthly-client-invoice
Criterion: Given a month with more walks than fit on one screen, when the owner scrolls the invoice, then every walk appears once, in date order.
Settles: L.text-04.invoice-request, L.text-06.invoice-view, L.presentation-11.invoice-view, L.presentation-12.invoice-view, L.limits-08.invoice-view

## A43: Large entries
Kind: chosen
Says: Walks come one at a time (A33), so the largest single item is one walk, whose fields have their own limits.
Rests on: the choice in A33
Under: monthly-client-invoice
Criterion: Given the owner putting in a walk, when the client text is over 200 characters, then it is not saved and the limit is shown.
Settles: L.limits-07.walks-intake

## A44: Numbers and counts on screen
Kind: chosen
Says: Every number is written one consistent way, following the owner's own region. Wording with a count reads correctly for none, one and many.
Rests on: mixed number styles invite misreading an amount
Under: monthly-client-invoice
Criterion: Given a month with exactly one walk, when its invoice is shown, then any count of walks is worded in the singular.
Settles: L.presentation-02.invoice-view, L.presentation-04.invoice-view

## A45: The price list file
Kind: chosen
Says: If the list is brought in as a file, only a plain table with the expected columns is accepted, judged by its content and not its name. Nothing is kept from it beyond what charging needs, so the Client column is not kept for charging (A1); anything of it that another decision brings in is protected as A46 and A52 say. The file itself is not kept or served, its name is never used to decide where anything is saved and is shown only as plain text, and no cell is ever run as a formula or code.
Rests on: keeping only what is used leaves nothing extra to leak or run
Under: monthly-client-invoice
Criterion: Given a list file with a cell written as a formula, when it is brought in, then the formula is never worked out or run.
Settles: L.file-intake-02.price-list-intake, L.file-intake-04.price-list-intake, L.file-intake-05.price-list-intake, L.file-intake-07.price-list-intake, L.stored-data-11.price-list-intake, L.authorization-09.price-list-intake, T.client-details.price-list-intake

## A46: Nothing is open without signing in
Kind: chosen
Says: Every page, request and stored item needs the signed-in owner, checked where the data is held and not only on screen. What no rule allows is refused. If the check cannot be completed, the request is refused. What a device says about who someone is counts only if the product can verify it was not altered. Requests sent by another site in the owner's name are refused, and opening a link or loading a page changes nothing. A saved address opened signed out leads to sign-in and shows no client data; one for something gone says it is not there.
Rests on: the documents allow only the owner (requirements line 13) and do not say where the product can be reached from
Under: new: owner-only-access
Criterion: Given nobody signed in, when any address or request for an invoice or walk is made, then no client, walk, price or invoice is returned.
Settles: L.authorization-03.invoice-request, L.authorization-04.invoice-request, L.authorization-06.invoice-request, L.authorization-07.walks-intake, L.authorization-08.invoice-view, L.authorization-10.invoice-request, L.user-action-12.invoice-view, T.client-details.walks-intake

## A47: Signing in
Kind: chosen
Says: There is one way in, for one account, the owner's. No account or password exists until the owner sets one up through a one-time step available only to whoever runs the product, which ends once used. After 5 failed tries, further tries wait 15 minutes, and the owner is told at next sign-in. A lost way in is recovered only through the same kind of one-time step. A fresh session is made at each sign-in and any earlier unsigned one is dropped.
Rests on: usual protection for a single account holding personal details
Under: new: owner-only-access
Criterion: Given 5 failed sign-in tries in a row, when another is made within 15 minutes, then it is refused even with the right details and the person is told when to try again.
Settles: L.sign-in-01.invoice-request, L.sign-in-02.invoice-request, L.sign-in-04.invoice-request, L.sign-in-05.invoice-request, L.sign-in-06.invoice-request, L.sign-in-10.invoice-request

## A48: Sessions
Kind: chosen
Says: A session ends after 30 minutes unused and 12 hours in all. At most 3 are open at once; a fourth ends the oldest. The owner can see them, end any or all, and is told at sign-in of one from a new device or of changed sign-in details. Ending or signing out takes effect on the very next request. Changing sign-in details or replacing the price list asks the owner to prove who they are again. After sign-out, stepping back shows no client data.
Rests on: short, visible sessions limit what a lost device opens
Under: new: owner-only-access
Criterion: Given an invoice on show, when the owner signs out and steps back, then no part of the invoice is shown.
Settles: L.sign-in-07.invoice-request, L.sign-in-08.invoice-view, L.sign-in-09.invoice-request, L.sign-in-11.walks-intake, L.sign-in-12.invoice-view, L.authorization-11.invoice-view, L.user-action-04.invoice-view

## A49: Strangers collecting or altering invoices
Kind: chosen
Says: Only the signed-in owner gets anything (A46), failed and refused attempts are recorded without client details, and the owner is shown them at next sign-in. What is shown travels encrypted, so it cannot be read or altered on the way, and is made from saved walks and prices, not from anything the browser sends back. This does not protect against someone who controls the owner's own device.
Rests on: refusal plus a visible record is how an attempt is both stopped and noticed
Under: new: owner-only-access
Criterion: Given a request for an invoice from someone not signed in, when the owner next signs in, then they are shown that a refused request was made.
Settles: T.client-details.invoice-view, T.client-details.invoice-request, T.invoice.invoice-view

## A50: Tampering with walks
Kind: chosen
Says: Only the signed-in owner can add, correct or remove a walk, each of these is recorded with its time, and each invoice lists every walk it is made from so it can be compared with the sheets.
Rests on: a visible list against the paper record exposes added or missing walks
Under: new: owner-only-access
Criterion: Given nobody signed in, when a walk is sent to be saved, then it is not saved.
Settles: T.invoice.walks-intake

## A51: What a reply and the device hold
Kind: chosen
Says: A reply holds only what the screen asked for: one client's invoice holds no other client's walks. Client names and walk dates never appear in an address. Pages and replies with client data are marked not to be stored by browsers or anything in between, and nothing about clients is kept on the device. The session value is the only thing kept there, unreadable to page code.
Rests on: copies that are never made cannot leak
Under: new: owner-only-access
Criterion: Given the owner viewing one client's invoice, when what was sent is examined, then it holds no other client's walks and no client name is in any address.
Settles: L.stored-data-05.client-identity, L.stored-data-06.invoice-view, L.stored-data-08.invoice-view, L.stored-data-10.client-identity, X.client-details.replies, F.browser.came-from, F.browser.kept-by-browser

## A52: What is sensitive and how it is protected
Kind: chosen
Says: Client identities and the dates of their walks are the sensitive data, since they could show when someone is away. Prices and invoices matter because altering them changes charges. Stored data and every copy are encrypted and readable only by the product and whoever runs it. Keys are kept apart from the data and its copies, used for nothing else and can be replaced; an exposed key is replaced and the data protected again. The risk of losing a key is part of A11.
Rests on: usual protection of personal data at rest
Under: new: owner-only-access
Criterion: Given a copy of the stored data without its key, when it is read, then no client name or walk date can be read from it.
Settles: L.stored-data-01.client, L.stored-data-01.walk, L.stored-data-02.client-identity, L.stored-data-03.client, X.client-details.stored, W.sensitive, W.prize

## A53: Nobody else receives anything
Kind: chosen
Says: This slice sends no client or walk data to any other party, monitoring and measurement included. Where the product is run is not chosen yet; choosing a party that would hold the data comes back to the owner.
Rests on: nothing is committed to (approach, Committed to)
Under: new: owner-only-access
Criterion: Given the product in use, when a walk is saved or an invoice got, successfully or not, then no client name or walk date is sent to any other party.
Settles: L.stored-data-07.client, X.client-details.telemetry

## A54: What is recorded
Kind: chosen
Says: Recorded: sign-ins and refusals, each walk added, corrected or removed, each change of prices, each invoice got, each failure, and each opening of client data by the signed-in owner. Each record has the event, the time from the product's own clock with its zone, an order number, and internal references to the client and walks, never names or walk dates. Typed or file text is not copied into records. The owner can look at them.
Rests on: enough to trace a wrong invoice without spreading client details
Under: monthly-client-invoice
Criterion: Given an invoice was got, when the records are read, then an entry shows when and refers to the walks used, with no client name or walk date in it.
Settles: L.logging-01.invoice, L.logging-02.invoice, L.logging-03.client-identity, L.logging-04.walks-intake, L.logging-11.invoice, L.stored-data-12.client, X.client-details.logs

## A55: Keeping the records
Kind: chosen
Says: Records cannot be edited or removed through the product, a gap or change in their order numbers is detectable, and they are included in whatever spare copy A11 settles. They are capped at 100 MB; as the cap nears the owner is told, and nothing is silently dropped. If a record cannot be written, a change to walks or prices is refused, and viewing still works with the owner told. How long they are kept is part of A8.
Rests on: a charge-changing event with no record cannot be traced
Under: monthly-client-invoice
Criterion: Given records that cannot be written, when the owner tries to save a walk, then it is not saved and the owner is told why.
Settles: L.logging-05.invoice, L.logging-06.walk, L.logging-08.invoice, L.logging-10.invoice

## A56: Failures: what is shown and who notices
Kind: chosen
Says: The only user is the owner, so the owner is who notices. Every failure is shown at once where the action was taken, saying what did not happen and what to do, without internal detail or client data; internal detail goes to the records without client data. Error messages and traces never carry client names or walk dates. Nothing else alerts anyone.
Rests on: requirements line 13; plain failure messages with no leaked detail are usual practice
Under: monthly-client-invoice
Criterion: Given a failure while getting an invoice, when the message and the records are read, then neither contains a client name or walk date, and the message says the invoice was not made.
Settles: L.logging-07.walks-intake, L.logging-09.walks-intake, X.client-details.errors-inside, X.client-details.errors-shown, W.noticed

## A57: If it cannot be used for an hour
Kind: chosen
Says: The owner invoices later, or types the invoice by hand from the sheets as today. The sheets remain the record, and no client is affected by an hour's delay.
Rests on: invoicing is monthly and today's way still exists (problem line 6)
Settles: W.unavailable

## A58: Test data is invented
Kind: chosen
Says: Examples and test data kept with the code use invented names, dates and prices only, never rows from the owner's list or sheets.
Rests on: code and its history are copied more widely than the data
Under: new: owner-only-access
Criterion: Given the code and its test data, when they are searched, then no real client name or walk from the owner's files or sheets is in them.
Settles: X.client-details.samples

## A59: Keyboard use
Kind: chosen
Says: Everything can be done by keyboard alone, focus is always visible, nothing traps it, and when something closes focus returns to where the owner came from.
Rests on: accessibility good practice, applied
Under: monthly-client-invoice
Criterion: Given only a keyboard, when the owner puts in a walk and gets and closes an invoice, then every step works, focus is visible throughout and ends back where the invoice was asked for.
Settles: L.accessibility-01.invoice-request, L.accessibility-02.invoice-view, L.accessibility-03.walks-intake, L.accessibility-04.invoice-view

## A60: Reading the screen without sight or colour
Kind: chosen
Says: Every control announces its name and purpose, anything shown without words has words with the same meaning, results of actions are announced, and nothing is told by colour alone, including an unpriced walk.
Rests on: accessibility good practice, applied
Under: monthly-client-invoice
Criterion: Given a screen reader, when the owner gets an invoice with an unpriced walk, then it announces that the walk has no list price.
Settles: L.accessibility-05.invoice-request, L.accessibility-06.invoice-view, L.accessibility-07.walks-intake, L.accessibility-08.invoice-view

## A61: Contrast, large text and motion
Kind: chosen
Says: Text has a contrast of at least 4.5 to 1 in every state and theme, everything stays usable with text at twice the size, and nothing moves that is not needed; any movement stops where less motion is asked for.
Rests on: accessibility good practice, applied
Under: monthly-client-invoice
Criterion: Given text at twice its size, when an invoice is shown, then every walk and amount can still be read with nothing cut off or overlapping.
Settles: L.accessibility-09.invoice-view, L.accessibility-10.invoice-view, L.accessibility-12.invoice-view

## A62: No settings in this slice
Kind: not here
Says: No criterion or choice gives the slice a setting the owner or whoever runs it must supply; if the build adds one, these questions are drawn again.
Rests on: kept.md drops configuration for this reason
Settles: V.every-setting.missing, V.every-setting.empty, V.every-setting.malformed, V.every-setting.outside

## A63: States slice 1 never reaches
Kind: not here
Says: Slice 1 sends no payment link and records no payment, so an invoice cannot be in these states while only this slice exists. Slices 2 and 3 must ask again.
Rests on: slice 1 "Left for later": links are slice 2 and unpaid invoices slice 3
Settles: S.invoice.link-sent.*, S.invoice.paid.*, C.states.invoice.paid, C.states.dead-end.14, C.states.dead-end.15

## A64: What the page may run and who may frame it
Kind: chosen
Says: The page loads and runs code only from the product itself, with no inline or outside code or styles; any component's code is served as part of the product from a fixed, checked copy. No other site may frame it, call it and read replies, or send it messages it acts on. Every reply states its true type and the browser is told not to guess. No submitted file or data reply is ever run as a page. The product sends nobody to an address supplied by someone else.
Rests on: standard browser protections
Under: new: owner-only-access
Criterion: Given another site, when it tries to show the product inside its own page, then the browser does not show it.
Settles: F.browser.context, F.browser.page-policy, F.browser.framing, F.browser.type-guessing, F.browser.other-sites, F.browser.messages, F.browser.others-code, F.browser.sent-on

## A65: What the browser holds to know the owner
Kind: chosen
Says: Only a session value is kept. Page code cannot read it, it is sent only over encrypted connections and only to the product, and not with requests other sites start. It, and any one-time setup value, is made from a secure random source, too long to guess, and ends as A47 and A48 say.
Rests on: standard session protection
Under: new: owner-only-access
Criterion: Given a session that has been ended, when its value is sent again, then the request is refused.
Settles: F.browser.known-by, F.unguessable.made

## A66: How it is reached over a network
Kind: chosen
Says: It answers only under its own intended address and refuses others. Every connection is encrypted; an unencrypted one is refused or moved to an encrypted one before anything is sent. Facts about the sender are not taken from anything the sender can set. Each address accepts only the kinds of request it needs. No diagnostic mode, file listing, source history, internal documentation, measurements or test code can be reached, and replies, refusals included, do not say what it is built from.
Rests on: standard network hardening
Under: new: owner-only-access
Criterion: Given the product running, when a request is made without encryption, then no client data is accepted or returned over it.
Settles: F.network.answers-to, F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, F.network.gives-away

## A67: Components written by others
Kind: chosen
Says: Every component, including those it brings with it, is listed with its source and fixed version, fetched only from that source and checked against its recorded fingerprint. Known flaws are checked for at every change and at least weekly; a serious one that applies is fixed within 7 days. As few components as possible see client data, outside input or sign-in values, or run code on installing, and each is reviewed first.
Rests on: standard practice for outside components; the 7 days can be overturned
Under: new: owner-only-access
Criterion: Given a component whose fetched content does not match its recorded fingerprint, when the product is built, then the build stops.
Settles: F.dependency.known-flaw, F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
