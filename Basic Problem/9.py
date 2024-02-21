# 9. String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.

def concat(a,b):    
    s = "{} {}".format(a,b)
    print(s)


x =str(input("Enter the string-1: "))

y =str(input("Enter the string-2: "))

concat(x,y)

