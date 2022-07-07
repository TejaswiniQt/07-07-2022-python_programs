#Program to add two numbers usinf function

#!/usr/bin/python

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

def add(x,y):
    sum=x+y
    return sum

result=add(num1,num2)
print("The sum of {0} and {1} is:{2}".format(num1,num2,result))
