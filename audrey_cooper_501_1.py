# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 3, assignment 1
# Purpose: To use nested loops to draw a pyrimid with asterisks

# assign num to user input to determine number of rows 
num = int(input("Enter a number. \n >> "))

count = 0

# a bunch of math shit i don't feel like explaining
for r in range(num + 1):

    for c in range(count):
        print(' ', end='')
        
    for c in range(num - count):
        print('*', end='')

    if (count == num):
        print("*",end='')
    else:
        print(' ',end='')    

    for c in range(num - count):
        print('*', end='')
    
    print()

    
    count = count + 1

num2 = int(input("Enter a number. \n >> "))


count2 = 1
for r in range(num2 + 1):
    for c in range(1,count2):
        print(c, end='')
    print()
    count2 = count2 + 1

        

'''
IDLE Output
Enter a number: 5
***** *****
 **** ****
  *** ***
   ** **
    * *
     *
Enter a number: 5

1
12
123
1234
12345
'''
