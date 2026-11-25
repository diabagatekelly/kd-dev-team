# Answers: slice 1

## A1: Carrying across an untouched list
Kind: fact
Says: The list keeper is shown the people in the notebook's order, each once, and nobody else.
Rests on: notebook-order-kept / 1
Settles: S.waiting-list.not-carried-across.notebook-order-kept-1
Under: notebook-order-kept

## A2: Nothing is the list until the whole of it is confirmed
Kind: chosen
Says: The names are entered as an unfinished draft. The keeper sees the whole draft in order and confirms it once. Confirming keeps every entry in its order or none of them. A draft is never shown as the waiting list. Nothing else is saved bit by bit as the list, so there is no partly carried list.
Rests on: One all-or-nothing step means a cut, crash or late failure cannot leave some people on the list and others missing, or a changed order.
Settles: L.sync-08.carry-across, L.durable-write-01.waiting-list, L.durable-write-06.waiting-list, L.durable-write-08.waiting-list, L.concurrency-03.list-view, L.concurrency-05.list-view, L.lifecycle-01.carry-across, L.lifecycle-05.waiting-list, L.long-operation-04.carry-across, L.long-operation-08.carry-across, C.states.waiting-list.being-carried-across, C.states.dead-end.1
Under: notebook-order-kept
Criterion: Given a draft of three entries has not been confirmed, when the keeper opens the list view, then they are told nothing has been carried across and are offered the unfinished draft, which is marked as unfinished.
Criterion: Given a draft of three entries, when the product is stopped while the confirmation is being saved and then started again, then the keeper finds either all three in their order as the list, or no list and the draft of three.

## A3: The draft survives leaving
Kind: chosen
Says: Each entry is saved to the draft as it is finished, and the screen says whether it is saved. At most the entry being typed is lost on leaving, reloading, a discarded screen, an ended session or a restart. The draft is kept until the keeper confirms or discards it. Nothing removes it on a timer, and the product never confirms it on its own. On return the keeper can carry on or discard it, and is told it is not yet the list.
Rests on: A volunteer typing from a notebook may stop partway, and typing about 40 people again invites mistakes. The draft is protected as the list is.
Settles: L.startup-read-04.carry-across, L.durable-write-12.carry-across, L.lifecycle-08.carry-across, L.user-action-05.carry-across, L.user-action-06.carry-across, L.user-action-10.carry-across, L.user-action-11.carry-across, L.long-operation-03.carry-across, L.long-operation-05.carry-across, L.long-operation-06.carry-across, S.waiting-list.being-carried-across.reopened, S.waiting-list.being-carried-across.restart, S.waiting-list.being-carried-across.time, S.waiting-list.being-carried-across.notebook-order-kept-1
Under: new: unfinished-draft
Criterion: Given a draft with two finished entries and a third half typed, when the keeper closes the product and opens it again, then the two finished entries are there in order, marked as an unfinished draft.
Criterion: Given the keeper's session ends during a draft, when they sign in again, then every entry shown as saved is still there.
Criterion: Given an unfinished draft, when the keeper chooses to discard it and confirms that, then no draft and no list is shown.

## A4: Doing the same thing twice
Kind: chosen
Says: As soon as confirm is used, the screen says it is saving and a second use does nothing more. A repeated or simultaneous confirmation makes one list only. Entering names while a draft exists continues that one draft; no second draft is started. A change made from an out-of-date window is refused, and that window is told to reload. It is not repeated automatically.
Rests on: One draft and one list prevent doubled people and silent overwriting.
Settles: L.user-action-01.carry-across, L.user-action-07.list-view, L.concurrency-01.carry-across, L.concurrency-04.carry-across, L.concurrency-09.carry-across, L.long-operation-11.carry-across, S.waiting-list.not-carried-across.again, S.waiting-list.being-carried-across.again
Under: new: one-list
Criterion: Given a complete draft, when confirm is used twice in quick succession, then one list is shown with each entry once.
Criterion: Given the same draft is open in two windows and it has been changed in one, when the other tries to save an older version, then it is refused, told to reload, and the newer draft is unchanged.

## A5: Once carried across, it cannot be replaced by carrying across
Kind: chosen
Says: When a list exists, any further carry across is refused, whether it comes from the screen, an old window or a direct request. The keeper is told a list is already there, can look at it, and that changing it is not offered. This holds whatever is later decided about correcting it.
Rests on: A different or old list sent again must not replace the true order.
Settles: L.misuse-01.carry-across, S.waiting-list.carried-across.notebook-order-kept-1, S.waiting-list.carried-across.again, S.waiting-list.out-of-date.notebook-order-kept-1, S.waiting-list.out-of-date.again, S.waiting-list.wrong.notebook-order-kept-1, S.waiting-list.wrong.again
Under: notebook-order-kept
Criterion: Given a list has been carried across, when a different list is sent to be carried across, even by a direct request, then it is refused with word that a list already exists and can be looked at but not changed here, and the list shown is unchanged.

