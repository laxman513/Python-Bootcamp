# Program 12 - Duck Typing with run()
class A:
    def run(self):
        print("A is running")

class B:
    def run(self):
        print("B is running")

def execute(obj):
    obj.run()

execute(A())
execute(B())
