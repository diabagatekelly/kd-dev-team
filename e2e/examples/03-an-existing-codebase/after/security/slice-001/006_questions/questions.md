# Questions

<!-- drawn from: 1762914767 -->

Drawn by script from kept.md and the slice's documents. Nothing here is answered.

## From the library

- L.limits-07.singer-name: singer-name: What is the largest single item the product accepts, and what happens to one that is larger?
- L.durable-write-01.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product guarantee is stored when a save is cut off partway: all of the old content, all of the new, or something it can detect and repair?
- L.durable-write-02.confirmation: confirmation: At what moment does the product say a change is saved, and how much recently confirmed work may be lost if power fails right after?
- L.durable-write-03.register: register (in each of its states: not-started, in-use, unavailable, ended): On what kinds of storage does the product promise its saved data survives a power loss, and how would it notice damage on storage that does not keep that promise?
- L.durable-write-04.record-action: record-action: What does the person see, and what state is the previously saved data in, when a save fails for lack of space?
- L.durable-write-05.record-action: record-action: What does the product do after storage reports a failed save, given that trying again and being told it worked does not prove the data is there?
- L.durable-write-06.register: register (in each of its states: not-started, in-use, unavailable, ended): When saved data is replaced wholesale, what is guaranteed to be found after a crash at any point during the replacement?
- L.durable-write-07.register: register (in each of its states: not-started, in-use, unavailable, ended): How does the product recognise and treat an incomplete or meaningless final record in a history it adds to over time?
- L.durable-write-08.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): Which pieces of saved data must always agree with one another, and what does the product do when it finds them disagreeing after a crash?
- L.durable-write-09.register: register (in each of its states: not-started, in-use, unavailable, ended): How does the product detect saved data that has silently changed since it was written, and what does it do with it?
- L.durable-write-10.register: register (in each of its states: not-started, in-use, unavailable, ended): How are copies of the saved data (backups, exports, device transfers) taken so that a copy made during a save is still usable?
- L.durable-write-11.register: register (in each of its states: not-started, in-use, unavailable, ended): Which files together make up the saved data, and what happens when only some of them are moved, copied, restored or cleaned up?
- L.durable-write-12.record-action: record-action: What happens to a save that is still in progress when the product is closed, and how does the person learn on return that it did not happen?
- L.startup-read-01.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product do at start when its saved data is damaged: refuse to run, run with what can be read, or start fresh, and what is the person told?
- L.startup-read-02.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product do when the thing in its saved-data location is not recognisably its own, and does it ever overwrite it?
- L.startup-read-03.register: register (in each of its states: not-started, in-use, unavailable, ended): How does the product tell a first run with nothing saved apart from saved data that exists but cannot be opened, and what does it do in each case?
- L.startup-read-04.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product do at start when it finds a save that an earlier run left unfinished: complete it, undo it, or ask?
- L.startup-read-05.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product do when it may read its saved data but not change it, including when that data needs repair first?
- L.startup-read-06.register: register (in each of its states: not-started, in-use, unavailable, ended): What does a starting copy of the product do when another copy is already repairing the saved data: wait, for how long, and what does it show meanwhile?
- L.startup-read-07.register: register (in each of its states: not-started, in-use, unavailable, ended): Where can the platform remove the product's saved data on its own, and what does the person find, and can get back, when that has happened?
- L.startup-read-08.register: register (in each of its states: not-started, in-use, unavailable, ended): After a rescue of damaged saved data, what is checked before the result is used, and how is the person told what may be missing, changed or back again?
- L.startup-read-09.register: register (in each of its states: not-started, in-use, unavailable, ended): How would the product or its owner find out that saved data is readable but wrong, and how far back can a good version be recovered?
- L.startup-read-10.register: register (in each of its states: not-started, in-use, unavailable, ended): Which spare copy does the product fall back on when its saved data is unusable, and when was bringing it back last actually tried?
- L.migration-01.register: register (in each of its states: not-started, in-use, unavailable, ended): What does a version of the product do when it meets saved data written by a later version: refuse, open it read-only, or use what it understands?
- L.migration-02.register: register (in each of its states: not-started, in-use, unavailable, ended): From how far back must saved data be carried forward, and what happens to data older than that: is it ever erased, and who agrees to that?
- L.migration-03.register: register (in each of its states: not-started, in-use, unavailable, ended): After a new version has saved anything, can the previous version still be put back, and what does it do with what the new one wrote?
- L.migration-07.register: register (in each of its states: not-started, in-use, unavailable, ended): For each value the new version expects, what do records saved before it existed get: a stated default, a marked blank, or a question to the person?
- L.migration-10.register: register (in each of its states: not-started, in-use, unavailable, ended): What state is the saved data in when bringing it up to date fails partway, and what does the product do the next time it starts?
- L.migration-11.register: register (in each of its states: not-started, in-use, unavailable, ended): Can spare copies taken under earlier versions still be brought back by the current version, and how long is that promised?
- L.concurrency-01.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): When two changes to the same item are made from what each saw earlier, which survives, and is the person whose change was replaced told?
- L.concurrency-02.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): Which rules span more than one item, and how are they kept true when two operations each change a different item at the same moment?
- L.concurrency-05.confirmation: confirmation: Can anything see or act on a change before it is final, and what happens to what was built on it if the change is withdrawn?
- L.concurrency-08.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product do when the stored data is in use by another operation: wait, try again, or tell the person, and for how long?
- L.concurrency-09.record-action: record-action: When an operation is cancelled because it clashed with another, is it repeated automatically from the start, and what if it cannot simply be repeated?
- L.concurrency-12.register: register (in each of its states: not-started, in-use, unavailable, ended): What stops two copies of the product from changing the same stored data at once, and in which setups (shared or remote storage, mixed versions) does that protection not hold?
- L.lifecycle-03.record-action: record-action: Which steps cannot be taken back once done, and is everything that could still fail checked before them?
- L.lifecycle-05.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): Which records only make sense as a pair or set, and how is one that exists without its partner found and dealt with?
- L.user-input-01.singer-name: singer-name: How long may each typed value be, and what does the person see when theirs is longer?
- L.user-input-02.record-action: record-action: Which fields are truly required, and what can a person do who has no value for one of them?
- L.user-input-03.singer-name: singer-name: Which characters does each field accept, and on what grounds is any character refused?
- L.user-input-04.singer-name: singer-name: Is each value asked for whole or in parts, and what happens when a person's value has fewer, more or differently ordered parts?
- L.user-input-05.record-action: record-action: Where is each rule about a typed value enforced, and what happens to a value that arrives without having passed the on-screen check?
- L.user-input-06.refusal: refusal: For each way a value can be refused, what does the message say and where does it appear?
- L.user-input-07.singer-name: singer-name: Is an empty or all-spaces value accepted, and are spaces around a value kept, removed or refused?
- L.user-input-09.singer-name: singer-name: Which values must be unique, how is sameness judged, and what is the person told when theirs is taken?
- L.user-input-10.singer-name: singer-name: Wherever typed text is later shown, stored or passed on, how is it kept from being acted on as anything but text?
- L.user-input-11.rehearsal-date: rehearsal-date: Which fields depend on one another, and what happens when their values do not agree?
- L.user-input-12.rehearsal-date: rehearsal-date: In which written forms may a number or a date be typed, and how is an ambiguous one settled?
- L.user-action-01.record-action: record-action: What does the person see at once after starting an operation, and what happens if they start it a second time before the first has finished?
- L.user-action-02.confirmation: confirmation: What does reloading do on each screen that follows an operation that changed something?
- L.user-action-03.confirmation: confirmation: What does each screen show, and what can be done from it, when it is reached by stepping back after the operation it led to?
- L.user-action-05.record-action: record-action: When are a person's changes saved, and what becomes of unsaved ones when they leave without warning the product?
- L.user-action-06.record-action: record-action: What does a person find when they come back to a screen their device has suspended or discarded in the meantime?
- L.user-action-07.record-action: record-action: When the same person has several windows open, how does each learn of a change made in another, and which one wins if both act?
- L.user-action-08.record-action: record-action: Which actions can be undone, for how long, and what can a person do about one that cannot?
- L.user-action-09.record-action: record-action: Which actions ask for confirmation, and why will a person still read the question on the one that matters?
- L.time-01.rehearsal: rehearsal (in each of its states: coming, held, not-held): Which behaviours depend on the device's own clock, and what happens to each when that clock is wrong?
- L.time-03.rehearsal: rehearsal (in each of its states: coming, held, not-held): What do waits, expiries and the order of events do when the clock is set back or leaps ahead?
- L.time-07.rehearsal-date: rehearsal-date: Which values are plain dates or plain times with no zone, and how are they kept from shifting when stored, moved or shown?
- L.time-08.rehearsal-date: rehearsal-date: Whose time zone governs each date and time the product handles, and what changes when a person's zone does?
- L.time-10.rehearsal: rehearsal (in each of its states: coming, held, not-held): How is each occurrence of a repeating schedule worked out, so that it stays at the intended local time all year?
- L.time-12.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): For each recorded time, is it when the thing happened or when it was recorded, and which of the two do later decisions use?
- L.text-01.singer-name: singer-name: When are two pieces of text counted as the same, and is that settled before they are stored or each time they are compared?
- L.text-02.singer-name: singer-name: Where does the product ignore the difference between capital and small letters, and by which language's rules?
- L.text-03.singer-name: singer-name: What does the product do with unseen characters and unusual spaces in text it stores and compares?
- L.text-04.singer-name: singer-name: Which differences does search ignore (accent marks, letter size, alternative ways of writing the same word) and which must match exactly?
- L.text-05.singer-name: singer-name: How does the product measure the length of text, and where may it cut text that is too long?
- L.text-09.confirmation: confirmation: Wherever a stored or typed value is put into a sentence or a row, what keeps text of the opposite direction from disturbing what surrounds it?
- L.text-12.confirmation: confirmation: How much room does each label and message have, and what happens when the wording in another language is longer or taller?
- L.text-10.stored-singer-name: stored-singer-name: Where must people tell names or labels apart by eye, and what stops one being made to look like another?
- L.presentation-01.confirmation: confirmation: In what form is each date shown, and could a reader anywhere take it for another day?
- L.presentation-06.confirmation: confirmation: Which digit shapes does the product show, and is that the reader's choice?
- L.presentation-09.confirmation: confirmation: Which calendar or calendars does the product show dates in, and what does a reader who uses another one see?
- L.authorization-01.record-action: record-action: For every operation and every kind of data, who is allowed, and where is that checked?
- L.authorization-02.singer-name: singer-name: How does the product confirm that the particular record asked for belongs to, or is shared with, the person asking?
- L.authorization-03.record-action: record-action: Where is each permission enforced, and what happens to a request that bypasses the screen?
- L.authorization-04.record-action: record-action: What may a person do when no rule mentions them or the thing they ask for?
- L.authorization-06.record-action: record-action: How does the product tell a request the person meant to make from one sent in their name by someone else's page?
- L.authorization-07.record-action: record-action: Which operations change something, and can any of them happen just because a link was followed or a page was loaded?
- L.authorization-09.register: register (in each of its states: not-started, in-use, unavailable, ended): Who may fetch each stored file directly, and is that checked the same way as the screen that shows it?
- L.logging-01.record-action: record-action: Which events must always leave a record?
- L.logging-02.record-action: record-action: What must every record say so that someone can later tell what happened and to whom?
- L.logging-03.singer-name: singer-name: Which values must never appear in a record, and how are they kept out?
- L.logging-07.record-action: record-action: When something fails, what does the person see and what goes only into the records?
- L.accessibility-01.record-action: record-action: For each thing a person can do on the screen, how is it done using the keyboard alone?
- L.accessibility-02.record-action: record-action: From every part of the screen a keyboard user can enter, how do they leave it?
- L.accessibility-03.record-action: record-action: How is the item that has keyboard focus shown, on every item that can take it?
- L.accessibility-04.record-action: record-action: Where does focus go when the item holding it closes or is removed?
- L.accessibility-05.record-action: record-action: What name and purpose does each control announce to someone who cannot see it?
- L.accessibility-06.confirmation: confirmation: For everything shown that is not text, what words give the same meaning?
- L.accessibility-06.refusal: refusal: For everything shown that is not text, what words give the same meaning?
- L.accessibility-07.confirmation: confirmation: How does someone who cannot see the screen learn the result of what they just did?
- L.accessibility-07.refusal: refusal: How does someone who cannot see the screen learn the result of what they just did?
- L.accessibility-08.confirmation: confirmation: Wherever colour carries meaning, what else on the screen carries the same meaning?
- L.accessibility-08.refusal: refusal: Wherever colour carries meaning, what else on the screen carries the same meaning?
- L.accessibility-09.confirmation: confirmation: What contrast between text and its background does every screen keep, in every state and theme?
- L.accessibility-09.refusal: refusal: What contrast between text and its background does every screen keep, in every state and theme?
- L.accessibility-10.confirmation: confirmation: What happens to each screen when its text is enlarged to twice its size?
- L.accessibility-10.refusal: refusal: What happens to each screen when its text is enlarged to twice its size?
- L.stored-data-01.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): Which data the product creates or holds would harm someone if seen or changed, and how strongly must each kind be protected?
- L.stored-data-02.register: register (in each of its states: not-started, in-use, unavailable, ended): Who could read each kind of sensitive data where it is stored and in every copy made of it, and what makes it unreadable to anyone else?
- L.stored-data-05.singer-name: singer-name: Does any sensitive value travel in an address or its query, and where would that be recorded?
- L.stored-data-08.confirmation: confirmation: For each reply, which fields are sent, and is any sent that the asker does not need or may not see?
- L.stored-data-09.singer-s-absence-from-a-rehearsal-told-in-advance: singer-s-absence-from-a-rehearsal-told-in-advance (in each of its states: being-recorded, recorded, withdrawn, rehearsal-past): How long is each kind of sensitive data kept, and what removes it when that time is up?
- L.stored-data-10.register: register (in each of its states: not-started, in-use, unavailable, ended): What does the product store on the person's device, and is any of it sensitive?
- L.misuse-02.record-action: record-action: What limits does each rule of the product set, and where is each enforced?
- L.misuse-03.record-action: record-action: What could a script do by calling the product again and again, and what stops it?
- L.misuse-07.record-action: record-action: Which fields may each request set, and what happens to a field that is sent and was not meant to be set?

