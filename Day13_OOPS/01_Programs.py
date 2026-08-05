# ==========================================================
# Day 13 - Object Oriented Programming (OOP)
# Programs 1 - 15
# ==========================================================


# ==========================================================
# Program 1 - Create First Class
# ==========================================================

print("\n========== Program 1 ==========")

class Student:
    pass

student = Student()

print(type(student))


# ==========================================================
# Program 2 - Constructor
# ==========================================================

print("\n========== Program 2 ==========")

class Employee:

    def __init__(self):
        print("Constructor Called")

employee = Employee()


# ==========================================================
# Program 3 - Constructor with Parameter
# ==========================================================

print("\n========== Program 3 ==========")

class Student:

    def __init__(self, name):
        self.name = name

student = Student("Laxman")

print(student.name)


# ==========================================================
# Program 4 - Multiple Instance Variables
# ==========================================================

print("\n========== Program 4 ==========")

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student = Student("Laxman", 44)

print(student.name)
print(student.age)


# ==========================================================
# Program 5 - Multiple Objects
# ==========================================================

print("\n========== Program 5 ==========")

class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Laxman")
student2 = Student("Rahul")
student3 = Student("Anil")

print(student1.name)
print(student2.name)
print(student3.name)


# ==========================================================
# Program 6 - Instance Method
# ==========================================================

print("\n========== Program 6 ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Student Name :", self.name)

student = Student("Laxman")

student.display()


# ==========================================================
# Program 7 - Display Multiple Objects
# ==========================================================

