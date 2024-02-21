# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

from math import sqrt

def Prime(n):
    if n<=1:
        return False
    
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True
        
 


def main():
    try:
        num = int(input("Enter an integer to count its digits: "))    
        prime = Prime(num)
        
        if prime== True:
            print("Prime Number")
        
        else:
            print("Not a Prime Number")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()