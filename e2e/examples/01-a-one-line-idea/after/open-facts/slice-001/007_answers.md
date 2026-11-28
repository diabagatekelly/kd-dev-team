## A1: The notebook stays the list to go by
Kind: fact
Says: This slice cannot change the list once it is brought across. The notebook is still kept up to date as today and is there to check against, so it stands where the two differ.
Rests on: slice-001/004_slice.md, "Left for later": the notebook can still be kept up to date as it is today, and still holds the order to check against.
Settles: L.sync-11.waiting-list, W.unavailable

## A2: The list says it is a copy of the notebook
Kind: chosen
Says: The product cannot know what has since been written in the notebook. The kept list says that it is the order as brought across, that later changes in the notebook are not in it, and that the notebook is the one to go by. It does not compare the two. Before anything is brought across, it says that no list has been brought across yet.
Rests on: A person must not take an old copy for the current order, and the product has no way to read the notebook.
Settles: L.sync-01.waiting-list, L.sync-04.shown-list, S.waiting-list.behind-notebook.bring-notebook-order-across-2, S.waiting-list.behind-notebook.time, C.states.dead-end.2
Under: bring-notebook-order-across
Criterion: Given a list that has been brought across, when the list keeper opens it, then it says that changes made in the notebook since are not in it and that the notebook is the one to go by.
Criterion: Given that nothing has been brought across, when the list keeper opens the list, then they see that no list has been brought across yet.

## A3: Checked as a whole, then kept all at once
Kind: chosen
Says: The list keeper gives the people in order into an unfinished list. While it is unfinished they can correct, remove, add and move entries. Then they are shown the whole of it, numbered, with the number of people, and asked to confirm that it matches the notebook. Only that confirmation makes it the kept list, all of it or none of it. The confirmation says it cannot be changed afterwards in the product as this slice builds it, because putting right is left for slice 3. An unfinished list is never shown as the waiting list.
Rests on: The order must be exactly the notebook's, a part list would put people in the wrong place, and one check of the whole list at the one step that matters is a question a person will still read.
Settles: L.sync-08.bringing-across, L.durable-write-01.waiting-list, L.durable-write-06.waiting-list, L.durable-write-08.waiting-list, L.concurrency-02.waiting-list, L.concurrency-05.bringing-across, L.lifecycle-01.bringing-across, L.lifecycle-02.bringing-across, L.lifecycle-05.waiting-list, L.user-action-09.bringing-across, L.long-operation-08.bringing-across, S.waiting-list.not-brought-across.bring-notebook-order-across-1, S.waiting-list.being-brought-across.bring-notebook-order-across-1
Under: bring-notebook-order-across
Criterion: Given an unfinished list of Person C, Person A and Person B, when the list keeper asks to finish, then they see all three numbered 1 to 3 in that order, the count of 3, and a question whether this matches the notebook, saying what confirming will fix.
Criterion: Given a confirmed list of which only part reached storage, when the list keeper opens the product, then no part of it is shown as the kept list and the whole unfinished list is there.
Criterion: Given an unfinished list with Person B placed before Person A by mistake, when the list keeper moves Person A above Person B and confirms, then the kept list has Person A before Person B.

## A4: Unfinished work is saved as it goes
Kind: chosen
Says: Each entry is saved to the unfinished list as it is given, and is marked saved only once it is stored. Leaving, closing, reloading, a discarded screen or an interruption loses at most the entry not yet marked saved. On return the product shows the unfinished list, says that it is not finished, and lets the list keeper carry on or discard it. It never finishes by itself. Discarding asks first and removes every entry.
Rests on: Giving about 40 entries takes a while, and a volunteer who is interrupted should neither lose the work nor end up with a part list taken for the whole.
Settles: L.durable-write-12.bringing-across, L.startup-read-04.waiting-list, L.lifecycle-04.bringing-across, L.user-action-05.bringing-across, L.user-action-06.bringing-across, L.user-action-10.bringing-across, L.long-operation-03.bringing-across, L.long-operation-04.bringing-across, L.long-operation-05.bringing-across, L.long-operation-06.bringing-across, S.waiting-list.being-brought-across.reopened, S.waiting-list.being-brought-across.bring-notebook-order-across-2, C.states.waiting-list.being-brought-across
Under: bring-notebook-order-across
Criterion: Given an unfinished list with two entries marked saved, when the list keeper closes the product and opens it again, then both are there in order, the list is marked unfinished, and they can carry on or discard it.
Criterion: Given an unfinished list, when the list keeper chooses to discard it and confirms, then none of its entries is shown again and the product says no list has been brought across.

## A5: An unfinished list left alone
Kind: chosen
Says: An unfinished list that nobody has touched for 30 days is removed, with its names. While it exists the product says when it will be removed in days left. The notebook still holds everything.
Rests on: Names should not be kept for work that was given up, 30 days leaves time for a volunteer to come back, and nothing is lost that the notebook does not hold.
Settles: L.lifecycle-08.bringing-across, S.waiting-list.being-brought-across.time
Under: bring-notebook-order-across
Criterion: Given an unfinished list untouched for 30 days, when the list keeper next opens the product, then none of its names is shown and they are told it was removed and that they can start again from the notebook.

## A6: Nothing happens to a list by waiting
Kind: chosen
Says: Time alone neither starts a list nor changes or removes a kept one in this slice. How long names are kept at all is for the owner.
Rests on: Removing or reordering a kept list unasked would change people's places.
Settles: S.waiting-list.not-brought-across.time, S.waiting-list.brought-across.time
Under: bring-notebook-order-across
Criterion: Given a kept list of three people, when 90 days pass with nobody using the product, then it still shows the same three in the same order.

