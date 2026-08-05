"""
==========================================================
Employee Management System
Day 13 Mini Project
==========================================================
"""

import os


class Employee:

    company = "JP Morgan"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID      : {self.emp_id}")
        print(f"Name    : {self.name}")
        print(f"Salary  : {self.salary}")
        print(f"Company : {Employee.company}")
        print("-" * 35)

    def to_file(self):
        return f"{self.emp_id},{self.name},{self.salary}\n"

    @staticmethod
    def from_file(line):
        data = line.strip().split(",")

        return Employee(
            int(data[0]),
            data[1],
            float(data[2])
        )

    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0

    @classmethod
    def change_company(cls, company):
        cls.company = company


FILE_NAME = "employees.txt"


def add_employee():

    print("\n===== Add Employee =====")

    emp_id = int(input("Enter Employee ID : "))
    name = input("Enter Employee Name : ")
    salary = float(input("Enter Salary : "))

    if not Employee.is_valid_salary(salary):
        print("Invalid Salary")
        return

    employee = Employee(emp_id, name, salary)

    with open(FILE_NAME, "a") as file:
        file.write(employee.to_file())

    print("\nEmployee Added Successfully.")


def view_employees():

    print("\n===== Employee List =====")

    if not os.path.exists(FILE_NAME):
        print("No employees found.")
        return

    with open(FILE_NAME, "r") as file:

        lines = file.readlines()

        if len(lines) == 0:
            print("No employees found.")
            return

        for line in lines:
            employee = Employee.from_file(line)
            employee.display()


def search_employee():

    print("\n===== Search Employee =====")

    if not os.path.exists(FILE_NAME):
        print("Employee file not found.")
        return

    search_id = int(input("Enter Employee ID : "))

    found = False

    with open(FILE_NAME, "r") as file:

        for line in file:

            employee = Employee.from_file(line)

            if employee.emp_id == search_id:

                employee.display()

                found = True

                break

    if not found:
        print("Employee Not Found.")

def update_salary():

    print("\n===== Update Salary =====")

    if not os.path.exists(FILE_NAME):
        print("Employee file not found.")
        return

    update_id = int(input("Enter Employee ID : "))

    updated = False

    employees = []

    with open(FILE_NAME, "r") as file:

        for line in file:

            employee = Employee.from_file(line)

            if employee.emp_id == update_id:

                new_salary = float(input("Enter New Salary : "))

                if not Employee.is_valid_salary(new_salary):
                    print("Invalid Salary")
                    return

                employee.salary = new_salary

                updated = True

            employees.append(employee)

    with open(FILE_NAME, "w") as file:

        for employee in employees:
            file.write(employee.to_file())

    if updated:
        print("Salary Updated Successfully.")
    else:
        print("Employee Not Found.")


def delete_employee():

    print("\n===== Delete Employee =====")

    if not os.path.exists(FILE_NAME):
        print("Employee file not found.")
        return

    delete_id = int(input("Enter Employee ID : "))

    deleted = False

    employees = []

    with open(FILE_NAME, "r") as file:

        for line in file:

            employee = Employee.from_file(line)

            if employee.emp_id == delete_id:

                deleted = True

            else:

                employees.append(employee)

    with open(FILE_NAME, "w") as file:

        for employee in employees:

            file.write(employee.to_file())

    if deleted:
        print("Employee Deleted Successfully.")
    else:
        print("Employee Not Found.")

def change_company():

    print("\n===== Change Company =====")

    company = input("Enter New Company Name : ")

    Employee.change_company(company)

    print("Company Changed Successfully.")
    print("Current Company :", Employee.company)


def menu():

    print("\n")
    print("=" * 45)
    print("      Employee Management System")
    print("=" * 45)
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Change Company")
    print("7. Exit")
    print("=" * 45)


def main():

    while True:

        menu()

        try:

            choice = int(input("Enter your choice : "))

            if choice == 1:

                add_employee()

            elif choice == 2:

                view_employees()

            elif choice == 3:

                search_employee()

            elif choice == 4:

                update_salary()

            elif choice == 5:

                delete_employee()

            elif choice == 6:

                change_company()

            elif choice == 7:

                print("\nThank you for using Employee Management System.")
                break

            else:

                print("Invalid Choice.")

        except ValueError:

            print("Please enter a valid number.")

        except Exception as ex:

            print("Error :", ex)


if __name__ == "__main__":
    main()