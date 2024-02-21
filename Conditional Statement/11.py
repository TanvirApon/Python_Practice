# 11. Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

def check(z):
    
    if z==0:
        print("Zero")
    elif z>0:
        print("Positive")    
    else:
        print("Negative")

def main():
    try:
        x=int(input("Enter a number: "))
        check(x)
               
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
