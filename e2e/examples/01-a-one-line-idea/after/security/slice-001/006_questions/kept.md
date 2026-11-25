# Kept: slice 1

## What the slice creates and keeps
- waiting-list: carry-over-list / 1
- person-s-place-on-the-list: carry-over-list / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `person-name` | text | the person who keeps the list, from the notebook | waiting-person-details | carry-over-list / 1 |
| `notebook-order` | list | the person who keeps the list, from the notebook | waiting-person-details | carry-over-list / 1 |
| `stored-list` | list | read back from where the list is kept | waiting-person-details | carry-over-list / 1 |

## Other things the slice has
- `carry-over`: the action of carrying the notebook over (carry-over-list / 1)
- `shown-list`: the waiting list as shown to the person who keeps it (carry-over-list / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The slice document says it needs nothing from outside. |
| receive-external-data: all | dropped | The slice document says it needs nothing from outside, so no outside data arrives. |
| sync-04 | `shown-list` | The shown list can fall behind later changes recorded in the notebook. |
| sync-01, sync-02, sync-03, sync-05, sync-06, sync-07, sync-08, sync-10, sync-11, sync-12 | dropped | The slice carries the notebook over and updates no copy from a source afterwards; later changes are left for slice 3. |
| sync-09 | dropped | This is the first slice, so no older version of the product shares the data. |
| limits-04 | waiting-list | The list holds everyone waiting, and the documents give only an approximate present count. |
| limits-07 | `person-name` | Each name carried over is an item the product accepts. |
| limits-08 | `shown-list` | The whole carried-over list is shown to be checked. |
| limits-09 | waiting-list | Keeping the list may use a paid service, and spending is limited. |
| limits-01, limits-02 | dropped | The slice needs nothing from outside that could refuse it for asking too often. |
| limits-03, limits-05, limits-06, limits-10, limits-11, limits-12 | dropped | The slice adds no usage quota, scheduled work or queue; its one action is carrying over one list. |
| durable-write-01 | `carry-over` | A save may be cut off while the notebook is being carried over. |
| durable-write-02 | `carry-over` | The person must know which part of what they carried over is saved. |
| durable-write-03 | waiting-list | The carried-over list has to survive where it is kept. |
| durable-write-04 | `carry-over` | Saving the list may fail for lack of space. |
| durable-write-05 | `carry-over` | Storage may report that saving the list failed. |
| durable-write-08 | waiting-list | The people on the list and their order must agree. |
| durable-write-09 | waiting-list | A silent change to the list would alter who is where. |
| durable-write-10 | waiting-list | A copy of the list may be taken while it is being saved. |
| durable-write-11 | waiting-list | The saved list may be moved or restored in part. |
| durable-write-12 | `carry-over` | The product may be closed while carried-over entries are being saved. |
| durable-write-06, durable-write-07 | dropped | The slice replaces no saved list wholesale and keeps no history that is added to. |
| startup-read-01 | waiting-list | The saved list may be damaged when next opened. |
| startup-read-02 | waiting-list | The place where the list is kept may hold something else. |
| startup-read-03 | waiting-list | An empty list must be told apart from one that cannot be opened. |
| startup-read-04 | `carry-over` | A carry-over may have been left unfinished. |
| startup-read-05 | waiting-list | The list may be readable but not changeable. |
| startup-read-07 | waiting-list | Wherever the list is kept, it may be removed without the person asking. |
| startup-read-08 | waiting-list | A rescued list could be missing people or have a changed order. |
| startup-read-09 | waiting-list | A readable list could be in the wrong order. |
| startup-read-10 | waiting-list | If the saved list is unusable, a spare copy decides what can be recovered. |
| startup-read-06 | dropped | The slice adds no repair of saved data by running copies. |
| migration-01 | waiting-list | The slice creates saved data that a different version may later meet. |
| migration-03 | waiting-list | A later version may save to this list and then be put back. |
| migration-02, migration-04, migration-05, migration-06, migration-07, migration-08, migration-09, migration-10, migration-11, migration-12 | dropped | This is the first saved data; the slice changes no stored format, name or meaning and updates nothing. |
| concurrency-01 | waiting-list | The documents do not rule out two changes made to the list from different views while carrying over. |
| concurrency-12 | waiting-list | The documents do not rule out two copies of the product writing the list. |
| concurrency-02, concurrency-03, concurrency-04, concurrency-05, concurrency-06, concurrency-07, concurrency-08, concurrency-09, concurrency-10, concurrency-11 | dropped | The slice has one action by the person who keeps the list, decides nothing from it, and adds no locks, holds or second viewer. |
| lifecycle-01 | `carry-over` | Carrying over several people may fail after some are in. |
| lifecycle-03 | `carry-over` | Carrying over may include a step that cannot be taken back. |
| lifecycle-04 | `carry-over` | A carry-over may stay unfinished. |
| lifecycle-05 | person-s-place-on-the-list | A place only makes sense as part of the list. |
| lifecycle-08 | `carry-over` | A carry-over may be started and abandoned. |
| lifecycle-11 | `person-name` | Names are kept, and the documents do not say what happens when the list is ended. |
| lifecycle-02, lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-12 | dropped | The slice adds no undoing, removal or time-limited hold. |
| user-input-01 | `person-name` | A name may be longer than what is accepted. |
| user-input-02 | `person-name` | A notebook entry may lack something the product asks for. |
| user-input-03 | `person-name` | Names contain varied characters. |
| user-input-04 | `person-name` | Names have differing parts and order. |
| user-input-05 | `carry-over` | Any rule on carried-over values must be enforced somewhere. |
| user-input-06 | `carry-over` | If a value is refused during carrying over, the person must be told. |
| user-input-07 | `person-name` | A blank name or extra spaces may be given. |
| user-input-09 | `person-name` | Two entries may have the same name, and the criterion counts each person once. |
| user-input-10 | `person-name` | Typed names are stored and shown. |
| user-input-11 | `notebook-order` | The people given and their order must agree. |
| user-input-08, user-input-12 | dropped | The slice takes in no typed number or date. |
| user-action-01 | `carry-over` | The person may start carrying over twice. |
| user-action-02 | `shown-list` | The shown list may be reloaded after carrying over. |
| user-action-03 | `shown-list` | The person may step back after carrying over. |
| user-action-05 | `carry-over` | The person may leave partway with entries unsaved. |
| user-action-06 | `carry-over` | The device may discard the work while the person reads the notebook. |
| user-action-07 | `carry-over` | The person may have the list open twice. |
| user-action-08 | `carry-over` | A mistake made while carrying over may need undoing. |
| user-action-09 | `carry-over` | Finishing or repeating the carry-over may call for confirmation. |
| user-action-10 | `carry-over` | The person may stop partway. |
| user-action-04 | `shown-list` | Names must not be shown to everyone, including whoever uses the device next. |
| user-action-11 | `carry-over` | Access may end while the person is carrying over, if access is limited. |
| user-action-12 | `shown-list` | A saved address to the list could be opened by someone else. |
| long-operation-04 | `carry-over` | Carrying over may stop partway. |
| long-operation-06 | `carry-over` | After an interruption the person needs to know where carrying over stands. |
| long-operation-08 | `carry-over` | Some entries may get in while others do not. |
| long-operation-01, long-operation-02, long-operation-03, long-operation-05, long-operation-07, long-operation-09, long-operation-10, long-operation-11, long-operation-12 | dropped | The documents give the slice no work that the product runs on its own while the person waits or goes elsewhere. |
| time: all | dropped | The criterion takes in, compares and shows no date or time; order comes from the notebook. |
| text-01 | `person-name` | Names may need to be told the same or different to count each person once. |
| text-02 | `person-name` | Names may differ only in capital letters. |
| text-03 | `person-name` | Names may carry unseen characters or unusual spaces. |
| text-05 | `person-name` | A long name may be cut. |
| text-09 | `shown-list` | Names in any writing direction are shown in rows. |
| text-10 | `shown-list` | The person must tell similar names apart when checking the list. |
| text-04, text-06, text-07, text-08, text-11, text-12 | dropped | The slice has no search, ordering by text, word splitting or second interface language. |
| presentation-04 | `shown-list` | The shown list may state how many people are on it, including none. |
| presentation-12 | `shown-list` | The notebook's order must hold across the whole shown list. |
| presentation-01, presentation-02, presentation-03, presentation-05, presentation-06, presentation-07, presentation-08, presentation-09, presentation-10, presentation-11 | dropped | The slice shows no date, time or amount and offers no reordering; the order is the notebook's. |
| corpus: all | dropped | The slice ships no body of content; the only content is what the person carries over. |
| secrets-01 | `shown-list` | Keeping names from everyone may need a credential, which has to be kept somewhere. |
| secrets-02 | `shown-list` | Any credential for seeing the list has to be set for someone. |
| secrets-03 | `shown-list` | Any such credential could end up in what the product records. |
| secrets-05 | `shown-list` | An exposed credential would expose the names. |
| secrets-06 | `shown-list` | The person could be refused with a credential that stopped working. |
| secrets-09 | `shown-list` | Any such credential is stored and sent in some form. |
| secrets-11 | `shown-list` | Losing any such credential could leave the list out of reach. |
| secrets-04, secrets-07, secrets-08, secrets-10, secrets-12 | dropped | The slice names no outside system and no credential held by the product for one, to rotate, narrow, share, deliver or audit. |
| authorization-01 | waiting-list | Names must not be shown to everyone, so who may carry over and see the list matters. |
| authorization-02 | `shown-list` | The list shown must be one the person asking may see. |
| authorization-03 | `shown-list` | A request for the list might bypass what is on screen. |
| authorization-04 | waiting-list | The documents leave open who else may see the list. |
| authorization-05 | waiting-list | Who keeps the list may change. |
| authorization-06 | `carry-over` | Another page could try to change the list in the person's name. |
| authorization-07 | `carry-over` | Carrying over changes the list. |
| authorization-08 | `shown-list` | A permission check may fail to complete. |
| authorization-10 | `shown-list` | Who is asking decides whether names may be shown. |
| authorization-11 | `shown-list` | Names already open may remain after access ends. |
| authorization-12 | `shown-list` | The person must be using the account they meant to, if there are accounts. |
| authorization-09 | dropped | The slice stores no file that is fetched. |
| configuration: all | dropped | The slice documents add no setting. |
| logging-01 | `carry-over` | A dispute about order may turn on what happened when the list was carried over. |
| logging-02 | `carry-over` | A record of carrying over has to say what happened. |
| logging-03 | `person-name` | Names could end up in records. |
| logging-07 | `carry-over` | A failed carry-over has to tell the person something. |
| logging-12 | `person-name` | Records that concern waiting people may be kept too long. |
| logging-04, logging-05, logging-06, logging-08, logging-09, logging-10, logging-11 | dropped | The slice documents add no record kept by the product beyond the list; whether carrying over leaves one is asked under the kept logging entries. |
| accessibility-01 | `carry-over` | The person may need to carry over by keyboard. |
| accessibility-02 | `carry-over` | A keyboard user must be able to leave each part used for carrying over. |
| accessibility-03 | `carry-over` | A keyboard user must see where they are while carrying over. |
| accessibility-04 | `carry-over` | The focused item may close as entries are carried over. |
| accessibility-05 | `carry-over` | The controls for carrying over need names. |
| accessibility-06 | `shown-list` | The shown list may use something other than text. |
| accessibility-07 | `carry-over` | Someone who cannot see the screen must learn the result. |
| accessibility-08 | `shown-list` | Colour may be used to mark something on the list. |
| accessibility-09 | `shown-list` | The person must be able to read the list to check it. |
| accessibility-10 | `shown-list` | The person may enlarge text to check the list. |
| accessibility-11 | `carry-over` | Carrying over from paper takes time, so any time limit matters. |
| accessibility-12 | `shown-list` | The screen showing the list may include movement. |
| sign-in-01 | `shown-list` | If a sign-in guards the names, it could be guessed. |
| sign-in-02 | `shown-list` | An account existing before sign-up could reach the names. |
| sign-in-03 | `shown-list` | Sign-in or recovery could reveal that a person is known to the product. |
| sign-in-04 | `shown-list` | The person could lose their way in to the list. |
| sign-in-05 | `shown-list` | A first way in has to reach the person who keeps the list. |
| sign-in-06 | `shown-list` | Every way in would reach the names. |
| sign-in-07 | `shown-list` | A changed way in could hand the list to someone else. |
| sign-in-08 | `shown-list` | A lasting session could leave the names open. |
| sign-in-09 | `shown-list` | The list may be opened in more than one session. |
| sign-in-10 | `shown-list` | An earlier session must not carry into access to the names. |
| sign-in-11 | `carry-over` | Changing the list may call for proof of identity again. |
| sign-in-12 | `shown-list` | A session left open may need to be ended. |
| stored-data-01 | waiting-list | The list holds names that are not to be shown to everyone. |
| stored-data-02 | waiting-list | Names exist wherever the list and its copies are kept. |
| stored-data-03 | waiting-list | Protecting the names may involve keys. |
| stored-data-04 | waiting-list | Losing such a key could lose the list. |
| stored-data-05 | `person-name` | A name could travel in an address. |
| stored-data-06 | `shown-list` | Something in between may keep a copy of the shown list. |
| stored-data-07 | waiting-list | Wherever the list is kept, another party may receive the names. |
| stored-data-08 | `shown-list` | What is sent to show the list could include more than needed. |
| stored-data-09 | waiting-list | The documents do not say how long people's details are kept. |
| stored-data-10 | `shown-list` | The device used may keep the names. |
| stored-data-12 | waiting-list | Whether reading the names is recorded affects what can be said about who saw them. |
| stored-data-11 | dropped | The slice takes in no file. |
| file-intake: all | dropped | The slice takes in names and their order, and no document speaks of a file. |
| misuse-02 | `carry-over` | Any rule on who is carried over and in what order must be enforced somewhere. |
| misuse-07 | `carry-over` | A request could set more than the names and their order. |
| misuse-03 | `carry-over` | The documents do not say the product cannot be reached by a script that repeats requests. |
| misuse-01, misuse-04, misuse-05, misuse-06, misuse-08 | dropped | The slice has one step, nothing in limited supply, no costly operation, and no document asks for a second person or treats speed as a sign. |
