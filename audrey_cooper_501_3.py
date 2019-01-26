# Programmer: Audrey Cooper
# Leb Section: 502
# Lab 2, assignment 3
# Purpose: To assign a letter grade from an input numerical grade

# assign grade variable to user input
grade = int(input("Enter your grade! "))

# utilize if statement to determine the classification of letter grade
if grade > 60:
    if grade >= 90:
        print("You made an A!")
    elif grade >= 80 and grade != 90:
        print("You made a B!")
    elif grade >= 70 and grade != 80:
        print("You made a C!")
    elif grade >= 60 and grade !=70:
        print("You made a D!")
else:
    # if grade is lower than 59, print failed statement.
    print("You failed.")

'''
IDLE Output
Enter your grade! 4
You failed.
'''
