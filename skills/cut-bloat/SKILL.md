---
name: cut-bloat
description: This skill should be used when the user says "bloat", "too much code", "cut this", "sewage", or a small request produced a large diff. Stat first. Delete only. Does not add code.
version: 0.1.0
license: MIT
compatibility: opencode
---

# Cut bloat

Bloat is a stat, not a read. Do not review the code to decide if the extra was reasonable.

Correctness and cutting are different voyages. If the named checks are failing, stop and send the human to `miss-check`. Do not cut and fix in this session.

## When to use

- The human says the diff is bloated, or a small order grew files, helpers, or a dependency.
- `git diff --stat` is over the budget in `ORDERS.md`.

Do not use to add features, rename for taste, or "simplify" by rewriting.

## Budget

Read the budget from `ORDERS.md` if it exists. If it does not, use:

- One behavior: at most 3 files.
- No new dependency.
- No new top-level directory.

Over budget, or a new dependency the order did not name: reject unread. Do not skim the diff to see if the bloat is justified.

## Procedure

1. Run `git diff --stat` before opening files. Record the numbers.
2. If over budget, say rejected unread, then continue to the delete pass only if the human asked to cut. If they only asked for a verdict, stop after the stat.
3. Delete code not required for the named checks to pass. Do not add code. Do not rename. Do not reformat. Do not split or merge files except by deleting a file the checks do not need.
4. If a deletion would fail a named check, leave that code and name it. Do not delete the check to make the stat smaller.
5. Run `git diff --stat` again. Show before and after.
6. Do not claim the checks pass. Tell the human to run them.

## Output

- Stat before.
- Rejected unread, or not.
- Stat after.
- Lines left in place because a named check needs them.
- One line: the human runs the checks. This session does not start the next feature.

## Verification

- The after stat is smaller, or you stopped because every remaining line is required by a named check.
- No new dependency.
- The diff adds no product behavior.
- You did not report "tests passed" unless the human ran them and pasted output.
