import json

data = {
    "name": "Vik",
    "age": 20,
    "percentage": 89.5,
    "subjects": ["Python", "CPP"],
    "is_student": True,
    "is_employed": False,
    "address": None
}

json_data = json.dumps(data, indent=4)

print(json_data)
print(type(json_data))

python_data = json.loads(json_data)

print(python_data)
print(type(python_data))