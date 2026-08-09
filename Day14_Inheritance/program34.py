# Program 34 - Output Prediction Practice

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        super().show()
        print("B")


class C(B):
    def show(self):
        super().show()
        print("C")


obj = C()
print(C.mro())
obj.show()
