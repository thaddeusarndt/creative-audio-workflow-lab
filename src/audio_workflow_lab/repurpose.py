"""Channel-specific creative repurposing prompts for synthetic track metadata."""

from __future__ import annotations

from typing import Any

CHANNEL_GUIDANCE = {
    "streaming": "Write concise release copy and playlist tags without making unverifiable performance claims.",
    "short-form": "Generate short-form video caption ideas focused on mood, hook, and behind-the-scenes context.",
    "social-clips": "Generate short-form video caption ideas focused on mood, hook, and behind-the-scenes context.",
    "newsletter": "Draft a personal-but-brief note for subscribers about the creative direction.",
}


def build_repurpose_plan(track: dict[str, Any]) -> list[dict[str, str]]:
    """Return prompt-ready repurposing tasks for each requested channel."""
    title = track.get("title", "Untitled Track")
    moods = ", ".join(track.get("mood_tags", [])) or "unspecified mood"
    plan = []
    for channel in sorted(set(track.get("release_channels", []))):
        guidance = CHANNEL_GUIDANCE.get(channel, "Create a concise channel-specific content idea.")
        plan.append({
            "channel": channel,
            "prompt": f"For the synthetic track '{title}' with moods {moods}: {guidance}",
            "safety_note": "Use synthetic metadata only; do not reference real clients, private files, or copyrighted audio assets.",
        })
    return plan
