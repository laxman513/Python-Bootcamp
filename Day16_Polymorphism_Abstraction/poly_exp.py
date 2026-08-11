class Payment:

    def pay(self):
        print("Processing Payment")

class UPI(Payment):

    def pay(self):
        super().pay()
        print("Pay using UPI")

upi = UPI()
upi.pay()

class Employee:

    def work(self):
        print("Employee is working")

class Developer(Employee):

    def work(self):
        print("Developer is working")

class Tester(Employee):

    def work(self):
        print("Tester is working")

employees = [Developer(), Tester()]

for employee in employees:
    employee.work()

class PDFReport:

    def generate(self):
        print("Generate PDF Report")

class ExcelReport:

    def generate(self):
        print("Generate Excel Report")

class HTMLReport:

    def generate(self):
        print("Generate HTML Report")

def geenrate_report(report):
    report.generate()

geenrate_report(PDFReport())
geenrate_report(ExcelReport())
geenrate_report(ExcelReport())

class CreditCard:

    def pay(self, amount):
        print(f"Paid Rs.{amount} using crddit card")

class UPI():

    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")

class Carsh:

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Cash")

def make_payment(obj, amount):
    obj.pay(amount)

make_payment(CreditCard(), 15000)
make_payment(Carsh(), 15000)
make_payment(UPI(), 15000)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [Employee("laxman", 1000), Employee("rahul", 15000), Employee("Krishna", 20000)]

employees = sorted(employees, key=lambda employee:employee.salary)

for employee in employees:
    print(employee.name, employee.salary)


def square(x):
    return x * x

def cube(x):
    return x * x * x

def caluculate(operation, number):
    print(operation(number))

caluculate(square, 2)
caluculate(cube, 2)


