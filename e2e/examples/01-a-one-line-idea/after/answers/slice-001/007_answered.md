# Answered

<!-- drawn from: 301820948 -->

Drawn by script from the answers. Nothing here is written by hand: change the answers and draw again.

## Criteria

- **notebook-order-kept / A2.1**: Given an unfinished list holding the invented names Wren Example then Ash Sample, when the list keeper moves Ash Sample above Wren Example, then Ash Sample is shown first and Wren Example second.
- **notebook-order-kept / A2.2**: Given a complete unfinished list, when the list keeper chooses to keep it, then they are shown the number of people, the first and last names and a warning that it cannot then be changed, and nothing is kept until they confirm.
- **notebook-order-kept / A3.3**: Given an unfinished list with two added entries, when the product is restarted and the list keeper signs in, then both entries are there in the same order, marked as not yet kept.
- **notebook-order-kept / A3.4**: Given a name typed but not yet added, when the list keeper tries to leave the screen, then they are warned that it will be lost.
- **notebook-order-kept / A3.5**: Given an unfinished list, when the list keeper discards it and confirms, then nothing has been carried across and none of its names is shown.
- **notebook-order-kept / A4.6**: Given a complete unfinished list, when keeping it is cut off partway and the product is next opened, then the list keeper is shown either the whole list as kept or the whole unfinished list marked as not kept, never part of either as kept.
- **notebook-order-kept / A4.7**: Given a complete unfinished list, when storing the list fails, then the list keeper is not told it is kept.
- **notebook-order-kept / A5.8**: Given a complete unfinished list and no storage space left, when the list keeper confirms keeping it, then they are told it is not kept, and the unfinished list is still there complete.
- **notebook-order-kept / A5.9**: Given storage stays in use by something else, when the list keeper confirms keeping, then within 10 seconds they are told it is not kept and can try again.
- **notebook-order-kept / A5.10**: Given a keep that failed, when the product is restarted, then the unfinished list is shown as not kept and nothing keeps it without the list keeper.
- **notebook-order-kept / A6.11**: Given a complete unfinished list, when two confirmations to keep it arrive at the same moment, then one list is kept with each entry once.
- **notebook-order-kept / A6.12**: Given a keep with no reply, when 30 seconds have passed, then the list keeper is told it is not known whether the list was kept and to reload.
- **notebook-order-kept / A7.13**: Given a kept list, when a request to keep a different list is sent directly, then it is refused and the list keeper is still shown the first list unchanged.
- **notebook-order-kept / A7.14**: Given a second window opened before the list was kept, when the list keeper adds an entry from it, then it is refused and they are told a list is already kept.
- **notebook-order-kept / A8.15**: Given two windows showing the same unfinished list, when one adds an entry and the other then moves an entry, then the move is refused and the second window shows the list including the added entry.
- **notebook-order-kept / A9.16**: Given the list has just been kept, when the list keeper steps back and reloads, then they are shown the kept list once and are offered no way to keep it again.
- **notebook-order-kept / A9.17**: Given nobody is signed in, when a saved address of the list is opened, then sign-in is shown and no name appears.
- **notebook-order-kept / A10.18**: Given nothing has been entered, when the signed-in list keeper opens the product, then they are told no list has been carried across.
- **notebook-order-kept / A10.19**: Given a kept list, when the list keeper opens it after a restart, then it shows the same people in the same order, the date it was kept, and that later notebook changes are not in it.
- **notebook-order-kept / A11.20**: Given an unfinished list, when a name of only spaces is added, then it is refused beside the field and the list is unchanged.
- **notebook-order-kept / A11.21**: Given an unfinished list, when a name of 201 characters is added, then it is refused, the 200 limit is stated, and nothing is cut or saved.
- **notebook-order-kept / A11.22**: Given an unfinished list, when the invented name "  Zoë   O'Sample-Placeholder " is added, then it is shown as "Zoë O'Sample-Placeholder".
- **notebook-order-kept / A11.23**: Given a request sent directly with an empty name, when it arrives, then it is refused and nothing is saved.
- **notebook-order-kept / A12.24**: Given an unfinished list containing the invented names "Ash Sample" and "ash sample", when the list keeper goes to keep it, then both are pointed out with their positions and neither is removed unless the keeper removes it.
- **notebook-order-kept / A13.25**: Given an unfinished list, when the invented name "<b>Moss</b>" is added, then it is shown exactly as typed, tags included.
- **notebook-order-kept / A13.26**: Given a 200-character name in the list, when the list is shown on a narrow screen, then the whole name can be read.
- **notebook-order-kept / A14.27**: Given an unfinished list with no entries, when keeping it is requested, then it is refused and the list keeper is told to add the names first.
- **notebook-order-kept / A14.28**: Given an unfinished list, when a request arrives with a missing order, a repeated position or an extra field, then it is refused and the stored list is unchanged.
- **notebook-order-kept / A15.29**: Given an unfinished list of 500 entries, when another is added, then it is refused, the limit of 500 is stated, and the 500 remain.
- **notebook-order-kept / A15.30**: Given a list longer than one screen, when the list keeper scrolls through it, then positions run from 1 to the last without a gap or repeat, in notebook order.
- **new: only-the-keeper / A16.31**: Given a kept list and nobody signed in, when the list is requested directly, then it is refused and the reply holds no name.
- **new: only-the-keeper / A16.32**: Given nobody signed in, when a request to add an entry is sent directly, then it is refused and the list is unchanged.
- **new: only-the-keeper / A16.33**: Given the permission check cannot be completed, when the list is requested, then it is refused and no name is sent.
- **new: only-the-keeper / A17.34**: Given the list keeper is signed in, when another site's page sends a request to keep or change the list, then it is refused and the list is unchanged.
- **new: only-the-keeper / A17.35**: Given an unfinished list, when any of the product's addresses is only opened, then nothing is added, kept or discarded.
- **new: only-the-keeper / A18.36**: Given a fresh product, when any sign-in is tried before setup, then it is refused.
- **new: only-the-keeper / A18.37**: Given a setup code that has been used once or is more than 24 hours old, when it is entered, then it is refused and the person is told to ask for a new one.
- **new: only-the-keeper / A18.38**: Given sign-in with a wrong password and with an unknown account, when each is tried, then both show the same message.
- **new: only-the-keeper / A19.39**: Given 5 wrong passwords in a row, when a sixth try is made within 15 minutes, then it is refused and the wait is stated.
- **new: only-the-keeper / A19.40**: Given a session unused for 30 minutes, when the list is requested, then sign-in is asked for and no name is sent.
- **new: only-the-keeper / A19.41**: Given a session 12 hours old, when the list is requested, then sign-in is asked for.
- **new: only-the-keeper / A19.42**: Given the list keeper has signed out, when they step back, then no name is shown.
- **new: only-the-keeper / A19.43**: Given a session on one device, when the keeper signs in on another, then the first is refused at its next request.
- **new: only-the-keeper / A20.44**: Given a signed-in keeper who has viewed the list, when the browser's stored data and history are looked through, then no name is found in them.
- **new: only-the-keeper / A21.45**: Given another site's page, when it tries to show the product inside a frame, then the browser does not show it.
- **new: only-the-keeper / A21.46**: Given the product's pages, when everything they load is listed, then nothing comes from another party's address.
- **new: only-the-keeper / A22.47**: Given the real installation, when a plain unencrypted request for the list is made, then no name is returned.
- **new: only-the-keeper / A22.48**: Given the real installation, when an error is provoked, then the reply shows no trace, version or file path.
- **new: safe-start / A23.49**: Given the storage setting is missing, when the product is started, then it does not start and names that setting.
- **new: safe-start / A23.50**: Given a trial installation, when any screen is opened, then it says it is a trial.
- **new: safe-start / A24.51**: Given a stored list altered outside the product, when the list keeper opens it, then no order is shown and they are told it cannot be trusted and to use the notebook.
- **new: safe-start / A24.52**: Given an unrecognised file where the list is stored, when the product starts, then that file is left unchanged and no new carrying across is offered.
- **new: safe-start / A24.53**: Given a sound list that can be read but not written, when the keeper opens it, then it is shown and marked as unchangeable.
- **new: safe-start / A25.54**: Given a list stored with a later version number, when the product starts, then it shows no list, says a newer version is needed, and leaves the stored data unchanged.
- **new: only-the-keeper / A26.55**: Given a copy of the stored data without its key, when it is searched for a name that was entered, then the name is not found.
- **new: records / A27.56**: Given a list has been kept, when the records are read, then one shows that it was kept, by which account, how many people and when, and none holds an entered name.
- **new: records / A27.57**: Given a failed keep, when the records, the error and the screen are read, then no entered name appears in the record or the error.
- **new: records / A27.58**: Given the files kept with the code, when their examples and test data are read, then every name in them is invented.
- **new: records / A28.59**: Given records cannot be written, when the list keeper confirms keeping the list, then it is not kept and they are told so.
- **new: records / A28.60**: Given a record removed from the middle, when the records are checked, then the gap is reported.
- **new: usable-by-all / A29.61**: Given only a keyboard, when the list keeper enters, reorders, checks and keeps a list, then every step can be done with the focused item visible.
- **new: usable-by-all / A29.62**: Given a screen reader, when keeping the list succeeds or fails, then the result is read out.
- **new: usable-by-all / A29.63**: Given text at twice its size, when the list is shown, then every name, number and control can be read and used.
- **new: safe-start / A30.64**: Given a component whose checksum does not match the list, when the product is built, then the build fails.

