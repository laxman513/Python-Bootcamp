# Program 32 - Employee, Developer and Manager

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee works")


class Developer(Employee):
    def work(self):
        super().work()
        print("Developer writes code")


class Manager(Employee):
    def work(self):
        super().work()
        print("Manager manages the team")


developer = Developer("Laxman")
manager = Manager("Ravi")

developer.work()
manager.work()