## A6: The kept list stays as it was
Kind: chosen
Says: After confirmation the list stays the same, in the same order, through reloads, stepping back, restarts and the passing of time, until some later feature changes it. Stepping back after confirming never offers to confirm again. The list view says when it was carried across and that it has not been updated since. Before that it says nothing has been carried across. Other windows show the list the next time they are loaded; an old window cannot change it.
Rests on: The list has no source that updates it in this slice, so its date is what tells the keeper how old it is.
Settles: L.sync-04.list-view, L.user-action-02.list-view, L.user-action-03.list-view, L.concurrency-06.list-view, L.long-operation-10.waiting-list, S.waiting-list.carried-across.reopened, S.waiting-list.carried-across.restart, S.waiting-list.carried-across.time, S.waiting-list.out-of-date.reopened, S.waiting-list.out-of-date.restart, S.waiting-list.out-of-date.time, S.waiting-list.wrong.reopened, S.waiting-list.wrong.restart, S.waiting-list.wrong.time
Under: notebook-order-kept
Criterion: Given a carried-across list, when the product is restarted and the keeper looks at it, then it shows the same entries in the same order, with the date it was carried across.
Criterion: Given the keeper has just confirmed, when they step back or reload, then there is still one list and no way offered to confirm it again.

## A7: Nothing carried across stays that way
Kind: chosen
Says: With no list and no draft, restarts, reloads and time change nothing. The keeper is told nothing has been carried across and can start.
Rests on: Only the keeper's own action should create a list.
Settles: S.waiting-list.not-carried-across.reopened, S.waiting-list.not-carried-across.restart, S.waiting-list.not-carried-across.time
Under: new: first-run
Criterion: Given nothing has ever been entered, when the keeper opens the list view, then they are told nothing has been carried across and are offered to start.

## A8: A failed confirmation
Kind: chosen
Says: If saving fails, including for lack of space or because storage reports an error, the keeper is told the list was not carried across. The product does not simply try again and report success. It reads back what is kept before saying the list is saved. The draft already saved stays. The keeper can try again themselves; if every try fails, nothing is the list, the draft remains and the notebook is still the list in use. They are told to get help from whoever runs the product. The failure is recorded without names. Reloads, restarts and time leave this as it is.
Rests on: A success message that is wrong would make the keeper trust a list that is not kept.
Settles: L.durable-write-04.carry-across, L.durable-write-05.carry-across, L.long-operation-07.carry-across, S.waiting-list.carry-across-failed.*, C.states.waiting-list.carry-across-failed, C.states.dead-end.2
Under: new: failed-save
Criterion: Given a complete draft and no space left to save, when the keeper confirms, then they are told it was not carried across and what to do, no list is shown, and the draft keeps every entry it had saved.
Criterion: Given a confirmation failed and the cause has been put right, when the keeper confirms again, then the whole list is shown once in its order.

## A9: When the product says saved
Kind: chosen
Says: The product says the list is carried across only after storage reports it durably kept and it has been read back. No confirmed list may be lost afterwards. A confirmation with no result after 30 seconds is shown as not known to be saved: the keeper is told to reload, which shows the list or the draft. While waiting, the screen shows that it is saving and for how long at most. The same 30 seconds applies when the stored data is in use. Nothing is retried without the keeper.
Rests on: With about 40 people a save should take seconds; a fixed limit tells a stopped save from a working one.
Settles: L.durable-write-02.carry-across, L.concurrency-08.carry-across, L.lifecycle-04.carry-across, L.long-operation-01.carry-across, L.long-operation-02.carry-across, L.long-operation-09.carry-across
Under: new: saved-means-saved
Criterion: Given a confirmation that gets no answer, when 30 seconds pass, then the keeper is told it is not known to be saved and to reload, and reloading shows either the whole list or the draft.

## A10: Refusing early
Kind: chosen
Says: Before entry starts the product checks that the person is the keeper, that no list exists and that it can save. Before confirming it checks every entry again. The only step that cannot be taken back in this slice is confirming, and all checks come before it.
Rests on: Nobody should type the whole notebook only to be refused at the end for something knowable at the start.
Settles: L.lifecycle-03.carry-across, L.long-operation-12.carry-across
Under: new: checked-first
Criterion: Given the product cannot save anything, when the keeper chooses to start carrying across, then they are told so before they are asked for any name.

## A11: No separate undo of a failed attempt
Kind: not here
Says: A failed confirmation keeps nothing as the list, so there is no completed step to undo and no undoing that can fail. Damaged stored data is covered with damage.
Rests on: The all-or-nothing confirmation.
Settles: L.lifecycle-02.waiting-list
Under: notebook-order-kept

## A12: The confirmation question
Kind: chosen
Says: Only confirming and discarding a draft ask for confirmation. Confirming shows the number of people and the whole list in order, asks the keeper to check it against the notebook, and says it cannot be changed here afterwards. Each entry can be edited, moved, added or removed while it is a draft.
Rests on: The question carries the actual list and what follows, so there is something to check rather than a yes to click through.
Settles: L.user-action-09.carry-across
Under: notebook-order-kept
Criterion: Given a draft with an entry in the wrong place, when the keeper moves it and then asks to confirm, then they are shown the number of people and the corrected order, with word that it cannot be changed here afterwards, before anything becomes the list.

## A13: Correcting the list after it is confirmed
Kind: owner
Says: To decide: what the keeper can do about a mistake found after confirming, and about the list going out of date. No slice includes changing it, so it can stay wrong or fall behind the notebook.
Rests on: What is in or out. 003_slices.md says slices 1 to 3 do not include changing or correcting the list.
Options: Let the keeper discard the whole list and carry it across again | Add correcting and keeping up to date to the slices before real names go in | Leave it unchangeable and treat the notebook as the real list for now
Recommended: Leave it unchangeable and treat the notebook as the real list for now, while only the keeper sees it; settle correcting before anyone else is shown a place.
If left: The list cannot be changed once confirmed, so the notebook stays the list to go by.
Harm: high
Settles: L.user-action-08.carry-across, C.states.dead-end.3, C.states.dead-end.4, C.states.dead-end.5, C.states.waiting-list.out-of-date, C.states.waiting-list.wrong
Under: notebook-order-kept

