import json

data = {
    "name": "Rahul",
    "language": "हिंदी"
}

json_string = json.dumps(
    data,
    ensure_ascii=False
)

json_bytes = json_string.encode("utf-8")

print(json_bytes)
print(type(json_bytes))