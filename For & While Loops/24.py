# 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.

def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1 
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def main():
    try:
        num = int(input("Enter an integer to count its digits: "))    
        fibo = fibonacci(num)
        print("Number of Fibonacci series is:", fibo)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
