employee = {
   "emp_id" : 101,
   "name": "Aditya",
   "Salary" : 37500
}

employee["Salary"] = 65000

print(employee)
print(employee["name"])


for key, value in employee.items():
    print(key,":", value)

# Sets

department = ["BI", "DEV", "DBA", "BI"]
unique_values = set(department)
print(unique_values)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Functions, Arguments, Return Values and List Comprehensions

def greet():
    print("Welcome to Python Learning")

greet()

#  Function with Argument 

def emp_details(name, department):
    print("Employee :", name)
    print("Employee :", department)

emp_details("Aditya", "BI") 

# Return values

def calculate_salary(basic, bonus):
    total = basic + bonus
    return total

result = calculate_salary(40000, 5000)

print(result)

# List Comprehension

numbers = [1,2,3,4,5,6]

squa = [num * num for num in numbers]

print(squa)

# Practise for set

def salary(mon_sal, bonus = 0):
    print((mon_sal*12)+bonus)

salary(55000,10000)


#File Hnadling in PY

with open("Employee.csv", "r") as file:
    data = file.read()

print(data)    

#JSON
