---
name: captain-order
description: This skill should be used when the user says "write the order", "captain-order", "done means", "before we code", or starts a build without a gradeable outcome. Blocks code until four lines are full. Rejects "keep going".
version: 0.1.0
license: MIT
compatibility: opencode
---

# Captain order

Write the order. Do not write the product. The order is the only thing a later session is allowed to see.

If this conversation has already been implementing, stop. Tell the human to open a new session with this skill and no other context.

## When to use

- A build is about to start and "done" is not a sentence a stranger could grade.
- The charge is activity: "keep going", "improve it", "make it better", "clean it up", "review and fix", "while you're in there".
- The human asks for the four lines.

Do not use to implement the order. That is a different session.

## Four lines

All four are required. A blank line means you ask one question and stop. Do not fill a blank by guessing.

- **Done means:** one sentence a stranger can grade. Who can do what, or what is true, that was not true before.
- **Grade:** V1, V2, and V3 when three exist. Each is a command, a click, or a look. Pass or fail. "Looks good" is not a grade. Reject it.
- **Not this:** the drift that must not be fed. Name the extra surface, file, or behavior.
- **Stop and ask:** merge, post, pay, send a message to a person, anything irreversible, or any change to "done means".

## Budget

If the human does not set one, write this default:

- One behavior.
- At most 3 files changed.
- No new dependency.
- No new top-level directory.

A tighter budget they name replaces the default. Do not loosen the default on your own.

## Procedure

1. Restate the four lines, including blanks.
2. If any line is blank or is activity rather than a shore, ask one question. Stop.
3. When all four hold, write them to `ORDERS.md` in the working directory only if that directory is a repo the human owns for this task. Otherwise print the four lines and tell them to put the text in the ticket or in a file outside the chat.
4. Stop. Tell them the implement session is new, and that it may see `ORDERS.md` and not this conversation.

Rejected charges, even if the four lines exist: any charge that changes "done means" inside the implement session. That change comes back here first.

## Output

Print the four lines and the budget. Then one sentence: do not implement in this session.

## Verification

- No product source file was created or edited.
- All four lines are non-empty and gradeable.
- The grade names an observable pass, not a feeling.
- "Not this" names a concrete drift, not "don't mess up".
