import pandas as pd

data = {
     "Employee" : ["Aditya","Rekha","Sneha","Amit"],
     "Department": ["BI", "IT", "HR", "BI"],
     "Salary": [45000, 55000, 40000, 60000]

}

df = pd.DataFrame(data)
# print(df)

# where in sql
#result = df.loc[df["Salary"] > 45000]
result = df.loc[(df["Salary"] > 45000) & 
                (df["Department"] == "BI")]
#print(result)

resul = df.groupby("Department").agg(
        Total_Salary = ("Salary", "sum"),     
        Avg_Salary = ("Salary", "mean")
        )
#print(resul)


#Merge Op

employees = pd.DataFrame({
    "EmpID": [101, 102, 103],
    "Name": ["Aditya", "Rahul", "Priya"]
})

departments = pd.DataFrame({
    "EmpID": [101, 102, 104],
    "Department": ["BI", "IT", "HR"]
})


merge_result = pd.merge(
employees,
departments,
on = "EmpID",
how = "inner"
)
print(merge_result)