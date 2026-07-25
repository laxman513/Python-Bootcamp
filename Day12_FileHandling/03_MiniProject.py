"""
==========================================================
Day 12 - File Handling
03_MiniProject.py

Student Record Management System
==========================================================
"""


FILE_NAME = "students.txt"


# ==========================================================
# Add Student
# ==========================================================

def add_student():

    name = input("Enter Student Name : ")

    with open(FILE_NAME, "a") as file:

        file.write(name + "\n")

    print("Student Added Successfully.")


# ==========================================================
# View Students
# ==========================================================

def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()

        if len(students) == 0:

            print("No Student Records Found.")

            return

        print("\nStudent List")
        print("-" * 30)

        for index, student in enumerate(students, start=1):

            print(index, ".", student.strip())

    except FileNotFoundError:

        print("No Student Records Found.")


# ==========================================================
# Search Student
# ==========================================================

def search_student():

    name = input("Enter Student Name : ")

    try:

        with open(FILE_NAME, "r") as file:

            students = file.read()

        if name.lower() in students.lower():

            print("Student Found.")

        else:

            print("Student Not Found.")

    except FileNotFoundError:

        print("No Student Records Found.")


# ==========================================================
# Delete Student
# ==========================================================

def delete_student():

    name = input("Enter Student Name : ")

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:

            for student in students:

                if student.strip().lower() != name.lower():

                    file.write(student)

                else:

                    found = True

        if found:

            print("Student Deleted Successfully.")

        else:

            print("Student Not Found.")

    except FileNotFoundError:

        print("No Student Records Found.")


# ==========================================================
# Count Students
# ==========================================================

def count_students():

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()

        print("Total Students :", len(students))

    except FileNotFoundError:

        print("Total Students : 0")


# ==========================================================
# Menu
# ==========================================================

while True:

    print("\n")
    print("=" * 45)
    print(" STUDENT RECORD MANAGEMENT SYSTEM ")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Count Students")
    print("6. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        count_students()

    elif choice == "6":

        print("Thank You...")

        break

    else:

        print("Invalid Choice")