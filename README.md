# Agent Plugin Marketplace

This repository is a small framework for building and publishing local agent plugins across Claude Code, GitHub Copilot CLI, and Codex CLI.

The repo keeps one canonical plugin manifest per plugin and generates platform metadata from it. The `code-reviewer` plugin provides focused code review guidance for agentic coding workflows, and `researcher` provides evidence-first research guidance.

## Structure

```text
.
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
├── .github/plugin/marketplace.json
├── plugins/
│   ├── code-reviewer/
│   │   ├── plugin.json
│   │   ├── .claude-plugin/plugin.json
│   │   ├── .codex-plugin/plugin.json
│   │   ├── skills/code-review/SKILL.md
│   │   └── agents/reviewer.agent.md
│   └── researcher/
│       ├── plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── skills/research/SKILL.md
│       └── agents/researcher.agent.md
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

Codex CLI:

```bash
codex plugin marketplace add ./
codex plugin add researcher@agent-plugin-marketplace
```

To install the code review plugin instead, run:

```bash
codex plugin add code-reviewer@agent-plugin-marketplace
```
