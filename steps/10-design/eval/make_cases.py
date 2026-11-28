#!/usr/bin/env python3
"""Write the cases of the design for the plugin evaluation.

Every case starts where the tests of open facts leave the made-up playhouse's slice that takes a
payment through a provider: the questions drawn, every one settled by answers "written before" (most
of them dismissed, so that the few a case is about stand out), two tests left open with what the
slice does either way, and one decision the owner took. Nothing real is fetched or sent.

An arm adds nothing for this stage (`bare`) or this repository's text (`text`, from
`design-skill.md`). kad's `architecture-design` is not an arm here: it is set beside ours on the two
real plans, where its own designs are kept.

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import io
import json
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "e2e"))   # found under -I


def load(name, path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


o = load("open_facts_cases", ROOT / "steps/09-open-facts/eval/make_cases.py")
design = load("design", ROOT / "designing/design.py")
a, s, q, answers, openfacts = o.a, o.s, o.q, o.answers, o.openfacts
startup, problem, questions = q.startup, q.problem, q.questions
says, never_says, write, in_file, not_in_file, trace, WROTE = q.says, q.never_says, q.write, q.in_file, q.not_in_file, q.trace, q.WROTE

# What an earlier session settled that a design must give a home: a criterion that rests on the provider's own words, a
# secret, the events, two things that fail with no criterion of their own, and one decision the owner took.
REFERENCE = """## A931: A payment request sent again
Kind: chosen
Says: Every payment request to PayRight carries a reference the product makes for that renewal, so that a request sent again takes no second payment.
Rests on: payright F6: "Sending the same reference again within 24 hours returns the first payment and does not take a second one."
Settles: L.call-external-02.payment-reference
Under: renew-and-pay
Criterion: Given a renewal whose payment request was sent, when the same request is sent again within 24 hours, then the subscriber is shown one payment for it.
"""
SECRET = """## A932: The secret key
Kind: chosen
Says: The secret key is read once from the settings of where the product runs, and no record, message or screen holds it.
Rests on: good practice for a credential.
Settles: L.secrets-03.secret-key
Under: renew-and-pay
Criterion: Given a payment request that failed, when the office reads the record of it, then nothing of the secret key appears in it.
"""
EVENTS = """## A933: A change of a payment told twice, or late
Kind: chosen
Says: A change of a renewal payment is applied once: the same change told again changes nothing, and one older than the state already held is set aside and recorded as set aside.
Rests on: a change applied twice, or an old one applied late, would show a refunded renewal as paid.
Settles: L.receive-external-data-02.payment-updated-event
"""
FAILED_SAVE = """## A934: The renewal cannot be saved after the money was taken
Kind: chosen
Says: When the payment was taken and recording it fails, the subscriber is told her payment is being checked, and the office is shown a payment with no renewal until one is recorded for it.
Rests on: money taken with nothing recorded is the worst this slice can do.
Settles: L.durable-write-05.renewal-payment
"""
UNREADABLE = """## A935: What is stored cannot be read at start
Kind: chosen
Says: The product does not start on stored renewals it cannot read: it says which could not be read and changes nothing.
Rests on: starting on an empty store would show every season ticket as not renewed.
Settles: L.startup-read-03.renewal-payment
"""
WHO_REFUNDS = (o.THEIRS[2].replace("Settles:", 'Decided: one named person (the user, 2026-03-01: "one named person, me")\nSettles:')
               + "Under: refund-a-renewal\nCriterion: Given someone in the office who is not the named person, when they ask to refund a renewal, then it is refused and they are told who can.\n")
BASE = [REFERENCE, SECRET, EVENTS, FAILED_SAVE, UNREADABLE, WHO_REFUNDS, o.NO_REPLY, o.ORDER]
# The two tests left open, as the stage before sorted them.
OPEN_FACTS = (o.OPEN_HEAD
              + o.block(1, "A901", "person", "Either way: a renewal whose payment request got no reply is shown as not yet known, and its payment is asked for again by its reference before anything else is done.")
              + "\n" + o.block(2, "A904", "later", "Either way: a change older than the state already held changes nothing.")
              + "\n## The owner's list, read\n")
# What a case adds.
TWO_COPIES = ["""## A941: Two copies of the product
Kind: chosen
Says: Two copies of the product may run at once: the documents do not say that only one does, so nothing may rest on there being one.
Rests on: the documents are silent on it.
Settles: L.startup-read-06.renewal-payment
""", """## A942: Two renewals of one season ticket at the same moment
Kind: chosen
Says: Of two renewals of one season ticket made at the same moment, one is recorded and the other is told the ticket is already being renewed; one payment is asked for.
Rests on: two payments for one renewal is money taken twice.
Settles: L.concurrency-09.renew-and-pay-1
Under: renew-and-pay
Criterion: Given a season ticket being renewed in one window, when it is renewed in a second window before the first is recorded, then the second is told it is already being renewed and one payment is shown.
"""]
EMAIL = """## A951: Learning days later that a payment settled or was declined
Kind: chosen
Says: A subscriber whose payment settles or is declined after she has left is sent an email that says so, at the address the playhouse holds for her.
Rests on: she is no longer looking at the screen when it is known.
Settles: L.long-operation-05.renewal-payment
Under: renew-and-pay
Criterion: Given a renewal whose payment is declined two days later, when the change is known, then an email telling her so is sent to her address within 10 minutes.
"""
TREATS_AS = """## A961: When a refund counts as given back
Kind: chosen
Says: The product treats a refund as given back as soon as the refund request to PayRight is answered, and shows the subscriber as refunded then.
Rests on: payright F10: "A settled payment can be refunded in full or in part within 90 days of settling."
Settles: L.call-external-10.refund-request
"""
RECORD = """## A971: A record of money moved
Kind: chosen
Says: Every payment taken and every refund given leaves a line the office can read, with the renewal it was for, when, and by whom.
Rests on: money moved with no record cannot be explained to a subscriber.
Settles: L.logging-01.renewal-payment
"""
# A design as an earlier session left it, which the script draws.
PARTS = """# Design: slice 1

