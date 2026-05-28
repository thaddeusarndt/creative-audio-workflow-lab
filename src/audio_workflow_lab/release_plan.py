"""Release checklist generation from synthetic track metadata."""

from __future__ import annotations

from typing import Any

from .metadata import validate_track


def _task(phase: str, task: str, detail: str) -> dict[str, str]:
    return {"phase": phase, "task": task, "detail": detail, "status": "todo"}


def build_release_plan(track: dict[str, Any]) -> list[dict[str, str]]:
    """Build a deterministic release checklist from a normalized track record."""
    title = track.get("title", "Untitled Track")
    channels = set(track.get("release_channels", []))
    assets = track.get("assets") or {}
    issues = set(validate_track(track))

    tasks = [
        _task("metadata", "Confirm track metadata", f"Verify title, artist, BPM, key, mood tags, and notes for {title}."),
    ]

    if "metadata_description_missing" in issues:
        tasks.append(_task("metadata", "Write release description", "Add a short synthetic description for public demo reporting."))
    if not assets.get("cover_art"):
        tasks.append(_task("assets", "Create cover art", "Create or select approved artwork before release packaging."))
    if not assets.get("clean_mix"):
        tasks.append(_task("assets", "Export clean mix", "Confirm a clean mix exists before any distribution workflow."))
    if "streaming" in channels:
        tasks.append(_task("distribution", "Prepare streaming metadata", "Check title casing, artist naming, mood tags, and release copy."))
    if "short-form" in channels or "social-clips" in channels:
        tasks.append(_task("content", "Cut short-form clips", "Plan 2-3 short snippets around hook, intro, and mood."))
    if "newsletter" in channels:
        tasks.append(_task("content", "Draft newsletter blurb", "Write a short story/context note for fans or collaborators."))

    tasks.append(_task("review", "Run final human review", "Human approval required before any real release action."))
    return tasks
