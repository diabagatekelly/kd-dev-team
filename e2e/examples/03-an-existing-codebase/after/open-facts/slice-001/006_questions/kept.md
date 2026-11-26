# Kept: slice 1

## What the slice creates and keeps
- A singer: see-who-will-miss / 1
- A rehearsal: record-for-singer / 3
- A singer's word that they will miss a rehearsal: record-for-singer / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `singer-name` | text | the section leader, naming who will miss | singer-details | record-for-singer / 2 |
| `rehearsal-date` | date | the section leader or the person who plans the programme, saying which rehearsal | no | record-for-singer / 3 |
| `todays-date` | date | whatever tells the register what day it is, to know whether a rehearsal has passed | no | record-for-singer / 3 |
| `kept-singer-name` | text | read back from the register | singer-details | see-who-will-miss / 1 |
| `kept-voice-part` | choice | read back from the register | no | see-who-will-miss / 1 |
| `kept-absence` | other | read back: which singer will miss which rehearsal | singer-details | see-who-will-miss / 2 |

## Other things the slice has
- `record-request`: a section leader's recording of an absence (record-for-singer / 1)
- `refusal-message`: what a section leader is told when nothing is recorded (record-for-singer / 2)
- `absence-view`: what the person who plans the programme is shown for a rehearsal (see-who-will-miss / 1)
- `saved-register`: what the register saves, the recorded absences among it (record-for-singer / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | the slice needs nothing from outside, and the requirements say "Outside systems: none." |
| receive-external-data: all | dropped | no outside system sends the slice anything: "Outside systems: none." |
| sync-04 | `absence-view` | the view can be looked at before all word is in, or with nothing recorded yet |
| sync-01, sync-02, sync-03, sync-05, sync-06, sync-07, sync-08, sync-09, sync-10, sync-11, sync-12 | dropped | the slice makes no second copy that is updated from a source: "The register is on a small computer at the church hall"; changes made while someone is looking are asked about under concurrency |
| limits-08 | `absence-view` | many names may have to be shown for one rehearsal |
| limits-01, limits-02, limits-09 | dropped | they need an outside or paid system, and "Outside systems: none." |
| limits-03, limits-04, limits-05, limits-10, limits-11, limits-12 | dropped | they need heavy or queued demand: "We are about 45 singers", and the slice schedules and queues nothing |
| limits-06, limits-07 | dropped | the slice sets no size or use limit and accepts no item beyond a name and a date; the length of a typed name is asked by user-input-01 |
| durable-write-01 | `saved-register` | recording an absence saves a change that could be cut off |
| durable-write-02 | `record-request` | a section leader relies on being shown that the absence is recorded |
| durable-write-03 | `saved-register` | absences must still be there after the hall computer loses power |
| durable-write-04 | `saved-register` | saving an absence can fail for lack of space |
| durable-write-05 | `saved-register` | the save of an absence can be reported as failed |
| durable-write-06 | `saved-register` | saving an absence may replace what holds the singers and attendance too |
| durable-write-07 | `saved-register` | absences are added over time and the last one may be incomplete |
| durable-write-08 | `singer-s-word-that-they-will-miss-a-rehearsal` | each absence must agree with a singer who is in the register |
| durable-write-09 | `saved-register` | a silently changed absence would give wrong numbers for a voice part |
| durable-write-10 | `saved-register` | a copy of the register may be taken while an absence is being saved |
| durable-write-11 | `saved-register` | the absences may be moved or restored apart from the singers they name |
| durable-write-12 | `record-request` | the register may be closed while an absence is being saved |
| startup-read-01 | `saved-register` | the saved absences or singers may be damaged when next read |
| startup-read-02 | `saved-register` | what is found where the register saves may not be the register's |
| startup-read-03 | `saved-register` | a register that cannot be opened must not pass for one with nobody missing |
| startup-read-04 | `saved-register` | an earlier save of an absence may have been left unfinished |
| startup-read-05 | `saved-register` | the person looking may be able to read the register and not change it |
| startup-read-06 | `saved-register` | the register may be opened again while it is being repaired |
| startup-read-07 | `saved-register` | the hall computer may remove saved data by itself; the documents do not say |
| startup-read-08 | `saved-register` | a rescued register could lose absences or bring old ones back |
| startup-read-09 | `saved-register` | absences can be readable and wrong |
| startup-read-10 | `saved-register` | an unusable register would take the recorded absences with it |
| migration-01 | `saved-register` | the slice adds absences to what is saved, which another version may not know |
| migration-02 | `saved-register` | singers and attendance saved before this slice have to be carried forward |
| migration-03 | `saved-register` | the earlier register may be put back after absences have been saved |
| migration-05 | `saved-register` | the earlier register may still be open when the new one first saves |
| migration-07 | `saved-register` | what is saved today holds no absences |
| migration-10 | `saved-register` | bringing today's saved data up to date can fail partway |
| migration-11 | `saved-register` | a spare copy taken before this slice may be brought back |
| migration-04, migration-06, migration-08, migration-09, migration-12 | dropped | there is one register, "on a small computer at the church hall"; the slice only adds absences, changes and renames no stored value, and has no work that lasts across an update |
| concurrency-01 | `singer-s-word-that-they-will-miss-a-rehearsal` | two section leaders may record from what each saw earlier |
| concurrency-02 | `record-request` | recording depends on both the singer being there and the rehearsal not having passed |
| concurrency-03 | `absence-view` | names and numbers are worked out from singers and absences together |
| concurrency-04 | `record-request` | whether there is such a singer is decided from the singers in the register at that moment |
| concurrency-05 | `absence-view` | an absence could be shown before its save has finished |
| concurrency-06 | `absence-view` | a new absence has to reach someone already looking |
| concurrency-08 | `saved-register` | the register may be in use when an absence is recorded |
| concurrency-09 | `record-request` | a recording may clash with another change and not go through |
| concurrency-12 | `saved-register` | section leaders share one computer and the register could be open twice |
| concurrency-07, concurrency-10, concurrency-11 | dropped | the slice gives no time-limited sole right, holds nothing while waiting for a person and has no long reading that could keep a save waiting |
| lifecycle-03 | `record-request` | a recorded absence cannot be taken back in this slice |
| lifecycle-05 | `singer-s-word-that-they-will-miss-a-rehearsal` | an absence makes sense only with its singer and its rehearsal |
| lifecycle-06 | `singer` | recorded absences belong to a singer who may leave the register |
| lifecycle-07 | `rehearsal` | absences depend on a rehearsal date that may be cancelled |
| lifecycle-01, lifecycle-02, lifecycle-04, lifecycle-08, lifecycle-09, lifecycle-10, lifecycle-11, lifecycle-12 | dropped | recording is one step with nothing in progress, held or abandoned, and the slice removes and undoes nothing; how long absences are kept is asked by stored-data-09 |
| user-input-01 | `singer-name` | a section leader gives a name of any length |
| user-input-02 | `record-request` | a recording needs to say who and which rehearsal |
| user-input-03 | `singer-name` | names carry marks and characters that might be refused |
| user-input-04 | `singer-name` | a singer's name has parts that may be given differently from the register |
| user-input-05 | `record-request` | the rules about the singer and the date must hold however a recording arrives |
| user-input-06 | `refusal-message` | the criteria refuse an unknown singer and a past rehearsal |
| user-input-07 | `singer-name` | a name may be given empty or with spaces around it |
| user-input-09 | `singer-name` | the singer is picked out by name, and two singers may share one |
| user-input-10 | `singer-name` | the name is later shown in the view |
| user-input-11 | `record-request` | the singer, the rehearsal and the section leader's own part have to fit together |
| user-input-12 | `rehearsal-date` | a date can be written in ways that mean different days |
| user-input-08 | dropped | nobody gives the slice a number |
| user-action-01 | `record-request` | a section leader needs to see the result and may record the same absence twice |
| user-action-02 | `absence-view` | what follows a recording may be loaded again |
| user-action-03 | `record-request` | someone may step back to the recording after it is done |
| user-action-05 | `record-request` | a section leader may walk away from a recording not yet saved |
| user-action-06 | `absence-view` | the view may be returned to after the computer has set it aside |
| user-action-07 | `absence-view` | the view and a recording may be open in two windows |
| user-action-08 | `record-request` | a wrong recording cannot be undone in this slice |
| user-action-09 | `record-request` | a recording for the wrong singer or date stays, so asking first may matter |
| user-action-12 | `absence-view` | a saved way back to one rehearsal's view may outlast the rehearsal |
| user-action-04, user-action-11 | dropped | they need signing in, and "The register as it stands has no accounts"; the slice adds none |
| user-action-10 | dropped | the slice has no longer operation: each criterion is one action |
| long-operation: all | dropped | the slice only records one absence or shows one rehearsal for a choir of about 45 singers |
| time-01 | `todays-date` | whether a rehearsal has passed depends on the day the computer thinks it is |
| time-03 | `todays-date` | a clock set back or forward changes which rehearsals count as passed |
| time-07 | `rehearsal-date` | a rehearsal is named by a date that must not shift to another day |
| time-08 | `todays-date` | today's date depends on a time zone |
| time-10 | `rehearsal` | rehearsals repeat every Thursday and the view tells the coming one from the one after |
| time-12 | `singer-s-word-that-they-will-miss-a-rehearsal` | when word was given and when it was recorded can differ, and Tuesday evening matters |
| time-02, time-04, time-05, time-06, time-09, time-11 | dropped | the register is on one computer, and the slice measures no span, handles no time of day, counts no months and orders nothing by recorded time |
| text-01 | `singer-name` | the name given must be matched with a name in the register |
| text-02 | `singer-name` | the name may be given with different capital letters |
| text-03 | `singer-name` | unseen characters or odd spaces could make a known singer unknown |
| text-04 | `singer-name` | finding a singer by name may meet accent marks or other spellings |
| text-05 | `absence-view` | a long name may be cut where it is shown |
| text-06 | `absence-view` | the names under each voice part come in some order |
| text-07 | `absence-view` | that order follows some language's rules, and the documents name none |
| text-09 | `absence-view` | names are set beside voice parts and numbers; the documents do not say how names are written |
| text-10 | `kept-singer-name` | the person reading must tell apart singers with alike names |
| text-12 | `absence-view` | names and messages need room on a small computer |
| text-08, text-11 | dropped | the slice stores nothing in text order and nothing depends on where words begin or end |
| presentation-01 | `absence-view` | the reader must know which rehearsal's date they are looking at |
| presentation-03 | `absence-view` | a pair such as 2 of 7 must be clear about meaning missing and not coming |
| presentation-04 | `absence-view` | a voice part may have none, one or several singers missing |
| presentation-06 | `absence-view` | numbers are shown and the documents do not say whose digits |
| presentation-09 | `absence-view` | dates are shown and the documents do not say in which calendar |
| presentation-10 | `absence-view` | singers are listed by names that have parts |
| presentation-12 | `absence-view` | a long list of absent singers has to keep its order and be all reachable |
| presentation-02, presentation-05, presentation-07, presentation-08, presentation-11 | dropped | the only numbers are whole counts within about 45 singers, and the slice shows no amount with decimals, no time of day, no week and no list that is reordered by column |
| corpus: all | dropped | the slice ships and uses no body of published content: it works on what the choir itself enters |
| secrets: all | dropped | the slice uses no credential: "The register as it stands has no accounts", it adds none, and "Outside systems: none." |
| authorization-01 | `record-request`; `absence-view` | several people use the computer, and who may record or look is not settled |
| authorization-02 | `record-request` | the thin path has a section leader recording for a singer in their own voice part |
| authorization-03 | `record-request` | a limit to the leader's own part would have to hold somewhere |
| authorization-04 | `absence-view` | anyone else at the computer is mentioned by no rule |
| authorization-05 | `record-request` | who is a section leader can change |
| authorization-06 | `record-request` | an absence could be recorded in a leader's name without their meaning it; the documents do not rule out how |
| authorization-07 | `record-request` | recording changes what is saved and must not happen just by opening something |
| authorization-08 | `record-request` | any check of who is recording may fail to complete |
| authorization-09 | `saved-register` | the saved register may be opened directly on the shared computer |
| authorization-10 | `record-request` | which section leader or part is recording may be taken on someone's say |
| authorization-11, authorization-12 | dropped | they need signing in, and "The register as it stands has no accounts"; the slice adds none |
| configuration: all | dropped | no criterion of the slice adds or changes a setting |
| logging-01 | `record-request` | someone may later ask whether and by whom an absence was recorded |
| logging-02 | `record-request` | a disputed absence needs enough kept to tell what happened |
| logging-03 | `kept-absence` | who will be away must not turn up where it should not |
| logging-04 | `singer-name` | a typed name may end up in a record |
| logging-05 | `record-request` | a record of a recording may fail to be written |
| logging-06 | `saved-register` | anything the register records about its use grows week by week |
| logging-07 | `refusal-message` | when recording fails, the leader needs to know without seeing internal detail |
| logging-08 | `saved-register` | any record kept on the hall computer is lost with it |
| logging-09 | `record-request` | a failed recording may need someone to be told |
| logging-10 | `saved-register` | anyone at the shared computer may be able to change what was recorded |
| logging-11 | `record-request` | any record of a recording takes its time from the computer's clock |
| logging-12 | `kept-absence` | any record naming who was away is kept for some length of time |
| accessibility-01 | `record-request` | a section leader may have only the keyboard |
| accessibility-02 | `record-request` | a keyboard user must be able to leave the recording |
| accessibility-03 | `record-request` | a keyboard user must see where they are before recording |
| accessibility-04 | `record-request` | what held the focus may go away once the absence is recorded or refused |
| accessibility-05 | `record-request` | the controls for who and which rehearsal need names for someone who cannot see them |
| accessibility-06 | `absence-view` | anything in the view that is not text needs words |
| accessibility-07 | `refusal-message` | someone who cannot see must learn that nothing was recorded |
| accessibility-08 | `absence-view` | a part with people missing might be marked by colour |
| accessibility-09 | `absence-view` | the names and numbers must be readable |
| accessibility-10 | `absence-view` | a reader may need much larger text on a small computer |
| accessibility-11, accessibility-12 | dropped | no criterion puts a time limit on a step or shows anything that moves |
| sign-in: all | dropped | the slice has no sign-in: "The register as it stands has no accounts", and singers do nothing in this slice |
| stored-data-01 | `kept-absence` | who will be away on which date is saved about named people |
| stored-data-02 | `saved-register` | names and absences sit on a computer several people use |
| stored-data-03 | `saved-register` | any protection of the saved names and absences would need a key |
| stored-data-04 | `saved-register` | losing such a key could lose the absences |
| stored-data-05 | `singer-name` | a name could travel in an address, and the documents do not say there is none |
| stored-data-06 | `absence-view` | something in between may keep a copy of the names shown |
| stored-data-08 | `absence-view` | the view shows names, and who needs to see them is open |
| stored-data-09 | `kept-absence` | past absences pile up with no stated end |
| stored-data-10 | `kept-absence` | absences are stored on the hall computer that section leaders use |
| stored-data-12 | `absence-view` | whether looking at who is away is recorded is not said |
| stored-data-07, stored-data-11 | dropped | "Outside systems: none." and nobody submits a file |
| file-intake: all | dropped | the slice accepts no file |
| misuse-01 | `record-request` | a recording may arrive without the singer or the rehearsal having been settled first |
| misuse-02 | `record-request` | the rules about unknown singers and past rehearsals need a place where they hold |
| misuse-03 | `record-request` | repeated recording could fill the register or distort the numbers; the documents do not rule it out |
| misuse-04 | `record-request` | many absences recorded at once would change what the programme is planned on |
| misuse-05 | `record-request` | one person alone can mark any number of singers as missing |
| misuse-07 | `record-request` | a recording must not change a singer's name, part or attendance |
| misuse-06, misuse-08 | dropped | nothing in the slice is costly to run or in limited supply |
