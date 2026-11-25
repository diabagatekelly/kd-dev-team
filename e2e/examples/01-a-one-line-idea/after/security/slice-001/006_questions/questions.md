# Questions

<!-- drawn from: 3074762779 -->

Drawn by script from kept.md and the slice's documents. Nothing here is answered.

## From the library

- L.sync-04.shown-list: shown-list: How does a person know how old the information in front of them is, and what is shown when there is none yet?
- L.limits-04.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What is the most the product is meant to handle at one time, and what does it do with demand beyond that?
- L.limits-07.person-name: person-name: What is the largest single item the product accepts, and what happens to one that is larger?
- L.limits-08.shown-list: shown-list: How many items may be asked for or shown in one go, and how does a person reach the rest?
- L.limits-09.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What is the most the product may spend on each paid outside service in a period, who is warned as it approaches, and what stops at the ceiling?
- L.durable-write-01.carry-over: carry-over: What does the product guarantee is stored when a save is cut off partway: all of the old content, all of the new, or something it can detect and repair?
- L.durable-write-02.carry-over: carry-over: At what moment does the product say a change is saved, and how much recently confirmed work may be lost if power fails right after?
- L.durable-write-03.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): On what kinds of storage does the product promise its saved data survives a power loss, and how would it notice damage on storage that does not keep that promise?
- L.durable-write-04.carry-over: carry-over: What does the person see, and what state is the previously saved data in, when a save fails for lack of space?
- L.durable-write-05.carry-over: carry-over: What does the product do after storage reports a failed save, given that trying again and being told it worked does not prove the data is there?
- L.durable-write-08.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which pieces of saved data must always agree with one another, and what does the product do when it finds them disagreeing after a crash?
- L.durable-write-09.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): How does the product detect saved data that has silently changed since it was written, and what does it do with it?
- L.durable-write-10.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): How are copies of the saved data (backups, exports, device transfers) taken so that a copy made during a save is still usable?
- L.durable-write-11.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which files together make up the saved data, and what happens when only some of them are moved, copied, restored or cleaned up?
- L.durable-write-12.carry-over: carry-over: What happens to a save that is still in progress when the product is closed, and how does the person learn on return that it did not happen?
- L.startup-read-01.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What does the product do at start when its saved data is damaged: refuse to run, run with what can be read, or start fresh, and what is the person told?
- L.startup-read-02.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What does the product do when the thing in its saved-data location is not recognisably its own, and does it ever overwrite it?
- L.startup-read-03.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): How does the product tell a first run with nothing saved apart from saved data that exists but cannot be opened, and what does it do in each case?
- L.startup-read-04.carry-over: carry-over: What does the product do at start when it finds a save that an earlier run left unfinished: complete it, undo it, or ask?
- L.startup-read-05.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What does the product do when it may read its saved data but not change it, including when that data needs repair first?
- L.startup-read-07.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Where can the platform remove the product's saved data on its own, and what does the person find, and can get back, when that has happened?
- L.startup-read-08.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): After a rescue of damaged saved data, what is checked before the result is used, and how is the person told what may be missing, changed or back again?
- L.startup-read-09.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): How would the product or its owner find out that saved data is readable but wrong, and how far back can a good version be recovered?
- L.startup-read-10.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which spare copy does the product fall back on when its saved data is unusable, and when was bringing it back last actually tried?
- L.migration-01.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What does a version of the product do when it meets saved data written by a later version: refuse, open it read-only, or use what it understands?
- L.migration-03.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): After a new version has saved anything, can the previous version still be put back, and what does it do with what the new one wrote?
- L.concurrency-01.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): When two changes to the same item are made from what each saw earlier, which survives, and is the person whose change was replaced told?
- L.concurrency-12.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What stops two copies of the product from changing the same stored data at once, and in which setups (shared or remote storage, mixed versions) does that protection not hold?
- L.lifecycle-01.carry-over: carry-over: When making something takes several steps and a later one fails, what is done about the steps already carried out, and who decides between undoing them and carrying on another way?
- L.lifecycle-03.carry-over: carry-over: Which steps cannot be taken back once done, and is everything that could still fail checked before them?
- L.lifecycle-04.carry-over: carry-over: How long may a thing stay in progress before the product treats the work as failed, and what then happens to it?
- L.lifecycle-05.person-s-place-on-the-list: person-s-place-on-the-list (in each of its states: in-notebook, carried-place, newly-joined, moved, taken-off): Which records only make sense as a pair or set, and how is one that exists without its partner found and dealt with?
- L.lifecycle-08.carry-over: carry-over: How long is something that was started and then abandoned kept, and what removes it afterwards?
- L.lifecycle-11.person-name: person-name: By when is a removed thing truly gone from every place it was kept, and how does that deadline fit with the period in which it can be restored?
- L.user-input-01.person-name: person-name: How long may each typed value be, and what does the person see when theirs is longer?
- L.user-input-02.person-name: person-name: Which fields are truly required, and what can a person do who has no value for one of them?
- L.user-input-03.person-name: person-name: Which characters does each field accept, and on what grounds is any character refused?
- L.user-input-04.person-name: person-name: Is each value asked for whole or in parts, and what happens when a person's value has fewer, more or differently ordered parts?
- L.user-input-05.carry-over: carry-over: Where is each rule about a typed value enforced, and what happens to a value that arrives without having passed the on-screen check?
- L.user-input-06.carry-over: carry-over: For each way a value can be refused, what does the message say and where does it appear?
- L.user-input-07.person-name: person-name: Is an empty or all-spaces value accepted, and are spaces around a value kept, removed or refused?
- L.user-input-09.person-name: person-name: Which values must be unique, how is sameness judged, and what is the person told when theirs is taken?
- L.user-input-10.person-name: person-name: Wherever typed text is later shown, stored or passed on, how is it kept from being acted on as anything but text?
- L.user-input-11.notebook-order: notebook-order: Which fields depend on one another, and what happens when their values do not agree?
- L.user-action-01.carry-over: carry-over: What does the person see at once after starting an operation, and what happens if they start it a second time before the first has finished?
- L.user-action-02.shown-list: shown-list: What does reloading do on each screen that follows an operation that changed something?
- L.user-action-03.shown-list: shown-list: What does each screen show, and what can be done from it, when it is reached by stepping back after the operation it led to?
- L.user-action-05.carry-over: carry-over: When are a person's changes saved, and what becomes of unsaved ones when they leave without warning the product?
- L.user-action-06.carry-over: carry-over: What does a person find when they come back to a screen their device has suspended or discarded in the meantime?
- L.user-action-07.carry-over: carry-over: When the same person has several windows open, how does each learn of a change made in another, and which one wins if both act?
- L.user-action-08.carry-over: carry-over: Which actions can be undone, for how long, and what can a person do about one that cannot?
- L.user-action-09.carry-over: carry-over: Which actions ask for confirmation, and why will a person still read the question on the one that matters?
- L.user-action-10.carry-over: carry-over: At each step of a longer operation, how does a person back out, and what is left behind if they do or simply leave?
- L.user-action-04.shown-list: shown-list: What remains visible on the device after a person signs out, including on screens reached by stepping back?
- L.user-action-11.carry-over: carry-over: What happens to work in progress when a person's signed-in period ends, and can they carry on after signing in again?
- L.user-action-12.shown-list: shown-list: What does a saved address to each screen lead to when the person is signed out, or when what it pointed at no longer exists?
- L.long-operation-04.carry-over: carry-over: When an operation is stopped partway, is the finished part undone, kept or completed later, and how is it shown?
- L.long-operation-06.carry-over: carry-over: After an interruption in the middle of an operation, does it resume, restart or stay abandoned, and what state is left meanwhile?
- L.long-operation-08.carry-over: carry-over: When only some items of an operation succeed, what is kept, what is reported, and how are the failed ones tried again?
- L.text-01.person-name: person-name: When are two pieces of text counted as the same, and is that settled before they are stored or each time they are compared?
- L.text-02.person-name: person-name: Where does the product ignore the difference between capital and small letters, and by which language's rules?
- L.text-03.person-name: person-name: What does the product do with unseen characters and unusual spaces in text it stores and compares?
- L.text-05.person-name: person-name: How does the product measure the length of text, and where may it cut text that is too long?
- L.text-09.shown-list: shown-list: Wherever a stored or typed value is put into a sentence or a row, what keeps text of the opposite direction from disturbing what surrounds it?
- L.text-10.shown-list: shown-list: Where must people tell names or labels apart by eye, and what stops one being made to look like another?
- L.presentation-04.shown-list: shown-list: How is wording that includes a count chosen for zero, one and each other form the reader's language has?
- L.presentation-12.shown-list: shown-list: When a list too long for one screen is put in order, does the order hold across all of it?
- L.secrets-01.shown-list: shown-list: Where does each credential the product uses live, and who can read that place?
- L.secrets-02.shown-list: shown-list: Which credentials are unique to each installation or person, and how does each one come to be set?
- L.secrets-03.shown-list: shown-list: How is each credential kept out of everything the product records or prints, and what is done when one is found there?
- L.secrets-05.shown-list: shown-list: When a credential is exposed, who cancels it, how fast, and what stops working until the new one is in place?
- L.secrets-06.shown-list: shown-list: What does the product do and tell the person when a credential it holds is no longer accepted?
- L.secrets-09.shown-list: shown-list: In what form is each credential stored and sent, and who could read it on the way or at rest?
- L.secrets-11.shown-list: shown-list: What does the product do when the place its credentials are kept cannot be reached, and how are they recovered if it is lost?
- L.authorization-01.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): For every operation and every kind of data, who is allowed, and where is that checked?
- L.authorization-02.shown-list: shown-list: How does the product confirm that the particular record asked for belongs to, or is shared with, the person asking?
- L.authorization-03.shown-list: shown-list: Where is each permission enforced, and what happens to a request that bypasses the screen?
- L.authorization-04.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What may a person do when no rule mentions them or the thing they ask for?
- L.authorization-05.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): When and how are a person's permissions reduced or removed as their role changes?
- L.authorization-06.carry-over: carry-over: How does the product tell a request the person meant to make from one sent in their name by someone else's page?
- L.authorization-07.carry-over: carry-over: Which operations change something, and can any of them happen just because a link was followed or a page was loaded?
- L.authorization-08.shown-list: shown-list: What does the product do with a request when the check of its permission cannot be completed?
- L.authorization-10.shown-list: shown-list: Which facts about a person's identity and permissions does the product take from the person's device, and how does it know they were not altered?
- L.authorization-11.shown-list: shown-list: How soon after signing out or losing access does everything a person already held stop working?
- L.authorization-12.shown-list: shown-list: How does the product make sure the account a person ends up signed in to is the one they chose?
- L.logging-01.carry-over: carry-over: Which events must always leave a record?
- L.logging-02.carry-over: carry-over: What must every record say so that someone can later tell what happened and to whom?
- L.logging-03.person-name: person-name: Which values must never appear in a record, and how are they kept out?
- L.logging-07.carry-over: carry-over: When something fails, what does the person see and what goes only into the records?
- L.logging-12.person-name: person-name: How long is each kind of record kept, and what removes it when that time is up?
- L.accessibility-01.carry-over: carry-over: For each thing a person can do on the screen, how is it done using the keyboard alone?
- L.accessibility-02.carry-over: carry-over: From every part of the screen a keyboard user can enter, how do they leave it?
- L.accessibility-03.carry-over: carry-over: How is the item that has keyboard focus shown, on every item that can take it?
- L.accessibility-04.carry-over: carry-over: Where does focus go when the item holding it closes or is removed?
- L.accessibility-05.carry-over: carry-over: What name and purpose does each control announce to someone who cannot see it?
- L.accessibility-06.shown-list: shown-list: For everything shown that is not text, what words give the same meaning?
- L.accessibility-07.carry-over: carry-over: How does someone who cannot see the screen learn the result of what they just did?
- L.accessibility-08.shown-list: shown-list: Wherever colour carries meaning, what else on the screen carries the same meaning?
- L.accessibility-09.shown-list: shown-list: What contrast between text and its background does every screen keep, in every state and theme?
- L.accessibility-10.shown-list: shown-list: What happens to each screen when its text is enlarged to twice its size?
- L.accessibility-11.carry-over: carry-over: Which steps have a time limit, and how does a person who needs longer get it?
- L.accessibility-12.shown-list: shown-list: What moves on the screen, and how does a person who asked for less motion get the product without it?
- L.sign-in-01.shown-list: shown-list: What stops someone guessing or replaying credentials at sign-in, and what does a person locked out by it do?
- L.sign-in-02.shown-list: shown-list: Which accounts exist before anyone signs up, and how is each removed or made unusable?
- L.sign-in-03.shown-list: shown-list: Can anyone tell from signing in, signing up or recovery whether a given person has an account, and does that matter here?
- L.sign-in-04.shown-list: shown-list: How does a person get back in after forgetting or losing what they sign in with, and how is that kept as strong as signing in?
- L.sign-in-05.shown-list: shown-list: How is a person's first credential or activation code made, delivered and ended?
- L.sign-in-06.shown-list: shown-list: What are all the ways to sign in, and is each held to the same strength?
- L.sign-in-07.shown-list: shown-list: What is a person told when their sign-in details change or an unusual sign-in happens, and by which route?
- L.sign-in-08.shown-list: shown-list: How long does a session last unused, and in all, before the person must sign in again, and on what grounds?
- L.sign-in-09.shown-list: shown-list: How many sessions may one account have at once, and what happens when one more starts?
- L.sign-in-10.shown-list: shown-list: What happens to the session a person held before signing in, and is a fresh one made at every sign-in?
- L.sign-in-11.carry-over: carry-over: Which changes and operations make a person prove again who they are, even while signed in?
- L.sign-in-12.shown-list: shown-list: How does a person, or whoever runs the product, see and end the sessions of an account?
- L.stored-data-01.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which data the product creates or holds would harm someone if seen or changed, and how strongly must each kind be protected?
- L.stored-data-02.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Who could read each kind of sensitive data where it is stored and in every copy made of it, and what makes it unreadable to anyone else?
- L.stored-data-03.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which keys protect what, where does each one live, and what may each be used for?
- L.stored-data-04.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): What happens to protected data when its key is lost, exposed or replaced?
- L.stored-data-05.person-name: person-name: Does any sensitive value travel in an address or its query, and where would that be recorded?
- L.stored-data-06.shown-list: shown-list: Which components in between may keep a copy of a reply, and how is sensitive data kept out of them?
- L.stored-data-07.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Which other parties receive any data from the product, and is any of it sensitive?
- L.stored-data-08.shown-list: shown-list: For each reply, which fields are sent, and is any sent that the asker does not need or may not see?
- L.stored-data-09.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): How long is each kind of sensitive data kept, and what removes it when that time is up?
- L.stored-data-10.shown-list: shown-list: What does the product store on the person's device, and is any of it sensitive?
- L.stored-data-12.waiting-list: waiting-list (in each of its states: empty, part-carried-over, carried-over, behind-notebook, wrong, unavailable, carry-over-refused, ended): Is the reading of sensitive data recorded, without the data itself, and who looks at that record?
- L.misuse-02.carry-over: carry-over: What limits does each rule of the product set, and where is each enforced?
- L.misuse-07.carry-over: carry-over: Which fields may each request set, and what happens to a field that is sent and was not meant to be set?
- L.misuse-03.carry-over: carry-over: What could a script do by calling the product again and again, and what stops it?

