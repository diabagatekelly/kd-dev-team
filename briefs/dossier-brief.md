# Brief: what the documentation says about everything this slice depends on

You are given, in the folder your task names, `plan/`: the planning documents of one slice of a product. Read them all. You see no code and no account of how the product later behaved. Read nothing else on this machine. Use the web to read the public documentation of whatever the slice depends on.

A dependency is anything the product relies on that its team does not control: another party's service, the operating system's facilities, a storage engine, a runtime, a browser, a body of content or reference data. For each one this slice touches, write down what its own documentation says, so that people answering questions about the plan can rest on facts and not on belief.

## For each dependency

1. **Every request or operation the slice needs from it**, and for each: what goes in and what comes back (the fields the slice uses, which may be absent or empty); what exists on the other side afterwards; the documented errors, with their exact names; documented timings, readiness signals, paging and limits; whether repeating it is safe; what the documentation says about a reply that never arrives.
2. **Every statement the plan makes about it** (a number, a status, a name, an assumption, anything the plan marks as to be verified), each marked AGREES, CONTRADICTS or NOT COVERED by the documentation, with the plan's words and where they are, and the documentation's words and where they are.
3. **What the documentation does not say** that this slice relies on: list each as OPEN, with the test against the real thing that would settle it.

## Rules

- Every fact carries the URL of the page it came from and a quote of at most 25 words. If you could not open a page, say so and state nothing from it.
- Never fill a gap from memory or from what such systems usually do. An honest OPEN is worth more than a plausible guess.
- Read the documentation pages in full where they are long (in consecutive parts); the facts that matter are often far down the page.
- Say plainly when two pages disagree.

Output: one Markdown file at the path your task gives, with a section per dependency and, within it, the three parts above, each fact on its own line with an id (`F1`, `F2`, ...), the plan statements with ids (`S1`, ...), and the open points with ids (`O1`, ...). Then reply with one line: the number of facts, of statements by mark, and of open points.
