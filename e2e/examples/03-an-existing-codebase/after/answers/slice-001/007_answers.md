# Answers: slice 1

The names and dates in the criteria are invented.

## A1: How it is used
Kind: chosen
Says: Recording and looking are added as commands of the existing register program on the hall's computer. They open no network address, serve no page and send nothing anywhere.
Rests on: the register is already used by command on that computer by the section leaders (the README and register.py), no document asks for a page, and the slice needs nothing from outside. Whether singers reach it from home matters only to slice 3.
Settles: F.browser.context, F.browser.page-policy, F.browser.framing, F.browser.type-guessing, F.browser.came-from, F.browser.other-sites, F.browser.messages, F.browser.others-code, F.browser.sent-on, F.browser.kept-by-browser, F.browser.known-by, F.network.answers-to, F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, F.network.gives-away, T.singer-details.record-request, L.stored-data-05.singer-name, L.stored-data-06.missing-view, L.user-action-12.missing-view, L.authorization-06.record-request, L.authorization-10.record-request
Under: record-for-singer
Criterion: Given the hall's computer with its network connected, when a section leader runs the command that records an absence, then the program opens no network address and makes no network connection.

## A2: No components from others
Kind: chosen
Says: The slice uses only the language and its standard library. No component written by someone else is added.
Rests on: recording and listing names and dates needs none, and the existing program uses none (register.py).
Settles: F.dependency.known-flaw, F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
Under: new: no-added-components
Criterion: Given a computer with the language installed and nothing added, when the program is run, then recording and looking both work.

## A3: No hidden values, fields or groups
Kind: not here
Says: The slice makes no value meant to be impossible to guess. There is one choir, and no rule hides any field of a record from someone who may see the record.
Rests on: A1 and the register having no accounts.
Settles: F.unguessable.made, F.several-people.fields, F.several-people.groups
Under: record-for-singer

## A4: No settings
Kind: not here
Says: The slice reads no setting.
Rests on: kept.md drops the configuration entries: the criteria add and change no setting.
Settles: V.every-setting.missing, V.every-setting.empty, V.every-setting.malformed, V.every-setting.outside
Under: record-for-singer

## A5: Who may record and see
Kind: owner
Says: Today there are no accounts, and whoever is at the hall's computer can use the register. With absences added, that person could see who will be away on which evening, record a false absence, or open and change the saved file. Nothing would show who did it. Whether others than whoever arranges the programme may see is also unconfirmed (requirements, question 2). Singers need no password either way.
Rests on: a risk only you can accept.
Settles: L.authorization-01.record-request, L.authorization-01.missing-view, L.authorization-02.absence, L.authorization-03.record-request, L.authorization-04.saved-register, L.authorization-05.record-request, L.authorization-08.record-request, L.authorization-09.saved-register, T.singer-details.missing-view, T.absence.record-request, T.absence.saved-register, W.who-sees
Under: see-who-missing
Options: accept that whoever can use the hall's computer can record, see and change absences, as with the register today | limit recording and seeing to section leaders and whoever arranges the programme, which needs a way to tell who they are
Recommended: accept it as with the register today, because the register has no accounts, and a check inside the program would not stop someone opening the saved file.
If left: the slice is no more protected than the register is today.
Harm: medium

## A6: When this counts as working, and how the list reaches the arranger
Kind: owner
Says: The slice works only if whoever arranges the programme gets the names in time to act. The list is on the hall's computer, and no document says they can get to that computer before rehearsal night. Nor does any say how often the program may fail, or how slow is too slow.
Rests on: how you want to use the product, which the documents don't say.
Settles: W.target

Under: see-who-missing
Options: whoever arranges the programme looks at the hall's computer themself | someone at the hall looks and passes the names on | the list must be readable away from the hall, which this slice does not provide
Recommended: look at the hall's computer themself, if they can get there in time, because it needs nothing more than this slice.
If left: the slice shows the list on the hall's computer only, and it may not be seen in time to rearrange the programme. How soon and how often it must work cannot be judged until this is known.
Harm: high

## A7: Mistaken or changed absences
Kind: owner
Says: Nothing in this slice takes back or corrects a recorded absence. A wrong singer or date, or a singer whose plans change, stays shown as missing. The requirements have no item for it (question 3).
Rests on: what is in or out.
Settles: L.lifecycle-03.absence, L.user-action-08.absence, C.states.dead-end.1, L.misuse-05.record-request
Under: record-for-singer
Options: add taking back an absence to the requirements and to this slice | add it to the requirements as a later slice | leave it out, and keep any correction by hand outside the program
Recommended: add it to this slice, because a mistake could otherwise make a voice part look short when it isn't, with two pieces needing at least four tenors (000_problem.md).
If left: a recorded absence cannot be put right in the program.
Harm: high

