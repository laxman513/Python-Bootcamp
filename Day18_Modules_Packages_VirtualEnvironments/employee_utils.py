COMPANY_NAME = "JP Morgan Chase & Co."

def caluculate_bonus(salary):

    return salary * 0.10

def caluculate_total_salary(salary):
    bonus = caluculate_bonus(salary)
    return salary + bonus
