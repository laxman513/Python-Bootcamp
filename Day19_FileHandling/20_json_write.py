import json

student = {
    "name": "Laxman",
    "age": 45,
    "marks": 95
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)


print("JSON file created successfully.")