# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 3, assignment 2
# Purpose: To create a menu driven calculator

# set calc equal to true so it runs continuously 
calc = True
while calc == True:
    # adds two numbers 
    def add(x, y):
       return x + y

    # subtracts two numbers 
    def subtract(x, y):
       return x - y

    # multiplies two numbers
    def multiply(x, y):
       return x * y

    # divides two numbers
    def divide(x, y):
       return x / y

    # menu driven portion that allows user to select operation
    print("Select operation.")
    print("1. Add ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Exit ")

    # user input for operation choice
    choice = input("Enter choice(1/2/3/4/5):")

    # user input for number choice to perform operation
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # statements to perform the correct operations and print their results
    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
       print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
       print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
       print(num1,"/",num2,"=", divide(num1,num2))
       
    elif choice == '5':
                break
    else:
        # input validation
        print("Invalid input")

'''
IDLE Output
Select operation.
1. Add 
2. Subtract 
3. Multiply 
4. Divide 
5. Exit 
Enter choice(1/2/3/4/5):4
Enter first number: 2
Enter second number: 2
2 / 2 = 1.0
Select operation.
1. Add 
2. Subtract 
3. Multiply 
4. Divide 
5. Exit 
Enter choice(1/2/3/4/5):
'''
    


    
