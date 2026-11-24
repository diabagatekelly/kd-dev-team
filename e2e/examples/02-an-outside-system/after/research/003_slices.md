# Slices: Walkers record each walk they do

| # | Slice | Items | Builds on | State |
|---|---|---|---|---|
| 1 | A walker records a walk for one of their clients: the day, 30 or 60 minutes, one dog | record-walk | nothing | chosen |
| 2 | A walker adds a second dog from the same home to a walk | record-walk | 1 | open |
| 3 | The owner sees the walks recorded for a client | see-client-walks | 1 | open |
| 4 | A walker or the owner corrects or removes a walk recorded wrongly | record-walk | 1 | open |
| 5 | A walker records a regular client's walks without typing each one again | record-walk | 1 | open |
| 6 | A walker records one outing that covers dogs from different homes | record-walk | 1 | open |
| 7 | A walker records a walk days after it was done | record-walk | 1 | open |
| 8 | The owner, or a holiday-cover walker, records a walk | record-walk | 1 | open |
| 9 | The owner sees walks that were on paper before the product | see-client-walks | 3 | open |

## Where to start
- **Can be started now:** slices 1, 2 and 3. Slice 1 is the ordinary path of the item: the walker picks one of their clients and records a walk that is kept. It leans on no open question; the walkers-and-clients list it needs is sized to the few clients the slice needs to be shown.
- **Wait for an answer** (each is a part of an item that leans on a question under "Not yet confirmed" in the requirements):
  - slice 4: question 5 (who corrects, and until when);
  - slice 5: question 2 (regular walks already there to confirm, or recorded each time);
  - slice 6: question 4 (dogs of different homes in one outing);
  - slice 7: question 7 (recording on the day or later);
  - slice 8: question 6 (the owner recording, and holiday-cover walkers);
  - slice 9: question 8 (paper walks coming across).
- **Open and may change slices 1 to 3:** question 1 (whose clients, and where the list of clients starts from) and question 3 (anything else a walk holds). Neither stops them; if an answer adds something, it comes back through the requirements first.
- **Recommended first: slice 1.** It shows a walker the one thing they do every day, kept safely, and every other slice builds on it. Slices 2 and 3 follow, and 3 is what lets the owner stop guessing.
