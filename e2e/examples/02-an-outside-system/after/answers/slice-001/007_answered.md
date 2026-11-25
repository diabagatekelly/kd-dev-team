# Answered

<!-- drawn from: 3012018646 -->

Drawn by script from the answers. Nothing here is written by hand: change the answers and draw again.

## Criteria

- **walker-walk-entry / A1.1**: Given a walker saving a walk, when the save is cut off before it is stored, then the walks list shows either the whole walk or no part of it.
- **walker-walk-entry / A1.2**: Given a walker whose walk has just been shown as saved, when the product loses power and starts again, then the walk is listed with the same client, day and length.
- **walker-walk-entry / A2.3**: Given a walker who has sent a walk, when no confirmation arrives within 15 seconds, then they are told it is not confirmed, their client, day and length are still shown, and they can send it again.
- **walker-walk-entry / A2.4**: Given a walk that was stored although its confirmation never reached the phone, when the walker sends the same entry again, then the walks list shows it once.
- **walker-walk-entry / A2.5**: Given a walker with one saved walk, when saving another fails because storage is full, then they are told it was not saved and the first walk is unchanged.
- **walker-walk-entry / A2.6**: Given a walk still being saved, when the walker closes the product and opens it again, then the walks list shows it only if it was stored.
- **walker-walk-entry / A3.7**: Given a walker with saved walks, when the walks list cannot be loaded, then they are told it could not be loaded and are not told they have no walks.
- **walker-walk-entry / A3.8**: Given a walker whose walk was just confirmed, when they open the walks list, then the walk is in it.
- **walker-walk-entry / A5.9**: Given saved walks written by a later version in a form this one does not know, when this version starts, then it changes none of them and reports why.
- **walker-walk-entry / A5.10**: Given a phone with an out-of-date entry screen, when it sends an entry the current version cannot accept, then no walk is added and the walker is told to reload.
- **walker-walk-entry / A6.11**: Given 120 clients and ten walkers, when all ten send a walk at the same moment, then each walk is saved once under the walker who sent it.
- **walker-walk-entry / A7.12**: Given a walker, when an entry larger than 10 KB reaches the product, then it is refused and no walk is added.
- **walker-walk-entry / A8.13**: Given a walker with 51 walks, when they open the walks list, then 50 are shown and they can reach the remaining one.
- **walker-walk-entry / A9.14**: Given saved data that is damaged or cannot be opened, when the product starts, then it reports itself unavailable, accepts no walk and leaves the data as it was.
- **walker-walk-entry / A9.15**: Given an installation already set up whose saved data is missing, when the product starts, then it does not show an empty list of walks and does not accept entries.
- **walker-walk-entry / A10.16**: Given an entry naming a client the product does not hold, when it is sent, then no walk is added and the walker is told that client is not available.
- **walker-walk-entry / A11.17**: Given a copy taken while walks are being entered, when it is restored to a trial installation, then it opens and every walk in it has its client and walker.
- **walker-walk-entry / A13.18**: Given the stored data stays busy for longer than 15 seconds, when a walker sends a walk, then they are told it is not confirmed.
- **walker-walk-entry / A15.19**: Given a walker who filled in a walk without sending it, when they leave and return, then the walks list does not contain it.
- **walker-walk-entry / A16.20**: Given a walker with a client and a length filled in but no day, when they try to save, then they are told a day is needed and no walk is added.
- **walker-walk-entry / A16.21**: Given a walker with a client and a day filled in but no length, when they try to save, then they are told a length is needed and no walk is added.
- **walker-walk-entry / A17.22**: Given an entry with no client sent without using the entry screen, when it reaches the product, then it is refused and no walk is added.
- **walker-walk-entry / A19.23**: Given a stored client, when a second client is added whose name differs only in capital letters or extra spaces, then it is refused as the same name.
- **walker-walk-entry / A20.24**: Given a client whose name contains markup characters, when a walker sees it in the walks list, then the characters are shown as written and nothing else happens.
- **walker-walk-entry / A21.25**: Given a client who is not offered to a walker, when an entry from that walker names the client, then it is refused and no walk is added.
- **walker-walk-entry / A22.26**: Given a walk on 3 November 2026 lasting 45 minutes, when the walker sees the walks list, then the day shows the month by name with the year and the length shows the word minutes.
- **walker-walk-entry / A22.27**: Given a walker with no walks, when they open the walks list, then it says there are none yet.
- **walker-walk-entry / A22.28**: Given a length entered with a fraction or letters, when it is sent, then it is refused with a message to give whole minutes, and no walk is added.
- **walker-walk-entry / A23.29**: Given a walker with a filled-in entry, when they tap save two times within 1 second, then the walks list shows one walk.
- **walker-walk-entry / A23.30**: Given a walker who has just saved a walk, when they reload the list or step back and forward, then no second walk is added.
- **walker-walk-entry / A24.31**: Given a walker who has just sent a walk, when no reply has arrived yet, then the screen shows that it is being saved and does not show it as saved.
- **walker-walk-entry / A25.32**: Given a walker with a filled-in entry, when they back out without saving, then no walk is added.
- **new: walker-access / A26.33**: Given a walker who has signed out, when someone steps back or opens a saved address on that phone, then no client name or walk is shown.
- **new: walker-access / A26.34**: Given a walker whose sign-in has ended, when they send a walk, then they are told to sign in again and no walk is added.
- **walker-walk-entry / A27.35**: Given a walker with the list open twice, when they add a walk in one and reload the other, then both show it once.
- **walker-walk-entry / A30.36**: Given a phone set to a different time zone, when a walker saves a walk for 3 November 2026, then it is listed on 3 November 2026.
- **walker-walk-entry / A31.37**: Given two walks saved for the same day, when the walker opens the list twice, then the later saved one is first both times.
- **walker-walk-entry / A32.38**: Given two clients whose long names differ only at the end, when a walker chooses a client on a narrow screen, then each name is shown whole.
- **new: walker-access / A33.39**: Given a person who is not signed in, when they open the entry screen or walks list, then no client or walk is shown.
- **new: walker-access / A33.40**: Given a first-access code already used or older than 24 hours, when someone uses it, then access is refused and they are told to ask for a new one.
- **new: walker-access / A33.41**: Given 5 failed sign-ins within 15 minutes, when a sixth is tried, then it is refused and the person is told to wait 15 minutes.
- **new: walker-access / A33.42**: Given a failed sign-in, when whoever runs the product reads its records, then nothing of the secret appears.
- **new: walker-access / A34.43**: Given a walker with the list open, when their access is ended and the phone makes its next request, then nothing more is shown or saved and they are asked to sign in.
- **walker-walk-entry / A35.44**: Given the credential for the product's data cannot be read, when the product starts, then it reports itself unavailable and saves nothing.
- **new: walker-access / A36.45**: Given a session unused for 30 days, when it is used again, then the person is asked to sign in.
- **new: walker-access / A36.46**: Given a session started 90 days ago, when it is used, then the person is asked to sign in.
- **new: walker-access / A36.47**: Given a walker signed in on 3 phones, when they sign in on a fourth, then the one unused longest asks to sign in again.
- **walker-walk-entry / A37.48**: Given two walkers with walks, when one asks for the other's walk directly, then nothing of it is shown.
- **walker-walk-entry / A37.49**: Given a signed-in walker, when their entry names a different walker, then it is refused and no walk is added for either.
- **walker-walk-entry / A37.50**: Given the permission check cannot be completed, when a walker sends a walk, then it is not saved and they are told so.
- **walker-walk-entry / A38.51**: Given a signed-in walker, when another site's page sends an entry from their browser, then no walk is added.
- **walker-walk-entry / A38.52**: Given a signed-in walker, when they follow any link to the product, then no walk is added.
- **walker-walk-entry / A38.53**: Given a signed-in walker, when they view the entry screen, then their own name is shown.
- **new: walker-access / A39.54**: Given a walker who no longer walks a client, when they next open the entry screen, then that client is not offered.
- **walker-walk-entry / A41.55**: Given a required setting is missing, when the product starts, then it does not serve and reports which setting.
- **walker-walk-entry / A41.56**: Given the real installation, when a request asks for a diagnostic mode, then nothing extra is shown.
- **walker-walk-entry / A42.57**: Given a walker saves a walk, when the maintainer reads the records, then they show who saved it and when, and nothing of the client's name.
- **walker-walk-entry / A42.58**: Given a failed save, when the walker sees the message, then it says the walk was not saved and shows no internal detail.
- **walker-walk-entry / A42.59**: Given a record older than 90 days, when the daily clean-up runs, then the record is gone.
- **walker-walk-entry / A43.60**: Given a screen reader, when an entry is saved or refused, then the result is spoken.
- **walker-walk-entry / A43.61**: Given text enlarged to 200 percent on a phone, when the walker uses the entry screen and walks list, then every value and button can be read and used.
- **walker-walk-entry / A43.62**: Given only a keyboard, when a walker enters a walk, then they can complete it and never get stuck.
- **walker-walk-entry / A44.63**: Given a walker saving or listing walks, when what is sent to the phone is inspected, then it holds no client address or door code.
- **walker-walk-entry / A44.64**: Given a walker saving a walk, when the web addresses used are inspected, then none holds a client's name.
- **walker-walk-entry / A46.65**: Given a walker who has sent 30 entries within one minute, when a 31st arrives in that minute, then it is refused with a message to wait and no walk is added.
- **walker-walk-entry / A46.66**: Given an entry carrying a price or another field it may not set, when it arrives, then it is refused and no walk is added.
- **walker-walk-entry / A48.67**: Given an entry whose client is unreadable or does not exist, when it is sent, then the walker is told the client is not available and no walk is added.
- **walker-walk-entry / A49.68**: Given an entry whose day is 30 February 2026, when it is sent, then it is refused with a message about the day and no walk is added.
- **new: walker-access / A50.69**: Given an altered sign-in, when it is used to list or enter walks, then nothing is shown or saved and sign-in is asked for.
- **walker-walk-entry / A51.70**: Given one stored walk with an unreadable length among others, when the walker opens the list, then the others show normally and that one is marked as having a problem, with no made-up length.
- **walker-walk-entry / A52.71**: Given an entry that fails inside the product, when the records, traces, monitoring and the reply are inspected, then no client name appears in them.
- **walker-walk-entry / A52.72**: Given the test data and examples kept with the code, when they are reviewed, then every client in them is invented.
- **walker-walk-entry / A54.73**: Given a walk on its way, when the same entry arrives from two requests at the same moment, then exactly one walk is stored.
- **walker-walk-entry / A55.74**: Given a walker with one saved walk, when an entry with no client is refused, then the saved walk is still listed unchanged.
- **walker-walk-entry / A58.75**: Given a client not yet completely added, when a walker opens the entry screen, then the client is not offered.
- **walker-walk-entry / A59.76**: Given two walkers who both walk a client, when each saves a walk for it at the same moment, then both walks are saved under that client.
- **walker-walk-entry / A60.77**: Given a walk for a client whose name has since changed, when the walker reloads the list, then the walk shows the new name once.
- **walker-walk-entry / A61.78**: Given a screen opened before a client left, when the walker sends a walk for that client, then it is refused as not available and no walk is added.
- **walker-walk-entry / A64.79**: Given another site, when it tries to show the product inside its own page, then the browser shows nothing of the product.
- **walker-walk-entry / A64.80**: Given a sign-in link carrying an outside address to continue to, when a walker signs in, then they are not sent to that address.
- **walker-walk-entry / A65.81**: Given a walk entry sent over an unencrypted connection, when it arrives, then no walk is added.
- **walker-walk-entry / A65.82**: Given a request for a diagnostic page, file listing or source history on the real installation, when it is made, then none is shown.
- **walker-walk-entry / A66.83**: Given a component whose fetched contents do not match the recorded checksum, when the product is built, then the build fails.
- **walker-walk-entry / A67.84**: Given a client stored with more than a name, when a walker's replies are inspected, then only the name and an internal identity are present.
- **new: walker-access / A68.85**: Given an identity of another walker's walk, when a walker asks for it, then it is refused as not available.
- **walker-walk-entry / A69.86**: Given repeated failed sign-ins for one walker, when the fifth fails within 15 minutes, then a record exists and the maintainer is told.
- **walker-walk-entry / A70.87**: Given any saved walk, when its record is looked up, then it shows which signed-in walker saved it and when.
- **walker-walk-entry / A72.88**: Given the product cannot be reached, when the outside check fails twice in a row, then the maintainer is told within 15 minutes.

