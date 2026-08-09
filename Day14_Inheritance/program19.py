# Program 19 - Multiple Inheritance MRO

class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


print(C.mro())

obj = C()
obj.show()
