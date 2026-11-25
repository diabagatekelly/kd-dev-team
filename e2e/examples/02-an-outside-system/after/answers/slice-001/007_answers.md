# Answers: slice 1

## A1: Saved means kept, and nothing is dropped silently
Kind: chosen
Says: The product says a walk is saved, and lists it as saved, only after the store has confirmed it is kept. An entry that is not confirmed is shown as not saved while the entry screen is still open, with what was typed still there to send again. No entry is accepted and later discarded.
Rests on: A walker takes a listed walk as saved and invoices will rest on it; confirming before listing leaves nothing that can be withdrawn later.
Settles: L.sync-02.save-request, L.sync-03.save-request, L.concurrency-05.walks-list
Under: walker-walk-entry
Criterion: Given a walker with a filled-in entry, when the product cannot confirm that the walk was kept, then they are told it was not confirmed as saved, what they typed is still there, and the list does not show it as saved.

## A2: The list says when it could not be read
Kind: chosen
Says: The walks list is read from the store each time it is opened. While it loads it says so; if it cannot be read it says so and offers to try again, and never shows "no walks" in its place. No older copy is shown as current.
Rests on: An empty list and an unread list look alike, and a walker would enter the same walks twice.
Settles: L.sync-04.walks-list
Under: walker-walk-entry
Criterion: Given a walker with at least one saved walk, when the list cannot be read, then they are told it could not be loaded and can try again, and they are not told they have no walks.

## A3: Whether walks can be entered with no signal
Kind: owner
Says: To decide: whether a walker must be able to enter walks while the phone has no signal. It also settles what the phone holds before it is sent, and what happens to that if the phone has to start again. What other answers say about unsent entries and what the phone holds (A20, A26, A43, A48, A95, A122) is written for the first option and is looked at again if the second is chosen.
Options: entry needs a signal, and an unsent entry is not kept once the screen is gone | walkers can enter with no signal, and the phone holds entries and sends them later
Recommended: entry needs a signal; it is the smaller slice and never leaves a walk that looks entered but has not arrived. If walkers often have no signal where they work, choose the other.
If left: slice 1 cannot say what happens to an entry made without a signal.
Harm: high
Settles: L.sync-05.save-request, L.limits-11.save-request
Under: walker-walk-entry

## A4: A partial list is never shown as whole
Kind: chosen
Says: The list is shown in parts, newest day first. It says when there are older walks not yet shown and lets the walker get them. A part that fails to load is reported as failed, not left out.
Rests on: A walker checks the list to see what is recorded; a silently short list reads as missing walks.
Settles: L.sync-08.walks-list, L.limits-08.walks-list
Under: walker-walk-entry
Criterion: Given a walker with more saved walks than the first part of the list holds, when they open the list, then it shows that there are older walks and lets them reach every one.

## A5: What is fetched, and when
Kind: chosen
Says: The list is fetched when the walker opens it, after a save, when they ask for older walks and when they try again. It fetches 50 walks at a time. Nothing is fetched in the background.
Rests on: Four walkers' lists are small; fetching on use needs no schedule and spends no phone data while the product is not in use.
Settles: L.sync-12.walks-list
Under: walker-walk-entry
Criterion: Given a walker with 51 saved walks, when they open the list, then it shows the 50 newest and offers the older one.

## A6: One version writes at a time, and older data is never damaged
Kind: chosen
Says: Walks and clients are kept in one central store that only the running product writes, and the saved data carries a format version. A phone showing an older screen has its entry either accepted whole by the current rules or refused with a request to reload; it never writes the store directly. During an update only one version writes.
Rests on: Keeping all writing in one place means mixed phone versions cannot damage each other's walks.
Settles: L.sync-09.walk, L.migration-04.walk
Under: walker-walk-entry
Criterion: Given a walker whose open screen is from an older version the product no longer accepts, when they save a walk, then they are told to reload and the walk is not shown as saved.

## A7: What walkers keep if the product is gone for good
Kind: owner
Says: To decide: whether anyone must be able to take the walks out of the product if it can no longer be reached for good. A phone keeps no copy under the recommended way of entering.
Options: no export in this slice; recovery rests on the business owner's spare copies | the business owner can take all walks out as a file
Recommended: no export in this slice; invoicing is not yet built, so the owner still works as they do today, and spare copies are asked about separately.
If left: nobody can take walks out except by whoever maintains the product.
Harm: medium
Settles: L.sync-11.walks-list
Under: walker-walk-entry

## A8: No quota for a walker
Kind: chosen
Says: No walker has a limit on how many walks they may enter in total. Protection against a flood of requests is a separate rate limit (see the answer on repeated sending).
Rests on: A cap on walks would stop real work from being recorded, and the volume of four walkers is small.
Settles: L.limits-03.walk
Under: walker-walk-entry

## A9: How much the product must handle
Kind: owner
Says: To decide: how many walkers using it at once, and how many clients, the product must handle. The documents give four walkers and about sixty clients, with holiday cover expected to roughly double it; they do not say whether that doubles walkers, walks or clients. Beyond what is chosen, a request that cannot be served is refused with a message to try again, never half done. Speed is asked in A153.
Options: 10 walkers using it at once and 120 clients | 25 walkers using it at once and 300 clients
Recommended: the first; it covers the doubling with room to spare.
If left: there is no number to test load or speed against.
Harm: medium
Settles: L.limits-04.installation
Under: walker-walk-entry

## A10: A refusal says why and what to do
Kind: chosen
Says: Whenever a limit or rule stops an entry, the walker is told which one, whether to change something or wait, and what they typed stays on the screen.
Rests on: A refusal with no next step leaves the walk unrecorded.
Settles: L.limits-06.entry-screen
Under: walker-walk-entry
Criterion: Given a walker who has sent 30 save requests in the last 60 seconds, when they save a walk, then they are told to wait 60 seconds and try again, and what they entered is still there.

## A11: The largest request
Kind: chosen
Says: An entry holds only a client chosen from a list, a day and a length. A request larger than 4 KB is refused and nothing of it is kept.
Rests on: The three values need far less than 4 KB.
Settles: L.limits-07.save-request
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request larger than 4 KB is sent, then it is refused and no walk is added.

## A12: A walk is kept whole or not at all
Kind: chosen
Says: A walk is written in one all-or-nothing step, with its client, day, length and walker together. An interrupted save leaves either the whole walk or nothing, and nothing unfinished has to be completed or asked about at start. This holds for the last record written too.
Rests on: A single transaction is the known solution to half-written records.
Settles: L.durable-write-01.walk, L.durable-write-07.walk, L.startup-read-04.walk
Under: walker-walk-entry
Criterion: Given a walker saving a walk, when the product is stopped partway through the save and started again, then the list shows either the whole walk or no walk from that entry.

## A13: How much saved work may be lost
Kind: owner
Says: To decide: how much confirmed work may be lost to a failure, how far back a good version must be recoverable, and how often bringing a spare copy back is tried. The product confirms a walk only once the store says it is kept (A1). A walk that is readable but wrong can only be noticed by the walker or the business owner reading the list.
Options: no confirmed walk lost to a power cut; a daily spare copy kept 30 days, with a restore tried before first use and every 3 months, so a lost or ruined store may lose up to a day | the same, with spare copies taken so that at most an hour can be lost | no spare copies
Recommended: the first; a day of walks can still be re-entered from memory, and it is far safer than one paper sheet.
If left: walks have no promised spare copy, and a lost store could lose all of them.
Harm: high
Settles: L.durable-write-02.walk, L.startup-read-10.installation, L.startup-read-09.walk
Under: walker-walk-entry

## A14: Storage that keeps its promise on power loss
Kind: test
Says: Not known: whether the storage the product will run on keeps confirmed writes through a power loss, and whether it reports damage. No hosting or storage is chosen and no page about one has been read.
Test: once storage is chosen, read its own statement on durability and damage checks, and cut a test installation off during saves, then compare confirmed walks with stored ones.
Harm: high
Settles: L.durable-write-03.installation
Under: walker-walk-entry

## A15: A failed save, for lack of space or any other storage error
Kind: chosen
Says: Any storage failure, including no space, is a failed save: the walker is told it was not saved, what they typed stays, and walks saved earlier are untouched. The product never counts a later "success" of the same failed write as proof; a retry is a new complete write, and the walk is confirmed only by reading it back as kept. The failure is recorded.
Rests on: After a storage error the state of that write cannot be trusted; reading back what is kept is the safe check.
Settles: L.durable-write-04.save-request, L.durable-write-05.save-request
Under: walker-walk-entry
Criterion: Given a walker with one saved walk and a store that refuses new writes, when they save another walk, then they are told it was not saved and the list still shows the first walk unchanged.

## A16: A walk and its client always agree
Kind: chosen
Says: Every walk points to exactly one stored client and one walker, and the store refuses a walk whose client or walker does not exist. A client that has walks cannot be erased from under them. If a walk is nonetheless found without its client or walker, it is kept, reported to whoever maintains the product, and not shown as a normal walk.
Rests on: A reference the store enforces is the known way to keep a pair together.
Settles: L.durable-write-08.walk, L.durable-write-08.client, L.lifecycle-05.walk, L.concurrency-02.walk
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request names a client that does not exist, then it is refused and no walk is added.

## A17: Silent damage and unreadable data
Kind: chosen
Says: The store's own integrity check runs at every start and once a day. Damaged data is never repaired or overwritten automatically: the product refuses new saves, tells walkers it is unavailable and that nothing new is being saved, and records the fault for whoever maintains it.
Rests on: Carrying on over damaged data risks wrong bills and spoils the chance of recovery.
Settles: L.durable-write-09.walk, L.startup-read-01.installation
Under: walker-walk-entry
Criterion: Given saved data that fails its integrity check, when the product starts, then walkers are told it is unavailable, no walk can be saved, and the data is left as it was.

## A18: After a rescue
Kind: chosen
Says: Data brought back from damage or a spare copy is used only after it passes the integrity check and every walk has its client and walker. Whoever restores it records the moment the copy was taken and tells the business owner that walks entered after it may be missing and that later removals may be back; the owner asks the walkers to check their lists.
Rests on: A restore silently loses recent work unless the people who know the work are told the cut-off.
Settles: L.startup-read-08.walk
Under: walker-walk-entry

## A19: Copies and the files that belong together
Kind: chosen
Says: Spare copies and moves are made only with the store's own consistent-copy method, never by copying files during a save. Walks, clients and walker accounts are one set, copied and restored together. The files that make it up are listed for whoever maintains the product, and the product refuses to start on a partial set.
Rests on: The store's own copy method is the known way to get a usable copy while writes go on.
Settles: L.durable-write-10.installation, L.durable-write-11.installation
Under: walker-walk-entry
Criterion: Given walks being saved, when a spare copy is taken and restored to a test installation, then it starts, passes its integrity check, and every walk in it has its client and walker.

