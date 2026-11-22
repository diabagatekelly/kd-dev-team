# Choir register

Who came to which rehearsal. Used on the hall's computer by the section leaders.

    python3 register.py add "Ada Lovell" alto
    python3 register.py tick 2026-03-05 "Ada Lovell"
    python3 register.py report 2026-03-05

Singers and attendance are kept in `data/register.json`. There are no accounts: whoever is at
the hall's computer can use it.
