from audio_workflow_lab.release_plan import build_release_plan


def test_build_release_plan_creates_ordered_tasks_from_metadata_gaps():
    track = {
        "title": "Sunset Bounce",
        "artist": "Demo Artist",
        "release_channels": ["streaming", "social-clips"],
        "assets": {"cover_art": False, "clean_mix": True, "instrumental": True},
        "mood_tags": ["bright", "dance"],
        "notes": "Synthetic demo."
    }

    plan = build_release_plan(track)

    assert plan[0]["phase"] == "metadata"
    assert any(task["task"] == "Create cover art" for task in plan)
    assert any(task["task"] == "Cut short-form clips" for task in plan)
    assert all(task["status"] == "todo" for task in plan)
