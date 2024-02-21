# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.


def vowel_checker(z):
    
    word = z.lower()
    lst=['a','e','i','o','u']
    
    if word in lst:
        return True
    else:
        return False
    
    
def main():
    try:
        x=str(input("Please enter the character you want to check: "))
        if x.isdigit():
            print("Error input is number")
            exit()
        if len(x) >1:
            print("Error input is greater then 1")
            exit()
        
        ans= vowel_checker(x)
        if ans == True:
            print(x,"is a vowel")
        else:
            print(x,"is a consonent")
            
    except ValueError:
        print("Please enter the correct data type")



if __name__ == "__main__":
    main()