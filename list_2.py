# Q2.
# Create a list of student marks and perform the following operations:
# i) Find the average marks from the list.
# ii) Find the number of students scoring more than average.
# iii) Find the maximum marks scored in the list.

marks = [65, 78, 89, 90, 45, 56, 67, 88, 76, 95,84, 72, 68, 91, 53, 60, 81, 74, 86, 79]

average = sum(marks) / len(marks)
count = 0
for mark in marks:
    if mark > average:
        count += 1
maximum = max(marks)

print("Marks:", marks)
print("Average Marks:", average)
print("Students scoring above average:", count)
print("Highest Marks:", maximum)