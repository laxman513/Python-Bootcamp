import employee_utils

salary = 50000

bonus = employee_utils.caluculate_bonus(salary)

total_salary = employee_utils.caluculate_total_salary(salary)

print("Company:", employee_utils.COMPANY_NAME)
print("Salary:", salary)
print("Bonus:", bonus)
print("Total salary:", total_salary)