## A14: The list never ends in this slice
Kind: not here
Says: Nothing in this slice ends or removes a confirmed list, so no event arises in an ended list and there is no way out to give it.
Rests on: The slice removes no thing; its only action carries the list across.
Settles: S.waiting-list.ended.*, C.states.waiting-list.ended, C.states.dead-end.6
Under: notebook-order-kept

## A15: What in the notebook counts as a person waiting
Kind: owner
Says: To decide: what is carried across when a notebook line is crossed out, has a note beside it, names two people, or has a name that is incomplete or unreadable.
Rests on: A rule of the waiting list that the documents do not give.
Options: Carry only lines still waiting, as the keeper reads them, one entry a line, writing an incomplete name as it stands | Settle each unclear line with the committee before carrying it | Carry every line and mark the unclear ones
Recommended: Settle each unclear line with the committee before carrying it, because a line left out or split changes who is first.
If left: The keeper judges each line alone as they enter it.
Harm: high
Settles: L.user-input-02.person-name
Under: notebook-order-kept

## A16: A name is one free line
Kind: chosen
Says: Each person is one name field, entered whole as written, with one part or several in any order. Letters of any language, accents, digits and punctuation are accepted. Line breaks and invisible control characters are removed, and runs of unusual or repeated spaces become one ordinary space. Spaces at each end are removed. Invisible joining marks that some writing needs are kept. A blank name is refused. The limit is 200 characters as a reader counts them; a longer one is refused and never cut. The cleaned form is what is stored and shown before confirming.
Rests on: Names vary widely; splitting or rejecting characters would alter what the notebook says.
Settles: L.user-input-01.person-name, L.user-input-03.person-name, L.user-input-04.person-name, L.user-input-07.person-name, L.text-03.person-name, L.text-05.person-name, L.limits-07.carry-across
Under: new: names-as-written
Criterion: Given a draft, when a name of one word with an accent and an apostrophe, with spaces at each end, is entered, then it is saved with the accent and apostrophe and without the end spaces.
Criterion: Given a draft, when a name of only spaces is entered, then it is refused beside the field and no entry is added.
Criterion: Given a draft, when a name of 201 characters is entered, then it is refused with the limit of 200 stated, the typed text stays, and nothing shortened is saved.

## A17: Two people with the same name
Kind: chosen
Says: Names need not be unique; each notebook line entered is its own entry with its own place. When a name matches another after cleaning, ignoring capital letters by language-neutral rules, the keeper is warned, shown both places, and says whether it is two people or one entered twice. Names are stored as typed. Look-alike names are not merged; the keeper tells them apart by place and spelling.
Rests on: "Each once" means one entry for each person, and different people may share a name.
Settles: L.user-input-09.person-name, L.text-01.person-name, L.text-02.person-name, L.text-10.list-view, V.notebook-order.twice
Under: notebook-order-kept
Criterion: Given a draft containing "Ash Sample" (invented), when "ash sample" is entered, then the keeper is warned with the other entry's place and can keep both as two people or drop the new one.

## A18: Names are only ever text
Kind: chosen
Says: A name is shown, stored and passed on only as text, never run or read as markup or a command. In a row it is isolated so that writing in the opposite direction cannot move the place number or neighbouring words. Anything meant as data is never served as a page.
Rests on: The standard protection against injected text.
Settles: L.user-input-10.person-name, L.text-09.person-name, F.browser.context, F.browser.type-guessing
Under: new: text-only
Criterion: Given an entry typed as <b>Moss</b> (invented), when the list is shown, then those characters appear as typed and nothing turns bold.
Criterion: Given an entry in right-to-left writing, when the list is shown, then its place number stays in the same position as on other rows.

## A19: Rules are checked where the list is kept
Kind: chosen
Says: Every rule on names, number of entries and when carrying across is allowed is enforced by the part that keeps the list; any on-screen check is only a help. A request may set only the names, their order and the draft actions. Who did it, the dates and whether the list is confirmed are set by the product; any other field is refused. A refusal says which entry and what to change, beside that entry and in a summary that can be reached by keyboard.
Rests on: A request can bypass the screen.
Settles: L.user-input-05.carry-across, L.user-input-06.carry-across, L.misuse-02.carry-across, L.misuse-07.carry-across
Under: new: checked-where-kept
Criterion: Given a direct request carrying a blank name, when it is sent, then it is refused and the draft is unchanged.
Criterion: Given a direct request that also tries to set the carried-across date, when it is sent, then it is refused and nothing changes.

## A20: The most entries accepted
Kind: chosen
Says: A list holds at most 500 people. The 501st is refused, with word that the limit is 500 and to ask whoever runs the product; saved entries stay. No part of a longer list is quietly dropped.
Rests on: The problem document says about 40 people are waiting, so 500 leaves ample room while bounding the size.
Settles: L.limits-04.waiting-list, L.limits-06.carry-across, V.notebook-order.long
Under: new: bounded-list
Criterion: Given a draft of 500 entries, when another is added, then it is refused with the limit and what to do, and the 500 stay in order.

