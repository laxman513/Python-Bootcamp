# Property override + parent setter reuse
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("Name cannot be empty")

class Student(Person):
    @property
    def name(self):
        return "Student: " + super().name

    @name.setter
    def name(self, value):
        Person.name.fset(self, value)

student = Student("Rahul")
student.name = "Amit"
print(student.name)
