# States

## The register

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `not-started` | not said in the documents | not said in the documents | none | not said in the documents |
| `in-use` | not said in the documents | Section leaders use it on the hall's computer. It keeps singers with their voice parts, and who came on a date. | none needed: it is the register's working state | 002_requirements.md, lines 9, 10 and 16 |
| `unavailable` | not said in the documents (the computer or the register cannot be used) | not said in the documents | none | not said in the documents |
| `ended` | not said in the documents | not said in the documents, including what is left | none | not said in the documents |

## A singer, with their voice part

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `in-register` | not said in the documents | A section leader can record a phoned absence for the singer. | none | 002_requirements.md, line 9; slice-001/004_slice.md, line 9 |
| `not-in-register` | not said in the documents | An attempt to record an absence is refused, and nothing is recorded. | none | slice-001/004_slice.md, line 10 |
| `left-choir` | not said in the documents | not said in the documents, including what happens to the singer's records | none | not said in the documents |

## A rehearsal

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `coming` | We rehearse every Thursday. How a particular date gets into the register, or whether it needs to, is not said. | A section leader can record that a singer will miss it. | not said in the documents | 000_problem.md, line 5; slice-001/004_slice.md, line 4 |
| `held` | not said in the documents | The register records who came on its date. | none | 002_requirements.md, line 10 |
| `not-held` | not said in the documents: whether any Thursday has no rehearsal is not confirmed | not said in the documents | none | 002_requirements.md, line 33 |

## A singer's absence from a rehearsal, told in advance

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `being-recorded` | A singer phones a section leader. What holds if recording is not finished is not said. | The section leader can record the absence. | recording it -> `recorded` | slice-001/004_slice.md, lines 4 and 9 |
| `recorded` | A section leader records it for the coming rehearsal. | The section leader is shown that it has been recorded. Seeing it by voice part is left for slice 2. | none | slice-001/004_slice.md, lines 9 and 16 |
| `withdrawn` | not said in the documents: whether a wrong notice, or one for a singer who can now come, is put right is not confirmed | not said in the documents | none | 002_requirements.md, line 28 |
| `rehearsal-past` | not said in the documents | not said in the documents, including whether the absence is kept and whether the singer coming after all changes it | none | not said in the documents |

## For the owner's list

- `not-started`: no way out. The documents do not say how a register begins, or what can be done before it does.
- `unavailable`: no way out. The documents do not say how absences are recorded meanwhile, or how the register comes back.
- `ended`: no way out. The documents do not say how the register is ended or what is left.
- `in-register`: no way out. The documents do not say how a singer is removed or their voice part changed, so the singer stays as recorded.
- `not-in-register`: no way out. No absence can be recorded for that name, and the documents for this activity do not say how a singer is added.
- `left-choir`: no way out. The documents do not say what happens to the singer or their records.
- `coming`: no way out stated. The documents do not say when a rehearsal stops being the coming one.
- `held`: no way out. The documents do not say how long its records are kept.
- `not-held`: no way out. The documents do not say what happens to absences recorded for that date.
- `recorded`: no way out. A wrong or outdated absence stays recorded, since no document gives a way to change or remove it.
- `withdrawn`: no way out. The documents do not say that an absence can be withdrawn or what would be left.
- `rehearsal-past`: no way out. The documents do not say what becomes of the absence after the rehearsal.
