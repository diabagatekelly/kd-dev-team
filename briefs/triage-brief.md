# Brief: which of the library's questions matter for this slice

You are given, in the folder your task names: `plan/` (the planning documents of one slice of a product) and `library.json` (a library of the ways software commonly fails, by kind of action; each entry has an `id`, an `action`, a `failure` and the `question` a plan must answer because of it). Read every planning document and every entry. Read nothing else on this machine and do not use the web. You see no code and no account of how the product later behaved.

For every entry, decide whether its question matters for this slice: can the entry's condition arise from something this slice adds or changes, so that what the product then does would matter to the person using it or to whoever maintains it?

- It matters even if the plan already answers it. You are not judging whether the plan covers it, only whether the question has to be asked here.
- It does not matter if the slice does nothing of that kind, or if the condition cannot arise for anything the slice does. Say which.
- When unsure, it matters. A question wrongly dropped is lost for good; one wrongly kept costs a line.

Output: a JSON array at the path your task gives, one object per entry of the library, in the library's order, with exactly:

- `id`: the entry's id, unchanged.
- `relevant`: `true` or `false`.
- `why`: one sentence. For `false`, why the condition cannot arise in this slice. For `true`, what in the slice makes it arise.
- `applies_to`: for `true`, the list of things in the slice the question must be answered for, each named in the product's own terms (each request, each stored thing, each setting, each field, each screen, as the case may be); for `false`, an empty list.

Then reply with one line: how many entries are relevant, and the total of the `applies_to` lists.