## A8: Singers who have left
Kind: owner
Says: The documents give no way to remove a singer. The register has no mark for someone who has left, so they can still have an absence recorded.
Rests on: what is in or out.
Settles: C.states.dead-end.2, C.states.singer-in-the-register.left-choir
Under: record-for-singer
Options: leave removing a singer out of this work | add it to the requirements
Recommended: leave it out, because it does not stop anyone recording or seeing an absence.
If left: someone who has left stays in the register.
Harm: low

## A9: How long absences are kept, and what duties apply
Kind: owner
Says: No document says how long past absences are kept, or whether any law or choir rule applies to holding singers' names with the dates they are away. I have read nothing about either, so I make no claim.
Rests on: an obligation only you can accept, and removal cannot be taken back.
Settles: L.stored-data-09.absence, L.logging-12.singer-name, W.obligations
Under: new: keeping-absences
Options: keep past absences with the register until you say otherwise, and check what duties the choir has | remove each absence a set time after its rehearsal
Recommended: keep them for now and check the duties, because keeping them can be changed later and removal cannot.
If left: nothing removes a past absence.
Harm: medium

## A10: The register file is in the code repository
Kind: owner
Says: `data/register.json` is a file tracked in this repository, which has a GitHub repository. I have not opened it, so I don't know whether its names are real, and I haven't checked who can see the repository. If absences are saved to a tracked file, a commit and push would send them there too. Taking a file out of the latest version does not take it out of the history.
Rests on: a risk you must accept, and rewriting history cannot be taken back.
Settles: X.singer-details.stored
Under: new: where-names-go
Options: stop tracking the file and decide separately about its history, if it holds real names | keep it tracked because its contents are invented | keep real names tracked and accept who can see them
Recommended: if the names are real, stop tracking the file before any absence is saved, and then decide about the history, because a push copies the names off the hall's computer.
If left: the file stays tracked, and any commit of it carries what it holds.
Harm: high

## A11: A copy away from the hall's computer
Kind: owner
Says: No document says that any spare copy of the register exists. The program will keep the previous version beside the register (A30), which does not help if the computer is lost or its disk fails.
Rests on: a cost and a risk only you can accept.
Settles: L.startup-read-10.saved-register, L.logging-08.saved-register
Under: new: spare-copy
Options: someone copies the register to a second device on a regular day | accept that losing the computer loses the register and the absences
Recommended: copy it regularly to a device the choir controls, because the copy takes little work and a lost register would have to be rebuilt by hand.
If left: the only copies this slice makes are on the hall's computer.
Harm: medium

## A12: Does a save survive power loss on this computer
Kind: test
Says: What the hall computer's system and disk do when power is lost just after a save is not known.
Rests on: no document describes the computer beyond its being small and at the church hall.
Settles: L.durable-write-03.saved-register
Under: record-for-singer
Test: find out the computer's system, file system and kind of disk, read what its documentation promises about flushing a file to disk and about a failed flush, and cut power just after a recording on a copy of the register with invented names.
Harm: medium

## A13: What else touches the saved file
Kind: test
Says: Whether anything on the hall's computer removes, restores or syncs the program's folder on its own is not known.
Rests on: no document says what else runs on that computer.
Settles: L.startup-read-07.saved-register
Under: see-who-missing
Test: look on the hall's computer for sync, cleanup and restore-on-restart software covering the program's folder, and note where copies of it go.
Harm: high

## A14: The computer's date and time zone
Kind: test
Says: Whether the hall computer's date and time zone are right, and stay right after it has been switched off, is not known. The program depends on them to tell whether a Thursday is still ahead (A24).
Rests on: no document says how the computer keeps time.
Settles: L.time-01.rehearsal, L.time-03.rehearsal
Under: record-for-singer
Test: compare the computer's date, time and time zone with a trusted clock, then again after it has been off overnight with its network as usual.
Harm: medium

## A15: Reading and using the screen
Kind: test
Says: The commands are typed and read in the computer's own text window. How that window works with a screen reader, shows keyboard focus, handles larger text and contrasts text is not known.
Rests on: no document says what the computer runs or what the people using it need.
Settles: L.accessibility-02.record-request, L.accessibility-03.record-request, L.accessibility-04.record-request, L.accessibility-05.record-request, L.accessibility-09.missing-view, L.accessibility-10.missing-view
Under: see-who-missing
Test: on the hall's computer, record and look using the keyboard only, with text at twice the size, and with its screen reader if anyone needs one; check that focus, prompts and names can be read.
Harm: low

