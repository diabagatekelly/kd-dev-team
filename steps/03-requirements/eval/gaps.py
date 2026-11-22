#!/usr/bin/env python3
"""Count which known gaps a run's requirements list raises as a question.

A gap is something the scenario's documents leave unsaid that would add, remove or change an
item. The first of each scenario's gaps were raised by runs of the free-form text; the ones
marked WALKED were found by walking the eight kinds by hand before any run of the other arms,
so that the measure does not only reward what the free-form text already finds.

Usage: python3 -I gaps.py RESULTS NAME...   (RESULTS holds traces/NAME-requirements-*.jsonl)
"""
import collections
import glob
import json
import os
import re
import sys

GAPS = {
    "01": {"who-is-a-member": r"\bmembers?\b[^\n]*(count|list|not yet|before join|join)|who (counts|is) (as )?a member|non-members?",
           "when-is-it-late": r"\bdue\b|overdue|\blate\b|how long|by when|return date",
           "which-tool-or-several": r"several|more than one|told apart|identif|same kind|one by one",
           "the-ledger-comes-across": r"ledger|already (out|on loan|borrowed)|existing loans|brought (in|across)",
           "a-mistake-put-right": r"mistake|correct|\bwrong\b|undo|put right",
           "who-may-record (WALKED)": r"(any|which|every|only) (of the )?volunteers?|who (may|can|is allowed)",
           "a-tool-back-broken (WALKED)": r"broken|damaged|condition"},
    "02": {"whole-rota-or-own-shifts": r"whole|own shifts|only their|everyone'?s shifts",
           "where-the-shifts-come-from": r"wall chart|come from|enters?\b|keeps? (planning|the chart)",
           "a-change-after-sending": r"after (it|the rota|sending)[^\n]*(sent|chang|correct|fix)|(chang|correct|fix)[^\n]*after|sent[^\n]*(chang|correct|fix)",
           "by-when-it-goes": r"sunday|by when|what day|what time|set time|how far ahead",
           "who-sends-if-not-the-manager (WALKED)": r"away|someone else|deput|only the manager|anyone other than|other than the manager",
           "who-counts-as-staff (WALKED)": r"who counts|new staff|new starters?|leav(es|ers?)|every(one| person) on"},
    "03": {"what-in-time-means": r"in time|by when|what date|how (long|many days) before",
           "who-places-a-child-in-a-team": r"team[^\n]*(choos|assign|plac|decid|pick|put)|(choos|assign|plac|pick|put)[^\n]*team",
           "the-secretary-sees": r"secretary",
           "a-registration-put-right": r"correct|withdraw|mistake|amend|chang\w* (a|the|their|an?y?) ?(child's )?(registration|details|entry)",
           "more-than-one-child-or-adult": r"more than one|several|guardian|siblings?|two children",
           "until-when-one-may-register (WALKED)": r"clos|deadline|until when|after the season (has )?start|late regist|cut-?off",
           "last-seasons-children (WALKED)": r"last season|each season|every season|carry over|returning|register(ed)? again"},
    "05": {"who-renews": r"office[^\n]*(renew|behalf)|who (does the )?renew|subscribers? (themselves|alone)|(renew)[^\n]*(office|behalf)",
           "what-lapsed-means": r"laps\w*[^\n]*(mean|when|date|count|exactly)|grace|(when|what date)[^\n]*laps",
           "renewing-after-a-lapse": r"already lapsed|after (it|the ticket|a ticket) (has )?laps|once (it has |it is )?lapsed|lapsed[^\n]*(still|renew)",
           "the-same-seats": r"\bseats?\b",
           "several-tickets-one-subscriber (WALKED)": r"more than one|several|household|family|two (season )?tickets|on behalf of (another|someone)",
           "a-renewal-taken-back (WALKED)": r"refund|cancel|undo|mistake|paid twice|wrong"},
}
SECTION = re.compile(r"(?:^|\n)#{1,6}[^\n]*not yet confirmed[^\n]*\n([\s\S]*?)(?=\n#{1,6} |\Z)", re.I)


def questions(document):
    """The text under "Not yet confirmed", or nothing."""
    found = SECTION.search(document or "")
    return found.group(1) if found else ""


def raised(scenario, document):
    """The names of the scenario's gaps that the document's questions raise."""
    text = questions(document)
    return [name for name, pattern in GAPS.get(scenario, {}).items() if re.search(pattern, text, re.I)]


def count(text):
    return len(re.findall(r"(?m)^\s*[-*] ", text))


def final_document(trace):
    document = None
    for line in open(trace, encoding="utf-8"):
        try:
            message = json.loads(line).get("message") or {}
        except ValueError:
            continue
        if message.get("role") != "assistant" or not isinstance(message.get("content"), list):
            continue
        for part in message["content"]:
            if part.get("type") == "tool_use" and "requirements" in str(part["input"].get("file_path", "")):
                given = part["input"]
                if part["name"] == "Write":
                    document = given.get("content")
                elif part["name"] == "Edit" and document is not None:
                    document = document.replace(given.get("old_string", ""), given.get("new_string", ""),
                                                -1 if given.get("replace_all") else 1)
    return document


def main(results, names):
    for name in names:
        hits, runs, asked, words = collections.Counter(), collections.Counter(), [], []
        for trace in sorted(glob.glob(f"{results}/traces/{name}-requirements-*.jsonl")):
            scenario = os.path.basename(trace)[len(name) + 14:][:2]
            if scenario not in GAPS:
                continue
            document = final_document(trace)
            runs[scenario] += 1
            asked.append(count(questions(document)))
            words.append(len((document or "").split()))
            for gap in raised(scenario, document):
                hits[scenario, gap] += 1
        total = sum(runs[s] * len(GAPS[s]) for s in runs)
        reliable = sum(1 for (s, _), n in hits.items() if n >= 0.8 * runs[s])
        print(f"{name}: {sum(hits.values())} of {total} raised ({100 * sum(hits.values()) // max(total, 1)}%), "
              f"{reliable} of {sum(len(GAPS[s]) for s in runs)} gaps in at least 8 runs of 10; "
              f"questions a list {min(asked or [0])} to {max(asked or [0])}, mean {sum(asked) / max(len(asked), 1):.1f}; "
              f"words {min(words or [0])} to {max(words or [0])}")
        for scenario in sorted(runs):
            print("  ", scenario, ", ".join(f"{gap} {hits[scenario, gap]}/{runs[scenario]}" for gap in GAPS[scenario]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
