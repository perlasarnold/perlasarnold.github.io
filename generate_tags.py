"""
Generates _data/photo_tags.json mapping each photo ID to a list of tags.
Tags are descriptive subject labels — never raw filenames.

Edit the RULES dict below to customize tag assignments, then re-run.
"""
import json, re, os

RULES = [
    # (filename pattern, tags to assign)
    (re.compile(r"CostaRica|CosaRica", re.I), ["wildlife", "travel", "nature"]),
    (re.compile(r"HuntingtonLib",        re.I), ["botanical", "architecture"]),
    # AMP = author's name initials, intentionally left untagged so they appear in "All"
    # but can be given tags here once you know the subject:
    # (re.compile(r"^AMP", re.I), ["street", "urban"]),
]

src  = os.path.join(os.path.dirname(__file__), "_data", "photos.json")
dest = os.path.join(os.path.dirname(__file__), "_data", "photo_tags.json")

with open(src, encoding="utf-8") as f:
    photos = json.load(f)["data"]

result = {}
for photo in photos:
    name = photo.get("name", "")
    tags = []
    for pattern, assigned_tags in RULES:
        if pattern.search(name):
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