## For the owner, by harm

### A14: A walker cannot take back an entry in this slice (high)
Decide whether a walker may change or remove a walk they entered by mistake. This is open question 3 of the requirements. Without it, the walker can check the three values on the entry screen before sending, with no separate confirmation step, and the business owner has no correction in the product until slice 2.

- walkers cannot change entries and the business owner corrects them
- walkers can change or remove their own entries

Recommended: walkers cannot change entries yet, because it keeps this slice small and the business owner's correction is already planned.
If left: A wrong walk stays as entered.
Questions waiting on it: 6

### A29: Which day a walk may be entered for (high)
Decide which days a walker may enter: only today and past days, and how far back, and whether a month ever closes to new entries.

- today and past days back to the start of last month
- today and any past day
- any day, including future ones

Recommended: today and past days back to the start of last month, because it covers late entry at month end and keeps out walks not yet done or long billed.
If left: Any past day or today is accepted and a future day is refused.
Questions waiting on it: 3

### A40: Which clients count as a walker's (high)
Decide which clients a walker is the walker for, so may see and enter walks for, including holiday or sickness cover, and whether they keep seeing past walks of clients they no longer walk.

- only clients the business owner assigns to the walker, cover included
- every walker may enter walks for every client

Recommended: only assigned clients, because the limit says client details are for the walker for that client.
If left: A walker is offered only clients assigned to them, and sees only walks of clients still assigned.
Questions waiting on it: 1

