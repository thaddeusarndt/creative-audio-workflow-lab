# Workflow

1. Load synthetic track metadata from JSON.
2. Normalize casing, tags, BPM, and release channels.
3. Validate missing release-prep requirements.
4. Generate a release checklist.
5. Generate safe repurposing prompts for selected channels.
6. Render a markdown report for human review.

The demo is intentionally local and deterministic. It does not call model APIs, distribution services, social platforms, or file-hosting systems.