## Each value taken in, each way it can be wrong

- V.singer-name.missing: `singer-name` (the section leader, saying which singer; how it is given is not decided) is missing, or null: what does the product do, and what is the person told?
- V.rehearsal-date.empty: `rehearsal-date` (the coming rehearsal; whether a person gives it is not decided) is empty: what does the product do, and what is the person told?
- V.rehearsal-date.missing: `rehearsal-date` (the coming rehearsal; whether a person gives it is not decided) is missing, or null: what does the product do, and what is the person told?
- V.rehearsal-date.malformed: `rehearsal-date` (the coming rehearsal; whether a person gives it is not decided) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.rehearsal-date.edge: `rehearsal-date` (the coming rehearsal; whether a person gives it is not decided) is at the very edge of what is allowed: what does the product do, and what is the person told?
- V.rehearsal-date.outside: `rehearsal-date` (the coming rehearsal; whether a person gives it is not decided) is outside what is allowed: what does the product do, and what is the person told?
- V.stored-singer-name.empty: `stored-singer-name` (read back from the register) is empty: what does the product do, and what is the person told?
- V.stored-singer-name.missing: `stored-singer-name` (read back from the register) is missing, or null: what does the product do, and what is the person told?
- V.stored-singer-name.long: `stored-singer-name` (read back from the register) is far longer or larger than expected: what does the product do, and what is the person told?
- V.stored-singer-name.twice: `stored-singer-name` (read back from the register) is the same as one already there: what does the product do, and what is the person told?
- V.stored-singer-name.characters: `stored-singer-name` (read back from the register) holds unusual characters or another encoding: what does the product do, and what is the person told?
- V.every-setting.missing: any setting the build reads is missing, or null: what does the product do at start, and who is told?
- V.every-setting.empty: any setting the build reads is empty: what does the product do at start, and who is told?
- V.every-setting.malformed: any setting the build reads is of the wrong type or malformed: what does the product do at start, and who is told?
- V.every-setting.outside: any setting the build reads is outside what is allowed: what does the product do at start, and who is told?
Not drawn, 4 already asked of the same thing by a library question above.