### A56: Two walks alike on one day (high)
Decide what happens when a walker deliberately enters a second walk for the same client, day and length as one already saved: it could be a real second walk or a mistake.

- warn the walker and let them save it
- save it without a word
- refuse it

Recommended: warn the walker and let them save it, because a real second walk is still recorded and a mistake is caught.
If left: The second walk is saved and listed as its own walk.
Questions waiting on it: 1

### A57: How clients get into the product (high)
Decide how clients, and which walker walks each, get into the product for this slice. Walk entry needs them there. This is also part of open question 8 of the requirements.

- whoever sets the product up loads the clients and walker assignments for the business owner
- the business owner adds them in the product, as a new requirement

Recommended: whoever sets the product up loads them, because it lets walk entry be used without widening the slice.
If left: There are no real clients for a walker to pick, so walk entry can only be tried with invented ones.
Questions waiting on it: 3

### A73: Legal and contract duties (high)
Decide that you will check what law applies to holding clients' and walkers' details, such as data protection duties, before real details are put in. No document says what applies, and none of it was read.

- check the duties before real client details are loaded
- go ahead and check later

Recommended: check before real client details are loaded, because duties may affect what is kept and for how long.
If left: The slice is tried with invented clients only.
Questions waiting on it: 1

### A4: Whether walkers can enter walks with no signal (medium)
Decide whether a walker must be able to enter a walk while their phone has no signal, to be sent later.

