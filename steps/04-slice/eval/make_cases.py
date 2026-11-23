#!/usr/bin/env python3
"""Write the slice stage's scenarios as cases for the plugin evaluation.

Every scenario starts inside the project's VM with a problem document, a scope map and a
requirements list in the planning folder, startup's report and table and every adopted text. The
ten rows of the stage's test are fourteen cases, since four rows hold two situations each (4, 6,
9 and 10). The last six also have a set of slices, a slice's own document and what the tracker
answers of merged work and open issues.

An arm adds nothing for this stage (`bare`), kad's `vertical-slicing` and `acceptance-criteria`
as they stand (`kad`, the cutting cases only: kad had nothing for the coming-back) or this
repository's own text (`text`, from `slice-skill.md`). kad's skill is named in the prompt, as its
orchestrator named it. The bare arm's routing table says that this one stage is done from the
report alone, or it would rightly stop.

Checks named `form-...` are on what nothing tells the bare model or kad's skills to write (the
table and its columns, a criterion's name, the headings): the result is reported with and
without them.

Usage: python3 -I make_cases.py ARM      (rewrites plugin-ARM/ beside this file; not kept in git)
"""
import importlib.util
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


startup = load("startup_cases", ROOT / "steps/00-startup/eval/make_cases.py")
problem = load("problem_cases", ROOT / "steps/01-problem/eval/make_cases.py")
requirements = load("requirements_cases", ROOT / "steps/03-requirements/eval/make_cases.py")
says, never_says, write = startup.says, startup.never_says, startup.write


def section(heading, holds):
    """`holds` is under a heading that has `heading` in it, before the next heading. The heading's
    line end is left for `holds`, so a pattern that begins at a line's start finds the first line."""
    return rf"(?:^|\n)#{{1,6}}[^\n]*(?:{heading})[^\n]*(?=\n)(?:(?!\n#{{1,6}}\s)[\s\S])*?(?:{holds})"


KAD = {"vertical-slicing": [HERE / "kad-vertical-slicing.md", ROOT.parent / "kad-dev-team-plugin/skills/vertical-slicing/SKILL.md"],
       "acceptance-criteria": [HERE / "kad-acceptance-criteria.md", ROOT.parent / "kad-dev-team-plugin/skills/acceptance-criteria/SKILL.md"]}
LIST, SET = "planning/002_requirements.md", "planning/003_slices.md"
GO_ON = "Go on to the next stage."
NEXT = "what's next"


def in_file(path, name, pattern, flags="i"):
    return {"type": "regex", "name": name, "target": {"source": "file", "path": path}, "flags": flags, "pattern": pattern}


def not_in_file(path, name, pattern, flags="i"):
    return {**in_file(path, name, pattern, flags), "match": "not_contains"}


def near(one, other, within=300):
    return rf"(?:{one})[\s\S]{{0,{within}}}(?:{other})|(?:{other})[\s\S]{{0,{within}}}(?:{one})"


def all_of(*words):
    """Every one of `words` somewhere in the text, in any order."""
    return "^" + "".join(rf"(?=[\s\S]*(?:{word}))" for word in words)


def never_runs(name, pattern):
    return {"type": "tool_used", "name": name, "tool": "Bash", "input_match": pattern, "min": 0, "max": 0}


WROTE = requirements.WROTE


def untouched(name, file):
    """No Write or Edit of a file whose name holds `file`, and no shell command that writes to one."""
    return [{"type": "regex", "name": name, "target": "trace", "match": "not_contains", "pattern": WROTE + file},
            never_runs(name + "-by-shell", rf"(?:>>?|\btee\b|\bsed\s+-i|\bmv\b|\bcp\b|\brm\b|\bperl\s+-\S*i)[^|;&]{{0,200}}{file}")]


# A slice is a row of the set's table: its number, its name, its items, what it builds on, its state.
ROW = r"(?:^|\n)\|[ \t]*\d+[ \t]*\|[^\n]*"
STATE = r"\|[ \t]*\**(?:{})\**[^|\n]*\|[ \t]*(?=\n|$)"


def row(number, state=None, holds=None):
    """The row of slice `number`, with `holds` in it, ending in `state`."""
    out = rf"(?:^|\n)\|[ \t]*{number}[ \t]*\|"
    if holds:
        out += rf"(?=[^\n]*(?:{holds}))"
    return out + r"[^\n]*" + (STATE.format(state) if state else "")


def rows(times):
    # Counted by where each row starts: a pattern that also ran along the row could be matched in
    # so many ways that a document with too few rows took minutes to fail.
    return rf"(?:(?:^|\n)\|[ \t]*\d+[ \t]*\|[\s\S]*?){{{times}}}"


def the_set(path=SET, low=2, high=8, states=r"built|chosen"):
    """What every set must be, in the form this stage's text gives it."""
    return [in_file(path, "form-the-table", r"\|[ \t]*#[ \t]*\|[ \t]*Slice[ \t]*\|[ \t]*Items[ \t]*\|[ \t]*Builds on[ \t]*\|[ \t]*State[ \t]*\|"),
            in_file(path, f"form-at-least-{low}-slices", rows(low)),
            not_in_file(path, f"form-at-most-{high}-slices", rows(high + 1)),
            not_in_file(path, "form-no-slice-is-marked-yet", ROW + STATE.format(states)),
            in_file(path, "form-says-where-to-start", r"(?:^|\n)#{1,6}[^\n]*where to start")]


def every_item(path, names):
    return in_file(path, "every-item-is-in-the-set", all_of(*[rf"\b{name}\b" for name in names]))


