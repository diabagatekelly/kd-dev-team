# Questions

<!-- drawn from: 2084867541 -->

Drawn by script from kept.md and the slice's documents. Nothing here is answered.

## From the library

- L.sync-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): When two copies hold different changes to the same thing, which one stands, and is the person shown both?
- L.sync-02.bringing-across: bringing-across: Is any change ever discarded without the person who made it being told, and can a discarded change be recovered?
- L.sync-03.bringing-across: bringing-across: How and when is a person told that something they saved earlier was not accepted, and what happens to their change?
- L.sync-04.shown-list: shown-list: How does a person know how old the information in front of them is, and what is shown when there is none yet?
- L.sync-07.bringing-across: bringing-across: What does the product do about changes made at the source during an update: pick them up in the same pass, the next one, or not at all?
- L.sync-08.bringing-across: bringing-across: How does the product know an update brought everything, and what does it show while it has caught up only partly?
- L.sync-11.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What can a person still do with the local copy, and can they take their information elsewhere, if the source never comes back?
- L.limits-04.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What is the most the product is meant to handle at one time, and what does it do with demand beyond that?
- L.limits-06.bringing-across: bringing-across: What is a person or a calling system told when a limit stops them, and can they tell what to do next?
- L.limits-07.bringing-across: bringing-across: What is the largest single item the product accepts, and what happens to one that is larger?
- L.limits-08.shown-list: shown-list: How many items may be asked for or shown in one go, and how does a person reach the rest?
- L.durable-write-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product guarantee is stored when a save is cut off partway: all of the old content, all of the new, or something it can detect and repair?
- L.durable-write-02.bringing-across: bringing-across: At what moment does the product say a change is saved, and how much recently confirmed work may be lost if power fails right after?
- L.durable-write-03.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): On what kinds of storage does the product promise its saved data survives a power loss, and how would it notice damage on storage that does not keep that promise?
- L.durable-write-04.bringing-across: bringing-across: What does the person see, and what state is the previously saved data in, when a save fails for lack of space?
- L.durable-write-05.bringing-across: bringing-across: What does the product do after storage reports a failed save, given that trying again and being told it worked does not prove the data is there?
- L.durable-write-06.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): When saved data is replaced wholesale, what is guaranteed to be found after a crash at any point during the replacement?
- L.durable-write-08.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which pieces of saved data must always agree with one another, and what does the product do when it finds them disagreeing after a crash?
- L.durable-write-09.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How does the product detect saved data that has silently changed since it was written, and what does it do with it?
- L.durable-write-10.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How are copies of the saved data (backups, exports, device transfers) taken so that a copy made during a save is still usable?
- L.durable-write-11.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which files together make up the saved data, and what happens when only some of them are moved, copied, restored or cleaned up?
- L.durable-write-12.bringing-across: bringing-across: What happens to a save that is still in progress when the product is closed, and how does the person learn on return that it did not happen?
- L.startup-read-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product do at start when its saved data is damaged: refuse to run, run with what can be read, or start fresh, and what is the person told?
- L.startup-read-02.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product do when the thing in its saved-data location is not recognisably its own, and does it ever overwrite it?
- L.startup-read-03.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How does the product tell a first run with nothing saved apart from saved data that exists but cannot be opened, and what does it do in each case?
- L.startup-read-04.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product do at start when it finds a save that an earlier run left unfinished: complete it, undo it, or ask?
- L.startup-read-05.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product do when it may read its saved data but not change it, including when that data needs repair first?
- L.startup-read-06.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does a starting copy of the product do when another copy is already repairing the saved data: wait, for how long, and what does it show meanwhile?
- L.startup-read-07.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Where can the platform remove the product's saved data on its own, and what does the person find, and can get back, when that has happened?
- L.startup-read-08.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): After a rescue of damaged saved data, what is checked before the result is used, and how is the person told what may be missing, changed or back again?
- L.startup-read-09.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How would the product or its owner find out that saved data is readable but wrong, and how far back can a good version be recovered?
- L.startup-read-10.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which spare copy does the product fall back on when its saved data is unusable, and when was bringing it back last actually tried?
- L.concurrency-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): When two changes to the same item are made from what each saw earlier, which survives, and is the person whose change was replaced told?
- L.concurrency-02.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which rules span more than one item, and how are they kept true when two operations each change a different item at the same moment?
- L.concurrency-03.shown-list: shown-list: Which sets of items must always be read as they stood at a single moment, and how is that ensured while changes are going on?
- L.concurrency-05.bringing-across: bringing-across: Can anything see or act on a change before it is final, and what happens to what was built on it if the change is withdrawn?
- L.concurrency-06.shown-list: shown-list: After a change is confirmed, how soon must every window, copy and device show it, and what does a person see in the meantime?
- L.concurrency-08.bringing-across: bringing-across: What does the product do when the stored data is in use by another operation: wait, try again, or tell the person, and for how long?
- L.concurrency-09.bringing-across: bringing-across: When an operation is cancelled because it clashed with another, is it repeated automatically from the start, and what if it cannot simply be repeated?
- L.concurrency-12.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What stops two copies of the product from changing the same stored data at once, and in which setups (shared or remote storage, mixed versions) does that protection not hold?
- L.lifecycle-01.bringing-across: bringing-across: When making something takes several steps and a later one fails, what is done about the steps already carried out, and who decides between undoing them and carrying on another way?
- L.lifecycle-02.bringing-across: bringing-across: How is a thing shown and handled when undoing it has itself failed, and who is alerted to sort it out by hand?
- L.lifecycle-03.bringing-across: bringing-across: Which steps cannot be taken back once done, and is everything that could still fail checked before them?
- L.lifecycle-04.bringing-across: bringing-across: How long may a thing stay in progress before the product treats the work as failed, and what then happens to it?
- L.lifecycle-05.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which records only make sense as a pair or set, and how is one that exists without its partner found and dealt with?
- L.lifecycle-08.bringing-across: bringing-across: How long is something that was started and then abandoned kept, and what removes it afterwards?
- L.user-input-01.person-name: person-name: How long may each typed value be, and what does the person see when theirs is longer?
- L.user-input-02.bringing-across: bringing-across: Which fields are truly required, and what can a person do who has no value for one of them?
- L.user-input-03.person-name: person-name: Which characters does each field accept, and on what grounds is any character refused?
- L.user-input-04.person-name: person-name: Is each value asked for whole or in parts, and what happens when a person's value has fewer, more or differently ordered parts?
- L.user-input-05.bringing-across: bringing-across: Where is each rule about a typed value enforced, and what happens to a value that arrives without having passed the on-screen check?
- L.user-input-06.bringing-across: bringing-across: For each way a value can be refused, what does the message say and where does it appear?
- L.user-input-07.person-name: person-name: Is an empty or all-spaces value accepted, and are spaces around a value kept, removed or refused?
- L.user-input-09.person-name: person-name: Which values must be unique, how is sameness judged, and what is the person told when theirs is taken?
- L.user-input-10.person-name: person-name: Wherever typed text is later shown, stored or passed on, how is it kept from being acted on as anything but text?
- L.user-action-01.bringing-across: bringing-across: What does the person see at once after starting an operation, and what happens if they start it a second time before the first has finished?
- L.user-action-02.shown-list: shown-list: What does reloading do on each screen that follows an operation that changed something?
- L.user-action-03.shown-list: shown-list: What does each screen show, and what can be done from it, when it is reached by stepping back after the operation it led to?
- L.user-action-04.shown-list: shown-list: What remains visible on the device after a person signs out, including on screens reached by stepping back?
- L.user-action-05.bringing-across: bringing-across: When are a person's changes saved, and what becomes of unsaved ones when they leave without warning the product?
- L.user-action-06.bringing-across: bringing-across: What does a person find when they come back to a screen their device has suspended or discarded in the meantime?
- L.user-action-07.bringing-across: bringing-across: When the same person has several windows open, how does each learn of a change made in another, and which one wins if both act?
- L.user-action-08.bringing-across: bringing-across: Which actions can be undone, for how long, and what can a person do about one that cannot?
- L.user-action-09.bringing-across: bringing-across: Which actions ask for confirmation, and why will a person still read the question on the one that matters?
- L.user-action-10.bringing-across: bringing-across: At each step of a longer operation, how does a person back out, and what is left behind if they do or simply leave?
- L.user-action-11.way-back-in: way-back-in: What happens to work in progress when a person's signed-in period ends, and can they carry on after signing in again?
- L.user-action-12.shown-list: shown-list: What does a saved address to each screen lead to when the person is signed out, or when what it pointed at no longer exists?
- L.long-operation-01.bringing-across: bringing-across: For each operation that can take more than a few seconds, what is the person shown while it runs?
- L.long-operation-02.bringing-across: bringing-across: How can a person tell an operation that is still working from one that has stopped?
- L.long-operation-03.bringing-across: bringing-across: Which operations can be stopped once started, and how?
- L.long-operation-04.bringing-across: bringing-across: When an operation is stopped partway, is the finished part undone, kept or completed later, and how is it shown?
- L.long-operation-05.bringing-across: bringing-across: How does a person who went elsewhere learn that an operation ended, and where do they find its result?
- L.long-operation-06.bringing-across: bringing-across: After an interruption in the middle of an operation, does it resume, restart or stay abandoned, and what state is left meanwhile?
- L.long-operation-07.bringing-across: bringing-across: Where is a late failure recorded, and how does the person who started the operation come to know of it?
- L.long-operation-08.bringing-across: bringing-across: When only some items of an operation succeed, what is kept, what is reported, and how are the failed ones tried again?
- L.long-operation-09.bringing-across: bringing-across: After how long without progress is an operation treated as stuck, and what happens to it then?
- L.long-operation-10.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How long is the result of a finished operation kept, and what does a person find after that?
- L.long-operation-11.bringing-across: bringing-across: When an operation is requested on something that already has one running, is the new one refused, queued, or does it replace the old?
- L.long-operation-12.bringing-across: bringing-across: What is checked before a long operation is accepted, so that a request sure to fail is refused at once?
- L.text-01.person-name: person-name: When are two pieces of text counted as the same, and is that settled before they are stored or each time they are compared?
- L.text-02.person-name: person-name: Where does the product ignore the difference between capital and small letters, and by which language's rules?
- L.text-03.person-name: person-name: What does the product do with unseen characters and unusual spaces in text it stores and compares?
- L.text-05.person-name: person-name: How does the product measure the length of text, and where may it cut text that is too long?
- L.text-09.shown-list: shown-list: Wherever a stored or typed value is put into a sentence or a row, what keeps text of the opposite direction from disturbing what surrounds it?
- L.text-10.shown-list: shown-list: Where must people tell names or labels apart by eye, and what stops one being made to look like another?
- L.text-12.shown-list: shown-list: How much room does each label and message have, and what happens when the wording in another language is longer or taller?
- L.presentation-04.shown-list: shown-list: How is wording that includes a count chosen for zero, one and each other form the reader's language has?
- L.presentation-12.shown-list: shown-list: When a list too long for one screen is put in order, does the order hold across all of it?
- L.secrets-01.way-back-in: way-back-in: Where does each credential the product uses live, and who can read that place?
- L.secrets-02.way-back-in: way-back-in: Which credentials are unique to each installation or person, and how does each one come to be set?
- L.secrets-05.way-back-in: way-back-in: When a credential is exposed, who cancels it, how fast, and what stops working until the new one is in place?
- L.secrets-09.way-back-in: way-back-in: In what form is each credential stored and sent, and who could read it on the way or at rest?
- L.authorization-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): For every operation and every kind of data, who is allowed, and where is that checked?
- L.authorization-03.bringing-across: bringing-across: Where is each permission enforced, and what happens to a request that bypasses the screen?
- L.authorization-04.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What may a person do when no rule mentions them or the thing they ask for?
- L.authorization-05.way-back-in: way-back-in: When and how are a person's permissions reduced or removed as their role changes?
- L.authorization-06.bringing-across: bringing-across: How does the product tell a request the person meant to make from one sent in their name by someone else's page?
- L.authorization-07.bringing-across: bringing-across: Which operations change something, and can any of them happen just because a link was followed or a page was loaded?
- L.authorization-08.shown-list: shown-list: What does the product do with a request when the check of its permission cannot be completed?
- L.authorization-10.way-back-in: way-back-in: Which facts about a person's identity and permissions does the product take from the person's device, and how does it know they were not altered?
- L.authorization-11.way-back-in: way-back-in: How soon after signing out or losing access does everything a person already held stop working?
- L.authorization-12.way-back-in: way-back-in: How does the product make sure the account a person ends up signed in to is the one they chose?
- L.configuration-05.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does each setting default to, and is the product safe to run if no default is ever changed?
- L.configuration-06.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What is switched on in a fresh installation, and which of it is actually needed?
- L.configuration-07.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): In what ways do the settings of the trial and real installations differ, and how is each difference accounted for?
- L.configuration-11.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which diagnostic modes exist, and what guarantees each is off where the product is really used?
- L.configuration-12.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Who and what can change each setting, and which settings can be influenced from outside?
- L.logging-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which events must always leave a record?
- L.logging-02.bringing-across: bringing-across: What must every record say so that someone can later tell what happened and to whom?
- L.logging-03.person-name: person-name: Which values must never appear in a record, and how are they kept out?
- L.logging-04.person-name: person-name: How is outside-supplied text recorded so that it cannot pass for, or damage, the product's own entries?
- L.logging-05.bringing-across: bringing-across: What does the product do when it cannot write a record: stop, continue without it, or something else?
- L.logging-06.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How much may the records grow, and what happens when that limit is reached?
- L.logging-07.bringing-across: bringing-across: When something fails, what does the person see and what goes only into the records?
- L.logging-08.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Where are the records kept, and do they survive the loss of the machine that wrote them?
- L.logging-09.bringing-across: bringing-across: Who or what reads the records, and which entries make someone get told?
- L.logging-10.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Who can change or remove records, and how would a change or removal be noticed?
- L.logging-11.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which clock does each record's time come from, and how are records from different places put in order?
- L.logging-12.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How long is each kind of record kept, and what removes it when that time is up?
- L.accessibility-01.bringing-across: bringing-across: For each thing a person can do on the screen, how is it done using the keyboard alone?
- L.accessibility-02.shown-list: shown-list: From every part of the screen a keyboard user can enter, how do they leave it?
- L.accessibility-03.shown-list: shown-list: How is the item that has keyboard focus shown, on every item that can take it?
- L.accessibility-04.bringing-across: bringing-across: Where does focus go when the item holding it closes or is removed?
- L.accessibility-05.bringing-across: bringing-across: What name and purpose does each control announce to someone who cannot see it?
- L.accessibility-06.shown-list: shown-list: For everything shown that is not text, what words give the same meaning?
- L.accessibility-07.bringing-across: bringing-across: How does someone who cannot see the screen learn the result of what they just did?
- L.accessibility-08.shown-list: shown-list: Wherever colour carries meaning, what else on the screen carries the same meaning?
- L.accessibility-09.shown-list: shown-list: What contrast between text and its background does every screen keep, in every state and theme?
- L.accessibility-10.shown-list: shown-list: What happens to each screen when its text is enlarged to twice its size?
- L.accessibility-11.bringing-across: bringing-across: Which steps have a time limit, and how does a person who needs longer get it?
- L.accessibility-12.shown-list: shown-list: What moves on the screen, and how does a person who asked for less motion get the product without it?
- L.sign-in-01.way-back-in: way-back-in: What stops someone guessing or replaying credentials at sign-in, and what does a person locked out by it do?
- L.sign-in-02.way-back-in: way-back-in: Which accounts exist before anyone signs up, and how is each removed or made unusable?
- L.sign-in-04.way-back-in: way-back-in: How does a person get back in after forgetting or losing what they sign in with, and how is that kept as strong as signing in?
- L.sign-in-05.way-back-in: way-back-in: How is a person's first credential or activation code made, delivered and ended?
- L.sign-in-06.way-back-in: way-back-in: What are all the ways to sign in, and is each held to the same strength?
- L.sign-in-07.way-back-in: way-back-in: What is a person told when their sign-in details change or an unusual sign-in happens, and by which route?
- L.sign-in-08.way-back-in: way-back-in: How long does a session last unused, and in all, before the person must sign in again, and on what grounds?
- L.sign-in-09.way-back-in: way-back-in: How many sessions may one account have at once, and what happens when one more starts?
- L.sign-in-10.way-back-in: way-back-in: What happens to the session a person held before signing in, and is a fresh one made at every sign-in?
- L.sign-in-11.way-back-in: way-back-in: Which changes and operations make a person prove again who they are, even while signed in?
- L.sign-in-12.way-back-in: way-back-in: How does a person, or whoever runs the product, see and end the sessions of an account?
- L.stored-data-01.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which data the product creates or holds would harm someone if seen or changed, and how strongly must each kind be protected?
- L.stored-data-02.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Who could read each kind of sensitive data where it is stored and in every copy made of it, and what makes it unreadable to anyone else?
- L.stored-data-03.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which keys protect what, where does each one live, and what may each be used for?
- L.stored-data-04.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What happens to protected data when its key is lost, exposed or replaced?
- L.stored-data-05.person-name: person-name: Does any sensitive value travel in an address or its query, and where would that be recorded?
- L.stored-data-06.shown-list: shown-list: Which components in between may keep a copy of a reply, and how is sensitive data kept out of them?
- L.stored-data-07.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Which other parties receive any data from the product, and is any of it sensitive?
- L.stored-data-08.shown-list: shown-list: For each reply, which fields are sent, and is any sent that the asker does not need or may not see?
- L.stored-data-09.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): How long is each kind of sensitive data kept, and what removes it when that time is up?
- L.stored-data-10.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What does the product store on the person's device, and is any of it sensitive?
- L.stored-data-12.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): Is the reading of sensitive data recorded, without the data itself, and who looks at that record?
- L.misuse-01.bringing-across: bringing-across: Which steps must happen in order, and what does the product do with a request for a later step when an earlier one was not done?
- L.misuse-02.bringing-across: bringing-across: What limits does each rule of the product set, and where is each enforced?
- L.misuse-03.bringing-across: bringing-across: What could a script do by calling the product again and again, and what stops it?
- L.misuse-04.bringing-across: bringing-across: Is anything done faster than a person could a sign of abuse here, and what is done about it?
- L.misuse-05.bringing-across: bringing-across: Which actions are grave enough to need a second person's agreement?
- L.misuse-07.bringing-across: bringing-across: Which fields may each request set, and what happens to a field that is sent and was not meant to be set?
- L.misuse-08.waiting-list: waiting-list (in each of its states: not-brought-across, being-brought-across, brought-across, behind-notebook, refused-each-time, stopped-by-itself, ended): What is in limited supply, and can a person take more than their share by how they ask?

