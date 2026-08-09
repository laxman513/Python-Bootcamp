# Program 18 - Method Search Through MRO

class A:
    def show(self):
        print("A")


class B(A):
    pass


obj = B()
obj.show()
