# Answers: slice 1

## A1: Recording a phoned absence for a singer in the register
Kind: fact
Says: A section leader records it for a singer in the register on a coming rehearsal, and is shown who is recorded as missing which date.
Rests on: record-for-singer / 1
Settles: S.singer-in-the-register.in-register.record-for-singer-1, S.rehearsal.coming-up.record-for-singer-1
Under: record-for-singer

## A2: A name the register does not have
Kind: fact
Says: The section leader is told there is no such singer, and no absence is shown for that name.
Rests on: record-for-singer / 2
Settles: S.singer-in-the-register.not-in-register.record-for-singer-1, S.singer-in-the-register.not-in-register.record-for-singer-2, S.rehearsal.coming-up.record-for-singer-2
Under: record-for-singer

## A3: A date that does not exist
Kind: fact
Says: The section leader is told there is no such date, and no absence is recorded. The message appears where the result of recording appears.
Rests on: record-for-singer / 3
Settles: S.singer-in-the-register.in-register.record-for-singer-3, S.rehearsal.coming-up.record-for-singer-3, L.user-input-06.record-for-singer-3
Under: record-for-singer

## A4: Who is shown as missing a coming rehearsal
Kind: fact
Says: Those recorded as missing that date are shown, and a singer recorded only for another date is not.
Rests on: see-who-missing / 1
Settles: S.singer-in-the-register.in-register.see-who-missing-1, S.rehearsal.coming-up.see-who-missing-1, S.absence.recorded.see-who-missing-1
Under: see-who-missing

## A5: A coming rehearsal with no absence recorded
Kind: fact
Says: The person looking is told that no absence is recorded for it.
Rests on: see-who-missing / 2
Settles: S.singer-in-the-register.in-register.see-who-missing-2, S.rehearsal.coming-up.see-who-missing-2, S.absence.recorded.see-who-missing-2
Under: see-who-missing

## A6: What each refusal says
Kind: chosen
Says: Every refusal appears where the result of recording appears, names what was wrong and says what to do next: unknown name (check the spelling against the register), no such date or unreadable date (the accepted form), not a Thursday, a date that has passed, a missing value (which one). When both the name and the date are wrong, both are named. A refusal records nothing and leaves existing absences as they were. Trying the same thing again gets the same refusal.
Rests on: a refusal that says what to do next lets the section leader finish the call
Settles: L.user-input-06.refusal-message, L.user-input-02.record-request, S.singer-in-the-register.not-in-register.record-for-singer-3, S.singer-in-the-register.not-in-register.again, S.singer-in-the-register.in-register.record-for-singer-2, S.absence.recorded.record-for-singer-2, S.absence.recorded.record-for-singer-3, S.absence.recorded-after-tuesday.record-for-singer-2, S.absence.recorded-after-tuesday.record-for-singer-3, S.rehearsal.took-place.record-for-singer-2, S.rehearsal.took-place.record-for-singer-3, S.absence.rehearsal-passed.record-for-singer-2, S.absence.rehearsal-passed.record-for-singer-3, V.singer-name.missing, V.rehearsal-date.missing, V.rehearsal-date.empty
Under: record-for-singer
Criterion: Given no singer's name has been given, when a section leader tries to record an absence, then they are told the name is needed.
Criterion: Given no date has been given, when a section leader tries to record an absence, then they are told the date is needed.
Criterion: Given no date has been given, when whoever arranges the programme tries to look at a rehearsal, then they are told the date is needed.

## A7: Typed names
Kind: chosen
Says: A name is typed as one value, as the register has it. Spaces at either end are removed, runs of spaces and unusual spaces count as one ordinary space, differently encoded forms of the same letter count as the same, and capital letters are ignored, by rules that do not depend on the computer's language setting. This is applied at each comparison, and the saved register is not rewritten for it. Unseen control characters are refused. Any letters and punctuation are accepted. A name of only spaces counts as missing. A name with parts missing, added or reordered does not match and is treated as unknown. A typed name over 200 characters is refused as too long, and a name is never cut where it is shown.
Rests on: a small difference in typing should not hide a singer, and a loose match could record the wrong one
Settles: L.user-input-01.singer-name, L.user-input-03.singer-name, L.user-input-04.singer-name, L.user-input-07.singer-name, L.text-01.singer-name, L.text-02.singer-name, L.text-03.singer-name, L.text-05.singer-name
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader records an absence typing "  robin   VALE " for a coming Thursday, then Robin Vale is shown as recorded.
Criterion: Given Robin Vale is the only singer with that surname, when a section leader tries to record an absence typing only "Vale", then they are told there is no such singer.
Criterion: Given the register is available, when a section leader gives a name of 201 characters, then they are told it is too long.

## A8: Typed text is only ever text
Kind: chosen
Says: Wherever a name is shown, saved or passed on, it is treated as plain text and never as a command, markup, a file path or a screen control sequence. Where it sits in a sentence or row, its direction is isolated so it cannot rearrange the text around it. Saved names are shown the same way as typed ones.
Rests on: treating input as data is the known way to stop it being acted on
Settles: L.user-input-10.singer-name, L.text-09.singer-name
Under: record-for-singer
Criterion: Given a typed name contains markup or screen control characters, when it is shown back in a refusal, then nothing in it changes how the screen behaves.