## Each value taken in, each way it can be wrong

- V.person-name.missing: `person-name` (The list keeper, from the notebook) is missing, or null: what does the product do, and what is the person told?
- V.list-order.empty: `list-order` (The list keeper, from the notebook) is empty: what does the product do, and what is the person told?
- V.list-order.missing: `list-order` (The list keeper, from the notebook) is missing, or null: what does the product do, and what is the person told?
- V.list-order.malformed: `list-order` (The list keeper, from the notebook) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.list-order.long: `list-order` (The list keeper, from the notebook) is far longer or larger than expected: what does the product do, and what is the person told?
- V.list-order.twice: `list-order` (The list keeper, from the notebook) is the same as one already there: what does the product do, and what is the person told?
- V.stored-list.empty: `stored-list` (The list as kept, read back when the list keeper returns) is empty: what does the product do, and what is the person told?
- V.stored-list.missing: `stored-list` (The list as kept, read back when the list keeper returns) is missing, or null: what does the product do, and what is the person told?
- V.stored-list.malformed: `stored-list` (The list as kept, read back when the list keeper returns) is of the wrong type or malformed: what does the product do, and what is the person told?
- V.stored-list.long: `stored-list` (The list as kept, read back when the list keeper returns) is far longer or larger than expected: what does the product do, and what is the person told?
- V.stored-list.twice: `stored-list` (The list as kept, read back when the list keeper returns) is the same as one already there: what does the product do, and what is the person told?
- V.every-setting.missing: any setting the build reads is missing, or null: what does the product do at start, and who is told?
- V.every-setting.empty: any setting the build reads is empty: what does the product do at start, and who is told?
- V.every-setting.malformed: any setting the build reads is of the wrong type or malformed: what does the product do at start, and who is told?
- V.every-setting.outside: any setting the build reads is outside what is allowed: what does the product do at start, and who is told?
Not drawn, 4 already asked of the same thing by a library question above.

