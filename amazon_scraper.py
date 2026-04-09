import os
import requests
import json
import re

def fetch_amazon_photos():
    base_url = "https://www.amazon.com/drive/v1/search/groups/c0DUWYbiQp-l29Y1XNeONw"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    all_clean_data = []
    total_count = None
    offset = 0
    limit = 200

    try:
        print("Fetching images from Amazon Photos...")
        while True:
            params = {
                "asset": "ALL",
                "filters": "type:(PHOTOS OR VIDEOS)",
                "limit": str(limit),
                "offset": str(offset),
                "lowResThumbnail": "true",
                "searchContext": "groups",
                "sort": "['contentProperties.contentDate DESC']",
                "tempLink": "true",
                "timeZone": "America/Los_Angeles",
                "groupShareToken": "c0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB",
                "resourceVersion": "V2",
                "ContentType": "JSON"
            }
            
            resp = requests.get(base_url, params=params, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            
            if total_count is None:
                total_count = data.get('count', 0)
            
            items = data.get('data', [])
            if not items:
                break
                
            for item in items:
                node_id = item.get('id')
                owner_id = item.get('ownerId')
                if node_id and owner_id:
                    image_url = f"https://thumbnails-photos.amazon.com/v1/thumbnail/{node_id}?viewBox=512&ownerId={owner_id}&groupShareToken={params['groupShareToken']}"
                    
                    clean_item = {
                        "id": node_id,
                        "name": item.get("name", "Photo"),
                        "imageUrl": image_url,
                        "contentProperties": {
                            "image": {}
                        }
                    }
                    
                    img_props = item.get("contentProperties", {}).get("image", {})
                    for prop in ["make", "model", "focalLength", "apertureValue", "exposureTime", "dateTimeOriginal"]:
                        if prop in img_props:
                            clean_item["contentProperties"]["image"][prop] = img_props[prop]
                    
                    # Fallback: if no date, try to extract from filename (e.g. IMG_20240417_...)
                    if not clean_item["contentProperties"]["image"].get("dateTimeOriginal"):
                        # Look for YYYYMMDD pattern like IMG_20240417_
                        match = re.search(r"(\d{4})(\d{2})(\d{2})", clean_item["name"])
                        if match:
                            y, m, d = match.groups()
                            clean_item["contentProperties"]["image"]["dateTimeOriginal"] = f"{y}-{m}-{d}T12:00:00.000Z"
                            
                    all_clean_data.append(clean_item)
                    
            offset += len(items)
            print(f"Fetched {offset} / {total_count}")
            
            if offset >= total_count:
                break

        # ── Apply manual metadata overrides ───────────────────────────────────
        overrides_file = os.path.join("_data", "metadata_overrides.json")
        if os.path.exists(overrides_file):
            with open(overrides_file, "r", encoding="utf-8") as f:
                overrides = json.load(f)
            applied = 0
            for item in all_clean_data:
                node_id = item["id"]
                if node_id in overrides:
                    override = overrides[node_id]
                    img = item["contentProperties"]["image"]
                    for field, value in override.items():
                        if field.startswith("_"):   # skip _name and other internal keys
                            continue
                        # Apply value regardless of whether it's empty (allows clearing)
                        img[field] = value
                    applied += 1
            print(f"Applied metadata overrides to {applied} photo(s).")
        # ─────────────────────────────────────────────────────────────────────

        final_data = {
            "count": len(all_clean_data),
            "data": all_clean_data
        }
        
        os.makedirs("_data", exist_ok=True)
        output_file = os.path.join("_data", "photos.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(final_data, f, indent=4)
        
        print(f"Successfully saved {len(all_clean_data)} photos to {output_file}")
    except Exception as e:
        print(f"Failed to fetch photos: {e}")

if __name__ == "__main__":
    fetch_amazon_photos()
