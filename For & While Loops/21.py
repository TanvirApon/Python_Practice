def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    
    return result

def main():
    try:
        n = int(input("Enter a number to calculate its factorial: "))
        
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return
        fact = factorial(n)
        print("The factorial of", n, "is:", fact)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
