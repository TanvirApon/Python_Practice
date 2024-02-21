'''
14. Grades Classification: Write a Python program that takes a student’s 
percentage as input and prints their corresponding grade according to the following criteria:
– 90% or above: A+ 

– 80-89%: A 

– 70-79%: B 

– 60-69%: C 

– Below 60%: Fail

'''

def check_grade(grade):
    
    if grade>=90:
        print("A+")
    elif grade>=80 and grade<90:
        print("A")
    elif grade>=70 and grade<80:
        print("B")
    elif grade>=60 and grade<70:
        print("C")
    else:
        print("Fail")
          
    
def main():
    try:
        x =int(input("Enter the percentage of student: "))
        check_grade(x)
    except ValueError:
        print("Please input the correct input type")    
        


if __name__ == '__main__':
    main()