print("\n========== Program 7 ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print(self.name)

student1 = Student("Laxman")
student2 = Student("Rahul")

student1.display()
student2.display()


# ==========================================================
# Program 8 - Change Instance Variable
# ==========================================================

print("\n========== Program 8 ==========")

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Laxman")

print(student.name)

student.name = "Rahul"

print(student.name)


# ==========================================================
# Program 9 - Return Value
# ==========================================================

print("\n========== Program 9 ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def get_name(self):

        return self.name

student = Student("Laxman")

print(student.get_name())


# ==========================================================
# Program 10 - Method Calling Another Method
# ==========================================================

print("\n========== Program 10 ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print("Hello", self.name)

    def welcome(self):

        print("Welcome")

        self.greet()

student = Student("Laxman")

student.welcome()


# ==========================================================
# Program 11 - __str__()
# ==========================================================

print("\n========== Program 11 ==========")

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name

student = Student("Laxman")

print(student)


# ==========================================================
# Program 12 - Class Variable
# ==========================================================

print("\n========== Program 12 ==========")

class Student:

    school = "ABC School"

student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
print(Student.school)


# ==========================================================
# Program 13 - Modify Class Variable
# ==========================================================

print("\n========== Program 13 ==========")

class Student:

    school = "ABC School"

Student.school = "XYZ School"

student = Student()

print(student.school)
print(Student.school)


# ==========================================================
# Program 14 - Class Variable vs Instance Variable
# ==========================================================

print("\n========== Program 14 ==========")

class Student:

    school = "ABC School"

student = Student()

student.school = "PQR School"

print(student.school)
print(Student.school)


# ==========================================================
# Program 15 - Attribute Lookup
# ==========================================================

print("\n========== Program 15 ==========")

class Student:

    school = "ABC School"

student = Student()

print(student.school)

student.school = "XYZ School"

print(student.school)

print(Student.school)

# ==========================================================
# Programs 16 - 30
# ==========================================================


# ==========================================================
# Program 16 - Update Instance Variable Using Method
# ==========================================================

print("\n========== Program 16 ==========")

class Student:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


student = Student("Laxman")

print(student.name)

student.change_name("Rahul")

print(student.name)


# ==========================================================
# Program 17 - Return Instance Variable
# ==========================================================

print("\n========== Program 17 ==========")

class Student:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


student = Student("Laxman")

result = student.get_name()

print(result)


# ==========================================================
# Program 18 - One Method Calling Another
# ==========================================================

print("\n========== Program 18 ==========")

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def welcome(self):
        print("Welcome")
        self.greet()


student = Student("Laxman")

student.welcome()


# ==========================================================
# Program 19 - Multiple Objects Calling Same Method
# ==========================================================

print("\n========== Program 19 ==========")

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student1 = Student("Laxman")
student2 = Student("Rahul")

student1.display()
student2.display()


# ==========================================================
# Program 20 - Employee Class
# ==========================================================

print("\n========== Program 20 ==========")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee :", self.name)
        print("Salary   :", self.salary)


employee = Employee("Laxman", 250000)

employee.display()


# ==========================================================
# Program 21 - Class Variable Example
# ==========================================================

print("\n========== Program 21 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Laxman")
emp2 = Employee("Rahul")

print(emp1.company)
print(emp2.company)
print(Employee.company)


# ==========================================================
# Program 22 - Modify Class Variable
# ==========================================================

print("\n========== Program 22 ==========")

class Employee:

    company = "JP Morgan"


Employee.company = "Google"

print(Employee.company)


# ==========================================================
# Program 23 - Class Variable vs Instance Variable
# ==========================================================

print("\n========== Program 23 ==========")

class Employee:

    company = "JP Morgan"


emp = Employee()

emp.company = "Microsoft"

print(emp.company)

print(Employee.company)


# ==========================================================
# Program 24 - Attribute Lookup
# ==========================================================

print("\n========== Program 24 ==========")

class Employee:

    company = "JP Morgan"


emp = Employee()

print(emp.company)

emp.company = "Google"

print(emp.company)

print(Employee.company)


# ==========================================================
# Program 25 - Interview Example
# ==========================================================

print("\n========== Program 25 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name

    def change_company(self):
        self.company = "Google"


emp1 = Employee("Laxman")
emp2 = Employee("Rahul")

emp1.change_company()

print(emp1.company)
print(emp2.company)
print(Employee.company)


# ==========================================================
# Program 26 - Employee Interview Example
# ==========================================================

print("\n========== Program 26 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Laxman")
emp2 = Employee("Rahul")

Employee.company = "Google"

emp1.company = "Microsoft"

print(emp1.company)
print(emp2.company)
print(Employee.company)


# ==========================================================
# Program 27 - Multiple Employees
# ==========================================================

print("\n========== Program 27 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name, "-", self.company)


emp1 = Employee("Laxman")
emp2 = Employee("Rahul")
emp3 = Employee("Anil")

emp1.display()
emp2.display()
emp3.display()


# ==========================================================
# Program 28 - Change Company
# ==========================================================

print("\n========== Program 28 ==========")

class Employee:

    company = "JP Morgan"


print(Employee.company)

Employee.company = "Microsoft"

print(Employee.company)


# ==========================================================
# Program 29 - __str__ Example
# ==========================================================

print("\n========== Program 29 ==========")

class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


emp = Employee("Laxman")

print(emp)


# ==========================================================
# Program 30 - Real World Employee Example
# ==========================================================

print("\n========== Program 30 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID      :", self.emp_id)
        print("Name    :", self.name)
        print("Salary  :", self.salary)
        print("Company :", Employee.company)


emp = Employee(101, "Laxman", 250000)

emp.display()

# ==========================================================
# Programs 31 - 40
# ==========================================================


# ==========================================================
# Program 31 - First Class Method
# ==========================================================

print("\n========== Program 31 ==========")

class Student:

    school = "ABC School"

    @classmethod
    def display_school(cls):
        print(cls.school)


Student.display_school()


# ==========================================================
# Program 32 - Change Class Variable
# ==========================================================

print("\n========== Program 32 ==========")

class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls):
        cls.school = "XYZ School"


Student.change_school()

print(Student.school)


# ==========================================================
# Program 33 - Call Class Method Using Object
# ==========================================================

print("\n========== Program 33 ==========")

class Student:

    school = "ABC School"

    @classmethod
    def display_school(cls):
        print(cls.school)


student = Student()

student.display_school()


# ==========================================================
# Program 34 - Instance Method + Class Method
# ==========================================================

print("\n========== Program 34 ==========")

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)

    @classmethod
    def display_school(cls):
        print(cls.school)


student = Student("Laxman")

student.display_name()

Student.display_school()


# ==========================================================
# Program 35 - Employee Class Method Example
# ==========================================================

print("\n========== Program 35 ==========")

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls):
        cls.company = "Google"


Employee.change_company()

print(Employee.company)


# ==========================================================
# Program 36 - First Static Method
# ==========================================================

print("\n========== Program 36 ==========")

class Calculator:

    @staticmethod
    def add(a, b):
        print(a + b)


Calculator.add(10, 20)


# ==========================================================
# Program 37 - Static Method Using Object
# ==========================================================

print("\n========== Program 37 ==========")

class Calculator:

    @staticmethod
    def add(a, b):
        print(a + b)


calculator = Calculator()

calculator.add(50, 25)


# ==========================================================
# Program 38 - Utility Method
# ==========================================================

print("\n========== Program 38 ==========")

class Math:

    @staticmethod
    def square(number):
        return number * number


print(Math.square(8))


# ==========================================================
# Program 39 - Instance + Static Method
# ==========================================================

print("\n========== Program 39 ==========")

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

    @staticmethod
    def college():
        print("ABC College")


student = Student("Laxman")

student.display()

Student.college()


# ==========================================================
# Program 40 - Bank Interest Calculator
# ==========================================================

print("\n========== Program 40 ==========")

class Bank:

    @staticmethod
    def calculate_interest(amount):
        return amount * 0.07


interest = Bank.calculate_interest(100000)

print("Interest :", interest)