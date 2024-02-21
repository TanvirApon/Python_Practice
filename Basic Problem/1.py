# 1. Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.

x = int(input("Enter The First Number: "))

y = int(input("Enter The Second Number: "))

x,y = y,x

print("After Swapping X: ", x)
print("After Swapping Y: ", y)