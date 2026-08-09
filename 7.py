#Write a python program to define a method check_armstrong with a parameter num that will return True if the number is Armstrong else False.

def checkArmstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == original

n = int(input("enter:"))

if checkArmstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")