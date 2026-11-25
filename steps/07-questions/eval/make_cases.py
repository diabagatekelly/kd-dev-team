#!/usr/bin/env python3
"""Write the questions stage's cases for the plugin evaluation.

Every case starts inside the project's VM with the made-up playhouse of the approach's and
research's cases, planned as far as research would leave it: a document for PayRight, the made-up
payment provider, and the states of what lasts. Nothing is fetched here: the stage reads the
documents and the library, and draws. The report is the stage script's own, as it stands for each
case's documents.

An arm adds nothing for this stage (`bare`), this repository's text (`text`, from
`questions-skill.md`) or kad's `reliability-requirements` and `security-requirements` together
(`kad`, on cases 1 and 2: copied beside this file as `kad-<skill>.md`, or read from kad's
repository beside this one; never committed). The bare arm's routing table says this one stage is
done from the report alone (its last line would rightly stop it).

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import importlib.util
import io
import json
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location("research_cases", ROOT / "steps/06-research/eval/make_cases.py")
research = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(research)

startup, problem, requirements, load = research.startup, research.problem, research.requirements, research.load
questions = load("questions", ROOT / "questions/questions.py")
says, never_says, write = startup.says, startup.never_says, startup.write
in_file, not_in_file, trace, near = research.in_file, research.not_in_file, research.trace, research.near
SITE, TODAY, WROTE = research.SITE, research.TODAY, research.WROTE
KAD = {name: [HERE / f"kad-{name}.md", ROOT.parent / f"kad-dev-team-plugin/skills/{name}/SKILL.md"]
       for name in ("reliability-requirements", "security-requirements")}
ENTRIES = json.loads((ROOT / "library/library.json").read_text(encoding="utf-8"))

THE_TICKET, THE_PAYMENT, THE_SYSTEM = research.THE_TICKET, research.THE_PAYMENT, research.THE_SYSTEM
PAY_SLICE = research.PAY_SLICE % research.RECORDED
PAYRIGHT = f"""# Research: PayRight

## What the slice needs from it
- F1: A payment is taken with one request. "To take a payment, send POST /v1/payments" ({SITE}/payments)
- F2: The reply holds three fields, and the status of a new payment is always pending. "The reply holds id, status and created_at. A new payment always has the status pending." ({SITE}/payments)
- F3: The reply does not say whether the card was accepted. "The reply does not tell you whether the card was accepted." ({SITE}/payments)
- F4: A payment becomes settled or declined within three working days. "A payment moves from pending to settled or declined. This takes up to 3 working days." ({SITE}/statuses)
- F5: The change is told by an event sent to an address of ours. "We tell you by sending a payment.updated event to your webhook address." ({SITE}/statuses)
- F6: The same reference within a day takes no second payment. "Sending the same reference again within 24 hours returns the first payment and does not take a second one." ({SITE}/payments)
- F7: The card's details never reach us: a token stands for them, once, for fifteen minutes. "A card_token is made by our card form in the subscriber's browser and can be used once, within 15 minutes." ({SITE}/payments)
- F8: A refused card comes back as an error by name. "card_declined (402): the card's bank refused the payment." ({SITE}/errors)
- F9: An account may send 100 requests a minute, and is told how long to wait. "rate_limited (429): wait for the number of seconds in the Retry-After header." ({SITE}/errors)
- F10: A refund is a request with an amount, within ninety days. "A settled payment can be refunded in full or in part within 90 days of settling." ({SITE}/refunds)
- F11: Every request carries the account's secret key. "Send your secret key in the Authorization header of every request." ({SITE}/)

## What our documents say about it
- S1 CONTRADICTS: 000_problem.md says "PayRight tells us straight away whether a card payment has gone through". "The reply does not tell you whether the card was accepted." ({SITE}/payments)
- S2 CONTRADICTS: 000_problem.md says "We can refund a subscriber at any time". "After 90 days a refund is refused with refund_window_closed (422)." ({SITE}/refunds)
- S3 NOT COVERED: 000_problem.md says "PayRight charges us 1.4% of each payment". No page read speaks of it.
- S4 AGREES: slice-001/004_slice.md says "her payment is being taken". "A new payment always has the status pending." ({SITE}/payments)