## Each value taken in, each way it can be wrong

- V.notebook-order.empty: `notebook-order` (the person who keeps the list, from the notebook) is empty: what does the product do, and what is the person told?
- V.notebook-order.missing: `notebook-order` (the person who keeps the list, from the notebook) is missing, or null: what does the product do, and what is the person told?
- V.notebook-order.malformed: `notebook-order` (the person who keeps the list, from the notebook) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.notebook-order.long: `notebook-order` (the person who keeps the list, from the notebook) is far longer or larger than expected: what does the product do, and what is the person told?
- V.notebook-order.twice: `notebook-order` (the person who keeps the list, from the notebook) is the same as one already there: what does the product do, and what is the person told?
- V.stored-list.empty: `stored-list` (read back from where the list is kept) is empty: what does the product do, and what is the person told?
- V.stored-list.missing: `stored-list` (read back from where the list is kept) is missing, or null: what does the product do, and what is the person told?
- V.stored-list.malformed: `stored-list` (read back from where the list is kept) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.stored-list.long: `stored-list` (read back from where the list is kept) is far longer or larger than expected: what does the product do, and what is the person told?
- V.stored-list.twice: `stored-list` (read back from where the list is kept) is the same as one already there: what does the product do, and what is the person told?
- V.every-setting.missing: any setting the build reads is missing, or null: what does the product do at start, and who is told?
- V.every-setting.empty: any setting the build reads is empty: what does the product do at start, and who is told?
- V.every-setting.malformed: any setting the build reads is of the wrong type or malformed: what does the product do at start, and who is told?
- V.every-setting.outside: any setting the build reads is outside what is allowed: what does the product do at start, and who is told?
Not drawn, 5 already asked of the same thing by a library question above.

