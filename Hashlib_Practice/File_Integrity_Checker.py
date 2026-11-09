import hashlib
from pathlib import Path

#Get path from user
path = Path(input("Enter File Path: "))

#Open file
with open(path, "rb") as file:
    content=file.read()
    #Convering each line to hash
    hash = hashlib.sha256(content)

print(hash.hexdigest())