# Answered

<!-- drawn from: 3295467229 -->

Drawn by script from the answers. Nothing here is written by hand: change the answers and draw again.

## Criteria

- **walker-walk-entry / A1.1**: Given a walker with a filled-in entry, when the product cannot confirm that the walk was kept, then they are told it was not confirmed as saved, what they typed is still there, and the list does not show it as saved.
- **walker-walk-entry / A2.2**: Given a walker with at least one saved walk, when the list cannot be read, then they are told it could not be loaded and can try again, and they are not told they have no walks.
- **walker-walk-entry / A4.3**: Given a walker with more saved walks than the first part of the list holds, when they open the list, then it shows that there are older walks and lets them reach every one.
- **walker-walk-entry / A5.4**: Given a walker with 51 saved walks, when they open the list, then it shows the 50 newest and offers the older one.
- **walker-walk-entry / A6.5**: Given a walker whose open screen is from an older version the product no longer accepts, when they save a walk, then they are told to reload and the walk is not shown as saved.
- **walker-walk-entry / A10.6**: Given a walker who has sent 30 save requests in the last 60 seconds, when they save a walk, then they are told to wait 60 seconds and try again, and what they entered is still there.
- **walker-walk-entry / A11.7**: Given a signed-in walker, when a save request larger than 4 KB is sent, then it is refused and no walk is added.
- **walker-walk-entry / A12.8**: Given a walker saving a walk, when the product is stopped partway through the save and started again, then the list shows either the whole walk or no walk from that entry.
- **walker-walk-entry / A15.9**: Given a walker with one saved walk and a store that refuses new writes, when they save another walk, then they are told it was not saved and the list still shows the first walk unchanged.
- **walker-walk-entry / A16.10**: Given a signed-in walker, when a save request names a client that does not exist, then it is refused and no walk is added.
- **walker-walk-entry / A17.11**: Given saved data that fails its integrity check, when the product starts, then walkers are told it is unavailable, no walk can be saved, and the data is left as it was.
- **walker-walk-entry / A19.12**: Given walks being saved, when a spare copy is taken and restored to a test installation, then it starts, passes its integrity check, and every walk in it has its client and walker.
- **walker-walk-entry / A20.13**: Given a walker who closed the screen while a save was under way and the walk was not kept, when they open the list again, then the list does not show it as saved.
- **walker-walk-entry / A21.14**: Given a saved-data location holding something that is not the product's own store, when the product starts, then it does not start, says why, and leaves what is there unchanged.
- **walker-walk-entry / A22.15**: Given a store that can only be read, when a walker saves a walk, then they are told it was not saved, and their earlier walks are still listed.
- **walker-walk-entry / A23.16**: Given one copy of the product holding the data for an upgrade, when a second copy starts, then the second changes nothing and stops with that reason after at most 60 seconds.
- **walker-walk-entry / A25.17**: Given saved data marked with a later format version, when this version starts, then it does not start, says why, and changes nothing.
- **walker-walk-entry / A28.18**: Given a walker whose save has just been confirmed, when they see their list, then it includes that walk.
- **walker-walk-entry / A29.19**: Given a store that stays busy, when a walker saves a walk, then after at most 3 tries within 5 seconds they are told it was not saved and can try again.
- **walker-walk-entry / A33.20**: Given a walker with a client and a day chosen, when they save with a length of 0, 1441, 4.5 or nothing, then they are told what length is accepted and no walk is added.
- **walker-walk-entry / A33.21**: Given a walker with a client and a length filled in, when they save with no day, then they are told a day is needed and no walk is added.
- **walker-walk-entry / A33.22**: Given a walker with a client and a day chosen, when they save with a length of 1 or of 1440, then the walk is saved with that length.
- **walker-walk-entry / A34.23**: Given a signed-in walker, when a save request without a client is sent without using the screen, then it is refused and no walk is added.
- **walker-walk-entry / A36.24**: Given two offered clients with the same name, when a walker chooses a client, then they can tell the two apart without any address or door code being shown, and the saved walk is for the one chosen.
- **walker-walk-entry / A37.25**: Given a client whose stored name contains markup characters, when a walker sees that name in the choice and in their list, then it appears exactly as written and nothing in it is acted on.
- **walker-walk-entry / A39.26**: Given a walker on the entry screen, when they save with the length written as "1:30", then they are told the length is a whole number of minutes and no walk is added.
- **walker-walk-entry / A40.27**: Given a walker whose entry has been sent, when the same entry is sent a second time, then their list shows one walk for it.
- **walker-walk-entry / A41.28**: Given a walker who has just saved a walk, when they reload the list or step back and reload, then no further walk is added.
- **walker-walk-entry / A42.29**: Given a walker who has signed out, when someone steps back or opens a saved address on that phone, then no walk and no client name is shown and sign-in is asked for.
- **walker-walk-entry / A43.30**: Given a walker with a half-filled entry, when they back out of the entry screen, then their list shows no new walk.
- **walker-walk-entry / A47.31**: Given a walker with a filled-in entry whose access has ended, when they save, then no walk is added and they are asked to sign in.
- **walker-walk-entry / A47.32**: Given an unsent entry kept for one walker, when a different walker signs in on that phone, then the entry and its client are not shown.
- **walker-walk-entry / A48.33**: Given a walker whose phone loses signal after pressing save, when the signal returns and they send the same entry again, then their list shows exactly one walk for it.
- **walker-walk-entry / A49.34**: Given a phone whose clock is a week wrong, when a walker picks 3 November 2026 and saves, then the walk is listed on 3 November 2026.
- **walker-walk-entry / A50.35**: Given a saved walk on 3 November 2026, when its list is opened on a phone set to a time zone many hours away, then it still shows 3 November 2026.
- **walker-walk-entry / A51.36**: Given a walker with several walks on the same day, when they open the list twice, then the walks are in the same order both times.
- **walker-walk-entry / A52.37**: Given an offered client whose name has an accented letter, when a walker searches for it in lower case without the accent, then that client is offered.
- **walker-walk-entry / A53.38**: Given two clients whose long names differ only at the end, when a walker sees them in the choice on a narrow phone, then both names are shown in full.
- **walker-walk-entry / A55.39**: Given a walk of 45 minutes on 3 November 2026, when a walker sees it in their list, then the day shows the month by name and the length reads "45 minutes".
- **walker-walk-entry / A57.40**: Given a sign-in and a failed save, when the product's records are read afterwards, then no password, one-time link, session value or other credential appears in them.
- **walker-walk-entry / A58.41**: Given a walker signed in on a phone, when their access is cancelled and the phone next asks for the list or saves a walk, then nothing is shown or added and they are told to sign in again or ask the business owner.
- **walker-walk-entry / A59.42**: Given an installation with a required credential missing, when the product starts, then it does not start, names the missing setting and shows no secret value.
- **walker-walk-entry / A61.43**: Given a request with no sign-in, when it asks for walks or clients or tries to add a walk, then it is refused and shows no walk or client.
- **walker-walk-entry / A62.44**: Given two walkers who each have walks, when one asks for the other's walk by its identifier, then it is answered as not found.
- **walker-walk-entry / A63.45**: Given a signed-in walker, when a save request names a different walker, then it is refused and no walk is added under either walker.
- **walker-walk-entry / A64.46**: Given a signed-in walker, when another site's page sends a save in their name, then it is refused and no walk is added.
- **walker-walk-entry / A65.47**: Given a signed-in walker and a permission check that cannot be completed, when they save a walk, then no walk is added and they are told to try again.
- **walker-walk-entry / A66.48**: Given a walker signed in on two phones, when they sign out on one, then that phone's next request is refused.
- **walker-walk-entry / A67.49**: Given a walker signed in, when they open the entry screen or their list, then their own name is shown.
- **walker-walk-entry / A69.50**: Given a time zone setting that names no real time zone, when the product starts, then it does not start and names that setting.
- **walker-walk-entry / A70.51**: Given a fresh installation, when someone with no access tries to sign up or sign in with a default account, then there is no way to.
- **walker-walk-entry / A71.52**: Given a trial installation, when a walker opens any screen, then it says it is a trial.
- **walker-walk-entry / A73.53**: Given the real installation with a debugging screen switched on in its settings, when it starts, then it does not start and says why.
- **walker-walk-entry / A74.54**: Given a walker who saves a walk, when the records are read, then one entry shows the time, the walker's account and the walk's identifier.
- **walker-walk-entry / A75.55**: Given a failed save for Example Client A, when the records are read, then the client's name appears nowhere in them.
- **walker-walk-entry / A76.56**: Given a save that fails inside the product, when the walker sees the message, then it shows no technical detail and does say what to do next.
- **walker-walk-entry / A82.57**: Given a walker using only a keyboard, when they choose a client and a day, type a length and save, then the walk is saved and they were never stuck in a chooser.
- **walker-walk-entry / A83.58**: Given a walker using a screen reader, when they save with no client, then they hear that a client is needed without searching the screen.
- **walker-walk-entry / A84.59**: Given text enlarged to twice its size on a phone, when a walker uses the entry screen and the list, then all text and controls can be read and used without sideways scrolling.
- **walker-walk-entry / A86.60**: Given 5 failed sign-in attempts for one account within 15 minutes, when a sixth is made, then it is refused and the person is told to wait 15 minutes or ask the business owner.
- **walker-walk-entry / A87.61**: Given a one-time link that has been used or is more than 24 hours old, when someone opens it, then it gives no access and says to ask the business owner for a new one.
- **walker-walk-entry / A88.62**: Given the sign-in screen, when it is tried for a person with an account and for one without, then the reply is the same.
- **walker-walk-entry / A90.63**: Given a session unused for more than 30 days, or begun more than 90 days ago, when it asks for the list, then nothing is shown and sign-in is asked for.
- **walker-walk-entry / A90.64**: Given a walker with 3 sessions, when they sign in a fourth time, then the least recently used one is asked to sign in at its next request.
- **walker-walk-entry / A91.65**: Given a signed-in walker, when they use the entry screen and their list, then no address and no door code appears on screen or in any reply sent to the phone.
- **walker-walk-entry / A93.66**: Given a walker searching, choosing a client, saving and opening their list, when the addresses and reply headers are inspected, then no client name appears in an address and the replies forbid storing.
- **walker-walk-entry / A94.67**: Given a walker using the entry screen and the list, when what the phone sends is inspected, then nothing goes anywhere but the product's own address.
- **walker-walk-entry / A95.68**: Given a walker allowed one client, when they open the client choice and their list, then the replies sent to the phone hold no other client and no address, door code, price or contact detail.
- **walker-walk-entry / A99.69**: Given an account that has sent 60 list requests in 60 seconds, when it sends another, then it is refused and told to wait 60 seconds, and another walker's list still loads.
- **walker-walk-entry / A101.70**: Given a signed-in walker, when a save request also carries a recorded time or any other unlisted field, then it is refused and no walk is added.
- **walker-walk-entry / A103.71**: Given a signed-in walker, when a save names a client they are not allowed or one that does not exist, then it is refused with the same message for both and no walk is added.
- **walker-walk-entry / A104.72**: Given an open entry screen whose chosen client the walker has since lost, when they save, then no walk is added and they are told to pick from the list again.
- **walker-walk-entry / A105.73**: Given a signed-in walker, when a save gives the day as 30 February 2027, then it is refused, they are told a real day is needed and no walk is added.
- **walker-walk-entry / A107.74**: Given a signed-in walker, when a save request with no length is sent without using the screen, then it is refused and no walk is added.
- **walker-walk-entry / A108.75**: Given a request with a made-up or removed session, when it tries to add a walk, then no walk is added and sign-in is asked for.
- **walker-walk-entry / A109.76**: Given two walker accounts with the same display name, when each saves a walk, then each list shows only its own.
- **walker-walk-entry / A110.77**: Given a saved walk whose client has lost its name, when the walker opens their list, then the walk is still shown, marked as name unavailable.
- **walker-walk-entry / A111.78**: Given walks for two clients with the same name, when the walker opens their list, then they can tell which walk is for which.
- **walker-walk-entry / A112.79**: Given a stored walk that points to no client, when its walker opens their list, then it is shown as client unavailable and the other walks are shown normally.
- **walker-walk-entry / A115.80**: Given a stored walk with an unreadable day, when its walker opens their list, then it is shown as day unavailable and the other walks are shown normally.
- **walker-walk-entry / A117.81**: Given a stored walk with a length of 0, when its walker opens their list, then it is shown with length unavailable.
- **walker-walk-entry / A118.82**: Given a stored walk of 1 minute, when its walker opens their list, then the length reads "1 minute".
- **walker-walk-entry / A119.83**: Given a save and a list that are each made to fail inside the product for Example Client A, when the logs, error traces and anything sent to monitoring are read, then the client's name appears in none of them.
- **walker-walk-entry / A120.84**: Given a signed-in walker, when a save naming a client they are not allowed is refused, then the reply holds no client name.
- **walker-walk-entry / A125.85**: Given a walker with a half-filled entry, when they reload the screen, then the entry is empty and their list shows no new walk.
- **walker-walk-entry / A126.86**: Given a walker with one saved walk, when they try to save an entry with no client, then they are told a client is needed and their list still shows exactly the one walk, unchanged.
- **walker-walk-entry / A127.87**: Given a walker with a saved walk, when the product is stopped and started again and they open their list, then the walk is there unchanged.
- **walker-walk-entry / A136.88**: Given two walkers allowed the same client, when both save a walk for it at the same moment, then each list shows that walker's walk and not the other's.
- **walker-walk-entry / A137.89**: Given a saved walk for a client whose stored name is then changed, when its walker opens their list again, then the same walk shows the new name.
- **walker-walk-entry / A140.90**: Given another site that puts the product inside a frame, when its page is opened, then the product is not shown in it.
- **walker-walk-entry / A141.91**: Given a sign-in address that carries another site's address to go on to, when a walker signs in through it, then they are not sent to that site.
- **walker-walk-entry / A142.92**: Given the real installation, when an unlisted address, a request naming another host or a wrong kind of request is tried, then it is refused with no listing, technical detail or name of what the product is built from.
- **walker-walk-entry / A146.93**: Given a signed-in walker, when they try to fetch a client or list that is not theirs, then nothing of it is shown and the records hold the refused attempt without any client name.
- **walker-walk-entry / A147.94**: Given the real installation, when the product is asked for or sent anything without encryption, then no client detail is returned and no walk is added.
- **walker-walk-entry / A148.95**: Given a saved walk altered directly in the store of a test installation, when the daily check runs, then the maintainer is alerted to it.
- **walker-walk-entry / A154.96**: Given a stopped test installation, when 2 checks 5 minutes apart have failed, then the maintainer is told.

