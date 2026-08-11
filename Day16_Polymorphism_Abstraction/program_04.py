# Program 04 - Same Method Name in Different Classes
class Email:
    def send(self):
        print("Sending email")

class SMS:
    def send(self):
        print("Sending SMS")

class WhatsApp:
    def send(self):
        print("Sending WhatsApp")

for message in [Email(), SMS(), WhatsApp()]:
    message.send()
