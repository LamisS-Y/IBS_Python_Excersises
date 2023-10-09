#Excersice 29 Draw Pyramid
# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
a = int(input("Please enter number of rows: "))
for i in range (1, a+1):
    space= (a -i)
    print(" "*space + "*"*(2*i-1)) 