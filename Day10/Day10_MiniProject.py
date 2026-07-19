import calculator
import random_utils
import date_utils


while True:

    print("\n========== Utility Toolkit ==========")
    print("1. Calculator")
    print("2. Random Number Generator")
    print("3. Date & Time")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Choose operation: ")

        if operation == "1":
            print("Result:", calculator.add(num1, num2))

        elif operation == "2":
            print("Result:", calculator.sub(num1, num2))

        elif operation == "3":
            print("Result:", calculator.mul(num1, num2))

        elif operation == "4":
            print("Result:", calculator.div(num1, num2))

        else:
            print("Invalid Operation.")

    elif choice == "2":

        print("Random Number:", random_utils.generate_random())

    elif choice == "3":

        print("Today's Date :", date_utils.current_date())
        print("Current Time :", date_utils.current_time())

    elif choice == "4":

        print("Thank you for using Utility Toolkit!")
        break

    else:
        print("Invalid Choice.")