# Words of how: a technology, a provider, a layout. None of the made-up lists uses one.
HOW = (problem.SOLUTION.replace("log ?ins?|sign[- ]in|", "").replace("notifications?|", "")
       + r"|\b(button|click(s|ed|ing)?|drop-?down|modal|checkbox|text ?box|sidebar|toolbar|icon|pop-?up|toast|"
         r"table (row|column)|JSON|SQL|server|endpoint|schema|spreadsheet)\b")
PROVIDERS = r"\b(gmail|sendgrid|mailgun|mailchimp|postmark|smtp|outlook|twilio|aws|amazon|google|microsoft|firebase)\b"
CRITERION = r"(?:^|\n)[ \t]*[-*] (?:\[[ xX]\] )?\*\*"
GIVEN = r"given[\s\S]{0,400}?\bwhen\b[\s\S]{0,400}?\bthen\b"
NO_CRITERIA_YET = [not_in_file(SET, "no-criteria-in-the-set", r"\bgiven\b[^\n]*\bwhen\b[^\n]*\bthen\b"),
                   *untouched("writes-no-slice-before-the-choice", r"_slice\.md")]
RECOMMENDS = says("recommends-a-start", r"recommend|suggest|I(?:'d| would) (?:start|begin|take|go)|start with|best (?:first|start|place)|my pick")
ASKS = says("asks-the-user", r"\?")
STOPS_THERE = {"type": "regex", "name": "writes-no-later-document", "target": "trace", "match": "not_contains",
               "pattern": WROTE + r"_(approach|research|questions|answers|open-facts|design|screens|stack|readiness)"}
MAP_UNTOUCHED = {"type": "regex", "name": "leaves-the-map-alone", "target": "trace", "match": "not_contains",
                 "pattern": WROTE + r"scope-map"}
TRACKER_UNTOUCHED = never_runs(
    "changes-nothing-on-the-tracker",
    r"gh\s+(?:issue|pr)\s+(?:close|edit|comment|create|reopen|delete|lock|pin|transfer|develop|merge|ready|review)|"
    r"gh\s+label|gh\s+api[^|;&]*(?:-X|--method)\s*(?:POST|PATCH|PUT|DELETE)|git\s+(?:merge|push)")
LIST_UNTOUCHED = untouched("leaves-the-list-alone", r"002_requirements")
ALWAYS = [STOPS_THERE, MAP_UNTOUCHED, TRACKER_UNTOUCHED, never_says("keeps-the-routing-table-out", r"\brouting table\b")]


def the_slice(path, names, least=2, most=10):
    """What a chosen slice's own document must be: criteria a person could check, nothing of how,
    nothing that is a later stage's, what is left out triaged."""
    item = "|".join(names)
    return [{"type": "file_exists", "name": "writes-the-slice", "path": path},
            in_file(path, "criteria-have-a-state-an-action-and-an-outcome", GIVEN),
            in_file(path, f"form-at-least-{least}-criteria-named-by-their-item",
                    section("criteria", rf"(?:{CRITERION}(?:{item}) ?/ ?\d+\*\*[\s\S]*?){{{least}}}")),
            not_in_file(path, "form-no-criterion-without-its-item", section("criteria", CRITERION + rf"(?!(?:{item}) ?/ ?\d+\*\*)")),
            not_in_file(path, f"at-most-{most}-criteria", rf"(?:\bgiven\b[\s\S]*?){{{most + 1}}}"),
            not_in_file(path, "nothing-of-how", HOW + "|" + PROVIDERS),
            # Who may do it, a doubled action and a failure of what the path depends on are later stages'.
            not_in_file(path, "none-of-the-later-stages-criteria", section(
                "criteria", r"\b(?:not (?:allowed|permitted|authori[sz]ed)|unauthori[sz]ed|permission|signed in|logged in|"
                            r"(?:taps?|press(?:es)?|submits?|sends?|saves?|records?) (?:it |this )?(?:twice|again|a second time)|"
                            r"double[- ](?:tap|click|submit)|time[sd]? out|is (?:down|unavailable|unreachable|offline)|"
                            r"(?:connection|network|signal) (?:is lost|drops|fails)|no (?:connection|signal|network)|"
                            r"fails? to (?:send|deliver|reach|respond)|cannot be (?:sent|delivered|reached)|bounces?)\b")),
            in_file(path, "form-what-is-left-is-triaged", section("left for later", r"usable without it|blocker")),
            in_file(path, "form-says-its-size", r"criteria:\s*\**\d+")]


# --- The weekly rota: a list of four items, one needing something outside (rows 1, 2, 5 and 6).
ROTA_NAMES = ["enter-the-week", "send-the-rota", "change-a-shift", "start-from-last-week"]
ROTA_LIST = """# Requirements: Send next week's rota to the staff

- [ ] **enter-the-week**: The manager can enter next week's shifts for every member of staff.
- [ ] **send-the-rota**: The manager can send each member of staff their own shifts for the week by email.
- [ ] **change-a-shift**: The manager can change a shift after the rota has been sent, and the member of staff whose shift changed is told.
- [ ] **start-from-last-week**: The manager can start a week from the week before instead of from nothing.

## Out for now
- Swapping shifts between staff, holidays and pay: not raised for this activity.

## Limits that apply
- The staff read email and nothing else: whatever a member of staff is sent or told reaches them by email.

## Not yet confirmed
Nothing.

## Outside systems and lasting things
- email, to the staff
- a week's rota
"""
ROTA_SET = """# Slices: Send next week's rota to the staff

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Enter one person's shifts for the week and email them to that person | enter-the-week, send-the-rota | nothing | open |
| 2 | Enter the whole week and email everyone their own shifts | enter-the-week, send-the-rota | 1 | open |
| 3 | Change a shift after the rota is sent, and tell that person | change-a-shift | 2 | open |
| 4 | Start a week from the week before | start-from-last-week | 2 | open |

## Where to start
Slice 1 can be started now. Slice 2 waits for 1; slices 3 and 4 wait for 2. Slice 1 is recommended: it is the smallest thing that puts a real email of shifts in front of one member of staff, and everything else builds on it.
"""
ROTA_SHOWN = ("I've cut the rota into four slices. 1: enter one person's shifts for the week and email them to that "
              "person. 2: enter the whole week and email everyone their own shifts. 3: change a shift after the rota "
              "is sent, and tell that person. 4: start a week from the week before. Slice 1 can be started now; 2 "
              "waits for 1, and 3 and 4 wait for 2. I recommend starting with slice 1: it is the smallest thing that "
              "puts a real email of shifts in front of one member of staff, and everything else builds on it. Where "
              "would you like to start?")