## Each class of sensitive values, each place it can leak to

- X.waiting-people.logs: can any of `person-name`, `list-order`, `stored-list` reach what the product logs, on the path that works and on each that fails?
- X.waiting-people.errors-inside: can any of `person-name`, `list-order`, `stored-list` reach an error's own message and trace, on the path that works and on each that fails?
- X.waiting-people.errors-shown: can any of `person-name`, `list-order`, `stored-list` reach an error shown or returned to whoever asked, on the path that works and on each that fails?
- X.waiting-people.telemetry: can any of `person-name`, `list-order`, `stored-list` reach what is sent to monitoring or measurement, on the path that works and on each that fails?
- X.waiting-people.samples: can any of `person-name`, `list-order`, `stored-list` reach test data and examples kept with the code, on the path that works and on each that fails?
- X.waiting-people.replies: can any of `person-name`, `list-order`, `stored-list` reach a reply that succeeded, to whoever asked, on the path that works and on each that fails?
- X.waiting-people.stored: can any of `person-name`, `list-order`, `stored-list` reach where it is stored, and every copy made of that, on the path that works and on each that fails?

## Each state, each event

- S.waiting-list.not-brought-across.bring-notebook-order-across-1: The waiting list is `not-brought-across` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.not-brought-across.bring-notebook-order-across-2: The waiting list is `not-brought-across` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.not-brought-across.again: The waiting list is `not-brought-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.not-brought-across.reopened: The waiting list is `not-brought-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.not-brought-across.time: The waiting list is `not-brought-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.being-brought-across.bring-notebook-order-across-1: The waiting list is `being-brought-across` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.being-brought-across.bring-notebook-order-across-2: The waiting list is `being-brought-across` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.being-brought-across.again: The waiting list is `being-brought-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.being-brought-across.reopened: The waiting list is `being-brought-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.being-brought-across.time: The waiting list is `being-brought-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.brought-across.bring-notebook-order-across-1: The waiting list is `brought-across` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.brought-across.bring-notebook-order-across-2: The waiting list is `brought-across` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.brought-across.again: The waiting list is `brought-across` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.brought-across.reopened: The waiting list is `brought-across` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.brought-across.time: The waiting list is `brought-across` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.bring-notebook-order-across-1: The waiting list is `behind-notebook` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.bring-notebook-order-across-2: The waiting list is `behind-notebook` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.again: The waiting list is `behind-notebook` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.reopened: The waiting list is `behind-notebook` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.behind-notebook.time: The waiting list is `behind-notebook` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.refused-each-time.bring-notebook-order-across-1: The waiting list is `refused-each-time` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.refused-each-time.bring-notebook-order-across-2: The waiting list is `refused-each-time` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.refused-each-time.again: The waiting list is `refused-each-time` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.refused-each-time.reopened: The waiting list is `refused-each-time` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.refused-each-time.time: The waiting list is `refused-each-time` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.stopped-by-itself.bring-notebook-order-across-1: The waiting list is `stopped-by-itself` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.stopped-by-itself.bring-notebook-order-across-2: The waiting list is `stopped-by-itself` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.stopped-by-itself.again: The waiting list is `stopped-by-itself` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.stopped-by-itself.reopened: The waiting list is `stopped-by-itself` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.stopped-by-itself.time: The waiting list is `stopped-by-itself` and a long time passes with nothing done: what happens to it, and what is the person shown?
- S.waiting-list.ended.bring-notebook-order-across-1: The waiting list is `ended` and what bring-notebook-order-across / 1 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.ended.bring-notebook-order-across-2: The waiting list is `ended` and what bring-notebook-order-across / 2 describes is done: what happens to it, and what is the person shown?
- S.waiting-list.ended.again: The waiting list is `ended` and the same action is done again at once: what happens to it, and what is the person shown?
- S.waiting-list.ended.reopened: The waiting list is `ended` and the page is reloaded, or the product closed and reopened, partway through: what happens to it, and what is the person shown?
- S.waiting-list.ended.time: The waiting list is `ended` and a long time passes with nothing done: what happens to it, and what is the person shown?
Not drawn, 14 already asked of the same thing by a library question above.

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