## A7: The order kept is the order shown
Kind: fact
Says: Coming back to the list shows the same people in the same order as were brought across.
Rests on: bring-notebook-order-across / 2
Settles: S.waiting-list.brought-across.bring-notebook-order-across-2, L.long-operation-10.waiting-list

## A8: Nothing to come back to yet
Kind: chosen
Says: Coming back before anything is confirmed shows either that no list has been brought across or the unfinished list marked as unfinished. Reloading changes nothing, and doing it again at once changes nothing.
Rests on: The list keeper must know which of the two they are looking at.
Settles: S.waiting-list.not-brought-across.bring-notebook-order-across-2, S.waiting-list.not-brought-across.again, S.waiting-list.not-brought-across.reopened, L.misuse-01.bringing-across
Under: bring-notebook-order-across
Criterion: Given that nothing has been brought across, when a request is made to confirm a list or to see the kept list, then no list is kept or shown and the person is told that none has been brought across.

## A9: Only one list is ever brought across
Kind: chosen
Says: Once a list is kept, another cannot be brought across over it or added to it. Trying says that a list is already there and shows it. A second confirmation of the same list, from a double press, a reload or an old screen, changes nothing and shows the kept list. Putting it right is left for slice 3.
Rests on: A second list replacing or joining the first would change people's places without anyone meaning it.
Settles: L.sync-02.bringing-across, L.concurrency-09.bringing-across, L.long-operation-12.bringing-across, V.list-order.twice, S.waiting-list.brought-across.bring-notebook-order-across-1, S.waiting-list.brought-across.again, S.waiting-list.brought-across.reopened, S.waiting-list.behind-notebook.bring-notebook-order-across-1, S.waiting-list.behind-notebook.again, S.waiting-list.behind-notebook.reopened, L.user-action-02.shown-list, L.user-action-03.shown-list
Under: bring-notebook-order-across
Criterion: Given a kept list, when anyone tries to bring across another, then the kept list is unchanged and they are told one is already there.
Criterion: Given the confirmation of a list has just succeeded, when the list keeper reloads or steps back and confirms again, then there is still one list with each person once, in the same order.

## A10: One thing at a time, and stale screens refused
Kind: chosen
Says: While a confirmation is running, the control is not usable and a second one is not accepted. A change to the unfinished list made from a window that has not seen a later change is refused, and that window is told to look at the list as it now is. This holds for any number of windows or running copies of the product. Nothing is repeated automatically. A window learns of changes when it is next used or reloaded.
Rests on: Refusing a stale change is the known way to stop one window silently undoing another.
Settles: L.concurrency-01.waiting-list, L.concurrency-06.shown-list, L.concurrency-08.bringing-across, L.concurrency-12.waiting-list, L.startup-read-06.waiting-list, L.user-action-01.bringing-across, L.user-action-07.bringing-across, L.long-operation-11.bringing-across, S.waiting-list.being-brought-across.again
Under: bring-notebook-order-across
Criterion: Given two windows showing the same unfinished list, when an entry is added in the first and then the second tries to change or confirm it without reloading, then the change is refused, the first window's entry remains, and the second window is told to reload.
Criterion: Given a confirmation is running, when the list keeper presses confirm again, then only one list is kept.

## A11: The shown list is one moment's list
Kind: chosen
Says: What is shown is the whole list as it stood at one moment, every person once, never a mix of before and after a change.
Rests on: A mix could show a person twice or not at all.
Settles: L.concurrency-03.shown-list
Under: bring-notebook-order-across
Criterion: Given a list being confirmed in one window, when it is opened in another at the same time, then it shows either no kept list or all of the kept list.

## A12: Waiting, progress and giving up
Kind: chosen
Says: While saving, the product shows that it is saving. If no answer comes within 30 seconds it stops waiting, says it could not tell whether the save happened, and asks the list keeper to reload to see what is there. It does not retry by itself. Nothing is saved or reported later in the background, so there is no late result to be told of.
Rests on: A volunteer must be able to tell working from stopped, and saying saved or failed without knowing would mislead.
Settles: L.sync-03.bringing-across, L.durable-write-02.bringing-across, L.long-operation-01.bringing-across, L.long-operation-02.bringing-across, L.long-operation-07.bringing-across, L.long-operation-09.bringing-across
Under: bring-notebook-order-across
Criterion: Given the product cannot be reached, when the list keeper saves an entry, then they see that it is saving and within 30 seconds are told it is not known to be saved and to reload to check.
Criterion: Given an entry marked saved, when the product is stopped and started again, then the entry is still there.

## A13: A save that fails
Kind: chosen
Says: Whatever the cause, lack of space included, a failed save is said to have failed, what was stored before is unchanged, and the entry is not marked saved. The product does not retry by itself or treat a later success as proof: it reads the stored list again before showing it as saved. The list keeper is told they can try again, and that if it keeps failing the notebook is still the list and who set the product up should be told. Every save being refused leaves the list unfinished or not brought across.
Rests on: Reading back what is stored is the only sound answer after storage reports failure, and a list keeper who is not technical needs one plain next step.
Settles: L.durable-write-04.bringing-across, L.durable-write-05.bringing-across, L.logging-07.bringing-across, S.waiting-list.refused-each-time.bring-notebook-order-across-1, S.waiting-list.refused-each-time.bring-notebook-order-across-2, S.waiting-list.refused-each-time.again, S.waiting-list.refused-each-time.reopened, S.waiting-list.refused-each-time.time, C.states.waiting-list.refused-each-time
Under: bring-notebook-order-across
Criterion: Given storage refuses every save, when the list keeper tries to confirm the list twice, then each time they are told it was not kept, that they can try again or tell whoever set the product up, and that the notebook is still the list, and no list is shown as kept.
Criterion: Given a save fails, when the message is shown, then it holds no name, no internal error text and no trace.