## A20: Closing during a save
Kind: chosen
Says: A save already sent may or may not complete if the walker closes the screen. On return the list read from the store shows what was really kept, and nothing else is shown as saved. While a save is under way the screen says it is not yet saved. Whether a save that never arrived is held on the phone and sent later follows what A3 settles.
Rests on: Only the store knows what arrived, so the list read from it is the truth.
Settles: L.durable-write-12.save-request
Under: walker-walk-entry
Criterion: Given a walker who closed the screen while a save was under way and the walk was not kept, when they open the list again, then the list does not show it as saved.

## A21: What is in the saved-data location
Kind: chosen
Says: A first run is started on purpose, by a set-up step. At normal start, a missing store, one that cannot be opened, or one without the product's own marker makes the product refuse to start and say which of these it is. It never creates a new store over, or writes into, something it does not recognise.
Rests on: Starting empty on a failed open would look like all walks vanished and could overwrite them.
Settles: L.startup-read-02.installation, L.startup-read-03.installation
Under: walker-walk-entry
Criterion: Given a saved-data location holding something that is not the product's own store, when the product starts, then it does not start, says why, and leaves what is there unchanged.

## A22: Readable but not writable
Kind: chosen
Says: If the data can be read but not changed, walkers can see their lists, are told that new walks cannot be saved just now, and the fault is recorded. Any needed repair waits for write access.
Rests on: Reading does no harm, and accepting entries that cannot be kept would lose walks.
Settles: L.startup-read-05.installation
Under: walker-walk-entry
Criterion: Given a store that can only be read, when a walker saves a walk, then they are told it was not saved, and their earlier walks are still listed.

## A23: One writer, and one repairer
Kind: chosen
Says: One running copy of the product changes the data at a time, held by an exclusive lock or by the store's own transactions. A second copy that would repair or upgrade waits up to 60 seconds, shows that it is waiting, then stops with that reason. The protection is not claimed for a store on shared network drives, which is not a supported set-up.
Rests on: A single holder with a bounded wait prevents two repairs from interleaving.
Settles: L.startup-read-06.installation, L.concurrency-12.installation
Under: walker-walk-entry
Criterion: Given one copy of the product holding the data for an upgrade, when a second copy starts, then the second changes nothing and stops with that reason after at most 60 seconds.

## A24: Whether the platform can remove the data
Kind: test
Says: Not known: whether the platform the product will be hosted on can remove its saved data on its own (inactivity, plan limits, redeploys), and what can be got back. No platform is chosen.
Test: once a platform is chosen, read its own pages on data deletion, inactivity and redeploys, and redeploy a test installation to see that walks remain.
Harm: high
Settles: L.startup-read-07.installation
Under: walker-walk-entry

## A25: Later and earlier versions
Kind: chosen
Says: A version that meets saved data marked with a later format refuses to start and says so; it neither reads part of it nor writes. Putting the previous version back is possible only while the format is unchanged; otherwise it refuses in the same way, and going back means restoring a spare copy.
Rests on: Refusing is the only behaviour that cannot damage data an older version does not understand.
Settles: L.migration-01.walk, L.migration-03.walk
Under: walker-walk-entry
Criterion: Given saved data marked with a later format version, when this version starts, then it does not start, says why, and changes nothing.

## A26: An older screen left open during an upgrade
Kind: chosen
Says: The central data is brought up to date by the running product, not by phones, so an open phone screen cannot block it. An old screen is handled as in A6: its entry is accepted whole or it is asked to reload. If A3 lets the phone hold entries, bringing those up to date is looked at again.
Rests on: The central store of A6 is upgraded in one place.
Settles: L.migration-05.installation
Under: walker-walk-entry

## A27: What the list reads together
Kind: chosen
Says: Each part of the list is read in one consistent read of walks and their client names, so a walk is never shown half saved or without its client while others are saving.
Rests on: A single read is the known way to get one moment's view.
Settles: L.concurrency-03.walks-list
Under: walker-walk-entry

## A28: When a confirmed walk shows
Kind: chosen
Says: Once a save is confirmed, the list on that phone includes the walk straight away. Another open screen or phone of the same walker shows it the next time its list is opened or reloaded.
Rests on: A walker uses one list at a time; live updating adds work for no stated need.
Settles: L.concurrency-06.walks-list
Under: walker-walk-entry
Criterion: Given a walker whose save has just been confirmed, when they see their list, then it includes that walk.

## A29: A busy store or a clash
Kind: chosen
Says: If the store is busy or a save is cancelled by a clash, the product tries the whole save again, up to 3 tries within 5 seconds, then tells the walker it was not saved and keeps what they typed. Repeating is safe because each entry carries its own identity and can be kept only once.
Rests on: A new walk reads nothing that a repeat could make stale, so a bounded automatic retry is safe.
Settles: L.concurrency-08.save-request, L.concurrency-09.save-request
Under: walker-walk-entry
Criterion: Given a store that stays busy, when a walker saves a walk, then after at most 3 tries within 5 seconds they are told it was not saved and can try again.

## A30: What cannot be taken back
Kind: chosen
Says: Saving a walk is the one step a walker cannot take back in slice 1, so every rule about the entry is checked before the walk is kept. The business owner's correction is slice 2, and a walker putting right their own entry waits on question 3.
Rests on: Checking everything first is the only protection where there is no way back; slice-001/004_slice.md leaves both kinds of correction for later.
Settles: L.lifecycle-03.walk
Under: walker-walk-entry

## A31: How long a save may take
Kind: owner
Says: To decide: how long a walker waits on a save before the product says it could not confirm it. After that they can send the same entry again without making a second walk.
Options: 15 seconds | 30 seconds
Recommended: 15 seconds; long enough for a weak signal, short enough that a walker does not walk off thinking it saved.
If left: there is no number for giving up on a save.
Harm: low
Settles: L.lifecycle-04.save-request
Under: walker-walk-entry

## A32: An abandoned entry
Kind: chosen
Says: An entry that was started and not sent is not kept anywhere. It lasts only as long as the screen it is typed on, so nothing has to remove it.
Rests on: Three values are quick to enter again, and drafts would need their own rules for expiry and privacy.
Settles: L.lifecycle-08.entry-screen
Under: walker-walk-entry

## A33: What the three values may be
Kind: chosen
Says: Client, day and length are all required. The client is picked from the clients offered, never typed as free text; text typed to search is only used to search, takes any character, stops at 100 characters, and spaces around it are ignored. The day is picked as a calendar date. The length is a whole number of minutes from 1 to 1440. An empty or all-spaces value counts as missing. Client names are shown whole as stored, not split into parts.
Rests on: The thin path gives client, day and length; picking rather than typing means no unknown client can be named, and 1440 minutes is one day.
Settles: L.user-input-01.entry-screen, L.user-input-02.entry-screen, L.user-input-03.entry-screen, L.user-input-04.walk-client, L.user-input-07.entry-screen, L.user-input-08.walk-length
Under: walker-walk-entry
Criterion: Given a walker with a client and a day chosen, when they save with a length of 0, 1441, 4.5 or nothing, then they are told what length is accepted and no walk is added.
Criterion: Given a walker with a client and a length filled in, when they save with no day, then they are told a day is needed and no walk is added.
Criterion: Given a walker with a client and a day chosen, when they save with a length of 1 or of 1440, then the walk is saved with that length.

## A34: Rules are enforced where the walk is kept
Kind: chosen
Says: Every rule about an entry is checked again by the product before the walk is kept; the screen's check is only a convenience. A request that breaks a rule is refused whole.
Rests on: Anything sent from a phone can be sent without the screen.
Settles: L.user-input-05.save-request
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request without a client is sent without using the screen, then it is refused and no walk is added.

## A35: Where a refusal is shown
Kind: chosen
Says: A missing client gives a message that a client is needed (walker-walk-entry / 2). Every other refusal names the value and what is accepted. Each message appears next to the value it is about, and one about the whole save appears by the save button.
Rests on: A message beside its field is found without hunting on a small screen.
Settles: L.user-input-06.client-needed-message
Under: walker-walk-entry

## A36: Telling clients with the same name apart
Kind: chosen
Says: A client is identified by the product's own identifier, not by name, so a walk always means one client. Where two offered clients have names that look the same once capitals and spacing are ignored, the choice shows a further label that tells them apart and is never an address or door code. Entering walks adds no client and changes no name.
Rests on: Two real clients can share a name, and the limit on addresses and door codes rules them out as labels where others could see them.
Settles: L.user-input-09.walk-client
Under: walker-walk-entry
Criterion: Given two offered clients with the same name, when a walker chooses a client, then they can tell the two apart without any address or door code being shown, and the saved walk is for the one chosen.

## A37: Typed and stored text is only ever text
Kind: chosen
Says: Client names and search text are always passed to the store as values and shown as plain text, never run or read as markup or commands. Names are shown isolated from the text around them, so right-to-left text cannot disturb a row or message.
Rests on: Separating values from code and escaping on output is the known solution.
Settles: L.user-input-10.entry-screen, L.text-09.client-name
Under: walker-walk-entry
Criterion: Given a client whose stored name contains markup characters, when a walker sees that name in the choice and in their list, then it appears exactly as written and nothing in it is acted on.

## A38: Which days a walk may be entered for
Kind: owner
Says: To decide: which days a walker may enter a walk for: whether a day still to come is allowed, and how far back a walk may be entered. Whatever is chosen, the boundary day is accepted, a day beyond it is refused with the allowed days named, and "today" is judged as in A50. This is separate from any month closing, which is question 3 of the requirements.
Options: today or any earlier day, never a day to come | only today and the previous 31 days | any day, including days to come
Recommended: today or any earlier day; a walk is a thing that has happened, and no cut-off is invented before question 3 is answered.
If left: the product cannot say whether a given day is refused.
Harm: medium
Settles: L.user-input-11.entry-screen, L.time-12.walk, V.walk-day.edge, V.walk-day.outside
Under: walker-walk-entry

## A39: How days and lengths are typed
Kind: chosen
Says: The day is chosen with a date picker, so no written date form is typed or guessed at. The length is typed as digits only, meaning minutes; signs, decimals, separators and units are refused, not interpreted.
Rests on: Removing free forms removes ambiguity.
Settles: L.user-input-12.walk-day, L.user-input-12.walk-length
Under: walker-walk-entry
Criterion: Given a walker on the entry screen, when they save with the length written as "1:30", then they are told the length is a whole number of minutes and no walk is added.

