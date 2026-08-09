# Program 03 - Single Inheritance

class Person:
    def show(self):
        print("Person")


class Student(Person):
    def study(self):
        print("Studying")


student = Student()
student.show()
student.study()
