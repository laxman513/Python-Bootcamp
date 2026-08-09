# Program 33 - Multiple Roles

class Employee:
    def employee_info(self):
        print("Employee")


class Developer:
    def developer_info(self):
        print("Developer")


class Manager:
    def manager_info(self):
        print("Manager")


class TechLead(Employee, Developer, Manager):
    def techlead_info(self):
        print("Tech Lead")


tech_lead = TechLead()

tech_lead.employee_info()
tech_lead.developer_info()
tech_lead.manager_info()
tech_lead.techlead_info()