## Open
- O1: What has happened when a request to take a payment gets no reply. Test: in PayRight's test mode, cut the connection after sending and ask for the payment by its reference.
- O2: Whether two events for one payment can arrive out of order. Test: in test mode, settle and refund a payment within a second and record the order the events arrive in.
"""
TICKET_TABLE = """## A season ticket

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `this-season` | the office issued it for this season | renew it for next season | renews and pays -> `renewed`; the season ends -> `lapsed` | "Given Ada Reyes holds a season ticket for this season" (slice-001/004_slice.md, renew-and-pay / 1) |
| `renewed` | the subscriber renews it and pays | not said in the documents | the office refunds the renewal -> not said in the documents | "then she is shown that her renewal is recorded" (slice-001/004_slice.md, renew-and-pay / 1) |
| `lapsed` | the season ends and it was not renewed | not said in the documents | not said in the documents | "about one in six lapses without anyone noticing" (000_problem.md) |
"""
PAYMENT_TABLE = f"""## A renewal payment

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `pending` | a payment is taken | wait | by itself -> `settled` or `declined` | "A new payment always has the status pending." ({SITE}/payments) |
| `settled` | PayRight settles it | nothing more | the office refunds it -> `refunded`; the cardholder disputes it -> `disputed` | "A payment moves from pending to settled or declined." ({SITE}/statuses) |
| `declined` | the card's bank refuses | pay again with another card | a new payment -> `pending` | "A declined payment is final. To try again, take a new payment with a new reference." ({SITE}/statuses) |
| `refunded` | the office refunds it | nothing more | none needed: the money is given back | "A settled payment can later become refunded or disputed." ({SITE}/statuses) |
| `disputed` | the cardholder disputes it | nothing: it is frozen | by itself -> `settled` or `lost` | "A disputed payment is frozen: it cannot be refunded or taken again until we close the dispute" ({SITE}/statuses) |
| `lost` | the dispute is lost | nothing | none | "or as lost, and the money goes back to the cardholder" ({SITE}/statuses) |
"""
DEAD_END = "\n## For the owner's list\n- `lost`: no way out. The money is the cardholder's again and the renewal stays recorded.\n"
STATES = "# States\n\n" + PAYMENT_TABLE + "\n" + TICKET_TABLE + DEAD_END
ONLY_THE_PAYMENT = "# States\n\n" + PAYMENT_TABLE + DEAD_END
ONLY_THE_TICKET = ("# States\n\nNothing is committed to, so no documentation was read: the rows come from the planning documents alone.\n\n"
                   + TICKET_TABLE.replace("renews and pays -> `renewed`", "renewed by hand at the office -> `renewed`"))
RESEARCHED = {"slice-001/006_research/payright.md": PAYRIGHT, "slice-001/006_research/states.md": STATES}

OPEN_QUESTION = ("1. **Part refunds (how much; bears on refund-a-renewal).** Can the office give back part of what a renewal "
                 "cost, or only all of it?\n")
QUOTE_LIST = """# Requirements: Renew a season ticket

- [ ] **renew-and-pay**: A subscriber can renew their season ticket for next season and pay for it by card.
- [ ] **quote-a-price**: The office can work out what a renewal costs before the subscriber decides.

## Out for now
- Single tickets: the next row of the scope map.

## Limits that apply
- None of the scope map's limits bears on this activity.

## Not yet confirmed
Nothing.

## Outside systems and lasting things
none
"""
QUOTE_SET = research.THE_SET % ("Work out what a renewal costs", "quote-a-price", "Renew a season ticket and pay for it", "renew-and-pay")
QUOTE_SLICE = """# Slice 1: Work out what a renewal costs

## Thin path
The office types a seat band and a number of seats and is shown what the renewal costs. Nothing is kept.

## Criteria
- **quote-a-price / 1**: Given the office is asked what a renewal costs, when they give seat band B and 2 seats, then they are shown the price for 2 seats in band B.
- **quote-a-price / 2**: Given the office gives a number of seats that is not a whole number from 1 to 8, when they ask for the price, then no price is shown and they are told how many seats a renewal may have.

## Needs from outside
none

## Left for later
- Renewing and paying: slice 2. Usable without it: the office tells the subscriber the price and renews by hand, as today.