## Importance
1. A renewal and the money taken for it: a defect takes money twice, or takes it and loses the renewal.
2. Who may give money back: a defect gives the playhouse's money away.
3. What the subscriber and the office are shown: a defect misleads, and can be put right.
4. The edges to the card payment provider and to what is stored: a defect there is seen, and either can be swapped.

## C1: Renewal
Side: strategic
Does: Records a subscriber's renewal of her season ticket before its payment is asked for, asks for that payment once under a reference of its own, and moves the season ticket when the payment is known. When the payment was taken and cannot be recorded, it says the payment is being checked and shows the office a payment with no renewal.
Home of: renew-and-pay / 1, renew-and-pay / 2, A931, A934, T1
Holds: a renewal payment: pending, settled, declined; a season ticket: this-season, renewed, lapsed
Sees: her-details
Uses: B1, B2

## C2: Refund
Side: strategic
Does: Gives a renewal's money back when the one who may refund asks, refuses anyone else, and shows the subscriber as refunded.
Home of: refund-a-renewal / 1, A913
Holds: a renewal payment: refunded
Sees: her-details
Uses: C1, B1, B2

## C3: Payment news
Side: strategic
Does: Takes each change of a payment as it is told, applies it once, and sets aside one older than the state already held, recording that it did.
Home of: A933, T2
Holds: a renewal payment: disputed
Uses: C1, B2

## C4: Card payments
Side: tactical
Does: The only part that knows PayRight: it sends payment and refund requests with the secret key, receives its events, and turns replies, events and refusals into the product's own outcomes. A request with no reply comes back as not yet known.
Home of: A932
Sees: credentials
Implements: B1
Isolates: PayRight
Leans on: payright F1 "To take a payment, send POST /v1/payments"; payright F6 "Sending the same reference again within 24 hours returns the first payment and does not take a second one."; T1; T2

## C5: Renewal records
Side: tactical
Does: Keeps renewals, their payments and season tickets through a restart. At start it refuses records it cannot read, says which, and changes nothing.
Home of: A935
Sees: her-details
Implements: B2

## C6: Start-up
Side: wiring
Does: Reads the settings once, makes each part and hands it what it uses.
Uses: C1, C2, C3, C4, C5

## B1: Taking a payment and giving it back
Owned by: C1
Crosses: an amount, a reference of the product's own, and back one of taken and being settled, refused, not yet known; for a refund, given back or refused with why.
Needs: a request that can be sent again under the same reference without taking money twice.
Technology: forced: the slice exists to take a card payment through the provider the problem fixes.

## B2: Keeping renewals
Owned by: C1
Crosses: a renewal, its payment's state and its season ticket's state, as plain values.
Needs: what is kept survives a restart, and a change is refused when the state it read has moved.
Technology: not forced: records held in memory, with the same refusal of a moved state, satisfy every test of this slice but the restart, which a file under a temporary folder satisfies.

