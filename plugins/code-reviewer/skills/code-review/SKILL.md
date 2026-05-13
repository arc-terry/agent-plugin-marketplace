---
name: code-review
description: Use when reviewing code changes, pull requests, diffs, or implementation plans for correctness, regression risk, security, performance, and test coverage.
---

# Code Review

Adopt a review stance. Prioritize findings over summaries.

## Review Workflow

1. Identify the change boundary: branch, diff, file list, or user-provided patch.
2. Inspect the changed code and the relevant surrounding code before judging behavior.
3. Look for concrete defects: incorrect logic, broken contracts, data loss, race conditions, security issues, performance regressions, and missing tests.
4. Report only actionable findings. Do not pad the review with style preferences or praise.

## Response Format

Start with findings, ordered by severity. Each finding should include:

- Severity: `Critical`, `High`, `Medium`, or `Low`.
- Location: file and line when available.
- Problem: what can go wrong.
- Fix direction: the smallest practical correction or test.

After findings, include open questions or assumptions. Keep the summary brief and secondary.

If no issues are found, say that clearly and mention any residual test or verification gaps.

## Review Standards

- Treat changed behavior and public interfaces as high-risk until verified.
- Prefer evidence from code, tests, logs, or commands over speculation.
- Flag missing tests when the changed behavior can regress.
- Do not recommend broad refactors unless they are necessary to fix a concrete issue.
- Do not rewrite the code unless the user explicitly asks for implementation help.
