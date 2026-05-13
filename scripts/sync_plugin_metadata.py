#!/usr/bin/env python3
"""Generate platform plugin metadata from canonical plugin manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MARKETPLACE_NAME = "agent-plugin-marketplace"
MARKETPLACE_DISPLAY_NAME = "Agent Plugin Marketplace"
PLUGIN_CATEGORY = "Productivity"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=False) + "\n"


def discover_plugins(root: Path) -> list[dict]:
    plugin_root = root / "plugins"
    if not plugin_root.exists():
        raise FileNotFoundError(f"missing plugin directory: {plugin_root}")

    manifests = []
    for manifest_path in sorted(plugin_root.glob("*/plugin.json")):
        manifest = load_json(manifest_path)
        plugin_name = manifest["name"]
        expected_path = plugin_root / plugin_name / "plugin.json"
        if manifest_path != expected_path:
            raise ValueError(
                f"manifest name {plugin_name!r} must match directory {manifest_path.parent.name!r}"
            )
        manifests.append(manifest)
    if not manifests:
        raise ValueError(f"no plugin manifests found in {plugin_root}")
    return manifests


def marketplace_for(plugins: list[dict], source_path_prefix: str = "./plugins") -> dict:
    return {
        "name": MARKETPLACE_NAME,
        "interface": {
            "displayName": MARKETPLACE_DISPLAY_NAME,
        },
        "plugins": [
            {
                "name": plugin["name"],
                "source": {
                    "source": "local",
                    "path": f"{source_path_prefix}/{plugin['name']}",
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": plugin.get("interface", {}).get("category", PLUGIN_CATEGORY),
            }
            for plugin in plugins
        ],
    }


def generated_files(root: Path) -> dict[Path, str]:
    plugins = discover_plugins(root)
    files: dict[Path, str] = {
        root / ".claude-plugin" / "marketplace.json": dump_json(marketplace_for(plugins)),
        root / ".github" / "plugin" / "marketplace.json": dump_json(marketplace_for(plugins)),
        root / ".agents" / "plugins" / "marketplace.json": dump_json(marketplace_for(plugins)),
    }
    for plugin in plugins:
        manifest_text = dump_json(plugin)
        plugin_dir = root / "plugins" / plugin["name"]
        files[plugin_dir / ".claude-plugin" / "plugin.json"] = manifest_text
        files[plugin_dir / ".codex-plugin" / "plugin.json"] = manifest_text
    return files


def check_files(files: dict[Path, str]) -> list[Path]:
    stale_paths = []
    for path, expected in files.items():
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale_paths.append(path)
    return stale_paths


def write_files(files: dict[Path, str]) -> None:
    for path, contents in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate marketplace and platform manifests from plugin.json files."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Marketplace repository root. Defaults to current working directory.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated files are missing or stale instead of writing them.",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        files = generated_files(root)
        if args.check:
            stale_paths = check_files(files)
            if stale_paths:
                for path in stale_paths:
                    print(f"stale generated metadata: {path}", file=sys.stderr)
                return 1
            print("generated metadata is current")
            return 0

        write_files(files)
        for path in files:
            print(f"wrote {path.relative_to(root)}")
        return 0
    except (FileNotFoundError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
