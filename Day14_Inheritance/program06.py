# Program 06 - Multiple Inheritance

class Father:
    def father_info(self):
        print("Father")


class Mother:
    def mother_info(self):
        print("Mother")


class Child(Father, Mother):
    def child_info(self):
        print("Child")


child = Child()
child.father_info()
child.mother_info()
child.child_info()