## D1: The renewal is recorded before its payment is asked for
Kind: chosen
Says: A renewal is recorded as waiting for its payment, then the payment is asked for under the renewal's reference.
Instead of: asking for the payment first, which leaves money taken and nothing recorded if the product stops between the two.
Because: stopped between the two steps, a renewal with no payment is left, which is asked for again by its reference; never a payment with no renewal.
Costs: a renewal can be seen waiting for a payment that was never asked for, and must be shown as such.
Architectural: yes: it orders the two steps every renewal takes.
Significant: yes: going back means changing what a stop half way leaves, and everything that reads it.
Non-obvious: yes: taking the money first is the usual order.

## D2: A change to a renewal payment names the state it read
Kind: chosen
Says: Each change of a renewal payment says which state it read, and is refused when the state has moved since.
Instead of: a lock held while the provider is asked, which a stop would leave held.
Because: nothing is held, so nothing is left behind by a stop.
Costs: a refused change is read again and asked again.
Architectural: yes: every part that changes a payment follows it.
Significant: yes: later slices that change a payment follow it.
Non-obvious: yes: a lock is the usual answer.
Keeps apart: a refund by the office and a change of the same payment told by the provider's event.
Two at once: both read settled; the first writes, the second is refused on the moved state, reads again and finds what the first left.
Crash: after the read and before the write nothing was changed, and the next reading is true.
Crash: after the write nothing is held, and the change stands.
Stopped while waiting: nothing waits on another; a stop between the read and the write changes nothing.
Leftover: there is no marker to leave, remove or change.
Reused name: nothing names an owner.

## At once
D2 keeps a refund and a change told by an event apart.

## Tests
Real: renewal records under a temporary folder, and the renewal, the refund and the payment news behind their real entries.
Faked: PayRight at its wire (its replies, its refusals, a request with no reply, its events), and the clock.

## Kept for later slices
The state of each season ticket and of each renewal payment, and the provider's payment id with the product's own reference: slice 2 reads which tickets are not renewed.

## No home
- renewal-payment.lost: a dispute lost is outside this slice; the state is kept as it is told and nothing here acts on it.
"""
RISK = """
## D3: Money taken and no renewal recorded
Kind: owner
Says: Between the provider taking a payment and the product recording it there is a moment no structure removes; D1 makes it rare, not impossible.
Options: the office is shown each morning any payment with no renewal and decides | any payment with no renewal after an hour is given back by itself
Recommended: the office is shown each morning any payment with no renewal and decides, because giving money back by itself can undo a renewal that was only slow.
If left: a payment with no renewal is seen only when the subscriber complains.
Harm: high
"""
WITH_RISK = PARTS.replace("\n## At once", RISK + "\n## At once")
# A project that already has code: season tickets kept by a part that exists, and the office's refund page calling the provider itself.
CODE = {"README.md": "# Playhouse\n\nSubscribers and their season tickets. Run with `python3 -m app`.\n",
        "app/__init__.py": "",
        "app/subscribers.py": ('"""Subscribers and their season tickets, kept in one file under data/."""\nimport json\nimport pathlib\n\nDATA = pathlib.Path("data/subscribers.json")\n\n\n'
                               "def season_ticket(ticket_id):\n    return json.loads(DATA.read_text())[\"tickets\"][ticket_id]\n\n\n"
                               "def set_season_ticket_state(ticket_id, state):\n    data = json.loads(DATA.read_text())\n    data[\"tickets\"][ticket_id][\"state\"] = state\n"
                               "    DATA.write_text(json.dumps(data))\n"),
        "app/office_pages.py": ('"""The office\'s pages."""\nimport os\nimport urllib.request\n\nfrom app import subscribers\n\n\n'
                                "def refund_page(ticket_id, payment_id):\n    # Gives the money back straight from the page.\n"
                                "    request = urllib.request.Request(f\"https://api.payright.example/v1/payments/{payment_id}/refunds\", method=\"POST\",\n"
                                "                                     headers={\"Authorization\": \"Bearer \" + os.environ[\"PAYRIGHT_SECRET_KEY\"]})\n"
                                "    urllib.request.urlopen(request)\n    subscribers.set_season_ticket_state(ticket_id, \"refunded\")\n    return \"Refunded.\"\n")}

