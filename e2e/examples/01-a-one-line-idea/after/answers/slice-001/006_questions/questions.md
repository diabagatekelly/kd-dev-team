# Questions

<!-- drawn from: 441215372 -->

Drawn by script from kept.md and the slice's documents. Nothing here is answered.

## From the library

- L.sync-04.list-view: list-view: How does a person know how old the information in front of them is, and what is shown when there is none yet?
- L.sync-08.carry-across: carry-across: How does the product know an update brought everything, and what does it show while it has caught up only partly?
- L.limits-04.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What is the most the product is meant to handle at one time, and what does it do with demand beyond that?
- L.limits-06.carry-across: carry-across: What is a person or a calling system told when a limit stops them, and can they tell what to do next?
- L.limits-07.carry-across: carry-across: What is the largest single item the product accepts, and what happens to one that is larger?
- L.limits-08.list-view: list-view: How many items may be asked for or shown in one go, and how does a person reach the rest?
- L.durable-write-01.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does the product guarantee is stored when a save is cut off partway: all of the old content, all of the new, or something it can detect and repair?
- L.durable-write-02.carry-across: carry-across: At what moment does the product say a change is saved, and how much recently confirmed work may be lost if power fails right after?
- L.durable-write-03.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): On what kinds of storage does the product promise its saved data survives a power loss, and how would it notice damage on storage that does not keep that promise?
- L.durable-write-04.carry-across: carry-across: What does the person see, and what state is the previously saved data in, when a save fails for lack of space?
- L.durable-write-05.carry-across: carry-across: What does the product do after storage reports a failed save, given that trying again and being told it worked does not prove the data is there?
- L.durable-write-06.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): When saved data is replaced wholesale, what is guaranteed to be found after a crash at any point during the replacement?
- L.durable-write-08.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which pieces of saved data must always agree with one another, and what does the product do when it finds them disagreeing after a crash?
- L.durable-write-09.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How does the product detect saved data that has silently changed since it was written, and what does it do with it?
- L.durable-write-10.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How are copies of the saved data (backups, exports, device transfers) taken so that a copy made during a save is still usable?
- L.durable-write-11.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which files together make up the saved data, and what happens when only some of them are moved, copied, restored or cleaned up?
- L.durable-write-12.carry-across: carry-across: What happens to a save that is still in progress when the product is closed, and how does the person learn on return that it did not happen?
- L.startup-read-01.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does the product do at start when its saved data is damaged: refuse to run, run with what can be read, or start fresh, and what is the person told?
- L.startup-read-02.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does the product do when the thing in its saved-data location is not recognisably its own, and does it ever overwrite it?
- L.startup-read-03.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How does the product tell a first run with nothing saved apart from saved data that exists but cannot be opened, and what does it do in each case?
- L.startup-read-04.carry-across: carry-across: What does the product do at start when it finds a save that an earlier run left unfinished: complete it, undo it, or ask?
- L.startup-read-05.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does the product do when it may read its saved data but not change it, including when that data needs repair first?
- L.startup-read-06.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does a starting copy of the product do when another copy is already repairing the saved data: wait, for how long, and what does it show meanwhile?
- L.startup-read-07.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Where can the platform remove the product's saved data on its own, and what does the person find, and can get back, when that has happened?
- L.startup-read-08.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): After a rescue of damaged saved data, what is checked before the result is used, and how is the person told what may be missing, changed or back again?
- L.startup-read-09.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How would the product or its owner find out that saved data is readable but wrong, and how far back can a good version be recovered?
- L.startup-read-10.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which spare copy does the product fall back on when its saved data is unusable, and when was bringing it back last actually tried?
- L.migration-01.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does a version of the product do when it meets saved data written by a later version: refuse, open it read-only, or use what it understands?
- L.migration-03.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): After a new version has saved anything, can the previous version still be put back, and what does it do with what the new one wrote?
- L.concurrency-01.carry-across: carry-across: When two changes to the same item are made from what each saw earlier, which survives, and is the person whose change was replaced told?
- L.concurrency-03.list-view: list-view: Which sets of items must always be read as they stood at a single moment, and how is that ensured while changes are going on?
- L.concurrency-04.carry-across: carry-across: Where does the product decide something from the set of items matching a condition, and what happens if that set changes before the decision is acted on?
- L.concurrency-05.list-view: list-view: Can anything see or act on a change before it is final, and what happens to what was built on it if the change is withdrawn?
- L.concurrency-06.list-view: list-view: After a change is confirmed, how soon must every window, copy and device show it, and what does a person see in the meantime?
- L.concurrency-08.carry-across: carry-across: What does the product do when the stored data is in use by another operation: wait, try again, or tell the person, and for how long?
- L.concurrency-09.carry-across: carry-across: When an operation is cancelled because it clashed with another, is it repeated automatically from the start, and what if it cannot simply be repeated?
- L.concurrency-12.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What stops two copies of the product from changing the same stored data at once, and in which setups (shared or remote storage, mixed versions) does that protection not hold?
- L.lifecycle-01.carry-across: carry-across: When making something takes several steps and a later one fails, what is done about the steps already carried out, and who decides between undoing them and carrying on another way?
- L.lifecycle-02.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How is a thing shown and handled when undoing it has itself failed, and who is alerted to sort it out by hand?
- L.lifecycle-03.carry-across: carry-across: Which steps cannot be taken back once done, and is everything that could still fail checked before them?
- L.lifecycle-04.carry-across: carry-across: How long may a thing stay in progress before the product treats the work as failed, and what then happens to it?
- L.lifecycle-05.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which records only make sense as a pair or set, and how is one that exists without its partner found and dealt with?
- L.lifecycle-08.carry-across: carry-across: How long is something that was started and then abandoned kept, and what removes it afterwards?
- L.user-input-01.person-name: person-name: How long may each typed value be, and what does the person see when theirs is longer?
- L.user-input-02.person-name: person-name: Which fields are truly required, and what can a person do who has no value for one of them?
- L.user-input-03.person-name: person-name: Which characters does each field accept, and on what grounds is any character refused?
- L.user-input-04.person-name: person-name: Is each value asked for whole or in parts, and what happens when a person's value has fewer, more or differently ordered parts?
- L.user-input-05.carry-across: carry-across: Where is each rule about a typed value enforced, and what happens to a value that arrives without having passed the on-screen check?
- L.user-input-06.carry-across: carry-across: For each way a value can be refused, what does the message say and where does it appear?
- L.user-input-07.person-name: person-name: Is an empty or all-spaces value accepted, and are spaces around a value kept, removed or refused?
- L.user-input-09.person-name: person-name: Which values must be unique, how is sameness judged, and what is the person told when theirs is taken?
- L.user-input-10.person-name: person-name: Wherever typed text is later shown, stored or passed on, how is it kept from being acted on as anything but text?
- L.user-action-01.carry-across: carry-across: What does the person see at once after starting an operation, and what happens if they start it a second time before the first has finished?
- L.user-action-02.list-view: list-view: What does reloading do on each screen that follows an operation that changed something?
- L.user-action-03.list-view: list-view: What does each screen show, and what can be done from it, when it is reached by stepping back after the operation it led to?
- L.user-action-04.list-view: list-view: What remains visible on the device after a person signs out, including on screens reached by stepping back?
- L.user-action-05.carry-across: carry-across: When are a person's changes saved, and what becomes of unsaved ones when they leave without warning the product?
- L.user-action-06.carry-across: carry-across: What does a person find when they come back to a screen their device has suspended or discarded in the meantime?
- L.user-action-07.list-view: list-view: When the same person has several windows open, how does each learn of a change made in another, and which one wins if both act?
- L.user-action-08.carry-across: carry-across: Which actions can be undone, for how long, and what can a person do about one that cannot?
- L.user-action-09.carry-across: carry-across: Which actions ask for confirmation, and why will a person still read the question on the one that matters?
- L.user-action-10.carry-across: carry-across: At each step of a longer operation, how does a person back out, and what is left behind if they do or simply leave?
- L.user-action-11.carry-across: carry-across: What happens to work in progress when a person's signed-in period ends, and can they carry on after signing in again?
- L.user-action-12.list-view: list-view: What does a saved address to each screen lead to when the person is signed out, or when what it pointed at no longer exists?
- L.long-operation-01.carry-across: carry-across: For each operation that can take more than a few seconds, what is the person shown while it runs?
- L.long-operation-02.carry-across: carry-across: How can a person tell an operation that is still working from one that has stopped?
- L.long-operation-03.carry-across: carry-across: Which operations can be stopped once started, and how?
- L.long-operation-04.carry-across: carry-across: When an operation is stopped partway, is the finished part undone, kept or completed later, and how is it shown?
- L.long-operation-05.carry-across: carry-across: How does a person who went elsewhere learn that an operation ended, and where do they find its result?
- L.long-operation-06.carry-across: carry-across: After an interruption in the middle of an operation, does it resume, restart or stay abandoned, and what state is left meanwhile?
- L.long-operation-07.carry-across: carry-across: Where is a late failure recorded, and how does the person who started the operation come to know of it?
- L.long-operation-08.carry-across: carry-across: When only some items of an operation succeed, what is kept, what is reported, and how are the failed ones tried again?
- L.long-operation-09.carry-across: carry-across: After how long without progress is an operation treated as stuck, and what happens to it then?
- L.long-operation-10.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How long is the result of a finished operation kept, and what does a person find after that?
- L.long-operation-11.carry-across: carry-across: When an operation is requested on something that already has one running, is the new one refused, queued, or does it replace the old?
- L.long-operation-12.carry-across: carry-across: What is checked before a long operation is accepted, so that a request sure to fail is refused at once?
- L.text-01.person-name: person-name: When are two pieces of text counted as the same, and is that settled before they are stored or each time they are compared?
- L.text-02.person-name: person-name: Where does the product ignore the difference between capital and small letters, and by which language's rules?
- L.text-03.person-name: person-name: What does the product do with unseen characters and unusual spaces in text it stores and compares?
- L.text-05.person-name: person-name: How does the product measure the length of text, and where may it cut text that is too long?
- L.text-09.person-name: person-name: Wherever a stored or typed value is put into a sentence or a row, what keeps text of the opposite direction from disturbing what surrounds it?
- L.text-10.list-view: list-view: Where must people tell names or labels apart by eye, and what stops one being made to look like another?
- L.text-12.list-view: list-view: How much room does each label and message have, and what happens when the wording in another language is longer or taller?
- L.presentation-12.list-view: list-view: When a list too long for one screen is put in order, does the order hold across all of it?
- L.authorization-01.carry-across: carry-across: For every operation and every kind of data, who is allowed, and where is that checked?
- L.authorization-01.list-view: list-view: For every operation and every kind of data, who is allowed, and where is that checked?
- L.authorization-02.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How does the product confirm that the particular record asked for belongs to, or is shared with, the person asking?
- L.authorization-03.list-view: list-view: Where is each permission enforced, and what happens to a request that bypasses the screen?
- L.authorization-04.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What may a person do when no rule mentions them or the thing they ask for?
- L.authorization-05.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): When and how are a person's permissions reduced or removed as their role changes?
- L.authorization-06.carry-across: carry-across: How does the product tell a request the person meant to make from one sent in their name by someone else's page?
- L.authorization-07.carry-across: carry-across: Which operations change something, and can any of them happen just because a link was followed or a page was loaded?
- L.authorization-08.list-view: list-view: What does the product do with a request when the check of its permission cannot be completed?
- L.authorization-10.list-view: list-view: Which facts about a person's identity and permissions does the product take from the person's device, and how does it know they were not altered?
- L.authorization-11.list-view: list-view: How soon after signing out or losing access does everything a person already held stop working?
- L.authorization-12.list-view: list-view: How does the product make sure the account a person ends up signed in to is the one they chose?
- L.configuration-01.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which settings are checked when the product starts, and what does the product do if one is missing or wrong?
- L.configuration-03.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which values differ between installations, and where is each one set?
- L.configuration-05.list-view: list-view: What does each setting default to, and is the product safe to run if no default is ever changed?
- L.configuration-06.list-view: list-view: What is switched on in a fresh installation, and which of it is actually needed?
- L.configuration-07.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): In what ways do the settings of the trial and real installations differ, and how is each difference accounted for?
- L.configuration-11.list-view: list-view: Which diagnostic modes exist, and what guarantees each is off where the product is really used?
- L.configuration-12.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Who and what can change each setting, and which settings can be influenced from outside?
- L.logging-01.carry-across: carry-across: Which events must always leave a record?
- L.logging-02.carry-across: carry-across: What must every record say so that someone can later tell what happened and to whom?
- L.logging-03.person-name: person-name: Which values must never appear in a record, and how are they kept out?
- L.logging-04.person-name: person-name: How is outside-supplied text recorded so that it cannot pass for, or damage, the product's own entries?
- L.logging-05.carry-across: carry-across: What does the product do when it cannot write a record: stop, continue without it, or something else?
- L.logging-06.carry-across: carry-across: How much may the records grow, and what happens when that limit is reached?
- L.logging-07.carry-across: carry-across: When something fails, what does the person see and what goes only into the records?
- L.logging-08.carry-across: carry-across: Where are the records kept, and do they survive the loss of the machine that wrote them?
- L.logging-09.carry-across: carry-across: Who or what reads the records, and which entries make someone get told?
- L.logging-10.carry-across: carry-across: Who can change or remove records, and how would a change or removal be noticed?
- L.logging-11.carry-across: carry-across: Which clock does each record's time come from, and how are records from different places put in order?
- L.logging-12.carry-across: carry-across: How long is each kind of record kept, and what removes it when that time is up?
- L.accessibility-01.carry-across: carry-across: For each thing a person can do on the screen, how is it done using the keyboard alone?
- L.accessibility-02.carry-across: carry-across: From every part of the screen a keyboard user can enter, how do they leave it?
- L.accessibility-03.carry-across: carry-across: How is the item that has keyboard focus shown, on every item that can take it?
- L.accessibility-04.carry-across: carry-across: Where does focus go when the item holding it closes or is removed?
- L.accessibility-05.carry-across: carry-across: What name and purpose does each control announce to someone who cannot see it?
- L.accessibility-06.list-view: list-view: For everything shown that is not text, what words give the same meaning?
- L.accessibility-07.carry-across: carry-across: How does someone who cannot see the screen learn the result of what they just did?
- L.accessibility-08.list-view: list-view: Wherever colour carries meaning, what else on the screen carries the same meaning?
- L.accessibility-09.list-view: list-view: What contrast between text and its background does every screen keep, in every state and theme?
- L.accessibility-10.list-view: list-view: What happens to each screen when its text is enlarged to twice its size?
- L.accessibility-11.carry-across: carry-across: Which steps have a time limit, and how does a person who needs longer get it?
- L.accessibility-12.list-view: list-view: What moves on the screen, and how does a person who asked for less motion get the product without it?
- L.sign-in-01.list-view: list-view: What stops someone guessing or replaying credentials at sign-in, and what does a person locked out by it do?
- L.sign-in-02.list-view: list-view: Which accounts exist before anyone signs up, and how is each removed or made unusable?
- L.sign-in-03.list-view: list-view: Can anyone tell from signing in, signing up or recovery whether a given person has an account, and does that matter here?
- L.sign-in-04.list-view: list-view: How does a person get back in after forgetting or losing what they sign in with, and how is that kept as strong as signing in?
- L.sign-in-05.list-view: list-view: How is a person's first credential or activation code made, delivered and ended?
- L.sign-in-06.list-view: list-view: What are all the ways to sign in, and is each held to the same strength?
- L.sign-in-07.list-view: list-view: What is a person told when their sign-in details change or an unusual sign-in happens, and by which route?
- L.sign-in-08.list-view: list-view: How long does a session last unused, and in all, before the person must sign in again, and on what grounds?
- L.sign-in-09.list-view: list-view: How many sessions may one account have at once, and what happens when one more starts?
- L.sign-in-10.list-view: list-view: What happens to the session a person held before signing in, and is a fresh one made at every sign-in?
- L.sign-in-11.carry-across: carry-across: Which changes and operations make a person prove again who they are, even while signed in?
- L.sign-in-12.list-view: list-view: How does a person, or whoever runs the product, see and end the sessions of an account?
- L.stored-data-01.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which data the product creates or holds would harm someone if seen or changed, and how strongly must each kind be protected?
- L.stored-data-02.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Who could read each kind of sensitive data where it is stored and in every copy made of it, and what makes it unreadable to anyone else?
- L.stored-data-03.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which keys protect what, where does each one live, and what may each be used for?
- L.stored-data-04.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What happens to protected data when its key is lost, exposed or replaced?
- L.stored-data-05.person-name: person-name: Does any sensitive value travel in an address or its query, and where would that be recorded?
- L.stored-data-06.list-view: list-view: Which components in between may keep a copy of a reply, and how is sensitive data kept out of them?
- L.stored-data-07.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Which other parties receive any data from the product, and is any of it sensitive?
- L.stored-data-08.list-view: list-view: For each reply, which fields are sent, and is any sent that the asker does not need or may not see?
- L.stored-data-09.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): How long is each kind of sensitive data kept, and what removes it when that time is up?
- L.stored-data-10.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What does the product store on the person's device, and is any of it sensitive?
- L.stored-data-12.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): Is the reading of sensitive data recorded, without the data itself, and who looks at that record?
- L.misuse-01.carry-across: carry-across: Which steps must happen in order, and what does the product do with a request for a later step when an earlier one was not done?
- L.misuse-02.carry-across: carry-across: What limits does each rule of the product set, and where is each enforced?
- L.misuse-03.carry-across: carry-across: What could a script do by calling the product again and again, and what stops it?
- L.misuse-04.carry-across: carry-across: Is anything done faster than a person could a sign of abuse here, and what is done about it?
- L.misuse-05.carry-across: carry-across: Which actions are grave enough to need a second person's agreement?
- L.misuse-06.carry-across: carry-across: Which operations are costly to run, and what stops one person's use of them from denying the others?
- L.misuse-07.carry-across: carry-across: Which fields may each request set, and what happens to a field that is sent and was not meant to be set?
- L.misuse-08.waiting-list: waiting-list (in each of its states: not-carried-across, being-carried-across, carry-across-failed, carried-across, out-of-date, wrong, ended): What is in limited supply, and can a person take more than their share by how they ask?

