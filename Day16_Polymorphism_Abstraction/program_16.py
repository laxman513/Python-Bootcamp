# Program 16 - Duck Typing with Printer and Scanner
class Printer:
    def execute(self):
        print("Printing document")

class Scanner:
    def execute(self):
        print("Scanning document")

def execute_device(device):
    device.execute()

execute_device(Printer())
execute_device(Scanner())