## Each class of sensitive values, each place it can leak to

- X.singer-details.logs: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach what the product logs, on the path that works and on each that fails?
- X.singer-details.errors-inside: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach an error's own message and trace, on the path that works and on each that fails?
- X.singer-details.errors-shown: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach an error shown or returned to whoever asked, on the path that works and on each that fails?
- X.singer-details.telemetry: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach what is sent to monitoring or measurement, on the path that works and on each that fails?
- X.singer-details.samples: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach test data and examples kept with the code, on the path that works and on each that fails?
- X.singer-details.replies: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach a reply that succeeded, to whoever asked, on the path that works and on each that fails?
- X.singer-details.stored: can any of `singer-name`, `rehearsal-date`, `stored-singer-name` reach where it is stored, and every copy made of that, on the path that works and on each that fails?

## Each state, each event

- S.register.not-started.record-phoned-absence-1: The register is `not-started` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.register.not-started.record-phoned-absence-2: The register is `not-started` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.register.not-started.again: The register is `not-started` and the same action is done again at once: what happens to it, and what is the person shown?
- S.register.not-started.reopened: The register is `not-started` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.register.not-started.time: The register is `not-started` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.register.in-use.record-phoned-absence-1: The register is `in-use` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.register.in-use.record-phoned-absence-2: The register is `in-use` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.register.in-use.again: The register is `in-use` and the same action is done again at once: what happens to it, and what is the person shown?
- S.register.in-use.reopened: The register is `in-use` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.register.in-use.time: The register is `in-use` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.register.unavailable.record-phoned-absence-1: The register is `unavailable` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.register.unavailable.record-phoned-absence-2: The register is `unavailable` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.register.unavailable.again: The register is `unavailable` and the same action is done again at once: what happens to it, and what is the person shown?
- S.register.unavailable.reopened: The register is `unavailable` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.register.unavailable.time: The register is `unavailable` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.register.ended.record-phoned-absence-1: The register is `ended` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.register.ended.record-phoned-absence-2: The register is `ended` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.register.ended.again: The register is `ended` and the same action is done again at once: what happens to it, and what is the person shown?
- S.register.ended.reopened: The register is `ended` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.register.ended.time: The register is `ended` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.record-phoned-absence-1: A singer, with their voice part is `in-register` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.record-phoned-absence-2: A singer, with their voice part is `in-register` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.again: A singer, with their voice part is `in-register` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.reopened: A singer, with their voice part is `in-register` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.restart: A singer, with their voice part is `in-register` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.second: A singer, with their voice part is `in-register` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.in-register.time: A singer, with their voice part is `in-register` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.record-phoned-absence-1: A singer, with their voice part is `not-in-register` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.record-phoned-absence-2: A singer, with their voice part is `not-in-register` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.again: A singer, with their voice part is `not-in-register` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.reopened: A singer, with their voice part is `not-in-register` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.restart: A singer, with their voice part is `not-in-register` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.second: A singer, with their voice part is `not-in-register` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.not-in-register.time: A singer, with their voice part is `not-in-register` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.record-phoned-absence-1: A singer, with their voice part is `left-choir` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.record-phoned-absence-2: A singer, with their voice part is `left-choir` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.again: A singer, with their voice part is `left-choir` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.reopened: A singer, with their voice part is `left-choir` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.restart: A singer, with their voice part is `left-choir` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.second: A singer, with their voice part is `left-choir` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.singer-with-their-voice-part.left-choir.time: A singer, with their voice part is `left-choir` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.rehearsal.coming.record-phoned-absence-1: A rehearsal is `coming` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.coming.record-phoned-absence-2: A rehearsal is `coming` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.coming.again: A rehearsal is `coming` and the same action is done again at once: what happens to it, and what is the person shown?
- S.rehearsal.coming.reopened: A rehearsal is `coming` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.rehearsal.coming.restart: A rehearsal is `coming` and the product stops and starts again: what happens to it, and what is the person shown?
- S.rehearsal.coming.second: A rehearsal is `coming` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.rehearsal.coming.time: A rehearsal is `coming` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.rehearsal.held.record-phoned-absence-1: A rehearsal is `held` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.held.record-phoned-absence-2: A rehearsal is `held` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.held.again: A rehearsal is `held` and the same action is done again at once: what happens to it, and what is the person shown?
- S.rehearsal.held.reopened: A rehearsal is `held` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.rehearsal.held.restart: A rehearsal is `held` and the product stops and starts again: what happens to it, and what is the person shown?
- S.rehearsal.held.second: A rehearsal is `held` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.rehearsal.held.time: A rehearsal is `held` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.rehearsal.not-held.record-phoned-absence-1: A rehearsal is `not-held` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.not-held.record-phoned-absence-2: A rehearsal is `not-held` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.rehearsal.not-held.again: A rehearsal is `not-held` and the same action is done again at once: what happens to it, and what is the person shown?
- S.rehearsal.not-held.reopened: A rehearsal is `not-held` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.rehearsal.not-held.restart: A rehearsal is `not-held` and the product stops and starts again: what happens to it, and what is the person shown?
- S.rehearsal.not-held.second: A rehearsal is `not-held` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.rehearsal.not-held.time: A rehearsal is `not-held` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.record-phoned-absence-1: A singer's absence from a rehearsal, told in advance is `being-recorded` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.record-phoned-absence-2: A singer's absence from a rehearsal, told in advance is `being-recorded` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.again: A singer's absence from a rehearsal, told in advance is `being-recorded` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.reopened: A singer's absence from a rehearsal, told in advance is `being-recorded` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.restart: A singer's absence from a rehearsal, told in advance is `being-recorded` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.being-recorded.time: A singer's absence from a rehearsal, told in advance is `being-recorded` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.record-phoned-absence-1: A singer's absence from a rehearsal, told in advance is `recorded` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.record-phoned-absence-2: A singer's absence from a rehearsal, told in advance is `recorded` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.again: A singer's absence from a rehearsal, told in advance is `recorded` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.reopened: A singer's absence from a rehearsal, told in advance is `recorded` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.restart: A singer's absence from a rehearsal, told in advance is `recorded` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.recorded.time: A singer's absence from a rehearsal, told in advance is `recorded` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.record-phoned-absence-1: A singer's absence from a rehearsal, told in advance is `withdrawn` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.record-phoned-absence-2: A singer's absence from a rehearsal, told in advance is `withdrawn` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.again: A singer's absence from a rehearsal, told in advance is `withdrawn` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.reopened: A singer's absence from a rehearsal, told in advance is `withdrawn` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.restart: A singer's absence from a rehearsal, told in advance is `withdrawn` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn.time: A singer's absence from a rehearsal, told in advance is `withdrawn` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.record-phoned-absence-1: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and what record-phoned-absence / 1 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.record-phoned-absence-2: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and what record-phoned-absence / 2 describes is done: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.again: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and the same action is done again at once: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.reopened: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.restart: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and the product stops and starts again: what happens to it, and what is the person shown?
- S.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past.time: A singer's absence from a rehearsal, told in advance is `rehearsal-past` and a long time passes with nothing done: what happens to it, and what is the person shown?
Not drawn, 12 already asked of the same thing by a library question above.