## A21: Empty, missing or broken order
Kind: chosen
Says: An empty list cannot be confirmed. A request with no order, or one that is not an ordered list of names, is refused as a whole and changes nothing. The keeper is told in plain words to add a name or reload.
Rests on: A broken request must not become the waiting list.
Settles: V.notebook-order.empty, V.notebook-order.missing, V.notebook-order.malformed
Under: new: checked-where-kept
Criterion: Given a draft with no entries, when the keeper tries to confirm, then it is refused with word to add at least one person, and no list is made.
Criterion: Given a saved draft, when a malformed order is sent, then it is refused and the draft is unchanged.

## A22: The whole list in one view
Kind: chosen
Says: The list view shows every entry on one scrolling page, each numbered with its place, so the order holds from first to last.
Rests on: With at most 500 short rows no paging is needed, and numbers help checking against the notebook.
Settles: L.limits-08.list-view, L.presentation-12.list-view
Under: notebook-order-kept
Criterion: Given a list longer than one screen, when the keeper scrolls from top to bottom, then every entry appears once, in the notebook's order, numbered from 1 without gaps.

## A23: Only the list keeper
Kind: chosen
Says: Only the signed-in list keeper may enter, discard, confirm or look at the draft or list. Everyone else, signed in or not, is refused everything, and so is anything no rule mentions. The check is made where the data is kept, on every request, from the product's own record of the session and role, never from what the device claims. If the check cannot be completed the request is refused. Committee members and people waiting get no access in this slice. There is one list, and no one else's records or groups to separate; the keeper may see every field.
Rests on: Least access. The requirements say names are not to be shown to everyone; viewing by others belongs to later slices.
Settles: L.authorization-01.*, L.authorization-02.waiting-list, L.authorization-03.list-view, L.authorization-04.waiting-list, L.authorization-08.list-view, L.authorization-10.list-view, F.several-people.fields, F.several-people.groups, W.who-sees, T.waiting-details.list-view
Under: new: keeper-only
Criterion: Given a carried-across list, when someone not signed in asks for it directly, then they are refused and the reply holds no name, place or number of people.
Criterion: Given a signed-in account that is not the list keeper, when it asks to see or carry across the list, then it is refused and nothing changes.
Criterion: Given the permission check cannot be completed, when the list is asked for, then it is refused and no name is sent.
Criterion: Given a refused request for the list, when the record of events is read, then it shows the refused try and its time, with no name from the list.

## A24: Requests made in the keeper's name
Kind: chosen
Says: Only a deliberate action in the product changes anything. Following a link or loading a page changes nothing. A change must carry proof that it came from the product's own page in the keeper's session. Other sites cannot call the product or read its replies, frame it or send it messages; it takes no messages from other windows.
Rests on: Standard protection against forged and framed requests.
Settles: L.authorization-06.carry-across, L.authorization-07.carry-across, F.browser.framing, F.browser.messages, F.browser.other-sites
Under: new: no-forged-requests
Criterion: Given the keeper is signed in, when another site's page sends a request to confirm or discard, then it is refused and nothing changes.
Criterion: Given a draft, when any address of the product is opened from a link, then nothing is changed.
Criterion: Given another site, when its page tries to show the product inside itself, then the product does not appear there.

## A25: What the page loads and where it sends
Kind: chosen
Says: The page loads code and styles only from the product itself and the browser blocks the rest. No other party's code, analytics or fonts are on it. It never sends a person to an address someone else supplied. It tells other sites nothing about the address a person came from. No name or other sensitive value is ever in an address.
Rests on: Nothing in the slice needs another party, so none gets a way to the names.
Settles: F.browser.page-policy, F.browser.others-code, F.browser.sent-on, F.browser.came-from, L.stored-data-05.person-name
Under: new: nothing-from-others
Criterion: Given the keeper uses every screen, when the addresses and the places the page contacts are inspected, then no address holds a name and nothing is contacted but the product.

## A26: Copies kept by the browser and in between
Kind: chosen
Says: Replies holding names are marked never to be stored by the browser or anything in between. The product keeps no names in the browser's storage. The browser holds only the session cookie, which scripts cannot read, which is sent only over an encrypted connection and not from other sites. After signing out, stepping back and saved addresses show no names: a saved address asks for sign-in. An address to something gone says it is not there. A window already open stops showing names when it next acts, and within 1 minute. What a person photographs, prints or copies is beyond the product.
Rests on: A shared or borrowed device must not keep the list.
Settles: L.user-action-04.list-view, L.user-action-12.list-view, L.stored-data-06.list-view, L.stored-data-10.waiting-list, F.browser.kept-by-browser, F.browser.known-by, L.authorization-11.list-view
Under: new: nothing-left-behind
Criterion: Given the keeper has seen the list and signed out, when someone steps back or opens its saved address, then no name appears and sign-in is asked for.
Criterion: Given the list is open in a second window, when the keeper signs out in the first, then within 1 minute the second shows no name.

