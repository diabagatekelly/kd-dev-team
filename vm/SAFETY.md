# Keeping the helper in its box

The AI helper does its work inside a small, separate computer that
lives inside yours (a "virtual machine", or VM). It is thrown away when
the work is done. This page says what keeps the helper inside that box,
in plain words. You do not have to do any of it by hand: the launcher
switches every lock on before it starts a VM, and refuses to start one
if a lock is off.

## What is locked, and why

| The lock | Why it matters |
|---|---|
| The helper can reach only a short list of websites | If something goes wrong inside the box, it cannot send your work anywhere else or fetch anything from an unknown place. Every other address is refused, and each refusal is written down |
| It cannot reach your computer or your home network | Your files, your printer, your router and other devices stay out of its reach |
| It works on its own copy of your project | It can never change or delete your own copy. You decide what comes back |
| It never holds your real passwords or keys | A gatekeeper outside the box adds them at the last moment, so there is nothing inside for it to copy or leak |
| It cannot open pages in your web browser | Your browser is signed in to your email, your bank and more. Nothing inside the box may steer it |
| It cannot see your browser tabs, be steered from another device, or use your clipboard | Each of these is a small door out of the box, so each is shut |
| The box is thrown away afterwards | Whatever happened inside ends with it |

## Check it yourself, in two commands

    vm.sh status            is every lock on?
    vm.sh selftest NAME     from inside a running box, try to break each rule

Each prints one line per lock, `ok` or `FAIL`, in the same words as the
table above. If anything says `OFF`, run `vm.sh secure` and it is put
right.

## The few things only you can do

1. **If you give the helper a key to your code host (to push for
   you), make it a key for that one project only, and do not tick
   "Workflows".** A key that can change a project's automation can make
   that automation run with the project's other secrets.
2. **Add a website to the list only when you know why it is needed.**
   The helper will ask; saying no is always safe.
3. **Keep the VM tool up to date.** Fixes to the gatekeeper arrive
   often.

## What this does not promise

No box is perfect. A fault in the VM tool itself could let something
out, which is how a well-known escape in 2026 happened: the one door
left open for downloads had a flaw. The locks above limit what could be
reached if that ever happened here, and the helper is given an ordinary
building task, with the model's own safeguards as they normally are,
not a task of breaking things. Inside the box the helper does not stop
to ask permission for each step: the box, not the asking, is what keeps
your computer safe, which is why every lock above matters.
While a box is running, whatever runs inside it can use your AI
subscription and, if you gave it a key, push to that one project.
