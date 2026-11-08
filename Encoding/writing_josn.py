import json

data = {
    "name": "Rahul",
    "city": "कोल्हापुर"
}

with open("Encoding/data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)