## A27: Signing in
Kind: chosen
Says: Sign-in is needed to see or change anything. There is one way in, by an established sign-in method, with no home-made one, picked at build to be manageable without a smartphone being the only way. No account or password exists by default. After 5 failed tries in a row, further tries wait 15 minutes, and the keeper is told when to try again. Messages do not reveal whether an account exists. The first way in is a single-use code or link that ends after use or after 24 hours, handed over by whoever sets the product up. Confirming needs no second sign-in beyond a live session. Secrets and session values come from a cryptographically secure random source.
Rests on: Established practice. The requirements' limits say non-technical volunteers and that a smartphone cannot be the only way.
Settles: L.sign-in-01.list-view, L.sign-in-02.list-view, L.sign-in-03.list-view, L.sign-in-05.list-view, L.sign-in-06.list-view, L.sign-in-11.carry-across, F.unguessable.made, L.misuse-04.carry-across
Under: new: sign-in
Criterion: Given a fresh installation, when anyone tries a default or common account, then there is none to get in with.
Criterion: Given 5 failed tries in a row, when a sixth is made within 15 minutes, then it is refused with the time when a try is possible again.
Criterion: Given a first-use code that was used or is over 24 hours old, when it is tried, then it is refused with word to ask for a new one.
Criterion: Given one address with an account and one without, when a wrong sign-in is tried for each, then the replies read the same.

## A28: Sessions
Kind: chosen
Says: A fresh session is made at every sign-in and any earlier one on that device is dropped. It ends after 30 minutes unused and after 12 hours in all. Two minutes before the unused limit the keeper is warned and can stay signed in. One session at a time: a new sign-in ends the older one. The keeper can sign out everywhere, and whoever runs the product can end all sessions. A change of sign-in details or a sign-in from a new device is shown at the next sign-in and sent by whatever contact route the sign-in method has.
Rests on: One keeper needs one session, and an unattended device must not stay open. The saved draft means nothing is lost when time runs out.
Settles: L.sign-in-07.list-view, L.sign-in-08.list-view, L.sign-in-09.list-view, L.sign-in-10.list-view, L.sign-in-12.list-view, L.authorization-12.list-view, L.accessibility-11.carry-across
Under: new: sign-in
Criterion: Given a signed-in keeper, when 30 minutes pass unused, then the next action asks for sign-in and shows no name.
Criterion: Given 28 minutes unused, when the warning appears and the keeper chooses to stay, then they remain signed in.
Criterion: Given a session on one device, when the keeper signs in on another, then the first can no longer see the list.
Criterion: Given a signed-in keeper, when the screen is looked at, then it shows which account is signed in and offers to sign out.

## A29: Getting back in and handing the list on
Kind: owner
Says: To decide: who can let the keeper back in if they lose their way in, and who gives access to a new keeper and takes it from the old one. Whoever holds that power can reach every name. Removed access stops at once under any choice.
Rests on: A risk and an obligation the society must accept.
Options: One other named committee member can arrange a new way in, checked in person | Only whoever runs the product can, after checking in person | Nobody can, and the list is carried across again from the notebook
Recommended: One other named committee member can arrange a new way in, checked in person, so it does not hang on one person and stays within reach of volunteers.
If left: Only whoever sets the product up could restore or move access.
Harm: medium
Settles: L.sign-in-04.list-view, L.authorization-05.waiting-list
Under: notebook-order-kept

## A30: Who is sure the order is right
Kind: owner
Says: To decide: whether someone besides the keeper checks the carried list against the notebook. The product refuses anyone else and refuses a replacement list, but it cannot know that what the keeper typed matches the notebook, so a person moved up or left out would pass.
Rests on: A rule of the society and a risk it accepts. The problem document says plots have gone to a friend out of turn.
Options: A second committee member checks the draft against the notebook beside the keeper before it is confirmed | The keeper checks alone and the society accepts the risk | The product requires a second person's own approval
Recommended: A second committee member checks the draft against the notebook beside the keeper, because it needs no new access and catches both slips and favours.
If left: The keeper alone vouches for the order.
Harm: high
Settles: L.misuse-05.carry-across, T.waiting-list.carry-across
Under: notebook-order-kept

## A31: Seeing the order that is really kept
Kind: chosen
Says: The list view is read from the kept list each time, never from a copy in the browser, over an encrypted connection. If the kept list cannot be read, no remembered or partial order is shown. The date carried across and the number of people are shown. A change made directly in storage is caught by the integrity check.
Rests on: A stale or substituted order must not be taken as right.
Settles: T.waiting-list.list-view
Under: notebook-order-kept
Criterion: Given the kept list cannot be reached, when the keeper opens the list view, then they are told it cannot be shown and no earlier order appears.

## A32: Encrypted connection and addresses
Kind: chosen
Says: Every connection is encrypted; an unencrypted request gets no data and is not accepted. The product answers only under its own configured host name and refuses others. Each address accepts only the kinds of request it needs and refuses the rest. Nothing else is reachable: no file listing, source history, documentation pages, measurement page or test code. Refusals reveal nothing about what it is built from.
Rests on: Standard hardening of anything reachable over a network.
Settles: F.network.answers-to, F.network.transport, F.network.kinds-of-request, F.network.left-on, F.network.gives-away, L.configuration-06.list-view, L.configuration-11.list-view, T.waiting-details.carry-across
Under: new: closed-to-others
Criterion: Given the product is in real use, when it is asked for anything without encryption, then no name is sent and no change is made.
Criterion: Given the product is in real use, when a request names another host or asks for an unoffered address, then it is refused with no name and no detail of the software.
Criterion: Given the product is in real use, when a request tries to switch on a diagnostic mode, then no diagnostic detail appears.

## A33: What the hosting in between reports
Kind: test
Says: It is not known which facts about a request, such as the sender's address or host name, whatever sits in front of the product supplies, or whether a sender can forge them. No place to run it has been chosen. Until tested, no permission rests on them.
Rests on: No document says how the product is run.
Test: Once a place to run it is chosen, send forged forwarding and host headers and see what the product receives.
Harm: medium
Settles: F.network.in-between
Under: notebook-order-kept