## Each value taken in, each way it can be wrong

- V.notebook-order.empty: `notebook-order` (the list keeper, from the notebook) is empty: what does the product do, and what is the person told?
- V.notebook-order.missing: `notebook-order` (the list keeper, from the notebook) is missing, or null: what does the product do, and what is the person told?
- V.notebook-order.malformed: `notebook-order` (the list keeper, from the notebook) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.notebook-order.long: `notebook-order` (the list keeper, from the notebook) is far longer or larger than expected: what does the product do, and what is the person told?
- V.notebook-order.twice: `notebook-order` (the list keeper, from the notebook) is the same as one already there: what does the product do, and what is the person told?
- V.every-setting.outside: any setting the build reads is outside what is allowed: what does the product do at start, and who is told?
Not drawn, 8 already asked of the same thing by a library question above.

## Each class of sensitive values, each place it can leak to

- X.waiting-details.logs: can any of `person-name`, `notebook-order` reach what the product logs, on the path that works and on each that fails?
- X.waiting-details.errors-inside: can any of `person-name`, `notebook-order` reach an error's own message and trace, on the path that works and on each that fails?
- X.waiting-details.errors-shown: can any of `person-name`, `notebook-order` reach an error shown or returned to whoever asked, on the path that works and on each that fails?
- X.waiting-details.telemetry: can any of `person-name`, `notebook-order` reach what is sent to monitoring or measurement, on the path that works and on each that fails?
- X.waiting-details.samples: can any of `person-name`, `notebook-order` reach test data and examples kept with the code, on the path that works and on each that fails?
- X.waiting-details.replies: can any of `person-name`, `notebook-order` reach a reply that succeeded, to whoever asked, on the path that works and on each that fails?
- X.waiting-details.stored: can any of `person-name`, `notebook-order` reach where it is stored, and every copy made of that, on the path that works and on each that fails?

