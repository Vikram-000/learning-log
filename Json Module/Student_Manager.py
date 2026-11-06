import json 

stud_data = {
    "S1" : {
        "Name": "Vik",
        "age": 20,
        "Grade": "A",
        "Subject" : ["Python", "CPP", "OOP"]
    },
    "S2" : {
        "Name": "Vik2",
        "age": 19,
        "Grade": "B",
        "Subject" : ["Python", "CPP", "OOP"]
    },
    "S3" : {
        "Name": "Vik3",
        "age": 18,
        "Grade": "C",
        "Subject" : ["Python", "CPP", "OOP"]
    }
}

stud = json.dumps(stud_data)
print(f"Json: {stud} \n Type: {type(stud)}")

with open("stud.json", "w+") as file:
    json.dump(stud_data, file)
    file.seek(0)
    loaded_stud = json.load(file)
    print(f"Json: {loaded_stud} \n Type: {type(loaded_stud)}")

stud = json.loads(stud)
print(f"Json: {stud} \n Type: {type(stud)}")
