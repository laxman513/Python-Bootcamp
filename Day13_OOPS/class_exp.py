class Student:
    def __init__(self, name):
        self.name = name
        print(self)
        print(name)
    def dispaly(self):
        print("Student Name:", self.name)

student = Student("Laxman")
student.dispaly()
print("Name:", student.name)


student1 = Student("Laxman")
student2 = Student("Rahul")
student3 = student1
student1 = Student("Anil")
print("-" * 30)
print(student1.name)
print(student2.name)
print(student3.name)
