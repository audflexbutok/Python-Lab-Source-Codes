# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 1, assignment 5
# Purpose: to take user input of three numbers and add them all together if
# none of the three numbers are the same number.

# assign 3 variables to user input and prompt and collect user input.
number_one = int(input("Enter a number! "))
number_two = int(input("Enter another number! "))
number_three = int(input("Enter one more number! "))

# if statement to ensure that neither of the numbers input are the same number
if number_one == number_two or number_one == number_three or number_two == number_three:
     # print result if any of the numbers are the same number
     print(0)
else:
     # print result if all the numbers are different 
     print(number_one + number_two + number_three)

'''
Output from IDLE
Enter a number! 3
Enter another number! 4485
Enter one more number! 82
4570
'''
