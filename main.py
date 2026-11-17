import pandas as pd

# Read CSV
df = pd.read_csv("emp.csv")

# Check data
#print(df.head())

# Calculate annual salary
df["Annual_Salary"] = df["Salary"] * 12

#print(df.Annual_Salary)

high_salary = df.loc[df["Salary"] > 50000]

# Department-wise analysis
summary = df.groupby("Department").agg(
    Total_Salary=("Salary", "sum"),
    Average_Salary=("Salary", "mean"),
    Employee_Count=("EmpID", "count")
)

high_salary.to_csv("high_salary.csv",index = False)

summary.to_json("department_summary.json",indent=4)

print(summary)