## A9: Two singers who look alike
Kind: chosen
Says: Nothing is recorded on a guess. If a typed name matches more than one singer, each match is shown with their voice part and the section leader picks one. Names that merely look similar are different names, and the confirmation shows the name and voice part as the register has them.
Rests on: recording the wrong singer cannot be put right in this slice
Settles: L.text-10.singer-name
Under: record-for-singer
Criterion: Given two singers in different voice parts have the same name, when a section leader enters that name for a coming Thursday, then they are asked which of the two is meant before anything is recorded.

## A10: Whether the register can hold two singers who cannot be told apart
Kind: test
Says: The documents do not say whether the register allows two singers with the same name and voice part, or the same singer saved twice, or what else could tell them apart.
Rests on: no document describes what makes a singer unique in the register
Test: In a copy of the register with invented names, try adding the same name and voice part twice, and look at what is saved that tells the two apart.
Harm: medium
Settles: L.user-input-09.singer-name, V.saved-singers.twice
Under: record-for-singer

## A11: Dates, as typed and as shown
Kind: chosen
Says: A date is accepted as year-month-day (2027-01-14) or as day, month name and year (14 January 2027). All-number day and month forms such as 01/02/2027 are refused as unclear. Dates are shown as weekday, day, month name and year, with Western digits, in the Gregorian calendar. A rehearsal date is a plain date with no clock time or time zone, saved and compared as that. "Today" is the date on the hall computer's clock, which is the hall's local date.
Rests on: a month written as a word cannot be mistaken for a day, and a plain date cannot shift between zones
Settles: L.user-input-12.rehearsal-date, L.time-07.rehearsal-date, L.time-08.rehearsal-date, L.presentation-01.rehearsal-date, L.presentation-06.rehearsal-date, L.presentation-09.rehearsal-date, V.rehearsal-date.malformed
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader enters 01/02/2027 as the date, then they are told the form is unclear and shown a form that is accepted.
Criterion: Given Robin Vale is in the register, when a section leader records an absence for them on 2027-01-14, then the date is shown as Thursday 14 January 2027.

## A12: Which dates can take an absence
Kind: chosen
Says: Only a Thursday that is not in the past takes an absence. Another weekday and a past date are refused. Any later Thursday is allowed, however far off, and is shown in full so that a mistyped year can be seen. The product works out Thursdays from the calendar and keeps no list of rehearsals. Whether the singer is known and whether the date is allowed are both checked. The rehearsal day itself is part of the owner's question on late word.
Rests on: the thin path covers a coming Thursday rehearsal, and extra rehearsals and Thursdays without one are left to slice 8
Settles: L.user-input-11.record-request, L.time-10.rehearsal, L.misuse-02.record-request, V.rehearsal-date.outside, S.rehearsal.took-place.record-for-singer-1, S.absence.rehearsal-passed.record-for-singer-1
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader tries to record an absence for them on a coming Friday, then they are told it is not a Thursday rehearsal and nothing is recorded.
Criterion: Given Robin Vale is in the register, when a section leader tries to record an absence for them on a Thursday before today, then they are told that rehearsal has passed and nothing is recorded.

## A13: Until when word can be recorded
Kind: owner
Says: What happens to a phoned absence recorded after Tuesday evening, up to and including the rehearsal day, until slice 6 settles late word.
Rests on: the slice leaves word after Tuesday evening to slice 6, and no document says whether recording it is refused meanwhile
Options: accept it up to the end of the rehearsal day and show it like any other | refuse it after Tuesday evening
Recommended: accept it up to the end of the rehearsal day and show it like any other, because late word is still better seen than lost
If left: nothing is built that depends on the cut-off
Harm: medium
Settles: S.absence.recorded-after-tuesday.record-for-singer-1, S.absence.recorded-after-tuesday.see-who-missing-1, S.absence.recorded-after-tuesday.see-who-missing-2, V.rehearsal-date.edge, C.states.absence.recorded-after-tuesday
Under: record-for-singer

## A14: Looking at a rehearsal that has passed, or a date that cannot be a rehearsal
Kind: chosen
Says: A past Thursday shows the absences recorded for it, said to have passed. They are what was recorded ahead, not who came. A date that is not a Thursday, does not exist or cannot be read gets the matching refusal and no list.
Rests on: showing what was recorded changes nothing, and an empty list for a wrong date would mislead
Settles: S.rehearsal.took-place.see-who-missing-1, S.rehearsal.took-place.see-who-missing-2, S.absence.rehearsal-passed.see-who-missing-1, S.absence.rehearsal-passed.see-who-missing-2, C.states.rehearsal.took-place, C.states.absence.rehearsal-passed
Under: see-who-missing
Criterion: Given an absence was recorded for a Thursday now past, when someone looks at that date, then the absence is shown and the rehearsal is said to have passed.
Criterion: Given the register is available, when someone looks at 31 February 2027, then they are told there is no such date.

## A15: A Thursday with no rehearsal
Kind: not here
Says: The slice has no way to know of a Thursday without a rehearsal: that is slice 8. It covers ordinary Thursday rehearsals only.
Rests on: 004_slice.md, Left for later: extra rehearsals and Thursdays without one are slice 8
Settles: S.rehearsal.no-rehearsal.*, C.states.rehearsal.no-rehearsal
Under: record-for-singer

