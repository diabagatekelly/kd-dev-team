# Answered

<!-- drawn from: 2972384866 -->

Drawn by script from the answers. Nothing here is written by hand: change the answers and draw again.

## Criteria

- **record-for-singer / A1.1**: Given the hall's computer with its network connected, when a section leader runs the command that records an absence, then the program opens no network address and makes no network connection.
- **new: no-added-components / A2.2**: Given a computer with the language installed and nothing added, when the program is run, then recording and looking both work.
- **record-for-singer / A17.3**: Given a section leader is recording an absence for Robin Vale, when the program is stopped before it says the absence is recorded, then on the next look the register opens with all earlier singers, attendance and absences, and Robin Vale's absence is either shown whole or not shown at all.
- **record-for-singer / A17.4**: Given an unfinished save file has been left beside the register, when whoever arranges the programme looks at a rehearsal, then they see what the last finished save held.
- **record-for-singer / A18.5**: Given the disk has no room for a save, when a section leader records an absence for Robin Vale on 14 January 2027, then they are told it was not recorded and why, and the earlier singers, attendance and absences are unchanged.
- **record-for-singer / A18.6**: Given saving fails for any reason, when a section leader records an absence, then they are never told that it is recorded.
- **see-who-missing / A19.7**: Given a saved absence on 14 January 2027 names Sam Reed, who is not in the register, when that date is looked at, then Sam Reed is shown as recorded missing and as not in the register.
- **see-who-missing / A20.8**: Given the register file is cut short, when whoever arranges the programme looks at 14 January 2027, then they are told the register cannot be used and which file it is, and are not told that no absence is recorded.
- **see-who-missing / A20.9**: Given the file where the register belongs holds something else, when a section leader records an absence, then it is refused and the file is left as it was.
- **record-for-singer / A21.10**: Given two windows are open, when absences for Robin Vale and Jo Marsh are recorded for 14 January 2027 at the same moment, then the list for that date shows both.
- **record-for-singer / A21.11**: Given another command holds the register for more than 5 seconds, when a section leader records an absence, then they are told it is in use, that nothing was recorded and to try again.
- **see-who-missing / A22.12**: Given a register that can be read but not changed, when whoever arranges the programme looks at 14 January 2027, then the list is shown and the file is unchanged.
- **see-who-missing / A22.13**: Given a list for 14 January 2027 has been shown and an absence is then recorded for that date, when the list is asked for again, then it includes that absence and shows the time it was made.
- **new: carry-the-register-forward / A23.14**: Given a register saved by today's program, when the new program first looks at a coming Thursday, then it says no absence is recorded and every singer and attendance mark is unchanged.
- **new: carry-the-register-forward / A23.15**: Given absences have been saved, when today's program runs its report and exits, with nothing else running, then the new program still shows those absences.
- **new: carry-the-register-forward / A23.16**: Given a register marked as written by a later version, when a section leader records an absence, then it is refused, they are told a newer program wrote it and to use that one, and the file is unchanged.
- **record-for-singer / A24.17**: Given today is Thursday 14 January 2027, when a section leader records an absence for that date, then it is recorded.
- **record-for-singer / A24.18**: Given today is Friday 15 January 2027, when a section leader records an absence for 14 January 2027, then it is refused as past and nothing is recorded.
- **record-for-singer / A24.19**: Given 13 January 2027 is a Wednesday still ahead, when a section leader records an absence for it, then it is refused, they are told to give a Thursday, and nothing is recorded.
- **record-for-singer / A24.20**: Given a Thursday more than 366 days ahead, when a section leader records an absence for it, then it is refused as too far ahead and nothing is recorded.
- **record-for-singer / A25.21**: Given Robin Vale is in the register, when a section leader gives the date as 14/01/2027, then it is refused, they are shown the form 2027-01-14, and nothing is recorded.
- **record-for-singer / A25.22**: Given no date is given, when someone asks who is missing, then they are told to give a date and no list is shown.
- **record-for-singer / A25.23**: Given Robin Vale is recorded for 2027-01-14, when that date's list is shown, then it is headed Thursday 14 January 2027.
- **record-for-singer / A26.24**: Given Robin Vale is in the register, when a section leader types "  robin   VALE " for a coming Thursday, then the absence is recorded and shown as Robin Vale, tenor.
- **record-for-singer / A26.25**: Given no name is given, when a section leader tries to record an absence, then they are asked for the full name and nothing is recorded.
- **record-for-singer / A26.26**: Given a typed name of 101 characters, when a section leader tries to record it, then they are told it is too long and nothing is recorded.
- **record-for-singer / A26.27**: Given the register holds both Jo Marsh and jo marsh, when a section leader records an absence for Jo Marsh, then they are told two entries match, both are shown, and nothing is recorded.
- **record-for-singer / A26.28**: Given a typed name containing a terminal control character, when a section leader tries to record it, then it is refused and the character has no effect on the screen.
- **record-for-singer / A27.29**: Given Robin Vale is in the register, when a section leader records an absence for 31 February 2027, then words in the same window say there is no such date, that nothing was recorded and to give a real date.
- **record-for-singer / A27.30**: Given any refused recording, when the message is shown without colour, then it still says that nothing was recorded and what to do next.
- **record-for-singer / A28.31**: Given Robin Vale is already recorded as missing 14 January 2027, when the same absence is recorded again, then the section leader is told it was already recorded and the list shows Robin Vale once.
- **record-for-singer / A28.32**: Given a saved file that holds the same absence twice, when that date is looked at, then the singer is listed once.
- **see-who-missing / A29.33**: Given a register with no singers, when a section leader records an absence, then they are told it has no singers and nothing is recorded.
- **see-who-missing / A29.34**: Given the file lists one exact singer name twice, when a rehearsal is looked at, then they are told the register cannot be used.
- **see-who-missing / A30.35**: Given the register file is absent, when whoever arranges the programme looks at 28 January 2027, then they are told the register cannot be found, not that no absence is recorded.
- **see-who-missing / A30.36**: Given a good register, when an absence is saved, then a readable copy of the register as it was just before is kept beside it.
- **see-who-missing / A31.37**: Given all of 45 invented singers are recorded for 14 January 2027, when the date is looked at, then all 45 appear once, with a total of 45.
- **see-who-missing / A31.38**: Given absences for two singers, when the list is shown, then each line has only the name and voice part, grouped in the register's order of parts.
- **record-for-singer / A32.39**: Given a section leader records an absence, when the saved entry is inspected, then it holds the singer, the rehearsal date and the time it was recorded.
- **new: names-do-not-leak / A33.40**: Given a damaged register containing invented names, when a command fails on it, then no singer's name, saved entry or program trace is shown.
- **new: names-do-not-leak / A33.41**: Given the tests and examples added for this slice, when they are read, then their singers are invented and none is copied from the register.
- **new: names-do-not-leak / A34.42**: Given a register readable only by its own computer account, when an absence is saved, then the register and its previous copy are still readable only by that account.
- **record-for-singer / A35.43**: Given a register with singers and attendance, when an absence is recorded with an extra value added to the command, then it is refused and the file is unchanged.
- **record-for-singer / A35.44**: Given a register with singers and attendance, when an absence is recorded successfully, then every singer, voice part and attendance mark is unchanged.
- **record-for-singer / A37.45**: Given the register has no Sam Reed, when an absence for Sam Reed is tried twice, then both times they are told there is no such singer and nothing is saved.
- **see-who-missing / A40.46**: Given Robin Vale was recorded as missing 14 January 2027 and today is 15 January 2027, when that date is looked at, then Robin Vale is shown and the list says the rehearsal has passed.
- **see-who-missing / A41.47**: Given an absence has been recorded, when the computer is restarted and its date is looked at, then the singer is still shown.
- **record-for-singer / A42.48**: Given today is Wednesday 13 January 2027, when an absence is recorded for 14 January 2027, then it appears in that date's list.

