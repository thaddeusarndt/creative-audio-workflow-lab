"""Track metadata normalization and validation for synthetic audio workflow demos."""

from __future__ import annotations

from typing import Any

REQUIRED_FIELDS = ["title", "artist", "bpm", "key", "duration_seconds", "mood_tags", "release_channels", "assets"]


def _title_case(value: Any) -> str:
    return str(value).strip().title()


def _normalize_tags(values: Any) -> list[str]:
    if not values:
        return []
    return sorted({str(value).strip().lower() for value in values if str(value).strip()})


def normalize_track(track: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized copy of a synthetic track metadata record."""
    normalized = dict(track)
    if "title" in normalized:
        normalized["title"] = _title_case(normalized["title"])
    if "artist" in normalized:
        normalized["artist"] = str(normalized["artist"]).strip()
    if "bpm" in normalized:
        normalized["bpm"] = int(normalized["bpm"])
    if "key" in normalized:
        key = str(normalized["key"]).strip()
        normalized["key"] = key[:1].upper() + key[1:].lower() if key else key
    if "duration_seconds" in normalized:
        normalized["duration_seconds"] = int(normalized["duration_seconds"])
    normalized["mood_tags"] = _normalize_tags(normalized.get("mood_tags", []))
    normalized["release_channels"] = _normalize_tags(normalized.get("release_channels", []))
    normalized["assets"] = dict(normalized.get("assets") or {})
    normalized["notes"] = str(normalized.get("notes", "")).strip()
    return normalized


def validate_track(track: dict[str, Any]) -> list[str]:
    """Return machine-readable issue codes for release-prep gaps."""
    issues: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in track or track[field] in (None, "", [], {}):
            issues.append(f"{field}_missing")

    bpm = track.get("bpm")
    if isinstance(bpm, int) and not 40 <= bpm <= 240:
        issues.append("bpm_out_of_range")

    if int(track.get("duration_seconds") or 0) <= 0:
        issues.append("duration_missing")

    assets = track.get("assets") or {}
    if not assets.get("cover_art"):
        issues.append("cover_art_missing")
    if not assets.get("clean_mix"):
        issues.append("clean_mix_missing")
    if not str(track.get("notes", "")).strip():
        issues.append("metadata_description_missing")

    return sorted(set(issues))
