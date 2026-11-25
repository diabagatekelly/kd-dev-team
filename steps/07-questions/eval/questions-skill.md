---
name: questions
description: Decide which of the library's questions matter for the chosen slice and what the slice takes in, then have every question drawn by script. Use when the startup report names "questions" as the next stage, and when the user answers anything this stage said.
---

# Questions

This stage finds every question the slice must answer before it is
built. It answers none of them, decides nothing and asks the user
nothing: the next stage answers, from the documents first.

Your judgement is two things, written in `kept.md` in the folder the
report names: which of the library's questions matter here, and what
the slice takes in. Everything else is drawn by the report's `draw`
command into `questions.md`, which you never write or edit.

**Read first.** The chosen slice, the requirements' limits, the
approach, every research document and `states.md`. Then the
report's `things` command: it prints what a question may apply to,
and the library's kinds. Read every kind with the `library` command,
four or five kinds at a time, every question of each.

**The library.** For every question: can what it describes arise
from something this slice adds or changes, so that what the product
then does would matter to whoever uses or maintains it?

- It is kept even where a document already answers it. You are not
  judging whether it is answered, only whether it must be asked.
- It is dropped only when the slice does nothing of that kind, or
  the condition cannot arise for anything it does. Say which.
- When unsure, keep it. A question wrongly dropped is lost for
  good; one wrongly kept costs a line.
- A kind the slice does nothing of at all is dropped whole, in one
  row (`migration: all`). Never drop a whole kind to save reading:
  one question of it that can arise keeps that question.
- A kept question applies to named things: a criterion, a lasting
  thing or a thing committed to, by the names `things` printed; a
  value of your table; or another thing you list (a request, a
  screen, a message, a stored file, a credential), with the
  criterion or research fact it comes from. Name the thing the
  question is really about, and every such thing.

**What the slice takes in.** Every value that reaches the slice
from outside it: each value a person gives; each field of a reply
that a criterion uses (research's facts say what comes back); each
value read back from where it was stored; a credential. For each:
a short name; its kind (`text`, `number`, `date`, `choice`,
`identifier`, `file`, `list`, or `other` when unsure); where it
comes from; whether someone would be harmed if another person saw
it (`yes` or `no`: a credential, a person's own details, anything
a limit of the user's protects); and its source, a criterion's
name or a research document and fact.

```markdown
# Kept: slice <n>

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `short-name` | choice | <who or what gives it> | no | <item / n, or document.md F3> |

## Other things the slice has
- `short-name`: <what it is> (<item / n, or document.md F3>)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external-01 | `short-name`; <another thing> | <what in the slice makes it arise> |
| user-input-04, user-input-11 | dropped | <why neither can arise here> |
| migration: all | dropped | <why the slice does nothing of the kind> |
```

Every question of the library is in exactly one row. Then run the
`draw` command. It refuses a file that leaves a question out, names
a thing nothing lists, or gives a value no source: put right what
it names and draw again. Where it says the drawing could not be
written, say so and leave it: never write `questions.md` yourself.

**Answer nothing.** No answer, no decision, no recommendation, no
criterion, in `kept.md` or in your reply. What research found
contradicted or left open is carried by the script as it stands:
do not settle it. Change no other document of the slice.

**Ask nothing.** No preference and no decision is asked of the user
here. Asked what you need from them, or offered answers: nothing is
needed now; the documents and tests answer first, and what is
theirs to decide comes to them once, as one short list.

**A lasting thing with no states.** If a criterion creates or keeps
a thing that `states.md` has no table for, say which thing and
which criterion first. Then load the research text and add its
table by that text's rules, each row with its source or `not said
in the documents`, nothing from what such things usually do. Then
go on.

**An answer to an earlier stage's question.** When the user's
message answers a question another stage left open (the
requirements' "Not yet confirmed"), that is that stage's work: load
its text, record the answer there, say what you recorded, then come
back and do this stage. Write no criterion from it here.

**Told to skip this stage.** Write nothing yet. Say once what
skipping costs (the cases nobody listed are the ones found in the
build, and the answers have nothing to be checked against) and that
this stage asks nothing of them; offer it again. If they still say
no, it is theirs: write `skipped.md` in the same folder (their
words, the date, that the library was not gone through), no
`kept.md`, and run `draw`: what needs no judgement is drawn all the
same. Say that the skipping goes to the owner's list as a risk
accepted. Do not start the next stage.

**Drawn before, and the documents changed.** The report says the
questions are to be drawn again. Read what changed. In `kept.md`,
change only what the change brings or removes: a kind dropped
before that the slice now does; a value or thing now taken in; rows
that applied to a thing no longer there. Leave the rest as it is,
and draw again.

**Stop there.** Say how many questions were drawn and of which
parts, in the command's own numbers, which kinds were dropped whole
and why, and anything the command refused. No answers, no design.
