# Program 19 - Duck Typing with save()
class File:
    def save(self):
        print("File saved")

class Database:
    def save(self):
        print("Data saved to database")

def save_data(storage):
    storage.save()

save_data(File())
save_data(Database())
