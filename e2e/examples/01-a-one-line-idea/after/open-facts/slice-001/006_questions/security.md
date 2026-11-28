# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | bring-notebook-order-across / 1: the list keeper is shown the list; the documents do not say it is not in a web browser |
| network | yes | bring-notebook-order-across / 2: the list keeper comes back to the list; the documents do not say it answers no requests at a network address |
| calls-out | no | slice-001/004_slice.md, "Needs from outside": none |
| dependency | yes | bring-notebook-order-across / 1: the documents do not say it uses no component someone else wrote |
| several-people | yes | 002_requirements.md, bring-notebook-order-across and see-where-they-stand: the list keeper keeps a list of other people, who are to see their own place |
| unguessable | yes | bring-notebook-order-across / 2: the list keeper comes back to the list; the documents do not say no link, code or session is made for that |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| `waiting-people` | `shown-list` | Someone other than the list keeper reads the names of the people waiting and the order they are in. | yes |
| `waiting-people` | `bringing-across` | Someone who can read what passes while the list is brought across learns who is waiting and in what order. | yes |
| `waiting-people` | `way-back-in` | Someone gets in as the list keeper and reads the name and place of everyone waiting. | yes |
| `waiting-list` | `bringing-across` | Someone who wants a plot sooner gets a changed order brought across, in their own way or in the list keeper's name, and a person who has waited longer is put behind. | yes |
| `waiting-list` | `way-back-in` | Someone takes over the way in and shuts the list keeper out, who can no longer see the list they brought across. | yes |
| `waiting-list` | `shown-list` | A person waiting gives a name written to be acted on rather than read, and when it is shown to the list keeper the list they see or the list kept is changed. | yes |