## Size
Two criteria.
"""
CLOSES = ("- **renew-and-pay / 3**: Given renewals close at midnight on 31 March, when she renews at 23:59 that day, then her renewal is "
          "recorded, and one minute later she is told that renewals have closed.\n")
BY_CHOICE = research.approach(research.need(
    "Taking a card payment for a renewal, and giving it back", "no limit of the user's bears on it", f"PayRight ({SITE}/)",
    f'"To take a payment, send POST /v1/payments" ({SITE}/payments)', 'committed: PayRight (the user, 2026-11-20: "PayRight is fine.")',
    f"CardWay (https://{research.CARDWAY}/): the user chose the other.", research.UNSETTLED), research.PAYRIGHT_LINE)
TO_CARDWAY = research.approach(research.need(
    "Taking a card payment for a renewal, and giving it back", "no limit of the user's bears on it", f"CardWay (https://{research.CARDWAY}/)",
    f'"Take a card payment with one call" (https://{research.CARDWAY}/)',
    f'committed: CardWay (the user, {TODAY}: "Use CardWay after all, the bank gives us a better rate with them.")',
    f"PayRight ({SITE}/): the user changed their mind.")
    + f"Changed: {TODAY}: CardWay in place of PayRight; \"the bank gives us a better rate with them\".\n",
    f"- CardWay: https://{research.CARDWAY}/, for taking a card payment for a renewal, and giving it back.\n")
CARDWAY_RESEARCHED = {
    "slice-001/008_approach.md": TO_CARDWAY,
    "slice-001/006_research/payright.md": f"No longer stands: slice-001/008_approach.md commits to CardWay in its place ({TODAY}).\n\n" + PAYRIGHT,
    "slice-001/006_research/cardway.md": research.CARDWAY_DOC.replace(
        "## Open\nNothing.", "## Open\n- O1: What has happened when a charge gets no reply. Test: in CardWay's test mode, cut the connection after sending."),
    "slice-001/006_research/states.md": research.CARDWAY_STATES + "\n" + TICKET_TABLE}

# kept.md as an earlier run of the stage left it, for the two cases where the documents then change.
KEEP = {
    "call-external-01": ("`payment-request`; A renewal payment", "the payment is taken by one request to PayRight"),
    "call-external-02": ("`payment-request`", "a subscriber may press pay twice"),
    "call-external-03": ("PayRight", "she waits on the same screen for PayRight"),
    "call-external-06": ("`payment-request`", "a card can be refused, and a refusal by the bank is final"),
    "receive-external-data-07": ("`payment-status`", "the status comes from PayRight and may be one the slice does not know"),
    "secrets-03": ("`payright-key`", "every request carries the account's secret key"),
    "user-action-01": ("renew-and-pay / 1", "she starts a payment and may start it again"),
    "durable-write-02": ("A season ticket", "the renewal is shown as recorded"),
}
VALUES = [("payment-status", "choice", "PayRight", "no", "payright.md F2"),
          ("card-token", "identifier", "PayRight's card form in her browser", "credentials", "payright.md F7"),
          ("payright-key", "other", "the playhouse's own settings", "credentials", "payright.md F11"),
          ("refund-amount", "number", "the office", "no", "refund-a-renewal / 1")]
NO_CLOCK = "nothing in the slice depends on a date or on the clock"


def kept_file(keep=KEEP, values=VALUES):
    """A kept.md that accounts for every entry of the real library: what is kept, and each kind's rest dropped."""
    lines = ["# Kept: slice 1", "", "## What the slice takes in", "| Value | Kind | From | Sensitive | Source |", "|---|---|---|---|---|"]
    lines += [f"| `{name}` | {kind} | {origin} | {sensitive} | {source} |" for name, kind, origin, sensitive, source in values]
    lines += ["", "## Other things the slice has", "- `payment-request`: the request that takes the payment for a renewal (renew-and-pay / 1)",
              "", "## Library", "| Entry | Applies to | Why |", "|---|---|---|"]
    kinds = []
    for entry in ENTRIES:
        if entry["action"] not in kinds:
            kinds.append(entry["action"])
    for kind in kinds:
        rest = [entry["id"] for entry in ENTRIES if entry["action"] == kind and entry["id"] not in keep]
        lines += [f"| {name} | {applies} | {why} |" for name, (applies, why) in keep.items() if name.startswith(kind + "-")]
        if rest:
            why = NO_CLOCK if kind == "time" else "the slice does nothing more of this kind"
            lines.append(f"| {kind + ': all' if len(rest) == sum(entry['action'] == kind for entry in ENTRIES) else ', '.join(rest)} | dropped | {why} |")
    return "\n".join(lines) + "\n"


