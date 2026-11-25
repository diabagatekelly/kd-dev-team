# Kept: slice 1

## What the slice creates and keeps
- invoice: monthly-client-invoice / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `chosen-client` | identifier | the owner, asking | client-details | monthly-client-invoice / 1 |
| `chosen-month` | date | the owner, asking | no | monthly-client-invoice / 4 |
| `client-name` | text | stored client information | client-details | monthly-client-invoice / 1 |
| `walk-date` | date | stored walks | client-details | monthly-client-invoice / 4 |
| `walk-length` | choice | stored walks | client-details | monthly-client-invoice / 2 |
| `walk-type` | choice | stored walks: regular or one-off | client-details | monthly-client-invoice / 3 |
| `price` | number | stored prices | client-details | monthly-client-invoice / 2 |

## Other things the slice has
- `invoice-request`: the owner asking for a client's invoice for a month (monthly-client-invoice / 1)
- `invoice-view`: what the owner is shown: walks, prices and total (monthly-client-invoice / 1)
- `refusal-message`: what the owner is told when no invoice is shown (monthly-client-invoice / 5)
- `no-walks-message`: what the owner is told when the client has no walks that month (monthly-client-invoice / 6)
- `stored-walks`: the walks an invoice is made from (monthly-client-invoice / 1)
- `stored-prices`: the prices an invoice is made from (monthly-client-invoice / 5)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The slice says it needs nothing from outside. |
| receive-external-data: all | dropped | No criterion receives anything from an outside system. |
| sync: all | dropped | No criterion keeps a local copy of a source or updates one. |
| limits-01, limits-02, limits-09 | dropped | The slice needs nothing from outside, so no outside or paid service is asked. |
| limits-03 | dropped | The slice's only actor is "the owner", and no criterion consumes a shared allowance. |
| limits-04 | `invoice-request` | There are about sixty clients, and the problem says the work roughly doubles in summer. |
| limits-08 | `invoice-view` | A month's walks for one client are shown together. |
| limits-05, limits-06, limits-10, limits-11, limits-12 | dropped | No criterion has a limit that stops someone, scheduled work or waiting work. |
| limits-07 | dropped | No criterion submits an item. |
| durable-write-01 | `invoice` | Invoice is a thing the product keeps, so saving it can be cut off. |
| durable-write-02 | `invoice` | The owner may rely on an invoice having been kept. |
| durable-write-03 | `invoice` | A kept invoice has to survive on whatever holds it. |
| durable-write-04 | `invoice` | Keeping an invoice can fail for lack of space. |
| durable-write-05 | `invoice` | Storage can report that keeping an invoice failed. |
| durable-write-06 | dropped | No criterion replaces saved data wholesale. |
| durable-write-07 | `invoice` | Invoices may build up month after month. |
| durable-write-08 | `invoice`; `stored-walks` | An invoice's walks and total are drawn from the stored walks. |
| durable-write-09 | `stored-prices` | A silently changed price would give a wrong total. |
| durable-write-10 | `invoice` | A copy of the saved data may be taken while an invoice is being kept. |
| durable-write-11 | `invoice` | The kept invoice depends on whatever else makes up the saved data. |
| durable-write-12 | `invoice` | The product may be closed while an invoice is being kept. |
| startup-read-01 | `stored-walks` | Damaged walks cannot give a complete invoice. |
| startup-read-02 | `stored-walks` | The slice reads walks from a saved-data location. |
| startup-read-03 | `stored-walks` | Unreadable walks must not be mistaken for the no-walks case of criterion 6. |
| startup-read-04 | `invoice` | An earlier run may leave the keeping of an invoice unfinished. |
| startup-read-05 | `stored-walks` | The walks may be readable but not changeable. |
| startup-read-06 | `stored-walks` | A second copy may start while the walks are being repaired. |
| startup-read-07 | `invoice` | Where the product runs is not said, so a platform may remove what it keeps. |
| startup-read-08 | `stored-walks` | Rescued walks could be missing or repeated on an invoice. |
| startup-read-09 | `stored-prices` | A readable but wrong price gives a wrong invoice. |
| startup-read-10 | `invoice` | Unusable saved data would need a spare copy. |
| migration: all | dropped | This is the first slice, the project has no code, and no criterion carries saved data forward; what must come across is still a blocker. |
| concurrency-01, concurrency-02 | dropped | No criterion changes an existing item. |
| concurrency-03 | `stored-walks`; `stored-prices` | One total is worked out from walks and prices together. |
| concurrency-04 | `stored-walks` | The invoice is decided from the set of walks in a month. |
| concurrency-05, concurrency-06, concurrency-07, concurrency-09, concurrency-10, concurrency-11 | dropped | No criterion changes shared items, takes exclusive use of them or runs clashing operations. |
| concurrency-08 | `stored-walks` | The walks may be in use when an invoice is asked for. |
| concurrency-12 | `invoice` | The documents do not rule out two copies of the product keeping invoices. |
| lifecycle-01, lifecycle-02, lifecycle-03 | dropped | No criterion makes something in separate steps, undoes anything or takes a step that cannot be taken back. |
| lifecycle-04 | `invoice` | states.md has a being-made state with no way out. |
| lifecycle-05 | `stored-walks`; `stored-prices` | A walk can lack its price, as in criterion 5. |
| lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11 | dropped | No criterion removes anything. |
| lifecycle-08 | `invoice` | An invoice may be shown and then left, with no way out said. |
| lifecycle-12 | dropped | No criterion holds anything for a limited time. |
| user-input-01 | `chosen-client` | How the owner gives the client is not said and may be typed. |
| user-input-02 | `invoice-request` | The request depends on a client and a month. |
| user-input-03 | `chosen-client` | A typed client may contain any character. |
| user-input-04 | `chosen-month` | A month may be asked for with or without its year, whole or in parts. |
| user-input-05 | `invoice-request` | Rules about the client and month have to be enforced somewhere. |
| user-input-06 | `refusal-message`; `no-walks-message` | Criteria 5 and 6 refuse to show an invoice. |
| user-input-07 | `invoice-request` | The client or month may be left empty. |
| user-input-08 | dropped | No criterion has the owner type a number. |
| user-input-09 | `chosen-client` | The owner must get the intended client among others. |
| user-input-10 | `client-name` | A stored client name is shown back. |
| user-input-11 | `invoice-request` | The client and month may not go together, as with a month before the client's first walk. |
| user-input-12 | `chosen-month` | A month can be written in several forms. |
| user-action-01 | `invoice-request` | The owner can ask again before the invoice appears. |
| user-action-02 | `invoice-view` | The view may be reloaded after an invoice has been made and kept. |
| user-action-03 | `invoice-view` | The owner can step back to it. |
| user-action-04 | `invoice-view` | It shows client details, and the documents do not say there is no signing out. |
| user-action-05, user-action-07, user-action-09, user-action-10, user-action-11 | dropped | The slice is one request to see an invoice: no criterion has edits, a destructive action, several steps or work in progress to carry on. |
| user-action-06 | `invoice-view` | A device may discard the view and bring it back. |
| user-action-08 | `invoice-request` | If asking keeps an invoice, the owner may want that undone. |
| user-action-12 | `invoice-view` | A saved address to it may be opened later. |
| long-operation: all | dropped | The only operation is showing one client's walks for one month, which no document makes a long one. |
| time-01 | `chosen-month` | Which month is offered or finished may depend on the clock. |
| time-02, time-03, time-05, time-06 | dropped | No criterion compares machines' clocks, waits or expires, uses a time of day or sets a future moment. |
| time-04 | `chosen-month` | The invoice covers a calendar span. |
| time-07 | `walk-date` | Criterion 4 turns on a walk's date staying on its own day. |
| time-08 | `walk-date` | The zone decides which day and month a walk falls in. |
| time-09 | `chosen-month` | The end of a month, including February, has to be found. |
| time-10 | `stored-walks` | Regular walks repeat weekly, and how they get in is not settled. |
| time-11 | `walk-date` | Two walks can have the same date. |
| time-12 | `walk-date` | Sheets are handed in at month end, after the walks happened. |
| text-01 | `client-name` | Two forms of a name may or may not be the same client. |
| text-02 | `chosen-client` | Finding a client may depend on letter case. |
| text-03 | `client-name` | Unseen characters could make one client look like two. |
| text-04 | `chosen-client` | The owner may search for a client. |
| text-05 | `client-name` | A long name may be cut when shown. |
| text-06 | `chosen-client` | Clients may be offered as a list. |
| text-07, text-08, text-11 | dropped | The slice's only reader is "the owner", and no criterion stores an ordered result or splits text into words. |
| text-09 | `client-name` | The documents do not say which writing directions names use. |
| text-10 | `client-name` | The owner must tell similar client names apart. |
| text-12 | `invoice-view` | The documents do not say that only one language is shown. |
| presentation-01 | `walk-date` | Walk dates may be shown on the invoice. |
| presentation-02 | `invoice-view` | It shows prices and a total. |
| presentation-03 | `price` | The documents name no currency. |
| presentation-04 | `refusal-message`; `invoice-view` | Wording may count walks: none, one or several. |
| presentation-05 | `price` | A half-price rule follows in slice 2, and amounts and totals are shown now. |
| presentation-06 | `invoice-view` | It shows digits, and the documents do not settle their shapes. |
| presentation-07, presentation-08 | dropped | No criterion shows a time of day, a week or rest days. |
| presentation-09 | `walk-date` | The documents do not name a calendar. |
| presentation-10 | `chosen-client` | Clients may be listed by name. |
| presentation-11 | `invoice-view` | Its walks may be ordered by a column. |
| presentation-12 | `invoice-view` | A month's walks may not fit one screen. |
| corpus: all | dropped | No criterion ships or updates a body of content; the prices are the business's own data. |
| secrets: all | dropped | The slice needs nothing from outside, and no criterion has the product use a credential of its own; signing in is asked about under sign-in. |
| authorization-01 | `invoice-request` | It reveals client details, and who may see invoices is open. |
| authorization-02 | `chosen-client` | The request names one client's records. |
| authorization-03 | `invoice-request` | A request might not come through the screen. |
| authorization-04 | `invoice-request` | No document says what others, such as walkers, may do. |
| authorization-05, authorization-09 | dropped | No criterion changes anyone's role or stores a file. |
| authorization-06 | `invoice-request` | The documents do not rule out a request sent by someone else's page. |
| authorization-07 | `invoice-request` | If asking keeps an invoice, opening a link could change something. |
| authorization-08 | `invoice-request` | A permission check may not complete. |
| authorization-10 | `invoice-request` | The request may carry claims about who is asking. |
| authorization-11 | `invoice-view` | Client details may stay visible after access ends. |
| authorization-12 | `invoice-request` | The documents do not say how the owner's account is chosen. |
| configuration: all | dropped | No criterion reads or changes a setting. |
| logging-01 | `invoice-request` | Someone may need to know an invoice was asked for or failed. |
| logging-02 | `invoice-request` | A record of it must say enough to explain a wrong invoice. |
| logging-03 | `client-name` | Client details could end up in records. |
| logging-04 | `client-name` | A stored name could be written into a record. |
| logging-05 | `invoice-request` | Writing its record can fail. |
| logging-06 | `invoice-request` | Records of requests grow. |
| logging-07 | `refusal-message` | The owner is told of failures such as a missing price. |
| logging-08 | `invoice-request` | Where its records would live is not said. |
| logging-09 | `invoice-request` | A failure may need someone to be told. |
| logging-10 | `invoice-request` | Its records could be changed or removed. |
| logging-11 | `invoice-request` | Its records would carry times. |
| logging-12 | `invoice-request` | Records that mention clients have no stated lifetime. |
| accessibility-01 | `invoice-request` | The owner asks through the product. |
| accessibility-02 | `invoice-view` | A keyboard user may enter it. |
| accessibility-03 | `invoice-request` | Its controls can take focus. |
| accessibility-04, accessibility-12 | dropped | No criterion closes or removes a focused item or shows movement. |
| accessibility-05 | `invoice-request` | Its controls need names. |
| accessibility-06 | `invoice-view` | It may show things that are not text. |
| accessibility-07 | `refusal-message`; `no-walks-message` | The result may be a refusal that has to be learned without sight. |
| accessibility-08 | `invoice-view` | It may mark regular and one-off walks. |
| accessibility-09 | `invoice-view` | It has text to read. |
| accessibility-10 | `invoice-view` | Walks and amounts must survive enlarged text. |
| accessibility-11 | `invoice-request` | A signed-in period could limit the time to ask. |
| sign-in-01 | `invoice-request` | It reveals client details, and no document rules out sign-in or a public address. |
| sign-in-02 | `invoice-request` | An account that exists beforehand could ask for invoices. |
| sign-in-03 | `invoice-request` | Whether others can learn of the owner's account is not settled. |
| sign-in-04 | `invoice-request` | An owner who cannot sign in cannot invoice. |
| sign-in-05 | `invoice-request` | The owner's first way in is not said. |
| sign-in-06 | `invoice-request` | There may be more than one way in. |
| sign-in-07 | `invoice-request` | Someone else's sign-in would expose invoices. |
| sign-in-08 | `invoice-request` | How long access to invoices lasts is not said. |
| sign-in-09 | `invoice-request` | The owner may be signed in more than once. |
| sign-in-10 | `invoice-request` | A session held before sign-in must not gain access to invoices. |
| sign-in-11 | dropped | No criterion changes sign-in details or does a grave operation. |
| sign-in-12 | `invoice-request` | A lost device may still be able to see invoices. |
| stored-data-01 | `invoice` | An invoice ties a client to walk dates and amounts. |
| stored-data-02 | `invoice` | Kept invoices and their copies can be read where they lie. |
| stored-data-03 | `invoice` | Protecting kept invoices may need keys. |
| stored-data-04 | `invoice` | A lost key would affect protected invoices. |
| stored-data-05 | `chosen-client` | The client could travel in an address. |
| stored-data-06 | `invoice-view` | Components in between may keep what is shown. |
| stored-data-07 | `invoice` | Where the product keeps data, and who else receives it, is not said. |
| stored-data-08 | `invoice-view` | Only what the owner needs should be sent. |
| stored-data-09 | `invoice` | No document says how long invoices are kept. |
| stored-data-10 | `invoice-view` | The owner's device may keep what is shown. |
| stored-data-11 | dropped | No criterion takes a file. |
| stored-data-12 | `invoice-view` | It is a reading of sensitive data. |
| file-intake: all | dropped | No criterion takes a file; bringing prices or other information in is still a blocker. |
| misuse-01 | `invoice-request` | An invoice can be asked for before walks or prices are in. |
| misuse-02 | `invoice-request` | The month and missing-price rules have to be enforced somewhere. |
| misuse-03 | `invoice-request` | A script could ask for every client's invoice. |
| misuse-04 | `invoice-request` | Very fast requests could be someone collecting client details. |
| misuse-05, misuse-06, misuse-08 | dropped | No criterion has a grave or costly operation or anything in limited supply. |
| misuse-07 | `invoice-request` | A request could carry a price or total the owner is not meant to set. |
