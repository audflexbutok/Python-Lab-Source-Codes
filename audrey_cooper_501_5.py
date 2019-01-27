# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 3, assignment 5
# Purpose: To get the computer to "guess" the number that the user is thinking of.

# initial print statement to start game
print("My guess is 50.")

# instantiate variable guess and assign it to 50
guess = 50

# instantiate variable game and assign it to True to keep the while loop running
game = True

# utilize while loop to continuously iterate until the computer guesses correctly
while game == True:
    
    # instantiate variable correct and assign it to user input
    correct = str(input("Is that guess too high or too low? (Type high or low, or correct.) \n >> "))
    if (correct) == "correct":
        break
    else:
        
        # if statement to compare user input to computer guess
        if correct == ("high"):
            
            # reassign and decrement guess value
            (guess) = (guess - 1)

            # print new guess
            print(guess)
            
        elif correct == ("low"):
            # reassign and increment guess value
            (guess) = (guess + 1)

            # print new guess
            print(guess)

'''
IDLE Output
My guess is 50.
Is that guess too high or too low? (Type high or low, or correct.)
>> high
49
Is that guess too high or too low? (Type high or low, or correct.)
>> high
48
Is that guess too high or too low? (Type high or low, or correct.)
>> high
47
Is that guess too high or too low? (Type high or low, or correct.)
>> low
48
Is that guess too high or too low? (Type high or low, or correct.)
>> low
49
Is that guess too high or too low? (Type high or low, or correct.)
>> correct
'''



              
                  
        
                  
                  
        
    
    
