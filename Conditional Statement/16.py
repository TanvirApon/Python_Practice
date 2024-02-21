# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

import datetime


def time_checker(h):
    
    if h>= 6 and h <= 12:
        print("Good Morning")
    elif h>12 and h<=18:
        print("Good Afternoon")
    elif h>18 and h<=20:
        print("Good Evening") 
    
    else:
        print("Good Night")           

def main():
    try:
        current_time = datetime.datetime.now()
        
        hour= current_time.hour
        
        time_checker(hour)
    
    except ValueError:
        print("Error in handeiling input")
        

if __name__ == "__main__":
    main()