## A34: Survival of saved data on the chosen storage
Kind: test
Says: It is not known which storage will be used or whether what it reports as saved survives a power loss. The product promises this only for storage that passes the test, and checks the list's integrity when read.
Rests on: No document names any storage.
Test: On the chosen storage, read its documentation and cut it off during and just after saves, then compare what is found.
Harm: high
Settles: L.durable-write-03.waiting-list
Under: notebook-order-kept

## A35: Whether the platform can remove the data
Kind: test
Says: It is not known whether the place the product will run can delete its data by itself, for instance for non-payment or inactivity, or what can be got back.
Rests on: No document names where it runs.
Test: Read the chosen provider's terms and documentation on deletion and recovery, and try a restore.
Harm: high
Settles: L.startup-read-07.waiting-list
Under: notebook-order-kept

## A36: Damaged, strange or unreadable data
Kind: chosen
Says: The product tells apart nothing ever saved, a list it can read, and data that exists but is damaged, unrecognised or unopenable. It checks the list's integrity, including that every place has one person and places run without gaps, at start and each read. On failure it shows no part of it, never says nothing was carried across, never overwrites or starts fresh, and tells the keeper the list cannot be read and to use the notebook and get help. Where data can be read but not written, an intact list is shown, changes are refused with that reason, and no repair is attempted.
Rests on: An apparently empty or partial list could be taken for the truth or overwritten.
Settles: L.durable-write-09.waiting-list, L.startup-read-01.waiting-list, L.startup-read-02.waiting-list, L.startup-read-03.waiting-list, L.startup-read-05.waiting-list
Under: new: damaged-data
Criterion: Given the kept list has been altered or cut short outside the product, when the keeper opens it, then they are told it cannot be read and what to do, with no names shown and no offer to start again.
Criterion: Given something unrecognised is where the list is kept, when the product starts, then it leaves it unchanged and says the list cannot be read.
Criterion: Given an intact list that cannot be written to, when the keeper opens it, then it is shown and no change is made to it.

## A37: Spare copies and recovery
Kind: chosen
Says: The saved data is kept as one unit, with its list, draft and the facts needed to check it. A consistent copy is taken by the storage's own backup method after confirming and then daily, never by copying files mid-save. The last 30 daily copies are kept, protected as the original. Part of a set is never used. Restoring is tried before real names are entered and then every year. A restored copy passes the integrity check, and the keeper checks it against the notebook, with its date shown and word that later changes may be missing or removed things back. There is no automatic repair: a damaged list is restored by whoever runs the product. If no copy can be used, only they can, by hand, set the damaged data aside without destroying it, so that the list can be carried across again from the notebook. The keeper finds a readable but wrong list by checking against the notebook, which is not to be thrown away.
Rests on: A tried copy plus the notebook gives two ways back. Whether the storage supports this is covered by its test.
Settles: L.durable-write-10.waiting-list, L.durable-write-11.waiting-list, L.startup-read-08.waiting-list, L.startup-read-09.waiting-list, L.startup-read-10.waiting-list
Under: new: spare-copy
Criterion: Given a confirmed list and its spare copy, when the original is removed and the copy restored, then the same people appear in the same order, with the copy's date.

## A38: One repairer at a time
Kind: not here
Says: The product never repairs data by itself at start, so no starting copy waits on another's repair.
Rests on: The choice to restore only by hand.
Settles: L.startup-read-06.waiting-list
Under: notebook-order-kept

## A39: More than one running copy
Kind: chosen
Says: The one-draft, one-list rule is enforced by the storage itself, so two running copies cannot make two lists or mix them. Only one version runs against the data. A setup where storage cannot enforce this is not used.
Rests on: A check held only in one running copy would not protect shared data.
Settles: L.concurrency-12.waiting-list
Under: new: one-list
Criterion: Given two running copies on the same data, when both confirm at once, then one succeeds, the other is refused, and one intact list is kept.

## A40: Later and earlier versions
Kind: chosen
Says: Saved data carries a version mark. A version that meets a later mark it does not know refuses to show or change the data and says a newer version wrote it; it leaves the data untouched. Going back is possible only when the older version knows the mark; otherwise the newer one is put back.
Rests on: Guessing at unknown data could corrupt the order.
Settles: L.migration-01.waiting-list, L.migration-03.waiting-list
Under: new: damaged-data
Criterion: Given data marked by a later version, when an earlier one starts, then it shows no list, says why, and leaves the data unchanged.

## A41: Settings
Kind: chosen
Says: The settings are where data and spare copies are kept, the host name, the secrets or keys, and which installation it is, trial or real. They differ between installations and are set outside the code by whoever runs the product, never by a request. At start each is checked; if one is missing or wrong the product does not start and says which, without showing its value, to whoever runs it. No default opens access, turns off encryption or points at another installation's data. Trial and real use separate data and secrets and otherwise the same protections. The trial uses invented names only and says on screen that it is a trial.
Rests on: Failing closed, and keeping real names out of trials.
Settles: L.configuration-01.waiting-list, L.configuration-03.waiting-list, L.configuration-05.list-view, L.configuration-07.waiting-list, L.configuration-12.waiting-list, V.every-setting.outside
Under: new: safe-settings
Criterion: Given a required setting is missing or invalid, when the product starts, then it does not serve anything and names the setting, without its value, to whoever runs it.
Criterion: Given a trial installation, when it is opened, then it says it is a trial and shows nothing from the real list.

