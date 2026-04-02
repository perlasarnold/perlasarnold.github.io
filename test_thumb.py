import requests

url = "https://www.amazon.com/drive/v1/nodes/rTWVU0QlQJe1jlhN2-Uw-w"
params = {
    "groupShareToken": "c0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB",
    "tempLink": "true",
    "resourceVersion": "V2",
    "ContentType": "JSON"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.amazon.com/"
}

r = requests.get(url, params=params, headers=headers)
print("Status Code:", r.status_code)
if r.status_code == 200:
    print(r.json().get("tempLink", "No temp link found"))
else:
    print(r.text)
