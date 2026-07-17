salary = float(input("Enter your Salary:"))
experience = float(input("Enter your exeperience:"))

print(isinstance(True, int))

if experience >= 10 and salary < 5000000:
    print("Congeratulations!")
    print("Bonus: ", salary * 0.20)
else:
    print("Congeratulations!")
    print("Bonus: ", salary * 0.10)