## A40: One entry makes at most one walk
Kind: chosen
Says: As soon as save is pressed the screen shows that it is saving and will not send again while waiting. Each entry carries its own identity from the moment the screen is opened, so sending it again, by a second press, a retry or a reload, adds no second walk and returns the one already kept.
Rests on: An identity per entry is the known way to make repeat sending safe.
Settles: L.user-action-01.save-request
Under: walker-walk-entry
Criterion: Given a walker whose entry has been sent, when the same entry is sent a second time, then their list shows one walk for it.

## A41: Reloading and stepping back
Kind: chosen
Says: After a save the walker lands on the list. Reloading it only reads it again. Stepping back reaches a fresh entry screen, never the sent entry ready to send again.
Rests on: Redirecting after a save is the known way to stop repeats by reload or back.
Settles: L.user-action-02.walks-list, L.user-action-03.entry-screen
Under: walker-walk-entry
Criterion: Given a walker who has just saved a walk, when they reload the list or step back and reload, then no further walk is added.

## A42: Nothing is left behind on the phone after signing out
Kind: chosen
Says: After sign-out or the end of access, no screen, including one reached by stepping back, shows walks or client names. Pages with them are marked not to be stored. A saved address to any screen leads a signed-out person to sign-in; an address to something that is gone, or not theirs, says only that it is not available.
Rests on: Client details are limited to the business owner and that client's walker; a phone can be passed to someone else.
Settles: L.user-action-04.walks-list, L.user-action-12.walks-list
Under: walker-walk-entry
Criterion: Given a walker who has signed out, when someone steps back or opens a saved address on that phone, then no walk and no client name is shown and sign-in is asked for.

## A43: Unsent entries when the walker leaves
Kind: chosen
Says: A walk is saved only when the walker presses save and it is confirmed. Typing on which save was not pressed is not kept (what happens to a pressed save with no signal follows A3): backing out, leaving or the phone discarding the screen adds nothing, and on return a discarded screen is a fresh, empty entry. The list always shows what was really kept. There are no other steps to back out of.
Rests on: One explicit save is plain to the walker, and keeping no draft leaves nothing to expose.
Settles: L.user-action-05.entry-screen, L.user-action-06.entry-screen, L.user-action-10.entry-screen
Under: walker-walk-entry
Criterion: Given a walker with a half-filled entry, when they back out of the entry screen, then their list shows no new walk.

## A44: Several windows
Kind: chosen
Says: Each window shows a change made elsewhere when it next loads. Entries from two windows are separate entries and both are kept under the same rules; slice 1 changes no walk, so neither can overwrite the other.
Rests on: Adding only means there is no winner to choose.
Settles: L.user-action-07.walks-list
Under: walker-walk-entry

## A45: No undo in this slice
Kind: fact
Says: A walker cannot undo or change a saved walk in slice 1. Until the business owner's correction is built (slice 2), the business owner allows for a mistake when typing invoices by hand.
Rests on: slice-001/004_slice.md, Left for later: "Correction of an entry by the business owner: slice 2. Usable without it: walkers can record walks, and the business owner can allow for a mistake when typing invoices by hand." and "A walker putting right their own entry, and any cut-off for entering walks: no slice yet, waiting on question 3."
Settles: L.user-action-08.walk
Under: walker-walk-entry

## A46: No extra question before saving
Kind: chosen
Says: Saving asks for no second confirmation. The client, day and length are all visible together beside the save button, and after saving the new walk is shown so a mistake is noticed.
Rests on: A question asked on every walk is soon tapped through unread.
Settles: L.user-action-09.entry-screen
Under: walker-walk-entry

## A47: Access ending partway through an entry
Kind: chosen
Says: If access has ended when the walker saves, nothing is kept and they are asked to sign in. After the same walker signs in again on that open screen, what they typed is still there to send. If someone else signs in, it is discarded.
Rests on: Work should survive a sign-in without ever passing to another person.
Settles: L.user-action-11.entry-screen
Under: walker-walk-entry
Criterion: Given a walker with a filled-in entry whose access has ended, when they save, then no walk is added and they are asked to sign in.
Criterion: Given an unsent entry kept for one walker, when a different walker signs in on that phone, then the entry and its client are not shown.

## A48: What a slow, broken or failed save looks like
Kind: chosen
Says: While saving, the screen shows a moving or worded "saving, not yet saved" sign. It ends in one of: saved; refused, with why; or not confirmed, after the wait the owner decides (A31) with no reply, which is also when a save counts as stuck. An interrupted save is not resumed by itself: the walker sends the same entry again, which cannot double it. A failure the walker did not see is recorded for whoever maintains the product; the walker learns of it by the walk's absence from their list.
Rests on: The list read from the store is the one reliable account of what was kept. Resuming by hand is written for A3's first option.
Settles: L.long-operation-01.save-request, L.long-operation-02.save-request, L.long-operation-06.save-request, L.long-operation-07.save-request, L.long-operation-09.save-request
Under: walker-walk-entry
Criterion: Given a walker whose phone loses signal after pressing save, when the signal returns and they send the same entry again, then their list shows exactly one walk for it.

## A49: Whose clock counts
Kind: chosen
Says: The walk's day is the day the walker picks. The product's own clock decides when a walk was recorded, when access ends and what "today" is; the phone's clock only suggests a starting day, which the walker sees and can change. No difference between clocks needs tolerating because the phone's time is never trusted. Waits are measured on a clock that only moves forward, so setting the time back or forward does not change them.
Rests on: A phone's clock can be wrong or changed by its holder.
Settles: L.time-01.walk-day, L.time-02.walk-day, L.time-03.walks-list
Under: walker-walk-entry
Criterion: Given a phone whose clock is a week wrong, when a walker picks 3 November 2026 and saves, then the walk is listed on 3 November 2026.

## A50: The day is a plain date in the business's time zone
Kind: chosen
Says: A walk's day is stored and shown as a calendar date with no time or zone, so it never shifts. "Today" is judged in the business's one time zone, set for the installation, wherever a phone is. Times of recording are stored as one universal time and are never shown as the walk's day.
Rests on: The business works in one place, and a plain date is the known way to stop days shifting.
Settles: L.time-07.walk-day, L.time-08.walk-day
Under: walker-walk-entry
Criterion: Given a saved walk on 3 November 2026, when its list is opened on a phone set to a time zone many hours away, then it still shows 3 November 2026.

## A51: One steady order for the list
Kind: chosen
Says: Walks are ordered by their day, newest first, then by when the product recorded them, newest first, then by the walk's identifier. The order is the same across every part of a long list, and the walker cannot reorder it in this slice. The recorded time only breaks ties.
Rests on: A final unique key gives one order even when times are equal.
Settles: L.time-11.walks-list, L.presentation-11.walks-list, L.presentation-12.walks-list
Under: walker-walk-entry
Criterion: Given a walker with several walks on the same day, when they open the list twice, then the walks are in the same order both times.

## A52: How names are compared, searched and ordered
Kind: chosen
Says: Stored names are kept as written and not changed by this slice. For search and look-alike checks, names are put in one Unicode form, unseen characters are removed, unusual and repeated spaces count as one space, and capitals are ignored by locale-independent rules. Search also ignores accent marks. A list of clients is ordered by the whole stored name, by English rules for every reader, with the identifier as the tie-break. Names are not split to order by a family name.
Rests on: These are the standard rules for matching names; the documents are in English and one fixed order suits a small team.
Settles: L.text-01.client-name, L.text-02.client-name, L.text-03.client-name, L.text-04.client-name, L.text-06.client-name, L.text-07.client-name, L.presentation-10.client-name
Under: walker-walk-entry
Criterion: Given an offered client whose name has an accented letter, when a walker searches for it in lower case without the accent, then that client is offered.

## A53: Long names and look-alike names
Kind: chosen
Says: A client's name is not cut where the walker is choosing or reading a walk: it wraps onto more lines, counted by what a reader sees as characters. Names that match once compared as in A52 get the further label of A36. Names that only look alike through different alphabets are not detected, which is acceptable because walkers cannot add or rename clients.
Rests on: Cutting a name can make two clients look the same.
Settles: L.text-05.client-name, L.text-10.client-name
Under: walker-walk-entry
Criterion: Given two clients whose long names differ only at the end, when a walker sees them in the choice on a narrow phone, then both names are shown in full.

## A54: Room for messages
Kind: chosen
Says: The product is in English only. Labels and messages wrap and are never cut off or placed over a control, so longer or larger text pushes the layout down.
Rests on: The documents are in English and name no other language.
Settles: L.text-12.client-needed-message
Under: walker-walk-entry

## A55: How days and lengths are shown
Kind: chosen
Says: A day is shown with weekday, day number, month name and year, such as "Tue 3 November 2026", in the Gregorian calendar, with Western digits. A length is shown as whole minutes with its unit in words, such as "45 minutes" or "1 minute"; there are no decimals or rounding. A count of walks uses its own wording for none, one and more than one. The date picker starts the week on Monday and marks no rest days. These rules are the same for every reader.
Rests on: A month name cannot be read as another day, and walks are entered in whole minutes.
Settles: L.presentation-01.walks-list, L.presentation-02.stored-walk-length, L.presentation-03.stored-walk-length, L.presentation-04.walks-list, L.presentation-05.stored-walk-length, L.presentation-06.walks-list, L.presentation-08.entry-screen, L.presentation-09.walks-list
Under: walker-walk-entry
Criterion: Given a walk of 45 minutes on 3 November 2026, when a walker sees it in their list, then the day shows the month by name and the length reads "45 minutes".

## A56: How a walker gets in
Kind: owner
Says: To decide: how a walker proves who they are on their phone. It is what they meet every time they come in, and what has to be recovered when lost.
Options: each walker has their own sign-in with a passkey or phone unlock, set up from a one-time link the business owner gives them | each walker has their own sign-in with an email address and password | each walker has a one-time code sent to their phone each time they sign in
Recommended: the first; there is no password to share or forget. It depends on walkers' phones supporting passkeys, which is to be checked once the way to build it is chosen. A code sent by message would also need an outside service the slice does not now have.
If left: walkers cannot be told apart, so no walk can be put down to one.
Harm: high
Settles: L.secrets-02.walker-access
Under: walker-walk-entry

## A57: How credentials are held
Kind: chosen
Says: Whatever way A56 settles, every walker's access is their own and none is shared, so a leak is traced to one account. Only what is needed to check a credential is stored, in a form it cannot be read back from (a slow salted hash for a password, only the public part for a passkey, only a hash for a link or session value). Everything is sent over encrypted connections, session values are held in cookies scripts cannot read, and no credential or session value is written to any record. If one is found in a record it is removed and the access it gives is cancelled.
Rests on: These are the standard ways to hold credentials.
Settles: L.secrets-01.walker-access, L.secrets-03.walker-access, L.secrets-08.walker-access, L.secrets-09.walker-access
Under: walker-walk-entry
Criterion: Given a sign-in and a failed save, when the product's records are read afterwards, then no password, one-time link, session value or other credential appears in them.