## For the owner, by harm

### A3: Whether walks can be entered with no signal (high)
To decide: whether a walker must be able to enter walks while the phone has no signal. It also settles what the phone holds before it is sent, and what happens to that if the phone has to start again. What other answers say about unsent entries and what the phone holds (A20, A26, A43, A48, A95, A122) is written for the first option and is looked at again if the second is chosen.

- entry needs a signal, and an unsent entry is not kept once the screen is gone
- walkers can enter with no signal, and the phone holds entries and sends them later

Recommended: entry needs a signal; it is the smaller slice and never leaves a walk that looks entered but has not arrived. If walkers often have no signal where they work, choose the other.
If left: slice 1 cannot say what happens to an entry made without a signal.
Questions waiting on it: 2

### A13: How much saved work may be lost (high)
To decide: how much confirmed work may be lost to a failure, how far back a good version must be recoverable, and how often bringing a spare copy back is tried. The product confirms a walk only once the store says it is kept (A1). A walk that is readable but wrong can only be noticed by the walker or the business owner reading the list.

- no confirmed walk lost to a power cut; a daily spare copy kept 30 days, with a restore tried before first use and every 3 months, so a lost or ruined store may lose up to a day
- the same, with spare copies taken so that at most an hour can be lost
- no spare copies

Recommended: the first; a day of walks can still be re-entered from memory, and it is far safer than one paper sheet.
If left: walks have no promised spare copy, and a lost store could lose all of them.
Questions waiting on it: 3

