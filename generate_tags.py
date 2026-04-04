"""
Generates _data/photo_tags.json mapping each photo ID to a list of tags.
Tags are descriptive subject labels — never raw filenames.

Edit the RULES list below to add or change tag assignments, then re-run.
Each rule is (regex pattern, [tags]). The first matching rule wins.
"""
import json, re, os

RULES = [
    # (filename pattern, tags to assign)
    # Costa Rica trips (covers both spelling variants in filenames)
    (re.compile(r"CostaRica|CosaRica",  re.I), ["wildlife", "nature", "travel"]),
    # Huntington Library & Gardens — primarily a botanical garden
    (re.compile(r"HuntingtonLib",       re.I), ["botanical"]),
    # Disney + Gators shoot
    (re.compile(r"DisneyGators",        re.I), ["wildlife", "travel"]),
    # Add new album rules here, e.g.:
    # (re.compile(r"^AMP",              re.I), ["street"]),
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