## For the owner, by harm

### A6: When this counts as working, and how the list reaches the arranger (high)
The slice works only if whoever arranges the programme gets the names in time to act. The list is on the hall's computer, and no document says they can get to that computer before rehearsal night. Nor does any say how often the program may fail, or how slow is too slow.

- whoever arranges the programme looks at the hall's computer themself
- someone at the hall looks and passes the names on
- the list must be readable away from the hall, which this slice does not provide

Recommended: look at the hall's computer themself, if they can get there in time, because it needs nothing more than this slice.
If left: the slice shows the list on the hall's computer only, and it may not be seen in time to rearrange the programme. How soon and how often it must work cannot be judged until this is known.
Questions waiting on it: 1

### A7: Mistaken or changed absences (high)
Nothing in this slice takes back or corrects a recorded absence. A wrong singer or date, or a singer whose plans change, stays shown as missing. The requirements have no item for it (question 3).

- add taking back an absence to the requirements and to this slice
- add it to the requirements as a later slice
- leave it out, and keep any correction by hand outside the program

Recommended: add it to this slice, because a mistake could otherwise make a voice part look short when it isn't, with two pieces needing at least four tenors (000_problem.md).
If left: a recorded absence cannot be put right in the program.
Questions waiting on it: 4

### A10: The register file is in the code repository (high)
`data/register.json` is a file tracked in this repository, which has a GitHub repository. I have not opened it, so I don't know whether its names are real, and I haven't checked who can see the repository. If absences are saved to a tracked file, a commit and push would send them there too. Taking a file out of the latest version does not take it out of the history.

