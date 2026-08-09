# Program 27 - isinstance() with Multiple Inheritance

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