## A16: Showing every singer's name
Kind: test
Says: Whether the computer's text window can take and show every character in the singers' names, including accents and other scripts, is not known.
Rests on: no document says what the computer runs.
Settles: L.text-09.singer-name, L.text-12.missing-view
Under: see-who-missing
Test: on a copy of the program with invented names that have accents, an apostrophe, a long double-barrelled name and right-to-left text, type each one, record it and view the list.
Harm: low

## A17: One whole save
Kind: chosen
Says: A save leaves either everything as it was or everything including the change, never part of each. It is written aside and then swapped in. A recording changes no singer and no attendance. A leftover unfinished file is never read as the register. It is ignored, and its recording counts as not made.
Rests on: replacing a file in one step is the usual way to avoid a half-written one; the program today writes straight over the file (register.py). What power loss does is left to A12.
Settles: L.durable-write-01.saved-register, L.durable-write-06.saved-register, L.durable-write-07.saved-register, L.durable-write-12.record-request, L.startup-read-04.saved-register, L.user-action-05.record-request
Under: record-for-singer
Criterion: Given a section leader is recording an absence for Robin Vale, when the program is stopped before it says the absence is recorded, then on the next look the register opens with all earlier singers, attendance and absences, and Robin Vale's absence is either shown whole or not shown at all.
Criterion: Given an unfinished save file has been left beside the register, when whoever arranges the programme looks at a rehearsal, then they see what the last finished save held.

## A18: When it says recorded
Kind: chosen
Says: The program says an absence is recorded only after the save has been flushed to disk and swapped in without an error. If any step reports an error, it says the absence was not recorded, or that it cannot tell, and asks the section leader to look at that date before trying again. It does not retry by itself. A full disk is reported the same way and the earlier register is left as it was.
Rests on: a person must not be told something is saved when it may not be. How much the disk really keeps is left to A12.
Settles: L.durable-write-02.absence, L.durable-write-04.record-request, L.durable-write-05.record-request, L.logging-07.record-request
Under: record-for-singer
Criterion: Given the disk has no room for a save, when a section leader records an absence for Robin Vale on 14 January 2027, then they are told it was not recorded and why, and the earlier singers, attendance and absences are unchanged.
Criterion: Given saving fails for any reason, when a section leader records an absence, then they are never told that it is recorded.

## A19: What must agree
Kind: chosen
Says: Each saved absence names a singer in the register and a date. If a saved absence names nobody in the register, the list still shows that name, marked as not in the register. Nothing is silently dropped or removed.
Rests on: hiding it could make a voice part look fuller than it is. The singer check and the save happen under the same hold on the register (A21).
Settles: L.durable-write-08.saved-register, L.lifecycle-05.absence, L.concurrency-02.absence, L.concurrency-02.singer-in-the-register, L.concurrency-04.record-request
Under: see-who-missing
Criterion: Given a saved absence on 14 January 2027 names Sam Reed, who is not in the register, when that date is looked at, then Sam Reed is shown as recorded missing and as not in the register.

## A20: A damaged or unrecognised register
Kind: chosen
Says: If the file cannot be read or opened, or is not shaped like the choir's register (including a missing or wrong-typed list of singers, a bad singer entry or a bad absence entry), recording and looking stop. They say the register cannot be used, name the file and say to get help or restore a good copy. Nothing is written over it and no partial list is shown. A register that has no absences yet, because it predates them, is valid. The program never repairs or rescues a file by itself. After someone restores or repairs it by hand, the same checks apply, and the person restoring it must check recent absences because later ones may be gone.
Rests on: a wrong or partial list would mislead more than a clear refusal.
Settles: L.startup-read-01.saved-register, L.startup-read-02.saved-register, L.startup-read-08.saved-register, V.saved-singers.missing, V.saved-singers.malformed, V.saved-absences.malformed
Under: see-who-missing
Criterion: Given the register file is cut short, when whoever arranges the programme looks at 14 January 2027, then they are told the register cannot be used and which file it is, and are not told that no absence is recorded.
Criterion: Given the file where the register belongs holds something else, when a section leader records an absence, then it is refused and the file is left as it was.

## A21: One at a time
Kind: chosen
Says: Every command of the new program that changes the register, adding a singer and marking attendance included, holds it for itself from reading to saving. A second one waits up to 5 seconds, then says the register is in use, changes nothing and asks the person to try again. It is not repeated automatically after that. A hold left by a program that has stopped does not block later ones. Looking reads one whole saved version. The hold covers only this program on this one computer. It does not cover the earlier program, an editor, or a folder shared or synced elsewhere.
Rests on: without it, two section leaders saving from the same starting point could lose one recording.
Settles: L.concurrency-01.saved-register, L.concurrency-03.missing-view, L.concurrency-08.saved-register, L.concurrency-09.record-request, L.concurrency-12.saved-register, L.startup-read-06.saved-register
Under: record-for-singer
Criterion: Given two windows are open, when absences for Robin Vale and Jo Marsh are recorded for 14 January 2027 at the same moment, then the list for that date shows both.
Criterion: Given another command holds the register for more than 5 seconds, when a section leader records an absence, then they are told it is in use, that nothing was recorded and to try again.

