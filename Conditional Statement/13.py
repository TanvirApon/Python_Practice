# 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

def leap_year(x):
    
    if x%400==0 or x%100 !=0 and x%4==0:
        return True
    else:
        return False      

def main():    
    try:
        x=int(input("Enter the year you want to check: "))
        ans= leap_year(x)
        
        if ans==True:
            print(x,"is a Leap Year")
        else:
            print(x,"is not a Leap Year")
        
    except ValueError:
        print("Please input the correct input type")
        

if __name__ == "__main__":
    main()