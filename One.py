import json

employee = {
    "name": "Aditya",
    "department": "BI",
    "salary": 45000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)


with open("employee.json", "r") as file:
    data = json.load(file)

print(data)