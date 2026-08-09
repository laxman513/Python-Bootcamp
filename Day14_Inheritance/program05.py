# Program 05 - Hierarchical Inheritance

class Person:
    def show(self):
        print("Person")


class Student(Person):
    def study(self):
        print("Studying")


class Employee(Person):
    def work(self):
        print("Working")


student = Student()
employee = Employee()

student.show()
student.study()

employee.show()
employee.work()
