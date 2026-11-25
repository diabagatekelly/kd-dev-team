# Kept: slice 1

## What the slice creates and keeps
- walk: walker-walk-entry / 1
- client: walker-walk-entry / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `walk-client` | other | the walker entering a walk | client-details | walker-walk-entry / 1 |
| `walk-day` | date | the walker entering a walk | no | walker-walk-entry / 1 |
| `walk-length` | number | the walker entering a walk | no | walker-walk-entry / 1 |
| `walker-identity` | identifier | whatever tells the product which walker is using the phone | no | walker-walk-entry / 1 |
| `client-name` | text | read back from the stored client | client-details | walker-walk-entry / 1 |
| `stored-walk-client` | other | read back from the stored walk | client-details | walker-walk-entry / 1 |
| `stored-walk-day` | date | read back from the stored walk | no | walker-walk-entry / 1 |
| `stored-walk-length` | number | read back from the stored walk | no | walker-walk-entry / 1 |

## Other things the slice has
- `entry-screen`: where a walker enters a walk on their phone (walker-walk-entry / 1)
- `walks-list`: where a walker is shown their walks (walker-walk-entry / 1)
- `save-request`: a walker's entry on its way to being kept (walker-walk-entry / 1)
- `client-needed-message`: what tells the walker a client is needed (walker-walk-entry / 2)
- `walker-access`: how the product knows whose walks are whose (walker-walk-entry / 1)
- `installation`: the running product that holds the walks (walker-walk-entry / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The slice needs nothing from outside the product. |
| receive-external-data: all | dropped | The slice receives nothing from an outside system. |
| sync-01, sync-06, sync-07, sync-10 | dropped | The slice only adds walks: it changes and removes nothing, so no differing changes, removals or changes underneath a person arise. |
| sync-02 | `save-request` | An entry made on a phone could be discarded before it is kept. |
| sync-03 | `save-request` | An entry that seemed saved on the phone could later not be accepted. |
| sync-04 | `walks-list` | The walker reads their walks on a phone, and what is shown may be old or not there yet. |
| sync-05 | `save-request` | The documents do not say whether a phone holds entries not yet sent. |
| sync-08 | `walks-list` | The list on a phone may hold only some of the walker's walks. |
| sync-09 | `walk` | A phone could run an older version while walks are saved by a newer one. |
| sync-11 | `walks-list` | A walker's record of walks may be wanted when the product cannot be reached for good. |
| sync-12 | `walks-list` | Walks are fetched to be shown on a walker's phone. |
| limits-01, limits-02, limits-09 | dropped | The slice uses no outside system or paid service. |
| limits-05, limits-10, limits-12 | dropped | The slice has one feature, no scheduled work and no work beyond saving an entry and showing walks. |
| limits-03 | `walk` | One walker could enter any number of walks. |
| limits-04 | `installation` | Four walkers and about sixty clients enter into it, and that is expected to roughly double. |
| limits-06 | `entry-screen` | A walker stopped by any limit while entering needs to know what to do. |
| limits-07 | `save-request` | An entry arrives with values whose size has to be bounded. |
| limits-08 | `walks-list` | A walker's walks build up past what one screen holds. |
| limits-11 | `save-request` | Entries may wait to be kept. |
| durable-write-06 | dropped | The slice only adds walks and replaces no saved data. |
| durable-write-01 | `walk` | Saving a walk could be cut off partway. |
| durable-write-02 | `walk` | The walker takes a listed walk as saved, and invoices will rest on it. |
| durable-write-03 | `installation` | Walks must survive a loss of power where they are stored. |
| durable-write-04 | `save-request` | Saving a walk could fail for lack of space. |
| durable-write-05 | `save-request` | Storage could report that saving a walk failed. |
| durable-write-07 | `walk` | Walks are a record added to over time, and the last one could be incomplete. |
| durable-write-08 | `walk`; `client` | Each walk names a client, so the two must agree. |
| durable-write-09 | `walk` | A walk silently changed would later be billed wrongly. |
| durable-write-10 | `installation` | A copy of the walks could be taken while one is being saved. |
| durable-write-11 | `installation` | Walks and clients together are the saved data. |
| durable-write-12 | `save-request` | A walker could close the product while a walk is saving. |
| startup-read-01 | `installation` | Saved walks or clients could be damaged at start. |
| startup-read-02 | `installation` | The product starts against a place where walks are saved. |
| startup-read-03 | `installation` | Having no walks yet must not be confused with failing to open them. |
| startup-read-04 | `walk` | An earlier run could leave a walk half saved. |
| startup-read-05 | `installation` | Saved walks could be readable but not writable. |
| startup-read-06 | `installation` | The documents do not say that only one copy of the product runs. |
| startup-read-07 | `installation` | The documents do not say where walks are stored or whether a platform can remove them. |
| startup-read-08 | `walk` | Rescued walks would feed invoices. |
| startup-read-09 | `walk` | A walk can be readable and still wrong. |
| startup-read-10 | `installation` | Lost walks would need a spare copy, as lost paper sheets do today. |
| migration-02, migration-06, migration-07, migration-08, migration-09, migration-10, migration-11, migration-12 | dropped | This is the first slice: there is no earlier saved data, and it changes, renames and converts nothing. |
| migration-01 | `walk` | Walks saved by a later version could be met by this one. |
| migration-03 | `walk` | This version may be put back after a later one has saved walks. |
| migration-04 | `walk` | Walkers' phones may run different versions during an update. |
| migration-05 | `installation` | An older copy still open on a phone could stand in the way of a later update. |
| concurrency-01, concurrency-04, concurrency-07, concurrency-10, concurrency-11 | dropped | The slice only adds walks: it edits no item, decides nothing from a set, and gives nobody sole or time-limited use. |
| concurrency-02 | `walk` | A walk must name a client while other operations happen. |
| concurrency-03 | `walks-list` | The list reads walks together with their clients while walks are being added. |
| concurrency-05 | `walks-list` | A walk could be listed before it is finally saved. |
| concurrency-06 | `walks-list` | A walker expects a confirmed walk to show on the phone. |
| concurrency-08 | `save-request` | Several walkers may save at once. |
| concurrency-09 | `save-request` | A save could be cancelled because it clashed with another. |
| concurrency-12 | `installation` | The documents do not say that only one copy of the product changes the data. |
| lifecycle-01, lifecycle-02, lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11, lifecycle-12 | dropped | The slice makes a walk in one step, holds nothing for a time, and undoes and removes nothing. |
| lifecycle-03 | `walk` | The slice gives no way to take back an entered walk. |
| lifecycle-04 | `save-request` | An entry could stay in progress without being kept. |
| lifecycle-05 | `walk` | A walk makes sense only with its client and its walker. |
| lifecycle-08 | `entry-screen` | A walker could start an entry and leave it. |
| user-input-01 | `entry-screen` | The walker gives values, and any typed one needs a length. |
| user-input-02 | `entry-screen` | A client is required, and the day and length are given with it. |
| user-input-03 | `entry-screen` | Anything the walker types may hold any character. |
| user-input-04 | `walk-client` | A client's name may be given whole or in parts. |
| user-input-05 | `save-request` | The client rule could be bypassed by an entry that skips the screen. |
| user-input-06 | `client-needed-message` | An entry without a client is refused with a message. |
| user-input-07 | `entry-screen` | A value could be left empty or filled with spaces. |
| user-input-08 | `walk-length` | The length is a number with edges. |
| user-input-09 | `walk-client` | The walker has to mean one particular client. |
| user-input-10 | `entry-screen` | What the walker gives is stored and shown again. |
| user-input-11 | `entry-screen` | Client, day, length and walker may not agree with one another. |
| user-input-12 | `walk-day`; `walk-length` | A day and a length can be written in several forms. |
| user-action-01 | `save-request` | A walker on a phone could send an entry again before it finishes. |
| user-action-02 | `walks-list` | The list follows a save and may be reloaded. |
| user-action-03 | `entry-screen` | A walker can step back to the entry after saving. |
| user-action-04 | `walks-list` | The list shows client details that must not stay visible to others. |
| user-action-05 | `entry-screen` | A walker can leave with an unsaved entry. |
| user-action-06 | `entry-screen` | A phone may discard the screen while the walker is away from it. |
| user-action-07 | `walks-list` | A walker could have the product open more than once. |
| user-action-08 | `walk` | The slice gives the walker no way to undo an entry. |
| user-action-09 | `entry-screen` | A wrong entry cannot be put right by the walker, so confirming may matter. |
| user-action-10 | `entry-screen` | A walker can back out partway through an entry. |
| user-action-11 | `entry-screen` | Access could end while a walker is entering. |
| user-action-12 | `walks-list` | A phone can keep an address to the walks. |
| long-operation-03, long-operation-04, long-operation-05, long-operation-08, long-operation-10, long-operation-11, long-operation-12 | dropped | The only operation saves a single walk: it has no parts, separate result or lengthy run to stop, queue or check in advance. |
| long-operation-01 | `save-request` | Saving from a phone can take more than a few seconds. |
| long-operation-02 | `save-request` | A walker needs to know a slow save from a stopped one. |
| long-operation-06 | `save-request` | A lost phone signal could interrupt a save. |
| long-operation-07 | `save-request` | A save could fail after the walker has moved on. |
| long-operation-09 | `save-request` | A save could make no progress. |
| time-04, time-05, time-06, time-09, time-10 | dropped | The walker gives a day and a length: the slice measures no span, takes no clock time, schedules nothing and counts no months. |
| time-01 | `walk-day` | The phone's clock may shape which day is offered or accepted. |
| time-02 | `walk-day` | The phone and the product may disagree on what day it is. |
| time-03 | `walks-list` | A changed clock could disturb the order of walks. |
| time-07 | `walk-day` | The day is a plain date that must not shift. |
| time-08 | `walk-day` | Some time zone decides which day a walk fell on. |
| time-11 | `walks-list` | Two walks on one day need an order. |
| time-12 | `walk` | A walk has a day it happened and may be entered later. |
| text-08, text-11 | dropped | The slice stores no result that depends on text order and does nothing that depends on where words begin. |
| text-01 | `client-name` | Client names may need comparing. |
| text-02 | `client-name` | Capital letters may differ in a client's name. |
| text-03 | `client-name` | A name may carry unseen characters. |
| text-04 | `client-name` | A walker may look for a client by name. |
| text-05 | `client-name` | A long name may be cut on a phone. |
| text-06 | `client-name` | Clients may be offered as a list. |
| text-07 | `client-name` | A list of clients needs some language's order. |
| text-09 | `client-name` | The name is shown in a row with other values. |
| text-10 | `client-name` | A walker must pick the right client among similar names. |
| text-12 | `client-needed-message` | The message has to fit a phone screen. |
| presentation-07 | dropped | The slice shows a day and a length, no time of day. |
| presentation-01 | `walks-list` | Each walk's day is shown. |
| presentation-02 | `stored-walk-length` | The length is shown as a number. |
| presentation-03 | `stored-walk-length` | The length needs its unit. |
| presentation-04 | `walks-list` | The list may word a count of walks, including none. |
| presentation-05 | `stored-walk-length` | A length could have a part of a unit. |
| presentation-06 | `walks-list` | Days and lengths are shown in digits. |
| presentation-08 | `entry-screen` | Choosing a day may show a week. |
| presentation-09 | `walks-list` | Days are shown in some calendar. |
| presentation-10 | `client-name` | Clients may be listed by name. |
| presentation-11 | `walks-list` | The list could be ordered by day, client or length. |
| presentation-12 | `walks-list` | A long list of walks needs one order throughout. |
| corpus: all | dropped | The slice ships and uses no body of content. |
| secrets-01 | `walker-access` | Telling walkers apart may rest on a credential. |
| secrets-02 | `walker-access` | Each walker may need their own credential. |
| secrets-03 | `walker-access` | A credential could end up in what the product records. |
| secrets-04 | `walker-access` | A credential may need replacing. |
| secrets-05 | `walker-access` | A walker's phone could be lost with access on it. |
| secrets-06 | `walker-access` | A walker's access could stop being accepted. |
| secrets-07 | `installation` | Anything the product uses to reach its data could allow too much. |
| secrets-08 | `walker-access` | The documents do not say whether walkers share any access. |
| secrets-09 | `walker-access` | Access from a phone is stored and sent. |
| secrets-10 | `installation` | The running product may need a credential to reach its data. |
| secrets-11 | `installation` | The place such credentials are kept could be lost. |
| secrets-12 | `walker-access` | Use of access bears on who saw client details. |
| authorization-09 | dropped | The slice stores no file. |
| authorization-01 | `walk`; `client` | Only certain people may see client details and enter walks. |
| authorization-02 | `walks-list` | A walker is shown their own walks. |
| authorization-03 | `save-request` | An entry could be sent without the screen. |
| authorization-04 | `installation` | Someone no rule mentions could ask for walks or clients. |
| authorization-05 | `walker-access` | A walker can leave, or stop walking a client. |
| authorization-06 | `save-request` | An entry could be sent in a walker's name by another page. |
| authorization-07 | `save-request` | Entering a walk changes what is kept. |
| authorization-08 | `save-request` | The check on who is entering could fail to complete. |
| authorization-10 | `walker-identity` | Which walker is entering reaches the product from a phone. |
| authorization-11 | `walker-access` | A walker who loses access may still have the walks open. |
| authorization-12 | `walker-access` | A walk entered under the wrong walker would be theirs in the record. |
| configuration-01 | `installation` | The product may start with a setting missing. |
| configuration-02 | `installation` | A setting could hold a senseless value. |
| configuration-03 | `installation` | A trial and a real installation may differ in values. |
| configuration-04 | `installation` | Whoever maintains it needs to see its settings. |
| configuration-05 | `installation` | Defaults decide whether it is safe as first set up. |
| configuration-06 | `installation` | A fresh installation may switch on more than entry needs. |
| configuration-07 | `installation` | A trial must not stand in wrongly for the real one. |
| configuration-08 | `installation` | A changed setting could affect all walkers. |
| configuration-09 | `installation` | A bad setting has to be put back. |
| configuration-10 | `installation` | The documents do not say who owns any setting. |
| configuration-11 | `installation` | A diagnostic mode could expose client details. |
| configuration-12 | `installation` | The documents do not say who may change settings. |
| logging-01 | `walk` | Disputes about walks may need a record of entry. |
| logging-02 | `walk` | A record must show who entered what. |
| logging-03 | `client-name` | Client details could enter the records. |
| logging-04 | `walk-client` | Anything a walker types could be recorded. |
| logging-05 | `installation` | A record could fail to be written. |
| logging-06 | `installation` | Records grow with use. |
| logging-07 | `save-request` | A failed save shows the walker something and records something. |
| logging-08 | `installation` | Records could be lost with their machine. |
| logging-09 | `installation` | The documents do not say who reads records. |
| logging-10 | `installation` | Records about walks could be altered. |
| logging-11 | `installation` | Phones and the product may record from different clocks. |
| logging-12 | `installation` | Records about walkers and clients need an end. |
| accessibility-01 | `entry-screen` | A walker may use a keyboard with their phone. |
| accessibility-02 | `entry-screen` | A keyboard user could get stuck in a chooser. |
| accessibility-03 | `entry-screen` | A keyboard user needs to see where they are. |
| accessibility-04 | `entry-screen` | A chooser or message may close while holding focus. |
| accessibility-05 | `entry-screen` | Each control must be usable without sight. |
| accessibility-06 | `walks-list` | The list may show something that is not text. |
| accessibility-07 | `entry-screen` | A walker must learn whether the walk was entered. |
| accessibility-08 | `client-needed-message` | A refusal may be marked by colour. |
| accessibility-09 | `entry-screen`; `walks-list` | Both screens are read on a phone, possibly outdoors. |
| accessibility-10 | `entry-screen`; `walks-list` | A walker may enlarge text on their phone. |
| accessibility-11 | `entry-screen` | Entry could have a time limit. |
| accessibility-12 | `entry-screen` | The screen may use motion. |
| sign-in-01 | `walker-access` | Someone could guess their way to a walker's walks. |
| sign-in-02 | `walker-access` | An account could exist before any walker has one. |
| sign-in-03 | `walker-access` | The documents do not say whether account existence matters. |
| sign-in-04 | `walker-access` | A walker could lose what they sign in with. |
| sign-in-05 | `walker-access` | A new or holiday cover walker needs first access. |
| sign-in-06 | `walker-access` | There may be more than one way in. |
| sign-in-07 | `walker-access` | A walker's access could be changed by someone else. |
| sign-in-08 | `walker-access` | Access on a phone may stay open. |
| sign-in-09 | `walker-access` | A walker may use more than one phone. |
| sign-in-10 | `walker-access` | A session from before sign-in could be reused. |
| sign-in-11 | `walker-access` | Some operation may need proof again. |
| sign-in-12 | `walker-access` | A lost phone's session needs ending. |
| stored-data-11 | dropped | The slice takes in no file. |
| stored-data-01 | `walk`; `client` | Client details are protected, and walks drive what is billed. |
| stored-data-02 | `client` | Client details exist where stored and in copies. |
| stored-data-03 | `installation` | Any protection by keys covers the stored data. |
| stored-data-04 | `installation` | Such a key could be lost or exposed. |
| stored-data-05 | `walk-client` | A chosen client could travel in an address. |
| stored-data-06 | `walks-list` | Replies carrying client details could be kept on the way. |
| stored-data-07 | `installation` | The documents do not say what other parties receive its data. |
| stored-data-08 | `walks-list` | Client information sent to a walker's phone could include more than needed, such as an address or door code. |
| stored-data-09 | `walk`; `client` | The documents give no end to how long these are kept. |
| stored-data-10 | `walks-list` | A phone may keep client details. |
| stored-data-12 | `client` | The limit on who sees client details raises whether reading is recorded. |
| file-intake: all | dropped | The slice takes in and stores no file from a person. |
| misuse-01, misuse-08 | dropped | Entry is a single step, and nothing in the slice is in limited supply. |
| misuse-02 | `walk` | The rules for a walk need to hold wherever it is entered. |
| misuse-03 | `save-request` | A script could send entries over and over. |
| misuse-04 | `save-request` | Many walks entered at once could be a sign of abuse. |
| misuse-05 | `walk` | Walks drive what clients pay, and the documents do not say whether any entry needs agreement. |
| misuse-06 | `walks-list` | Repeated fetching of a long list could crowd out others. |
| misuse-07 | `save-request` | An entry could carry fields the walker is not meant to set, such as another walker. |
