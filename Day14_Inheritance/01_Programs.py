# ==========================================================
# Day 14 - Inheritance
# Program 1 - Basic Inheritance
# ==========================================================

class Animal:
    
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()

# ==========================================================
# Program 2 - Child Class with Its Own Method
# ==========================================================


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# ==========================================================
# Program 3 - Parent Constructor
# ==========================================================

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):

        print("Name:", self.name)

class Student(Person):

    pass

student = Student("Laxman")

student.display_name()

# ==========================================================
# Program 4 - Using super()
# ==========================================================

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, age):
        self.age = age

        super().__init__(name)

    def display_name(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Laxman", 16)

student.display_name()

# ==========================================================
# Program 5 - Parent and Child Methods
# ==========================================================


class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name :", self.name)


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_salary(self):
        print("Salary :", self.salary)


employee = Employee("Laxman", 250000)

employee.display_name()
employee.display_salary()

# ==========================================================
# Program 6 - Method Overriding
# ==========================================================


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# ==========================================================
# Program 7 - super() with Method Overriding
# ==========================================================


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()

dog.sound()
dog.sound()

# ==========================================================
# Program 8 - super() with Constructor and Method
# ==========================================================

class Person:

    def __init__(self, name):

        self.name = name

    def dispaly(self):

        print("Name:", self.name)

class Employee(Person):

    def __init__(self, name, age):
        super().__init__(name)

        self.age = age

    def dispaly(self):
        super().dispaly()
        print("Age:", self.age)

employee = Employee("Laxman", 46)
employee.dispaly()

# ==========================================================
# Program 9 - Inheritance with Different Attributes
# ==========================================================


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_manager(self):
        print("Name      :", self.name)
        print("Salary    :", self.salary)
        print("Team Size :", self.team_size)


manager = Manager("Laxman", 250000, 10)

manager.display_manager()

# ==========================================================
# Program 10 - Child Using Parent Attributes
# ==========================================================


class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print("Balance :", self.balance)


class SavingsAccount(BankAccount):

    def add_interest(self, interest):
        self.balance = self.balance + interest


account = SavingsAccount("ACC101", 50000)

account.show_balance()

account.add_interest(5000)

account.show_balance()

# ==========================================================
# Program 11 - isinstance() with Inheritance
# ==========================================================


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


# ==========================================================
# Program 12 - issubclass() with Inheritance
# ==========================================================


class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Dog, Dog))


# ==========================================================
# Program 13 - Single Inheritance with Multiple Methods
# ==========================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def work(self):
        print(self.name, "is working")

class Developer(Employee):

    def write_code(self):
        print(self.name, "is writing Python Code")

developer = Developer("Laxman", 25000)
developer.display_employee()
developer.work()
developer.write_code()

# ==========================================================
# Program 14 - Child Accessing Parent Attributes
# ==========================================================


class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department


class Developer(Employee):

    def display(self):
        print("Name       :", self.name)
        print("Department :", self.department)


developer = Developer("Laxman", "Technology")

developer.display()


# ==========================================================
# Program 15 - Child Constructor Without super()
# ==========================================================


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, age, name):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age :", self.age)


student = Student("Laxman", 16)

student.display()

# ==========================================================
# Program 16 - Multilevel Inheritance
# ==========================================================

class Person():

    def show_peson(self):
        print("I am a person")

class Employee(Person):

    def show_employee(self):
        print("I am an Employee")

class Manager(Employee):

    def show_manager(self):
        print("I am a Manager")

manager = Manager()
manager.show_peson()
manager.show_employee()
manager.show_manager()

# ==========================================================
# Program 17 - Multilevel Inheritance with Constructors
# ==========================================================


class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Manager(Employee):

    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def display(self):
        print("Name       :", self.name)
        print("Employee ID:", self.employee_id)
        print("Team Size  :", self.team_size)


manager = Manager("Laxman", "EMP101", 8)

manager.display()

# ==========================================================
# Program 18 - Multilevel Inheritance with Method Overriding
# ==========================================================


class Person:

    def display(self):
        print("I am a person")


class Employee(Person):

    def display(self):
        print("I am an employee")


class Manager(Employee):

    def display(self):
        print("I am a manager")


manager = Manager()

manager.display()

# ==========================================================
# Program 19 - super() Across Multiple Levels
# ==========================================================


class Person:

    def display(self):
        print("Person")


class Employee(Person):

    def display(self):
        super().display()
        print("Employee")


class Manager(Employee):

    def display(self):
        super().display()
        print("Manager")


manager = Manager()

manager.display()

# ==========================================================
# Program 20 - Multilevel Inheritance with Data
# ==========================================================


class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name       :", self.name)
        print("Salary     :", self.salary)
        print("Department :", self.department)


manager = Manager("Laxman", 250000, "Technology")

manager.display()

# ==========================================================
# Program 21 - Multiple Inheritance
# ==========================================================


class Father:

    def father_method(self):
        print("This is Father's method")


class Mother:

    def mother_method(self):
        print("This is Mother's method")


class Child(Father, Mother):

    def child_method(self):
        print("This is Child's method")


child = Child()

child.father_method()
child.mother_method()
child.child_method()

# ==========================================================
# Program 22 - Same Method in Multiple Parent Classes
# ==========================================================


