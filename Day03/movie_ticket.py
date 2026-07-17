age = int(input("Your age:"))

if age > 18:
    ID = input("Do you have id yes/no:").strip().lower()
    if ID == "yes":
        print("Allowed")
    elif ID == "no":
        print("ID Required")
    else:
        print("Invalid input. Please enter yes/no.")
else:
    print("Not allowed")