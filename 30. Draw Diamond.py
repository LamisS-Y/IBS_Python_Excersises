#Excersice 30 Draw Diamond
# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = int(input("Please enter number of rows: "))
for i in range (1, a+1, 2):
    space= (a -i) // 2
    print(" "*space + "*"* i) 
for y in range (a-1, 0, -2):
    space= (a -y) // 2
    print(" "*space + "*"* y) 