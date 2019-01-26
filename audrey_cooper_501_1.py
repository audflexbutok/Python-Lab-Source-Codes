# Programmer: Audrey Cooper
# Lab Section: 502
# Lab 2, assignment 1
# Purpose: To determine the number of desks needed for an input number of
# students in 3 classes. Two students can sit at one desk.

# import math library to use ceiling function
# ceiling function takes the lowest value of the floating point integer
# in order to truncate the final answer
import math

# assign class1, 2, and 3 to input to take user input of number of students
# in each respective class
class1 = int(input("How many students are in the first class? "))

# assign desk1 variable to the ceiling of the number of half the students 
desk1 = math.ceil((class1)/2)

# print number of desks needed for class 1
print(desk1)

class2 = int(input("How many students are in the second class? "))

# assign desk2 variable to the ceiling of the number of half the students
desk2 = math.ceil((class2)/2)

# print number of desks needed for class 2
print(desk2)

class3 = int(input("How many students are in the third class? "))

# assign desk3 variable to the ceiling of the number of half the students 
desk3 = math.ceil((class3)/2)

# print number of desks needed for class 3 
print(desk3)

# assign desk_total to the sum of all the class desks
desk_total = (desk1 + desk2 + desk3)

# print the total number of desks needed for all three classes
print(desk_total)


'''
IDLE Output
How many students are in the first class? 20
10
How many students are in the second class? 21
11
How many students are in the third class? 22
11
32
'''
