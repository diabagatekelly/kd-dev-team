# Slice 1: The list keeper brings across the notebook's order and sees it kept

## Thin path
The list keeper brings the waiting list across from the notebook, and is shown it in just the order it has there.

## Criteria
The people below are invented.

- **bring-notebook-order-across / 1**: Given a notebook that lists Person C, then Person A, then Person B, none of them yet brought across, when the list keeper brings the list across, then the list keeper is shown those three and nobody else, with Person C first, Person A second and Person B third.
- **bring-notebook-order-across / 2**: Given that this list has been brought across and the list keeper has since left it, when the list keeper comes back to it, then it shows Person C first, Person A second and Person B third.

## Needs from outside
none

## Left for later
- A person waiting sees their own place in the order: slice 2. Usable without it: the list keeper can see the order that was brought across, and people can still phone to ask where they are.
- Changing the list after it is brought across: slice 3. Usable without it: the notebook can still be kept up to date as it is today.
- Putting right a place that is wrong, including one brought across wrongly: slice 3. Usable without it: the notebook still holds the order to check against.

## Size
Criteria: 2.
