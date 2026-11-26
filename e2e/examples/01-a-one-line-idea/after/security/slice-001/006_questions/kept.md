# Kept: slice 1

## What the slice creates and keeps
- waiting-list: notebook-order-kept / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `person-name` | text | the list keeper, from the notebook | waiting-details | notebook-order-kept / 1 |
| `notebook-order` | list | the list keeper, from the notebook | waiting-details | notebook-order-kept / 1 |

## Other things the slice has
- `carry-across`: the list keeper having the list carried across (notebook-order-kept / 1)
- `list-view`: what the list keeper is shown of the carried-across list (notebook-order-kept / 1)
- `stored-list`: wherever the carried-across list is stored, and any copy of it (notebook-order-kept / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The requirements say "Outside systems: none" and the slice needs nothing from outside |
| receive-external-data: all | dropped | The requirements say "Outside systems: none", so no reply or notification arrives |
| sync-04 | `list-view` | The list can go out of date, and before carrying across there is none to show |
| sync-08 | `carry-across` | Only part of the notebook list may have come across |
| sync-01, sync-02, sync-03, sync-05, sync-06, sync-07, sync-09, sync-10, sync-11, sync-12 | dropped | The slice carries the list across from nothing and keeps no copy that updates from a source |
| limits-04 | waiting-list | The list holds as many people as are carried across |
| limits-06 | `carry-across` | A limit on the list could stop the keeper partway and leave them needing to know what to do |
| limits-07 | `carry-across` | One carrying across takes a whole list, whose size could pass what is accepted |
| limits-08 | `list-view` | The keeper is shown every person on the carried-across list |
| limits-01, limits-02, limits-09 | dropped | The requirements say "Outside systems: none" |
| limits-03, limits-05, limits-10, limits-11, limits-12 | dropped | The slice has one action by the list keeper, with no shared allowance, other feature, schedule or queued work |
| durable-write-01 | waiting-list | A save cut off partway could keep only part of the list |
| durable-write-02 | `carry-across` | The keeper needs to know when the list is safely kept |
| durable-write-03 | waiting-list | The list has to survive wherever it is kept |
| durable-write-04 | `carry-across` | Saving the list could fail for lack of space |
| durable-write-05 | `carry-across` | Storage could report that saving the list failed |
| durable-write-06 | waiting-list | Trying again after a failure could replace what was saved of the list |
| durable-write-08 | waiting-list | The people on the list and their order must agree |
| durable-write-09 | waiting-list | A silent change would break the notebook's order |
| durable-write-10 | waiting-list | A copy of the list could be taken while it is being saved |
| durable-write-11 | waiting-list | What makes up the saved list could be only partly moved or restored |
| durable-write-12 | `carry-across` | The keeper could close the product while the list is being saved |
| durable-write-07 | dropped | The slice keeps the list and adds to no history over time |
| startup-read-01 | waiting-list | The saved list could be found damaged |
| startup-read-02 | waiting-list | Something unrecognised could be where the list is expected |
| startup-read-03 | waiting-list | "Nothing carried across" must not be confused with a list that cannot be opened |
| startup-read-04 | `carry-across` | An earlier carrying across could be left unfinished |
| startup-read-05 | waiting-list | The list might be readable but not changeable |
| startup-read-06 | waiting-list | The documents do not say that only one copy of the product reads the list |
| startup-read-07 | waiting-list | Where the list will be kept is not yet known |
| startup-read-08 | waiting-list | A rescued list could have lost people or changed their order |
| startup-read-09 | waiting-list | A list can be readable and still be in the wrong order |
| startup-read-10 | waiting-list | An unusable list would need a spare copy to come back from |
| migration-01 | waiting-list | An earlier version could be run against a list saved by a later one |
| migration-03 | waiting-list | A new version of what this slice delivers could save the list and then be withdrawn |
| migration-02, migration-04, migration-05, migration-06, migration-07, migration-08, migration-09, migration-10, migration-11, migration-12 | dropped | This is the first slice: no earlier saved data exists and the slice changes no stored form |
| concurrency-01 | `carry-across` | Two attempts could each start from seeing nothing carried across |
| concurrency-03 | `list-view` | The people and their order must be read as they stood together |
| concurrency-04 | `carry-across` | Carrying across starts from nothing being there, which could stop being true before it finishes |
| concurrency-05 | `list-view` | A partly carried list could be seen before it is complete |
| concurrency-06 | `list-view` | Another window or device could still show nothing carried across |
| concurrency-08 | `carry-across` | The list could be in use when it is being saved |
| concurrency-09 | `carry-across` | A second attempt could clash with the first |
| concurrency-12 | waiting-list | The documents do not say that only one copy of the product can change the list |
| concurrency-02, concurrency-07, concurrency-10, concurrency-11 | dropped | The slice makes one list, with no rule between separate changes, timed right, multiple holds or sole-use wait |
| lifecycle-01 | `carry-across` | Several people are carried across and a later one could fail |
| lifecycle-02 | waiting-list | Clearing a failed carrying across could itself fail |
| lifecycle-03 | `carry-across` | No slice yet includes changing the list once it is across |
| lifecycle-04 | `carry-across` | Carrying across could stay unfinished |
| lifecycle-05 | waiting-list | A person without a place, or a place without a person, would make no sense |
| lifecycle-08 | `carry-across` | The keeper could abandon carrying across partway |
| lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11 | dropped | The slice removes no thing |
| lifecycle-12 | dropped | The slice holds nothing for a limited time |
| user-input-01 | `person-name` | A name from the notebook has a length |
| user-input-02 | `person-name` | A notebook entry could lack a full or readable name |
| user-input-03 | `person-name` | Names can contain varied characters |
| user-input-04 | `person-name` | A name in the notebook could have one part or several |
| user-input-05 | `carry-across` | Names reach the product through the carrying across, where any rule must hold |
| user-input-06 | `carry-across` | An entry could be refused while the list is carried across |
| user-input-07 | `person-name` | A name could be blank or have spaces around it |
| user-input-09 | `person-name` | Two entries could carry the same name while each person must appear once |
| user-input-10 | `person-name` | The name given is later shown to the keeper |
| user-input-08, user-input-12 | dropped | The slice takes in no number or date |
| user-input-11 | dropped | A name and the order of the list put no condition on each other's values |
| user-action-01 | `carry-across` | The keeper could start carrying across twice |
| user-action-02 | `list-view` | The keeper could reload after carrying across |
| user-action-03 | `list-view` | The keeper could step back after carrying across |
| user-action-04 | `list-view` | Names could stay visible on a device after the keeper leaves |
| user-action-05 | `carry-across` | The keeper could leave with part of the list unsaved |
| user-action-06 | `carry-across` | The keeper's device could discard the screen partway through |
| user-action-07 | `list-view` | The keeper could have the list open in two windows |
| user-action-08 | `carry-across` | The keeper could carry across something wrong and want it undone |
| user-action-09 | `carry-across` | Carrying across may be a step the keeper cannot take back |
| user-action-10 | `carry-across` | The keeper could back out partway through the list |
| user-action-11 | `carry-across` | The documents do not say whether a signed-in period could end partway |
| user-action-12 | `list-view` | A saved address to the list could be opened later by someone not entitled to it |
| long-operation-01 | `carry-across` | Carrying a whole list across may take more than a few seconds |
| long-operation-02 | `carry-across` | A stopped carrying across could look like a working one |
| long-operation-03 | `carry-across` | The keeper may need to stop partway |
| long-operation-04 | `carry-across` | Stopping could leave part of the list across |
| long-operation-05 | `carry-across` | The keeper could go elsewhere before it ends |
| long-operation-06 | `carry-across` | It could be interrupted partway through the list |
| long-operation-07 | `carry-across` | A late failure could leave the keeper believing the list is across |
| long-operation-08 | `carry-across` | Some people could come across and others not |
| long-operation-09 | `carry-across` | It could stop making progress |
| long-operation-10 | waiting-list | The result of carrying across is the list, which is kept |
| long-operation-11 | `carry-across` | Another carrying across could be asked for while one is unfinished |
| long-operation-12 | `carry-across` | Something certain to fail could be found only after much of the list is across |
| time: all | dropped | The slice takes in no date or time, and its one criterion takes the order from the notebook with no clock |
| text-01 | `person-name` | "Each once" depends on telling entries apart, and names may match |
| text-02 | `person-name` | Names could differ only in capital letters |
| text-03 | `person-name` | A name could carry unseen characters or unusual spaces |
| text-05 | `person-name` | A long name could be cut |
| text-09 | `person-name` | A name written in the opposite direction is put into a row of the list |
| text-10 | `list-view` | The keeper must tell similar names apart to check the list against the notebook |
| text-12 | `list-view` | Names and messages need room where the list is shown |
| text-04, text-11 | dropped | The slice has no search and nothing that depends on word boundaries |
| text-06, text-07, text-08 | dropped | The list is ordered as the notebook is, never by its text |
| presentation-12 | `list-view` | A list longer than one screen must keep the notebook's order throughout |
| presentation-01, presentation-07, presentation-08, presentation-09 | dropped | The slice shows no date, time or calendar |
| presentation-02, presentation-03, presentation-04, presentation-05, presentation-06 | dropped | The slice's criterion shows people in order, with no number, amount or count |
| presentation-10, presentation-11 | dropped | The list is never ordered by name or by a column |
| corpus: all | dropped | The slice ships no body of content: the only list is the society's own, which the keeper has carried across |
| secrets: all | dropped | The slice and the documents name no credential the product uses, and the slice needs nothing from outside |
| authorization-01 | `carry-across`; `list-view` | The documents say names are not to be shown to everyone, so who may carry across and look matters |
| authorization-02 | waiting-list | A request for the list must come from someone entitled to it |
| authorization-03 | `list-view` | The list could be asked for without going through what the keeper is shown |
| authorization-04 | waiting-list | Someone no rule mentions could ask for the list |
| authorization-05 | waiting-list | The person who keeps the list could change |
| authorization-06 | `carry-across` | A request to carry across could be sent in the keeper's name |
| authorization-07 | `carry-across` | Carrying across changes what is kept and could be set off by loading a page |
| authorization-08 | `list-view` | The check on who may see the names could fail to complete |
| authorization-10 | `list-view` | The keeper's device could be relied on to say who is looking |
| authorization-11 | `list-view` | The keeper could lose access while the list is open |
| authorization-12 | `list-view` | The documents do not rule out accounts, and the wrong one would expose or change the list |
| authorization-09 | dropped | The slice takes in and keeps no file that anyone fetches |
| configuration-01 | waiting-list | How the list is kept is not yet known and may rest on a setting checked at start |
| configuration-03 | waiting-list | A trial and the real list may be kept in different places |
| configuration-05 | `list-view` | A default left unchanged could leave the names open to others |
| configuration-06 | `list-view` | Something switched on from the start could expose the list |
| configuration-07 | waiting-list | A trial with invented names and the real list may be set up differently |
| configuration-11 | `list-view` | A diagnostic mode could reveal the names |
| configuration-12 | waiting-list | A setting that decides where the list is kept could be changed from outside |
| configuration-02, configuration-04, configuration-08, configuration-09, configuration-10 | dropped | The documents give this slice no setting that anyone chooses or changes |
| logging-01 | `carry-across` | Showing fair handling later could depend on knowing the list was carried across |
| logging-02 | `carry-across` | Someone may need to tell what was carried across and by whom |
| logging-03 | `person-name` | Names must not be shown to everyone, including through records |
| logging-04 | `person-name` | A name given from outside could be written into a record |
| logging-05 | `carry-across` | A record of carrying across could fail to be written |
| logging-06 | `carry-across` | Records of attempts could grow |
| logging-07 | `carry-across` | A failed carrying across needs a message for the keeper and perhaps a record |
| logging-08 | `carry-across` | A record of carrying across could be lost with its machine |
| logging-09 | `carry-across` | A failure may need someone to be told |
| logging-10 | `carry-across` | A changed record could hide what happened to the order |
| logging-11 | `carry-across` | A record of carrying across would carry a time |
| logging-12 | `carry-across` | Records could hold people's details longer than needed |
| accessibility-01 | `carry-across` | The keeper may need to carry the list across with a keyboard alone |
| accessibility-02 | `carry-across` | A keyboard user must be able to leave each part of carrying across |
| accessibility-03 | `carry-across` | A keyboard user needs to see where they are while carrying across |
| accessibility-04 | `carry-across` | Something holding focus could close while the list is carried across |
| accessibility-05 | `carry-across` | Whoever keeps the list may not be able to see the controls |
| accessibility-06 | `list-view` | Anything shown with the list that is not text needs the same meaning in words |
| accessibility-07 | `carry-across` | A keeper who cannot see the screen must learn whether the list came across |
| accessibility-08 | `list-view` | Colour could be used to mark something in the list |
| accessibility-09 | `list-view` | The keeper has to read the names to check them |
| accessibility-10 | `list-view` | The keeper could enlarge the text while checking the order |
| accessibility-11 | `carry-across` | A time limit could cut off a keeper working slowly through the notebook |
| accessibility-12 | `list-view` | Anything moving while the list is shown could hinder the keeper |
| sign-in-01 | `list-view` | If the keeper signs in to see the names, someone could guess the way in |
| sign-in-02 | `list-view` | An account present from the start could open the list |
| sign-in-03 | `list-view` | Sign-in could reveal who has access to the list |
| sign-in-04 | `list-view` | A keeper who forgets how to get in would lose sight of the list |
| sign-in-05 | `list-view` | The keeper would need a first way in |
| sign-in-06 | `list-view` | The weakest way in would decide who can see the names |
| sign-in-07 | `list-view` | A changed way in could hand the list to someone else |
| sign-in-08 | `list-view` | A lasting session could leave the list open |
| sign-in-09 | `list-view` | The keeper could be signed in on more than one device |
| sign-in-10 | `list-view` | A session held beforehand could be reused to see the list |
| sign-in-11 | `carry-across` | Carrying across sets everyone's place and may call for proof of who is doing it |
| sign-in-12 | `list-view` | A session left on another device could need ending |
| stored-data-01 | waiting-list | The names and order could harm people or fairness if seen or changed |
| stored-data-02 | waiting-list | The saved list and its copies hold people's names |
| stored-data-03 | waiting-list | Any protection of the saved list could rest on keys |
| stored-data-04 | waiting-list | Losing a key could lose the saved list |
| stored-data-05 | `person-name` | A name could end up in an address |
| stored-data-06 | `list-view` | Something between could keep a copy of the names shown |
| stored-data-07 | waiting-list | Whatever keeps the list could pass it to another party |
| stored-data-08 | `list-view` | More could be sent than the keeper needs to see |
| stored-data-09 | waiting-list | The documents do not say how long people's names are kept |
| stored-data-10 | waiting-list | The list could be stored on the keeper's own device |
| stored-data-12 | waiting-list | Someone may need to know who has read the names |
| stored-data-11 | dropped | The slice takes in no file |
| file-intake: all | dropped | The slice takes in a name and an order, and no file |
| misuse-01 | `carry-across` | Carrying across could be asked for when the list is already across |
| misuse-02 | `carry-across` | Any rule on what may be carried across, and when, has to hold somewhere |
| misuse-03 | `carry-across` | The documents do not say the product is out of a script's reach |
| misuse-04 | `carry-across` | The documents do not say whether very fast repeated attempts can happen |
| misuse-05 | `carry-across` | It sets the order for plots, and plots have gone to a friend out of turn |
| misuse-06 | `carry-across` | Repeated carrying across could use up what the monthly limit pays for |
| misuse-07 | `carry-across` | More than names in order could be sent while carrying across |
| misuse-08 | waiting-list | An earlier place is in limited supply, and someone could be put in twice or too high |
