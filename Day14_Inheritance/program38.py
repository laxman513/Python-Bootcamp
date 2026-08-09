# Program 38 - Multiple Inheritance with Constructors and super()

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        print("Employee constructor")


class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language
        print("Developer constructor")


developer = Developer("Laxman", 101, "Python")

print(developer.name)
print(developer.employee_id)
print(developer.language)
