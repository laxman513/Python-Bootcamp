import numpy as np

def main():
    employees = np.array([
        [101, 25, 2, 50000],
        [102, 30, 5, 70000],
        [103, 35, 8, 90000],
        [104, 40, 12, 120000],
        [105, 28, 4, 65000]
    ])

    employee_ids = employees[:, 0]
    ages = employees[:, 1]
    exeperiences = employees[:, 2]
    salaries = employees[:, 3]

    print("===============================================\n")
    print("============EMPLOYEE DATA ANALYZER=============\n")
    print("\nEmployee Dataset")
    print(employees)

    print("\nNumber of Employees:", employees.shape[0])
    print("\n-----Basic Statistics-----")    

    print("\nAverage Age:", np.mean(ages))
    print("\nAverage Exeperience:", np.mean(exeperiences))
    print("\nAverage Salary:", np.mean(salaries))

    print("Minimum Salary:", np.min(salaries))
    print("Maximum Salary:", np.max(salaries))

    high_salary_employees = employees[employees[:, 3] > 70000]
    print("\n------High Salary Employeess-------")
    print("Employees earning more than 70000:")
    print(high_salary_employees)

    oldest_index = np.argmax(ages)
    print("\n-------Oldest Employee Details------:")
    print("Employee Id:", employees[oldest_index][0])
    print("Employee Id:", employee_ids[oldest_index])
    print("Age:", ages[oldest_index])

    experienced_index = np.argmax(exeperiences)

    print("\n--- Most Experienced Employee ---")
    print("Employee ID:", employee_ids[experienced_index])
    print("Experience:", exeperiences[experienced_index], "years")

    print("\n===================================")
    print("        ANALYSIS COMPLETED")
    print("===================================")

if __name__ == "__main__":
    main()