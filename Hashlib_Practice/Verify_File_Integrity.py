import hashlib
from pathlib import Path

try:
    #Take Path and Expected Hash from user
    path = Path(input("Enter File Path: "))
    excepted_hash = input("Enter Expected Hash: ").strip()

    #Calculate hash of file 
    with open(path,"rb") as file:
        content = file.read()
        hash_sha256 = hashlib.sha256(content)

    #Check if expected hash matches the actual hash of the file
    if (hash_sha256.hexdigest() == excepted_hash):
        print("File is authentic. Hashes match!")
    else:
        print("WARNING! File integrity check failed!")

except FileNotFoundError:
    print("File not found, enter correct path")
except Exception as e:
    print(f"Something went wrong: {e}")