## A22: Looking never writes
Kind: chosen
Says: Looking at a rehearsal changes nothing. The attendance report also stops saving. The program today saves after every command, the report included (register.py). Where the register can be read but not changed, looking works, and recording says it cannot save. A list is a picture of the moment it was shown. It says when it was made, and does not update itself, in another window or after the computer sleeps. Running the command again shows every absence confirmed before it.
Rests on: an old look that saves could overwrite a newer recording.
Settles: L.authorization-07.record-request, L.startup-read-05.saved-register, L.sync-10.missing-view, L.concurrency-06.missing-view, L.user-action-06.missing-view, L.user-action-07.missing-view
Under: see-who-missing
Criterion: Given a register that can be read but not changed, when whoever arranges the programme looks at 14 January 2027, then the list is shown and the file is unchanged.
Criterion: Given a list for 14 January 2027 has been shown and an absence is then recorded for that date, when the list is asked for again, then it includes that absence and shows the time it was made.

## A23: Earlier and later versions
Kind: chosen
Says: The register saved today is carried forward as it is. It has no absences, which means none are recorded; nothing is made up for past rehearsals and no old data is erased. Using the new program needs no separate update step. Bringing back an older copy works the same, with no time limit, but it lacks any absence recorded after it was made. A register marked as written by a later version is refused for both looking and changing. The earlier program must not be run alongside the new one, because it saves after every command and does not take part in the hold (A21). If it is put back, it must leave saved absences intact.
Rests on: carrying everything forward loses nothing, and a first save is as whole as any other (A17).
Settles: L.migration-01.saved-register, L.migration-02.saved-register, L.migration-03.saved-register, L.migration-05.saved-register, L.migration-07.saved-register, L.migration-10.saved-register, L.migration-11.saved-register, V.saved-absences.missing
Under: new: carry-the-register-forward
Criterion: Given a register saved by today's program, when the new program first looks at a coming Thursday, then it says no absence is recorded and every singer and attendance mark is unchanged.
Criterion: Given absences have been saved, when today's program runs its report and exits, with nothing else running, then the new program still shows those absences.
Criterion: Given a register marked as written by a later version, when a section leader records an absence, then it is refused, they are told a newer program wrote it and to use that one, and the file is unchanged.

## A24: Which dates can be recorded
Kind: chosen
Says: An absence is recorded only for a Thursday from today to 366 days ahead, by the hall computer's own date. The rehearsal day counts as ahead until midnight. A past date, a day that isn't a Thursday or a date further ahead is refused with the reason and what is allowed. The program holds no list of rehearsals or time of day: every Thursday counts. Thursdays without a rehearsal and extra rehearsals wait for slice 8, so an absence for a skipped Thursday is accepted.
Rests on: the slice covers a coming Thursday and ordinary Thursdays (004_slice.md); the limit on how far ahead catches a mistyped year.
Settles: V.rehearsal-date.edge, V.rehearsal-date.outside, L.user-input-11.record-request, L.time-10.rehearsal, L.time-08.rehearsal-date, C.states.rehearsal.took-place, C.states.rehearsal.no-rehearsal, S.rehearsal.took-place.record-for-singer-1, S.rehearsal.no-rehearsal.record-for-singer-1, S.rehearsal.no-rehearsal.record-for-singer-2, S.rehearsal.no-rehearsal.record-for-singer-3, S.rehearsal.no-rehearsal.see-who-missing-1, S.rehearsal.no-rehearsal.see-who-missing-2, S.rehearsal.no-rehearsal.again, S.rehearsal.no-rehearsal.reopened, S.rehearsal.no-rehearsal.restart, S.rehearsal.no-rehearsal.second, S.rehearsal.no-rehearsal.time
Under: record-for-singer
Criterion: Given today is Thursday 14 January 2027, when a section leader records an absence for that date, then it is recorded.
Criterion: Given today is Friday 15 January 2027, when a section leader records an absence for 14 January 2027, then it is refused as past and nothing is recorded.
Criterion: Given 13 January 2027 is a Wednesday still ahead, when a section leader records an absence for it, then it is refused, they are told to give a Thursday, and nothing is recorded.
Criterion: Given a Thursday more than 366 days ahead, when a section leader records an absence for it, then it is refused as too far ahead and nothing is recorded.

