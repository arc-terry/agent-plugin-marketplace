# Code Reviewer Plugin

Code Reviewer adds a focused review workflow for agentic coding tools. It is meant for reviewing local changes, pull requests, or a bounded patch before merge.

## What It Reviews

- Correctness bugs and behavioral regressions.
- Security, data-loss, and reliability risks.
- Performance issues that are likely to matter in real use.
- Missing or weak tests for changed behavior.
- Documentation gaps when they block safe use or review.

## Usage

Ask the agent to use the Code Reviewer plugin, then provide a branch, diff, pull request, or file set to review. Findings should be ordered by severity and include file and line references when available.

Example prompts:

- `Review my current changes.`
- `Find bugs and missing tests in this patch.`
- `Check this PR for regressions.`

## Metadata

The canonical manifest is `plugins/code-reviewer/plugin.json`. Run `python3 scripts/sync_plugin_metadata.py` from the repository root after changing it.
