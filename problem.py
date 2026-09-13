from math import factorial
i=1
num=9
ans=0
for _ in range (num):
    ans+=(i**2)/factorial(i)
    i+=1
print(ans)
