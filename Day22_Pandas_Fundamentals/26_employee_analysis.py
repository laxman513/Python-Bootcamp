import pandas as pd


df = pd.DataFrame({
    "Name": [
        "Rahul", "Priya", "Amit",
        "Sneha", "Kiran", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT",
        "HR", "IT", "Finance"
    ],
    "Age": [25, 30, 35, 28, 40, 32],
    "Experience": [2, 5, 8, 4, 12, 7],
    "Salary": [50000, 60000, 90000, 65000, 120000, 70000]
})

print("========== EMPLOYEE DATA ==========")
print(df)

print("\n========== SALARY STATISTICS ==========")
print("Average Salary:", df["Salary"].mean())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())

print("\n========== HIGH SALARY EMPLOYEES ==========")
print(df[df["Salary"] > 70000])
# print(df.query("Salary > 70000"))

print("\n========== AVERAGE SALARY BY DEPARTMENT ==========")
department_salary = df.groupby("Department")["Salary"].mean().reset_index()
print(department_salary)

print("\n========== EMPLOYEES SORTED BY SALARY ==========")
sorted_df = df.sort_values(
    "Salary",
    ascending=True    
)
print(sorted_df)