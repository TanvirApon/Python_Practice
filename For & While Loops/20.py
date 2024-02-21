# 20. sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.


def main():
    n=int(input("Enter ta number: "))
    sum=0
    
    for i in range(1,n+1):
        sum = sum+i
    
    print(sum)


if __name__ == "__main__":
    main()        