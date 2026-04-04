"""
Generates _data/photo_tags.json mapping each photo ID to a list of tags.
Tags are descriptive subject labels — never raw filenames.

Two rule types are supported — the first matching rule wins:
  FILENAME_RULES : (regex pattern matched against filename, [tags])
  DATE_RULES     : ((date_from, date_to) YYYY-MM range, [tags])
                   Matches photos whose EXIF dateTimeOriginal falls in range.
"""
import json, re, os

# ── Filename-based rules ────────────────────────────────────────────────────
FILENAME_RULES = [
    # Costa Rica trips (covers both spelling variants in filenames)
    (re.compile(r"CostaRica|CosaRica",  re.I), ["nature", "travel"]),
    # Huntington Library & Gardens — gardens = nature
    (re.compile(r"HuntingtonLib",       re.I), ["nature"]),
    # Disney + Gators shoot — gators = nature
    (re.compile(r"DisneyGators",        re.I), ["nature", "travel"]),
    # Add new filename-prefix rules here, e.g.:
    # (re.compile(r"CityShoot|Downtown", re.I), ["city"]),
]

# ── Date-range rules ────────────────────────────────────────────────────────
# Format: ("YYYY-MM-from", "YYYY-MM-to", [tags])
# Matches any photo whose EXIF date falls within the month range (inclusive).
DATE_RULES = [
    # Venice trip — March 2018 Showcase-Square shots
    ("2018-03", "2018-03", ["city", "travel"]),
    # Add more date-range rules here as you identify other trips, e.g.:
    # ("2024-03", "2024-03", ["city", "travel"]),
]

# ───────────────────────────────────────────────────────────────────────────
src  = os.path.join(os.path.dirname(__file__), "_data", "photos.json")
dest = os.path.join(os.path.dirname(__file__), "_data", "photo_tags.json")

with open(src, encoding="utf-8") as f:
    photos = json.load(f)["data"]

result = {}
for photo in photos:
    name  = photo.get("name", "")
    img   = photo.get("contentProperties", {}).get("image", {})
    date  = img.get("dateTimeOriginal", "")  # e.g. "2018-03-24T00:23:12.000Z"
    ym    = date[:7] if date else ""          # "YYYY-MM"
    tags  = []

    # 1. Try filename rules first
    for pattern, assigned_tags in FILENAME_RULES:
        if pattern.search(name):
            tags = assigned_tags
            break

    # 2. Fall back to date-range rules if no filename rule matched
    if not tags and ym:
        for date_from, date_to, assigned_tags in DATE_RULES:
            if date_from <= ym <= date_to:
                tags = assigned_tags
                break

    result[photo["id"]] = tags

with open(dest, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print(f"Written {len(result)} entries to {dest}")
tag_counts = {}
for tags in result.values():
    for t in tags:
        tag_counts[t] = tag_counts.get(t, 0) + 1
print("Tag distribution:", tag_counts)