## A58: Replacing and cancelling a walker's access
Kind: chosen
Says: Walkers' access is not replaced on a schedule. For a lost phone or an exposed credential, the business owner, or whoever maintains the product for them until the owner has a screen for it, cancels that walker's sessions and credential; the cancellation takes effect on the next request. Only that walker is stopped, until given new access. A refused credential or session leads to sign-in with a message that they need to sign in again or ask the business owner.
Rests on: Replacing on a schedule adds lockouts without a known gain; cancelling at once is what limits a loss.
Settles: L.secrets-04.walker-access, L.secrets-05.walker-access, L.secrets-06.walker-access
Under: walker-walk-entry
Criterion: Given a walker signed in on a phone, when their access is cancelled and the phone next asks for the list or saves a walk, then nothing is shown or added and they are told to sign in again or ask the business owner.

## A59: The product's own credentials
Kind: chosen
Says: Any credential the running product needs, such as for its store, is made per installation, given only the rights the product needs to read and add its own data, with upgrades using a separate one. It reaches the product from the host's protected settings, never from the code, an address, a command line or a record. If it cannot be read the product refuses to start and says which one is missing, never showing its value. A lost one is replaced by making a new one; none is the only way to the data.
Rests on: Least privilege and secrets kept outside the code are standard practice, whatever host is chosen.
Settles: L.secrets-07.installation, L.secrets-10.installation, L.secrets-11.installation
Under: walker-walk-entry
Criterion: Given an installation with a required credential missing, when the product starts, then it does not start, names the missing setting and shows no secret value.

## A60: Which clients a walker is offered
Kind: owner
Says: To decide: which clients count as a walker's own, so which clients a walker is offered and may enter walks for, including when someone covers for another walker. The documents limit addresses and door codes to the business owner and "the walker for that client" but do not say how a walker comes to be that. It also settles how clients get into the product before a walker can pick one.
Options: the business owner sets which walkers each client has, and a walker is offered only those, by name | every walker is offered every client's name, with no address or door code
Recommended: the first; a client's name and walking days stay with the people who walk them, and cover is given by adding the walker to the client.
If left: it cannot be said whose clients a walker sees, and the entry screen cannot be built.
Harm: high
Settles: L.authorization-01.client
Under: walker-walk-entry

## A61: Who may do what with walks
Kind: chosen
Says: In slice 1 a signed-in walker may add a walk under their own name for a client they are allowed (A60) and may read their own walks. Nobody changes or removes a walk through slice 1. No walker sees another's walks. The business owner's correction is slice 2. The product checks this for every operation where the data is read or written. Anything no rule allows is refused, including any address or operation not listed and any request with no sign-in.
Rests on: Deny unless allowed is standard practice, and walks show which clients are walked.
Settles: L.authorization-01.walk, L.authorization-04.installation
Under: walker-walk-entry
Criterion: Given a request with no sign-in, when it asks for walks or clients or tries to add a walk, then it is refused and shows no walk or client.

## A62: Each record is checked against the walker asking
Kind: chosen
Says: Every read of walks is limited to the signed-in walker's own, by the walker the product knows from the session, not by anything the request says. Asking for another's walk is answered as if it did not exist. Every permission is checked by the product itself, so a request sent without the screen meets the same checks.
Rests on: Filtering by the session's walker is the known way to stop one person reading another's records.
Settles: L.authorization-02.walks-list, L.authorization-03.save-request
Under: walker-walk-entry
Criterion: Given two walkers who each have walks, when one asks for the other's walk by its identifier, then it is answered as not found.

## A63: What is taken from the phone
Kind: chosen
Says: Who the walker is and what they may do come only from the session the product holds. The phone sends the client, day, length and the entry's identity, and none of these is trusted without checking. A walker or any other field named in the request that a walker may not set is refused. The session value is random and cannot be guessed or altered into another's.
Rests on: Anything on the phone can be altered.
Settles: L.authorization-10.walker-identity
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request names a different walker, then it is refused and no walk is added under either walker.

## A64: Requests sent by another page, or by a link
Kind: chosen
Says: Only a deliberate save request changes anything; following a link or loading a page never does. A save is accepted only with the product's own origin and its protection against forged requests, and the session cookie is not sent with other sites' requests that change things.
Rests on: These are the standard defences against forged requests.
Settles: L.authorization-06.save-request, L.authorization-07.save-request
Under: walker-walk-entry
Criterion: Given a signed-in walker, when another site's page sends a save in their name, then it is refused and no walk is added.

## A65: A permission check that cannot finish
Kind: chosen
Says: If the product cannot complete the check, the request is refused: nothing is shown or kept, the walker is told to try again, and the failure is recorded.
Rests on: Failing closed is standard practice.
Settles: L.authorization-08.save-request
Under: walker-walk-entry
Criterion: Given a signed-in walker and a permission check that cannot be completed, when they save a walk, then no walk is added and they are told to try again.

## A66: When access is reduced or ends
Kind: chosen
Says: When a walker leaves, the business owner (or the maintainer for them, as in A58) cancels their access; when a walker stops having a client, that client stops being offered to them under the rule A60 settles. Sign-out, cancellation and a change of rights apply from the very next request, including from screens already open. What is already drawn on an open screen cannot be taken back until it next asks for anything or is reopened. Walks already entered stay recorded under the walker who entered them.
Rests on: Checking each request against the current rights is what makes removal take effect.
Settles: L.authorization-05.walker-access, L.authorization-11.walker-access
Under: walker-walk-entry
Criterion: Given a walker signed in on two phones, when they sign out on one, then that phone's next request is refused.

## A67: Ending up in the account that was meant
Kind: chosen
Says: Signing in always starts a new session and ends the one the screen held; a one-time link used while someone else is signed in does not silently switch or merge accounts but signs them out first and says whose access is being set up. Every screen of a signed-in walker shows their name.
Rests on: A new session at each sign-in and a visible name stop walks being entered under the wrong person.
Settles: L.authorization-12.walker-access, L.sign-in-10.walker-access
Under: walker-walk-entry
Criterion: Given a walker signed in, when they open the entry screen or their list, then their own name is shown.

## A68: A record of how access is used
Kind: chosen
Says: Each sign-in, failed sign-in, sign-out, issue and cancellation of access is recorded with the account and time, without any credential. The maintainer looks at it when something is reported or an alert is raised (A80). Use of the product's own credentials is whatever the host records.
Rests on: This is what is needed to trace misuse of an account.
Settles: L.secrets-12.walker-access
Under: walker-walk-entry

## A69: Settings checked at start
Kind: chosen
Says: Every required setting (where the data is, the business's time zone, the product's own address, its credentials, and whether this is a trial) is checked at start for presence and sense: the time zone must be a known one, the address an encrypted one, numbers within stated ranges. A missing or senseless value stops the start with the setting's name, and no secret value is shown.
Rests on: Failing at start is better than failing on a walker's save.
Settles: L.configuration-01.installation, L.configuration-02.installation
Under: walker-walk-entry
Criterion: Given a time zone setting that names no real time zone, when the product starts, then it does not start and names that setting.

## A70: Safe defaults and little switched on
Kind: chosen
Says: Where a default exists it is the safe one: diagnostics off, sign-in required, encrypted connections required. Settings with no safe default, such as the data's location and credentials, have none and must be set. A fresh installation turns on only sign-in, walk entry and the walker's list, with no default account or password and no public sign-up.
Rests on: Safe if nothing is changed is standard practice.
Settles: L.configuration-05.installation, L.configuration-06.installation
Under: walker-walk-entry
Criterion: Given a fresh installation, when someone with no access tries to sign up or sign in with a default account, then there is no way to.

## A71: Trial and real installations
Kind: chosen
Says: The two differ only in their data location, address, credentials and trial mark, each set in that installation's protected settings; anything else that differs is written down with its reason. A trial uses invented data and says on every screen that it is a trial. It cannot be started against the real installation's data.
Rests on: A trial that can touch real data or look real causes lost or false walks.
Settles: L.configuration-03.installation, L.configuration-07.installation
Under: walker-walk-entry
Criterion: Given a trial installation, when a walker opens any screen, then it says it is a trial.

## A72: Seeing, changing and putting back settings
Kind: chosen
Says: Only whoever maintains the product can change settings, through the host's protected settings; nothing a walker or request sends can change one. The maintainer owns every setting. They can see in one place every setting in use and where it came from, with secrets hidden. Each change is noted with who, when, what and why; it is tried on the trial installation first, then applied to the one real installation and checked by saving and reading a test walk by a test account. The previous value is kept, and going back is applying it and restarting.
Rests on: One owner, a record and a trial first are standard for a small installation.
Settles: L.configuration-04.installation, L.configuration-08.installation, L.configuration-09.installation, L.configuration-10.installation, L.configuration-12.installation
Under: walker-walk-entry

## A73: Diagnostic modes
Kind: chosen
Says: The only diagnostic is more detailed records, which still never hold client names or credentials. No debugging screen or detailed error page exists on the real installation, and it refuses to start with one switched on.
Rests on: Debug output is a common way details leak.
Settles: L.configuration-11.installation
Under: walker-walk-entry
Criterion: Given the real installation with a debugging screen switched on in its settings, when it starts, then it does not start and says why.

## A74: What is recorded
Kind: chosen
Says: A record is made of every walk saved, every save refused or failed, refused permissions, access events (A68), starts and stops, storage and integrity faults, and restores. Each says when, what happened, the outcome, which account, and the identifiers of the walk and client concerned, plus the reason for a refusal.
Rests on: This is what settles later disputes about what was entered, by whom and when.
Settles: L.logging-01.walk, L.logging-02.walk
Under: walker-walk-entry
Criterion: Given a walker who saves a walk, when the records are read, then one entry shows the time, the walker's account and the walk's identifier.

## A75: What stays out of records
Kind: chosen
Says: Client names, addresses, door codes, search text and credentials never go into records; identifiers are used instead. Records are built from named fields, not from raw requests. Any outside text that must be recorded is stored as an escaped, length-limited value that cannot start a new entry.
Rests on: Records are read by people the client-details limit does not name.
Settles: L.logging-03.client-name, L.logging-04.walk-client
Under: walker-walk-entry
Criterion: Given a failed save for Example Client A, when the records are read, then the client's name appears nowhere in them.

## A76: What the walker sees of a failure
Kind: chosen
Says: The walker sees plainly that the walk was not saved or not confirmed and what to do next, with a short reference. Technical detail goes only into records under the same reference.
Rests on: Error detail helps an attacker and not a walker.
Settles: L.logging-07.save-request
Under: walker-walk-entry
Criterion: Given a save that fails inside the product, when the walker sees the message, then it shows no technical detail and does say what to do next.

