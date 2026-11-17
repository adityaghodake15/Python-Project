monthly_salary = float(input("Enter monthly salary: "))
bonus = float(input("Enter bonus (press Enter for 0): ") or 0)


# 2. Function to calculate annual salary
def calculate_annual_salary(monthly_salary, bonus=0):
    return (monthly_salary * 12) + bonus


# 3. Return annual salary
annual_salary = calculate_annual_salary(monthly_salary, bonus)

print("Annual Salary: ₹", annual_salary)


#File Hnadling in PY

with open("Employee.csv", "w") as file:
    file.write("Aditya - BI Developer")