def playhouse(**kwargs):
    more = kwargs.pop("more", None) or {}
    documents = research.playhouse(kwargs.pop("the_slice", PAY_SLICE), **kwargs)
    return {**documents, **more}


def with_question(documents):
    return {**documents, "002_requirements.md": documents["002_requirements.md"].replace("## Not yet confirmed\nNothing.\n", "## Not yet confirmed\n" + OPEN_QUESTION)}


def row_of(entry, kind):
    """A row of kept.md's library that holds that entry, by its name or with its whole kind."""
    return rf"(?:^|\n)\|[^|\n]*(?:{entry}\b|{kind}:\s*all)[^|\n]*\|"


def keeps(entry, thing=None):
    kind = entry.rsplit("-", 1)[0]
    return in_file("@KEPT@", f"keeps-{entry}" + ("-for-the-right-thing" if thing else ""),
                   row_of(entry, kind) + r"(?!\s*`?dropped)" + (rf"[^|\n]*(?:{thing})" if thing else ""))


def drops(kind):
    return not_in_file("@KEPT@", f"drops-the-kind-{kind}", rf"(?:^|\n)\|[^|\n]*{kind}(?:-\d\d|:\s*all)[^|\n]*\|(?!\s*`?dropped)")


def takes_in(name, value, origin="", sensitive=""):
    return in_file("@KEPT@", name, rf"(?:^|\n)\|[^|\n]*(?:{value})[^|\n]*\|[^|\n]*\|[^|\n]*{origin}[^|\n]*\|\s*{sensitive}")


SENSITIVE = r"`?(?!no\b)[a-z]"   # the name of a class, or a plain yes
KEPT_WRITTEN = {"type": "file_exists", "name": "writes-what-is-kept", "path": "@KEPT@"}
DRAWN = [{"type": "tool_used", "name": "draws-with-the-command", "tool": "Bash", "min": 1, "input_match": r"questions\.py[\s\S]*\bdraw\b"},
         trace("the-command-drew", r"drawn(?:: |, and not written)[^\n]{0,600}?\d+ questions: ", never=False),
         trace("does-not-write-the-drawing-by-hand", WROTE + r"_questions/questions[.]md")]
# What nothing tells the bare model: that the library is read by the command, a few kinds at a time.
FORM = [{"type": "tool_used", "name": "form-reads-the-library-with-the-command", "tool": "Bash", "min": 2, "input_match": r"questions\.py[\s\S]*\blibrary\b"}]
NOTHING_ANSWERED = [not_in_file("@KEPT@", "answers-nothing", r"(?:^|\n)#+[^\n]*\b(answers?|decisions?)\b|(?:^|\n)\s*[-*]?\s*\**(Answer|Decision)\**\s*:"),
                    never_says("recommends-nothing", r"\bI(?:'d| would)? recommend(?!ed (?:nothing|no\b))|my recommendation")]
ASKS_NOTHING = [never_says("asks-no-preference", r"would you (like|prefer|rather)|do you (want|prefer)|which (would|do) you|your preference"),
                never_says("asks-nothing-of-the-product", r"(should|shall) (the product|it|we)\b[^.?\n]*\?|what should happen[^?\n]*\?|how (should|do you want)[^?\n]*\?")]
LATER = trace("writes-no-later-document", WROTE + r"_(answers|open-facts|design|screens|stack|readiness)")
EARLIER = trace("changes-no-earlier-document", WROTE + r"(00[0134]_(problem|scope-map|slices|slice)|_approach)[^\"]*[.]md")
LIST_LEFT = trace("leaves-the-requirements-alone", WROTE + r"002_requirements[.]md")
RESEARCH_LEFT = trace("leaves-research-alone", WROTE + r"_research/")
NO_TABLE = never_says("keeps-the-routing-table-out", r"\brouting table\b")
REAL = research.NO_REAL_NAME[0]
GO_ON = research.GO_ON
SKIP = "Skip this stage, it's a small slice. Go on to the design."
PUSHED_BACK = ("I can skip it, and it is yours to say. What it costs: the cases nobody lists are the ones found in the build, and the "
               "answers stage has nothing to be checked against. This stage asks nothing of you: I go through the library and a "
               "script draws the questions. Shall I do it after all?")
OFFERS = research.OFFERS