## A77: A record that cannot be written, and full records
Kind: chosen
Says: The record of a saved walk is kept with the walk in the same all-or-nothing write, so a walk is never kept without it. Failing to write other, running records does not stop walkers; the product raises an alert. Running records are capped in size, the oldest rotated out first, with an alert at 80 per cent; the walk records are kept with the data and are not rotated for space.
Rests on: The record of who entered a walk matters as much as the walk, and running logs should not stop the work.
Settles: L.logging-05.installation, L.logging-06.installation
Under: walker-walk-entry

## A78: Records survive the machine, and are protected
Kind: chosen
Says: Walk records are part of the saved data and its spare copies. Running records are also sent to a place separate from the machine that writes them. The product offers no way to edit or remove a record; only the maintainer can reach them, and walk records are chained so a changed or removed one shows in a daily check.
Rests on: Add-only records with a check are the known way to notice tampering.
Settles: L.logging-08.installation, L.logging-10.installation
Under: walker-walk-entry

## A79: Record times
Kind: chosen
Says: Every record's time comes from the product's clock, in universal time, with a running number to order entries made at the same moment. A phone's time is not used.
Rests on: One clock gives one order.
Settles: L.logging-11.installation
Under: walker-walk-entry

## A80: Who reads records and who is told
Kind: chosen
Says: The maintainer reads records. They are alerted to integrity or storage faults, a failed start, a record that cannot be written or was altered, repeated failed sign-ins and the request limits being reached.
Rests on: Unwatched faults go unnoticed until invoicing.
Settles: L.logging-09.installation
Under: walker-walk-entry

## A81: How long records are kept
Kind: owner
Says: To decide: how long walk records, access records and running logs are kept, and what removes them. This is an obligation the business carries about people's information, and no document says what law or contract binds it.
Options: walk records as long as the walk itself, access records 12 months, running logs 30 days, each removed automatically | everything 90 days | everything kept with no end
Recommended: the first, once you have checked what your own legal and tax duties require.
If left: records pile up with no end, or are removed with no agreed rule.
Harm: medium
Settles: L.logging-12.installation
Under: walker-walk-entry

## A82: Keyboard use and focus
Kind: chosen
Says: Everything on the entry screen, including choosing a client and a day and saving, works by keyboard alone using standard controls; every chooser can be left with Escape or by moving on, so focus is never trapped. Focus is always shown by a clearly visible outline. When a chooser or message closes, focus goes back to the control that opened it, or to the next sensible one.
Rests on: Standard accessibility practice (WCAG 2.2 level AA, taken as the working standard and not as a statement of legal duty).
Settles: L.accessibility-01.entry-screen, L.accessibility-02.entry-screen, L.accessibility-03.entry-screen, L.accessibility-04.entry-screen
Under: walker-walk-entry
Criterion: Given a walker using only a keyboard, when they choose a client and a day, type a length and save, then the walk is saved and they were never stuck in a chooser.

## A83: For someone who cannot see the screen
Kind: chosen
Says: Each control has a visible label that is also its announced name, with its purpose and state. Results (saving, saved, refused, not confirmed) are announced without the walker having to look for them, and a refusal moves them to the value at fault. Anything that is not text has words with the same meaning, and colour is never the only signal.
Rests on: Standard accessibility practice (WCAG 2.2 level AA).
Settles: L.accessibility-05.entry-screen, L.accessibility-06.walks-list, L.accessibility-07.entry-screen, L.accessibility-08.client-needed-message
Under: walker-walk-entry
Criterion: Given a walker using a screen reader, when they save with no client, then they hear that a client is needed without searching the screen.

## A84: Contrast, large text and motion
Kind: chosen
Says: In every state and theme, text has at least 4.5 to 1 contrast (3 to 1 for large text and for the outlines of controls and focus). At twice the text size nothing is cut off, overlapped or reachable only by scrolling sideways. Only the saving sign may move, it has words too, and it stays still for a walker who asked for less motion.
Rests on: Standard accessibility practice (WCAG 2.2 level AA).
Settles: L.accessibility-09.entry-screen, L.accessibility-09.walks-list, L.accessibility-10.entry-screen, L.accessibility-10.walks-list, L.accessibility-12.entry-screen
Under: walker-walk-entry
Criterion: Given text enlarged to twice its size on a phone, when a walker uses the entry screen and the list, then all text and controls can be read and used without sideways scrolling.

## A85: No time limit on filling in an entry
Kind: chosen
Says: Filling in an entry has no time limit. If the session has ended by the time of saving, A47 applies. The wait for a reply to a save (A31) is not a limit on the person.
Rests on: Nothing in the slice needs a walker to hurry.
Settles: L.accessibility-11.entry-screen
Under: walker-walk-entry

## A86: Guessing at sign-in
Kind: chosen
Says: Whatever way A56 settles, one-time links and codes are long or short-lived and work once. After 5 failed attempts in 15 minutes for one account or from one address, further attempts are refused for 15 minutes; the message says to wait or ask the business owner. A used or expired link or code is refused.
Rests on: Rate limits and single use are the standard defence against guessing and replay.
Settles: L.sign-in-01.walker-access
Under: walker-walk-entry
Criterion: Given 5 failed sign-in attempts for one account within 15 minutes, when a sixth is made, then it is refused and the person is told to wait 15 minutes or ask the business owner.

## A87: Accounts, first access and recovery
Kind: chosen
Says: No account exists until the business owner asks for one for a named walker; there are no default or shared accounts, and any set-up or test account is removed or disabled before real use. First access is a random one-time link or code that ends after 24 hours or on first use, handed by the business owner to that walker, and a newer one ends the older. Lost access is recovered the same way, after the old access is cancelled, so recovery is no weaker than first access. There is exactly one ordinary way to sign in, the one A56 settles, and no side door.
Rests on: The business owner knows each walker, which makes issuing by them the strong and simple route.
Settles: L.sign-in-02.walker-access, L.sign-in-04.walker-access, L.sign-in-05.walker-access, L.sign-in-06.walker-access
Under: walker-walk-entry
Criterion: Given a one-time link that has been used or is more than 24 hours old, when someone opens it, then it gives no access and says to ask the business owner for a new one.

## A88: Whether an account's existence shows
Kind: chosen
Says: Sign-in and recovery give the same reply whether or not the person has an account.
Rests on: It costs nothing and avoids telling outsiders who walks for the business.
Settles: L.sign-in-03.walker-access
Under: walker-walk-entry
Criterion: Given the sign-in screen, when it is tried for a person with an account and for one without, then the reply is the same.

## A89: Being told about changes to access
Kind: chosen
Says: Slice 1 has no outside way to send messages. A walker is told at their next sign-in when their access was last set up or changed and when a new device was added. Failed attempts that reach the limit alert the maintainer (A80). The business owner is the one who makes changes, so they know of them first.
Rests on: Telling the person in the product needs no outside service.
Settles: L.sign-in-07.walker-access
Under: walker-walk-entry

## A90: Sessions
Kind: chosen
Says: A session ends after 30 days unused and after 90 days in all. An account may have 3 sessions at once; starting a fourth ends the least recently used. Adding a new sign-in or changing how one signs in asks the walker to prove who they are again; entering a walk does not. A walker can see their sessions and end them, and the maintainer can do the same for any account, for the business owner when asked.
Rests on: A walker uses their own phone daily, the data shown is limited to their own clients, and a lost phone is handled by ending its session.
Settles: L.sign-in-08.walker-access, L.sign-in-09.walker-access, L.sign-in-11.walker-access, L.sign-in-12.walker-access
Under: walker-walk-entry
Criterion: Given a session unused for more than 30 days, or begun more than 90 days ago, when it asks for the list, then nothing is shown and sign-in is asked for.
Criterion: Given a walker with 3 sessions, when they sign in a fourth time, then the least recently used one is asked to sign in at its next request.

## A91: What is sensitive and how it is protected
Kind: chosen
Says: Client names, which walker walks which client and on which days, and credentials are sensitive: seen only by those allowed, encrypted on the way and wherever stored, spare copies and running records included. Walk entries also drive billing, so changing them is as serious as seeing them. Addresses and door codes are the most sensitive; slice 1 neither asks for, keeps nor shows them. Only the product and the maintainer can reach the stored data and its copies, and the maintainer's access is by their own named account.
Rests on: The limit on addresses and door codes, and the harm named in security.md for client details and walks.
Settles: L.stored-data-01.walk, L.stored-data-01.client, L.stored-data-02.client
Under: walker-walk-entry
Criterion: Given a signed-in walker, when they use the entry screen and their list, then no address and no door code appears on screen or in any reply sent to the phone.

## A92: Keys
Kind: chosen
Says: Stored data and spare copies are encrypted with keys kept apart from them: one for the live store, another for spare copies, used for nothing else. They are held in protected key storage reached only by the product or the maintainer as needed. A recovery copy of the spare-copy key is kept separately by the maintainer. A lost key makes what only it protects unreadable, so losing the live key means restoring from a copy. An exposed key is replaced and the data encrypted again, and old copies under it are removed once newer ones exist and have been restored once.
Rests on: Separate keys held apart from the data are standard practice.
Settles: L.stored-data-03.installation, L.stored-data-04.installation
Under: walker-walk-entry

## A93: Nothing sensitive in addresses or caches
Kind: chosen
Says: Client names, search text, the chosen client and credentials are never put in a web address, apart from a one-time sign-in link's own token, which works once, is removed from the address as soon as it is used and is kept out of records. Replies with client or walk details are marked so that neither the phone nor anything between stores them.
Rests on: Addresses and stored replies are common places for details to leak.
Settles: L.stored-data-05.walk-client, L.stored-data-06.walks-list
Under: walker-walk-entry
Criterion: Given a walker searching, choosing a client, saving and opening their list, when the addresses and reply headers are inspected, then no client name appears in an address and the replies forbid storing.

## A94: Who else receives data
Kind: chosen
Says: No other party is given data in slice 1: no analytics, advertising, error-reporting or outside content on the pages. Whoever hosts the product holds it in order to run it. Nothing goes to Tallypay in this slice.
Rests on: slice-001/004_slice.md says the slice needs nothing from outside.
Settles: L.stored-data-07.installation
Under: walker-walk-entry
Criterion: Given a walker using the entry screen and the list, when what the phone sends is inspected, then nothing goes anywhere but the product's own address.

## A95: Only what the screen needs
Kind: chosen
Says: The client choice sends only each offered client's identifier, name and any telling-apart label. The list sends only the walker's own walks: identifier, day, length and client name. No address, door code, price or contact detail is sent. The list and client names are not stored on the phone; the session cookie is. Whether unsent entries are stored there follows A3.
Rests on: Sending and storing less leaves less to lose.
Settles: L.stored-data-08.walks-list, L.stored-data-10.walks-list
Under: walker-walk-entry
Criterion: Given a walker allowed one client, when they open the client choice and their list, then the replies sent to the phone hold no other client and no address, door code, price or contact detail.

