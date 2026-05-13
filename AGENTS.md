# Repository Guidelines

## Project Structure & Module Organization

This repository is a local agent plugin marketplace framework. Marketplace metadata lives at the root, and plugin implementations live under `plugins/`.

- `.agents/plugins/marketplace.json` for Codex CLI marketplace metadata.
- `.claude-plugin/marketplace.json` for Claude Code marketplace metadata.
- `.github/plugin/marketplace.json` for GitHub Copilot CLI marketplace metadata.
- `plugins/<plugin-name>/plugin.json` for the canonical shared plugin manifest.
- `plugins/<plugin-name>/skills/` for plugin skills.
- `plugins/<plugin-name>/agents/` for plugin agent definitions.
- `scripts/` for repository-local automation.
- `tests/` for automated tests.
- `docs/` for design notes, operational guides, and contributor-facing documentation.
- `assets/` for static images, sample data, or other non-code resources.

Keep generated files, dependency directories, and local caches out of version control unless intentionally part of the project.

## Build, Test, and Development Commands

Run commands from the repository root:

- `python3 scripts/sync_plugin_metadata.py`: generate platform marketplace files and platform manifest copies from canonical plugin manifests.
- `python3 scripts/sync_plugin_metadata.py --check`: verify generated metadata is current without writing files.
- `python3 -m unittest`: run the full test suite.

Do not require contributors to infer setup steps from CI files alone.

## Coding Style & Naming Conventions

Use Python standard-library tooling for repository automation unless a stronger need is introduced. Keep JSON stable and generated through `scripts/sync_plugin_metadata.py`.

Prefer:

- Kebab-case plugin names such as `code-reviewer`.
- Canonical plugin manifests at `plugins/<plugin-name>/plugin.json`.
- Test files named to match the unit under test, such as `test_sync_plugin_metadata.py`.
- Small scripts with focused responsibilities.

## Testing Guidelines

Add tests with any new behavior. Place tests in `tests/`. Cover normal behavior, edge cases, and regressions for fixed bugs. For metadata changes, include JSON validity and stale-file detection where applicable.

## Commit & Pull Request Guidelines

Readable Git history is not available here, so no repository-specific commit convention can be inferred. Use concise, imperative commit messages, for example `Add user creation tests` or `Fix config parsing error`.

Pull requests should include a short summary, test results, linked issues when applicable, and screenshots for UI changes. Keep PRs focused so reviewers can understand the behavior change and verify it locally.

## Agent-Specific Instructions

Before editing, inspect the current tree and avoid overwriting unrelated user changes. Edit canonical `plugins/<plugin-name>/plugin.json` files, then run `python3 scripts/sync_plugin_metadata.py`; do not hand-edit generated platform manifest copies unless you are changing the generator itself.
