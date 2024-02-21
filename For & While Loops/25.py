# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.


def checker(a):
    sum=0
    for i in a:
        if i%2==0:
            sum +=i
    print(sum)        
  

def main():
    lst=[]
    n=int(input("N:"))
    
    for i in range(0,n):
        a=int(input("Numbers:"))
        lst.append(a)
        checker(lst)


if __name__ =="__main__":
    main()