## Each class of sensitive values, each place it can leak to

- X.waiting-person-details.logs: can any of `person-name`, `notebook-order`, `stored-list` reach what the product logs, on the path that works and on each that fails?
- X.waiting-person-details.errors-inside: can any of `person-name`, `notebook-order`, `stored-list` reach an error's own message and trace, on the path that works and on each that fails?
- X.waiting-person-details.errors-shown: can any of `person-name`, `notebook-order`, `stored-list` reach an error shown or returned to whoever asked, on the path that works and on each that fails?
- X.waiting-person-details.telemetry: can any of `person-name`, `notebook-order`, `stored-list` reach what is sent to monitoring or measurement, on the path that works and on each that fails?
- X.waiting-person-details.samples: can any of `person-name`, `notebook-order`, `stored-list` reach test data and examples kept with the code, on the path that works and on each that fails?
- X.waiting-person-details.replies: can any of `person-name`, `notebook-order`, `stored-list` reach a reply that succeeded, to whoever asked, on the path that works and on each that fails?
- X.waiting-person-details.stored: can any of `person-name`, `notebook-order`, `stored-list` reach where it is stored, and every copy made of that, on the path that works and on each that fails?

## Each state, each event

- S.waiting-list.empty.carry-over-list-1: Waiting list is `empty` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.empty.again: Waiting list is `empty` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.empty.reopened: Waiting list is `empty` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.empty.restart: Waiting list is `empty` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.empty.time: Waiting list is `empty` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.part-carried-over.carry-over-list-1: Waiting list is `part-carried-over` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.part-carried-over.again: Waiting list is `part-carried-over` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.part-carried-over.reopened: Waiting list is `part-carried-over` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.part-carried-over.restart: Waiting list is `part-carried-over` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.part-carried-over.time: Waiting list is `part-carried-over` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.carried-over.carry-over-list-1: Waiting list is `carried-over` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.carried-over.again: Waiting list is `carried-over` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.carried-over.reopened: Waiting list is `carried-over` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.carried-over.restart: Waiting list is `carried-over` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.carried-over.time: Waiting list is `carried-over` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.carry-over-list-1: Waiting list is `behind-notebook` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.again: Waiting list is `behind-notebook` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.reopened: Waiting list is `behind-notebook` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.restart: Waiting list is `behind-notebook` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.time: Waiting list is `behind-notebook` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.wrong.carry-over-list-1: Waiting list is `wrong` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.wrong.again: Waiting list is `wrong` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.wrong.reopened: Waiting list is `wrong` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.wrong.restart: Waiting list is `wrong` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.wrong.time: Waiting list is `wrong` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.unavailable.carry-over-list-1: Waiting list is `unavailable` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.unavailable.again: Waiting list is `unavailable` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.unavailable.reopened: Waiting list is `unavailable` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.unavailable.restart: Waiting list is `unavailable` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.unavailable.time: Waiting list is `unavailable` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.carry-over-refused.carry-over-list-1: Waiting list is `carry-over-refused` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.carry-over-refused.again: Waiting list is `carry-over-refused` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.carry-over-refused.reopened: Waiting list is `carry-over-refused` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.carry-over-refused.restart: Waiting list is `carry-over-refused` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.carry-over-refused.time: Waiting list is `carry-over-refused` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.ended.carry-over-list-1: Waiting list is `ended` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.ended.again: Waiting list is `ended` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.ended.reopened: Waiting list is `ended` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.ended.restart: Waiting list is `ended` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.ended.time: Waiting list is `ended` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.carry-over-list-1: A person's place on the list is `in-notebook` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.again: A person's place on the list is `in-notebook` and the same action is done again at once: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.reopened: A person's place on the list is `in-notebook` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.restart: A person's place on the list is `in-notebook` and the product stops and starts again: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.second: A person's place on the list is `in-notebook` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.in-notebook.time: A person's place on the list is `in-notebook` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.carry-over-list-1: A person's place on the list is `carried-place` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.again: A person's place on the list is `carried-place` and the same action is done again at once: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.reopened: A person's place on the list is `carried-place` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.restart: A person's place on the list is `carried-place` and the product stops and starts again: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.second: A person's place on the list is `carried-place` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.carried-place.time: A person's place on the list is `carried-place` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.carry-over-list-1: A person's place on the list is `newly-joined` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.again: A person's place on the list is `newly-joined` and the same action is done again at once: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.reopened: A person's place on the list is `newly-joined` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.restart: A person's place on the list is `newly-joined` and the product stops and starts again: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.second: A person's place on the list is `newly-joined` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.newly-joined.time: A person's place on the list is `newly-joined` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.carry-over-list-1: A person's place on the list is `moved` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.again: A person's place on the list is `moved` and the same action is done again at once: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.reopened: A person's place on the list is `moved` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.restart: A person's place on the list is `moved` and the product stops and starts again: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.second: A person's place on the list is `moved` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.moved.time: A person's place on the list is `moved` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.carry-over-list-1: A person's place on the list is `taken-off` and what carry-over-list / 1 describes is done: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.again: A person's place on the list is `taken-off` and the same action is done again at once: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.reopened: A person's place on the list is `taken-off` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.restart: A person's place on the list is `taken-off` and the product stops and starts again: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.second: A person's place on the list is `taken-off` and a second copy of the product, a second device or a second person acts on it at the same moment: what happens to it, and what is the person shown?
- S.person-s-place-on-the-list.taken-off.time: A person's place on the list is `taken-off` and a long time passes with nothing done: what happens to it, and what is the person shown?
Not drawn, 8 already asked of the same thing by a library question above.

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
- F.unguessable.made: Which values are meant to be impossible to guess (a link, a code, a session, an identifier), and how is each one made?

