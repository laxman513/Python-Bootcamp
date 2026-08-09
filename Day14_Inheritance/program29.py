# Program 29 - super() vs Explicit Parent Call

class Father:
    def show(self):
        print("Father")


class Child(Father):
    def show(self):
        super().show()
        print("Child")


child = Child()
child.show()