WIDER = "Just put all four in the first slice, I'd rather have the whole thing in one go. And we can build it on Google Sheets."
HELD = ("I'd keep slice 1 as it is, and here is what the wider cut costs. With all four in one slice nothing can be "
        "shown to a member of staff until entering, sending, changing and copying a week are all built, so a wrong "
        "guess about what the email should say is found last and not first. With the thin slice one person gets a "
        "real email of their shifts first, and the rest is built on what that shows. Which tool it is built on is "
        "decided at a later stage, so I've left that out. Shall I keep slice 1 as the start, or do you still want "
        "all four in one?")
INSISTS = ("I hear you, but I still want all four in one. The owner wants to see the whole thing working at the staff "
           "meeting on the 14th, not a piece of it.")
ERRORS_FIRST = ("Before any of these I want a slice that does all the error handling: every way it can go wrong, "
                "handled first. Then the rest.")
ROTA = {"000_problem.md": requirements.ROTA_PROBLEM, "001_scope-map.md": requirements.ROTA_MAP, "002_requirements.md": ROTA_LIST}
ROTA_ROW_OF_ALL = r"(?:^|\n)\|" + "".join(rf"(?=[^\n]*\b{name}\b)" for name in ROTA_NAMES) + r"[^\n]*"
NO_TECHNOLOGY = [not_in_file(SET, "the-floated-technology-is-in-no-line", r"google|sheets"),
                 {"type": "regex", "name": "writes-the-floated-technology-nowhere", "target": "trace", "match": "not_contains",
                  "pattern": r'"name"\s*:\s*"(?:Write|Edit)"[^\n]*Google'}]
COST = (r"(?:nothing|not[^.\n]{0,30}anything|no ?one|nobody)[^.\n]{0,80}(?:shown|see|use|learn|test|try)|"
        r"(?:shown?|see|learn|feedback|find out|found|discover|show)[^.\n]{0,100}(?:later|last|until|only (?:when|after|once)|at the end)|"
        r"until (?:all|every|the whole)|before (?:anything|anyone|you|we)[^.\n]{0,60}(?:learn|see|shown|use)|"
        r"\blonger\b|\brisk|\bcosts?\b|wrong[^.\n]{0,60}(?:late|later|last)|all (?:four|of it|at once)[^.\n]{0,80}(?:before|until)")

# --- The village hall: a list of one small item (row 3).
HALL_PROBLEM = """# Problem: Is the hall free?

## The problem
- The village hall is hired out for parties and classes. One volunteer keeps the bookings in her own diary.
- When she is away nobody on the committee can say whether a date is free, and an enquiry waits days for an answer.

## Why now
- She is away for six weeks from next month.

## Constraints
- None stated yet.

## Open questions
- None.
"""
HALL_MAP = """# Scope map: Is the hall free?

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | See whether the hall is free on a date | Anyone on the committee can answer an enquiry without the diary | now |
| 2 | Take a booking | A booking is recorded once, where everyone on the committee sees it | next |

## Holds for every activity
- None stated yet.

## Open
- None.
"""
HALL_LIST = """# Requirements: See whether the hall is free on a date

- [ ] **see-a-date**: A member of the committee can see whether the hall is free on a given date.

## Out for now
- Taking a booking: another row of the scope map. The bookings shown are those already in the diary.

## Limits that apply
None.

## Not yet confirmed
Nothing.

## Outside systems and lasting things
- a booking of the hall
"""

