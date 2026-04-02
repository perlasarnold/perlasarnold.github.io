import re
import json

with open("amazon.html", "r", encoding="utf-8") as f:
    content = f.read()

# look for var window.Drive = { ... } or something similar
match = re.search(r'bs\.Weblabs\s*=\s*(.*?});', content, re.DOTALL)
if match:
    # print head
    print("Found Weblabs")

# Let's search for the share details
share_match = re.search(r'shareId"\s*:\s*"([^"]+)"', content)
print("Share ID:", share_match.group(1) if share_match else None)

node_match = re.search(r'nodeId"\s*:\s*"([^"]+)"', content)
print("Node ID:", node_match.group(1) if node_match else None)

print("Endpoints:")
endpoints = set(re.findall(r'https://[^"]*?[/]v1/[^"]+', content))
for e in endpoints:
    print(e)
