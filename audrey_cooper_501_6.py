# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 1, assignment 6
# Purpose: To create a rock, paper, scissors game using if and elif statements
# as well as separate player input.

# assign player_one and player_two variables to their respective inputs
player_one = str(input("Player 1? "))
player_two = str(input("Player 2? "))

# if statement for player_one input validation
if player_one != "rock" and player_one != "paper" and player_one != "scissors":
    print("This is not a valid input!")
else:
    # if statement for player_two input validation
    if player_two != "rock" and player_two != "paper" and player_two != "scissors":
        print("This is not a valid input!")
    else:
        # if and elif statement to determine the winner
        if player_one == player_two:
            print("Tie!")
        elif player_one == "rock" and player_two == "paper":
            print("Player 2 wins!")
        elif player_one == "rock" and player_two == "scissors":
            print("Player 1 wins!")
        elif player_one == "paper" and player_two == "rock":
            print("Player 1 wins!")
        elif player_one == "paper" and player_two == "scissors":
            print("Player 2 wins!")
        elif player_one == "scissors" and player_two == "rock":
            print("Player 2 wins!")
        elif player_one == "scissors" and player_two == "paper":
            print("Player 1 wins!")
            
'''
Player 1? rock
Player 2? paper
Player 2 wins!
'''
            
        
        

    
            
            
        

