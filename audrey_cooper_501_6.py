# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 2, assignment 6
# Purpose: To create a guessing game with the computer. The computer 'picks a
# random number' and has the user guess what that number is.

# import random function to utilize random number selection
import random

# assign hidden to a random integer within range 1-9
hidden = random.randint(1,9)

# assign variable count to 0 to count the number of guesses it took
count = 0

# while loop to iterate while a condition is true 
while(1):
    
    # assign guess variable to user input 
    guess = input("Enter a number between 1 and 9! (Or type exit to leave this program!)")

    # add one to count in the while loop to count a guess for each iteration
    count = count + 1

    # if statement to break the loop if user types exit 
    if (guess)== 'exit':
        break
    
    # else statement that determines whether the user needs to increment
    # or decrement their guess and then prints the result
    else:
        if int(guess) == hidden:
            print("You're right!" + 'Guesses: %d' %(count))
        elif int(guess) > hidden:
            print("Your guess is too high!")
        elif int(guess) < hidden:
            print("Your guess is too low!")

'''
IDLE Output
Enter a number between 1 and 9! (Or type exit to leave this program!) 9
Your guess is too high!
Enter a number between 1 and 9! (Or type exit to leave this program!) 7
Your guess is too low!
Enter a number between 1 and 9! (Or type exit to leave this program!) 8
You're right!Guesses: 3
Enter a number between 1 and 9! (Or type exit to leave this program!) exit
'''
