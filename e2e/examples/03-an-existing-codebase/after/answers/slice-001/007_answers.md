# Answers: slice 1

## A1: An absence for a singer in the register is recorded and shown
Kind: fact
Says: a section leader's absence for a singer in the register and a coming Thursday is recorded, and the singer is shown as going to miss it.
Rests on: record-for-singer / 1
Settles: S.singer.in-register.record-for-singer-1, S.rehearsal.coming.record-for-singer-1

## A2: The view shows each voice part's names and numbers
Kind: fact
Says: for a rehearsal the view shows, under each voice part, the names of those with an absence recorded and how many that is of the part.
Rests on: see-who-will-miss / 1
Settles: S.singer.in-register.see-who-will-miss-1, S.rehearsal.coming.see-who-will-miss-1, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.see-who-will-miss-1

## A3: An absence counts only for its own rehearsal
Kind: fact
Says: an absence for one Thursday is not shown or counted for another.
Rests on: see-who-will-miss / 2
Settles: S.singer.in-register.see-who-will-miss-2, S.rehearsal.coming.see-who-will-miss-2, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.see-who-will-miss-2, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.see-who-will-miss-2

## A4: An unknown name is refused
Kind: fact
Says: where the register has no singer of that name, the section leader is told so and nothing is recorded.
Rests on: record-for-singer / 2
Settles: S.singer.in-register.record-for-singer-2, S.rehearsal.coming.record-for-singer-2, S.singer.not-in-register.record-for-singer-1, S.singer.not-in-register.record-for-singer-2, S.singer.not-in-register.record-for-singer-3, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.record-for-singer-2

## A5: A passed rehearsal is refused
Kind: fact
Says: an absence for a rehearsal whose date has passed is refused, the section leader is told it has passed, and nothing is recorded.
Rests on: record-for-singer / 3
Settles: S.singer.in-register.record-for-singer-3, S.rehearsal.coming.record-for-singer-3, S.rehearsal.passed.record-for-singer-1, S.rehearsal.passed.record-for-singer-3, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.record-for-singer-3

## A6: A passed rehearsal and an unknown name together
Kind: chosen
Says: when both rules refuse, nothing is recorded and the section leader is told of each thing that is wrong.
Rests on: telling everything at once saves a second refused try.
Settles: S.rehearsal.passed.record-for-singer-2
Under: record-for-singer
Criterion: Given a name that is not in the register and a rehearsal that has passed, when a section leader tries to record that absence, then they are told both that there is no such singer and that the rehearsal has passed, and nothing is recorded.

## A7: One absence for a singer and a rehearsal, however often it is recorded
Kind: chosen
Says: recording an absence that is already recorded changes nothing; the section leader is told it was already recorded.
Rests on: a second copy would count one singer twice and make a part look shorter than it is.
Settles: S.singer.in-register.again, S.rehearsal.coming.again, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.record-for-singer-1, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.again, V.kept-absence.twice
Under: record-for-singer
Criterion: Given a singer's absence for a coming rehearsal is already recorded, when it is recorded again, then the section leader is told it was already recorded and the view counts that singer once.

## A8: What is asked before an absence is saved
Kind: chosen
Says: because a wrong absence misleads until someone notices and removes it, the singer's name, voice part and the rehearsal date with its weekday are shown and a yes is asked before saving. Every rule is checked before that and again at the save. Anything left before the yes records nothing.
Rests on: confirming the details that could be wrong stops a slip before it changes the numbers.
Settles: L.user-action-09.record-request, L.lifecycle-03.record-request, L.user-action-05.record-request
Under: record-for-singer
Criterion: Given a section leader has named a singer and a coming Thursday, when they leave without saying yes to the shown name, voice part and date, then no absence is recorded.

## A9: When an absence counts as recorded
Kind: chosen
Says: the section leader is told it is recorded only after the save has completed and reached the computer's storage. Closing or losing power before that message means it must be looked for in the view and recorded again if absent.
Rests on: a confirmation given before the save is complete can be false.
Settles: L.durable-write-02.record-request, L.durable-write-12.record-request, L.concurrency-05.absence-view
Under: record-for-singer
Criterion: Given a section leader has been told an absence is recorded, when the register is closed at once and opened again, then the view shows that absence.

## A10: A save is all or nothing
Kind: chosen
Says: after an interrupted save the register holds either all that was there before or all of that and the new absence, never a part. Saved data is not added to or overwritten in place, so no half-written last entry or unfinished save is ever used.
Rests on: the same saved data may hold singers and attendance, which an interrupted save must not damage.
Settles: L.durable-write-01.saved-register, L.durable-write-06.saved-register, L.durable-write-07.saved-register, L.startup-read-04.saved-register, L.migration-10.saved-register
Under: record-for-singer
Criterion: Given a register with singers, attendance and absences, when the save of a new absence is cut off at any point and the register is opened again, then everything saved before is there and the new absence is either wholly there or not at all.

## A11: A save that fails
Kind: chosen
Says: for lack of space or any other failure the section leader is told the absence was not recorded and that what was saved before is unchanged. It is not retried by itself and a later success is not assumed; they record it again and check the view, or tell the person who plans the programme.
Rests on: a failed save shown as done would leave a missing singer unknown.
Settles: L.durable-write-04.saved-register, L.durable-write-05.saved-register, L.logging-05.record-request, L.logging-09.record-request
Under: record-for-singer
Criterion: Given the register cannot be saved to, when a section leader confirms an absence, then they are told it was not recorded and that they can try again or tell the person who plans the programme, and everything saved before is unchanged.