## A25: Writing and showing dates
Kind: chosen
Says: A date is typed as year-month-day, such as 2027-01-14, the form the register already uses. It must have four digits, two and two; other forms are refused with an example, so day and month are never guessed. Spaces around it are removed. It is a plain date with no time or time zone, kept as typed. It is shown with weekday, month name and year, as in Thursday 14 January 2027, in the Gregorian calendar with the digits 0 to 9. A missing, empty or malformed date records and lists nothing, and the person is told the form to use. A date that does not exist is refused as no such date.
Rests on: the existing commands use this form (README), and a written month can't be mistaken for a day.
Settles: V.rehearsal-date.empty, V.rehearsal-date.missing, V.rehearsal-date.malformed, L.user-input-12.rehearsal-date, L.time-07.rehearsal-date, L.presentation-01.rehearsal-date, L.presentation-06.rehearsal-date, L.presentation-09.rehearsal-date
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader gives the date as 14/01/2027, then it is refused, they are shown the form 2027-01-14, and nothing is recorded.
Criterion: Given no date is given, when someone asks who is missing, then they are told to give a date and no list is shown.
Criterion: Given Robin Vale is recorded for 2027-01-14, when that date's list is shown, then it is headed Thursday 14 January 2027.

## A26: Typing a name
Kind: chosen
Says: A singer is given as one full name, in the order the register has it; a singer and a date are both required. There is no fallback for a missing one. Spaces at the ends are removed and runs of spaces, unusual ones included, count as one. Capitals are ignored using the language's language-neutral case folding, and accented letters typed in different ways count as the same. Accents themselves still count. These rules apply when comparing; the saved spelling stays and is what is shown. No part-name or near match is accepted. Input over 100 characters is refused as too long, not cut; a longer name already saved is shown whole and matches nothing typed until corrected. Empty or missing names are refused with a request for the full name. No printable character is refused. Control and invisible direction characters are refused. If two saved names count as the same, nothing is recorded and both are shown for the register to be corrected. The register keeps one entry per exact name (register.py), so it cannot hold two singers with identical names. Names that merely look alike are told apart by the voice part shown with the confirmation.
Rests on: forgiving spacing and capitals avoids false refusals, and exact matching otherwise avoids picking the wrong singer. All checks are made by the program as it acts, whatever started it.
Settles: L.user-input-01.singer-name, L.user-input-02.record-request, L.user-input-03.singer-name, L.user-input-04.singer-name, L.user-input-05.record-request, L.user-input-07.singer-name, L.user-input-09.singer-name, L.user-input-10.singer-name, L.text-01.singer-name, L.text-02.singer-name, L.text-03.singer-name, L.text-05.singer-name, L.text-10.singer-name, V.singer-name.missing, L.misuse-02.record-request
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader types "  robin   VALE " for a coming Thursday, then the absence is recorded and shown as Robin Vale, tenor.
Criterion: Given no name is given, when a section leader tries to record an absence, then they are asked for the full name and nothing is recorded.
Criterion: Given a typed name of 101 characters, when a section leader tries to record it, then they are told it is too long and nothing is recorded.
Criterion: Given the register holds both Jo Marsh and jo marsh, when a section leader records an absence for Jo Marsh, then they are told two entries match, both are shown, and nothing is recorded.
Criterion: Given a typed name containing a terminal control character, when a section leader tries to record it, then it is refused and the character has no effect on the screen.

## A27: Refusal messages
Kind: chosen
Says: A refusal appears in the same window, in words, straight after the command. It says that nothing was recorded, why, and what to do: check the name against the register, give a real date, use the date form, or choose an allowed Thursday. A successful recording is also said in words (A28). The command also reports failure to whatever ran it. Messages show no program trace.
Rests on: each refusal needs a next step the person can take.
Settles: L.user-input-06.refusal-message, L.user-input-06.record-for-singer-3, L.accessibility-07.record-request, L.accessibility-08.refusal-message
Under: record-for-singer
Criterion: Given Robin Vale is in the register, when a section leader records an absence for 31 February 2027, then words in the same window say there is no such date, that nothing was recorded and to give a real date.
Criterion: Given any refused recording, when the message is shown without colour, then it still says that nothing was recorded and what to do next.

## A28: Recording is one short step
Kind: chosen
Says: Recording is one command with the name and date, with no further steps and no "are you sure". Nothing is saved until it is run; leaving before then leaves nothing. The result names the singer, voice part and date. Running it again, from history or by two people, keeps one absence and says it was already recorded. A command line has no page to reload or go back to. No second person's agreement is needed.
Rests on: a routine confirmation soon goes unread, while a result naming singer, part and date lets a mistake be noticed. Putting one right is A7.
Settles: L.user-action-01.record-request, L.user-action-02.record-request, L.user-action-03.record-request, L.user-action-09.record-request, L.user-action-10.record-request, V.saved-absences.twice
Under: record-for-singer
Criterion: Given Robin Vale is already recorded as missing 14 January 2027, when the same absence is recorded again, then the section leader is told it was already recorded and the list shows Robin Vale once.
Criterion: Given a saved file that holds the same absence twice, when that date is looked at, then the singer is listed once.

