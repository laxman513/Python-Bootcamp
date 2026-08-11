class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(10000)

print(account._BankAccount__balance)

print(account.__dict__)





class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Laxman", 16)

print(student.__dict__)

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def study(self):
        print("Studying")


student = Student("Laxman")

print(student.__dict__)
print(Student.__dict__)

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary can not be negative")

employee = Employee(10000)
employee.set_salary(-5000)

print(employee.get_salary())

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

employee = Employee(5000)
print(employee.salary)

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 10000:
            self.__salary = salary
        else:
            print("Invalid salary")

employee = Employee(50000)

employee.salary = 5000

print(employee.salary)


class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Student(Person):

    # @Person.name.setter
    def name(self, value):
        self._Person__name = value


student = Student("Rahul")

student.name = "Amit"

print(student.name)

print("_" * 30)

class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("Name cannot be empty")


class Student(Person):

    @property
    def name(self):
        return "Student: " + super().name

    @name.setter
    def name(self, value):
        super(Student, Student).name.__set__(self, value)


student = Student("Rahul")

print(student.name)

student.name = "Amit"

print(student.name)

print("*" * 30)

class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("Name cannot be empty")


class Student(Person):

    @property
    def name(self):
        return "Student: " + super().name


student = Student("Rahul")

student.name = ""

print(student.name)

