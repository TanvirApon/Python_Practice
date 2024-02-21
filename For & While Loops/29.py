# 29. Reverse String: Write a Python program using a while loop to reverse a given string.

def reverse(a):
    return a[::-1]

def main():
    try:
        x = str(input("Enter string: "))    
        ans = reverse(x)
        print(ans)     
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()