# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

def count_digits(n):

    count = 0
    if n == 0:
        return 1
    
    while n != 0:
    
        count += 1
        n //= 10
    
    return count

def main():
    try:
   
        num = int(input("Enter an integer to count its digits: "))
        
        digit_count = count_digits(num)
        print("Number of digits in", num, "is:", digit_count)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()


