# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 3, assignment 4
# Purpose: To make a small menu driven calculator that utilizes a variety
# of functions imported from the math library.

# import math library to utilize math functions
import math


# print statements for menu driven program
print("1) Convert degrees to radians.")
print("2) Calculate the length of the vector from the origin to a point.")
print("3) Calculate the tangent in radians.")
print("4) Return the ceiling of a number.")
print("5) Return the floor of a number.")
print("6) Exit")


# instantiate variable calc and assign it to true so while loop runs
# continuously until the loop is broken
calc = True
while calc == True:

    # instantiate variable choice and assign it to user input
    choice = int(input("Select an operation!"))

    # if statement to operate menu driven program based on user input
    if choice == 1:
        
        # instanatiate variable degr and assign it to user input
        degr = int(input("Enter a degree to convert to radians! "))
        
        # print statement utilizing math degree function
        print (math.degrees(degr))
    elif choice == 2:
        # instantiate variables xpoint & ypoint and assign it to user input
        xpoint = int(input("Enter the X point."))
        ypoint = int(input("Enter the Y point."))

        # print statement utilizing math hypotenuse function
        print(math.hypot(xpoint,ypoint))
        
    elif choice == 3:
        # instantiate variable tantorad and assign it to user input
        tantorad = int(input("Enter a number to find its tangent in radians! "))

        # print statement utilizing math tangent function
        print(math.tan(tantorad))

    elif choice == 4:

        # instantiate variable ceilnum and assign it to user input
        ceilnum = int(input("Enter a number to find its ceiling! "))

        # print statement utilizing math ceiling function
        print(math.ceil(cielnum))
        
    elif choice == 5:

        # instantiate variable floornum and assign it to user input
        floornum = int(input("Enter a number to find its floor! "))

        # print statemnet utilizing math floor function
        print(math.floor(floornum))
        
    elif choice == 6:
        # break statement to exit the while loop
        break

'''
IDLE Output
1) Convert degrees to radians.
2) Calculate the length of the vector from the origin to a point.
3) Calculate the tangent in radians.
4) Return the ceiling of a number.
5) Return the floor of a number.
6) Exit
Select an operation!2
Enter the X point.5
Enter the Y point.6
7.810249675906654
Select an operation!6
'''
          

      