## A42: Protecting the stored list
Kind: chosen
Says: Names and their order are the sensitive data, in the draft, the list and every copy; an altered order harms as much as a seen one. They are encrypted where stored and in spare copies. Only the product, and whoever runs it with access to the storage, can read or alter them; access to storage is limited to named people. Established managed encryption is used: keys are kept apart from the data and copies, each for one purpose. A way to recover the data key is kept separately. An exposed key is replaced and the data re-encrypted; if every way to a key is lost the copies cannot be read and the list is carried across again from the notebook. No other party receives names for its own use; whoever hosts the product stores them. A reply sends only the names, places, the date and the count.
Rests on: Standard protection of personal details; the notebook remains a way back.
Settles: L.stored-data-01.waiting-list, L.stored-data-02.waiting-list, L.stored-data-03.waiting-list, L.stored-data-04.waiting-list, L.stored-data-07.waiting-list, L.stored-data-08.list-view, T.waiting-details.stored-list, X.waiting-details.stored, X.waiting-details.replies, W.sensitive
Under: new: protected-storage
Criterion: Given a spare copy taken from where it is stored, when it is opened without the key, then no name or order can be read from it.
Criterion: Given the keeper views the list, when the reply is inspected, then it holds nothing beyond names, places, the date carried across and the count.

## A43: What would be wanted
Kind: chosen
Says: Someone meaning harm would want to read who is waiting, or to move, drop or add people. Access is kept to the keeper, replacement is refused, the stored data is protected and checked, and the order's truth to the notebook is on the owner's list.
Rests on: The security pass's table of what is wanted.
Settles: W.prize
Under: notebook-order-kept

## A44: Reading is recorded
Kind: chosen
Says: Each showing of the list or draft is recorded with the account and time, with no names. So are refused tries and sign-ins. Whoever runs the product can read this, and looks at it when something seems wrong.
Rests on: It lets an unexpected reading be noticed.
Settles: L.stored-data-12.waiting-list
Under: new: event-record
Criterion: Given the keeper views the list, when the record is read, then it shows the account and time and no name from the list.

## A45: How long names are kept, and what duties apply
Kind: owner
Says: To decide: what the society must do before real names go in, and how long names are kept, including spare copies and names of people no longer waiting. The documents do not say whether a law, the council lease or members' expectations bind this. Nothing here removes the confirmed list.
Rests on: An obligation the society must accept.
Options: Find out which data protection duties apply, and settle how long names are kept, before real names go in | Go ahead now, keep the list while the waiting list is in use, and accept the risk
Recommended: Find out and settle it before real names go in, because the list holds personal details of about 40 people.
If left: Trials use invented names; the duties and the time names are kept stay unsettled.
Harm: high
Settles: W.obligations, L.stored-data-09.waiting-list
Under: notebook-order-kept

## A46: What leaves a record
Kind: chosen
Says: Records are made of: sign-ins and failures, lockouts, refused requests, draft started and discarded, confirmation tried, succeeded or failed, list shown, access given or removed, integrity failures, restores and setting failures. Each says what happened, to which thing, the outcome, the account where known, the time and for a confirmation the number of people. Single draft entries are not recorded. No names, passwords, codes or session values go in. Times come from the product's own clock in UTC, with a running number to order them. Outside text is not put in records; where unavoidable it is escaped as one value.
Rests on: Enough to say later who carried the list across and when, without making a second copy of it.
Settles: L.logging-01.carry-across, L.logging-02.carry-across, L.logging-03.person-name, L.logging-04.person-name, L.logging-11.carry-across, X.waiting-details.logs
Under: new: event-record
Criterion: Given a list of three invented people is confirmed, when the record is read, then it shows the account, time, outcome and the number three, and none of the names.
Criterion: Given a confirmation fails, when the record is read, then the failure is there and no name is.

## A47: Looking after the records
Kind: chosen
Says: Records are kept for 12 months, then removed automatically, and are capped at 100 MB, dropping the oldest and noting that. They are copied daily apart from the machine that writes them, so at most a day is lost with it. Only whoever runs the product can read or remove them; the product only adds to them, and a gap in the running numbers shows removal. A confirmation is not completed if its record cannot be written, and the keeper is told it failed; for other events an unwritable record means the list is not shown and nothing changes. Repeated refused tries are counted together so they cannot flood the record.
Rests on: The record of who set the order must exist and stay bounded.
Settles: L.logging-05.carry-across, L.logging-06.carry-across, L.logging-08.carry-across, L.logging-10.carry-across, L.logging-12.carry-across
Under: new: event-record
Criterion: Given records cannot be written, when the keeper confirms, then they are told it was not carried across and no list is made.

## A48: Errors and monitoring
Kind: chosen
Says: The keeper sees plain words on what happened and what to do, with a reference number. Technical detail goes only to the records. Neither error messages, traces nor anything sent to monitoring carries names or the order, including request contents. No outside monitoring or measurement service is used. Test data and examples use invented names only.
Rests on: Errors and test data are common ways for personal details to leak.
Settles: L.logging-07.carry-across, X.waiting-details.errors-inside, X.waiting-details.errors-shown, X.waiting-details.telemetry, X.waiting-details.samples
Under: new: no-leaks
Criterion: Given saving fails during a confirmation of invented names, when the message and the error detail are read, then neither holds any of the names.
Criterion: Given the code's test data and examples, when they are read, then every name is invented.