## A29: The register's lists at their edges
Kind: chosen
Says: With no singers, recording says the register has no singers and to add them first. With no absences for a date, the list says none is recorded; that does not mean everyone is coming. There is no cut-off on the number of singers or absences. All are read and shown. A duplicate singer entry that the file's format would silently collapse is treated as a damaged register (A20). Singers matching under the name rules are handled by A26.
Rests on: the choir is about 45 singers, and cutting a list would hide absences.
Settles: V.saved-singers.empty, V.saved-singers.long, V.saved-singers.twice, V.saved-absences.empty, V.saved-absences.long
Under: see-who-missing
Criterion: Given a register with no singers, when a section leader records an absence, then they are told it has no singers and nothing is recorded.
Criterion: Given the file lists one exact singer name twice, when a rehearsal is looked at, then they are told the register cannot be used.

## A30: Wrong but readable data
Kind: chosen
Says: Before replacing the register, the program keeps the previous good version beside it, with the same access. That gives one step back only, restored by hand. The program does not detect a well-formed change made by hand or by damage. The list shows names so that people can question them; nothing proves them right. A copy for backup is made while no command is running; because saves are swapped whole (A17), a copy of the register file is a complete version. The register file is the only file needed; the previous version and any temporary files are not read in normal use. If the register file is absent, recording and looking say it cannot be found and do not treat it as a register with no absences. Adding the first singer can still start a new register, and says that it did.
Rests on: a seal or history would not stop someone able to edit the files, and one previous copy helps recover from the latest mistake.
Settles: L.durable-write-09.saved-register, L.durable-write-10.saved-register, L.durable-write-11.saved-register, L.startup-read-09.saved-register, L.startup-read-03.saved-register, L.startup-read-03.see-who-missing-2
Under: see-who-missing
Criterion: Given the register file is absent, when whoever arranges the programme looks at 28 January 2027, then they are told the register cannot be found, not that no absence is recorded.
Criterion: Given a good register, when an absence is saved, then a readable copy of the register as it was just before is kept beside it.

## A31: What the list shows
Kind: chosen
Says: For one date, the list shows each recorded singer's full name and voice part, all in one output that can be scrolled, with a total at the end. It shows nothing else about them, and no shortages (slice 2). It is in one fixed order: voice part in the register's order, then the whole saved name, ignoring capitals, by the language's built-in character order. That is not any one language's alphabetical order, and surnames are not picked out. All meaning is in text, with no colour or symbols needed. Everything can be typed with the keyboard.
Rests on: a short list for about 45 singers needs no paging, and names are saved whole.
Settles: L.limits-08.missing-view, L.text-06.missing-view, L.text-07.missing-view, L.presentation-10.missing-view, L.presentation-12.missing-view, L.stored-data-08.missing-view, L.accessibility-01.record-request, L.accessibility-01.missing-view, L.accessibility-06.missing-view, L.accessibility-08.missing-view
Under: see-who-missing
Criterion: Given all of 45 invented singers are recorded for 14 January 2027, when the date is looked at, then all 45 appear once, with a total of 45.
Criterion: Given absences for two singers, when the list is shown, then each line has only the name and voice part, grouped in the register's order of parts.

## A32: What is recorded about recordings
Kind: chosen
Says: Each saved absence also keeps the date and time it was recorded, by the hall computer's clock; this is not when the singer phoned, and no decision in this slice uses it. It does not say who recorded it, because there are no accounts. There is no separate log, so there is nothing extra to fill up, rotate or fail on its own. Refused attempts and looks are not recorded, so attempts to misuse or read the list will not be noticed. Nobody is told automatically when something breaks: the person running the command sees the failure and has to pass it on. The time comes from the one hall computer's clock. The saved time can be changed by anyone who can change the file. Names are stored only as the register's own spelling.
Rests on: the time helps with a disputed entry without making another copy of names. The risk of open access is A5.
Settles: L.logging-01.record-request, L.logging-02.record-request, L.logging-04.singer-name, L.logging-05.record-request, L.logging-06.record-request, L.logging-10.record-request, L.time-12.absence, L.logging-09.record-request, L.logging-11.record-request, L.stored-data-12.missing-view, W.noticed
Under: record-for-singer
Criterion: Given a section leader records an absence, when the saved entry is inspected, then it holds the singer, the rehearsal date and the time it was recorded.