## A16: The same absence recorded twice
Kind: chosen
Says: Recording an absence already recorded for that singer and date, whether at once, later or from a second window, keeps one absence and says it was already recorded. While one request is being saved, a second cannot create another.
Rests on: a repeat is harmless when the singer and date together can only be recorded once
Settles: L.user-action-01.record-request, S.singer-in-the-register.in-register.again, S.rehearsal.coming-up.again, S.absence.recorded.again, S.absence.recorded.record-for-singer-1, S.absence.recorded-after-tuesday.again, V.saved-absences.twice
Under: record-for-singer
Criterion: Given Robin Vale is already recorded as missing a coming Thursday, when a section leader records the same absence again, then they are told it was already recorded.
Criterion: Given Robin Vale's absence has been recorded twice for one date, when someone looks at that date, then Robin Vale is listed once.

## A17: Saying it is saved, leaving, reloading and going back
Kind: chosen
Says: On starting, the section leader sees that it is being recorded when it is not instant. "Recorded" is said only after storage has confirmed the save. Nothing is saved before the section leader sends the request, and giving up or leaving before that leaves nothing. If the product is closed during a save, afterwards the absence is either wholly there or not at all, and looking at the date shows which. Reloading or stepping back never records anything by itself, and sending the same request again follows the rule on repeats. Opening or following anything only reads.
Rests on: a confirmation given early or a save made by reloading would mislead the section leader
Settles: L.durable-write-02.absence, L.durable-write-12.record-request, L.user-action-02.record-request, L.user-action-03.record-request, L.user-action-05.record-request, L.user-action-10.record-request, L.authorization-07.record-request, S.singer-in-the-register.in-register.reopened, S.rehearsal.coming-up.reopened, S.absence.recorded.reopened, S.absence.recorded-after-tuesday.reopened, S.rehearsal.took-place.reopened, S.absence.rehearsal-passed.reopened, S.rehearsal.took-place.again, S.absence.rehearsal-passed.again
Under: record-for-singer
Criterion: Given a section leader has entered a name and date but not sent them, when they leave, then no absence is recorded.
Criterion: Given an absence has just been recorded, when the section leader reloads or steps back, then nothing new is recorded.

## A18: What is still there after a restart
Kind: chosen
Says: Singers and recorded absences are unchanged by closing or restarting the product, and by time passing. A singer or name that was never in the register leaves nothing behind. A rehearsal moves from coming to passed when its date is over, with nothing to be done.
Rests on: what was confirmed has to outlast the program that saved it
Settles: S.singer-in-the-register.not-in-register.reopened, S.singer-in-the-register.not-in-register.restart, S.singer-in-the-register.not-in-register.time, S.singer-in-the-register.in-register.restart, S.singer-in-the-register.in-register.time, S.rehearsal.coming-up.restart, S.rehearsal.coming-up.time, S.rehearsal.took-place.restart, S.rehearsal.took-place.time, S.absence.recorded.restart, S.absence.recorded-after-tuesday.restart, S.absence.recorded-after-tuesday.time, S.absence.rehearsal-passed.restart
Under: record-for-singer
Criterion: Given an absence was confirmed as recorded, when the product is closed and opened again, then the absence is shown for its date.

## A19: Saving is all or nothing
Kind: chosen
Says: A save cut off, failed or interrupted while replacing saved data leaves either everything as it was or everything with the new absence, never part of either. Saving an absence never alters singers or attendance. No history file is read half-written: an incomplete last entry is never treated as an absence, and is reported as damage.
Rests on: an all-or-nothing save is the known solution to a cut-off write
Settles: L.durable-write-01.saved-register, L.durable-write-06.saved-register, L.durable-write-07.saved-register, L.startup-read-04.saved-register
Under: new: keep-register-safe
Criterion: Given a saved register, when the product is stopped partway through saving an absence, then on the next start all earlier singers, attendance and absences are there.
Criterion: Given a saved register, when an absence is recorded, then singers and attendance are unchanged.

## A20: A save that fails
Kind: chosen
Says: If there is no space or storage reports a failure, the section leader is told the absence was not recorded, that earlier data is kept, and to note the call on paper, tell whoever looks after the computer and check the date's list later. The product does not retry on its own and never turns a reported failure into success.
Rests on: a retry that appears to work does not prove the data is there
Settles: L.durable-write-04.record-request, L.durable-write-05.record-request, L.logging-07.record-request
Under: record-for-singer
Criterion: Given the disk is full, when a section leader records an absence, then they are told it was not recorded.
Criterion: Given saving fails, when the register is next read, then everything saved before the attempt is there.

## A21: Surviving a power cut on the hall computer
Kind: test
Says: It is not known what the hall computer, its disk and its file system keep after a sudden loss of power, or how the register is stored today.
Rests on: no document describes the computer's storage
Test: Find the computer's system, disk and where the register is kept. Check that a confirmed save is forced to disk there, and cut power to a spare or test copy just after one.
Harm: high
Settles: L.durable-write-03.saved-register
Under: new: keep-register-safe

