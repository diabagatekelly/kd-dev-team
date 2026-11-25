# Kept: slice 1

## What the slice creates and keeps
- A renewal payment: renew-and-pay / 1
- The season ticket: renew-and-pay / 1

## What the slice takes in
| Value | Kind | From | Sensitive | Source |
|---|---|---|---|---|
| `season-ticket-id` | identifier | the subscriber, naming the ticket to renew | her-details | renew-and-pay / 1 |
| `card-token` | identifier | PayRight's card form in the subscriber's browser | credentials | payright.md F7 |
| `payment-id` | identifier | PayRight's reply to a payment request | no | payright.md F2 |
| `payment-status` | choice | PayRight's reply and its payment.updated event | no | payright.md F2 |
| `created-at` | date | PayRight's reply | no | payright.md F2 |
| `payment-error-code` | choice | PayRight, when the card is refused or too many requests were sent | no | payright.md F8 |
| `retry-after` | number | PayRight's Retry-After header | no | payright.md F9 |
| `refund-amount` | number | the office, asking for a refund | no | payright.md F10 |
| `renewal-to-refund` | identifier | the office, naming the renewal to give back | her-details | refund-a-renewal / 1 |
| `refund-error-code` | choice | PayRight, when a refund is refused | no | payright.md S2 |
| `secret-key` | other | the playhouse's PayRight account, set where the product runs | credentials | payright.md F11 |
| `stored-payment-state` | choice | read back from where the renewal payment is kept | no | refund-a-renewal / 1 |
| `stored-ticket-state` | choice | read back from where the season ticket is kept | no | renew-and-pay / 1 |

## Other things the slice has
- `renewal-request`: the subscriber's request to renew and pay (renew-and-pay / 1)
- `payment-request`: our request to PayRight to take a payment (payright.md F1)
- `payment-reference`: the reference sent with each payment request (payright.md F6)
- `payment-reply`: PayRight's reply holding id, status and created_at (payright.md F2)
- `payment-updated-event`: the payment.updated event PayRight sends us (payright.md F5)
- `webhook-address`: our address that receives those events (payright.md F5)
- `refund-request`: our request to PayRight to give a payment back (payright.md F10)
- `renewal-screen`: what shows the subscriber the renewal is recorded and the payment being taken (renew-and-pay / 1)
- `card-refused-screen`: what tells the subscriber the card was refused and lets them pay with another (renew-and-pay / 2)
- `refund-screen`: what the office uses to refund, and what shows the subscriber as refunded (refund-a-renewal / 1)