- T.waiting-people.shown-list: someone after `waiting-people` comes through `shown-list`: Someone other than the list keeper reads the names of the people waiting and the order they are in. What stops it, and how would anyone know it was tried?
- T.waiting-people.bringing-across: someone after `waiting-people` comes through `bringing-across`: Someone who can read what passes while the list is brought across learns who is waiting and in what order. What stops it, and how would anyone know it was tried?
- T.waiting-people.way-back-in: someone after `waiting-people` comes through `way-back-in`: Someone gets in as the list keeper and reads the name and place of everyone waiting. What stops it, and how would anyone know it was tried?
- T.waiting-list.bringing-across: someone after `waiting-list` comes through `bringing-across`: Someone who wants a plot sooner gets a changed order brought across, in their own way or in the list keeper's name, and a person who has waited longer is put behind. What stops it, and how would anyone know it was tried?
- T.waiting-list.way-back-in: someone after `waiting-list` comes through `way-back-in`: Someone takes over the way in and shuts the list keeper out, who can no longer see the list they brought across. What stops it, and how would anyone know it was tried?
- T.waiting-list.shown-list: someone after `waiting-list` comes through `shown-list`: A person waiting gives a name written to be acted on rather than read, and when it is shown to the list keeper the list they see or the list kept is changed. What stops it, and how would anyone know it was tried?

