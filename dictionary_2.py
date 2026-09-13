student = {
    "R1": {"name": "Ayashi", "dept": "CSE", "marks": 85},
    "R2": {"name": "Kaustav", "dept": "ECE", "marks": 72},
    "R3": {"name": "Subhra", "dept": "CSE", "marks": 91},
    "R4": {"name": "Saswata", "dept": "IT", "marks": 78},
    "R5": {"name": "Pinaki", "dept": "CSE", "marks": 88}
}

# Sort highest marks to lowest marks
sorted_student = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("Students sorted according to marks:")
for roll, details in sorted_student.items():
    print(roll, details)


# print stu with max marks
max_student = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent with maximum marks:")
print(max_student)


# avg marks of stusent
total = sum(details["marks"] for details in student.values())
average = total / len(student)

print("\nAverage marks:", average)

 
# stu score > avg marks
print("Students scoring more than average:")
for roll, details in student.items():
    if details["marks"] > average:
        print(roll, details)