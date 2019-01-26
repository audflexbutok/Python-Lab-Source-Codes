# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 1, assignment 3
# Purpose: To take user input (name and age) and then calculate what year the
# user will be 100 years old, while addressing them by name in the print
# statement output.

# assign name/age to string input to prompt and collect user input
name = str(input("What's your name?"))
age = int(input("How old are you?"))

# assign years_to_onehundred variable to 100 - current age and add current year
# to determine what year the user will be 100 years old.
years_to_onehundred = ((100 - age) + 2018)

# print results
print(name, "you will be one hundred years old in", years_to_onehundred)

'''
Output from IDLE
What's your name? Audrey
How old are you? 19
Audrey you will be one hundred years old in 2099
'''
