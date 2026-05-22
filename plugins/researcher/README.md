# Researcher Plugin

Researcher adds an evidence-first workflow for agentic coding tools. It is meant for answering research questions, comparing evidence, evaluating sources, and producing cited summaries.

## Contents

- `plugin.json`: canonical shared plugin manifest.
- `.claude-plugin/plugin.json`: generated Claude Code manifest copy.
- `.codex-plugin/plugin.json`: generated Codex manifest copy.
- `skills/research/SKILL.md`: research workflow skill.
- `agents/researcher.agent.md`: researcher agent instructions.
- `commands/research.md`: command prompt for repeatable research requests.
- `examples/`: usage and output examples.

## What It Researches

- Current documentation, standards, policies, and APIs.
- Evidence for technical or product decisions.
- Claims that need source support or uncertainty notes.
- Conflicting information across sources.

## Usage

Ask the agent to use the Researcher plugin, then provide a question, claim, source set, or decision to investigate. Results should include citations and caveats when evidence is incomplete or conflicting.

Example prompts:

- `Research this topic and cite sources.`
- `Compare the evidence for these options.`
- `Summarize what is known and what remains uncertain.`

## Metadata

The canonical manifest is `plugins/researcher/plugin.json`. Run `python3 scripts/sync_plugin_metadata.py` from the repository root after changing it.
