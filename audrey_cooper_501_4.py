# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 1, assignment 4
# Purpose: To take user input of a letter and determine if that input is a
# vowel or a consonant.

# assign a to input to prompt and collect user input
a = input("Enter a letter! ")

# use an if statement to iterate through the vowel choices to determine
# if a (user input) meets the vowel requirements
if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
    # print vowel result
    print("This letter is a vowel!")
else:
    # print consonant result
    print("This letter is a consonant!")
    
'''
Output from IDLE
Enter a letter!a
This letter is a vowel!
'''
