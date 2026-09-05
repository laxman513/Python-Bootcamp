import json

student = {
    "name": "Rahul",
    "age": 20,
    "address": {
        "city": "Hyderabad",
        "state": "Telangana"
    },
    "subjects": [
        "Python",
        "Math",
        "Science"
    ]
}

# Write JSON
with open("student_details.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Students details JSON created")

with open("student_details.json", "r", encoding="utf-8") as file:
    student_details = json.load(file)

print("Name:", student_details["name"])
print("City:", student_details["address"]["city"])
print("State:", student_details["address"]["state"])
print("First Subject:", student_details["subjects"][0])
