# Program 02 - Child Adds Its Own Method

class Person:
    def display_name(self):
        print("Person")


class Student(Person):
    def study(self):
        print("Studying")


student = Student()
student.display_name()
student.study()