## For the owner, by harm

### A33: A second pair of eyes on the order (high)
Whether the list keeper alone may keep the list, or someone else must check it against the notebook first. The product cannot tell whether a name was moved up or left out while typing, and plots have gone to a friend out of turn before. A different or old list sent to replace a kept one is a separate threat, which the product refuses.

- a second committee member reads the whole list against the notebook with the list keeper before it is kept, and the committee notes who and when
- the list keeper checks and keeps it alone

Recommended: a second committee member reads the whole list against the notebook with the list keeper before it is kept, and the committee notes who and when, because it needs no change to the product and gives something to show if the order is questioned
If left: the list keeper can keep it alone, and nobody can show that it matches the notebook.
Questions waiting on it: 2

### A34: A mistake or change after the list is kept (high)
In this slice a kept list cannot be changed, so it can go out of date or stay wrong, and keeping it cannot be undone inside the product. Which list counts meanwhile is yours to decide, as is whether this is acceptable.

- the notebook stays the true list until the product can change its own
- the kept list is the true list from the day it is kept, and changes wait
- changing a kept list is brought into this slice

Recommended: the notebook stays the true list until the product can change its own, because nobody's turn then depends on a copy that cannot be put right
If left: the kept list cannot be changed and nothing says which list counts.
Questions waiting on it: 7

