# 4. Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

def lstToString(s):
    
    listToStr = ' '.join(map(str, s))
    
    print(type(listToStr))
    print(listToStr)



lst=[]

n=int(input("Enter the size of list:"))

for i in range (0,n):
    lst.append(input("Enter the numbers: "))
    
    print(type(lst))
    print(lst)
    
    
    print("--------------------------------")
    print("After type casting: ")
    
    lstToString(lst)