## A14: A stored list that cannot be trusted
Kind: chosen
Says: Each time the list is read, the product checks that it is the product's own, complete and unaltered: places run from 1 with none missing or repeated, each has a name, and the whole matches what was recorded when it was kept. If it fails, is not recognisably the product's, or cannot be opened, the product shows no part of it as the list, does not treat it as never brought across, does not overwrite it, and says to go by the notebook and tell whoever set the product up. If it can be read but not changed, a list that passes is shown and any save says it failed. This is also what happens if the platform has removed or emptied it after it was kept.
Rests on: A part or altered list would put people in the wrong place; failing closed and keeping the damaged data for recovery is the known safe course.
Settles: L.durable-write-03.waiting-list, L.durable-write-09.waiting-list, L.durable-write-11.waiting-list, L.startup-read-01.waiting-list, L.startup-read-02.waiting-list, L.startup-read-03.waiting-list, L.startup-read-05.waiting-list, L.startup-read-07.waiting-list, V.stored-list.empty, V.stored-list.missing, V.stored-list.malformed, V.stored-list.twice, S.waiting-list.stopped-by-itself.bring-notebook-order-across-1, S.waiting-list.stopped-by-itself.bring-notebook-order-across-2, S.waiting-list.stopped-by-itself.again, S.waiting-list.stopped-by-itself.reopened, S.waiting-list.stopped-by-itself.time, C.states.waiting-list.stopped-by-itself
Under: bring-notebook-order-across
Criterion: Given a kept list whose stored order has been altered outside the product, when the list keeper opens it, then no list is shown, and they are told it cannot be trusted, to go by the notebook, and to tell whoever set the product up.
Criterion: Given a kept list whose stored data has been removed or cannot be opened, when the list keeper opens the product, then they are not told that no list was ever brought across and are not offered to bring one over it.

## A15: Spare copies and bringing one back
Kind: chosen
Says: A copy of the stored data is taken once a day, only as a whole that was saved, and kept for 30 days unless the owner sets another period. Its protection and access are the same as the original's. Bringing one back is tried once before real names go in. A copy brought back passes the same checks as in A14, and the list keeper is told which day it is from and to check it against the notebook. Wrong but readable data is found by that check against the notebook, and copies reach back 30 days. How much loss and downtime is acceptable is for the owner.
Rests on: A daily whole copy that has been restored once is the known protection, and the notebook is an independent record to check a restored list against.
Settles: L.durable-write-10.waiting-list, L.startup-read-08.waiting-list, L.startup-read-09.waiting-list, L.startup-read-10.waiting-list
Under: bring-notebook-order-across
Criterion: Given a kept list of invented people and the previous day's copy, when the stored data is lost and the copy is brought back, then the same people appear in the same order, with a notice of the copy's day and to check it against the notebook.

## A16: What a name may be
Kind: chosen
Says: Each place has one field, the name, taken whole and as written, so two or more names in one notebook entry stay together. It is required, 1 to 200 characters after spaces at the ends are removed. Letters of any language, marks, digits, spaces and punctuation are accepted. Line breaks and invisible control characters are refused, and unusual spaces are made ordinary ones. Length is counted in characters as a person sees them and nothing is ever cut. Capitals are kept as typed. Which entries in the notebook count as places is for the owner.
Rests on: Names do not fit fixed parts, so one free field with only unseen characters refused is the known safe rule; 200 is far above a real name.
Settles: L.user-input-01.person-name, L.user-input-03.person-name, L.user-input-04.person-name, L.user-input-07.person-name, L.limits-07.bringing-across, L.text-03.person-name, L.text-05.person-name, V.person-name.missing
Under: bring-notebook-order-across
Criterion: Given an unfinished list, when the list keeper gives an empty or all-spaces name, then nothing is added and they are asked for a name.
Criterion: Given an unfinished list, when the list keeper gives a name of 201 characters, then nothing is added or cut, what they typed stays, and they are told the limit of 200.
Criterion: Given an unfinished list, when the list keeper gives the invented name "  Zoë O'Example-Test " , then it is saved as "Zoë O'Example-Test".

## A17: The same name twice
Kind: chosen
Says: Names need not be unique, and two people with one name keep two places. Names count as the same for the warning when they match ignoring capitals, extra spaces and different encodings of the same letter, by general rules not tied to one language, judged when compared; the stored name stays as typed. The list keeper is warned, shown the other place, and may keep both or remove one. Nothing is merged.
Rests on: Two different people can share a name, while the same entry typed twice is a likely slip.
Settles: L.user-input-09.person-name, L.text-01.person-name, L.text-02.person-name
Under: bring-notebook-order-across
Criterion: Given an unfinished list with Person A at place 1, when the list keeper adds "person a", then they are warned that the name is already at place 1 and can keep both or remove the new one, and neither is changed or merged.

## A18: Rules are enforced by the product, and refusals are plain
Kind: chosen
Says: Every rule on names, order, size and who may act is enforced where the list is stored, whatever the screen has checked. A request carries only what it is meant to set; places are worked out from the order, and any other field makes it refused. A refusal says by the entry concerned what is wrong and what to do, and keeps what was typed.
Rests on: A check on the screen alone can be bypassed.
Settles: L.user-input-05.bringing-across, L.user-input-06.bringing-across, L.misuse-02.bringing-across, L.misuse-07.bringing-across, L.limits-06.bringing-across, V.list-order.malformed
Under: bring-notebook-order-across
Criterion: Given a signed-in list keeper, when a request that bypasses the screen sends an empty name, a place number of its own, or an order that is not a list, then it is refused and the stored list is unchanged.

