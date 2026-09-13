import math

marks=[]
bio=[70,50,80,10,20]
chem=[75,55,85,15,25]
phy=[72,52,82,12,22]
marks.append(bio)
marks.append(chem)
marks.append(phy)

max_marks=max(marks)
min_marks=min(marks)
avg_marks=sum(marks)/15
stu=marks.index(max_marks)
for i in range(len(marks)):
    print(max(marks[i]))
    print(sum(marks)//5)

print("max_marks = ",max_marks)
print("min_marks = ",min_marks)
print("avg_marks = ",avg_marks)
print("stu_highest_marks = ",stu)

for num in marks[i]:
    if num<50:
        num+=10
stu_80=0
for num in marks[1]:
    if num>=80:
        stu_80+=1
print(stu_80)
min_mark_stu2=9999999
for i in range(len(marks)):


    