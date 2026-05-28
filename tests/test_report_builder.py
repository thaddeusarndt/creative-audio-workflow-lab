from audio_workflow_lab.report_builder import render_track_report


def test_render_track_report_includes_safety_banner_and_plan_sections():
    track = {
        "title": "Midnight Sketch",
        "artist": "Demo Artist",
        "bpm": 92,
        "key": "A minor",
        "duration_seconds": 146,
        "mood_tags": ["reflective", "warm"],
        "release_channels": ["streaming"],
        "assets": {"cover_art": True, "clean_mix": True},
        "notes": "Synthetic demo metadata only."
    }

    report = render_track_report(track)

    assert report.startswith("# Creative Audio Workflow Report")
    assert "Clean-room demo" in report
    assert "## Release Checklist" in report
    assert "## Repurposing Prompts" in report
    assert "Midnight Sketch" in report
