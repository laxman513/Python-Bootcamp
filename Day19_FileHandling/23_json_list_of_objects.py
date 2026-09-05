import json

students = [
    {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    {
        "name": "Priya",
        "age": 21,
        "marks": 92
    },
    {
        "name": "Arjun",
        "age": 19,
        "marks": 78
    }
]

# Write JSON
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("Students json file created")

# Read JSON
with open("students.json", "r", encoding="utf-8") as file:

    data = json.load(file)

print("\nStudent Data:")

for student in data:
    print(
        f"Name: {student["name"]} - "
        f"Age: {student["age"]} - "
        f"Marks: {student["marks"]}"
    )


