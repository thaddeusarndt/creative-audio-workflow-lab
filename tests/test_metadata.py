from audio_workflow_lab.metadata import normalize_track, validate_track


def test_normalize_track_trims_strings_and_sorts_tags():
    track = {
        "title": "  midnight sketch  ",
        "artist": " Demo Artist ",
        "bpm": "92",
        "key": "a minor",
        "duration_seconds": 146,
        "mood_tags": ["warm", "reflective", "warm"],
        "release_channels": ["streaming"],
        "assets": {"cover_art": True, "clean_mix": True},
    }

    normalized = normalize_track(track)

    assert normalized["title"] == "Midnight Sketch"
    assert normalized["artist"] == "Demo Artist"
    assert normalized["bpm"] == 92
    assert normalized["key"] == "A minor"
    assert normalized["mood_tags"] == ["reflective", "warm"]


def test_validate_track_reports_missing_release_requirements():
    track = normalize_track({
        "title": "Sunset Bounce",
        "artist": "Demo Artist",
        "bpm": 118,
        "key": "C major",
        "duration_seconds": 181,
        "mood_tags": ["bright"],
        "release_channels": ["streaming"],
        "assets": {"cover_art": False, "clean_mix": True},
    })

    issues = validate_track(track)

    assert "cover_art_missing" in issues
    assert "metadata_description_missing" in issues
