# 7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def palidrome(a):
    
    z = a[::-1]
    
    if z == a:
        print(a,"is Palidrome")
        
    else:
        print(a,"is not a Palindrome")

x = str(input("Enter the string: "))

palidrome(x)