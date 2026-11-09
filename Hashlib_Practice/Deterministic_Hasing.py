import hashlib
import json

data1 = {
    "name": "Alice",
    "age": 25,
    "status": "active"
}

data2 = {
    "status": "active",
    "age": 25,
    "name": "Alice"
}

json_data1 = json.dumps(data1, sort_keys=True, separators=(",", ":"))
json_data2 = json.dumps(data2, sort_keys=True, separators=(",", ":"))

hash_a = hashlib.sha256(json_data1.encode())
hash_b = hashlib.sha256(json_data2.encode())

flag = hash_a.hexdigest() == hash_b.hexdigest()

print(f"Are hashes identical?: {flag}")