## A19: An empty list, and how large a list may be
Kind: chosen
Says: A list with nobody on it, or with no order sent, cannot be confirmed. A list holds up to 500 people. The 501st is refused, saying so and to tell whoever set the product up. A stored list over that size fails the checks of A14.
Rests on: The problem says about 40 people are waiting, so 500 leaves ample room while bounding what is accepted.
Settles: L.limits-04.waiting-list, V.list-order.empty, V.list-order.missing, V.list-order.long, V.stored-list.long
Under: bring-notebook-order-across
Criterion: Given an unfinished list with nobody on it, when the list keeper asks to finish, then nothing is kept and they are told to add the people first.
Criterion: Given an unfinished list of 500 invented people, when one more is added, then it is refused with the limit and what to do, and the 500 are unchanged.

## A20: The whole list on one page
Kind: chosen
Says: The list is shown whole on one page that scrolls, each person with their place number counted from 1, in the notebook's order throughout. The count reads "1 person" or "3 people"; with nobody it says no one has been added. The wording is in English. Long names wrap and labels have room to grow.
Rests on: Checking against the notebook is easiest with the whole of about 40 people in one place.
Settles: L.limits-08.shown-list, L.presentation-04.shown-list, L.presentation-12.shown-list, L.text-12.shown-list
Under: bring-notebook-order-across
Criterion: Given a kept list of 60 invented people, when the list keeper opens it, then all 60 are reachable by scrolling one page, numbered 1 to 60 in order.
Criterion: Given an unfinished list with one person, when it is shown, then the count reads "1 person".

## A21: A name is only ever text
Kind: chosen
Says: A name is shown, stored and passed on only as text and is never run or read as markup or a command. Each name is isolated so that right-to-left or reordering characters cannot disturb its place number or other rows; characters that only reorder text are refused. Look-alike names are told apart by their place numbers and checked against the notebook.
Rests on: Escaping on output and isolating each value is the known answer to text written to be acted on.
Settles: L.user-input-10.person-name, L.text-09.shown-list, L.text-10.shown-list, T.waiting-list.shown-list
Under: bring-notebook-order-across
Criterion: Given the invented name "<script>alert(1)</script>" in a list, when the list is shown, then those characters appear as written, nothing runs and the order is unchanged.

## A22: Only the list keeper
Kind: chosen
Says: In this slice only the signed-in list keeper may see or act on the list, unfinished or kept. Everyone else, and anything no rule mentions, is refused. Each request is checked where the data is, not only on the screen, and if the check cannot be completed the request is refused. What others may see is decided when the slices that show it are built. There is one list and one account, with no groups and no record partly hidden from the one who may see it.
Rests on: The requirements say people's names are not shown to everyone and leave open who else may see; refusing by default is the known safe course.
Settles: L.authorization-01.waiting-list, L.authorization-03.bringing-across, L.authorization-04.waiting-list, L.authorization-08.shown-list, L.user-action-12.shown-list, T.waiting-people.shown-list, W.who-sees
Under: new: keep-list-private
Criterion: Given a kept list, when someone not signed in opens its address or sends a request for it or to change it, then they see no name, place or count and nothing changes, and they are asked to sign in.
Criterion: Given the check of who is asking cannot be completed, when the list is requested, then no name is shown and the person is told to try again later.

## A23: One account, made at setup
Kind: chosen
Says: No account exists until setup, which makes the one list keeper account. There is no sign-up, no default or spare account and no default password. Whoever sets the product up gives the list keeper, in person or by a route only they receive, a link that works once and for 24 hours, with which they choose their own password. An expired or used link says so and to ask for a new one. There is one way to sign in: that account and password. What the list keeper sets is known to nobody else.
Rests on: A single account with a one-time first link leaves nothing guessable or shared behind.
Settles: L.secrets-02.way-back-in, L.sign-in-02.way-back-in, L.sign-in-05.way-back-in, L.sign-in-06.way-back-in
Under: new: keep-list-private
Criterion: Given a setup link already used or more than 24 hours old, when it is opened, then no password can be set and the person is told to ask for a new link.
Criterion: Given a freshly set up product, when someone tries to sign up or to sign in with a common default name and password, then no account is made and none is entered.

## A24: Guessing at sign-in
Kind: chosen
Says: The password is at least 12 characters, may be a phrase, may be pasted or filled by a password manager, and common ones are refused. After 5 wrong tries in a row, further tries wait 15 minutes, with the wait said; this ends by itself, so the list keeper is not locked out for good. A wrong try never says which part was wrong. At the next sign-in the list keeper is told of wrong tries since the last one.
Rests on: A long password with a short growing barrier to guessing is established practice and does not let a stranger lock the keeper out for good.
Settles: L.sign-in-01.way-back-in, L.misuse-03.bringing-across, L.misuse-04.bringing-across
Under: new: keep-list-private
Criterion: Given 5 wrong passwords in a row, when a sixth try is made within 15 minutes, even with the right one, then it is refused and the person is told to wait 15 minutes.
Criterion: Given wrong tries since the last sign-in, when the list keeper signs in, then they are told how many there were.

## A25: How long being signed in lasts
Kind: chosen
Says: Signed in ends after 30 minutes unused or 12 hours in all, or when the list keeper signs out. A fresh session is made at each sign-in and any earlier one on that browser ends. Up to 3 can be open at once; a fourth ends the oldest. Two minutes before the unused limit the product warns and lets them stay signed in. Entries marked saved are kept; after signing in again they carry on.
Rests on: Short sessions limit what a shared or lost device reaches, and saved entries and a warning mean a slow volunteer loses nothing.
Settles: L.sign-in-08.way-back-in, L.sign-in-09.way-back-in, L.sign-in-10.way-back-in, L.user-action-11.way-back-in, L.accessibility-11.bringing-across
Under: new: keep-list-private
Criterion: Given a signed-in list keeper unused for 28 minutes, when the warning appears and they choose to stay, then they remain signed in; when they do nothing for 2 more minutes, the next request asks them to sign in and shows no name.
Criterion: Given signing in has ended partway through an unfinished list, when the list keeper signs in again, then every entry marked saved is there.

