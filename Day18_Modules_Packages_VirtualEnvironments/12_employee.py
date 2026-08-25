import employee_utils as eu

salary = 60000

print("Company:", eu.COMPANY_NAME)
print("Bonus:", eu.calculate_bonus(salary))
print("Total salary:", eu.calculate_total_salary(salary))