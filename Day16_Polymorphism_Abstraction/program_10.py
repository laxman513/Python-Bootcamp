# Program 10 - Employee Polymorphism
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is coding")

class Tester(Employee):
    def work(self):
        print("Tester is testing")

for employee in [Developer(), Tester()]:
    employee.work()
