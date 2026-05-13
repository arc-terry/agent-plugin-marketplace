# Agent Plugin Marketplace

This repository is a small framework for building and publishing local agent plugins across Claude Code, GitHub Copilot CLI, and Codex CLI.

The repo keeps one canonical plugin manifest per plugin and generates platform metadata from it. The first plugin, `code-reviewer`, provides focused code review guidance for agentic coding workflows.

## Structure

```text
.
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
├── .github/plugin/marketplace.json
├── plugins/
│   └── code-reviewer/
│       ├── plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── skills/code-review/SKILL.md
│       └── agents/reviewer.agent.md
├── scripts/sync_plugin_metadata.py
└── tests/test_sync_plugin_metadata.py
```

## Commands

Generate marketplace files and platform manifests:

```bash
python3 scripts/sync_plugin_metadata.py
```

Check whether generated files are current:

```bash
python3 scripts/sync_plugin_metadata.py --check
```

Run tests:

```bash
python3 -m unittest
```

## Adding Or Editing A Plugin

1. Create or update `plugins/<plugin-name>/plugin.json`.
2. Add plugin content such as `skills/`, `agents/`, docs, scripts, or assets.
3. Run `python3 scripts/sync_plugin_metadata.py`.
4. Run `python3 -m unittest`.

The generated platform files should not be edited by hand. Change the canonical `plugin.json` instead.

## Marketplace Installation

Claude Code:

```text
/plugin marketplace add ./
```

GitHub Copilot CLI:

```bash
copilot plugin marketplace add ./
```

Codex CLI uses the repo-local marketplace metadata at `.agents/plugins/marketplace.json`.