## A49: Whether the hosting records request contents
Kind: test
Says: It is not known whether the place the product runs records or samples request or reply contents on its own, which could hold names.
Rests on: No document names where it runs.
Test: Carry across invented names on the chosen host, then search every log and monitoring view it offers for them.
Harm: medium
Settles: L.logging-09.carry-across
Under: notebook-order-kept

## A50: Noticing a breakage
Kind: chosen
Says: The keeper notices when the list cannot be used, from the plain message, and tells whoever runs the product. A failed integrity check or failed spare copy is also shown to the keeper at next sign-in and sent to whoever runs it. They read the records when told; nothing else needs watching.
Rests on: One user and a five-volunteer committee; a monitoring service would add cost and work.
Settles: W.noticed
Under: new: damaged-data
Criterion: Given the daily spare copy failed, when the keeper next signs in, then they are told and told whom to tell.

## A51: What an outage costs and what counts as working
Kind: chosen
Says: An hour's outage delays carrying across or looking; the notebook is still there and people can still phone. No availability figure is promised. It does not work if the list is ever wrong or lost, or if showing it or confirming takes more than 5 seconds in ordinary use.
Rests on: The slice's own note that people can still phone, and that only the keeper uses it.
Settles: W.unavailable, W.target
Under: new: quick-enough
Criterion: Given a list of 500 invented entries on an ordinary connection, when the keeper opens it, then it is fully shown within 5 seconds.

## A52: Calling it too often
Kind: chosen
Says: Requests from one source or account are limited to 120 a minute; beyond that they are refused with when to try again, and sign-in has its own tighter limit. With size and entry limits and one draft, repeats cannot grow storage without bound. A flood that gets past this is a matter for the hosting.
Rests on: One person typing needs far fewer, so scripts are slowed without troubling the keeper.
Settles: L.misuse-03.carry-across
Under: new: bounded-list
Criterion: Given more than 120 requests from one source within a minute, when another arrives, then it is refused with when to try again.

## A53: The monthly cost under repeated use
Kind: test
Says: It is not known what the chosen way of running it charges, or whether repeated requests, records or copies could take it past 10 pounds a month.
Rests on: The requirements' 10 pound limit; no document names a provider or price.
Test: Check the chosen provider's price page and whether spending can be capped, including heavy repeated requests.
Harm: medium
Settles: L.misuse-06.carry-across
Under: notebook-order-kept

## A54: No limited place to grab
Kind: chosen
Says: An earlier place is the limited thing. Nobody but the keeper can set places, each line has one place, matching names are warned about, and a confirmed list cannot be replaced. People waiting cannot add themselves.
Rests on: Only the keeper's carrying across sets the order in this slice.
Settles: L.misuse-08.waiting-list
Under: notebook-order-kept

## A55: Keyboard and screen reader
Kind: chosen
Says: Everything, including adding, editing, moving, removing, confirming and discarding, can be done by keyboard alone, with no trap. Focus is always visibly marked. When something closes or is removed, focus goes to the control that opened it, or the next entry, or the list's heading. Each control announces its name and purpose, including which entry it acts on. Results, saving, errors and warnings are announced without moving focus unexpectedly.
Rests on: Established accessibility practice; the keeper's abilities are not known.
Settles: L.accessibility-01.carry-across, L.accessibility-02.carry-across, L.accessibility-03.carry-across, L.accessibility-04.carry-across, L.accessibility-05.carry-across, L.accessibility-07.carry-across
Under: new: usable-by-all
Criterion: Given only a keyboard, when the keeper enters three invented names, moves one, removes one and confirms, then every step can be done, leaving any part of the screen, with the focused item always visible.
Criterion: Given a screen reader, when a confirmation succeeds or fails, then the result is read out.
Criterion: Given a screen reader, when focus is on an entry's remove control, then it says what it does and to which entry.

## A56: Reading the screen
Kind: chosen
Says: Anything not text has the same meaning in words. Colour never carries meaning alone. Text has a contrast of at least 4.5 to 1 in every state and theme. At twice the text size nothing is cut off or overlapped, and long names wrap. Nothing moves except a saving indicator, which stays still for those who ask for less motion, with words in its place. Labels wrap rather than being cut, so longer wording fits; only one language is offered.
Rests on: Established accessibility practice.
Settles: L.accessibility-06.list-view, L.accessibility-08.list-view, L.accessibility-09.list-view, L.accessibility-10.list-view, L.accessibility-12.list-view, L.text-12.list-view
Under: new: usable-by-all
Criterion: Given a name of 200 characters, when text is enlarged to twice its size, then the whole name, its place and every control can still be read and used.
Criterion: Given any screen, when its text is measured against its background, then the contrast is at least 4.5 to 1.

## A57: Components
Kind: chosen
Says: Few components are used. A list of all of them, including those they bring, with versions and sources, is kept; versions are locked with checksums and fetched only from their official registries, with names checked when added. Automatic flaw alerts are on. A serious flaw is fixed within 7 days of the alert and others within 30. Those that handle sign-in, encryption, outside data or run at install are chosen from well-maintained ones, install scripts are off unless needed, and the build has no access to real names.
Rests on: Standard supply chain practice.
Settles: F.dependency.known-flaw, F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
Under: new: components
Criterion: Given a component's file differs from its recorded checksum, when the product is built, then the build fails.
Criterion: Given the product as built, when its component list is compared with what is installed, then every component appears with its version and source.
