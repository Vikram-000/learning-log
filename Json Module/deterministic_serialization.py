import json

data = {
    "name": "Alex",
    "age": 22,
    "city": "Pune"
}

result = json.dumps(
    data,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=False
)

print(result)