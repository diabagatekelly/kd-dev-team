# Kept: slice 1

## What the slice creates and keeps
- client: monthly-client-invoice / 1
- walk: monthly-client-invoice / 1
- price-list-entry: monthly-client-invoice / 1
- invoice: monthly-client-invoice / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `client-identity` | text | whatever says whose walk it is, from the walkers' sheets | client-details | monthly-client-invoice / 1 |
| `walk-date` | date | when the walk was, from the walkers' sheets | client-details | monthly-client-invoice / 1 |
| `walk-length` | other | the walk's length, from the walkers' sheets and the price list | no | monthly-client-invoice / 2 |
| `list-price` | number | the owner's price list | no | monthly-client-invoice / 1 |
| `invoice-month` | date | the month the owner asks for | no | monthly-client-invoice / 1 |

## Other things the slice has
- `walks-intake`: the way the walks on the sheets reach the product, not yet decided (monthly-client-invoice / 1)
- `price-list-intake`: the way the owner's price list reaches the product, not yet decided (monthly-client-invoice / 1)
- `invoice-request`: the owner getting a client's invoice for a month (monthly-client-invoice / 1)
- `invoice-view`: what the owner is shown of the invoice (monthly-client-invoice / 2)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | the approach commits to nothing, so the slice sends no request to an outside system |
| receive-external-data: all | dropped | nothing comes from an outside system: the walks and prices are supplied by the owner |
| sync-01 | price-list-entry | the owner has their own price list and the product may hold the prices too, so the two could differ |
| sync-04 | `invoice-view` | an invoice could be made from prices or walks older than what the owner now has |
| sync-06 | price-list-entry | an entry taken off the owner's list could still be charged |
| sync-02, sync-03, sync-10 | dropped | the documents have only the owner doing the invoicing and describe no editing of a saved thing in this slice |
| sync-09 | walk | a later version of the product could share the saved walks with this one |
| sync-05, sync-07, sync-08, sync-11, sync-12 | dropped | the slice updates no copy from a running source: no source system is committed to |
| limits-04 | `invoice-request` | about sixty clients, roughly double in summer, set how much one month holds |
| limits-07 | `walks-intake` | a month of walks could arrive as one large item |
| limits-08 | `invoice-view` | a client's month could hold more walks than are shown at once |
| limits-01, limits-02, limits-09 | dropped | the slice calls no outside system and uses no paid service |
| limits-03, limits-05, limits-06, limits-10, limits-11, limits-12 | dropped | only the owner does the invoicing, and the slice has no shared, scheduled or waiting work |
| durable-write-01 | walk | a month of walks could be cut off while being saved |
| durable-write-02 | walk | walks the owner thinks are saved become charges |
| durable-write-04 | walk | saving walks can fail for lack of space |
| durable-write-05 | walk | a failed save of walks could leave a walk uncharged |
| durable-write-08 | invoice | an invoice must agree with its walks and their prices |
| durable-write-09 | price-list-entry | a silently changed price would be charged |
| durable-write-10 | walk | walks are kept, and sheets can be lost, so a usable copy matters |
| durable-write-03 | walk | where the walks are stored is not yet decided |
| durable-write-06 | price-list-entry | the price list could be replaced wholesale when brought in again |
| durable-write-07 | dropped | no criterion adds to a history |
| durable-write-11 | walk | what makes up the saved data is not yet decided |
| durable-write-12 | `walks-intake` | the product could be closed while walks are being saved |
| startup-read-01 | walk | the slice reads saved walks and could find them damaged |
| startup-read-03 | walk | no walks saved and walks that cannot be opened must not look the same |
| startup-read-07 | walk | where the walks are kept is not decided, so something else may be able to remove them |
| startup-read-09 | price-list-entry | a readable but wrong price would be charged |
| startup-read-10 | walk | it matters what is fallen back on if the walks become unusable |
| startup-read-02 | walk | the product reads from a saved-data location that could hold something else |
| startup-read-04 | walk | an earlier save of walks could be unfinished |
| startup-read-05 | walk | the saved walks could be readable but not changeable |
| startup-read-06, startup-read-08 | dropped | no document speaks of more than one copy running, and the slice rescues no data |
| migration: all | dropped | this is the first slice and no product code or saved product data exists to carry forward |
| concurrency-03 | invoice | an invoice reads walks and prices that must belong to one moment |
| concurrency-04 | invoice | the invoice is made from the month's walks, and that set can still grow |
| concurrency-06 | `invoice-view` | an open invoice could lag behind a changed walk or price |
| concurrency-12 | walk | nothing says only one copy of the product can run against the walks |
| concurrency-01, concurrency-02, concurrency-05, concurrency-07, concurrency-08, concurrency-09, concurrency-10, concurrency-11 | dropped | only the owner does the invoicing, and the slice has no competing changes, holds or exclusive rights |
| lifecycle-01 | `walks-intake` | bringing in a month of walks can fail partway |
| lifecycle-05 | walk | a walk makes sense only with its client and a price for its length |
| lifecycle-06 | client | a client's walks and invoices belong to that client |
| lifecycle-07 | price-list-entry | invoices may depend on an entry that is removed |
| lifecycle-08 | invoice | an invoice with an unpriced walk could be left unfinished |
| lifecycle-10 | walk | a walk removed by mistake would go uncharged |
| lifecycle-11 | client | what is kept about a former client is not said |
| lifecycle-03 | invoice | whether anything about getting an invoice cannot be taken back is not said |
| lifecycle-02, lifecycle-04, lifecycle-09, lifecycle-12 | dropped | the slice undoes nothing in steps, holds nothing for a time and keeps no copies that learn of removals |
| user-input-01 | `client-identity` | text saying who the client is has some length |
| user-input-02 | `walks-intake` | a sheet may be missing something about a walk |
| user-input-03 | `client-identity` | names contain varied characters |
| user-input-05 | `walks-intake` | rules about walks and prices need one place to hold however they arrive |
| user-input-06 | `walks-intake` | a walk can be unusable and the owner must learn why |
| user-input-07 | `client-identity` | stray spaces could split one client into two |
| user-input-08 | `list-price` | a price has edges such as zero or a mistyped large figure |
| user-input-09 | `client-identity`; walk | two clients may look alike, and one walk could be put in twice |
| user-input-10 | `client-identity` | the text is shown again on the invoice |
| user-input-11 | walk | a walk's date, length and client must make sense together |
| user-input-12 | `walk-date`; `list-price` | dates and amounts can be written in more than one way |
| user-input-04 | `client-identity` | whether a client is told apart by one value or several is not said |
| user-action-01 | `invoice-request` | the owner could ask for the same invoice again before it appears |
| user-action-02 | `invoice-view` | nothing says whether showing an invoice again makes it anew |
| user-action-05 | `walks-intake` | walks part entered could be lost on leaving |
| user-action-08 | `walks-intake` | a wrongly entered walk needs a way back |
| user-action-04 | `invoice-view` | client details could stay visible after the owner leaves |
| user-action-07 | `invoice-view` | the owner could have the invoice open twice |
| user-action-10 | `walks-intake` | the owner may stop partway through a month's walks |
| user-action-03 | `invoice-view` | the owner could step back to an invoice after prices or walks changed |
| user-action-06 | `walks-intake` | a screen discarded during a long entry of walks could lose them |
| user-action-09 | `walks-intake` | taking in a month of walks could replace or repeat earlier ones, which may call for a confirmation |
| user-action-11 | `walks-intake` | a signed-in period could end partway through the walks |
| user-action-12 | `invoice-view` | a saved address to an invoice could be opened later or by someone else |
| long-operation-01 | `walks-intake` | bringing in a month of walks may take more than a few seconds |
| long-operation-06 | `walks-intake` | it could be interrupted partway |
| long-operation-08 | `walks-intake` | some walks may be usable and others not |
| long-operation-02 | `walks-intake` | a stalled intake must not look like a working one |
| long-operation-03 | `walks-intake` | the owner may find they are taking in the wrong month's walks |
| long-operation-04 | `price-list-intake` | a price list taken in only partly would charge from an incomplete list |
| long-operation-05 | `walks-intake` | the owner may leave while a month of walks is taken in |
| long-operation-07 | `walks-intake` | a walk that fails late would go uncharged unnoticed |
| long-operation-09 | `walks-intake` | an intake could stop making progress |
| long-operation-10 | `walks-intake` | the owner may need the result of an intake later to check it against the sheets |
| long-operation-11 | `walks-intake` | a second intake of the same month could be started while one runs |
| long-operation-12 | `walks-intake` | walks sure to be refused, as with no price list present, could be checked first |
| time-01 | `invoice-month` | which month is offered or meant may rest on the device's clock |
| time-07 | `walk-date` | a walk's date must not move into another month |
| time-08 | `walk-date` | which month a walk falls in depends on whose date it is |
| time-12 | walk | when the walk happened and when it was put in can fall in different months |
| time-02, time-03, time-04, time-05, time-06, time-09, time-10, time-11 | dropped | the slice works from calendar dates written on sheets: it times, schedules and orders no events |
| text-01 | `client-identity` | walks are grouped by whether two clients are the same |
| text-02 | `client-identity` | capital letters could split one client |
| text-03 | `client-identity` | unseen characters could split one client |
| text-05 | `client-identity` | a long name may be cut |
| text-06 | `invoice-view` | walks or clients may be listed by text |
| text-10 | `client-identity` | the owner must tell similar clients apart before billing one |
| text-04 | `invoice-request` | the owner may have to find a client by name |
| text-07, text-08, text-09, text-11, text-12 | dropped | no document speaks of readers in other languages: the one reader is the owner |
| presentation-01 | `invoice-view` | walk dates may be shown |
| presentation-03 | `invoice-view` | amounts need an unmistakable currency |
| presentation-05 | `list-price` | prices have decimal places |
| presentation-02 | `invoice-view` | amounts are numbers on screen |
| presentation-04 | `invoice-view` | wording may count walks, including one or none |
| presentation-11 | `invoice-view` | the owner may order a client's walks by date or amount to check them against a sheet |
| presentation-12 | `invoice-view` | a month of walks longer than one screen must stay in order throughout |
| presentation-06, presentation-07, presentation-08, presentation-09, presentation-10 | dropped | the slice shows dates and amounts to the owner alone: no zones, week layout, other calendars or list of people |
| corpus: all | dropped | the slice ships no body of content: the prices and walks are the owner's own data |
| secrets: all | dropped | the approach commits to nothing, so no document gives the product a credential to use; the owner's own access is asked about under sign-in and authorization |
| authorization-01 | invoice; client | only the owner does the invoicing, and client details are kept |
| authorization-03 | `invoice-request` | the limit to the owner has to hold somewhere |
| authorization-04 | `invoice-request` | someone other than the owner is covered by no rule |
| authorization-06 | `invoice-request` | another page could send a request as the owner if the product is reached through a browser, which is not decided |
| authorization-07 | `walks-intake` | taking walks in changes what is charged, so it must not happen by merely opening something |
| authorization-08 | `invoice-view` | a failed check of who is asking must not leave client details open |
| authorization-09 | `price-list-intake` | a price list or other file the product stores could be fetched directly |
| authorization-10 | `invoice-request` | what says the asker is the owner could come from their device |
| authorization-11 | `invoice-view` | a lost or shared device could keep access to invoices |
| authorization-02, authorization-05, authorization-12 | dropped | only the owner does the invoicing, so there are no other users' records, role changes or accounts to confuse |
| configuration: all | dropped | no criterion or document gives the slice a setting: prices are data the owner supplies |
| logging-01 | invoice | a wrong invoice may need tracing |
| logging-03 | `client-identity` | client details could reach records |
| logging-07 | `walks-intake` | a failure must be told to the owner |
| logging-02 | invoice | tracing a wrong invoice needs records that say which client and walks were involved |
| logging-04 | `walks-intake` | text taken from the sheets or a file could end up in a record |
| logging-05 | invoice | getting an invoice could happen while no record can be written |
| logging-06 | walk | records of every walk taken in would grow month after month |
| logging-08 | invoice | records needed to trace an invoice could be lost with the machine |
| logging-09 | `walks-intake` | a failed walk is only noticed if someone is told or reads the record |
| logging-10 | invoice | a record of what was charged could be changed without notice |
| logging-11 | invoice | records of walks and invoices need to be put in order |
| logging-12 | client | records could keep client details after they are no longer needed |
| accessibility-01 | `invoice-request` | the documents do not say the owner can do without the keyboard when asking for an invoice |
| accessibility-02 | `invoice-view` | the owner must be able to leave whatever part of the invoice they enter |
| accessibility-03 | `walks-intake` | if walks are typed in, the owner must see where the typing goes |
| accessibility-04 | `invoice-view` | closing an invoice leaves the owner's place to be settled |
| accessibility-05 | `invoice-request` | the controls for choosing a client and month need names |
| accessibility-06 | `invoice-view` | the invoice could mark something without words |
| accessibility-07 | `walks-intake` | the owner must learn whether a walk was taken in |
| accessibility-08 | `invoice-view` | a walk with no list price could be marked by colour |
| accessibility-09 | `invoice-view` | the amounts must be readable |
| accessibility-10 | `invoice-view` | the invoice's walks and amounts must survive enlarged text |
| accessibility-12 | `invoice-view` | the form of the product is not decided, so something on it could move |
| accessibility-11 | dropped | no criterion or document gives any step of the slice a time limit |
| sign-in-01 | `invoice-request` | if the owner signs in, someone could guess their way to client details |
| sign-in-02 | `invoice-request` | an account that exists from the start would open the invoices to whoever knows it |
| sign-in-04 | `invoice-request` | an owner who loses their way in cannot invoice, as nobody else does it |
| sign-in-05 | `invoice-request` | the owner's first way in would have to be made somehow |
| sign-in-06 | `invoice-request` | any second way in would also reach client details |
| sign-in-07 | `invoice-request` | the owner may need to learn that someone else signed in as them |
| sign-in-08 | `invoice-view` | a session left open would leave invoices readable |
| sign-in-09 | `invoice-request` | the owner could be signed in on more than one device |
| sign-in-10 | `invoice-request` | a session held before signing in must not become the owner's for someone else |
| sign-in-11 | `walks-intake` | changing what clients are charged may call for proof that it is the owner |
| sign-in-12 | `invoice-view` | the owner may need to end access from a lost device |
| sign-in-03 | dropped | only the owner does the invoicing: nobody else signs up |
| stored-data-01 | client; walk | client details and when their dogs are walked are kept |
| stored-data-02 | `client-identity` | copies of client details could be read by others |
| stored-data-09 | client | how long client details are kept is not said |
| stored-data-07 | client | whether any other party receives client details is not said |
| stored-data-03 | client | client details may be protected with a key |
| stored-data-04 | walk | losing such a key could lose the walks still to be charged |
| stored-data-05 | `client-identity` | asking for a client's invoice could put who they are in an address |
| stored-data-06 | `invoice-view` | an invoice sent to the owner's screen could be copied on the way |
| stored-data-08 | `invoice-view` | a reply could carry other clients' details along with the one asked for |
| stored-data-10 | `client-identity` | the owner's device could hold client details |
| stored-data-11 | `price-list-intake` | a submitted price list file could carry hidden details, including client entries |
| stored-data-12 | client | whether reading client details is recorded is not said |
| file-intake-02 | `price-list-intake` | the owner's price list is a file, and it may be taken in as one |
| file-intake-04 | `price-list-intake` | a taken-in file's name could be used where it is saved |
| file-intake-05 | `price-list-intake` | a cell of the file could be run when used or opened again |
| file-intake-07 | `price-list-intake` | the file's name could be shown back in a message |
| file-intake-01, file-intake-03, file-intake-06, file-intake-08 | dropped | no packed files or pictures, and nobody but the owner supplies or receives a file |
| misuse-01 | `invoice-request` | an invoice could be asked for before the month's sheets are all in |
| misuse-02 | invoice | charging only list prices is a rule that must hold somewhere |
| misuse-07 | `walks-intake` | a walk that arrives with a price of its own must not set the charge |
| misuse-03, misuse-04, misuse-05, misuse-06, misuse-08 | dropped | only the owner does the invoicing, and nothing is in limited supply or needs a second person |