## A22: Whether the computer can remove or move the saved register
Kind: test
Says: It is not known whether the register sits where the computer cleans up or syncs files on its own, or which files together make it up.
Rests on: no document says where or how the register is saved
Test: On the hall computer, find every file that makes up the register and check for automatic clean-up, sync or reset of that place.
Harm: high
Settles: L.startup-read-07.saved-register, L.durable-write-11.saved-register
Under: new: keep-register-safe

## A23: Unreadable, damaged or unfamiliar saved data
Kind: chosen
Says: Nothing saved at all is a first run and is said as such. Saved data that is damaged, unreadable, not recognisably the register's, partly missing, of the wrong shape, or inconsistent (such as an absence for a singer who is not there) stops both recording and showing: the person is told the register cannot be read and who to ask, it is never shown as having no absences, and it is never overwritten, repaired or started afresh on its own. Singers or absences wholly absent where they should be are damage. A saved set with no absences, in a version that holds them, means none are recorded. With no singers, every name is unknown and the person is told the register holds no singers.
Rests on: refusing is safer than writing over data or showing a wrong empty list
Settles: L.startup-read-01.saved-register, L.startup-read-02.saved-register, L.startup-read-03.saved-register, L.startup-read-03.see-who-missing-2, L.durable-write-08.saved-register, L.lifecycle-05.absence, V.saved-singers.empty, V.saved-singers.missing, V.saved-singers.malformed, V.saved-absences.empty, V.saved-absences.missing, V.saved-absences.malformed
Under: new: keep-register-safe
Criterion: Given the saved register is damaged, when someone looks at a rehearsal, then they are told it cannot be read instead of being shown that no absence is recorded.
Criterion: Given the file at the register's place is not a register, when a section leader tries to record an absence, then that file is left unchanged.
Criterion: Given a saved absence names a singer who is not in the register, when someone looks at a rehearsal, then they are told the register is inconsistent.
Criterion: Given the register holds no singers, when a section leader tries to record an absence, then they are told it holds no singers.

## A24: A register that can be read but not changed
Kind: chosen
Says: If it can be read but not changed, who is missing is still shown, and recording says it cannot be saved and to tell whoever looks after the computer. Nothing that needs repair is altered. The product repairs nothing itself, so no other copy ever waits on a repair.
Rests on: reading is still useful, and the product has no automatic repair
Settles: L.startup-read-05.saved-register, L.startup-read-06.saved-register
Under: new: keep-register-safe
Criterion: Given the register can be read but not changed, when someone looks at a rehearsal, then the recorded absences are shown.

## A25: Silent changes, wrong data and rescue
Kind: chosen
Says: Each read checks that the saved data is whole and that every absence has a singer and a real Thursday date. The slice does not claim to detect a believable but wrong change: a section leader or the arranger would notice it against what they know. No automatic rescue exists. A register put back by hand passes the same checks before use, and whoever does it is told that absences recorded after that copy are missing.
Rests on: checks catch damage, and nothing can prove a believable value is true
Settles: L.durable-write-09.saved-register, L.startup-read-08.saved-register, L.startup-read-09.saved-register
Under: new: keep-register-safe

## A26: Spare copies of the register
Kind: owner
Says: Whether singers and absences need a spare copy, kept where losing the hall computer does not lose it too. This slice makes no routine copy unless asked for. The documents name none.
Rests on: a spare is a cost and a risk to accept, and each copy also holds singers' details
Options: no routine spare in this slice, accepting that losing the computer can lose the register | a regular copy kept off the hall computer, in a place you name
Recommended: a regular copy kept off the hall computer, in a place you name, because the register also holds who came and cannot be rebuilt from this slice
If left: no routine spare is made, and a lost or broken computer can lose everything
Harm: high
Settles: L.startup-read-10.saved-register, L.logging-08.saved-register
Under: new: keep-register-safe

## A27: Taking copies, and bringing old ones back
Kind: chosen
Says: Any copy of the register is taken so that it holds a whole state, never one caught mid-save. A copy made before absences existed can still be opened by the new version, shows no absences, and whoever brings it back is told that later absences are not in it. This holds for as long as the new version reads the register as it is today.
Rests on: a copy is only useful if it opens and says what it lacks
Settles: L.durable-write-10.saved-register, L.migration-11.saved-register
Under: new: keep-register-safe
Criterion: Given a copy of the register saved before this slice, when the new version opens it, then its singers and attendance are all there.

## A28: Carrying today's register forward
Kind: chosen
Says: The register as saved today is carried forward with every singer and attendance record kept, and nothing erased for being old. It starts with no absences: none is made up. Before first changing it, the product keeps an untouched copy beside it. If bringing it up to date fails, the register stays as it was, the person is told, and the next start tries again from that unchanged state. A version that meets data from a later version refuses to change it.
Rests on: keeping the original is the known protection for a change of saved data
Settles: L.migration-01.saved-register, L.migration-02.saved-register, L.migration-07.saved-register, L.migration-10.saved-register
Under: new: keep-register-safe
Criterion: Given the register saved today, when the new version first uses it, then every singer and attendance record is still there.
Criterion: Given the register saved today, when the new version first looks at a coming Thursday, then it says no absence is recorded.
Criterion: Given bringing the register up to date fails, when the register is checked afterwards, then it is as it was before.
Criterion: Given a register written by a later version, when this version tries to record an absence, then it says the register is from a newer version and leaves it unchanged.