class Father:

    def show(self):
        print("Father's method")


class Mother:

    def show(self):
        print("Mother's method")


class Child(Father, Mother):
    pass


child = Child()

child.show()

# ==========================================================
# Program 23 - Checking MRO
# ==========================================================


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass


child = Child()

child.show()

print(Child.mro())

# ==========================================================
# Program 24 - Changing Parent Order
# ==========================================================


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Mother, Father):
    pass


child = Child()

child.show()

print(Child.mro())

# ==========================================================
# Program 25 - Calling Both Parent Methods Explicitly
# ==========================================================


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):

    def show(self):
        Father.show(self)
        Mother.show(self)
        print("Child")


child = Child()

child.show()

# ==========================================================
# Program 26 - Multiple Inheritance with super()
# ==========================================================


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):

    def show(self):
        super().show()
        print("Child")


child = Child()

child.show()

# ==========================================================
# Program 27 - Cooperative Multiple Inheritance
# ==========================================================

class Base:

    def show(self):
        pass

class Father(Base):

    def show(self):
        print("Father")
        super().show()


class Mother:

    def show(self):
        print("Mother")
        super().show()


class Child(Father, Mother):

    def show(self):
        print("Child")
        super().show()


child = Child()

child.show()

# ==========================================================
# Program 28 - Multiple Inheritance with Different Methods
# ==========================================================


class Employee:

    def employee_info(self):
        print("Employee information")


class Developer:

    def developer_info(self):
        print("Developer information")


class SoftwareEngineer(Employee, Developer):

    def engineer_info(self):
        print("Software Engineer information")


engineer = SoftwareEngineer()

engineer.employee_info()
engineer.developer_info()
engineer.engineer_info()

# ==========================================================
# Program 29 - Multiple Inheritance with Constructors
# ==========================================================


class Employee:

    def __init__(self, employee_id):
        self.employee_id = employee_id


class Developer:

    def __init__(self, language):
        self.language = language


class SoftwareEngineer(Employee, Developer):

    def __init__(self, employee_id, language):
        Employee.__init__(self, employee_id)
        Developer.__init__(self, language)

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Language   :", self.language)


engineer = SoftwareEngineer("EMP101", "Python")

engineer.display()


# ==========================================================
# Program 30 - Same Method in Multiple Parents
# ==========================================================


class Employee:

    def show(self):
        print("Employee")


class Developer:

    def show(self):
        print("Developer")


class SoftwareEngineer(Employee, Developer):

    def show_all(self):
        Employee.show(self)
        Developer.show(self)
        print("Software Engineer")


engineer = SoftwareEngineer()

engineer.show_all()

# ==========================================================
# Program 31 - Diamond Inheritance
# ==========================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

obj.show()

# ==========================================================
# Program 32 - Diamond Inheritance with super()
# ==========================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()

obj.show()

# ==========================================================
# Program 33 - Understanding MRO
# ==========================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

print(D.mro())

obj.show()

# ==========================================================
# Program 34 - MRO with Three Parent Classes
# ==========================================================


class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C:

    def show(self):
        print("C")


class D(A, B, C):
    pass


obj = D()

print(D.mro())

obj.show()


# ==========================================================
# Program 35 - Multiple Inheritance with super() and MRO
# ==========================================================


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()

print(D.mro())

obj.show()


# ==========================================================
# Program 36 - Calling a Specific Parent Method
# ==========================================================


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):

    def show(self):
        Father.show(self)
        Mother.show(self)
        print("Child")


child = Child()

child.show()

# ==========================================================
# Program 37 - Employee Multiple Inheritance
# ==========================================================


class Employee:

    def employee_info(self):
        print("Employee ID: EMP101")


class Developer:

    def developer_info(self):
        print("Programming Language: Python")


class Manager:

    def manager_info(self):
        print("Team Size: 8")


class SoftwareEngineer(Employee, Developer, Manager):

    def display(self):
        self.employee_info()
        self.developer_info()
        self.manager_info()


engineer = SoftwareEngineer()

engineer.display()

# ==========================================================
# Program 38 - isinstance() with Multiple Inheritance
# ==========================================================


class Employee:
    pass


class Developer:
    pass


class SoftwareEngineer(Employee, Developer):
    pass


engineer = SoftwareEngineer()

print(isinstance(engineer, SoftwareEngineer))
print(isinstance(engineer, Employee))
print(isinstance(engineer, Developer))

# ==========================================================
# Program 39 - issubclass() with Multiple Inheritance
# ==========================================================


class Employee:
    pass


class Developer:
    pass


class SoftwareEngineer(Employee, Developer):
    pass


print(issubclass(SoftwareEngineer, Employee))
print(issubclass(SoftwareEngineer, Developer))
print(issubclass(SoftwareEngineer, SoftwareEngineer))

# ==========================================================
# Program 40 - Complete Multiple Inheritance Example
# ==========================================================


class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)


class Developer(Employee):

    def show(self):
        super().show()
        print("Developer")


class Manager(Employee):

    def show(self):
        super().show()
        print("Manager")


class TechLead(Developer, Manager):

    def show(self):
        super().show()
        print("Tech Lead")


tech_lead = TechLead("Laxman")

print("MRO:")
print(TechLead.mro())

print("\nOutput:")
tech_lead.show()