## A26: Signing out, ending sessions and changing the password
Kind: chosen
Says: Signing out takes effect at once, and stepping back shows no name. The list keeper can end all other sessions; changing the password does so too, as does removing access, at once. Changing the password needs the current one, and the product tells the list keeper on the screen at the next sign-in that it changed. Bringing the list across needs the password again if it was last given more than 15 minutes before. If a password is exposed, the list keeper changes it, or whoever set the product up ends all sessions and issues a new one-time link as soon as they are told; nobody can get in with the old one afterwards.
Rests on: Ending access at once and asking again before the one step that fixes everyone's order is established practice.
Settles: L.secrets-05.way-back-in, L.sign-in-07.way-back-in, L.sign-in-11.way-back-in, L.sign-in-12.way-back-in, L.authorization-11.way-back-in, L.user-action-04.shown-list
Under: new: keep-list-private
Criterion: Given the list keeper has signed out, when someone steps back on that device or uses what was held before, then no name is shown.
Criterion: Given two devices signed in, when the password is changed on one, then the other's next request is refused.
Criterion: Given the password was last given more than 15 minutes ago, when the list keeper confirms the list, then it is kept only after they give the password again.

## A27: What proves who someone is
Kind: chosen
Says: The browser holds only a random session value that means nothing by itself, out of reach of the page's code, sent only over the encrypted connection and only to this product. Who the person is and what they may do is looked up by the product and never taken from the device. The product shows which account is signed in. The password is stored only in a form made for passwords that cannot be turned back into it, and travels only encrypted. Any secret the product itself needs is kept outside the code, readable only by the running product and whoever sets it up.
Rests on: This is the established way to hold sessions and passwords; the account name on screen shows the keeper they are in their own.
Settles: L.secrets-01.way-back-in, L.secrets-09.way-back-in, L.authorization-10.way-back-in, L.authorization-12.way-back-in, F.browser.known-by
Under: new: keep-list-private
Criterion: Given a signed-in browser, when its stored session value is altered or made up, then the request is refused and no name is shown.
Criterion: Given a password has been set, when the stored data, the code and the records are looked through, then the password appears in none of them.

## A28: Values that cannot be guessed
Kind: chosen
Says: The session value and the one-time setup link are the only values meant to be unguessable. Each is made fresh from the platform's secure random source with at least 128 bits, expires as in A23 and A25, and is stored so that reading the store does not give a usable one.
Rests on: This is the established way to make such values.
Settles: F.unguessable.made
Under: new: keep-list-private
Criterion: Given two setup links and two sessions made one after another, when they are compared, then none can be worked out from another, and the stored data holds none in usable form.

## A29: Another site acting in the list keeper's name
Kind: chosen
Says: Anything that changes something needs a deliberate send from the product's own page, carrying proof it came from there; following a link or loading a page changes nothing. Pages of other sites may not call the product or read its replies, frame it or send it messages, and the product takes no messages from other windows. It never sends a person on to an address someone else supplied. It tells other sites nothing about the address a person came from.
Rests on: These are the established defences against requests forged from another site.
Settles: L.authorization-06.bringing-across, L.authorization-07.bringing-across, F.browser.framing, F.browser.came-from, F.browser.other-sites, F.browser.messages, F.browser.sent-on
Under: new: keep-list-private
Criterion: Given a signed-in list keeper, when another site's page sends a request to confirm a list, or a link to the product is followed, then nothing is changed.
Criterion: Given another site tries to show the product inside its page, when the page loads, then the product is not shown there.

## A30: What the page may load and how replies are read
Kind: chosen
Says: The page runs only the product's own code and styles from its own address, with nothing from another party loaded while it runs, and the browser is told to block anything else. Every reply states its type and the browser is told not to guess another. A reply meant as data cannot run as a page. No one can submit a file.
Rests on: A strict page policy and declared types are established defences.
Settles: F.browser.context, F.browser.page-policy, F.browser.type-guessing, F.browser.others-code
Under: new: keep-list-private
Criterion: Given the product's pages and data replies, when they are inspected in a browser, then nothing loads from another address, other code is blocked, each reply states its type with guessing forbidden, and opening a data address runs nothing.

## A31: The connection and what can be reached
Kind: chosen
Says: Every connection is encrypted; an unencrypted one is sent to the encrypted address without carrying any list data, and the browser is told to use only encryption. The product answers only under its own address and refuses other host names. It trusts no sender-supplied fact about where a request came from. Each address accepts only the kinds of request it needs. No diagnostic mode, file listing, source history, documentation, measurement page or test code can be reached where it is really used, and a refusal does not say what the product is built from or show a trace.
Rests on: These are established hardening measures.
Settles: T.waiting-people.bringing-across, F.network.answers-to, F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, F.network.gives-away
Under: new: keep-list-private
Criterion: Given the product in real use, when it is asked over an unencrypted connection, under another host name, with a kind of request it does not accept, or for a diagnostic or source address, then no name is returned and the reply shows no trace or component name.

## A32: Settings that are safe as they come
Kind: chosen
Says: With nothing changed the product is closed: it needs sign-in, has diagnostic modes off and switches on nothing the criteria do not need. Settings can be changed only by whoever sets it up, never by a request or a page. A missing, empty, malformed or out-of-range setting that is needed stops the product from starting, with a message naming the setting, not its value, to whoever sets it up.
Rests on: Safe defaults and refusing to start on a bad setting stop a mistake from opening the list.
Settles: L.configuration-05.waiting-list, L.configuration-06.waiting-list, L.configuration-11.waiting-list, L.configuration-12.waiting-list, V.every-setting.missing, V.every-setting.empty, V.every-setting.malformed, V.every-setting.outside
Under: new: keep-list-private
Criterion: Given a needed setting is missing, empty, malformed or out of range, when the product starts, then it does not serve the list and names the setting, without its value, to whoever sets it up.

