
student = {
    "name": "Thomas Morelli",
    "age": 20,
    "major": "MIS Major",
    "hobbies": ["Pickleball", "Church", "Fortnite"]
}


student["State"] = "Texas"


student["age"] += 1


for key, value in student.items():
    print(f"{key.capitalize()}: {value}")