## A29: What today's program does with a register holding absences
Kind: test
Says: It is not known whether the program as it is today would keep, lose or damage absences if it were put back, or left running, once they are saved.
Rests on: no document says how the existing program reads and writes the register
Test: On a copy with invented data, record an absence with the new version, then use today's program to read and to save, and see what remains. Repeat with today's program already open during the first use.
Harm: high
Settles: L.migration-03.saved-register, L.migration-05.saved-register
Under: new: keep-register-safe

## A30: Two things happening at once
Kind: chosen
Says: Every change is made to the register as it is at that moment, never by writing back an older picture of it, so two recordings made together both stay. The singer is checked and the absence saved as one step. If the register is busy, the product waits up to 5 seconds, then says nothing was recorded and to try again. Nothing is cancelled and repeated behind the person's back. A second window or copy follows the same rules. One person's absence never replaces another's.
Rests on: checking and saving as one step is the known way to stop lost changes
Settles: L.concurrency-01.saved-register, L.concurrency-02.absence, L.concurrency-02.singer-in-the-register, L.concurrency-04.record-request, L.concurrency-08.saved-register, L.concurrency-09.record-request, S.singer-in-the-register.not-in-register.second, S.singer-in-the-register.in-register.second, S.rehearsal.coming-up.second, S.rehearsal.took-place.second, S.absence.recorded.second, S.absence.recorded-after-tuesday.second, S.absence.rehearsal-passed.second
Under: new: keep-register-safe
Criterion: Given two section leaders act from two windows, when each records a different singer at the same moment, then both absences are shown.
Criterion: Given another operation holds the register for more than 5 seconds, when a section leader records an absence, then they are told it was not recorded and to try again.

## A31: Whether the protection against two copies holds where the register is kept
Kind: test
Says: It is not known whether the place the register is stored supports stopping two copies from writing at once, for instance if it is shared or synced, or if today's program takes part.
Rests on: no document says where the register is stored or how today's program writes it
Test: Where the register really is, save from two copies at the same moment, including today's program with the new one, and check that nothing is lost.
Harm: medium
Settles: L.concurrency-12.saved-register
Under: new: keep-register-safe

## A32: How fresh the list is
Kind: chosen
Says: The list for a date is read in one go, as the register stood at one moment, and shows when it was read. Every new look after a confirmation includes the new absence. A list already on screen, in another window, or left open or restored later, does not change by itself: its time shows its age, and looking again reads afresh. A saved way back to a date's list reads it afresh, and if the date or register cannot be shown it says why. No signing out exists.
Rests on: a dated list read at one moment cannot pass for a live one
Settles: L.sync-10.missing-view, L.concurrency-03.missing-view, L.concurrency-06.missing-view, L.user-action-06.missing-view, L.user-action-07.missing-view, L.user-action-12.missing-view
Under: see-who-missing
Criterion: Given a list for a coming Thursday was shown before an absence was recorded, when it is looked at afresh, then the new absence is on it.
Criterion: Given the register is available, when a rehearsal's list is shown, then it says when it was read.

## A33: What the list holds and in what order
Kind: chosen
Says: Every singer recorded for the date is shown at once, with no cut-off: the choir is about 45. Where it is longer than the screen, all of it can be reached by scrolling, in one order throughout. It is ordered by the whole name as the register writes it, ignoring capitals and treating accented letters beside their plain ones, by one fixed rule for everyone. Names are never cut, and rows and messages wrap. Only the date, the time read and each singer's name and voice part are shown. Saved lists far larger than a choir could produce, over 1,000 singers or 10,000 absences for one date, are treated as damage.
Rests on: the whole of a small list answers the arranger's question, and voice part tells like names apart
Settles: L.limits-08.missing-view, L.text-06.missing-view, L.text-07.missing-view, L.text-12.missing-view, L.presentation-10.missing-view, L.presentation-12.missing-view, L.stored-data-08.missing-view, V.saved-singers.long
Under: see-who-missing
Criterion: Given 45 singers are recorded as missing one Thursday, when it is looked at, then all 45 can be reached.

## A34: A very large number of saved absences
Kind: chosen
Says: Absences build up over the weeks and the total is not damage by itself: only more than 10,000 for a single date is, since a date can hold at most one per singer.
Rests on: a limit on the running total would one day shut out a healthy register
Settles: V.saved-absences.long
Under: see-who-missing

## A35: Taking back or correcting an absence
Kind: owner
Says: A recorded absence has no way out. A wrong singer or date, or a singer whose plans change, stays shown as missing, and the programme could be changed for someone who is coming.
Rests on: the requirements have no item for it (002_requirements.md line 20), and what is in or out is yours
Options: add taking back an absence as a requirement before the product is relied on | leave it out and live with mistakes staying shown
Recommended: add taking back an absence as a requirement before the product is relied on, because one mistake could misdirect a rehearsal plan
If left: the slice is built with no way to take an absence back
Harm: high
Settles: L.lifecycle-03.absence, L.user-action-08.absence, L.user-action-09.record-request, C.states.dead-end.1
Under: record-for-singer

