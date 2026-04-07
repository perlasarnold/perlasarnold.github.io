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
    # Philippines / Mount Pinatubo — August 2011 Showcase
    ("2011-08", "2011-08", ["nature", "travel"]),
]

# ── Location rules ─────────────────────────────────────────────────────────
LOCATION_FILENAME_RULES = [
    (re.compile(r"CostaRica|CosaRica", re.I), "Costa Rica"),
    (re.compile(r"HuntingtonLib", re.I), "Huntington Library, CA"),
    (re.compile(r"Disney", re.I), "Disney, FL"),
]

LOCATION_DATE_RULES = [
    ("2018-03", "2018-03", "Venice, Italy"),
    ("2011-08", "2011-08", "Laguna Beach"),
    ("2016-12", "2016-12", "Mount Pinatubo"),
    ("2017-01", "2017-01", "Grand Canyon"),
]

# ───────────────────────────────────────────────────────────────────────────
src  = os.path.join(os.path.dirname(__file__), "_data", "photos.json")
dest = os.path.join(os.path.dirname(__file__), "_data", "photo_tags.json")
loc_dest = os.path.join(os.path.dirname(__file__), "_data", "photo_locations.json")


with open(src, encoding="utf-8") as f:
    photos = json.load(f)["data"]

result = {}
loc_result = {}

for photo in photos:
    name  = photo.get("name", "")
    img   = photo.get("contentProperties", {}).get("image", {})
    date  = img.get("dateTimeOriginal", "")  # e.g. "2018-03-24T00:23:12.000Z"
    ym    = date[:7] if date else ""          # "YYYY-MM"
    tags  = []
    loc   = ""

    # 1. Subject Tags
    for pattern, assigned_tags in FILENAME_RULES:
        if pattern.search(name):
            tags = assigned_tags
            break
    if not tags and ym:
        for date_from, date_to, assigned_tags in DATE_RULES:
            if date_from <= ym <= date_to:
                tags = assigned_tags
                break
    result[photo["id"]] = tags

    # 2. Location Tags
    for pattern, assigned_loc in LOCATION_FILENAME_RULES:
        if pattern.search(name):
            loc = assigned_loc
            break
    if not loc and ym:
        for date_from, date_to, assigned_loc in LOCATION_DATE_RULES:
            if date_from <= ym <= date_to:
                loc = assigned_loc
                break
    if loc:
        loc_result[photo["id"]] = loc

with open(dest, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

with open(loc_dest, "w", encoding="utf-8") as f:
    json.dump(loc_result, f, indent=2)

print(f"Written {len(result)} entries to {dest}")
tag_counts = {}
for tags in result.values():
    for t in tags:
        tag_counts[t] = tag_counts.get(t, 0) + 1
print("Tag distribution:", tag_counts)