## By what the slice is

- F.browser.context: What stops a reply meant as data, or a file someone submitted, from being shown and run as a page when its address is opened directly?
- F.browser.page-policy: From where may the page load and run code, and what does the browser do with anything else?
- F.browser.framing: May another site show this product inside a page of its own, and what prevents it?
- F.browser.type-guessing: How is the browser kept from treating a reply as a different type from the one it was sent as?
- F.browser.came-from: What does the browser tell other sites about the address a person came from, and is anything sensitive in that address?
- F.browser.other-sites: Which other sites' pages may call this product and read its replies, and how are all the rest refused?
- F.browser.messages: Does the page take messages from other windows, and how does it know which to trust?
- F.browser.others-code: Which code or styles on the page come from another party, and what stops a changed copy from running with everything the page can reach?
- F.browser.sent-on: Can the product send a person on to an address that someone else supplied?
- F.browser.kept-by-browser: What does the browser keep of a page that showed sensitive data, and for how long?
- F.browser.known-by: What does the product keep in the browser to know a person by, and what else can read it or cause it to be sent?
- F.network.answers-to: At which addresses and under which host names does the product answer, and what does it do with a request that names another?
- F.network.transport: Is every connection to it encrypted, and what happens to one that is not?
- F.network.in-between: Which facts about a request does it take from something in between (the sender's address, the host first asked for), and can the sender set them?
- F.network.kinds-of-request: Which kinds of request does each address accept, and what happens to the others?
- F.network.left-on: What can be reached that nobody meant to offer: a diagnostic mode, a listing of files, the history of the source, pages of documentation or measurement, test code?
- F.network.gives-away: What does a reply reveal about what the product is built from, a refusal included?
- F.dependency.known-flaw: When a component the product uses is found to have a known flaw, how is that learned, and how soon is the component replaced?
- F.dependency.inventory: Is there a list of every component used, those they bring with them included, and of where each comes from?
- F.dependency.look-alike: What makes sure each component is fetched from the place intended, and is the one intended?
- F.dependency.trusted-most: Which components are trusted with the most (they see credentials, read outside data, run when installed), and what limits them?
- F.several-people.fields: Within a record a person may see or change, are there fields they may not?
- F.several-people.groups: Can one group's use ever show or change what belongs to another group?

## What someone who means harm would want

- T.singer-s-absence-from-a-rehearsal-told-in-advance.phone-call: someone after `singer-s-absence-from-a-rehearsal-told-in-advance` comes through `phone-call`: Someone phones as a singer who means to come, and that singer is recorded as absent, so the programme may be changed for no reason. What stops it, and how would anyone know it was tried?
- T.singer-details.phone-call: someone after `singer-details` comes through `phone-call`: A caller learns from a section leader whether a named singer will be away. What stops it, and how would anyone know it was tried?
- T.singer-s-absence-from-a-rehearsal-told-in-advance.record-action: someone after `singer-s-absence-from-a-rehearsal-told-in-advance` comes through `record-action`: Someone other than a section leader records false absences, and a voice part appears short when it is not. What stops it, and how would anyone know it was tried?
- T.singer-details.record-action: someone after `singer-details` comes through `record-action`: Someone tries names to learn who is in the choir. What stops it, and how would anyone know it was tried?
- T.singer-details.confirmation: someone after `singer-details` comes through `confirmation`: Someone who sees the screen or what it leaves behind learns that a named singer will be away on a given evening. What stops it, and how would anyone know it was tried?
- T.singer-details.refusal: someone after `singer-details` comes through `refusal`: From which names are refused and which are not, an outsider learns who sings in the choir. What stops it, and how would anyone know it was tried?
- T.singer-details.saved-register: someone after `singer-details` comes through `saved-register`: Someone who reaches the saved register or a copy of it learns who the singers are and when they will be away. What stops it, and how would anyone know it was tried?
- T.register.record-action: someone after `register` comes through `record-action`: What someone gives as a name or date damages the register, and the section leaders lose its singers and attendance. What stops it, and how would anyone know it was tried?

## Asked of every slice

- W.unavailable: What happens, and to whom, if what this slice adds cannot be used for an hour?
- W.target: How often may it fail, and how slow is too slow, before someone would say it does not work?
- W.noticed: Who notices when it breaks, and how?
- W.sensitive: What does this slice touch that would harm someone if another person saw or changed it?
- W.who-sees: Who uses it, and may any of them see or change what belongs to another?
- W.obligations: Does a law, a contract or an outside system's terms bind how this is handled?
- W.prize: What would someone who means harm want from what this slice adds?

## Carried from research

- C.states.register.not-started: The register, `not-started`: not said in the documents (not said in the documents | not said in the documents | none | not said in the documents)
- C.states.register.in-use: The register, `in-use`: not said in the documents (not said in the documents | Section leaders use it on the hall's computer. It keeps singers with their voice parts, and who came on a date. | none needed: it is the register's working state | 002_requirements.md, lines 9, 10 and 16)
- C.states.register.unavailable: The register, `unavailable`: not said in the documents (not said in the documents (the computer or the register cannot be used) | not said in the documents | none | not said in the documents)
- C.states.register.ended: The register, `ended`: not said in the documents (not said in the documents | not said in the documents, including what is left | none | not said in the documents)
- C.states.singer-with-their-voice-part.in-register: A singer, with their voice part, `in-register`: not said in the documents (not said in the documents | A section leader can record a phoned absence for the singer. | none | 002_requirements.md, line 9; slice-001/004_slice.md, line 9)
- C.states.singer-with-their-voice-part.not-in-register: A singer, with their voice part, `not-in-register`: not said in the documents (not said in the documents | An attempt to record an absence is refused, and nothing is recorded. | none | slice-001/004_slice.md, line 10)
- C.states.singer-with-their-voice-part.left-choir: A singer, with their voice part, `left-choir`: not said in the documents (not said in the documents | not said in the documents, including what happens to the singer's records | none | not said in the documents)
- C.states.rehearsal.coming: A rehearsal, `coming`: not said in the documents (We rehearse every Thursday. How a particular date gets into the register, or whether it needs to, is not said. | A section leader can record that a singer will miss it. | not said in the documents | 000_problem.md, line 5; slice-001/004_slice.md, line 4)
- C.states.rehearsal.held: A rehearsal, `held`: not said in the documents (not said in the documents | The register records who came on its date. | none | 002_requirements.md, line 10)
- C.states.rehearsal.not-held: A rehearsal, `not-held`: not said in the documents (not said in the documents: whether any Thursday has no rehearsal is not confirmed | not said in the documents | none | 002_requirements.md, line 33)
- C.states.singer-s-absence-from-a-rehearsal-told-in-advance.withdrawn: A singer's absence from a rehearsal, told in advance, `withdrawn`: not said in the documents (not said in the documents: whether a wrong notice, or one for a singer who can now come, is put right is not confirmed | not said in the documents | none | 002_requirements.md, line 28)
- C.states.singer-s-absence-from-a-rehearsal-told-in-advance.rehearsal-past: A singer's absence from a rehearsal, told in advance, `rehearsal-past`: not said in the documents (not said in the documents | not said in the documents, including whether the absence is kept and whether the singer coming after all changes it | none | not said in the documents)
- C.states.dead-end.1: for the owner's list: `not-started`: no way out. The documents do not say how a register begins, or what can be done before it does.
- C.states.dead-end.2: for the owner's list: `unavailable`: no way out. The documents do not say how absences are recorded meanwhile, or how the register comes back.
- C.states.dead-end.3: for the owner's list: `ended`: no way out. The documents do not say how the register is ended or what is left.
- C.states.dead-end.4: for the owner's list: `in-register`: no way out. The documents do not say how a singer is removed or their voice part changed, so the singer stays as recorded.
- C.states.dead-end.5: for the owner's list: `not-in-register`: no way out. No absence can be recorded for that name, and the documents for this activity do not say how a singer is added.
- C.states.dead-end.6: for the owner's list: `left-choir`: no way out. The documents do not say what happens to the singer or their records.
- C.states.dead-end.7: for the owner's list: `coming`: no way out stated. The documents do not say when a rehearsal stops being the coming one.
- C.states.dead-end.8: for the owner's list: `held`: no way out. The documents do not say how long its records are kept.
- C.states.dead-end.9: for the owner's list: `not-held`: no way out. The documents do not say what happens to absences recorded for that date.
- C.states.dead-end.10: for the owner's list: `recorded`: no way out. A wrong or outdated absence stays recorded, since no document gives a way to change or remove it.
- C.states.dead-end.11: for the owner's list: `withdrawn`: no way out. The documents do not say that an absence can be withdrawn or what would be left.
- C.states.dead-end.12: for the owner's list: `rehearsal-past`: no way out. The documents do not say what becomes of the absence after the rehearsal.
