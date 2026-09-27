---
name: make-grade
description: This skill should be used when the user says "make the grade", "implement the order", "build this", or a new session has the order and no review yet. Makes the grade pass. Does not review itself. Stops at budget.
version: 0.1.0
license: MIT
compatibility: opencode
---

# Make grade

Make the grade commands pass. Do not review your own work. Do not report arrival.

If this conversation already contains a review, a hunt, a cut, or a summary of what an agent fixed, stop. New session. Attach the order only.

## When to use

- The four lines exist outside this chat.
- The human wants that order built, and nothing else.

Do not use to invent the order, to fix a miss you have not encoded as a check, or to grade the result. If any line is blank, stop and name `captain-order`.

## Procedure

1. Read the order. If "done means", the grade, "not this", or "stop and ask" is missing, stop. Do not interview and then code in this session.
2. Read only the files the grade needs. Do not tour the repo.
3. Change only what the grade needs. Default budget if the order has none: one behavior, at most 3 files, no new dependency, no new top-level directory.
4. Do not build anything in "not this". Do not spawn a reviewer, a hunter, or a second implementer. A subagent here is still this ship.
5. You may run a grade command to see the failure. You may edit again while still inside budget. You may not start a review of the code you just wrote.
6. If the next edit would pass the budget, add a dependency, add a behavior, or change "done means", stop and say which line tripped. Do not do the thing.
7. Stop when the commands you ran are green, or when you must ask. Print the commands and the output. Say the human runs them to accept. Do not say done.

## Output

- Files changed, from `git diff --stat`.
- Grade commands and the output you saw.
- One line: you accept by running these. This session does not review itself.

## Verification

- Stat is inside budget.
- No new dependency the order did not name.
- No file whose only job is a review note, a summary, or a new behavior in "not this".
- You did not claim the human may skip running the grade.
