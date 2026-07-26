FILE_NAME = "students_exp.txt"

def add_student():

    student_name = input("Enter Student Name : ")
    with open(FILE_NAME, "w") as file:
        file.write(student_name + "\n")
    print("Successfully added student")

def view_student():

    print("Students List\n")
    print("-" * 40)

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

            if len(students) == 0:
                print("No Student Records Found.")
                return
            
            print("Students List\n")
            print("-" * 40) 

            for index, student in enumerate(students, start=1):
                print(index, ". ", student.strip())

    except FileNotFoundError:
        print("No Student Records Found.")


def search_student():

    name = input("Enter Student Name : ")

    try:
        with open(FILE_NAME, "r") as file:
            students = file.read()

            if name.lower() in students.lower():
                print("Student Found")
            else:
                print("No Student Found")


    except FileNotFoundError:
            print("No Student Records Found.")

def delete_student():

    name = input("Enter Student NAme : ")

    try:

        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:

            for student in students:

                if name.lower() != student.lower():

                    file.write(student)

                else: 

                    found = True

            if found:

                print("Student Deleted Successfully.")

            else:

                print("Student Not Found.")

         
    except FileNotFoundError:
            print("No Student Records Found.")

def count_students():

    try:
        with open(FILE_NAME, "r") as file:

            students = file.readlines()

        print("Total Students : ", len(students))

    except FileNotFoundError:

       print("File Not Found.")

while True:

    print("\n")
    print("=" * 40)
    print("\nStudent record Managemetn System")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Count Students")
    print("1. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_student()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        count_students()

    elif choice == "6":

        print("Thank you")

        break

    else:

        print("Invalid Input.")
    

