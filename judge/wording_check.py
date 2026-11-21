#!/usr/bin/env python3
"""Refuse a frozen text that names a concept of one product's domain.

The next plugin must serve any product in any domain (the owner,
2026-11-20), so a prompt, a method or a brief that is frozen for a
validation step may not lean on the finance projects it is tested on.
This is a word list, not a judgment: it catches the obvious leak.

Usage: wording_check.py FILE [FILE ...]   (exit 1 if any term is found)
"""
import re
import sys

TERMS = (
    "plaid", "bank", "banks", "banking", "transaction", "transactions",
    "ledger", "ledgers", "merchant", "merchants", "currency", "currencies",
    "payment", "payments", "finance", "finances", "financial", "accounting",
    "keychain", "keychains", "endpoint", "endpoints", "api", "apis", "http",
    "https", "sqlite",
)
_PATTERN = re.compile(r"\b(" + "|".join(TERMS) + r")\b", re.IGNORECASE)


def find_terms(text):
    """Return (line number, term) for every listed term in the text."""
    hits = []
    for number, line in enumerate(text.splitlines(), start=1):
        for match in _PATTERN.finditer(line):
            hits.append((number, match.group(1).lower()))
    return hits


def main(paths):
    failed = False
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            for number, term in find_terms(handle.read()):
                print(f"{path}:{number}: {term}")
                failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
