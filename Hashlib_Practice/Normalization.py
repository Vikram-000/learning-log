import hashlib
import json 
from pathlib import Path

def normalize(event_a_path, event_b_path):
        # Load Json Files 
        with open(event_a_path, "r", encoding="utf-8") as file:
            data_a = json.load(file)
            data_a.pop("execution_id", None)
            data_a.pop("timestamp", None)
        with open(event_b_path, "r", encoding="utf-8") as file:
            data_b = json.load(file)
            data_b.pop("execution_id", None)
            data_b.pop("timestamp", None)
        return data_a, data_b

try:
    # Get Path from User
    event_a_path = Path(input("Enter event A path: "))
    event_b_path = Path(input("Enter event B path: "))

    # Getting data from normalize function 
    data_a, data_b = normalize(event_a_path, event_b_path)

    #Converting to json and encoding python objects
    json_data_a = json.dumps(data_a, sort_keys=True, separators=(",",":")).encode()
    json_data_b = json.dumps(data_b, sort_keys=True, separators=(",",":")).encode()

    # Converting json objects to hash using sha256
    hash_A = hashlib.sha256(json_data_a)
    hash_B = hashlib.sha256(json_data_b)

    # Comparing hashes of both files  
    if hash_A.digest() == hash_B.digest():
        print("Both json content are same")
    else:
        print("Both json content are not same")

except FileNotFoundError:
    print("Can't find the files required")

except json.JSONDecodeError:
    print("Invalid JSON file")

except Exception as e:
    print(f"Error: {e}")