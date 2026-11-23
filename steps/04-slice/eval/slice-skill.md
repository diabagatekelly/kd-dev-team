---
name: slice
description: Cut the requirements of the "now" activity into the set of thin slices, write the criteria of the slice the user chooses, and come back to the set after a merge. Use when the startup report names "slice" as the next stage or says a coming-back is due, and when the user chooses, widens or joins slices or says that work has turned something up.
---

# The slice

What to build first, and what after it. From the requirements list
of the "now" activity: the whole set of thin slices, where to start,
and criteria for the one slice being worked on. You are the expert
on this: recommend, and say so when a cut the user asks for would
cost them. All of it is what, never how.

Two documents, under the names the startup report gives. The set:

```markdown
# Slices: <the "now" activity>

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | <a verb phrase a person would recognise> | item-name, item-name | nothing | open |
| 2 | <another> | item-name | 1 | open |

## Where to start
Which slices can be started now, which wait and for what. The one you recommend first, and why.
```

Two more sections are added to the set when there is something to
put in them, never empty: `## Issues`, a line an issue (`- #<number>
<its title>: <where it belongs>, because <why>.`), and `## What
changed`, a line a change with its reason.

The chosen slice, in the folder of its number:

```markdown
# Slice <#>: <the verb phrase>

## Thin path
One or two sentences: who does what, and what they are shown.

## Criteria
- **item-name / 1**: Given <a starting state>, when <one action>, then <what someone could check by looking>.

## Needs from outside
What this path needs that the product cannot do by itself, by its everyday name. Or `none`.

## Left for later
Each thing this slice leaves out: the slice of the set that takes it, then `Usable without it: <what the person can do meanwhile>` or `Blocker: <why the build waits>`.

## Size
Criteria: <n>.
```

**Cutting the set.** Read the requirements list. Slices come from
its items, by their names, and from nothing else: not "Out for now",
not another row of the scope map, not what such a product usually
has. A slice is one behaviour, from a person's action to what they
are shown, through everything it takes to get there. Its actor is a
real person, never "the system". It is never a layer or a task:
groundwork rides with the first slice that needs it, sized to that
slice. Too big is the whole activity at once; too thin is something
nobody could be shown. Where the thin cut is not obvious: the
ordinary path before its variations; one kind of input at a time;
one step of a sequence that is of use by itself; the same thing over
a smaller surface; speed and the like later. Handling what goes
wrong is spread over the slices, never all first or all last: a
slice carries the refusals its own rule makes for someone using it
as meant, the common ones are a later slice, the rare ones later
still. Every item is in some slice, and one item may take two. A
list of one small item is one slice: make up no more. A slice's
number is never changed or reused. Every state is written `open`.

**The order.** "Builds on" holds the slices a slice cannot be shown
without, or `nothing`. A slice whose item leans on a question under
"Not yet confirmed" cannot be started until it is answered: say so
under "Where to start". Recommend one start: the slice that shows a
person the most for the least, and that the others build on.

**Then ask once.** Show the set, say which slice you recommend and
why, and ask where to start. Write no criteria before the answer.
A set of one slice has nothing to choose: go straight on.

**The chosen slice.** Mark it `chosen` in the set and write its
document. A criterion is one starting state, one action and one
outcome a person could check by looking, with invented values,
named by its item and a number. Write the ordinary path and the
refusals this behaviour's own rule makes (a value it cannot take, a
thing that is not there): one for a rule, not one for every way of
mistyping, and none added to look thorough. Nothing the list does
not know of: no state, step or thing made up to have something to
refuse. A limit is a starting state, not a criterion of its own.
Not yours, and written once by later
stages: who may do it, a request for what is not theirs, the same
action done twice, the failure of anything the path depends on. A
criterion that compares (a duplicate, a match) says what makes two
things the same; where the list does not say, it goes under "Left
for later". No technology, provider, storage, structure or layout: a
provider the user set as a limit is named as that limit and no
more, and one the user floats in passing is left out of both
documents. No two criteria contradict. Nothing of tests, review or
delivery: criteria are not a definition of done. Then tell the user
what the slice is, its size and what it needs from outside.

**Holding the line.** When the user wants a slice wider, two joined,
everything in the first, the groundwork first or all the error
handling first: say once what that costs them (what is shown later,
what is built before anything is learned) and what the thin cut
gives, and offer the thin cut again; for error handling, offer it
spread over the slices as above. Change nothing yet. If they still
want it, it is theirs: change the set, say its size, and record
their reason in their own words under "What changed". Do not argue
twice. When the user is right, a slice too thin to show or two that
a person could not tell apart, join them without argument.

**Coming back.** When the report says a coming-back is due:

- Do what it lists and no more: mark a slice `built`, check a box.
  Only merged work marks or checks, never the user's word or yours.
- Place every issue it lists, without asking: in the slice in hand,
  in a later slice of the set, or in a later row of the scope map,
  each under "Issues" with why. `gh issue view <number>` reads one
  whose title does not say enough. Only an issue that no slice and
  no row covers is put to the user, in or out, and it is placed
  when they have answered.
- Say whether the list still holds. A change to it is named for the
  requirements stage, where the user confirms it: add or change no
  item yourself.
- Say whether the set still holds. Where it does, say so and leave
  it. Where it does not, propose the new set in your reply: each
  slice split, joined, added, dropped or moved, with its reason,
  the built ones as they are. Write it only after the user agrees,
  as the report says a changed set is written, ending with "What
  changed".
- Recommend what to start next. When the report says the activity
  is done, say so and ask which row of the scope map is the next
  "now".

A mark, a box and an issue's line are made in the documents as they
stand: they are no change to the set. When the user says that work
has turned something up (two slices are one, an item was wrong), it
is the same: propose, wait for the yes, and leave the item to the
requirements stage.

**Stop there.** No approach, no research, no design. Nothing on the
tracker is closed, labelled, commented on or begun.
