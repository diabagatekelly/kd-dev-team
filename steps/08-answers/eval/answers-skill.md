---
name: answers
description: Settle every drawn question of the chosen slice, from the documents first, and write the criteria that follow. Use when the startup report names "answers" as the next stage, when the user answers anything this stage said or decides something on the owner's list, and when the user says to skip the answers.
---

# Answers

The questions are drawn. This stage settles every one of them and
writes the criteria that follow. It asks the user nothing: what is
theirs to decide is gathered, and reaches them once, as one short
list ranked by harm.

Your judgement is one file, the answers, at the path the report
names. A script says which questions no answer settles yet, refuses
what does not hold, and draws `answered.md` beside it: the criteria,
the owner's list, what is to be tested, what was chosen. You never
write that drawing.

**Read first.** The chosen slice, the requirements' limits, the
approach, every research document, `states.md`, `kept.md` and
`security.md`. Then the report's `next` command: it lists the
questions still to settle, sixty at a time.

**An answer settles many questions.** Write an answer for a
behaviour, a fact or a decision, and give it every question it truly
settles: a person answering those questions honestly would say this
and nothing more. `L.entry.*` is every thing of a library entry;
`S.thing.state.*` every event in one state. One answer a question.

```markdown
## A1: <a short title>
Kind: fact | chosen | owner | test | not here | look up
Says: <what holds, what is chosen, what is to decide, what is not known, or why it does not arise>
Rests on: <fact: the document and its line, fact or criterion; chosen: the reason>
Settles: <ids, separated by commas>
Under: <the slice's item, or `new: a-name`>
Criterion: Given <a state>, when <one action or event>, then <what someone can see>.
```

**Which kind, asked in this order.**

1. `fact`: a document of the slice says it. Rest it on that
   document by name: a criterion (`item / n`), a research fact
   (the research document's own name and the fact: `payright F12`
   where the document is `payright.md`), a line of the requirements.
   Never on what such systems usually do.
2. `not here`: the question does not arise in this slice. Say why
   in one line. A question wrongly dismissed is lost for good: where
   you are not sure, answer it.
3. `look up`: it turns on how a thing the slice is committed to
   behaves, and its research document does not say. Do not answer
   it from what such systems usually do, and do not make it a test
   yet: say in `Says` exactly what must be known. They are looked
   up together, below.
4. `test`: looked up, and no page says. Say what is not known, the test that would settle it
   (`Test:`), and `Harm:` high, medium or low if the guess is wrong.
   Write no criterion on the guess. An open point of the research
   is a test, not a fact, however likely it looks.
5. `owner`: only one of these four. A rule of the product in the
   user's own field that the documents cannot know. A matter of
   taste, or of how they want to experience the product. A risk, a
   cost or an obligation they must accept, and any choice that
   cannot be taken back once made. What is in or out. Give
   `Options:` (two or more, separated by `|`), `Recommended:` one of
   them and why, `If left:` what happens while it is undecided, and
   `Harm:`. Write no criterion: it waits for them. What the
   documents already decide is a fact, not asked again; how to
   protect something is chosen, and only a risk left after that is
   theirs. How fast and how reliable it must be, and what law or
   contract binds it, are theirs wherever the documents do not say:
   the script refuses them chosen.
6. `chosen`: everything else. Good practice in security, in what a
   person is told and in what is recorded is applied, not asked. A
   technical problem with a known solution is solved: say what is
   chosen and, in `Rests on`, why. The user can overturn it later.
   A choice says nothing of how something outside behaves that the
   research does not say. An answer that speaks of a thing the slice
   is committed to gives, in `Rests on`, the fact of its research
   document and that document's own words in quotes (`payright F6:
   "returns the first payment"`): the script looks for them there
   and refuses the answer otherwise. Say no more of the thing than
   those words say.

**Criteria.** Write one where someone could see the behaviour go
wrong, under the slice's item it belongs to. What an answer says
the product does, or never does, and someone could check, has its
criterion: a thing only said is a thing nobody tests.

- one Given, one action or event, one outcome a person could check
  by looking. The outcome, never the mechanism;
- the path that fails as well as the one that works: refused, not
  found, sent twice, no reply;
- for a sensitive value, its absence: "nothing of the key appears in
  the record of a failed call";
- every wait, retry and giving up has its number, or says
  `unbounded, owner approved`;
- a permanent refusal says what the person can do next.

Wording of messages and the fields of a record are not criteria:
say them in `Says`.

**Looked up, together.** Once `next` lists nothing, run the
report's `lookups` command. Where it lists any, load the research
text and do what it says of things the answers ask for, all of them
in one go. Then change each `look up` answer in place: a `fact` or
a choice resting on the new fact and its words, or a `test` where
no page says.

**The work.** Run `next`. Answer what it lists by adding blocks to
the end of the answers file with your file tool, never through the
shell and never by writing the file again whole. Run `next` again,
until none is left. Then run `draw`: put right what it names and
draw again. Where it says the drawing could not be written, say so
and leave it.

**Ask nothing, change nothing else.** No preference is asked of the
user and no other document is changed. Asked what you need from
them, or offered answers: nothing now. What waits for them is said,
and comes to them once, as one list, after what is to test has been
tested: do not ask for it here, and do not invite it.

**The user decides something on the list.** Add to that answer
`Decided: <the choice> (the user, <date>: "<their words>")`, write
the criteria that now follow, and draw again. Never mark a decision
taken that they did not take; a choice against the recommendation
is recorded as they made it.

**Told to skip this stage.** Write nothing yet. Say once what
skipping costs (the questions stay open and the slice gets no
criteria from them, so each is settled by whoever builds it) and
that this stage asks nothing of them; offer it again. If they still
say no, the answers file is one line, `Skipped at the user's word,
<date>: "<their words>"`, and you run `draw`. Say that the skipping
goes to the owner's list as a risk accepted. Do not start the next
stage.

**Written before, and the questions changed.** `next` lists the new
ones; `draw` names an answer that settles a question no longer
asked. Change only those, in place.

**Stop there.** Say, in the command's own numbers, how many answers
settle how many questions and of which kinds, how many criteria
were written, and what waits for the owner, the gravest first. No
design.
