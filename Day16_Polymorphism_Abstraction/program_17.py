# Program 17 - Polymorphic Notification
class EmailNotification:
    def notify(self):
        print("Email notification")

class SMSNotification:
    def notify(self):
        print("SMS notification")

def notify_user(notification):
    notification.notify()

notify_user(EmailNotification())
notify_user(SMSNotification())
