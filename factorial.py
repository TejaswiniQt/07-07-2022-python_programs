#!/usr/bin/python

def factorial(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num -1
    return fact

num = int(input("Enter the num:"))

result=factorial(num)
print("factorial of {0} is {1}".format(num,result))
