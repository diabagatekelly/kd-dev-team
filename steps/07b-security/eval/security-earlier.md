# Security: slice 1

## Facts about the slice
| Fact | Holds | Source |
|---|---|---|
| browser | yes | renew-and-pay / 1: the subscriber is shown; payright.md F7: a card form in her browser |
| network | yes | payright.md F5: PayRight sends events to our address |
| calls-out | yes | 005_approach.md: PayRight is committed to |
| dependency | yes | payright.md F7: PayRight's card form runs in the page |
| several-people | yes | refund-a-renewal / 1: the office acts on a subscriber's renewal |
| unguessable | yes | payright.md F6: a reference is sent with each payment request |

## What someone who means harm would want
| Wanted | Through | Worst from there | Asked |
|---|---|---|---|
| credentials | `payment-request` | someone holding the secret key takes payments or gives refunds as the playhouse | yes |
| credentials | `refund-request` | someone who can send it gives back money that was never asked for | yes |
| `card-token` | `renewal-request` | a token read on its way is used once, within its 15 minutes, to pay for someone else's renewal | yes |
| her-details | `refund-screen` | someone who is not the office sees whose renewals were paid, and refunds them | yes |
| her-details | `renewal-screen` | another subscriber is shown her renewal and its payment by naming her ticket | yes |
| her-details | `card-refused-screen` | nothing more than the renewal screen shows | no: it shows only that her own card was refused |
| her-details | `webhook-address` | anyone who knows the address sends a made-up event and a renewal is shown as paid | yes |
| her-details | `payment-updated-event` | a true event sent again later puts a refunded renewal back to paid | yes |
| credentials | `payment-reply` | nothing: the reply holds an id, a status and a time | no: it carries no credential |
| credentials | `payment-reference` | a reference that can be guessed lets someone make a payment request pass for a repeat | yes |