## A33: Keeping names from leaking
Kind: chosen
Says: Singers' names and absences go to no log or monitoring service. Unexpected errors show a short plain message with no trace and no saved data. A refusal may repeat the name just typed; an ambiguous-name refusal shows only the matching names. Successful output goes only to the window that asked. Tests and examples use invented names.
Rests on: only what the person needs for the action should be shown or copied.
Settles: L.logging-03.singer-name, X.singer-details.logs, X.singer-details.errors-inside, X.singer-details.errors-shown, X.singer-details.telemetry, X.singer-details.samples, X.singer-details.replies
Under: new: names-do-not-leak
Criterion: Given a damaged register containing invented names, when a command fails on it, then no singer's name, saved entry or program trace is shown.
Criterion: Given the tests and examples added for this slice, when they are read, then their singers are invented and none is copied from the register.

## A34: Protecting the saved file
Kind: chosen
Says: The singers' names and absences, both sensitive, are stored on the hall's computer. The slice adds no encryption and so no key. The saved register and its previous copy rely on the computer's own sign-in and file permissions, and are never made readable more widely than the register was. This does not protect them from someone who can use that computer account, or take an unprotected disk or copy; accepting access at the computer is A5.
Rests on: a key kept beside the program would not keep out someone using the same account, and a lost key would lose the register.
Settles: L.stored-data-10.saved-register, L.stored-data-01.absence, L.stored-data-01.saved-register, L.stored-data-02.saved-register, L.stored-data-03.saved-register, L.stored-data-04.saved-register, T.singer-details.saved-register, W.sensitive, W.prize
Under: new: names-do-not-leak
Criterion: Given a register readable only by its own computer account, when an absence is saved, then the register and its previous copy are still readable only by that account.

## A35: Harm to the register through a request
Kind: chosen
Says: A recording takes only a name and a date, and can only add one absence. Extra values are refused. Typed text is only ever treated as text, never run as a command or used as a file path. Repeating it adds nothing (A28); recording many different valid absences is possible for anyone allowed to run it (A5), limited by singers times Thursdays in range, with no speed limit. Fast recording is not treated or flagged as abuse.
Rests on: a narrow command cannot be used to edit singers or attendance.
Settles: T.saved-register.record-request, L.misuse-04.record-request, L.misuse-03.record-request, L.misuse-07.record-request
Under: record-for-singer
Criterion: Given a register with singers and attendance, when an absence is recorded with an extra value added to the command, then it is refused and the file is unchanged.
Criterion: Given a register with singers and attendance, when an absence is recorded successfully, then every singer, voice part and attendance mark is unchanged.

## A36: If it cannot be used for an hour
Kind: chosen
Says: Section leaders can't record and the list can't be read. A section leader notes the phone call by hand and records it when the program works again. If this happens close to the rehearsal, names have to be passed on by hand.
Rests on: the register is on one computer, and this slice adds no second route.
Settles: W.unavailable
Under: record-for-singer

## A37: A name not in the register
Kind: chosen
Says: For a name that isn't in the register, recording is refused and nothing is saved or listed, however often it is tried, including after restarts, by two people or after a long time. Looking neither adds nor lists them, apart from a saved absence that has lost its singer (A19). Once added to the register, the singer can be recorded.
Rests on: record-for-singer / 2 and the register's way of adding singers.
Settles: S.singer-in-the-register.not-in-register.record-for-singer-1, S.singer-in-the-register.not-in-register.record-for-singer-3, S.singer-in-the-register.not-in-register.see-who-missing-1, S.singer-in-the-register.not-in-register.see-who-missing-2, S.singer-in-the-register.not-in-register.again, S.singer-in-the-register.not-in-register.reopened, S.singer-in-the-register.not-in-register.restart, S.singer-in-the-register.not-in-register.second, S.singer-in-the-register.not-in-register.time, C.states.singer-in-the-register.not-in-register
Under: record-for-singer
Criterion: Given the register has no Sam Reed, when an absence for Sam Reed is tried twice, then both times they are told there is no such singer and nothing is saved.

## A38: Singers in the register, whatever else is true of them
Kind: chosen
Says: A singer listed in the register can have an absence recorded, including one who has been asked whether they're still coming or who has in fact left: the register keeps no mark for either. An unknown name or impossible date is refused as the slice says. The list shows only those recorded for the chosen date. Repeats and two people recording keep one entry; reopening, restarting or time passing changes neither the singer nor a saved absence.
Rests on: the register holds names, voice parts and attendance only; asking singers who stopped coming is the next activity, and removal is A8.
Settles: S.singer-in-the-register.in-register.record-for-singer-2, S.singer-in-the-register.in-register.see-who-missing-2, S.singer-in-the-register.in-register.again, S.singer-in-the-register.in-register.reopened, S.singer-in-the-register.in-register.restart, S.singer-in-the-register.in-register.second, S.singer-in-the-register.in-register.time, S.singer-in-the-register.asked-if-still-coming.*, S.singer-in-the-register.left-choir.*, C.states.singer-in-the-register.asked-if-still-coming
Under: record-for-singer

