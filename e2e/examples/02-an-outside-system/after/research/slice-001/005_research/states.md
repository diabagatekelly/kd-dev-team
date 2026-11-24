# States

Slice 1 needs nothing from outside and the approach committed to nothing, so no documentation was read and no other research document is written. The three lasting things below are kept by the product itself, so each row comes from the planning documents alone.

## A walk

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `recorded` | A walker records it with the day, 30 or 60 minutes and one dog | The walker finds it among the walks they have recorded | Corrected -> `corrected`; removed -> `removed`; added to an invoice -> `invoiced` | "then the walk is still among the walks they have recorded" (slice-001/004_slice.md, record-walk / 4); who corrects or removes, and until when, is not said in the documents (002_requirements.md, question 5) |
| `corrected` | Someone corrects a wrongly recorded walk | not said in the documents | not said in the documents | "who can correct or remove it, and until when" (002_requirements.md, question 5) |
| `removed` | Someone removes a wrongly recorded walk | not said in the documents | none | "who can correct or remove it, and until when" (002_requirements.md, question 5) |
| `invoiced` | The month's walks are turned into an invoice for the client | not said in the documents | none | "I turn a month's walks into an invoice for each client and send the payment link" (001_scope-map.md, row 2); what happens to the walk afterwards is not said in the documents |

## A client

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `in-product` | not said in the documents (who puts the client there is open) | The walker picks the client to record a walk | The client stops -> `stopped` | "Given a walker on their phone with a client in the product" (slice-001/004_slice.md, record-walk / 1); "Who tells the product which walker has which client" (002_requirements.md, question 1) |
| `stopped` | The client stops | not said in the documents | none | "A regular client has the same walks every week until they change or stop" (002_requirements.md, question 2); who records the stopping is not said in the documents |

## A walker

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `active` | not said in the documents | Records walks for their clients | A walker stops walking -> `gone` | "A walker: four now, more with holiday cover." (002_requirements.md); how a walker joins is not said in the documents |
| `gone` | A walker stops walking | not said in the documents | none | not said in the documents |

## For the owner's list
- `removed`: no way out. The walk is no longer among the recorded walks; whether it can be brought back is not said.
- `invoiced`: no way out. The walk is part of an invoice; the documents name no way to put right a walk after that.
- `stopped`: no way out. The client no longer has walks; what happens to the walks already recorded is not said.
- `gone`: no way out. What happens to the walker's recorded walks is not said.