D = "@DESIGN@"
NEXT = {"type": "tool_used", "name": "form-asks-the-command-what-has-no-home", "tool": "Bash", "min": 1, "input_match": r"design\.py[\s\S]*\bnext\b"}
DRAW = {"type": "tool_used", "name": "draws-with-the-command", "tool": "Bash", "min": 1, "input_match": r"design\.py[\s\S]*\bdraw\b"}
DREW = r"drawn(?:: |, and not written)[^\n]{0,700}?"
NOTHING_WAITS = trace("the-command-drew-with-nothing-waiting", DREW + r"\b[2-9] parts \([1-9] strategic, [1-9] tactical\)[^\n]*0 decisions wait for the owner; 0 go back", never=False)
NOT_BY_HAND = trace("does-not-write-the-drawing-by-hand", WROTE + r"_designed[.]md")
LEFT_ALONE = [trace("changes-no-earlier-document", WROTE + r"(00[0-4]_(problem|scope-map|requirements|slices|slice)|_approach|_research/|_questions/|_answers|_open-facts)"),
              trace("writes-no-later-document", WROTE + r"_(screens|stack|readiness|owner-list)"),
              trace("writes-no-code", WROTE + r"/(app|src|lib)/[^\"]*[.](py|js|ts)")]
NOT_WHOLE = trace("form-never-writes-the-design-again-whole", r"\"name\"\s*:\s*\"Write\"[\s\S]{0,80}?file_path\\?\"\s*:\s*\\?\"[^\"]*_design[.]md")
NOTHING_WRITTEN = trace("writes-nothing", WROTE + r"_design[.]md")
SKIP = "Skip the design, it's a small slice. Just start building."
PUSHED_BACK = ("I can skip it, and it is yours to say. What it costs: how the slice is made up, and which part is the home of each criterion and each "
               "open fact, is then settled by whoever builds it, one file at a time. The design asks almost nothing of you. Shall I do it?")
PLUGGABLE = "Go on. And make the payment part pluggable, with a registry of providers, so we can add other providers later."
SAID_THE_COST = ("The design is drawn: six parts, with PayRight known to one of them only, behind a boundary the renewal owns. I did not add a registry of "
                 "providers: the problem fixes PayRight for two more years, so there is one real case, and a registry would be built and tested for a "
                 "second that may never come; the boundary already lets the provider be swapped by writing one part. It is yours to insist on.")
BROUGHT = ("The design is drawn and one decision waits for you. Money taken and no renewal recorded: between PayRight taking a payment and the product "
           "recording it there is a moment no structure removes. Either the office is shown each morning any payment with no renewal and decides "
           "(recommended, because giving money back by itself can undo a renewal that was only slow), or any payment with no renewal after an hour is "
           "given back by itself. If left, such a payment is seen only when the subscriber complains.")


def block(letter, name, *also):
    """A block of the design of that letter that holds every pattern in `also`."""
    return in_file(D, name, rf"(?:^|\n)## {letter}\d+" + "".join(r"(?=(?:(?!\n## )[\s\S])*?" + each + ")" for each in also))