## A33: Trials and tests use invented people only
Kind: chosen
Says: Any trial copy, test data and example uses invented names only and never a copy of the real list. A trial differs from the real one only in its address, its secrets and its data.
Rests on: The requirements say names are not to be shown to everyone, and a trial is less guarded.
Settles: L.configuration-07.waiting-list, X.waiting-people.samples
Under: new: keep-list-private
Criterion: Given the code, its tests and any trial copy, when they are looked through, then every person in them is invented and none comes from the notebook or the real list.

## A34: What is recorded
Kind: chosen
Says: A record is written for setup, each sign-in and wrong try, each lockout, password change and ending of access, each confirmed or discarded or removed list, each failed save and each failed check of the stored list. Each says what happened, which account, when by the product's own server clock in universal time, whether it worked, and for a list how many people; records are kept in the order written. Reading the list is recorded the same way, as that it was read. No name, password or session value goes into a record, and no text a person typed goes in at all. If the record of confirming or discarding a list cannot be written, that action is not carried out and the person is told it failed; other failures to record do not stop use.
Rests on: These events show later what happened to the order without copying anyone's name into records.
Settles: L.logging-01.waiting-list, L.logging-02.bringing-across, L.logging-03.person-name, L.logging-04.person-name, L.logging-05.bringing-across, L.logging-11.waiting-list, L.stored-data-12.waiting-list, X.waiting-people.logs
Under: new: keep-list-private
Criterion: Given a list of invented people is entered, confirmed and read, and one save fails, when the records are looked through, then the confirmation, reading and failure are there with account, time, result and count, and no name, password or session value is.
Criterion: Given records cannot be written, when the list keeper confirms a list, then it is not kept and they are told it failed.

## A35: Looking after the records
Kind: chosen
Says: Records are kept apart from the list with the daily copy, so the loss of one machine loses at most a day of them. Only whoever sets the product up can read them, and nothing in the product changes or removes them; their numbering shows a gap. They are capped at a size far above a year's use, with the oldest removed first and that removal recorded. Nobody reads them routinely: they are read when the list keeper reports something wrong. The list keeper is told on the screen of failures and wrong sign-ins as they affect them. How long records are kept is part of what the owner decides about keeping people's details.
Rests on: A society of volunteers has no one to watch records, so what matters is shown to the list keeper and the rest is there when needed.
Settles: L.logging-06.waiting-list, L.logging-08.waiting-list, L.logging-09.bringing-across, L.logging-10.waiting-list
Under: new: keep-list-private
Criterion: Given the list keeper is signed in, when they use anything in the product, then no way is offered to change or remove a record.

## A36: Names do not leak
Kind: chosen
Says: Names, places and the order never go into an error's message or trace, an error shown to whoever asked, or an address or its query. Nothing is sent to any monitoring or measurement service. A successful reply carries names only to the signed-in list keeper and only what the screen shows.
Rests on: Keeping personal details out of errors, addresses and measurement is established practice.
Settles: L.stored-data-05.person-name, L.stored-data-08.shown-list, X.waiting-people.errors-inside, X.waiting-people.errors-shown, X.waiting-people.telemetry, X.waiting-people.replies
Under: new: keep-list-private
Criterion: Given a list of invented people, when it is used and each failure in these criteria is made to happen, then no name appears in any address, error message, trace or request to another party, and replies carry no field the screen does not need.

## A37: Names are not left behind in browsers or on the way
Kind: chosen
Says: Pages and replies that show names are marked not to be stored by browsers or anything in between. The product stores no names on the device; only the session value of A27 is held there.
Rests on: This keeps the list off shared devices and intermediate stores.
Settles: L.stored-data-06.shown-list, L.stored-data-10.waiting-list, F.browser.kept-by-browser
Under: new: keep-list-private
Criterion: Given the list keeper has viewed the list and signed out, when the browser's stored data and cache are looked through, then no name is found.

## A38: How stored names are protected
Kind: chosen
Says: What harms someone here is the names and their order (seen), the order (changed) and the sign-in values. The list, its unfinished form and every copy are encrypted where stored, with keys kept and managed apart from the data, each used only for that, readable only by the running product and whoever sets it up. Nobody else can open them. Whoever sets the product up keeps a spare of the keys somewhere separate. A replaced key is brought in without losing data; an exposed one is replaced and the data encrypted again; if all copies of a key are lost the list cannot be read and is brought across again from the notebook. The only other party that may hold the data is whoever the product runs on, which receives it to store and serve it and for nothing else.
Rests on: Encryption at rest with separately held keys is established, and the notebook means a lost key does not lose the list.
Settles: L.stored-data-01.waiting-list, L.stored-data-02.waiting-list, L.stored-data-03.waiting-list, L.stored-data-04.waiting-list, L.stored-data-07.waiting-list, X.waiting-people.stored, W.sensitive
Under: new: keep-list-private
Criterion: Given the stored data and a copy of it without the keys, when they are looked through, then no invented name in the list can be read.

## A39: The ways someone could take the order or the way in
Kind: chosen
Says: Getting in as the list keeper to read the list is met by A23 to A27, and an attempt shows as wrong tries told to the keeper and recorded. A changed order cannot be brought across without the keeper's session and fresh password, over a kept list not at all, and the keeper checks it whole against the notebook before it is kept; confirmations are recorded. Someone taking over the way in is met by the same measures and noticed when the keeper cannot sign in or sees sessions or changes they did not make; the notebook remains, and recovery is what the owner decides.
Rests on: These follow from the measures already chosen.
Settles: T.waiting-people.way-back-in, T.waiting-list.bringing-across, T.waiting-list.way-back-in, L.misuse-08.waiting-list
Under: new: keep-list-private
Criterion: Given a signed-in session older than 15 minutes in someone else's hands, when they try to confirm an unfinished list without the password, then nothing is kept and the refusal is recorded.

