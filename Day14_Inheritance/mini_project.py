class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print("Employee ID:", self.employee_id)


class Developer(Employee):

    def __init__(self, name, age, employee_id, language):
        super().__init__(name, age, employee_id)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)


class Tester(Employee):

    def __init__(self, name, age, employee_id, tool):
        super().__init__(name, age, employee_id)
        self.tool = tool

    def display(self):
        super().display()
        print("Testing Tool:", self.tool)


class TechLead(Developer, Tester):

    def __init__(self, name, age, employee_id, language, tool):
        # Developer and Tester have different constructor signatures.
        # For this Day 14 project, initialize the common part directly.
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.language = language
        self.tool = tool

    def display(self):
        print("----- Tech Lead -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Language:", self.language)
        print("Testing Tool:", self.tool)


# Create objects

developer = Developer(
    "Ravi",
    25,
    101,
    "Python"
)

tester = Tester(
    "Anita",
    28,
    102,
    "Selenium"
)

tech_lead = TechLead(
    "Laxman",
    45,
    103,
    "Python",
    "Selenium"
)


# Display employees

print("DEVELOPER")
developer.display()

print("\nTESTER")
tester.display()

print("\nTECH LEAD")
tech_lead.display()


# Check isinstance()

print("\n--- isinstance() ---")

print(isinstance(developer, Developer))
print(isinstance(developer, Employee))
print(isinstance(developer, Person))

print(isinstance(tech_lead, TechLead))
print(isinstance(tech_lead, Developer))
print(isinstance(tech_lead, Tester))
print(isinstance(tech_lead, Employee))
print(isinstance(tech_lead, Person))


# Check issubclass()

print("\n--- issubclass() ---")

print(issubclass(Developer, Employee))
print(issubclass(Developer, Person))

print(issubclass(TechLead, Developer))
print(issubclass(TechLead, Tester))
print(issubclass(TechLead, Employee))
print(issubclass(TechLead, Person))


# Display MRO

print("\n--- TechLead MRO ---")

print(TechLead.mro())