### A56: How a walker gets in (high)
To decide: how a walker proves who they are on their phone. It is what they meet every time they come in, and what has to be recovered when lost.

- each walker has their own sign-in with a passkey or phone unlock, set up from a one-time link the business owner gives them
- each walker has their own sign-in with an email address and password
- each walker has a one-time code sent to their phone each time they sign in

Recommended: the first; there is no password to share or forget. It depends on walkers' phones supporting passkeys, which is to be checked once the way to build it is chosen. A code sent by message would also need an outside service the slice does not now have.
If left: walkers cannot be told apart, so no walk can be put down to one.
Questions waiting on it: 1

### A60: Which clients a walker is offered (high)
To decide: which clients count as a walker's own, so which clients a walker is offered and may enter walks for, including when someone covers for another walker. The documents limit addresses and door codes to the business owner and "the walker for that client" but do not say how a walker comes to be that. It also settles how clients get into the product before a walker can pick one.

- the business owner sets which walkers each client has, and a walker is offered only those, by name
- every walker is offered every client's name, with no address or door code

Recommended: the first; a client's name and walking days stay with the people who walk them, and cover is given by adding the walker to the client.
If left: it cannot be said whose clients a walker sees, and the entry screen cannot be built.
Questions waiting on it: 1

### A114: Two walks for one client on one day (high)
To decide: whether two walks for the same client on the same day are ordinary, or something the walker should be warned about or stopped from entering. This is separate from one entry sent twice, which never makes two walks (A40).

- allowed with no warning
- allowed after the walker is told one is already recorded and confirms
- refused

Recommended: allowed after a warning; it catches the same walk typed twice without stopping a real second walk.
If left: a walk typed twice could be billed twice.
Questions waiting on it: 1

### A133: How clients get into the product (high)
To decide: how the clients a walker picks from get into the product, how their names are changed and how one stops being a client, and whether doing that is part of slice 1. A walker cannot enter a walk until the client is there, and neither the slice nor any other slice in the set says who puts them there. Question 8 of the requirements asks what must come across.

- for slice 1, whoever maintains the product loads client names and their walkers once from a list the business owner gives; a screen to manage clients is planned separately
- the business owner gets a screen to add clients and set their walkers, and it is added to what is built before slice 1 is used

Recommended: the first; it keeps slice 1 thin, with names and walkers only and no addresses or door codes, and the maintainer makes later changes the same way when the business owner asks.
If left: there is no client to pick, and slice 1 cannot be used.
Questions waiting on it: 15

### A156: What law or contract binds it (high)
To decide, or to find out: which law or contract binds how client and walker information is handled. The documents name only the business's limit on addresses and door codes and a Tallypay contract, which nothing in this slice uses. No data protection, accessibility or record-keeping duty is stated.

- you or an adviser confirm which duties apply before real client details are put in
- go ahead on the protections chosen here and accept that a duty may be missed

Recommended: the first; the answers here are good practice and not a statement that any law is met.
If left: it is unknown whether the product meets what binds the business.
Questions waiting on it: 1

### A7: What walkers keep if the product is gone for good (medium)
To decide: whether anyone must be able to take the walks out of the product if it can no longer be reached for good. A phone keeps no copy under the recommended way of entering.

- no export in this slice; recovery rests on the business owner's spare copies
- the business owner can take all walks out as a file

Recommended: no export in this slice; invoicing is not yet built, so the owner still works as they do today, and spare copies are asked about separately.
If left: nobody can take walks out except by whoever maintains the product.
Questions waiting on it: 1

### A9: How much the product must handle (medium)
To decide: how many walkers using it at once, and how many clients, the product must handle. The documents give four walkers and about sixty clients, with holiday cover expected to roughly double it; they do not say whether that doubles walkers, walks or clients. Beyond what is chosen, a request that cannot be served is refused with a message to try again, never half done. Speed is asked in A153.

- 10 walkers using it at once and 120 clients
- 25 walkers using it at once and 300 clients

Recommended: the first; it covers the doubling with room to spare.
If left: there is no number to test load or speed against.
Questions waiting on it: 1

### A38: Which days a walk may be entered for (medium)
To decide: which days a walker may enter a walk for: whether a day still to come is allowed, and how far back a walk may be entered. Whatever is chosen, the boundary day is accepted, a day beyond it is refused with the allowed days named, and "today" is judged as in A50. This is separate from any month closing, which is question 3 of the requirements.

- today or any earlier day, never a day to come
- only today and the previous 31 days
- any day, including days to come

Recommended: today or any earlier day; a walk is a thing that has happened, and no cut-off is invented before question 3 is answered.
If left: the product cannot say whether a given day is refused.
Questions waiting on it: 4

### A81: How long records are kept (medium)
To decide: how long walk records, access records and running logs are kept, and what removes them. This is an obligation the business carries about people's information, and no document says what law or contract binds it.

- walk records as long as the walk itself, access records 12 months, running logs 30 days, each removed automatically
- everything 90 days
- everything kept with no end

Recommended: the first, once you have checked what your own legal and tax duties require.
If left: records pile up with no end, or are removed with no agreed rule.
Questions waiting on it: 1

### A96: How long walks and clients are kept (medium)
To decide: how long walks and client details are kept, including after someone stops being a client, and what removes them. It is an obligation about people's information, and walks will also be the record behind invoices.

- walks and clients for 6 years after the walk or after the client leaves, then removed automatically
- walks and clients for 2 years, then removed automatically
- kept with no end

Recommended: the first as a starting point only; check it against your own tax and data protection duties, which no document states.
If left: nothing is ever removed.
Questions waiting on it: 2

### A113: A past walk for a client the walker no longer has (medium)
To decide: whether a walker still sees, in their list, their past walks for a client they no longer walk, with the client's name. The limit on addresses and door codes does not cover names.

- the walk stays listed with its day and length, and the client's name is hidden
- the walk stays listed with the client's name
- the walk is no longer listed

Recommended: the first; the walker can still account for their work, and a former client's name goes no further.
If left: it cannot be said what the list shows once a client moves to another walker.
Questions waiting on it: 1

### A138: A walk for someone no longer a client (medium)
To decide: whether a walker may still enter a walk for someone who has stopped being a client, for instance a walk done before they left and not yet entered. If not, that walk has to reach the business owner another way.

- no: they are no longer offered, and the walker tells the business owner about any walk not yet entered
- yes, for days up to the day they left

Recommended: yes, for days up to the day they left; a walk that was done should be able to be recorded and billed.
If left: it cannot be said whether such a walk is refused.
Questions waiting on it: 1

### A151: A walker's unlocked phone in other hands (medium)
To decide, as a risk to accept or not: someone holding a walker's unlocked phone with the product signed in can see that walker's clients and enter false walks. The phone's own lock, ending sessions (A58) and the walker seeing their list limit it; the record cannot tell whose hand it was.

- accept it, relying on the phone's lock and cancelling access when a phone is lost
- require the phone's unlock or a sign-in again before each time the product is opened

Recommended: accept it; asking each time slows every entry, and walks can be checked before billing.
If left: the risk stands, and nobody has accepted it.
Questions waiting on it: 1

### A160: Changing, closing and removing walks (medium)
To decide what is in or out: whether a walker can put right or remove a walk they entered, for example one entered by mistake, and until when walks for a month can be entered or changed. This is question 3 of the requirements; the slice leaves a walker's own correction and any cut-off for later.

