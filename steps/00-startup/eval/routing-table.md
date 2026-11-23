
What to do with this report

Take the rows in order. Act on the first row that applies, then stop,
unless the row says to go on.

| # | When the report says | Do | Never |
|---|---|---|---|
| 0 | a line says REFUSED, or startup could not read everything | Stop. Say what could not be read, in the report's words, and that nothing else is done until it reads. | Guess what the unread part would have said. Go on to the tracker, the documents or any stage. |
| 1 | the system is NOT supported by the VM tool | Stop. Say which system this is and why it cannot be used, in the report's words. | Offer another way to work. Go on to the tracker or the documents. |
| 2 | the VM tool is not installed | Say what would be installed, with which command, and why (all work on the project runs inside a VM). Ask for a yes and wait. | Run the command before the yes. Start anything else. |
| 3 | not signed in to the VM tool | Hand the sign-in to the user: name the command, to be run in their own terminal. Wait. | Run the sign-in yourself. |
| 4 | a lock is OFF | Run the command the report gives for turning every lock on, then say what was off and that it is now on. Then take row 5 or 6 from what that command printed. If a lock stays off, refuse to use any VM and say why. | Ask first. Use a VM while a lock is off. |
| 5 | there is no VM for this project | Say that the project is worked on inside a VM, and what making one does, in the report's words. Ask for a yes and wait. After the yes, run the command the report gives, then give the user the command it prints for continuing inside the VM. | Make it before the yes. Start anything else here. |
| 6 | a VM for this project exists, and this session is not inside it | Give the user the command the report gives for continuing inside the VM, to run in their own terminal. Say the work goes on there. Stop. | Run that command yourself. Do any of the project's work here. |
| 7 | the planning folder is not chosen yet | Ask where the planning documents are, or where to create them. Say that the problem comes first once the folder is known. When the user names the folder, run the command the report gives to record it, read the documents again as it says, and take row 10. | Ask again for a folder the report already names. Write a document before the folder is recorded. |
| 8 | a pull request is ready to merge, or has comments to address | Put it first: name it and what it needs. Then go on to rows 9 and 10, in that order, as what follows. | Merge it: merging is the user's. Put the documents ahead of it. |
| 9 | an open issue is labelled critical, high or blocking | Name it and ask whether to address it before the next stage. Then go on to row 10 as what follows. | Start on it, or pass over it, without the answer. |
| 10 | none of the above stops you | Name the next stage by the documents. Where the report says "out of order", say which document is missing and that it comes first. When a stage is finished and the user says to go on, read the documents again with the command the report gives, and take this row with what it prints. | Skip past a missing document. Name a document yourself: its name and number come from the report. |

Whatever the user asks for:

- Begin the answer with the row you acted on. What follows it comes
  after, and is said to come after.
- The project is worked on only inside its VM. Unless the report says
  this session is inside a VM, write no file of the project and run
  no build. Asked to build while rows 0 to 6 apply, do the row first
  and say that the build waits for it.
- Asked to build something the documents do not reach yet, start at
  the next stage by the documents (the problem, where there are none)
  and say so. Do not build.
- The only things asked of the user at startup: the yes to install;
  the yes to make the project's VM;
  where the planning documents go; whether to address a critical, high
  or blocking issue first. Everything else is decided and said.
- The user sees neither this table nor the report: never mention the
  table or a row's number. Say what you found, in plain words.
- Trust the report: do not read the project's files or call the
  tracker again to check it. Reading the documents again, with the
  command the report gives, is how the next stage is found.
- Never suggest what the product might be or do, not even as
  examples: that is the user's to say.
- A file of the user's (a sheet, an export, a screenshot) is never
  opened, searched or copied here, wherever it is. Ask the user to
  describe it on their own machine, as the report says, and to paste
  what that prints; list it in `sources.md` in the planning folder
  (what it is, where the user keeps it, the date, its columns as
  pasted). An example in a document is invented, and said to be: a
  real name or figure the user gives as an example is not written
  down.
- A stage with no text of its own here is not built yet. Say so and
  stop: do not do its work some other way, and do not offer to.
