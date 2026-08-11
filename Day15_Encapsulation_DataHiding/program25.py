# super() with a property getter
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class Student(Person):
    @property
    def name(self):
        return "Student: " + super().name

student = Student("Rahul")
print(student.name)