## A96: How long walks and clients are kept
Kind: owner
Says: To decide: how long walks and client details are kept, including after someone stops being a client, and what removes them. It is an obligation about people's information, and walks will also be the record behind invoices.
Options: walks and clients for 6 years after the walk or after the client leaves, then removed automatically | walks and clients for 2 years, then removed automatically | kept with no end
Recommended: the first as a starting point only; check it against your own tax and data protection duties, which no document states.
If left: nothing is ever removed.
Harm: medium
Settles: L.stored-data-09.walk, L.stored-data-09.client
Under: walker-walk-entry

## A97: A record of reading client details
Kind: chosen
Says: Each time the client choice or a walks list is fetched, a record keeps the account, time and which was fetched, with no names. The maintainer looks at it when something is reported.
Rests on: It lets a complaint about who saw client details be looked into without copying the details.
Settles: L.stored-data-12.client
Under: walker-walk-entry

## A98: The rules of a walk
Kind: chosen
Says: A walk must have the signed-in walker, a client that walker is allowed (A60), a day allowed by the rule A38 settles, a length of 1 to 1440 whole minutes (A33) and its own entry identity. All of them are checked by the product where the walk is kept, and the unchangeable ones by the store too.
Rests on: walker-walk-entry / 1 and 2 give the values; one place of enforcement cannot be bypassed from a phone.
Settles: L.misuse-02.walk
Under: walker-walk-entry

## A99: Repeated and rapid requests
Kind: chosen
Says: Each account may send 30 save requests and 60 list or client-choice requests in 60 seconds, then is refused for 60 seconds and told to wait. Reaching a limit is recorded and alerts the maintainer, but no account is locked or walk removed by itself. A list fetch returns at most 50 walks, so one walker's use cannot grow without bound. Many walks entered quickly can be honest catching up, so speed below the limit is not treated as abuse.
Rests on: These are far above what a person entering walks does and still stop a script from flooding.
Settles: L.misuse-03.save-request, L.misuse-04.save-request, L.misuse-06.walks-list
Under: walker-walk-entry
Criterion: Given an account that has sent 60 list requests in 60 seconds, when it sends another, then it is refused and told to wait 60 seconds, and another walker's list still loads.

## A100: No second person's agreement
Kind: chosen
Says: Entering a walk needs no one else's agreement in slice 1; nothing is billed from it by the product yet, and each walk is recorded against its walker. Whether the business owner checks invoices before clients get them is question 4 of the requirements.
Rests on: An approval for every walk would add back the work the product is meant to remove.
Settles: L.misuse-05.walk
Under: walker-walk-entry

## A101: Fields a walker may not set
Kind: chosen
Says: A save may carry only the client, day, length, the entry's identity and the protection against forged requests. A request carrying any other field, such as a walker, a recorded time or a price, is refused whole.
Rests on: Accepting only listed fields is the known way to stop extra values being set.
Settles: L.misuse-07.save-request
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request also carries a recorded time or any other unlisted field, then it is refused and no walk is added.

## A102: No client given
Kind: fact
Says: An entry with no client, whether empty or absent, is refused: the walker is told a client is needed and no walk is added.
Rests on: walker-walk-entry / 2: "when they try to enter a walk with a day and a length but no client, then they are told a client is needed and their walks show none."
Settles: V.walk-client.empty, V.walk-client.missing
Under: walker-walk-entry

## A103: A client value that is not one the walker may use
Kind: chosen
Says: A client value that is malformed, too long, in odd characters, names no client, names one since removed, or one this walker is not allowed, is refused. The walker is told that client cannot be chosen and to pick from the list again; the reply does not say whether such a client exists.
Rests on: One reply for all of these gives nothing away.
Settles: V.walk-client.malformed, V.walk-client.outside, V.walk-client.long, V.walk-client.dangling, V.walk-client.characters
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save names a client they are not allowed or one that does not exist, then it is refused with the same message for both and no walk is added.

## A104: A client at the edge of being allowed
Kind: chosen
Says: Whether a client is allowed is judged at the moment the walk is saved, not when the screen was opened. If the walker lost the client in between, the save is refused as in A103; if they still have it, it is accepted.
Rests on: The current rights are the ones that protect the client.
Settles: V.walk-client.edge
Under: walker-walk-entry
Criterion: Given an open entry screen whose chosen client the walker has since lost, when they save, then no walk is added and they are told to pick from the list again.

## A105: Day missing or not a real date
Kind: chosen
Says: A day that is empty, absent, malformed or not a real calendar date, such as 30 February, is refused; the walker is told a real day is needed and what they typed stays.
Rests on: A walk without a real day cannot be put in a month.
Settles: V.walk-day.empty, V.walk-day.missing, V.walk-day.malformed
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save gives the day as 30 February 2027, then it is refused, they are told a real day is needed and no walk is added.

## A107: Length missing or not a number
Kind: chosen
Says: A length that is empty, absent, of the wrong type or not whole digits is refused; the walker is told the length is needed as a whole number of minutes from 1 to 1440.
Rests on: A33 and A39 set what is accepted.
Settles: V.walk-length.empty, V.walk-length.missing, V.walk-length.malformed
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save request with no length is sent without using the screen, then it is refused and no walk is added.

## A108: No usable identity
Kind: chosen
Says: A request whose session is empty, absent, malformed, or points to a session or account that no longer exists is treated as signed out: nothing is shown or kept, sign-in is asked for, and the refusal is recorded without the value.
Rests on: Anything short of a valid session is no identity.
Settles: V.walker-identity.empty, V.walker-identity.missing, V.walker-identity.malformed, V.walker-identity.dangling
Under: walker-walk-entry
Criterion: Given a request with a made-up or removed session, when it tries to add a walk, then no walk is added and sign-in is asked for.

## A109: The same identity twice
Kind: chosen
Says: One walker on several devices is the same walker with separate sessions, within the limit of A90. Two accounts can never share an identifier or sign-in: setting up a second one with the same is refused, and walkers with the same name remain separate accounts.
Rests on: The store enforces unique account identifiers.
Settles: V.walker-identity.twice
Under: walker-walk-entry
Criterion: Given two walker accounts with the same display name, when each saves a walk, then each list shows only its own.

## A110: A stored client name that is empty, missing or very long
Kind: chosen
Says: A client with an empty or missing name is a data fault: it is not offered for new walks, a walk already pointing to it is listed as "name unavailable" with its day and length, and the maintainer is told. A very long name is shown in full, wrapped (A53); the store limits a name to 200 characters.
Rests on: A walk must not disappear because a name is faulty, and a blank choice cannot be picked safely.
Settles: V.client-name.empty, V.client-name.missing, V.client-name.long
Under: walker-walk-entry
Criterion: Given a saved walk whose client has lost its name, when the walker opens their list, then the walk is still shown, marked as name unavailable.

## A111: Two clients with one name
Kind: chosen
Says: When two clients' names match, the list and the choice show the further label of A36 for each.
Rests on: The walker has to tell which client a walk is for.
Settles: V.client-name.twice
Under: walker-walk-entry
Criterion: Given walks for two clients with the same name, when the walker opens their list, then they can tell which walk is for which.

## A112: A stored walk whose client is unreadable
Kind: chosen
Says: A stored walk whose client reference is empty, missing, malformed, out of range, too long, oddly encoded or pointing to no client is a data fault: it is kept unchanged, shown to its walker as "client unavailable" with its day and length, never guessed or reassigned, and reported to the maintainer. The edge of what is allowed is a client the walker has since lost: see the answer on lost clients.
Rests on: Hiding or repairing by guess would lose a walk or bill the wrong client.
Settles: V.stored-walk-client.empty, V.stored-walk-client.missing, V.stored-walk-client.malformed, V.stored-walk-client.outside, V.stored-walk-client.long, V.stored-walk-client.dangling, V.stored-walk-client.characters
Under: walker-walk-entry
Criterion: Given a stored walk that points to no client, when its walker opens their list, then it is shown as client unavailable and the other walks are shown normally.

## A113: A past walk for a client the walker no longer has
Kind: owner
Says: To decide: whether a walker still sees, in their list, their past walks for a client they no longer walk, with the client's name. The limit on addresses and door codes does not cover names.
Options: the walk stays listed with its day and length, and the client's name is hidden | the walk stays listed with the client's name | the walk is no longer listed
Recommended: the first; the walker can still account for their work, and a former client's name goes no further.
If left: it cannot be said what the list shows once a client moves to another walker.
Harm: medium
Settles: V.stored-walk-client.edge
Under: walker-walk-entry

## A114: Two walks for one client on one day
Kind: owner
Says: To decide: whether two walks for the same client on the same day are ordinary, or something the walker should be warned about or stopped from entering. This is separate from one entry sent twice, which never makes two walks (A40).
Options: allowed with no warning | allowed after the walker is told one is already recorded and confirms | refused
Recommended: allowed after a warning; it catches the same walk typed twice without stopping a real second walk.
If left: a walk typed twice could be billed twice.
Harm: high
Settles: V.stored-walk-client.twice
Under: walker-walk-entry

## A115: A stored day that cannot be read
Kind: chosen
Says: A stored day that is empty, missing or not a real date is a data fault: the walk is kept unchanged, shown apart at the top of the list as "day unavailable", and reported to the maintainer.
Rests on: A faulty walk must be noticed, not hidden or given a guessed day.
Settles: V.stored-walk-day.empty, V.stored-walk-day.missing, V.stored-walk-day.malformed
Under: walker-walk-entry
Criterion: Given a stored walk with an unreadable day, when its walker opens their list, then it is shown as day unavailable and the other walks are shown normally.

## A116: A real stored day at or past the entry range
Kind: chosen
Says: A walk already kept with a real date is shown with that date, including one on the boundary or outside what may be entered today, for example after the rule has changed. It is not altered or hidden. A day outside what the product can show at all is a data fault as in A115.
Rests on: The entry rule governs new entries; changing or hiding a kept walk would lose a record.
Settles: V.stored-walk-day.edge, V.stored-walk-day.outside
Under: walker-walk-entry

## A117: A stored length that cannot be right
Kind: chosen
Says: A stored length that is empty, missing, not a whole number or outside 1 to 1440 is a data fault: the walk is kept unchanged, listed with "length unavailable", and reported to the maintainer.
Rests on: A guessed length would be billed.
Settles: V.stored-walk-length.empty, V.stored-walk-length.missing, V.stored-walk-length.malformed, V.stored-walk-length.outside
Under: walker-walk-entry
Criterion: Given a stored walk with a length of 0, when its walker opens their list, then it is shown with length unavailable.

