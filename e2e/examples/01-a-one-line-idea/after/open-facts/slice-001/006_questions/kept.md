# Kept: slice 1

## What the slice creates and keeps
- waiting-list: bring-notebook-order-across / 1, bring-notebook-order-across / 2

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `person-name` | text | The list keeper, from the notebook | waiting-people | bring-notebook-order-across / 1 |
| `list-order` | list | The list keeper, from the notebook | waiting-people | bring-notebook-order-across / 1 |
| `stored-list` | list | The list as kept, read back when the list keeper returns | waiting-people | bring-notebook-order-across / 2 |

## Other things the slice has
- `bringing-across`: the list keeper's operation of bringing the notebook's list across (bring-notebook-order-across / 1)
- `shown-list`: the list as shown to the list keeper (bring-notebook-order-across / 1)
- `way-back-in`: how the list keeper comes back to the list, while names are not shown to everyone (bring-notebook-order-across / 2)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The slice document's "Needs from outside" says none, so the slice sends no request outside. |
| receive-external-data: all | dropped | The slice document's "Needs from outside" says none, so no data arrives from an outside system. |
| sync-01 | `waiting-list` | The notebook and the list brought across are two copies, and the notebook can still be changed. |
| sync-02 | `bringing-across` | If the list is brought across again, something brought across earlier could be dropped. |
| sync-03 | `bringing-across` | What the list keeper brought across has to be there later, so a late rejection would matter. |
| sync-04 | `shown-list` | The list shown may be older than the notebook, and before bringing across there is nothing to show. |
| sync-07 | `bringing-across` | The notebook may be changed while its list is being brought across. |
| sync-08 | `bringing-across` | Only part of the notebook's list may have come across. |
| sync-11 | `waiting-list` | The list keeper may need the list when the product holding it cannot be had. |
| sync-05, sync-06, sync-12 | dropped | The slice has no updating of the list from the notebook after it is brought across; changing it is left for later (slice document, "Left for later"). |
| sync-09 | dropped | This is the first slice and no slice is built, so there is no older version to share data with. |
| sync-10 | dropped | The slice has no way to change a list once brought across (slice document, "Left for later"); two windows are asked about under user-action-07. |
| limits-04 | `waiting-list` | The problem says about 40 people are waiting, and the list can hold some number of them. |
| limits-06 | `bringing-across` | A limit could stop the list keeper partway through the list. |
| limits-07 | `bringing-across` | A list or an entry could be larger than what is accepted. |
| limits-08 | `shown-list` | About 40 people may not be shown in one go. |
| limits-01, limits-02, limits-09 | dropped | The slice document's "Needs from outside" says none, so it uses no outside or paid outside service. |
| limits-03, limits-05 | dropped | Both need competing demand; in this slice only the list keeper acts, on one list of about 40 people. |
| limits-10, limits-11, limits-12 | dropped | The criteria have no scheduled work and no queue of waiting work. |
| durable-write-01 | `waiting-list` | A save of the list could be cut off with only some people stored. |
| durable-write-02 | `bringing-across` | The list keeper has to know when what was brought across is safely kept. |
| durable-write-03 | `waiting-list` | The list has to be there when the list keeper comes back. |
| durable-write-04 | `bringing-across` | Saving the list could fail for lack of space. |
| durable-write-05 | `bringing-across` | Storage could report that saving the list failed. |
| durable-write-06 | `waiting-list` | A stored list could be replaced if it were brought across again. |
| durable-write-08 | `waiting-list` | The names and their order must agree with each other. |
| durable-write-09 | `waiting-list` | A silent change to the stored order would move people ahead or back. |
| durable-write-10 | `waiting-list` | A copy of the list could be taken while it is being saved. |
| durable-write-11 | `waiting-list` | Whatever holds the list could be only partly moved or restored. |
| durable-write-12 | `bringing-across` | The list keeper could close the product while the list is being saved. |
| durable-write-07 | dropped | The criteria keep the list's order, not a history added to over time. |
| startup-read-01 | `waiting-list` | The kept list could be damaged when it is next opened. |
| startup-read-02 | `waiting-list` | Something else could be where the list is expected. |
| startup-read-03 | `waiting-list` | A list never brought across must not be confused with one that cannot be opened. |
| startup-read-04 | `waiting-list` | A save of the list could have been left unfinished. |
| startup-read-05 | `waiting-list` | The list could be readable but not changeable. |
| startup-read-06 | `waiting-list` | The documents do not say that only one copy of the product ever opens the list. |
| startup-read-07 | `waiting-list` | Where the list is kept is not decided, and it could be removed without the list keeper doing it. |
| startup-read-08 | `waiting-list` | A rescued list could have people missing or out of order. |
| startup-read-09 | `waiting-list` | A list that opens but is in the wrong order would put people in the wrong place. |
| startup-read-10 | `waiting-list` | A spare copy may be needed if the kept list is unusable. |
| migration: all | dropped | This is the first slice and none is built, so there is no data saved by an earlier version. |
| concurrency-01 | `waiting-list` | The list keeper could bring it across from two places, each seeing no list yet. |
| concurrency-02 | `waiting-list` | The order is a rule across all the people on the list. |
| concurrency-03 | `shown-list` | The people and their order must be read as they stood at one moment. |
| concurrency-05 | `bringing-across` | A list only partly brought across could be seen as if complete. |
| concurrency-06 | `shown-list` | Another window or device could show the list before it has caught up. |
| concurrency-08 | `bringing-across` | The stored list could be in use when it is being saved. |
| concurrency-09 | `bringing-across` | A second attempt that clashes with the first could be cancelled. |
| concurrency-12 | `waiting-list` | The documents do not say that two copies of the product can never change the list. |
| concurrency-04, concurrency-07, concurrency-10, concurrency-11 | dropped | The criteria make no decision from a matching set, grant no timed exclusive right, hold only one list, and have no operation that needs sole use against many readers. |
| lifecycle-01 | `bringing-across` | Bringing about 40 people across may take several steps, and a later one may fail. |
| lifecycle-02 | `bringing-across` | Clearing away a failed attempt could itself fail. |
| lifecycle-03 | `bringing-across` | The slice has no way to change the list once it is brought across. |
| lifecycle-04 | `bringing-across` | Bringing across could stay unfinished. |
| lifecycle-05 | `waiting-list` | A name without a place, or a place without a name, would make no sense. |
| lifecycle-08 | `bringing-across` | The list keeper could start bringing the list across and give up. |
| lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11 | dropped | The slice removes nothing from the list; taking people off it is left for later. |
| lifecycle-12 | dropped | The criteria hold nothing for a limited time. |
| user-input-01 | `person-name` | Each name is given by the list keeper and has some length. |
| user-input-02 | `bringing-across` | A notebook entry may lack something the product asks for. |
| user-input-03 | `person-name` | A name from the notebook may hold any characters. |
| user-input-04 | `person-name` | An entry's name may not fit a fixed set of parts. |
| user-input-05 | `bringing-across` | Any rule about what is brought across has to be enforced somewhere. |
| user-input-06 | `bringing-across` | The list keeper must understand why something was refused. |
| user-input-07 | `person-name` | A name could be given empty or with extra spaces. |
| user-input-09 | `person-name` | Two people waiting could have the same name. |
| user-input-10 | `person-name` | The name is stored and shown again. |
| user-input-08, user-input-12 | dropped | The criteria take in names and their order, with no typed number or date. |
| user-input-11 | dropped | The slice takes in only names and their order, and neither limits what the other may be. |
| user-action-01 | `bringing-across` | The list keeper could start it a second time before it has finished. |
| user-action-02 | `shown-list` | The list keeper could reload after bringing the list across. |
| user-action-03 | `shown-list` | The list keeper could step back after bringing the list across. |
| user-action-04 | `shown-list` | Names must not be left visible to others on the device. |
| user-action-05 | `bringing-across` | The list keeper could leave partway through the list. |
| user-action-06 | `bringing-across` | A device could discard the screen while the list is only partly given. |
| user-action-07 | `bringing-across` | The list keeper could have two windows open and act in both. |
| user-action-08 | `bringing-across` | The list keeper could bring across something wrong and want it back. |
| user-action-09 | `bringing-across` | With no later change in this slice, whether to confirm the list matters. |
| user-action-10 | `bringing-across` | The list keeper may back out partway. |
| user-action-11 | `way-back-in` | If the list keeper is signed in, that could end while the list is being brought across. |
| user-action-12 | `shown-list` | A saved address to the list could be opened by someone who may not see names. |
| long-operation-01 | `bringing-across` | Bringing about 40 people across may take more than a few seconds. |
| long-operation-02 | `bringing-across` | The list keeper must be able to tell a working attempt from a stopped one. |
| long-operation-03 | `bringing-across` | The list keeper may want to stop it. |
| long-operation-04 | `bringing-across` | Stopping could leave some people across and others not. |
| long-operation-05 | `bringing-across` | The list keeper may go elsewhere before it ends. |
| long-operation-06 | `bringing-across` | It could be interrupted partway through the list. |
| long-operation-07 | `bringing-across` | A failure could happen after the list keeper thinks it is done. |
| long-operation-08 | `bringing-across` | Some people could come across and others fail. |
| long-operation-09 | `bringing-across` | An attempt could stop making progress. |
| long-operation-10 | `waiting-list` | Its result is the kept list, which the list keeper comes back to. |
| long-operation-11 | `bringing-across` | A second attempt could be asked for while one is running. |
| long-operation-12 | `bringing-across` | An attempt sure to fail, with a list already across, could be accepted. |
| time: all | dropped | The criteria take in, keep and show no date, time or span. |
| text-01 | `person-name` | Showing those people and nobody else depends on telling names apart. |
| text-02 | `person-name` | Names may differ only in capital and small letters. |
| text-03 | `person-name` | A name could carry unseen characters or unusual spaces. |
| text-05 | `person-name` | A long name could be cut short. |
| text-09 | `shown-list` | A name in a row could disturb the place shown beside it. |
| text-10 | `shown-list` | The list keeper tells the people apart by eye when checking the order. |
| text-12 | `shown-list` | Names and labels need room in the list. |
| text-04, text-11 | dropped | The criteria have no search and nothing that depends on where words begin and end. |
| text-06, text-07, text-08 | dropped | The list's order is the notebook's, not one worked out from the text (bring-notebook-order-across / 1). |
| presentation-04 | `shown-list` | Wording could count the people on the list, including none or one. |
| presentation-12 | `shown-list` | The notebook's order must hold across the whole list if it takes more than one screen. |
| presentation-01, presentation-07, presentation-08, presentation-09 | dropped | The criteria show no date, time or calendar. |
| presentation-02, presentation-03, presentation-05, presentation-06 | dropped | The criteria show no amount or measured number, only people in order, and the problem says about 40 are waiting. |
| presentation-10, presentation-11 | dropped | The list is ordered only as in the notebook, not by name or by a chosen column. |
| corpus: all | dropped | The slice ships no body of content; its only content is the list the list keeper brings across. |
| secrets-01 | `way-back-in` | Keeping names from everyone may need a credential, which would be kept somewhere. |
| secrets-02 | `way-back-in` | Any such credential has to be set by someone. |
| secrets-05 | `way-back-in` | Any such credential could be exposed. |
| secrets-09 | `way-back-in` | Any such credential would be stored and sent in some form. |
| secrets-03, secrets-04, secrets-06, secrets-07, secrets-08, secrets-10, secrets-11, secrets-12 | dropped | The slice needs nothing from outside and takes in no credential for the product to use; the list keeper's own way in is asked about in the rows above and under sign-in. |
| authorization-01 | `waiting-list` | People's names are not to be shown to everyone. |
| authorization-03 | `bringing-across` | Someone other than the list keeper must not get past the screen to the list. |
| authorization-04 | `waiting-list` | The requirements leave open who else may see the list. |
| authorization-05 | `way-back-in` | Who keeps the list could change. |
| authorization-06 | `bringing-across` | A list brought across in the list keeper's name by another page would change the order. |
| authorization-07 | `bringing-across` | Following a link must not bring across or change the list. |
| authorization-08 | `shown-list` | The check of who is asking could fail to complete. |
| authorization-10 | `way-back-in` | The product could take from the device who the list keeper is. |
| authorization-11 | `way-back-in` | A lost device or lost access could still reach the names. |
| authorization-12 | `way-back-in` | The list keeper must come back to their own list and not another account. |
| authorization-02, authorization-09 | dropped | The slice has one list and one person acting on it, and its criteria store no file to be fetched. |
| configuration-05 | `waiting-list` | A default left unchanged could expose the names. |
| configuration-06 | `waiting-list` | Something switched on from the start could reach the list. |
| configuration-07 | `waiting-list` | A trial set up differently could hold or show real names. |
| configuration-11 | `waiting-list` | A diagnostic mode could show the names. |
| configuration-12 | `waiting-list` | Whoever can change settings could affect who reaches the list. |
| configuration-01, configuration-02, configuration-03, configuration-04, configuration-08, configuration-09, configuration-10 | dropped | The criteria add no setting that a person or an installation chooses. |
| logging-01 | `waiting-list` | The council wants fairness shown, and what happened to the order may need a record. |
| logging-02 | `bringing-across` | Someone may later need to tell what was brought across and by whom. |
| logging-03 | `person-name` | Names must not leak through records. |
| logging-04 | `person-name` | A name written into a record is text from outside the product. |
| logging-05 | `bringing-across` | A record of bringing across could fail to be written. |
| logging-06 | `waiting-list` | Any records about the list can grow. |
| logging-07 | `bringing-across` | A failure has to make sense to a list keeper who is not technical. |
| logging-08 | `waiting-list` | Records about the list could be lost with the machine holding them. |
| logging-09 | `bringing-across` | Somebody may need to be told when bringing across fails. |
| logging-10 | `waiting-list` | A changed record could hide a change to the order. |
| logging-11 | `waiting-list` | Records about the list would carry times. |
| logging-12 | `waiting-list` | Records about people waiting are kept for some period. |
| accessibility-01 | `bringing-across` | The list keeper may need to do it with a keyboard alone. |
| accessibility-02 | `shown-list` | A keyboard user must be able to leave each part of the list. |
| accessibility-03 | `shown-list` | A keyboard user must see where they are on it. |
| accessibility-04 | `bringing-across` | Focus can be lost when a part used for bringing across closes. |
| accessibility-05 | `bringing-across` | Its controls must make sense to someone who cannot see them. |
| accessibility-06 | `shown-list` | Anything in the list that is not text needs words. |
| accessibility-07 | `bringing-across` | Someone who cannot see the screen must learn whether it worked. |
| accessibility-08 | `shown-list` | Colour could be used to mark something in the list. |
| accessibility-09 | `shown-list` | The list has to be readable. |
| accessibility-10 | `shown-list` | The text of the list may be enlarged. |
| accessibility-11 | `bringing-across` | A time limit could cut off someone bringing across slowly. |
| accessibility-12 | `shown-list` | Anything that moves could get in the way of reading the list. |
| sign-in-01 | `way-back-in` | If coming back needs signing in, someone could guess the way in. |
| sign-in-02 | `way-back-in` | An account made in advance could reach the names. |
| sign-in-04 | `way-back-in` | The list keeper could lose what they use to get back in. |
| sign-in-05 | `way-back-in` | The list keeper's first way in has to be made and given to them. |
| sign-in-06 | `way-back-in` | There could be more than one way in. |
| sign-in-07 | `way-back-in` | An unusual way in to the names may need to be known about. |
| sign-in-08 | `way-back-in` | The criteria have the list keeper leave and come back. |
| sign-in-09 | `way-back-in` | The list keeper could be signed in more than once. |
| sign-in-10 | `way-back-in` | A session from before signing in could be carried over. |
| sign-in-11 | `way-back-in` | Bringing across sets everyone's order and may call for proof again. |
| sign-in-12 | `way-back-in` | A session left open could need ending. |
| sign-in-03 | dropped | Only the list keeper acts in this slice and its criteria have no signing up. |
| stored-data-01 | `waiting-list` | Seeing the names or changing the order could harm people waiting. |
| stored-data-02 | `waiting-list` | The names are stored and are not to be shown to everyone. |
| stored-data-03 | `waiting-list` | Any protection of the stored list by key needs the key kept somewhere. |
| stored-data-04 | `waiting-list` | Losing such a key could lose the list. |
| stored-data-05 | `person-name` | A name could end up in an address. |
| stored-data-06 | `shown-list` | Something in between could keep a copy of the names. |
| stored-data-07 | `waiting-list` | Whatever the product runs on could receive the names. |
| stored-data-08 | `shown-list` | More could be sent than is shown. |
| stored-data-09 | `waiting-list` | People's names are kept for some period. |
| stored-data-10 | `waiting-list` | The list or part of it could be left on a device. |
| stored-data-12 | `waiting-list` | Whether looking at the names is recorded matters when they are limited. |
| stored-data-11 | dropped | The criteria take in names and their order, not a submitted file. |
| file-intake: all | dropped | The criteria take in names and their order from a paper notebook, not a file. |
| misuse-01 | `bringing-across` | The list could be asked for before it has been brought across, or while it is partly across. |
| misuse-02 | `bringing-across` | Any rule on what may be brought across has a place where it is enforced. |
| misuse-03 | `bringing-across` | The documents do not say that nothing can call it again and again. |
| misuse-04 | `bringing-across` | The documents do not say that no one but a person can act on it. |
| misuse-05 | `bringing-across` | It sets who is ahead of whom, and the problem reports a row over plots going to friends. |
| misuse-07 | `bringing-across` | A request could set a place or another field that was not meant to be set. |
| misuse-08 | `waiting-list` | A place near the front is in limited supply. |
| misuse-06 | dropped | The criteria have one person bringing across one list of about 40 people, and nothing costly to run. |
