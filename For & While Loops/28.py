# 28. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

def sum_(a):
    sum=0
    for i in a:
        sum+=i
        avg =float(sum/len(a))
        
    print("Sum: ",sum)
    
    print("Average: ",avg) 
    
def min_(a):
    print("Minimum: ",min(a))
    
    
def max_(a):
    print("Maximum: ",max(a))       
  

def main():
    lst=[]
    n=int(input("N:"))
    
    for i in range(0,n):
        a=int(input("Numbers:"))
        lst.append(a)
        
    sum_(lst)
    min_(lst)
    max_(lst)


if __name__ =="__main__":
    main()