# name, what it shows, the documents, documents laid over them once the questions were drawn (or nothing), the user's words, checks,
# whether the requirements or research may be changed, earlier turns, whether kad's skills have something for it
SCENARIOS = [
    ("01-a-thing-committed-to-and-researched",
     "One thing committed to and researched, a thing held there and one the product keeps, a credential among what is taken in: every entry accounted for, the values listed, drawn by the command, nothing answered or asked.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more=RESEARCHED), None, GO_ON,
     [KEPT_WRITTEN, *DRAWN, *FORM,
      keeps("call-external-01", r"payment|request|payright"), keeps("call-external-06", r"payment|request|card|payright"),
      keeps("receive-external-data-07", r"status"), keeps("secrets-03", r"key|secret|credential|token"), keeps("user-action-01"),
      drops("corpus"),
      takes_in("lists-the-status-received", r"status", origin="PayRight"),
      takes_in("marks-the-card-token-sensitive", r"token|card", sensitive=SENSITIVE),
      takes_in("marks-the-secret-key-sensitive", r"key|secret|credential", sensitive=SENSITIVE),
      takes_in("lists-the-refund-amount", r"amount|refund"),
      trace("fewer-than-500-lines-from-the-library", r"drawn[^\n]{0,300}?questions: [1-4]?\d?\d from the library", never=False),
      *NOTHING_ANSWERED, LIST_LEFT, trace("leaves-the-research-document-alone", WROTE + r"_research/payright")], "", None, True),
    ("02-nothing-committed-to",
     "Nothing is committed to and the product keeps one thing, some of its rows not said: the kinds on outside systems dropped, every state drawn, no provider named.",
     playhouse(the_slice=research.SEE_SLICE, the_approach=research.WITHOUT, inventory=(THE_TICKET,), the_set=research.SEE_SET,
               more={"slice-001/006_research/states.md": ONLY_THE_TICKET}), None, GO_ON,
     [KEPT_WRITTEN, *DRAWN, *FORM, drops("call-external"),
      trace("draws-the-states", r"drawn[^\n]{0,600}?, [1-9]\d* of states", never=False),
      trace("carries-what-research-left-unsaid", r"drawn[^\n]{0,600}?, [1-9]\d* carried from research", never=False),
      REAL, *NOTHING_ANSWERED, LIST_LEFT, RESEARCH_LEFT], "", None, True),
    ("03-no-lasting-thing",
     "The slice keeps nothing and needs nothing from outside: the values and the library are still done, and no state is drawn.",
     {name: text for name, text in {**playhouse(the_slice=QUOTE_SLICE, the_set=QUOTE_SET, fixed=False), "002_requirements.md": QUOTE_LIST}.items()
      if "approach" not in name}, None, GO_ON,
     [KEPT_WRITTEN, *DRAWN, *FORM, drops("call-external"),
      takes_in("lists-the-number-of-seats", r"seats?|number"), takes_in("lists-the-seat-band", r"band"),
      trace("draws-no-state", r"drawn[^\n]{0,600}?, 0 of states", never=False),
      *NOTHING_ANSWERED, LIST_LEFT], "", None, False),
    ("04-a-thing-kept-with-no-states",
     "A criterion records a renewal of a season ticket and the states have no table for it: named first, walked by research's rules, then drawn.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT), more={**RESEARCHED, "slice-001/006_research/states.md": ONLY_THE_PAYMENT}), None, GO_ON,
     [KEPT_WRITTEN, *DRAWN,
      says("names-the-thing-with-no-states", near(r"season ticket|renewal(?! payment)", r"states|table|states\.md|walk", 300)),
      in_file("planning/slice-001/006_research/states.md", "its-table-is-added", r"(?:^|\n)##[^\n]*(?:season ticket|renewal(?! payment))"),
      in_file("planning/slice-001/006_research/states.md", "its-rows-are-sourced-or-said-not-to-be",
              r"(?:^|\n)##[^\n]*(?:season ticket|renewal(?! payment))[\s\S]*(00[0-4]_|not said in the documents)"),
      in_file("planning/slice-001/006_research/states.md", "the-other-table-is-left", r"A disputed payment is frozen"),
      *NOTHING_ANSWERED, LIST_LEFT], "research", None, False),
    ("05-an-earlier-question-answered",
     "The user answers one of the requirements' open questions in the message that says to go on: recorded there, said, and the questions drawn.",
     with_question(playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more=RESEARCHED)), None,
     GO_ON + " And on the open question about refunds: the office always gives back the whole price, never part of it.",
     [KEPT_WRITTEN, *DRAWN,
      not_in_file("planning/002_requirements.md", "the-question-is-no-longer-open", r"## Not yet confirmed[\s\S]*Can the office give back part"),
      in_file("planning/002_requirements.md", "the-answer-is-recorded", r"whole|in full|full price|all of it|never part|not part"),
      says("says-what-was-recorded", near(r"refund|whole|full", r"record|requirements|noted|wrote|updated|confirmed", 400)),
      *NOTHING_ANSWERED, RESEARCH_LEFT], "requirements", None, False),
    ("06-asked-what-is-needed",
     "The user offers to answer how failures should be handled: nothing is asked; said that the documents answer first and theirs comes once; the questions drawn.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more=RESEARCHED), None,
     GO_ON + " What do you need from me? Just ask me how failures should be handled and I'll tell you.",
     [KEPT_WRITTEN, *DRAWN,
      says("says-nothing-is-needed-now", r"nothing (is )?(needed|from you|to ask)|no(thing)? (questions?|input) (for|from) you|do(?: not|n't) need|not needed|"
                                         r"asks? (you )?nothing|none (for|from) you|later|once|one (short )?list"),
      *NOTHING_ANSWERED, LIST_LEFT, RESEARCH_LEFT], "", None, False),
    ("07a-skip-the-stage", "The user says to skip the stage: said once what it costs, the stage offered again; nothing written yet.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more=RESEARCHED), None, SKIP,
     [says("says-what-it-costs", r"build|found late|late|miss|nobody list|not listed|unasked|nothing to (be )?check|risk|cost|defect|gap"),
      says("says-it-asks-nothing-of-them", r"asks? (nothing|no)|nothing (of|from) you|no questions? (for|to) you|without (asking|you)|do(?: not|n't) need (anything|you)"),
      says("offers-the-stage-again", OFFERS),
      trace("writes-nothing-yet", WROTE + r"_questions/"), LIST_LEFT, RESEARCH_LEFT], "ask", None, False),
    ("07b-the-user-insists", "The next turn: the user insists: recorded as skipped at their word, what needs no judgement drawn, no design started.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more=RESEARCHED), None, "No. Skip it.",
     [{"type": "file_exists", "name": "records-the-skipping", "path": "@FOLDER@skipped.md"},
      in_file("@FOLDER@skipped.md", "in-their-words-with-the-date", r"skip[\s\S]*20\d\d-\d\d-\d\d|20\d\d-\d\d-\d\d[\s\S]*skip"),
      trace("writes-no-kept-file", WROTE + r"_questions/kept[.]md"), *DRAWN,
      says("says-it-goes-to-the-owners-list", r"owner'?s list|risk"),
      LIST_LEFT, RESEARCH_LEFT], "", [("user", SKIP), ("assistant", PUSHED_BACK)], False),
    ("08a-a-criterion-added-after",
     "A criterion was added to the slice after the questions were drawn, and it depends on the clock: the kind dropped before is kept, the earlier rows left, drawn again.",
     playhouse(inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), more={**RESEARCHED, "slice-001/007_questions/kept.md": kept_file()}),
     {"slice-001/004_slice.md": PAY_SLICE.replace("- **refund-a-renewal / 1**", CLOSES + "- **refund-a-renewal / 1**").replace("Three criteria", "Four criteria")},
     GO_ON,
     [*DRAWN,
      not_in_file("@KEPT@", "the-kind-is-no-longer-dropped-whole", r"\|\s*time:\s*all\s*\|\s*`?dropped"),
      in_file("@KEPT@", "a-question-of-the-clock-is-kept", r"(?:^|\n)\|[^|\n]*time-\d\d[^|\n]*\|(?!\s*`?dropped)"),
      in_file("@KEPT@", "the-earlier-rows-are-left", r"the payment is taken by one request to PayRight[\s\S]*a card can be refused, and a refusal by the bank is final"),
      *NOTHING_ANSWERED, LIST_LEFT, RESEARCH_LEFT], "", None, False),
    ("08b-the-approach-changed-after",
     "The approach changed and research was written again for another thing after the questions were drawn: nothing left that applies to the old thing, drawn again.",
     {**playhouse(the_approach=BY_CHOICE, inventory=(THE_SYSTEM, THE_PAYMENT, THE_TICKET), fixed=False,
                  more={**RESEARCHED, "slice-001/007_questions/kept.md": kept_file()})},
     CARDWAY_RESEARCHED, GO_ON,
     [*DRAWN,
      not_in_file("@KEPT@", "nothing-applies-to-the-old-thing", r"payright"),
      in_file("@KEPT@", "the-new-thing-is-applied-to", r"cardway|charge"),
      in_file("@KEPT@", "the-earlier-rows-are-left", r"user-action-01[^|\n]*\|[^|\n]*renew-and-pay"),
      *NOTHING_ANSWERED, LIST_LEFT, RESEARCH_LEFT], "", None, False),
]
BARE_TABLE = ("- The questions stage has no text of its own here: do it from this report and the documents. A later stage "
              "with no text of its own here is not built yet. Say so and stop: do not do its work some other way, "
              "and do not offer to.\n")


