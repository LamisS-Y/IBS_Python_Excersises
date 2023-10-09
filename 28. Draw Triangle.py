#Excersise 28 Draw Triangle
# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was
a = int(input("Please enter number of rows: "))
for i in range (1,a+1):
    print("*" * i)