- stop tracking the file and decide separately about its history, if it holds real names
- keep it tracked because its contents are invented
- keep real names tracked and accept who can see them

Recommended: if the names are real, stop tracking the file before any absence is saved, and then decide about the history, because a push copies the names off the hall's computer.
If left: the file stays tracked, and any commit of it carries what it holds.
Questions waiting on it: 1

### A5: Who may record and see (medium)
Today there are no accounts, and whoever is at the hall's computer can use the register. With absences added, that person could see who will be away on which evening, record a false absence, or open and change the saved file. Nothing would show who did it. Whether others than whoever arranges the programme may see is also unconfirmed (requirements, question 2). Singers need no password either way.

- accept that whoever can use the hall's computer can record, see and change absences, as with the register today
- limit recording and seeing to section leaders and whoever arranges the programme, which needs a way to tell who they are

Recommended: accept it as with the register today, because the register has no accounts, and a check inside the program would not stop someone opening the saved file.
If left: the slice is no more protected than the register is today.
Questions waiting on it: 12

### A9: How long absences are kept, and what duties apply (medium)
No document says how long past absences are kept, or whether any law or choir rule applies to holding singers' names with the dates they are away. I have read nothing about either, so I make no claim.

- keep past absences with the register until you say otherwise, and check what duties the choir has
- remove each absence a set time after its rehearsal

Recommended: keep them for now and check the duties, because keeping them can be changed later and removal cannot.
If left: nothing removes a past absence.
Questions waiting on it: 3

### A11: A copy away from the hall's computer (medium)
No document says that any spare copy of the register exists. The program will keep the previous version beside the register (A30), which does not help if the computer is lost or its disk fails.

- someone copies the register to a second device on a regular day
- accept that losing the computer loses the register and the absences

Recommended: copy it regularly to a device the choir controls, because the copy takes little work and a lost register would have to be rebuilt by hand.
If left: the only copies this slice makes are on the hall's computer.
Questions waiting on it: 2

### A8: Singers who have left (low)
The documents give no way to remove a singer. The register has no mark for someone who has left, so they can still have an absence recorded.

- leave removing a singer out of this work
- add it to the requirements

Recommended: leave it out, because it does not stop anyone recording or seeing an absence.
If left: someone who has left stays in the register.
Questions waiting on it: 2

## Decided by the owner

Nothing.

## To test, by harm

- A13 (high): Whether anything on the hall's computer removes, restores or syncs the program's folder on its own is not known. Test: look on the hall's computer for sync, cleanup and restore-on-restart software covering the program's folder, and note where copies of it go.
- A12 (medium): What the hall computer's system and disk do when power is lost just after a save is not known. Test: find out the computer's system, file system and kind of disk, read what its documentation promises about flushing a file to disk and about a failed flush, and cut power just after a recording on a copy of the register with invented names.
- A14 (medium): Whether the hall computer's date and time zone are right, and stay right after it has been switched off, is not known. The program depends on them to tell whether a Thursday is still ahead (A24). Test: compare the computer's date, time and time zone with a trusted clock, then again after it has been off overnight with its network as usual.
- A15 (low): The commands are typed and read in the computer's own text window. How that window works with a screen reader, shows keyboard focus, handles larger text and contrasts text is not known. Test: on the hall's computer, record and look using the keyboard only, with text at twice the size, and with its screen reader if anyone needs one; check that focus, prompts and names can be read.
- A16 (low): Whether the computer's text window can take and show every character in the singers' names, including accents and other scripts, is not known. Test: on a copy of the program with invented names that have accents, an apostrophe, a long double-barrelled name and right-to-left text, type each one, record it and view the list.

