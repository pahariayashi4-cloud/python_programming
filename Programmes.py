# ADD:

#print(sum([10,5]))
'''a=2
b=4
sum=a+b
print(sum)
'''
#user input
'''a = input('1st no:')
b=input('2nt no:')
sum=int(a)+int(b)
print(sum)'''

#function 
'''def add(a,b):
    return a+b
a=4
b=4
sum = add(a,b)
print(sum)'''

#MAXIMUM

'''a=5
b=7
print(max(a,b))'''

# ternary operator
'''a=7
b=3
print(a if a>b else b)'''

# if-else
'''a=4
b=6
if a>b:
    print(a)
else:
    print(b)'''

#FACTORIAL

'''n =6
fact = 1
for i in range (1, n+1):    #for i in range(1, 7):   # since n+1 = 6+1 = 7  
    fact *= i    #fact *= i → fact = fact × i
    print(fact)'''

'''n =6
fact = 1
for i in range (1, n+1):      #for i in range(1, 7):   # since n+1 = 6+1 = 7
    fact *= i    #fact *= i → fact = fact × i
print(fact)'''

#recrsion
'''n=4
def fact(n):
    if (n==0 or n==1) :
        return 1
    else:
        return n*fact(n-1)
print(fact(n))'''

#EVEN

'''n=1
if n%2==0:
    print('even')
else:
    print('odd')'''