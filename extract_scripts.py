from bs4 import BeautifulSoup
import json

with open("amazon.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

scripts = soup.find_all("script")
print(f"Found {len(scripts)} script tags")

for i, s in enumerate(scripts):
    content = s.string if s.string else ""
    if "c0DUWYbiQp-l29Y1XNeONw" in content or "c0DUWYbiQp" in content or "Y0iSRUBZHsJhWSOUngm5OB" in content:
        print(f"Script {i} contains the share link details. Length: {len(content)}")
        with open(f"script_{i}.js", "w", encoding="utf-8") as out:
            out.write(content)