### A35: Notebook lines that are not one clear name (high)
What the list keeper does with a line that is crossed out, unreadable, only part of a name, naming two people, or out of sequence through arrows or insertions. The product needs one non-empty name per place and cannot know your rule.

- the list keeper and one other committee member agree each such line before the list is kept, entering what is known with its place
- the list keeper decides each such line alone

Recommended: the list keeper and one other committee member agree each such line before the list is kept, entering what is known with its place, because each is a judgement about someone's turn
If left: the list keeper decides each one while typing, with no note of it.
Questions waiting on it: 1

### A39: What law or agreement binds the handling of names (high)
The list is personal data. The documents do not say what data protection law, council lease term or society rule applies, such as what the people waiting must be told. This is not a statement of what the law requires.

- a committee member checks what applies before real names are entered
- real names are entered without that check

Recommended: a committee member checks what applies before real names are entered, because the duty falls on the society and may change what is built
If left: only invented names should be entered.
Questions waiting on it: 1

### A37: Who takes over, and who can let them in (medium)
Who may replace the list keeper, who removes the old keeper's access, and who may give a new one-time code if the way in is lost.

- the committee decides, and whoever set the product up gives the new code and ends the old access the same day
- the list keeper names their own replacement

Recommended: the committee decides, and whoever set the product up gives the new code and ends the old access the same day, because control of the list then does not rest with one person
If left: only whoever set the product up can restore access, on no agreed authority.
Questions waiting on it: 2

