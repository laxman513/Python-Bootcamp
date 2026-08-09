# Program 08 - Calling Parent Method with super()

class Person:
    def show(self):
        print("Person")


class Student(Person):
    def show(self):
        super().show()
        print("Student")


student = Student()
student.show()
