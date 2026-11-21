
What to do with this report

Take the rows in order. Act on the first row that applies, then stop,
unless the row says to go on.

| # | When the report says | Do | Never |
|---|---|---|---|
| 1 | the system is NOT supported by the VM tool | Stop. Say which system this is and why it cannot be used, in the report's words. | Offer another way to work. Go on to the tracker or the documents. |
| 2 | the VM tool is not installed | Say what would be installed, with which command, and why (all work on the project runs inside a VM). Ask for a yes and wait. | Run the command before the yes. Start anything else. |
| 3 | not signed in to the VM tool | Hand the sign-in to the user: name the command, to be run in their own terminal. Wait. | Run the sign-in yourself. |
| 4 | a lock is OFF | Run the command the report gives for turning every lock on, then say what was off and that it is now on. If a lock stays off, refuse to use any VM and say why. | Ask first. Use a VM while a lock is off. |
| 5 | the planning folder is not chosen yet | Ask where the planning documents are, or where to create them. Say that the problem comes first once the folder is known. | Ask again for a folder the report already names. |
| 6 | a pull request is ready to merge, or has comments to address | Put it first: name it and what it needs. Then go on to rows 7 and 8, in that order, as what follows. | Merge it: merging is the user's. Put the documents ahead of it. |
| 7 | an open issue is labelled critical, high or blocking | Name it and ask whether to address it before the next stage. Then go on to row 8 as what follows. | Start on it, or pass over it, without the answer. |
| 8 | none of the above stops you | Name the next stage by the documents. Where the report says "out of order", say which document is missing and that it comes first. | Skip past a missing document. |

Whatever the user asks for:

- No work on the project happens on this machine outside a VM. Write
  no file of the project here and run no build here. Asked to build
  while rows 1 to 4 apply, do the row first and say that the build
  waits for it.
- Asked to build something the documents do not reach yet, start at
  the next stage by the documents (the problem, where there are none)
  and say so. Do not build.
- The only things asked of the user at startup: the yes to install;
  where the planning documents go; whether to address a critical, high
  or blocking issue first. Everything else is decided and said.
- Trust the report: do not read the project's files or call the
  tracker again to check it.
