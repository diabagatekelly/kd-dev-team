# Slice 1: A walker records a walk for one of their clients

## Thin path
A walker, on their phone, picks one of their clients and records a walk done today: 30 or 60 minutes, one dog. They are shown the walk kept, with the client, the day, the length and the dog, and they find it again among the walks they have recorded.

## Criteria
- **record-walk / 1**: Given a walker on their phone with a client in the product, when they record a 30-minute walk for that client with one dog, then they are shown the walk with that client, today's day, 30 minutes and that dog.
- **record-walk / 2**: Given the same walker and client, when they record a 60-minute walk with one dog, then they are shown the walk with 60 minutes, and it is a second walk beside the first, not a change to it.
- **record-walk / 3**: Given a walker recording a walk, when they give a length that is neither 30 nor 60 minutes (for example 45), then the walk is not kept and they are told the length must be 30 or 60 minutes.
- **record-walk / 4**: Given a walker who has recorded a walk, when they close the product and open it again later, then the walk is still among the walks they have recorded.

## Needs from outside
none

## Left for later
- A second dog from the same home on a walk: slice 2. Usable without it: the walker records walks with one dog.
- The owner seeing a client's walks: slice 3. Usable without it: each walker sees the walks they recorded themselves.
- Correcting or removing a walk recorded wrongly: slice 4. Usable without it: the walker can record walks; a wrong one stays until then.
- A regular client's walks without typing each again, and one-off extras recorded differently: slice 5. Usable without it: every walk, regular or extra, is recorded one by one.
- One outing covering dogs from different homes: slice 6. Usable without it: each home's walk is recorded on its own.
- Recording a walk for a day other than today: slice 7. Usable without it: a walk is recorded on the day it is done.
- The owner, or a holiday-cover walker, recording a walk: slice 8. Usable without it: the four walkers record their own walks.
- Where the list of about sixty clients comes from, and which walker may record for which client: no slice yet, it waits for question 1 of the requirements. Usable without it: a walker records walks for the clients that are in the product.
- Anything else a walk holds beyond the day, length and dog: no slice yet, it waits for question 3 of the requirements. Usable without it: the walk holds those three things.

## Size
Criteria: 4.
