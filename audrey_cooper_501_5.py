# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 2, assignment 5
# Purpose: to determine whether a number is divisible by 2 or not by using the
# modulus operator

# utilize a while loop to iterate though user input while 1 is true
while(1):
    # assign num variable to a user input 
    num = int(input("Enter a number that is divisible by 2 please! "))
    # use if statement to determine if number if divisible by 2
    # modulus operator is used to determine if the remainder is 0
    if (num%2 == 0):
        # print success result statements
        print("Good job!")
        # break from loop once requirement is met
        break
    # else condition if mod 2 does not equal 0
    else:
        # print failed result statements
        print("You fool!")

'''
IDLE Output
Enter a number that is divisible by 2 please! 5
You fool!
Enter a number that is divisible by 2 please! 6
Good job!
'''