## A40: Usable without a mouse or sight
Kind: chosen
Says: Everything can be done by keyboard, nothing traps it, and the focused item is clearly marked. When something is removed or closed, focus moves to the next sensible item. Every control has a name and purpose that a screen reader announces, results of saving and refusals are announced, and anything not text has words. Colour never carries meaning alone. Text contrast is at least 4.5 to 1 in every state, text enlarged to twice its size loses nothing, and nothing moves for someone who asked for less motion. The list is shown as a numbered list a screen reader can follow.
Rests on: These are established accessibility measures, and many members are elderly.
Settles: L.accessibility-01.bringing-across, L.accessibility-02.shown-list, L.accessibility-03.shown-list, L.accessibility-04.bringing-across, L.accessibility-05.bringing-across, L.accessibility-06.shown-list, L.accessibility-07.bringing-across, L.accessibility-08.shown-list, L.accessibility-09.shown-list, L.accessibility-10.shown-list, L.accessibility-12.shown-list
Under: bring-notebook-order-across
Criterion: Given only a keyboard, when the list keeper signs in, enters, corrects, moves, removes and confirms entries and signs out, then each can be done, focus is always visible and never trapped or lost.
Criterion: Given a screen reader, when an entry is saved or refused, then the result is announced and each control's name and each person's place are read.
Criterion: Given text at twice its size and reduced motion asked for, when each screen is used, then nothing is cut off or moves, and text keeps a contrast of at least 4.5 to 1.

## A41: Looking after the parts other people wrote
Kind: chosen
Says: The build keeps a list of every component, those they bring with them included, with where each comes from, at fixed versions checked against recorded fingerprints from the intended source. As few as possible are used, and those that see passwords, read what is typed or run at install are the ones reviewed first. Known flaws are checked for automatically. Who acts on a warning and how soon is part of what the owner decides about upkeep.
Rests on: Pinned, listed and checked components are established practice.
Settles: F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
Under: new: keep-list-private
Criterion: Given the built product, when its component list is compared with what is installed, then each is listed with source and version, and a component whose fingerprint does not match is refused.

## A42: No groups and nothing partly hidden
Kind: not here
Says: There is one society, one list and one account that sees it, so there are no groups to keep apart and no field hidden from someone who may see the record.
Settles: F.several-people.fields, F.several-people.groups

## A43: This slice has no way to end the list
Kind: not here
Says: No criterion ends or closes the waiting list, so the ended state cannot be reached in this slice; removing an unfinished list is A4 and A5, and keeping names is for the owner.
Settles: S.waiting-list.ended.bring-notebook-order-across-1, S.waiting-list.ended.bring-notebook-order-across-2, S.waiting-list.ended.again, S.waiting-list.ended.reopened, S.waiting-list.ended.time, C.states.waiting-list.ended

## A44: Changes in the notebook while it is being brought across
Kind: chosen
Says: The product takes only what the list keeper gives. A change in the notebook during the work gets in only if the keeper puts it in the unfinished list before confirming; the check at confirmation asks that it match the notebook as it is now.
Rests on: The product cannot see the notebook, so the whole-list check is where such a change is caught.
Settles: L.sync-07.bringing-across
Under: bring-notebook-order-across
Criterion: Given an unfinished list, when the list keeper is asked to confirm, then the question asks whether it matches the notebook as it stands now.

## A45: Who notices it is broken
Kind: chosen
Says: The list keeper notices when they use it, because every failure is shown to them with what to do. Nothing watches it for them in this slice, and the notebook remains meanwhile.
Rests on: Only the list keeper uses this slice, and watching would add cost and work for volunteers.
Settles: W.noticed
Under: bring-notebook-order-across
Criterion: Given storage is unavailable, when the list keeper opens the product, then they are told it is not working, to go by the notebook and to tell whoever set it up.

## A46: What someone who means harm would want
Kind: fact
Says: The names of the people waiting and their order, a better place for someone, and the list keeper's way in.
Rests on: bring-notebook-order-across / 1; the requirements say people's names are not shown to everyone.
Settles: W.prize

## A47: A mistake found after the list is kept
Kind: fact
Says: In this slice a kept list cannot be undone, put right or brought across again, a mistake made while bringing it across included. That is left for slice 3, and the notebook holds the order to check against meanwhile.
Rests on: slice-001/004_slice.md, "Left for later": putting right a place that is wrong, including one brought across wrongly, is slice 3, and the notebook still holds the order to check against.
Settles: L.lifecycle-03.bringing-across, L.user-action-08.bringing-across, C.states.dead-end.1

