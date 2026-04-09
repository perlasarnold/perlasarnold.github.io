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
# Format: ("YYYY-MM-DD", "YYYY-MM-DD", [tags])
# Matches any photo whose EXIF date falls within the range (inclusive).
DATE_RULES = [
    # Venice trip — March 2018 Showcase-Square shots
    ("2018-03-01", "2018-03-31", ["city", "travel"]),
    # Philippines / Mount Pinatubo — August 2011 Showcase
    ("2011-08-01", "2011-08-31", ["nature", "travel"]),
]

LOCATION_FILENAME_RULES = [
    (re.compile(r"HuntingtonLib", re.I), "Huntington Library, San Marino, CA"),
    (re.compile(r"DisneyGators", re.I), "Gatorland, Orlando, FL"),
    (re.compile(r"Disney", re.I), "Walt Disney World Resort, FL"),
]
LOCATION_DATE_RULES = [
    # Explicit dates (must come first so they take precedence over general month-wide fallbacks)
    ("2016-12-15", "2016-12-15", "Mount Pinatubo, Philippines"),
    ("2017-01-28", "2017-01-28", "Grand Canyon, Arizona"),
    ("2017-12-28", "2018-01-04", "New York City, NY"),
    
    ("2018-03-24", "2018-03-25", "Venice, Italy"),
    ("2018-03-26", "2018-03-26", "Giverny, France"),
    ("2018-03-28", "2018-03-29", "Paris, France"),
    
    ("2018-11-08", "2018-11-08", "Keystone, South Dakota"),
    ("2019-05-04", "2019-05-04", "Lake Tahoe, CA"),
    ("2020-11-21", "2020-11-22", "Mammoth Lakes, CA"),
    
    ("2021-03-30", "2021-03-30", "Durham, North Carolina"),
    ("2021-03-31", "2021-03-31", "Atlanta, Georgia"),
    ("2021-04-01", "2021-04-01", "Nashville, Tennesee"),
    ("2021-08-18", "2021-08-18", "Laguna Beach, CA"),
    ("2021-12-25", "2021-12-26", "Yosemite, CA"),

    ("2022-02-06", "2022-02-06", "Antipolo, Rizal, Philippines"),
    ("2022-06-10", "2022-06-12", "Banff, Alberta, Canada"),
    
    ("2023-03-15", "2023-03-15", "Pirámide del Sol, Mexico"),
    ("2023-03-16", "2023-03-17", "Mexico City, Mexico"),

    ("2023-05-26", "2023-05-27", "Antigua, Guatemala"),
    ("2023-05-28", "2023-05-28", "Santiago Atitlán, Guatemala"),
    ("2023-05-29", "2023-05-29", "Tikal, Guatemala"),
    ("2023-05-30", "2023-05-30", "Antigua, Guatemala"),
    
    ("2023-06-03", "2023-06-03", "Natural History Museum, Los Angeles, CA"),

    ("2023-12-26", "2023-12-26", "Bryce Canyon, Utah"),
    ("2023-12-27", "2023-12-27", "Zion National Park, Utah"),

    ("2024-03-01", "2024-03-03", "Cartagena, Bolivar, Colombia"),
    ("2024-03-04", "2024-03-05", "Salento, Quindio, Colombia"),
    ("2024-03-06", "2024-03-06", "Bogotá, Bogota, Colombia"),

    ("2024-03-24", "2024-03-24", "Irvine, CA"),
    ("2024-04-06", "2024-04-06", "Irvine, CA"),

    ("2024-04-07", "2024-04-07", "Pasadena, CA"),
    ("2024-04-17", "2024-04-17", "Irvine, CA"),
    
    ("2024-05-08", "2024-05-08", "Bari, Italy"),
   
    ("2024-05-10", "2024-05-13", "Rome, Italy"),
    ("2024-05-14", "2024-05-14", "Pisa, Italy"),
    ("2024-05-15", "2024-05-15", "Milan, Italy"),
    ("2024-05-16", "2024-05-16", "Walenstadt, Switzerland"),
    ("2024-05-17", "2024-05-17", "Lucerne, Switzerland"),
    ("2024-05-18", "2024-05-18", "Engelberg, Switzerland"),
    ("2024-05-18", "2024-05-18", "Amsterdam, Netherlands"),
    ("2024-05-19", "2024-05-20", "Fiumucuno, Italy"),


    
    ("2024-06-29", "2024-06-29", "Morro Bay, CA"),
    
    ("2024-07-19", "2024-07-20", "Grand Canyon, Arizona"),
    ("2024-07-21", "2024-07-21", "Colorado Springs, Colorado"),
    ("2024-10-31", "2024-10-31", "Old Towne Orange, CA"),
    
    ("2025-03-16", "2025-03-16", "Edinburgh, United Kingdom"),
    ("2025-03-17", "2025-03-17", "Scottish Highlands, United Kingdom"),
    ("2025-03-18", "2025-03-18", "Edinburgh, United Kingdom"),
    ("2025-03-19", "2025-03-19", "Cotswolds, United Kingdom"),
    ("2025-03-20", "2025-03-20", "Oxford, United Kingdom"),
    ("2025-03-21", "2025-03-21", "London, United Kingdom"),
    ("2025-03-22", "2025-03-22", "Wales, United Kingdom"),
    ("2025-03-23", "2025-03-23", "London, United Kingdom"),
    
    ("2025-07-19", "2025-07-19", "Huntington Library, San Marino, CA"),
    
    ("2025-07-26", "2025-07-26", "Carbon Canyon Regional Park, Brea, CA"),
    ("2025-10-26", "2025-10-26", "Downtown Los Angeles, CA"),
    
    ("2025-12-20", "2025-12-21", "Nassau, Bahamas"),
    ("2025-12-23", "2025-12-23", "EPCOT, Walt Disney World Resort, FL"),
    ("2025-12-24", "2025-12-24", "Kennedy Space Center, Merritt Island, FL"),
    ("2025-12-25", "2025-12-25", "EPCOT, Walt Disney World Resort, FL"),
    ("2025-12-26", "2025-12-26", "Gatorland, Orlando, FL"),
    
    ("2026-01-31", "2026-02-01", "La Fortuna, Costa Rica"),
    ("2026-02-02", "2026-02-02", "Tenorio Volcano National Park, Costa Rica"),
    ("2026-02-28", "2026-02-28", "North Back Bay Trail, Newport Beach, CA"),
    
    ("2026-03-15", "2026-03-15", "Huntington Library, San Marino, CA"),
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
    ymd   = date[:10] if date else ""         # "YYYY-MM-DD"
    tags  = []
    loc   = ""

    # 1. Subject Tags
    for pattern, assigned_tags in FILENAME_RULES:
        if pattern.search(name):
            tags = assigned_tags
            break
    if not tags and ymd:
        for date_from, date_to, assigned_tags in DATE_RULES:
            if date_from <= ymd <= date_to:
                tags = assigned_tags
                break
    result[photo["id"]] = tags

    # 2. Location Tags
    for pattern, assigned_loc in LOCATION_FILENAME_RULES:
        if pattern.search(name):
            loc = assigned_loc
            break
    if not loc and ymd:
        for date_from, date_to, assigned_loc in LOCATION_DATE_RULES:
            if date_from <= ymd <= date_to:
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