## Library
| Entry | Applies to | Why |
|---|---|---|
| call-external-01 | `payment-request` | a payment request can get no reply (payright.md O1), so it may or may not have taken effect |
| call-external-02 | `payment-reference` | PayRight returns the first payment for a repeated reference within 24 hours (F6); a repeat must be recognised as one |
| call-external-03 | payright | every renewal waits on PayRight, and no wait limit is written down |
| call-external-04 | payright | a payment may take 3 working days to settle (F4) while the request itself is quick; the limit must not mistake one for the other |
| call-external-05 | `payment-request` | a payment request that failed may be sent again, and a second payment must not be taken |
| call-external-06 | `payment-error-code` | card_declined is final and rate_limited is worth another try (F8, F9) |
| call-external-07 | payright | all card payments stay with PayRight, so its outage stops every renewal |
| call-external-08 | renew-and-pay-1 | the subscriber waits for the payment request and sees "being taken" |
| call-external-09 | renew-and-pay-2 | the renewal is recorded before the payment is known; a refused card leaves that step behind |
| call-external-10 | `refund-request` | a refund is allowed only within 90 days of settling (F10), and a payment may have become disputed |
| call-external-11 | payright | the slice cannot take or give back money without PayRight |
| call-external-12 | renew-and-pay-1 | what the subscriber is told when PayRight cannot be reached |
| receive-external-data-01 | `payment-reply`; `payment-updated-event` | values from PayRight are stored and shown (F2, F5) |
| receive-external-data-02 | `payment-updated-event` | an event may be sent again and must change nothing the second time |
| receive-external-data-03 | `payment-updated-event` | two events for one payment may arrive out of order (O2) |
| receive-external-data-04 | renewal-payment | a payment's change is told only by event (F5); one missed leaves it pending |
| receive-external-data-05 | `webhook-address` | anyone could send an event to our address |
| receive-external-data-06 | `payment-updated-event` | whether to confirm receipt before or after recording the change |
| receive-external-data-07 | `payment-status` | the states list pending, settled, declined, refunded, disputed, lost; PayRight may send another |
| receive-external-data-08 | payright | the reply holds three fields today (F2) and could change |
| receive-external-data-09 | `retry-after` | a number from PayRight that is waited on |
| receive-external-data-10 | payright | replies and events are read from PayRight |
| receive-external-data-11 | `payment-reply` | the reply holds three named fields and a cut-off reply may hold some |
| receive-external-data-12 | `payment-reply` | the reply does not say whether the card was accepted (F3), against what our problem document expects (S1) |
| sync-01 | renewal-payment | our record and PayRight's can differ on one payment, for example refunded here and disputed there |
| sync-02 | `payment-updated-event` | an event set aside as old or repeated is a change dropped |
| sync-03 | renew-and-pay-1 | the subscriber was told "being taken" and the payment may later be declined |
| sync-04 | renewal-payment | the state shown is as old as the last event received |
| sync-10 | renew-and-pay-1 | the payment moves from pending to settled or declined while the subscriber looks at it |
| sync-05, sync-06, sync-07, sync-08, sync-09, sync-11, sync-12 | dropped | the slice does no update pass and keeps no local copy it refreshes from a source: a payment's state arrives as single events (payright.md F5) |
| limits-01 | payright | PayRight allows 100 requests a minute (F9) |
| limits-02 | `retry-after` | PayRight says how long to wait (F9) |
| limits-03 | `renewal-request` | one subscriber could press pay again and again |
| limits-04 | `renewal-request` | renewals open in eight weeks (000_problem.md), and many may come at once |
| limits-05 | payright | when PayRight's request limit is near, renewing and refunding compete |
| limits-06 | `payment-error-code` | the subscriber or office is told when rate_limited stops them |
| limits-09 | payright | PayRight charges 1.4% of each payment (000_problem.md, S3) |
| limits-11 | `payment-request` | requests waiting on PayRight's limit or an outage |
| limits-12 | renew-and-pay-1 | a subscriber may leave while the payment is being taken |
| limits-07, limits-08, limits-10 | dropped | the slice takes no file or large item, shows no list (slice 2) and runs no scheduled work |
| durable-write-01 | renewal-payment | a save of a renewal payment can be cut off |
| durable-write-02 | renew-and-pay-1 | the subscriber is told the renewal is recorded |
| durable-write-03 | renewal-payment | a recorded renewal must survive a power loss |
| durable-write-04 | renewal-payment | a save can fail for lack of space while a payment is being taken |
| durable-write-05 | renewal-payment | a failed save after money was taken |
| durable-write-06 | season-ticket | the ticket's state is replaced on renewal |
| durable-write-07 | `payment-updated-event` | each payment's changes may be kept as a history that grows |
| durable-write-08 | renewal-payment | the payment's state and the ticket's state must agree |
| durable-write-09 | renewal-payment | a stored payment state that silently changed would show a wrong refund |
| durable-write-10 | renewal-payment | copies of the stored payments taken while a payment is being recorded |
| durable-write-11 | season-ticket | which stored data holds ticket and payment together |
| durable-write-12 | renew-and-pay-1 | the product closed while a renewal is being recorded |
| startup-read-01 | renewal-payment | the product reads stored payments at start |
| startup-read-02 | season-ticket | the slice adds stored tickets in a place the product reads at start |
| startup-read-03 | renewal-payment | first run against stored data that cannot be opened |
| startup-read-04 | renewal-payment | a renewal recorded and its payment not yet taken, when the product stopped |
| startup-read-05 | season-ticket | stored tickets that can be read but not changed |
| startup-read-06 | renewal-payment | the documents do not say one copy only runs |
| startup-read-07 | season-ticket | the documents do not say where stored tickets live |
| startup-read-08 | renewal-payment | after a rescue, payment states may be missing |
| startup-read-09 | renewal-payment | a stored payment state readable but wrong |
| startup-read-10 | season-ticket | which spare copy of tickets and payments is fallen back on |
| migration-12 | renewal-payment | a payment may stay pending up to 3 working days (F4), so an update may land in the middle of one |
| migration-01, migration-02, migration-03, migration-04, migration-05, migration-06, migration-07, migration-08, migration-09, migration-10, migration-11 | dropped | this is the first slice built and no earlier version's saved data exists (the office works from a spreadsheet, 000_problem.md); nothing is renamed, retyped or carried forward |
| concurrency-01 | renewal-payment | the office refunds while an event changes the same payment |
| concurrency-02 | season-ticket | a ticket is renewed only when its payment is recorded |
| concurrency-05 | renew-and-pay-1 | the renewal is shown as recorded while the payment is only pending and may be declined |
| concurrency-06 | refund-a-renewal-1 | the subscriber is shown as refunded in every window |
| concurrency-07 | `card-token` | a token is usable once, within 15 minutes (F7) |
| concurrency-08 | renewal-payment | an event and a refund both need the stored payment |
| concurrency-09 | renew-and-pay-1 | a renewal clashing with another may be repeated and must not take a second payment |
| concurrency-10 | renewal-payment | a refund changes payment and ticket together |
| concurrency-12 | renewal-payment | the documents do not say a second copy of the product cannot run |
| concurrency-03, concurrency-04, concurrency-11 | dropped | each criterion reads one renewal; no report over a set (slice 2), no decision from a matching set, no operation needing sole use |
| lifecycle-01 | renew-and-pay-2 | renewal recorded, then the card is refused |
| lifecycle-02 | refund-a-renewal-1 | a refund request to PayRight can fail |
| lifecycle-03 | renewal-payment | taking a payment and giving it back cannot be taken back |
| lifecycle-04 | renewal-payment | a payment stays pending up to 3 working days (F4) |
| lifecycle-05 | season-ticket | a renewed ticket and its payment belong together |
| lifecycle-08 | renewal-payment | a renewal started and never paid |
| lifecycle-12 | `card-token` | the token is held 15 minutes (F7) |
| lifecycle-06, lifecycle-07, lifecycle-09, lifecycle-10, lifecycle-11 | dropped | no criterion removes anything: refunded and lapsed are states, not removals |
| user-input-02 | `renewal-request` | which values the renewal needs |
| user-input-05 | `renewal-request` | a request may arrive without passing the on-screen check |
| user-input-06 | refund-screen | what the office is told when a refund value is refused |
| user-input-08 | `refund-amount` | smallest and largest refund |
| user-input-09 | `payment-reference` | a repeated renewal must be recognised, not paid twice |
| user-input-11 | `refund-amount` | the refund and the payment amount must agree |
| user-input-12 | `refund-amount` | the written form of a number the office types |
| user-input-01, user-input-03, user-input-04, user-input-07, user-input-10 | dropped | the slice takes no typed text: the card form is PayRight's (F7) and the ticket and renewal are chosen, not typed |
| user-action-01 | renew-and-pay-1 | what the subscriber sees at once, and a second press of pay |
| user-action-02 | `renewal-screen` | reloading after a payment was started |
| user-action-03 | `renewal-screen` | stepping back after paying |
| user-action-05 | renew-and-pay-1 | leaving without warning mid-renewal |
| user-action-06 | `renewal-screen` | returning after the token's 15 minutes (F7) |
| user-action-07 | `renewal-request` | the same subscriber with two windows paying |
| user-action-08 | refund-a-renewal-1 | a refund cannot be undone |
| user-action-09 | `refund-screen` | the refund is final and should be confirmed |
| user-action-10 | renew-and-pay-1 | backing out of a renewal |
| user-action-11 | renew-and-pay-1 | a signed-in period ending mid-renewal |
| user-action-12 | `renewal-screen` | an address saved from the renewal screen |
| user-action-04 | dropped | no criterion signs anyone in or out |
| long-operation-01 | renew-and-pay-1 | the payment may take 3 working days (F4) |
| long-operation-02 | renewal-payment | pending versus stopped |
| long-operation-03 | renewal-payment | whether a pending payment can be stopped |
| long-operation-04 | renew-and-pay-1 | stopping a renewal partway |
| long-operation-05 | renewal-payment | how the subscriber learns it settled or was declined |
| long-operation-06 | renewal-payment | an interruption while pending |
| long-operation-07 | renewal-payment | a payment declined days later |
| long-operation-09 | renewal-payment | pending without an event |
| long-operation-10 | renewal-payment | how long the result of a payment stays shown |
| long-operation-11 | renewal-payment | a refund asked of a payment still pending |
| long-operation-12 | `refund-request` | a refund after 90 days is sure to fail (S2) |
| long-operation-08 | dropped | each operation acts on one renewal, so there are no items to partly succeed |
| time-01 | `payment-reference` | the 24-hour reference window depends on a clock |
| time-02 | `created-at` | PayRight's time and ours differ |
| time-03 | `payment-reference` | a clock set back inside the 24 hours |
| time-04 | `refund-request` | 90 days, 3 working days, 15 minutes and 24 hours |
| time-07 | season-ticket | a season has plain dates |
| time-08 | `created-at` | whose zone governs it |
| time-09 | `refund-request` | 90 days counted from settling |
| time-11 | `payment-updated-event` | two events with an equal time |
| time-12 | `created-at` | when PayRight created the payment, not when we recorded it |
| time-05, time-06, time-10 | dropped | the slice stores no future local moment and no repeating schedule |
| text-09 | `renewal-screen` | the subscriber's name in a message |
| text-10 | `refund-screen` | the office must tell two renewals apart by eye |
| text-12 | `card-refused-screen` | room for the message |
| text-01, text-02, text-03, text-04, text-05, text-06, text-07, text-08, text-11 | dropped | the slice compares, searches, cuts and orders no text |
| presentation-02 | `refund-amount` | how the number is written |
| presentation-03 | `refund-amount` | the unit of the refund |
| presentation-05 | `refund-amount` | decimals and rounding of a refund |
| presentation-01, presentation-04, presentation-06, presentation-07, presentation-08, presentation-09, presentation-10, presentation-11, presentation-12 | dropped | no criterion shows a date or time, a count, a list or a name order |
| corpus: all | dropped | the slice ships no body of content |
| secrets-01 | `secret-key` | the key sits somewhere the product runs |
| secrets-02 | `secret-key` | the key is the playhouse's account's |
| secrets-03 | `secret-key` | it must stay out of records |
| secrets-04 | `secret-key` | replacing it while renewals run |
| secrets-05 | `secret-key` | its exposure lets someone take payments |
| secrets-06 | `secret-key` | PayRight may refuse it |
| secrets-07 | `secret-key` | the key sends every request |
| secrets-08 | `secret-key` | the documents do not say who holds it |
| secrets-09 | `secret-key` | it travels in a header |
| secrets-10 | `secret-key` | how it reaches the running product |
| secrets-11 | `secret-key` | where it is kept is unreachable |
| secrets-12 | `secret-key` | a record of its use |
| authorization-01 | refund-a-renewal-1 | only the office should refund |
| authorization-02 | season-ticket | the subscriber renews only their own |
| authorization-03 | refund-a-renewal-1 | a refund request sent past the screen |
| authorization-04 | `renewal-request` | what a person with no rule may do |
| authorization-05 | refund-a-renewal-1 | office staff changing role |
| authorization-06 | `renewal-request` | a renewal sent from someone else's page |
| authorization-07 | `renewal-request` | a link or load must not start a payment |
| authorization-08 | refund-a-renewal-1 | the check of who may refund cannot be completed |
| authorization-10 | `renewal-request` | which ticket the request names comes from the device |
| authorization-11 | `renewal-screen` | access lost mid-renewal |
| authorization-12 | `renewal-request` | the account the subscriber is in |
| authorization-09 | dropped | the slice stores and serves no file |
| configuration-01 | payright | its settings are checked at start |
| configuration-02 | `webhook-address` | what values make sense |
| configuration-03 | payright | the account differs per installation |
| configuration-04 | payright | one place to see the settings |
| configuration-05 | payright | defaults |
| configuration-06 | `webhook-address` | what is switched on |
| configuration-07 | payright | PayRight test mode versus real (O1) |
| configuration-08 | payright | introducing a changed setting |
| configuration-09 | payright | returning a setting |
| configuration-10 | payright | a record of changes |
| configuration-11 | payright | diagnostic modes for it |
| configuration-12 | `webhook-address` | who can change it |
| logging-01 | renewal-payment | payments and refunds should leave a record |
| logging-02 | renewal-payment | what each record says |
| logging-03 | `card-token` | must never be recorded |
| logging-04 | `payment-updated-event` | outside text recorded |
| logging-05 | renewal-payment | a record that cannot be written |
| logging-06 | renewal-payment | growth of the records |
| logging-07 | renew-and-pay-2 | what the subscriber sees against what is recorded |
| logging-08 | renewal-payment | where records are kept |
| logging-09 | renewal-payment | who is told of a lost payment |
| logging-10 | renewal-payment | who can change records |
| logging-11 | `created-at` | which clock |
| logging-12 | renewal-payment | how long records are kept |
| accessibility-01 | `renewal-screen` | doing it by keyboard |
| accessibility-02 | `card-refused-screen` | leaving it |
| accessibility-03 | `renewal-screen` | the focus shown |
| accessibility-04 | `card-refused-screen` | where focus goes when it closes |
| accessibility-05 | `refund-screen` | control names |
| accessibility-06 | `renewal-screen` | non-text meaning |
| accessibility-07 | renew-and-pay-1 | learning the result |
| accessibility-08 | `card-refused-screen` | colour for refusal |
| accessibility-09 | `renewal-screen` | contrast |
| accessibility-10 | `renewal-screen` | text at twice the size |
| accessibility-11 | `card-token` | 15 minutes to pay (F7) |
| accessibility-12 | `renewal-screen` | the "being taken" indication may move |
