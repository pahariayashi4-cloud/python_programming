# Q1.
# WAP to create a list of 10 students' marks.
# Create another list where the marks of students scoring
# more than 8 marks are stored.
# Do not take any duplicate values in the list.

# List of 10 unique student marks
marks = [5, 9, 7, 10, 8, 6, 4, 3, 2, 1]
name = ['sumit','me','jett','reyna','veto','cypher','vyse','mik','dua lipa','phnx']
# Students scoring more than 8
above_8 = []

for i in range(len(marks)):
    if marks[i] >=8:
        above_8.append(name[i])

print("Original Marks:", marks)
print("Marks greater than 8:", above_8)