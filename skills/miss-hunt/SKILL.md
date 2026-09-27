---
name: miss-hunt
description: This skill should be used when the user says "review missed it", "still misses things", "I don't trust this", or a review plan left holes. Fresh context only. Three failing tests. Does not fix.
version: 0.1.0
license: MIT
compatibility: opencode
---

# Miss hunt

Find holes the last review could not see, because that review shared the author's frame. Do not fix them here.

If this conversation contains the implementation, the review plan, a summary of what was fixed, or a subagent's review, stop. Those are the frame. Tell the human to open a new session with only the done-means sentence and how to run the thing. Do not attach the review plan.

## When to use

- A review, including one done by subagents in the build session, still missed cases.
- The human does not trust the result and cannot yet name the miss.

Do not use to fix, to restyle, or to rewrite the review plan. Style notes are not findings.

## Procedure

1. Read the done-means sentence. If you do not have one, stop and ask for that sentence only.
2. Run the thing. Do not read the implementation to invent cases the code already handles.
3. Find 3 inputs where the result is wrong relative to done-means. For each, add a failing test in the existing test place. One new test file is allowed if there is no test place. No product edits.
4. Each test must fail for a behavior reason, not because it does not compile.
5. If you find fewer than 3, say `REVIEW_FAILED` and what you could not reach. Do not pad with style, naming, or "could be cleaner".
6. Stop. Do not fix.

A review that returns only style notes is `REVIEW_FAILED`.

## Output

- `PASS` only when 3 failing behavior tests exist. Otherwise `REVIEW_FAILED`.
- For each test: the input, the wrong result, the path.
- One line: the human keeps the real misses and drops the ones that are thoroughness theater. Each kept miss is a later `make-pass` session. This session does not fix.

## Verification

- Product source is unchanged.
- Three tests fail for behavior, or the verdict is `REVIEW_FAILED`.
- The review plan from the build session was not an input.
- No fix was applied.