## A36: No confirmation step and no second person
Kind: chosen
Says: Recording asks for no second confirmation and no second person. The result names the singer, voice part and date in full.
Rests on: a question asked on every call soon goes unread, and showing exactly what was recorded makes a mistake visible
Settles: L.misuse-05.record-request
Under: record-for-singer
Criterion: Given Robin Vale is a tenor in the register, when an absence is recorded for them, then the result shows their name, voice part and the date.

## A37: A singer who has left the choir
Kind: owner
Says: The documents give no way to remove a singer from the register, so one who has left stays in it and can still have an absence recorded.
Rests on: whether removing singers is in or out is yours, and removal may not be reversible
Options: leave removing singers out for now | add marking a singer as having left as a requirement
Recommended: leave removing singers out for now, because it does not stop this slice answering who will be missing
If left: every singer in the register is treated alike
Harm: low
Settles: C.states.singer-in-the-register.left-choir, C.states.dead-end.2
Under: record-for-singer

## A38: No separate state for a singer who has left or is being asked
Kind: chosen
Says: The slice adds and reads no mark for a singer who has left or is being asked whether they're still coming. Anyone in the register is treated as a singer in it: recording, refusals, repeats, restarts and the list work the same. Someone not in it is unknown. How a singer gets into or out of the register is not changed here.
Rests on: asking singers is the next activity, and the slice's criteria turn only on whether a singer is in the register
Settles: S.singer-in-the-register.asked-if-still-coming.*, S.singer-in-the-register.left-choir.*, S.singer-in-the-register.not-in-register.see-who-missing-1, S.singer-in-the-register.not-in-register.see-who-missing-2, C.states.singer-in-the-register.asked-if-still-coming, C.states.singer-in-the-register.not-in-register
Under: record-for-singer

## A39: Who may record and who may see
Kind: owner
Says: Who may record absences and see who will be missing, and whether anything checks it. The register has no accounts. With no check, anyone who can use the hall computer, a singer or visitor included, can see who will be away and record a false absence, nothing says who did it, and nothing changes when someone stops being a section leader. This is also your question 2 on who needs to see.
Rests on: who may see singers' details, and the risk of having no check, are yours to accept
Options: no check in the product, so anyone who can use the hall computer can record and see | a shared passcode for section leaders and whoever arranges the programme, with none for singers
Recommended: no check in the product, so anyone who can use the hall computer can record and see, if only section leaders and you can get at that computer, because a shared passcode adds little there; if others can use it, choose the passcode
If left: nothing that depends on who may use it is built, and the product is not to be relied on with real singers
Harm: high
Settles: L.authorization-01.record-request, L.authorization-01.missing-view, L.authorization-02.absence, L.authorization-04.saved-register, L.authorization-05.record-request, L.authorization-10.record-request, W.who-sees
Under: new: who-may-use

## A40: Where any rule is enforced
Kind: chosen
Says: Every rule about names, dates and, if one is chosen, who may act is enforced where the register is read or changed, not only on screen, so a request that skips the screen meets the same rules. A request can set only the singer and the rehearsal date. Anything else sent is refused. If a permission check exists and cannot be completed, the request is refused. No request sent by another site or program in a person's name is accepted: recording takes a deliberate action in the product itself, and nothing is changed by opening or following anything.
Rests on: a rule checked only on screen can be walked round
Settles: L.user-input-05.record-request, L.authorization-03.record-request, L.authorization-06.record-request, L.authorization-08.record-request, L.misuse-07.record-request
Under: new: who-may-use
Criterion: Given the screen's own checks are skipped, when a request to record an absence for an unknown singer reaches the product, then nothing is recorded.

## A41: How it is used, and from where
Kind: owner
Says: How section leaders record and how whoever arranges the programme looks before rehearsal night, and from where. The register is on the hall computer, today's program is spoken of as having commands, and no document says you can get to it before the night from anywhere else.
Rests on: how you want to use the product is yours, and so is whether looking from elsewhere is in
Options: on the hall computer only, by typed commands | on the hall computer only, on a simple screen with forms | also from elsewhere, such as your own phone or computer
Recommended: on the hall computer only, on a simple screen with forms, because section leaders can use it without learning commands and nothing is opened to other machines; if you cannot get to the hall before the night, this will not serve you
If left: how it is used is not designed
Harm: high
Settles: F.network.answers-to
Under: see-who-missing

## A42: Protecting whatever can be reached
Kind: chosen
Says: Which addresses it answers at waits for your choice of how and from where it is used. Nothing between sender and product is trusted for facts about a request. Every connection between machines must be encrypted, and an unencrypted one is refused. If use stays on the hall computer, nothing travels between machines to be watched. Each address accepts only the kind of request it is for. No diagnostic mode, file listing, source history, documentation page, measurement or test code is reachable, and no reply or refusal names what the product is built from.
Rests on: what is not offered cannot be attacked, and encryption is the known protection for what travels
Settles: F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, F.network.gives-away, T.singer-details.record-request
Under: new: who-may-use