## Chosen without asking; the owner can overturn any of these

- A1: Recording and looking are added as commands of the existing register program on the hall's computer. They open no network address, serve no page and send nothing anywhere. Because: the register is already used by command on that computer by the section leaders (the README and register.py), no document asks for a page, and the slice needs nothing from outside. Whether singers reach it from home matters only to slice 3.
- A2: The slice uses only the language and its standard library. No component written by someone else is added. Because: recording and listing names and dates needs none, and the existing program uses none (register.py).
- A17: A save leaves either everything as it was or everything including the change, never part of each. It is written aside and then swapped in. A recording changes no singer and no attendance. A leftover unfinished file is never read as the register. It is ignored, and its recording counts as not made. Because: replacing a file in one step is the usual way to avoid a half-written one; the program today writes straight over the file (register.py). What power loss does is left to A12.
- A18: The program says an absence is recorded only after the save has been flushed to disk and swapped in without an error. If any step reports an error, it says the absence was not recorded, or that it cannot tell, and asks the section leader to look at that date before trying again. It does not retry by itself. A full disk is reported the same way and the earlier register is left as it was. Because: a person must not be told something is saved when it may not be. How much the disk really keeps is left to A12.
- A19: Each saved absence names a singer in the register and a date. If a saved absence names nobody in the register, the list still shows that name, marked as not in the register. Nothing is silently dropped or removed. Because: hiding it could make a voice part look fuller than it is. The singer check and the save happen under the same hold on the register (A21).
- A20: If the file cannot be read or opened, or is not shaped like the choir's register (including a missing or wrong-typed list of singers, a bad singer entry or a bad absence entry), recording and looking stop. They say the register cannot be used, name the file and say to get help or restore a good copy. Nothing is written over it and no partial list is shown. A register that has no absences yet, because it predates them, is valid. The program never repairs or rescues a file by itself. After someone restores or repairs it by hand, the same checks apply, and the person restoring it must check recent absences because later ones may be gone. Because: a wrong or partial list would mislead more than a clear refusal.
- A21: Every command of the new program that changes the register, adding a singer and marking attendance included, holds it for itself from reading to saving. A second one waits up to 5 seconds, then says the register is in use, changes nothing and asks the person to try again. It is not repeated automatically after that. A hold left by a program that has stopped does not block later ones. Looking reads one whole saved version. The hold covers only this program on this one computer. It does not cover the earlier program, an editor, or a folder shared or synced elsewhere. Because: without it, two section leaders saving from the same starting point could lose one recording.
- A22: Looking at a rehearsal changes nothing. The attendance report also stops saving. The program today saves after every command, the report included (register.py). Where the register can be read but not changed, looking works, and recording says it cannot save. A list is a picture of the moment it was shown. It says when it was made, and does not update itself, in another window or after the computer sleeps. Running the command again shows every absence confirmed before it. Because: an old look that saves could overwrite a newer recording.
- A23: The register saved today is carried forward as it is. It has no absences, which means none are recorded; nothing is made up for past rehearsals and no old data is erased. Using the new program needs no separate update step. Bringing back an older copy works the same, with no time limit, but it lacks any absence recorded after it was made. A register marked as written by a later version is refused for both looking and changing. The earlier program must not be run alongside the new one, because it saves after every command and does not take part in the hold (A21). If it is put back, it must leave saved absences intact. Because: carrying everything forward loses nothing, and a first save is as whole as any other (A17).
- A24: An absence is recorded only for a Thursday from today to 366 days ahead, by the hall computer's own date. The rehearsal day counts as ahead until midnight. A past date, a day that isn't a Thursday or a date further ahead is refused with the reason and what is allowed. The program holds no list of rehearsals or time of day: every Thursday counts. Thursdays without a rehearsal and extra rehearsals wait for slice 8, so an absence for a skipped Thursday is accepted. Because: the slice covers a coming Thursday and ordinary Thursdays (004_slice.md); the limit on how far ahead catches a mistyped year.
- A25: A date is typed as year-month-day, such as 2027-01-14, the form the register already uses. It must have four digits, two and two; other forms are refused with an example, so day and month are never guessed. Spaces around it are removed. It is a plain date with no time or time zone, kept as typed. It is shown with weekday, month name and year, as in Thursday 14 January 2027, in the Gregorian calendar with the digits 0 to 9. A missing, empty or malformed date records and lists nothing, and the person is told the form to use. A date that does not exist is refused as no such date. Because: the existing commands use this form (README), and a written month can't be mistaken for a day.
- A26: A singer is given as one full name, in the order the register has it; a singer and a date are both required. There is no fallback for a missing one. Spaces at the ends are removed and runs of spaces, unusual ones included, count as one. Capitals are ignored using the language's language-neutral case folding, and accented letters typed in different ways count as the same. Accents themselves still count. These rules apply when comparing; the saved spelling stays and is what is shown. No part-name or near match is accepted. Input over 100 characters is refused as too long, not cut; a longer name already saved is shown whole and matches nothing typed until corrected. Empty or missing names are refused with a request for the full name. No printable character is refused. Control and invisible direction characters are refused. If two saved names count as the same, nothing is recorded and both are shown for the register to be corrected. The register keeps one entry per exact name (register.py), so it cannot hold two singers with identical names. Names that merely look alike are told apart by the voice part shown with the confirmation. Because: forgiving spacing and capitals avoids false refusals, and exact matching otherwise avoids picking the wrong singer. All checks are made by the program as it acts, whatever started it.
- A27: A refusal appears in the same window, in words, straight after the command. It says that nothing was recorded, why, and what to do: check the name against the register, give a real date, use the date form, or choose an allowed Thursday. A successful recording is also said in words (A28). The command also reports failure to whatever ran it. Messages show no program trace. Because: each refusal needs a next step the person can take.
- A28: Recording is one command with the name and date, with no further steps and no "are you sure". Nothing is saved until it is run; leaving before then leaves nothing. The result names the singer, voice part and date. Running it again, from history or by two people, keeps one absence and says it was already recorded. A command line has no page to reload or go back to. No second person's agreement is needed. Because: a routine confirmation soon goes unread, while a result naming singer, part and date lets a mistake be noticed. Putting one right is A7.
- A29: With no singers, recording says the register has no singers and to add them first. With no absences for a date, the list says none is recorded; that does not mean everyone is coming. There is no cut-off on the number of singers or absences. All are read and shown. A duplicate singer entry that the file's format would silently collapse is treated as a damaged register (A20). Singers matching under the name rules are handled by A26. Because: the choir is about 45 singers, and cutting a list would hide absences.
- A30: Before replacing the register, the program keeps the previous good version beside it, with the same access. That gives one step back only, restored by hand. The program does not detect a well-formed change made by hand or by damage. The list shows names so that people can question them; nothing proves them right. A copy for backup is made while no command is running; because saves are swapped whole (A17), a copy of the register file is a complete version. The register file is the only file needed; the previous version and any temporary files are not read in normal use. If the register file is absent, recording and looking say it cannot be found and do not treat it as a register with no absences. Adding the first singer can still start a new register, and says that it did. Because: a seal or history would not stop someone able to edit the files, and one previous copy helps recover from the latest mistake.
- A31: For one date, the list shows each recorded singer's full name and voice part, all in one output that can be scrolled, with a total at the end. It shows nothing else about them, and no shortages (slice 2). It is in one fixed order: voice part in the register's order, then the whole saved name, ignoring capitals, by the language's built-in character order. That is not any one language's alphabetical order, and surnames are not picked out. All meaning is in text, with no colour or symbols needed. Everything can be typed with the keyboard. Because: a short list for about 45 singers needs no paging, and names are saved whole.
- A32: Each saved absence also keeps the date and time it was recorded, by the hall computer's clock; this is not when the singer phoned, and no decision in this slice uses it. It does not say who recorded it, because there are no accounts. There is no separate log, so there is nothing extra to fill up, rotate or fail on its own. Refused attempts and looks are not recorded, so attempts to misuse or read the list will not be noticed. Nobody is told automatically when something breaks: the person running the command sees the failure and has to pass it on. The time comes from the one hall computer's clock. The saved time can be changed by anyone who can change the file. Names are stored only as the register's own spelling. Because: the time helps with a disputed entry without making another copy of names. The risk of open access is A5.
- A33: Singers' names and absences go to no log or monitoring service. Unexpected errors show a short plain message with no trace and no saved data. A refusal may repeat the name just typed; an ambiguous-name refusal shows only the matching names. Successful output goes only to the window that asked. Tests and examples use invented names. Because: only what the person needs for the action should be shown or copied.
- A34: The singers' names and absences, both sensitive, are stored on the hall's computer. The slice adds no encryption and so no key. The saved register and its previous copy rely on the computer's own sign-in and file permissions, and are never made readable more widely than the register was. This does not protect them from someone who can use that computer account, or take an unprotected disk or copy; accepting access at the computer is A5. Because: a key kept beside the program would not keep out someone using the same account, and a lost key would lose the register.
- A35: A recording takes only a name and a date, and can only add one absence. Extra values are refused. Typed text is only ever treated as text, never run as a command or used as a file path. Repeating it adds nothing (A28); recording many different valid absences is possible for anyone allowed to run it (A5), limited by singers times Thursdays in range, with no speed limit. Fast recording is not treated or flagged as abuse. Because: a narrow command cannot be used to edit singers or attendance.
- A36: Section leaders can't record and the list can't be read. A section leader notes the phone call by hand and records it when the program works again. If this happens close to the rehearsal, names have to be passed on by hand. Because: the register is on one computer, and this slice adds no second route.
- A37: For a name that isn't in the register, recording is refused and nothing is saved or listed, however often it is tried, including after restarts, by two people or after a long time. Looking neither adds nor lists them, apart from a saved absence that has lost its singer (A19). Once added to the register, the singer can be recorded. Because: record-for-singer / 2 and the register's way of adding singers.
- A38: A singer listed in the register can have an absence recorded, including one who has been asked whether they're still coming or who has in fact left: the register keeps no mark for either. An unknown name or impossible date is refused as the slice says. The list shows only those recorded for the chosen date. Repeats and two people recording keep one entry; reopening, restarting or time passing changes neither the singer nor a saved absence. Because: the register holds names, voice parts and attendance only; asking singers who stopped coming is the next activity, and removal is A8.
- A39: For a coming Thursday, a valid recording is saved and shown; an unknown singer or impossible date is refused. The list shows those recorded for that date, or says none is recorded. Repeats and two recordings follow A28 and A21. A reload or restart keeps what was finished. When its date has passed by the computer's date, it takes no new absence. Because: record-for-singer / 1 to 3 and see-who-missing / 1 and 2, with A17, A21, A24 and A28.
- A40: A passed Thursday takes no new absence, however it is tried or repeated; other refusals still say there is no such singer or date. Its saved absences can still be looked at, and the list says the rehearsal has passed. With none saved, it says none is recorded. Restarting, a second person and passing time change nothing saved. Marking who came works as before. Because: the slice records only for a coming rehearsal, and keeping past entries removes nothing.
- A41: A saved absence stays through restarts and time. It shows for its own date only. Recording it again keeps one (A28). A refused attempt changes nothing. Recording another singer at the same moment keeps both (A21). The attendance marks are separate: if the singer comes after all, they can be marked as coming and the absence remains. Because: see-who-missing / 1 and the slice only adding absences; putting one right is A7.
- A42: In this slice an absence recorded after Tuesday evening, up to the end of the rehearsal day, is accepted and listed like any other, with no late mark. The program does not warn anyone, so a list read earlier can miss it. Repeats, refusals, restarts and two people behave as for any absence. What late word should mean is slice 6. Because: late word is left for slice 6 (004_slice.md), and hiding a known absence would make the list wrong.
