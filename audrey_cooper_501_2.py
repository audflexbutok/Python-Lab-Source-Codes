# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 2, assignment 2
# Purpose: To determine whether a year is a leap year or not

# assign year variable to user input 
year = int(input("Enter a year to find out if it's a leap year! "))

# if statement to determine whether or not a year is divisible by 400
if (year%400 == 0):
    # print leap year results
    print(year, "is a leap year!")
elif(year%4 == 0)and (year%100 != 0):
    print(year, "is a leap year!")
else:
    # print non leap year results if year does not meet leap requirements
    print(year, "is not a leap year.")
   


'''
IDLE output
Enter a year to find out if it's a leap year! 2000
2000 is a leap year!

Enter a year to find out if it's a leap year! 2012
2012 is a leap year!

Enter a year to find out if it's a leap year! 2100
2100 is not a leap year.
'''






    
    
    
