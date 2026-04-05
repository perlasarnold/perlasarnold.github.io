import json

with open('_data/photos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

missing = []
for item in data['data']:
    img = item.get('contentProperties', {}).get('image', {})
    missing_fields = [f for f in ['make', 'model', 'focalLength', 'apertureValue', 'exposureTime', 'dateTimeOriginal'] if f not in img]
    if missing_fields:
        missing.append({'id': item['id'], 'name': item['name'], 'missing': missing_fields, 'has': list(img.keys())})

lines = []
lines.append(f"Total photos: {data['count']}")
lines.append(f"Photos missing metadata: {len(missing)}")
lines.append("")
for m in missing:
    lines.append(f"  {m['name']} ({m['id']})")
    lines.append(f"    Missing: {m['missing']}")
    lines.append(f"    Has: {m['has']}")
    lines.append("")

with open('audit_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Done. See audit_output.txt")
