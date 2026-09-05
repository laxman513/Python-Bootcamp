from pathlib import Path
import json


STUDENT_FILE = Path("data") / "students.json"


def load_students():
    try:
        with open(STUDENT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Student data file contains invalid JSON.")
        return []


def save_students(students):
    STUDENT_FILE.parent.mkdir(exist_ok=True)

    with open(STUDENT_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def get_next_id(students):
    if not students:
        return 1

    return max(student["id"] for student in students) + 1


def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

    except ValueError:
        print("Age and marks must be numeric.")
        return

    student = {
        "id": get_next_id(students),
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


def list_students(students):
    if not students:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )


def search_student(students):
    name = input("Enter student name to search: ").strip()

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found:")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

            found = True

    if not found:
        print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Data Manager =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            list_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            print("Exiting Student Data Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()