ORDERS = [r"\nKeeps apart:\s*\S", r"\nTwo at once:\s*\S", r"\nCrash:\s*\S", r"\nStopped while waiting:\s*\S", r"\nLeftover:\s*\S", r"\nReused name:\s*\S"]
# name, what it shows, the answers a case adds, what is laid after the open facts are drawn (a function of the document names), the user's
# words, checks, earlier turns
SCENARIOS = [
    ("01-a-slice-designed",
     "The slice as the open facts leave it: the command asked what has no home, parts named for the product, one tactical part alone knowing the provider "
     "and leaning on its research's words, the open facts and what fails given their homes, what is faked said, what slice 2 will read kept, a decision "
     "chosen with its three checks and not asked, drawn by the command.",
     [], None, q.GO_ON,
     [NEXT, block("C", "one-tactical-part-isolates-the-provider-and-leans-on-its-words", r"\nSide:\s*tactical", r"\nIsolates:[^\n]*PayRight", r"\nLeans on:[^\n]*payright[^\n]*F\d+[^\n]*\""),
      block("C", "an-open-fact-has-its-home-in-a-part", r"\nHome of:[^\n]*\bT1\b"),
      block("C", "what-fails-with-no-criterion-has-its-home-in-a-part", r"\nHome of:[^\n]*\bA934\b"),
      block("C", "the-owners-decision-has-its-home", r"\nHome of:[^\n]*\bA913\b"),
      block("B", "a-boundary-says-what-it-needs-of-what-stands-behind", r"\nOwned by:\s*C\d+", r"\nNeeds:\s*\S", r"\nTechnology:\s*(not )?forced:"),
      block("D", "a-decision-is-chosen-with-what-was-not-taken-and-the-three-checks", r"\nKind:\s*chosen", r"\nInstead of:\s*\S", r"\nCosts:\s*\S", r"\nArchitectural:\s*(yes|no)\b",
            r"\nNon-obvious:\s*(yes|no)\b"),
      in_file(D, "the-tests-fake-the-provider-at-its-wire", r"\n## Tests\n[\s\S]*?Faked:[^\n]*PayRight"),
      in_file(D, "says-what-a-later-slice-will-read", r"\n## Kept for later slices\n+\s*(?![-* ]*none\b)\S"),
      DRAW, NOTHING_WAITS, NOT_BY_HAND, *LEFT_ALONE, *q.ASKS_NOTHING], None),
    ("02-two-things-at-once",
     "The answers say two copies may run and two renewals of one ticket may come at the same moment: a decision keeps them apart and is walked through "
     "every bad order before it is chosen; `At once` names it; drawn.",
     TWO_COPIES, None, q.GO_ON,
     [NEXT, block("D", "what-keeps-them-apart-is-walked-through-every-order", *ORDERS), in_file(D, "at-once-names-the-decision", r"\n## At once\n[\s\S]*?\bD\d+\b"),
      block("C", "the-two-renewals-have-their-home", r"\nHome of:[^\n]*\bA942\b"), DRAW, NOTHING_WAITS, NOT_BY_HAND, *LEFT_ALONE], None),
    ("03-a-lock-the-user-proposes",
     "Two copies may run, and the user proposes a lock file with the process number: it is walked through its orders like any other, what a crash leaves "
     "and a number given out again are said, and it is not taken as it stands: a mechanism with no such hole is chosen, or the hole is the owner's to accept.",
     TWO_COPIES, None, "Go on. For two copies running at once, just write a lock file with the process number at start and delete it at exit.",
     [block("D", "the-lock-is-walked-through-every-order", *ORDERS),
      says("says-what-a-crash-leaves", r"crash|killed|stops? (half|before|without)|left behind|stale|never (deleted|removed)|power"),
      says("says-the-number-may-be-given-out-again", r"reus|given (out )?again|another process|same (process )?number|taken over by|no longer (the|its)|not the (one|process)"),
      not_in_file(D, "a-hole-is-not-chosen", r"(?:^|\n)## D\d+(?=(?:(?!\n## )[\s\S])*?\nKind:\s*chosen)(?=(?:(?!\n## )[\s\S])*?\n(?:Crash|Leftover|Reused name):[^\n]*"
                                              r"(stuck until|until someone|nobody (would |will |can )?(know|notice)|both (proceed|run|go on)))"),
      DRAW, trace("the-command-drew", DREW + r"\b[2-9] parts \(", never=False), NOT_BY_HAND, *LEFT_ALONE], None),
    ("04a-a-part-for-a-case-that-may-come",
     "The user asks for a registry of providers for others that may come: the slice is designed as recommended, with the provider behind one boundary; "
     "said once what the registry would cost here and that it is theirs to insist on; no registry is designed.",
     [], None, PLUGGABLE,
     [says("says-what-it-would-cost-here", r"one (real )?(case|provider)|only (one|PayRight)|two (more )?years|no second|second (provider|case)|may (never )?come|not need(ed)?|speculat|nothing (uses|needs)"),
      says("says-it-is-theirs-to-insist-on", r"insist|still want|your (call|choice|decision)|yours to|say so|if you (do|still|would)|tell me|\?"),
      not_in_file(D, "designs-no-registry", r"(?:^|\n)## C\d+:[^\n]*(registr|plug-?in)"),
      block("C", "one-tactical-part-isolates-the-provider", r"\nSide:\s*tactical", r"\nIsolates:[^\n]*PayRight"),
      DRAW, NOTHING_WAITS, NOT_BY_HAND, *LEFT_ALONE], None),
    ("04b-the-user-insists",
     "The next turn: the user insists on the registry: it is theirs, recorded as a decision of the owner's in their words with the date and its cost, "
     "the parts changed to match, drawn again; the next stage not started.",
     [], lambda names: {names["design"]: PARTS, "draw": True}, "No, I want the registry. We will add a second provider next year.",
     [block("D", "recorded-as-the-owners-in-their-words", r"\nKind:\s*owner", r"\nDecided:[^\n]*\(the user, 20\d\d-\d\d-\d\d: \"[^\"\n]+\"\)", r"\nIf left:\s*\S"),
      in_file(D, "the-parts-are-changed-to-match", r"(?:^|\n)## [CB]\d+:(?=(?:(?!\n## )[\s\S])*?(registr|provider))"),
      DRAW, trace("the-command-drew-with-none-waiting", DREW + r"0 decisions wait for the owner", never=False), NOT_WHOLE, NOT_BY_HAND, *LEFT_ALONE],
     [("user", PLUGGABLE), ("assistant", SAID_THE_COST)]),
    ("05-a-need-from-outside-the-approach-lacks",
     "An answer has the product send an email, and the approach commits to nothing that sends one: it goes back to the approach, said to the user with "
     "whose it is; no way of sending is picked here; drawn with one thing going back.",
     [EMAIL], None, q.GO_ON,
     [in_file(D, "sends-it-back-to-the-approach", r"\n## Goes back\n[\s\S]*?[-*]\s*`?approach`?\s*:[^\n]*(e-?mail|send)"),
      says("says-it-is-the-approachs", r"approach"), says("says-what-is-needed", r"e-?mail"),
      not_in_file(D, "picks-no-way-of-sending-here", r"\b(SendGrid|Mailgun|Postmark|Amazon SES|\bSES\b|SMTP|sendmail|Mailchimp|Resend)\b"),
      DRAW, trace("the-command-drew-with-one-going-back", DREW + r"\b[1-9] go back to an earlier stage", never=False), NOT_BY_HAND, *LEFT_ALONE], None),
    ("06-asked-for-what-is-out",
     "The user asks for single tickets through the same part, which the requirements put out for now: nothing of it is designed, said whose it is to "
     "change; the slice as it stands is designed and drawn, and no earlier document is changed.",
     [], None, "Go on. And put single tickets through the same payment part while you are at it.",
     [says("says-it-is-out-for-now", r"out for now|not in (this|the) slice|scope map|requirements|next row|later"),
      not_in_file(D, "designs-nothing-for-single-tickets", r"(?:^|\n)## [CBD]\d+:[^\n]*single ticket|\nHome of:[^\n]*single"),
      DRAW, trace("the-command-drew", DREW + r"\b[2-9] parts \(", never=False), NOT_BY_HAND, *LEFT_ALONE], None),
    ("07-leaned-on-and-not-known",
     "An answer says the product treats a refund as given back once the request is answered, on words of the research that say nothing of when: the "
     "design names it as leaned on and not known, with what the part does either way; drawn, and counted.",
     [TREATS_AS], None, q.GO_ON,
     [in_file(D, "names-what-is-leaned-on-and-not-known", r"\nLeans on:[^\n]*\bunknown\s*:\s*\S"), in_file(D, "says-what-is-done-either-way", r"\nEither way:\s*\S"),
      DRAW, trace("the-command-counted-it", DREW + r"\b[1-9] things leaned on and not known", never=False), NOT_BY_HAND, *LEFT_ALONE], None),
    ("08-a-project-that-already-has-code",
     "The project has code: season tickets are kept by a part that exists, and the office's refund page calls the provider itself. The code is read "
     "first; what exists is used under its name; the fault is located, with a decision to put it right now or leave it; no code is written.",
     [], lambda names: {"code": True}, q.GO_ON,
     [{"type": "tool_used", "name": "reads-the-code-first", "tool": "*", "min": 1, "input_match": r"app/|subscribers|office_pages|\*\*/\*[.]py|[.]py\b"},
      in_file(D, "says-what-is-already-there", r"\n## Already there\n[\s\S]*?subscribers"),
      in_file(D, "locates-the-fault", r"(refund|office)[\s\S]{0,300}(PayRight|provider)[\s\S]{0,300}(direct|itself|straight|own|bypass|without|not through|outside)|"
                                      r"(direct|itself|straight|bypass|not through)[\s\S]{0,300}(PayRight|provider)"),
      block("D", "decides-now-or-later", r"\nKind:\s*(chosen|owner)", r"(refund page|office page|office_pages|office's page|existing|already)"),
      DRAW, trace("the-command-drew", DREW + r"\b[2-9] parts \(", never=False), NOT_BY_HAND, *LEFT_ALONE], None),
    ("09a-skip-the-stage", "The user says to skip the design: said once what it costs and that it asks almost nothing of them, offered again, nothing written.",
     [], None, SKIP,
     [says("says-what-skipping-costs", r"whoever builds|builder|in the build|one file at a time|home|no(body| one) decides|left to"), says("offers-the-stage-again", q.OFFERS),
      NOTHING_WRITTEN, *LEFT_ALONE], None),
    ("09b-the-user-insists", "The next turn: the user insists: recorded as skipped at their word, drawn by the command, nothing built and no later stage started.",
     [], None, "No. Skip it.",
     [in_file(D, "in-their-words-with-the-date", r"[Ss]kipped at the user's word[\s\S]*20\d\d-\d\d-\d\d|20\d\d-\d\d-\d\d[\s\S]*[Ss]kip"),
      DRAW, trace("the-command-drew-the-skip", r"skipped at the user's word: none of the \d+ things settled before has a home", never=False), NOT_BY_HAND, *LEFT_ALONE],
     [("user", SKIP), ("assistant", PUSHED_BACK)]),
    ("10-the-answers-changed-after",
     "The design was drawn, then the answers gained one: only it is given a home, the parts before are left as they were, drawn again.",
     [RECORD], lambda names: {names["design"]: PARTS, "draw": "before", "hold": "A971"}, q.GO_ON,
     [NEXT, block("C", "the-new-answer-has-its-home", r"\nHome of:[^\n]*\bA971\b"),
      in_file(D, "leaves-the-parts-before", r"## C3: Payment news\nSide: strategic\nDoes: Takes each change of a payment as it is told, applies it once"),
      in_file(D, "leaves-the-decisions-before", r"## D1: The renewal is recorded before its payment is asked for\nKind: chosen"),
      DRAW, NOTHING_WAITS, NOT_WHOLE, NOT_BY_HAND, *LEFT_ALONE, *q.ASKS_NOTHING], None),
    ("11a-the-owners-decision-is-brought-once",
     "The design is drawn and one decision of it waits for the owner: shown with its options, the one recommended and what happens if left, asked for "
     "once; nothing is decided for them and nothing written.",
     [], lambda names: {names["design"]: WITH_RISK, "draw": True}, q.GO_ON,
     [says("shows-the-decision", r"no renewal|money taken|payment (with|and) no"), says("with-what-is-recommended", r"recommend"),
      says("with-what-happens-if-left", r"if (it is |it's |this is )?left|left (undecided|open|as)|otherwise|until (you|then)"),
      not_in_file(D, "decides-nothing-for-them", r"\nDecided:"), NOTHING_WRITTEN, *LEFT_ALONE], None),
    ("11b-the-owner-decides",
     "The next turn: the owner decides against the recommendation: recorded on that decision in their words with the date, drawn again with none "
     "waiting; the next stage not started.",
     [], lambda names: {names["design"]: WITH_RISK, "draw": True}, "Give it back by itself after an hour. I don't want to look every morning.",
     [block("D", "records-it-in-their-words", r"\nKind:\s*owner", r"\nDecided:[^\n]*(hour|by itself|given back)[^\n]*\(the user, 20\d\d-\d\d-\d\d: \"[^\"\n]+\"\)"),
      DRAW, trace("the-command-drew-with-none-waiting", DREW + r"0 decisions wait for the owner; 0 go back", never=False), NOT_WHOLE, NOT_BY_HAND, *LEFT_ALONE],
     [("user", q.GO_ON), ("assistant", BROUGHT)]),
]
BARE_TABLE = q.BARE_TABLE.replace("The questions stage", "The design stage")