# --- The monthly race: an item leaning on an unanswered question, and one that compares records (row 4).
RACE_NAMES = ["register-a-runner", "record-a-finish", "publish-the-results"]
RACE_PROBLEM = """# Problem: Results of the monthly race

## The problem
- The club runs a five-kilometre race on the first Sunday of every month, with sixty to ninety runners.
- Runners sign a sheet on the day. Finish times are written on a clipboard as runners cross the line.
- Afterwards a volunteer works out whose time is whose from the two sheets. It takes an evening, and most months two or three runners are given someone else's time.
- Results go up on the clubhouse wall a week later.

## Why now
- The spring series starts in six weeks and counts towards the club championship.

## Constraints
- The volunteers at the finish have a phone each and no power or shelter.

## Open questions
- Whether results are shown with every runner's name, or each runner sees only their own.
"""
RACE_MAP = """# Scope map: Results of the monthly race

| # | What the user does | What it covers | When |
|---|---|---|---|
| 1 | Record the results of a race | Every runner is registered, timed and given their own result | now |
| 2 | Follow the championship table | A runner sees where they stand over the series | later |

## Holds for every activity
- The volunteers at the finish have a phone each and no power or shelter.

## Open
- Whether results are shown with every runner's name, or each runner sees only their own.
"""
RACE_LIST = """# Requirements: Record the results of a race

- [ ] **register-a-runner**: A volunteer can register a runner for the race on the day, and a runner who is already registered is not registered a second time.
- [ ] **record-a-finish**: A timekeeper can record each finish as a runner crosses the line.
- [ ] **publish-the-results**: The race secretary can publish the results of the race to the runners.

## Out for now
- The championship table: another row of the scope map.

## Limits that apply
- The volunteers at the finish have a phone each and no power or shelter: registering a runner and recording a finish must be doable on a phone, outdoors.

## Not yet confirmed
- Whether results are shown with every runner's name, or each runner sees only their own (covers, publish-the-results). It changes what publish-the-results shows, and to whom.

## Outside systems and lasting things
- a race
- a runner's registration for a race
- a finish
"""
RACE_SET = """# Slices: Record the results of a race

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Register a runner and see them on the start list | register-a-runner | nothing | open |
| 2 | Record a finish and see the finishes in order | record-a-finish | nothing | open |
| 3 | Publish the results to the runners | publish-the-results | 1, 2 | open |

## Where to start
Slices 1 and 2 can be started now. Slice 3 cannot be started until the question of who sees whose result is answered, and it waits for 1 and 2. Slice 1 is recommended: a start list is the first thing a volunteer can be shown, and a finish means nothing without a runner to give it to.
"""
RACE_SHOWN = ("I've cut the race into three slices. 1: register a runner and see them on the start list. 2: record a "
              "finish and see the finishes in order. 3: publish the results to the runners. Slices 1 and 2 can be "
              "started now. Slice 3 cannot be started until the open question is answered: are results shown with "
              "every runner's name, or does each runner see only their own? I recommend starting with slice 1. "
              "Where would you like to start?")
RACE = {"000_problem.md": RACE_PROBLEM, "001_scope-map.md": RACE_MAP, "002_requirements.md": RACE_LIST}
WAITS = r"until|cannot|can't|can ?not|\bwaits?\b|\bblocked\b|not yet confirmed|unanswered|once (?:it|that|the question) is|answer(?:ed)? first"
DUPLICATE = r"already registered|second time|\btwice\b|duplicate|same runner|registered before"
KEY = r"\bsame (?:[a-z]+ ){0,3}(?:name|number|date of birth|birthday|email|phone|address|club|bib)"

# --- The tool library: a set, a slice built and merged, issues (rows 7 to 10).
TOOLS_NAMES = ["record-a-loan", "record-a-return", "see-who-has-it", "list-overdue-tools"]
TOOLS_SET = """# Slices: Borrow and return a tool

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | Record a loan and see who has the tool | record-a-loan, see-who-has-it | nothing | %s |
| 2 | Record a return and see the tool as back | record-a-return, see-who-has-it | 1 | %s |
| 3 | See every tool that has not come back | list-overdue-tools | 1 | %s |

## Where to start
Slice 1 can be started now; slices 2 and 3 wait for it. Slice 1 is recommended: nothing else can be shown without a loan on record.
"""
TOOLS_ROWS = [r"\| 1 \| Record a loan and see who has the tool \| record-a-loan, see-who-has-it \| nothing \|",
              r"\| 2 \| Record a return and see the tool as back \| record-a-return, see-who-has-it \| 1 \|",
              r"\| 3 \| See every tool that has not come back \| list-overdue-tools \| 1 \|"]
SLICE = """# Slice %s

## Thin path
%s

## Criteria
%s

## Needs from outside
none

## Left for later
%s

## Size
Criteria: %d.
"""
CRITERIA = {
    1: ["record-a-loan / 1**: Given the drill is on the shelf and Ana Ruiz is a member, when a volunteer records that Ana Ruiz took the drill, then the drill is shown as out with Ana Ruiz.",
        "record-a-loan / 2**: Given the drill is out with Ana Ruiz, when a volunteer tries to record that Ben Okoro took the drill, then the loan is refused and the volunteer is told the drill is out with Ana Ruiz.",
        "see-who-has-it / 1**: Given the drill is out with Ana Ruiz, when a volunteer looks up the drill, then they are shown Ana Ruiz and the day she took it.",
        "see-who-has-it / 2**: Given the ladder is on the shelf, when a volunteer looks up the ladder, then they are shown that nobody has it."],
    2: ["record-a-return / 1**: Given the drill is out with Ana Ruiz, when a volunteer records that the drill came back, then the drill is shown as on the shelf.",
        "record-a-return / 2**: Given the ladder is on the shelf, when a volunteer tries to record that the ladder came back, then they are told the ladder is not out.",
        "see-who-has-it / 3**: Given the drill came back today, when a volunteer looks up the drill, then they are shown that nobody has it."],
    3: ["list-overdue-tools / 1**: Given the drill and the saw are out and the ladder is on the shelf, when a volunteer asks for the tools that have not come back, then they are shown the drill and the saw, each with the member who has it.",
        "list-overdue-tools / 2**: Given every tool is on the shelf, when a volunteer asks for the tools that have not come back, then they are told there are none."],
}
SLICES = {
    1: ("1: Record a loan and see who has the tool",
        "A volunteer at the desk records which member took which tool, and is shown that member against the tool.",
        "- Recording that a tool came back: slice 2. Usable without it: a tool that is out stays shown as out, and the paper ledger still records returns.\n"
        "- The list of every tool not back: slice 3. Usable without it: a volunteer can look up one tool at a time."),
    2: ("2: Record a return and see the tool as back",
        "A volunteer at the desk records that a tool came back, and is shown that nobody has it.",
        "- The list of every tool not back: slice 3. Usable without it: a volunteer can look up one tool at a time."),
    3: ("3: See every tool that has not come back",
        "A volunteer asks for the tools that have not come back and is shown each with the member who has it.",
        "Nothing."),
}


