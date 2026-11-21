# Brief: answer part of the library's questions for one slice

You are given, in the folder your task names: `plan/` (the planning documents of one slice), `dossier.md` (what the public documentation says about everything the slice depends on, each fact with its source) and `cells.json`. You see no code and no account of how the product later behaved. Read nothing else on this machine. You may use the web only to read more of the public documentation of what the slice depends on.

Each cell of `cells.json` is one question from a library of the ways software commonly fails (`failure`, `question`), to be answered for one thing in this slice (`thing`). For every cell, read what the plan says and what the dossier says, and fill in four fields:

- `kind`, what sort of answer the question needs here, exactly one of:
  - `fact`: the answer depends on how something the product relies on actually behaves.
  - `owner`: the answer is a choice about what the product should do for the person using it, which only its owner can make.
  - `planner`: the answer is a technical choice with a sensible default.
- `tag`, exactly one of:
  - `DECIDED`: the plan settles what happens. Quote the words that settle it, with the document and line.
  - `PLAN SILENT`: the plan does not say.
  - `CONTRADICTS DOCS`: the plan decides it, but the documentation of something the product depends on says otherwise.
  - `IMPOSSIBLE`: it cannot happen for this thing. Say why in a few words.
- `says`: for `DECIDED`, the quoted words and where they are. For `PLAN SILENT` and `CONTRADICTS DOCS`, one or two sentences in this product's own terms: when exactly this would happen here, and what would then go wrong or what the person would meet. For `IMPOSSIBLE`, the reason.
- `source`: for every cell whose `says` states anything about how a dependency behaves, the dossier fact it rests on (its id) or a URL with a quote of at most 20 words. If the documentation does not say, write `NEEDS A TEST:` and the test against the real thing that would settle it. Otherwise an empty string.

Rules:

1. A plan's decision that rests on a belief about a dependency is checked against the dossier before it is tagged: if the documentation says otherwise it is `CONTRADICTS DOCS`, and if the documentation is silent the cell stays `DECIDED` with `source` set to `NEEDS A TEST: ...`.
2. Never state a fact about a dependency from memory. Cite it or mark it for a test.
3. A general statement in the plan settles a cell only if it plainly covers this thing in this case; when unsure, the cell is `PLAN SILENT`.
4. Fill every cell. Change nothing but `kind`, `tag`, `says` and `source`.

Output: the same array with those four fields filled, as valid JSON at the path your task gives. Then reply with one line: the count of each tag and of each kind.