def main(arm):
    if arm not in ("bare", "kad", "text"):
        raise SystemExit("arm: bare, kad or text")
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-questions-trial-{arm}", "version": "0.0.1",
         "description": "Stage 7's test only: startup and the earlier stages as adopted, and one arm's text."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n', executable=True)
    table = (ROOT / "steps/00-startup/eval/routing-table.md").read_text(encoding="utf-8")
    if arm != "text":
        last = table.rindex("- A stage with no text")
        assert "not built yet" in table[last:]
        table = table[:last] + (BARE_TABLE.replace("has no text of its own here: do it from this report and the documents",
                                                   "is done with the skills the user names") if arm == "kad" else BARE_TABLE)
    write(plugin / "hooks" / "routing-table.md", table)
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for script in ("research/page.py", "questions/questions.py", "library/library.json"):
        write(plugin / script, (ROOT / script).read_text(encoding="utf-8"))
    for name, source in load("make_plugin", ROOT / "e2e/make_plugin.py").SKILLS.items():
        if name != "questions":   # this stage's own text is one arm's, not every arm's
            write(plugin / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    if arm == "kad":
        for name, places in KAD.items():
            write(plugin / "skills" / name / "SKILL.md", next(path for path in places if path.exists()).read_text(encoding="utf-8"))
    elif arm == "text":
        write(plugin / "skills" / "questions" / "SKILL.md", (HERE / "questions-skill.md").read_text(encoding="utf-8"))
    else:
        used = []
    cleanup = startup._Cleanup()
    for name, description, documents, after, prompt, graders, may, earlier, for_kad in SCENARIOS:
        if arm == "kad":
            if not for_kad:
                continue
            prompt += " Use the reliability-requirements and security-requirements skills."
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        (machine.project / "planning").mkdir()
        machine.run("stage.sh", "remember", "planning")

        def lay(these):
            for relative, text in these.items():
                path = machine.project / "planning" / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8", newline="\n")
        lay(documents)
        if after is not None:
            # The questions as drawn from the documents before they changed, by the script itself.
            said = io.StringIO()
            assert questions.main(["draw", str(machine.project / "planning/slice-001")], said) == 0, (name, said.getvalue())
            lay(after)
        done = machine.run("report.sh")
        found = re.search(r"next stage by the documents: questions \(its document: (\S+/), ([^\n]*)", done.stdout)
        assert done.returncode == 0 and found, (name, done.stdout)
        assert ("to draw again" in found.group(2)) == (after is not None), (name, found.group(2))
        folder = found.group(1)
        report = done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@")
        assert str(ROOT) not in report, (name, report)
        machine.set("gh/summary", done.stdout.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        machine.set("web/allowed", "api.anthropic.com")
        checks = list(graders) + [LATER, EARLIER, NO_TABLE] + ([] if may == "ask" else ASKS_NOTHING) + used
        if may == "research":
            checks = [check for check in checks if check is not RESEARCH_LEFT]
        checks = json.loads(json.dumps(checks).replace("@KEPT@", folder + "kept.md").replace("@FOLDER@", folder))
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, checks, earlier)
              .replace("name: problem-", "name: questions-").replace("tags: [problem]", "tags: [questions]")
              .replace("max_turns: 20", "max_turns: 60").replace("timeout_seconds: 400", "timeout_seconds: 1200"))
        # The folder is there when the run starts: a run's shell cannot make one.
        write(case / "scaffold.sh", startup.scaffold(machine) + f"mkdir -p {folder}\n", executable=True)
        if earlier:
            write(case / "history.jsonl", startup.history(earlier))
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(checks)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bare")
