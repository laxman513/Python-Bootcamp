# ============================================================
# Day 09 Mini Project
# Employee Management System using Functions
# Author : Laxman
# ============================================================

employees = []


# ------------------------------------------------------------
# Add Employee
# ------------------------------------------------------------
def add_employee():
    print("\nAdd Employee")
    print("-" * 30)

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Name        : ")
    department = input("Enter Department : ")
    salary = float(input("Enter Salary      : "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("\nEmployee Added Successfully.")


# ------------------------------------------------------------
# View Employees
# ------------------------------------------------------------
def view_employees():

    print("\nEmployee List")
    print("-" * 50)

    if len(employees) == 0:
        print("No Employees Found.")
        return

    for emp in employees:
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}")
        print("-" * 50)


# ------------------------------------------------------------
# Search Employee
# ------------------------------------------------------------
def search_employee():

    emp_id = input("\nEnter Employee ID : ")

    found = False

    for emp in employees:

        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("-" * 30)
            print(emp)
            found = True
            break

    if not found:
        print("Employee Not Found.")


# ------------------------------------------------------------
# Total Salary
# ------------------------------------------------------------
def total_salary():

    total = 0

    for emp in employees:
        total += emp["salary"]

    print("\nTotal Salary :", total)


# ------------------------------------------------------------
# Highest Salary
# ------------------------------------------------------------
def highest_salary():

    if len(employees) == 0:
        print("No Employees Available.")
        return

    highest = max(employees, key=lambda emp: emp["salary"])

    print("\nHighest Salary Employee")
    print("-" * 30)
    print(highest)


# ------------------------------------------------------------
# Menu
# ------------------------------------------------------------
def menu():

    while True:

        print("\n")
        print("=" * 50)
        print("Employee Management System")
        print("=" * 50)

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Total Salary")
        print("5. Highest Salary")
        print("6. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            total_salary()

        elif choice == "5":
            highest_salary()

        elif choice == "6":
            print("\nThank You...")
            break

        else:
            print("Invalid Choice")


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
menu()