## Asked of every slice

- W.unavailable: What happens, and to whom, if what this slice adds cannot be used for an hour?
- W.target: How often may it fail, and how slow is too slow, before someone would say it does not work?
- W.noticed: Who notices when it breaks, and how?
- W.sensitive: What does this slice touch that would harm someone if another person saw or changed it?
- W.who-sees: Who uses it, and may any of them see or change what belongs to another?
- W.obligations: Does a law, a contract or an outside system's terms bind how this is handled?
- W.prize: What would someone who means harm want from what this slice adds?

## Carried from research

- C.states.waiting-list.being-brought-across: The waiting list, `being-brought-across`: not said in the documents (not said in the documents | not said in the documents | not said in the documents | not said in the documents)
- C.states.waiting-list.refused-each-time: The waiting list, `refused-each-time`: not said in the documents (not said in the documents | not said in the documents | not said in the documents | not said in the documents)
- C.states.waiting-list.stopped-by-itself: The waiting list, `stopped-by-itself`: not said in the documents (not said in the documents | not said in the documents | not said in the documents | not said in the documents)
- C.states.waiting-list.ended: The waiting list, `ended`: not said in the documents (not said in the documents | not said in the documents | not said in the documents | not said in the documents)
- C.states.dead-end.1: for the owner's list: `brought-across`: no way out. The list keeper has the list in the order it was brought across. Changing it, or putting right a wrong place, is left for later (slice-001/004_slice.md lines 17 and 18).
- C.states.dead-end.2: for the owner's list: `behind-notebook`: no way out. The list brought across no longer matches the notebook if the change affects what it holds; the notebook can still be kept up to date and checked against.