## A43: If a page in a browser is used
Kind: chosen
Says: These hold if any part is shown in a browser, and are met trivially if not. Data is always sent with its true type, with type guessing off, and is never run as a page. The page loads and runs only its own code and styles, none from another party. No other site may frame it, call it or read its replies, and it takes no messages from other windows. It sends nobody on to a supplied address, tells other sites nothing of where a person came from, and no name is put in an address. Pages and replies showing singers' details are not to be stored by the browser or anything between. Nothing is kept in the browser to know a person by. If a passcode is chosen, what it leaves behind is settled with that choice.
Rests on: these are the standard protections for a page holding personal details
Settles: F.browser.*, L.stored-data-05.singer-name, L.stored-data-06.missing-view
Under: new: who-may-use
Criterion: Given the product is used in a browser, when a name is looked up or recorded, then the name does not appear in the address.

## A44: What is stored, and who can open the files
Kind: chosen
Says: The harm is in singers' names joined with when they will be away, and in a false or lost absence. The product keeps this only with the register on the hall computer, with no copy on the device used to view it, apart from copies named in these answers or chosen by you. It makes no files readable by more accounts than the register itself. It uses no key of its own: the key would sit on the same computer. So there is no key to lose or replace. Protection is the computer's own sign-in and file permissions, and who can get at it falls under your question on who may use it.
Rests on: a key kept beside the data it locks protects little
Settles: L.stored-data-01.absence, L.stored-data-01.saved-register, L.stored-data-03.saved-register, L.stored-data-04.saved-register, L.stored-data-10.saved-register, X.singer-details.stored, W.sensitive, W.prize
Under: new: who-may-use

## A45: Who can read or change the register's files on the hall computer
Kind: test
Says: It is not known which accounts or people can open, copy or change the saved register and its copies directly, or whether the disk is protected if the computer is taken.
Rests on: no document describes the computer's accounts or disk
Test: On the hall computer, check who can sign in, who can open or change the register's files, whether the disk is encrypted and where copies go.
Harm: high
Settles: L.authorization-09.saved-register, L.stored-data-02.saved-register, T.singer-details.saved-register, T.absence.saved-register
Under: new: who-may-use

## A46: Seeing who looked, and noticing misuse
Kind: chosen
Says: Looking at a list is not recorded. A person not meant to see it, or one trying it, would not be noticed by the product: what limits that is who can use the computer, which is your question. Nothing else lets anything be changed from the list.
Rests on: with no accounts a record of looking could not say who looked
Settles: L.stored-data-12.missing-view, T.singer-details.missing-view
Under: new: who-may-use

## A47: False, repeated or destructive requests
Kind: chosen
Says: The only change offered is adding one absence for one known singer and one allowed date: nothing offered removes or alters singers, attendance or absences. Repeats keep one absence. A script could add absences for real singers one at a time: there is no rate limit and speed is not treated as abuse, since the harm is bounded by one per singer per date. Each recording leaves a record with its time, so a burst can be seen afterwards. A false absence typed by someone who can use the product is the risk in your question on who may use it.
Rests on: offering no destructive request is stronger than guarding one
Settles: L.misuse-03.record-request, L.misuse-04.record-request, T.absence.record-request, T.saved-register.record-request
Under: new: who-may-use
Criterion: Given a saved register, when any request the product offers is made, then no singer or attendance record is changed or removed.

## A48: How long absences are kept
Kind: owner
Says: How long a record of who was away is kept. No document says. Asking singers who miss without a word, the next activity, may need past ones.
Rests on: keeping singers' details is an obligation you accept, and deleting cannot be taken back
Options: keep them until you decide otherwise | remove each a year after its rehearsal | remove each once its rehearsal has passed
Recommended: remove each a year after its rehearsal, because it covers a season while not keeping singers' details for ever
If left: absences are kept and nothing removes them
Harm: low
Settles: L.stored-data-09.absence, S.absence.recorded.time, S.absence.rehearsal-passed.time
Under: new: keep-register-safe

## A49: Law and other obligations
Kind: owner
Says: No document says what law or agreement binds keeping singers' names with when they will be away. The product holds this about about 45 people. What applies has not been checked.
Rests on: what law or contract binds it is yours to say
Options: you check what data protection duties the choir has before real names are used | you confirm that nothing beyond what already covers the register applies
Recommended: you check what data protection duties the choir has before real names are used, because the absences are new details about people
If left: no claim is made that any duty is met
Harm: medium
Settles: W.obligations
Under: new: who-may-use

## A50: How reliable and how fast, and an hour without it
Kind: owner
Says: How often it may fail, how slow is too slow, and what it means if it cannot be used for an hour, for instance while a singer is on the phone or on Tuesday evening.
Rests on: how fast and reliable it must be is yours
Options: an hour out is acceptable with calls noted on paper, answers within 2 seconds, and no failure that loses a confirmed absence | it must be usable every time it is needed, with a second way to record and see
Recommended: an hour out is acceptable with calls noted on paper, answers within 2 seconds, and no failure that loses a confirmed absence, because a section leader can record the call afterwards
If left: no target is set or tested
Harm: low
Settles: W.unavailable, W.target
Under: new: keep-register-safe

