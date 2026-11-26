# The library

`library.json`: 290 ways software commonly fails, by kind of action,
each with the question a plan must answer and the public page it
rests on. `library_check.py` checks and merges it; a kind holds 8 to
12 entries.

## Sources and their licences

Each entry names its source and quotes at most twenty words of it as
evidence. The questions and the descriptions of failures are this
project's own words.

The kinds `sign-in`, `stored-data`, `file-intake` and `misuse` (40
entries) rest on the OWASP Application Security Verification
Standard 5.0.0 (https://github.com/OWASP/ASVS), © The OWASP
Foundation, licensed under Creative Commons Attribution-ShareAlike
4.0 (https://creativecommons.org/licenses/by-sa/4.0/). Each of those
entries cites the requirement by its number; the quoted phrases are
the standard's and remain under that licence.