### A38: How long names and records are kept (medium)
How long the list, an abandoned unfinished list, any copies, and the records are held, what ends them, and what is left when the list is finished with. The slice itself removes nothing but a discarded unfinished list.

- the list is held while the waiting list runs, an unfinished list untouched for 90 days is removed, copies go after 90 days and records after 2 years
- everything is held until the committee asks for its removal

Recommended: the list is held while the waiting list runs, an unfinished list untouched for 90 days is removed, copies go after 90 days and records after 2 years, because names are not then held without a reason while fairness can still be shown
If left: everything stays until someone removes it by hand.
Questions waiting on it: 6

### A40: How reliable it must be, and who notices a failure (medium)
How long it may be out of use, how slow is too slow, who notices a fault, whether spare copies are kept, and how much may be lost. In this slice the notebook still holds the list. A failure during use is shown to the keeper; nobody else is told automatically.

- the notebook is kept safe as the fallback, one spare copy is made when the list is kept and restoring it is tried once, an outage of a few days is acceptable, and the list keeper reports faults to whoever set it up
- the notebook is the only fallback and no spare copy is made
- the product must be watched and restored within an agreed number of hours

Recommended: the notebook is kept safe as the fallback, one spare copy is made when the list is kept and restoring it is tried once, an outage of a few days is acceptable, and the list keeper reports faults to whoever set it up, because it suits volunteers and a small budget
If left: no spare copy is promised, no speed or uptime is promised, and a fault is noticed only when the keeper next uses it.
Questions waiting on it: 6

## Decided by the owner

Nothing.

## To test, by harm

- A41 (high): Where the list will be stored is not chosen, so it is not known whether what is reported stored survives a power cut or restart. Test: once the storage is chosen, read its own documentation on durability, then cut it off during and just after a save and compare what is read back.
- A42 (high): It is not known whether the chosen place deletes stored data on redeploys, inactivity, unpaid bills or plan limits, or what can be got back. Test: once it is chosen, read its terms and documentation on deletion and recovery, and check that data survives a restart and a redeploy.
- A43 (high): The product itself sends the names to no other party. It is not known what the place it runs, or anything between it and the keeper, receives, keeps or passes on, or what it charges against the 10 pounds a month. Test: once the hosting is chosen, read its data, logging, sharing and pricing terms, and check its logs after a trial with invented names.

## Chosen without asking; the owner can overturn any of these

