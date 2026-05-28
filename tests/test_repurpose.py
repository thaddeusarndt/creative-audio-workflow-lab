from audio_workflow_lab.repurpose import build_repurpose_plan


def test_build_repurpose_plan_returns_channel_specific_prompts():
    track = {
        "title": "Midnight Sketch",
        "mood_tags": ["reflective", "warm"],
        "release_channels": ["newsletter", "short-form", "streaming"],
    }

    plan = build_repurpose_plan(track)

    channels = {item["channel"] for item in plan}
    assert channels == {"newsletter", "short-form", "streaming"}
    assert all("Midnight Sketch" in item["prompt"] for item in plan)
    assert all("synthetic" in item["safety_note"].lower() for item in plan)
