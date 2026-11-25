---
name: security
description: Look at the chosen slice as someone who means harm would, and add what that finds to the slice's questions. Use when the startup report names "security" as the next stage, when the user answers anything this stage said, and when the user says to skip the security pass.
---

# Security

The questions are drawn. This stage looks at the slice once more, as
someone who means harm would, and adds its questions to the same
list. It answers none of them, decides nothing and asks the user
nothing: the next stage answers, from the documents first.

Your judgement is two tables, written in `security.md` beside
`kept.md` in the folder the report names. The report's `draw`
command then draws the questions again with it. You never write or
edit `questions.md`.

**Read first.** The chosen slice, the requirements' limits, the
approach, every research document, `states.md` and `kept.md`.

**Facts about the slice.** Six, each `yes` or `no`, each with the
criterion or the document's line that says so. Where the documents
do not say, it is `yes`: a fact wrongly `no` loses its questions for
good.

- `browser`: a person uses it in a web browser.
- `network`: it answers requests at a network address, on one
  machine or many.
- `calls-out`: it calls another system.
- `dependency`: it adds a component someone else wrote.
- `several-people`: more than one person uses it, or one person
  acts for several.
- `unguessable`: it makes a value meant to be impossible to guess (a
  link, a code, a session).

**What someone who means harm would want.** Go through `kept.md`.
For each class of sensitive values: what would someone want it for,
here? What is wanted need not be a value: a thing the slice keeps
or commits to is wanted too (money given back, a place taken), by
the name the documents give it. For each other thing the slice has (a request, a screen, an
address that receives, a stored file): who else could send it, read
it, change it or send it again, and following it through the slice,
what is the worst they reach? One row for each pair worth asking,
by the names `kept.md` uses:

- The worst is one plain sentence of what happens and to whom. Not
  "access is gained"; never a control or a fix.
- `Asked` is `yes`, or `no: ` and the reason it is dismissed, so
  nobody works it out again. A value that is public by design is not
  a secret: dismiss it with that reason.
- Every class and every other thing is in at least one row. A thing
  the slice plainly has that `kept.md` does not list is added to
  `kept.md`'s own list, with its source, and nothing else is changed
  there.
- A thing that gives nothing worth having wants `nothing`, and is
  dismissed with the reason.
- A slice with little to attack has few rows marked `yes`. Say so;
  do not pad.

```markdown
# Security: slice <n>

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | <item / n, or the document's line> |
| network | no | <the document's line that says so> |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `class-or-value` | `other-thing` | <what happens, and to whom> | yes |
| `class-or-value` | `other-thing` | <what was considered> | no: <why it is dismissed> |
```

Write `security.md` with your file tool, not through the shell.
Then run the `draw` command. It refuses a fact left out or without
a source, a class nobody is said to want, a thing nothing comes
through and a name `kept.md` does not have: put right what it names
and draw again. Where it says the drawing could not be written, say
so and leave it.

**It cannot be made safe as it is cut.** Only where the documents
say that something the slice cannot be safe without is not there or
is out (nobody signs in; nothing of the kind is planned). Where they
simply do not say, that is a question, asked already or a row of
yours: go on. Otherwise write nothing. Say what is missing and what
that forces, with one recommendation and not a list of ways: it is
the slice's to decide, with the user.

**Answer nothing, ask nothing.** No control, no fix, no criterion
and no recommendation of how, in `security.md` or in your reply. No
preference is asked of the user: what is theirs to decide comes to
them once, as one short list. Change no other document.

**Told to skip this stage.** Write nothing yet. Say once what
skipping costs (nobody has looked at the slice as an attacker would
before it is built) and that this stage asks nothing of them; offer
it again. If they still say no, it is theirs: `security.md` is one
line, `Skipped at the user's word, <date>: "<their words>"`, and you
run `draw`, which then draws every fixed question. Say that the
skipping goes to the owner's list as a risk accepted. Do not start
the next stage.

**Written before, and the documents or `kept.md` changed.** Change
only what the change brings: a fact that now holds, a new class or
thing and what comes through it, a row for a thing no longer there.
Edit in place; every other row stays word for word. Draw again, and
say what you changed or that nothing needed changing.

**Stop there.** Say which facts hold, how many questions were added
of each part in the command's own numbers, and what was dismissed
and why. No answers, no design.
