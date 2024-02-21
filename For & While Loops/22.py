# 22. Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

def Mul(n):
    for i in range(0,11):
        print(n,"X",i,"=",n*i)

def main():
    try:
        n = int(input("Enter a number to multiplication table : "))
        Mul(n)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
