import requests
import json

url = "https://www.amazon.com/drive/v1/search/groups/c0DUWYbiQp-l29Y1XNeONw"
params = {
    "asset": "ALL",
    "filters": "type:(PHOTOS OR VIDEOS)",
    "limit": "200",
    "lowResThumbnail": "true",
    "searchContext": "groups",
    "sort": "['contentProperties.contentDate DESC']",
    "tempLink": "false",
    "timeZone": "America/Los_Angeles",
    "groupShareToken": "c0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB",
    "resourceVersion": "V2",
    "ContentType": "JSON"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, params=params, headers=headers)
print("Status:", resp.status_code)
if resp.status_code == 200:
    data = resp.json()
    print("Fetched items count:", data.get('count'))
    print("CORS Headers:")
    for k, v in resp.headers.items():
        if "access-control" in k.lower():
            print("  ", k, ":", v)

else:
    print(resp.text[:500])