## A12: Changes made at the same moment
Kind: chosen
Says: recordings are applied one at a time, each on the latest saved register, with the rules checked again then, so one never overwrites another. This holds for two open copies on the hall computer, and for the attendance commands too. No promise is made for shared or remote storage, which the slice does not use.
Rests on: several section leaders use one computer (000_problem.md line 17), and a lost absence would not be noticed.
Settles: L.concurrency-01.singer-s-word-that-they-will-miss-a-rehearsal, L.concurrency-02.record-request, L.concurrency-04.record-request, L.concurrency-12.saved-register, S.singer.in-register.second, S.rehearsal.coming.second, S.singer.not-in-register.second
Under: record-for-singer
Criterion: Given the register is open twice, when two different absences are confirmed at the same moment, then the view shows both.

## A13: The register is busy
Kind: chosen
Says: a recording waits for another change to finish for at most 5 seconds. Then it gives up, says the absence was not recorded and that it can be tried again; it is never repeated by itself.
Rests on: changes here are small, and an endless or silent wait would leave the section leader unsure.
Settles: L.concurrency-08.saved-register, L.concurrency-09.record-request
Under: record-for-singer
Criterion: Given another change holds the register for longer than 5 seconds, when a section leader confirms an absence, then after 5 seconds they are told it was not recorded and can be tried again.

## A14: The view is read at one moment and says what it is
Kind: chosen
Says: the view reads singers and absences together as they stood at one moment, shows the time it did so, and says that it shows only absences recorded so far, so others may still be missing. With none recorded it says so and does not say everyone is coming. A change made later appears when the view is looked at again, including after reloading, a second window or the computer waking; it does not update by itself.
Rests on: an old or empty view must not be read as a full account of who is coming.
Settles: L.sync-04.absence-view, L.concurrency-03.absence-view, L.concurrency-06.absence-view, L.user-action-02.absence-view, L.user-action-06.absence-view, L.user-action-07.absence-view
Under: see-who-will-miss
Criterion: Given no absence is recorded for the coming rehearsal, when the person who plans the programme looks at it, then they see the time of the reading and words saying no absences are recorded so far, with nothing saying that everyone is coming.

## A15: Every name is reachable
Kind: chosen
Says: every absent singer is listed, with no limit on how many; where they do not fit on one screen the rest are reached by scrolling, in the same order. Long names wrap and are never cut.
Rests on: a name left off or cut could hide who is missing among about 45 singers (000_problem.md line 5).
Settles: L.limits-08.absence-view, L.text-05.absence-view, L.text-12.absence-view, L.presentation-12.absence-view, V.kept-singer-name.long, V.kept-absence.long, V.kept-absence.edge
Under: see-who-will-miss
Criterion: Given every singer in the register, one with a very long name, has an absence for the coming rehearsal, when the view is looked at, then every name can be read in full and each part shows all of its singers as missing.

