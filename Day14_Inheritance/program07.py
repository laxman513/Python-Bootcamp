# Program 07 - Method Overriding

class Person:
    def show(self):
        print("Person")


class Student(Person):
    def show(self):
        print("Student")


student = Student()
student.show()