- entry needs a signal
- walks can be entered without a signal and sent later

Recommended: entry needs a signal, because nothing then waits unseen on a phone where it could be lost; choose the other if walkers often have no signal.
If left: No walk is held on the phone for later sending: a walker without a signal is told the walk is not saved.
Questions waiting on it: 3

### A12: How many days of walks may be lost with the storage (medium)
Decide whether it is acceptable that, if the stored data itself is lost, walks entered since the last daily copy (up to a day's worth) are gone and must be entered again.

- accept losing up to one day of walks
- require much less than a day, at possibly more cost

Recommended: accept up to one day, because walkers can still re-enter a day's walks from memory.
If left: Daily copies are made, and up to a day of walks could be lost.
Questions waiting on it: 1

### A18: Which lengths a walk may have (medium)
Decide whether a walker may enter only the walk lengths on the price list, or any length. Prices go by length, and anything not listed is added to the list first (002_requirements.md line 21).

- only lengths on the price list
- any whole number of minutes

Recommended: only lengths on the price list, because every walk entered can then be priced; it needs the lengths to be in the product.
If left: Any whole number of minutes from 1 to 1440 is accepted, and anything outside that is refused.
Questions waiting on it: 1

### A45: How long walks and client details are kept (medium)
Decide how long walks and client details are kept, and when they are removed, including after someone stops being a client.

- keep until the business owner decides otherwise
- remove after a set number of years

Recommended: keep until the business owner decides otherwise, because invoices rest on walks and nothing should vanish before a period is chosen.
If left: Nothing is removed automatically.
Questions waiting on it: 2

### A47: Whether entries need a check by the business owner (medium)
Decide whether a walker's entry counts for billing as soon as it is saved, or only once the business owner has agreed to it.

- counts as soon as saved
- counts only after the business owner agrees

Recommended: counts as soon as saved, because approving every walk would bring back much of the monthly work.
If left: A saved walk stands as entered.
Questions waiting on it: 1

### A63: Who changes or ends a client (medium)
Decide who changes a client's details and who marks that someone has stopped being a client, before there is a way to do it in the product. Walks already entered are kept.

- whoever runs the product does it when the business owner asks
- the business owner does it in the product, as a new requirement

Recommended: whoever runs the product does it when asked, because changes are likely rare and the slice stays small.
If left: Clients stay as first loaded, and a former client stays on offer until someone marks them.
Questions waiting on it: 6

### A71: The risk of a borrowed unlocked phone (medium)
Decide whether it is enough that walkers lock their own phones, given that someone holding a walker's unlocked, signed-in phone can enter false walks that would be billed.

- rely on the phone's lock
- ask the walker to prove who they are before each entry

Recommended: rely on the phone's lock, because proving identity for every walk would slow walkers and the lists show who entered what.
If left: No extra proof is asked beyond the signed-in session.
Questions waiting on it: 1

## Decided by the owner

Nothing.

## To test, by harm

Nothing.

## Chosen without asking; the owner can overturn any of these

- A1: The product tells the walker a walk is saved only after it is durably stored. A walk is stored whole or not at all. Nothing is listed as saved before that. A walk once confirmed must survive a power loss. Because: Invoices rest on these walks, and a half or falsely confirmed walk would be billed wrongly or lost.
- A2: Until the product confirms the walk, the phone shows it as being saved. If no confirmation comes within 15 seconds, or the save fails for any reason, the walker is told it is not confirmed, what they entered stays on screen, and they can send it again. Sending it again never makes a second walk. The product does not retry by itself, and a failed save is never reported as saved. Earlier walks are untouched. Because: A walker must not believe in a walk that is not there. 15 seconds is long enough for a slow phone signal and short enough to wait out.
- A3: The walks list shows what the product holds at the moment it is fetched, each walk with its client read at the same moment. It is fetched when opened, reloaded or after a save, with no background fetching. A confirmed walk is in the next fetch. If the fetch fails or is incomplete, the walker is told the list could not be loaded; it is never shown as empty or complete. A list already on screen says when it was fetched. Because: A walker must be able to tell no walks from walks not loaded; fetching on demand is enough for one walker's own list.
- A5: A version that meets saved data from a later version it does not understand refuses to change it and says so. A phone showing an out-of-date screen is told to reload before its entry is accepted if the entry no longer fits. An update must keep the previous version able to be put back, or say before it runs that it cannot. An update that an old open screen would block does not wait for it; that screen is told to reload. Because: Refusing is safer than guessing at records that will be billed.
- A6: The slice is made to serve at least ten walkers entering at once and 120 clients, which covers four walkers and about sixty clients roughly doubled. No cap is put on a walker's number of walks. Beyond what it can serve, an entry is refused as not saved with an invitation to try again, never dropped silently. Because: 000_problem.md lines 4 and 11 give the size and the expected doubling; the margin costs little.
- A7: Any limit that stops an entry says that the walk was not saved, which limit it was and what to do: shorten or correct the value, or try again later. An entry larger than 10 KB is refused whole; nothing is cut short. Because: One walk is a few short values, so anything larger is not a walk.
- A8: The walks list shows the 50 newest walks by day, and the walker can ask for older ones until all have been reached. Because: It keeps the list quick on a phone without hiding anything.
- A9: At start the product checks that its saved data is there, is its own and is readable. If it is damaged, unfamiliar, cannot be opened or cannot be written, it saves nothing, says it is unavailable and records why for whoever runs it. It never starts afresh over existing data; a new empty store is made only by a deliberate first setup. It repairs nothing by itself. Only one copy changes the data's form at a time; another waits up to 60 seconds and then says it is unavailable. Because: Starting empty or guessing would silently lose the record the invoices come from.
- A10: Every stored walk names one stored client and one walker. A walk that would not is never stored. If one is found anyway, it is not dropped or guessed at: it is reported to whoever runs the product. This holds when several things change at once. Because: A walk with no client or walker cannot be billed or traced.
- A11: Walks and clients are kept on storage that its provider states keeps confirmed writes through power loss, with integrity checks that report damage. A consistent copy of all of it together is taken at least daily without stopping entry, kept apart from the live data for 30 days, and restoring it is tried before first real use and every three months. Nothing is restored automatically. After a restore the whole copy is checked for walks without a client or walker, and the business owner is told the time of the copy, so walks entered since can be asked for again. A walk that is readable but wrong is found by a person; earlier copies show what it was, up to 30 days back. Silent change to a single value is not promised to be detected beyond the storage's own checks. Because: Daily tested copies are ordinary good practice; how much loss is acceptable is asked separately.
- A13: When the stored data is busy, or a save is cancelled by a clash, the product tries within the same 15 seconds the walker waits, at most three times, then reports the walk as not saved. Only one copy of the product's data is written to, and the store itself keeps writers from damaging each other, however many copies of the product run. Because: Several walkers saving at once is normal and should not fail visibly.
- A15: An entry that is started and not sent is not stored by the product. It stays only while the screen is open; if the walker leaves or the phone discards the screen, it is gone and nothing is listed. Because: An entry is three values and quick to redo; a stored draft could be mistaken for a walk.
- A16: Client, day and length are all required, and each is given whole. The client is picked from the clients the product offers, never typed as a new one, so no name's parts or characters are entered. A day is picked as a calendar date. The length is a whole number of minutes. A walker missing a value cannot save and is told which is missing. Empty or blank counts as missing. Because: walker-walk-entry / 1 gives these three; picking avoids misspelled or ambiguous clients and dates.
- A17: Every rule for a walk is checked by the product when the entry arrives, whatever the screen checked. A refusal is shown next to the value it concerns, in plain words saying what to do; a missing client says a client is needed. Because: A check only on the phone can be bypassed; walker-walk-entry / 2 requires the missing-client message.
- A19: No two clients may carry the same name as walkers see it; sameness ignores capital letters, accent-only differences do count, and extra or unseen spaces are ignored. When two clients would share a name, whoever adds them gives each a distinct name that holds no address or door code. Names are cleaned of unseen control characters and surrounding or doubled spaces when stored, written in one standard form, and compared that way. A name that looks like another one is for whoever adds it to change. Because: A walker must pick the right client, and the limit in 002_requirements.md line 15 rules out using an address more widely than needed.
- A20: Everything taken from a person or read back from storage is treated as plain text when shown, stored or passed on, and never run or read as commands. Each client name is shown isolated, so that right-to-left text cannot reorder the day or length beside it. Because: Standard protection against injected content.
- A21: The client must be one the product offers to that walker at the moment the entry arrives. The day and length do not depend on each other or on the client. An entry naming a client not offered to that walker is refused and says the client is not available to them. Because: A walker's entry must not reach clients they are not given.
- A22: The day is picked from a calendar and shown with the weekday, day number, month name and year. The length is typed or picked as whole minutes, digits only, and shown with the word minutes. No fractions or rounding arise. The product is in English, uses the Gregorian calendar and Western digits, shows weeks from Monday and marks no rest days. Wording and counts read correctly for none, one and many walks. Messages wrap and are never cut off. Because: A written month cannot be mistaken for another day; the documents are in English and name no other language or calendar.
- A23: On sending, the walker at once sees that the walk is being saved and cannot send that entry again until it ends. Each entry carries its own identity, so the same entry arriving twice makes one walk. Reloading the list or stepping back after saving sends nothing again: stepping back shows an empty new entry. A second walk deliberately entered is a new entry. Because: Phones double-tap and resend, and a doubled walk would be billed twice.
- A24: While saving, a moving or changing saving indicator and the words that it is being saved are shown. After 15 seconds with no confirmation the product treats the attempt as stuck, stops showing it as in progress and says it is not confirmed. An interrupted save is not resumed by itself; the walker sends it again or checks the list. A failure the product notices is recorded for whoever runs it; the walker learns of it on the screen, or by the walk not being in the list. Nothing is sent to them later. Because: One short save needs only a clear running, saved or not confirmed state.
- A25: A walk is saved only when the walker sends it. Backing out or leaving before that stores nothing. If the phone suspends the screen, the walker finds either what they had typed or a blank entry, never a walk shown as saved that was not. No confirmation step is added: the three values are on one screen beside the save button, and a separate question would be tapped through unread. Because: One screen with three values is its own review.
- A26: When a walker is signed out, for whatever reason, no walk, client name or entry stays visible, including by stepping back or from a saved address; each leads to sign-in. An entry sent without valid sign-in is refused as not saved and the walker is told to sign in again; it is not kept and they enter it again. After signing in, a saved address opens only what that walker may see, and one pointing at something gone says it is not available. Because: A phone can be shared or lost, and the list shows client details.
- A27: Each window shows what it fetched, and sees walks added elsewhere when reloaded or reopened. Walks are only added in this slice, so no window overrides another. Because: With no editing there is nothing to conflict.
- A30: A walk's day is a calendar date with no time or zone and is never converted. Today means today in the business's own time zone, as the product sees it, not the phone's clock. A wrong phone clock may only preselect the wrong day, which is checked on arrival. Walkers elsewhere do not change this. Because: A dog walk belongs to the local day it happened.
- A31: Walks are listed newest day first and, on the same day, latest saved first, using the order the product stored them, so a changed clock cannot reorder them. The order holds across every part of a long list. The list has no choice of column order. Each walk keeps both the day it happened, which later billing uses, and when it was recorded by the product's clock, kept only as record. Because: A stable order avoids walks jumping or being missed between parts.
- A32: The clients offered are listed alphabetically by the name as walkers see it, in English ordering, whatever the phone's language. If searching is offered it ignores capital letters and accents and finds any part of the name. A name may be up to 100 characters, counted as a reader counts them; it is shown whole, wrapping on a narrow screen, and is never cut. Because: One fixed ordering is predictable; a cut name could be mistaken for another client.
- A33: Each walker signs in as themselves; no access is shared. The business owner, or whoever runs the product for them, gives each walker their first access through a single-use link or code that lasts 24 hours, handed to that walker. No account exists before that, apart from none built in. Only one way to sign in exists, with a secret that cannot be guessed by trying: after 5 failed tries in 15 minutes sign-in for that account waits 15 minutes. Secrets are never stored readably, travel only encrypted, and never appear in addresses or records; one found in a record is replaced and removed. Sign-in answers do not reveal whether an account exists. A walker who loses access gets a new single-use code the same way, which ends the old access. Secrets are replaced when lost or exposed, not on a schedule. Because: Telling walkers apart is needed for their walks and the limit on client details; these are standard protections.
- A34: Whoever runs the product for the business owner can end all of a walker's access at once, when a phone is lost, access is exposed or the walker leaves. From the next request nothing works on any ended session, and the person is told to sign in again or ask for new access. Walks already entered stay. The walker is told when their access is changed, by the business owner. Because: Former walkers and lost phones must lose client details immediately.
- A35: Any credential the product needs to reach its own data is unique to the installation, allowed only to read and change that data, kept in a protected secret store that only the running product and its maintainer can read, handed to the product without appearing in code, records or command lines, and different between trial and real. If the store cannot be reached the product reports itself unavailable. A lost one is replaced by a new one, not recovered. Because: Standard least privilege.
- A36: A walker stays signed in until 30 days unused or 90 days in all, whichever comes first. A walker may be signed in on at most 3 phones or browsers; a fourth sign-in ends the one unused longest. A new session is made at every sign-in and anything held before is ended. A walker can sign out. Entering and listing walks need no second proof; changing the sign-in secret does. Because: Walkers use their own phones daily, so frequent sign-in would hinder; limits still end forgotten sessions.
- A37: The product decides every request itself. A walker may enter walks as themselves only, list only their own walks, and be offered only the clients they walk for. The business owner's own use of walks and clients comes with later slices. Anyone else, and anything no rule allows, gets nothing. The walker is taken only from the signed-in session, never from anything the phone sends; an entry that names another walker is refused. If the permission check cannot be completed, the request is refused as not saved or not loaded. Asking for another walker's walk looks the same as asking for one that does not exist. Because: 002_requirements.md line 15 limits who may see client details; refusing by default is standard.
- A38: Walks are added only by a deliberate send from the product's own screen with a valid session. Following a link or loading a page changes nothing, and a send made by another site's page in a signed-in walker's browser is refused. Signing in shows the walker's own name so they can see whose account they are in; it never signs them into an account chosen by a link. Because: Standard protection against forged requests.
- A39: Signing out, losing access, leaving or no longer walking a client takes effect on the next request, on every session: the walker can no longer enter walks for that client or see anything they may not. What is already drawn on a screen disappears on its next request. Whether a walker keeps seeing their own past walks with a client they no longer walk is decided separately. Because: Client details must stop flowing as soon as the reason ends.
- A41: At start every setting is checked for presence and a sensible range; if one is missing or wrong the product does not start serving and names it, without showing secret values. Every setting has a safe default or must be given. Settings are kept with the product's definition apart from secrets, listed with where each came from in one place for the maintainer, changed only by the maintainer (never from a request), tried on the trial installation first, recorded with who and why, and can be put back within 15 minutes. Trial and real installations differ only in listed values, address, secrets and data; the trial holds only invented clients. Only what walk entry and sign-in need is switched on. No diagnostic mode that shows client details can be on in the real one. The maintainer owns the settings. Because: Ordinary safe operation for a small product.
- A42: Each saved or refused walk, each sign-in, failed sign-in, access change, end of access and permission refusal leaves a record with the time on the product's clock, who, what happened, the walk's and client's internal identity and the outcome. A record of a saved walk is the trace of who entered it. Records never hold client names, addresses, door codes or secrets. Text from outside is stored escaped, so it cannot look like an entry of the product. A person sees a plain message; details go to records only. Records are kept apart from the product's machine, can be added to but not altered by the product, only the maintainer can reach them and deletions leave their own trace. They are kept 90 days, then removed automatically, and capped at a set size with a warning at 80 percent. If a record cannot be written, walk entry continues and the maintainer is alerted; a walk's own saved who and when stay with the walk. The maintainer is told of repeated failed sign-ins and failed saves. Order is by the product's clock then sequence. Who read client details is recorded as who opened a list and when, without the details, and is looked at when something is suspected. Because: Enough to settle disputes and spot misuse while keeping client details out of records.
- A43: Every control can be reached and used with a keyboard or switch, in a sensible order, with a visible focus mark and no trap; closing a chooser or message returns focus to where it was or to the value in error. Each control announces its name and purpose, and results such as saved, not saved or client needed are announced. Nothing relies on colour or pictures alone: errors have words. Text and background keep at least 4.5 to 1 contrast, text can be doubled without losing anything, motion is reduced when the phone asks, and no step has a time limit apart from the ordinary sign-in expiry. Because: Common accessibility practice, which also helps outdoor phone use.
- A44: Client names, which days they are walked, addresses and door codes would harm if seen; walks would harm if changed. All are encrypted in transit and at rest including copies, with keys held by the storage's managed protection apart from the data, readable only by the product and its maintainer; a lost key makes data unreadable and is covered by keeping the key recoverable, and an exposed key is replaced. Walk entry and the list send only client name, day, length and an internal identity, never an address or door code. No client detail goes in a web address. Replies are marked not to be stored by anything between, and the phone keeps no copy of walks or clients beyond what is on screen. No other party receives data, apart from whoever hosts the product, which holds it encrypted at rest. This slice stores no address or door code. Because: 002_requirements.md line 15; sending less is the surest protection.
- A46: All limits and rules are enforced where the product receives entries: required values, allowed client, day and length ranges, size and identity. A request may set only client, day, length and the entry's own identity; any other field, including walker or price, makes it refused. A walker may send at most 30 entries a minute and 300 a day; beyond that entries are refused with a wait message, and the maintainer is told. Fetching lists is limited to 60 a minute for each walker, so one person cannot crowd out others. Nothing in walk entry needs a second person's agreement. Because: A person entering walks cannot reach these rates, and a script can.
- A48: An entry whose client is empty or missing is refused with the message that a client is needed. One that is not a client identity the product can read, is oversized, holds strange characters, names no client, names one that is gone or one not offered to this walker, is refused saying the client is not available, with nothing about whether it exists. Any client offered to the walker is accepted, the first or last alike. Nothing is saved on refusal, and the walker can pick again. Because: walker-walk-entry / 2 requires the missing-client refusal; the same answer for unknown and not offered reveals nothing.
- A49: An empty or missing day or length is refused naming the missing one. A value that is not a real calendar date, or not a whole number, is refused saying what is expected. A day outside the days allowed is refused saying which days can be entered; the first and last allowed days are accepted. Nothing is saved on refusal and the other values stay on screen. Because: A walk without a true day and length cannot be billed.
- A50: With no signed-in walker, or an identity that is empty, unreadable, altered or of an account that is ended or gone, nothing is shown or saved and the person is asked to sign in. The same walker signed in on a second phone is the same walker, and walks from both are theirs. Two accounts never share an identity, and an identity is never reused. Because: Every walk and client shown depends on knowing who asks.
- A51: Clients cannot be stored without a name, or with a name over 100 characters or the same as another. If a client name or a walk's client, day or length is nevertheless read back empty, missing, unreadable, impossible, outside its rules or pointing to no client, that walk is shown as having a problem to report to the business owner, without inventing a value, the rest of the list still shows, and it is recorded by internal identity. A client with an unreadable or empty name is not offered for entry. Values at the edge of the rules, long names within the limit and any script's characters are shown whole as written. A client with many walks appears on each of them, which is not a duplicate. A stored day older than the entry range still shows. A walk whose client has since gone keeps showing the client's stored name, only to a walker still allowed to see it. Because: One bad record must not hide the others, and a guessed value would be billed.
- A52: Client names and identities beyond an internal one never go into logs, error messages or traces, monitoring or measurement, on success or failure. An error shown to anyone names no client. Test data and examples use only invented clients. Successful replies give a walker only the names of clients they may see. Stored and copied data is encrypted and reachable only by the product and its maintainer. Because: 002_requirements.md line 15.
- A54: While a walk is on its way it is not in the list. Sending the same entry again, reloading, closing and reopening, or waiting makes at most one walk. After a reload the walker sees it only if it was stored; otherwise they enter it again. A refused entry elsewhere does not affect it. A different walk sent meanwhile from another device is separate. After 15 seconds without confirmation it is shown as not confirmed. Because: The entry's own identity makes repeats safe.
- A55: Entering a refused walk, reloading, reopening, using a second device or the passing of time changes and removes nothing in a saved walk. The same entry sent again makes no second walk. A saved walk stays listed until a later slice gives a way to change it. Because: This slice only adds walks.
- A58: A client is offered only once stored whole with a valid name and an assigned walker. A half-added client is not offered, and an entry naming it is refused as not available. Adding it twice, restarting, reloading, waiting or two people acting at once never leaves two clients with one name or a half client on offer. A walker's refused entry changes nothing. Because: A walker must not bill walks to a record that is not finished.
- A59: Entering a walk, or being refused one, changes nothing about the client. Repeats, reloads, restarts, several walkers entering for the client at once and the passing of time leave the client current, and each separate walk is saved under it. Because: walker-walk-entry / 1 only records a walk.
- A60: A walk stays tied to the same client when the client's details change, and shows the current name. An entry made from a screen with the old name still goes to the same client if the walker still walks them. A change is seen on the next fetch; a restart or the passing of time does not undo it. A refused entry changes nothing. Because: A walk is tied to the client's identity, not its name.
- A61: Once marked as no longer a client, it is not offered and a new entry naming it, even from an old screen or sent at the same moment as the change, is refused as not available. Walks already saved stay saved. The walker is told to speak to the business owner about a walk done before the client left. This holds after restarts, repeats and any length of time. Because: Refusing is safe until the business owner has a way to add late walks; nothing is removed.
- A64: Where the product runs in a browser: each reply is sent with its true type and the browser told not to guess another; data replies are never run as pages. Pages load and run code only from the product itself and no inline or outside code. No other site may frame it or read its replies, and it takes no messages from other windows. It uses no code or styles served by another party. It sends people only to its own addresses. It sends no address details to other sites, and no client detail is in an address. Pages with client details are not kept in the browser's cache. The sign-in is held in a cookie that page code cannot read, sent only over encrypted connections and not by other sites' requests. Because: Standard browser protections.
- A65: It answers only at its own address and host name and refuses others. Every connection is encrypted; an unencrypted one is sent to the encrypted address and nothing is accepted over it. It trusts facts passed on by anything in between only from its own hosting layer, never as proof of who someone is. Each address accepts only its intended kind of request and refuses others. No diagnostics, file listings, source history, documentation pages, measurement pages or test code are reachable. Replies, refusals included, do not say what it is built from. Because: Standard protections for a service on a network.
- A66: A complete list of components and their sources, including what they bring, is kept with the product, with exact versions and checksums, fetched only from the intended sources. Known flaws are checked automatically at least daily; a serious one is fixed or contained within 7 days, others within 30. Components that see credentials, read outside data or run at install are kept few, reviewed before adding and given no more access than needed. Because: Standard supply-chain care.
- A67: A walker sees of a client only its name, never its address, door code or anything else. The business is the only group; no other business's data is held. Because: 002_requirements.md line 15 and 000_problem.md line 4.
- A68: Session values, first-access codes and links, and any request-protection values are made by a secure random source, long enough that guessing is not practical. Internal identities of walks and clients are not secrets: every request is checked for permission whatever identity it names. Because: Standard practice.
- A69: Client names reach only signed-in walkers for their own assigned clients, over encrypted connections; data and copies are encrypted and reachable only by the product and maintainer; access can be ended at once. Attempts show in records of failed sign-ins, refused requests and list openings, and the maintainer is told of repeated failures and of access to stored data outside the product where the hosting records it. Someone using a walker's unlocked phone while signed in looks like that walker: the phone's own lock is the defence, and it is not detected by itself. Because: Layered standard protections; what remains is said.
- A70: Walks come only from a signed-in walker for themselves and their own clients, once for each entry, within rate limits, each recorded with who and when. Only the product and maintainer can reach stored data, changes to records leave a trace, and daily copies let walks be restored. A false walk made with a real walker's access or unlocked phone cannot be told apart by the product; the walker sees it in their own list and the business owner can question it. Because: Standard protections; what remains is put to the business owner.
- A72: If walk entry is down for an hour, walkers keep their walks on paper and enter them later; nothing already saved is lost. It does not work if more than 1 in 100 saves fail in a month, or saves often take more than 5 seconds. A check from outside every 5 minutes and alerts on failed saves tell the maintainer, who tells the business owner; walkers also see failures on screen. What would harm if seen or changed: client names with walk days, and walks, which drive bills. A walker may see only their own walks and assigned clients. Someone meaning harm would want clients' routines or to add or alter billed walks. Because: Modest targets suit a small business whose entry can wait.
