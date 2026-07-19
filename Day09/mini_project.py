employees = []

# --------------------------------
# Add Employee
# --------------------------------

def add_employee():
    print("\nAdd Employee")
    print("-" * 30)

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Name        : ")
    department = input("Enter Department    : ")
    salary = float(input("Enter Salary      : "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee Added Successfully\n\n")

# --------------------------------
# View Employees
# --------------------------------

def view_employees():

    print("Employee List")
    print("-" * 30)

    if len(employees) == 0:
        print("No Employees Found.")
        return

    for emp in employees:
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}")
        print("-" * 30)

# --------------------------------
# Search Employees
# --------------------------------

def search_employee():

    emp_id = input("Enter Employee ID : ")
    
    found = False

    for emp in employees:

        if emp['id'] == emp_id:

            found == True
            print("\nEmployee Found")
            print("-" * 30)
            print(emp)
            break
    if not found:
        print("\nEmployee Not Found.")


# --------------------------------
# Total Salary
# --------------------------------

def total_salary():

    total_sal = 0

    for emp in employees:
        total_sal += emp['salary']

    print(f"\nTotal Salary : {total_sal}")


# --------------------------------
# Highest Salary
# --------------------------------

def highest_salary():

    if len(employees) == 0:
        print("No Employees Found.")
        return
    
    highest_salary_employee = max(employees, key = lambda emp: emp['salary'])

    print("Highest Salary Employee")
    print(30 * "-\n")
    
    print(highest_salary_employee)

# ------------------------------------------------------------
# Menu
# ------------------------------------------------------------

def menu():

    while True:

        print("\n")

        print("=" * 50)
        print("Employee Managemetn System")
        print("=" * 50)

        print("\n")

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Total Salary")
        print("5. Highest Salary")
        print("6. Exit")
        
        print("\n")
        choice = input("Enter Choice : ")

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
            print("\nThank you.")
            break

        else:
            print("Invalid Choice")

# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
menu()

