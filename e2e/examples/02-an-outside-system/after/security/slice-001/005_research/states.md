# States

## Walk

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `being-entered` | not said in the documents | not said in the documents | none | not said in the documents |
| `entered` | A walker enters it with a client, day and length | The walker sees it among their walks; the business owner can correct it | The business owner corrects it -> `corrected`; it goes on the client's invoice -> `invoiced` | slice-001/004_slice.md line 7; 002_requirements.md lines 4 and 6 |
| `corrected` | The business owner corrects a walk a walker entered | Whether it can be corrected again is not said in the documents | It goes on the client's invoice -> `invoiced` | 002_requirements.md lines 4 and 6 |
| `invoiced` | The business owner gets the client an invoice for the month's walks | Whether the walk can still be changed is not said in the documents | none | 002_requirements.md line 6 |
| `changed-by-walker` | not said in the documents | not said in the documents | none | not said in the documents (002_requirements.md line 22 asks) |
| `closed-to-changes` | not said in the documents | not said in the documents | none | not said in the documents (002_requirements.md line 22 asks) |
| `removed` | not said in the documents | not said in the documents | none | not said in the documents |

## Client

| State | Entered by | What the person can do | Way out | Source |
|---|---|---|---|---|
| `being-added` | not said in the documents | not said in the documents | none | not said in the documents (002_requirements.md line 27 asks what must come across) |
| `current` | not said in the documents | A walker can enter a walk for the client | none | slice-001/004_slice.md line 7; 000_problem.md line 4 |
| `details-changed` | not said in the documents | not said in the documents | none | not said in the documents |
| `no-longer-a-client` | not said in the documents | not said in the documents | none | not said in the documents |

## For the owner's list
- Walk `being-entered`: no way out. The documents do not say what a walker has between entering a walk and seeing it among their walks.
- Walk `invoiced`: no way out. The documents do not say what can happen to a walk once it is on an invoice.
- Walk `changed-by-walker`: no way out. The documents do not say whether a walker can change an entry, or what follows.
- Walk `closed-to-changes`: no way out. The documents do not say whether or when a month's walks close.
- Walk `removed`: no way out. The documents do not say whether a walk can be removed, for example one entered by mistake.
- Client `being-added`: no way out. The documents do not say how a client gets into the product.
- Client `current`: no way out. The documents do not say how a client stops being current.
- Client `details-changed`: no way out. The documents do not say who changes a client's details or what follows.
- Client `no-longer-a-client`: no way out. The documents do not say what happens to the client or their walks.