- A2: The names are put in as an unfinished list that is not yet the waiting list. The list keeper can add, change, move and remove entries in it. The whole of it is then shown, numbered, to check against the notebook. It becomes the waiting list only through a separate "keep this list" step, which asks for confirmation, shows the number of people with the first and last names, and says that this version of the product cannot change the list afterwards. All checks are made before that step. Because: a mistake in order costs a person their turn, so it must be catchable before it is kept; a question that shows the count and both ends gives the reader something to check rather than a bare yes or no.
- A3: Each entry added, changed, moved or removed is saved when it is made, and is shown as saved only once it has been stored. Leaving, signing out, a reload, a discarded screen or a restart loses at most the one entry still being typed, and the keeper is warned before leaving with one typed but not added. On return the keeper finds the unfinished list, clearly marked as not yet the waiting list, and carries on or discards it. Discarding asks first and removes all of it. Nothing finishes it or keeps it without the keeper, however long it waits, and there is no stuck state to detect because it only moves when the keeper acts. How long an abandoned one may be held is part of the question of how long names are kept. Because: typing a whole notebook may take more than one sitting, and elderly or non-technical volunteers must be able to stop without losing work.
- A4: Keeping the list is one change: afterwards the whole list with its order is stored, or none of it is and the unfinished list is as it was. The people and their positions are written and read together, so no screen ever shows a part-kept list as the waiting list. "Your list is kept" is said only after the stored list has been read back and matches what was confirmed. There is never a half-made list to undo or clear by hand. Because: a part of a waiting list looks like a whole one and would drop people from their turn.
- A5: If keeping fails for any reason (no space, a storage error, storage in use, read-only), the keeper is told the list is not kept, that their entries are still there, and to try again or contact whoever set the product up. The cause goes only into the record. Nothing is retried automatically, and there is no limit on the keeper's own later tries. A try after a failure is believed only once the stored list reads back as confirmed. Storage in use is waited for at most 10 seconds. A failed try never overwrites or removes what was saved before. If storing a single entry fails, the entry is shown as not saved. Because: an honest failure with the work preserved is safe whatever the storage does, and an automatic retry could report success falsely.
- A6: On confirming, the screen at once says the list is being kept and the button cannot be used again. If no result has arrived after 30 seconds, the keeper is told it is not yet known whether the list was kept and to reload; reloading shows what is really stored. The keep step cannot be stopped once confirmed. A second request while one is running never makes a second list. Because: a visible state with a fixed give-up time tells working from stopped without claiming a result.
- A7: Once a list is kept, every request to add to it, change it, keep another or discard it is refused, whether it comes from a screen, an old page, a second window or a direct call, and the person is told a list is already kept and that this version cannot change it. This holds when the kept list is out of date or wrong. What should be done about a mistake found afterwards is on the owner's list. Because: the slice includes no changing of a kept list (003_slices.md), and silent replacement would let an old or altered list take the true order's place.
- A8: Every change says which version of the unfinished list it was made from. A change from an older version is refused, never merged or repeated by itself; the window says the list changed elsewhere and shows the current one. A window or device shows the current list on its next load or action; nothing is pushed to it. Only one running copy of the product may write the stored list, and stored changes are refused if the stored version has moved on. Because: refusing stale changes keeps the order from being altered without the keeper seeing it.
- A9: Reloading or stepping back never repeats a change. Every screen shows what is stored now: after keeping, stepping back shows the kept list with no way to enter or keep again. A saved address opened while signed out leads to sign-in and shows no name; one pointing at an unfinished list that no longer exists shows the current state. Because: showing only the current state avoids a second action and a stale order.
- A10: With nothing entered, the keeper is told no list has been carried across and offered to start; a restart or any length of time changes nothing. A kept list shows the date it was kept and says that anything changed in the notebook since is not in it. "Nothing carried across" is shown only when the storage is reachable, recognised and empty. Because: a dated list cannot pass for a current one.
- A11: Each entry is one required field holding the name whole, as the notebook writes it, with one part or many. All letters, marks, digits, punctuation and spaces of any language are accepted. Line breaks, tabs, control characters and invisible direction or zero-width characters that serve no part of a name are refused; unusual spaces become ordinary ones, while joiners that a script needs are kept. Spaces at the ends are removed and runs of spaces become one; an empty result is refused. A name may be up to 200 characters as a reader counts them; a longer one is refused with the limit stated and never cut. Rules are enforced where the data is stored, not only on screen. A refusal appears beside the field, says what is wrong and how to put it right, and keeps what was typed. What to do with a notebook line that cannot be read or is not one full name is on the owner's list. Because: refusing only what cannot be seen or breaks the row lets real names through, and a cut name could make two people look alike.
- A12: Names need not be unique. Every entry is its own place, and the product never merges or removes one. Entries that match when capitals (by language-independent folding), accents composed differently and extra spaces are set aside are pointed out to the keeper before keeping, and the keeper says whether they are two people or one entered twice, then removes the extra if one. The names themselves are stored with their capitals as typed. Because: two people can share a name, so only the keeper can tell, while "each once" requires a double entry to be noticed.
- A13: A name is shown, stored and passed on only as text, never run as page code, a command or a query. Each name is isolated so that right-to-left text cannot move the numbers or neighbouring text. Similar names are told apart by their position number, shown in a typeface that distinguishes look-alike characters. Rows and messages wrap and grow; nothing is cut off. Because: standard handling of outside text.
- A14: The order is nothing but the sequence of the entries; positions are numbered 1 upward by the product and are never typed. A list with no entries cannot be kept. A request with a missing, null or wrongly formed order, or with gaps, repeated positions or unknown entries, is refused whole, and the keeper is told nothing was changed. Only the fields name and order are accepted; any other field sent is refused with the request. Because: a position computed from the sequence cannot disagree with it.
- A15: The list takes at most 500 people. Adding a further one is refused, saying the limit and to contact whoever set the product up; nothing already entered is lost. A request far over the size of a full list is refused before it is processed. The whole list is shown as one scrolling list in one order, numbered throughout, with no paging or re-sorting. Because: about 40 people are waiting for 84 plots (000_problem.md), so 500 leaves ample room while bounding any request.
- A16: In this slice one account, the list keeper's, may enter, keep and see the list. Everyone else, signed in or not, is refused everything that no rule allows. Every request is checked where the data is held, whatever screen it came from; the list has one owner and each request is checked against it. Identity and permission are never taken from anything the device can alter. If the check cannot be completed, the request is refused. A reply holds only what that screen needs. The committee's and waiting people's access belong to later slices. Because: the requirement that names are not shown to everyone (002_requirements.md); deny by default is the safe rule until later slices add others.
- A17: Only requests of the kind made for changing can change anything; opening a link or loading a page changes nothing. Each change must carry proof it came from the product's own page. Because: standard protection against requests forged by another site.
- A18: A fresh product has no account and no default password. Whoever sets it up creates the keeper's account with a one-time code, handed over in person, that works once and ends after 24 hours; the keeper then sets their own password of at least 12 characters, with known-breached ones refused. That is the only way in apart from a replacement code made the same way. Sign-in gives the same answer whether or not an account exists, and there is no public sign-up. A new session is made at every sign-in and any earlier one is dropped, so the page shows whose account is signed in. Codes, session identifiers and request proofs come from a cryptographically secure random source. Who may hand out a replacement code is on the owner's list. Because: one account for a volunteer needs no public route in, and each extra route is another thing to protect.
- A19: After 5 wrong tries in a row sign-in waits 15 minutes, and the person is told how long. A session ends after 30 minutes unused and 12 hours in all. One session at a time: a new sign-in ends the old one, and a replacement code or password change ends all sessions. Signing out or losing access stops the session at the next request, and stepping back shows no name. A password change or replacement is shown at the next sign-in with its time. Changing the password asks for the current one; keeping the list needs only the signed-in session and the confirmation. Because entries are saved as made, an ended session loses at most the entry being typed. Because: short, single sessions limit a device left open, and saved entries make that harmless to a slow typist.
- A20: No name or password is put in an address. Replies holding names are marked not to be stored by the browser or anything in between. The browser stores no names; only a session cookie that page code cannot read, sent only over encrypted connections and not with other sites' requests. No address is sent to other sites. Because: standard handling of personal data in a browser.
- A21: The page loads code and styles only from the product itself, with no other party's code. It cannot be framed by another site, replies are sent with their true type and the browser told not to guess, data replies are never run as pages, no other site's page may read replies, the page takes no messages from other windows, and it never sends anyone on to an address someone supplied. Because: standard browser protections; nothing in the slice needs the opposite.
- A22: The product answers only to its own host name over an encrypted connection; a plain request is redirected and carries no data back, and another host name is refused. It trusts facts added by something in between only from the one component set up to add them. Each address accepts only the kinds of request it needs. Diagnostic modes, file listings, source history, test code and documentation pages are off or absent where real names are held. Refusals and errors name no component, version or path. A fresh installation has only sign-in switched on. Someone looking over the keeper's shoulder is not something the product can stop. Because: the least reachable surface is the safe default.
- A23: The settings are where the list is stored, the host name, whether this is a trial or the real installation, and any secret key. All are checked at start; a missing or invalid one stops the start with a message naming the setting, never its secret value, to whoever started it. There is no default that opens access. Only whoever sets the product up can change them, outside the product; nothing in a request can. A trial uses invented names only, has its own storage, says on screen that it is a trial, and otherwise runs the same settings. Because: failing at start is better than running with names somewhere unintended.
- A24: The people and their positions are stored together with a check value over the whole. At start and at every read, the product tells apart: nothing stored; stored and sound; present but damaged, changed, disagreeing, unrecognised or unreadable. In the last case it shows no order and offers no new carrying across, never overwrites or deletes what is there, and tells the keeper the stored list cannot be trusted, to use the notebook and contact whoever set it up. The check value catches damage but not someone able to recompute it. If storage can be read but not written, a sound list is shown, marked as unchangeable, and nothing is repaired. A recovered list is shown as recovered, with its date and number of people, and is not relied on until the keeper has checked it against the notebook. A readable but wrong list is found only by checking it against the notebook; how far back a good copy goes is on the owner's list. Because: showing a damaged order as true would be worse than showing none.
- A25: Everything that makes up the saved list, its version, its check value and any unfinished list, is copied and restored together, by a method that takes it as it stood at one moment; a partial set fails the check and is treated as untrustworthy. The stored form carries a version number. A version meeting data from a later one refuses to open it, changes nothing and says a newer version is needed; so an earlier version put back leaves the newer data intact. Because: refusing is the one behaviour that cannot lose data written by a later version.
- A26: Names and order are the sensitive data: seeing them exposes who is waiting, and changing them can cost a person their turn. The stored list, the unfinished list and every copy are encrypted while stored, readable only by the product and whoever runs it. Keys are kept apart from the data and the code, each used for one purpose (stored data, sessions), and replaceable; an exposed key is replaced and the data re-encrypted. A lost data key means the list is restored from a readable copy or carried across again from the notebook. The session key being replaced only signs people out. Because: a copy taken without its key then gives nothing away.
- A27: Records are made of: setup, sign-in, refused sign-in and lockout, sign-out, password change, each opening of the list, the list kept, discarded, keep failed, refused attempts to change or reach the list, and a failed trust check. Each says what happened, the outcome, which account if any, the number of people where relevant, and the time from the server's clock in UTC with a sequence number. They hold no name, order, password, code or session value, and no free text typed by anyone, so outside text cannot forge a line. Errors carry an error code and no request contents. Nothing is sent to monitoring or measurement. Test data and examples use invented names only. Opening the list is recorded, which is how reading is traced. Because: fairness may need to be shown later, which needs events and times but not names.
- A28: Records are kept apart from the list, and the product can only add to them; each is numbered and chained to the one before, so a gap or change shows when checked. Only whoever runs the product can read or remove them, and a copy goes with the list's spare copies if there are any. Ordinary records are limited to 10 MB; repeated refusals are counted into one record, and at the limit the oldest refusals go first while kept-list records stay. If the record of keeping the list cannot be written, the list is not kept. If a record of a refusal cannot be written, the refusal still stands. Because: the one change that sets everyone's place must never go unrecorded.
- A29: Everything, including moving an entry, is done with the keyboard alone, using named "move up", "move down" and "move to position" controls with no dragging needed. Focus is always visibly outlined and can leave every part; when something holding focus closes, focus goes to the control that opened it or the next entry. Every control has a spoken name saying what it does and to which position. Results and refusals are announced. Anything not text, and any meaning shown by colour, also has words. Text contrast is at least 4.5 to 1 in every state. At twice the text size nothing is lost or overlaps. Nothing moves except a progress sign, which stays still for anyone who asked for less motion and is given in words. Because: the recognised accessibility level (WCAG 2.2 AA), and volunteers and members who are not technical.
- A30: Every component, including those brought in by others, is listed with its version and source and fetched only from the named source with its checksum verified. As few as possible are trusted with passwords, names or install-time execution, and install-time scripts are off unless needed. Known flaws are checked automatically on every change and at least weekly; a serious one is replaced within 14 days. Because: standard supply-chain practice.
- A31: Only the keeper can run anything beyond sign-in. Sign-in tries are limited and request sizes bounded, and nothing in the slice is paid for per use by the product's own design. A stranger causing the lockout can delay the keeper by 15 minutes at a time. What the place the product runs charges is covered by the test of hosting. Because: bounding the open route limits what a stranger can use up.
- A32: An earlier place is the scarce thing. Positions come only from the sequence the keeper confirmed, through the one account, and no request can set a position for one person outside that sequence. Entering a person twice is pointed out as a matching name. Favouritism by the person doing the typing is on the owner's list. Because: the order can then be got only through the checked list.
