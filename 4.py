# wpp to define a method factorial that takes a param & returns the result after computing factorial of the number 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)