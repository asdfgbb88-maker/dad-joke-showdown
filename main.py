from pathlib import Path

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(
    "I confronted my shadow for following me. It just copies my every move.",
    encoding="utf-8",
)
