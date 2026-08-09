# Program 37 - Multiple Inheritance with Cooperative super()

class Employee:
    def show(self):
        print("Employee")


class Developer(Employee):
    def show(self):
        super().show()
        print("Developer")


class Tester(Employee):
    def show(self):
        super().show()
        print("Tester")


class TechLead(Developer, Tester):
    def show(self):
        super().show()
        print("TechLead")


print(TechLead.mro())

obj = TechLead()
obj.show()

# MRO:
# TechLead -> Developer -> Tester -> Employee -> object
#
# Output:
# Employee
# Tester
# Developer
# TechLead