## A16: What order names come in
Kind: owner
Says: under each voice part the names need an order; whether by first name or family name is how you want to read them.
Settles: L.text-06.absence-view, L.text-07.absence-view, L.presentation-10.absence-view
Under: see-who-will-miss
Options: alphabetical by the name as written in the register, so first name first | alphabetical by family name
Recommended: alphabetical by the name as written, because it needs no guess at which part of a name is the family name
If left: names are shown alphabetically as written.
Harm: low
Decided: alphabetical by the name as written in the register (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given two altos with absences whose names as written are Wilma Ashdown and Bettina Young, when the view is looked at, then Bettina Young is listed before Wilma Ashdown.

## A17: How dates and counts are written
Kind: chosen
Says: dates are shown with weekday, day, month name and year in the Gregorian calendar, with ordinary digits and English wording like the rest of the register. Counts read as "2 of 7 known to be missing"; zero reads as "0 of 5", and one and several are worded correctly.
Rests on: a written month and weekday cannot be read as another day, and saying "known to be missing" stops the number being read as who is coming.
Settles: L.presentation-01.absence-view, L.presentation-03.absence-view, L.presentation-04.absence-view, L.presentation-06.absence-view, L.presentation-09.absence-view
Under: see-who-will-miss
Criterion: Given 1 of 7 altos has an absence for the coming rehearsal, when the view is looked at, then it shows that rehearsal's weekday, day, month name and year, and says 1 of 7 altos is known to be missing.

## A18: How a rehearsal date is given
Kind: chosen
Says: a date is typed in one form only, year-month-day. It is a plain calendar date with no time or zone and is never shifted. Anything empty, unreadable, impossible or in another form records nothing, and the form wanted is shown.
Rests on: one stated form leaves no day and month to confuse.
Settles: L.user-input-12.rehearsal-date, L.time-07.rehearsal-date, V.rehearsal-date.malformed
Under: record-for-singer
Criterion: Given a section leader gives a rehearsal date as 03/04/2027, when they try to record an absence, then nothing is recorded and they are shown the year-month-day form to use.

## A19: Which dates are accepted
Kind: chosen
Says: slice 1 accepts only Thursdays that have not passed, however far ahead; the confirmation shows the full date so a wrong year is seen. Another weekday is refused with the next Thursday named. Breaks, extra rehearsals and changed days are slice 6.
Rests on: slice 1 covers ordinary Thursday rehearsals (slice-001/004_slice.md line 23), and refusing other days catches a mistyped date before it is saved.
Settles: V.rehearsal-date.outside, L.time-10.rehearsal
Under: record-for-singer
Criterion: Given a date that has not passed and is not a Thursday, when a section leader tries to record an absence for it, then nothing is recorded and they are told ordinary rehearsals are on Thursdays and shown the next one.

## A20: No rehearsal date given
Kind: chosen
Says: when recording, a missing or empty date records nothing and asks for one. When looking, no date means the coming Thursday, today's if today is a Thursday, and the view names the date it chose.
Rests on: guessing a date for a record that cannot be undone is unsafe; for looking the next rehearsal is the one wanted and is shown by name.
Settles: V.rehearsal-date.empty, V.rehearsal-date.missing
Under: see-who-will-miss
Criterion: Given today is a Monday, when the view is asked for with no date, then it shows the coming Thursday and names its date.

## A21: Recording on the day of the rehearsal
Kind: owner
Says: it is not said until when a Thursday counts as not yet passed. A singer may phone that afternoon.
Settles: S.rehearsal.on-the-day.record-for-singer-1, S.rehearsal.on-the-day.record-for-singer-3, V.rehearsal-date.edge, V.todays-date.edge, C.states.rehearsal.on-the-day
Under: record-for-singer
Options: accept absences up to the end of the Thursday itself | stop at the time the rehearsal starts, which means giving the register that time | stop at the end of Wednesday
Recommended: up to the end of the Thursday, because a late call is still true and useful, and no start time has to be kept
If left: whether a call on the day can be recorded is undecided, and the slice cannot say what happens then.
Harm: medium
Decided: accept absences up to the end of the Thursday itself (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given it is late on a Thursday and not yet Friday by the hall computer's clock, when a section leader records an absence for that day's rehearsal, then it is accepted.

## A22: Everything else on the day
Kind: chosen
Says: on the day the view shows today's rehearsal like any coming one. An unknown name is refused as always. Saved absences stay through reloads, restarts, a second copy and the passing hours; what recording is accepted on the day is the decision above.
Rests on: nothing about looking or keeping needs to change on the day.
Settles: S.rehearsal.on-the-day.record-for-singer-2, S.rehearsal.on-the-day.see-who-will-miss-1, S.rehearsal.on-the-day.see-who-will-miss-2, S.rehearsal.on-the-day.again, S.rehearsal.on-the-day.reopened, S.rehearsal.on-the-day.restart, S.rehearsal.on-the-day.second, S.rehearsal.on-the-day.time
Under: see-who-will-miss
Criterion: Given today is a Thursday and an absence for today is recorded, when the view is looked at, then it shows that absence under today's date.

## A23: After Tuesday evening, slice 1 does nothing different
Kind: fact
Says: slice 1 has no Tuesday cut-off. The rehearsal is still a coming one and the view shows what has been recorded. What Tuesday evening changes is slice 7.
Rests on: slice-001/004_slice.md line 24
Settles: S.rehearsal.after-tuesday-evening.*

## A24: Saved absences stay as they are over reloads and restarts
Kind: chosen
Says: reloading, closing, restarting or time passing neither changes, repeats nor removes a saved absence or a singer; anything not confirmed was not saved. A rehearsal moves to passed only by its date.
Rests on: what was recorded must still be there on Tuesday evening.
Settles: S.singer.in-register.reopened, S.singer.in-register.restart, S.singer.in-register.time, S.rehearsal.coming.reopened, S.rehearsal.coming.restart, S.rehearsal.coming.time, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.reopened, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.restart
Under: see-who-will-miss
Criterion: Given an absence is recorded for a coming rehearsal, when the hall computer is restarted and the view is looked at, then the absence is shown once.

## A25: A refusal leaves nothing behind
Kind: chosen
Says: a refused recording keeps nothing, so it changes no view and survives no reload or restart. Each later try is judged afresh. Refused every time, the section leader tells the person who plans the programme.
Rests on: record-for-singer / 2 and 3 record nothing, so there is nothing to carry forward.
Settles: S.singer-s-word-that-they-will-miss-a-rehearsal.refused.*, S.singer.not-in-register.see-who-will-miss-1, S.singer.not-in-register.see-who-will-miss-2, S.singer.not-in-register.again, S.singer.not-in-register.reopened, S.singer.not-in-register.restart, S.singer.not-in-register.time
Under: record-for-singer
Criterion: Given an absence was refused for an unknown name, when the view is looked at, then nothing under that name is shown or counted.

## A26: What a refusal says and how the person goes on
Kind: chosen
Says: each refusal appears where the recording was made, in plain words in the same text as everything else: what is wrong and what to do. For an unknown name: check the spelling or have the singer added to the register, which it already allows. For a passed date or wrong form: give another date. No internal detail is shown.
Rests on: a refusal with no next step leaves a phoned absence unrecorded.
Settles: L.user-input-06.refusal-message, L.logging-07.refusal-message, L.accessibility-07.refusal-message, C.states.dead-end.2, F.network.gives-away
Under: record-for-singer
Criterion: Given the register has no singer of the name given, when the recording is refused, then readable text says nothing was recorded and to check the spelling or have the singer added.

## A27: How a typed name is matched
Kind: chosen
Says: a name matches when it is the same ignoring capital letters, spaces at the ends and repeated spaces, and treating the two ways of encoding the same accented letter as one. Compared at each recording; the register's own spelling is what is saved and shown. Accent marks, hyphens, other spellings, word order and missing parts must match. Nothing is guessed.
Rests on: ignoring harmless typing differences helps, while guessing could record the wrong singer.
Settles: L.text-01.singer-name, L.text-02.singer-name, L.text-04.singer-name, L.user-input-04.singer-name
Under: record-for-singer
Criterion: Given a singer is in the register as Perpetua Quill, when a section leader names "  perpetua  quill ", then the confirmation shows Perpetua Quill as the singer.

## A28: Odd, empty and long names typed in
Kind: chosen
Says: any letters and punctuation may be typed. There is no separate length limit: a name matching nobody is refused as unknown. An empty, all-space or missing name asks for a name. Hidden or control characters are never matched away or acted on; the name is handled only as text.
Rests on: the only valid names are those already in the register.
Settles: L.user-input-01.singer-name, L.user-input-03.singer-name, L.user-input-07.singer-name, L.user-input-10.singer-name, L.text-03.singer-name, V.singer-name.missing, L.logging-04.singer-name
Under: record-for-singer
Criterion: Given a section leader gives only spaces as the name, when they try to record an absence, then nothing is recorded and they are asked for the singer's name.

## A29: Two singers whose names match
Kind: chosen
Says: where more than one singer matches, they are shown with voice part and the section leader says which; if they cannot be told apart, nothing is recorded and they are told why. Names are shown exactly as the register has them.
Rests on: recording the wrong one of two singers would give wrong numbers until someone noticed.
Settles: L.user-input-09.singer-name, V.kept-singer-name.twice, L.text-10.kept-singer-name
Under: record-for-singer
Criterion: Given two singers' names match what was typed, when a section leader tries to record an absence, then nothing is recorded until one particular singer has been picked out.

## A30: Both fields are needed and must agree
Kind: chosen
Says: a singer and a rehearsal date are both required; with either unknown nothing is recorded. The rules about them are held where the absence is saved, whatever way the request arrived, in this order: both given, singer found, date acceptable, yes given. The section leader's own part is not checked by the register in this slice's criteria; see who may record.
Rests on: a rule kept only on the screen can be passed by.
Settles: L.user-input-02.record-request, L.user-input-05.record-request, L.user-input-11.record-request, L.misuse-01.record-request, L.misuse-02.record-request, L.authorization-07.record-request
Under: record-for-singer
Criterion: Given a request to record arrives with no confirmation, when the register handles it, then nothing is saved.

## A31: A recording changes nothing but absences
Kind: chosen
Says: a recording adds one absence; it cannot set or change a singer's name or voice part, or attendance. Nothing else sent with it is saved.
Rests on: the request needs only a singer and a date.
Settles: L.misuse-07.record-request, F.several-people.fields
Under: record-for-singer
Criterion: Given a register with singers and attendance, when an absence is recorded, then every singer's name and voice part and all attendance are as before.

## A32: What the computer shows after recording
Kind: chosen
Says: at once the section leader sees that the absence is recorded, or why it is not. Going back or starting again records nothing by itself; a new yes is needed, and a repeat is reported as already recorded.
Rests on: nobody should have to guess whether it worked.
Settles: L.user-action-01.record-request, L.user-action-03.record-request
Under: record-for-singer
Criterion: Given a section leader confirms an acceptable absence, when the save completes, then they see the singer's name and the rehearsal date with words saying it is recorded.

## A33: What is kept about each recording
Kind: chosen
Says: each absence is saved with the date and time it was recorded, by the hall computer's clock, in the same save. That is when it was recorded, not when the singer phoned. Which rehearsal it is for decides where it counts. There is no separate log; refused and failed tries keep nothing. Who recorded it is not known, since nobody is asked to identify themselves.
Rests on: the time helps settle a disputed entry and will be needed for Tuesday evening, while a second log would be one more copy of names and absences.
Settles: L.logging-01.record-request, L.logging-02.record-request, L.logging-11.record-request, L.time-12.singer-s-word-that-they-will-miss-a-rehearsal
Under: record-for-singer
Criterion: Given an absence has just been recorded, when the saved register is examined, then that absence has the date and time it was recorded.

## A34: Names and absences stay out of other records and messages
Kind: chosen
Says: nothing is written to a log. A failure shows plain words with no internal error text or trace, and never another singer's name or absence. Nothing is sent to monitoring.
Rests on: every extra place a name and absence date reaches is another place to leak from.
Settles: L.logging-03.kept-absence, X.singer-details.logs, X.singer-details.errors-inside, X.singer-details.errors-shown, X.singer-details.telemetry
Under: record-for-singer
Criterion: Given a save is made to fail, when the section leader sees the failure and the computer's records of the register are searched, then no singer's saved name or absence appears in an error trace or log.

## A35: Tests and examples use invented people
Kind: chosen
Says: tests and examples use made-up names and absences, never anything copied from the register.
Rests on: files kept with the code are copied wherever the code goes.
Settles: X.singer-details.samples
Under: record-for-singer
Criterion: Given the tests and examples kept with the code, when they are read, then every name and absence in them is invented.

## A36: A successful view shows only what it needs
Kind: chosen
Says: the view shows the rehearsal date, time of reading, voice parts, absent singers' names and the counts, and nothing else about a singer. No reason for absence is collected. A recording's answer shows only the singer concerned.
Rests on: planning the programme needs who and which part only.
Settles: L.stored-data-08.absence-view, X.singer-details.replies
Under: see-who-will-miss
Criterion: Given one alto has an absence, when the view is looked at, then no singer without an absence is named and nothing about the absent singer beyond name and voice part is shown.

## A37: Where names and absences are kept, and what must not carry them off
Kind: chosen
Says: absences are saved only in the register on the hall computer, in a place the computer does not clear by itself. What the register saves is kept out of the project's version history, so no absence is committed or pushed. Nothing is sent anywhere. No further encryption or key is added; the computer's own protection is what covers it. What was already committed before this slice is not changed by this choice.
Rests on: the documents keep the register on the hall computer (000_problem.md line 17) and name no outside system; a key kept on the same shared computer would add loss without keeping its users out.
Settles: X.singer-details.stored, L.stored-data-03.saved-register, L.stored-data-04.saved-register, L.stored-data-10.kept-absence, L.startup-read-07.saved-register
Under: record-for-singer
Criterion: Given an absence has been recorded in a copy of the project, when the changes offered for committing are listed, then nothing the register saved is among them.

## A38: What would harm someone
Kind: chosen
Says: singers' names with the dates they will be away would harm if seen, since they can show when someone is away from home; changed or removed absences would mislead the programme. Both are kept to the register on the hall computer and protected as far as the access decision below allows.
Rests on: the security pass, from the slice's own view and saved register.
Settles: L.stored-data-01.kept-absence, W.sensitive, W.prize
Under: see-who-will-miss
Criterion: Given absences are recorded, when the slice is used, then no name or absence is sent off the hall computer.

## A39: Anyone at the hall computer
Kind: owner
Says: the register has no accounts. As the slice stands, anyone who can use the hall computer, or open or copy what the register saves, can see who will be away, record absences no singer sent, or change the saved data, and nobody could tell who did it or that anyone looked. The register also does not hold a section leader to their own voice part. Is that acceptable?
Settles: L.authorization-01.record-request, L.authorization-01.absence-view, L.authorization-02.record-request, L.authorization-03.record-request, L.authorization-04.absence-view, L.authorization-05.record-request, L.authorization-08.record-request, L.authorization-10.record-request, L.authorization-09.saved-register, L.stored-data-02.saved-register, L.stored-data-12.absence-view, L.logging-10.saved-register, L.durable-write-09.saved-register, L.startup-read-09.saved-register, L.misuse-03.record-request, L.misuse-04.record-request, W.who-sees, T.singer-details.absence-view, T.singer-details.saved-register, T.singer-s-word-that-they-will-miss-a-rehearsal.record-request, T.singer-s-word-that-they-will-miss-a-rehearsal.saved-register
Under: see-who-will-miss
Options: accept it for slice 1, with access limited by who can use the hall computer; own voice part is the choir's habit and not enforced | require section leaders and you to identify yourselves before recording or looking, which changes the slice and means deciding how
Recommended: accept it for slice 1, if only trusted people can use that computer, because it is how attendance already works and singers need nothing; check that this is true
If left: anyone at the computer can do all of this, and the risk has been accepted by nobody.
Harm: high
Decided: accept it for slice 1, on the recommendation's condition that only trusted people can use the hall computer, which has not yet been confirmed as checked; own voice part is not enforced (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given nobody has said who they are, when someone at the hall computer records an absence for a singer in any voice part, then it is recorded without asking them to identify themselves.

## A40: No second person and no extra checks on numbers
Kind: chosen
Says: recording needs no second person's approval. A singer can be recorded only once for a rehearsal.
Rests on: a second approval would slow every phone call; the confirmation catches slips, and deliberate false entry is part of the access decision.
Settles: L.misuse-05.record-request
Under: record-for-singer
Criterion: Given one person at the computer, when they confirm an acceptable absence, then it is recorded without anyone else's approval.

## A41: A wrong absence cannot be removed
Kind: owner
Says: you took slice 1 without any way to correct an entry, and you weren't sure whether it is needed. Looking closer: a wrong or no longer true absence stays shown and counted for good as the documents stand, so a part can look too short when you are choosing the programme, including for tenors before the concert.
Settles: L.user-action-08.record-request, C.states.dead-end.8, C.states.dead-end.10
Under: new: remove-absence
Options: add removing a wrong absence to slice 1 | keep slice 1 as it is, with section leaders telling you which entries are wrong
Recommended: add removing a wrong absence to slice 1, because otherwise the numbers you plan from can stay wrong; this is a change from what I recommended before
If left: slice 1 stays as written and a wrong entry stays shown and counted.
Harm: high
Decided: add removing a wrong absence to slice 1 (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given a wrong absence is recorded for a coming rehearsal, when a section leader removes it and says yes to the shown singer and date, then that singer is no longer shown or counted as missing that rehearsal.
Criterion: Given a section leader has chosen an absence to remove, when they leave without saying yes, then the absence is still shown and counted.
Criterion: Given the register has no absence for that singer and rehearsal, when a section leader tries to remove one, then they are told there is none and nothing is changed.
Criterion: Given the register cannot be saved to, when a section leader confirms a removal, then they are told the absence was not removed and it is still shown.

## A42: A wrong absence until it is removed
Kind: chosen
Says: a wrong or withdrawn absence stays shown and counted until a section leader removes it; looking, recording it again, reloading, restarting or time passing does not remove it. This replaces what slice-001/004_slice.md line 26 says, following the decision to add removal.
Rests on: the register cannot know an absence is wrong until someone says so.
Settles: S.singer-s-word-that-they-will-miss-a-rehearsal.wrong-or-withdrawn.*
Under: new: remove-absence
Criterion: Given a wrong absence has not been removed, when the hall computer is restarted and the view is looked at, then the absence is still shown and counted.

## A43: Seeing the absences away from the hall
Kind: owner
Says: you need them by Tuesday evening, and the register is on the hall computer. As chosen below, slice 1 can be looked at only on that computer. Must you be able to see it from somewhere else?
Settles: F.network.answers-to
Under: see-who-will-miss
Options: looking at the hall computer, or being told by someone who looks there, is enough for slice 1, so the register answers at no network address | you must see it from elsewhere, which adds to the slice and needs a way to be chosen and protected
Recommended: the hall computer is enough for slice 1, because nothing then has to be reachable from outside; only if you or someone you trust can look there on Tuesday evening
If left: slice 1 as written does not promise any way to see absences away from the hall computer.
Harm: high
Decided: the hall computer is enough for slice 1, on the recommendation's condition that the person who plans the programme or someone they trust can look there on Tuesday evening, which has not yet been confirmed as checked (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given slice 1 is in use, when the hall computer is checked for network addresses the register answers at, then there are none.

## A44: No web page and nothing reached over a network
Kind: chosen
Says: as decided for where the absences are seen, slice 1 is used on the hall computer itself, with no web page and nothing reached over a network, so there are no pages, requests from elsewhere or replies to attack or keep. If it ever has to be seen from elsewhere, these answers are looked at again.
Rests on: the register is on the hall computer (000_problem.md line 17), no criterion asks for access from elsewhere, and offering none is the smallest thing to protect.
Settles: F.browser.context, F.browser.page-policy, F.browser.framing, F.browser.type-guessing, F.browser.came-from, F.browser.other-sites, F.browser.messages, F.browser.others-code, F.browser.sent-on, F.browser.kept-by-browser, F.browser.known-by, F.network.transport, F.network.in-between, F.network.kinds-of-request, F.network.left-on, L.authorization-06.record-request, L.user-action-12.absence-view, L.stored-data-05.singer-name, L.stored-data-06.absence-view

## A69: How well it has to work
Kind: owner
Says: the documents do not say how often it may fail or how slow is too slow.
Settles: W.target
Under: see-who-will-miss
Options: recording and looking each finish within 2 seconds on the hall computer, and any fault is put right before the next Tuesday evening | no stated target for slice 1
Recommended: the 2 seconds and the Tuesday evening repair, because that is when you need the numbers
If left: no speed or reliability target is checked.
Harm: low
Decided: recording and looking each finish within 2 seconds on the hall computer, and any fault is put right before the next Tuesday evening (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given a register of 60 invented singers and the register not held by another change, when an absence is confirmed or a rehearsal is looked at on the hall computer, then the result appears within 2 seconds.

## A45: No added components
Kind: chosen
Says: the slice adds no component written by someone else, beyond what the register already runs on.
Rests on: recording and listing need nothing extra, and each addition would have to be watched.
Settles: F.dependency.known-flaw, F.dependency.inventory, F.dependency.look-alike, F.dependency.trusted-most
Under: record-for-singer
Criterion: Given the finished slice, when what it needs installed is listed, then nothing new is on the list.

## A46: No secret values and no separate groups
Kind: not here
Says: the slice makes no link, code, session or other value that must be impossible to guess, and there is one choir with no separate groups of data.
Rests on: no criterion creates such a value or a group.
Settles: F.unguessable.made, F.several-people.groups

## A47: No settings
Kind: not here
Says: the slice reads no setting, so none can be missing or wrong.
Rests on: no criterion of the slice adds or reads a setting.
Settles: V.every-setting.missing, V.every-setting.empty, V.every-setting.malformed, V.every-setting.outside

## A48: Using it with a keyboard and hearing it read
Kind: chosen
Says: everything in recording and looking can be done with the keyboard alone, including leaving any part. Where there are controls, focus is always visible, moves to the result message when what held it goes, and each control has a spoken name. All results are text.
Rests on: ordinary accessibility practice; section leaders' needs are not stated.
Settles: L.accessibility-01.record-request, L.accessibility-02.record-request, L.accessibility-03.record-request, L.accessibility-04.record-request, L.accessibility-05.record-request
Under: record-for-singer
Criterion: Given no mouse, when a section leader records an absence or abandons it partway, then both can be done with the keyboard alone, with where they are always visible.

## A49: Reading the view
Kind: chosen
Says: all meaning is in words, never only colour or a symbol. The text keeps at least 4.5 to 1 contrast where the slice sets colours, otherwise follows the computer's own, and stays complete at twice the size. Names are kept apart from numbers whichever direction they are written in.
Rests on: ordinary accessibility practice.
Settles: L.accessibility-06.absence-view, L.accessibility-08.absence-view, L.accessibility-09.absence-view, L.accessibility-10.absence-view, L.text-09.absence-view
Under: see-who-will-miss
Criterion: Given absences are recorded, when the view is read at twice the text size without colour, then every name, voice part and number is there and understandable.

## A50: The clock the register goes by
Kind: chosen
Says: today is the date on the hall computer's clock in its local time zone, read at each use; no allowance is made for a wrong or changed clock, which could accept a passed rehearsal or refuse a coming one, but never alters a saved date. Recording and looking show today's date so a wrong one can be seen. If no sensible date can be read, nothing is recorded and the person is told to check the computer's clock.
Rests on: the register is on one computer, and showing the date used makes a wrong clock visible without another service.
Settles: L.time-01.todays-date, L.time-03.todays-date, L.time-08.todays-date, V.todays-date.empty, V.todays-date.missing, V.todays-date.malformed, V.todays-date.outside
Under: record-for-singer
Criterion: Given the hall computer's date is set to a wrong day, when a section leader starts to record an absence, then the date the register takes as today is shown to them.

## A51: Saved data that cannot be read
Kind: chosen
Says: if the saved register is damaged, not the register's own, cannot be opened, or holds absences of the wrong shape, the register shows no view and records nothing. It says the register cannot be read, never shows it as nobody missing, never overwrites or repairs it, and says to leave it as it is and get help. So there is no repair to wait for and no rescued data used unchecked.
Rests on: carrying on with partial data would give wrong numbers or destroy what could be recovered.
Settles: L.startup-read-01.saved-register, L.startup-read-02.saved-register, L.startup-read-06.saved-register, L.startup-read-08.saved-register, V.kept-absence.malformed
Under: see-who-will-miss
Criterion: Given the saved register is damaged, when someone asks for the view, then they are told it cannot be read, no counts are shown, and the saved data is left unchanged.

## A52: No saved register at all
Kind: chosen
Says: where nothing is saved, the view says no register was found and shows no counts; this is told apart from a register that cannot be opened. Adding the first singer still starts a new register as before. Recording finds no singer.
Rests on: an empty view could be mistaken for a full choir.
Settles: L.startup-read-03.saved-register
Under: see-who-will-miss
Criterion: Given nothing has been saved where the register looks, when the view is asked for, then it says no register was found and shows no counts.

## A53: A register that can be read but not changed
Kind: chosen
Says: the view works and recording is refused, saying it cannot be saved; nothing is repaired.
Rests on: looking needs no change.
Settles: L.startup-read-05.saved-register
Under: see-who-will-miss
Criterion: Given the saved register can be read but not changed, when someone looks at the view, then the recorded absences are shown.

## A54: Spare copies and getting back from loss
Kind: owner
Says: if the hall computer or its saved register is lost or damaged, absences, singers and attendance may be lost. How much loss is acceptable and whether to look after a copy elsewhere is a cost and risk for you. No spare copy is mentioned in the documents, so none can be said to work. A copy must be taken so it is whole, with the register not being saved at that moment, kept as private as the original, and restored as one unit.
Settles: L.startup-read-10.saved-register, L.durable-write-03.saved-register, L.logging-08.saved-register
Under: record-for-singer
Options: no spare copy for slice 1: after a loss, section leaders record coming absences again from memory or ask singers | someone takes a copy each week to a safe place and tries restoring it once before relying on it
Recommended: a weekly copy kept privately, with one restore tried, because the same data holds the singers and attendance
If left: no copy is promised and a loss may be permanent.
Harm: medium
Decided: someone takes a copy each week to a safe, private place and tries restoring it once before relying on it; who does this is not yet named (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given a weekly copy of the saved register, when it is restored to a separate place for the one trial before it is relied on, then the singers, attendance and absences are as they were when the copy was made.

## A55: Copies and moving the register
Kind: chosen
Says: absences are saved together with the singers they name, as part of the one register, so copying or restoring the register takes them together. A copy taken while a save is happening holds the register wholly before or wholly after it. Restoring an older copy loses what was recorded since, which has to be said by whoever restores it.
Rests on: absences separated from their singers would be meaningless.
Settles: L.durable-write-10.saved-register, L.durable-write-11.saved-register
Under: record-for-singer
Criterion: Given a copy of the saved register is made while an absence is being saved, when the copy is opened, then it reads as a whole register, with or without that absence.

## A56: An absence that no longer matches a singer
Kind: chosen
Says: the slice removes no singer and cancels no rehearsal. If a saved absence names nobody in the register, because a singer left or data was restored in part, it is kept, not counted, and the view warns that an absence does not match any singer, without saying everyone is accounted for.
Rests on: silently dropping it would hide a possible gap; deleting it could not be undone.
Settles: L.durable-write-08.singer-s-word-that-they-will-miss-a-rehearsal, L.lifecycle-05.singer-s-word-that-they-will-miss-a-rehearsal, L.lifecycle-06.singer, V.kept-absence.dangling, S.singer.left-the-choir.*, C.states.singer.left-the-choir
Under: see-who-will-miss
Criterion: Given a saved absence for the coming rehearsal names nobody in the register, when the view is looked at, then it warns that one absence matches no singer, and counts it in no part.

## A57: A singer whose voice part has changed
Kind: chosen
Says: the slice adds no way to change a part. A singer is counted under the part the register holds when the view is looked at, for the numbers missing and the part's total alike; absences stay with the singer.
Rests on: the programme is planned for the parts as they are now.
Settles: S.singer.changed-voice-part.*, C.states.singer.changed-voice-part
Under: see-who-will-miss
Criterion: Given a singer with a coming absence is now held as a bass instead of a tenor, when the view is looked at, then they are counted as missing under bass only.

## A58: Singer records with something missing or wrong
Kind: chosen
Says: if a singer's name is empty or missing, or their voice part is missing or not one of the four, the view says the register has a singer entry it cannot place, and that the numbers may be incomplete; it does not drop it silently. Unusual characters in a stored name are shown as plain text, and ones that cannot be displayed are marked.
Rests on: a singer silently left out would make a part's numbers wrong.
Settles: V.kept-singer-name.empty, V.kept-singer-name.missing, V.kept-singer-name.characters, V.kept-voice-part.missing, V.kept-voice-part.outside, V.kept-absence.characters
Under: see-who-will-miss
Criterion: Given a singer in the saved register has no valid voice part, when the view is looked at, then it warns that a singer cannot be placed and the numbers may be incomplete.

## A59: No absences saved, and absences for other dates
Kind: chosen
Says: an empty or absent list of absences is read as none recorded. Absences for other dates, passed ones or non-Thursdays among them, are never counted for the rehearsal looked at.
Rests on: a register saved before this slice has no absences, and see-who-will-miss / 2 counts a rehearsal's own only.
Settles: V.kept-absence.empty, V.kept-absence.missing, V.kept-absence.outside, L.migration-07.saved-register, L.migration-02.saved-register
Under: see-who-will-miss
Criterion: Given a register saved before this slice, with singers and attendance and no absences, when the view is looked at, then every part shows none missing of its singers and all singers and attendance are still there.

## A60: Old and new versions of the register
Kind: chosen
Says: there is no separate conversion: old saved data and spare copies of it are read as they are, for as long as the register is used. The older register is closed before the new one is used. Putting the older version back must not remove absences or damage singers and attendance, and this is checked before the new one is used; the older one will not show absences. A version that meets saved data marked as from a later version refuses to change it and says so; the version from before this slice cannot do that.
Rests on: going back must stay possible without losing what was recorded.
Settles: L.migration-01.saved-register, L.migration-03.saved-register, L.migration-05.saved-register, L.migration-11.saved-register
Under: record-for-singer
Criterion: Given absences have been saved, when the version from before this slice ticks someone's attendance, then the absences are still saved.

## A61: How long past absences are kept
Kind: owner
Says: nothing says what happens to absences, past rehearsals or the times they were recorded after the date passes. They are personal details. The next activity, on singers who have gone quiet, may want to know who sent word.
Settles: L.stored-data-09.kept-absence, L.logging-12.kept-absence, L.logging-06.saved-register, S.singer-s-word-that-they-will-miss-a-rehearsal.recorded.time, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.time, S.rehearsal.passed.time, C.states.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed, C.states.dead-end.6, C.states.dead-end.11
Under: record-for-singer
Options: keep them for 12 months after the rehearsal, then remove them | keep them with no end | remove them soon after each rehearsal
Recommended: 12 months, because it leaves them for the next activity without keeping them for ever; removal would be built before the first reaches that age
If left: they are kept with no end.
Harm: medium
Decided: keep them for 12 months after the rehearsal, then remove them, with the removal in place before the first absence reaches that age (the user, 2026-11-26: "I take what you recommend for each of them.")
Criterion: Given an absence is for a rehearsal more than 12 months ago and the removal is in place, when the removal has been carried out and the saved register is examined, then neither the absence nor the time it was recorded is there.

## A62: A passed rehearsal otherwise
Kind: chosen
Says: while its absences are kept, a passed date can still be looked at and is marked as passed. Looking, repeating, reloading, restarting or a second copy changes nothing about it.
Rests on: what was recorded stays readable and clearly in the past.
Settles: S.rehearsal.passed.see-who-will-miss-1, S.rehearsal.passed.see-who-will-miss-2, S.rehearsal.passed.again, S.rehearsal.passed.reopened, S.rehearsal.passed.restart, S.rehearsal.passed.second, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.record-for-singer-1, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.record-for-singer-2, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.record-for-singer-3, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.see-who-will-miss-1, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.again, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.reopened, S.singer-s-word-that-they-will-miss-a-rehearsal.rehearsal-passed.restart
Under: see-who-will-miss
Criterion: Given a passed rehearsal has recorded absences, when its date is looked at, then they are shown with words saying the rehearsal has passed.

## A63: Cancelled or moved rehearsals
Kind: not here
Says: slice 1 has no way to cancel or move a rehearsal; slice 6 takes breaks, extra rehearsals and changed days. Anything recorded stays under its original date.
Rests on: slice-001/004_slice.md line 23
Settles: S.rehearsal.cancelled-or-moved.*, L.lifecycle-07.rehearsal, C.states.dead-end.7

## A64: Word sent by the singer
Kind: not here
Says: singers send nothing in slice 1; that is slice 2.
Rests on: slice-001/004_slice.md line 19
Settles: S.singer-s-word-that-they-will-miss-a-rehearsal.sent-by-singer.*, C.states.dead-end.9

## A65: Singers being asked whether they're still coming
Kind: chosen
Says: slice 1 does not know whether a singer has been asked. Their absence is recorded, kept and shown like any other singer's.
Rests on: asking is the next activity on the scope map and nothing in slice 1 depends on it.
Settles: S.singer.asked-if-coming.*, C.states.dead-end.3
Under: record-for-singer
Criterion: Given a singer has been asked whether they are still coming, when an absence is recorded for them, then it is recorded and shown like any other.

## A66: Taking singers out and changing voice parts
Kind: owner
Says: the documents give no way to take a singer out of the register or change their voice part. If either happens, totals and parts could be out of date when you plan. Is that part of this work?
Settles: C.states.dead-end.1, C.states.dead-end.4, C.states.dead-end.5
Under: see-who-will-miss
Options: leave both out of slice 1 | add them to the requirements
Recommended: leave them out of slice 1, because neither is needed to record and see absences
If left: they stay out.
Harm: low
Decided: leave both out of slice 1 (the user, 2026-11-26: "I take what you recommend for each of them.")

## A67: When it cannot be used, and how that is noticed
Kind: chosen
Says: if recording or looking does not work, the person using it sees a message and tells the person who plans the programme. Section leaders note phoned absences and record them when it works again; the planner asks them directly meanwhile. Nothing watches it by itself.
Rests on: this falls back on what people can do without the register, and it is used by a few people who will see a failure.
Settles: W.unavailable, W.noticed
Under: record-for-singer
Criterion: Given the register cannot be read or saved, when someone tries to use it, then it says it is not working and to pass absences to the person who plans the programme directly.

## A68: Duties about members' details
Kind: owner
Says: the register would hold dated absences of named people. The documents name no law, agreement or choir rule, and I have not checked any. Which apply is not something I can choose.
Settles: W.obligations
Under: record-for-singer
Options: find out before real use what the choir must do about members' personal details | go ahead on your confirmation that nothing applies beyond what is already done for the register
Recommended: find out before real use, from whoever is responsible for the choir's records
If left: nobody has confirmed what applies.
Harm: medium
Decided: find out before real use, from whoever is responsible for the choir's records; not yet done (the user, 2026-11-26: "I take what you recommend for each of them.")
