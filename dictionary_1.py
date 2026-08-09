# Q5.
# Create a dictionary of employees where Employee ID is the key.
# Employee details are stored as a nested dictionary.
# The dictionary contains records of 5 employees.
# Perform:
# i) Print the record of employee with ID E1.
# ii) Print the department of employee E4.

employees = {
    "E1": {"Name": "Amit", "Dept": "HR", "Salary": 30000},
    "E2": {"Name": "Rahul", "Dept": "IT", "Salary": 45000},
    "E3": {"Name": "Neha", "Dept": "Finance", "Salary": 40000},
    "E4": {"Name": "Priya", "Dept": "Marketing", "Salary": 35000},
    "E5": {"Name": "Rohan", "Dept": "Sales", "Salary": 32000}
}

# Employee E1 Record
print("Employee E1 Record:")
print(employees["E1"])

# Department of E4
print("\nDepartment of E4:")
print(employees["E4"]["Dept"])