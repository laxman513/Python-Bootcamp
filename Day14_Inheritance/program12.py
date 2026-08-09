# Program 12 - Constructor Chaining

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


manager = Manager("Laxman", 101, 10)

print(manager.name)
print(manager.employee_id)
print(manager.team_size)
