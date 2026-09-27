---
name: make-pass
description: This skill should be used when the user says "make this pass", "make-pass", "fix this check", or a failing check already exists. Makes that one check pass. Touches nothing else.
version: 0.1.0
license: MIT
compatibility: opencode
---

# Make pass

Make one failing check pass. Touch nothing else.

If this conversation wrote the product, wrote the check, or reviewed the code, stop. New session. Attach the check path and this sentence only: when I do X, I expected Y, I got Z.

## When to use

- A check already fails for the reason the human named.
- The charge is to make that check pass.

Do not use to write the check. That is `miss-check`. Do not use to hunt for more misses. That is `miss-hunt`. Do not use to cut. That is a later session.

## Procedure

1. Run the check. Confirm it fails because of Z, not because it does not compile. If it fails for a different reason, stop and say so. Do not retarget the check.
2. Change the product only enough for this check to pass. No rename. No reformat. No second test. No new dependency. No new behavior the check does not demand.
3. If the fix needs a new file, a new dependency, or a change to "done means", stop and say so. Do not take it.
4. Run the check again. If it passes, stop. Do not look for the next miss.
5. Show `git diff --stat` and the check output. The human runs the check to accept. You do not say arrived.

## Output

- The check path.
- Fail output before, pass output after, both trimmed.
- Stat.
- One line: nothing else was in scope. The next miss is a new session.

## Verification

- The same check that failed now passes.
- The diff does not add a dependency, a second test, or an unnamed behavior.
- You did not review the rest of the change.
