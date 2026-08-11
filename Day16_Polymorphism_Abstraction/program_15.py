# Program 15 - Polymorphic Message Sending
class Email:
    def send(self):
        print("Email sent")

class SMS:
    def send(self):
        print("SMS sent")

class WhatsApp:
    def send(self):
        print("WhatsApp message sent")

def send_message(message):
    message.send()

for message in [Email(), SMS(), WhatsApp()]:
    send_message(message)
