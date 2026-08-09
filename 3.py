#Write a py program to take a year and find out whether it is a leap year or not?

a = int(input("Enter a year: "))

if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")