## What someone who means harm would want

- T.waiting-person-details.shown-list: someone after `waiting-person-details` comes through `shown-list`: Someone who should not see the list reads the names of the people waiting and where each one stands. What stops it, and how would anyone know it was tried?
- T.waiting-person-details.carry-over: someone after `waiting-person-details` comes through `carry-over`: Someone other than the person carrying the notebook over gets the names and their order while they are being carried over. What stops it, and how would anyone know it was tried?
- T.waiting-list.carry-over: someone after `waiting-list` comes through `carry-over`: Someone who should not be able to carry over adds, replaces or reorders people, so that someone moves ahead of those who have waited longer. What stops it, and how would anyone know it was tried?
- T.waiting-list.carry-over: someone after `waiting-list` comes through `carry-over`: A person allowed to carry over puts a friend higher than the notebook does, nobody can tell, and those waiting lose their turn. What stops it, and how would anyone know it was tried?
- T.waiting-list.shown-list: someone after `waiting-list` comes through `shown-list`: The person checking is shown an order that differs from the one kept, accepts it as matching the notebook, and a wrong order stands. What stops it, and how would anyone know it was tried?

## Asked of every slice

- W.unavailable: What happens, and to whom, if what this slice adds cannot be used for an hour?
- W.target: How often may it fail, and how slow is too slow, before someone would say it does not work?
- W.noticed: Who notices when it breaks, and how?
- W.sensitive: What does this slice touch that would harm someone if another person saw or changed it?
- W.who-sees: Who uses it, and may any of them see or change what belongs to another?
- W.obligations: Does a law, a contract or an outside system's terms bind how this is handled?
- W.prize: What would someone who means harm want from what this slice adds?

