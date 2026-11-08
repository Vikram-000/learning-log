import json

data = "{'name': 'Alex'}"

try:
    result = json.loads(data)
    print(result)

except json.JSONDecodeError:
    print("Invalid JSON format!")



from datetime import datetime

data = {
    "name": "Alex",
    "date": datetime.now()
}

try:
    result = json.dumps(data)
    print(result)

except TypeError:
    print("Cannot serialize this data!")



data = "{invalid json}"

try:
    result = json.loads(data)

except json.JSONDecodeError:
    print("JSON format is incorrect!")

except TypeError:
    print("Invalid data type!")

except Exception as e:
    print("Unexpected error:", e)