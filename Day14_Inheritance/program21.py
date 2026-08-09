# Program 21 - Diamond Inheritance

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