## Carried from research

- C.states.waiting-list.empty: Waiting list, `empty`: not said in the documents (not said in the documents; the criterion starts here | The person who keeps the list can carry the notebook over. | carry the notebook over -> `carried-over` | slice-001/004_slice.md, line 9)
- C.states.waiting-list.part-carried-over: Waiting list, `part-carried-over`: not said in the documents (not said in the documents: what there is between starting to carry over and having finished | not said in the documents | none | not said in the documents)
- C.states.waiting-list.behind-notebook: Waiting list, `behind-notebook`: not said in the documents (The person who keeps the list records a later change in the notebook. | The carried-over list does not show the change. What else can be done with it is not said in the documents. | none | slice-001/004_slice.md, line 16)
- C.states.waiting-list.wrong: Waiting list, `wrong`: not said in the documents (A place on the list is wrong or disputed. How it gets that way is not said in the documents. | not said in the documents; whether it can be corrected is not yet confirmed | none | 002_requirements.md, line 18)
- C.states.waiting-list.unavailable: Waiting list, `unavailable`: not said in the documents (not said in the documents: the list stopping working with nobody doing anything | not said in the documents | none | not said in the documents)
- C.states.waiting-list.carry-over-refused: Waiting list, `carry-over-refused`: not said in the documents (not said in the documents: carrying over being refused every time | not said in the documents | none | not said in the documents)
- C.states.waiting-list.ended: Waiting list, `ended`: not said in the documents (not said in the documents: how the list is ended | not said in the documents, including what is left | none | not said in the documents)
- C.states.person-s-place-on-the-list.in-notebook: A person's place on the list, `in-notebook`: not said in the documents (The person is on the list in the paper notebook. How they got there is not said in the documents. | They can phone to ask where they are. | the notebook is carried over -> `carried-place` | 000_problem.md, line 5; slice-001/004_slice.md, line 9)
- C.states.person-s-place-on-the-list.newly-joined: A person's place on the list, `newly-joined`: not said in the documents (not said in the documents: how someone joins the list from now on, and what decides their place | not said in the documents | none | 002_requirements.md, lines 17 and 19 (not yet confirmed))
- C.states.person-s-place-on-the-list.moved: A person's place on the list, `moved`: not said in the documents (not said in the documents: whether anything can move a person up or down | not said in the documents | none | 002_requirements.md, line 19 (not yet confirmed))
- C.states.person-s-place-on-the-list.taken-off: A person's place on the list, `taken-off`: not said in the documents (not said in the documents: how and when someone is taken off | not said in the documents, including what is left | none | 002_requirements.md, line 17 (not yet confirmed))
- C.states.dead-end.1: for the owner's list: `part-carried-over`: no way out. The documents do not say what the person who keeps the list is left with if carrying over is not finished.
- C.states.dead-end.2: for the owner's list: `behind-notebook`: no way out. The carried-over list does not show later changes recorded in the notebook.
- C.states.dead-end.3: for the owner's list: `wrong`: no way out. A wrong or disputed place has no stated way to be corrected.
- C.states.dead-end.4: for the owner's list: `unavailable`: no way out. The documents do not say what anyone is left with if the list stops working.
- C.states.dead-end.5: for the owner's list: `carry-over-refused`: no way out. The documents do not say what the person who keeps the list is left with if carrying over is always refused.
- C.states.dead-end.6: for the owner's list: `ended`: no way out. The documents do not say what is left of the list, or whether it can be started again.
- C.states.dead-end.7: for the owner's list: `carried-place`: no way out. The place stays as carried over; no change to it is stated.
- C.states.dead-end.8: for the owner's list: `newly-joined`: no way out. The documents do not say what happens to the place of someone who joins from now on.
- C.states.dead-end.9: for the owner's list: `moved`: no way out. The documents do not say whether places move, or what follows if one does.
- C.states.dead-end.10: for the owner's list: `taken-off`: no way out. The documents do not say whether someone taken off can come back.
