import json
from datetime import datetime

#------------------------------------------------------------
#Datetime Format
data = {
    "date": datetime.now().isoformat()
}

json_data = json.dumps(data)

#Stored in string
print(f"Time = {json_data}\nType =  {type(json_data)}\n")

#------------------------------------------------------------
# Set
data = {
    "numbers": list({1, 2, 3, 4})
}

print(f"Set = {json.dumps(data)}\nType =  {type(json.dumps(data))}\n")

#------------------------------------------------------------
#Custom objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Rahul", 20)

data = student.__dict__

print(f"Custom Objects = {json.dumps(data)}\nType = {type(json.dumps(data))}")