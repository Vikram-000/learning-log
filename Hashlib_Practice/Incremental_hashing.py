import hashlib
from pathlib import Path

try:
    #Get File Path from user 
    path = Path(input("Enter File Path: "))

    #Generate hashing object
    hash_sha256 = hashlib.new("sha256")

    #Read and update hash line by line
    with open(path, "rb") as file:
        for line in file:
            hash_sha256.update(line)

    print(hash_sha256.hexdigest())

except FileNotFoundError:
    print("File not found, enter correct path")
except Exception as e:
    print(f"Something went wrong: {e}")