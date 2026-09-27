---
name: miss-check
description: This skill should be used when the user says "this isn't doing what I wanted", "expected Y got Z", "it's wrong", or a specific behavior missed. Writes one failing check. Does not fix.
version: 0.1.0
license: MIT
compatibility: opencode
---

# Miss check

Turn one miss into a check that fails for the reason the human named. Do not fix the product.

If this conversation already contains the implementation, stop. Tell the human to open a new session with only this sentence attached:

`When I do X, I expected Y, I got Z. Write one failing check. Do not fix.`

## When to use

- One behavior is wrong.
- The human can say what they did, what they expected, and what they got.

Do not use for a pile of misses. One sentence, one check. The next miss is the next session. Do not use to fix, refactor, or explain the architecture.

## Procedure

1. Require the sentence: when I do X, I expected Y, I got Z. If any part is missing, ask one question and stop. Do not invent Y.
2. Write one failing test, or one command that prints `FAIL` for Z and would print `PASS` for Y. Put the check in the project's existing test place. If there is no test place, one new test file is allowed. No other new file.
3. Run the check. It must fail because of Z, not because the test does not compile. If it fails for a different reason, fix the check, not the product.
4. Stop. Do not edit product code. Do not "while you're here."

Completion: the check fails for the named reason, and the diff does not touch product code.

## Output

- The sentence, unchanged.
- The check path.
- The fail output, trimmed.
- One line: the fix is a new session whose only charge is to make this check pass, touching nothing else. If that fix needs a new file, a new dependency, or a new behavior, that session must stop and say so.

## Verification

- The check fails.
- The failure matches Z.
- Product source is unchanged.
- Exactly one miss is encoded.