def slice_document(number):
    title, path, later = SLICES[number]
    return SLICE % (title, path, "\n".join("- **" + line for line in CRITERIA[number]), later, len(CRITERIA[number]))


def completes(number):
    return f"slice {number}: " + ", ".join(line.split("**")[0] for line in CRITERIA[number])


def tools(states, checked=(), slices=(1,)):
    """The tool library part-way through: the set with these states, these boxes checked, these slices written."""
    listed = requirements.TOOLS_LIST
    for name in checked:
        listed = listed.replace(f"- [ ] **{name}**", f"- [x] **{name}**")
    out = {"000_problem.md": requirements.TOOLS_PROBLEM, "001_scope-map.md": requirements.TOOLS_MAP,
           "002_requirements.md": listed, "003_slices.md": TOOLS_SET % states}
    for place, number in enumerate(slices):
        out[f"slice-{number:03d}/{4 + place:03d}_slice.md"] = slice_document(number)
    return out


def merged(number, slice_number, title):
    return "\t".join(["merged", str(number), completes(slice_number), title])


FIRST = merged(12, 1, "Record a loan and see who has the tool")
ISSUES = [("21", "bug", "After a loan is recorded, looking up the tool still says nobody has it",
           "Recorded the drill out to a member at the desk on Saturday. Looked the drill up straight after: it says nobody has it."),
          ("22", "-", "The list of tools not back should say how many days each has been out",
           "When we get the list of what has not come back, we will want to see how long each tool has been gone."),
          ("23", "-", "Members ask whether they could buy the library's old tools",
           "Three members have asked at the desk whether worn tools could be sold to them instead of thrown away.")]
BUILT_1 = [in_file(SET, "marks-the-merged-slice-built", TOOLS_ROWS[0] + r"\s*\**built"),
           in_file(LIST, "checks-the-box-merged-work-finished", r"- \[[xX]\] \*\*record-a-loan\*\*"),
           not_in_file(LIST, "checks-no-box-merged-work-did-not-finish",
                       r"- \[[xX]\] \*\*(?:record-a-return|see-who-has-it|list-overdue-tools)\*\*"),
           in_file(SET, "leaves-the-other-slices-as-they-are", TOOLS_ROWS[1] + r"\s*open[\s\S]*" + TOOLS_ROWS[2] + r"\s*open"),
           *untouched("writes-no-new-set", r"slices-v\d"), *untouched("writes-no-slice-before-the-choice", r"slice-00[23]/"),
           not_in_file(LIST, "adds-no-item", r"(?:(?:^|\n)[ \t]*[-*] \[[ xX]\][\s\S]*?){5}")]
MID_SLICE = ("We're part-way through building the return, and it has shown us two things. Recording a return and the "
             "list of tools not back are really one thing: a tool is on that list exactly until its return is "
             "recorded, so nobody could tell slices 2 and 3 apart. And see-who-has-it is wrong as written: the "
             "volunteers don't need who has a tool, they need the day it is due back.")
PROPOSED = ("You're right that they are one: a person could not be shown one without the other. Here is the set I "
            "propose. Slice 1, record a loan and see who has the tool, is built and stays as it is. Slice 2 becomes: "
            "record a return, and see every tool that has not come back (record-a-return, see-who-has-it, "
            "list-overdue-tools), building on 1; it is the slice in hand. Slice 3 is dropped: it is joined into 2, "
            "because a tool is on the list exactly until its return is recorded. The second thing is a change to the "
            "list, and that is the requirements stage's: see-who-has-it would say the day a tool is due back, not "
            "who has it. I have changed no item. Shall I write this as the new set?")
MID = tools(("built", "chosen", "open"), checked=["record-a-loan"], slices=(1, 2))
NEW_SET = "planning/006_slices-v002.md"

