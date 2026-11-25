# Kept: slice 1

## What the slice creates and keeps
- singer-s-absence-from-a-rehearsal-told-in-advance: record-phoned-absence / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `singer-name` | text | the section leader, saying which singer; how it is given is not decided | singer-details | record-phoned-absence / 1 |
| `rehearsal-date` | date | the coming rehearsal; whether a person gives it is not decided | singer-details | record-phoned-absence / 1 |
| `stored-singer-name` | text | read back from the register | singer-details | record-phoned-absence / 2 |

## Other things the slice has
- `record-action`: the section leader's act of recording an absence (record-phoned-absence / 1)
- `confirmation`: what the section leader is shown once it is recorded (record-phoned-absence / 1)
- `refusal`: what the section leader is shown for a name the register does not hold (record-phoned-absence / 2)
- `phone-call`: the singer's call to a section leader, which the recording starts from (record-phoned-absence / 1)
- `saved-register`: what the register has saved on the hall's computer, and any copy of it (record-phoned-absence / 2)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external: all | dropped | The requirements say "Outside systems: none." |
| receive-external-data: all | dropped | The requirements say "Outside systems: none.", so nothing arrives from one. |
| sync: all | dropped | The slice keeps one register, "on a small computer at the church hall", and makes no second copy to update. |
| limits-01, limits-02, limits-09 | dropped | The requirements say "Outside systems: none." |
| limits-03, limits-04, limits-05, limits-10 | dropped | One section leader's recording is the whole action; the choir is "about 45 singers" and nothing is scheduled or shared out. |
| limits-06 | dropped | The slice's rules set no limit on use that could stop a person. |
| limits-07 | `singer-name` | The name given is the one item of open length that the slice accepts. |
| limits-08 | dropped | The slice shows one recorded absence and asks for no list. |
| limits-11, limits-12 | dropped | The slice holds no waiting work. |
| durable-write-01 | `register` | Recording an absence saves into a register that already holds singers and attendance. |
| durable-write-02 | `confirmation` | The section leader is told the absence is recorded. |
| durable-write-03 | `register` | Absences must survive on the hall's small computer. |
| durable-write-04 | `record-action` | Saving an absence can fail for lack of space on that computer. |
| durable-write-05 | `record-action` | The save of an absence can be reported as failed. |
| durable-write-06 | `register` | Saving an absence may replace what the register had saved. |
| durable-write-07 | `register` | Absences are added over time, and the last one may be incomplete. |
| durable-write-08 | `singer-s-absence-from-a-rehearsal-told-in-advance` | Each absence must agree with a singer and a rehearsal. |
| durable-write-09 | `register` | A saved absence or singer could change without anyone knowing. |
| durable-write-10 | `register` | A copy of the register may be taken while an absence is being saved. |
| durable-write-11 | `register` | Absences become part of the saved data that might be moved or restored. |
| durable-write-12 | `record-action` | The program or computer may be closed while an absence is being saved. |
| startup-read-01 | `register` | The register must be read to find the singer, and may be damaged. |
| startup-read-02 | `register` | What is found where the register should be may not be the register. |
| startup-read-03 | `register` | A register that cannot be opened must not pass for one with no singers. |
| startup-read-04 | `register` | An earlier recording may have been left unfinished. |
| startup-read-05 | `register` | The register may be readable but refuse a new absence. |
| startup-read-06 | `register` | Nothing says only one copy of the program can be running while damaged data is repaired. |
| startup-read-07 | `register` | Nothing says whether the hall's computer can remove the saved register by itself. |
| startup-read-08 | `register` | A rescued register may have lost or restored absences. |
| startup-read-09 | `register` | An absence against the wrong singer would be readable but wrong. |
| startup-read-10 | `register` | The slice relies on the saved register, which may become unusable. |
| migration-01 | `register` | The register as it works today may meet saved data that now holds absences. |
| migration-02 | `register` | The existing register must be carried into a version that records absences. |
| migration-03 | `register` | The previous program may be put back after an absence has been saved. |
| migration-04, migration-05, migration-12 | dropped | The register is on "a small computer at the church hall" and the program is "run by typed commands": no rollout runs versions side by side or carries long work over. |
| migration-06, migration-08, migration-09 | dropped | The slice adds absences; no criterion renames, redefines or discards anything stored. |
| migration-07 | `register` | The saved register has no value for absences today. |
| migration-10 | `register` | Bringing the existing register up to date for absences could fail partway. |
| migration-11 | `register` | An earlier copy of the register, with no absences, may be brought back. |
| concurrency-01 | `singer-s-absence-from-a-rehearsal-told-in-advance` | Several section leaders use the register, so two may record from what each saw earlier. |
| concurrency-02 | `singer-s-absence-from-a-rehearsal-told-in-advance` | An absence depends on the singer being in the register when it is saved. |
| concurrency-03, concurrency-04 | dropped | The slice reads one singer and one rehearsal, and no criterion removes either or decides from a changing set. |
| concurrency-05 | `confirmation` | Success must not be shown for a change that is later lost. |
| concurrency-06, concurrency-07, concurrency-10, concurrency-11 | dropped | The slice has no second view to refresh, no time-limited right and no operation holding several things or needing sole use while it waits. |
| concurrency-08 | `register` | The register may be in use by another command when an absence is recorded. |
| concurrency-09 | `record-action` | A recording that clashes with another change may be cancelled. |
| concurrency-12 | `register` | Nothing stops two copies of the program being run on the same register. |
| lifecycle-01, lifecycle-02, lifecycle-04, lifecycle-08, lifecycle-12 | dropped | Recording is one action in the criteria, with no later step, undoing, lasting in-progress state or hold. |
| lifecycle-03 | `record-action` | No document gives a way to take a recorded absence back. |
| lifecycle-05 | `singer-s-absence-from-a-rehearsal-told-in-advance` | An absence only makes sense with its singer and rehearsal. |
| lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11 | dropped | No criterion of the slice removes anything. |
| user-input-01 | `singer-name` | A section leader may give a name of any length. |
| user-input-02 | `record-action` | Which singer, and perhaps which date, is needed to record an absence. |
| user-input-03 | `singer-name` | Singers' names can contain varied characters. |
| user-input-04 | `singer-name` | A name may be given in full, in part or in another order. |
| user-input-05 | `record-action` | The singer must be in the register however the recording arrives. |
| user-input-06 | `refusal` | A name that is not in the register is refused. |
| user-input-07 | `singer-name` | The name may be empty or have spaces around it. |
| user-input-08 | dropped | The slice takes in no number. |
| user-input-09 | `singer-name` | The absence is attached by saying which singer, and two singers may share a name. |
| user-input-10 | `singer-name` | The name is shown back and used with stored data. |
| user-input-11 | `rehearsal-date` | The date must fit the rehearsal the absence is for. |
| user-input-12 | `rehearsal-date` | If the date is typed, it can be written in several ways. |
| user-action-01 | `record-action` | A section leader may record the same absence twice. |
| user-action-02, user-action-03 | `confirmation` | How recording is shown is not decided, so reloading or stepping back may be possible. |
| user-action-04, user-action-11 | dropped | The slice adds no sign-in; the program's description says "it has no accounts". |
| user-action-05 | `record-action` | A section leader may leave before the absence is saved. |
| user-action-06, user-action-07 | `record-action` | How recording is done is not decided; it may be left suspended or open more than once. |
| user-action-08 | `record-action` | A wrong singer may be recorded and no document gives an undo. |
| user-action-09 | `record-action` | Whether to confirm matters where a wrong recording cannot be undone. |
| user-action-10 | dropped | The criteria have one action, not a longer operation with steps. |
| user-action-12 | dropped | The slice adds no sign-in and no criterion returns to a saved screen. |
| long-operation: all | dropped | The slice records one absence in one action and has no long-running work. |
| time-01 | `rehearsal` | Working out which rehearsal is coming may depend on the computer's clock. |
| time-02, time-04, time-05 | dropped | The slice uses one computer, measures no span and takes in no time of day. |
| time-03 | `rehearsal` | A wrong or changed clock could change which rehearsal is coming. |
| time-06, time-09, time-11 | dropped | The slice stores a plain rehearsal date, counts no months and orders no events. |
| time-07 | `rehearsal-date` | The rehearsal date must not shift when saved or shown. |
| time-08 | `rehearsal-date` | Which day it is decides which rehearsal is coming. |
| time-10 | `rehearsal` | The choir rehearses every Thursday. |
| time-12 | `singer-s-absence-from-a-rehearsal-told-in-advance` | The phone call and its recording may happen at different times, either side of Tuesday evening. |
| text-01, text-02, text-03, text-04 | `singer-name` | The name given has to be matched with a name in the register. |
| text-05 | `singer-name` | A long name may be measured or cut. |
| text-06, text-07, text-08, text-11 | dropped | The slice orders no list and needs no word boundaries. |
| text-09, text-12 | `confirmation` | The singer's name is put into what the section leader is shown. |
| text-10 | `stored-singer-name` | A section leader may have to tell similar singers' names apart. |
| presentation-01, presentation-06, presentation-09 | `confirmation` | The section leader is shown the rehearsal date. |
| presentation-02, presentation-03, presentation-04, presentation-05 | dropped | The slice shows no amount or count. |
| presentation-07, presentation-08, presentation-10, presentation-11, presentation-12 | dropped | The slice shows no time of day, week or list. |
| corpus: all | dropped | The slice ships and uses no body of published content, only the choir's own register. |
| secrets: all | dropped | The slice uses no credential; the program's description says "it has no accounts". |
| authorization-01 | `record-action` | An absence is recorded in another person's name, and who may do it matters. |
| authorization-02 | `singer-name` | Whether a section leader may record for any singer or only some is not confirmed. |
| authorization-03, authorization-04, authorization-06, authorization-07 | `record-action` | It changes the register, and how it is reached and limited is not decided. |
| authorization-09 | `register` | The saved register may be reachable without going through the program. |
| authorization-05, authorization-08, authorization-10, authorization-11, authorization-12 | dropped | The slice checks no identity or permission: "this slice does not stop anyone else at that computer". |
| configuration: all | dropped | No criterion adds or changes a setting. |
| logging-01 | `record-action` | Someone may need to know that an absence was recorded or refused. |
| logging-02 | `record-action` | It may later matter who recorded an absence for whom, and when. |
| logging-03 | `singer-name` | A record of events could include singers' details. |
| logging-07 | `record-action` | Recording can fail, and the section leader must be shown something. |
| logging-04, logging-05, logging-06, logging-08, logging-09, logging-10, logging-11, logging-12 | dropped | No criterion makes the slice keep a log apart from the absence itself. |
| accessibility-01, accessibility-02, accessibility-03, accessibility-04, accessibility-05 | `record-action` | A section leader performs it, and how it is done is not decided. |
| accessibility-06, accessibility-07, accessibility-08, accessibility-09, accessibility-10 | `confirmation`; `refusal` | These are the two results a section leader must be able to take in. |
| accessibility-11, accessibility-12 | dropped | No criterion has a time limit or anything that moves. |
| sign-in: all | dropped | The slice adds no sign-in; the program's description says "it has no accounts". |
| stored-data-01 | `singer-s-absence-from-a-rehearsal-told-in-advance` | It says which named singer will be away. |
| stored-data-02 | `register` | The register and its copies hold singers' details. |
| stored-data-03, stored-data-04, stored-data-06, stored-data-07, stored-data-11 | dropped | The slice adds no key, sends nothing to another party or through one, and takes no file. |
| stored-data-05 | `singer-name` | How the name is passed is not decided. |
| stored-data-08 | `confirmation` | What is shown about a singer should be only what is needed. |
| stored-data-09 | `singer-s-absence-from-a-rehearsal-told-in-advance` | No document says how long an absence is kept. |
| stored-data-10 | `register` | The register with singers' details is stored on the hall's computer. |
| stored-data-12 | dropped | The slice adds no reading of stored details beyond confirming the singer just named. |
| file-intake: all | dropped | No person submits a file in this slice. |
| misuse-01, misuse-04, misuse-05, misuse-06, misuse-08 | dropped | Recording is one cheap step with no order of steps, speed rule, second approval or limited supply. |
| misuse-02 | `record-action` | The slice limits recording to a singer in the register and the coming rehearsal. |
| misuse-03 | `record-action` | Nothing says the recording cannot be repeated by a script. |
| misuse-07 | `record-action` | A recording must not set more than the absence. |
