class Student:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello ", self.name)

    def welcome(self):
        print("Welcome")
        self.greet()

    school = "ABC School"

    @classmethod
    def display_school(abc):
        print(abc.school)

    @classmethod
    def change_school(abc):
        abc.school = "XYZ School"

    @staticmethod
    def college():
        print("ABC College")


student = Student("Laxman")
print(student.name)

student.change_name("Rahul")
print(student.name)

result = student.get_name()
print(result)

student.welcome()

Student.display_school()

Student.change_school()
Student.display_school()

Student.college()
student.college()


