"""CLI entrypoint for generating synthetic creative audio workflow reports."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .report_builder import render_track_report


def slugify(value: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    return re.sub(r"-+", "-", slug).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate reports from synthetic track metadata.")
    parser.add_argument("--input", default="examples/synthetic_tracks.json", help="Path to synthetic track metadata JSON.")
    parser.add_argument("--output-dir", default="reports/generated", help="Directory for markdown reports.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    tracks = json.loads(input_path.read_text())
    for track in tracks:
        report = render_track_report(track)
        title = track.get("title", "untitled-track")
        path = output_dir / f"{slugify(title)}_report.md"
        path.write_text(report)
        print(path)


if __name__ == "__main__":
    main()
