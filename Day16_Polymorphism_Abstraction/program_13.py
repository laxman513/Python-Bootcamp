# Program 13 - Duck Typing with code()
class Developer:
    def code(self):
        print("Developer is coding")

class Robot:
    def code(self):
        print("Robot is coding")

def start_coding(obj):
    obj.code()

start_coding(Developer())
start_coding(Robot())