# (name, description, documents when the session started, documents added since, what the tracker answers,
#  the next stage the report names, prompt, checks, said before, folders there at the start, cutting or coming back)
SCENARIOS = [
    ("01-a-list-of-four-items", "A list of four items: the whole set, what each builds on, a start recommended, the choice asked; no criteria yet.",
     ROTA, {}, [], "slice (its document: planning/003_slices.md", GO_ON,
     [{"type": "file_exists", "name": "writes-the-set", "path": SET}, *the_set(), every_item(SET, ROTA_NAMES),
      in_file(SET, "form-says-what-each-builds-on", all_of(r"\|[ \t]*nothing[ \t]*\|[ \t]*open", r"\|[ \t]*\d+(?:[ \t]*(?:,|and)[ \t]*\d+)*[ \t]*\|[ \t]*open")),
      not_in_file(SET, "nothing-from-outside-the-list", r"\bswap|holiday"), not_in_file(SET, "nothing-of-how", HOW + "|" + PROVIDERS),
      *NO_CRITERIA_YET, RECOMMENDS, ASKS, *LIST_UNTOUCHED], None, [], True),
    ("02-the-user-chooses", "The second turn: the chosen slice written, its criteria pointing at items, the need from outside with no provider.",
     ROTA, {"003_slices.md": ROTA_SET}, [], "slice (its document: planning/003_slices.md", "Yes, start with slice 1.",
     [*the_slice("planning/slice-001/004_slice.md", ROTA_NAMES),
      in_file(SET, "form-marks-the-chosen-slice", row(1, "chosen")), not_in_file(SET, "form-marks-no-other-slice", row("[234]", "chosen|built")),
      in_file("planning/slice-001/004_slice.md", "says-what-it-needs-from-outside", section("needs? from outside|outside", r"e-?mail")),
      *untouched("writes-no-other-slice", r"slice-00[234]/"), *LIST_UNTOUCHED],
     [("user", GO_ON), ("assistant", ROTA_SHOWN)], ["slice-001"], True),
    ("03-a-list-of-one-small-item", "A list of one small item: one slice, and no set made up for it.",
     {"000_problem.md": HALL_PROBLEM, "001_scope-map.md": HALL_MAP, "002_requirements.md": HALL_LIST}, {}, [],
     "slice (its document: planning/003_slices.md", GO_ON,
     [{"type": "file_exists", "name": "writes-the-set", "path": SET}, every_item(SET, ["see-a-date"]),
      in_file(SET, "form-the-table", the_set()[0]["pattern"]), in_file(SET, "form-at-least-1-slice", rows(1)),
      not_in_file(SET, "one-slice-and-no-more", rows(2) + r"|(?:(?:^|\n)[ \t]*(?:#{2,6}[ \t]*slice|[-*]|\d+\.)[ \t]*\**(?:slice )?[2-9]\b)"),
      not_in_file(SET, "nothing-from-outside-the-list", r"take a booking|record a booking|make a booking"),
      not_in_file(SET, "nothing-of-how", HOW + "|" + PROVIDERS), *LIST_UNTOUCHED], None, ["slice-001"], True),
    ("04a-an-item-with-an-open-question", "An item leaning on an unanswered question: its slice cannot be started, and the set says so.",
     RACE, {}, [], "slice (its document: planning/003_slices.md", GO_ON,
     [{"type": "file_exists", "name": "writes-the-set", "path": SET}, *the_set(), every_item(SET, RACE_NAMES),
      in_file(SET, "says-the-slice-cannot-be-started", near(r"publish|results|slice [2-9]|\b[2-9]\b", WAITS, 250)),
      in_file(SET, "says-why-it-waits", near(WAITS, r"question|confirm|answer|decid|name|only their own", 300)),
      not_in_file(SET, "nothing-of-how", HOW + "|" + PROVIDERS), not_in_file(SET, "nothing-from-outside-the-list", r"championship"),
      *NO_CRITERIA_YET, RECOMMENDS, ASKS, *LIST_UNTOUCHED], None, [], True),
    ("04b-a-comparison-needs-its-key", "The second turn: a rule that compares records names what makes two the same, or is left for later, triaged.",
     RACE, {"003_slices.md": RACE_SET}, [], "slice (its document: planning/003_slices.md", "Start with slice 1.",
     [*the_slice("planning/slice-001/004_slice.md", RACE_NAMES, least=1),
      in_file(SET, "form-marks-the-chosen-slice", row(1, "chosen")),
      in_file("planning/slice-001/004_slice.md", "the-comparison-names-its-key-or-is-left-for-later",
              section("left for later|deferred|later", DUPLICATE) + "|" + section("criteria", KEY)),
      not_in_file("planning/slice-001/004_slice.md", "no-comparison-asserted-without-its-key",
                  section("criteria", rf"(?:^|\n)[ \t]*[-*] (?:(?!{KEY})[^\n])*(?:{DUPLICATE})(?:(?!{KEY})[^\n])*(?=\n|$)")),
      *untouched("writes-no-other-slice", r"slice-00[23]/"), *LIST_UNTOUCHED],
     [("user", GO_ON), ("assistant", RACE_SHOWN)], ["slice-001"], True),
    ("05-everything-in-the-first-and-a-technology", "The second turn: the user wants all of it in the first slice and floats a tool: pushed back once, with the cost.",
     ROTA, {"003_slices.md": ROTA_SET}, [], "slice (its document: planning/003_slices.md", WIDER,
     [says("says-what-the-wider-cut-costs", COST), says("offers-the-thin-cut-again", r"\?"),
      says("names-the-thin-cut", r"slice 1|thin|small|one person|first slice|as (?:it is|drawn|cut|proposed)"),
      *untouched("changes-no-set-before-the-answer", r"_slices"), *untouched("writes-no-slice-before-the-answer", r"_slice\.md"),
      *NO_TECHNOLOGY, *LIST_UNTOUCHED],
     [("user", GO_ON), ("assistant", ROTA_SHOWN)], [], True),
    ("06a-the-user-insists", "The third turn: the user still wants the wider cut: taken, its size said, their reason recorded.",
     ROTA, {"003_slices.md": ROTA_SET}, [], "slice (its document: planning/003_slices.md", INSISTS,
     [in_file(SET, "the-wider-cut-is-taken", ROTA_ROW_OF_ALL),
      in_file(SET, "records-the-users-reason", r"staff meeting|the 14th|whole thing"),
      in_file(SET, "form-records-it-under-what-changed", section("what changed", r"staff meeting|the 14th|whole thing|owner")),
      says("says-its-size", r"(?:\d+|four|five|six|seven|eight|nine|ten|eleven|twelve|\w+teen|twenty)\s+(?:criteria|items|behaviou?rs|requirements)|criteria:\s*\d+|\bsize\b"),
      never_says("does-not-argue-twice", r"are you sure|I(?:'d| would)? still (?:recommend|suggest|advise|urge)|strongly (?:recommend|advise|suggest)|reconsider|one more time"),
      *NO_TECHNOLOGY, *LIST_UNTOUCHED],
     [("user", GO_ON), ("assistant", ROTA_SHOWN), ("user", WIDER), ("assistant", HELD)], ["slice-001"], True),
    ("06b-error-handling-first", "The second turn: the user wants all the error handling first: spread over the slices, not all first.",
     ROTA, {"003_slices.md": ROTA_SET}, [], "slice (its document: planning/003_slices.md", ERRORS_FIRST,
     [says("spreads-the-errors-over-the-slices",
           r"(?:essential|basic|its own|their own|own rule)[\s\S]{0,400}(?:later|next|rare|common)|\btier|all[- ]or[- ]nothing|"
           r"(?:with|in|inside|as part of) (?:each|every|its|the) (?:own )?slice|slice by slice|each slice (?:carries|handles|brings|has|gets)|"
           r"spread (?:over|across)"),
      says("offers-it-again", r"\?"),
      not_in_file(SET, "no-slice-of-error-handling", r"(?:^|\n)\|[^\n]*error[- ]handling|(?:^|\n)\|[^\n]*\ball (?:the )?errors"),
      *untouched("writes-no-slice-before-the-choice", r"_slice\.md"), *LIST_UNTOUCHED],
     [("user", GO_ON), ("assistant", ROTA_SHOWN)], [], True),
    ("07-a-merge", "A merge names every criterion of one slice: checked off; the set holds and is not rewritten; the next slice recommended.",
     tools(("chosen", "open", "open")), {}, [FIRST], "slice, the coming-back", NEXT,
     [*BUILT_1, not_in_file(SET, "chooses-no-slice-for-the-user", ROW + STATE.format("chosen")),
      says("recommends-what-is-next", r"recommend|suggest|I(?:'d| would) (?:start|take|go)|next[^.\n]{0,80}(?:slice|return|not come back)|start (?:with|on)")],
     None, [], False),
    ("08-a-merge-and-three-issues", "A merge and three issues: each placed with its reason, two without asking; in or out asked for the one no row covers.",
     tools(("chosen", "open", "open")), {},
     [FIRST, *["\t".join(["issue", number, labels, title]) for number, labels, title, _ in ISSUES]], "slice, the coming-back", NEXT,
     [*BUILT_1, in_file(SET, "places-every-issue", all_of("#21", "#22", "#23")),
      in_file(SET, "places-the-first-in-the-slice-in-hand", r"#21[^\n]*(?:slice 1|in hand|record a loan|just built|built)"),
      in_file(SET, "places-the-second-in-a-later-slice", r"#22[^\n]*(?:slice 3|not come back|later slice)"),
      says("asks-in-or-out-for-the-third", near(r"#23|old tools|buy", r"\?", 400)),
      never_says("asks-nothing-of-the-first-two", r"#2[12][^.?!\n]*\?")],
     None, [], False),
    ("09a-work-shows-two-slices-are-one", "Mid-slice, the user says two slices are one and an item was wrong: a new set proposed, nothing written, the item left to the requirements.",
     MID, {}, [FIRST], "approach (its document: planning/slice-002/006_approach.md)", MID_SLICE,
     [says("proposes-the-two-as-one", r"\bjoin|\bmerg|combin|\bone slice|single slice|\bfold|become(?:s)? one|into (?:slice )?2|together"),
      says("leaves-the-built-slice", near(r"slice 1|built", r"stays?|unchanged|as it is|as they are|untouched|not touched|left|keeps?|remains?", 200)),
      says("names-the-requirements-stage-for-the-item", near(r"see-who-has-it|item|due back", r"requirements", 400)),
      says("asks-before-it-replaces-the-set", r"\?"),
      *untouched("writes-no-set-before-the-yes", r"_slices"), *LIST_UNTOUCHED],
     None, [], False),
    ("09b-the-user-agrees", "The second turn: the new set written as a new version, with what changed; the earlier set and the built slice as they were.",
     MID, {}, [FIRST], "approach (its document: planning/slice-002/006_approach.md)", "Yes, write it.",
     [{"type": "file_exists", "name": "writes-the-new-set-under-its-name", "path": NEW_SET},
      *untouched("leaves-the-earlier-set-as-it-was", r"003_slices\.md"),
      in_file(NEW_SET, "the-built-slice-is-as-it-was", TOOLS_ROWS[0] + r"\s*\**built"),
      in_file(NEW_SET, "the-two-are-one", r"(?:^|\n)\|(?=[^\n]*\brecord-a-return\b)(?=[^\n]*\blist-overdue-tools\b)[^\n]*"),
      in_file(NEW_SET, "form-says-what-changed", section("what changed", r"\bone\b|same|told apart|until|join|merg|combin")),
      *LIST_UNTOUCHED],
     [("user", MID_SLICE), ("assistant", PROPOSED)], [], False),
    ("10a-the-last-slice-merged", "The last slice is merged: checked off, the activity said to be done, the next \"now\" asked.",
     tools(("built", "built", "chosen"), checked=["record-a-loan", "record-a-return", "see-who-has-it"], slices=(1, 2, 3)), {},
     [FIRST, merged(15, 2, "Record a return"), merged(19, 3, "The tools not back")], "slice, the coming-back", NEXT,
     [in_file(SET, "marks-the-last-slice-built", TOOLS_ROWS[2] + r"\s*\**built"),
      not_in_file(LIST, "checks-every-box", r"- \[ \]"), not_in_file(LIST, "adds-no-item", BUILT_1[-1]["pattern"]),
      says("says-the-activity-is-done", r"\bdone\b|complete|finished|every (?:slice|box|requirement|item)|all (?:three|four|the) (?:slices|boxes|requirements|items)"),
      says("asks-which-row-is-the-next-now", near(r"\?", r"now|next|reserve|\brow\b|scope map|activity", 300)),
      *untouched("writes-no-new-set", r"slices-v\d")],
     None, [], False),
    ("10b-nothing-is-due", "Nothing merged since the last coming-back and no issue: no coming-back; the next stage named.",
     MID, {}, [FIRST], "approach (its document: planning/slice-002/006_approach.md)", NEXT,
     [says("names-the-next-stage", r"approach"),
      never_says("checks-nothing-off", r"(?:I(?:'ve| have)|now) (?:marked|checked|ticked)|checked off|marked[^.\n]{0,40}built"),
      {"type": "tool_used", "name": "writes-no-file", "tool": "Write", "min": 0, "max": 0},
      {"type": "tool_used", "name": "edits-no-file", "tool": "Edit", "min": 0, "max": 0}],
     None, [], False),
]
BARE_TABLE = ("- The slice stage has no text of its own here: do it from this report and the documents. A later stage "
              "with no text of its own here is not built yet. Say so and stop: do not do its work some other way, "
              "and do not offer to.\n")


