# Program 01 - Basic Inheritance

class Person:
    def display_name(self):
        print("Person")


class Student(Person):
    pass


student = Student()
student.display_name()