- keep all of it out of slice 1, and the business owner allows for mistakes when typing invoices by hand
- add a walker's own correction or removal to what is built before slice 1 is used

Recommended: the first, as the slice already stands; when to close a month can be decided before invoicing.
If left: slice 1 is built with no way for a walker to put right a mistake.
Questions waiting on it: 6

### A31: How long a save may take (low)
To decide: how long a walker waits on a save before the product says it could not confirm it. After that they can send the same entry again without making a second walk.

- 15 seconds
- 30 seconds

Recommended: 15 seconds; long enough for a weak signal, short enough that a walker does not walk off thinking it saved.
If left: there is no number for giving up on a save.
Questions waiting on it: 1

### A153: How often it may fail and how slow is too slow (low)
To decide: how often walk entry may be unavailable and when it is too slow. The size to handle is asked in A9 and the wait on a save in A31.

- unavailable for no more than 4 hours in a month, with saves and lists usually within 3 seconds on a working signal
- unavailable for no more than 24 hours in a month, same speed
- a stricter promise of under 1 hour a month

Recommended: the first; walkers can note a walk and enter it later, and a stricter promise costs more to run.
If left: there is no point at which anyone would say it does not work.
Questions waiting on it: 1

## Decided by the owner

Nothing.

## To test, by harm

- A14 (high): Not known: whether the storage the product will run on keeps confirmed writes through a power loss, and whether it reports damage. No hosting or storage is chosen and no page about one has been read. Test: once storage is chosen, read its own statement on durability and damage checks, and cut a test installation off during saves, then compare confirmed walks with stored ones.
- A24 (high): Not known: whether the platform the product will be hosted on can remove its saved data on its own (inactivity, plan limits, redeploys), and what can be got back. No platform is chosen. Test: once a platform is chosen, read its own pages on data deletion, inactivity and redeploys, and redeploy a test installation to see that walks remain.

## Chosen without asking; the owner can overturn any of these

