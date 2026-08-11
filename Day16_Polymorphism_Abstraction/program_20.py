# Program 20 - Polymorphic Authentication
class PasswordLogin:
    def authenticate(self):
        print("Authenticated using password")

class FingerprintLogin:
    def authenticate(self):
        print("Authenticated using fingerprint")

def login(method):
    method.authenticate()

login(PasswordLogin())
login(FingerprintLogin())
