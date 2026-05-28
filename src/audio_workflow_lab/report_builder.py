"""Markdown report rendering for the creative audio workflow demo."""

from __future__ import annotations

from typing import Any

from .metadata import normalize_track, validate_track
from .release_plan import build_release_plan
from .repurpose import build_repurpose_plan


def render_track_report(track: dict[str, Any]) -> str:
    """Render a clean markdown report for one synthetic track."""
    normalized = normalize_track(track)
    issues = validate_track(normalized)
    release_plan = build_release_plan(normalized)
    repurpose_plan = build_repurpose_plan(normalized)

    lines = [
        "# Creative Audio Workflow Report",
        "",
        "> Clean-room demo using synthetic metadata only. No real audio assets, client files, credentials, stems, masters, or private release data are included.",
        "",
        f"## Track: {normalized.get('title', 'Untitled Track')}",
        "",
        f"- Artist: {normalized.get('artist', 'Unknown')}",
        f"- BPM: {normalized.get('bpm', 'n/a')}",
        f"- Key: {normalized.get('key', 'n/a')}",
        f"- Duration: {normalized.get('duration_seconds', 'n/a')} seconds",
        f"- Mood tags: {', '.join(normalized.get('mood_tags', [])) or 'n/a'}",
        f"- Release channels: {', '.join(normalized.get('release_channels', [])) or 'n/a'}",
        "",
        "## Validation",
        "",
    ]

    if issues:
        lines.extend(f"- `{issue}`" for issue in issues)
    else:
        lines.append("- No release-prep gaps found in synthetic metadata.")

    lines.extend(["", "## Release Checklist", ""])
    for item in release_plan:
        lines.append(f"- **{item['phase']}**: {item['task']} — {item['detail']} ({item['status']})")

    lines.extend(["", "## Repurposing Prompts", ""])
    for item in repurpose_plan:
        lines.append(f"- **{item['channel']}**: {item['prompt']}")
        lines.append(f"  - Safety: {item['safety_note']}")

    lines.append("")
    return "\n".join(lines)