- A1: The product says a walk is saved, and lists it as saved, only after the store has confirmed it is kept. An entry that is not confirmed is shown as not saved while the entry screen is still open, with what was typed still there to send again. No entry is accepted and later discarded. Because: A walker takes a listed walk as saved and invoices will rest on it; confirming before listing leaves nothing that can be withdrawn later.
- A2: The walks list is read from the store each time it is opened. While it loads it says so; if it cannot be read it says so and offers to try again, and never shows "no walks" in its place. No older copy is shown as current. Because: An empty list and an unread list look alike, and a walker would enter the same walks twice.
- A4: The list is shown in parts, newest day first. It says when there are older walks not yet shown and lets the walker get them. A part that fails to load is reported as failed, not left out. Because: A walker checks the list to see what is recorded; a silently short list reads as missing walks.
- A5: The list is fetched when the walker opens it, after a save, when they ask for older walks and when they try again. It fetches 50 walks at a time. Nothing is fetched in the background. Because: Four walkers' lists are small; fetching on use needs no schedule and spends no phone data while the product is not in use.
- A6: Walks and clients are kept in one central store that only the running product writes, and the saved data carries a format version. A phone showing an older screen has its entry either accepted whole by the current rules or refused with a request to reload; it never writes the store directly. During an update only one version writes. Because: Keeping all writing in one place means mixed phone versions cannot damage each other's walks.
- A8: No walker has a limit on how many walks they may enter in total. Protection against a flood of requests is a separate rate limit (see the answer on repeated sending). Because: A cap on walks would stop real work from being recorded, and the volume of four walkers is small.
- A10: Whenever a limit or rule stops an entry, the walker is told which one, whether to change something or wait, and what they typed stays on the screen. Because: A refusal with no next step leaves the walk unrecorded.
- A11: An entry holds only a client chosen from a list, a day and a length. A request larger than 4 KB is refused and nothing of it is kept. Because: The three values need far less than 4 KB.
- A12: A walk is written in one all-or-nothing step, with its client, day, length and walker together. An interrupted save leaves either the whole walk or nothing, and nothing unfinished has to be completed or asked about at start. This holds for the last record written too. Because: A single transaction is the known solution to half-written records.
- A15: Any storage failure, including no space, is a failed save: the walker is told it was not saved, what they typed stays, and walks saved earlier are untouched. The product never counts a later "success" of the same failed write as proof; a retry is a new complete write, and the walk is confirmed only by reading it back as kept. The failure is recorded. Because: After a storage error the state of that write cannot be trusted; reading back what is kept is the safe check.
- A16: Every walk points to exactly one stored client and one walker, and the store refuses a walk whose client or walker does not exist. A client that has walks cannot be erased from under them. If a walk is nonetheless found without its client or walker, it is kept, reported to whoever maintains the product, and not shown as a normal walk. Because: A reference the store enforces is the known way to keep a pair together.
- A17: The store's own integrity check runs at every start and once a day. Damaged data is never repaired or overwritten automatically: the product refuses new saves, tells walkers it is unavailable and that nothing new is being saved, and records the fault for whoever maintains it. Because: Carrying on over damaged data risks wrong bills and spoils the chance of recovery.
- A18: Data brought back from damage or a spare copy is used only after it passes the integrity check and every walk has its client and walker. Whoever restores it records the moment the copy was taken and tells the business owner that walks entered after it may be missing and that later removals may be back; the owner asks the walkers to check their lists. Because: A restore silently loses recent work unless the people who know the work are told the cut-off.
- A19: Spare copies and moves are made only with the store's own consistent-copy method, never by copying files during a save. Walks, clients and walker accounts are one set, copied and restored together. The files that make it up are listed for whoever maintains the product, and the product refuses to start on a partial set. Because: The store's own copy method is the known way to get a usable copy while writes go on.
- A20: A save already sent may or may not complete if the walker closes the screen. On return the list read from the store shows what was really kept, and nothing else is shown as saved. While a save is under way the screen says it is not yet saved. Whether a save that never arrived is held on the phone and sent later follows what A3 settles. Because: Only the store knows what arrived, so the list read from it is the truth.
- A21: A first run is started on purpose, by a set-up step. At normal start, a missing store, one that cannot be opened, or one without the product's own marker makes the product refuse to start and say which of these it is. It never creates a new store over, or writes into, something it does not recognise. Because: Starting empty on a failed open would look like all walks vanished and could overwrite them.
- A22: If the data can be read but not changed, walkers can see their lists, are told that new walks cannot be saved just now, and the fault is recorded. Any needed repair waits for write access. Because: Reading does no harm, and accepting entries that cannot be kept would lose walks.
- A23: One running copy of the product changes the data at a time, held by an exclusive lock or by the store's own transactions. A second copy that would repair or upgrade waits up to 60 seconds, shows that it is waiting, then stops with that reason. The protection is not claimed for a store on shared network drives, which is not a supported set-up. Because: A single holder with a bounded wait prevents two repairs from interleaving.
- A25: A version that meets saved data marked with a later format refuses to start and says so; it neither reads part of it nor writes. Putting the previous version back is possible only while the format is unchanged; otherwise it refuses in the same way, and going back means restoring a spare copy. Because: Refusing is the only behaviour that cannot damage data an older version does not understand.
- A26: The central data is brought up to date by the running product, not by phones, so an open phone screen cannot block it. An old screen is handled as in A6: its entry is accepted whole or it is asked to reload. If A3 lets the phone hold entries, bringing those up to date is looked at again. Because: The central store of A6 is upgraded in one place.
- A27: Each part of the list is read in one consistent read of walks and their client names, so a walk is never shown half saved or without its client while others are saving. Because: A single read is the known way to get one moment's view.
- A28: Once a save is confirmed, the list on that phone includes the walk straight away. Another open screen or phone of the same walker shows it the next time its list is opened or reloaded. Because: A walker uses one list at a time; live updating adds work for no stated need.
- A29: If the store is busy or a save is cancelled by a clash, the product tries the whole save again, up to 3 tries within 5 seconds, then tells the walker it was not saved and keeps what they typed. Repeating is safe because each entry carries its own identity and can be kept only once. Because: A new walk reads nothing that a repeat could make stale, so a bounded automatic retry is safe.
- A30: Saving a walk is the one step a walker cannot take back in slice 1, so every rule about the entry is checked before the walk is kept. The business owner's correction is slice 2, and a walker putting right their own entry waits on question 3. Because: Checking everything first is the only protection where there is no way back; slice-001/004_slice.md leaves both kinds of correction for later.
- A32: An entry that was started and not sent is not kept anywhere. It lasts only as long as the screen it is typed on, so nothing has to remove it. Because: Three values are quick to enter again, and drafts would need their own rules for expiry and privacy.
- A33: Client, day and length are all required. The client is picked from the clients offered, never typed as free text; text typed to search is only used to search, takes any character, stops at 100 characters, and spaces around it are ignored. The day is picked as a calendar date. The length is a whole number of minutes from 1 to 1440. An empty or all-spaces value counts as missing. Client names are shown whole as stored, not split into parts. Because: The thin path gives client, day and length; picking rather than typing means no unknown client can be named, and 1440 minutes is one day.
- A34: Every rule about an entry is checked again by the product before the walk is kept; the screen's check is only a convenience. A request that breaks a rule is refused whole. Because: Anything sent from a phone can be sent without the screen.
- A35: A missing client gives a message that a client is needed (walker-walk-entry / 2). Every other refusal names the value and what is accepted. Each message appears next to the value it is about, and one about the whole save appears by the save button. Because: A message beside its field is found without hunting on a small screen.
- A36: A client is identified by the product's own identifier, not by name, so a walk always means one client. Where two offered clients have names that look the same once capitals and spacing are ignored, the choice shows a further label that tells them apart and is never an address or door code. Entering walks adds no client and changes no name. Because: Two real clients can share a name, and the limit on addresses and door codes rules them out as labels where others could see them.
- A37: Client names and search text are always passed to the store as values and shown as plain text, never run or read as markup or commands. Names are shown isolated from the text around them, so right-to-left text cannot disturb a row or message. Because: Separating values from code and escaping on output is the known solution.
- A39: The day is chosen with a date picker, so no written date form is typed or guessed at. The length is typed as digits only, meaning minutes; signs, decimals, separators and units are refused, not interpreted. Because: Removing free forms removes ambiguity.
- A40: As soon as save is pressed the screen shows that it is saving and will not send again while waiting. Each entry carries its own identity from the moment the screen is opened, so sending it again, by a second press, a retry or a reload, adds no second walk and returns the one already kept. Because: An identity per entry is the known way to make repeat sending safe.
- A41: After a save the walker lands on the list. Reloading it only reads it again. Stepping back reaches a fresh entry screen, never the sent entry ready to send again. Because: Redirecting after a save is the known way to stop repeats by reload or back.
- A42: After sign-out or the end of access, no screen, including one reached by stepping back, shows walks or client names. Pages with them are marked not to be stored. A saved address to any screen leads a signed-out person to sign-in; an address to something that is gone, or not theirs, says only that it is not available. Because: Client details are limited to the business owner and that client's walker; a phone can be passed to someone else.
- A43: A walk is saved only when the walker presses save and it is confirmed. Typing on which save was not pressed is not kept (what happens to a pressed save with no signal follows A3): backing out, leaving or the phone discarding the screen adds nothing, and on return a discarded screen is a fresh, empty entry. The list always shows what was really kept. There are no other steps to back out of. Because: One explicit save is plain to the walker, and keeping no draft leaves nothing to expose.
- A44: Each window shows a change made elsewhere when it next loads. Entries from two windows are separate entries and both are kept under the same rules; slice 1 changes no walk, so neither can overwrite the other. Because: Adding only means there is no winner to choose.
- A46: Saving asks for no second confirmation. The client, day and length are all visible together beside the save button, and after saving the new walk is shown so a mistake is noticed. Because: A question asked on every walk is soon tapped through unread.
- A47: If access has ended when the walker saves, nothing is kept and they are asked to sign in. After the same walker signs in again on that open screen, what they typed is still there to send. If someone else signs in, it is discarded. Because: Work should survive a sign-in without ever passing to another person.
- A48: While saving, the screen shows a moving or worded "saving, not yet saved" sign. It ends in one of: saved; refused, with why; or not confirmed, after the wait the owner decides (A31) with no reply, which is also when a save counts as stuck. An interrupted save is not resumed by itself: the walker sends the same entry again, which cannot double it. A failure the walker did not see is recorded for whoever maintains the product; the walker learns of it by the walk's absence from their list. Because: The list read from the store is the one reliable account of what was kept. Resuming by hand is written for A3's first option.
- A49: The walk's day is the day the walker picks. The product's own clock decides when a walk was recorded, when access ends and what "today" is; the phone's clock only suggests a starting day, which the walker sees and can change. No difference between clocks needs tolerating because the phone's time is never trusted. Waits are measured on a clock that only moves forward, so setting the time back or forward does not change them. Because: A phone's clock can be wrong or changed by its holder.
- A50: A walk's day is stored and shown as a calendar date with no time or zone, so it never shifts. "Today" is judged in the business's one time zone, set for the installation, wherever a phone is. Times of recording are stored as one universal time and are never shown as the walk's day. Because: The business works in one place, and a plain date is the known way to stop days shifting.
- A51: Walks are ordered by their day, newest first, then by when the product recorded them, newest first, then by the walk's identifier. The order is the same across every part of a long list, and the walker cannot reorder it in this slice. The recorded time only breaks ties. Because: A final unique key gives one order even when times are equal.
- A52: Stored names are kept as written and not changed by this slice. For search and look-alike checks, names are put in one Unicode form, unseen characters are removed, unusual and repeated spaces count as one space, and capitals are ignored by locale-independent rules. Search also ignores accent marks. A list of clients is ordered by the whole stored name, by English rules for every reader, with the identifier as the tie-break. Names are not split to order by a family name. Because: These are the standard rules for matching names; the documents are in English and one fixed order suits a small team.
- A53: A client's name is not cut where the walker is choosing or reading a walk: it wraps onto more lines, counted by what a reader sees as characters. Names that match once compared as in A52 get the further label of A36. Names that only look alike through different alphabets are not detected, which is acceptable because walkers cannot add or rename clients. Because: Cutting a name can make two clients look the same.
- A54: The product is in English only. Labels and messages wrap and are never cut off or placed over a control, so longer or larger text pushes the layout down. Because: The documents are in English and name no other language.
- A55: A day is shown with weekday, day number, month name and year, such as "Tue 3 November 2026", in the Gregorian calendar, with Western digits. A length is shown as whole minutes with its unit in words, such as "45 minutes" or "1 minute"; there are no decimals or rounding. A count of walks uses its own wording for none, one and more than one. The date picker starts the week on Monday and marks no rest days. These rules are the same for every reader. Because: A month name cannot be read as another day, and walks are entered in whole minutes.
- A57: Whatever way A56 settles, every walker's access is their own and none is shared, so a leak is traced to one account. Only what is needed to check a credential is stored, in a form it cannot be read back from (a slow salted hash for a password, only the public part for a passkey, only a hash for a link or session value). Everything is sent over encrypted connections, session values are held in cookies scripts cannot read, and no credential or session value is written to any record. If one is found in a record it is removed and the access it gives is cancelled. Because: These are the standard ways to hold credentials.
- A58: Walkers' access is not replaced on a schedule. For a lost phone or an exposed credential, the business owner, or whoever maintains the product for them until the owner has a screen for it, cancels that walker's sessions and credential; the cancellation takes effect on the next request. Only that walker is stopped, until given new access. A refused credential or session leads to sign-in with a message that they need to sign in again or ask the business owner. Because: Replacing on a schedule adds lockouts without a known gain; cancelling at once is what limits a loss.
- A59: Any credential the running product needs, such as for its store, is made per installation, given only the rights the product needs to read and add its own data, with upgrades using a separate one. It reaches the product from the host's protected settings, never from the code, an address, a command line or a record. If it cannot be read the product refuses to start and says which one is missing, never showing its value. A lost one is replaced by making a new one; none is the only way to the data. Because: Least privilege and secrets kept outside the code are standard practice, whatever host is chosen.
- A61: In slice 1 a signed-in walker may add a walk under their own name for a client they are allowed (A60) and may read their own walks. Nobody changes or removes a walk through slice 1. No walker sees another's walks. The business owner's correction is slice 2. The product checks this for every operation where the data is read or written. Anything no rule allows is refused, including any address or operation not listed and any request with no sign-in. Because: Deny unless allowed is standard practice, and walks show which clients are walked.
- A62: Every read of walks is limited to the signed-in walker's own, by the walker the product knows from the session, not by anything the request says. Asking for another's walk is answered as if it did not exist. Every permission is checked by the product itself, so a request sent without the screen meets the same checks. Because: Filtering by the session's walker is the known way to stop one person reading another's records.
- A63: Who the walker is and what they may do come only from the session the product holds. The phone sends the client, day, length and the entry's identity, and none of these is trusted without checking. A walker or any other field named in the request that a walker may not set is refused. The session value is random and cannot be guessed or altered into another's. Because: Anything on the phone can be altered.
- A64: Only a deliberate save request changes anything; following a link or loading a page never does. A save is accepted only with the product's own origin and its protection against forged requests, and the session cookie is not sent with other sites' requests that change things. Because: These are the standard defences against forged requests.
- A65: If the product cannot complete the check, the request is refused: nothing is shown or kept, the walker is told to try again, and the failure is recorded. Because: Failing closed is standard practice.
- A66: When a walker leaves, the business owner (or the maintainer for them, as in A58) cancels their access; when a walker stops having a client, that client stops being offered to them under the rule A60 settles. Sign-out, cancellation and a change of rights apply from the very next request, including from screens already open. What is already drawn on an open screen cannot be taken back until it next asks for anything or is reopened. Walks already entered stay recorded under the walker who entered them. Because: Checking each request against the current rights is what makes removal take effect.
- A67: Signing in always starts a new session and ends the one the screen held; a one-time link used while someone else is signed in does not silently switch or merge accounts but signs them out first and says whose access is being set up. Every screen of a signed-in walker shows their name. Because: A new session at each sign-in and a visible name stop walks being entered under the wrong person.
- A68: Each sign-in, failed sign-in, sign-out, issue and cancellation of access is recorded with the account and time, without any credential. The maintainer looks at it when something is reported or an alert is raised (A80). Use of the product's own credentials is whatever the host records. Because: This is what is needed to trace misuse of an account.
- A69: Every required setting (where the data is, the business's time zone, the product's own address, its credentials, and whether this is a trial) is checked at start for presence and sense: the time zone must be a known one, the address an encrypted one, numbers within stated ranges. A missing or senseless value stops the start with the setting's name, and no secret value is shown. Because: Failing at start is better than failing on a walker's save.
- A70: Where a default exists it is the safe one: diagnostics off, sign-in required, encrypted connections required. Settings with no safe default, such as the data's location and credentials, have none and must be set. A fresh installation turns on only sign-in, walk entry and the walker's list, with no default account or password and no public sign-up. Because: Safe if nothing is changed is standard practice.
- A71: The two differ only in their data location, address, credentials and trial mark, each set in that installation's protected settings; anything else that differs is written down with its reason. A trial uses invented data and says on every screen that it is a trial. It cannot be started against the real installation's data. Because: A trial that can touch real data or look real causes lost or false walks.
- A72: Only whoever maintains the product can change settings, through the host's protected settings; nothing a walker or request sends can change one. The maintainer owns every setting. They can see in one place every setting in use and where it came from, with secrets hidden. Each change is noted with who, when, what and why; it is tried on the trial installation first, then applied to the one real installation and checked by saving and reading a test walk by a test account. The previous value is kept, and going back is applying it and restarting. Because: One owner, a record and a trial first are standard for a small installation.
- A73: The only diagnostic is more detailed records, which still never hold client names or credentials. No debugging screen or detailed error page exists on the real installation, and it refuses to start with one switched on. Because: Debug output is a common way details leak.
- A74: A record is made of every walk saved, every save refused or failed, refused permissions, access events (A68), starts and stops, storage and integrity faults, and restores. Each says when, what happened, the outcome, which account, and the identifiers of the walk and client concerned, plus the reason for a refusal. Because: This is what settles later disputes about what was entered, by whom and when.
- A75: Client names, addresses, door codes, search text and credentials never go into records; identifiers are used instead. Records are built from named fields, not from raw requests. Any outside text that must be recorded is stored as an escaped, length-limited value that cannot start a new entry. Because: Records are read by people the client-details limit does not name.
- A76: The walker sees plainly that the walk was not saved or not confirmed and what to do next, with a short reference. Technical detail goes only into records under the same reference. Because: Error detail helps an attacker and not a walker.
- A77: The record of a saved walk is kept with the walk in the same all-or-nothing write, so a walk is never kept without it. Failing to write other, running records does not stop walkers; the product raises an alert. Running records are capped in size, the oldest rotated out first, with an alert at 80 per cent; the walk records are kept with the data and are not rotated for space. Because: The record of who entered a walk matters as much as the walk, and running logs should not stop the work.
- A78: Walk records are part of the saved data and its spare copies. Running records are also sent to a place separate from the machine that writes them. The product offers no way to edit or remove a record; only the maintainer can reach them, and walk records are chained so a changed or removed one shows in a daily check. Because: Add-only records with a check are the known way to notice tampering.
- A79: Every record's time comes from the product's clock, in universal time, with a running number to order entries made at the same moment. A phone's time is not used. Because: One clock gives one order.
- A80: The maintainer reads records. They are alerted to integrity or storage faults, a failed start, a record that cannot be written or was altered, repeated failed sign-ins and the request limits being reached. Because: Unwatched faults go unnoticed until invoicing.
- A82: Everything on the entry screen, including choosing a client and a day and saving, works by keyboard alone using standard controls; every chooser can be left with Escape or by moving on, so focus is never trapped. Focus is always shown by a clearly visible outline. When a chooser or message closes, focus goes back to the control that opened it, or to the next sensible one. Because: Standard accessibility practice (WCAG 2.2 level AA, taken as the working standard and not as a statement of legal duty).
- A83: Each control has a visible label that is also its announced name, with its purpose and state. Results (saving, saved, refused, not confirmed) are announced without the walker having to look for them, and a refusal moves them to the value at fault. Anything that is not text has words with the same meaning, and colour is never the only signal. Because: Standard accessibility practice (WCAG 2.2 level AA).
- A84: In every state and theme, text has at least 4.5 to 1 contrast (3 to 1 for large text and for the outlines of controls and focus). At twice the text size nothing is cut off, overlapped or reachable only by scrolling sideways. Only the saving sign may move, it has words too, and it stays still for a walker who asked for less motion. Because: Standard accessibility practice (WCAG 2.2 level AA).
- A85: Filling in an entry has no time limit. If the session has ended by the time of saving, A47 applies. The wait for a reply to a save (A31) is not a limit on the person. Because: Nothing in the slice needs a walker to hurry.
- A86: Whatever way A56 settles, one-time links and codes are long or short-lived and work once. After 5 failed attempts in 15 minutes for one account or from one address, further attempts are refused for 15 minutes; the message says to wait or ask the business owner. A used or expired link or code is refused. Because: Rate limits and single use are the standard defence against guessing and replay.
- A87: No account exists until the business owner asks for one for a named walker; there are no default or shared accounts, and any set-up or test account is removed or disabled before real use. First access is a random one-time link or code that ends after 24 hours or on first use, handed by the business owner to that walker, and a newer one ends the older. Lost access is recovered the same way, after the old access is cancelled, so recovery is no weaker than first access. There is exactly one ordinary way to sign in, the one A56 settles, and no side door. Because: The business owner knows each walker, which makes issuing by them the strong and simple route.
- A88: Sign-in and recovery give the same reply whether or not the person has an account. Because: It costs nothing and avoids telling outsiders who walks for the business.
- A89: Slice 1 has no outside way to send messages. A walker is told at their next sign-in when their access was last set up or changed and when a new device was added. Failed attempts that reach the limit alert the maintainer (A80). The business owner is the one who makes changes, so they know of them first. Because: Telling the person in the product needs no outside service.
- A90: A session ends after 30 days unused and after 90 days in all. An account may have 3 sessions at once; starting a fourth ends the least recently used. Adding a new sign-in or changing how one signs in asks the walker to prove who they are again; entering a walk does not. A walker can see their sessions and end them, and the maintainer can do the same for any account, for the business owner when asked. Because: A walker uses their own phone daily, the data shown is limited to their own clients, and a lost phone is handled by ending its session.
- A91: Client names, which walker walks which client and on which days, and credentials are sensitive: seen only by those allowed, encrypted on the way and wherever stored, spare copies and running records included. Walk entries also drive billing, so changing them is as serious as seeing them. Addresses and door codes are the most sensitive; slice 1 neither asks for, keeps nor shows them. Only the product and the maintainer can reach the stored data and its copies, and the maintainer's access is by their own named account. Because: The limit on addresses and door codes, and the harm named in security.md for client details and walks.
- A92: Stored data and spare copies are encrypted with keys kept apart from them: one for the live store, another for spare copies, used for nothing else. They are held in protected key storage reached only by the product or the maintainer as needed. A recovery copy of the spare-copy key is kept separately by the maintainer. A lost key makes what only it protects unreadable, so losing the live key means restoring from a copy. An exposed key is replaced and the data encrypted again, and old copies under it are removed once newer ones exist and have been restored once. Because: Separate keys held apart from the data are standard practice.
- A93: Client names, search text, the chosen client and credentials are never put in a web address, apart from a one-time sign-in link's own token, which works once, is removed from the address as soon as it is used and is kept out of records. Replies with client or walk details are marked so that neither the phone nor anything between stores them. Because: Addresses and stored replies are common places for details to leak.
- A94: No other party is given data in slice 1: no analytics, advertising, error-reporting or outside content on the pages. Whoever hosts the product holds it in order to run it. Nothing goes to Tallypay in this slice. Because: slice-001/004_slice.md says the slice needs nothing from outside.
- A95: The client choice sends only each offered client's identifier, name and any telling-apart label. The list sends only the walker's own walks: identifier, day, length and client name. No address, door code, price or contact detail is sent. The list and client names are not stored on the phone; the session cookie is. Whether unsent entries are stored there follows A3. Because: Sending and storing less leaves less to lose.
- A97: Each time the client choice or a walks list is fetched, a record keeps the account, time and which was fetched, with no names. The maintainer looks at it when something is reported. Because: It lets a complaint about who saw client details be looked into without copying the details.
- A98: A walk must have the signed-in walker, a client that walker is allowed (A60), a day allowed by the rule A38 settles, a length of 1 to 1440 whole minutes (A33) and its own entry identity. All of them are checked by the product where the walk is kept, and the unchangeable ones by the store too. Because: walker-walk-entry / 1 and 2 give the values; one place of enforcement cannot be bypassed from a phone.
- A99: Each account may send 30 save requests and 60 list or client-choice requests in 60 seconds, then is refused for 60 seconds and told to wait. Reaching a limit is recorded and alerts the maintainer, but no account is locked or walk removed by itself. A list fetch returns at most 50 walks, so one walker's use cannot grow without bound. Many walks entered quickly can be honest catching up, so speed below the limit is not treated as abuse. Because: These are far above what a person entering walks does and still stop a script from flooding.
- A100: Entering a walk needs no one else's agreement in slice 1; nothing is billed from it by the product yet, and each walk is recorded against its walker. Whether the business owner checks invoices before clients get them is question 4 of the requirements. Because: An approval for every walk would add back the work the product is meant to remove.
- A101: A save may carry only the client, day, length, the entry's identity and the protection against forged requests. A request carrying any other field, such as a walker, a recorded time or a price, is refused whole. Because: Accepting only listed fields is the known way to stop extra values being set.
- A103: A client value that is malformed, too long, in odd characters, names no client, names one since removed, or one this walker is not allowed, is refused. The walker is told that client cannot be chosen and to pick from the list again; the reply does not say whether such a client exists. Because: One reply for all of these gives nothing away.
- A104: Whether a client is allowed is judged at the moment the walk is saved, not when the screen was opened. If the walker lost the client in between, the save is refused as in A103; if they still have it, it is accepted. Because: The current rights are the ones that protect the client.
- A105: A day that is empty, absent, malformed or not a real calendar date, such as 30 February, is refused; the walker is told a real day is needed and what they typed stays. Because: A walk without a real day cannot be put in a month.
- A107: A length that is empty, absent, of the wrong type or not whole digits is refused; the walker is told the length is needed as a whole number of minutes from 1 to 1440. Because: A33 and A39 set what is accepted.
- A108: A request whose session is empty, absent, malformed, or points to a session or account that no longer exists is treated as signed out: nothing is shown or kept, sign-in is asked for, and the refusal is recorded without the value. Because: Anything short of a valid session is no identity.
- A109: One walker on several devices is the same walker with separate sessions, within the limit of A90. Two accounts can never share an identifier or sign-in: setting up a second one with the same is refused, and walkers with the same name remain separate accounts. Because: The store enforces unique account identifiers.
- A110: A client with an empty or missing name is a data fault: it is not offered for new walks, a walk already pointing to it is listed as "name unavailable" with its day and length, and the maintainer is told. A very long name is shown in full, wrapped (A53); the store limits a name to 200 characters. Because: A walk must not disappear because a name is faulty, and a blank choice cannot be picked safely.
- A111: When two clients' names match, the list and the choice show the further label of A36 for each. Because: The walker has to tell which client a walk is for.
- A112: A stored walk whose client reference is empty, missing, malformed, out of range, too long, oddly encoded or pointing to no client is a data fault: it is kept unchanged, shown to its walker as "client unavailable" with its day and length, never guessed or reassigned, and reported to the maintainer. The edge of what is allowed is a client the walker has since lost: see the answer on lost clients. Because: Hiding or repairing by guess would lose a walk or bill the wrong client.
- A115: A stored day that is empty, missing or not a real date is a data fault: the walk is kept unchanged, shown apart at the top of the list as "day unavailable", and reported to the maintainer. Because: A faulty walk must be noticed, not hidden or given a guessed day.
- A116: A walk already kept with a real date is shown with that date, including one on the boundary or outside what may be entered today, for example after the rule has changed. It is not altered or hidden. A day outside what the product can show at all is a data fault as in A115. Because: The entry rule governs new entries; changing or hiding a kept walk would lose a record.
- A117: A stored length that is empty, missing, not a whole number or outside 1 to 1440 is a data fault: the walk is kept unchanged, listed with "length unavailable", and reported to the maintainer. Because: A guessed length would be billed.
- A118: Stored lengths of 1 and 1440 minutes are valid and shown as "1 minute" and "1440 minutes". Because: A33 sets the range and A55 the wording.
- A119: No client name or client search text reaches logs, an error's own message or trace, or anything sent to monitoring, whether the work succeeds or fails. Errors carry identifiers only, and values from requests and the store are not copied into error text or traces. Because: Logs, traces and monitoring are read by people the client-details limit does not name.
- A120: An error returned to anyone carries no client name or other client detail. A successful reply carries names only of clients the signed-in walker may see (A60, and A113 for past walks), only as A95 lists. Because: The limit on who sees client details; a failure must not show more than success.
- A121: Test data and examples kept with the code are invented, such as "Example Client A". No real client, address or door code is copied there or into a trial. Because: Code is copied and shared beyond those who may see client details.
- A122: They are stored only in the product's store, its spare copies and, as identifiers only, its records, protected as in A91 and A92. They are not written to temporary exports or files for fault-finding. What, if anything, the phone holds for unsent entries follows A3. Because: Fewer copies are fewer places to protect.
- A125: Pressing save again at once adds nothing more (A40). Reloading or reopening before the save was sent gives a fresh empty entry; after it was sent, the list shows whether the walk was kept. Entries open on two devices are separate entries, each kept if it passes the rules, subject to what A114 settles. An entry left for a long time is not kept anywhere else; saving it later runs every check again, including whether the session and the client are still allowed. Because: Nothing exists in the store until a save is accepted.
- A126: Entering another walk adds it beside the saved one and changes nothing in it. Another walk for the same client on the same day follows what A114 settles. An attempt with no client is refused as in walker-walk-entry / 2 and the saved walks stay listed. Because: Slice 1 only adds walks.
- A127: Sending the same entry again, or reloading or reopening, leaves one saved walk (A40, A41). It survives a restart of the product. Another device of the same walker shows it when its list is next loaded, and no other walker sees it. Time passing does not change it in slice 1; how long it is kept is what A96 settles. Because: Slice 1 gives no way to change or remove a walk.
- A136: Entering walks never changes a client. Entering for the same client again follows A40 for the same entry and A114 for a new one. Reloading, reopening or a restart leaves the client as it was and offers it again to those allowed. Two walkers allowed the same client may save at once and both walks are kept under their own walker. Time passing alone changes nothing about the client in slice 1. Because: Slice 1 only reads clients.
- A137: Slice 1 has no screen that changes a client, but the stored name may be corrected by whoever loads clients. A walk stays with the same client by its identifier, and lists and choices show the current name the next time they load. An entry open during the change is saved for the client chosen; one with no client is still refused. Repeating, reloading, a restart, a second device or the passing of time causes no further change. Because: The identifier, not the name, says which client is meant (A36).
- A139: An entry with no client is refused as ever. Walks already saved for a former client are kept and are not removed by the client leaving, whether after repeating, reloading, a restart, an action from a second device or the passing of time; what a walker sees of them follows A113, and how long they are kept follows A96. Whether a new walk is accepted is what A138 settles, judged when it is saved. Because: Walks done are the record behind billing.
- A140: Data replies are sent with their true type and a header forbidding the browser to guess another, and the slice accepts no files. A content policy lets the page load and run code and styles only from the product's own address, with no inline script, and blocks everything else. No other site may frame it. No code or styles come from another party's address; components are shipped with the product. The page takes no messages from other windows. Because: These are the standard browser protections.
- A141: Other sites are told nothing of the address a person came from. No other site's page may call the product and read replies. The product never sends a person on to an address someone else supplied. Pages with client details are marked not to be stored. A walker is known only by a session cookie sent over encrypted connections, unreadable by scripts, tied to the product's own host and not sent with other sites' requests that change things. Because: These are the standard settings for a signed-in site.
- A142: The product answers only to its own configured host name and refuses others. All connections are encrypted; an unencrypted one is redirected before anything is served and the browser is told to use only encryption, and a save sent unencrypted is refused. A sender's address or host is believed only from the known component in front of the product, never from what the sender supplies. Each address accepts only its own kinds of request and refuses others. No diagnostic page, file listing, source history, documentation or measurement page or test code is reachable, and refusals do not name what the product is built from. Because: These are the standard network protections.
- A143: The exact version of every component, including those they bring, is locked in a list with its source and content check, and is fetched only from the named source. An automated check for known flaws runs on every change and daily and alerts the maintainer; a serious flaw that applies is fixed within 7 days and others within 30. Few components are used, those that see credentials, read outside data or run at install are listed and reviewed, install scripts are off unless needed, and the running product has only the rights it needs. Because: Standard practice for third-party code.
- A144: A walker sets only the client, day, length and entry identity, and sees of a record only what A95 lists; other fields, such as who recorded it and when, are not theirs to set. The product serves one business, so there is no other group whose data could be shown. Because: 000_problem.md describes one business with four walkers.
- A145: One-time links and codes, session values and protection against forged requests are made by the system's secure random generator with at least 128 bits; a code a person types may be shorter only with the single use, short life and attempt limits of A86 and A87. Identifiers of walks and clients are random too, but nothing relies on that: every access is checked. Because: Secure randomness is the standard solution.
- A146: The list and the client choice are limited by the session's walker (A60, A62), and carry only what A95 lists. Sessions end and can be cancelled (A58, A90). Someone trying shows as refused permissions, failed sign-ins and limits reached in the records, and repeated ones alert the maintainer. Use of a stolen but valid session looks like the walker; it shows only in the record of fetches and sign-ins. Because: security.md, client-details through walks-list, entry-screen and walker-access.
- A147: Encryption on every connection (A142) stops reading and altering on the way; the browser refuses an unencrypted or wrongly identified connection to the product once told to use only encryption. An attempt on the path may not be visible to the product; refused connections show in the host's records where it keeps them. Because: security.md, client-details through save-request; encrypted connections are the known solution.
- A148: The data, copies and records are encrypted, reachable only by the product and the maintainer through named accounts with a second factor, with least rights (A59, A91, A92). Client names stay out of records. Changes and removals of walks show against the chained walk records and daily check (A78), and lost data is restored from spare copies as far as A13 allows. Access to the host is recorded where the host does so, and integrity faults alert the maintainer. Someone with the maintainer's full access could defeat these checks. Because: security.md, client-details and walk through installation.
- A149: Only a signed-in walker can add walks, only for allowed clients, under their own name, with forged requests refused, one walk per entry and a rate limit (A40, A62, A64, A99). Each walk is recorded with account and time, so odd ones can be traced; the walker sees them in their list. A walker can still deliberately enter a walk that never happened, which the product cannot tell apart; until invoicing is built the business owner bills by hand. Because: security.md, walk through save-request.
- A150: The walker of a walk comes only from the session (A63), access is individual and never shared (A57), guessing is limited (A86), and a walker is told of new sign-ins and devices (A89) and can end sessions. The record keeps account, time and session for each walk, which shows which access was used, not whose hand used it. Because: security.md, walk through walker-access.
- A152: Walkers cannot save walks or see their lists, and are told so when the product can still answer. They note walks and enter them afterwards for the day they happened, subject to the days A38 allows. Nothing already confirmed is lost by the outage itself. Because: The day of a walk is separate from when it is entered (A49).
- A154: A check from outside the machine tries the product every 5 minutes and tells the maintainer after 2 failures in a row. The alerts of A80 also reach them. Walkers can tell the business owner. Because: A fault should not wait for invoicing day to be found.
- A155: The slice touches client names, which walker walks whom and on which days, walkers' credentials and the walks that will drive bills. Four walkers use it; none may see or change what is another's. What the business owner sees in the product starts with slice 2. Because: security.md names client-details and walk as what someone would want; 002_requirements.md limits addresses and door codes to the business owner and the walker for that client.
- A157: Client details, to learn who is walked and when, and the walks, to add false ones, repeat them, blame another walker, or change and destroy them. Each way in that security.md lists is answered above. Because: security.md, What someone who means harm would want.
- A158: Before saving, a walk is only what is typed on the screen. After pressing save it is shown as saving and not yet saved, and it ends as saved and listed, refused with why, or not confirmed (A48). Leaving the screen is always a way out. Because: A1, A43 and A48 together leave no state in which a walker cannot tell what to do.
