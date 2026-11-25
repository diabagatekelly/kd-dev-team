# Kept: slice 1

## What the slice creates and keeps
- absence: record-for-singer / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `singer-name` | text | a section leader | singer-details | record-for-singer / 1 |
| `rehearsal-date` | date | a section leader, or whoever arranges the programme | no | record-for-singer / 1 |
| `saved-singers` | list | read back from the saved register | singer-details | record-for-singer / 2 |
| `saved-absences` | list | read back from what was saved | singer-details | see-who-missing / 1 |

## Other things the slice has
- `record-request`: a section leader's request to record an absence (record-for-singer / 1)
- `refusal-message`: what a section leader is told when an absence is refused (record-for-singer / 2)
- `missing-view`: what whoever arranges the programme is shown for one rehearsal (see-who-missing / 1)
- `saved-register`: what the product keeps stored, the singers and the recorded absences (record-for-singer / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | the slice needs nothing from outside (004_slice.md, "Needs from outside": none) |
| receive-external-data: all | dropped | no data arrives from an outside system: the slice needs nothing from outside |
| sync-10 | `missing-view` | an absence can be recorded while the list for that rehearsal is being looked at |
| sync-01, sync-02, sync-03, sync-04, sync-05, sync-06, sync-07, sync-08, sync-09, sync-11, sync-12 | dropped | the slice makes no second copy and updates nothing from a source: the register is on the one hall computer (000_problem.md line 14); older and newer versions are asked about under migration |
| limits-08 | `missing-view` | many singers could be missing the same rehearsal and be listed together |
| limits-01, limits-02, limits-09 | dropped | the slice calls no outside system and uses no paid service |
| limits-03, limits-04, limits-05, limits-10, limits-11, limits-12 | dropped | the harm needs heavy demand or queued or scheduled work: the choir is about 45 singers (000_problem.md line 4) on one small computer (line 14), and the criteria queue and schedule nothing |
| limits-06, limits-07 | dropped | the slice sets no usage limit and accepts no item beyond single typed values, whose length is asked under user-input-01 |
| durable-write-01 | `saved-register` | saving an absence could be cut off while the singers are stored too |
| durable-write-02 | `absence` | the section leader is shown that the absence is recorded |
| durable-write-03 | `saved-register` | absences must still be there on the hall computer after it loses power |
| durable-write-04 | `record-request` | recording an absence is a save that can run out of space |
| durable-write-05 | `record-request` | the storage can report that saving an absence failed |
| durable-write-06 | `saved-register` | adding an absence may replace what is saved |
| durable-write-07 | `saved-register` | absences are added over time, and the last one could be incomplete |
| durable-write-08 | `saved-register` | each saved absence must agree with a saved singer |
| durable-write-09 | `saved-register` | a saved absence or singer could change unnoticed and alter who is shown missing |
| durable-write-10 | `saved-register` | a copy of the register could be taken while an absence is being saved |
| durable-write-11 | `saved-register` | singers and absences together are what the slice needs to read |
| durable-write-12 | `record-request` | the product could be closed while an absence is being saved |
| startup-read-01 | `saved-register` | the saved singers or absences could be damaged |
| startup-read-02 | `saved-register` | something else could be where the register is expected, and recording would write there |
| startup-read-03 | `saved-register`; `see-who-missing-2` | an unreadable register must not pass for one with no absences |
| startup-read-04 | `saved-register` | an earlier recording could have been left unfinished |
| startup-read-05 | `saved-register` | the list could be readable when an absence cannot be saved |
| startup-read-06 | `saved-register` | a second copy could start while the saved register is being repaired |
| startup-read-07 | `saved-register` | whether the hall computer can remove the saved register on its own affects who is shown missing |
| startup-read-08 | `saved-register` | a rescued register could have lost absences or singers |
| startup-read-09 | `saved-register` | readable but wrong absences would mislead whoever arranges the programme |
| startup-read-10 | `saved-register` | if the register is unusable, absences and singers need a spare to come from |
| migration-01 | `saved-register` | once absences are added, versions of the program differ in what they expect saved |
| migration-02 | `saved-register` | the register saved today must be carried forward |
| migration-03 | `saved-register` | the earlier program could be put back after absences are saved |
| migration-05 | `saved-register` | the earlier program could still be running when the new one first uses the register |
| migration-07 | `saved-register` | the register saved today holds nothing about absences |
| migration-10 | `saved-register` | the first use of the register by the new program could fail partway |
| migration-11 | `saved-register` | a spare copy made today holds no absences and might be brought back later |
| migration-04, migration-06, migration-08, migration-09, migration-12 | dropped | there is one installation (000_problem.md line 14), and the criteria only add absences: they change, rename and discard no saved value and leave no work in progress |
| concurrency-01 | `saved-register` | two section leaders' recordings could start from the same saved register |
| concurrency-02 | `absence`; `singer-in-the-register` | an absence is only allowed for a singer in the register |
| concurrency-03 | `missing-view` | the list reads singers and absences while one may be being recorded |
| concurrency-04 | `record-request` | the product decides from the saved singers whether the name may be recorded |
| concurrency-06 | `missing-view` | a newly recorded absence has to show to whoever arranges the programme |
| concurrency-08 | `saved-register` | the register could be in use when an absence is recorded |
| concurrency-09 | `record-request` | a recording could be turned down because it clashed with another |
| concurrency-12 | `saved-register` | two copies of the program could be open on the hall computer |
| concurrency-05, concurrency-07, concurrency-10, concurrency-11 | dropped | the criteria withdraw no change, give no time-limited right, hold no set of things while waiting and have no continuous stream of readers |
| lifecycle-03 | `absence` | no document gives a way to take back a recorded absence |
| lifecycle-05 | `absence` | an absence makes sense only with its singer |
| lifecycle-01, lifecycle-02, lifecycle-04, lifecycle-06, lifecycle-07, lifecycle-08, lifecycle-09, lifecycle-10, lifecycle-11, lifecycle-12 | dropped | recording is one action, and the slice removes nothing, undoes nothing, holds nothing and leaves nothing in progress; how long absences are kept is asked under stored-data-09 |
| user-input-01 | `singer-name` | a section leader gives the singer's name |
| user-input-02 | `record-request` | an absence needs a singer and a date |
| user-input-03 | `singer-name` | names may contain marks or letters that could be refused |
| user-input-04 | `singer-name` | a name may have more or fewer parts than the way it is asked for |
| user-input-05 | `record-request` | the refusals for singer and date have to hold wherever a request comes from |
| user-input-06 | `refusal-message`; `record-for-singer-3` | the criteria refuse an unknown singer and a date that does not exist |
| user-input-07 | `singer-name` | a typed name may be empty or carry extra spaces |
| user-input-09 | `singer-name` | the name is what picks out the singer, and two singers could share one |
| user-input-10 | `singer-name` | the typed name is shown back and kept |
| user-input-11 | `record-request` | whether an absence is allowed depends on the singer and the date together |
| user-input-12 | `rehearsal-date` | a date such as one in January can be written in several ways |
| user-input-08 | dropped | the slice takes in no number |
| user-action-01 | `record-request` | a section leader could record the same absence again while the first is being saved |
| user-action-02 | `record-request` | what follows a recording could be reloaded |
| user-action-03 | `record-request` | a section leader could step back to the request after it succeeded |
| user-action-05 | `record-request` | a section leader could leave before the absence is saved |
| user-action-06 | `missing-view` | the list could be left on the hall computer and be out of date on return |
| user-action-07 | `missing-view` | the list and a recording could be open in two windows |
| user-action-08 | `absence` | a mistaken absence cannot be put right in this slice |
| user-action-09 | `record-request` | a wrong singer or date, once recorded, stays |
| user-action-10 | `record-request` | a section leader could give up partway through recording |
| user-action-12 | `missing-view` | an address for one rehearsal's list could be saved and opened later |
| user-action-04, user-action-11 | dropped | the slice does no sign-in or sign-out; the register has no accounts (002_requirements.md line 15) |
| long-operation: all | dropped | each criterion is a single short action on the register of about 45 singers (000_problem.md line 4); no operation is started and left running |
| time-01 | `rehearsal` | whether a rehearsal is still ahead depends on today's date |
| time-03 | `rehearsal` | a changed clock could turn a coming rehearsal into a past one |
| time-07 | `rehearsal-date` | the rehearsal date is a plain date and must not move a day |
| time-08 | `rehearsal-date` | which day it is decides whether the rehearsal is ahead |
| time-10 | `rehearsal` | we rehearse every Thursday, so the product may have to tell which dates are rehearsals |
| time-12 | `absence` | when an absence was recorded may matter against the Tuesday evening need |
| time-02, time-04, time-05, time-06, time-09, time-11 | dropped | there is one computer (000_problem.md line 14), and the criteria use plain dates only: they measure no span, set no clock time, count no months and order no events |
| text-01 | `singer-name` | the typed name is matched against the register |
| text-02 | `singer-name` | a name may be typed with different capital letters |
| text-03 | `singer-name` | an unusual space could stop a name matching |
| text-05 | `singer-name` | a long name may be cut where it is shown |
| text-06 | `missing-view` | the missing singers are listed in some order |
| text-07 | `missing-view` | the names in the list may come from more than one language |
| text-09 | `singer-name` | the name is put into the confirmation, the refusal and the list |
| text-10 | `singer-name` | a section leader must pick the right singer between similar names |
| text-12 | `missing-view` | names and messages need room to be read in full |
| text-04, text-08, text-11 | dropped | the criteria have no search (matching is asked under text-01), keep no result that depends on ordering and do nothing with word boundaries |
| presentation-01 | `rehearsal-date` | the date is shown back to the section leader and heads what is looked at |
| presentation-06 | `rehearsal-date` | the date is shown with digits |
| presentation-09 | `rehearsal-date` | a date is shown in some calendar |
| presentation-10 | `missing-view` | the missing singers are a list of people |
| presentation-12 | `missing-view` | the list could be longer than the hall computer's screen |
| presentation-02, presentation-03, presentation-04, presentation-05, presentation-07, presentation-08, presentation-11 | dropped | the criteria show names and dates only: no amount, count, clock time, week or sortable column |
| corpus: all | dropped | the slice ships no body of content |
| secrets: all | dropped | the slice uses no credential: it needs nothing from outside and the register has no accounts (002_requirements.md line 15) |
| authorization-01 | `record-request`; `missing-view` | only section leaders are named to record, and the arranger to see, with no accounts today |
| authorization-02 | `absence` | whether a person asking may reach a given absence is not yet settled |
| authorization-03 | `record-request` | a request could reach the register another way than the intended one |
| authorization-04 | `saved-register` | singers or others at the hall computer are named by no rule |
| authorization-05 | `record-request` | someone may stop being a section leader |
| authorization-06 | `record-request` | an absence could be recorded by a request the person did not mean to make |
| authorization-07 | `record-request` | recording changes the register and must not happen just by opening something |
| authorization-08 | `record-request` | if who may record is checked, the check could fail |
| authorization-09 | `saved-register` | the saved names and absences could be opened directly |
| authorization-10 | `record-request` | what says the person is a section leader may come from where they sit or what they enter |
| authorization-11, authorization-12 | dropped | the slice does no sign-in, so nothing is held after signing out and no account is chosen (002_requirements.md line 15) |
| configuration: all | dropped | the criteria add and change no setting |
| logging-01 | `record-request` | a disputed or mistaken absence may need a record of its recording |
| logging-02 | `record-request` | with no accounts, a record may not tell who recorded an absence |
| logging-03 | `singer-name` | names and absences could end up in records |
| logging-04 | `singer-name` | a typed name could be written into a record |
| logging-05 | `record-request` | a record of a recording could fail to be written |
| logging-06 | `record-request` | records of recordings would grow on the small computer |
| logging-07 | `record-request` | saving an absence can fail, and someone must be told |
| logging-08 | `saved-register` | records kept only on the hall computer could be lost with it |
| logging-09 | `record-request` | someone may need to notice recordings that fail |
| logging-10 | `record-request` | people using the hall computer could change a record of who recorded what |
| logging-11 | `record-request` | a record's time would come from the hall computer's clock |
| logging-12 | `singer-name` | records holding names would need an end |
| accessibility-01 | `record-request`; `missing-view` | recording and looking are things a person does on a screen |
| accessibility-02 | `record-request` | a keyboard user must be able to leave whatever records an absence |
| accessibility-03 | `record-request` | the person recording must see where their typing goes |
| accessibility-04 | `record-request` | something may close once an absence is recorded or refused |
| accessibility-05 | `record-request` | the singer and date entries need names someone can hear |
| accessibility-06 | `missing-view` | anything in the list that is not text needs words |
| accessibility-07 | `record-request` | the section leader must learn whether the absence was recorded or refused |
| accessibility-08 | `missing-view`; `refusal-message` | colour could be used to mark who is missing or what was refused |
| accessibility-09 | `missing-view` | names must be readable on the hall computer's screen |
| accessibility-10 | `missing-view` | someone may need the list with larger text |
| accessibility-11, accessibility-12 | dropped | the criteria have no step with a time limit and nothing that moves |
| sign-in: all | dropped | the slice does no sign-in: the register has no accounts (002_requirements.md line 15) |
| stored-data-01 | `absence`; `saved-register` | who will be away is a singer's own detail, and a changed one misleads the arranger |
| stored-data-02 | `saved-register` | names and absences are stored on a computer several people use |
| stored-data-03 | `saved-register` | whether the saved names and absences need a key to protect them is open |
| stored-data-04 | `saved-register` | if they are protected by a key, it could be lost |
| stored-data-05 | `singer-name` | a name could travel in an address when it is looked up or recorded |
| stored-data-06 | `missing-view` | something between the register and the screen could keep a copy of the list |
| stored-data-08 | `missing-view` | the list could show more about a singer than is needed |
| stored-data-09 | `absence` | no document says how long a past absence is kept |
| stored-data-10 | `saved-register` | the hall computer is the device the names and absences are stored on |
| stored-data-12 | `missing-view` | the list shows who will be away |
| stored-data-07, stored-data-11 | dropped | the slice sends nothing to another party (004_slice.md, "Needs from outside": none) and takes in no file |
| file-intake: all | dropped | the slice takes in no file |
| misuse-02 | `record-request` | the rules on singer and date have to be enforced somewhere |
| misuse-03 | `record-request` | something repeating the request could fill the register with absences |
| misuse-04 | `record-request` | many absences recorded at once could mean something is wrong |
| misuse-05 | `record-request` | a recorded absence cannot be taken back in this slice |
| misuse-07 | `record-request` | a recording must not change anything about the singer |
| misuse-01, misuse-06, misuse-08 | dropped | recording has no earlier step, no costly operation and nothing in limited supply |
