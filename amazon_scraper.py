import os
import requests
import json

def fetch_amazon_photos():
    url = "https://www.amazon.com/drive/v1/search/groups/c0DUWYbiQp-l29Y1XNeONw"
    params = {
        "asset": "ALL",
        "filters": "type:(PHOTOS OR VIDEOS)",
        "limit": "200",
        "lowResThumbnail": "true",
        "searchContext": "groups",
        "sort": "['contentProperties.contentDate DESC']",
        "tempLink": "true",
        "timeZone": "America/Los_Angeles",
        "groupShareToken": "c0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB",
        "resourceVersion": "V2",
        "ContentType": "JSON"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        print("Fetching images from Amazon Photos...")
        resp = requests.get(url, params=params, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        
        # Inject the correct image download URL for hotlinking and strip PII
        if 'data' in data:
            clean_data = []
            for item in data['data']:
                node_id = item.get('id')
                owner_id = item.get('ownerId')
                if node_id and owner_id:
                    # Construct hotlink URL for 1024px viewBox
                    image_url = f"https://thumbnails-photos.amazon.com/v1/thumbnail/{node_id}?viewBox=1024&ownerId={owner_id}&groupShareToken={params['groupShareToken']}"
                    
                    # Aggressively filter out PII (owner IDs, geolocation, etc), keeping only public display fields
                    clean_item = {
                        "id": node_id,
                        "name": item.get("name", "Photo"),
                        "imageUrl": image_url,
                        "contentProperties": {
                            "image": {}
                        }
                    }
                    
                    # Safely extract safe display info if it exists
                    img_props = item.get("contentProperties", {}).get("image", {})
                    for prop in ["make", "model", "focalLength", "apertureValue", "exposureTime", "dateTimeOriginal"]:
                        if prop in img_props:
                            clean_item["contentProperties"]["image"][prop] = img_props[prop]
                            
                    clean_data.append(clean_item)
            
            data['data'] = clean_data
            if 'aggregations' in data:
                del data['aggregations'] # Prevents leaking Amazon Group IDs
        
        # Ensure _data directory exists
        os.makedirs("_data", exist_ok=True)
        
        output_file = os.path.join("_data", "photos.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print(f"Successfully saved {data.get('count', 0)} photos to {output_file}")
    except Exception as e:
        print(f"Failed to fetch photos: {e}")

if __name__ == "__main__":
    fetch_amazon_photos()
