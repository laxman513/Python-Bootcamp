# Program 06 - Runtime Polymorphism
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

class Tester(Employee):
    def work(self):
        print("Tester is testing software")

employees = [Developer(), Tester(), Employee()]

for employee in employees:
    employee.work()