## Each state, each event

- S.waiting-list.not-carried-across.notebook-order-kept-1: The waiting list is `not-carried-across` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.not-carried-across.again: The waiting list is `not-carried-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.not-carried-across.reopened: The waiting list is `not-carried-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.not-carried-across.restart: The waiting list is `not-carried-across` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.not-carried-across.time: The waiting list is `not-carried-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.being-carried-across.notebook-order-kept-1: The waiting list is `being-carried-across` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.being-carried-across.again: The waiting list is `being-carried-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.being-carried-across.reopened: The waiting list is `being-carried-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.being-carried-across.restart: The waiting list is `being-carried-across` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.being-carried-across.time: The waiting list is `being-carried-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.carry-across-failed.notebook-order-kept-1: The waiting list is `carry-across-failed` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.carry-across-failed.again: The waiting list is `carry-across-failed` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.carry-across-failed.reopened: The waiting list is `carry-across-failed` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.carry-across-failed.restart: The waiting list is `carry-across-failed` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.carry-across-failed.time: The waiting list is `carry-across-failed` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.carried-across.notebook-order-kept-1: The waiting list is `carried-across` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.carried-across.again: The waiting list is `carried-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.carried-across.reopened: The waiting list is `carried-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.carried-across.restart: The waiting list is `carried-across` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.carried-across.time: The waiting list is `carried-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.out-of-date.notebook-order-kept-1: The waiting list is `out-of-date` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.out-of-date.again: The waiting list is `out-of-date` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.out-of-date.reopened: The waiting list is `out-of-date` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.out-of-date.restart: The waiting list is `out-of-date` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.out-of-date.time: The waiting list is `out-of-date` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.wrong.notebook-order-kept-1: The waiting list is `wrong` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.wrong.again: The waiting list is `wrong` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.wrong.reopened: The waiting list is `wrong` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.wrong.restart: The waiting list is `wrong` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.wrong.time: The waiting list is `wrong` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.ended.notebook-order-kept-1: The waiting list is `ended` and what notebook-order-kept / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.ended.again: The waiting list is `ended` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.ended.reopened: The waiting list is `ended` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.ended.restart: The waiting list is `ended` and the product stops and starts again: what happens to it, and what is the person shown?
- S.waiting-list.ended.time: The waiting list is `ended` and a long time passes with nothing done: what happens to it, and what is the person shown?
Not drawn, 7 already asked of the same thing by a library question above.

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

- T.waiting-details.list-view: someone after `waiting-details` comes through `list-view`: Someone not entitled to the list reads the names and places of the people waiting. What stops it, and how would anyone know it was tried?
- T.waiting-details.carry-across: someone after `waiting-details` comes through `carry-across`: Someone who can watch the list being carried across learns who is waiting and in what order. What stops it, and how would anyone know it was tried?
- T.waiting-details.stored-list: someone after `waiting-details` comes through `stored-list`: Someone who reaches the kept list or a copy of it takes everyone's names and places. What stops it, and how would anyone know it was tried?
- T.waiting-list.carry-across: someone after `waiting-list` comes through `carry-across`: Someone moves a friend higher or leaves a person out as the list is carried across, so that person loses their turn for a plot. What stops it, and how would anyone know it was tried?
- T.waiting-list.carry-across: someone after `waiting-list` comes through `carry-across`: Someone sends a different list, or an old one again, and it replaces the true order for everyone waiting. What stops it, and how would anyone know it was tried?
- T.waiting-list.list-view: someone after `waiting-list` comes through `list-view`: Someone makes the list keeper be shown an order other than the one kept, so a wrong order is taken to be right. What stops it, and how would anyone know it was tried?

## Asked of every slice

- W.unavailable: What happens, and to whom, if what this slice adds cannot be used for an hour?
- W.target: How often may it fail, and how slow is too slow, before someone would say it does not work?
- W.noticed: Who notices when it breaks, and how?
- W.sensitive: What does this slice touch that would harm someone if another person saw or changed it?
- W.who-sees: Who uses it, and may any of them see or change what belongs to another?
- W.obligations: Does a law, a contract or an outside system's terms bind how this is handled?
- W.prize: What would someone who means harm want from what this slice adds?

## Carried from research

- C.states.waiting-list.being-carried-across: The waiting list, `being-carried-across`: not said in the documents (not said in the documents | not said in the documents | none | not said in the documents)
- C.states.waiting-list.carry-across-failed: The waiting list, `carry-across-failed`: not said in the documents (not said in the documents, including what happens if every try fails | not said in the documents | none | not said in the documents)
- C.states.waiting-list.out-of-date: The waiting list, `out-of-date`: not said in the documents (The list not being changed or corrected once it is across; which events call for a change is not said in the documents | People can see places that are out of date, once they can see places | none | "the places seen can go out of date or stay wrong" (003_slices.md, line 15))
- C.states.waiting-list.wrong: The waiting list, `wrong`: not said in the documents (not said in the documents | People can see places that stay wrong, once they can see places | none | "the places seen can go out of date or stay wrong" (003_slices.md, line 15))
- C.states.waiting-list.ended: The waiting list, `ended`: not said in the documents (not said in the documents, including what is left afterwards | not said in the documents | none | not said in the documents)
- C.states.dead-end.1: for the owner's list: `being-carried-across`: no way out. The documents do not say what the list keeper is left with while it is only partly across.
- C.states.dead-end.2: for the owner's list: `carry-across-failed`: no way out. The documents do not say what the list keeper is left with.
- C.states.dead-end.3: for the owner's list: `carried-across`: no way out. The list keeper has the list as carried across; no slice includes changing it.
- C.states.dead-end.4: for the owner's list: `out-of-date`: no way out. The places on the list can stay out of date.
- C.states.dead-end.5: for the owner's list: `wrong`: no way out. The places on the list can stay wrong.
- C.states.dead-end.6: for the owner's list: `ended`: no way out. The documents do not say what is left or whether the list can be started again.
