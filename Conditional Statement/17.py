# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.



#Triangle_Checker
def Triangle_Checker(a,b,c):
    if a == b and b == c:
        print("equilateral")
    elif a == b and b != c:
        print("scalene")
    else:
        print("isosceles")
        
    
    
# Main Function 
def main():
    try:
        x=float(input("Enter the first number: "))
        y=float(input("Enter the Second number: "))
        z=float(input("Enter the Third number: "))
        Triangle_Checker(x,y,z) 
    except ValueError:
        print("Please Enter a Valid Input")
        

if __name__ == "__main__":
    main()
    