# Program 04 - Multilevel Inheritance

class Person:
    def person_info(self):
        print("Person")


class Employee(Person):
    def employee_info(self):
        print("Employee")


class Manager(Employee):
    def manager_info(self):
        print("Manager")


manager = Manager()
manager.person_info()
manager.employee_info()
manager.manager_info()
