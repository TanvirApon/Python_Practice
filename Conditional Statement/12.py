# 12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        largest = largest_of_three(num1, num2, num3)
        print("The largest number is:", largest)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