## A51: What is recorded about the product's own work
Kind: chosen
Says: Each recorded absence, refusal, failed save and unreadable register leaves a record with the hall computer's time, the kind of event, the outcome and, once valid, the rehearsal date. It does not say who the singer is or who acted. Records hold no typed text. The time is when it was recorded, not when the singer phoned, and is not used to decide anything. Records come from one computer and are kept in the order written. They stay within 1 MB in total, the oldest dropping off, which is also how they end. If a record cannot be written, the absence is still recorded and the person is not stopped. Nothing is sent anywhere and nobody is alerted. Whoever looks after the computer reads them when a failure is reported. They are as open to change as other files there, and a change would not be detected.
Rests on: events without names are enough to trace a fault, and records must not block recording or fill the computer
Settles: L.logging-01.record-request, L.logging-02.record-request, L.logging-04.singer-name, L.logging-05.record-request, L.logging-06.record-request, L.logging-09.record-request, L.logging-10.record-request, L.logging-11.record-request, L.logging-12.singer-name, L.time-12.absence
Under: new: keep-register-safe
Criterion: Given records cannot be written, when a section leader records an absence, then it is still recorded.
Criterion: Given the records have reached 1 MB, when another event is recorded, then their total stays within 1 MB.

## A52: Singers' details stay out of records, errors and examples
Kind: chosen
Says: No typed or saved name, singer list or absence list goes into a record, an error's own message or trace, anything sent for monitoring (nothing is sent), or test data and examples kept with the code, which use invented names. An unexpected failure shows a plain message with no saved data. On screen, a name is shown only in the result or refusal for what the person typed, in the choice between matching singers, and in the list asked for.
Rests on: details that are never copied cannot leak from the copy
Settles: L.logging-03.singer-name, X.singer-details.logs, X.singer-details.errors-inside, X.singer-details.errors-shown, X.singer-details.telemetry, X.singer-details.samples, X.singer-details.replies
Under: new: keep-register-safe
Criterion: Given saving an absence fails, when the records and error output are read, then no singer's name is in them.
Criterion: Given a damaged register, when the error is shown, then it shows none of the saved names.

## A53: The hall computer's clock
Kind: chosen
Says: Whether a date has passed, and the time shown on lists and records, come from the hall computer's clock. If it is wrong, a coming rehearsal could be refused as past or a past one accepted: a refusal for a past date states what today is taken to be, so the error can be seen. Moving the clock changes no saved absence. The slice has no waits across days and nothing expires. The 5-second wait for a busy register is measured so that setting the clock does not alter it.
Rests on: showing the date relied on lets a person notice a wrong clock
Settles: L.time-01.rehearsal, L.time-03.rehearsal
Under: record-for-singer
Criterion: Given a section leader enters a Thursday before the computer's date, when it is refused, then the refusal shows the date taken as today.

## A54: Using it without a mouse, sight or colour
Kind: chosen
Says: Everything can be done by keyboard alone, and focus can always be moved out of any part. Where there is a screen with controls, focus is visibly marked, moves to the result when recording finishes or something closes, and each control says its name and purpose to a screen reader. Results and refusals are given as text and announced. Nothing relies on colour or a picture alone. Text has a contrast of at least 4.5 to 1, and at twice the size it wraps with nothing lost.
Rests on: this is accepted accessibility practice
Settles: L.accessibility-01.record-request, L.accessibility-01.missing-view, L.accessibility-02.record-request, L.accessibility-03.record-request, L.accessibility-04.record-request, L.accessibility-05.record-request, L.accessibility-06.missing-view, L.accessibility-07.record-request, L.accessibility-08.missing-view, L.accessibility-08.refusal-message, L.accessibility-09.missing-view, L.accessibility-10.missing-view
Under: record-for-singer
Criterion: Given only a keyboard is used, when a section leader records an absence, then they can finish and see the result.
Criterion: Given text is at twice its size, when a rehearsal's list is looked at, then every name can be read in full.

## A55: Who notices when it breaks
Kind: chosen
Says: Whoever is using it sees the failure at once and is told to tell whoever looks after the computer. Nothing watches it otherwise.
Rests on: for one small computer, a plain message to the person there is enough to start a repair
Settles: W.noticed
Under: new: keep-register-safe

## A56: Components others wrote
Kind: chosen
Says: Nothing new that someone else wrote is added unless needed. Whatever the product uses, including what that brings with it, is listed with its source and a fixed version, and fetched only from its official source with its contents checked. No component is given credentials or outside data, and any that runs code at installation is avoided. Known flaws are checked for whenever the product is changed and at least monthly, and a serious one affecting it is fixed or the component replaced within 30 days.
Rests on: the fewer and better known the components, the less there is to go wrong
Settles: F.dependency.*
Under: new: keep-register-safe

## A57: One choir, nothing to guess
Kind: chosen
Says: There is one choir and one register, so there are no groups to keep apart. No field of an absence is hidden from someone allowed to see it, and only singer and date can be set. No value is relied on for being hard to guess.
Rests on: the slice makes no link, code or session, and any passcode chosen would reopen this
Settles: F.several-people.*, F.unguessable.made
Under: new: who-may-use

## A58: No settings
Kind: not here
Says: The slice adds and reads no new setting.
Rests on: kept.md: configuration is dropped because the criteria add and change no setting
Settles: V.every-setting.missing, V.every-setting.empty, V.every-setting.malformed, V.every-setting.outside
Under: new: keep-register-safe