## A118: A stored length at the edge
Kind: chosen
Says: Stored lengths of 1 and 1440 minutes are valid and shown as "1 minute" and "1440 minutes".
Rests on: A33 sets the range and A55 the wording.
Settles: V.stored-walk-length.edge
Under: walker-walk-entry
Criterion: Given a stored walk of 1 minute, when its walker opens their list, then the length reads "1 minute".

## A119: Client details stay out of logs, errors and monitoring
Kind: chosen
Says: No client name or client search text reaches logs, an error's own message or trace, or anything sent to monitoring, whether the work succeeds or fails. Errors carry identifiers only, and values from requests and the store are not copied into error text or traces.
Rests on: Logs, traces and monitoring are read by people the client-details limit does not name.
Settles: X.client-details.logs, X.client-details.errors-inside, X.client-details.telemetry
Under: walker-walk-entry
Criterion: Given a save and a list that are each made to fail inside the product for Example Client A, when the logs, error traces and anything sent to monitoring are read, then the client's name appears in none of them.

## A120: Client details in replies and errors shown
Kind: chosen
Says: An error returned to anyone carries no client name or other client detail. A successful reply carries names only of clients the signed-in walker may see (A60, and A113 for past walks), only as A95 lists.
Rests on: The limit on who sees client details; a failure must not show more than success.
Settles: X.client-details.errors-shown, X.client-details.replies
Under: walker-walk-entry
Criterion: Given a signed-in walker, when a save naming a client they are not allowed is refused, then the reply holds no client name.

## A121: No real client in tests or examples
Kind: chosen
Says: Test data and examples kept with the code are invented, such as "Example Client A". No real client, address or door code is copied there or into a trial.
Rests on: Code is copied and shared beyond those who may see client details.
Settles: X.client-details.samples
Under: walker-walk-entry

## A122: Where client details are stored
Kind: chosen
Says: They are stored only in the product's store, its spare copies and, as identifiers only, its records, protected as in A91 and A92. They are not written to temporary exports or files for fault-finding. What, if anything, the phone holds for unsent entries follows A3.
Rests on: Fewer copies are fewer places to protect.
Settles: X.client-details.stored
Under: walker-walk-entry

## A123: An entry being filled in, completed
Kind: fact
Says: When the walker saves an entry with a client, day and length, their list shows that walk with that client, day and length.
Rests on: walker-walk-entry / 1: "when they enter a walk for that client on 3 November 2026 lasting 45 minutes, then their walks show one walk with that client, day and length."
Settles: S.walk.being-entered.walker-walk-entry-1
Under: walker-walk-entry

## A124: An entry being filled in, with no client
Kind: fact
Says: Saving an entry that has a day and length but no client tells the walker a client is needed and adds no walk.
Rests on: walker-walk-entry / 2: "then they are told a client is needed and their walks show none."
Settles: S.walk.being-entered.walker-walk-entry-2
Under: walker-walk-entry

## A125: An entry being filled in, interrupted or left
Kind: chosen
Says: Pressing save again at once adds nothing more (A40). Reloading or reopening before the save was sent gives a fresh empty entry; after it was sent, the list shows whether the walk was kept. Entries open on two devices are separate entries, each kept if it passes the rules, subject to what A114 settles. An entry left for a long time is not kept anywhere else; saving it later runs every check again, including whether the session and the client are still allowed.
Rests on: Nothing exists in the store until a save is accepted.
Settles: S.walk.being-entered.again, S.walk.being-entered.reopened, S.walk.being-entered.second, S.walk.being-entered.time
Under: walker-walk-entry
Criterion: Given a walker with a half-filled entry, when they reload the screen, then the entry is empty and their list shows no new walk.

## A126: With a walk already entered, entering again
Kind: chosen
Says: Entering another walk adds it beside the saved one and changes nothing in it. Another walk for the same client on the same day follows what A114 settles. An attempt with no client is refused as in walker-walk-entry / 2 and the saved walks stay listed.
Rests on: Slice 1 only adds walks.
Settles: S.walk.entered.walker-walk-entry-1, S.walk.entered.walker-walk-entry-2
Under: walker-walk-entry
Criterion: Given a walker with one saved walk, when they try to save an entry with no client, then they are told a client is needed and their list still shows exactly the one walk, unchanged.

## A127: A saved walk over time and across devices
Kind: chosen
Says: Sending the same entry again, or reloading or reopening, leaves one saved walk (A40, A41). It survives a restart of the product. Another device of the same walker shows it when its list is next loaded, and no other walker sees it. Time passing does not change it in slice 1; how long it is kept is what A96 settles.
Rests on: Slice 1 gives no way to change or remove a walk.
Settles: S.walk.entered.again, S.walk.entered.reopened, S.walk.entered.second, S.walk.entered.time
Under: walker-walk-entry
Criterion: Given a walker with a saved walk, when the product is stopped and started again and they open their list, then the walk is there unchanged.

## A128: Corrected walks
Kind: not here
Says: Nothing in slice 1 corrects a walk; the business owner's correction is slice 2, so no walk is in this state.
Settles: S.walk.corrected.*
Under: walker-walk-entry

## A129: Invoiced walks
Kind: not here
Says: Slice 1 makes no invoice; invoices start in slice 3, so no walk is in this state.
Settles: S.walk.invoiced.*
Under: walker-walk-entry

## A130: Walks changed by the walker
Kind: not here
Says: Slice 1 gives a walker no way to change a walk; that waits on question 3 and has no slice, so no walk is in this state.
Settles: S.walk.changed-by-walker.*
Under: walker-walk-entry

## A131: Walks closed to changes
Kind: not here
Says: Nothing in slice 1 closes walks or a month to changes; any cut-off waits on question 3 and has no slice, so no walk is in this state.
Settles: S.walk.closed-to-changes.*
Under: walker-walk-entry

## A132: Removed walks
Kind: not here
Says: Slice 1 has no way to remove a walk, so no walk is in this state. Removal at the end of a keeping time is part of what A96 settles.
Settles: S.walk.removed.*
Under: walker-walk-entry

## A133: How clients get into the product
Kind: owner
Says: To decide: how the clients a walker picks from get into the product, how their names are changed and how one stops being a client, and whether doing that is part of slice 1. A walker cannot enter a walk until the client is there, and neither the slice nor any other slice in the set says who puts them there. Question 8 of the requirements asks what must come across.
Options: for slice 1, whoever maintains the product loads client names and their walkers once from a list the business owner gives; a screen to manage clients is planned separately | the business owner gets a screen to add clients and set their walkers, and it is added to what is built before slice 1 is used
Recommended: the first; it keeps slice 1 thin, with names and walkers only and no addresses or door codes, and the maintainer makes later changes the same way when the business owner asks.
If left: there is no client to pick, and slice 1 cannot be used.
Harm: high
Settles: S.client.being-added.*, C.states.client.being-added, C.states.client.current, C.states.client.details-changed, C.states.client.no-longer-a-client, C.states.dead-end.6, C.states.dead-end.7, C.states.dead-end.8, C.states.dead-end.9
Under: walker-walk-entry

## A134: Entering a walk for a current client
Kind: fact
Says: A walker can enter a walk for a client, with a day and a length, and sees it among their walks.
Rests on: walker-walk-entry / 1: "a client called Example Client A, when they enter a walk for that client on 3 November 2026 lasting 45 minutes, then their walks show one walk with that client, day and length."
Settles: S.client.current.walker-walk-entry-1
Under: walker-walk-entry

## A135: An entry with no client while clients are current
Kind: fact
Says: The walker is told a client is needed and no walk is added; the clients are unaffected.
Rests on: walker-walk-entry / 2: "when they try to enter a walk with a day and a length but no client, then they are told a client is needed and their walks show none."
Settles: S.client.current.walker-walk-entry-2
Under: walker-walk-entry

## A136: A current client otherwise
Kind: chosen
Says: Entering walks never changes a client. Entering for the same client again follows A40 for the same entry and A114 for a new one. Reloading, reopening or a restart leaves the client as it was and offers it again to those allowed. Two walkers allowed the same client may save at once and both walks are kept under their own walker. Time passing alone changes nothing about the client in slice 1.
Rests on: Slice 1 only reads clients.
Settles: S.client.current.again, S.client.current.reopened, S.client.current.restart, S.client.current.second, S.client.current.time
Under: walker-walk-entry
Criterion: Given two walkers allowed the same client, when both save a walk for it at the same moment, then each list shows that walker's walk and not the other's.

## A137: A client whose details have changed
Kind: chosen
Says: Slice 1 has no screen that changes a client, but the stored name may be corrected by whoever loads clients. A walk stays with the same client by its identifier, and lists and choices show the current name the next time they load. An entry open during the change is saved for the client chosen; one with no client is still refused. Repeating, reloading, a restart, a second device or the passing of time causes no further change.
Rests on: The identifier, not the name, says which client is meant (A36).
Settles: S.client.details-changed.*
Under: walker-walk-entry
Criterion: Given a saved walk for a client whose stored name is then changed, when its walker opens their list again, then the same walk shows the new name.

## A138: A walk for someone no longer a client
Kind: owner
Says: To decide: whether a walker may still enter a walk for someone who has stopped being a client, for instance a walk done before they left and not yet entered. If not, that walk has to reach the business owner another way.
Options: no: they are no longer offered, and the walker tells the business owner about any walk not yet entered | yes, for days up to the day they left
Recommended: yes, for days up to the day they left; a walk that was done should be able to be recorded and billed.
If left: it cannot be said whether such a walk is refused.
Harm: medium
Settles: S.client.no-longer-a-client.walker-walk-entry-1
Under: walker-walk-entry

## A139: A former client otherwise
Kind: chosen
Says: An entry with no client is refused as ever. Walks already saved for a former client are kept and are not removed by the client leaving, whether after repeating, reloading, a restart, an action from a second device or the passing of time; what a walker sees of them follows A113, and how long they are kept follows A96. Whether a new walk is accepted is what A138 settles, judged when it is saved.
Rests on: Walks done are the record behind billing.
Settles: S.client.no-longer-a-client.walker-walk-entry-2, S.client.no-longer-a-client.again, S.client.no-longer-a-client.reopened, S.client.no-longer-a-client.restart, S.client.no-longer-a-client.second, S.client.no-longer-a-client.time
Under: walker-walk-entry

## A140: Pages are only ever the product's own
Kind: chosen
Says: Data replies are sent with their true type and a header forbidding the browser to guess another, and the slice accepts no files. A content policy lets the page load and run code and styles only from the product's own address, with no inline script, and blocks everything else. No other site may frame it. No code or styles come from another party's address; components are shipped with the product. The page takes no messages from other windows.
Rests on: These are the standard browser protections.
Settles: F.browser.context, F.browser.page-policy, F.browser.framing, F.browser.type-guessing, F.browser.others-code, F.browser.messages
Under: walker-walk-entry
Criterion: Given another site that puts the product inside a frame, when its page is opened, then the product is not shown in it.