def main(arm):
    if arm not in ("bare", "kad", "text"):
        raise SystemExit("arm: bare, kad or text")
    plugin = HERE / f"plugin-{arm}"
    shutil.rmtree(plugin, ignore_errors=True)
    write(plugin / ".claude-plugin" / "plugin.json", json.dumps(
        {"name": f"kd-slice-trial-{arm}", "version": "0.0.1",
         "description": "Stage 4's test only: startup and the earlier stages as adopted, and one arm's text."}, indent=2) + "\n")
    write(plugin / "hooks" / "hooks.json", json.dumps({"hooks": {"SessionStart": [{"hooks": [
        {"type": "command", "command": 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/report.sh"'}]}]}}, indent=2) + "\n")
    write(plugin / "hooks" / "report.sh", startup.HOOK + 'cat "${CLAUDE_PLUGIN_ROOT}/hooks/routing-table.md"\n', executable=True)
    table = (ROOT / "steps/00-startup/eval/routing-table.md").read_text(encoding="utf-8")
    if arm != "text":
        last = table.rindex("- A stage with no text")
        assert "not built yet" in table[last:]
        table = table[:last] + BARE_TABLE.replace("has no text of its own here: do it from this report and the documents",
                                                  "is done with the skill the user names" if arm == "kad" else
                                                  "has no text of its own here: do it from this report and the documents")
    write(plugin / "hooks" / "routing-table.md", table)
    (plugin / "startup").mkdir()
    for script in [*startup.STARTUP.glob("*.sh"), startup.STARTUP / "tracker.jq"]:
        shutil.copy(script, plugin / "startup" / script.name)
    for name, source in load("make_plugin", ROOT / "e2e/make_plugin.py").SKILLS.items():
        if name != "slice":
            write(plugin / "skills" / name / "SKILL.md", (ROOT / source).read_text(encoding="utf-8"))
    used = [{"type": "tool_used", "name": "uses-the-stage-text", "tool": "Skill", "min": 1}]
    if arm == "kad":
        for name, sources in KAD.items():
            write(plugin / "skills" / name / "SKILL.md", next(path for path in sources if path.exists()).read_text(encoding="utf-8"))
    elif arm == "text":
        write(plugin / "skills" / "slice" / "SKILL.md", (HERE / "slice-skill.md").read_text(encoding="utf-8"))
    else:
        used = []
    cleanup = startup._Cleanup()
    for name, description, before, added, tracker, expected, prompt, graders, earlier, folders, cutting in SCENARIOS:
        if arm == "kad":
            if not cutting:
                continue
            prompt += " Use the vertical-slicing skill."
        machine = startup.standin_machine.Machine(cleanup)
        machine.inside_vm()
        machine.repository(startup.REMOTE)
        machine.have("gh")
        machine.set("gh/lines", "\n".join([f"ok\t0\t{sum(line.startswith('issue') for line in tracker)}", *tracker]))
        for number, _, title, body in ISSUES:
            if any(line.startswith(f"issue\t{number}\t") for line in tracker):
                machine.set(f"gh/issue-{number}", f"title:\t{title}\nstate:\tOPEN\nnumber:\t{number}\n--\n{body}")
        (machine.project / "planning").mkdir()
        machine.run("stage.sh", "remember", "planning")

        def put(documents):
            for relative, text in documents.items():
                path = machine.project / "planning" / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
        put(before)
        done = machine.run("report.sh")   # what the session was given when it started
        assert done.returncode == 0 and "next stage by the documents: " + expected in done.stdout, (name, done.stdout)
        machine.set("gh/summary", done.stdout.split("\nTracker\n")[1].split("\nDocuments\n")[0])
        put(added)
        case = plugin / "evals" / name
        write(case / "report.txt", done.stdout.replace(str(startup.STARTUP), "@STARTUP@").replace(machine.data.as_posix(), "@DATA@"))
        # With nothing due, a session names a stage that is not built and never reaches this stage's text.
        used_here = [] if name.startswith("10b") else used
        write(case / "case.yaml", problem.case_yaml(name, description, prompt, graders + ALWAYS + used_here, earlier)
              .replace("name: problem-", "name: slice-").replace("tags: [problem]", "tags: [slice]")
              .replace("max_turns: 20", "max_turns: 30").replace("timeout_seconds: 400", "timeout_seconds: 600"))
        # A slice's folder is there when the run starts: in the evaluation a run's shell cannot make one.
        write(case / "scaffold.sh", startup.scaffold(machine) + "".join(f"mkdir -p planning/{folder}\n" for folder in folders),
              executable=True)
        if earlier:
            write(case / "history.jsonl", startup.history(earlier))
        for path in sorted(machine.state.rglob("*")):
            if path.is_file() and path.name != "calls.log":
                write(case / "state" / path.relative_to(machine.state), path.read_text(encoding="utf-8"))
        for path in sorted(machine.project.rglob("*")):
            if path.is_file() and ".git" not in path.relative_to(machine.project).parts:
                write(case / "project" / path.relative_to(machine.project), path.read_text(encoding="utf-8"))
        print(f"{name}: {len(graders + ALWAYS + used_here)} checks")
    cleanup.run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bare")
