age = int(input("Enter your age:"))
salary = float(input("Enter your salary:"))

if age >= 18:
    if salary >= 500000:
        print("Eligible for Premium Card")
    else:
        print("Eligible for normal card")
else:
    print("Not Eligible for anything")
