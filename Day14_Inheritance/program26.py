# Program 26 - issubclass()

class Person:
    pass


class Student(Person):
    pass


print(issubclass(Student, Person))
print(issubclass(Student, Student))