## A39: A coming rehearsal
Kind: chosen
Says: For a coming Thursday, a valid recording is saved and shown; an unknown singer or impossible date is refused. The list shows those recorded for that date, or says none is recorded. Repeats and two recordings follow A28 and A21. A reload or restart keeps what was finished. When its date has passed by the computer's date, it takes no new absence.
Rests on: record-for-singer / 1 to 3 and see-who-missing / 1 and 2, with A17, A21, A24 and A28.
Settles: S.rehearsal.coming-up.again, S.rehearsal.coming-up.reopened, S.rehearsal.coming-up.restart, S.rehearsal.coming-up.second, S.rehearsal.coming-up.time
Under: see-who-missing

## A40: A rehearsal that has passed
Kind: chosen
Says: A passed Thursday takes no new absence, however it is tried or repeated; other refusals still say there is no such singer or date. Its saved absences can still be looked at, and the list says the rehearsal has passed. With none saved, it says none is recorded. Restarting, a second person and passing time change nothing saved. Marking who came works as before.
Rests on: the slice records only for a coming rehearsal, and keeping past entries removes nothing.
Settles: S.rehearsal.took-place.record-for-singer-2, S.rehearsal.took-place.record-for-singer-3, S.rehearsal.took-place.see-who-missing-1, S.rehearsal.took-place.see-who-missing-2, S.rehearsal.took-place.again, S.rehearsal.took-place.reopened, S.rehearsal.took-place.restart, S.rehearsal.took-place.second, S.rehearsal.took-place.time, S.absence.rehearsal-passed.*, C.states.absence.rehearsal-passed
Under: see-who-missing
Criterion: Given Robin Vale was recorded as missing 14 January 2027 and today is 15 January 2027, when that date is looked at, then Robin Vale is shown and the list says the rehearsal has passed.

## A41: A recorded absence
Kind: chosen
Says: A saved absence stays through restarts and time. It shows for its own date only. Recording it again keeps one (A28). A refused attempt changes nothing. Recording another singer at the same moment keeps both (A21). The attendance marks are separate: if the singer comes after all, they can be marked as coming and the absence remains.
Rests on: see-who-missing / 1 and the slice only adding absences; putting one right is A7.
Settles: S.absence.recorded.*
Under: see-who-missing
Criterion: Given an absence has been recorded, when the computer is restarted and its date is looked at, then the singer is still shown.

## A43: Recording a singer's absence for a coming rehearsal
Kind: fact
Says: The section leader is shown that the singer is recorded as missing that date.
Rests on: record-for-singer / 1
Settles: S.singer-in-the-register.in-register.record-for-singer-1, S.rehearsal.coming-up.record-for-singer-1
Under: record-for-singer

## A44: An unknown singer
Kind: fact
Says: The person is told there is no such singer, and no absence is shown for that name.
Rests on: record-for-singer / 2
Settles: S.singer-in-the-register.not-in-register.record-for-singer-2, S.rehearsal.coming-up.record-for-singer-2
Under: record-for-singer

## A45: A date that does not exist
Kind: fact
Says: The person is told there is no such date, and no absence is recorded.
Rests on: record-for-singer / 3
Settles: S.singer-in-the-register.in-register.record-for-singer-3, S.rehearsal.coming-up.record-for-singer-3
Under: record-for-singer

## A46: Who is shown as missing
Kind: fact
Says: Before the night, a singer recorded for that date is shown as missing it, and one recorded only for another date is not.
Rests on: see-who-missing / 1
Settles: S.singer-in-the-register.in-register.see-who-missing-1, S.rehearsal.coming-up.see-who-missing-1
Under: see-who-missing

## A47: A rehearsal with no absence
Kind: fact
Says: The person is told that no absence is recorded for it.
Rests on: see-who-missing / 2
Settles: S.rehearsal.coming-up.see-who-missing-2
Under: see-who-missing

## A42: Word after Tuesday evening
Kind: chosen
Says: In this slice an absence recorded after Tuesday evening, up to the end of the rehearsal day, is accepted and listed like any other, with no late mark. The program does not warn anyone, so a list read earlier can miss it. Repeats, refusals, restarts and two people behave as for any absence. What late word should mean is slice 6.
Rests on: late word is left for slice 6 (004_slice.md), and hiding a known absence would make the list wrong.
Settles: S.absence.recorded-after-tuesday.*, C.states.absence.recorded-after-tuesday
Under: record-for-singer
Criterion: Given today is Wednesday 13 January 2027, when an absence is recorded for 14 January 2027, then it appears in that date's list.
