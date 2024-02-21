# 26. Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.


def pattern_1(n):
    for i in range(0,n):
        print("*"*i)
       
   
def pattern_2(n):
    for i in range(n,0,-1):
        print("*"*i)
   
   

def main():
    try:
        n = int(input("Enter an integer to count its digits: "))
        pattern_1(n) 
        pattern_2(n)    
     
       
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

    