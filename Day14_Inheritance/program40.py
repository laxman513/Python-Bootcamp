# Program 40 - Final Day 14 Challenge

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show(self):
        super().show()
        print("Employee ID:", self.employee_id)


class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language

    def show(self):
        super().show()
        print("Language:", self.language)


class Tester(Employee):
    def __init__(self, name, employee_id, tool):
        super().__init__(name, employee_id)
        self.tool = tool

    def show(self):
        super().show()
        print("Testing Tool:", self.tool)


class TechLead(Developer, Tester):
    def __init__(self, name, employee_id, language, tool):
        # This example intentionally demonstrates a limitation:
        # Developer and Tester constructors are not designed as
        # cooperative multiple-inheritance constructors because
        # their parameter lists are different.
        #
        # We therefore initialize the shared Employee/Person part
        # explicitly and add the two role-specific attributes.
        Person.__init__(self, name)
        self.employee_id = employee_id
        self.language = language
        self.tool = tool

    def show(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Language:", self.language)
        print("Testing Tool:", self.tool)
        print("Role: Tech Lead")


tech_lead = TechLead(
    "Laxman",
    101,
    "Python",
    "Selenium"
)

tech_lead.show()

print("\nMRO:")
print(TechLead.mro())
