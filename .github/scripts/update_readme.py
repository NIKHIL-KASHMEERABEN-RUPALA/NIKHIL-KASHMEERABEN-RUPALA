#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import random

repo_root = Path(__file__).resolve().parents[2]
readme_path = repo_root / "README.md"

start_marker = "<!-- AUTO_UPDATE:START -->"
end_marker = "<!-- AUTO_UPDATE:END -->"

quotes = [
    "Keeping the profile alive and refreshed.",
    "Maintaining a fresh pulse for the profile.",
    "Autonomous README refresh in progress.",
    "A small digital heartbeat for the profile page.",
    "Profile metadata refreshed for visibility.",
    "This README is being kept alive automatically.",
]

now = datetime.now(timezone.utc)
updated_at = now.strftime("%Y-%m-%d %H:%M:%S UTC")
note = random.choice(quotes)

block = f"""{start_marker}
## 🔄 README Auto-Refresh
- Last updated: {updated_at}
- Status: Active
- Schedule: Every 6 hours (UTC)
- Note: {note}
{end_marker}
"""

if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")

    if start_marker in content and end_marker in content:
        before, _ = content.split(start_marker)
        _, after = content.split(end_marker, 1)
        new_content = before + block + after.lstrip()
    else:
        new_content = content.rstrip() + "\n\n" + block + "\n"

    if new_content != content:
        readme_path.write_text(new_content, encoding="utf-8")
        print(f"README updated at {updated_at}")
    else:
        print("README already up to date.")
else:
    readme_path.write_text(block + "\n", encoding="utf-8")
    print(f"README created with auto-refresh block at {updated_at}")
