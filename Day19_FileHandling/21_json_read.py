import json

with open("student.json", "r", encoding="utf-8") as file:

    student = json.load(file)

    print("Student Name:", student['name'])
    print("Student Age:", student['age'])
    print("Student Marks:", student["marks"])