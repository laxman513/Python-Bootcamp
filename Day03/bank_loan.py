age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
credit_score = float(input("Enter your credit score: "))

if age >= 21:

    if salary >= 500000:

        if credit_score >= 750:

            print("Loan Approved")

            existing_customer = input(
                "Are you an existing customer (yes/no): "
            ).strip().lower()

            if existing_customer == "yes":
                print("Fast Track Approval")

            elif existing_customer == "no":
                print("Normal Processing")

            else:
                print("Invalid Input")

        else:
            print("Credit score too low.")

    else:
        print("Salary must be at least ₹5,00,000.")

else:
    print("Age is not eligible.")