## A141: What leaves the browser or stays in it
Kind: chosen
Says: Other sites are told nothing of the address a person came from. No other site's page may call the product and read replies. The product never sends a person on to an address someone else supplied. Pages with client details are marked not to be stored. A walker is known only by a session cookie sent over encrypted connections, unreadable by scripts, tied to the product's own host and not sent with other sites' requests that change things.
Rests on: These are the standard settings for a signed-in site.
Settles: F.browser.came-from, F.browser.other-sites, F.browser.sent-on, F.browser.kept-by-browser, F.browser.known-by
Under: walker-walk-entry
Criterion: Given a sign-in address that carries another site's address to go on to, when a walker signs in through it, then they are not sent to that site.

## A142: What the network can reach
Kind: chosen
Says: The product answers only to its own configured host name and refuses others. All connections are encrypted; an unencrypted one is redirected before anything is served and the browser is told to use only encryption, and a save sent unencrypted is refused. A sender's address or host is believed only from the known component in front of the product, never from what the sender supplies. Each address accepts only its own kinds of request and refuses others. No diagnostic page, file listing, source history, documentation or measurement page or test code is reachable, and refusals do not name what the product is built from.
Rests on: These are the standard network protections.
Settles: F.network.answers-to, F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, F.network.gives-away
Under: walker-walk-entry
Criterion: Given the real installation, when an unlisted address, a request naming another host or a wrong kind of request is tried, then it is refused with no listing, technical detail or name of what the product is built from.

## A143: Components the product is built from
Kind: chosen
Says: The exact version of every component, including those they bring, is locked in a list with its source and content check, and is fetched only from the named source. An automated check for known flaws runs on every change and daily and alerts the maintainer; a serious flaw that applies is fixed within 7 days and others within 30. Few components are used, those that see credentials, read outside data or run at install are listed and reviewed, install scripts are off unless needed, and the running product has only the rights it needs.
Rests on: Standard practice for third-party code.
Settles: F.dependency.known-flaw, F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
Under: walker-walk-entry

## A144: Fields and groups
Kind: chosen
Says: A walker sets only the client, day, length and entry identity, and sees of a record only what A95 lists; other fields, such as who recorded it and when, are not theirs to set. The product serves one business, so there is no other group whose data could be shown.
Rests on: 000_problem.md describes one business with four walkers.
Settles: F.several-people.fields, F.several-people.groups
Under: walker-walk-entry

## A145: Values that must not be guessable
Kind: chosen
Says: One-time links and codes, session values and protection against forged requests are made by the system's secure random generator with at least 128 bits; a code a person types may be shorter only with the single use, short life and attempt limits of A86 and A87. Identifiers of walks and clients are random too, but nothing relies on that: every access is checked.
Rests on: Secure randomness is the standard solution.
Settles: F.unguessable.made
Under: walker-walk-entry

## A146: Against reading other walkers' clients
Kind: chosen
Says: The list and the client choice are limited by the session's walker (A60, A62), and carry only what A95 lists. Sessions end and can be cancelled (A58, A90). Someone trying shows as refused permissions, failed sign-ins and limits reached in the records, and repeated ones alert the maintainer. Use of a stolen but valid session looks like the walker; it shows only in the record of fetches and sign-ins.
Rests on: security.md, client-details through walks-list, entry-screen and walker-access.
Settles: T.client-details.walks-list, T.client-details.entry-screen, T.client-details.walker-access
Under: walker-walk-entry
Criterion: Given a signed-in walker, when they try to fetch a client or list that is not theirs, then nothing of it is shown and the records hold the refused attempt without any client name.

## A147: Against reading or altering an entry on its way
Kind: chosen
Says: Encryption on every connection (A142) stops reading and altering on the way; the browser refuses an unencrypted or wrongly identified connection to the product once told to use only encryption. An attempt on the path may not be visible to the product; refused connections show in the host's records where it keeps them.
Rests on: security.md, client-details through save-request; encrypted connections are the known solution.
Settles: T.client-details.save-request
Under: walker-walk-entry
Criterion: Given the real installation, when the product is asked for or sent anything without encryption, then no client detail is returned and no walk is added.

## A148: Against reaching the data
Kind: chosen
Says: The data, copies and records are encrypted, reachable only by the product and the maintainer through named accounts with a second factor, with least rights (A59, A91, A92). Client names stay out of records. Changes and removals of walks show against the chained walk records and daily check (A78), and lost data is restored from spare copies as far as A13 allows. Access to the host is recorded where the host does so, and integrity faults alert the maintainer. Someone with the maintainer's full access could defeat these checks.
Rests on: security.md, client-details and walk through installation.
Settles: T.client-details.installation, T.walk.installation
Under: walker-walk-entry
Criterion: Given a saved walk altered directly in the store of a test installation, when the daily check runs, then the maintainer is alerted to it.

## A149: Against false or repeated walks sent to the product
Kind: chosen
Says: Only a signed-in walker can add walks, only for allowed clients, under their own name, with forged requests refused, one walk per entry and a rate limit (A40, A62, A64, A99). Each walk is recorded with account and time, so odd ones can be traced; the walker sees them in their list. A walker can still deliberately enter a walk that never happened, which the product cannot tell apart; until invoicing is built the business owner bills by hand.
Rests on: security.md, walk through save-request.
Settles: T.walk.save-request
Under: walker-walk-entry

## A150: Against entering as another walker
Kind: chosen
Says: The walker of a walk comes only from the session (A63), access is individual and never shared (A57), guessing is limited (A86), and a walker is told of new sign-ins and devices (A89) and can end sessions. The record keeps account, time and session for each walk, which shows which access was used, not whose hand used it.
Rests on: security.md, walk through walker-access.
Settles: T.walk.walker-access
Under: walker-walk-entry

## A151: A walker's unlocked phone in other hands
Kind: owner
Says: To decide, as a risk to accept or not: someone holding a walker's unlocked phone with the product signed in can see that walker's clients and enter false walks. The phone's own lock, ending sessions (A58) and the walker seeing their list limit it; the record cannot tell whose hand it was.
Options: accept it, relying on the phone's lock and cancelling access when a phone is lost | require the phone's unlock or a sign-in again before each time the product is opened
Recommended: accept it; asking each time slows every entry, and walks can be checked before billing.
If left: the risk stands, and nobody has accepted it.
Harm: medium
Settles: T.walk.entry-screen
Under: walker-walk-entry

## A152: If walk entry is unavailable for an hour
Kind: chosen
Says: Walkers cannot save walks or see their lists, and are told so when the product can still answer. They note walks and enter them afterwards for the day they happened, subject to the days A38 allows. Nothing already confirmed is lost by the outage itself.
Rests on: The day of a walk is separate from when it is entered (A49).
Settles: W.unavailable
Under: walker-walk-entry

## A153: How often it may fail and how slow is too slow
Kind: owner
Says: To decide: how often walk entry may be unavailable and when it is too slow. The size to handle is asked in A9 and the wait on a save in A31.
Options: unavailable for no more than 4 hours in a month, with saves and lists usually within 3 seconds on a working signal | unavailable for no more than 24 hours in a month, same speed | a stricter promise of under 1 hour a month
Recommended: the first; walkers can note a walk and enter it later, and a stricter promise costs more to run.
If left: there is no point at which anyone would say it does not work.
Harm: low
Settles: W.target
Under: walker-walk-entry

## A154: Noticing that it is broken
Kind: chosen
Says: A check from outside the machine tries the product every 5 minutes and tells the maintainer after 2 failures in a row. The alerts of A80 also reach them. Walkers can tell the business owner.
Rests on: A fault should not wait for invoicing day to be found.
Settles: W.noticed
Under: walker-walk-entry
Criterion: Given a stopped test installation, when 2 checks 5 minutes apart have failed, then the maintainer is told.

## A155: What is sensitive here and who sees it
Kind: chosen
Says: The slice touches client names, which walker walks whom and on which days, walkers' credentials and the walks that will drive bills. Four walkers use it; none may see or change what is another's. What the business owner sees in the product starts with slice 2.
Rests on: security.md names client-details and walk as what someone would want; 002_requirements.md limits addresses and door codes to the business owner and the walker for that client.
Settles: W.sensitive, W.who-sees
Under: walker-walk-entry

## A156: What law or contract binds it
Kind: owner
Says: To decide, or to find out: which law or contract binds how client and walker information is handled. The documents name only the business's limit on addresses and door codes and a Tallypay contract, which nothing in this slice uses. No data protection, accessibility or record-keeping duty is stated.
Options: you or an adviser confirm which duties apply before real client details are put in | go ahead on the protections chosen here and accept that a duty may be missed
Recommended: the first; the answers here are good practice and not a statement that any law is met.
If left: it is unknown whether the product meets what binds the business.
Harm: high
Settles: W.obligations
Under: walker-walk-entry

## A157: What someone meaning harm would want
Kind: chosen
Says: Client details, to learn who is walked and when, and the walks, to add false ones, repeat them, blame another walker, or change and destroy them. Each way in that security.md lists is answered above.
Rests on: security.md, What someone who means harm would want.
Settles: W.prize
Under: walker-walk-entry

## A158: Between entering a walk and seeing it
Kind: chosen
Says: Before saving, a walk is only what is typed on the screen. After pressing save it is shown as saving and not yet saved, and it ends as saved and listed, refused with why, or not confirmed (A48). Leaving the screen is always a way out.
Rests on: A1, A43 and A48 together leave no state in which a walker cannot tell what to do.
Settles: C.states.walk.being-entered, C.states.dead-end.1
Under: walker-walk-entry

## A159: What happens to corrected and invoiced walks
Kind: not here
Says: Slice 1 neither corrects nor invoices a walk; correction is slice 2 and invoicing is slice 3, where what can happen to such walks is settled.
Settles: C.states.walk.corrected, C.states.walk.invoiced, C.states.dead-end.2
Under: walker-walk-entry

## A160: Changing, closing and removing walks
Kind: owner
Says: To decide what is in or out: whether a walker can put right or remove a walk they entered, for example one entered by mistake, and until when walks for a month can be entered or changed. This is question 3 of the requirements; the slice leaves a walker's own correction and any cut-off for later.
Options: keep all of it out of slice 1, and the business owner allows for mistakes when typing invoices by hand | add a walker's own correction or removal to what is built before slice 1 is used
Recommended: the first, as the slice already stands; when to close a month can be decided before invoicing.
If left: slice 1 is built with no way for a walker to put right a mistake.
Harm: medium
Settles: C.states.walk.changed-by-walker, C.states.walk.closed-to-changes, C.states.walk.removed, C.states.dead-end.3, C.states.dead-end.4, C.states.dead-end.5
Under: walker-walk-entry