## A48: Your duties for people's details, and the council's terms
Kind: owner
Says: What law, society rule or term of the council lease covers keeping the names of people waiting in the product? The documents do not say. Data protection law may apply, and this planning has not checked it.
Rests on: An obligation that only the society can find out and accept.
Options: Find out what applies before any real name is put in, building and trying it with invented names meanwhile | Put real names in without finding out, accepting that risk
Recommended: Find out first, because the names belong to other people and the lease renewal depends on fair dealing.
If left: It can be built and tried with invented names, and no real name should go in.
Harm: high
Settles: W.obligations
Decided: Find out what applies before any real name is put in, building and trying it with invented names meanwhile (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: new: keep-list-private
Criterion: Given the society has not yet found out what applies to keeping the names, when the product and its copies are looked through, then every name in them is invented.

## A49: How long people's details are kept
Kind: owner
Says: How long should the names, their copies and the records of what happened be kept? This slice removes no kept name.
Rests on: An obligation the society must accept.
Options: Keep the list while the society uses it, records for 12 months and copies for 30 days, and remove everything if the society stops using it | Set other periods, from what the society finds it is bound by
Recommended: The first, because it keeps what is needed to answer a question raised at a yearly meeting and no more; check it against what you find about your duties.
If left: Nothing kept is removed, apart from abandoned unfinished lists and copies older than 30 days.
Harm: medium
Settles: L.stored-data-09.waiting-list, L.logging-12.waiting-list
Decided: Keep the list while the society uses it, records for 12 months and copies for 30 days, and remove everything if the society stops using it (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: new: keep-list-private
Criterion: Given a record more than 12 months old and a copy more than 30 days old, when the stored data is looked through, then neither is there.
Criterion: Given a kept list in use for more than 12 months, when the list keeper opens it, then it is still there.
Criterion: Given the society has stopped using the product and it has been closed down, when its storage, copies and records are looked through, then no list, name or record is left.

## A50: What in the notebook counts as a place
Kind: owner
Says: Is each entry still waiting one place, taken in the order written, with only the name coming across? What about crossed-out entries, entries naming two people, or anything noted beside a name that affects who is ahead?
Rests on: A rule of the society that the documents do not give.
Options: Each entry still waiting is one place, in written order, name only, with crossed-out entries left out | The notebook has other marks or details that change who counts or who is ahead, which you describe
Recommended: The first if it is true of your notebook, because you asked for the order just as it is; if anything else decides who is ahead, say so before the build.
If left: Only names in the order you give them are kept, and anything else stays in the notebook.
Harm: high
Settles: L.user-input-02.bringing-across
Decided: Each entry still waiting is one place, in written order, name only, with crossed-out entries left out (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: bring-notebook-order-across
Criterion: Given an unfinished list, when the list keeper adds an entry, then only a name is asked for and it takes the place in the order where it is put.

## A51: A second person checking the order
Kind: owner
Says: Should a second committee member check the list against the notebook before it is relied on? In this slice only the list keeper acts.
Rests on: A rule of the society about fairness.
Options: A second committee member checks it against the notebook, outside the product, before anyone relies on it | The list keeper's own check is enough
Recommended: A second person's check, because it costs little, needs nothing built and gives the committee something to say about fairness after last year's row.
If left: The list keeper's own check is the only one.
Harm: medium
Settles: L.misuse-05.bringing-across
Decided: A second committee member checks it against the notebook, outside the product, before anyone relies on it (the user, 2026-11-26: "I take what you recommend for each of them.")

## A52: If the list keeper cannot get in, or someone else takes over
Kind: owner
Says: If the list keeper forgets the password, loses access or hands the job on, who may give access to them or to a new list keeper?
Rests on: A rule of the society about who may be trusted with the list.
Options: The person who set the product up gives a new one-time link only when two committee members ask, and ends the old access | The person who set the product up does so when the list keeper alone asks, and for a new list keeper when the committee asks
Recommended: The second, with the link going only to the person named and all old access ending, because it is simple for volunteers and a new keeper still needs the committee.
If left: Nobody has agreed a way back in, and the notebook is all there is if access is lost.
Harm: medium
Settles: L.sign-in-04.way-back-in, L.authorization-05.way-back-in
Decided: The person who set the product up gives a new one-time link when the list keeper alone asks, and for a new list keeper when the committee asks; the link goes only to the person named and all old access ends (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: new: keep-list-private
Criterion: Given a new one-time link has been issued for the list keeper or a new one, when the old password or an old session is used, then it is refused.
Criterion: Given a new one-time link, when the person named uses it within 24 hours, then they set their own password and see the same kept list, and the link does not work again.

## A53: Who looks after it and its fixes
Kind: owner
Says: The committee has no technical members. Who applies security fixes when a component has a known flaw, and how soon?
Rests on: A risk and a cost the society must accept.
Options: Choose a way of building that leaves as much upkeep as possible to the service it runs on, and name someone who applies the rest within 14 days, sooner for a serious flaw | Accept that flaws may go unfixed until someone is found
Recommended: The first, because it holds other people's names and five non-technical volunteers cannot be expected to patch it. Any cost has to fit the 10 pounds a month.
If left: It can be built and tried with invented names, but nobody is responsible for fixing it.
Harm: high
Settles: F.dependency.known-flaw
Decided: Choose a way of building that leaves as much upkeep as possible to the service it runs on, and name someone who applies the rest within 14 days, sooner for a serious flaw (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: new: keep-list-private
Criterion: Given a known flaw in a component that the service it runs on does not look after, when 14 days have passed since the warning, then the product in use no longer holds the flawed version.

## A54: How reliable it must be
Kind: owner
Says: How often may it fail, how slow is too slow, and how much recent work may be lost, before you would say it does not work?
Rests on: How fast and reliable it must be is the society's to say.
Options: It may be out of use for up to a few days, up to a day of work may be lost if storage fails, and pages should appear within 5 seconds on an ordinary connection | It must be back the same day with nothing confirmed ever lost
Recommended: The first, because the notebook is there meanwhile and a stricter promise is likely to cost more than 10 pounds a month allows, which has not been priced.
If left: It is built with daily copies and no promise about time out of use.
Harm: low
Settles: W.target
Decided: It may be out of use for up to a few days, up to a day of work may be lost if storage fails, and pages should appear within 5 seconds on an ordinary connection (the user, 2026-11-26: "I take what you recommend for each of them.")
Under: bring-notebook-order-across
Criterion: Given a list of 500 invented people and an ordinary connection, when any page is opened, then it appears within 5 seconds.
Criterion: Given storage has failed, when the latest copy is brought back, then everything saved more than 24 hours before the failure is there.
