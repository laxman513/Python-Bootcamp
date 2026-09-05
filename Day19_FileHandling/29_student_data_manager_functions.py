from pathlib import Path
import json

STUDENT_FILE = Path("student_data") / "students.json"

def load_students():
    try:
        with open(STUDENT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_student(students):
    with open(STUDENT_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def add_student(students, student):
    students.append(student)
    save_student(students)

    print("Student added succssfully.")

def list_students(students):
    if not students:
        print("No Students found")
        return
    
    print("\nStudent list")

    for student in students:
        print(
            f"{student['id']} - "
            f"{student['name']} - "
            f"{student['age']} - "
            f"{student['marks']}"
        )

def search_student(students, name):
    found = False

    for student in students:
        if(student["name"].lower() == name.lower()):
            print("search student:\n")
            print(
                f"{student['id']} - "
                f"{student['name']} - "
                f"{student['age']} - "
                f"{student['marks']}"
            )
            found = True

        if not found:
               print("Student not found.")

students = load_students()

student = {
    "id": 1,
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

add_student(students, student)

list_students(students)

search_student(students, "Rahul")


