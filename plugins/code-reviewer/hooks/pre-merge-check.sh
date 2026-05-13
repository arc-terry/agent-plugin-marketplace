#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$repo_root"

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest
PYTHONDONTWRITEBYTECODE=1 python3 scripts/sync_plugin_metadata.py --check
