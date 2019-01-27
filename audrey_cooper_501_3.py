# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 3, assignment 3
# Purpose: To use boolean functions and relational operators to test whether
# a number is prime or not.

# define isPrime function with variable x as argument
def isPrime(x):
    # instantiate variable count and assign it to 0 (For Boolean values 0 & 1)
    # assigning count to 0 automatically makes it True unless the if statement
    # proves otherwise False 
    count = 0

    # if statement to iterate/compare argument
    if x < 2:

        # set count equal to 1 to make it equal to true 
        count = 1;
    else:
        
        # use for loop to iterate through 2 to 1 less than argument number
        for i in range(2, x-1):
            
            # if the modulus of x is 0, set count equal to 0 (true)
            if x%1 == 0:
            count = 1
            
    # if statement to return True or False based on variable count assignment        
    if count == 0:
        return True
    else:
        return False

# instantiate variable num and assign it to user input
num = int(input("Enter a number to test if it is prime or not! "))

# pass user input value num through isPrime function as an argument
if isPrime(num):
    # print results
    print("That number is prime!")
else:
    print("That number is not prime!")


'''
Output from IDLE
Enter a number to test if it is prime or not!50
That number is not prime!
'''
