# Q3.
# Create a tuple of 20 employee names and perform:
# i) Print each name and its frequency.
# ii) Remove duplicate names and find number of distinct names.
# iii) Print the employee having maximum frequency.
# iv) Sort the tuple alphabetically.
# v) Input an employee name and check whether it exists.

employees = (
    "Amit", "Rahul", "Priya", "Amit", "Neha",
    "Rahul", "Riya", "Aman", "Karan", "Rohan",
    "Priya", "Amit", "Simran", "Riya", "Neha",
    "Aman", "Kunal", "Rahul", "Sneha", "Amit"
)

frequency = {}

for name in employees:
    frequency[name] = frequency.get(name, 0) + 1

print("Employee Frequency:")
for name, count in frequency.items():
    print(name, ":", count)

distinct = set(employees)
print("\nDistinct Employee Names:", distinct)
print("Number of Distinct Names:", len(distinct))

max_name = max(frequency, key=frequency.get)
print("\nEmployee with Maximum Frequency:", max_name)

print("\nAlphabetically Sorted:")
print(tuple(sorted(employees)))

search = input("\nEnter employee name to search: ")

if search in employees:
    print(search, "exists in the tuple.")
else:
    print(search, "does not exist.")