def before(drawn, *blocks):
    """Answers as an earlier session left them: the blocks, and every other question dismissed or, for the two a choice may not settle, a fact."""
    taken = set(o.settled_ids(blocks, drawn))
    groups = {}
    for name in answers.asked(drawn):
        if name not in taken:
            groups.setdefault(".".join(name.split(".")[:2]), []).append(name)
    out = ["# Answers: slice 1\n"]
    for number, (group, names) in enumerate(groups.items(), 1):
        said = ("Kind: fact\nSays: Settled in an earlier session.\nRests on: 002_requirements.md, the limits that apply.\n" if group in ("W.target", "W.obligations")
                else "Kind: not here\nSays: Settled in an earlier session: it does not arise in this slice.\n")
        out.append(f"## A{number}: {group}\n{said}Settles: {', '.join(names)}\n")
    return "\n".join(out) + "\n" + "\n".join(blocks)


def read_by_a_reader(folder):
    """The second reader's file as it would stand had it found every claim on its words: no case here is about it."""
    read = openfacts.load(folder)
    lines = ["# Read", "", openfacts.READ_STAMP % "claude-sonnet-5-5", "",
             "Kept by script from what a second reader said of each claim against the words it rests on. Never written by hand.", ""]
    lines += [f"- {each['name']} [{each['mark']}]: says" for each in openfacts.claims(read)]
    openfacts.read_file(read).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main(arm):
    if arm not in ("bare", "text"):
        raise SystemExit("arm: bare or text")
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-design-trial-{arm}", "version": "0.0.1",
         "description": "The test of the design only: startup and the earlier stages as adopted, and one arm's text."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n', executable=True)
    table = (ROOT / "steps/00-startup/eval/routing-table.md").read_text(encoding="utf-8")
    if arm != "text":
        last = table.rindex("- A stage with no text")
        assert "not built yet" in table[last:]
        table = table[:last] + BARE_TABLE
    write(plugin / "hooks" / "routing-table.md", table)
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for script in ("research/page.py", "questions/questions.py", "library/library.json", "answers/answers.py", "openfacts/openfacts.py", "openfacts/reader.md",
                   "designing/design.py"):
        write(plugin / script, (ROOT / script).read_text(encoding="utf-8"))
    for name, source in q.load("make_plugin", ROOT / "e2e/make_plugin.py").SKILLS.items():
        if name != "design":   # this stage's own text is one arm's, not every arm's
            write(plugin / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    used = []
    if arm == "text":
        write(plugin / "skills" / "design" / "SKILL.md", (HERE / "design-skill.md").read_text(encoding="utf-8"))
        used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    cleanup = startup._Cleanup()
    for name, description, more, after, prompt, graders, earlier in SCENARIOS:
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "ok\t0\t0")
        planning = machine.project / "planning"
        planning.mkdir()
        machine.run("stage.sh", "remember", "planning")
        slice_folder = planning / "slice-001"

        def lay(these, top=planning):
            for relative, text in these.items():
                path = top / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8", newline="\n")

        def draw(script=questions):
            said = io.StringIO()
            assert script.main(["draw", str(slice_folder)], said) == 0, (name, said.getvalue())

        lay(q.playhouse(**s.PAID))
        folder = re.search(r"next stage by the documents: questions \(its document: (\S+/)", machine.run("report.sh").stdout).group(1)
        inside = folder.split("planning/", 1)[1]
        lay({inside + "kept.md": q.kept_file()})
        draw()
        lay({inside + "security.md": s.EARLIER_SECURITY})
        draw()
        answers_file = re.search(r"next stage by the documents: answers \(its document: (\S+_answers\.md)\)", machine.run("report.sh").stdout).group(1)
        drawn = (planning / inside / "questions.md").read_text(encoding="utf-8")
        laid = after({"design": "slice-001/010_design.md"}) if after else {}
        hold, again, code = laid.pop("hold", None), laid.pop("draw", False), laid.pop("code", False)
        blocks = [*BASE, *more]
        first = [each for each in blocks if not (hold and each.startswith(f"## {hold}:"))]

        def draw_before():
            draw(answers)
            lay({"slice-001/009_open-facts.md": OPEN_FACTS})
            read_by_a_reader(slice_folder)
            draw(openfacts)

        lay({answers_file.split("planning/", 1)[1]: before(drawn, *first)})
        draw_before()
        found = re.search(r"next stage by the documents: design \(its document: (\S+_design\.md)\)", machine.run("report.sh").stdout)
        assert found, (name, machine.run("report.sh").stdout)
        document = found.group(1)
        assert document.endswith("slice-001/010_design.md"), document
        lay(laid)
        if again:
            draw(design)
        if hold:
            lay({answers_file.split("planning/", 1)[1]: before(drawn, *blocks)})
            draw_before()
        if code:
            lay(CODE, machine.project)
        done = machine.run("report.sh")
        waits = ("drawn; 1 decisions of the design wait" if name.startswith("11") else "to draw again" if hold
                 else "screens (" if name.startswith("04b") else "design (its document: planning/slice-001/010_design.md)")
        assert done.returncode == 0 and "next stage by the documents: " in done.stdout and waits in done.stdout, (name, done.stdout)
        assert "design.py\" next" in done.stdout or name.startswith("04b"), (name, done.stdout)
        report = done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@")
        assert str(ROOT) not in report, (name, report)
        machine.set("gh/summary", done.stdout.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        machine.set("web/allowed", "\n".join(["api.anthropic.com", q.research.HOST]))
        for page, body in q.research.pages().items():
            machine.set(f"web/pages/{q.research.HOST}/{page}", body)
        checks = json.loads(json.dumps(list(graders) + used).replace(D, document))
        case = plugin / "evals" / name
        write(case / "report.txt", report)
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, checks, earlier)
              .replace("name: problem-", "name: design-").replace("tags: [problem]", "tags: [design]")
              .replace("max_turns: 20", "max_turns: 80").replace("timeout_seconds: 400", "timeout_seconds: 1500"))
        write(case / "scaffold.sh", startup.scaffold(machine), executable=True)
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
