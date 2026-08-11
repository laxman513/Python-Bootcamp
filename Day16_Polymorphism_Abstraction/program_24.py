# Program 24 - sorted() with key
names = ["Raj", "Alexander", "Bob", "John"]

print(sorted(names, key=len))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [
    Employee("Laxman", 1000),
    Employee("Rahul", 15000),
    Employee("Krishna", 20000)
]

employees = sorted(employees, key=lambda employee: employee.salary)

for employee in employees:
    print(employee.name, employee.salary)
